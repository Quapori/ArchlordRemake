# AgcmOcTree (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmOcTree` (Octree für Sichtbarkeit: Wurzeln, Knoten, Clumps, Zeichendaten) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Aufrufer in anderen Modulen, EP8-Quelle `Modules/AClient/AgcmOcTree/AgcmOcTree.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, die Rückrufe für Wurzel- und Knotendaten, die vier Quadtree-Funktionen und die beiden Fassungen von `Add`/`RemoveCustomRenderDataFromOcTree`. Nicht zugeordnet sind `AddClumpToOcTree`, `RemoveClumpFromOcTree`, `TestClumpOctrees`, `TestAtomicOctreesByClump`, die Zeichenfunktionen (`DrawDebugBoxes`, `DrawQuadNodes`, `DrawOcTreeNodes`), die `OcTreesForAllAtomicsIntersection…`-Familie und `LineGetIntersectionSectors`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmOcTree.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 1 | `OnAddModule` | `0x006FC8A0` | 150 | vtable/String |
| 2 | `OnIdle` | `0x006FB330` | 18 | vtable/String |
| 3 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 4 | `CBInitRootData` | `0x006FC210` | 463 | Callback-Registrierung |
| 5 | `CBRemoveRootData` | `0x006FC3E0` | 115 | Callback-Registrierung |
| 6 | `CBInitNodeData` | `0x006FB350` | 47 | Callback-Registrierung |
| 7 | `CBRemoveNodeData` | `0x006FB380` | 112 | Callback-Registrierung |
| 8 | `DivideRootQuadTree` | `0x006FB3F0` | 505 | von Hand geprüft |
| 9 | `RemoveRootQuadTree` | `0x006FB5F0` | 62 | von Hand geprüft |
| 10 | `CreateRootByTerrain` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `GetQuadNodes` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `SetAllQuadY` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 13 | `SetAllQuadY` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `TestClumpOctrees` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `CallBackSetOcTreeIDs` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `TestAtomicOctreesByClump` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `DivideToLeafTree` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `CBSaveRootData` | `0x006FC460` | 83 | Callback-Registrierung |
| 19 | `CBLoadRootData` | `0x006FC4C0` | 78 | Callback-Registrierung |
| 20 | `SaveQuadTreeBoxes` | `0x006FB630` | 247 | von Hand geprüft |
| 21 | `LoadQuadTreeBoxes` | `0x006FB730` | 213 | von Hand geprüft |
| 22 | `AddClumpToOcTree` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `RemoveClumpFromOcTree` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `AddCustomRenderDataToOcTree` | `0x006FC510` | 166 | von Hand geprüft |
| 25 | `AddCustomRenderDataToOcTree` | `0x006FB8C0` | 348 | von Hand geprüft |
| 26 | `RemoveCustomRenderDataFromOcTree` | `0x006FCAC0` | 530 | von Hand geprüft |
| 27 | `RemoveCustomRenderDataFromOcTree` | `0x006FCCE0` | 350 | von Hand geprüft |
| 28 | `SetClumpAndDrawStart` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `SetDrawEnd` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `DrawDebugBoxes` | – | | Debug-Zeichnen, im Binary nicht gefunden |
| 31 | `DrawQuadNodes` | – | | Debug-Zeichnen, im Binary nicht gefunden |
| 32 | `DrawOcTreeNodes` | – | | Debug-Zeichnen, im Binary nicht gefunden |
| 33 | `OcTreeForAllClumps` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `NodeForAllClumps` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 35 | `SetWorldIntersectionCallBack` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 36 | `OcTreeChildCheck` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 37 | `OneOcTreeForAllAtomicsIntersection` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 38 | `OcTreesForAllAtomicsIntersection` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 39 | `OcTreesForAllAtomicsIntersection2` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 40 | `OcTreesForAllAtomicsIntersection3` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 41 | `OcTreesForAllAtomicsIntersection4` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 42 | `OcTreesForAllAtomicsIntersection5` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `LineGetIntersectionSectors` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

18 von 44 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006FB270`), `~AgcmOcTree` (`0x006FC1E0`).

## Vtable

Die Slots laut `vtables.tsv`: 0 Destruktor `0x006FC1E0`, 1 `OnAddModule` (`0x006FC8A0`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`), 3 `OnIdle` (`0x006FB330`, 18 Byte), 4 und 5 gemeinsamer Rumpf `0x0067FAB0`, 6 und 7 `0x0067AC90` (`OnDestroy` = `return TRUE`).

## OnAddModule (0x006FC8A0)

Holt [`ApmOcTree`](ApmOcTree.md) und [`ApmMap`](ApmMap.md) und hängt über `ApmOcTree` je einen Datenblock an Wurzeln (`CBRemoveRootData` `0x006FC3E0`) und Knoten (`CBInitNodeData` `0x006FB350`, `CBRemoveNodeData` `0x006FB380`) an (Aufrufe `0x00588B60`/`0x00588B30`), meldet danach `CBSaveRootData` (`0x006FC460`), `CBLoadRootData` (`0x006FC4C0`) und `CBInitRootData` (`0x006FC210`) an. Die Reihenfolge entspricht der Quelle.

## Wurzelbäume

`CBInitRootData` (`0x006FC210`, 463 Byte) ruft `DivideRootQuadTree` (`0x006FB3F0`, 505 Byte, rekursiv); `CBRemoveRootData` ruft `RemoveRootQuadTree` (`0x006FB5F0`); `CBSaveRootData` ruft `SaveQuadTreeBoxes` (`0x006FB630`, rekursiv, schreibt Boxen), `CBLoadRootData` ruft `LoadQuadTreeBoxes` (`0x006FB730`). Diese vier Funktionen sind über den Aufrufgraphen eindeutig.

## Eigene Zeichendaten im Octree

`AddCustomRenderDataToOcTree` gibt es in zwei Fassungen: mit Kennung (`0x006FB8C0`, 348 Byte, vom Gras-Modul gerufen) und mit Position (`0x006FC510`, 166 Byte, von [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md):addLight` gerufen). `RemoveCustomRenderDataFromOcTree` ebenfalls: mit Position (`0x006FCAC0`, 530 Byte, CCSLog-Nummer 3001, von `AgcmDynamicLightmap::removeLight`/`clearLights`, vom Wasser-Modul und von [`AgcmRender`](AgcmRender.md) gerufen) und mit Kennung (`0x006FCCE0`, 350 Byte, CCSLog-Nummer 3002, vom Gras-Modul gerufen). Die Namen `CCSLog::ctor_or_dtor_…` waren falsch: die beiden Funktionen legen lediglich ein `CCSLog`-Objekt (3001/3002) an.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der vier `…CustomRenderData…`-Funktionen folgt den Aufrufern (Gras: Kennung; Licht: Position), den `CCSLog`-Nummern 3001/3002 aus der Quelle und der Quellreihenfolge Position vor Kennung; die Funktionsrümpfe wurden nicht Zeile für Zeile verglichen.
- `AddClumpToOcTree` und `RemoveClumpFromOcTree` liegen vermutlich bei `0x006FC630` (360 Byte, von `AgcmRender` gerufen) und `0x006FC7B0` (229 Byte), welche Funktion welche ist, ließ sich nicht trennen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, gemeinsamer Rumpf: 2, nicht im Client: 10, ohne Kandidat: 9, zugeordnet: 7.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `OcTreeChildCheck` | 51 | `0x006FBB00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OcTreeForAllClumps` | 20 | `0x006FC5C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddClumpToOcTree` | 91 | `0x006FC940` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LineGetIntersectionSectors` | 150 | `0x006FBD40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OcTreesForAllAtomicsIntersection2` | 47 | `0x006FC7B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OcTreesForAllAtomicsIntersection` | 57 | `0x006FC630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OneOcTreeForAllAtomicsIntersection` | 45 | `0x006FBC30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmRender`](AgcmRender.md), [`ApmMap`](ApmMap.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmMap`](AgcmMap.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmTargeting`](AgcmTargeting.md), [`ApmOcTree`](ApmOcTree.md)
