# AgcmRender (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmRender` (Szenen-Rendering: Listen je Renderklasse, Beleuchtung, Octree, Blend-Pässe) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmRender`. Alle Adressen gelten nur für den 2017er Build. Die Klasse erbt zusätzlich `CRenderFadeInOut`, `CUsableRwFrameTable`, `CD3DFxMng` und `CEdgeRender`, deren Code im selben Adressbereich (`0x005AE100`–`0x005BC7A0`) liegt.

## Kernbefund

- **Abdeckung:** 31 von 196 Quellmethoden sind einer Binary-Adresse zugeordnet (siehe Tabelle); das Modul besteht aus großen, stark ineinander gefalteten Funktionen mit wenig Zeichenketten, und die RenderWare-Bibliothek ist ohne Symbole eingelinkt. Die Zuordnung konzentriert sich deshalb auf den Hauptpfad `Render`.
- **Render-Pipeline unverändert:** `Render` löst die Callbacks in der Reihenfolge 0, 10, 1, 3, 2, 11 aus (IDs wie in der Quelle) und ruft die Pässe in der Reihenfolge der Quelle auf: Welt, Octree, Terrain-Shadow2, nicht-transparent, Occlusion, UV-Animation, Ambient, Alpha-Test, Skin-Pipe, transparent, Blend (sortiert/unsortiert), unsichtbare Atomics, `ClearLists`.
- **Lichtfälle:** `RenderAtomic` kennt sieben Sonderlicht-Zustände (Login-Auswahl, Schatten, Quest-Objekt, Betäubung, Einfrieren, Vergiftung, Picking) mit eigenen Farben; Werte und Reihenfolge entsprechen `enumLightingType`.
- **Lua:** `OnLuaInitialize` registriert genau die drei Funktionen der Quelle (`SetOcLineCheck`, `GetOcLineCheck`, `SetCharacterLightEffect`).
- **Sichtbare Abweichungen:** keine im Ablauf der gelesenen Funktionen; Unterschiede in nicht zugeordneten Methoden sind nicht ausgeschlossen.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmRender.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetDrawCollisionTerrain` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 1 | `SetDrawCollisionObject` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 2 | `IsMaptoolBuild` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 3 | `OnAddModule` | `0x005B5E30` | 205 | Zeichenketten/Konstanten (geprüft) |
| 4 | `OnInit` | `0x005B7A00` | 1053 | von Hand geprüft |
| 5 | `OnDestroy` | `0x005B8010` | 153 | von Hand geprüft |
| 6 | `OnIdle` | `0x005AE530` | 311 | von Hand geprüft |
| 7 | `OnCameraStateChange` | `0x005AE670` | 52 | von Hand geprüft |
| 8 | `OnLuaInitialize` | `0x005AE6B0` | 60 | von Hand geprüft |
| 9 | `SetMainFrame` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 10 | `Render` | `0x005BA490` | 2008 | Zeichenketten/Konstanten (geprüft) |
| 11 | `SetWorldCamera` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 12 | `SetLight` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 13 | `MyWorldAddAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 14 | `MyWorldAddClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 15 | `MyWorldRemoveAtomic` | `0x005B3F60` | 350 | von Hand geprüft |
| 16 | `MyWorldRemoveClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 17 | `AddClumpToRenderWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 18 | `RemoveClumpFromRenderWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 19 | `AddAtomicToRenderWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 20 | `RemoveAtomicFromRenderWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 21 | `UpdateBoundingSphere` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 22 | `AddLightToRenderWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 23 | `RemoveLightFromRenderWorld` | `0x005B7E20` | 347 | Aufrufgraph (geprüft) |
| 24 | `GetLightByAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 25 | `CB_LIGHT_UPDATE` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 26 | `CB_LIGHT_RENDER` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 27 | `MyWorldGetAtomicLocalLightsCallBack` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 28 | `MyWorldGetAtomicLocalLightsDummyCallBack` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 29 | `SetAtomicListCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 30 | `InitAtomicSetRenderCallBack` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 31 | `AddClumpToWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 32 | `AddAlphaBModeClumpToWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 33 | `AddBillAtomicToWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 34 | `AddAtomicToWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 35 | `AddAlphaBModeAtomicToWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 36 | `AtomicSetInfoBlendAlpha` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 37 | `InitAtomicDatas` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 38 | `InitAtomicDatas` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 39 | `InitAtomicDatasCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 40 | `AddClumpFromUDA` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 41 | `SetRenderCBFromUDACB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 42 | `RemoveClumpFromWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 43 | `RemoveAtomicFromWorld` | `0x005B40C0` | 235 | Aufrufgraph (geprüft) |
| 44 | `ReturnDefOriginalRenderCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 45 | `CheckAlphaAtomicFromClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 46 | `CheckAlphaAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 47 | `AtomicSetAlpha` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 48 | `AtomicSetNonAlpha` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 49 | `AtomicSetAmbient` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 50 | `AtomicSetAlphaFunc` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 51 | `AtomicSetLastZWrite` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 52 | `GetCameraDistance` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 53 | `ClearLists` | `0x005B8880` | 679 | von Hand geprüft |
| 54 | `DefaultAtomicListTestRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 55 | `ImmediateAtomicListTestRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 56 | `DefaultAtomicRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 57 | `ImmediateAtomicRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 58 | `DefaultTerrainRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 59 | `ImmediateTerrainRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 60 | `RenderWorldAtomics` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 61 | `RenderMyCamera` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 62 | `ProcessBillboardDraw` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 63 | `RenderAtomic` | `0x005AEC10` | 996 | Zeichenketten/Konstanten (geprüft) |
| 64 | `RenderSortedBlendAtomics` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 65 | `RenderNotSortedBlendAtomics` | `0x005AF010` | 953 | Aufrufreihenfolge in `Render` + Größe |
| 66 | `RenderNonAlphaAtomics` | `0x005AF3D0` | 97 | von Hand geprüft |
| 67 | `RenderAlphaAtomics` | `0x005B38F0` | 76 | von Hand geprüft |
| 68 | `RenderAmbientAtomics` | `0x005AF440` | 145 | von Hand geprüft |
| 69 | `RenderAlphaFuncAtomics` | `0x005AF4E0` | 139 | von Hand geprüft |
| 70 | `RenderSkinPipeBlendAtomics` | `0x005AF570` | 1125 | Aufrufreihenfolge in `Render` + Größe |
| 71 | `RenderSkinPipeAtomics` | `0x005AF9F0` | 93 | von Hand geprüft |
| 72 | `RenderSkinPipeAlphaAtomics` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 73 | `RenderSkinPipeAlphaFuncAtomics` | `0x005AFA50` | 136 | von Hand geprüft |
| 74 | `RenderUVAnimAtomics` | `0x005AFAE0` | 284 | Aufrufreihenfolge in `Render` + Größe |
| 75 | `RenderLastZWriteAtomics` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 76 | `TerrainDataSet` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 77 | `RenderCallbackForAmbientAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 78 | `RenderCallbackForAlphaFuncAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 79 | `RenderCallbackForBlendAtomicNotSort` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 80 | `RenderCallbackForAlphaAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 81 | `RenderCallbackForNonAlphaAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 82 | `RenderCallbackForSkinPipe` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 83 | `RenderCallbackForSkinPipeBlend` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 84 | `RenderCallbackForSkinPipeAlpha` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 85 | `RenderCallbackForSkinPipeAlphaFunc` | `0x005BB450` | 221 | Zeichenkette |
| 86 | `RenderCallbackForUVAnim` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 87 | `RenderCallbackForUVAnimSkin` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 88 | `RenderCallbackForLastZWrite` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 89 | `RenderCallbackForNone` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 90 | `RenderCallbackForAmbientAtomicBill` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 91 | `RenderCallbackForAlphaFuncAtomicBill` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 92 | `RenderCallbackForAlphaAtomicBill` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 93 | `RenderCallbackForBlendAtomicNotSortBill` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 94 | `RenderCallbackForNonAlphaAtomicBill` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 95 | `RenderCallbackForBlendAtomicBill` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 96 | `SetCallbackCustomRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 97 | `SetCallbackPreRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 98 | `SetCallbackPostRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 99 | `SetCallbackPostRender2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 100 | `SetCallbackPostRenderOcTreeClear` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 101 | `SetCallbackRemoveAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 102 | `SetCallbackRemoveClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 103 | `SetCallbackOctreeUDASet` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 104 | `SetCallbackOctreeIDSet` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 105 | `SetCallbackAddAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 106 | `SetCallbackAddClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 107 | `RenderWorldForAllIntersections` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 108 | `CBWorldIntersection` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 109 | `GeometryMaterialFlagOff` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 110 | `GeometryMaterialFlagOn` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 111 | `OriginalAtomicRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 112 | `OriginalClumpRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 113 | `SetUVAnimRenderCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 114 | `ReturnUVAnimRenderCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 115 | `RenderClumpOriginalDefaultRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 116 | `UpdateDistanceForTool` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 117 | `AddCustomToBlendRenderList` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 118 | `ResetLighting` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 119 | `CustomizeLighting` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 120 | `SetSectorDistanceC` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 121 | `SetSectorDistanceA` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 122 | `CalcBoundingSphere` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 123 | `AddTerrainToSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 124 | `AddAtomicToSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 125 | `AddClumpToSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 126 | `CallBackForEnumAtomicAddSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 127 | `RemoveAtomicFromSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 128 | `RemoveClumpFromSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 129 | `AddCustomRenderToSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 130 | `RemoveCustomRenderFromSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 131 | `CallBackForEnumAtomicRemoveSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 132 | `RenderCustomObjects` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 133 | `CBInitSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 134 | `CBRemoveSector` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 135 | `CBInitSectorData` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 136 | `CBRemoveSectorData` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 137 | `WorldToAtomicRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 138 | `WorldToAtomicFrustumRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 139 | `CullModeWorldRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 140 | `CalcWorldBoundingSphere` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 141 | `SetBoundingSphereFromUDA` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 142 | `SetBoundingSphereFromUDA` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 143 | `CallBackForEnumAtomicforSetBSFromUDA` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 144 | `AddUpdateInfotoClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 145 | `AddUpdateInfotoAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 146 | `RemoveUpdateInfoFromClump` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 147 | `RemoveUpdateInfoFromAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 148 | `RemoveUpdateInfoFromClump2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 149 | `RemoveUpdateInfoFromAtomic2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 150 | `RemoveUpdateInfoFromClump3` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 151 | `RemoveUpdateinfoFromAtomic3` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 152 | `StreamReadClumpRenderType` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 153 | `StreamWriteClumpRenderType` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 154 | `GetRenderTypeName` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 155 | `GetRenderBlendModeName` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 156 | `SetRenderTypeCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 157 | `ClumpSetRenderType` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 158 | `SetRenderTypeCheckCustDataCB` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 159 | `ClumpSetRenderTypeCheckCustData` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 160 | `MakeOctrees` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 161 | `SaveAllOctrees` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 162 | `AddCustomRenderObject` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 163 | `RemoveCustomRenderObject` | `0x005B7840` | 234 | von Hand geprüft |
| 164 | `RenderCallbackForAlphaAtomic2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 165 | `RenderCallbackForBlendAtomic2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 166 | `RenderCallbackForLastBlendAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 167 | `RenderCallbackForAlphaAtomicBill2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 168 | `RenderCallbackForBlendAtomicBill2` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 169 | `_GetSortFactor` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 170 | `InsertPreListOcTree` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 171 | `InsertPreListWorld` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 172 | `InsertPreListCustom` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 173 | `GetWorldPosToScreenPos` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 174 | `UpdateOBufferAndDrawTest` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 175 | `UpdateOBufferAndDrawNotTest` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 176 | `IsExcept` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 177 | `OcTreeModeRender` | `0x005B6D60` | 1947 | von Hand geprüft |
| 178 | `SetTerrainOccluderBoxs` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 179 | `OcTreeChildRender` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 180 | `SetMaxHeightTable` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 181 | `SetOccluderLine` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 182 | `RenderCallbackForVSFadeAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 183 | `RenderCallbackForSpecialRendering` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 184 | `ProcessFadeAtomic` | `0x005B0F80` | 898 | Zeichenketten/Konstanten (geprüft) |
| 185 | `SetDirectionalLightAdjust` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 186 | `SetAmbientLightAdjust` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 187 | `GetCameraDistanceOnXZ` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 188 | `AtomicAmbOcclMVLRenderCallBack` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |
| 189 | `RenderAmbOcclMVLAtomics` | `0x005B2C70` | 1979 | Aufrufreihenfolge in `Render` + Größe |
| 190 | `RenderInvisibleAtomics` | `0x005B3440` | 586 | Zeichenkette |
| 191 | `_RenderBlendAtomic_BillBoard` | `0x005B50B0` | 245 | Aufrufreihenfolge in `Render` + Größe |
| 192 | `_RenderBlendAtomic_LastBlended` | `0x005B3C90` | 76 | Aufrufreihenfolge in `Render` + Größe |
| 193 | `_RenderBlendAtomic` | `0x005B51B0` | 210 | Aufrufreihenfolge in `Render` + Größe |
| 194 | `_ChangeRenderStateForBlendAtomic` | `0x005B1850` | 320 | Aufrufgraph (geprüft) |
| 195 | `_RestoreRenderStateForBlendAtomic` | – | | nicht zugeordnet (inline, eingefaltet oder ohne eindeutigen Anker) |

31 von 196 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmRender` (`0x005B8E00`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xC00` | `m_pApmOcTree` | `MyWorldRemoveAtomic`: `GetModule("ApmOcTree")`; `[+0xB84]` im Modul ist `m_bOcTreeEnable` |
| `0xC1C … 0xC28 / 0xC2C … 0xC38` | `m_colorOriginalAmbient / m_colorOriginalDirect` | `OnIdle` kopiert die Lichtfarben (`+0x18..0x24` der RpLight) |
| `0xC3C` | `m_colorBlack` | `RenderAmbientAtomics` setzt die Ambient-Farbe darauf |
| `0xC74` | `m_pViewMatrixAt` | `OnIdle`: `[+0xCA0]+0x40` |
| `0xC7C` | `m_listWorldClumps` | `OnDestroy`: erste freigegebene Liste |
| `0xC90 / 0xC94 / 0xC98` | `m_ulLastTick / m_ulCurTick / m_ulCurTickDiff` | `OnIdle` |
| `0xCA0` | `m_pCamera` | `OnIdle`, `OnCameraStateChange` |
| `0xCA4 / 0xCA8` | `m_pAmbientLight / m_pDirectLight` | `OnIdle`, `RenderAtomic` |
| `0xCC0 / 0xCC4` | `m_iCameraRasterWidth / m_iCameraRasterHeight` | `OnCameraStateChange` |
| `0xCC8` | `m_fFogConstant.x` | `OnIdle`: `min(Dichte × 1,4427, 1)` |
| `0xCE0` | `m_iRenderCount` | `OnIdle` setzt 0 (Quelle: `Render` bricht ab Zähler ≥ 2 ab) |
| `0xD14 … 0xE70` | `Render-Listen (siehe Tabelle)` | `ClearLists` |
| `0xEAC / 0xEB0` | `m_listCustomRender / m_listLocalLight` | `OnDestroy`, `RemoveCustomRenderObject` |
| `0xF14` | `m_pInvisibleMaterial[5]` | `OnDestroy`: fünf Materialien freigegeben |
| `0xF2C` | `m_bUseCullMode` | `MyWorldRemoveAtomic` |
| `0xF3C … 0xFCC` | `Lichtfarben für Sonderstatus` | siehe Tabelle Sonderbeleuchtung |

## Ablauf von Render() (0x005BA490)

Reihenfolge der Schritte im Binary, gegen `AgcmRender::Render` der Quelle gelesen. Die Callback-IDs sind gegenüber der Quelle unverändert (`AGCMRENDER_CB_*`: 0 PRERENDER, 1 POSTRENDER, 2 POSTRENDER2, 3 POSTRENDER_OCTREE_CLEAR, 10 MTEXTURE_RENDER, 11 CUSTOM_RENDER); sie werden im Binary in genau dieser Reihenfolge ausgelöst: 0, 10, 1, 3, 2, 11.

| Schritt | Quelle | Binary | Beleg |
|---:|---|---|---|
| 1 | `ApAutoWriterLock`, `AuAutoLock` (ResourceLoader) | Sperren am Anfang, `GetModule("AgcmResourceLoader")` | gelesen |
| 2 | Render-States (Fog-Ende, BlendOp, Blend, ZWrite, Texturstufe 0) | `0x004C9CA0`/`0x004C9D10` (`RwRenderStateSet`/`RwD3D9SetTextureStageState`) | gelesen |
| 3 | `EnumCallback(PRERENDER)` | `EnumCallback(0)` | Konstante |
| 4 | `RpWorldRender(m_pWorld)` | `0x00431C40` | Position |
| 5 | Octree-Pfad: `OcTreeModeRender`, `UpdateOBufferAndDraw…`; sonst `RenderWorldAtomics`, `RenderCustomObjects`, `CullModeWorldRender` | `OcTreeModeRender` (`0x005B6D60`) und weitere, teils nicht zugeordnete Teilpässe (`0x005B41B0`, `0x005B95E0`, `0x005B9640`, `0x005BA120`, `0x005B9EF0`) | Teilweise |
| 6 | `TerrainDataSet`, Shadow2-Terrainpass | `0x005B14F0` (Vermutung für `TerrainDataSet`), Schleifen über die Shadow2-Liste | Position |
| 7 | `EnumCallback(MTEXTURE_RENDER)` | `EnumCallback(10)` | Konstante |
| 8 | `RenderNonAlphaAtomics` | `0x005AF3D0` (Hash-Liste `+0xD14`, 7 Buckets) | gelesen |
| 9 | `RenderAmbOcclMVLAtomics` | `0x005B2C70` | Größe (316 Quellzeilen ↔ 1979 Byte) |
| 10 | `RenderUVAnimAtomics` (erster Aufruf) | `0x005AFAE0` (wird zweimal aufgerufen, wie in der Quelle) | Aufrufanzahl |
| 11 | `RenderAmbientAtomics` | `0x005AF440` (Ambient auf Schwarz, danach `+0xC1C` zurück) | gelesen |
| 12 | `RenderAlphaFuncAtomics` | `0x005AF4E0` (Alpha-Test-Referenz 220 = `0xDC`, danach 0) | gelesen |
| 13 | `RenderSkinPipeAtomics` | `0x005AF9F0` (Liste `+0xE50`) | gelesen |
| 14 | `RenderSkinPipeAlphaFuncAtomics` | `0x005AFA50` (Liste `+0xE70`, Referenz 220) | gelesen |
| 15 | `RenderUVAnimAtomics` (zweiter Aufruf) | `0x005AFAE0` | Aufrufanzahl |
| 16 | `RenderAlphaAtomics` | `0x005B38F0` (Map `+0xD68`) | gelesen |
| 17 | `RenderSkinPipeAlphaAtomics`, `RenderLastZWriteAtomics` | inline (`RenderAtomic`-Schleifen in `Render`) | Position |
| 18 | `RenderSkinPipeBlendAtomics` | `0x005AF570` | Größe |
| 19 | `EnumCallback(POSTRENDER)`, `EnumCallback(POSTRENDER_OCTREE_CLEAR)` | `EnumCallback(1)`, `EnumCallback(3)` | Konstante |
| 20 | `RenderSortedBlendAtomics` | inline: `_RenderBlendAtomic_BillBoard` (`0x005B50B0`), `_RenderBlendAtomic_LastBlended` (`0x005B3C90`), `_RenderBlendAtomic` (`0x005B51B0`) | Quelle gelesen, Reihenfolge |
| 21 | `RenderNotSortedBlendAtomics` | `0x005AF010` | Größe (174 Zeilen ↔ 953 Byte) |
| 22 | `EnumCallback(POSTRENDER2)` | `EnumCallback(2)` | Konstante |
| 23 | `RenderInvisibleAtomics` | `0x005B3440` | Zeichenkette |
| 24 | `EnumCallback(CUSTOM_RENDER)`, `ClearLists` | `EnumCallback(11)`, `ClearLists` (`0x005B8880`), danach Sperren freigeben | gelesen |

## Sonderbeleuchtung in RenderAtomic (0x005AEC10)

`RenderAtomic` wählt je nach `customLightStatus` des Clumps (Byte `+0x36` der Render-Info) andere Lichtfarben; die Farben liegen in `AgcmRender` (je `RwRGBAReal`, 16 Byte). Die Fälle entsprechen `enumLightingType` der Quelle:

| Wert | Name | Ersetzte Farbe | Offset |
|---:|---|---|---|
| 1 | `LIGHT_LOGIN_SELECT` | Richtungslicht = `m_lightColorAtLoginSelect[1]` | `+0xF6C` |
| 2 | `LIGHT_IN_SHADOW` | Richtungslicht = `m_lightColorInShadow[1]`, Ambient = `[0]` | `+0xF4C`, `+0xF3C` |
| 3 | `LIGHT_QUEST_OBJECT` | Ambient = `m_lightColorOfQuestObject[0]` | `+0xF7C` |
| 4 | `LIGHT_STATUS_STUN` | Ambient = `m_lighterColorBySpecialStatus[0]` | `+0xFAC` |
| 5 | `LIGHT_QUEST_FREEZE` | Ambient = `m_lighterColorBySpecialStatus[1]` | `+0xFBC` |
| 6 | `LIGHT_QUEST_POISON` | Ambient = `m_lighterColorBySpecialStatus[2]` | `+0xFCC` |
| 7 | `LIGHT_PICKING` | Ambient = `m_lightColorPicking` | `+0xF9C` |

Zusätzlich verändert `SetCharacterLightEffect` (Lua) die Farbe zeitabhängig: Eine Dreieckswelle über den Engine-Taktzähler (`DAT_009A1D18+0x12E24`) mischt zwei Farben (Typ 1 und 2) mit der Periode `2 × Dauer` (Typ 2: Standardperiode 1000 ms).

## Lua-Funktionen

Tabelle `MVLuaGlue` bei `0x0094FE34`, registriert durch `OnLuaInitialize` (`0x005AE6B0`); wie in der Quelle genau drei Einträge:

| Lua-Name | Funktionszeiger |
|---|---|
| `SetOcLineCheck` | `0x005B2840` |
| `GetOcLineCheck` | `0x005B2870` |
| `SetCharacterLightEffect` | `0x005B28B0` |

Die drei Funktionen sind in der Ghidra-Projektkopie nicht als Funktionen angelegt (kein Dekompilat); die Zeiger stammen aus der Tabelle.

## Render-Listen (Buckets)

`ClearLists` (`0x005B8880`) setzt die Hash-Listen (je 7 Einträge, `R_HASH_SIZE` = 7) zurück:

| Liste | Offset | Verwendet von |
|---|---|---|
| `m_listNonAlpha` | `+0xD14` | `RenderNonAlphaAtomics` |
| `m_listAmbient` | `+0xD30` | `RenderAmbientAtomics` |
| `m_listAlphaFunc` | `+0xD4C` | `RenderAlphaFuncAtomics` |
| `m_listSkinning` | `+0xE50` | `RenderSkinPipeAtomics` |
| `m_listSkinningAlphaFunc` | `+0xE70` | `RenderSkinPipeAlphaFuncAtomics` |
| `m_mapAlpha` | `+0xD68` | `RenderAlphaAtomics` |
| `m_BlendAtomics` | `+0xD80` | `_RenderBlendAtomic*` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`Render`-Ablauf, die Listenpässe, `RenderAtomic`-Lichtfälle, `OnIdle`, `OnDestroy`, `OnCameraStateChange`, `ClearLists`, `MyWorldRemoveAtomic`, `RemoveCustomRenderObject`).
- `RenderSortedBlendAtomics` ist im Binary in `Render` eingefaltet (inline); `RenderSkinPipeAlphaAtomics` und `RenderLastZWriteAtomics` ebenfalls.

## Grenzen

- Zugeordnet sind überwiegend die Pässe in `Render` und die Lebenszyklus-Funktionen. Rund 160 Methoden (Hinzufügen/Entfernen von Atomics und Clumps, Sektorverwaltung, Octree-Hilfen, Fade/Update-Info, Callback-Setter) sind nicht einzeln adressiert; die `SetCallback*`-Setter sind mit gleichartigen Funktionen anderer Module zusammengefaltet.
- Die Einträge „Größe“ und „Aufrufanzahl“ beruhen auf der Position in `Render` und der Quellgröße und wurden nicht Zeile für Zeile gelesen; „gelesen“ heißt: Dekompilat und Quelle verglichen.
- Die Farbwerte der Sonderlichter und weitere Konstanten (Konstruktor, `OnInit`) wurden nicht ausgewertet.
- Nicht untersucht sind die Basisklassen-Teile (`CRenderFadeInOut`, `CD3DFxMng`, `CEdgeRender`), der Shader-Pfad ([`AgcmPostFX`](AgcmPostFX.md)) und die RenderWare-Aufrufe selbst.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 10, eingebaut: 29, gemeinsamer Rumpf: 11, nicht im Client: 27, ohne Kandidat: 79, zugeordnet: 17.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsExcept` | 64 | `0x005B05F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAtomicFromSector` | 39 | `0x005B3940` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddAtomicToSector` | 30 | `0x005B4AF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateOBufferAndDrawTest` | 113 | `0x005B9EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AtomicPreRender` | 67 | `0x005B9C40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddTerrainToSector` | 10 | `0x005B02A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCustomToBlendRenderList` | 19 | `0x005B9560` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MyWorldAddAtomic` | 96 | `0x005B5F00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LightValueUpdate` | 18 | `0x005B1370` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetWorldPosToScreenPos` | 29 | `0x005B0530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveUpdateInfoFromClump` | 24 | `0x005B3B50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CullModeWorldRender` | 126 | `0x005B9640` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCustomRenderFromSector` | 14 | `0x005B3A60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CustomizeLighting` | 4 | `0x005B01F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderWorldForAllIntersections` | 44 | `0x005AFF50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddAtomicToWorld` | 30 | `0x005BC6F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddLightToRenderWorld` | 93 | `0x005B58A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `AddClumpToWorld` (`0x005BC5E0`), `RemoveClumpFromWorld` (`0x005BC5E0`), `RenderCallbackForBlendAtomic` (`0x005BB920`), `RenderCallbackForBlendAtomicBill` (`0x005BB920`), `RenderCustomObjects` (`0x005BA120`), `AddUpdateInfotoClump` (`0x005BC5E0`), `AddCustomRenderObject` (`0x005B4C20`), `InsertPreListWorld` (`0x005B6780`), `UpdateOBufferAndDrawNotTest` (`0x005BA120`), `SetTerrainOccluderBoxs` (`0x005B6780`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmPostFX`](AgcmPostFX.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmCamera2`](AgcmCamera2.md), [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmEventPointLight`](AgcmEventPointLight.md), [`AgcmGlare`](AgcmGlare.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmItem`](AgcmItem.md), [`AgcmLODManager`](AgcmLODManager.md), [`AgcmLensFlare`](AgcmLensFlare.md), [`AgcmMap`](AgcmMap.md), [`AgcmNatureEffect`](AgcmNatureEffect.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmPostFX`](AgcmPostFX.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmShadowmap`](AgcmShadowmap.md), [`AgcmSound`](AgcmSound.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmTuner`](AgcmTuner.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUVAnimation`](AgcmUVAnimation.md), [`ApmOcTree`](ApmOcTree.md)
