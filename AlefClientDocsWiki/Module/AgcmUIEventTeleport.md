# AgcmUIEventTeleport (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIEventTeleport` (Teleport-Oberfläche: Zielliste, Gebühr, Ladefenster) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIEventTeleport/AgcmUIEventTeleport.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 24 von 24 Quellmethoden sind zugeordnet; neu sind `CBReceivedTeleportCanceled`/`CBMapLoadEnd` (gleiche Adresse), `IsDisablePoint`, `CheckIsUsablePortalByMurdererPoint`, `RefreshTeleportList`; `OnInit` und `OnDestroy` stehen als zusammengefaltete Rümpfe.
- **Mörder-Schwellen:** 40 / 60 / 100 Punkte, Stufe 3 sperrt das Portal.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIEventTeleport.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006C5A70` | 452 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `OnIdle` | `0x006C5570` | 39 | vtable/String |
| 4 | `AddFunctions` | `0x006C5A10` | 85 | Zeichenkette |
| 5 | `AddEvents` | `0x006C5100` | 300 | Zeichenkette |
| 6 | `AddUserData` | `0x006C4C20` | 52 | Zeichenkette |
| 7 | `AddDisplay` | `0x006C55A0` | 110 | Zeichenkette |
| 8 | `CBSelectTeleportPoint` | `0x006C5610` | 984 | Callback-Registrierung |
| 9 | `CBCannotUseForTransforming` | `0x006C4C60` | 42 | Callback-Registrierung |
| 10 | `CBCannotUseForCombatMode` | `0x006C4C90` | 51 | Callback-Registrierung |
| 11 | `CBReceivedTeleportStart` | `0x006C4CD0` | 60 | Callback-Registrierung |
| 12 | `CBReceivedTeleportCanceled` | `0x006C4D10` | 63 | ver |
| 13 | `CBMapLoadEnd` | `0x006C4D10` | 63 | gleiche Adresse wie `CBReceivedTeleportCanceled` (vom Linker zusammengefaltet) |
| 14 | `CBSelfUpdatePosition` | `0x006C4D50` | 136 | Callback-Registrierung |
| 15 | `CBRequestTeleport` | `0x006C4DE0` | 355 | UI-Registrierung |
| 16 | `CBRefreshList` | `0x006C59F0` | 22 | UI-Registrierung |
| 17 | `CBDisplayTeleport` | `0x006C5230` | 308 | UI-Registrierung |
| 18 | `CBDisplaySelfTeleport` | `0x006C5370` | 238 | UI-Registrierung |
| 19 | `CBDisplayTeleportFee` | `0x006C4F50` | 151 | UI-Registrierung |
| 20 | `CBConfirmPvPZone` | `0x006C4FF0` | 49 | UI-Registrierung |
| 21 | `RefreshTeleportList` | `0x006C5460` | 260 | ver |
| 22 | `IsDisablePoint` | `0x006C5030` | 54 | ver |
| 23 | `CheckIsUsablePortalByMurdererPoint` | `0x006C5070` | 94 | ver |

24 von 24 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006C4B50`), `~AgcmUIEventTeleport` (`0x006C50D0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xC68` | `Ereignis-ID „Ladefenster schließen“` | `CBReceivedTeleportCanceled` |
| `0xC84` | `Flag „Kartenladen gestartet“ (`m_bIsStartedMapLoading`)` | `CBReceivedTeleportCanceled` |
| `0xC0C` | `Liste gesperrter Punkt-IDs (20 × 4 Byte)` | `IsDisablePoint` |
| `0xBAC` | `Zeiger auf `AgcmCharacter`` | `RefreshTeleportList` |

## Vtable

Vtable bei `0x008D504C`: Slot 0 Destruktor `0x006C50D0`, 1 `OnAddModule` (`0x006C5A70`), 2 `OnInit`-Rumpf `0x0067AC90` (leer in der Quelle), 3 `OnIdle` (`0x006C5570`), 6/7 `return TRUE`-Rumpf `0x0067AC90`.

## Callbacks (OnAddModule, 0x006C5A70)

Neun Module werden geholt (u. a. [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgpmEventTeleport`](AgpmEventTeleport.md), [`AgcmMap`](AgcmMap.md), [`AgpmSiegeWar`](AgpmSiegeWar.md)). Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgcmEventTeleport`: Teleportpunkt gewählt | `CBSelectTeleportPoint` | `0x006C5610` |
| `AgcmEventTeleport`: nicht benutzbar (Verwandlung) | `CBCannotUseForTransforming` | `0x006C4C60` |
| `AgcmEventTeleport`: nicht benutzbar (Kampfmodus) | `CBCannotUseForCombatMode` | `0x006C4C90` |
| `AgpmEventTeleport`: Teleport begonnen | `CBReceivedTeleportStart` | `0x006C4CD0` |
| `AgpmEventTeleport`: Teleport abgebrochen | `CBReceivedTeleportCanceled` | `0x006C4D10` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x006C4D50` |
| `AgcmMap`: Karte fertig geladen | `CBMapLoadEnd` | `0x006C4D10` |

Danach `AddFunctions`, `AddEvents`, `AddUserData` und `AddDisplay`. `CBReceivedTeleportCanceled` und `CBMapLoadEnd` haben in der Quelle denselben Rumpf (Ladefenster schließen, falls es offen ist) und stehen im Binary auf derselben Adresse `0x006C4D10`; das Binary meldet sie beide an.

## Teleportpunkte

`RefreshTeleportList` (`0x006C5460`) prüft für jeden Zielpunkt (bis `m_lTargetPoint`), ob er deaktiviert ist (`IsDisablePoint`, `0x006C5030`: bis zu 20 gesperrte Punkt-IDs) und wirft sonst je nach Geld und Gebühr (`AgpmEventTeleport::GetFee`) die Ereignisse „normal“ oder „zu wenig Geld“.
`CheckIsUsablePortalByMurdererPoint` (`0x006C5070`) holt den Mörder-Wert des Self-Characters: bei 40 oder 60 Punkten (Stufe 1 und 2) ist das Portal benutzbar, bei 100 (Stufe 3) nicht, bei anderen Werten benutzbar. Die drei Schwellen stimmen mit `AGPMCHAR_MURDERER_LEVEL1/2/3_POINT` der Quelle überein (40, 60, 100).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006C5A10`, `0x006C55A0`, `0x006C4C20`, `0x006C5100`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (2)

| Name | Id | Handler |
|---|---:|---|
| `Teleport` |  | `CBRequestTeleport` |
| `TeleportRefreshList` |  | `CBRefreshList` |

**Anzeige** (3)

| Name | Id | Handler |
|---|---:|---|
| `Teleport_Name` | 0 | `CBDisplayTeleport` |
| `Teleport_Self` | 0 | `CBDisplaySelfTeleport` |
| `Teleport_Fee` | 0 | `CBDisplayTeleportFee` |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `Teleport_Targets` |  | – |

**Ereignis** (9)

| Name | Id | Handler |
|---|---:|---|
| `TELEPORT_SELECT_WINDOW_CLOSE` | 0 | – |
| `need_select_teleport_point` | 0 | – |
| `TELEPORT_LOADING_WINDOW_OPEN` | 0 | – |
| `TELEPORT_LOADING_WINDOW_CLOSE` | 0 | – |
| `TELEPORT_ConfirmPvPZone` |  | `CBConfirmPvPZone` |
| `TELEPORT_NotEnoughMOney` |  | `CBConfirmPvPZone` |
| `TELEPORT_DisplayNormal` | 0 | – |
| `TELEPORT_DisplayNoMoney` | 0 | – |
| `TELEPORT_DisplayDisable` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`IsDisablePoint`, `CheckIsUsablePortalByMurdererPoint`, Registrierungsreihenfolge).

## Grenzen

- `CBSelectTeleportPoint` (984 Byte) und die Anzeige-Callbacks waren bereits zugeordnet und wurden hier nicht neu gelesen.
- `RefreshTeleportList` wurde nur nach Aufgerufenen (Ereignisse, Gebühr) und Größe zugeordnet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2, nicht als eigene Funktion: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgcmMap`](AgcmMap.md), [`AgpmEventTeleport`](AgpmEventTeleport.md), [`AgpmSiegeWar`](AgpmSiegeWar.md)
