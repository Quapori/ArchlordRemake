# AgcmGrass (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmGrass` (Gras: Laden pro Sektor, Auftragswarteschlange, Rendern, Schatten) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmGrass/AgcmGrass.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Rückrufe, Auftragswarteschlange, Laden/Entladen, Schattenprüfung, Detailstufe und das Lesen der Grasdaten. Nicht zugeordnet sind `SaveGrassInfoToINI`, `SaveToFiles`, `UnityForSave` (Werkzeugfunktionen), `MakeGrassVerts`, `InitGrass`, `AddGrass`/`RemoveGrass`, `UpdateGrassHeight` und die Kleinfunktionen.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmGrass.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0064B730` | 256 | vtable/String |
| 1 | `OnInit` | `0x0064B830` | 72 | vtable/String |
| 2 | `RemoveAll` | `0x0064C480` | 460 | von Hand geprüft |
| 3 | `OnDestroy` | `0x0064C660` | 240 | vtable/String |
| 4 | `OnIdle` | `0x0064BE80` | 864 | vtable/String |
| 5 | `LoadGrassInfoFromINI` | `0x0064C840` | 1830 | von Hand geprüft |
| 6 | `SaveGrassInfoToINI` | – | | Werkzeugfunktion, im Binary nicht gefunden |
| 7 | `MakeGrassVerts` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 8 | `CB_LIGHT_VALUE_UPDATE` | `0x006499D0` | 586 | Callback-Registrierung |
| 9 | `InitGrass` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `GrassMatrixSet` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `CB_GRASS_UPDATE` | `0x0064A730` | 284 | Callback-Registrierung |
| 12 | `CB_GRASS_RENDER` | `0x0064B880` | 794 | Callback-Registrierung |
| 13 | `CB_SHADOW_UPDATE` | `0x0064A990` | 15 | Callback-Registrierung |
| 14 | `DeleteAll` | `0x0064AC10` | 280 | von Hand geprüft |
| 15 | `JobQueueAdd` | `0x00649480` | 319 | von Hand geprüft |
| 16 | `JobQueueRemove` | `0x0064AD40` | 200 | von Hand geprüft |
| 17 | `LoadGrass` | `0x0064AE10` | 1511 | von Hand geprüft |
| 18 | `CB_LOAD_MAP` | `0x0064B400` | 363 | Callback-Registrierung |
| 19 | `CB_UNLOAD_MAP` | `0x0064B570` | 92 | Callback-Registrierung |
| 20 | `CheckAndUpdateInShadow` | `0x0064A850` | 237 | von Hand geprüft |
| 21 | `AddGrass` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `RemoveGrass` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `UpdateGrassHeight` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `UpdateGrassHeight` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 25 | `CB_OCTREE_ID_SET` | `0x006495C0` | 312 | Callback-Registrierung |
| 26 | `GetGrassMinHeight` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `CB_GET_MIN_HEIGHT` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `CheckGrassList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `OptimaizeGrassList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `UnityForSave` | – | | Werkzeugfunktion, im Binary nicht gefunden |
| 31 | `SaveToFiles` | – | | Werkzeugfunktion, im Binary nicht gefunden |
| 32 | `SetGrassDetail` | `0x0064B5D0` | 343 | von Hand geprüft |
| 33 | `SetDirectoryPath` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `GetGrassRoot` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 35 | `CB_GRASS_DISTCORRECT` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

19 von 36 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0064c1f0` (`0x0064C1F0`), `ctor_or_dtor_0064c3a0` (`0x0064C3A0`), `~AgcmGrass` (`0x0064C7C0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBB4` | `D3D9-Gerät` | `OnInit` |
| `this+0xC18` | `Auftragswarteschlange (Zeiger)` | `OnInit` |
| `this+0xC24` | `Höchstzahl der Aufträge (1000)` | `OnInit` |

## OnAddModule (0x0064B730)

Holt sieben Module in der Reihenfolge der Quelle: [`AgcmRender`](AgcmRender.md), [`ApmMap`](ApmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`ApmOcTree`](ApmOcTree.md), [`AgcmMap`](AgcmMap.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmShadow2`](AgcmShadow2.md). Anmeldungen: `CB_OCTREE_ID_SET` (`0x006495C0`) bei `AgcmRender`, `CB_GET_MIN_HEIGHT` bei `ApmMap`, Karte laden/entladen `CB_LOAD_MAP` (`0x0064B400`) und `CB_UNLOAD_MAP` (`0x0064B570`) bei `AgcmMap`, `CB_LIGHT_VALUE_UPDATE` (`0x006499D0`) bei `AgcmEventNature` und `CB_SHADOW_UPDATE` (`0x0064A990`) bei `AgcmShadow2`.

## OnInit (0x0064B830)

Merkt sich das D3D9-Gerät (`this+0xBB4`), ruft `SetGrassDetail` mit dem Wert 1 (in der Quelle `GRASS_DETAIL_MEDIUM`) und legt die Auftragswarteschlange mit 1000 Einträgen zu je 12 Byte (12000 Byte) an (`this+0xC18`, Anzahl `this+0xC24`), wie in der Quelle.

## Auftragswarteschlange

`JobQueueAdd` (`0x00649480`, 319 Byte) sucht einen gleichen Auftrag und hängt sonst an; bei vollem Puffer wird er laut Quelle verdoppelt. `JobQueueRemove` (`0x0064AD40`, 200 Byte) markiert Aufträge des Sektors als entfernt und ruft für noch nicht abgearbeitete Wurzeln `DeleteAll` (`0x0064AC10`, 280 Byte). `CB_UNLOAD_MAP` ruft `JobQueueRemove` und dann `JobQueueAdd`; `SetGrassDetail` (`0x0064B5D0`) ruft `CB_LOAD_MAP` für alle Wurzeln erneut.

## Laden und Schatten

`CB_LOAD_MAP` ruft `LoadGrass` (`0x0064AE10`, 1511 Byte, früher als `Grass::ctor_or_dtor` benannt). `CheckAndUpdateInShadow` (`0x0064A850`) prüft für jede Pflanze den Schattenpuffer von `AgcmShadow2` und wählt den dunklen oder hellen Vertexpuffer. `RemoveAll` (`0x0064C480`) wird von `OnDestroy` (`0x0064C660`) gerufen. `LoadGrassInfoFromINI` (`0x0064C840`, 1830 Byte) liest die Schlüssel `TEXTURE_NAME` (`%d:%s`), `GRASS_ID`, `GRASS_NAME`, `TEXTURE_ID`, `SHAPE_TYPE`, `GRASS_WIDTH`, `GRASS_HEIGHT`, `GRASS_WIDTH_RANDOM`, `GRASS_HEIGHT_RANDOM`, `ANIM_TYPE` über `ApModuleStream`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `JobQueueAdd`, `JobQueueRemove`, `DeleteAll`, `CheckAndUpdateInShadow`, `SetGrassDetail`, `RemoveAll`, `LoadGrass` und `LoadGrassInfoFromINI` sind über Aufrufbeziehungen (Graph), Zeichenketten und Größen zugeordnet, nicht Zeile für Zeile verglichen; `LoadGrassInfoFromINI` und `SaveGrassInfoToINI` haben dieselben Schlüssel, die Zuordnung zum Lesen folgt aus den `sscanf`-Formaten.
- Die Struktur der Aufträge (12 Byte je Eintrag) folgt aus der Größe `12000` in `OnInit`; die Feldnamen der Quelle wurden nicht nachgeprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 8, ohne Kandidat: 9.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventNature`](AgcmEventNature.md), [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmRender`](AgcmRender.md), [`AgcmShadow2`](AgcmShadow2.md), [`ApmMap`](ApmMap.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmMap`](AgcmMap.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmWater`](AgcmWater.md)
