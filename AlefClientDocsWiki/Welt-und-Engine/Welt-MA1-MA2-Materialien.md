# Alefclient World-Dateien, MA1/MA2, 3D-Infos und Materials

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Welt, Engine und Rendering](Index.md)*

Stand: 2026-09-05

## Kurzfazit

Die installierten World-Dateien unter `C:\Spiele\Archlord\world` sind sektorbasierte MagPack-Container:

- `*.ma1`: kleine sektorweise `C*.amf` Payloads, sehr wahrscheinlich Terrain-/Collision-/Height-Daten
- `a*.ma2`: sektorweise `R*.dff` Payloads
- `b*.ma2`: sektorweise `D*.dff` Payloads

Der Client laedt diese Daten ueber eigene Pack-/Dekompressionsfunktionen und uebergibt die dekomprimierten Streams danach an RenderWare:

- `FUN_0058b170`: oeffnet/liest `MagPack Ver 0.1a`
- `FUN_0058afb0` / `FUN_0058af10`: sucht Eintrag nach Name und dekomprimiert ihn
- `FUN_008518f0`: aPLib-artige Dekompression
- `FUN_005f3a70`: liest aus einem `R*.dff`-Stream zuerst ein RenderWare Texture Dictionary
- `FUN_007357d0`: liest danach einen RenderWare Atomic/Clump-nahen Streamteil ueber Chunk `0x14`

Damit ist die Welt nicht eine monolithische RenderWare-World-Datei, sondern ein 16x16-Sektorstreaming-System mit getrennten Containerdateien fuer Height/Collision, Terrain-Renderdaten und Detail-/Zusatzdaten.

## Installierter Dateibestand

Quelle: `C:\Spiele\Archlord\world`

| Typ | Anzahl | Groesse |
| --- | ---: | --- |
| `*.ma1` | 177 | min 9,267, max 186,032, avg ca. 23,156 Bytes |
| `a*.ma2` | 167 | min 1,590,085, max 4,622,920, avg ca. 2,754,787 Bytes |
| `b*.ma2` | 167 | min 2,248,579, max 5,001,190, avg ca. 3,574,008 Bytes |

Namensbereich:

- `ma1`: nur Prefix `a`
- `ma2`: Prefix `a` und `b`
- erkannte Koordinatenbereiche in Dateinamen: X `17..32`, Z `17..32`
- Beispiel: `a001717x.ma2` enthaelt Sektoren X `272..287`, Z `272..287`

Dateiname-Mapping:

```text
divisionId = ((sectorX + 400) >> 4) * 100 + ((sectorZ + 400) >> 4)
```

Beispiel:

```text
sectorX = -128 -> sectorX + 400 = 272
sectorZ = -128 -> sectorZ + 400 = 272
divisionId = 17 * 100 + 17 = 1717
World\a001717x.ma1
World\a001717x.ma2
World\b001717x.ma2
```

## MagPack-Containerformat

Alle untersuchten `ma1`/`ma2` Dateien beginnen mit:

```text
MagPack Ver 0.1a
```

Header-/Table-Aufbau aus Tooling und Client-Pseudocode:

```c
char header[0x32];              // "MagPack Ver 0.1a", nullgefuellt
for (i = 0; i < 0x100; i++) {
    uint8  nameLen;
    char   name[nameLen];
    uint32 storedSizeXor;       // storedSize ^ 0x6969
}
uint8 tableEndZero;             // 0
for (i = 0; i < 0x100; i++) {
    uint32 unpackedSizeXor;     // unpackedSize ^ 0x6969
    byte   compressed[storedSize];
}
```

Konstanten:

- Headergroesse: `0x32`
- Eintraege pro Pack: `0x100` = 256
- XOR-Key fuer Groessenfelder: `0x6969`
- Dekompression: aPLib-artiger Depacker in `FUN_008518f0`

Client-Belege:

- `alefclient.pseudocode.c:331598`: Headervergleich mit `MagPack Ver 0.1a`
- `alefclient.pseudocode.c:331660`: `storedSize = value ^ 0x6969`
- `alefclient.pseudocode.c:331315`: `unpackedSize = firstDword ^ 0x6969`
- `alefclient.pseudocode.c:331327` und `331404`: Dekompression ueber `FUN_008518f0`

## MA1: AMF-Sektordaten

Loader-Fund:

- `alefclient.pseudocode.c:223087`: `wsprintfA(..., "a%06dx.ma1", divisionId)`
- `FUN_00511bc0`: cachet bis zu 9 `ma1`-Packs und oeffnet daraus Sektordaten

Eintraege in `a001717x.ma1`:

```text
C272,272.amf
C273,272.amf
C274,272.amf
...
```

Beispielwerte aus `a001717x.ma1`:

| Eintrag | Stored/Packed | Unpacked |
| --- | ---: | ---: |
| `C272,272.amf` | 26 | 1,040 |
| `C273,272.amf` | 23 | 1,040 |
| `C274,272.amf` | 45 | 1,040 |

Alle geprueften AMF-Eintraege aus `a001717x.ma1` haben `unpackedSize = 1040`.

Bekannte Struktur aus dekomprimiertem Sample `C272,272.amf`:

- Laenge: 1,034 bis 1,040 Bytes, je nach Tool/Endpadding
- Anfang als DWord: `0x00001002`
- danach sehr regelmaessige 16-bit-/32-bit-Werte, z.B. viele Hoehenwerte um `0x0E65`

Interpretation:

- `C*.amf` ist sehr wahrscheinlich ein kompakter pro-Sektor Height-/Collision-/Terrain-Samplingblock.
- 1,040 Bytes passen gut zu einem festen Raster plus kleinem Header.
- Die Werte wirken wie Terrainhoehen oder komprimierte Collision-/Walkmesh-Hoehen.

Offen:

- Exakte Feldbreiten und Rasterdimension sind noch nicht final benannt.
- Das Sample zeigt regelmaessige Werte, aber die direkte RenderWare-Geometrie liegt nicht im `C*.amf`-Top-Level.

## MA2: R- und D-DFF-Sektoren

Der Client hat zwei getrennte `ma2`-Pfade:

### R-Pfad

Fundstellen:

- `alefclient.pseudocode.c:411054`: `a%06dx.ma2`
- `alefclient.pseudocode.c:411055`: `R%d,%d.dff`
- `FUN_005f3b10`: direkter R-Sektor-Ladepfad mit Transform/Placement
- `FUN_005f4020`: generischer Ladepfad fuer Typ `param_3 == 1`

Beispiel `a001717x.ma2`:

| Eintrag | Stored/Packed | Unpacked |
| --- | ---: | ---: |
| `R272,272.dff` | 11,772 | 32,236 |
| `R273,272.dff` | 11,570 | 32,236 |
| `R274,272.dff` | 11,711 | 32,236 |

Alle geprueften `R*.dff` in `a001717x.ma2` haben `unpackedSize = 32,236`.

Nach aPLib-Dekompression beginnt `R272,272.dff` mit RenderWare Chunk `0x16`:

```text
id      = 0x00000016
size    = 11120
version = 0x1C02002D
```

`0x16` ist RenderWare Texture Dictionary. Im dekomprimierten Sample finden sich vier `DXT1`-Texturblöcke bei:

```text
0x0080
0x0980
0x1280
0x1B80
```

Das legt nahe:

- `R*.dff` enthaelt mindestens ein sektorbezogenes RenderWare Texture Dictionary.
- Die Texturen sind DXT1-komprimiert.
- Der Texture-Dictionary-Name entspricht dem Sektor, z.B. `R272,272`.

Client-Verhalten:

- `FUN_005f3a70` sucht zuerst Chunk `0x16`.
- Danach wird das Texture Dictionary gelesen.
- Texturen werden in ein Texture Dictionary des Renderers eingefuegt.
- Danach wird der Stream weiter fuer `FUN_007357d0` benutzt.

### D-Pfad

Fundstellen:

- `alefclient.pseudocode.c:411308`: `b%06dx.ma2`
- `alefclient.pseudocode.c:411311`: `D%d,%d.dff`
- `FUN_005f4020`: generischer Ladepfad fuer Typ `param_3 == 2`

Beispiel `b001717x.ma2`:

| Eintrag | Stored/Packed | Unpacked |
| --- | ---: | ---: |
| `D272,272.dff` | 16,218 | 127,436 |
| `D273,272.dff` | 16,054 | 127,436 |
| `D274,272.dff` | 15,588 | 127,944 |
| `D282,272.dff` | 17,461 | 128,290 |

In `b001717x.ma2`:

- Packed min/max/avg: 8,705 / 19,497 / ca. 15,469 Bytes
- Unpacked min/max/avg: 127,436 / 136,388 / ca. 128,825 Bytes

Interpretation:

- `D*.dff` ist deutlich groesser als `R*.dff` und wird anders gerendert/initialisiert.
- Im `D`-Pfad setzt der Client vor dem Atomic/Clump-Read ein Texture Dictionary und ruft `FUN_00662410(param_1 + 0xf5c)`.
- Nach erfolgreichem Laden werden Materials/Atomics je nach Geometrietyp nachbearbeitet.

Offen:

- Das alte Hilfsprogramm `ALMapCompressor.exe` hat fuer `D*.dff` einen zu kleinen festen Zielpuffer (`0x7DEC`) und kann diese Samples nicht dekomprimieren.
- Die korrekte Unpacked-Size steht aber im Pack selbst; fuer `D272,272.dff` ist sie `127436`.
- Der naechste praktische Schritt ist ein kleiner eigener `FUN_008518f0`/aPLib-kompatibler Depacker mit variablem Zielpuffer.

## RenderWare-Stream-Aufbau

### Texture Dictionary

`FUN_005f3a70`:

```text
RwStreamFindChunk(stream, 0x16, ...)
RpTextureDictionaryStreamRead(stream)
TextureDictionaryForAllTextures(... callback ...)
```

Effekt:

- Sektor-Texturen aus `R*.dff` werden geladen.
- Danach wird das vorherige globale/aktive Texture Dictionary wieder zurueckgesetzt.

### Atomic-/Clump-naher Teil

`FUN_007357d0`:

```text
read uint32 from stream
if != 0:
    find RenderWare chunk 0x14
    read object via FUN_00435440(stream)
    attach current frame/transform
```

`0x14` ist im RenderWare-Kontext ein Atomic-Chunk. Das passt dazu, dass die Sektorwelt nicht als ein globaler `RpWorld` geladen wird, sondern als viele sektorweise Atomics/Clumps.

### Render Flags / Nachbearbeitung

In `FUN_005f4020`:

- Typ `1` / `R*.dff`: rendert/registriert mit Flag `0x24`
- Typ `2` / `D*.dff`: wenn Geometrie-Typ `2`, Flag `0x14`, sonst `0x04`
- Bei Typ `2` werden Materials iteriert:
  - `FUN_0064ec00(material)`
  - `FUN_0064ecb0(material, FUN_005f2760)`

Das sieht nach einem Material-/RenderCallback fuer Detail- oder Spezialmaterialien aus.

## Materialien und Material-Extensions

Der Client hat eigene RenderType-/Materialdaten auf RenderWare-Materialien.

Wichtige globale Hinweise:

- `AgcmRenderType::vftable`
- `AgcdClumpRenderTypeData::vftable`
- `CRT_CLUMP_RENDER_TYPE_NUM`
- `CRT_CLUMP_RENDER_TYPE%d`
- `RidableMaterialType`
- `materialAmbient`
- `materialDiffuse`
- `materialSpecular`
- `materialColr`

Material-Helper:

- `FUN_0064ec00`: holt plugin-/extensiondaten fuer ein Material
- `FUN_0064ec50`: setzt/liest Effektparameter, z.B. `materialDiffuse`
- `FUN_0064ec70`: setzt Texturparameter, z.B. `animTexture`
- `FUN_0064ec90`: liest Effektparameter, z.B. `materialDiffuse`
- `FUN_0064ecb0`: setzt Material-Callback an Offset `+0x8b0`
- `FUN_0064ee80`: prueft, ob fuer ein Objekt/Atomic RenderType-Daten existieren

Gesehene Materialparameter:

| Parameter | Kontext |
| --- | --- |
| `materialAmbient` | Ambient-Farbe als Effekt-/Materialkonstante |
| `materialDiffuse` | Diffuse-Farbe; wird auch temporaer veraendert, z.B. Alpha-/Fade-Pfad |
| `materialSpecular` | Specular-Farbe |
| `animTexture` | Zusatztextur fuer UV-Animation |
| `velocity` | UV-/Effektbewegung |
| `materialColr` | serialisierte RGBA-/Farbinfo in Effekt-/Clumpdaten |

Die `.fx`-Shader aus `C:\Spiele\Archlord\effect` passen zu diesen Parametern:

- `simple.fx`: `materialAmbient`, `materialDiffuse`, `materialSpecular`
- `uvanim*.fx`: `animTexture`, `velocity`, Materialfarben
- `perpixelgloss*.fx`: Material-/Glossparameter
- `detailbump.fx`: Bump/OIM-Materialdaten

## Texturpfade fuer World-Materials

Der Ressourcenpfad fuer Welttexturen ist in `FUN_00410e20` sichtbar:

- `Texture\World\`
- `Texture\World\Low\`
- `Texture\World\Medium\`
- `texture\world`
- `texture\world\low`
- `texture\world\medium`

Im vorherigen TX1-Fund wurde bestaetigt:

- `texture\world` liegt gepackt in `Data.Dat`/`Reference.Dat`
- `.tx1` Dateien dekodieren mit Key `asdfqwer`
- Ergebnis ist RenderWare Texture Dictionary Chunk `0x16`

Damit gibt es zwei World-Texturquellen:

- grosse globale/regionale `texture\world\*.tx1` Texture Dictionaries
- sektorbezogene `R*.dff` Texture Dictionaries aus `a*.ma2`

## Zusammenhang mit Octree/Wasser/Gras

Die `ma1`/`ma2` World-Dateien sind nicht dasselbe wie:

- `world\octree\OT%d.dat`
- `world\water\WT%d.dat`
- `world\grass\GR%d.dat`

Alle sind aber an dasselbe Sektor-/Division-System gekoppelt:

- 800x800 Weltgrid
- Divisionen in 16x16 Sektoren
- Dateinamen kodieren Sektor-/Divisionkoordinaten mit `+400` Offset

Die Trennung wirkt so:

| Datenbereich | Dateien | Inhalt |
| --- | --- | --- |
| Terrain/Collision/Height | `a*.ma1` -> `C*.amf` | kompakte AMF-Sektordaten |
| Terrain Render/Texturen | `a*.ma2` -> `R*.dff` | RenderWare Texture Dictionaries plus weiterer Stream |
| Detail-/Zusatz-3D | `b*.ma2` -> `D*.dff` | groessere RenderWare Atomic/Clump-nahe Daten |
| Spatial Partition | `world\octree\OT*.dat` | Octree-IDs/BBox/Objektpartition |
| Wasser | `world\water\WT*.dat` | Wasserflaechen/Waves |
| Gras | `world\grass\GR*.dat` | Grass-Instanzen/Templates |

## Material-Aufbau der World-Daten

Die Materials werden zur Laufzeit aus mehreren Quellen zusammengesetzt. Es gibt aktuell keinen Hinweis auf eine separate World-Material-Datei neben den `ma2`-Streams; der Client baut die Materialbindung aus RenderWare-Daten, Texture Dictionaries und einer eigenen Material-Plugin-Erweiterung.

### 1. Sector-Stream laden

Der World-Loader waehlt je nach Datentyp einen MagPack-Container und einen Eintrag:

- Terrain/Render-Sektor: `a%06dx.ma2` -> `R%d,%d.dff`
- Detail-/Zusatz-Geometrie: `b%06dx.ma2` -> `D%d,%d.dff`

Die Eintraege werden aus `MagPack Ver 0.1a` gelesen, mit XOR `0x6969` entgroesst und ueber den aPLib-aehnlichen Depacker (`FUN_008518f0`) entpackt. Danach wird aus dem entpackten Speicher ein RenderWare-Stream erstellt.

### 2. Texture Dictionary vorbereiten

Fuer `R*.dff` ruft der Loader `FUN_005f3a70` auf. Diese Funktion sucht im Stream nach RenderWare Chunk `0x16` und liest ihn als Texture Dictionary. Danach werden die Texturen iteriert und in das aktive/rendererweite Texture Dictionary bei `renderer + 0xba0 + 0x112c` uebernommen.

Der bereits dekomprimierte Testsektor `R272,272.dff` bestaetigt dieses Bild:

- Top-Level Chunk: `0x16` / Texture Dictionary
- RW-Version: `0x1C02002D`
- Name: `R272,272`
- 4 erkannte `DXT1`-Texturbloecke

Fuer `D*.dff` wird kein eigenes TXD aus demselben Stream vorgeladen. Der Loader setzt stattdessen das aktive Texture Dictionary auf das rendererweite Dictionary (`FUN_004bf290(... + 0x112c)`) und schreibt ueber `FUN_00662410(param_1 + 0xf5c)` den aktuellen Texture-/Suchpfad in TLS. `FUN_00662410` ist sehr klein und setzt nur `TLS + 0x14 = param_1`; das ist wahrscheinlich der aktuelle Ressourcenpfad, den der RenderWare-Loader beim Aufloesen von Textur-Namen nutzt.

### 3. Atomic/Geometry erzeugt die Basis-Materials

Nach der Texture-Dictionary-Vorbereitung ruft der Loader `FUN_007357d0` auf. Diese Funktion liest aus dem RenderWare-Stream weiter und sucht Chunk `0x14`, also RenderWare Atomic. Daraus entstehen die eigentlichen `RpAtomic`/`RpGeometry`/`RpMaterial`-Objekte.

Die Basis-Materialien kommen damit direkt aus dem RenderWare-Stream:

- Materialliste der Geometry
- Textur-Referenzen per Name/Dictionary
- Materialfarbe und Surface Properties aus dem RW-Material
- eventuelle RW-Extensions

### 4. Eigenes Material-Plugin

Der Client registriert in `FUN_0064eaf0` mehrere RenderWare-Plugin-Erweiterungen mit Plugin-ID `0xfffff009`. Dazu gehoeren Erweiterungen fuer Objekt-/Geometry-/Material-nahe Daten. Fuer Materials ist besonders die globale Offset-Verwaltung um `DAT_0095d8ac` wichtig.

Wichtige Wrapper:

- `FUN_0064ec00(material)` gibt die eigene Material-Plugin-Struktur zurueck.
- `FUN_0064ec20(material, key, float)` setzt Float-Parameter.
- `FUN_0064ec50(material, key, vec4)` setzt Vektor-/Farbparameter.
- `FUN_0064ec70(material, key, texture)` setzt Texturparameter.
- `FUN_0064ec90(...)` setzt ebenfalls einen Material-/Effect-Parameter ueber die Plugin-Struktur.
- `FUN_0064ecb0(material, callback)` schreibt einen Callback nach `pluginData + 0x8b0`.

Beim Laden von `D*.dff` gibt es einen speziellen Pfad: Wenn die geladene Geometry vom Typ `2` ist, iteriert der Client ueber die Materialliste. Fuer jedes Material mit vorhandener Plugin-Struktur setzt er:

```text
FUN_0064ecb0(material, FUN_005f2760)
```

`FUN_005f2760` holt spaeter die Plugin-Struktur des Materials (`FUN_0064ebf0`) und ruft ueber die Render-/Pipeline-Struktur einen Funktionszeiger bei Offset `0xD0` auf. Als Argument wird auch ein Wert aus der Plugin-Struktur bei `DAT_009eefec` uebergeben. Das sieht nach der finalen Bindung der erweiterten Materialdaten an den Renderpfad aus.

### 5. Effect-/Shader-Parameter werden auf Materials geschrieben

Ein separater Parser verarbeitet Material-/Effect-Kommandos und schreibt sie ueber die `FUN_0064ec*`-Wrapper in die Material-Plugin-Daten. Sichtbare Schluessel:

| Kommando | Wirkung |
| --- | --- |
| `TEXTURE` | laedt eine Textur und setzt `animTexture` |
| `AMBIENT` | RGB bytes -> float RGBA, setzt `materialAmbient` |
| `DIFFUSE` | RGB bytes -> float RGBA, setzt `materialDiffuse` |
| `SPECULAR` | RGB bytes -> float RGBA, setzt `materialSpecular` |
| `Uv Translation` | vec4, setzt `velocity` |
| `UV Scale` | vec4, setzt `scale` |
| `UV Rotation` | float, setzt `rotation` |
| `UV Anim weight` | float, setzt `weight` |
| `U Selection vector` | vec4, setzt `uSelect` |
| `V Selection vector` | vec4, setzt `vSelect` |

Diese Parameter passen zu den gefundenen FX-Dateien wie `uvanim*.fx`, `simple.fx`, `perpixelgloss*.fx` und `detailbump.fx`. Die World-Materials bestehen also nicht nur aus RW-Standardmaterialien, sondern aus:

```text
RW Geometry Material
  + Texture Dictionary Binding
  + Client Material Plugin 0xfffff009
  + Effect-/Shader-Parameter
  + optionaler Render-Callback FUN_005f2760
```

### 6. Renderpfad-Auswahl

Nach dem Laden registriert der Client das Objekt ueber `FUN_007065f0` mit unterschiedlichen Flags:

- `R*.dff`/Terrain-Renderpfad: Flag `0x24`
- `D*.dff` mit Geometry-Typ `2`: Flag `0x14`
- sonstiger `D*.dff`-Pfad: Flag `0x04`

Damit entscheidet nicht allein das Material im DFF ueber das Rendering. Der World-Loader waehlt zuerst einen Objekt-/Renderpfad, danach ergaenzt die Material-Plugin-Struktur die eigentlichen Shader- und Texturparameter.

## Praktische Befehle / Tools

Vorhandenes Tooling:

- `ALMapExtractor`
- `ALMapCompressor`

Wichtige Einschraenkung:

- `ALMapExtractor` extrahiert MagPack-Eintraege, schreibt aber die einzelnen Streams noch komprimiert.
- `ALMapCompressor` kann `R*.dff` dekomprimieren, hat aber fuer `D*.dff` aktuell einen zu kleinen Zielpuffer.

Neues Workspace-Hilfstool:

- `tools\extract_magpack_entry.py`

Status:

- Das Tool liest MagPack-Tabellen und berechnet `storedSize`/`unpackedSize` korrekt.
- Die integrierte pure-Python-aPLib-Dekompression ist noch nicht validiert und erzeugt aktuell keine belastbaren `D*.dff` Ergebnisse.
- Fuer reine Header-/Tabellenanalyse ist das Tool bereits nutzbar.

## Naechste sinnvolle Schritte

1. Den Depacker in `tools\extract_magpack_entry.py` gegen `FUN_008518f0` exakt anpassen oder stattdessen den vorhandenen C-Depacker mit variablem Zielpuffer neu bauen.
2. `D*.dff` dekomprimieren und auf RenderWare Top-Level-Chunks `0x14`, `0x10`, `0x1A` und Extension-Chunks scannen.
3. `DAT_00c301d4..DAT_00c301f8` Shader-Slots mit den `R`/`D` Renderpfaden verknuepfen.
4. Material-Callbacks aus `FUN_0064ecb0(..., FUN_005f2760)` und `FUN_005f2760` rueckbenennen.
5. `C*.amf`-Raster entschluesseln: Header, Hoehenraster, eventuelle Collision-/Walkability-Bits.
