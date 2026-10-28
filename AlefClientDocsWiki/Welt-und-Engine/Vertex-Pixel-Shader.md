# Alefclient Vertex- und Pixel-Shader - Findings

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Welt, Engine und Rendering](Index.md)*

Stand: 2026-09-05

## Kurzfazit

Der Client nutzt eine klassische Direct3D-9/D3DX-Effect-Pipeline. Es gibt zwei Shader-Quellen:

- lose HLSL/FX-Dateien unter `C:\Spiele\Archlord\effect\*.fx`
- zur Laufzeit zusammengebaute Vertex-Shader-Assembler-Strings im Client-Code

Die Asset-Shader sind fast durchgehend DirectX-8/9-era Profile:

- Vertex Shader: ueberwiegend `vs_1_1`
- Pixel Shader: `ps_1_1`, `ps_1_2`, vereinzelt `ps_1_4`, `ps_2_0`
- `simple.fx` nennt noch `vs_1_0`; der D3DX-Code im Client remappt `vs_1_0` intern auf `vs_1_1`.

## D3DX-/Shader-System in der Binary

Relevante Strings und Xrefs aus `alefclient.pseudocode.c` und `engine_keyword_xrefs.tsv`:

| Fund | Bedeutung |
| --- | --- |
| `Microsoft (R) D3DX9 Shader Assembler 5.04.00.2904` | eingebetteter/gelinkter D3DX9-Assembler-Code |
| `Microsoft (R) D3DX9 Shader Compiler 5.04.00.2904` | eingebetteter/gelinkter D3DX9-Compiler-Code |
| `Direct3DShaderValidatorCreate9` | Shader-Validator wird dynamisch gesucht |
| `vertexshader`, `pixelshader` | D3DX-Effect-Parser-Tokens |
| `VERTEXSHADERCONSTANT*`, `PIXELSHADERCONSTANT*` | D3DX Effect State/Constant Handling |
| `$PRESHADER_VS`, `$PRESHADER_PS` | D3DX PresShader-Unterstuetzung |

Wichtige Pseudocode-Fundstellen:

- `alefclient.pseudocode.c:61934`: `vs_1_0 is no longer supported; using vs_1_1`
- `alefclient.pseudocode.c:61938`: `ps_1_0 is no longer supported; using ps_1_1`
- `alefclient.pseudocode.c:62021`: Assembly-Fragmente werden nur fuer `vs_1_1`, `vs_2_0`, `vs_2_x`, `vs_2_sw`, `ps_2_0`, `ps_2_x`, `ps_2_sw` akzeptiert.
- `alefclient.pseudocode.c:151192` und `151475`: D3DX9 Shader Compiler String
- `alefclient.pseudocode.c:59740` und `59858`: D3DX9 Shader Assembler String

## Effect-Dateien

Gefundene Shader-Assets unter `C:\Spiele\Archlord\effect`:

| Datei | Groesse | VS | PS | Techniques |
| --- | ---: | --- | --- | --- |
| `ambientocclusion.fx` | 9,291 | `vs_1_1` | `ps_1_2` | `AmbientOcclusion`, `Simple`, `AmbOcclOnly` |
| `ambientocclusionmvl.fx` | 10,539 | `vs_1_1` | `ps_1_2` | `AmbientOcclusionMVL`, `Simple`, `AmbOcclMVLOnly` |
| `ambientocclusionmvl2.fx` | 10,629 | `vs_1_1` | `ps_1_2` | `AmbientOcclusionMVL`, `Simple`, `AmbOcclMVLOnly` |
| `ambientocclusionppl.fx` | 10,565 | `vs_1_1` | `ps_1_2` | `AmbientOcclusionPPL`, `Simple`, `AmbOcclPPLOnly` |
| `detailbump.fx` | 14,143 | `vs_1_1` | `ps_1_1`, `ps_2_0` | `DetailBump`, `OcclusionIntervalMaps`, `Simple` |
| `invisible.fx` | 9,462 | `vs_1_1` | fixed-function/null PS | `Invisible` |
| `perpixelgloss.fx` | 9,201 | `vs_1_1` | `ps_1_1` | `PerPixelGloss`, `Simple` |
| `perpixelgloss2.fx` | 14,213 | `vs_1_1` | `ps_1_1` | `PerPixelGloss`, `Simple` |
| `perpixelgloss3.fx` | 14,160 | `vs_1_1` | `ps_1_1` | `PerPixelGloss`, `Simple` |
| `post.fx` | 62,516 | `vs_1_1` | `ps_1_1`, `ps_1_4`, `ps_2_0` | viele Post-FX Techniques |
| `scygnus.fx` | 14,684 | `vs_1_1` | `ps_1_2` | `RandomTwinkle`, `TSS`, `Simple` |
| `simple.fx` | 6,357 | `vs_1_0` | fixed-function/null PS | `Simple` |
| `uvanim.fx` | 16,270 | `vs_1_1` | `ps_1_1` | `UVAnim`, `Simple` |
| `uvanimaddalpha.fx` | 16,257 | `vs_1_1` | `ps_1_1` | `UVAnim`, `Simple` |
| `uvanimaddalpha2.fx` | 16,420 | `vs_1_1` | `ps_1_1` | `UVAnim`, `Simple` |
| `uvanimaddalpha3.fx` | 14,981 | `vs_1_1` | `ps_1_1` | `UVAnim`, `Simple` |
| `uvanimrevsubtract.fx` | 15,810 | `vs_1_1` | `ps_1_1` | `UVAnim`, `Simple` |

## Effect-Gruppen

### Simple / fixed-function Fallback

`simple.fx` ist ein einfacher Per-Vertex-Lighting-Shader. Er nutzt:

- `worldViewProj : WorldViewProjection`
- `worldView : WorldView`
- optional `boneMatrices : BoneMatrices`
- `Fog`, `LightAmbient`, `LightDirection`, `LightColor`
- `LightPosition0/1`, `LightDirection0/1`, `LightParameters0/1`, `LightColor0/1`

Technique:

- `Simple`
- `VertexShader = compile vs_1_0 SimpleVS();`
- `PixelShader = NULL;`

Da die Binary `vs_1_0` auf `vs_1_1` umbiegt, ist das praktisch ein `vs_1_1`-Pfad mit fixed-function Pixel-Verarbeitung.

### Ambient Occlusion

Dateien:

- `ambientocclusion.fx`
- `ambientocclusionmvl.fx`
- `ambientocclusionmvl2.fx`
- `ambientocclusionppl.fx`

Gemeinsame Merkmale:

- Basistextur plus Ambient-Occlusion-Textur
- meist `Normalize.dds` als Cube-Map fuer Normalisierung
- Per-Vertex-Lighting mit Fog
- Pixel-Shader in `ps_1_2`

Varianten:

- `MVL`: Many Vertex Lights, bis zu 5 lokale Lichter im Vertex Shader vorbereitet
- `PPL`: Per Pixel Lighting, zwei Passes fuer lokale Lichtbeitraege
- `Simple`: fixed-function/null Pixel-Shader-Fallback
- `AmbOcclOnly`: rendert nur/primär AO-Anteil

### PerPixelGloss

Dateien:

- `perpixelgloss.fx`
- `perpixelgloss2.fx`
- `perpixelgloss3.fx`

Gemeinsame Merkmale:

- `vs_1_1` plus `ps_1_1`
- Basistextur, Gloss-/Specular-Anteil und `Normalize.dds`
- Material- und Lichtkonstanten ueber D3DX Effect Semantics
- `Simple` Fallback ohne Pixel Shader

`perpixelgloss2.fx` und `perpixelgloss3.fx` haben eine separate `glossMap`; die erste Variante arbeitet schmaler mit Basistextur/Normalisierung.

### UV Animation

Dateien:

- `uvanim.fx`
- `uvanimaddalpha.fx`
- `uvanimaddalpha2.fx`
- `uvanimaddalpha3.fx`
- `uvanimrevsubtract.fx`

Gemeinsame Merkmale:

- `baseTexture`, `animTexture`, optional `maskTexture`
- `time : Time`
- Parameter fuer UV-Bewegung, Gewichtung und/oder Alpha-Verhalten
- optional Skinning ueber `BoneMatrices`
- `UVAnim` Technique mit `vs_1_1` und `ps_1_1`
- `Simple` Technique mit zwei fixed-function Passes

Die Namen deuten auf unterschiedliche Blend-/Alpha-Modi: normale UV-Animation, AddAlpha-Varianten und Reverse-Subtract.

### DetailBump / Occlusion Interval Maps

`detailbump.fx` enthaelt:

- `baseTexture`
- `NormalizeTex`
- `Bump3DTex`
- `OimRiseTex`
- `OimFallTex`

Techniques:

- `DetailBump`: `vs_1_1`, Pixel Shader ueber ein vorkompiliertes/asm Fragment
- `OcclusionIntervalMaps`: `vs_1_1`, `ps_2_0`
- `Simple`: fixed-function/null Pixel Shader

Das ist der staerkste Material-Shader ausserhalb von `post.fx`.

### Invisible

`invisible.fx` beschreibt einen Pseudo-Refraction-Effekt fuer Unsichtbarkeit:

- `baseTexture`
- `sceneTexture`
- `NormalizeTex`
- Parameter `invisibleAlpha`
- Parameter `refractionScale`

Technique:

- `Invisible`
- `VertexShader = compile vs_1_1 VS();`
- `PixelShader = NULL;`

Obwohl `sceneTexture` und Refraction-Parameter vorhanden sind, nutzt die sichtbare Technique keinen Pixel Shader. Das kann bedeuten, dass der Effekt im gefundenen Asset deaktiviert/reduziert wurde oder ueber Renderstates/fixed-function Multipass umgesetzt wird.

### Scygnus / Twinkle

`scygnus.fx` ist ein Spezialeffekt:

- `baseTexture`
- `maskTexture`
- `NormalizeTex`
- prozedurale/lookup Texturen `SineTex`, `RandomTex`
- `RandomTwinkle` Technique mit `vs_1_1` und `ps_1_2`
- `TSS` und `Simple` Fallbacks mit fixed-function Pixel-Pfad

Der Name und die Parameter deuten auf funkeln/flackern, vermutlich fuer Waffen-, Skill- oder Objekt-Effekte.

## Postprocessing (`post.fx`)

`post.fx` ist separat wichtig, weil der Client es explizit laedt.

Binary-Pfad:

- Funktion: `FUN_005c0f90`
- `alefclient.pseudocode.c:375474`: prueft `effect/post.txt`
- `alefclient.pseudocode.c:375476`: falls nicht vorhanden, prueft `effect/post.fx`
- `alefclient.pseudocode.c:375485`: erstellt/kompiliert Effect aus `effect/post.fx`
- Wenn `effect/post.txt` vorhanden ist, wird es gelesen und mit dem Haupt-Key `1111` entschluesselt, bevor daraus ein Effect erstellt wird.

Das legt nahe:

- `post.fx` ist die plaintext/source Fallback-Datei.
- `post.txt` ist wahrscheinlich eine verschluesselte oder vorkompilierte/cached Effect-Variante.
- Entschluesselung von `post.txt` nutzt dieselbe CryptoAPI-RC4-Methode wie INIs/Reference-Dateien, also Key `1111`.

Aktueller Dateistand: Unter `C:\Spiele\Archlord` wurde kein `post.txt` gefunden; vorhanden und auswertbar ist `C:\Spiele\Archlord\effect\post.fx`.

Nach dem Effect-Load holt der Client Effect-Handles fuer unter anderem:

- `g_txScene`
- `g_txSquare`
- `g_squareRatio`
- `g_txPrev`
- `g_center`
- `g_radius`
- `g_txTransSource`

Wichtige `post.fx` Techniques:

- Belichtung: `ControlExposure`, `Average`, `LightAdapt`
- Kopieren/Downsample: `Copy`, `DownSample`
- Blur/Bloom: `BlurH`, `BlurV`, `BlurHLC`, `BlurVLC`, `BloomComp`, `BoxBlur1`, `BoxBloomComp`
- Farbfilter: `Grayscale`, `Sepia`, `Negative`, `X2`
- Screen-space Effekte: `EdgeDetect`, `ClampingCircle`, `Wave`, `Shockwave`, `Darken`, `Brighten`, `Ripple`, `Twist`
- Uebergaenge: `TransSaturate`, `TransMeshuggah`, `TransCrossFade`

Shaderprofile:

- fast alle Vertex Shader: `vs_1_1`
- einfache Pixelpfade: `ps_1_1`
- einzelne auskommentierte/alternative Pfade: `ps_1_4`
- Blur/Bloom/Composition teils `ps_2_0`

Render-Targets/Texturen in `post.fx`:

- `g_tx64x64`
- `g_tx16x16`
- `g_tx4x4`
- `g_txExposure`
- `g_txCurrentExposure`
- `g_txScene`
- `g_txPrev`
- `g_txSquare`
- `g_txSrcBlurH`
- `g_txSrcBlurV`
- `g_txSrcBloomComp`
- Effekt-LUTs/Texturen fuer Wasser/Screen-Verzerrung, Circle Clamp, Shockwave, Darken, Twist und Transitions

## Wasser-Shader-Anbindung

`decoded_hwaterstatus_ini.txt` enthaelt pro Wasser-ID zwei Shader-Auswahlfelder:

- `Shader14ID`
- `Shader11ID`

Fundstelle im Client:

- Funktion: `FUN_00646ad0`
- `alefclient.pseudocode.c:469456`: erkennt `Shader14ID`
- `alefclient.pseudocode.c:469471`: erkennt `Shader11ID`
- Speicherlayout im HWater-Statusblock:
  - `Shader14ID` wird nach `param_1 + 0x2450 + id * 0x98` geschrieben
  - `Shader11ID` wird nach `param_1 + 0x2454 + id * 0x98` geschrieben

Gefundene Werte in `decoded_hwaterstatus_ini.txt`:

- `Shader14ID`: nur `0` oder `1`
- `Shader11ID`: nur `0` oder `1`

Interpretation:

- Sehr wahrscheinlich waehlt `Shader14ID` einen Pixel-Shader-1.4-faehigen Wasserpfad.
- `Shader11ID` waehlt einen Pixel-Shader-1.1-kompatiblen Fallback.
- Die IDs sind keine Dateinamen; sie sind interne Auswahlwerte fuer bereits vorhandene Wasser-Shader-Varianten.

Das passt zu `post.fx`, wo Wasser-/Ripple-Verzerrungen sowohl auskommentierte `ps_1_4`/`ps_2_0` Pfade als auch aktive `ps_1_1`-Assembler-Fragmente haben.

## Runtime-generierte Vertex Shader

Neben den `.fx` Dateien baut `FUN_006550c0` mehrere Vertex-Shader-Assembler-Programme als Strings zusammen und kompiliert/assembliert sie ueber `FUN_00654bd0`.

Wichtige Fundstellen:

- `alefclient.pseudocode.c:478586`: `FUN_00654bd0`
- `alefclient.pseudocode.c:478591`: Funktion nimmt Shader-Quelltext und ruft intern den D3DX Assembler/Compiler-Pfad
- `alefclient.pseudocode.c:478653`: Runtime-Shader werden nur initialisiert, wenn `DAT_00c301fc != 0`
- `alefclient.pseudocode.c:479163`: `DAT_00c301fc = (0x100 < deviceCaps...)`, also Feature-/Caps-bedingt
- `alefclient.pseudocode.c:479221`: Cleanup gibt die erzeugten Shader wieder frei

Die generierten Shader beginnen mit:

```text
vs_1_1
dcl_position v0
dcl_normal v1
dcl_color0 v2
dcl_texcoord0 v3
...
def c14, 1.0, 0.0, 0.5, 0.0
```

Danach werden je nach Variante Instruktionsblaecke angehaengt:

- Transform: `m4x4 oPos, v0, c0`
- Fog: `dp4 r0.x, v0, c15` plus `mad oFog, -r0.x, c7.y, c7.x`
- diffuse Lichtberechnung: Dot-Produkt mit `c4`, Multiplikation mit `c5`, Addition von Ambient/Farbe `c6`
- specular/eye-vector-artiger Block ueber `c21`
- UV-Weiterleitung:
  - `oT0` bis `oT5`
  - Varianten mit vertauschten/ausgewaehlten `v3` bis `v8`
- Projektions-/Environment-Texture-Variante mit Matrix `c8` und Konstanten `c12/c13`

Globale Shader-Slots:

- `DAT_00c301d4`
- `DAT_00c301d8`
- `DAT_00c301dc`
- `DAT_00c301e0`
- `DAT_00c301e8`
- `DAT_00c301ec`
- `DAT_00c301f0`
- `DAT_00c301f4`
- `DAT_00c301f8`

Diese Runtime-Shader wirken wie feste Welt-/Terrain-/Material-Vertex-Shader fuer Multi-Texturing, Fog, Licht und Environment-/Projektions-Texturkoordinaten. Die genaue Zuordnung pro Slot ist noch nicht vollstaendig benannt, aber die Instruktionsstrings zeigen klar:

- Position/Normal/Farbe plus bis zu sechs Texcoord-Inputs
- Vertex-Fog
- Diffuse + Specular-Ausgabe ueber `oD0`/`oD1`
- unterschiedliche Texture-Coordinate-Routings fuer Multi-Pass- oder Multi-Texture-Materialien

## Wahrscheinliche Zuordnung nach Render-Funktion

| Bereich | Shaderpfad |
| --- | --- |
| Charaktere / animierte Meshes | `.fx` mit optionalem `SKINNING` und `BoneMatrices` |
| einfache Meshes | `simple.fx` oder `Simple` Techniques anderer FX-Dateien |
| Materialeffekte | `perpixelgloss*.fx`, `detailbump.fx`, `uvanim*.fx` |
| unsichtbare Charakter-/Skill-Effekte | `invisible.fx` |
| funkelnde Spezialeffekte | `scygnus.fx` |
| Wasser / HWater | Konfigurationsfelder `Shader14ID`/`Shader11ID` plus interne Shaderauswahl |
| Vollbild-/Posteffekte | `post.fx` oder verschluesseltes `effect/post.txt` |
| Terrain/Welt-Multitexturing | Runtime-generierte `vs_1_1` Assembler-Shader in `FUN_006550c0` |

## Offene Punkte

- Die genauen Direct3D-Wrapper-Namen sind noch nicht rueckbenannt. Sehr wahrscheinlich liegen `CreateVertexShader`, `SetVertexShader`, `SetPixelShader` usw. hinter `FUN_004c27xx`/`FUN_004c9xxx` Wrappern.
- Die Slot-Zuordnung `DAT_00c301d4` bis `DAT_00c301f8` sollte als naechstes ueber Xrefs auf konkrete Renderpfade gemappt werden.
- `effect/post.txt` sollte, falls es in einer anderen Client-Version auftaucht, mit Key `1111` dekodiert und gegen `post.fx` verglichen werden.
- Fuer Wasser fehlen noch die eigentlichen internen Pixel-Shader-Assembler-Fragmente ausserhalb von `post.fx`; Suche nach `ps_1_1`, `ps_1_4`, `Shader14ID`, `Shader11ID` in direkter Umgebung der Wasser-Renderfunktionen ist der naechste Schritt.
