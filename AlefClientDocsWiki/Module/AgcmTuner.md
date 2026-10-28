# AgcmTuner (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmTuner` (Leistungsabstimmung: Aktualisierungstakt für Schrift und Linsenreflex, Reichweiten-Tabellen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmTuner/AgcmTuner.cpp`/`AgcmTuner.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 4 von 5 Quellmethoden sind zugeordnet; `OnDestroy` liegt am gemeinsamen Rumpf `0x0067AC90`. `SetVariableByOption` fehlt im Binary: die Quelle ruft sie nirgends auf.
- **Abweichungen:** `OnIdle` ist im Binary nur der Takt-Teil (159 Byte); die in der Quelle auskommentierte Abstimmung nach Bildrate (LOD- und Kartenreichweite) ist nicht übersetzt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmTuner.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006925D0` | 182 | vtable/String |
| 1 | `OnInit` | `0x00692690` | 207 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `OnIdle` | `0x00692760` | 159 | vtable/String |
| 4 | `SetVariableByOption` | – | | nicht im Binary: in der Quelle ohne Aufrufer |

4 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmTuner` (`0x00692390`), `scalar_deleting_dtor` (`0x00692800`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | ``m_bStart`` | `OnIdle` |
| `this+0xB9C / 0xBA0` | ``m_uiLastTick` / `m_uiCurTickDiff`` | `OnIdle` |
| `this+0xBC4 / 0xBC8 / 0xBCC` | `Kartenreichweiten Laden / Grob / Detail` | `OnAddModule` |
| `this+0xBD0` | ``m_uiElapsedTime[10]`` | `OnIdle`, `OnInit` |
| `this+0xBF8` | ``m_uiUpdateTime[10]` (Platz 0 = 100, Platz 1 = 40)` | `OnInit`, `OnIdle` |
| `this+0xC20` | ``m_bUpdate[10]`` | `OnInit` |
| `this+0xC2C` | ``m_uiTickDiff[10]`` | `OnIdle` |
| `this+0xC5C` | ``m_bAutoTuning`` | `OnInit` |
| `this+0xC60 / 0xC64 / 0xC68` | `LOD-Typ / Karten-Ladetyp / Schatten-Typ` | `OnInit` |
| `this+0xC6C / 0xC7C / 0xC88` | `Tabellen LOD (4) / Kartenladen (4) / Schatten (3)` | `OnInit` |
| `this+0xC98..0xCB4` | `Modulzeiger: Render 0xC98, Map 0xC9C, LODManager 0xCA0, Font 0xCA4, Water 0xCA8, LensFlare 0xCAC, Shadow 0xCB0, TextBoardMng 0xCB4` | `OnAddModule` |

## Vtable und Aufbau

Vtable `0x008CDD34`: Slot 0 Löschwrapper (`0x00692800`), 1 `OnAddModule` (`0x006925D0`), 2 `OnInit` (`0x00692690`), 3 `OnIdle` (`0x00692760`), 4 und 5 `0x0067FAB0`, 6 und 7 `0x0067AC90` (Slot 7 ist `OnDestroy`: `return TRUE`), 8 und 9 `0x004E3420`, 13 bis 16 die gemeinsamen Leer-Rümpfe der [`AgcModule`](AgcModule.md)-Virtuellen. Der Konstruktor (`0x00692390`, 563 Byte) setzt Modulname `AgcmTuner`, schaltet Idle ein und nullt alle Felder und Tabellen.
`OnAddModule` (`0x006925D0`) holt [`AgcmLODManager`](AgcmLODManager.md), [`AgcmFont`](AgcmFont.md), [`AgcmLensFlare`](AgcmLensFlare.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmWater`](AgcmWater.md), [`AgcmRender`](AgcmRender.md) und [`AgcmMap`](AgcmMap.md) und setzt die Kartenreichweiten (Laden und Grob je 10, Detail 5; die Werte liegen als Gleitkommakonstanten bei `0x008983C8`, `0x00897EC0`).

## Takt und Voreinstellungen

`OnInit` (`0x00692690`) nullt für zehn Behandlungsplätze Zeitzähler, Aktualisierungsflag (auf 1) und Tick-Differenz, setzt die Aktualisierungszeiten für Platz 0 (Schrift) auf 100 und Platz 1 (Linsenreflex) auf 40 (`0x28`) und die Voreinstellungen: automatische Abstimmung aus, LOD-Typ 2, Karten-Ladetyp 2, Schatten-Typ 1, dazu die drei Tabellen (LOD, Kartenladen, Schattenentfernung; Werte als Konstanten bei `0x0089A848`, `0x0089DA68`, `0x008CDD78/7C` und `0x00897EC0`).
`OnIdle` (`0x00692760`, 159 Byte) merkt beim ersten Aufruf nur den Takt, danach addiert es die Tick-Differenz auf jeden der zehn Zeitzähler; überschreitet ein Zähler seine Aktualisierungszeit, wird die Differenz abgelegt, der Zähler zurückgesetzt und für Platz 0 das Flag `m_bUpdateThisFrame` von `AgcmFont` (`+0x1B80`), für Platz 1 das von `AgcmLensFlare` (`+0xE28`) gesetzt. Die Quelle (161 Zeilen) enthält dazu auskommentierte Abstimmungslogik, die im Binary fehlt.

## Abweichungen von der EP8-Quelle

- `OnIdle` enthält im Binary nur den Takt-Teil; die automatische Abstimmung der Quelle ist (auskommentiert) nicht übersetzt.

## Grenzen

- Die Tabellenwerte (0,5/1/2/99 für LOD; 2/5/7/10 für Kartenladen; 1/0,5/0 für Schatten) stammen aus der Quelle; im Binary liegen sie als Gleitkommakonstanten an den genannten Adressen und wurden nicht einzeln ausgelesen.
- `OnDestroy` ist über Vtable-Slot 7 und die Form (`return TRUE`) zugeordnet, nicht über einen Aufrufer.
- Die Zuordnung der Zählerplätze 0 und 1 zu Schrift und Linsenreflex folgt aus den Flags `+0x1B80` und `+0xE28`, deren Namen (`m_bUpdateThisFrame`) aus der Quelle stammen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcModule`](AgcModule.md), [`AgcmFont`](AgcmFont.md), [`AgcmLODManager`](AgcmLODManager.md), [`AgcmLensFlare`](AgcmLensFlare.md), [`AgcmMap`](AgcmMap.md), [`AgcmRender`](AgcmRender.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmWater`](AgcmWater.md)
