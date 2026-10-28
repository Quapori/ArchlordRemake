# AgcmDynamicLightmap (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmDynamicLightmap` (dynamische Lichtkarte für Punktlichter) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, `OnInit`, `OnIdle`, `OnDestroy`, `postRenderCB`, `render`, `addLight`, `removeLight`, `clearLights` und `CreateLightmap` zugeordnet; `turnOnLight`, `turnOffLight`, `customUpdateCB`, `customRenderCB`, `Im2DRenderQuad` und `previewLightmap` nicht einzeln gefunden.
- **OnAddModule** (`0x006FAA30`): holt [`AgcmRender`](AgcmRender.md) (Rückruf `postRenderCB` `0x006FAA10`), [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`ApmOcTree`](ApmOcTree.md) in dieser Reihenfolge wie die Quelle. `postRenderCB` ruft `render` (`0x006FA7B0`, 605 Byte) nur bei eingeschaltetem Modul.
- **OnInit** (`0x006FA610`) ruft `CreateLightmap(0x200)` (`0x006FA470`); `addLight` (`0x006FAD90`, 675 Byte, ruft `AgcmOcTree::AddCustomRenderDataToOcTree`) und `removeLight` (`0x006FAC80`, sucht das Licht in der Liste und entfernt es) lassen nur Licht-Typen 0x80–0x82 (Punkt, Spot, Soft-Spot) zu; `clearLights` (`0x006FB040`) wird von `OnDestroy` (`0x006FB140`) gerufen.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmDynamicLightmap.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006FAA30` | 117 | vtable/String |
| 1 | `OnInit` | `0x006FA610` | 42 | vtable/String |
| 2 | `OnDestroy` | `0x006FB140` | 129 | vtable/String |
| 3 | `OnIdle` | `0x006FA640` | 150 | vtable/String |
| 4 | `addLight` | `0x006FAD90` | 675 | von Hand geprüft |
| 5 | `removeLight` | `0x006FAC80` | 263 | von Hand geprüft |
| 6 | `clearLights` | `0x006FB040` | 256 | von Hand geprüft |
| 7 | `turnOnLight` | – | | nicht einzeln gefunden |
| 8 | `turnOffLight` | – | | nicht einzeln gefunden |
| 9 | `render` | `0x006FA7B0` | 605 | von Hand geprüft |
| 10 | `postRenderCB` | `0x006FAA10` | 24 | Callback-Registrierung |
| 11 | `customUpdateCB` | – | | Rumpf ohne Wirkung, nicht einzeln gefunden |
| 12 | `customRenderCB` | – | | nicht einzeln gefunden |
| 13 | `CreateLightmap` | `0x006FA470` | 414 | von Hand geprüft |
| 14 | `Im2DRenderQuad` | – | | nicht einzeln gefunden |
| 15 | `previewLightmap` | – | | Werkzeugfunktion, nicht gefunden |

10 von 16 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006fab90` (`0x006FAB90`), `ctor_or_dtor_006fb1d0` (`0x006FB1D0`), `~AgcmDynamicLightmap` (`0x006FB250`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `render`, `addLight`, `clearLights` und `CreateLightmap` sind über Aufrufbeziehungen (`postRenderCB`, `OnInit`, `OnDestroy`), die Lichttypprüfung und die Größe zugeordnet, nicht Zeile für Zeile verglichen.
- `addLight` (`0x006FAD90`) und `removeLight` (`0x006FAC80`) waren zunächst vertauscht; die Typprüfung steht in beiden, den Ausschlag gab, dass `0x006FAD90` `AddCustomRenderDataToOcTree` ruft und `0x006FAC80` einen Eintrag in der Liste sucht und freigibt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 3, ohne Kandidat: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmRender`](AgcmRender.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmEff2`](AgcmEff2.md), [`AgcmEventPointLight`](AgcmEventPointLight.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmShadowmap`](AgcmShadowmap.md)
