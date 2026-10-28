# AgcmWater (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmWater` (Wasser, Wellen, Hochqualitätswasser mit Spiegelung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmWater/AgcmWater.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: jede Quellmethode ist einer Adresse zugeordnet oder begründet. Zugeordnet sind Modulaufbau, alle im Client benutzten Rückrufe, die Auftragswarteschlange, Erzeugen/Entfernen von Wasser und Wellen, `SetWaterDetail`, `ChangeHWaterMode` (beide Fassungen), Reflexion, Shader-Konstanten, Rendern und die beiden INI-Lader. Alle Funktionen des Moduls liegen zwischen `0x00642D40` und `0x0064922F` (dahinter beginnt [`AgcmGrass`](AgcmGrass.md)).
- **Nicht im Binary:** Editor-/Werkzeugfunktionen (`AddWater`, `DeleteWater`, `AddWave`, `AutoMakeWave`, `DeleteWave`, `ChangeWater`, `ChangeStatus`, `RemoveWaterRange`, `SaveToFiles`, `Save…ToINI`, `ChangeHWaterStatus`, `CloseHandleList`, `UpdateEMCB`, `GetWaterType`, `GetWaterStatus`), die toten Reflexionshelfer und die leeren oder nur auskommentiert benutzten Rückrufe; jede Zeile der Tabelle nennt den Grund.
- **Abweichungen:** keine festgestellt; `UpdateReflectionMap` entspricht dem frühen `return` der Quelle (Reflexions-Rendern ist abgeschaltet).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmWater.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006489C0` | 244 | vtable/String |
| 1 | `OnInit` | `0x00643310` | 653 | vtable/String |
| 2 | `RemoveAll` | `0x00647F60` | 64 | von Hand geprüft |
| 3 | `OnDestroy` | `0x00647FA0` | 596 | vtable/String |
| 4 | `onLostDevice` | – | | leerer Rumpf, nicht virtuell; nur vom statischen Rückruf `newD3D9ReleaseDeviceCB` gerufen, der Aufruf ist weggefallen |
| 5 | `onResetDevice` | – | | leerer Rumpf, nicht virtuell; nur vom statischen Rückruf `newD3D9RestoreDeviceCB` gerufen, der Aufruf ist weggefallen |
| 6 | `OnIdle` | `0x00648AC0` | 953 | vtable/String |
| 7 | `OnCameraStateChange` | `0x006435A0` | 180 | vtable/String |
| 8 | `CB_POST_RENDER_REFLECTION_DRAW` | `0x00646EC0` | 255 | von Hand geprüft |
| 9 | `CB_POST_RENDER2` | `0x00646FC0` | 236 | von Hand geprüft |
| 10 | `CB_W1Update` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer leerer Rumpf (`AddWaterToRender` übergibt `Element::GetSize`)` (vom Linker zusammengefaltet) |
| 11 | `CB_W2Update` | `0x006470B0` | 20 | von Hand geprüft |
| 12 | `CB_W2Render` | `0x00643660` | 53 | von Hand geprüft |
| 13 | `CB_W1Release` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer leerer Rumpf (`AddWaterToRender` übergibt `Element::GetSize`)` (vom Linker zusammengefaltet) |
| 14 | `CB_W2Release` | – | | wird nirgends übergeben (`AddWaveToRender` übergibt nur `CB_W2Update` und `CB_W2Render`); im Binary nicht vorhanden |
| 15 | `WaveUpdate` | `0x006436A0` | 1189 | von Hand geprüft |
| 16 | `SetWaterDetail` | `0x00649230` | 249 | von Hand geprüft |
| 17 | `DeleteAll` | `0x006470D0` | 528 | von Hand geprüft |
| 18 | `ReleaseWater` | `0x00643B50` | 65 | von Hand geprüft |
| 19 | `ReleaseWave` | – | | leerer Rumpf; die Aufrufe (`DeleteAll`, `JobQueueRemove…`) sind weggefallen |
| 20 | `AddWaterToRender` | `0x00643BA0` | 65 | von Hand geprüft |
| 21 | `RemoveWaterFromRender` | – | | in `DeleteAll` eingebaut (`RemoveAtomicFromWorld` und `RemoveUpdateInfoFromAtomic2` mit den leeren Rückrufen) |
| 22 | `AddWaveToRender` | `0x00647360` | 366 | von Hand geprüft |
| 23 | `RemoveWaveFromRender` | `0x00643BF0` | 79 | von Hand geprüft |
| 24 | `JobQueueRemoveAll` | `0x00643C40` | 182 | von Hand geprüft |
| 25 | `JobQueueAdd` | `0x00643D00` | 319 | von Hand geprüft |
| 26 | `JobQueueRemove` | `0x00643E40` | 325 | von Hand geprüft |
| 27 | `OnLoadSectorWaterLevelCallback` | `0x00648200` | 1461 | von Hand geprüft |
| 28 | `OnReleaseSectorWaterLevelCallback` | `0x00643F90` | 88 | von Hand geprüft |
| 29 | `AddWater` | – | | Editorfunktion, von keinem Client-Modul gerufen; im Binary nicht vorhanden |
| 30 | `DeleteWater` | – | | Editorfunktion, von keinem Client-Modul gerufen; im Binary nicht vorhanden |
| 31 | `MakeWater` | `0x00643FF0` | 1380 | von Hand geprüft |
| 32 | `MakeWave` | `0x006474D0` | 605 | von Hand geprüft |
| 33 | `ChangeWater` | – | | Editorfunktion (Rumpf praktisch leer), von keinem Client-Modul gerufen; im Binary nicht vorhanden |
| 34 | `WaveDataSet` | `0x00644560` | 216 | von Hand geprüft |
| 35 | `AddWave` | – | | nur von `AutoMakeWave` gerufen (Editor); im Binary nicht vorhanden |
| 36 | `AutoMakeWave` | – | | nur von den Editorfunktionen `AddWater` und `RemoveWaterRange` gerufen; im Binary nicht vorhanden |
| 37 | `DeleteWave` | – | | Editorfunktion; im Binary nicht vorhanden |
| 38 | `GetWater` | `0x00644640` | 256 | von Hand geprüft |
| 39 | `GetWaterType` | – | | von keinem Modul gerufen; im Binary nicht vorhanden |
| 40 | `GetWaterHeight` | `0x00644740` | 56 | von Hand geprüft |
| 41 | `GetWaterStatus` | – | | von keinem Modul gerufen; im Binary nicht vorhanden |
| 42 | `SaveToFiles` | – | | Editorfunktion; im Binary nicht vorhanden |
| 43 | `RemoveWaterRange` | – | | Editorfunktion; im Binary nicht vorhanden |
| 44 | `ChangeStatus` | – | | Editorfunktion; im Binary nicht vorhanden |
| 45 | `GetShader` | `0x00644780` | 200 | von Hand geprüft |
| 46 | `InitBumpMaps` | `0x00644850` | 539 | von Hand geprüft |
| 47 | `SkinAtomicDraw` | – | | nur von den `ImmediateHWater…`-Funktionen benutzt, die selbst nur im toten Teil von `UpdateReflectionMap` stehen; im Binary nicht vorhanden |
| 48 | `ImmediateHWaterAtomicListRender` | – | | nur im toten Teil von `UpdateReflectionMap` benutzt; im Binary nicht vorhanden |
| 49 | `ImmediateHWaterAtomicRender` | – | | nur im toten Teil von `UpdateReflectionMap` benutzt; im Binary nicht vorhanden |
| 50 | `ImmediateHWaterTerrainRender` | – | | nur im toten Teil von `UpdateReflectionMap` benutzt; im Binary nicht vorhanden |
| 51 | `SetReflectShaderConstant` | – | | in der Quelle nirgends aufgerufen; im Binary nicht vorhanden |
| 52 | `sgn` | – | | nur von `ModifyD3DProjectionMatrix` benutzt; im Binary nicht vorhanden |
| 53 | `ModifyD3DProjectionMatrix` | – | | nur im Teil von `UpdateReflectionMap` hinter dem frühen `return` benutzt; im Binary nicht vorhanden |
| 54 | `UpdateReflectionMap` | `0x00644A80` | 83 | von Hand geprüft |
| 55 | `AddHWaterToRender` | `0x006487C0` | 97 | von Hand geprüft |
| 56 | `RemoveHWaterFromRender` | – | | in `DeleteAll` und `ChangeHWaterMode` (Sektorfassung) eingebaut |
| 57 | `ReleaseHWater` | – | | in `DeleteAll` und `ChangeHWaterMode` (Sektorfassung) eingebaut (Freigabe der Puffer) |
| 58 | `ChangeHWaterMode` | `0x00648E80` | 939 | von Hand geprüft |
| 59 | `ChangeHWaterMode` | `0x00648830` | 388 | von Hand geprüft |
| 60 | `SetShaderCommonConstant` | `0x00644AE0` | 884 | von Hand geprüft |
| 61 | `SetShaderConstant` | `0x00644E60` | 555 | von Hand geprüft |
| 62 | `CB_POST_RENDER` | – | | die Anmeldung in `OnAddModule` ist auskommentiert; im Binary nicht vorhanden |
| 63 | `CB_HWUpdate` | `0x00645090` | 51 | von Hand geprüft |
| 64 | `CB_HWRender` | `0x00647730` | 90 | von Hand geprüft |
| 65 | `CB_HWRelease` | – | | wird nirgends übergeben; im Binary nicht vorhanden |
| 66 | `RenderHQWater` | `0x006450D0` | 786 | von Hand geprüft |
| 67 | `RenderHQWater` | `0x006453F0` | 860 | von Hand geprüft |
| 68 | `UpdateEMCB` | – | | in der Quelle nirgends benutzt; im Binary nicht vorhanden |
| 69 | `MakeHWaterFromWater` | – | | Fassung ohne Argument (alle Sektoren): wird nur im toten Zweig von `SetWaterDetail` und in `ChangeHWaterStatus` (Editor) gerufen; im Binary nicht vorhanden. Die Sektorfassung ist `0x00647790`, gerufen von `OnIdle` (Auftrag `WATER_JOB_MAKEANDADDHWATER`) |
| 70 | `MakeHWaterFromWater` | `0x00647790` | 1977 | von Hand geprüft |
| 71 | `ChangeHWaterStatus` | – | | Editorfunktion, nirgends aufgerufen; im Binary nicht vorhanden |
| 72 | `LoadStatusInfoT1FromINI` | `0x00645760` | 2908 | von Hand geprüft |
| 73 | `SaveStatusInfoT1ToINI` | – | | Editorfunktion; im Binary nicht vorhanden |
| 74 | `LoadHWaterStatusFromINI` | `0x006462C0` | 2881 | von Hand geprüft |
| 75 | `SaveHWaterStatusToINI` | – | | Editorfunktion; im Binary nicht vorhanden |
| 76 | `CloseHandleList` | – | | in der Quelle nirgends benutzt; im Binary nicht vorhanden |
| 77 | `OnLoadSectorWaterLevelCallback` | – | | zweite Definition (Quelle Zeile 6639) steht in einem Kommentarblock und gehört nicht zum übersetzten Modul; die gültige ist `0x00648200` |
| 78 | `CBDeleteAllQueue` | `0x00646E30` | 15 | von Hand geprüft |
| 79 | `CB_DistCorrect` | – | | nur in auskommentiertem Code benutzt; im Binary nicht vorhanden |

45 von 80 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmWater` (`0x00642D40`), `newD3D9ReleaseDeviceCB` (`0x00646E40`), `~AgcmWater` (`0x00646E80`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA4` | `Zeiger [`ApmOcTree`](ApmOcTree.md) (`+0xB84` = `m_bOcTreeEnable`)` | `RemoveWaveFromRender`, `AddWaveToRender` |
| `this+0xBB8` | `Kopf der Sektorliste (Sektoren verkettet über `+0x1C`)` | `GetWater`, `RemoveAll` |
| `this+0xBC8` | `Wasserstufe (0 = hoch)` | `CB_POST_RENDER2` |
| `this+0xBCC` | `Liste der zu zeichnenden Wellen (`m_listDrawWave`)` | `CB_W2Render` |
| `this+0xBD0` | `Liste der zu zeichnenden Hochqualitätswasser (`m_listDrawHWater`)` | `CB_HWRender` |
| `this+0x3828` | `D3D9-Gerät` | `InitBumpMaps`, `RenderHQWater` |
| `this+0x3830 / 0x3834` | `Hauptkamera / Spiegelkamera` | `UpdateReflectionMap`, `OnCameraStateChange` |
| `this+0x38D4` | `Hochqualitätswasser aktiv (`m_bEnableHWater`)` | `OnCameraStateChange`, `CB_POST_RENDER_REFLECTION_DRAW` |
| `this+0x3A1C…0x3A24` | `Auftragswarteschlange: Zeiger, Zähler, Höchstzahl` | `JobQueue…` |

## Vtable

Vtable-Slots: 0 `~AgcmWater` (`0x00646E80`), 1 `OnAddModule` (`0x006489C0`), 2 `OnInit` (`0x00643310`), 3 `OnIdle` (`0x00648AC0`), 4 und 5 `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x00647FA0`), 8 und 9 gemeinsamer Rumpf `0x004E3420`. Der Konstruktor steht bei `0x00642D40` (1486 Byte, trägt die Zeichenkette `AgcmWater`); er hieß vorher `ctor_or_dtor`.

## Rückrufe für Wasser, Wellen und Reflexion

`CB_W2Render` (`0x00643660`) legt eine Welle mit `UpdateCount > 0` (Feld `+0x28`) als 8-Byte-Eintrag vorn in die Liste `this+0xBCC` (`m_listDrawWave`). `CB_W2Update` (`0x006470B0`, 20 Byte) ruft nur `WaveUpdate` (`0x006436A0`) und gibt TRUE. `CB_POST_RENDER_REFLECTION_DRAW` (`0x00646EC0`) kopiert die Matrix der Hauptkamera (`this+0x3830`) in die der Spiegelkamera (`this+0x3834`), kehrt `up.y`, `right.x`, `right.z`, `at.y` um, spiegelt `pos.y` an der Wasserhöhe (`this+0x3844`) und rückt die Position um das 200-fache der Blickrichtung zurück; bei gesetztem `m_bReflectionUpdate` (`this+0x38C8`) und abgelaufenem Zähler (`this+0x38CC` gegen `this+0x38D0`) ruft es `UpdateReflectionMap`. `CB_POST_RENDER2` (`0x00646FC0`) ruft bei hoher Wasserstufe (`this+0xBC8 == 0`) `RenderHQWater()` und zeichnet danach die Wellen-Liste mit Im3D (`6` Eckpunkte je Welle, Textur je Status). `CBDeleteAllQueue` (`0x00646E30`) ruft `JobQueueRemoveAll`. `CB_HWUpdate` (`0x00645090`) setzt beim ersten Aufruf `m_bReflectionUpdate` und übernimmt die Höhe des Hochqualitätswassers (`+0xC`) in `this+0x387C` und `this+0x3844`. `CB_HWRender` (`0x00647730`) ruft bei aktivem Octree `RenderHQWater(HWater*)` und legt sonst einen Eintrag in `this+0xBD0` (`m_listDrawHWater`) an.

## Welle, Wasser und Auftragswarteschlange

`WaveUpdate` (`0x006436A0`, 1189 Byte) verschiebt Position und Textur-Koordinaten einer Welle um die Frame-Zeit (`this+0xBC0`), wechselt die Farbe der sechs Eckpunkte und setzt die Welle nach Ablauf zurück. `WaveDataSet` (`0x00644560`) setzt Anfangsrichtung (Kosinus/Sinus), Textur-Koordinaten und Zähler einer neuen Welle. `MakeWater` (`0x00643FF0`, 1380 Byte) baut das Geometrie-Viereck (4 Eckpunkte, Größe aus den Feldern `+2/+10` der Wasserdaten) und hängt es mit `AddWaterToRender` an. `MakeWave` (`0x006474D0`, 605 Byte) füllt die sechs Eckpunkte einer Welle und ruft bei gesetztem Merker `AddWaveToRender` (`0x00647360`); dieser registriert bei aktivem Octree die Rückrufe `CB_W2Render`/`CB_W2Update` über `AddCustomRenderDataToOcTree`, sonst über `AddCustomRenderToSector`. `ReleaseWater` (`0x00643B50`) zerstört Frame und Atomic; `RemoveWaveFromRender` (`0x00643BF0`) entfernt die Welle aus Octree bzw. Sektor. `DeleteAll` (`0x006470D0`) räumt die drei Listen eines Sektors, `RemoveAll` (`0x00647F60`) ruft es für alle Sektoren. `GetWater` (`0x00644640`) sucht über Sektorindex und Rechteck, `GetWaterHeight` (`0x00644740`) liefert daraus die Höhe (`+0xC`).
`JobQueueRemoveAll` (`0x00643C40`), `JobQueueAdd` (`0x00643D00`) und `JobQueueRemove` (`0x00643E40`) arbeiten auf dem Feld `this+0x3A1C` (Einträge zu 12 Byte, Zähler `this+0x3A20`, Höchstzahl `this+0x3A24`, Verdopplung bei Überlauf, Sperre `this+0x3A00` wenn `this+0x3A18` gesetzt). Auftragsarten 4/5/6 werden freigegeben, wie in der Quelle (`WAVEADDTOSECTOR`, `WATERADDTOSECTOR`, `SECTORADDTOSECTORLIST`). `OnReleaseSectorWaterLevelCallback` (`0x00643F90`) ruft `JobQueueRemove` und danach `JobQueueAdd(7, …)` und bricht bei Detailstufe 2 ab (`SECTOR_HIGHDETAIL`); es holt die Instanz über `DAT_009E2AC0` (`m_pThis`).

## Hochqualitätswasser

`UpdateReflectionMap` (`0x00644A80`) beendet die Hauptkamera, beginnt/löscht/beendet die Spiegelkamera (Z-Puffer) und beginnt die Hauptkamera erneut; der Rest der Quelle (Himmel, `RenderMyCamera`) steht dort nach einem frühen `return` und ist im Binary entfernt. `SetShaderCommonConstant` (`0x00644AE0`, 884 Byte) und `SetShaderConstant` (`0x00644E60`, Status-Eintrag zu `0x98` Byte) setzen die Shader-Konstanten. `RenderHQWater(HWater*)` (`0x006450D0`) und `RenderHQWater()` (`0x006453F0`, Schleife über `this+0xBD0`) setzen Shader, Texturen und Sampler und zeichnen. `InitBumpMaps` (`0x00644850`) rechnet die Höhenkarten in Bump-Karten um (Differenzen benachbarter Texel); es wird von `LoadHWaterStatusFromINI` (`0x006462C0`) gerufen, wie in der Quelle. `GetShader` (`0x00644780`) übersetzt Shader-Quelltext zu Vertex- oder Pixel-Shader je nach Flag. `AddHWaterToRender` (`0x006487C0`) registriert `CB_HWUpdate`/`CB_HWRender`; `ChangeHWaterMode(bOn, Sektor)` (`0x00648830`) hängt die Liste eines Sektors ein oder aus.

## INI-Laden

`LoadStatusInfoT1FromINI` (`0x00645760`, 2908 Byte) liest pro Status `WTTYPE`, `BMODE_L1` und andere Schlüssel (Zeichenketten im Binary, Format `%d:%s`, `MAX_ID_USED`); `LoadHWaterStatusFromINI` (`0x006462C0`, 2881 Byte) liest unter anderem `Green` und `Height`. Die `Save…ToINI`-Gegenstücke fehlen im Binary (Werkzeugcode).

## Detailstufe und Geräteverlust

`SetWaterDetail` (`0x00649230`, 249 Byte, direkt hinter `OnIdle`) ist die Stufenumschaltung der Optionen (Aufrufer ist die [`AgcmUIOption`](AgcmUIOption.md)-Funktion `0x005DAB00`, wie in der Quelle): die höchste Stufe (0) wird auf mittel (1) abgebildet; war vorher die hohe Stufe aktiv (`this+0xBC8 == 0`), ruft sie `ChangeHWaterMode(FALSE)` (`0x00648E80`). Bei „mittel“ fügt sie für alle Sektoren, deren Wellen noch nicht angemeldet sind (Merker `+0xC`), jede Welle mit `AddWaveToRender` an und setzt den Merker; bei allen anderen Stufen meldet sie die Wellen mit dem Octree- bzw. Sektor-Entferner (`RemoveWaveFromRender`, hier eingebaut) ab. Zuletzt schreibt sie die neue Stufe.
`ChangeHWaterMode(BOOL)` (`0x00648E80`, 939 Byte) läuft über alle Sektoren (`this+0xBB8`) und ruft `ChangeHWaterMode(BOOL, Sektor)` (`0x00648830`); beim Ausschalten gibt sie die Shader und die Spiegel-Texturen/-Kamera frei, beim Einschalten legt sie die beiden 512×512-Raster und die Spiegelkamera an. `newD3D9ReleaseDeviceCB` (`0x00646E40`, 21 Byte) ist der statische Rückruf für den Geräteverlust: ist `m_pThis` gesetzt, ruft er den alten Rückruf; der Aufruf der leeren `onLostDevice` ist weggefallen. Sein Gegenstück `newD3D9RestoreDeviceCB` liegt bei `0x00646E60` (von `OnAddModule` übergeben, nicht als Funktion im Export, deshalb nicht gelesen).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind Rückrufe, `UpdateReflectionMap`, `RenderHQWater` (beide), die Auftragswarteschlange, `AddWaterToRender`, `AddWaveToRender`, `RemoveWaveFromRender` und `SetWaterDetail`; `WaveUpdate`, `MakeWater`, `MakeWave`, `WaveDataSet`, `GetWater`, `GetWaterHeight`, `GetShader`, `InitBumpMaps` und die Shader-Konstanten sind über Struktur, Größenverhältnis und Aufrufbeziehungen zugeordnet (z. B. ruft `OnLoadSectorWaterLevelCallback` `MakeWater`, `WaveDataSet`, `MakeWave`), nicht Zeile für Zeile verglichen.
- Die Aussagen „im Binary nicht vorhanden“ stützen sich jeweils auf die Quelle (kein Aufrufer außerhalb des Moduls, nur auskommentierte oder tote Aufrufe) und auf die Aufrufersuche im Binary; eine Suche über den ganzen Quellbaum fand keine Verwendung der Editorfunktionen außerhalb von `AgcmWater.cpp`. Der einzige Aufrufer von außen (`SetWaterDetail` aus `AgcmUIOption`) ist im Binary gefunden; bei [`AgcmWorld`](AgcmWorld.md) waren Sendefunktionen zunächst übersehen worden, deshalb wurde hier jede Lücke gegen Aufrufer geprüft.
- `CBDeleteAllQueue` (`0x00646E30`) ist nur über den Aufruf von `JobQueueRemoveAll` zugeordnet. `GetCubeMapViewMatrix`, `GetHandle` und `SetReflectShaderCommonConstant` stehen in der Quelle in Kommentarblöcken und gehören nicht zum übersetzten Modul.
- `newD3D9RestoreDeviceCB` (`0x00646E60`) ist nicht gelesen, weil es im Export keine Funktion ist; die Zuordnung folgt der Reihenfolge in `OnAddModule`.
- Bei gleichnamigen Überladungen (`MakeHWaterFromWater`, `OnLoadSectorWaterLevelCallback`, `RenderHQWater`, `ChangeHWaterMode`) steht in der Beleg-Spalte pauschal „von Hand geprüft“; dort wurden die Aufrufbeziehungen und die Paarung der Fassungen geprüft, nicht jeder Rumpf vollständig (`OnLoadSectorWaterLevelCallback`, 1461 Byte, ist nur über seine Aufrufe von `MakeWater`, `WaveDataSet` und `MakeWave` und die Registrierung in `OnAddModule` zugeordnet).
- Die Offsets stammen aus den genannten Funktionen; Feldnamen der Quelle (`m_listDrawWave` usw.) sind aus der Verwendung gefolgert, nicht aus der Klassenlayout-Rechnung belegt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, nicht als eigene Funktion: 11, nicht im Client: 17.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmGrass`](AgcmGrass.md), [`AgcmUIOption`](AgcmUIOption.md), [`AgcmWorld`](AgcmWorld.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmMap`](AgcmMap.md), [`AgcmShadowmap`](AgcmShadowmap.md), [`AgcmTuner`](AgcmTuner.md)
