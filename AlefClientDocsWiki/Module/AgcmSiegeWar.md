# AgcmSiegeWar (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmSiegeWar` (Belagerungs-Pakete senden, Minimap-Punkte der Belagerungsobjekte, Texturen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmSiegeWar/AgcmSiegeWar.cpp`. Das Paketformat steht im Bericht [AgpmSiegeWar](AgpmSiegeWar.md), die Oberfläche in [AgcmUISiegeWar](AgcmUISiegeWar.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 33 von 36 Quellmethoden zugeordnet; offen sind `SendCancelAttackApplication` (nicht im Binary), `GetSiegeWarDisplayInfo` (eingebaut) und `SetCallbackOpenCheckResult` (Einzeiler ohne eigene Funktion).
- **Pakete:** 14 Sendefunktionen; jede ist über die Operationsnummer im gebauten Paket eindeutig (1, 3, 4, 5, 7, 8, 11, 13, 16, 18, 20, 22, 23, 27). Operation 6 (Angriffsanmeldung zurückziehen) sendet der Client nicht.
- **Rückrufe:** Reihenfolge und Bedingungen in `OnAddModule` wie in der Quelle (Minimap optional); die vier Rückrufe verwalten Minimap-Punkte für neun Belagerungs-Monstertypen und entfernen nach Ablauf der Belagerung die Gilden-NPCs.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmSiegeWar.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E1590` | 218 | vtable/String |
| 1 | `SendNextSiegeWarTime` | `0x006E0520` | 143 | von Hand geprüft |
| 2 | `SendDefenseApplication` | `0x006E05B0` | 125 | von Hand geprüft |
| 3 | `SendCancelDefenseApplication` | `0x006E0630` | 125 | von Hand geprüft |
| 4 | `SendAttackApplication` | `0x006E06B0` | 125 | von Hand geprüft |
| 5 | `SendCancelAttackApplication` | – | | keine Funktion im Binary, die Operation 6 sendet (nicht aufgerufen, vom Linker entfernt) |
| 6 | `SendRequestAttackApplGuildList` | `0x006E0730` | 130 | von Hand geprüft |
| 7 | `SendRequestDefenseApplGuildList` | `0x006E07C0` | 130 | von Hand geprüft |
| 8 | `SendSelectDefenseGuild` | `0x006E0850` | 139 | von Hand geprüft |
| 9 | `SendRequestDefenseGuildList` | `0x006E08E0` | 125 | von Hand geprüft |
| 10 | `SendRequestOpenAttackObject` | `0x006E0960` | 128 | von Hand geprüft |
| 11 | `SendRequestUseAttackObject` | `0x006E09E0` | 128 | von Hand geprüft |
| 12 | `SendRequestRepairAttackObject` | `0x006E0A60` | 128 | von Hand geprüft |
| 13 | `SendRemoveItemToAttackObject` | `0x006E0AE0` | 140 | von Hand geprüft |
| 14 | `SendAddItemToAttackObject` | `0x006E0B70` | 140 | von Hand geprüft |
| 15 | `SendCarveASeal` | `0x006E0C00` | 128 | von Hand geprüft |
| 16 | `ClickCharacter` | `0x006E0C80` | 142 | von Hand geprüft |
| 17 | `SetCatapultUseTexture` | `0x006E0D10` | 25 | von Hand geprüft |
| 18 | `SetCatapultRepairTexture` | `0x006E0D30` | 25 | von Hand geprüft |
| 19 | `SetAtkResTowerUseTexture` | `0x006E0D50` | 25 | von Hand geprüft |
| 20 | `SetAtkResTowerRepairTexture` | `0x006E0D70` | 25 | von Hand geprüft |
| 21 | `SetCastleOwnerTexture` | `0x006E0D90` | 37 | von Hand geprüft |
| 22 | `GetCatapultUseTexture` | `0x006E0DC0` | 7 | von Hand geprüft |
| 23 | `GetCatapultRepairTexture` | `0x006E0DD0` | 7 | von Hand geprüft |
| 24 | `GetAtkResTowerUseTexture` | `0x006E0DE0` | 7 | von Hand geprüft |
| 25 | `GetAtkResTowerRepairTexture` | `0x006E0DF0` | 7 | von Hand geprüft |
| 26 | `GetCastleOwnerTextureTexture` | `0x006E0E00` | 24 | von Hand geprüft |
| 27 | `GetSiegeWarGuildType` | `0x006E0E20` | 135 | von Hand geprüft |
| 28 | `CBInitCharacter` | `0x006E14E0` | 166 | von Hand geprüft |
| 29 | `CBUpdateCharStatus` | `0x006E0F10` | 151 | von Hand geprüft |
| 30 | `CBRemoveCharacter` | `0x006E1010` | 139 | von Hand geprüft |
| 31 | `CBRemoveNPCGuildCharacter` | `0x006E10A0` | 353 | von Hand geprüft |
| 32 | `GetSiegeWarDisplayInfo` | – | | lineare Suche, in die Rückrufe eingebaut |
| 33 | `AddSiegeWarDisplayInfo` | `0x006E1480` | 94 | von Hand geprüft |
| 34 | `RemoveSiegeWarDisplayInfo` | `0x006E0FB0` | 91 | von Hand geprüft |
| 35 | `SetCallbackOpenCheckResult` | – | | Einzeiler (`SetCallback`), keine eigene Funktion gefunden |

33 von 36 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmSiegeWar` (`0x006E1350`), `~AgcmSiegeWar_body` (`0x006E13F0`), `~AgcmSiegeWar` (`0x006E1460`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98 / 0xB9C / 0xBA0` | `Anzeigeliste (`std::vector`, 8 Byte je Eintrag)` | `AddSiegeWarDisplayInfo`, `RemoveSiegeWarDisplayInfo` |
| `0xBA4–0xBB4` | `Zeiger auf [`AgpmCharacter`](AgpmCharacter.md), [`AgpmSiegeWar`](AgpmSiegeWar.md), [`AgpmGuild`](AgpmGuild.md), `AgcmCharacter`, [`AgcmMinimap`](AgcmMinimap.md)` | `OnAddModule` |
| `0xBB8–0xBC4` | `Katapult-/Wiederbelebungsturm-Texturen (je Nutzen, Reparatur)` | Set-/Get-Funktionen |
| `0xBC8` | `Burg-Besitzer-Texturen (5)` | `SetCastleOwnerTexture` |

## Vtable

Vtable bei `0x008D8904`: Slot 0 Destruktor `0x006E1460`, 1 `OnAddModule` (`0x006E1590`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`, `return TRUE`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (`OnIdle`), 6 und 7 `0x0067AC90`.

## OnAddModule (0x006E1590)

Holt `AgpmCharacter` (`this+0xBA4`), `AgpmSiegeWar` (`0xBA8`), `AgpmGuild` (`0xBAC`), `AgcmCharacter` (`0xBB0`) und `AgcmMinimap` (`0xBB4`); die ersten vier sind Pflicht, `AgcmMinimap` ist optional. Nur mit Minimap werden die Rückrufe `AgpmCharacter`: Charakter angelegt (`CBInitCharacter`, `0x006E14E0`), Aktionsstatus geändert (`CBUpdateCharStatus`, `0x006E0F10`) und Charakter entfernt (`CBRemoveCharacter`, `0x006E1010`) angemeldet; der Rückruf `AgpmSiegeWar`: Burginfo aktualisiert → `CBRemoveNPCGuildCharacter` (`0x006E10A0`) wird immer angemeldet. Reihenfolge und Bedingungen entsprechen der Quelle.

## Pakete senden (Send…)

Alle 14 im Binary vorhandenen `Send…` bauen das Paket in `AgpmSiegeWar` und schicken es mit `SendPacket` (`0x004E45A0`); die Selbst-ID kommt aus `AgcmCharacter` (`this+0xBB0`, dort `+0x15964`). Die Zuordnung stützt sich auf die Operationsnummer, die jede `MakePacket…` in das Paket schreibt (Aufzählung `AGPMSIEGE_OPERATION_*` der Quelle):

| Funktion | Adresse | `MakePacket…` | Operation |
|---|---|---|---|
| `SendNextSiegeWarTime` | `0x006E0520` | `0x00521610` | 1 |
| `SendDefenseApplication` | `0x006E05B0` | `0x005216E0` | 3 |
| `SendCancelDefenseApplication` | `0x006E0630` | `0x005217B0` | 4 |
| `SendAttackApplication` | `0x006E06B0` | `0x00521880` | 5 |
| `SendRequestAttackApplGuildList` | `0x006E0730` | `0x00521950` | 7 |
| `SendRequestDefenseApplGuildList` | `0x006E07C0` | `0x00521A60` | 8 |
| `SendSelectDefenseGuild` | `0x006E0850` | `0x00521C40` | 11 |
| `SendRequestDefenseGuildList` | `0x006E08E0` | `0x00521B70` | 13 |
| `SendRequestOpenAttackObject` | `0x006E0960` | `0x0051F9A0` | 16 |
| `SendRequestUseAttackObject` | `0x006E09E0` | `0x0051FA00` | 18 |
| `SendRequestRepairAttackObject` | `0x006E0A60` | `0x0051FA60` | 20 |
| `SendRemoveItemToAttackObject` | `0x006E0AE0` | `0x0051FB20` | 23 |
| `SendAddItemToAttackObject` | `0x006E0B70` | `0x0051FAC0` | 22 |
| `SendCarveASeal` | `0x006E0C00` | `0x0051FB80` | 27 |

`SendCancelAttackApplication` (Operation 6) hat im Binary keine eigene Funktion; die Operation 6 wird vom Client nicht gesendet (kein Aufrufer einer solchen Funktion gefunden). Die Prüfungen (`pcsSiegeWar` nicht leer, `ullNextSiegeWarTime != 0`, Gildenname nicht leer, Paketlänge über dem 12-Byte-Kopf) entsprechen der Quelle.

## ClickCharacter (0x006E0C80)

Fragt `GetSiegeWarMonsterType` (`0x00520350`) ab. Bei Typ 6 (Thron) wird geprüft, ob die Prüffunktion `0x00521F00` zustimmt, dann `SendCarveASeal`; bei Typ 9 oder 10 (Angriffs-Wiederbelebungsturm, Katapult) wird zuerst geprüft, ob der eigene Charakter zur angreifenden Gilde gehört (`IsAttackGuild`, `0x0051FDA0`), dann `SendRequestOpenAttackObject`. Andere Typen liefern `FALSE`.

## Minimap-Rückrufe

Alle vier Rückrufe reagieren nur auf die neun Belagerungs-Monstertypen 1–7, 9 und 10 (Wachturm, Innentor, Außentor, Lebensturm, Verteidigungs-Wiederbelebungsturm, Thron, Archon-Augen, Angriffs-Wiederbelebungsturm, Katapult).
- `CBInitCharacter` (`0x006E14E0`): Ist der Charakter noch nicht in der Anzeigeliste und `m_bNPCDisplayForMap` (`+0x7D4`) nicht gesetzt, legt es einen Minimap-Punkt an (`AgcmMinimap::AddPoint`, `0x006E3640`; Typ 3 = normal, 4 = zerstört bei Aktionsstatus 2) und trägt Charakter-ID und Index mit `AddSiegeWarDisplayInfo` (`0x006E1480`) ein.
- `CBUpdateCharStatus` (`0x006E0F10`): Sucht den Eintrag und setzt den Punkttyp neu (3 oder 4).
- `CBRemoveCharacter` (`0x006E1010`): Entfernt den Minimap-Punkt (`0x006E2A60`) und den Eintrag (`RemoveSiegeWarDisplayInfo`, `0x006E0FB0`).
- `CBRemoveNPCGuildCharacter` (`0x006E10A0`): Nur wenn der Belagerungs-Status 7 (Zeit abgelaufen) ist, sammelt es alle Monster mit Gilden-ID (`GetCharSequence` `0x00502F90`, `IsMonster` `0x00502950`, `GetADCharacter` `0x0054D230`, nicht-leere Gilden-ID) in einer `std::list` und entfernt sie danach mit `RemoveCharacter` (`0x005060F0`).
Die Anzeigeliste ist ein `std::vector` aus Paaren (Charakter-ID, Minimap-Index) bei `this+0xB98`/`0xB9C`/`0xBA0`; `GetSiegeWarDisplayInfo` ist als lineare Suche in die Rückrufe eingebaut.

## Texturen und Gildentyp

Die zehn Zugriffsfunktionen sind Einzeiler: `SetCatapultUseTexture`/`…RepairTexture` schreiben `this+0xBB8`/`0xBBC`, `SetAtkResTowerUseTexture`/`…RepairTexture` `0xBC0`/`0xBC4` (jeweils nur bei Zeiger ≠ 0), `SetCastleOwnerTexture` (`0x006E0D90`) ab `0xBC8` mit Index 0–4 (`AGPMSIEGEWAR_MAX_CASTLE` = 5). Die Getter geben die Zeiger zurück (`0x006E0DC0`–`0x006E0E00`).
`GetSiegeWarGuildType` (`0x006E0E20`) liefert 1 für die angreifende, 2 für die verteidigende Gilde und sonst −1 (auch wenn die Belagerung nicht läuft); `IsAttackGuild` (`0x0051FDA0`) und `IsDefenseGuild` (`0x0051FD50`) werden dort aufgerufen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Namen der vier Rückrufe waren zunächst durch den Anker-Scan vertauscht; sie wurden anhand der Dekompilate (Minimap-Punkt anlegen/ändern/entfernen, Status 7) und der Registrierung in `OnAddModule` korrigiert.
- Die Zuordnung der `MakePacket…` stützt sich auf die Operationsnummer im Paket; die Feldreihenfolge der Pakete wurde nicht geprüft.
- `GetSiegeWarGuildType` ist über Rückgabewerte (−1/1/2) und die Aufrufe von `IsAttackGuild`/`IsDefenseGuild` zugeordnet, nicht Zeile für Zeile verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, nicht im Client: 1, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmMinimap`](AgcmMinimap.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmGuild`](AgpmGuild.md), [`AgpmSiegeWar`](AgpmSiegeWar.md)
- **Erwähnt in:** [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md)
