# ApmOcTree (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `ApmOcTree` (Octree der Welt für Sichtbarkeit und Gras: Sektorwurzeln, Knoten, Laden aus Dateien) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/APublic/ApmOcTree/ApmOcTree.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten. Zugeordnet sind Registrierung, Lade- und Entladepfad, Knoten- und Wurzelverwaltung und die Abfragen `GetNodeForInsert`/`GetLeafID`. Eingebaut sind `GetStartNode(Knoten)`, `GetStartNode(Wurzel, Index)` und `GetNodeID`.
- **Nicht im Binary:** `SaveToFiles`/`SaveNode` und `DivideAllTree`/`DivideAllChilds` (nur von Editor-Funktionen gerufen – [`AgcmRender`](AgcmRender.md):SaveAllOctrees`, [`AgcmOcTree`](AgcmOcTree.md):DivideToLeafTree` –, die selbst keinen Aufrufer haben), `CombineNodeChilds`, `OptimizeTree`/`OptimizeChild`, `GetNode(AuPOS*)` und `GetNode(Knoten, AuPOS*)` (in der Quelle ohne Aufrufer) sowie die auskommentierte zweite Fassung von `LoadFromFiles`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApmOcTree.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00588450` | 48 | vtable/String |
| 1 | `OnInit` | `0x005898E0` | 210 | vtable/String |
| 2 | `DestroyAll` | `0x005899C0` | 60 | von Hand geprüft |
| 3 | `OnDestroy` | `0x00589A00` | 54 | vtable/String |
| 4 | `DestroyTree` | `0x00588D20` | 191 | von Hand geprüft |
| 5 | `DestroyChilds` | `0x00588480` | 56 | von Hand geprüft |
| 6 | `GetRoot` | `0x005884C0` | 46 | von Hand geprüft |
| 7 | `SetRoot` | `0x005884F0` | 67 | von Hand geprüft |
| 8 | `GetRootByWorldPos` | `0x00589A40` | 114 | von Hand geprüft |
| 9 | `GetNode` | `0x00588DF0` | 52 | von Hand geprüft |
| 10 | `GetNode` | `0x00588540` | 76 | von Hand geprüft |
| 11 | `GetStartNode` | `0x00588E30` | 428 | von Hand geprüft |
| 12 | `GetStartNode` | – | | eingebaut (kleine Fassungen mit Knoten bzw. Wurzel und Index) |
| 13 | `GetStartNode` | – | | eingebaut (kleine Fassungen mit Knoten bzw. Wurzel und Index) |
| 14 | `GetNodeID` | – | | eingebaut (drei Zeilen) |
| 15 | `TestBoxPos` | `0x00588590` | 129 | von Hand geprüft |
| 16 | `DivideNode` | `0x00588FE0` | 61 | von Hand geprüft |
| 17 | `CombineNodeChilds` | – | | nicht im Binary: nur rekursiv gerufen, sonst ohne Aufrufer |
| 18 | `MakeChild` | `0x00588620` | 386 | von Hand geprüft |
| 19 | `CreateRoot` | `0x005887D0` | 853 | von Hand geprüft |
| 20 | `AttachOcTreeNodeData` | `0x00588B30` | 33 | von Hand geprüft |
| 21 | `AttachOcTreeRootData` | `0x00588B60` | 33 | von Hand geprüft |
| 22 | `SetCallbackInitRoot` | `0x006DA540` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf mit Kennung 0 (Aufrufer `AgcmOcTree::OnAddModule`)` (vom Linker zusammengefaltet) |
| 23 | `DivideAllTree` | – | | nicht im Binary: einziger Aufrufer (`AgcmOcTree::DivideToLeafTree`) hat selbst keinen Aufrufer |
| 24 | `DivideAllChilds` | – | | nicht im Binary: nur von `DivideAllTree` gerufen |
| 25 | `GetNode` | – | | nicht im Binary: Fassungen mit `AuPOS*` in der Quelle ohne Aufrufer |
| 26 | `GetNode` | – | | nicht im Binary: Fassungen mit `AuPOS*` in der Quelle ohne Aufrufer |
| 27 | `GetNodeForInsert` | `0x00589020` | 219 | von Hand geprüft |
| 28 | `OptimizeTree` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 29 | `OptimizeChild` | – | | nicht im Binary: nur von `OptimizeTree` gerufen |
| 30 | `GetLeafID` | `0x00589110` | 605 | von Hand geprüft |
| 31 | `SaveToFiles` | – | | nicht im Binary: einziger Aufrufer (`AgcmRender::SaveAllOctrees`) hat selbst keinen Aufrufer |
| 32 | `SaveNode` | – | | nicht im Binary: nur von `SaveToFiles` gerufen |
| 33 | `LoadFromFiles` | `0x00589370` | 1086 | von Hand geprüft |
| 34 | `LoadNode` | `0x00588B90` | 258 | von Hand geprüft |
| 35 | `SetCallBackSave` | `0x00588CA0` | 18 | von Hand geprüft |
| 36 | `SetCallBackLoad` | `0x00588CC0` | 18 | von Hand geprüft |
| 37 | `CB_LoadSector` | `0x005897B0` | 37 | Callback-Registrierung |
| 38 | `CB_ClearSector` | `0x005897E0` | 248 | Callback-Registrierung |
| 39 | `LoadFromFiles` | – | | zweite Definition in der Quelle auskommentiert |

27 von 40 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ApmOcTree` (`0x00588390`), `GetNode_start` (`0x00588540`), `scalar_deleting_dtor` (`0x00588CE0`), `GetNode_root` (`0x00588DF0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB84` | `Zeiger auf die Moduldaten / Modulzeiger (nicht einzeln belegt)` | `OnInit` |
| `this+0xB88` | `Zeiger [`ApmMap`](ApmMap.md)` | `OnAddModule`, `OnInit` |
| `this+0xB8C / 0xB90` | `Rückrufe Speichern / Laden (`m_pfSaveCB`, `m_pfLoadCB`)` | `SetCallBackSave`, `SetCallBackLoad` |
| `this+0xB94` | `Wurzelfeld 800 × 800 Zeiger` | `GetRoot`, `SetRoot`, `GetRootByWorldPos` |
| `this+0x30DF94` | `Tabelle der Masken je Tiefe (acht Werte)` | `OnInit`, `GetNode` |
| `this+0x30DFB4` | `Tabelle der Verschiebungen je Tiefe (0, 6, 9, 12, 15, 18, 21, 24)` | `OnInit`, `MakeChild` |
| `Knoten+0xA / 0xB / 0xC` | `Blattflag / Tiefe / halbe Kantenlänge` | `DivideNode`, `MakeChild` |
| `Knoten+0x10` | `acht Kindzeiger` | `DivideNode`, `GetNodeForInsert` |

## Vtable und Aufbau

`ApmOcTree` (Octree der Welt: eine Wurzel je Sektor, Knoten mit acht Kindern) ist von `ApModule` abgeleitet. Konstruktor `0x00588390` (181 Byte), Löschwrapper `0x00588CE0`. `OnAddModule` (`0x00588450`, 48 Byte) holt `ApmMap` (`this+0xB88`) und legt zwei Datenblöcke an (`SetModuleData` mit 0x40 Byte, Kennung 0, und 0x2C Byte, Kennung 1; nach den Größen Knoten und Wurzel). `OnInit` (`0x005898E0`, 210 Byte) füllt die Tabellen für Maske und Verschiebung der Knoten-ID (acht Einträge; Masken 0, `0x1C0`, `0xE00`, `0x7000`, `0x38000`, `0x1C0000`, `0xE00000`, `0x7000000` und Verschiebungen 0, 6, 9, 12, 15, 18, 21, 24; je Tiefe drei Bit) und meldet `CB_LoadSector` (`0x005897B0`) bei `ApmMap` zum Laden und `CB_ClearSector` (`0x005897E0`) zum Entladen eines Sektors an. `OnDestroy` (`0x00589A00`) ruft `DestroyAll` (`0x005899C0`) unter Sperre.
Die Wurzeln liegen in einem Feld von 800 × 800 Zeigern bei `this+0xB94` (`MAP_WORLD_INDEX_WIDTH` × Höhe, Index = Spalte · 800 + Zeile); `GetRoot` (`0x005884C0`, 46 Byte) und `SetRoot` (`0x005884F0`, 67 Byte) prüfen die Grenzen. `this+0xB8C`/`+0xB90` halten die Zeiger der Speicher- und Lade-Rückrufe (`SetCallBackSave` `0x00588CA0`, `SetCallBackLoad` `0x00588CC0`).

## Knoten

Ein Knoten enthält: Kennung `+0`, Elternknoten `+4`, Blattflag `+0xA`, Tiefe `+0xB`, halbe Kantenlänge `+0xC`, acht Kinder `+0x10` bis `+0x2C`, Mittelpunkt `+0x30` bis `+0x38` und Kugelradius `+0x3C`. `MakeChild` (`0x00588620`, 386 Byte) legt das Kind einer Ecke (0 bis 7) an: berechnet Tiefe, halbe Kantenlänge, Mittelpunkt (± halbe Länge je Ecke) und Kennung (drei Bit je Tiefe). `DivideNode` (`0x00588FE0`, 61 Byte) teilt einen Knoten in acht Kinder und merkt es als Nicht-Blatt. `TestBoxPos` (`0x00588590`, 129 Byte) prüft, ob ein Punkt in einer Würfelbox um einen Mittelpunkt liegt.
`CreateRoot` (`0x005887D0`, 853 Byte; Aufrufer `GetStartNode` und `LoadFromFiles`) legt die Wurzel eines Sektors an (Sektorgrenzen und Höhen aus `ApmMap`, danach Rückruf `InitRoot`); `GetStartNode(x, y, z)` (`0x00588E30`, 428 Byte) findet oder erzeugt über `GetRoot`/`SetRoot`/`CreateRoot` die Wurzel zu einer Weltposition. `GetNode(Wurzel, ID)` (`0x00588DF0`) und `GetNode(Knoten, ID)` (`0x00588540`) laufen über die drei Bit je Tiefe der Kennung bis zum Knoten; `GetNodeForInsert` (`0x00589020`, 219 Byte) liefert den Knoten zu einer Kennung und teilt bei Bedarf (`DivideNode`); `GetLeafID` (`0x00589110`, 605 Byte) bestimmt die Kennung des Blatts für eine Position. `GetRootByWorldPos` (`0x00589A40`, 114 Byte) rechnet die Weltposition in den Sektorindex um (Division durch 6400 mit Versatz von 400 Sektoren); das Nachladen der Quelle (`bLoad`) ist im Binary nicht übersetzt, weil die Quelle den Parameter zu Beginn auf FALSE setzt.

## Laden und Aufräumen

`LoadFromFiles` (`0x00589370`, 1.086 Byte; Aufrufer `CB_LoadSector`) öffnet die Octree-Datei der Division, liest sie und baut die Wurzel mit `LoadNode` (`0x00588B90`, rekursiv) auf; die zweite Definition in der Quelle ist auskommentiert. `CB_ClearSector` zerstört die Wurzel beim Entladen (`DestroyTree` `0x00588D20`, rekursiv über `DestroyChilds` `0x00588480`).
`AttachOcTreeNodeData` (`0x00588B30`) und `AttachOcTreeRootData` (`0x00588B60`) sind 33-Byte-Einzeiler um `SetAttachedModuleData`; `AgcmOcTree::OnAddModule` ruft sie mit 8 Byte (Knoten) bzw. 0x14 Byte (Wurzel). `SetCallbackInitRoot` liegt am gemeinsamen `SetCallback`-Rumpf `0x006DA540` (Kennung 0), den `AgcmOcTree::OnAddModule` mit `CBInitRootData` aufruft.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen; `GetRootByWorldPos` lädt nie nach (auch in der Quelle: `bLoad = FALSE`).

## Grenzen

- Gelesen sind `OnAddModule`, `OnInit`, `GetRoot`, `SetRoot`, `GetRootByWorldPos`, `TestBoxPos`, `DivideNode`, `GetNodeForInsert` und die Kopf- und Anfangsteile von `MakeChild`; `CreateRoot`, `GetStartNode`, `GetLeafID` und `LoadFromFiles` sind über Aufrufbeziehungen, Größe und je ein Merkmal zugeordnet (z. B. `CreateRoot` als Aufrufer der Knotenanlage, `GetLeafID` als Aufruf aus dem Gras-Modul) und nicht Zeile für Zeile verglichen.
- Die Eigenschaft „Editor-Funktionen ohne Aufrufer“ folgt aus einer Textsuche der Quelle nach den Namen; Aufrufe über Funktionszeiger oder Makros wären so nicht erfasst.
- Die Knotenfelder oberhalb von `+0x30` (Mittelpunkt, Grenzen) sind nur grob aus `MakeChild` gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, nicht als eigene Funktion: 11, nicht im Client: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmOcTree`](AgcmOcTree.md), [`AgcmRender`](AgcmRender.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmRender`](AgcmRender.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmWater`](AgcmWater.md), [`ApmObject`](ApmObject.md)
