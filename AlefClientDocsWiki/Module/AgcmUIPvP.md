# AgcmUIPvP (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIPvP` (PvP-Gebietsanzeige, PvP-Systemmeldungen und Rassenkampf-Einblendung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIPvP/AgcmUIPvP.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 18 von 18 Quellmethoden sind zugeordnet; neu sind `InitBattleInfo`, `DrawBattleInfoResult`, `DrawBattleInfoTime`, `DrawBattleInfoScore` und `OnRaceBattleStatus`.
- **Systemmeldungen:** 29 Codes, Reihenfolge und Farben wie in der Quelle; „Ziel unverwundbar“ wird nur einmal in Folge gezeigt.
- **Rassenkampf:** Status 1/2/3 steuern Zeit, Punkte und Ergebnis; alle Positionen, Farben und Zeiten stimmen mit der Quelle überein.
- **Hinweis:** `OnIdle` ist durch `EnableIdle(FALSE)` im Konstruktor abgeschaltet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIPvP.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006A83A0` | 825 | vtable/String |
| 1 | `OnInit` | `0x006A75D0` | 11 | vtable/String |
| 2 | `OnDestroy` | `0x006A75E0` | 84 | vtable/String |
| 3 | `OnIdle` | `0x006A8330` | 51 | vtable/String |
| 4 | `CBChangeRegionIndex` | `0x006A6DF0` | 593 | Callback-Registrierung |
| 5 | `CBUpdateExp` | `0x006A7050` | 156 | Callback-Registrierung |
| 6 | `CBRecvCannotUseTeleport` | `0x006A70F0` | 63 | Callback-Registrierung |
| 7 | `CBEnterSafeArea` | `0x006A7130` | 63 | Callback-Registrierung |
| 8 | `CBEnterFreeArea` | `0x006A7170` | 63 | Callback-Registrierung |
| 9 | `CBEnterCombatArea` | `0x006A71B0` | 63 | Callback-Registrierung |
| 10 | `CBUpdateResurrectStatus` | `0x006A71F0` | 54 | Callback-Registrierung |
| 11 | `CBRaceBattleStatus` | `0x006A8370` | 35 | Callback-Registrierung |
| 12 | `OnRaceBattleStatus` | `0x006A82B0` | 118 | manual |
| 13 | `InitBattleInfo` | `0x006A7230` | 401 | manual |
| 14 | `DrawBattleInfoResult` | `0x006A73D0` | 235 | manual |
| 15 | `DrawBattleInfoTime` | `0x006A74D0` | 201 | manual |
| 16 | `DrawBattleInfoScore` | `0x006A7640` | 517 | manual |
| 17 | `CBSystemMessage` | `0x006A7850` | 2526 | Callback-Registrierung |

18 von 18 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIPvP` (`0x006A6D20`), `~AgcmUIPvP` (`0x006A75A0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBA4…0xBC4` | `Modulzeiger ([`AgpmGrid`](AgpmGrid.md) +0xBA4, [`AgpmItem`](AgpmItem.md) +0xBA8, [`AgpmPvP`](AgpmPvP.md) +0xBAC, `AgcmCharacter` +0xBB0, [`AgcmWorld`](AgcmWorld.md) +0xBB4, [`AgcmUIControl`](AgcmUIControl.md) +0xBB8, [`AgcmUIManager2`](AgcmUIManager2.md) +0xBBC, [`AgcmUIMain`](AgcmUIMain.md) +0xBC0, [`AgcmUICharacter`](AgcmUICharacter.md) +0xBC4)` | `OnAddModule` |
| `0xB98 / 0xB9C / 0xBA0` | `Zeiger auf [`ApmMap`](ApmMap.md) / [`AgpmFactors`](AgpmFactors.md) / [`AgpmCharacter`](AgpmCharacter.md)` | `OnAddModule` |
| `0xBC8 / 0xBCC` | `Gitter-Symbol PvP-frei / Gefahrengebiet (`new`, in `OnDestroy` gelöscht)` | `CBChangeRegionIndex`, `OnDestroy` |
| `0xBD0 / 0xBD4` | `Ergebnis von `AddSystemMessageGridItem` (Symbol angezeigt)` | `CBChangeRegionIndex` |
| `0xBD8…0xBF4` | `Ereignis-IDs (Teleport, Sicher, Frei, Gefahr, Start, Ende)` | `OnAddModule` |
| `0xBDC / 0xBE0` | `Benutzerdatum und Wert `IsDisableInPvPDanger`` | `OnAddModule` |
| `0xBF8` | `Flag „im Gefahrengebiet“` | `CBChangeRegionIndex` |
| `0xC08 / 0xC0C` | `Restzeit des Rassenkampfs (ms) / letzte Idle-Zeit` | `OnIdle`, `OnRaceBattleStatus` |
| `0x00C23BEC` | `statisch: voriger Systemmeldungs-Code (`m_lPrevCode`)` | `CBSystemMessage` |

## Vtable

Vtable bei `0x008CFBDC`: Slot 0 Destruktor `0x006A75A0`, 1 `OnAddModule` (`0x006A83A0`), 2 `OnInit` (`0x006A75D0`), 3 `OnIdle` (`0x006A8330`), 6 der gemeinsame `return TRUE`-Rumpf `0x0067AC90`, 7 `OnDestroy` (`0x006A75E0`).

## Registrierung (OnAddModule, 0x006A83A0)

Holt zwölf Module (`ApmMap`, `AgpmFactors`, `AgpmCharacter`, `AgcmCharacter`, `AgcmWorld`, `AgcmUIControl`, `AgcmUIManager2`, `AgcmUIMain`, `AgcmUICharacter`, `AgpmItem`, `AgpmPvP`, `AgpmGrid`) und bricht ab, wenn eines der elf Pflichtmodule fehlt (`AgpmGrid` ist optional). Danach neun Callbacks in der Reihenfolge der Quelle:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmCharacter`: Regionswechsel | `CBChangeRegionIndex` | `0x006A6DF0` |
| `AgpmFactors`: Faktor-UI aktualisiert | `CBUpdateExp` | `0x006A7050` |
| `AgpmPvP`: Teleport gesperrt | `CBRecvCannotUseTeleport` | `0x006A70F0` |
| `AgpmPvP`: sicheres Gebiet betreten | `CBEnterSafeArea` | `0x006A7130` |
| `AgpmPvP`: PvP-freies Gebiet betreten | `CBEnterFreeArea` | `0x006A7170` |
| `AgpmPvP`: Kampfgebiet betreten | `CBEnterCombatArea` | `0x006A71B0` |
| `AgpmPvP`: Systemmeldung | `CBSystemMessage` | `0x006A7850` |
| `AgpmPvP`: Rassenkampf-Status | `CBRaceBattleStatus` | `0x006A8370` |
| `AgcmUICharacter`: Wiederbelebungs-Status | `CBUpdateResurrectStatus` | `0x006A71F0` |

Danach sechs Ereignisse (`PvP_RecvCannotUseTeleport`, `PvP_RegionSafe`, `PvP_RegionPvPFree`, `PvP_RegionPvPDanger`, `PvP_PvPStart`, `PvP_PvPEnd`) und das Benutzerdatum `IsDisableInPvPDanger` (Typ Bool, 4 Byte).

## Gebietswechsel (CBChangeRegionIndex, 0x006A6DF0)

Nur für den eigenen Charakter. Aus der Region des Charakters liest die Funktion die Sicherheitsart (zwei Bit im Regions-Template, Wert 1 = PvP-frei, 2 = Gefahrengebiet). In einem PvP-freien Gebiet entsteht einmalig ein Gitter-Symbol (`m_pPvPFree` aus `AgcmUIControl`) mit dem Tooltip `STI_ALARM_FREEAREA` (UI-Text `0x29D`), wird als Systemmeldungs-Symbol angezeigt und das Ereignis `PvP_RegionPvPFree` geworfen. Im Gefahrengebiet gilt dasselbe mit `m_pPvPDanger`, Text `0x29E` und Ereignis `PvP_RegionPvPDanger`; zusätzlich werden das Flag „im Gefahrengebiet“ (`+0xBF8`) gesetzt und `IsDisableInPvPDanger` auf 0 gesetzt. In allen anderen Gebieten werden die Symbole entfernt und `PvP_RegionSafe` geworfen.
Der Tooltip kommt im Binary aus der Stringtabelle (`ClientStr`); die Quelle hat dafür den `_AREA_GLOBAL_`-Zweig, die Textvariante `"Free Area"` / `"Danger Area"` (ohne `_AREA_GLOBAL_`) ist im Binary nicht enthalten. Das passt zu den anderen Berichten (2017er Build = Global-Variante).

## Systemmeldungen (CBSystemMessage, 0x006A7850)

Die Funktion (2526 Byte) verzweigt über 29 Codes des Pakets `AgpdPvPSystemMessage` (Code in Feld 0; Zahlenfolge wie `eAGPMPVP_SYSTEM_CODE`: 0 sicheres Gebiet … 0x1C Mörder-Strafe). Farben wie in der Quelle: Gebietsmeldungen orange `0xFFFF9900`, Todes-/Verbots-/Sperrmeldungen dunkelrot `0xFFCC0000`, Hinweise türkis `0xFF00CC99`, Charisma `0xFFFFCC00`, Standard gelb `0xFFFFFF00`.
Die Meldungstexte kommen aus `AgcmUIManager2::GetUIMessage` (`0x005E6600`) mit Namen wie `PvP_Msg_EnterSafeArea`, `PvP_Msg_EnterFreeArea` (bis `_3`/`_4`), `PvP_Msg_EnterCombatArea` (bis `_6`), `PvP_Msg_CannotInviteGuild`, `PvP_Msg_TargetInvincible` und `PvP_Msg_NotEnoughLevel`; ausgegeben wird mit `0x0057C210` (Systemmeldung).
„Ziel unverwundbar“ (Code 0x11) wird nur einmal hintereinander ausgegeben: Der vorige Code steht in einer statischen Variable (`0x00C23BEC`, `m_lPrevCode`); bei Wiederholung liefert die Funktion 0. Der Name des Ziels wird durch `****` ersetzt, wenn es in einem Schlachtfeld oder Schrein-Kampf ist (Binary: `0x00569400`/`0x0056A950`, Zeichenkette bei `0x008CFCFC`).
Konstanten im Binary: Unverwundbarkeit 30 s (`AGPMPVP_INVINCIBLE_TIME` 30 000 ms, `/1000` = `0x1E`) für „Schutz beginnt“, Mindeststufe 10 (`AGPMPVP_BATTLE_SQAURE_REQUIRE_LEVEL`) für „zu niedrige Stufe“. Bei den Gebietsmeldungen entfallen die Zusatzzeilen (`…_3`/`…_4` im PvP-freien, `…_2`/`…_3` im Kampfgebiet) für die Welt „NC17“.

## Rassenkampf-Anzeige

`OnRaceBattleStatus` (`0x006A82B0`, Quelle `OnRaceBattleStatus(lRemained)`): Ist die Restzeit nicht −1, wird sie in Millisekunden gespeichert (`× 1000`, `+0xC08`). Danach nach Status: 1 (bereit) zeigt die Zeit, 2 (läuft) Zeit und Punktestand, 3 (beendet) setzt den Status auf 4 (Belohnung) und zeigt das Ergebnis. Die Aufrufer: `CBRaceBattleStatus` (`0x006A8370`, liest die Restzeit aus dem dritten Parameter) und `OnIdle`.
`DrawBattleInfoTime` (`0x006A74D0`): Text `0x28B` mit Minuten und Sekunden, Schrift 3, X 5, Y 230, Farbe `0xFFFF6600`, Skalierung 1,05, Dauer `0x7FFFFFFF` (dauerhaft). `DrawBattleInfoScore` (`0x006A7640`): drei Zeilen „Rasse:Punkte“ bei X 10 und Y 300 / 345 / 390 (Abstand 45), die eigene Rasse grün `0xFF00FF00`, die beiden anderen rot `0xFFFF0000`, jeweils der nächste Rassencode modulo 5 ohne 0. Die Rassennamen sind die UI-Texte `0x28C`–`0x28E` und `0x305` (Mensch, Ork, Mondelf, Drachling). `DrawBattleInfoResult` (`0x006A73D0`): Siegerrasse mit Text `0x28F`, Y 230, Farbe `0xFFFF6600`, Dauer 5000 ms; ohne bekannte Rasse bricht die Funktion mit 0 ab. Alle Konstanten stimmen mit der Quelle überein.
`InitBattleInfo` (`0x006A7230`, aus `OnInit`) leert die sieben Kampf-Texteffekte von `AgcmUIManager2` (Fenster 1: Haupt-, Ober- und Untertext; Fenster 2–7: Untertext; Abstand 0x1E34 Byte zwischen den Fenstern; bei 2–7 ist der letzte Parameter der Standardwert 500).

## OnIdle (0x006A8330)

`OnIdle` zieht alle 500 ms (`AGCMUIPVP_IDLE_CLOCK_INTERVAL`) 500 ms von der Restzeit ab und ruft `OnRaceBattleStatus(-1)`. Im Konstruktor wird jedoch `EnableIdle(FALSE)` aufgerufen (`0x004E45D0(0)`), die Funktion läuft also in diesem Build nie; die Restzeit wird nur durch Serverpakete gesetzt. Die Quellprüfung `0 > m_ulRaceBattleRemainedTime` (vorzeichenlos, immer falsch) ist im Binary entfallen.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006A83A0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Ereignis** (6)

| Name | Id | Handler |
|---|---:|---|
| `PvP_RecvCannotUseTeleport` | 0 | – |
| `PvP_RegionSafe` | 0 | – |
| `PvP_RegionPvPFree` | 0 | – |
| `PvP_RegionPvPDanger` | 0 | – |
| `PvP_PvPStart` | 0 | – |
| `PvP_PvPEnd` | 0 | – |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `IsDisableInPvPDanger` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierungsreihenfolge, `CBChangeRegionIndex`, die vier `DrawBattleInfo…`-Funktionen, `OnRaceBattleStatus`, `OnIdle`, die Verzweigungen von `CBSystemMessage`).

## Grenzen

- `CBSystemMessage` (2526 Byte) wurde über die Verzweigungsfolge, die Farben, die Textnamen und die Sonderfälle (0x09, 0x11, 0x12, 0x18, 0x1C) gelesen; die Formatargumente der übrigen Meldungen (Namen, Zahlen) wurden nicht einzeln verglichen.
- Die Hilfsaufrufe in `OnAddModule` (z. B. `0x005033C0` für `SetCallbackBindingRegionChange`) wurden hier nicht umbenannt; sie gehören zu den Modulen `AgpmCharacter`, `AgpmPvP` und `AgcmUICharacter`.
- Die Zuordnung der Bit-Werte der Sicherheitsart (1 = PvP-frei, 2 = Gefahrengebiet) stützt sich auf die Reihenfolge der Zweige und die Tooltip-Texte, nicht auf die Definition des Regions-Templates.

## Querverweise

- **Erwähnt Module:** [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmWorld`](AgcmWorld.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgpmPvP`](AgpmPvP.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md)
