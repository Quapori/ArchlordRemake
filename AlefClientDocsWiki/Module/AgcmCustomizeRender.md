# AgcmCustomizeRender (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmCustomizeRender` (Vorschau beim Aussehen-Ändern: Kamera, Render-Ziel, Gesicht/Haare) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmCustomizeRender/AgcmCustomizeRender.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Geräteverlust, Kamera/Render-Ziel, `Init`, `Render`, Gesicht/Haare und die zwölf Kameraschalter. Nicht zugeordnet sind `Start`/`End`/`SetWorld`/`DrawQuad`, `RenderAtomicCB`, `RemoveCustomizeAtomicCB`, die `SetCameraPosY/Z`-, `SetTargetPosY`-, `SetZoom`- und `SetPreview…`-Setter, `GetHairNum`/`GetFaceNum` und die acht `AtUp/AtDown`-Schalter.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmCustomizeRender.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | `0x006619C0` | 252 | von Hand geprüft |
| 1 | `RenderAtomicCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `RemoveCustomizeAtomicCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 3 | `SetCameraPos` | `0x00660530` | 710 | von Hand geprüft |
| 4 | `CreateCamera` | `0x00660800` | 263 | von Hand geprüft |
| 5 | `CreateRenderTarget` | `0x00660910` | 285 | von Hand geprüft |
| 6 | `DestoryRenderTarget` | `0x00660C90` | 121 | von Hand geprüft |
| 7 | `ClumpClone` | `0x00660A30` | 465 | von Hand geprüft |
| 8 | `SetState` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `GetState` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `SetWidth` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `SetHeight` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 13 | `OnDestroy` | `0x00660C10` | 114 | vtable/String |
| 14 | `OnAddModule` | `0x00661680` | 104 | vtable/String |
| 15 | `OnLostDevice` | `0x00661570` | 35 | gleiche Adresse wie `in den statischen Geräte-Rückruf eingebaut` (vom Linker zusammengefaltet) |
| 16 | `OnResetDevice` | `0x006615A0` | 46 | gleiche Adresse wie `in den statischen Geräte-Rückruf eingebaut` (vom Linker zusammengefaltet) |
| 17 | `Start` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `SetWorld` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `End` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `DrawQuad` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `Render` | `0x00660DF0` | 1368 | von Hand geprüft |
| 22 | `SetCameraPosY` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `SetCameraPosZ` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `SetTargetPosY` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 25 | `SetPreviewFar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `SetPreviewNear` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `SetZoom` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `SetFace` | `0x006618B0` | 178 | Zeichenkette |
| 29 | `SetHair` | `0x00661970` | 73 | von Hand geprüft |
| 30 | `AttachFace` | `0x00661720` | 194 | von Hand geprüft |
| 31 | `DetachFace` | `0x00661360` | 117 | von Hand geprüft |
| 32 | `AttachHair` | `0x006617F0` | 179 | von Hand geprüft |
| 33 | `DetachHair` | `0x006613E0` | 122 | von Hand geprüft |
| 34 | `LeftTurnOn` | `0x00661460` | 11 | von Hand geprüft |
| 35 | `RightTurnOn` | `0x00661470` | 11 | von Hand geprüft |
| 36 | `LeftTurnOff` | `0x00661480` | 20 | von Hand geprüft |
| 37 | `RightTurnOff` | `0x006614A0` | 20 | von Hand geprüft |
| 38 | `IsLeftTurnOn` | `0x006614C0` | 13 | von Hand geprüft |
| 39 | `IsRightTurnOn` | `0x006614D0` | 13 | von Hand geprüft |
| 40 | `ZoomInOn` | `0x006614E0` | 11 | von Hand geprüft |
| 41 | `ZoomOutOn` | `0x006614F0` | 11 | von Hand geprüft |
| 42 | `ZoomInOff` | `0x00661500` | 20 | von Hand geprüft |
| 43 | `ZoomOutOff` | `0x00661520` | 20 | von Hand geprüft |
| 44 | `IsZoomInOn` | `0x00661540` | 13 | von Hand geprüft |
| 45 | `IsZoomOutOn` | `0x00661550` | 13 | von Hand geprüft |
| 46 | `AtUpOn` | – | | im Binary nicht vorhanden (nicht aufgerufen, entfernt) |
| 47 | `AtDownOn` | – | | im Binary nicht vorhanden |
| 48 | `AtUpOff` | – | | im Binary nicht vorhanden |
| 49 | `AtDownOff` | – | | im Binary nicht vorhanden |
| 50 | `IsAtUpOn` | – | | im Binary nicht vorhanden |
| 51 | `IsAtDownOn` | – | | im Binary nicht vorhanden |
| 52 | `GetHairNum` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 53 | `GetFaceNum` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 54 | `GetTexture` | `0x00661560` | 7 | von Hand geprüft |

31 von 55 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006615D0`), `~AgcmCustomizeRender` (`0x006616F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB9C` | `Kamerazustand (0 = keiner, 1 links, 2 rechts, 3 hinein, 4 heraus)` | Kameraschalter |
| `this+0xBA0` | `Render-Ziel-Textur (`GetTexture`)` | `GetTexture` |

## Vtable und OnAddModule

Vtable-Slots: 0 `~AgcmCustomizeRender` (`0x006616F0`), 1 `OnAddModule` (`0x00661680`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`), 3 bis 5 `0x0067FAB0`, 7 `OnDestroy` (`0x00660C10`). `OnAddModule` setzt die Raster-Erweiterung des D3D9-Geräts, merkt sich die alten Release-/Restore-Rückrufe, setzt eigene Rückrufe (`0x00661570`, `0x006615A0`) und holt [`AgcmResourceLoader`](AgcmResourceLoader.md) und `AgcmCharacter` – wie in der Quelle.

## Geräteverlust

Die beiden statischen Rückrufe `NewD3D9ReleaseDeviceCB` (`0x00661570`) und `NewD3D9RestoreDeviceCB` (`0x006615A0`) rufen die alten Rückrufe und danach die Modulfunktionen; `OnLostDevice` und `OnResetDevice` sind in sie eingebaut (sie rufen `DestoryRenderTarget` `0x00660C90` bzw. `CreateRenderTarget` `0x00660910`).

## Kamera und Rendern

`Init` (`0x006619C0`) ruft `CreateCamera` (`0x00660800`), `CreateRenderTarget`, `ClumpClone` (`0x00660A30`, 465 Byte), `SetFace` (`0x006618B0`) und `SetHair` (`0x00661970`). `SetCameraPos` (`0x00660530`, 710 Byte) rechnet mit Sinus/Kosinus; `Render` (`0x00660DF0`, 1368 Byte) ist die größte Funktion und ruft `SetCameraPos`.

## Gesicht und Haare

`SetFace` ruft `DetachFace` (`0x00661360`) und `AttachFace` (`0x00661720`); `SetHair` ruft `DetachHair` (`0x006613E0`) und `AttachHair` (`0x006617F0`). Die Detach-Funktionen rufen den gemeinsamen Entferner `0x00661C20` (vermutlich `RemoveCustomizeAtomicCB`).

## Kamerabedienung

Die Kamerazustände sind Zahlen in `this+0xB9C`: 1 = links drehen, 2 = rechts drehen, 3 = hineinzoomen, 4 = herauszoomen (wie `CS_LEFT_TURN` … `CS_ZOOM_OUT` in der Quelle). Die 13 Einzeiler liegen in der Reihenfolge der Quelle hintereinander: `LeftTurnOn` (`0x00661460`), `RightTurnOn` (`0x00661470`), `LeftTurnOff` (`0x00661480`), `RightTurnOff` (`0x006614A0`), `IsLeftTurnOn` (`0x006614C0`), `IsRightTurnOn` (`0x006614D0`), `ZoomInOn` (`0x006614E0`), `ZoomOutOn` (`0x006614F0`), `ZoomInOff` (`0x00661500`), `ZoomOutOff` (`0x00661520`), `IsZoomInOn` (`0x00661540`), `IsZoomOutOn` (`0x00661550`) und `GetTexture` (`0x00661560`, liefert `this+0xBA0`). Die entsprechenden `AtUp…`/`AtDown…`-Funktionen (Zustände 5 und 6) sind im Binary nicht vorhanden.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `Init`, `CreateCamera`, `CreateRenderTarget`, `ClumpClone`, `SetCameraPos` und `Render` sind über Aufrufbeziehungen, Größenverhältnisse zu den Quellzeilen und die Quellreihenfolge zugeordnet, nicht Zeile für Zeile verglichen.
- Die Zuordnung von `AttachFace`/`AttachHair` (`0x00661720`/`0x006617F0`) und `DetachFace`/`DetachHair` (`0x00661360`/`0x006613E0`) folgt der Aufrufstruktur von `SetFace`/`SetHair` (Gesicht zuerst) und der Quellreihenfolge.
- Dass die `AtUp…`/`AtDown…`-Funktionen fehlen, ist aus dem Fehlen von Funktionen mit den Werten 5/6 geschlossen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 7, gemeinsamer Rumpf: 1, nicht im Client: 14, ohne Kandidat: 4, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `End` | 15 | `0x00660D30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmResourceLoader`](AgcmResourceLoader.md)
- **Erwähnt in:** [`AgcmUICustomizing`](AgcmUICustomizing.md)
