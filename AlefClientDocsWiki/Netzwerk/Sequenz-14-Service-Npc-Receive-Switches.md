# Winsock Sequenz 14: Receive-Switches der Service-NPCs

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Diese Datei vertieft [`WINSOCK_SEQUENCE_13_SERVICE_NPCS.md`](Sequenz-13-Service-Npcs.md) und konzentriert sich auf die Parser/Receive-Seite der Service- und Crafting-Module. Quellen sind `alefclient.pseudocode.c`. Es wurde kein Live-Traffic mitgeschnitten; Bedeutungen sind Inferenz aus Parserfeldern, Eventcallbacks und UI-Folgen.

## Kurzfazit

- Die Service-Module dekodieren Serverantworten mit `FUN_004e9fb0(...)`.
- Viele Parser setzen vor dem Dekodieren den Subopcode auf `0xff`. Danach entscheidet das Lowbyte von `param_3`, welcher Handler ausgefuehrt wird.
- Die Parser pruefen fast immer, ob die Antwort zum lokalen Charakter gehoert. Bei falscher oder blockierender Character-ID wird die Nachricht verworfen.
- Eventmodule liefern meist "Oeffnen/Schliessen/Status"; Kernmodule liefern die eigentlichen Resultate von Craft, Convert, Refine, Repair, Skillkauf usw.

## Gemeinsamer Parseraufbau

Typisches Muster:

```text
if packetLen invalid: return 0
subop = 0xff
FUN_004e9fb0(layout, 1, packet, packetLen, &subop, &charIdOrEventId, ...)
character = FUN_005035f0(charId)
if local-only && character is busy: reject
switch ((char)subop) { ... }
```

Wichtig: Wenn `param_6[0] == 0`, wird meist geprueft, ob die Nachricht zum lokalen Charakter passt und ob dieser nicht gerade in einem Zustand ist, der das Update blockiert.

## Refinery Receive

### Eventmodul `AgpmEventRefinery` `0x3f`

Receive-/Parserfunktion: `FUN_0056ff20`.

Dekodiert:

```text
FUN_004e9fb0(AgpmEventRefinery + 0xb90, 1, packet, len,
             &subop, &eventObjectId, &characterId)
```

Validierung:

- `eventObjectId` muss auf ein Eventobjekt zeigen.
- Das Eventobjekt muss Typ/Funktions-ID `0x1a` besitzen.
- `characterId` muss auf einen bekannten Charakter zeigen.

Subops:

| Subop | Clientaktion |
|---:|---|
| `0` | `FUN_0056fc60(event, character)`; NPC/Event-Interaktion oeffnen oder Bewegungsziel setzen |
| `1` | `FUN_00574960(event, character)`; generischer Event-Abschluss/Statuspfad |

### Kernmodul `AgpmRefinery` `0x4b`

Receive-/Parserfunktion bei `AgpmRefinery + 0xc4c` um `FUN_005293..`.

Dekodiert:

```text
FUN_004e9fb0(AgpmRefinery + 0xc4c, 1, packet, len,
             &subop, &characterId, &local_2c, &local_28, &local_34, &local_30)
```

Subops:

| Subop | Clientaktion |
|---:|---|
| `1` | `FUN_004e4070(1, local_30, local_34)`; Result/Eventcallback, wahrscheinlich Refine-Ergebnis |
| `2` | `FUN_00529350(character, &local_28)`; Character-/Itemdaten aktualisieren |

Inferenz:

- `local_28` ist sehr wahrscheinlich ein strukturierter Refine-Resultblock.
- `local_34/local_30` sind wahrscheinlich Item-/Resultobjekte fuer UI- oder Itemupdate-Callbacks.
- Server sendet mindestens ein Ergebnis-Update und einen Status-/Inventory-Sync.

## Product Receive

### Eventmodul `AgpmEventProduct` `0x3a`

Sendeseitig sichtbare Subops:

- `0`: Event oeffnen.
- `2`: Product-/Listenaktion.
- `4`: zweite Product-/Listenaktion.

Der dazugehoerige Event-Receive ist im gleichen Muster wie Bank/Refinery aufgebaut, die Kernresultate laufen aber ueber [`AgpmProduct`](../Module/AgpmProduct.md).

### Kernmodul `AgpmProduct` `0x17`

Receive-/Parserfunktion: `FUN_00560210`.

Dekodiert:

```text
FUN_004e9fb0(AgpmProduct + 0xd5c, 1, packet, len,
             &subop, &characterId, &param_4, &local_2c,
             &local_28, &local_1c, &local_20, local_14, &local_18)
```

Validierung:

- `characterId` muss auf einen bekannten Charakter zeigen.
- Bei lokalem Empfang wird blockierender Charakterzustand abgewiesen.
- Subops groesser `3` werden ignoriert, aber als erfolgreich konsumiert.

Subops:

| Subop | Clientaktion |
|---:|---|
| `0` | Jump-Table-Handler `PTR_LAB_005603c4[0]` |
| `1` | Jump-Table-Handler `PTR_LAB_005603c4[1]` |
| `2` | Jump-Table-Handler `PTR_LAB_005603c4[2]` |
| `3` | Jump-Table-Handler `PTR_LAB_005603c4[3]` |

Kontext aus Folgefunktionen:

- `FUN_00560410` prueft Product-Voraussetzungen: Rezept verfuegbar, Materialien vorhanden, Bedingungen erfuellt.
- Fehlercodes im Product-Kontext: `6`, `8`, `9` tauchen bei fehlendem Material, ungueltigem Ziel oder nicht verfuegbarem Rezept auf.
- UI [`AgcmUIProductSkill`](../Module/AgcmUIProductSkill.md) fuehrt Listen fuer kauf-/lern-/produzierbare Eintraege und Materiallisten.

Inferenz:

- Serverantworten fuer `0x17` synchronisieren Ergebnis, Rezeptstatus, Materialverbrauch und/oder Product-Skill-Fortschritt.
- Die Resultcodes sollten serverseitig gegen Recipe/Skill/Material/Inventarplatz aufgeloest werden.

## SkillMaster Receive

### Eventmodul `AgpmEventSkillMaster` `0x3b`

Receive-/Parserfunktion: `FUN_00572640`.

Dekodiert:

```text
FUN_004e9fb0(AgpmEventSkillMaster + 0x8904, 1, packet, len,
             &subop, &eventObjectId, &characterId,
             &local_10, &local_14, local_18, &param_4, local_4)
```

Validierung:

- Wenn `eventObjectId != 0`, wird ein Eventobjekt via `FUN_0055dff0(eventObjectId)` gesucht.
- `characterId` muss zum bekannten Character aufloesen.
- Lokale blockierende Characterzustaende werden verworfen.
- Subops groesser `9` werden konsumiert, ohne sichtbaren Handler.

Subops:

| Subop | Clientaktion |
|---:|---|
| `0` | Jump-Table-Handler `PTR_LAB_005728fc[0]` |
| `1` | Jump-Table-Handler `PTR_LAB_005728fc[1]` |
| `2` | Jump-Table-Handler `PTR_LAB_005728fc[2]` |
| `3` | Jump-Table-Handler `PTR_LAB_005728fc[3]` |
| `4` | Jump-Table-Handler `PTR_LAB_005728fc[4]` |
| `5` | Jump-Table-Handler `PTR_LAB_005728fc[5]` |
| `6` | Jump-Table-Handler `PTR_LAB_005728fc[6]` |
| `7` | Jump-Table-Handler `PTR_LAB_005728fc[7]` |
| `8` | Jump-Table-Handler `PTR_LAB_005728fc[8]` |
| `9` | Jump-Table-Handler `PTR_LAB_005728fc[9]` |

Sendeseitig sichtbare Subops:

- `1`: `FUN_00570e40`.
- `2`: `FUN_00570ee0`.
- `4`: `FUN_00570fa0`.
- `8`: `FUN_00571030`.

Inferenz:

- `0/1/2/4/8` sind sehr wahrscheinlich Oeffnen, Lernen, Upgrade, BuyMastery und Evolution/Reset-nahe Aktionen.
- Die restlichen Server-Subops `3/5/6/7/9` wirken wie Ergebnis-/Listen-/Fehlerupdates.
- Die UI-Strings `Skill_ErrorAlreadyLearnSkill`, `Skill_ConfirmLearnSkill`, `SkillSetBuyMastery*`, `SkillSetUpgradeMastery*` sprechen fuer Resultcodes pro Skill-Lernen und Mastery-Kauf.

## ItemConvert Receive

### Eventmodul `AgpmEventItemConvert` `0x38`

Receive-/Parserfunktion: `FUN_00575440`.

Dekodiert:

```text
FUN_004e9fb0(AgpmEventItemConvert + 0xb94, 1, packet, len,
             &subop, &eventObjectId, &characterId)
```

Validierung:

- `eventObjectId` muss auf Eventtyp/Funktions-ID `0x16` zeigen.
- `characterId` muss bekannt sein.

Subops:

| Subop | Clientaktion |
|---:|---|
| `0` | `FUN_00575180(event, character)`; Convert-NPC/Event oeffnen |
| `1` | `FUN_004e4070(1, event, character)`; Eventstatus/Result |
| `2` | `FUN_004e4070(2, event, character)`; Eventstatus/Result |

### Kernmodul `AgpmItemConvert` `0x16`

Receive-/Parserfunktion bei `AgpmItemConvert + 0x2688`, direkt nach Konstruktor/Parserbereich.

Dekodiert:

```text
FUN_004e9fb0(AgpmItemConvert + 0x2688, 1, packet, len,
             &subop, &characterId, local_8, &param_4,
             local_20, local_14, local_18, local_1c,
             &local_10, local_8 + 1)
```

Validierung:

- `characterId` muss, wenn lokal, zum aktiven Charakter passen.
- `local_8[0]` wird als Item-ID interpretiert und ueber `FUN_00558380(...)` aufgeloest.
- Subops kleiner `0x0d` springen in eine Handler-Tabelle.
- Subops ab `0x0d` werden bei bekanntem Character konsumiert und schliessen den Eventzustand.

Subops:

| Subop | Bedeutung aus Sendeseite/UI |
|---:|---|
| `0` | Server-only/Status, kein direkter Sendebuilder gefunden |
| `1` | Physical-/Convertaktion mit Item und Extra-ID |
| `2` | Convertaktion nur mit Item |
| `3` | Socket-/Rune-nahe Aktion mit Extra-ID |
| `4` | Builder vorhanden, Wrapper nicht direkt gefunden |
| `5` | Server-only/Result |
| `6` | Server-only/Result |
| `7` | Server-only/Result |
| `8` | Server-only/Result |
| `9` | Server-only/Result |
| `10` | Server-only/Result |
| `0x0b` | Convertaktion mit Extra-ID |
| `0x0c` | Convertaktion mit Extra-ID |

UI-Resultstrings zeigen, welche Fehler/Ergebnisse Server-Subops tragen koennen:

- `AlreadyFull`
- `ImproperItem`
- `NotEnoughMoney`
- `NotEnoughSocket`
- `InvalidCatalyst`
- `InvalidRune`
- `LowCharLevel`
- `LowItemLevel`
- `TryEquipItem`
- `AlreadyAntiConvert`
- `Success`
- `Fail`
- `KeepCurrent`
- `Initialize`
- `Destroy`

Inferenz:

- `0x16` ist eines der wertvollsten Serverprotokolle fuer Itemdaten, weil hier Itemmodifikation, Zufallsergebnis, Geldverbrauch, Materialverbrauch und Socket-/Rune-Zustand zusammenfallen.
- Die Server-Datenbank braucht atomare Item- und Geldtransaktionen. Ein teilweise gebuchter Convert waere sofort duplizier-/verlustanfaellig.

## Bank Receive

Receive-/Parserfunktion: `FUN_00575930`.

Dekodiert:

```text
FUN_004e9fb0(AgpmEventBank + 0xb8c, 1, packet, len,
             &subop, &eventObjectId, &characterId)
```

Validierung:

- Wenn `eventObjectId != 0`, wird Eventobjekt aufgeloest.
- Falls Eventobjekt vorhanden ist, muss es Typ/Funktions-ID `0x14` haben.
- `characterId` muss bekannt sein.

Subops:

| Subop | Clientaktion |
|---:|---|
| `0` | `FUN_005756c0(event, character)`; Bankzugriff oeffnen/starten |
| `1` | `FUN_00574960(event, character)`; generischer Eventstatus |
| `2` | `FUN_004e4070(2, 0, character)`; Bankstatus/Close/Update |

Wichtig: Die eigentlichen Bank-Item- und Geldbewegungen sind in den Item-/Bank-Callbacks versteckt (`FUN_006ebcb0`, `FUN_006ebec0`, `FUN_005a10f0`, `FUN_005a0fd0`) und muessen separat opcodeweise gemappt werden.

## ItemRepair Receive

Event-/Oeffnungsparser: `FUN_00575f30` sendet Subop `3` zum Oeffnen. Die serverseitige Antwort verwendet denselben `AgpmEventItemRepair + 0xb94`-Parserbereich.

Konkreter Reparaturrequest: `FUN_00575c00`.

Sendefelder:

```text
FUN_004ea280(AgpmEventItemRepair + 0xb94, 1, outLen, 0x34,
             &subop, eventObject, &characterId,
             itemIdList[20], repairCostLow, repairCostHigh)
```

Serverantworten werden UI-seitig auf diese Resultgruppen abgebildet:

- Reparierbar/erfolgreich.
- `ItemRepair_AlreadyMax_Msg`.
- `ItemRepair_InsufficientMoney_Msg`.
- `ItemRepair_DontRepair_Msg`.
- generische Meldungs-IDs `0x13d`, `0x13e`, `0x13f`, `0x141`, `0x142` tauchen im Repair-UI-Kontext auf.

Inferenz:

- Der Server sendet entweder ein direktes Reparaturresultat oder aktualisierte Itemzustandsdaten, die dann die UI-Gridliste und Kostenanzeige zuruecksetzen.
- Der Client uebergibt Kosten an den Server, aber der Server darf diesen Wert nur als Anzeige-/Echo-Wert behandeln und muss die Kosten aus Itemzustand neu berechnen.

## Protokollrisiken und Serverpflichten

- Client sendet viele IDs direkt: Character-ID, Item-ID, Event-ID, Banklayer, Materiallisten. Keine dieser IDs darf serverseitig ungeprueft verwendet werden.
- Mehrere Aktionen sind wirtschaftlich kritisch: Bank, Repair, Convert, Refinery, Product und SkillMaster. Sie brauchen Transaktionen mit Row-/Item-Locks.
- Bei Convert/Refinery/Product muss der Server den Zufallswurf und Materialverbrauch bestimmen, nicht der Client.
- Bei SkillMaster muss der Server Skillpunkte, Geld, Level, Klasse, Prerequisites und NPC-Angebot pruefen.
- Bei Bank muss der Server Banklayer und Gridkoordinaten pruefen; Clientchecks sind nur UI-Komfort.

## Naechste Detailarbeit

- `FUN_006ebcb0`, `FUN_006ebec0`, `FUN_005a10f0`, `FUN_005a0fd0` fuer Bank-Geld/Item-Transaktionen aufloesen.
- Jump-Table-Ziele von `AgpmItemConvert + 0x2688`, `AgpmProduct + 0xd5c` und `AgpmEventSkillMaster + 0x8904` einzeln disassemblieren und benennen.
- Die lokalen INI-Dateien fuer Convert, Refinery, ProductSkill und Evolution mit den Parserfeldern abgleichen.
