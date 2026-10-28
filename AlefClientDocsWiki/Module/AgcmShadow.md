# AgcmShadow (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmShadow` (einfache Objektschatten: Hüllkugeln, Schattenkamera, Projektion auf das Gelände) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmShadow/AgcmShadow.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 16 von 19 Quellmethoden sind zugeordnet. `ShadowRasterResample`, `ShadowRasterBlur` und `Im2DRenderQuad` fehlen im Binary: in der Quelle ruft sie nur ein auskommentierter Block und der Beispielcode `Etc/ASample/src/alshadow*.cpp` (das Modul benutzt `InvertRaster` statt Weichzeichnen). Zusätzlich ist die freie Funktion `SetRwIm3DVertex` (`0x005BCA70`) zugeordnet.
- **Abweichungen:** keine festgestellt; die Quelle (EP8) und das 2017er Binary stimmen in `CB_Update`, `ShadowDraw` und `Render` im Ablauf überein.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmShadow.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005BDAB0` | 124 | vtable/String |
| 1 | `OnInit` | `0x005BC7A0` | 159 | vtable/String |
| 2 | `OnDestroy` | `0x005BC840` | 186 | vtable/String |
| 3 | `OnIdle` | `0x005BC900` | 42 | vtable/String |
| 4 | `Render` | `0x005BD6E0` | 811 | von Hand geprüft |
| 5 | `SetShadowEnable` | `0x005BC930` | 313 | Zeichenkette |
| 6 | `ShadowDraw` | `0x005BCD70` | 1249 | von Hand geprüft |
| 7 | `InvertRaster` | `0x005BD260` | 275 | von Hand geprüft |
| 8 | `UpdateBoundingSphere` | `0x005BD690` | 78 | von Hand geprüft |
| 9 | `AddShadow` | `0x005BE100` | 206 | von Hand geprüft |
| 10 | `DeleteShadow` | `0x005BE1D0` | 30 | von Hand geprüft |
| 11 | `CalcBoundingSphere` | `0x005BD380` | 178 | von Hand geprüft |
| 12 | `CB_POST_RENDER` | `0x005BDA10` | 24 | Callback-Registrierung |
| 13 | `CB_Update` | `0x005BDDA0` | 828 | von Hand geprüft |
| 14 | `CB_Release` | `0x005BDA30` | 95 | von Hand geprüft |
| 15 | `GetLevel` | `0x005BD440` | 81 | von Hand geprüft |
| 16 | `ShadowRasterResample` | – | | nicht im Binary: Aufrufe nur in auskommentiertem Code und im Beispiel `alshadow.cpp` |
| 17 | `ShadowRasterBlur` | – | | nicht im Binary: Aufrufe nur in auskommentiertem Code und im Beispiel `alshadow.cpp` |
| 18 | `Im2DRenderQuad` | – | | nicht im Binary: nur von `ShadowRasterResample`/`ShadowRasterBlur` gerufen |

16 von 19 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmShadow` (`0x005BDB50`), `~AgcmShadow_body` (`0x005BDD00`), `~AgcmShadow` (`0x005BE0E0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA0` | `Zeiger `AgcmCharacter` (für `GetSelfRideClump`, Feld `+0x1080`)` | `CB_Update`, `Render` |
| `this+0xBA4` | ``m_fShadowStrength` (0,9)` | `ShadowDraw` |
| `this+0xBA8` | `Zeiger auf die Kreisschatten-Textur` | `ShadowDraw` |
| `this+0xBAC` | `Anfang von `m_fLODOriginalShadowDistance` (3×4 Float)` | `GetLevel`, `OnInit` |
| `this+0xBDC` | ``m_fShadowDistFactor`` | `GetLevel` |
| `this+0xBF0 / 0xBF4 / 0xBF8 / 0xBFC` | `Welt-Kamera / gerichtetes Licht / Umgebungslicht / Schattenkamera (aus der Verwendung in `Render`, nicht einzeln gegen Namen geprüft)` | `Render`, `CB_Update` |
| `this+0xC04` | `Kopfknoten der Schattenliste (`std::list<ShadowInfo*>`)` | `CB_Update`, `CB_Release`, `Render` |
| `this+0xD0C` | ``m_bDrawShadow`` | `CB_POST_RENDER`, `CB_Update` |

## Vtable und Aufbau

Konstruktor `0x005BDB50` (trägt `AgcmShadow` ein, schaltet Idle ein, setzt Schattenstärke `0.9`, Anzahl gezeichneter Schatten `5`, Hintergrundfarbe weiß mit Alpha 0, `m_bDrawShadow` = FALSE), Destruktorrumpf `0x005BDD00` (leert die Schattenliste), Löschwrapper `0x005BE0E0`. Die Schattenliste (`std::list<ShadowInfo*>`) hat ihren Kopfknoten bei `this+0xC04`; die STL-Hilfen `size` (`0x005BDA90`) und `push_back` (`0x005BDB30`) sind eigene kleine Funktionen.
`OnAddModule` (`0x005BDAB0`) holt [`AgcmRender`](AgcmRender.md) und [`AgcmMap`](AgcmMap.md), meldet `CB_POST_RENDER` (`0x005BDA10`) bei `AgcmRender` an und übernimmt Welt, Kamera sowie gerichtetes und Umgebungslicht. `OnInit` (`0x005BC7A0`) setzt die Entfernungsstufen je Schattenstufe, `OnIdle` (`0x005BC900`) nur die Zeitzähler, `SetShadowEnable` (`0x005BC930`) legt bei Aktivierung zwei Parallelkameras, die Kreisschatten-Textur (`ShadowCircle.bmp`) und das 512×512-Zielraster an und baut sie bei Deaktivierung über `OnDestroy` (`0x005BC840`) ab.

## Schatten anmelden

`AddShadow` (`0x005BE100`, 206 Byte; als `ShadowInfo::ctor_or_dtor` vorbenannt) prüft das Objektflag `0x100000` (`ACUOBJECT_TYPE_OBJECTSHADOW`), legt ein `ShadowInfo` im Pool an (`ShadowInfo::operator new`, `0x005BD4A0`, Pool `ApMemory<ShadowInfo,2000>`), berechnet über `RpClumpForAllAtomics(CalcBoundingSphere)` die Hüllkugel, setzt bei Radius 0 die Ersatzwerte (Mittelpunkt y = 110, Radius 120; die Konstanten liegen als Gleitkommawerte bei `0x008BB4AC`/`0x008BB4A8`), multipliziert mit `SHADOW_SPHERE_EXPAND` (1,5) zum Zonenradius und hängt über `AgcmRender::AddUpdateInfotoClump` die Rückrufe `CB_Update` und `CB_Release` an; schlägt das fehl, wird das `ShadowInfo` gelöscht.
`DeleteShadow` (`0x005BE1D0`, 30 Byte) ruft `RemoveUpdateInfoFromClump2` mit denselben beiden Rückrufen. `CB_Release` (`0x005BDA30`) sucht das `ShadowInfo` in der Liste, entfernt den Knoten und löscht das Objekt über den virtuellen Löscher (Slot 0, `ShadowInfo::scalar_deleting_dtor` bei `0x005BD660`, dessen Rumpf der Pool-`operator delete` `0x005BD5D0` unter einer kritischen Sektion ist). Aufrufer in der Quelle: `AgcmCharacter.cpp` (Zeilen 3708 und 5238), `MainWindow.cpp` und `LuaFunc.cpp` des Clients. Im Binary rufen `AddShadow` die Funktionen `0x0040A2E0` und `0x005A7310`, `DeleteShadow` die Funktion `0x005A6700` (nach Aufrufgraph; die Zuordnung zu `AgcmCharacter`/`MainWindow` ist nicht einzeln geprüft).

## Pro Bild

`CB_Update` (`0x005BDDA0`, 828 Byte) ist der pro Objekt und Bild gerufene Rückruf: kein Schatten, wenn Zeichnen aus ist, das Licht fehlt, das Objekt unsichtbar ist (Flag `0x10000000`) oder die Schattenstufe 0 ist. `GetLevel` (`0x005BD440`) liefert die Stufe 0 bis 3 aus der Tabelle `m_fLODOriginalShadowDistance` (Tabellenanfang `this+0xBAC`, 3 Zeilen zu 4 Float, danach bei `this+0xBDC` der Entfernungsfaktor) gegen `calcDistance` (`Klumpen+0x38`). Ab Stufe 3 (`eLevelNon`) oder wenn schon mehr als `m_iShadowDrawMaxNum` Schatten in der Liste sind (außer bei Schattenstufe 1, dem eigenen Charakter), kehrt er zurück. Sonst berechnet er Kugelmittelpunkt, Kameraparameter, Kameramatrix aus dem Licht, Inversmatrix und die Kollisionsbox und hängt das `ShadowInfo` an die Liste.
`CB_POST_RENDER` (`0x005BDA10`) ruft `Render` (`0x005BD6E0`, 811 Byte), wenn `m_bDrawShadow` gesetzt ist. `Render` schaltet Nebel und beide Lichter ab, rendert je `ShadowInfo` die Atomics des Objekts in das 512×512-Raster (Effekte pro Atomic zeitweise aus), beim eigenen Charakter zusätzlich das Reittier, ruft `InvertRaster` (`0x005BD260`) und dann `ShadowDraw`, stellt Nebel und Lichter wieder her und leert die Liste.

## Schatten auf das Gelände

`ShadowDraw` (`0x005BCD70`, 1249 Byte) setzt die Zustände (Clamp, linear, Quellblend 0), wählt bei Stufe `eLevelCircle` die Kreistextur, sonst das Zielraster, bestimmt aus der Kollisionsbox das Sektorraster in Schritten von `MAP_STEPSIZE` (400), liest die Höhen mit `HP_GetHeightGeometryOnly` (`0x005F3A40`) in einen Rahmenspeicher und baut je Gitterzelle zwei Dreiecke über `SetRwIm3DVertex` (`0x005BCA70`, 757 Byte, keine Methode, sondern freie Funktion der Quelle). `SetRwIm3DVertex` transformiert die Dreieckspunkte mit `invMatrix`, verwirft Dreiecke ganz außerhalb des Schattenvolumens, setzt UV aus x/y und Alpha, bei `fade` abnehmend mit z. Anschließend `RwIm3DTransform` und `RwIm3DRenderPrimitive` (Dreiecksliste).
`InvertRaster` zeichnet ein Viereck über das ganze Raster mit Blend Quelle=Inverse-Zielfarbe, um das Schattenbild umzukehren.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind `AddShadow`, `DeleteShadow`, `CB_Update`, `CB_Release`, `GetLevel`, `Render`, `ShadowDraw`, `SetRwIm3DVertex`, `InvertRaster`, `CalcBoundingSphere` und `UpdateBoundingSphere`; `OnInit`, `OnDestroy`, `OnIdle`, `SetShadowEnable` und `OnAddModule` waren schon benannt und wurden nur über Aufbau und Aufrufe geprüft.
- Die drei Weichzeichner-Funktionen gelten als „nicht im Binary“, weil in der Quelle kein Aufrufer außerhalb von Kommentaren und Beispielcode steht und im Binary neben `InvertRaster` keine weitere Funktion mit einem Viereck aus vier Im2D-Vertices im AgcmShadow-Bereich liegt (die beiden anderen Aufrufe der Zeichenfunktion `0x34` mit 4 Vertices liegen in `0x006424A0` und `0x00652840`, fremden Modulen).
- Die Offsets sind aus der Verwendung gefolgert; die Reihenfolge der Zeiger bei `0xBF0`–`0xBFC` ist nicht einzeln belegt.
- `UpdateBoundingSphere` (`0x005BD690`) hat im Binary einen Aufrufer bei `0x006ED680`; dieser ist nicht weiter geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 1, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmMap`](AgcmMap.md), [`AgcmRender`](AgcmRender.md)
- **Erwähnt in:** [`AgcModule`](AgcModule.md), [`AgcmItem`](AgcmItem.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTuner`](AgcmTuner.md)
