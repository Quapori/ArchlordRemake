# AgcmMap (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmMap` (Karte: Sektoren laden, Positionswechsel, Zonen, Höhen- und Strahlabfragen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Aufrufer in anderen Modulen, EP8-Quelle `Modules/AClient/AgcmMap/AgcmMap.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: jede der 146 Quellmethoden ist einer Adresse zugeordnet (66 Einträge der Tabelle, darunter zwei zusammengefaltete Rümpfe) oder begründet. Alle Methoden, die Client-Module aufrufen (`GetHeight`, `HP_GetHeight`, `HP_GetHeightGeometryOnly`, `GetHeight_Lowlevel_HeightOnly`, `GetMapPositionFromMousePosition`, `SetSectorIndexInsertBBox`, `GetSectorList`, `LoadSector`, `ClearAllSectors`, `MyCharacterPositionChange`, `LoadTargetPosition`, `__SetAutoLoadRange`, `DeleteMyCharacterCheck`, …), liegen im Binary. Die übrigen sind Editor- und Werkzeugcode, den im Client nichts aufruft; jede Zeile der Tabelle nennt den Grund.
- **Korrektur zu einer früheren Fassung dieses Berichts:** `0x005F3980` und `0x005F3A40` sind `HP_GetHeightGeometryOnly` (nicht `HP_GetHeight`); `HP_GetHeight` ist `0x005F5E60`/`0x005F5F30`, und `GetHeight` ist `0x005F6040`. Entscheidend waren die Aufrufbeziehungen: die Geometrie-Fassungen rufen `GetHeight_Lowlevel_HeightOnly` (`0x005F2A00`), die anderen `GetHeight_Lowlevel` (`0x005F51C0`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmMap.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetBBoxCallback` | – | | nur von der Inline-Fassung `GetSectorList(RpAtomic*)` benutzt; in `GetSectorList` (`0x005F23C0`) eingebaut |
| 1 | `_IntersectionCallBackFindDistance` | `0x005F26B0` | 29 | von Hand geprüft |
| 2 | `_GetClumpCallback` | – | | nur von `GetCursorClump` benutzt (unreferenziert); im Binary nicht vorhanden |
| 3 | `_GetClumpPickingOnlyCallback` | – | | nur von `GetCursorClump` benutzt (unreferenziert); im Binary nicht vorhanden |
| 4 | `CollisionAtomicSectorCallback` | `0x005F26D0` | 26 | seqmatch |
| 5 | `OnAddModule` | `0x005F5D20` | 320 | vtable/String |
| 6 | `OnInit` | `0x005F6CE0` | 979 | vtable/String |
| 7 | `ToggleZoneRough` | `0x005F26F0` | 171 | von Hand geprüft |
| 8 | `ShowAll` | `0x005F43C0` | 10 | seqmatch |
| 9 | `OnDestroy` | `0x005F27A0` | 17 | vtable/String |
| 10 | `OnIdle` | `0x005F27C0` | 18 | vtable/String |
| 11 | `SetTexturePath` | `0x005F27E0` | 29 | von Hand geprüft |
| 12 | `SetTexDict` | `0x005F2800` | 55 | von Hand geprüft |
| 13 | `SetCamera` | `0x005F2840` | 18 | von Hand geprüft |
| 14 | `SetDataPath` | `0x005F2860` | 34 | von Hand geprüft |
| 15 | `InitMapClientModule` | `0x005F2890` | 30 | von Hand geprüft |
| 16 | `InitMapToolData` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 17 | `InitMapToolLoadRange` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 18 | `MyCharacterPositionChange` | `0x005F6840` | 854 | von Hand geprüft |
| 19 | `OnLoadSector` | `0x0067FAB0` | 8 | gleiche Adresse wie `gemeinsamer Rumpf (Vtable-Slot 17)` (vom Linker zusammengefaltet) |
| 20 | `OnLoadRough` | `0x005F43D0` | 167 | vtable/String |
| 21 | `OnLoadDetail` | `0x005F4480` | 171 | vtable/String |
| 22 | `OnDestorySector` | `0x005F38D0` | 55 | vtable/String |
| 23 | `OnDestroyRough` | `0x005F28B0` | 98 | vtable/String |
| 24 | `OnDestroyDetail` | `0x005F2920` | 87 | vtable/String |
| 25 | `GetWorld` | `0x005F2980` | 52 | von Hand geprüft |
| 26 | `GetCurrentDetail` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 27 | `MakeDetailWorld` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 28 | `RecalcNormal` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 29 | `RecalcBoundingBox` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 30 | `Update` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 31 | `RecalcBoundingBox` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 32 | `RecalcNormals` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 33 | `UpdateAll` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 34 | `GenerateRoughMap` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 35 | `SetCurrentDetail` | `0x005F3910` | 109 | von Hand geprüft |
| 36 | `SetCurrentDetail` | `0x005F29C0` | 49 | von Hand geprüft |
| 37 | `CreateWorldImport` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 38 | `CreateDWSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 39 | `DestroyDWSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 40 | `GetDWSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 41 | `UpdateNormal2` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 42 | `MakeDetailWorld` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 43 | `LockSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 44 | `IsLockedSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 45 | `UnlockSectors` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 46 | `LoadTargetPosition` | `0x005F6BA0` | 143 | von Hand geprüft |
| 47 | `LoadAll` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 48 | `LoadAll` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 49 | `SaveAll` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 50 | `SaveAll` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 51 | `D_SetHeight` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 52 | `D_SetValue` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 53 | `D_GetEdgeTurn` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 54 | `D_GetEdgeTurn` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 55 | `D_SetEdgeTurn` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 56 | `D_SetTile` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 57 | `GetWorldSectorInfo` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 58 | `GetWorldSectorInfoOnly` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 59 | `SectorPreviwTextureSetup` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 60 | `IsInSectorRadius` | – | | nur von `SetSectorIndexInsert` gerufen; die Aufrufe von [`AgcmEventNature`](AgcmEventNature.md)/[`AgcmGrass`](AgcmGrass.md) gehören zu `ApWorldSector::IsInSectorRadius`; im Binary nicht vorhanden |
| 61 | `_GetHeightCallback` | `0x005F4EB0` | 93 | von Hand geprüft |
| 62 | `_GetHeightClientCallback` | `0x005F5060` | 342 | von Hand geprüft |
| 63 | `HP_GetHeight` | `0x005F5E60` | 194 | von Hand geprüft |
| 64 | `HP_GetHeight` | `0x005F5F30` | 268 | von Hand geprüft |
| 65 | `HP_GetHeightGeometryOnly` | `0x005F3980` | 186 | von Hand geprüft |
| 66 | `HP_GetHeightGeometryOnly` | `0x005F3A40` | 260 | von Hand geprüft |
| 67 | `GetHeight` | `0x005F6040` | 1411 | von Hand geprüft |
| 68 | `GetHeight_Lowlevel_HeightOnly` | `0x005F2A00` | 379 | von Hand geprüft |
| 69 | `GetHeight_Lowlevel` | `0x005F51C0` | 1240 | von Hand geprüft |
| 70 | `GetHeight_Lowlevel_Collision` | – | | von keinem Modul gerufen; im Binary nicht vorhanden |
| 71 | `GetSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 72 | `IsGeometry` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 73 | `LoadDWSector` | – | | Fassung ohne Detailstufe (lädt beide Stufen): wird nur im Editor-Zweig (Quelle Zeile 4620) gerufen; `OnLoadRough`/`OnLoadDetail` rufen die Fassung mit Detailstufe `0x005F3B50`; im Binary nicht vorhanden |
| 74 | `LoadDWSector` | `0x005F3B50` | 820 | von Hand geprüft |
| 75 | `ReleaseDWSector` | `0x005F2B90` | 86 | von Hand geprüft |
| 76 | `LoadSector` | `0x005F2BF0` | 215 | von Hand geprüft |
| 77 | `ReleaseSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 78 | `ReleaseSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 79 | `CallBackMapDataLoad` | `0x005F56A0` | 20 | von Hand geprüft |
| 80 | `CallBackMapDataDestroy` | `0x005F56C0` | 143 | von Hand geprüft |
| 81 | `BspExport` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 82 | `GetMapPositionFromMousePosition_tool` | – | | Werkzeugfassung, von keinem Client-Modul gerufen; im Binary nicht vorhanden |
| 83 | `GetMapPositionFromMousePosition` | `0x005F5750` | 1120 | von Hand geprüft |
| 84 | `SetAutoLoadRange` | `0x005F2CD0` | 149 | von Hand geprüft |
| 85 | `__SetAutoLoadRange` | `0x005F6C30` | 173 | von Hand geprüft |
| 86 | `IsLoadedDetail` | `0x005F2D70` | 41 | von Hand geprüft |
| 87 | `MakeRoughPolygon` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 88 | `CopyDetailNormalToRoughNormal` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 89 | `ApplyAlpha` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 90 | `ApplyAlphaToSector` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 91 | `DeleteMyCharacterCheck` | `0x005F2DA0` | 21 | von Hand geprüft |
| 92 | `DumpTexDict` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 93 | `GetCursorClump` | – | | von keinem Modul gerufen; im Binary nicht vorhanden |
| 94 | `RemoveHPInfo` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 95 | `SetSectorIndexInsert` | – | | die Aufrufe in `AgcmObject.cpp` sind auskommentiert (nur die Fassung mit Hüllbox wird benutzt); im Binary nicht vorhanden |
| 96 | `SetSectorIndexInsertBBox` | `0x005F2DC0` | 375 | von Hand geprüft |
| 97 | `CreateImAtomic` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 98 | `SectorForAllAtomicsIntersection` | `0x005F4530` | 384 | von Hand geprüft |
| 99 | `LoadingSectorsForAllAtomicsIntersection` | `0x005F46C0` | 498 | von Hand geprüft |
| 100 | `LoadingSectorsForAllAtomicsIntersection2` | `0x005F48C0` | 417 | von Hand geprüft |
| 101 | `LoadingSectorsForAllAtomicsIntersection3` | – | | in der Quelle nur von nicht benutzten Funktionen oder auskommentiert gerufen (`AgcuCamConstrain.cpp` ruft die Fassung 3 nur in einem Kommentar); im Binary nicht vorhanden |
| 102 | `LoadingSectorsForAllAtomicsIntersection4` | – | | in der Quelle nur von nicht benutzten Funktionen oder auskommentiert gerufen (`AgcuCamConstrain.cpp` ruft die Fassung 3 nur in einem Kommentar); im Binary nicht vorhanden |
| 103 | `LoadingSectorsForAllAtomicsIntersection5` | – | | in der Quelle nur von nicht benutzten Funktionen oder auskommentiert gerufen (`AgcuCamConstrain.cpp` ruft die Fassung 3 nur in einem Kommentar); im Binary nicht vorhanden |
| 104 | `LineGetIntersectionSectors` | `0x005F2F40` | 735 | von Hand geprüft |
| 105 | `LoadingSectorsForAllClumps` | – | | in der Quelle nur von nicht benutzten Funktionen oder auskommentiert gerufen (`AgcuCamConstrain.cpp` ruft die Fassung 3 nur in einem Kommentar); im Binary nicht vorhanden |
| 106 | `LoadingSectorsForAllClumps_OCTREE` | – | | in der Quelle nur von nicht benutzten Funktionen oder auskommentiert gerufen (`AgcuCamConstrain.cpp` ruft die Fassung 3 nur in einem Kommentar); im Binary nicht vorhanden |
| 107 | `LoadingSectorsForAllAtomicsIntersection` | – | | zweite Definition (Quelle Zeile 11054, ältere Fassung) steht in einem auskommentierten Block; die gültige ist `0x005F46C0` |
| 108 | `_AgcmMapSectorDataConstructor` | `0x005F3220` | 61 | von Hand geprüft |
| 109 | `_AgcmMapSectorDataDestructor` | `0x005F3260` | 102 | von Hand geprüft |
| 110 | `CBMyCharacterPositionChange` | `0x005F3E90` | 447 | von Hand geprüft |
| 111 | `FlushLoadSector` | `0x005F32D0` | 245 | von Hand geprüft |
| 112 | `CBMyCharacterPositionChange2` | `0x005F33D0` | 414 | seqmatch |
| 113 | `SetPreLightForAllGeometry` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 114 | `CreateCollisionAtomic` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 115 | `__CreateWorldCollisionImport` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 116 | `CreateAllCollisionAtomic` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 117 | `DestroyAllCollisionAtomic` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 118 | `EnumLoadedDivision` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 119 | `CBLoadedDivisionCheck` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 120 | `IsLoadedDivision` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 121 | `IsLoadedDivision` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 122 | `EnumLoadedDivisionObject` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 123 | `CreateCompactDataFromDetailInfo` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 124 | `SaveGeometryBlocking` | – | | nur von den Stream-Rückrufen des Editors (unter `USE_MFC`) benutzt; im Binary nicht vorhanden |
| 125 | `LoadGeometryBlocking` | – | | nur von den Stream-Rückrufen des Editors (unter `USE_MFC`) benutzt; im Binary nicht vorhanden |
| 126 | `LoadSkyBlocking` | – | | nur von den Stream-Rückrufen des Editors (unter `USE_MFC`) benutzt; im Binary nicht vorhanden |
| 127 | `CBLoadGeometry` | – | | wird in `OnAddModule` nur unter `USE_MFC` (Editor) angemeldet; im Binary nicht vorhanden |
| 128 | `CBSaveGeometry` | – | | wird in `OnAddModule` nur unter `USE_MFC` (Editor) angemeldet; im Binary nicht vorhanden |
| 129 | `CBLoadMoonee` | – | | wird in `OnAddModule` nur unter `USE_MFC` (Editor) angemeldet; im Binary nicht vorhanden |
| 130 | `CBSaveMoonee` | – | | wird in `OnAddModule` nur unter `USE_MFC` (Editor) angemeldet; im Binary nicht vorhanden |
| 131 | `GetOnObject` | `0x005F4050` | 278 | von Hand geprüft |
| 132 | `GetType` | `0x005F4170` | 283 | von Hand geprüft |
| 133 | `ClearAllSectors` | `0x005F3570` | 169 | seqmatch |
| 134 | `ZoneLoadingDivision` | `0x005F65D0` | 334 | von Hand geprüft |
| 135 | `LoadZoneRoughBuffer` | `0x005F5BC0` | 337 | von Hand geprüft |
| 136 | `FlushZoneRoughBuffer` | `0x005F4DA0` | 85 | von Hand geprüft |
| 137 | `CheckSelfCharacterRegionChange` | `0x005F6720` | 285 | von Hand geprüft |
| 138 | `GetSectorList` | `0x005F23C0` | 533 | von Hand geprüft |
| 139 | `LoadRoughTexture` | `0x005F3620` | 146 | seqmatch |
| 140 | `LoadRoughAtomic` | `0x005F36C0` | 488 | seqmatch |
| 141 | `CBMTextureRender` | `0x005F42C0` | 93 | von Hand geprüft |
| 142 | `AllocSectorGridInfo` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 143 | `RenderSectorGrid` | – | | Editor-/Werkzeugfunktion, von keinem Client-Modul gerufen (Suche im Quellbaum); im Binary nicht vorhanden |
| 144 | `CBDestroySector_Start` | `0x005F38B0` | 24 | von Hand geprüft |
| 145 | `CBDestroySector_End` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer leerer Rumpf` (vom Linker zusammengefaltet) |

66 von 146 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `fxConstUploadCB` (`0x005F2350`), `__RsIntersectionCallBackGeometryTriangleAtomic` (`0x005F25E0`), `AgcmMap` (`0x005F4A80`), `~AgcmMap` (`0x005F4CB0`), `__GetWorldSectorGeometryCallback` (`0x005F4E00`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98 / 0xB9C / 0xBA0 / 0xBA4 / 0xBA8` | `Zeiger [`ApmMap`](ApmMap.md) / [`AgcmRender`](AgcmRender.md) / [`AgcmResourceLoader`](AgcmResourceLoader.md) / [`AgcmOcTree`](AgcmOcTree.md) / [`ApmOcTree`](ApmOcTree.md)` | `OnAddModule` |
| `this+0xBAC / 0xBB0` | `Kennungen der beiden Lader (Positionswechsel / Sektor zerstören)` | `OnAddModule` |
| `this+0xBD4` | `Name des Kachel-Wörterbuchs (256 Byte)` | `SetTexDict` |
| `this+0xD10…0xD18` | `letzte Position des eigenen Charakters` | `CheckSelfCharacterRegionChange` |
| `this+0xD1C` | `Avatarposition gesetzt` | `__SetAutoLoadRange` |
| `this+0xD20` | `Datenpfad (256 Byte)` | `SetDataPath` |
| `this+0xE20` | ``m_bFirstPosition`` | `InitMapClientModule`, `DeleteMyCharacterCheck` |
| `this+0xF50` | `Kamera (`m_pstCamera`)` | `SetCamera` |
| `this+0xF5C` | `Texturpfad (128 Byte)` | `SetTexturePath` |
| `this+0xFE0 / 0xFE4` | `Initialisiert-Merker / Index der angehängten Sektordaten` | `InitMapClientModule`, `OnAddModule` |
| `this+0x1004` | `Welt (`m_pWorld`)` | `InitMapClientModule` |
| `this+0x1008 / 0x1010 / 0x1014` | `Ladereichweiten Kartendaten / Rauh / Detail` | `SetAutoLoadRange` |
| `this+0x1020` | `Zahl der zu ladenden Sektoren` | `CBMyCharacterPositionChange`, `ZoneLoadingDivision` |
| `this+0x102C` | `Zeitzähler (`m_ulCurTick`) für die Strahlabfragen` | `LoadingSectorsForAllAtomicsIntersection` |
| `this+0x106C / 0x1070` | `Vektor der Zonen-Rauh-Atomics (Anfang / Ende)` | `LoadZoneRoughBuffer`, `CBMTextureRender` |
| `this+0x1078` | `aktuelle Zonen-Division` | `ZoneLoadingDivision`, `CheckSelfCharacterRegionChange` |
| `this+0x107C` | ``m_bShowZoneRough`` | `ToggleZoneRough`, `CBMTextureRender` |

## Vtable und Aufbau

Das Modul liegt im Adressbereich `0x005F2350`–`0x005F6CE0` (die Quelle beginnt mit statischen Hilfsfunktionen, deshalb liegt `fxConstUploadCB` bei `0x005F2350` noch vor `OnDestroy`). Vtable-Slots: 0 `~AgcmMap` (`0x005F4D80`, Löschwrapper), 1 `OnAddModule` (`0x005F5D20`), 2 `OnInit` (`0x005F6CE0`), 3 `OnIdle` (`0x005F27C0`), 4 und 5 `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x005F27A0`), 8 `0x004E3420`, 17 `OnLoadSector` (gemeinsamer Rumpf `0x0067FAB0`), 18 `OnDestorySector` (`0x005F38D0`), 19 `OnLoadRough` (`0x005F43D0`), 20 `OnLoadDetail` (`0x005F4480`), 21 `OnDestroyRough` (`0x005F28B0`), 22 `OnDestroyDetail` (`0x005F2920`). Der Konstruktor (`0x005F4A80`, 554 Byte, trägt `AgcmMap`) und der Destruktorrumpf (`0x005F4CB0`) sind zugeordnet.

## Einrichtung durch die Engine

`MyEngine` (Hauptprogramm) richtet das Modul in dieser Reihenfolge ein; die zugehörigen Funktionen sind aus dem Aufrufer `OnPostRegisterModule` (`0x00410EB0`) und der Quelle bestimmt: `SetAutoLoadRange(8, 6, 2)` (`0x005F2CD0`, setzt die Ladereichweiten für Kartendaten, Rauh- und Detailstufe und gibt sie an `ApmOcTree` und `AgcmRender` weiter), `SetDataPath` (`0x005F2860`, kopiert bis 256 Zeichen nach `this+0xD20`), `InitMapClientModule` (`0x005F2890`, setzt `m_bFirstPosition`, den Initialisiert-Merker und `m_pWorld`), `SetCamera` (`0x005F2840`, `this+0xF50`), `SetTexDict` (`0x005F2800`, kopiert bis 255 Zeichen nach `this+0xBD4` und setzt einen Merker), `SetTexturePath` (`0x005F27E0`, `strncat` bis 127 Zeichen nach `this+0xF5C`). `GetWorld` (`0x005F2980`, 52 Byte) legt mit `RpWorldCreate` die Welt mit der Hüllbox ±1 000 000 an; Aufrufer ist `OnPreRegisterModule` (`0x00410DC0`).
`OnAddModule` holt `ApmMap`, `AgcmRender`, `AgcmResourceLoader`, `AgcmOcTree` und `ApmOcTree` (Zeiger ab `this+0xB98`), übernimmt `m_bUseCullMode` und registriert zwei Lader beim Ressourcenlader: `CBMyCharacterPositionChange` (`0x005F3E90`) mit `CBMyCharacterPositionChange2` (`0x005F33D0`) und `CBDestroySector_Start` (`0x005F38B0`, löst den Rückruf 1 aus) mit dem leeren Rumpf `0x0067AC90` als `CBDestroySector_End`. Danach setzt es `CallBackMapDataLoad` (`0x005F56A0`) und `CallBackMapDataDestroy` (`0x005F56C0`) bei `ApmMap`, hängt die Sektordaten an (Erzeuger `_AgcmMapSectorDataConstructor` `0x005F3220`, Zerstörer `0x005F3260`; je 220 Byte) und meldet `CBMTextureRender` (`0x005F42C0`) bei `AgcmRender` an. Die Stream-Rückrufe `CBLoad/SaveGeometry` und `CBLoad/SaveMoonee` werden in der Quelle nur unter `USE_MFC` (Editor) angemeldet. `OnInit` registriert über AngelScript `ShowAll` (`0x005F43C0`, ruft `SetCurrentDetail(2, TRUE)`) und `ToggleZoneRough` (`0x005F26F0`, kehrt `this+0x107C` um und gibt eine Konsolenmeldung aus).

## Sektoren laden

`LoadSector` (`0x005F2BF0`) holt den Sektor aus `ApmMap` oder lädt ihn (Sperre um den Ladevorgang); `ClearAllSectors` (`0x005F3570`) entfernt alle geladenen Sektoren außer dem aktuellen mit `ApmMap::DeleteSector`. `CBMyCharacterPositionChange` (`0x005F3E90`, 447 Byte) setzt die Thread-Kennung (`GetCurrentThreadId`, wie `btid` in der Quelle) und läuft über die Kartendaten-Ladereichweite (`this+0x1008`) um den neuen Sektor, lädt fehlende Sektoren (`LoadSector`) und zählt die zu ladenden Sektoren (`this+0x1020`). `FlushLoadSector` (`0x005F32D0`, 245 Byte) läuft über alle geladenen Sektoren (`ApmMap+0x2B1C74` = Anzahl, `+0x271C78` = Liste), bildet den Sektorabstand (Maximum der Indexdifferenzen) und vergleicht ihn mit den Ladereichweiten. `LoadDWSector` (`0x005F3B50`, 820 Byte) baut die Dateinamen `b%06dx.ma2`, `D%d,%d.dff`, `a%06dx.ma2` und `R%d,%d.dff` unter `World\\` und wird von `OnLoadRough` und `OnLoadDetail` gerufen; `LoadRoughAtomic` (`0x005F36C0`) lädt die Rauh-Atomic, `LoadRoughTexture` (`0x005F3620`, 146 Byte) liest das Texturwörterbuch (Chunk `0x16`) und holt die erste Textur. `ReleaseDWSector` (`0x005F2B90`) gibt die Detaildaten eines Sektors frei und wird von `CallBackMapDataDestroy` und `OnDestorySector` gerufen. `IsLoadedDetail` (`0x005F2D70`) prüft, ob zu einer Detailstufe ein Atomic vorhanden ist; `SetCurrentDetail` gibt es zweimal: für alle Sektoren (`0x005F3910`) und für einen Sektor (`0x005F29C0`, bei `OP_DONOTLOADSECTOR`-Flag wirkungslos).

## Positionswechsel und Zonen

`MyCharacterPositionChange` (`0x005F6840`, 854 Byte) bekommt Vor- und Nachposition (je drei Werte) und das Neuladen-Flag, rechnet die Sektorindizes (`(x + 0x271000) / 0x1900 - 400`, also 6400 Einheiten je Sektor), meldet nicht mehr benötigte Ladeaufträge ab (`RemoveAllEntry`) und fügt neue hinzu (`AddLoadEntry`). `LoadTargetPosition` (`0x005F6BA0`) leert alle Sektoren, ruft `MyCharacterPositionChange` mit der Zielposition und arbeitet den Ladeauftrag-Speicher ab (`OnIdleLoad`, solange Aufträge warten). `DeleteMyCharacterCheck` (`0x005F2DA0`) setzt `m_bFirstPosition` zurück und leert die Ladeschlange; `__SetAutoLoadRange` (`0x005F6C30`) setzt die Reichweiten, lädt bei gesetzter Avatarposition (`this+0xD1C`) sofort neu und löst den Rückruf 6 aus. `CheckSelfCharacterRegionChange` (`0x005F6720`) vergleicht die Regionen beider Positionen und stößt `ZoneLoadingDivision` (`0x005F65D0`) an. Diese setzt das Sofortlade-Merkmal des `AgcmResourceLoader` (`+0x13F4`), zählt Sektoren der Division (16 × 16), holt die Regionsvorlage und ruft `LoadZoneRoughBuffer` (`0x005F5BC0`) mit Quelle, Höhenversatz, Ziel und Radius aus der Vorlage. `LoadZoneRoughBuffer` leert zuerst den Puffer (`FlushZoneRoughBuffer`, `0x005F4DA0`) und lädt dann je Sektor im Radius eine Rauh-Atomic.

## Höhen- und Strahlabfragen

`GetHeight` (`0x005F6040`, 1411 Byte, 27 Aufrufer außerhalb des Moduls) entspricht der Quelle Zeile für Zeile in der Eingangslogik: fehlt `ApmMap` oder der Sektor, kommt die Standardhöhe 1,0; ist die niedrige Detailstufe nicht geladen, wird das Flag `OP_HEIGHTUPDATEAFTERLOAD` (`0x4`) gesetzt und die Standardhöhe geliefert; danach bestimmt es das Segment, behandelt „keine Schicht“, fragt befahrbare Objekte ab und interpoliert über `HP_GetHeight` auf den Segmentpunkten. `HP_GetHeight` gibt es in der Fassung mit Sektor und Segmentindizes (`0x005F5E60`) und mit Weltposition (`0x005F5F30`); beide laufen über `GetHeight_Lowlevel` (`0x005F51C0`, 1240 Byte), das Strahlen durch `SectorForAllAtomicsIntersection` (`0x005F4530`) mit den Rückrufen `_GetHeightCallback` (`0x005F4EB0`, nimmt nur befahrbare Objekte) und `_GetHeightClientCallback` (`0x005F5060`, nur Weltsektoren) schickt. Die Geometrie-Fassungen `HP_GetHeightGeometryOnly` (Sektor `0x005F3980`, Position `0x005F3A40`, 13 Aufrufer) laufen stattdessen über `GetHeight_Lowlevel_HeightOnly` (`0x005F2A00`) mit dem Rückruf `CollisionAtomicSectorCallback` (`0x005F26D0`). `GetOnObject` (`0x005F4050`) und `GetType` (`0x005F4170`) fragen die befahrbaren Objekte eines Segments ab (Aufrufer: `0x005A3070` bzw. `0x005C9310`).
`LineGetIntersectionSectors` (`0x005F2F40`, 735 Byte) rechnet vier Sektorindizes aus Start und Ende des Strahls (`ftol`) und baut die Liste der geschnittenen Sektoren. `LoadingSectorsForAllAtomicsIntersection` (`0x005F46C0`, mit Terrain, erhöht den Zeitzähler `this+0x102C`) wird von `GetMapPositionFromMousePosition` (`0x005F5750`, 1120 Byte, 8 Parameter, Aufrufer sind [`AgcmTargeting`](AgcmTargeting.md)-Funktionen) gerufen; `LoadingSectorsForAllAtomicsIntersection2` (`0x005F48C0`, ohne Terrain) von `AgcmTargeting::OnMouseMove` (`0x00636660`). `__GetWorldSectorGeometryCallback` (`0x005F4E00`, freie Funktion der Quelle) sammelt die getroffenen Atomics in einer Liste. `SetSectorIndexInsertBBox` (`0x005F2DC0`, 375 Byte) trägt ein Objekt in die Sektorindizes seiner Hüllbox ein (Aufrufer sind [`AgcmObject`](AgcmObject.md)-Funktionen `0x006736E0` und `0x00673F70`); `GetSectorList` (`0x005F23C0`, 533 Byte) liefert die von einem Atomic berührten Sektoren – die Hilfsfunktion `GetBBoxCallback` und die Fassung mit Hüllbox sind darin eingebaut.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen den Quelltext gelesen sind `GetHeight` (Eingangslogik), `HP_GetHeight`/`HP_GetHeightGeometryOnly` (beide Fassungen), `FlushLoadSector`, `LoadZoneRoughBuffer`, `FlushZoneRoughBuffer`, `GetOnObject`, `GetType`, `InitMapClientModule`, `SetAutoLoadRange`, `__SetAutoLoadRange`, `DeleteMyCharacterCheck`, `LoadTargetPosition`, `ToggleZoneRough`, `ShowAll`, `GetWorld` und der Aufbau von `OnAddModule`/`OnInit`; `CBMyCharacterPositionChange` ist durch die Registrierung beim Ressourcenlader (Argumentreihenfolge) bestätigt.
- Nur über Struktur, Zeichenketten, Aufrufer und Größenverhältnisse (nicht Zeile für Zeile) zugeordnet sind `LoadDWSector`, `LoadRoughAtomic`, `LoadRoughTexture`, `ClearAllSectors`, `SetCurrentDetail` (beide), `MyCharacterPositionChange`, `CheckSelfCharacterRegionChange`, `ZoneLoadingDivision`, `GetHeight_Lowlevel`, `GetHeight_Lowlevel_HeightOnly`, `LineGetIntersectionSectors`, `SectorForAllAtomicsIntersection`, `LoadingSectorsForAllAtomicsIntersection`/`…2`, `GetMapPositionFromMousePosition`, `SetSectorIndexInsertBBox`, `GetSectorList`, `ReleaseDWSector`, `_GetHeightCallback`, `_GetHeightClientCallback` und die statischen Hilfsfunktionen (`fxConstUploadCB`, `__RsIntersectionCallBackGeometryTriangleAtomic`, `__GetWorldSectorGeometryCallback`, `_IntersectionCallBackFindDistance`, `CollisionAtomicSectorCallback`). Die Namen der Rückrufe unterscheiden sich durch ihren Inhalt (Typprüfung auf befahrbare Objekte gegenüber Weltsektoren) und durch die Stelle, an der sie übergeben werden.
- Die Aussagen „im Binary nicht vorhanden“ stützen sich auf die Quelle (kein Aufrufer außerhalb des Moduls laut Suche in `Modules/AClient`, `Client` und `Etc`, nur auskommentierte oder editorinterne Aufrufe) und auf die Aufrufersuche im Binary. Funktionen, die außerhalb des Moduls aufgerufen werden, wurden dabei einzeln gesucht und gefunden, weil bei [`AgcmWorld`](AgcmWorld.md) und [`AgcmWater`](AgcmWater.md) zuerst übersehene Funktionen auftauchten.
- Weitere Funktionen im Adressbereich ohne eigene Quellmethode: `0x005F2B80` (Hilfsrückruf in `LoadRoughTexture`, speichert eine Textur), `0x005F4320` (Listenanhängen), `0x005F4280` (Bruchstück ohne Aufrufer). Unter den STL-Funktionen liegen weitere Vorlagen (Vektoren/Listen) der Sektor- und Rauh-Atomic-Listen.
- Die Offsets stammen aus den genannten Funktionen; Feldnamen der Quelle sind aus der Verwendung gefolgert, nicht aus einer Layout-Rechnung.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht im Client: 46, ohne Kandidat: 42.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventNature`](AgcmEventNature.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmObject`](AgcmObject.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmWater`](AgcmWater.md), [`AgcmWorld`](AgcmWorld.md), [`ApmMap`](ApmMap.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmCamera2`](AgcmCamera2.md), [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmItem`](AgcmItem.md), [`AgcmLensFlare`](AgcmLensFlare.md), [`AgcmNatureEffect`](AgcmNatureEffect.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTuner`](AgcmTuner.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIEventTeleport`](AgcmUIEventTeleport.md)
