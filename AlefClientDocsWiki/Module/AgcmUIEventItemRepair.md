# AgcmUIEventItemRepair (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIEventItemRepair` (Reparatur-Fenster beim NPC) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIEventItemRepair/AgcmUIEventItemRepair.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 27 von 28 Quellmethoden sind zugeordnet; neu sind `RefreshGrid`, `RefreshRepairCost`, `ShowMessage`, `ClearGridMainUI`, `FindItemRepairGrid`, `AddItemRepairItemGrid`, `RemoveItemRepairItemGrid` und `OnMoveItem`.
- **Gitter:** 20 Plätze, 4 Spalten.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIEventItemRepair.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006C6AE0` | 518 | vtable/String |
| 1 | `OnInit` | `0x006C5C40` | 44 | vtable/String |
| 2 | `OnDestroy` | `0x006C5C70` | 24 | vtable/String |
| 3 | `AddFunctions` | `0x006C6A30` | 163 | Zeichenkette |
| 4 | `AddEvents` | `0x006C5C90` | 228 | Zeichenkette |
| 5 | `AddUserDatas` | `0x006C5D80` | 121 | Zeichenkette |
| 6 | `AddDisplay` | `0x006C61D0` | 69 | Zeichenkette |
| 7 | `ClearGridMainUI` | `0x006C6220` | 56 | ver |
| 8 | `RefreshGrid` | `0x006C5E00` | 50 | ver |
| 9 | `RefreshInventoryMoney` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `RefreshRepairCost` | `0x006C5E40` | 21 | ver |
| 11 | `FindItemRepairGrid` | `0x006C6260` | 51 | ver |
| 12 | `ShowMessage` | `0x006C5E60` | 122 | ver |
| 13 | `CBGrant` | `0x006C5EF0` | 121 | Callback-Registrierung |
| 14 | `CBItemRepairAck` | `0x006C5F70` | 113 | Callback-Registrierung |
| 15 | `CBSelfUpdatePosition` | `0x006C5FF0` | 166 | Callback-Registrierung |
| 16 | `CBRideFailMessage` | `0x006C60A0` | 44 | Callback-Registrierung |
| 17 | `CBMoveItem` | `0x006C69A0` | 136 | UI-Registrierung |
| 18 | `OnMoveItem` | `0x006C66B0` | 439 | ver |
| 19 | `CBMoveEndItem` | `0x006C62A0` | 290 | UI-Registrierung |
| 20 | `AddItemRepairItemGrid` | `0x006C63D0` | 98 | ver |
| 21 | `RemoveItemRepairItemGrid` | `0x006C6440` | 71 | ver |
| 22 | `CBRemoveInventoryGrid` | `0x006C6490` | 80 | Callback-Registrierung |
| 23 | `CBUpdateMoney` | `0x006C60D0` | 78 | Callback-Registrierung |
| 24 | `CBDisplayInventoryMoney` | `0x006C6120` | 57 | UI-Registrierung |
| 25 | `CBDisplayRepairCost` | `0x006C6160` | 57 | UI-Registrierung |
| 26 | `CBItemRepairUIOpen` | `0x006C64E0` | 166 | UI-Registrierung |
| 27 | `CBItemRepairReq` | `0x006C6870` | 298 | UI-Registrierung |

27 von 28 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmUIEventItemRepair` (`0x006C61A0`), `AgcmUIEventItemRepair` (`0x006C6590`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBF8 / 0xBFC / 0xC00` | `Benutzerdaten Hauptgitter / Inventargeld / Reparaturkosten` | `RefreshGrid`, `RefreshRepairCost` |
| `0xC04` | `Reparaturgitter `m_RepairItemGrid`` | `ClearGridMainUI` |
| `0xC28` | `Zeigerliste `m_pSources` (20 × 4 Byte)` | `FindItemRepairGrid` |

## Vtable

Vtable bei `0x008D5284`: Slot 0 Destruktor `0x006C61A0`, 1 `OnAddModule` (`0x006C6AE0`), 2 `OnInit` (`0x006C5C40`), 7 `OnDestroy` (`0x006C5C70`), 6 `return TRUE`-Rumpf `0x0067AC90`.

## Callbacks (OnAddModule, 0x006C6AE0)

Elf Module werden geholt (u. a. [`AgpmEventItemRepair`](AgpmEventItemRepair.md), [`AgcmEventItemRepair`](AgcmEventItemRepair.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmSkill`](AgcmSkill.md)). Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x006C5FF0` |
| `AgcmEventItemRepair`: Ereignis gewährt | `CBGrant` | `0x006C5EF0` |
| [`AgpmItem`](AgpmItem.md): Gegenstand aus dem Inventargitter entfernt | `CBRemoveInventoryGrid` | `0x006C6490` |
| [`AgpmCharacter`](AgpmCharacter.md): Geld geändert | `CBUpdateMoney` | `0x006C60D0` |
| `AgpmEventItemRepair`: Reparatur bestätigt | `CBItemRepairAck` | `0x006C5F70` |
| `AgcmSkill`: Reiten fehlgeschlagen | `CBRideFailMessage` | `0x006C60A0` |

Danach `AddFunctions`, `AddEvents`, `AddUserDatas` und `AddDisplay`. Reihenfolge wie in der Quelle.

## Reparatur-Gitter

Das Gitter hat 20 Plätze (4 Spalten; Index = Zeile × 4 + Spalte), die zugehörigen Zeiger liegen in `m_pSources`. `AddItemRepairItemGrid` (`0x006C63D0`) trägt einen Gegenstand ein, `RemoveItemRepairItemGrid` (`0x006C6440`) löscht ihn, `FindItemRepairGrid` (`0x006C6260`) sucht ihn, `ClearGridMainUI` (`0x006C6220`) leert Gitter und Zeigerliste. `RefreshGrid` (`0x006C5E00`) und `RefreshRepairCost` (`0x006C5E40`) aktualisieren die Benutzerdaten; `RefreshInventoryMoney` ist in `CBUpdateMoney` eingebaut. `OnMoveItem` (`0x006C66B0`) fügt per Ziehen einen Gegenstand ein, wenn er im Inventar liegt (Status 2) und noch Platz ist.

## Rückmeldungen (ShowMessage, 0x006C5E60)

Die Ergebniscodes verzweigen wie in der Quelle: 1 Erfolg (Systemmeldung `STI_REPAIR_COMPLETE`), 2 zu wenig Geld (Ereignis `+0xBD8`), 3 bereits voll (Ereignis `+0xBD4`), 4 und 5 Systemmeldungen (UI-Texte `0x13E`/`0x13F`).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006C6A30`, `0x006C5C90`, `0x006C5D80`, `0x006C61D0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (4)

| Name | Id | Handler |
|---|---:|---|
| `ItemRepair_MoveItem` |  | `CBMoveItem` |
| `ItemRepair_MoveEnd` |  | `CBMoveEndItem` |
| `ItemRepair_UIOpen` |  | `CBItemRepairUIOpen` |
| `ItemRepair_RepairReq` |  | `CBItemRepairReq` |

**Ereignis** (7)

| Name | Id | Handler |
|---|---:|---|
| `ItemRepair_UIOpen_Event` | 0 | – |
| `ItemRepair_UIClose_Event` | 0 | – |
| `ItemRepair_InventoryUIOpen_Event` | 0 | – |
| `ItemRepair_InventoryUIClose_Event` | 0 | – |
| `ItemRepair_AlreadyMax_Msg` | 0 | – |
| `ItemRepair_InsufficientMoney_Msg` | 0 | – |
| `ItemRepair_DontRepair_Msg` | 0 | – |

**UserData** (3)

| Name | Id | Handler |
|---|---:|---|
| `ItemRepair_Cost_Data` | 0 | – |
| `ItemRepair_MainGrid_Data` |  | – |
| `ItemRepair_InventoryMoney_Data` | 0 | – |

**Anzeige** (2)

| Name | Id | Handler |
|---|---:|---|
| `ItemRepair_InventoryMoney_Display` | 0 | `CBDisplayInventoryMoney` |
| `ItemRepair_Cost_Display` | 0 | `CBDisplayRepairCost` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`ShowMessage`, Gitterfunktionen, Registrierungsreihenfolge).

## Grenzen

- `RefreshInventoryMoney` (4 Zeilen) ist in `CBUpdateMoney` eingebaut und nicht als eigene Funktion zu finden.
- `OnMoveItem` wurde nur nach Aufrufern und Aufgerufenen zugeordnet, nicht Zeile für Zeile verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventItemRepair`](AgcmEventItemRepair.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventItemRepair`](AgpmEventItemRepair.md), [`AgpmItem`](AgpmItem.md)
