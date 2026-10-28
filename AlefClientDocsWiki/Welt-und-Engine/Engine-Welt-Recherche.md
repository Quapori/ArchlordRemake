# AlefClient Engine/World Research

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Welt, Engine und Rendering](Index.md)*

Stand: 2026-09-05

Quellen:
- `alefclient.pseudocode.c`
- `alefclient.disasm.txt`
- `engine_keyword_xrefs.tsv`
- installierte Laufzeitdaten unter `C:\Spiele\Archlord`

Die Analyse ist statisch. `alefclient.exe` wurde nicht ausgefuehrt.

## 1. RenderWare-artige Engine

Der Client ist nicht nur "RenderWare-artig", sondern nutzt eindeutig RenderWare-Konzepte und D3D9-RenderWare-Pipelines.

Harte Binary-Belege:
- `Error initializing RenderWare.` in `FUN_0059bd40`
- `RenderWare Application` in `FUN_0064d8e0`
- [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md):LoadClump`-Fehlerstrings in `FUN_00664a80`
- `RwStreamOpen`, `RwStreamReadChunkHeaderInfo`, `RpClumpStreamRead`
- Pipeline-Strings:
  - `nodeD3D9SkinAtomicAllInOne.csl`
  - `nodeD3D9AtomicAllInOne.csl`
  - `nodeD3D9WorldSectorAllInOne.csl`
  - `nodeD3D9SubmitNoLight.csl`
  - `myNodeD3D9AtomicAllInOne`
  - `PVSWorldSector.csl`

Wichtige Schlussfolgerung:
- `RpClump` ist das zentrale Modell-/Charakter-Containerformat.
- `RpAtomic` ist die einzelne renderbare Mesh-Einheit.
- `RwStream` wird fuer gepackte/Memory-basierte Asset-Ladevorgaenge benutzt.
- Die Engine haengt eigene D3D9-All-In-One-Nodes in RenderWare-Pipelines ein.

Besonders wertvolle Funktionen:
- `FUN_00664a80`: Clump-Ladepfad, nutzt RenderWare-Stream und `RpClumpStreamRead`.
- `FUN_00410e20`: grosser Ressourcen-/Texture-Pfad; Ghidra-Timeout, aber viele Texture-Pfade sichtbar.
- `FUN_0067224f0`/Effektbereich: Effekt-Clumps werden geladen/geklont; Fehlerstring `RpClump Load/clone Failed`.

## 2. Vertex- und Pixel-Shader

Der wichtigste echte Shaderpfad sitzt im High-Water-System.

Shader-Belege:
- `vs.1.1` in `FUN_00649690`
- `ps.1.4` in `FUN_00649690`
- `ps.1.1` in `FUN_00649690`
- weitere Shaderstrings um `FUN_007d...`/D3DX-Effektcompiler-Spuren im Pseudocode

Wasser-Vertexshader:
- erwartet Position, Normal, Blendweight, Texcoord0 und Tangent
- berechnet sinusfoermige Wasserverformung
- erzeugt normalisierte Normalen/Tangenten/Binormalen neu
- erzeugt Reflection-UVs
- animiert zwei Bumpmap-UV-Sets ueber Zeit
- uebergibt View- und Light-Vektoren in Tangent Space
- nutzt Vertex-Alpha/Blendweight fuer Wassertransparenz

Pixelshader `ps.1.4`:
- sampelt zwei Bumpmaps
- mittelt/skalierte Bump-Offsets
- berechnet View dot Normal und Reflection-Vektor
- sampelt Reflection-Map
- sampelt Fresnel-Lookup
- addiert Specular-Highlight
- gibt Alpha aus Vertex/Interpolant weiter

Pixelshader `ps.1.1`:
- einfacherer Fallbackpfad
- kombiniert zwei Bumpmaps und Reflection/Farbe
- nutzt weniger Instruktionen und einfachere Specular-/Fresnel-Naeherung

HWater-Statusfelder aus dem Parser:
- `DirX0..`, `DirY0..`
- `Height0..`
- `Speed0..`
- `TexX0`, `TexX1`, `TexY0`, `TexY1`
- `ReflectionWeight`
- `AlphaMin`, `AlphaMax`, `AlphaDecreaseHeight`
- `WaveMin`, `WaveMax`, `WaveDecreaseHeight`
- `VertexPerTile`
- `BumpTexID`
- `FresnelTexID`
- `BaseR`, `BaseG`, `BaseB`
- `Shader14ID`, plus weiterer Shader-ID-Pfad fuer Fallback

## 3. Octree-basierte Weltaufteilung

Der Client hat ein Modul [`ApmOcTree`](../Module/ApmOcTree.md) und ein Clientmodul [`AgcmOcTree`](../Module/AgcmOcTree.md).

Harte Binary-Belege:
- Modulstrings `ApmOcTree` und `AgcmOcTree`
- Runtime-Dateiname `world\octree\OT%d.dat` in `FUN_005897b0`
- Objekt-/Template-Schluessel `OcTreeIDNum`, `OcTreeIDData`
- serialisierte Schluessel `OCTREE_DNUM`, `OCTREE_DATA`, `OCTREE_MAXBBOX`
- Typen/RTTI: `OcTreeIDList`, `ApmOcTree`, `AgcmOcTree`

Weltgrid:
- Sektorindizes werden im Code mit `+400` auf einen Bereich `0..799` gemappt.
- Sichtbar in HWater-Erzeugung: `iVar13 = sectorX + 400`, `iVar14 = sectorZ + 400`, Boundscheck gegen `799`.
- Damit ist das Weltgrid 800 x 800 Sektoren.

Gemeinsame Weltcontainer-Idee:
- Octree, Wasser und Gras sind sektorbasiert.
- Octree-Dateien sind logisch `OT%d.dat`.
- Wasser-Dateien sind logisch `WT%d.dat`.
- Gras-Dateien sind logisch `GR%d.dat`.
- Installiert liegen sie gepackt als `Data.Dat`/`Reference.Dat`-Paare unter `world\octree`, `world\water`, `world\grass`.

Installierte Welt-Daten:
- `C:\Spiele\Archlord\world\octree\Data.Dat`: 168,230,772 Bytes
- `C:\Spiele\Archlord\world\octree\Reference.Dat`: 3,977 Bytes
- `C:\Spiele\Archlord\world\water\Data.Dat`: 3,431,020 Bytes
- `C:\Spiele\Archlord\world\water\Reference.Dat`: 3,171 Bytes
- `C:\Spiele\Archlord\world\grass\Data.Dat`: 81,759,948 Bytes
- `C:\Spiele\Archlord\world\grass\Reference.Dat`: 4,022 Bytes

`world\octree\Data.Dat` beginnt mit `01 00 00 00`, danach Offsets/Groessen. Das passt zu einem versionierten Pack-/Containerformat.

## 4. Charakteranpassung

Die Charakteranpassung besteht aus Face/Hair-Listen, UI-Callbacks, Kauf-/Servereventlogik und RenderWare-Atomic-Austausch.

Konfigurationen:
- `Ini\CharacterTemplateCustomize.ini`
- `Ini\avatarset.ini`
- `Ini\%sCharacterCustomizeList.txt`
- installiert:
  - `C:\Spiele\Archlord\ini\charactertemplatecustomize.ini` 114,908 Bytes
  - `C:\Spiele\Archlord\ini\avatarset.ini` 219,917 Bytes
  - `C:\Spiele\Archlord\ini\charactercustomizelist.txt` 24,605 Bytes

Default-Face/Hair-Writer:
- `FUN_0061b680`: schreibt `DEFAULT_FACE_NUM`, `DEFAULT_FACE%04d`, `DEFAULT_RENDER_TYPE_FACE%04d`
- `FUN_0061b7d0`: schreibt `DEFAULT_HAIR_NUM`, `DEFAULT_HAIR%04d`, `DEFAULT_RENDER_TYPE_HAIR%04d`
- `FUN_0061b920`: ruft beide Writer auf und schreibt zusaetzlich `CUSTOMIZE_REVIEW`

Assetpfade:
- `DefaultHead\Face\` in `FUN_00707fd0`
- `DefaultHead\Hair\` in `FUN_007081b0`

Public/Event-Logik:
- [`AgpmEventCharCustomize`](../Module/AgpmEventCharCustomize.md)
- sichtbare Typen: `Hair`, `Face`
- serialisierte Werte: `FaceNum`, `HairNum`
- Event/UI-Funktionen:
  - `OpenCustomizeUI`
  - `CloseCustomizeUI`
  - `CustomizeBuyConfirm`
  - `CustomizeNeedDismountRide`
  - `CustomizeNeedRestoreTransform`
  - `CustomizeFaceList`
  - `CustomizeHairList`
  - `CustomizeBuyPrice`
  - `CustomizeIsActiveBuy`
  - `CustomizePreview`

UI-Texte/Bindings:
- `Customize_UseLevel`
- `Customize_PriceMoney`
- `Customize_Ticket`
- `Customize_HairStyle`
- `Customize_FaceStyle`
- `Customize_TotalPriceMoney`

Renderseite:
- [`AgcmCustomizeRender`](../Module/AgcmCustomizeRender.md) existiert als eigenes Modul.
- Face/Hair werden nicht nur als Texturparameter behandelt, sondern offenbar als eigene Clump/Atomic-nahe Assets geladen, geklont und an Charaktermodelle gehaengt.

## 5. Weltkarte

Region-/Map-Konfiguration:
- `Ini/regiontemplate.ini` in `FUN_0040da90`
- `Ini\worldmap.ini` in `FUN_006e2ad0`
- `INI\WORLDMAPNAME.XML` in `FUN_0067f480`

Regiontemplate-Felder:
- `WorldMap`
- `SkySet`
- `VisibleDistance`
- `TopViewHeight`
- `ResurrectionX`
- `ResurrectionZ`
- `ZoneSrcX`
- `ZoneSrcZ`
- `ZoneHeight`
- `ZoneDstX`
- `ZoneDstZ`
- `ZoneRadius`

Worldmap-Felder:
- `XStart`
- `ZStart`
- `RegionTexture`
- `RegionRoadTexture`
- `UIActiveAreaSX`
- `UIActiveAreaSY`
- `UIActiveAreaEX`
- `UIActiveAreaEY`

Worldmap-UI:
- `WorldMap_Toggle`
- `WorldMap_RightClick`
- `WorldMap_LeftClick`
- `WorldMap_LoadMapToggle`
- `WorldMap_MapEventPos`
- `WorldMap_WorldName`
- `WorldMap_RegionName`
- Castle-Buttons fuer Human, Orc, MoonElf, DragonScion und Archlord, jeweils drei Varianten.

Installierte Dateien:
- `C:\Spiele\Archlord\ini\worldmap.ini`: 68,173 Bytes
- `C:\Spiele\Archlord\ini\worldmapname.xml`: 8,252 Bytes

Beide Dateien sind im installierten Client nicht direkt sauberer Klartext. `worldmap.ini` beginnt z.B. mit `E1 09 2F 0B ...`.

## 6. Wasser

Dateien:
- Runtime-String `world\water\WT%d.dat`
- `Ini/WaterStatusT1.ini`
- `Ini/HWaterStatus.ini`
- installiert:
  - `C:\Spiele\Archlord\ini\waterstatust1.ini`: 8,126 Bytes
  - `C:\Spiele\Archlord\ini\hwaterstatus.ini`: 8,386 Bytes

Normales Wasser:
- statusbasiert
- benutzt Texture-Layer, Blendstates, Tilegroessen und Wave-Emitter
- wahrscheinlich RenderWare/D3D9 fixed-function Material-/Atomic-Pfad

High Water:
- wird aus normalem Wasser erzeugt (`MakeHWaterFromWater : Status_ID (%d)`)
- baut Vertexbuffer pro Wasserflaeche
- `VertexPerTile` skaliert die Tesselation
- nutzt Terrainhoehe zur Alpha-/Wave-Abnahme
- nutzt Reflection-, Bump- und Fresnel-Texturen
- nutzt programmierbare Shader `vs.1.1`, `ps.1.4`, `ps.1.1`

Sektorpayload aus vorhandener Analyse:
- Watercount
- pro Wasser: StatusID, X/Z Offset, TileXLength, TileZLength, Height
- Wavecount
- pro Wave: StatusID, Offset, Width, Height, SpawnCount, YRotAngle, TranslationSpeed, Origin

## 7. Gras

Dateien:
- Runtime-String `world\grass\GR%d.dat` in `FUN_0064b5f0`
- `Ini/GrassTemplate.ini`
- installiert:
  - `C:\Spiele\Archlord\ini\grasstemplate.ini`: 37,806 Bytes
  - `C:\Spiele\Archlord\world\grass\Data.Dat`: 81,759,948 Bytes

Templateparser `FUN_0064d030` liest:
- `TEXTURE_NAME`
- `TEXTURE_ID`
- `GRASS_ID`
- `GRASS_NAME`
- `SHAPE_TYPE`
- `GRASS_WIDTH`
- `GRASS_HEIGHT`
- `GRASS_WIDTH_RANDOM`
- `GRASS_HEIGHT_RANDOM`
- `ANIM_TYPE`
- `ANIM_AMOUNT`
- `ANIM_SPEED`
- `IMAGE_START_X`
- `IMAGE_START_Y`
- `IMAGE_WIDTH`
- `IMAGE_HEIGHT`

Strukturhinweise:
- GrassInfo-Eintrag ist im Parser 0x68 Bytes gross.
- `ANIM_AMOUNT` wird als float gespeichert.
- `ANIM_SPEED` wird als `int / Konstante` in float umgerechnet.
- Texturen werden ueber `TEXTURE_NAME` als `id:name`-Paar gelesen.
- Grasgruppen sind an Octree-IDs gekoppelt (`octree_sector_x`, `octree_sector_z`, `octree_id` laut vorhandener Rekonstruktion).

Renderpfad:
- kein klarer programmierbarer Shaderpfad fuer Gras.
- Belege deuten auf fixed-function D3D9/FVF/DrawPrimitiveUP-artiges Rendering.

## 8. Himmel und Natureffekte

Dateien:
- `Ini/SkySet.ini`
- `Ini/alefskysetting.ini`
- `Ini/NatureEffect.ini`
- `Ini/LensFlare.ini`
- installiert:
  - `skyset.ini`: 627,822 Bytes
  - `alefskysetting.ini`: 130 Bytes
  - `natureeffect.ini`: 5,271 Bytes
  - `lensflare.ini`: 762 Bytes

Skyset-Parser `FUN_005d1a00` arbeitet mit sechs Zeitbloecken und Flags.

Zeitblock-Startwerte im Code:
- Block 0: 0
- Block 1: 5
- Block 2: 7
- Block 3: 13
- Block 4: 19
- Block 5: 21

Flag-Bits:
- `1`: Light/Skyfarben
- `2`: Fog
- `4`: Clouds/Sun/Circumstance
- `8`: Effekte
- `0x10`: Background music
- `0x20`: Weather effects

Sky-/Light-Keys:
- `%02d_SkyTop`
- `%02d_SkyBottom`
- `%02d_Ambient`
- `%02d_Directional`

Fog-Keys:
- `%02d_FogColor`
- `%02d_FogDistance`
- `%02d_FogFarClip`

Cloud-/Himmelskoerper-Keys:
- `%02d_CloudTexture1`
- `%02d_CloudSpeed1`
- `%02d_CloudColor1`
- `%02d_CloudTexture2`
- `%02d_CloudSpeed2`
- `%02d_CloudColor2`
- `%02d_Circumstance`
- `%02d_CircumstanceColor`
- `%02d_Sun`
- `%02d_SunColor`

Effekt-/Audio-/Weather-Keys:
- `%02d_EffectInterval`
- `%02d_EffectIndex_%02d` fuer 5 Slots
- `%02d_EffectRate_%02d` fuer 5 Slots
- `%02d_BackGroundMusic`
- `%02d_WeatherEffect1`
- `%02d_WeatherEffect2`

Nature/Lensflare:
- Module [`AgpmNatureEffect`](../Module/AgpmNatureEffect.md), [`AgcmNatureEffect`](../Module/AgcmNatureEffect.md), [`AgcmLensFlare`](../Module/AgcmLensFlare.md)
- Script-/UI-Export `SetNatureEffect`
- Script-/UI-Export `ChangeLensFlareTemplate`
- Wettertyp-String `SNOW` sichtbar; vorhandene Analyse nennt zusaetzlich Rain/Thunder/Fog/Sandstorm/Fireworks.

## 9. Wichtige naechste RE-Schritte

1. `ApModuleStream`/`AuIniManager`/`AuExcelTxtLib` entschluesseln oder hooken, um die installierten INI/XML/TXT-Dateien sauber zu dumpen.
2. `Reference.Dat`-Format fuer `world\octree`, `world\water`, `world\grass` rekonstruieren.
3. Aus `Data.Dat` virtuelle Dateien `OT%d.dat`, `WT%d.dat`, `GR%d.dat` extrahieren.
4. Danach Parser fuer die 16x16-Sektorcontainer schreiben:
   - Header/Version
   - Offset-/Groessentabelle
   - Payload je Sektor
5. Octree-ID-Bitlayout und Grass-/Water-Zuordnung visualisieren.
6. `AgcmCustomizeRender` weiter verfolgen, um exakt zu belegen, welche Atomic/Frame/Skin/HAnim-Aufrufe beim Face/Hair-Austausch passieren.
