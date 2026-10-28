# Welt-, Octree-, Wasser- und Graskonfigurationen

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Welt, Engine und Rendering](Index.md)*

Stand: 2026-09-05

## Kurzfassung

- Die relevanten losen Config-Dateien sind mit dem allgemeinen Key `1111` entschluesselbar.
- Der gleiche `Reference.Dat`/`Data.Dat`-Packmechanismus gilt fuer `world\octree`, `world\water`, `world\grass`, `texture\world` und `texture\worldmap`.
- `Reference.Dat` ist nur der verschluesselte Index. `Data.Dat` enthaelt die rohen Payloads an den Offsets aus dem Index.
- Die Weltsektoren sind dateinamensbasiert in 2D-Kacheln organisiert:
  - `world\octree\OT%d.dat`
  - `world\water\WT%d.dat`
  - `world\grass\GR%d.dat`
- Die beobachteten Sektordateien benutzen zweistellige X/Z-Codes, z.B. `ot1831.dat`, `wt2024.dat`, `gr1831.dat`.
- Die bekannte Sektorabdeckung der drei World-Packs liegt jeweils im Bereich X `17..32`, Z `17..32`, aber nicht jede Kombination existiert in jedem Pack.

## Relevante Dateien

### Entschluesselte Config-Artefakte

- `decoded_worldmap.ini.txt`
- `decoded_worldmapname_xml.txt`
- `decoded_waterstatust1.ini.txt`
- `decoded_hwaterstatus_ini.txt`
- `decoded_grasstemplate.ini.txt`
- `decoded_natureeffect_ini.txt`
- `decoded_skyset_ini.txt`
- `decoded_alefskysetting_ini.txt`

### Pack-Indizes

| Pack | Eintraege | Gesamtgroesse | Min | Max | X | Z |
|---|---:|---:|---:|---:|---:|---:|
| `world\octree` | 172 | 163600520 | 3076 | 1514204 | 17..32 | 17..32 |
| `world\water` | 137 | 3374620 | 4100 | 135996 | 17..32 | 17..32 |
| `world\grass` | 174 | 75859848 | 3076 | 6393816 | 17..32 | 17..32 |
| `texture\worldmap` | 90 | 43573525 | 197107 | 967582 | n/a | n/a |

## Weltkarte

`ini\worldmap.ini`

- Entschluesselt mit `1111`.
- 232 nummerierte Abschnitte.
- 227 eindeutige `GroupID`-Werte.
- Jede Region verweist auf eine `.png`-Textur.
- Wichtige Felder:
  - `Comment`
  - `XStart`, `ZStart`, `XEnd`, `ZEnd`
  - `ItemID`
  - `ParentGroupID`
  - `GroupID`
  - `RegionTexture`
  - `RegionRoadTexture`
  - `UIActiveAreaSX`, `UIActiveAreaSY`, `UIActiveAreaEX`, `UIActiveAreaEY`

Beispiel fuer den Root-Bereich:

```ini
[1]
Comment=Chantra Continent
XStart=-409677
ZStart=-206464
XEnd=409741
ZEnd=204455
ParentGroupID=
GroupID=Chantra Continent
RegionTexture=wmap0001.png
```

Top-Level-/Hauptgruppen aus `ParentGroupID`:

| ParentGroupID | Kinder |
|---|---:|
| `Dragonscion Zone` | 33 |
| `Moon Elf Zone` | 19 |
| `Human Zone` | 14 |
| `Orc Zone` | 13 |
| `Dead Zone` | 10 |
| `Chantra Continent` | 5 |

`ini\worldmapname.xml`

- Plain XML nach Decode.
- Encoding-Angabe: `ks_c_5601-1987`.
- Beginnt mit `World>Chantra...`.
- Wird vom Client ueber `INI\WORLDMAPNAME.XML` geladen.

## Octree

### Module und Loader

Relevante Namen/Xrefs:

- [`ApmOcTree`](../Module/ApmOcTree.md)
- [`AgcmOcTree`](../Module/AgcmOcTree.md)
- `world\octree`
- `world\octree\OT%d.dat`
- `OCTREE_DNUM`
- `OCTREE_DATA`
- `OCTREE_MAXBBOX`

Wichtige Funktionen:

- `FUN_005887f0`: Konstruktor/Init fuer `ApmOcTree`.
  - Initialisiert 800 x 800 Raster-/Statusarrays.
  - Setzt Modulnamen `ApmOcTree`.
- `FUN_005887b0` / `FUN_00588920`: Zugriff auf 800 x 800 Kachelarrays.
- `FUN_005897b0`: laedt `world\octree\OT%d.dat` on demand.
- `FUN_00672dc0`: schreibt/parst objektbezogene Octree-Felder wie `OCTREE_DNUM`, `OCTREE_DATA`, `OCTREE_MAXBBOX`.
- `FUN_00795f80` / nahe `FUN_007964d0`: weiterer Objekt-/Octree-Serialize-Pfad mit `OCTREE_DATA`.

### Sektor-Dateiformel

Der Loader formatiert:

```c
sprintf(local_27c, "world\\octree\\OT%d.dat", sectorId);
```

Der beobachtete `sectorId` wird aus groberen Kachelkoordinaten gebildet:

```text
sectorId = sectorX * 100 + sectorZ
sectorX ~= worldGridX >> 4
sectorZ ~= worldGridZ >> 4
```

Das passt zu Dateinamen wie:

- `ot1831.dat` -> X `18`, Z `31`
- `ot2024.dat` -> X `20`, Z `24`
- `ot3232.dat` waere X `32`, Z `32`, falls vorhanden.

### `world\octree` Pack

- `Reference.Dat` root: `world\octree`
- Eintraege: 172
- Gesamtpayload: 163600520 Bytes
- Dateigroessen:
  - Minimum: 3076 Bytes
  - Maximum: 1514204 Bytes
  - Durchschnitt: ca. 951166 Bytes

Erste Eintraege:

| Index | Name | Offset | Size |
|---:|---|---:|---:|
| 0 | `ot1831.dat` | `0x09B75C7C` | 1133972 |
| 1 | `ot1928.dat` | `0x02031DF0` | 1338940 |
| 2 | `ot2020.dat` | `0x03F932AC` | 1034580 |
| 3 | `ot2024.dat` | `0x026CEA3C` | 1013756 |
| 4 | `ot2031.dat` | `0x02178C2C` | 1236644 |

### Beobachtete interne OT-Struktur

`extracted_ot1831.dat`:

```text
len=1133972
u32[0..3]=0x00000001,0x00000804,0x00000C2C,0x00001430
```

Headerbytes:

```text
01 00 00 00 04 08 00 00 2C 0C 00 00 30 14 00 00
8C 0F 00 00 BC 23 00 00 8C 0F 00 00 48 33 00 00
```

Interpretation:

- Die OT-Datei ist nicht RC4-verschluesselt.
- Direkt am Anfang liegt eine interne Offset-/Laengen-Tabelle.
- Danach folgen die eigentlichen Octree-/Objektchunks.
- Der vollstaendige innere Chunkparser ist noch offen.

## Wasser

### Low-/Classic-Water: `waterstatust1.ini`

`ini\waterstatust1.ini`

- Entschluesselt mit `1111`.
- Abschnitte:
  - `[WaterTextures]`
  - `[WaveTextures]`
  - `[Setting]`
- `WaterTextures`: 3 Texturen.
- `WaveTextures`: 4 Texturen.
- 20 `ID`-Bloecke (`0..19`), obwohl `MAX_ID_USED=9` gesetzt ist.

Wichtige Felder pro Wasserstatus:

- Typ/Render:
  - `WTTYPE`
  - `BMODE_L1`, `BOP_L1`, `RENDERBMODE_L1`
  - `BMODE_L2`, `BLENDSRC_L2`, `BLENDDEST_L2`
- Layer-Texturen:
  - `WATERFILE_L1`
  - `WATERFILE_L2`
- Farbe/Alpha:
  - `RED_L1`, `GREEN_L1`, `BLUE_L1`, `ALPHA_L1`
- UV-Scroll:
  - `U_L1`, `V_L1`
  - `U_L2`, `V_L2`
- Kachelung:
  - `TILESIZE_L1`
- Wellen:
  - `WAVEFILE`
  - `WAVEWIDTH`, `WAVEHEIGHT`
  - `WAVELIFETIME`
  - `WAVESCALEX`, `WAVESCALEZ`
  - `WAVERED`, `WAVEGREEN`, `WAVEBLUE`
  - `WAVEMINNUM`, `WAVEMAXNUM`

Beobachtete Wertebereiche:

| Feld | Bereich / Werte |
|---|---|
| `ID` | `0..19` |
| `WTTYPE` | `0, 1` |
| `RENDERBMODE_L1` | `-1, 0, 3` |
| `TILESIZE_L1` | `0, 4, 8` |
| `U_L1` | `0..0.004` |
| `V_L1` | `-0.002..0.0004` |
| `U_L2` | `-0.002..0.0003` |
| `V_L2` | `-0.0001..0.004` |
| `WAVEFILE` | `0..3` |
| `WAVELIFETIME` | `0, 5000, 7400, 7500` |
| `WAVEMINNUM/WAVEMAXNUM` | `0..1` / `0..3` |

Texturelisten:

```ini
[WaterTextures]
FN=0:water_nomal_01.bmp
FN=1:water_nomal_02.bmp
FN=2:WATER_NOMAL_02.BMP

[WaveTextures]
FN=0:water_wave.tif
FN=1:water_oceangradient_01_.bmp
FN=2:WATER_WAVE.TIF
FN=3:WATER_OCEANGRADIENT_01.BMP
```

### High-/Shader-Water: `hwaterstatus.ini`

`ini\hwaterstatus.ini`

- Entschluesselt mit `1111`.
- Abschnitte:
  - `[BumpMap Textures]`
  - `[FresnelMap Textures]`
  - `[Setting]`
- Bump-Texturen: 3.
- Fresnel-Texturen: 5.
- 20 `ID`-Bloecke (`0..19`).

Wichtige Felder:

- Farbe:
  - `Red`, `Green`, `Blue`
  - `BaseR`, `BaseG`, `BaseB`
- Wellenvektoren:
  - `DirX`, `DirY`
  - `Height`
  - `Speed`
- UV-Offsets:
  - `TexX0`, `TexX1`, `TexY0`, `TexY1`
- Transparenz:
  - `AlphaMin`, `AlphaMax`, `AlphaDecreaseHeight`
- Reflektion/Welle:
  - `ReflectionWeight`
  - `WaveMin`, `WaveMax`, `WaveDecreaseHeight`
- Tesselation/Shader:
  - `VertexPerTile`
  - `BumpTexID`
  - `FresnelTexID`
  - `Shader14ID`
  - `Shader11ID`

Beobachtete Wertebereiche:

| Feld | Bereich / Werte |
|---|---|
| `ID` | `0..19` |
| `VertexPerTile` | `1, 2` |
| `BumpTexID` | `0, 1` |
| `FresnelTexID` | `0..4` |
| `Shader14ID` | `0, 1` |
| `Shader11ID` | `0, 1` |
| `ReflectionWeight` | `0.3, 0.6, 0.8, 1` |
| `AlphaMin` | `0..0.7` |
| `AlphaMax` | `0.75, 0.8, 1` |
| `AlphaDecreaseHeight` | `50, 100, 150, 200, 400` |
| `WaveMin` | `0, 0.2, 0.25` |
| `WaveMax` | `1` |
| `WaveDecreaseHeight` | `400, 800` |

Texturelisten:

```ini
[BumpMap Textures]
FN=0:Water_bump_01.bmp
FN=1:WATER_BUMP_01.BMP
FN=2:WATER_OCEANGRADIENT_01.BMP

[FresnelMap Textures]
FN=0:water_oceangradient_01.bmp
FN=1:water_oceangradient_01_.bmp
FN=2:Waterbump.bmp
FN=3:WATER_OCEANGRADIENT_01.BMP
FN=4:WATER_NOMAL_02.BMP
```

### Wasser-Loader und Pack

Relevante Namen/Xrefs:

- [`AgcmWater`](../Module/AgcmWater.md)
- `world\water`
- `world\water\WT%d.dat`
- `WATERFILE_L1`
- `WATERFILE_L2`
- `OP_Water`
- `OP_UpdateWater`
- `MakeHWaterFromWater : Status_ID (%d)`

Wichtige Funktionen:

- `FUN_00645f70`: liest/parst die Classic-Water-Statusfelder aus `waterstatust1.ini`.
- `FUN_00648be0`: referenziert `world\water\WT%d.dat`.
- `FUN_005df350`: registriert/verdrahtet `AgcmWater`, [`AgcmGrass`](../Module/AgcmGrass.md), `OP_Water`, `OP_UpdateWater`.
- `FUN_00643580` / `FUN_00692b50`: `AgcmWater`-Modulspuren.

`world\water` Pack:

- `Reference.Dat` root: `world\water`
- Eintraege: 137
- Gesamtpayload: 3374620 Bytes
- Dateigroessen:
  - Minimum: 4100 Bytes
  - Maximum: 135996 Bytes
  - Durchschnitt: ca. 24632 Bytes

Erste Eintraege:

| Index | Name | Offset | Size |
|---:|---|---:|---:|
| 0 | `wt2024.dat` | `0x0025B834` | 24820 |
| 1 | `wt2125.dat` | `0x0030CE78` | 96844 |
| 2 | `wt2126.dat` | `0x00261928` | 17636 |
| 3 | `wt2627.dat` | `0x003248C4` | 78796 |
| 4 | `wt2727.dat` | `0x00121094` | 8116 |

Beobachtete interne WT-Struktur:

```text
extracted_wt2024.dat
len=24820
u32[0..3]=0x00000002,0x00000804,0x00000018,0x0000081C
```

Interpretation:

- Keine weitere RC4-Schicht sichtbar.
- Anfang ist eine interne Tabelle.
- Viele erste Datenbloecke sind klein (`0x18` Bytes), wahrscheinlich pro Subtile/Water-Plane-Eintrag.

## Gras

### `grasstemplate.ini`

`ini\grasstemplate.ini`

- Entschluesselt mit `1111`.
- Abschnitte:
  - `[Textures]`
  - `[GRASSINFO]`
- 31 Grass-Texturen (`TEXTURE_NAME=0..30`).
- 124 Grass-Template-IDs.
- 13 `GRASS_GROUP`-Gruppen.

Texturen:

```ini
TEXTURE_NAME=0:GRASS_HU_01.tif
TEXTURE_NAME=1:GRASS_HU_02.tif
TEXTURE_NAME=2:GRASS_HU_03.tif
...
TEXTURE_NAME=30:grass_ep_3st_02.tif
```

Wichtige Felder pro Grass-Template:

- `GRASS_ID`
- `GRASS_NAME`
- `TEXTURE_ID`
- `SHAPE_TYPE`
- `GRASS_WIDTH`
- `GRASS_HEIGHT`
- `GRASS_WIDTH_RANDOM`
- `GRASS_HEIGHT_RANDOM`
- `ANIM_TYPE`
- `ANIM_AMOUNT`
- `ANIM_SPEED`
- `IMAGE_START_X`, `IMAGE_START_Y`
- `IMAGE_WIDTH`, `IMAGE_HEIGHT`

Beobachtete Wertebereiche:

| Feld | Bereich / Werte |
|---|---|
| `GRASS_ID` | 124 Eintraege |
| `TEXTURE_ID` | `0..30` |
| `SHAPE_TYPE` | `0, 1` |
| `GRASS_WIDTH` | `40..150` |
| `GRASS_HEIGHT` | `100..170` |
| `GRASS_WIDTH_RANDOM` | `1..5` |
| `GRASS_HEIGHT_RANDOM` | `1..5` |
| `ANIM_TYPE` | immer `0` in dieser Datei |
| `ANIM_AMOUNT` | `2..6` |
| `ANIM_SPEED` | `1..5` inklusive Dezimalwerten wie `1.5` |

Parserbeleg:

- `FUN_0064d030` liest u.a.:
  - `TEXTURE_NAME`
  - `GRASS_ID`
  - `GRASS_NAME`
  - `TEXTURE_ID`
  - `SHAPE_TYPE`
  - `GRASS_WIDTH`
  - `GRASS_HEIGHT`
  - `GRASS_WIDTH_RANDOM`
  - `GRASS_HEIGHT_RANDOM`
  - `ANIM_TYPE`
  - `ANIM_AMOUNT`
  - `ANIM_SPEED`
  - `IMAGE_*`

### Grass-Loader und Pack

Relevante Namen/Xrefs:

- `AgcmGrass`
- `world\grass`
- `world\grass\GR%d.dat`
- `BGrass Draw: %d`

Wichtige Funktionen:

- `FUN_0064b5f0`: referenziert `world\grass\GR%d.dat`.
- `FUN_0064c9e0`: `AgcmGrass`-Konstruktor/Init, setzt Root `world\grass`.
- `FUN_0064d030`: parst `grasstemplate.ini`.

`world\grass` Pack:

- `Reference.Dat` root: `world\grass`
- Eintraege: 174
- Gesamtpayload: 75859848 Bytes
- Dateigroessen:
  - Minimum: 3076 Bytes
  - Maximum: 6393816 Bytes
  - Durchschnitt: ca. 435976 Bytes

Erste Eintraege:

| Index | Name | Offset | Size |
|---:|---|---:|---:|
| 0 | `gr1831.dat` | `0x0002AB74` | 467308 |
| 1 | `gr1928.dat` | `0x00448DF8` | 872272 |
| 2 | `gr2020.dat` | `0x007E66E0` | 219644 |
| 3 | `gr2024.dat` | `0x011B5350` | 4328072 |
| 4 | `gr2120.dat` | `0x011AFFB4` | 12176 |

Beobachtete interne GR-Struktur:

```text
extracted_gr1831.dat
len=467308
u32[0..3]=0x00000002,0x00000804,0x00000004,0x00000808
```

Interpretation:

- Keine weitere RC4-Schicht sichtbar.
- Anfang ist eine interne Offset-/Laengen-Tabelle.
- Viele Anfangseintraege sind `0x04` Bytes gross, was auf kompakte per-cell IDs/Flags hindeutet.

## Sky und Nature Effects

### `alefskysetting.ini`

- Kleine Texturzuordnung fuer Sky-Texturen.

```ini
[Texture]
01=SKY00001.tif
02=SKY00002.tif
03=SKY00003.tif
09=SKY00009.tif
10=SKY00010.tif
00=SKY00000.tif
05=SKY00005.tif
```

### `skyset.ini`

- 147 nummerierte SkySet-Abschnitte.
- Section-IDs beobachtet: `0..148`, mit einer Luecke.
- Pro Abschnitt sind `ModuleData1=AgpmEventNature` und `ModuleData2=AgcmEventNature` typisch.
- Zeit-/State-Slots: `00`, `05`, `07`, `13`, `19`, `21`.
- Typische Felder pro Slot:
  - `SkyTop`, `SkyBottom`
  - `Ambient`, `Directional`
  - `CloudTexture1`, `CloudSpeed1`, `CloudColor1`
  - `CloudTexture2`, `CloudSpeed2`, `CloudColor2`
  - `Circumstance`, `CircumstanceColor`
  - `Sun`, `SunColor`
  - `FogColor`, `FogDistance`, `FogFarClip`
  - `EffectInterval`
  - `EffectIndex_01..05`
  - `EffectRate_01..05`
  - `BackGroundMusic`
  - `WeatherEffect1`, `WeatherEffect2`

### `natureeffect.ini`

- 3 Texturen:
  - `NE_Snow.tif`
  - `NE_Rain.tif`
  - `NE_Pollen.tif`
- 11 NatureEffect-IDs.
- Wichtige Felder:
  - `NEFFECT_ID`
  - `TEXTURE_ID`
  - `NEFFECT_TYPE`
  - `NEFFECT_SIZE_MIN/MAX`
  - `NEFFECT_SPEED_MIN/MAX`
  - `NEFFECT_SWING_MIN/MAX`
  - `NEFFECT_DENSITY_MIN/MAX`
  - `NEFFECT_RED/GREEN/BLUE/ALPHA_MIN/MAX`
  - `NEFFECT_SKYSET`

Beobachtete Zuordnung:

| NEFFECT_ID | TEXTURE_ID | TYPE | SKYSET |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 98 |
| 1 | 1 | 1 | 99 |
| 2 | 0 | 0 | 112 |
| 3 | 0 | 0 | 101 |
| 4..10 | 0 | 0 | 0 |

## Offene Punkte

- Die innere Struktur von `OT*.dat`, `WT*.dat` und `GR*.dat` ist noch nicht komplett dekodiert.
- Bisheriger Stand: alle drei Dateitypen starten mit internen Tabellen und liegen nach Pack-Extraktion unverschluesselt vor.
- Naechster sinnvoller Schritt ist ein Parser fuer diese Tabellen:
  - erstes DWORD als Tabellen-/Header-Typ pruefen,
  - danach Offset/Size-Paare validieren,
  - alle Offsets gegen Dateilaenge pruefen,
  - Subchunks klassifizieren.
