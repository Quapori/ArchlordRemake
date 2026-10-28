# AlefClient Engine/World Findings

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Welt, Engine und Rendering](Index.md)*

Stand: 2026-09-05

Quelle: statische Analyse von `C:\Spiele\Archlord\alefclient.exe`, Ghidra-Pseudocode/Disassembly in diesem Ordner, String-/Xref-Export sowie Abgleich mit dem vorhandenen EP8-C++-Quellbaum.

Wichtig: Die Datei wurde nicht ausgefuehrt. Die Aussagen unten sind statische Reverse-Engineering- und Source-Code-Funde. Wo der Quellcode dieselbe Logik belegt, ist die Aussage deutlich belastbarer als reine Pseudocode-Inferenz.

## Kurzfazit

Der Client nutzt keine nur "RenderWare-artige" Engine, sondern ist tatsaechlich stark RenderWare-basiert. Zentrale Typen und Pipelines sind `RwRaster`, `RwTexture`, `RwCamera`, `RwStream`, `RpWorld`, `RpClump`, `RpAtomic`, `RpGeometry`, `RpMaterial`, `RpMorphTarget`, `RpHAnimHierarchy` und `RpSkin`. Der D3D9-Backend-Pfad ist sichtbar, inklusive eigener RenderWare-All-in-one-Nodes und Shaderpfade.

Die Welt ist in ein grosses 800x800-Sektorgrid organisiert. Ein logischer 16x16-Division-Container buendelt Sektordaten fuer Octree, Wasser und Gras. Die Octree-Struktur ist zweistufig unter dem Root, mit bis zu vier vertikal gestapelten Roots pro Sektor. Wasser besitzt eigene fixed-function- und Shader-Renderpfade; hochwertiges Wasser nutzt Vertex Shader 1.1 und Pixel Shader 1.1/1.4. Gras ist dagegen ein D3D9 fixed-function/RenderWare-Im3D-aehnlicher Billboarding-Pfad.

Charakteranpassung ist ein eigenes System fuer Face/Hair-Atomics. Es laedt Listen aus verschluesselten/packbaren Konfigurationsdateien, prueft Spielbedingungen beim Kauf und haengt geklonte RenderWare-Atomics mit Skin/HAnim-Hierarchie an die Charakter-Clumps.

## Artefakte

- `analysis/alefclient/alefclient.disasm.txt`: vollstaendige Disassembly, ca. 92 MB.
- `analysis/alefclient/alefclient.pseudocode.c`: Ghidra-Pseudocode, ca. 30 MB.
- `analysis/alefclient/functions.tsv`: Funktionsuebersicht.
- `analysis/alefclient/engine_keyword_xrefs.tsv`: 1.651 relevante String-/Xref-Zeilen zu Engine-, World-, Shader-, Water-, Grass- und Customize-Begriffen.
- `analysis/alefclient/ghidra_scripts/ExportEngineKeywordXrefs.java`: Exportskript fuer die Xref-Tabelle.

## RenderWare-Engine

Die Engine ist RenderWare-basiert, nicht nur aehnlich benannt.

Belastbare Quellbelege:

- `Modules/AClient/AgcSkeleton/CRenderDevice_Renderware.h`
- `Modules/AClient/AgcSkeleton/CRenderDevice_Renderware.cpp`
- RenderWare-Typen quer durch Clientmodule: `RwRaster`, `RwTexture`, `RwCamera`, `RwFrame`, `RwStream`, `RwMatrix`, `RpWorld`, `RpClump`, `RpAtomic`, `RpGeometry`, `RpMaterial`, `RpMorphTarget`, `RpHAnimHierarchy`, `RpSkin`.

Wichtige Struktur:

- `RpWorld`: Szene/Welt-Container und Ray-/Intersection-Ziel.
- `RpClump`: Modellgruppe, typischerweise Charakter oder zusammengesetztes Objekt.
- `RpAtomic`: einzelnes renderbares Mesh innerhalb eines Clumps.
- `RpGeometry`, `RpMaterial`, `RpMorphTarget`: Meshdaten, Materialdaten, Vertex-/Morphdaten.
- `RwFrame`: Transformhierarchie.
- `RpHAnimHierarchy` und `RpSkin`: Charakter-Skeleton/Skinning.

Beispiel: [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md):LoadClump` nutzt `AuPackingManager`, oeffnet einen RenderWare-Memory-Stream, liest Chunkheader und ruft `RpClumpStreamRead`. Das passt im Pseudocode zur dekompilierten Funktion bei etwa `0x00664a80`.

D3D9-/Pipeline-Hinweise aus dem Binary:

- `nodeD3D9SkinAtomicAllInOne.csl`
- `nodeD3D9WorldSectorAllInOne.csl`
- `myNodeD3D9AtomicAllInOne`
- Toon-/Custom-Pipeline-Pluginspuren

Das heisst: Der Client verwendet RenderWare als Szenen-/Asset-/Clump-System und bindet eigene D3D9-spezifische Renderpfade daran.

## Vertex- und Pixel-Shader

Die klarsten Shader befinden sich im Wassermodul:

- `Modules/AClient/AgcmWater/AgcmWater.cpp`
- Vertex Shader: `vs.1.1`
- Pixel Shader: `ps.1.1` und `ps.1.4`

Shader-Erzeugung:

- [`AgcmWater`](../Module/AgcmWater.md):GetShader` assembliert Shader mit `D3DXAssembleShader`.
- Danach werden sie mit `RwD3D9CreatePixelShader` bzw. `RwD3D9CreateVertexShader` in RenderWare/D3D9 eingebunden.
- Assemblerfehler werden per Debugausgabe sichtbar gemacht.

Hardwareauswahl:

- Hochwertiges Wasser verlangt mindestens Vertex Shader 1.1 und Pixel Shader 1.1.
- Wenn Pixel Shader 1.4 vorhanden ist, wird ein besserer High-Water-Pfad aktiv.
- Sonst faellt der Client auf den Pixel-Shader-1.1-Pfad zurueck.
- Es gibt einen Force-1.1-Schalter (`m_bForce11Shader`).

Wasser-Shader-Funktionen:

- Sinusfoermige Vertex-Verformung.
- Normal-/Tangent-/Binormal-Neuberechnung fuer bewegte Wasseroberflaeche.
- Reflection-UVs.
- Zwei animierte Bump-Map-Layer.
- Tangent-space View-/Light-Vektoren.
- Fresnel-Lookup auf Basis von View dot Normal.
- Reflection-Sampling und Specular-Anteil.

Weitere Shader-/Postprocessing-Hinweise:

- `Modules/AClient/AgcmGlare/blurvshaderD3D9.vsh`
- passender Pixel-Shader-Pfad im Glare-Modul
- HLSL-/Shaderparser-Spuren im Source/Binary

Gras nutzt dagegen keinen programmierbaren Shaderpfad. Es setzt den D3D9-Vertexshader auf `NULL` und zeichnet ueber fixed-function/FVF mit Position, Diffuse, Specular und einer Texturkoordinate.

## Weltgrid und Worldmap

Die Welt ist in ein festes Sektorgrid organisiert.

Zentrale Konstanten aus `Modules/APublic/ApmMap/ApmMap.h`:

- `MAP_WORLD_INDEX_WIDTH = 800`
- `MAP_WORLD_INDEX_HEIGHT = 800`
- `MAP_SECTOR_WIDTH = 6400.0f`
- `MAP_DEFAULT_DEPTH = 16`

Abgeleitete Bedeutung:

- Sektorindizes laufen effektiv von ca. `-400` bis `399`.
- Ein Sektor ist `6400` Welteinheiten breit.
- Eine 16x16-Division umfasst `102400 x 102400` Welteinheiten.
- Das volle 800x800-Grid umfasst grob `5.120.000 x 5.120.000` Welteinheiten.

Region-/Worldmap-Konfigurationen:

- Regiontemplate-Schluessel: `Name`, `ParentIndex`, `ItemSection`, `Type`, `Comment`, `WorldMap`, `SkySet`, `VisibleDistance`, `TopViewHeight`, `LevelLimit`, `LevelMin`, `ResurrectionX`, `ResurrectionZ`, `ZoneSrcX`, `ZoneSrcZ`, `ZoneHeight`, `ZoneDstX`, `ZoneDstZ`, `ZoneRadius`.
- Regionelemente: `Index`, `Kind`, `StartX`, `StartZ`, `EndX`, `EndZ`.
- `worldmap.ini` verbindet Weltkoordinaten mit UI-Regionen.

Worldmap-Schluessel:

- `Comment`
- `XStart`, `ZStart`, `XEnd`, `ZEnd`
- `ItemID`
- `ParentGroupID`, `GroupID`
- `RegionTexture`
- `RegionRoadTexture`
- `UIActiveAreaSX`, `UIActiveAreaSY`, `UIActiveAreaEX`, `UIActiveAreaEY`

`WORLDMAPNAME.XML` liefert lokalisierte Welt- und Regionsnamen. Das UI-Modul `Modules/AClient/AgcmMinimap/AcUIWorldmap.*` behandelt Worldmap-Anzeige, Klickpositionen, Regionsnamen, Schlossbuttons und Minimap-Interaktion.

## Octree-Weltaufteilung

Der Octree ist sektorbasiert und eng an das 800x800-Weltgrid gekoppelt.

Zentrale Konstanten aus `Modules/APublic/ApmOcTree/ApmOcTree.h`:

- `OCTREE_SPHEREVAL = 1.75f`
- `OCTREE_MAXDEPTH = 2`
- `OCTREE_MAX_ROOT_COUNT = 4`

Node-/ID-Aufbau:

- Jeder Node besitzt eine 32-bit-ID.
- Die ID kodiert Rootindex, Leaf-Bit, Tiefe und bis zu sieben 3-bit-Levelpfade.
- Ein Root hat bis zu acht Kinder pro Ebene.
- Bei `OCTREE_MAXDEPTH = 2` ergibt das Root -> Level 1 -> Leaf.

Raumaufteilung:

- Root-Halfsize pro Sektor: `MAP_SECTOR_WIDTH / 2 = 3200`.
- Root-Wuerfelbreite: `6400`.
- Level-1-Wuerfelbreite: `3200`.
- Leaf-Wuerfelbreite: `1600`.
- Bounding-Sphere-Radius am Root: `3200 * 1.75 = 5600`.
- Pro Sektor koennen bis zu vier Roots vertikal gestapelt werden, wenn die Terrainhoehe das braucht.

Clienterzeugung:

- [`AgcmOcTree`](../Module/AgcmOcTree.md):CreateRootByTerrain` nimmt Terrain-Atomics, liest Geometrie/MorphTarget-Vertices und bestimmt Min-/Max-Y.
- Zusaetzlich existiert eine 2D-Quadtree-Struktur fuer Top-Height/Box-Daten, ebenfalls mit Tiefe 2.
- `TestClumpOctrees` transformiert Atomic-Vertices in Weltkoordinaten, sampelt lange Kanten in 800er-Schritten, sammelt Leaf-IDs und kann vollstaendige 8er-Siblinggruppen zum Parent zusammenfassen.

Nutzung:

- Terrain-/Objekt-/Charakter-Intersection.
- Targeting.
- Lensflare-/Sichtbarkeitspruefungen.
- Kamera-/Mauskarten-Interaktion.
- Streaming/Loading-Status mit Critical Section gegen doppelte Loads.

## Gemeinsames Division-Dateiformat

Octree, Wasser und Gras verwenden denselben 16x16-Containeraufbau.

Logische Dateinamen:

- Octree: `world/octree/OT%d.dat`
- Wasser: `world/water/WT%d.dat`
- Gras: `world/grass/GR%d.dat`

Containerheader:

- `uint32 version`
- 16x16 Eintraege
- jeder Eintrag: `int32 absolute_data_offset` und `int32 byte_size`
- Datenstart: `4 + 16 * 16 * 8 = 2052` Bytes

Das ist wichtig fuer Extraktion: Die Dateien sind nicht einfach lineare Listen, sondern kleine Divisionsarchive mit Offsettabelle.

## Octree-Dateipayload

Octree-Sektorpayload:

- `int32 root_count`
- pro Root: `float centerY`
- danach rekursive Node-Daten

Node-Serialisierung:

- `uint32 id`
- `uint32 objectnum`
- `int32 bHasChild`
- `float sphere_radius`
- `float sphere_center_x`
- `float sphere_center_y`
- `float sphere_center_z`
- `uint32 hsize`
- `uint32 level`
- falls `bHasChild`: rekursiv 8 Child-Nodes

Nach dem Octree-Teil kann der Client ueber Callback noch Zusatzdaten, z.B. Quadtree-/Clientdaten, anhaengen.

## Wasser

Normales Wasser und High-Quality-Wasser sind getrennte Runtime-Pfade, teilen sich aber Status-/Konfigurationsdaten.

Wichtige Konstanten aus `AgcmWater`:

- Water-Datensatz: 16 Bytes.
- Wave-Datensatz: 40 Bytes.
- 10 Dateislots.
- 20 normale WaterStatus-Eintraege.
- 20 High-WaterStatus-Eintraege.
- Wave-View-Range: 2.
- Reflection-Texture: 512x512.

`WaterStatus` enthaelt:

- Water type.
- Blendoperation und Blendmodes.
- Zwei Texturlayer mit IDs, Farbe/Alpha und UV-Speed.
- Tile size.
- Wave-Textur/ID, Dimensionen, Lifetime, Scale, RGB, Min-/Max-Count.

`HWaterStatus` enthaelt:

- RGB/Basisfarbe.
- Vier Richtungsvektoren.
- Vier Hoehenwerte.
- Vier Geschwindigkeiten.
- Zwei Texturbewegungen.
- Reflection weight.
- Alpha-/Height-Min-Max-Decrease-Parameter.
- Vertex-per-tile.
- Bump- und Fresnel-Textur-ID.
- Shader-ID-Paare fuer `ps.1.4` und `ps.1.1`.

Wasser-Sektorpayload:

- `int32 Watercount`
- pro Water 16 Bytes: `int32 StatusID`, `int16 XOffset`, `int16 ZOffset`, `int16 TileXLength`, `int16 TileZLength`, `int32 Height`
- `int32 Wavecount`
- pro Wave 40 Bytes: `int32 StatusID`, `int16 XOffset`, `int16 ZOffset`, `int32 Width`, `int32 Height`, `int32 SpawnCount`, `float YRotAngle`, `float TranslationSpeed`, `RwV3d origin`

Versionen:

- Version 1: aelteres Offset-/Wave-Verhalten.
- Version 2: Kommentar im Code nennt geaendertes Wave-SpawnTiming von 4-10 auf 2-8 Sekunden.

Renderpfade:

- Normales Wasser: RenderWare/D3D9-Material-/Atomic-Pfad.
- High Water: eigener Shaderpfad mit Vertex-/Indexbuffern, Reflection-Kamera und Bump-/Fresnel-Texturen.

## Gras

Gras ist template- und gruppenbasiert.

Template-Schluessel:

- `TEXTURE_NAME`
- `TEXTURE_ID`
- `GRASS_GROUP`
- `GRASS_ID`
- `GRASS_NAME`
- `SHAPE_TYPE`
- `GRASS_WIDTH`
- `GRASS_HEIGHT`
- Width-/Height-Randomwerte
- `ANIM_TYPE`
- `ANIM_AMOUNT`
- `ANIM_SPEED`
- `IMAGE_START_X`
- `IMAGE_START_Y`
- `IMAGE_WIDTH`
- `IMAGE_HEIGHT`

Formen:

- `CROSS = 0`
- `PERPENDICULAR = 1`

Runtime-Struktur:

- einzelnes Grass: ID/Shadow, Rotation X/Y, Scale, Animation, Position, Matrix, Vertexbuffer, Texture.
- `GrassInfo`: Name, Texture-ID, Shape, Original-/Dark-Vertexbuffer, Animationsdaten, Dimensionen, Atlasrechteck.
- `GrassGroup`: Bounding Sphere, Octree-ID, Grass-Liste, MaxY, Kameraindex, Draworder.

Renderpfad:

- fixed-function D3D9.
- `RwD3D9SetVertexShader(NULL)`.
- `DrawPrimitiveUP` mit Triangle Lists.
- FVF: XYZ, Diffuse, Specular, TEX1.

Gras-Sektorpayload Version 2:

- `int32 group_count`
- pro Gruppe: `int32 grass_count`, `int32 octree_sector_x`, `int32 octree_sector_z`, `uint32 octree_id`, Bounding Sphere `x/y/z/r`, `float maxY`
- pro Pflanze 28 Bytes: `int32 grass_id`, Position `x/y/z`, `float rotX`, `float rotY`, `float scale`

Version 1 ignoriert den gespeicherten Radius und verwendet fest `700`.

## Himmel und Natureffekte

[`AgcmEventNature`](../Module/AgcmEventNature.md) steuert Skysets, Wetterflags, Naturpartikel, Lensflare, Musik und Fog/Lighting.

Sky-Zeitbloecke:

- `0`: Night2, 00-05
- `1`: Dawn, 05-07
- `2`: Daytime1, 07-13
- `3`: Daytime2, 13-18/19 je nach Kommentar/Keyfolge
- `4`: Evening, 19-21
- `5`: Night1, 21-24

Sky-Datenflags:

- `LIGHT = 1`
- `FOG = 2`
- `CLOUD = 4`
- `EFFECT = 8`
- `MUSIC = 0x10`
- `WEATHER = 0x20`
- `ALL = 0x3f`

Weatherflags:

- `USE_LENS_FLARE = 1`
- `SHOW_STAR = 2`
- `SHOW_BREATH = 4`
- `SHOW_MOON = 8`
- `DISABLE_POINT_LIGHT = 0x10`
- `DISABLE_WEATHER = 0x20`

Sky-Konfigurationskeys:

- `%02d_SkyTop`
- `%02d_SkyBottom`
- `%02d_Ambient`
- `%02d_Directional`
- `%02d_FogColor`
- `%02d_FogDistance`
- `%02d_FogFarClip`
- `%02d_CloudTexture1`
- `%02d_CloudTexture2`
- `%02d_CloudSpeed1`
- `%02d_CloudSpeed2`
- `%02d_CloudColor1`
- `%02d_CloudColor2`
- `%02d_Circumstance`
- `%02d_CircumstanceColor`
- `%02d_Sun`
- `%02d_SunColor`
- `%02d_EffectInterval`
- `%02d_EffectIndex_%02d`
- `%02d_EffectRate_%02d`
- `%02d_BackGroundMusic`
- `%02d_WeatherEffect1`
- `%02d_WeatherEffect2`

Natureffekt-Typen:

- `NONE = -1`
- `SNOW`
- `RAIN`
- `RAIN_WITH_THUNDER`
- `RAIN_WITH_FOG`
- `SANDSTORM`
- `FIREWORKS_DISPLAY`

Natureffekt-Templatekeys:

- `TEXTURE_NAME`
- `NEFFECT_ID`
- `TEXTURE_ID`
- `NEFFECT_TYPE`
- `SIZE_MIN`, `SIZE_MAX`
- `SPEED_MIN`, `SPEED_MAX`
- `SWING_MIN`, `SWING_MAX`
- `DENSITY_MIN`, `DENSITY_MAX`
- `RED_MIN`, `RED_MAX`
- `GREEN_MIN`, `GREEN_MAX`
- `BLUE_MIN`, `BLUE_MAX`
- `ALPHA_MIN`, `ALPHA_MAX`
- `NEFFECT_SKYSET`

Lensflare:

- Template-Datei mit Fallback auf `Ini/LensFlare.ini`.
- Sun-Flare wird post-render behandelt, Moon-Flare pre-render.
- Sichtbarkeit nutzt `RpWorld`-/Ray-Intersections und D3D9-Occlusion-Query.
- Aktivierung haengt am Sky-Weatherflag `USE_LENS_FLARE`.

## Charakteranpassung

Die Charakteranpassung ist ein Face-/Hair-System auf RenderWare-Atomic-Basis.

Konfigurationen:

- `Ini/CharacterTemplateCustomize.ini`
- `Ini/avatarset.ini`
- `%sCharacterCustomizeList.txt`

Template-Schluessel:

- `DEFAULT_FACE_NUM`
- `DEFAULT_FACE%04d`
- `DEFAULT_RENDER_TYPE_FACE%04d`
- `DEFAULT_HAIR_NUM`
- `DEFAULT_HAIR%04d`
- `DEFAULT_RENDER_TYPE_HAIR%04d`

Assetpfade:

- `DefaultHead/Face/`
- `DefaultHead/Hair/`

Event-/Gameplay-Seite:

- Modul: [`AgpmEventCharCustomize`](../Module/AgpmEventCharCustomize.md)
- Operationen: `REQUEST`, `RESPONSE`, `BUY`
- Callbacks: `GRANT`, `AFTER_UPDATE`
- Listenspalten: `Type`, `Number`, `Sell Name`, `Case`, `CharacterTID`, `UseLevel`, `Price(Money)`, `Price(Skull)`
- Typen: Hair, Face
- Cases: All, Ingame, Login, None

Kauf-/Update-Logik:

- Request enthaelt Face- und Hair-Index.
- Server-/Public-Logik prueft Charakter, Eventstatus, Range, Template, Level und Preis.
- Bezahlung erfolgt ueber Money oder Item-Currency.
- Danach wird der Customize-Index aktualisiert und `AFTER_UPDATE` ausgeloest.

Render-/Preview-Logik:

- Face/Hair werden als eigene `RpAtomic`-Objekte geladen/geklont.
- Alte Custom-Atomics werden entfernt und zerstoert.
- Neue Atomics bekommen ein eigenes Frame und werden dem Clump hinzugefuegt.
- Skin/HAnim-Hierarchie wird gesetzt, Normals werden normalisiert.
- Der Preview-Renderer klont den Charakter-Clump, entfernt bestehende Custom-Atomics und rendert in eine Offscreen-RenderWare-Kamera mit Raster/Z-Raster/Texture.

Audit-Hinweis:

- In der Buy-/Levelpruefung wirkt die Initialisierung/Verwendung von `minLevel` auffaellig: Wenn `minLevel` mit 0 startet und Hair per `MIN(entryLevel, minLevel)` einbezogen wird, bleibt der Wert 0. Das koennte bedeuten, dass eine reine oder spaet verarbeitete Hair-Pruefung die Levelanforderung zu niedrig bewertet. Das sollte direkt gegen den final genutzten Branch geprueft werden, bevor man daraus eine Exploit-Aussage macht.
- Ebenfalls auffaellig: Fuer Face/Hair scheint teilweise ein gemeinsamer `itemTid`-/Currency-Pfad verwendet zu werden. Gemischte Waerungen zwischen Face und Hair koennten dadurch fehleranfaellig sein. Auch das ist ein Code-Audit-Kandidat, keine abschliessende Laufzeitbehauptung.

## Installierte Spieldaten

Im installierten Client unter `C:\Spiele\Archlord` wurden relevante Konfigurations- und Packdateien gefunden:

- `GrassTemplate.ini`
- `HWaterStatus.ini`
- `WaterStatusT1.ini`
- `SkySet.ini`
- `alefskysetting.ini`
- `NatureEffect.ini`
- `LensFlare.ini`
- `CharacterTemplateCustomize.ini`
- `avatarset.ini`
- `worldmap.ini`
- `WORLDMAPNAME.XML`
- `regiontemplate.ini`
- `LODDISTANCETYPE.TXT`
- `world/octree/Data.Dat` und `Reference.Dat`
- `world/water/Data.Dat` und `Reference.Dat`
- `world/grass/Data.Dat` und `Reference.Dat`
- `Texture/World/Data.Dat` und `Reference.Dat`

Mehrere `ini`-/`xml`-Dateien sind nicht plaintext; die ersten Bytes unterscheiden sich deutlich von Klartext. Das passt zu den Codepfaden ueber `ApModuleStream`, `AuIniManager` und `AuExcelTxtLib` mit Decryption-Flag. Die `Data.Dat`-/`Reference.Dat`-Paare sind zusaetzlich ein Packing-/Virtual-Filesystem-Layer.

Fehlend in der geprueften Installation:

- `RegionPerculiarity.xml`
- `Texture/Tiles.txd`

## Was der Pseudocode konkret verraet

Der Pseudocode allein zeigt die Binary-Seite: Funktionsadressen, Stringverweise, gelinkte RenderWare-/D3D9-Symbole, Konfigurationskeys und grobe Kontrollfluesse. Besonders nuetzlich waren:

- Clump-Ladepfad um `0x00664a80`.
- Wasser-Shader- und Statuspfade im Bereich des `AgcmWater`-Codes.
- Gras-Templateparser, im Pseudocode u.a. als Funktion um `0x0064d030` sichtbar.
- Nature-/Sky-Parser, u.a. um `0x0063af50` und `0x005d1a00`.
- Viele String-Xrefs zu `Rw*`, `Rp*`, `WaterStatus`, `HWaterStatus`, `GrassTemplate`, `SkySet`, `NatureEffect`, `CharacterCustomize`.

Der vorhandene C++-Source-Abgleich macht daraus belastbare Strukturinformationen: exakte Struct-Felder, Dateiformate, Konstanten, Serialisierungsreihenfolgen und die Trennung zwischen normalen Runtime-Pfaden und Editor-/Tool-/Serverlogik.

## Praktische naechste Schritte

Sinnvolle Folgearbeiten:

- Parser fuer die 16x16-Division-Dateien bauen: zuerst Header/Offsettabelle, dann Octree/Water/Grass-Payloads.
- Decryption-/Packing-Pfad fuer `ApModuleStream`/`AuIniManager`/`AuExcelTxtLib` nachziehen, um die installierten `.ini`/`.xml` sauber zu lesen.
- Worldmap-/Region-/Skyset-Daten in JSON dumpen und daraus eine technische Karte bauen.
- Octree-Visualisierung erzeugen: Sector -> Root stack -> Leaf IDs -> Objekt-/Grass-/Water-Zuordnung.
- Character-Customize-Listen extrahieren und mit Assetpfaden verknuepfen.
- Die zwei Customize-Audit-Hinweise gezielt in Source und Binary gegentesten.
