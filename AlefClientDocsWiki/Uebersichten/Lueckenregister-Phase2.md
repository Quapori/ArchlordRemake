# Phase 2

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Erzeugt mit `gapclose.py register`. Jede Quellmethode ohne Binary-Adresse bekommt einen Status mit Beleg. **zugeordnet** = eindeutiger Treffer (mindestens zwei unabhängige Belege, Reihenfolge der Quelle passt zur Adressreihenfolge); **gemeinsamer Rumpf** = `SetCallback`-Einzeiler; **nicht im Client** = in der Quelle ruft sie kein Client-Modul (nur Server oder niemand); **eingebaut** = kleine Funktion mit Aufrufer im Client, ohne eigene Adresse; **Kandidat unbestätigt** = Aufrufer im Client und ein Kandidat mit nur einem Beleg oder mehrdeutig (nicht benannt); **ohne Kandidat** / **nicht als eigene Funktion** = Aufrufer im Client, aber keine unbenannte Funktion mit Beleg (bei „nicht als eigene Funktion“ ist im Klassenbereich gar keine unbenannte Funktion mehr übrig); in beiden Fällen ist die Methode vermutlich eingebaut oder entfernt.

Zahlen: Kandidat unbestätigt 3, eingebaut 54, gemeinsamer Rumpf 39, nicht als eigene Funktion 27, nicht im Client 192, ohne Kandidat 159, zugeordnet 14

## AgcmMap (eingebaut 2, nicht im Client 46, ohne Kandidat 42)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetBBoxCallback` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::CBOnAddObject; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `InitMapToolData` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `InitMapToolLoadRange` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnLoadSector` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmMap::CallBackMapDataLoad |
| `GetCurrentDetail` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmMap::Update, AgcmMap::UpdateAll, AgcmMap::SetCurrentDetail |
| `MakeDetailWorld` | 1017 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::Update; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakeDetailWorld` | 190 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::Update; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RecalcNormal` | 65 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::RecalcNormals, AgcmMap::GenerateRoughMap, AgcmMap::MakeDetailWorld; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RecalcBoundingBox` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::BspExport; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RecalcBoundingBox` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::BspExport; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Update` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RecalcNormals` | 49 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateAll` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GenerateRoughMap` | 67 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateWorldImport` | 191 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateDWSector` | 94 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::MakeDetailWorld; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `DestroyDWSector` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::MakeDetailWorld, AgcmMap::CreateDWSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetDWSector` | 65 | ohne Kandidat |  | Aufrufer im Client: _MaptoolClientSaveData::GeometryStreamWrite, _MaptoolClientSaveData::MooneeStreamWrite, AgcmMap::RecalcNormal; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `UpdateNormal2` | 529 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LockSector` | 83 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::RecalcNormal, AgcmMap::GenerateRoughMap, AgcmMap::MakeDetailWorld; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsLockedSector` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::D_SetHeight; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `UnlockSectors` | 54 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::RecalcNormals, AgcmMap::GenerateRoughMap, AgcmMap::MakeDetailWorld; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `LoadAll` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::_BuildEffSetContainer; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `LoadAll` | 57 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::_BuildEffSetContainer; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SaveAll` | 268 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveAll` | 269 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `D_SetHeight` | 229 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::RecalcNormal; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `D_SetValue` | 102 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::SetPreLightForAllGeometry; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `D_GetEdgeTurn` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `D_GetEdgeTurn` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `D_SetEdgeTurn` | 86 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `D_SetTile` | 188 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::ApplyAlpha; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetWorldSectorInfo` | 159 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::D_SetHeight, AgcmMap::D_SetEdgeTurn, AgcmMap::D_SetTile; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetWorldSectorInfoOnly` | 139 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::ApplyAlpha, AgcmMap::ApplyAlphaToSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SectorPreviwTextureSetup` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::D_SetTile; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsInSectorRadius` | 61 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::AddEventNatureObject, AgcmGrass::RemoveGrass, AgcmMap::SetSectorIndexInsert; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetHeight_Lowlevel_Collision` | 71 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSector` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcdCamConstrain_Terrain::bPreChkTerrain, AgcmCharacter::GetValidDestination, AgcmCharacter::BlockingPositionCheck; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsGeometry` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::GetSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `LoadDWSector` | 198 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::OnLoadRough, AgcmMap::OnLoadDetail, AgcmMap::LoadAll; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `ReleaseSector` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseSector` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `BspExport` | 634 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMapPositionFromMousePosition_tool` | 228 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeRoughPolygon` | 598 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CopyDetailNormalToRoughNormal` | 42 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ApplyAlpha` | 191 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::ApplyAlphaToSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `ApplyAlphaToSector` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DumpTexDict` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCursorClump` | 121 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveHPInfo` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSectorIndexInsert` | 69 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateImAtomic` | 518 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadingSectorsForAllAtomicsIntersection3` | 37 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadingSectorsForAllAtomicsIntersection4` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadingSectorsForAllAtomicsIntersection5` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::GetMapPositionFromMousePosition_tool; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `LoadingSectorsForAllClumps` | 38 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadingSectorsForAllClumps_OCTREE` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPreLightForAllGeometry` | 76 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateCollisionAtomic` | 47 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::CreateAllCollisionAtomic, AgcmMap::DestroyAllCollisionAtomic; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `__CreateWorldCollisionImport` | 105 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::CreateCollisionAtomic; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CreateAllCollisionAtomic` | 66 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyAllCollisionAtomic` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnumLoadedDivision` | 39 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::IsLoadedDivision, ApmMap::EnumLoadedDivision; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBLoadedDivisionCheck` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::IsLoadedDivision; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsLoadedDivision` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsLoadedDivision` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnumLoadedDivisionObject` | 75 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateCompactDataFromDetailInfo` | 69 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::BspExport; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SaveGeometryBlocking` | 73 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadGeometryBlocking` | 54 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadSkyBlocking` | 54 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBLoadGeometry` | 27 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSaveGeometry` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBLoadMoonee` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSaveMoonee` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AllocSectorGridInfo` | 62 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::RenderSectorGrid; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RenderSectorGrid` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBDestroySector_End` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `__MakeDetailWorldImport` | 131 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::MakeDetailWorldAtomic; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakeDetailWorldAtomic` | 39 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RpDWSectorInit` | 48 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::CreateDWSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RpDWSectorGetDetail` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::CreateDWSector, AgcmMap::DestroyDWSector, AgcmMap::GetDWSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RpDWSectorSetCurrentDetail` | 61 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::OnDestroyRough, AgcmMap::OnDestroyDetail, AgcmMap::SetCurrentDetail; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RpDWSectorBuildAtomicCollision` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RpDWSectorDestroyDetail` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::OnDestroyRough, AgcmMap::OnDestroyDetail, AgcmMap::ReleaseDWSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RpDWSectorDestroyDetail` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::OnDestroyRough, AgcmMap::OnDestroyDetail, AgcmMap::ReleaseDWSector; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RpDWSectorGetCurrentDetail` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::GetCurrentDetail, AgcmMap::GetWorldSectorInfo, AgcmMap::GetWorldSectorInfoOnly; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsPolygonDataLoaded` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::UpdateNormal2, AgcmMap::RpDWSectorSetCurrentDetail; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RpDWSectorDestroy` | 79 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::DestroyDWSector, AgcmMap::_AgcmMapSectorDataDestructor, AgcmMap::RpDWSectorDestroyDetail; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgcmOcTree (eingebaut 2, gemeinsamer Rumpf 2, nicht im Client 10, ohne Kandidat 9, zugeordnet 7)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OcTreeChildCheck` | 51 | zugeordnet | `0x006FBB00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OcTreeForAllClumps` | 20 | zugeordnet | `0x006FC5C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddClumpToOcTree` | 91 | zugeordnet | `0x006FC940` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LineGetIntersectionSectors` | 150 | zugeordnet | `0x006FBD40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OcTreesForAllAtomicsIntersection2` | 47 | zugeordnet | `0x006FC7B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OcTreesForAllAtomicsIntersection` | 57 | zugeordnet | `0x006FC630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OneOcTreeForAllAtomicsIntersection` | 45 | zugeordnet | `0x006FBC30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CreateRootByTerrain` | 88 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MakeOctrees; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetQuadNodes` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmOcTree::CreateRootByTerrain; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `SetAllQuadY` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmOcTree::CreateRootByTerrain |
| `SetAllQuadY` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmOcTree::CreateRootByTerrain; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `TestClumpOctrees` | 182 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MakeOctrees; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CallBackSetOcTreeIDs` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmOcTree::TestClumpOctrees; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `TestAtomicOctreesByClump` | 122 | ohne Kandidat |  | Aufrufer im Client: AgcmOcTree::CallBackSetOcTreeIDs; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `DivideToLeafTree` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveClumpFromOcTree` | 103 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MyWorldRemoveClump; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `SetClumpAndDrawStart` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetDrawEnd` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DrawDebugBoxes` | 82 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetOctreeDebugSector` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DrawOctreeDebugSectorBox` | 57 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DrawQuadNodes` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DrawOcTreeNodes` | 72 | ohne Kandidat |  | Aufrufer im Client: AgcmOcTree::DrawDebugBoxes; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `NodeForAllClumps` | 39 | ohne Kandidat |  | Aufrufer im Client: AgcmOcTree::OcTreeForAllClumps; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `SetWorldIntersectionCallBack` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmRender::OnAddModule |
| `OcTreesForAllAtomicsIntersection3` | 44 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OcTreesForAllAtomicsIntersection4` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OcTreesForAllAtomicsIntersection5` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmResourceLoader (eingebaut 3, gemeinsamer Rumpf 1, nicht im Client 5, ohne Kandidat 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCurrentTexDict` | 112 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddTexDict` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::SetCurrentTexDict; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `GetTexDict` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::SetCurrentTexDict, AgcmResourceLoader::RemoveTexDict; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `RemoveTexDict` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBGetTextureFromTexDict` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::LoadTextureFromTexDict; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `WriteAllTexDicts` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `InstanceAtomic` | 34 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::CBInstanceAtomic; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `CBInstanceAtomic` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::InstanceClump; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `InstanceClump` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmExportResource::CheckLoadedClump |
| `SetCallbackLoadEntryEmpty` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetHierarchy` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCharacter::InitCharacterBackThread, AgcmCharacter::UpdateMainAnimation, AgcmCharacter::LoadTemplateDefaultFace |
| `CBFilterModeMaterial` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmResourceLoader::CBInitAtomic |
| `GetAtomicUsrDataArrayInt` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindLoadEntry` | 28 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_HexStringToDWORD` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::_LoadColor, AgcChatMessage::_PushAndParseString, AgcmUINotice::_ParseMessage; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |

## AgcmTargeting (eingebaut 3, gemeinsamer Rumpf 2, nicht im Client 4, ohne Kandidat 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnRButtonDown` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AgcSenderWindow::OnRButtonDown |
| `CBDetailCollision` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::CBIntersectAtomic; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `SetRwCamera` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::OnAddModule; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplate` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `SetShowCursor` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackLButtonDownPickSomething` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLButtonDownPickNothing` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetCharacterClump` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTargetBase` | 48 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::AgcmTargeting, AgcmTargeting::OnMouseMove; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `TargetLast` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearTarget` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `TargetNearestDebug` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTargeting::OnInit |
| `TargetNextDebug` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTargeting::OnInit |

## AgpmCombat (gemeinsamer Rumpf 2, nicht als eigene Funktion 12, nicht im Client 15)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetHeroicDamageMin` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::CalcHeroicAttack; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `GetHeroicResistanceByHeroicClass` | 27 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetHeroicResistanceByAttackerHeroicClass` | 27 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::CalcHeroicAttack; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `GetPhysicalResistance` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::CalcPhysicalAttack; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `GetPhysicalBlockRate` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::IsShieldDefenseSuccess; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `GetSkillBlockRate` | 15 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetAdditionalHitRate` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::IsAttackSuccess; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `GetAdditionalEvadeRate` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::ProcessEvade; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `GetAdditionalDodgeRate` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::ProcessEvade; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `IsShieldDefenseSuccess` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::ProcessCombat; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `IsAttackSuccess` | 81 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::ProcessCombat; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `IsFirstSpiritAttackSuccess` | 46 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::ProcessCombat; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `IsSecondSpiritAttackSuccess` | 34 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::ProcessCombat; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `CalcHeroicAttack` | 44 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmCombat::CalcHeroicAttackForSkill, AgpmCombat::ProcessCombat; im Adressbereich der Klasse (0x00579270–0x0057A3C0) ist keine unbenannte Funktion mehr übrig |
| `CalcHeroicAttackForSkill` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CalcBasePhysicalAttackForSkill` | 45 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcSecondSpiritAttack` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcItemFirstSpiritAttack` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcItemFirstSpiritDefense` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcItemSecondSpiritAttack` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetWeaponTypeValue` | 57 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCharacterTypeValue` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetArmourAttributeInfo` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ProcessCombat` | 135 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `ProcessEvade` | 34 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CalcPenaltyExp` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcAtkPenaltyLevelGap` | 32 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |

## AgpmFactors (eingebaut 3, gemeinsamer Rumpf 16, nicht im Client 29, ohne Kandidat 20)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `IsUseFactor` | 16 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketFactor` | 125 | ohne Kandidat |  | Aufrufer im Client: AgpmFactors::MakePacketFactors, AgpmFactors::MakePacketFactorsOneType, AgpmFactors::MakePacketFactorsCharView; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketFactors` | 40 | ohne Kandidat |  | Aufrufer im Client: AgpmFactors::MakePacketFactor, AgpmFactors::MakePacketResult, AgpmItem::MakePacketItem; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketFactorsOneType` | 46 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::MakePacketSkillDIRT; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketResult` | 32 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketFactorsCharView` | 84 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::MakePacketCharView, AgpmOptimizedPacket2::MakePacketCharView; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketFactorsCharHPMax` | 65 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::MakePacketSyncMemberHPMax; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketFactorsCharHP` | 48 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakePacketFactorsItemView` | 38 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketMoney` | 28 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketItem` | 39 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::AddItemPacketToBuffer; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketItemRestrict` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketLevel` | 46 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::MakePacketCharLevel; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketFactorDiffer` | 41 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::MakePacketItem, AgpmItem::MakePacketItemInforMationResult, AgpmItem::MakePacketItemInforMationResult; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakePacketFactorDiffer` | 85 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::MakePacketItem, AgpmItem::MakePacketItemInforMationResult, AgpmItem::MakePacketItemInforMationResult; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetAttackableRange` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateFactor` | 176 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::UpdateFactor, AgpmEventFactors::ProcessUpdateEventFactors, AgpmEventFactors::ProcessUpdateFactor; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `UpdateFactor` | 100 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::UpdateFactor, AgpmEventFactors::ProcessUpdateEventFactors, AgpmEventFactors::ProcessUpdateFactor; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `InitUpdateFactor` | 29 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `InitUpdateFactor` | 29 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `FindCharacterClassIndex` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::StreamReadMasteryTxt; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CharacterTypeStreamWriteCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmFactors::OnAddModule |
| `CharacterTypeStreamWrite` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFactorTypeName` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFactorININame` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFactorDetail` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CopyFactorNotZero` | 19 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `CopyFactorNotZero` | 34 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `CopyFactorStatus` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddResultFactor` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddResultFactor` | 39 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackUpdateFactorParty` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorUI` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorSkillPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorHeroicPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorDamage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorView` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorMovement` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorBonusExp` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorHp` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorMp` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorMurdererPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorCharismaPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactorDurability` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CompareFactor` | 16 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::IsTargetFactorCharacter; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CompareFactor` | 44 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::IsTargetFactorCharacter; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CalcResultFactor` | 39 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CalcPercentFactor` | 103 | ohne Kandidat |  | Aufrufer im Client: AgpmFactors::CalcResultFactor; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetValue` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB, AgcmCharacter::CBReceiveAction, AgcmCharacter::InitCharacterBackThread |
| `SetValue` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::SetHPZero, AgcuEffIniMng::_Write_EffSet_txt, AgcuEffIniMng::_Write_EffBase_txt |
| `GetLevelBefore` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::GetLevelBefore, AgpmCharacter::GetLevelOriginal, AgpmCharacter::SetCharacterLevelLimit; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetMurderPoint` | 16 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SetExp` | 12 | nicht im Client |  | Aufrufer nur im Server (10); kein Treffer im Binary |
| `GetHP` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::GetHP; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetMaxHP` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::GetMaxHP; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetMP` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetMaxMP` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSP` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetMaxSP` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkillLevel` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkill, AgcmSkill::GetTwicePacketInteval, CUiCharacterProperty::_GetZeroBasePropertyByPassive; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `AllocAgpdFactor` | 18 | nicht im Client |  | Aufrufer nur im Server (7); kein Treffer im Binary |
| `FreeAgpdFactor` | 16 | nicht im Client |  | Aufrufer nur im Server (10); kein Treffer im Binary |
| `SetFactorDataName` | 11 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsMustSend` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmFactors::MakePacketFactor; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `PrintDataTypeLog` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmGrid (Kandidat unbestätigt 2, eingebaut 4, nicht im Client 4, ohne Kandidat 7, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCountByTemplate` | 24 | zugeordnet | `0x00587530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Init` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmAIDlg::OpenTemplates, AgcmAIDlg::OpenTemplate, AgcmCustomizeRender::AgcmCustomizeRender; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `InitGridMemoryPool` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLayer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRow` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StreamReadPolyMorphTable, AgcmEventEffectData::ReadCommonCharEffectData, AgcmEventEffectData::ReadConvertedArmourEffectData |
| `GetColumn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StreamReadPolyMorphTable, AgcmEventEffectData::ReadConvertedArmourEffectData, AgcmEventEffectData::ReadMovingSoundData |
| `GetItem` | 14 | Kandidat unbestätigt | `0x00587480` | Aufrufer im Client: AgcmCharacter::OnChagneEquipItemByEvolution, AgcmCharacter::OnEquipCharonForSummoner, AgcmCharacter::AttachRideClump; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `IsExistItemTemplate` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::HasItemTemplate; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `GetItemByTemplate` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::IsArchlordDungeonPoint, AgpmGrid::IsExistItemTemplate, AgpmItem::AutoInsertStackMerge; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `GetQuestItemByTemplate` | 22 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsMovalbeGrid` | 42 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Add` | 47 | Kandidat unbestätigt | `0x005873E0` | Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `AttachGridItemTextureData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIControl::OnAddModule |
| `IsLocked` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::RemoveCharacter, AgcmMap::ClearAllSectors; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `LockItem` | 38 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::LockGrid; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `ReleaseItem` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::RemoveStatus, AgpmItem::ReleaseGrid; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `IsFullGrid` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIEventItemRepair::OnMoveItem, AgcmUIGuildWarehouse::OnItemMovedOut, AgcmUIRefinery::OnMoveItem |
| `CheckEnoughItem` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmUIQuest2::CheckPointQuest; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |

## AgpmPathFind (eingebaut 4, nicht im Client 4, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `lock` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcaAnimation2::RemoveRtAnim, AgcaAnimation2::ReadRtAnim, AgcmEff2::CBLoadEffBase |
| `unlock` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmPathFind::pathFind |
| `initSearchNode` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmPathFind::AgpmPathFind |
| `reset` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: tagStParticleProfile::tagStParticleProfile, AgcmShrine::EnterGameMode |
| `getPathToExternalList` | 58 | ohne Kandidat |  | Aufrufer im Client: AgpmPathFind::pathFind; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `initStartPoint` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `initTargetPoint` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `pathFind` | 179 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `pathFind` | 110 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |

## ApAdmin (eingebaut 12, nicht im Client 2, ohne Kandidat 2, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetObjectCount` | 6 | zugeordnet | `0x004EA9C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCount` | 7 | zugeordnet | `0x004EA9A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHashMapINT32` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: ApAdmin::AddObject, ApAdmin::AddObject, ApAdmin::AddStringKey |
| `RemoveHashMapINT32` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: ApAdmin::RemoveObject, ApAdmin::RemoveObject |
| `ClearHashMapINT32` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApAdmin::InitializeObject, ApAdmin::RemoveObjectAll |
| `ClearHashMapstring` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApAdmin::InitializeObject, ApAdmin::RemoveObjectAll |
| `UpdateStringKey` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ChangeSkillTemplateName; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `IsObject` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpaCharacter::IsCharacter, AgpaCharacter::IsCharacter |
| `IsObject` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpaCharacter::IsCharacter, AgpaCharacter::IsCharacter |
| `RLock` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: ApAdmin::GlobalRLock |
| `WLock` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIMailBox::CBRemoveMail, AgpmAdmin::AdminLock, AgpmAdmin::OnReceive |
| `Release` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCustomizeRender::Render, AgcmEventEffect::CBRemoveAnimation, AgcmEventEffect::CopyCharAnimAttachedData |
| `GetCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcmEventNature::LoadTextureScriptFile, CUiExNPCMsgBoxGrid::OnWindowRender |
| `UpdateKey` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::ChangeUIName, AgpmEventTeleport::ChangeTeleportPointName, AgpmEventTeleport::ChangeTeleportGroupName; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `GlobalRLock` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GlobalWLock` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApmEventManager::RemoveEvent |
| `GlobalRelease` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApmEventManager::RemoveEvent |
| `SetNotUseLockManager` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## ApLockManager (eingebaut 4, nicht im Client 2, ohne Kandidat 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DeleteInstance` | 8 | ohne Kandidat |  | Aufrufer im Client: CAuResourceKeeperApp::~CAuResourceKeeperApp; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `GetCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcmEventNature::LoadTextureScriptFile, CUiExNPCMsgBoxGrid::OnWindowRender |
| `Lock` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmEventNature::OnIdle, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBLoadSector |
| `Unlock` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmEventNature::OnIdle, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBLoadSector |
| `SafeRemoveUnlock` | 11 | ohne Kandidat |  | Aufrufer im Client: ApMutualEx::Destroy, ApMutualEx::SafeRelease; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `RemoveCheck` | 10 | ohne Kandidat |  | Aufrufer im Client: ApLockManager::RemoveUnlock, ApLockManager::SafeRemoveUnlock, ApLockManager::AllUnlock; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SequenceLockforMultiple` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SequenceUnlockforMultiple` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SequenceLock` | 8 | ohne Kandidat |  | Aufrufer im Client: ApLockManager::InsertLock; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SequenceUnlock` | 11 | ohne Kandidat |  | Aufrufer im Client: ApLockManager::InsertLock; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `IsExistData` | 7 | ohne Kandidat |  | Aufrufer im Client: ApModuleManager::Dispatch; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `AllUnlock` | 9 | ohne Kandidat |  | Aufrufer im Client: ApModuleManager::Dispatch; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `RecursionLock` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: ApLockManager::SequenceLock |
| `RecursionUnlock` | 7 | ohne Kandidat |  | Aufrufer im Client: ApLockManager::SequenceUnlock, ApLockManager::AllUnlock; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |

## ApMemoryManager (eingebaut 2, nicht als eigene Funktion 2, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetAllocatedCount` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckBeginGuardByte` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: ApMemoryManager::NewObject, ApMemoryManager::DeleteObject; im Adressbereich der Klasse (0x004E6900–0x004E72E0) ist keine unbenannte Funktion mehr übrig |
| `CheckEndGuardByte` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: ApMemoryManager::NewObject, ApMemoryManager::DeleteObject; im Adressbereich der Klasse (0x004E6900–0x004E72E0) ist keine unbenannte Funktion mehr übrig |
| `GetAllocated` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: ApMemoryManager::NewObject, ApMemoryManager::DeleteObject |
| `SetAllocation` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: ApMemoryManager::NewObject, ApMemoryManager::DeleteObject |
| `GetEnable` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## ApModule (eingebaut 2, gemeinsamer Rumpf 2, nicht im Client 15, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ReleaseCallBackDataList` | 13 | ohne Kandidat |  | Aufrufer im Client: ApModule::~ApModule; kein unbenannter Kandidat mit Beleg unter 3383 unbenannten Funktionen im Klassenbereich |
| `ReleaseStreamDataList` | 13 | ohne Kandidat |  | Aufrufer im Client: ApModule::~ApModule; kein unbenannter Kandidat mit Beleg unter 3383 unbenannten Funktionen im Klassenbereich |
| `OnPreDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `Idle3` | 27 | ohne Kandidat |  | Aufrufer im Client: ApModuleManager::Idle3; kein unbenannter Kandidat mit Beleg unter 3383 unbenannten Funktionen im Klassenbereich |
| `AddIdleEvent2` | 19 | nicht im Client |  | Aufrufer nur im Server (6); kein Treffer im Binary |
| `AddIdleEvent3` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveIdleEvent` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveIdleEvent2` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveIdleEvent3` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetIdleEvent3` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxIdleEvent` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::AgcmUIGuideMessage |
| `SetMaxIdleEvent2` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxIdleEvent3` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMaxIdleEvent` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMaxIdleEvent2` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMaxIdleEvent3` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `m_fConstructorCB` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `m_fDestructorCB` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddPreReceiveModule` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnableIdle3` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `Receive` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcDebugWindow::RenderNetwork, AgcmUILogin::ParsePatchCodeString, CGameFramework::CheckPatchCode |

## ApModuleManager (eingebaut 1, nicht im Client 6, ohne Kandidat 6, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Dispatch` | 53 | zugeordnet | `0x004E35A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddModule` | 121 | zugeordnet | `0x004E3AD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveModule` | 36 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetModule` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcAuth::login, AgcmAdmin::OnAddModule, AgcmAdmin::GetUIMessageString; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakeSPClientExit` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeSPClientCrash` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnableModuleIdle3` | 59 | ohne Kandidat |  | Aufrufer im Client: ApModule::EnableIdle3; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Idle` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnIdle, AgcEngine::Debug_Idle; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Idle2` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnIdle, AgcEngine::Debug_Idle2; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Idle3` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Destroy` | 98 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmItem::ItemDestructorCB, AgcmObject::ReleaseObjectData; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetClockCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCashMall::SendPacketRefreshCash, AgcmCharacter::MoveSelfCharacter, AgcmCharacter::CharacterPosIdleProcess |
| `GetModuleCount` | 9 | ohne Kandidat |  | Aufrufer im Client: ApModuleManager::Destroy; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `WriteSlowIdleLog` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `WriteSlowDispatchLog` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## ApMutualEx (eingebaut 1, nicht als eigene Funktion 1, nicht im Client 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Release` | 22 | zugeordnet | `0x004E7CC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `WLock` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIMailBox::CBRemoveMail, AgpmAdmin::AdminLock, AgpmAdmin::OnReceive; im Adressbereich der Klasse (0x004E7B40–0x004E7D60) ist keine unbenannte Funktion mehr übrig |
| `ResetRemoveLock` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetNotUseLockManager` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: ApAdmin::SetNotUseLockManager |

## ApmMap (Kandidat unbestätigt 1, eingebaut 5, gemeinsamer Rumpf 7, nicht im Client 30, ohne Kandidat 26, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetSectorList` | 84 | zugeordnet | `0x005109E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetSkillDbgCB` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmSkill::OnInit |
| `IsPassThis` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCharList` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkill, ApmEventManager::GetAreaCharacters, ApmEventManager::GetAreaCharacters; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetCharList` | 105 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkill, ApmEventManager::GetAreaCharacters, ApmEventManager::GetAreaCharacters; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetCharList` | 118 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkill, ApmEventManager::GetAreaCharacters, ApmEventManager::GetAreaCharacters; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetCharList` | 121 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkill, ApmEventManager::GetAreaCharacters, ApmEventManager::GetAreaCharacters; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetNPCList` | 118 | ohne Kandidat |  | Aufrufer im Client: ApmMap::GetCharList, ApmMap::GetCharList, ApmMap::GetCharList; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetNPCList` | 121 | ohne Kandidat |  | Aufrufer im Client: ApmMap::GetCharList, ApmMap::GetCharList, ApmMap::GetCharList; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetMonsterList` | 116 | ohne Kandidat |  | Aufrufer im Client: ApmMap::GetCharList, ApmMap::GetCharList, ApmMap::GetCharList; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetMonsterList` | 120 | ohne Kandidat |  | Aufrufer im Client: ApmMap::GetCharList, ApmMap::GetCharList, ApmMap::GetCharList; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetObjectList` | 133 | ohne Kandidat |  | Aufrufer im Client: AgcmAmbOcclMap::searchAtomicById; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `DeleteSector` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::ReleaseSector, AgcmMap::__SetAutoLoadRange, AgcmMap::CBMyCharacterPositionChange2; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `DeleteChars` | 32 | ohne Kandidat |  | Aufrufer im Client: ApWorldSector::RemoveAllData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `MoveChar` | 37 | ohne Kandidat |  | Aufrufer im Client: ApmMap::UpdateChar; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `DeleteNPCs` | 31 | ohne Kandidat |  | Aufrufer im Client: ApmMap::DeleteChars; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `DeleteMonsters` | 31 | ohne Kandidat |  | Aufrufer im Client: ApmMap::DeleteChars; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `UpdateItem` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MoveItem` | 26 | ohne Kandidat |  | Aufrufer im Client: ApmMap::UpdateItem; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `UpdateObject` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MoveObject` | 25 | ohne Kandidat |  | Aufrufer im Client: ApmMap::UpdateObject; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `AttachSegmentData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackAddChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoveChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadSector` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackClearSector` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `LoadDivision` | 31 | ohne Kandidat |  | Aufrufer im Client: ApmMap::LoadAll; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `LoadAll` | 83 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::_BuildEffSetContainer, AgcmMap::LoadAll, AgcmMap::LoadAll; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SaveAll` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::SaveAll; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `ClearAllSector` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddObjectBlocking` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearAllObjectBlocking` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearAllHeightPool` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetHeight` | 9 | Kandidat unbestätigt | `0x00518800` | Aufrufer im Client: AgcmCharacter::CharacterPosIdleProcess, AgcmCharacter::InclinePlaneQuadruped, AgcmCharacter::InclinePlaneBiped; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `AddBindType` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearAllBindData` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: ApmMap::OnDestroy |
| `GetBindList` | 14 | ohne Kandidat |  | Aufrufer im Client: ApmMap::AddBindElementRect, ApmMap::GetBindData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `AddBindElementRect` | 16 | ohne Kandidat |  | Aufrufer im Client: ApmMap::AddBindElementCircle; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `AddBindElementCircle` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsChangedBind` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetBindData` | 40 | ohne Kandidat |  | Aufrufer im Client: ApmMap::IsChangedBind; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsSameRegion` | 8 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsSameRegionInvolveParent` | 13 | nicht im Client |  | Aufrufer nur im Server (7); kein Treffer im Binary |
| `GetLoadedDivisionInfo` | 15 | ohne Kandidat |  | Aufrufer im Client: ApmMap::AddLoadedDivision; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `EnumLoadedDivision` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::IsLoadedDivision; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `AddLoadedDivision` | 27 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveLoadedDivision` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveTempate` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveTemplate` | 61 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddRegion` | 16 | ohne Kandidat |  | Aufrufer im Client: ApmMap::LoadRegion; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetRegion` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::GetDefaultSky, AgcmMap::CreateCompactDataFromDetailInfo, AgcmMap::CheckSelfCharacterRegionChange; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `RemoveRegion` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveAllRegion` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveRegion` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadRegion` | 49 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadDimensionTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveDimensionTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddDimensionTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveDimensionTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetDimensionTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateDimension` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApWorldSector::SetupSector |
| `DestroyDimension` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReloadWorldMap` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CChatCmd::CallBack_OnReloadWorldmap |
| `SaveWorldMap` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveAllWorldMap` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApmMap::LoadWorldMap |
| `LoadRegioinPerculiaritySkulTid` | 12 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `LoadRegioinPerculiaritySkulRestrictionTime` | 12 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## ApmObject (eingebaut 5, gemeinsamer Rumpf 6, nicht im Client 3, ohne Kandidat 13)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AttachObjectData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::OnAddModule, AgcmEventEffect::OnAddModule, AgcmObject::OnAddModule |
| `CreateObject` | 8 | ohne Kandidat |  | Aufrufer im Client: ApmObject::AddObject, ApmObject::StreamRead, ApmObject::StreamRead; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `AddObject` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcaAnimation2::AddRtAnim, AgcaAnimation2::AddFlags, AgcaEventEffectData::CreateData; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `DeleteObject` | 30 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::CreateShareTexture, AcTextureList::MakeTempBitmap, CBmp::Release; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `DeleteObject` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::CreateShareTexture, AcTextureList::MakeTempBitmap, CBmp::Release; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `DeleteAllObject` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachObjectTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::OnAddModule, SequenceNumberManager::AttachTemplateSequenceData, AgcmGeometryDataManager::OnAddModule |
| `CreateTemplate` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::AddCharacterTemplate, AgpmItem::AddItemTemplate, AgpmQuest::AddTemplate; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `DestroyTemplate` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmCharacter::OnDestroy, AgpmCharacter::AddCharacterTemplate, AgpmCharacter::RemoveCharacterTemplate |
| `DestroyAllTemplate` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadItemTemplate, AgcmExportResource::ReadObjectTemplate, AgcmObject::ReloadObjectClump; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `AddObjectTemplate` | 13 | ohne Kandidat |  | Aufrufer im Client: ObjectLoader::AddTemplate, ApmObject::StreamReadTemplate; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `DeleteObjectTemplate` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWriteTemplate` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `StreamRead` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateStreamReadCB, AgcmExportResource::ReadUIINI, AgcmItem::ItemTemplateStreamReadCB; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `StreamWrite` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `StreamWrite` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `StreamWrite` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `StreamReadAllDivision` | 12 | ohne Kandidat |  | Aufrufer im Client: ApmObject::StreamReadAllDivisionVersion2; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `StreamReadAllDivision` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: ApmObject::StreamReadAllDivisionVersion2 |
| `StreamReadAllDivisionVersion2` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateInit` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRide, AgpmCharacter::OnOperationAdd, AgpmCharacter::StaticCharacterReadCB |
| `SetCallbackInitObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadSector` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadError` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## ApmOcTree (gemeinsamer Rumpf 1, nicht als eigene Funktion 11, nicht im Client 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetNode` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventEffect::RemoveAllConvertedItemGradeEventEffect, AgcmEventEffect::RemoveContinuativetSkillEventEffect, AgcmOcTree::RemoveCustomRenderDataFromOcTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `GetNode` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventEffect::RemoveAllConvertedItemGradeEventEffect, AgcmEventEffect::RemoveContinuativetSkillEventEffect, AgcmOcTree::RemoveCustomRenderDataFromOcTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `GetNode` | 32 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventEffect::RemoveAllConvertedItemGradeEventEffect, AgcmEventEffect::RemoveContinuativetSkillEventEffect, AgcmOcTree::RemoveCustomRenderDataFromOcTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `GetNode` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventEffect::RemoveAllConvertedItemGradeEventEffect, AgcmEventEffect::RemoveContinuativetSkillEventEffect, AgcmOcTree::RemoveCustomRenderDataFromOcTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `GetStartNode` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmEventNPCTrade::IsItemInGrid, ApmOcTree::GetNodeForInsert, ApmOcTree::GetLeafID; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `GetStartNode` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmEventNPCTrade::IsItemInGrid, ApmOcTree::GetNodeForInsert, ApmOcTree::GetLeafID; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `GetNodeID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CombineNodeChilds` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackInitRoot` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `DivideAllTree` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmOcTree::DivideToLeafTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `DivideAllChilds` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: ApmOcTree::DivideAllTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `OptimizeTree` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OptimizeChild` | 34 | nicht als eigene Funktion |  | Aufrufer im Client: ApmOcTree::OptimizeTree; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `SaveToFiles` | 135 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmRender::SaveAllOctrees; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |
| `SaveNode` | 24 | nicht als eigene Funktion |  | Aufrufer im Client: ApmOcTree::SaveToFiles; im Adressbereich der Klasse (0x00588390–0x00589A40) ist keine unbenannte Funktion mehr übrig |

## AuCryptManager (nicht im Client 9, ohne Kandidat 12)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetAlgorithm` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetPublicAlgorithmString` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetPrivateAlgorithmString` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetAlgorithmString` | 12 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::GetPublicAlgorithmString, AuCryptManager::GetPrivateAlgorithmString; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsPublicCopy` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsPrivateCopy` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeRandomKey` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `InitializeActor` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `InitializeActor` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `InitializeActorPublic` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmStartupEncryption::CBPublic, AgcmStartupEncryption::CBDynCodePublic, AuCryptManager::InitializeActor; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `InitializeActorPrivate` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmStartupEncryption::CBPublic, AgcmStartupEncryption::CBDynCodePrivate, AuCryptManager::InitializeActor; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Encrypt` | 15 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::EncryptByPublic, AuCryptManager::EncryptByPrivate, AuPacket::EncryptPacket; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Decrypt` | 15 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::DecryptByPublic, AuCryptManager::DecryptByPrivate, AuSeed::Decrypt; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `DecryptByPublic` | 12 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::Decrypt, AuCryptManager::Decrypt; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `EncryptByPrivate` | 12 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::Encrypt, AuCryptManager::Encrypt; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `DecryptByPrivate` | 12 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::Decrypt, AuCryptManager::Decrypt; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsUseDynCode` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmStartupEncryption::CBDynCodePublic, AgcmStartupEncryption::CBDynCodePrivate, AuCryptManager::InitServer; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `InitServer` | 25 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetClientDynCode` | 14 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::GetClientDynCodePublic, AuCryptManager::GetClientDynCodePrivate; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetClientDynCodePublic` | 13 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::GetClientDynCode; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetClientDynCodePrivate` | 13 | ohne Kandidat |  | Aufrufer im Client: AuCryptManager::GetClientDynCode; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AuPacket (eingebaut 1, nicht als eigene Funktion 1, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakeStaticPacket` | 138 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FreePacket` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAdmin::SendAdminClientRequest, AgcmArchlord::SendRequestEvent, AgcmAuction::SendSelect; im Adressbereich der Klasse (0x004E9F10–0x004EA850) ist keine unbenannte Funktion mehr übrig |
| `FreeStaticPacket` | 7 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `FreeEncryptBuffer` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AuPacket::EncryptPacket |
