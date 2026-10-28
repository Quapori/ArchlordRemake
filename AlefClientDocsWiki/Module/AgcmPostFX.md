# AgcmPostFX (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmPostFX` (Nachbearbeitung: Blenden, Belichtung, Übergänge über D3DX-Effekte) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmPostFX/AgcmPostFX.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Ein-/Ausschalten, Render-Ziele, Belichtung, Technik-Liste und die Bildaufbereitung. Nicht zugeordnet sind `CreateFX`, `SetRadius`/`SetCenter`, `OnResetDevice`, `changeRenderTarget`, `saveImmediateFrame`, `GetCount` und die zweite `GetInstance`-Fassung (eingebaut oder ohne Anker).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmPostFX.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005C04B0` | 64 | vtable/String |
| 1 | `PostFX_ON` | `0x005BFBA0` | 94 | as-register |
| 2 | `PostFX_OFF` | `0x005BF4E0` | 105 | as-register |
| 3 | `OnInit` | `0x005C0BE0` | 3225 | vtable/String |
| 4 | `OnIdle` | `0x005BFC00` | 168 | vtable/String |
| 5 | `OnDestroy` | `0x005C0900` | 441 | vtable/String |
| 6 | `OnLostDevice` | `0x005BF550` | 58 | von Hand geprüft |
| 7 | `OnResetDevice` | – | | nicht einzeln gefunden (vermutlich in den Rückruf `0x005C0470` eingebaut) |
| 8 | `GetInstance` | `0x005BF590` | 106 | von Hand geprüft |
| 9 | `GetInstance` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `CreateFX` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `DeleteFX` | `0x005C06F0` | 33 | von Hand geprüft |
| 12 | `DeleteFX` | `0x005C04F0` | 98 | von Hand geprüft |
| 13 | `AllDeleteFX` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `RenderPostFX` | `0x005BFCB0` | 1666 | von Hand geprüft |
| 15 | `changeRenderTarget` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `OnCameraStateChange` | `0x005C0340` | 70 | vtable/String |
| 17 | `_AverageScene` | `0x005BF010` | 280 | von Hand geprüft |
| 18 | `_ControlExposure` | `0x005BF130` | 328 | von Hand geprüft |
| 19 | `SetRadius` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `SetRadius` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `SetCenter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `SetCenter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `AutoExposureControlOff` | `0x005BF2A0` | 113 | von Hand geprüft |
| 24 | `createRenderTargets` | `0x005BF630` | 1164 | Zeichenkette |
| 25 | `destroyRenderTargets` | `0x005BF380` | 253 | von Hand geprüft |
| 26 | `saveImmediateFrame` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `_AutoNameGenerate` | `0x005C05D0` | 284 | Zeichenkette |
| 28 | `GetCount` | – | | eine Zeile, eingebaut |

18 von 29 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `saveNextFrame` (`0x005BEC80`), `ctor_or_dtor_005c0720` (`0x005C0720`), `ctor_or_dtor_005c0ac0` (`0x005C0AC0`), `~AgcmPostFX` (`0x005C0BC0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBFC` | `Merker „automatische Belichtung an“ (`m_bAutoExposureControl`)` | `AutoExposureControlOff` |

## OnAddModule (0x005C04B0)

Setzt die Raster-Erweiterung des D3D9-Geräts (`RwRasterGetPluginOffset`), merkt sich die alten Release-/Restore-Rückrufe und setzt eigene Rückrufe (`0x005BFB50`, `0x005C0470`) – wie `newD3D9ReleaseDeviceCB`/`…RestoreDeviceCB` in der Quelle. Die Rückrufe sind als Funktionen nicht Teil der Methodenliste.

## OnInit (0x005C0BE0)

3225 Byte. Holt [`AgcmRender`](AgcmRender.md), meldet über AngelScript die Methoden `PostFX_ON()`, `PostFX_OFF(bool)`, `saveNextFrame()` und die Variable `int m_bOn` an (Typname `postFX`) und lädt dann die Effektdatei: Makros `ARCHLORD`, Existenzprüfung von `effect/post.txt`, Einlesen von `effect/post.txt`/`effect/post.fx` und Auflösen der Parameternamen (`g_txScene`, `g_txSquare`, `g_squareRatio`, `g_txPrev`, `g_center`, `g_radius`, `g_txTransSource`, `g_windowSize`, `g_fElapsedTime`, `g_txCurrentExposure`). Bei Fehlern erscheint „FX compile error … so post fx will be disabled.“ (Zeichenkette im Binary).

## Render-Ziele und Belichtung

`createRenderTargets` (`0x005BF630`, 1164 Byte) legt die Ziele `g_tx64x64`, `g_tx16x16`, `g_tx4x4` und `g_txExposure…` an; `destroyRenderTargets` (`0x005BF380`) gibt sie frei. `OnLostDevice` (`0x005BF550`) ruft `destroyRenderTargets`, `OnCameraStateChange` (`0x005C0340`) ruft `OnLostDevice` und `createRenderTargets`. `RenderPostFX` (`0x005BFCB0`, 1666 Byte) ist die größte Funktion und ruft `_ControlExposure` (`0x005BF130`); `_AverageScene` (`0x005BF010`) ist die Vorgängerfunktion gleicher Bauart (vier Durchgänge). `AutoExposureControlOff` (`0x005BF2A0`) sperrt das Raster der Belichtungskette, schreibt viermal den Wert `0x66` (= 0,4 × 255), gibt es wieder frei und setzt den Merker `this+0xBFC` zurück.

## Technik-Liste

`GetInstance(Name)` (`0x005BF590`) durchsucht die Liste; `DeleteFX(Name)` (`0x005C06F0`, 23 Aufrufer) ruft `GetInstance` und `DeleteFX(Technique*&)` (`0x005C04F0`). `_AutoNameGenerate` (`0x005C05D0`) erzeugt Namen im Format `PostFX_%d`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `_AverageScene` und `_ControlExposure` haben eine ähnliche Form (je ein Effekt-Durchgang mit Vertexpuffer); die Reihenfolge `0x005BF010` → `0x005BF130` folgt der Quellreihenfolge, nur `_ControlExposure` wird von `RenderPostFX` gerufen.
- `DeleteFX` (zwei Fassungen) und `GetInstance` sind über Aufrufbeziehungen und Größen zugeordnet, nicht Zeile für Zeile verglichen.
- Der Feldname zum Offset `0xBFC` folgt aus der Quelle (`m_autoExposure.m_bAutoExposureControl`), wurde aber nicht über die Strukturlage nachgeprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, nicht im Client: 2, ohne Kandidat: 5.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmRender`](AgcmRender.md)
- **Erwähnt in:** [`AgcmEff2`](AgcmEff2.md), [`AgcmRender`](AgcmRender.md)
