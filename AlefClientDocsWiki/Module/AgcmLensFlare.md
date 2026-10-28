# AgcmLensFlare (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmLensFlare` (Linsenreflexe von Sonne und Mond) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Modulaufbau, Darstellung, Rückrufe, Geräteverlust und das Lesen der Vorlage sind zugeordnet; `StreamWriteTemplate`, `CBSkyChange`, `CBLightRayIntersect`, `checkAndUpdateOcclusionQuery` und die Kleinfunktionen wurden nicht einzeln gefunden.
- **OnAddModule** (`0x00642910`): Module [`AgcmRender`](AgcmRender.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmMap`](AgcmMap.md), [`AgpmTimer`](AgpmTimer.md), [`ApmMap`](ApmMap.md) (Zeichenketten im Dekompilat); `CB_PRE_RENDER` (`0x006428D0`, rendert nur bei Typ Mond, Wert 1) und `CB_POST_RENDER` (`0x006428F0`, nur bei Typ Sonne, Wert 0) rufen beide `RenderLensFlare` (`0x006424A0`, 1680 Byte).
- **OnInit** (`0x00642A60`) meldet über AngelScript `void ChangeLensFlareTemplate(string &in)` an; `ChangeLensFlareTemplate` (`0x006421C0`) liest `ini/%s.ini` bzw. `Ini/LensFlare.ini` über `StreamReadTemplate` (`0x00641B00`, Schlüssel `Number` und Format `%f,%f,%d,%d,%d,%d,%d`).
- **OnIdle** (`0x00642330`) liest die Sonnenposition von `AgcmEventNature` und ruft `GetWorldPosToScreenPos` (`0x00641920`).
- **Geräteverlust:** `onLostDevice` (`0x00642100`) gibt die Occlusion-Abfrage (`this+0xEB0`) frei, `onResetDevice` (`0x00642140`) legt sie über `CreateQuery(9)` neu an.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmLensFlare.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `ResetContent` | `0x00641650` | 80 | von Hand geprüft |
| 1 | `ChangeLensFlareTemplate` | `0x006421C0` | 366 | Zeichenkette |
| 2 | `OnInit` | `0x00642A60` | 730 | vtable/String |
| 3 | `OnAddModule` | `0x00642910` | 321 | vtable/String |
| 4 | `OnIdle` | `0x00642330` | 349 | vtable/String |
| 5 | `CBLightRayIntersect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `OnDestroy` | `0x00641820` | 49 | vtable/String |
| 7 | `OnCameraStateChange` | `0x00642490` | 8 | vtable/String |
| 8 | `CB_PRE_RENDER` | `0x006428D0` | 24 | von Hand geprüft |
| 9 | `CB_POST_RENDER` | `0x006428F0` | 24 | von Hand geprüft |
| 10 | `RenderLensFlare` | `0x006424A0` | 1680 | von Hand geprüft |
| 11 | `SetMyWorldCamera` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `CameraStatusChange` | `0x00641860` | 185 | von Hand geprüft |
| 13 | `GetWorldPosToScreenPos` | `0x00641920` | 478 | von Hand geprüft |
| 14 | `StreamReadTemplate` | `0x00641B00` | 860 | von Hand geprüft |
| 15 | `StreamWriteTemplate` | – | | im Binary nicht gefunden (Schreibcode für Werkzeuge) |
| 16 | `CBSkyChange` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `checkAndUpdateOcclusionQuery` | – | | nicht einzeln gefunden (vermutlich in `RenderLensFlare` oder die Aufrufer eingebaut) |
| 18 | `onLostDevice` | `0x00642100` | 60 | von Hand geprüft |
| 19 | `onResetDevice` | `0x00642140` | 67 | von Hand geprüft |

15 von 20 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006416A0`), `~AgcmLensFlare` (`0x00642190`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Typ der Vorlage (0 Sonne, 1 Mond)` | `CB_PRE_RENDER`, `CB_POST_RENDER` |
| `this+0xDF0` | `Zeiger, aus dem Matrixwerte gelesen werden (vermutlich Kamera)` | `GetWorldPosToScreenPos` |
| `this+0xEB0` | `Zeiger auf die Occlusion-Abfrage` | `onLostDevice`, `onResetDevice` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `GetWorldPosToScreenPos` ist nur über den Aufruf aus `OnIdle` mit der Sonnenposition und die große Rechenstruktur zugeordnet; die Occlusion-Abfrage-Funktion wurde nicht von ihr getrennt.
- Die Typwerte 0 = Sonne und 1 = Mond folgen aus den Vergleichen in den beiden Rückrufen und der Namensreihenfolge; die Aufzählung der Quelle wurde nicht nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht im Client: 1, ohne Kandidat: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventNature`](AgcmEventNature.md), [`AgcmMap`](AgcmMap.md), [`AgcmRender`](AgcmRender.md), [`AgpmTimer`](AgpmTimer.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmTuner`](AgcmTuner.md)
