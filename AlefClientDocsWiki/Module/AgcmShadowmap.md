# AgcmShadowmap (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmShadowmap` (Schattenkarte mit Vertex-/Pixel-Shader, Schatten-Kamera, Clump-Verwaltung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmShadowmap/AgcmShadowmap.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig – jede Quellmethode ist entweder einer Adresse zugeordnet oder als in der Quelle unreferenziert (und im Binary entfernt) begründet. Zugeordnet sind Aufbau, Ein-/Ausschalten, Schattenkamera, Clump-Verwaltung, beide Render-Durchläufe samt Pipeline-Umschaltung, alle vier Pipeline-Erzeuger und alle Zeichen-/Skin-Rückrufe. Im Binary nicht vorhanden sind `Im2DRenderQuad`, `previewShadowmap` und `createSubTexelPrecisionMap`; alle drei sind in der Quelle unreferenziert (die Vorschau ist auskommentiert, die Subtexel-Textur wird nie erzeugt) und wurden vom Linker entfernt. `releaseClumpCB` ist der gemeinsame leere Rumpf `0x0067AC90`.
- **Abweichungen:** keine festgestellt. Die beiden großen Funktionen `0x006F8200` und `0x006F92F0` (je über 4 KB) gehören nicht zu `AgcmShadowmap`, sondern zu [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md) (gemeinsamer Aufrufer `0x006FA6E0`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmShadowmap.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006F81B0` | 69 | vtable/String |
| 1 | `getShader` | `0x006F5750` | 227 | von Hand geprüft |
| 2 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `OnDestroy` | `0x006F64F0` | 25 | vtable/String |
| 4 | `On` | `0x006F6C00` | 2110 | von Hand geprüft |
| 5 | `Off` | `0x006F5840` | 509 | von Hand geprüft |
| 6 | `SetEnable` | `0x006F7470` | 34 | von Hand geprüft |
| 7 | `setShadowMapPipeline` | `0x006F7B90` | 115 | von Hand geprüft |
| 8 | `setShadowScenePipeline` | `0x006F7C10` | 115 | von Hand geprüft |
| 9 | `returnToOriginalPipeline` | `0x006F74A0` | 127 | von Hand geprüft |
| 10 | `renderShadowmap` | `0x006F7C90` | 794 | von Hand geprüft |
| 11 | `render` | `0x006F7FB0` | 331 | von Hand geprüft |
| 12 | `registerClump` | `0x006F7B30` | 48 | von Hand geprüft |
| 13 | `unregisterClump` | `0x006F7B60` | 43 | von Hand geprüft |
| 14 | `updateShadowCam` | `0x006F5A40` | 741 | von Hand geprüft |
| 15 | `preRenderCB` | `0x006F5D30` | 42 | Callback-Registrierung |
| 16 | `postRenderCB` | `0x006F8100` | 168 | Callback-Registrierung |
| 17 | `updateClumpCB` | `0x006F79E0` | 224 | von Hand geprüft |
| 18 | `releaseClumpCB` | `0x0067AC90` | 6 | gleiche Adresse wie `leerer Rumpf (gemeinsamer Rumpf `Element::GetSize`, wird von `registerClump` und `unregisterClump` als Freigabe-Rückruf übergeben)` (vom Linker zusammengefaltet) |
| 19 | `createAtomicPipeline` | `0x006F6A00` | 112 | von Hand geprüft |
| 20 | `powerpipeRenderCB` | `0x006F6510` | 773 | von Hand geprüft |
| 21 | `createAtomicSkinPipeline` | `0x006F6A70` | 145 | von Hand geprüft |
| 22 | `powerpipeSkinLightingCB` | `0x006F6820` | 127 | von Hand geprüft |
| 23 | `powerpipeSkinGetMaterialShaderCB` | `0x006F5D60` | 53 | von Hand geprüft |
| 24 | `powerpipeSkinMeshRenderCB` | `0x006F5DA0` | 570 | von Hand geprüft |
| 25 | `createAtomicPipelineForShadowmap` | `0x006F68A0` | 112 | von Hand geprüft |
| 26 | `powerpipeRenderForShadowmapCB` | `0x006F5FE0` | 467 | von Hand geprüft |
| 27 | `createAtomicSkinPipelineForShadowmap` | `0x006F6910` | 143 | von Hand geprüft |
| 28 | `powerpipeSkinLightingForShadowmapCB` | `0x006F61C0` | 42 | von Hand geprüft |
| 29 | `powerpipeSkinGetMaterialShaderForShadowmapCB` | `0x006F61F0` | 53 | von Hand geprüft |
| 30 | `powerpipeSkinMeshRenderForShadowmapCB` | `0x006F6230` | 283 | von Hand geprüft |
| 31 | `catMatrices` | `0x006F6350` | 291 | von Hand geprüft |
| 32 | `Im2DRenderQuad` | – | | wird in der Quelle nur von `previewShadowmap` gerufen; im Binary nicht vorhanden (vom Linker entfernt) |
| 33 | `previewShadowmap` | – | | in der Quelle nur in einer auskommentierten Zeile von `postRenderCB` aufgerufen (`//	pThis->previewShadowmap();`), damit unreferenziert; im Binary nicht vorhanden |
| 34 | `create11BitEncodingMap` | `0x006F6480` | 105 | von Hand geprüft |
| 35 | `createSubTexelPrecisionMap` | – | | in der Quelle nirgends aufgerufen (nur die Definition und das Mitglied `m_pSubTexelPrecisionTexture`); im Binary nicht vorhanden. `On` erzeugt nur die beiden 512×512-Raster, keine 8-Bit-Textur |

33 von 36 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmShadowmap` (`0x006F7730`), `AgcmShadowmap` (`0x006F7840`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xC70` | `Schatten an (`m_bOn`)` | `Off`, `updateClumpCB` |
| `this+0xC74` | `Spieler-Clump` | `updateShadowCam`, `updateClumpCB` |
| `this+0xC78 / 0xC7C` | `Anfang / Ende der gesammelten Clumps (`std::vector`)` | `render`, `postRenderCB` |
| `this+0xC84` | `Shader unterstützt (`m_bShaderSupported`)` | `updateClumpCB` |
| `this+0xCC8…0xCE0` | `Stapel der ursprünglichen Pipelines (`std::deque`)` | `setShadowMapPipeline`, `returnToOriginalPipeline` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmShadowmap` (`0x006F79C0`, Löschwrapper), 1 `OnAddModule` (`0x006F81B0`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`), 3 bis 5 `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x006F64F0`, ruft `Off`), 8 `0x004E3420`. Der Konstruktor (`0x006F7840`, trägt `AgcmShadowmap`) und der Destruktorrumpf (`0x006F7730`, ruft `Off`) sind zugeordnet. `OnAddModule` holt [`AgcmRender`](AgcmRender.md).

## Ein- und Ausschalten

`SetEnable` (`0x006F7470`, 34 Byte) ruft bei 0 `Off` (`0x006F5840`, 509 Byte: gibt Shader, Texturen und Kamera frei, wenn `this+0xC70` gesetzt ist), sonst `On` (`0x006F6C00`, 2110 Byte; hier stehen die Vertex-Shader-Quelltexte als Zeichenketten, z. B. `vs.1.1 … dcl_position v0`). `getShader` (`0x006F5750`) übersetzt Shader-Quelltext mit demselben Muster wie [`AgcmWater`](AgcmWater.md):GetShader` (Compiler-Aufruf `0x004498F5`, danach Vertex- oder Pixel-Shader je nach Flag). `create11BitEncodingMap` (`0x006F6480`) erzeugt die 2048-Texel-Codiertextur (11-Bit-Codierung).

## Kamera und Rendern

`preRenderCB` (`0x006F5D30`, schon benannt) ruft `updateShadowCam` (`0x006F5A40`, 741 Byte: berechnet aus dem Spieler-Clump `this+0xC74` die Schattenkamera, Fenster und Clip-Ebenen). `catMatrices` (`0x006F6350`) verkettet Matrizen und wird von zwei Funktionen gerufen (`0x006F6510`, `0x006F6820`). `postRenderCB` (`0x006F8100`) ruft nacheinander `renderShadowmap` (`0x006F7C90`, 794 Byte) und `render` (`0x006F7FB0`, 331 Byte). Beide laufen über die gesammelten Clumps (`this+0xC78…0xC7C`) und setzen je Atomic die Pipeline um: `renderShadowmap` mit `setShadowMapPipeline` (`0x006F7B90`), `render` mit `setShadowScenePipeline` (`0x006F7C10`); danach stellt `returnToOriginalPipeline` (`0x006F74A0`) die alte Pipeline aus einem Stapel (`std::deque` bei `this+0xCC8…0xCE0`) wieder her. Die beiden Setzfunktionen unterscheiden sich im Binary nur durch die Adresse und ihre Verwendung.
`updateClumpCB` (`0x006F79E0`) trägt einen Clump ein, wenn Schatten an sind, ein Spieler-Clump existiert, der Clump nicht unsichtbar ist (`0x10000000`) und seine Bounding-Sphere im Frustum der Schattenkamera liegt (`std::vector::push_back` ist `0x006F7800`). `registerClump` (`0x006F7B30`) meldet ihn mit `updateClumpCB` bei `AgcmRender` an, `unregisterClump` (`0x006F7B60`) meldet ihn ab.

## Pipelines und Zeichen-Rückrufe

Die vier Erzeuger legen je eine RenderWare-Pipeline an und setzen die Rückrufe: `createAtomicPipeline` (`0x006F6A00`, Szene, ohne Skelett) und `createAtomicSkinPipeline` (`0x006F6A70`, Szene, mit Skelett) verwenden `powerpipeRenderCB` (`0x006F6510`, 773 Byte) bzw. die Skin-Rückrufe `powerpipeSkinLightingCB` (`0x006F6820`, ruft `catMatrices`), `powerpipeSkinGetMaterialShaderCB` (`0x006F5D60`, liefert den Szenen-Vertex-Shader `m_pShadowSceneVShader[numWeights]`, Feld `this+0xCA0`) und `powerpipeSkinMeshRenderCB` (`0x006F5DA0`, 570 Byte). `createAtomicPipelineForShadowmap` (`0x006F68A0`) und `createAtomicSkinPipelineForShadowmap` (`0x006F6910`) verwenden `powerpipeRenderForShadowmapCB` (`0x006F5FE0`, 467 Byte) bzw. `powerpipeSkinLightingForShadowmapCB` (`0x006F61C0`), `powerpipeSkinGetMaterialShaderForShadowmapCB` (`0x006F61F0`, Shader `m_pShadowMapVShader[numWeights]`, Feld `this+0xC88`) und `powerpipeSkinMeshRenderForShadowmapCB` (`0x006F6230`, 283 Byte).
Unterscheidung Szene/Schattenkarte: `powerpipeRenderCB` setzt die Szenen-Shader-Konstanten (Welt-View-Projektion, Schatten-Textur- und -MVP-Matrix über `catMatrices`, Tiefen-Bias, Lichtrichtung) und bindet die Schattenkarte; `powerpipeRenderForShadowmapCB` setzt nur Welt-View-Projektion und eine Tiefenkonstante und bindet die 11-Bit-Codiertextur. Dieselbe Trennung gilt für die Skin-Rückrufe (`…Lighting…` ruft `catMatrices` nur in der Szenen-Fassung).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die zwölf Pipeline-Funktionen (`0x006F5D60…0x006F6A70`) sind über die Aufrufbeziehungen zugeordnet: jeder Erzeuger trägt die Adressen seiner Rückrufe, und die Rückrufe unterscheiden sich durch ihren Inhalt (Szene: `catMatrices`, `m_pShadowSceneVShader`; Schattenkarte: `m_pShadowMapVShader`). Zeile für Zeile verglichen sind sie nicht; die Rümpfe von `powerpipeSkinMeshRenderCB` und `…ForShadowmapCB` sind nur überflogen.
- Gegen die Quelle gelesen sind `SetEnable`, `updateClumpCB`, `registerClump` und `preRenderCB` (Aufrufbeziehung); `getShader` ist über das gleiche Muster wie `AgcmWater::GetShader` zugeordnet.
- `updateShadowCam` ist über den Aufrufer `preRenderCB` zugeordnet, nicht Zeile für Zeile verglichen. `On` (`0x006F6C00`) und `Off` (`0x006F5840`) sind über `SetEnable`, die Größe und die Shader-Zeichenketten zugeordnet.
- `renderShadowmap` und `render` sind über die Aufrufreihenfolge in `postRenderCB` und die Größenverhältnisse (98 bzw. 47 Quellzeilen) getrennt; `setShadowMapPipeline`/`setShadowScenePipeline` (`0x006F7B90`/`0x006F7C10`) sind nur über ihre Verwendung in `renderShadowmap` bzw. `render` unterschieden – im Binary sind beide Rümpfe fast gleich.
- `catMatrices` ist über die Matrizenverkettung und den Aufruf von `0x0044554F` zugeordnet; `create11BitEncodingMap` über die Größe 0x800 und die Füllschleife.
- Die Offsets stammen aus den genannten Funktionen; Feldnamen der Quelle sind aus der Verwendung gefolgert.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, nicht im Client: 2, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmRender`](AgcmRender.md), [`AgcmWater`](AgcmWater.md)
- **Erwähnt in:** [`AgcmCamera2`](AgcmCamera2.md)
