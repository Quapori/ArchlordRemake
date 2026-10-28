# AgcmShadow2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmShadow2` (Schatten von Objekten über eine Schattentextur: Kamera, Raster, Bit-Puffer) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmShadow2/AgcmShadow2.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Aufbau, Einstellungen, Schattenkamera, die Texturerzeugung samt Hilfsfunktionen und der Bit-Puffer. Nicht im Binary vorhanden sind `BrightenShadow` und `CBBlitter` (nirgends angemeldet); `GetSectorData` ist eingebaut, `CB_POST_RENDER` ist ein leerer Rumpf und `SetCallbackTextureUpdate` ein zusammengefalteter Einzeiler.
- **Abweichungen:** keine festgestellt. `ShadowTextureRender` steht in der Quelle zwischen `ClumpCBSetShadowList` und `AddToShadow2List`/`ApplyMatrix`, im Binary als größte Funktion hinter ihren Hilfsfunktionen.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmShadow2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00652980` | 318 | vtable/String |
| 1 | `OnInit` | `0x006530B0` | 1096 | vtable/String |
| 2 | `ChangeDarkenValue` | `0x00652030` | 46 | as-register |
| 3 | `ChangeLightAngle` | `0x00652060` | 266 | as-register |
| 4 | `OnDestroy` | `0x00652170` | 157 | vtable/String |
| 5 | `SetEnable` | `0x00652210` | 307 | von Hand geprüft |
| 6 | `OnIdle` | `0x00652350` | 93 | vtable/String |
| 7 | `OnCameraStateChange` | `0x006523B0` | 36 | vtable/String |
| 8 | `GetSectorData` | – | | in die Aufrufer eingebaut |
| 9 | `ClumpCBSetShadowList` | `0x006523E0` | 63 | von Hand geprüft |
| 10 | `AddToShadow2List` | `0x00652420` | 79 | von Hand geprüft |
| 11 | `CB_SECTOR_CAHNGE` | `0x00652470` | 71 | Callback-Registrierung |
| 12 | `CB_POST_RENDER` | – | | leerer Rumpf, mit einem gemeinsamen Rumpf zusammengefaltet |
| 13 | `ApplyMatrix` | `0x006524C0` | 145 | von Hand geprüft |
| 14 | `UpdateShadowBuffer` | `0x00652560` | 511 | von Hand geprüft |
| 15 | `GetShadowBuffer` | `0x00652770` | 202 | von Hand geprüft |
| 16 | `SetCallbackTextureUpdate` | – | | Einzeiler, mit anderen `SetCallback…` zusammengefaltet |
| 17 | `BrightenShadow` | – | | im Binary nicht vorhanden (nirgends aufgerufen) |
| 18 | `DarkerRaster` | `0x00652AC0` | 171 | von Hand geprüft |
| 19 | `InvertRaster` | `0x00652B70` | 85 | von Hand geprüft |
| 20 | `CBBlitter` | – | | im Binary nicht vorhanden (nirgends angemeldet) |
| 21 | `RenderRaster` | `0x00652840` | 269 | von Hand geprüft |

17 von 22 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmShadow2` (`0x00651ED0`), `~AgcmShadow2` (`0x00652950`), `ShadowTextureRender` (`0x00652BD0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x8C40…0x8C47` | `acht Bit-Masken `0x01…0x80` (`m_cMaskShadowBuffer`)` | `OnInit`, `GetShadowBuffer` |
| `this+0x8C48` | `Abdunklungswert 0…255 (`m_nShadowDarkenValue`)` | `ChangeDarkenValue`, `DarkerRaster` |
| `this+0x8C4C` | ``m_bEnableShadow`` | `SetEnable`, `GetShadowBuffer` |
| `this+0xC40` | `Bit-Puffer des Schattens (`0x8000` Byte)` | `UpdateShadowBuffer`, `GetShadowBuffer` |

## Aufbau und Einstellungen

Der Konstruktor (`0x00651ED0`) trägt den Modulnamen `AgcmShadow2` ein. `OnAddModule` (`0x00652980`) holt [`AgcmRender`](AgcmRender.md), [`AgcmShadow`](AgcmShadow.md), [`ApmMap`](ApmMap.md), [`AgcmMap`](AgcmMap.md), [`ApmOcTree`](ApmOcTree.md) und [`AgcmOcTree`](AgcmOcTree.md), meldet `CB_SECTOR_CAHNGE` (`0x00652470`) für Sektorwechsel und Kartenende an. `OnInit` (`0x006530B0`) wird bei fehlendem Vertex-Shader (`AgcmRender+0xCB0`) übersprungen, legt den Licht-Frame an, ruft `ChangeLightAngle(14.0)` und füllt die acht Bit-Masken `0x01…0x80` (`this+0x8C40…`); danach folgt die AngelScript-Anmeldung von `ChangeDarkenValue` und `ChangeLightAngle`. `ChangeDarkenValue` (`0x00652030`) begrenzt den Wert auf 0…255 (Feld `this+0x8C48`). `ChangeLightAngle` (`0x00652060`) rechnet aus dem Wert (0…24) einen Winkel und dreht den Licht-Frame.

## Schattenkamera

`SetEnable` (`0x00652210`, 307 Byte): erzeugt bei Einschalten Kamera, Frame, Zwischenraster und Schattentextur (`this+0xBDC`, `0xBB0`, `0xBB4`, Größe aus `this+0xC3C`), setzt den Aktualisierungszähler auf 1 und `m_bEnableShadow` (`this+0x8C4C`); beim Ausschalten ruft es `OnDestroy` (Vtable-Slot 7, Offset `+0x1C`). Es kehrt sofort zurück, wenn der Vertex-Shader nicht verfügbar ist. `OnIdle` (`0x00652350`) zählt den Aktualisierungszähler bis 3 hoch und setzt ihn nach 120 000 ms zurück; `OnCameraStateChange` (`0x006523B0`) setzt ihn bei Größenänderung/Aktivierung auf 1.

## Schattentextur erzeugen

`ShadowTextureRender` (`0x00652BD0`, 1235 Byte) ist die größte Funktion: sie sammelt über Octree (`ClumpCBSetShadowList`, `0x006523E0`) oder Sektorlisten (`AddToShadow2List`, `0x00652420`) die schattenwerfenden Clumps, positioniert die Schattenkamera über dem Sektor, zeichnet die Clumps, ruft `InvertRaster` (`0x00652B70`) und `DarkerRaster` (`0x00652AC0`), danach `ApplyMatrix` (`0x006524C0`) und `UpdateShadowBuffer` (`0x00652560`) und löst den Rückruf „Textur aktualisiert“ aus. `RenderRaster` (`0x00652840`) zeichnet das bildschirmfüllende Viereck mit der Rastertextur und dem Grauwert. `UpdateShadowBuffer` rechnet das Schattenbild in einen Bit-Puffer (`this+0xC40`, `0x8000` Byte; Schwellwert `0x1F` je Farbkanal), `GetShadowBuffer` (`0x00652770`) prüft darin ein Bit zu einer Weltposition (Rückgabe 0 außerhalb der Textur).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind `SetEnable`, `OnIdle`, `AddToShadow2List`, `ClumpCBSetShadowList`, `ChangeDarkenValue`; `ShadowTextureRender`, `ApplyMatrix`, `UpdateShadowBuffer`, `GetShadowBuffer`, `RenderRaster`, `DarkerRaster` und `InvertRaster` sind über Aufrufbeziehungen (`ShadowTextureRender` ruft alle), Größe und Renderstate-Folge zugeordnet, nicht Zeile für Zeile verglichen.
- `InvertRaster` und `DarkerRaster` sind durch ihre Aufrufreihenfolge in `ShadowTextureRender` (erst Invertieren, dann Abdunkeln) und den Kamera-Umgang (nur `DarkerRaster` setzt das Raster der Kamera) getrennt.
- Die Feldnamen der Offsets stammen aus der Quelle und der Verwendung, nicht aus einer Layout-Rechnung.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht als eigene Funktion: 1, nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmRender`](AgcmRender.md), [`AgcmShadow`](AgcmShadow.md), [`ApmMap`](ApmMap.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmGrass`](AgcmGrass.md), [`AgcmItem`](AgcmItem.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md)
