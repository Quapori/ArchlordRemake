# Winsock Sequenz 13: Service-NPCs, Bank, Repair, Refinery, SkillMaster, ItemConvert, Product

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Diese Datei dokumentiert die serverrelevanten NPC-Service-Module des `alefclient.exe`. Quellen sind `alefclient.pseudocode.c`, besonders die `AgpmEvent...`-, `AgcmEvent...`-, UI- und Stammdatenmodule. Es wurde kein Live-Traffic mitgeschnitten; Datenbanktabellen sind Inferenz aus Paketfeldern, UI-Flows und lokal geladenen Tabellen.

## Kurzfazit

- Service-NPCs laufen ueber das generische Eventsystem und senden fast immer erst ein NPC/Event-bezogenes Paket.
- Die eigentliche Aktion ist je nach Feature auf zwei Ebenen verteilt:
  - Eventmodule `0x34`, `0x36`, `0x38`, `0x3a`, `0x3b`, `0x3f` fuer NPC-Interaktion.
  - Kernmodule wie [`AgpmItemConvert`](../Module/AgpmItemConvert.md) `0x16`, [`AgpmProduct`](../Module/AgpmProduct.md) `0x17` und [`AgpmRefinery`](../Module/AgpmRefinery.md) `0x4b` fuer die eigentliche wirtschaftliche Aktion.
- Das Paketmuster bleibt gleich: Lowbyte-Subopcode wird in ein bestehendes Integer-Feld geschrieben, Event-ID/Objektbezug kommt ueber `FUN_0055ca00(...)`, danach `FUN_004ea280(...)` und `FUN_004e45d0(...)`.
- Clientseitige Validierungen sind stark vorhanden, aber nicht vertrauenswuerdig fuer den Server: Geld, Level, Itemtyp, Haltbarkeit, Slots, Catalyst/Rune und Banklayer muessen serverseitig erneut validiert werden.

## Relevante Module

| Modul | Modul-ID | Clientwrapper | Zweck |
|---|---:|---|---|
| [`AgpmEventItemRepair`](../Module/AgpmEventItemRepair.md) | `0x34` | [`AgcmEventItemRepair`](../Module/AgcmEventItemRepair.md) | Repair-NPC, Reparaturliste, Reparaturrequest |
| [`AgpmEventBank`](../Module/AgpmEventBank.md) | `0x36` | [`AgcmEventBank`](../Module/AgcmEventBank.md) | Bank-NPC, Bank UI, Bank-Slots, Geld/Item-Lagerung |
| [`AgpmEventItemConvert`](../Module/AgpmEventItemConvert.md) | `0x38` | [`AgcmEventItemConvert`](../Module/AgcmEventItemConvert.md) | Convert-NPC oeffnen/validieren |
| [`AgpmEventProduct`](../Module/AgpmEventProduct.md) | `0x3a` | [`AgcmEventProduct`](../Module/AgcmEventProduct.md) | Product-/Crafting-NPC |
| [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md) | `0x3b` | [`AgcmEventSkillMaster`](../Module/AgcmEventSkillMaster.md) | SkillMaster, Skill-Lernen/Upgrade, Evolution |
| [`AgpmEventRefinery`](../Module/AgpmEventRefinery.md) | `0x3f` | [`AgcmEventRefinery`](../Module/AgcmEventRefinery.md) | Refinery-NPC |
| `AgpmItemConvert` | `0x16` | [`AgcmItemConvert`](../Module/AgcmItemConvert.md) | eigentliche Convert-Aktionen |
| `AgpmProduct` | `0x17` | [`AgcmProduct`](../Module/AgcmProduct.md) | eigentliche Product/Craft-Aktion |
| `AgpmRefinery` | `0x4b` | [`AgcmRefinery`](../Module/AgcmRefinery.md) | eigentliche Refinery-Aktion |

## Gemeinsames Eventmuster

Die `AgcmEvent...`-Wrapper registrieren sich beim [`AgcmEventManager`](../Module/AgcmEventManager.md) mit Funktions-IDs. Beim Anklicken/Ausloesen eines Event-Objekts prueft der Client zuerst, ob der lokale Charakter bereits in einer blockierenden Aktion ist:

```text
FUN_00504fa0(localCharacterCID, 1)
```

Wenn frei, wird ein `AgpmEvent...`-Paket gebaut:

```text
FUN_004ea280(eventModule + layoutOffset, 1, outLen, moduleId, &subopOrEvent, eventObject, &characterCid, ...)
FUN_004e45d0(packet, len, 0, 3, 0)
FUN_00502d00(packet, 1)
```

Der Eventbezug wird ueber `FUN_0055ca00(eventObjectOrFunction)` extrahiert. In den Dekompilaten erscheint oft `param_X = param_X & 0xffffff00` oder `CONCAT31(..., subop)`: das Lowbyte ist der Subopcode, die oberen Bytes behalten einen Objekt-/Eventbezug.

## Bank

### Modul und Layout

`AgpmEventBank`:

- Konstruktor `FUN_00575590`.
- Modul-ID `0x36`.
- Hauptlayout bei `param_1 + 0xb8c`.
- Feldlayout:

```text
FUN_004e9f30(param_1 + 0x2e3, 1,1, 0xc,1, 5,1, 0xff,0)
```

`AgcmEventBank`:

- Konstruktor `FUN_006df800`.
- Bindet [`AgpmCharacter`](../Module/AgpmCharacter.md), `AgpmEventBank`, `AgcmEventManager`, `AgcmCharacter`.
- Registriert Event-Funktion `0x14` mit `FUN_006df870`.
- Registriert zusaetzliche Item-/UI-Callbacks via `FUN_006dd1e0(...)` und `FUN_006e9650(...)`.

### Sendepfad

`FUN_006df870` ist der Event-Callback:

```text
AgcmEventBank event callback
  -> FUN_005757b0(AgpmEventBank, eventData+4, &outLen)
  -> FUN_004e45d0(packet, outLen, 0, 3, 0)
```

`FUN_005757b0` baut das Paket:

```text
FUN_004ea280(AgpmEventBank + 0xb8c, 1, outLen, 0x36, &eventSubop, eventObject, &characterCid)
```

Das Lowbyte wird vor dem Senden auf `0` gesetzt. Das ist sehr wahrscheinlich der Request "Bank-NPC oeffnen / Bankzugriff starten".

### UI und Clientaktionen

[`AgcmUIEventBank`](../Module/AgcmUIEventBank.md) registriert:

- Events: `Bank_OpenUI`, `Bank_CloseUI`, `Bank_ItemUpdate`, `Item_ConfirmBuyBankSlot`, `Bank_NotEnoughBuyCost`.
- Datenfelder: `BankGrid`, `BankMoney`, `BankDummy`, `BankLayerIndex`.
- Commands: `Bank_MoveItem`, `Bank_Money_Input`, `Bank_Money_Set_Input`, `Bank_Money_Set_Output`, `Item_RequestBuyBankSlot`, `Item_BuyBankSlot`, `Item_CancelBankSlot`, `Item_SetBankPrice`, `Item_BankUpdateLayer`, `Item_BankDragDropItem`.
- Statuschecks: `IsActiveBuyBankSlot`, `IsActiveBankSlot1`, `IsActiveBankSlot2`, `IsActiveBankSlot3`.

`FUN_006befc0` verarbeitet die Geld-Eingabe:

- liest Betrag aus Edit-Control mit `atof(...)` und konvertiert mit `FUN_007fecc6()`.
- unterscheidet Deposit/Withdraw ueber `param_1 + 0xbd0`.
- prueft Clientgrenze `0x3b9aca01` fuer kombinierte Geldsumme.
- ruft `FUN_005a10f0(...)` oder `FUN_005a0fd0(...)` auf, also lokale Geldtransfer-Requests/Updates.

`FUN_006bf200` behandelt Bank-Slot-Kauf:

- prueft verfuegbares Geld gegen Slotpreis.
- zeigt `Bank_NotEnoughBuyCost`, wenn Geld nicht reicht.
- sendet anschliessend ueber `FUN_006ebec0(characterId)`.

`FUN_006bf490` behandelt Drag/Drop in Bank:

- nimmt selektierte Item-ID.
- prueft den aktiven Banklayer gegen `character + 0x550`.
- ruft `FUN_006ebcb0(itemId, localCharacterCid, bankLayer, -1, -1)`.

### Server-Inferenz Bank

Wahrscheinliche Tabellen/Strukturen:

- `character_bank_slots`: `character_id`, freigeschaltete Layer/Slots, Kaufzeit, Preisstufe.
- `character_bank_items`: `character_id`, `item_id`, `bank_layer`, `grid_x`, `grid_y`, stack/count.
- `character_wallets`: Inventar-Geld und Bank-Geld getrennt oder mit Ledger-Typ.
- `bank_transactions`: Deposit, withdraw, move item, buy slot, Fehlergrund, vorher/nachher.

Server muss pruefen:

- Besitzer des Items.
- Item nicht equipped/locked/trade/auction.
- Banklayer freigeschaltet.
- Gridposition frei.
- Geldlimit/Overflow.
- Slotkaufpreis und Waehrung.

## ItemRepair

### Modul und Layout

`AgpmEventItemRepair`:

- Konstruktor `FUN_00575a90`.
- Modul-ID `0x34`.
- Hauptlayout bei `param_1 + 0xb94`.
- Zweites Layout bei `param_1 + 0x4d2a`.
- Feldlayout enthaelt unter anderem eine Liste von `0x14` Eintraegen:

```text
FUN_004e9f30(param_1 + 0x2e5, 1,1, 0xc,1, 5,1, 5,0x14, 7,1, 5,1, 0xff,0)
```

`AgcmEventItemRepair`:

- Konstruktor `FUN_006dfa70`.
- Bindet `AgpmEventItemRepair`, `AgcmEventManager`, `AgcmCharacter`, `AgpmCharacter`.
- Registriert Event-Funktion `0x11` mit `FUN_006dfb10`.
- Zusaetzlich Callback via `FUN_0056d2e0(...)`.

### Sendepfade

Oeffnen/Interaktion:

```text
FUN_006dfb10
  -> FUN_00575f30(AgpmEventItemRepair, eventData+4, &outLen)
  -> FUN_004e45d0(...)

FUN_00575f30:
  subop = 3
  FUN_004ea280(AgpmEventItemRepair + 0xb94, 1, outLen, 0x34, &subop, eventObject, &characterCid, 0,0,0)
```

Reparaturrequest:

```text
FUN_006c6ec0
  sammelt bis zu 0x14 Item-IDs aus UI-Liste
  berechnet/uebergibt Gesamtkosten low/high
  -> FUN_00575c00(AgpmEventItemRepair, eventObject, subop, characterId, itemIdList, costLow, costHigh, ..., &outLen)
  -> FUN_004e45d0(...)
```

`FUN_00575c00` baut:

```text
FUN_004ea280(AgpmEventItemRepair + 0xb94, 1, outLen, 0x34,
             &eventSubop, eventObject, &characterId, itemIdList, costLow, costHigh)
```

Der UI-Request ruft `FUN_00575c00(..., subop 0, ...)` auf; `FUN_00575f30` nutzt `subop 3` fuer den Event/NPC-Oeffnungspfad.

### UI und Clientvalidierung

[`AgcmUIEventItemRepair`](../Module/AgcmUIEventItemRepair.md) registriert:

- Events: `ItemRepair_UIOpen_Event`, `ItemRepair_UIClose_Event`, `ItemRepair_InventoryUIOpen_Event`, `ItemRepair_InventoryUIClose_Event`.
- Meldungen: `ItemRepair_AlreadyMax_Msg`, `ItemRepair_InsufficientMoney_Msg`, `ItemRepair_DontRepair_Msg`.
- Datenfelder: `ItemRepair_Cost_Data`, `ItemRepair_MainGrid_Data`, `ItemRepair_InventoryMoney_Data`.
- Commands: `ItemRepair_MoveItem`, `ItemRepair_MoveEnd`, `ItemRepair_UIOpen`, `ItemRepair_RepairReq`.

`FUN_006c6d00` laesst nur Items mit Itemstatus/type `*(short *)(item + 0x12a) == 2` zu, verhindert doppelte Eintraege und blockiert Items ohne reparierbare Haltbarkeit.

`FUN_00575c90` berechnet Reparaturkosten:

- liest Current/Max-Durability aus Faktorblock `item + 0x5c`.
- Kosten basieren auf Differenz und einer itembezogenen Wertfunktion.
- zusaetzlicher Faktor ueber `FUN_0058ac00(...)`.

### Server-Inferenz Repair

Wahrscheinliche Tabellen/Strukturen:

- `item_instances`: aktuelle/maximale Haltbarkeit, Besitzer, Status.
- `repair_transactions`: `character_id`, NPC/Event-ID, Item-ID-Liste, berechnete Kosten, Ergebnis.
- `money_ledger`: Belastung mit Grund `repair`.

Server muss pruefen:

- Alle Item-IDs gehoeren dem Charakter.
- Items sind reparierbar und nicht bereits max.
- Reparaturkosten serverseitig neu berechnen.
- Geld reicht und wird atomar abgezogen.
- Haltbarkeit wird atomar auf Zielwert gesetzt.

## ItemConvert

### Eventmodul `0x38`

`AgpmEventItemConvert`:

- Konstruktor `FUN_00575060`.
- Modul-ID `0x38`.
- Hauptlayout bei `param_1 + 0xb94`.
- Layout:

```text
FUN_004e9f30(param_1 + 0x2e5, 1,1, 0xc,1, 5,1, 0xff,0)
```

`AgcmEventItemConvert`:

- Konstruktor `FUN_006df5e0`.
- Bindet `AgpmCharacter`, `AgpmItemConvert`, `AgpmEventItemConvert`, `AgcmCharacter`, `AgcmEventManager`.
- Registriert Event-Funktion `0x16` mit `FUN_006df630`.

Oeffnungspfad:

```text
FUN_006df630
  -> FUN_00575280(AgpmEventItemConvert, eventData+4, &outLen)
  -> FUN_004e45d0(...)

FUN_00575280:
  FUN_004ea280(AgpmEventItemConvert + 0xb94, 1, outLen, 0x38, &subop0, eventObject, &characterCid)
```

### Kernmodul `AgpmItemConvert` `0x16`

`AgpmItemConvert`:

- Konstruktor `FUN_00583d90`.
- Modul-ID `0x16`.
- Hauptlayout bei `param_1 + 0x2688`.
- Grosses Stammdatenlayout bei `param_1 + 0x53e7`.
- Liest lokale Konvertierungstabellen; Fehlermeldung im Code:

```text
AgpmItemConvert::StreamReadConvertTable() Error (1) !!!
```

Sichtbare Paketbuilder:

| Funktion | Subopcode | Felder |
|---|---:|---|
| `FUN_005946c0` | `1` | char/item/target/catalyst-artige 3 IDs |
| `FUN_00594720` | `2` | char/item |
| `FUN_00594780` | `3` | char/item/socket-or-catalyst |
| `FUN_005947e0` | `4` | gleiche Form wie Subop 3, im Wrapper nicht direkt gefunden |
| `FUN_00594840` | `0x0b` | char/item/extra |
| `FUN_005948a0` | `0x0c` | char/item/extra |

Alle nutzen:

```text
FUN_004ea280(AgpmItemConvert + 0x2688, 1, outLen, 0x16, &subop, &characterId, &itemId, &extraId, ...)
```

`AgcmItemConvert` sendet diese Pakete ueber:

- `FUN_006eaf20` -> `FUN_005946c0`.
- `FUN_006eafa0` -> `FUN_00594720`.
- `FUN_006eb010` -> `FUN_00594780`.
- `FUN_006eb090` -> `FUN_00594840`.
- `FUN_006eb110` -> `FUN_005948a0`.

### UI und Convertarten

[`AgcmUIEventItemConvert`](../Module/AgcmUIEventItemConvert.md) registriert:

- Modes: `Convert_SetPhysicalConvert`, `Convert_SetSocketConvert`, `Convert_SetRuneConvert`.
- Commands: `Convert_AddItem`, `Convert_AddItemSocket`, `Convert_Start`, `Convert_OK`, `Convert_Cancel`.
- Datenfelder: `Convert_Grid`, `Convert_Grid_Socket`, `Convert_Cost`, `Convert_Type`, `Convert_Item`, `Convert_Result`.
- UI-Update: `Convert_Update_NPCConv`, `Convert_Update_ConvertInfo`, `Convert_Update_ConvertConfirm`.

Ergebnis-/Fehlerstrings zeigen die serverseitigen Regeln:

- Physical: `Convert_Physical_Result_AlreadyFull`, `Convert_Physical_Result_ImproperItem`, `Convert_Physical_Success`, `Convert_Physical_KeepCurrent`, `Convert_Physical_Initialize`, `Convert_Physical_Destroy`.
- Socket: `Convert_Socket_Result_ImproperItem`, `Convert_Socket_Result_NotEnoughMoney`, `Convert_Socket_Result_AlreadyFull`, `Convert_Socket_NotEnoughInvenMoney`, `Convert_Socket_Success`, `Convert_Socket_Destroy`.
- Rune: `Convert_Rune_Result_NotEnoughSocket`, `Convert_Rune_Invalid_Rune`, `Convert_Rune_Low_Item_Level`, `Convert_Rune_Improper_Item`, `Convert_Rune_Already_Anti_Conv`, `Convert_Rune_Destroy`.
- Generisch: `Convert_Err_AlreadyFull`, `Convert_Err_NotExistItem`, `Convert_Err_InvalidCatalyst`, `Convert_Err_InvalidRune`, `Convert_Err_NotEnoughSocket`, `Convert_Err_LowCharLevel`, `Convert_Err_LowItemLevel`, `Convert_Err_ImproperPart`, `Convert_Err_NotEnoughMoney`, `Convert_Err_TryEquipItem`, `Convert_Err_AlreadyAntiConvert`.

Die UI verhindert Konvertierung von Equipped/ungeeigneten Items, aber die Serverantworten zeigen, dass der Server diese Fehler ebenfalls liefern muss.

### Server-Inferenz ItemConvert

Wahrscheinliche Tabellen/Strukturen:

- `convert_rules`: Typ `physical/socket/rune`, erlaubte Itemteile, Levelgrenzen, Kosten, Erfolgsrate, Maxslots.
- `convert_catalysts`: Catalyst-ItemTID, Rule-ID, Verbrauchsmenge.
- `convert_runes`: Rune-ItemTID, Effekt, Levelanforderung, Anti-Convert-Flags.
- `item_conversion_history`: Character, Item, Catalyst/Rune, Kosten, Zufallswurf, Ergebnis.
- `item_sockets`: Item-ID, Slotindex, Rune-ID, Status.
- `money_ledger` und `item_ledger` fuer atomaren Verbrauch.

Server muss pruefen:

- Item existiert, gehoert dem Charakter und ist nicht equipped/locked.
- Catalyst/Rune existiert und gehoert dem Charakter.
- Levelanforderung von Charakter und Item.
- Teil/Part passt.
- Socketanzahl und Anti-Convert-Zustand.
- Geld und Verbrauchsmaterial werden atomar gebucht.

## Refinery

### Stammdatenmodul `AgpmRefinery`

`AgpmRefinery`:

- Konstruktor `FUN_00529100`.
- Modul-ID `0x4b`.
- Layout bei `param_1 + 0x313`.
- Bindet [`AgpmItem`](../Module/AgpmItem.md), [`AgpmGrid`](../Module/AgpmGrid.md), [`AgpmFactors`](../Module/AgpmFactors.md), `AgpmCharacter`.
- Registriert zusaetzlich Objekt-/Eventbezug:

```text
FUN_004e4190(0x18, 0)
FUN_004e4190(0x68, 1)
```

`AgpaRefineItem` ist ein eigener Container. `FUN_0058d0c0` legt RefineItems ueber einen String-Key ab.

### Eventmodul `0x3f`

`AgpmEventRefinery`:

- Konstruktor `FUN_0056fb20`.
- Modul-ID `0x3f`.
- Hauptlayout bei `param_1 + 0xb90`.
- Zweites Layout bei `param_1 + 0x4d29`.

`AgcmEventRefinery`:

- Konstruktor `FUN_006de620`.
- Bindet `AgpmCharacter`, `AgpmEventRefinery`, `AgcmCharacter`, `AgcmEventManager`.
- Registriert Event-Funktion `0x1a` mit `FUN_006de690`.

Oeffnungspfad:

```text
FUN_006de690
  -> FUN_0056fd70(AgpmEventRefinery, eventData+4, &outLen)
  -> FUN_004e45d0(...)

FUN_0056fd70:
  FUN_004ea280(AgpmEventRefinery + 0xb90, 1, outLen, 0x3f, &subop0, eventObject, &characterCid)
```

### Kernaktion `AgcmRefinery`

`AgcmRefinery` bindet `AgpmRefinery`. Die sichtbare Sendefunktion ist `FUN_006e7e50`:

```text
local_5 = 2
FUN_004ea280(AgpmRefinery + 0xc4c, 1, outLen, 0x4b,
             &subop2, &param_2, &param_3, param_4, 0, 0)
FUN_004e45d0(...)
```

Der UI-Pfad `FUN_006a11c0` sammelt zehn Item-IDs aus einem lokalen Array `local_28[10]` und ruft `FUN_006e7e50(...)`. Daraus folgt: Refinery sendet eine bis zu 10 Eintraege umfassende Materialliste.

### Server-Inferenz Refinery

Wahrscheinliche Tabellen/Strukturen:

- `refinery_recipes`: Recipe-ID/Name, benoetigte Materialien, Ergebnis, Erfolgsrate, Kosten.
- `refinery_npcs`: Event-ID, erlaubte Recipe-Gruppe.
- `refinery_attempts`: Character, Event-ID, Material-Item-IDs, Ergebnis, Kosten, Zufallswurf.
- `item_ledger`: verbrauchte Materialien und erzeugtes/refined Item.

Server muss pruefen:

- Alle zehn Materialslots bzw. belegte Slots gehoeren dem Charakter.
- Recipe passt zu Material-TIDs und NPC/Event.
- Stackmengen und Itemzustand.
- Erfolg/Fehlschlag und Materialverbrauch serverseitig bestimmen.

## Product / Crafting

### Eventmodul `0x3a`

`AgpmEventProduct`:

- Konstruktor `FUN_00570040`.
- Modul-ID `0x3a`.
- Hauptlayout bei `param_1 + 0xb94`.
- Zweites Layout bei `param_1 + 0x4d2a`.
- Mehrere Subops sichtbar:
  - `FUN_005704c0`: Lowbyte `0`.
  - `FUN_005705c0`: Lowbyte `2`.
  - `FUN_00570540`: Lowbyte `4`.

`AgcmEventProduct`:

- Konstruktor `FUN_006de850`.
- Bindet `AgpmCharacter`, `AgpmEventProduct`, `AgcmCharacter`, `AgcmEventManager`.
- Registriert Event-Funktion `0x18` mit `FUN_006de8a0`.
- Hat direkte Wrapper:
  - `FUN_006de980` -> `FUN_005705c0`, Subop `2`.
  - `FUN_006dea10` -> `FUN_00570540`, Subop `4`.

### Kernmodul `AgpmProduct`

`AgcmProduct` sendet ueber `AgpmProduct` Modul `0x17`:

```text
FUN_006e8000:
  local_5 = 0
  FUN_004ea280(AgpmProduct + 0xd5c, 1, outLen, 0x17,
               &subop0, arg1, arg2, arg3, arg4, 0,0,0)
```

[`AgcmUIProductSkill`](../Module/AgcmUIProductSkill.md):

- Grids: `PDSK_LISTGRID`, `PDSK_BUYLISTGRID`.
- Datenfelder: `PDSK_BUYINVENMONEY`, `PDSK_BUYACTIVEBUYBTN`, `PDSK_TITLE`.
- Interne Listen haben jeweils `0x3c` Slots.
- `FUN_006a11c0`/Refinery-nahe Logik sammelt Materiallisten; Product UI unterscheidet Listen-Item (`type 2`) und Skill/Recipe (`type 1`).

Stammdatencontainer:

- `AgpaProductSkillFactor`.
- `AgpaComposeTemplate`.
- `AgpaSkillTemplate`.

### Server-Inferenz Product

Wahrscheinliche Tabellen/Strukturen:

- `product_skills`: Skill-ID, Charakterlevel, Beruf/Rank, Kosten.
- `compose_templates`: Recipe-ID, Materialliste, Ergebnisliste, Erfolgsrate.
- `character_product_skills`: gelernte/gekaufte Product-Skills, Ranks, EXP.
- `product_attempts`: Character, Recipe, Materialien, Ergebnis, Kosten.
- `product_shop_entries`: NPC/Event-ID, angebotene Skills/Recipes.

Server muss pruefen:

- Rezept/Skill ist beim NPC verfuegbar.
- Charakter hat erforderlichen Product-Skill/Rank.
- Materialien und Geld vorhanden.
- Ergebnisplatz im Inventar vorhanden.

## SkillMaster

### Modul und Layout

`AgpmEventSkillMaster`:

- Konstruktor `FUN_00574520`.
- Modul-ID `0x3b`.
- Groesser als die anderen Eventmodule; haelt mehrere interne Listen ab `0x2227`, `0x222d`, `0x2233`, `0x2239`.
- Enthaelt `AgpmEventSkillMasterEvolution` als Unterobjekt bei `param_1 + 0xb6cb`.
- Hauptlayout bei `param_1 + 0x8904`.
- Zweites Layout bei `param_1 + 0x6c86`.
- Initialisiert einen grossen Bereich von `32000` Bytes fuer SkillMaster-Daten.

`AgcmEventSkillMaster`:

- Konstruktor `FUN_006deb70`.
- Bindet `AgpmCharacter`, `AgpmEventSkillMaster`, `AgcmCharacter`, [`AgcmItem`](../Module/AgcmItem.md), [`AgcmSkill`](../Module/AgcmSkill.md), `AgcmEventManager`.
- Registriert Event-Funktion `0x19`.
- Registriert Skill-/Item-Callbacks via `FUN_005781f0(...)` und `FUN_0058ee20(...)`.

### Sendepfade

Sichtbare Builder im `AgpmEventSkillMaster`:

| Funktion | Subopcode | Bedeutung aus Kontext |
|---|---:|---|
| `FUN_00570e40` | `1` | NPC/Event oeffnen oder SkillMaster-Aktion mit Skill-ID |
| `FUN_00570ee0` | `2` | Aktion mit zusaetzlichem Level/Index; `param_5 > 0` |
| `FUN_00570fa0` | `4` | SkillMaster-Request ohne extra Itemliste |
| `FUN_00571030` | `8` | Aktion ohne Eventobjekt, nur Character/Skill-Daten |

Wrapper:

- `FUN_006dec60` -> `FUN_00570e40`, Subop `1`.
- `FUN_006decf0` -> `FUN_00570ee0`, Subop `2`.
- `FUN_006debe0` -> `FUN_00570fa0`, Subop `4`.
- `FUN_006ded90` -> `FUN_00571030`, Subop `8`.

Alle senden:

```text
FUN_004ea280(AgpmEventSkillMaster + 0x8904, 1, outLen, 0x3b, &subop, eventObjectOr0, &characterCid, ...)
FUN_004e45d0(...)
```

### UI-/Skill-Hinweise

Skill-UI-Strings zeigen Skillkauf und Mastery:

- `Skill_SetMasteryTab_5`
- `Skill_ErrorAlreadyLearnSkill`
- `Skill_ConfirmLearnSkill`
- Commands: `SkillSetMastery0` bis `SkillSetMastery4`, `SkillSetMasteryHighLevel`, `SkillSetMasteryHeroic`.
- Commands: `SkillSetBuyMastery0` bis `SkillSetBuyMastery3`.
- Commands: `SkillSetUpgradeMastery0` bis `SkillSetUpgradeMastery3`.
- Evolution-Kontext: `Evolution`, `IsEvolutionNotUseInitSkillItem`, `INI\\ItemEvolutionTable.txt`.

### Server-Inferenz SkillMaster

Wahrscheinliche Tabellen/Strukturen:

- `skill_master_npcs`: Event-ID, erlaubte Klassen/Rassen/Skillgruppen.
- `skill_templates`: Skill-ID, Mastery, Maxlevel, Levelkosten, Prerequisites.
- `character_skills`: Character, Skill-ID, Level, Mastery, Cooldowns/Flags.
- `skill_purchase_transactions`: Skill-ID, Kosten, SP/Geld-Verbrauch, Ergebnis.
- `evolution_rules`: Item/Skill/Charakter-Anforderung, Zielzustand, Kosten.
- `character_evolution_state`: Fortschritt, freigeschaltete Stufen.

Server muss pruefen:

- Klasse/Rasse/Level/Skillpunkte/Geld.
- Prerequisite-Skills und Maxlevel.
- SkillMaster-NPC bietet diese Skillgruppe an.
- Evolution-Items nicht equipped/locked und korrekt verbraucht.

## Was wann zum Server geht

1. Charakter klickt einen Service-NPC/Eventtrigger.
2. `AgcmEventManager` ruft die registrierte Funktion auf:
   - Bank `0x14`
   - Repair `0x11`
   - ItemConvert `0x16`
   - Product `0x18`
   - SkillMaster `0x19`
   - Refinery `0x1a`
3. Client prueft blockierende Aktion/Distanz/Eventzustand.
4. Eventpaket wird mit Modul-ID `0x34/0x36/0x38/0x3a/0x3b/0x3f` gesendet.
5. Server bestaetigt und liefert UI-/Statusdaten oder oeffnet den Service.
6. Bei konkreter Aktion sendet der Client ein spezialisiertes Paket:
   - Bank: Item/Geld/Slotkauf ueber Item-/Bank-Callbacks.
   - Repair: `0x34` mit bis zu 20 Item-IDs und Kosten.
   - ItemConvert: `0x16` mit Item/Catalyst/Rune/Subop.
   - Refinery: `0x4b` mit bis zu 10 Material-IDs.
   - Product: `0x17` oder `0x3a` je nach Craft/Skill/Listenaktion.
   - SkillMaster: `0x3b` Subops `1/2/4/8`.
7. Server sendet Ergebnisstatus; Client zeigt Erfolg/Fehler und aktualisiert Items, Geld, Skills oder UI-Listen.

## Noch offene Detailarbeit

- Die genauen Receive-Switches fuer `0x34`, `0x36`, `0x38`, `0x3a`, `0x3b`, `0x3f`, `0x16`, `0x17`, `0x4b` sollten als naechster Schritt opcodeweise aus `FUN_004e9fb0(...)`-Aufrufern extrahiert werden.
- Bank-Geld/Item-Callbacks `FUN_006ebcb0`, `FUN_006ebec0`, `FUN_005a10f0`, `FUN_005a0fd0` sollten tiefer gemappt werden, da sie wahrscheinlich die eigentlichen Bank-Transaktionspakete bauen.
- `AgpmItemConvert::StreamReadConvertTable()` sollte mit den zugehoerigen INI-Dateien aus den Spieldaten abgeglichen werden; dort stehen vermutlich die exakten Tabellenfelder.
- `AgpmEventSkillMasterEvolution` verdient eine eigene Deep-Dive-Datei, weil es stark nach einem separaten Skill/Item-Evolution-Protokoll aussieht.
