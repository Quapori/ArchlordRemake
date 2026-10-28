# AgcmUVAnimation (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUVAnimation` (UV-Animation von Materialien: Liste, Zeitfortschritt, Anmeldung bei [`AgcmRender`](AgcmRender.md)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmUVAnimation/AgcmUVAnimation.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; alle Methoden bis auf die eingebauten bzw. nicht verwendeten sind zugeordnet und gegen die Quelle gelesen. Nicht als eigene Funktion vorhanden sind `IsVaildUVAnimation` (in `UpdateUVAnimation` eingebaut), `CallBack_DeleteAtomic` (in `CallBack_RemoveAtomic` eingebaut) und `Callback_UVConstructor` (nirgends angemeldet).
- **Abweichungen:** keine festgestellt; die in der Quelle auskommentierten Anmeldungen `SetCallbackRemoveAtomic`/`RemoveClump` fehlen auch im Binary.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUVAnimation.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DCA50` | 83 | vtable/String |
| 1 | `OnIdle` | `0x006DC680` | 72 | vtable/String |
| 2 | `OnDestroy` | `0x006DC4E0` | 51 | vtable/String |
| 3 | `UpdateUVAnimation` | `0x006DC520` | 148 | von Hand geprüft |
| 4 | `AddUVAnimation` | `0x006DC840` | 94 | von Hand geprüft |
| 5 | `RemoveUVAnimation` | `0x006DC5C0` | 91 | von Hand geprüft |
| 6 | `FindUVAnimation` | `0x006DC490` | 69 | von Hand geprüft |
| 7 | `IsVaildUVAnimation` | – | | in `UpdateUVAnimation` eingebaut |
| 8 | `CallBack_AddAtomic` | `0x006DC990` | 69 | Callback-Registrierung |
| 9 | `CallBack_AddClump` | `0x006DCA20` | 40 | Callback-Registrierung |
| 10 | `CallBack_DeleteAtomic` | – | | in `CallBack_RemoveAtomic` eingebaut (kein eigener Aufrufer) |
| 11 | `CallBack_DeleteClump` | `0x006DC930` | 40 | von Hand geprüft |
| 12 | `CallBack_FindAtomic` | `0x006DC9E0` | 63 | von Hand geprüft |
| 13 | `CallBack_FindGeometry` | `0x006DC960` | 37 | von Hand geprüft |
| 14 | `CallBack_FindMaterial` | `0x006DC8A0` | 46 | von Hand geprüft |
| 15 | `CallBack_RemoveAtomic` | `0x006DC8D0` | 63 | von Hand geprüft |
| 16 | `CallBack_RemoveGeometry` | `0x006DC6D0` | 37 | von Hand geprüft |
| 17 | `CallBack_RemoveMaterial` | `0x006DC620` | 46 | von Hand geprüft |
| 18 | `Callback_UVConstructor` | – | | im Binary nicht vorhanden (nirgends angemeldet) |
| 19 | `Callback_UVDestructor` | `0x006DC650` | 40 | von Hand geprüft |

17 von 20 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUVAnimation` (`0x006DC700`), `~AgcmUVAnimation` (`0x006DC7A0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Kopfknoten der Liste `m_listUVAnimation` (Einträge zu 16 Byte: Knoten, Material, Zeit)` | `UpdateUVAnimation`, `FindUVAnimation` |
| `this+0xBA0` | `Zeitstempel des letzten Takts (`m_nPrevTickCount`)` | `OnIdle` |

## Aufbau

Der Konstruktor (`0x006DC700`) setzt die Vtable, legt die leere Liste `m_listUVAnimation` an (Kopfknoten bei `this+0xB98`), trägt den Modulnamen `AgcmUVAnimation` ein und schaltet `OnIdle` an (`EnableIdle(TRUE)`); `m_nPrevTickCount` liegt bei `this+0xBA0`. Der Destruktor (`0x006DC7A0`) räumt die Liste; `0x006DC910` ist der Löschwrapper. `OnAddModule` (`0x006DCA50`) holt `AgcmRender`, meldet `CallBack_AddAtomic` und `CallBack_AddClump` an und setzt `MatDestrucTorCallbackUV` (`DAT_00C2B358`) auf `Callback_UVDestructor` (`0x006DC650`) und `m_pThis` (`DAT_00C23C14`).

## Takt und Liste

`OnIdle` (`0x006DC680`) bildet die Zeitdifferenz zum letzten Takt mal `0,001` (Konstante `_DAT_0089A8E8`) und ruft `UpdateUVAnimation` (`0x006DC520`). Dieses läuft über die Liste, entfernt Einträge mit ungültigem Material (Referenzzähler ≤ 0, keine Effekte, keine Textur; `IsVaildUVAnimation` ist eingebaut) und ruft für gültige `RpMaterialUVAnimAddAnimTime` und `RpMaterialUVAnimApplyUpdate` und addiert die Zeit. `AddUVAnimation` (`0x006DC840`) prüft Material und Textur, ruft `FindUVAnimation` (`0x006DC490`) und hängt hinten an; `RemoveUVAnimation` (`0x006DC5C0`) sucht und löscht den Eintrag.

## Durchlauf-Rückrufe

Material: `CallBack_FindMaterial` (`0x006DC8A0`, bei vorhandener UV-Animation `AddUVAnimation`) und `CallBack_RemoveMaterial` (`0x006DC620`, `RemoveUVAnimation`). Geometrie: `CallBack_FindGeometry` (`0x006DC960`) und `CallBack_RemoveGeometry` (`0x006DC6D0`) rufen den Durchlauf über alle Materialien. Atomic: `CallBack_AddAtomic` (`0x006DC990`) und `CallBack_FindAtomic` (`0x006DC9E0`) laufen über die Geometrie und alle LOD-Geometrien, `CallBack_RemoveAtomic` (`0x006DC8D0`) entsprechend für das Entfernen. `CallBack_AddClump` (`0x006DCA20`) und `CallBack_DeleteClump` (`0x006DC930`) laufen über alle Atomics des Clumps.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `CallBack_FindAtomic`/`CallBack_RemoveAtomic` und `CallBack_FindGeometry`/`CallBack_RemoveGeometry` sind Paare mit gleicher Struktur; die Trennung folgt dem jeweils aufgerufenen Material-Rückruf (`0x006DC8A0` bzw. `0x006DC620`).
- Der Destruktor-Wrapper `0x006DC910` war schon benannt; dass `0x006DC7A0` der eigentliche Destruktorrumpf ist, folgt aus dem Leeren der Liste und dem Rücksetzen der Vtable.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 2, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmRender`](AgcmRender.md)
- **Erwähnt in:** [`AgcmEff2`](AgcmEff2.md)
