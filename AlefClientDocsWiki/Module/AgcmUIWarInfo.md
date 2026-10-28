# AgcmUIWarInfo (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIWarInfo` (Anzeige der Kriegsinformation: Schritt, Mitte, Zeit und PvP-Zähler) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIWarInfo/AgcmUIWarInfo.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 18 von 20 Quellmethoden sind einer Adresse zugeordnet (`OnDestroy`, `OnInit`, `OnIdle` als gemeinsame Rümpfe); neu sind `AddUserData`, `AddDisplay`, `OpenWarInfo`, `CloseWarInfo`, `SetPvPInfo`, `SetFactor` und `UpdateTimeStep`.
- **Nicht im Binary:** `SetStepMessage` und `UpdateCenterMessage` (STL-Karten mit Nachrichten) haben keine Adresse; die Textfelder `Schritt` und `Mitte` werden damit in diesem Client nicht über dieses Modul gefüllt.
- **UI:** 3 Funktionen, 4 Anzeigen, 4 Benutzerdaten, 5 Ereignisse – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIWarInfo.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0068B990` | 104 | vtable/String |
| 1 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf (Vtable-Slot 3)` (vom Linker zusammengefaltet) |
| 4 | `AddEvent` | `0x0068B3A0` | 164 | Zeichenkette |
| 5 | `AddFunction` | `0x0068B850` | 134 | Zeichenkette |
| 6 | `AddDisplay` | `0x0068B8E0` | 131 | manual |
| 7 | `AddUserData` | `0x0068B450` | 170 | manual |
| 8 | `OpenWarInfo` | `0x0068B500` | 116 | manual |
| 9 | `CloseWarInfo` | `0x0068B580` | 40 | manual |
| 10 | `SetStepMessage` | – | | im Binary nicht vorhanden (vermutlich entfernt, da nirgends aufgerufen) |
| 11 | `UpdateCenterMessage` | – | | im Binary nicht vorhanden (vermutlich entfernt, da nirgends aufgerufen) |
| 12 | `CBGetTimeEditControl` | `0x0068B5B0` | 46 | UI-Registrierung |
| 13 | `CBGetStepMessageEditControl` | `0x0068B5E0` | 68 | UI-Registrierung |
| 14 | `CBGetCenterMessageEditControl` | `0x0068B630` | 56 | UI-Registrierung |
| 15 | `UpdateTimeStep` | `0x0068B970` | 18 | manual |
| 16 | `SetTimeStep` | `0x0068B670` | 135 | Zeichenkette |
| 17 | `CBDisplayPvPInfo` | `0x0068B700` | 57 | UI-Registrierung |
| 18 | `SetPvPInfo` | `0x0068B740` | 127 | manual |
| 19 | `SetFactor` | `0x0068B7C0` | 95 | manual |

18 von 20 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x0068B300`), `~AgcmUIWarInfo` (`0x0068B820`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98 / 0xB9C` | `Zeiger auf [`AgcmUIManager2`](AgcmUIManager2.md) / Fenster `UI_WarInfo`` | `OnAddModule` |
| `0xBA0…0xBB0` | `Ereignis-IDs (Öffnen, Schließen, drei Textfeld-Ereignisse)` | `OpenWarInfo`, `CloseWarInfo` |
| `0xBC0…0xBCC` | `vier Benutzerdaten für die Zähler` | `AddUserData`, `SetPvPInfo` |
| `0xBD0…0xBDC` | `Zähler (Charakter-Siege / -Niederlagen / Rassen-Siege / -Niederlagen)` | `SetPvPInfo` |
| `0xBE0 / 0xC01 / 0xC22` | `drei Zeichenketten (`m_szFactor1…3`)` | `SetFactor` |
| `0xC44` | `Flag „Fenster offen“` | `OpenWarInfo`, `CloseWarInfo` |

## Vtable

Vtable bei `0x008CC6BC`: Slot 0 Destruktor `0x0068B820`, 1 `OnAddModule` (`0x0068B990`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`, `OnDestroy`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (u. a. `OnIdle`).

## Registrierung (OnAddModule, 0x0068B990)

Holt nur `AgcmUIManager2` (Pflicht) und ruft `AddEvent` (`0x0068B3A0`), `AddFunction` (`0x0068B850`), `AddUserData` (`0x0068B450`) und `AddDisplay` (`0x0068B8E0`); danach sucht es das Fenster `UI_WarInfo` (`GetUI`, `0x005E19F0`) und bricht ab, wenn es fehlt. Es gibt keine Modul-Callbacks: Die Daten setzt das Modul [`AgcmWarInfo`](AgcmWarInfo.md) (Kriegsinformation), das `OpenWarInfo`, `CloseWarInfo`, `SetPvPInfo`, `SetFactor` und `UpdateTimeStep` aufruft.

## Registrierte Namen

Fünf Ereignisse (`WarInfoUIOpen`, `WarInfoUIClose`, `WarInfoGetStepMessageEditControl`, `WarInfoGetCenterMessageEditControl`, `WarInfoGetTimeEditControl`), drei Funktionen, mit denen das Fenster dem Modul seine Textfelder übergibt (`WarInfoGet…EditControl`, jeweils mit Beschreibungstext), vier Zähler (`Character_Win_Count`, `Character_Lose_Count`, `Race_Win_Count`, `Race_Lose_Count` – je als Benutzerdatum und als Anzeige mit den IDs 0…3 über `CBDisplayPvPInfo`).

## Öffnen, Zähler, Zeit

`OpenWarInfo` (`0x0068B500`) setzt das Flag „offen“ (`+0xC44`) und wirft die vier Ereignisse Öffnen, Schritt-, Mitten- und Zeit-Textfeld holen; `CloseWarInfo` (`0x0068B580`) löscht das Flag und wirft „Schließen“.
`SetPvPInfo` (`0x0068B740`) speichert die vier Zähler (Charakter-Siege, -Niederlagen, Rassen-Siege, -Niederlagen) und aktualisiert die vier Benutzerdaten; `CBDisplayPvPInfo` schreibt die Zahl als Text. `SetFactor` (`0x0068B7C0`) kopiert drei Zeichenketten zu je 32 Zeichen (`MAX_WARINFO_FACTOR_LENGTH`) nach `+0xBE0`, `+0xC01` und `+0xC22`, wenn alle drei vorhanden sind.
`SetTimeStep` (`0x0068B670`) schreibt „`<Zahl> <UiMsg_WarInfo_Min>`“ in das Zeitfeld; `UpdateTimeStep` (`0x0068B970`) ruft nur `SetTimeStep`. Die drei `CBGet…EditControl` (`0x0068B5B0`, `0x0068B5E0`, `0x0068B630`) merken das Textfeld; das Schrittfeld wird zusätzlich ohne Maus-Scrolling, aber scrollbar eingerichtet, das Mittenfeld nur scrollbar.

## Aufrufer

`AgcmWarInfo::CBOperationUpdateTimeStep` (`0x0068A8B0`) öffnet das Fenster und setzt die Zeit, `…UpdateFactor` (`0x0068A910`) setzt die Zeichenketten, `…UpdateCharacterPvPInfo` / `…UpdateRacePvPInfo` (`0x0068AA20`, `0x0068AA90`) die Zähler; `AgcmWarInfo::OnIdle` (`0x0068A860`) setzt die Zähler nach 30 Zeiteinheiten (`+0x1E`) auf 0 und schließt das Fenster.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x0068B3A0`, `0x0068B850`, `0x0068B450`, `0x0068B8E0`, `0x0068B990`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Ereignis** (5)

| Name | Id | Handler |
|---|---:|---|
| `WarInfoUIOpen` | 0 | – |
| `WarInfoUIClose` | 0 | – |
| `WarInfoGetStepMessageEditControl` | 0 | – |
| `WarInfoGetCenterMessageEditControl` | 0 | – |
| `WarInfoGetTimeEditControl` | 0 | – |

**Funktion** (3)

| Name | Id | Handler |
|---|---:|---|
| `WarInfoGetStepMessageEditControl` |  | `CBGetStepMessageEditControl` |
| `WarInfoGetCenterMessageEditControl` |  | `CBGetCenterMessageEditControl` |
| `WarInfoGetTimeEditControl` |  | `CBGetTimeEditControl` |

**UserData** (4)

| Name | Id | Handler |
|---|---:|---|
| `Character_Win_Count` |  | – |
| `Character_Lose_Count` |  | – |
| `Race_Win_Count` |  | – |
| `Race_Lose_Count` |  | – |

**Anzeige** (4)

| Name | Id | Handler |
|---|---:|---|
| `Character_Win_Count` | 0 | `CBDisplayPvPInfo` |
| `Character_Lose_Count` | 1 | `CBDisplayPvPInfo` |
| `Race_Win_Count` | 2 | `CBDisplayPvPInfo` |
| `Race_Lose_Count` | 3 | `CBDisplayPvPInfo` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den vorhandenen Funktionen (Registrierung, `OpenWarInfo`, `SetPvPInfo`, `SetFactor`, `SetTimeStep`, `CBDisplayPvPInfo`).

## Grenzen

- Dass `SetStepMessage` und `UpdateCenterMessage` entfernt wurden, folgt daraus, dass im Modulbereich keine Funktion mit den Zeichenketten `<\n>` oder dem Aufruf `SetLookLine` liegt; das wurde nicht im gesamten Binary gesucht.
- Die Aufrufer in `AgcmWarInfo` wurden nur für die Zuordnung der Parameter gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 3, ohne Kandidat: 1, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `UpdateCenterMessage` | 33 | `0x0068BB20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmWarInfo`](AgcmWarInfo.md)
- **Erwähnt in:** [`AgcmWarInfo`](AgcmWarInfo.md)
