# AgpmEventPointLight (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmEventPointLight` (Punktlicht-Ereignis an Objekten: Daten, Stream, Rückrufe beim Hinzufügen und Entfernen von Objekten) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/APublic/AgpmEventPointLight/AgpmEventPointLight.cpp` und `Include/AgpmEventPointLight.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle sieben Methoden sind zugeordnet (die sechs Rückrufe waren schon über die Registrierung benannt).
- **Abweichungen:** keine; im Binary fehlt nur die Hinweismeldung (`TRACE`) der Quelle.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmEventPointLight.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0056A670` | 116 | vtable/String |
| 1 | `CBEventPointLightConstructor` | `0x0056A4A0` | 75 | Callback-Registrierung |
| 2 | `CBEventPointLightDestructor` | `0x0056A4F0` | 25 | Callback-Registrierung |
| 3 | `CBEventPointLightStreamWrite` | `0x0056A510` | 84 | Callback-Registrierung |
| 4 | `CBEventPointLightStreamRead` | `0x0056A570` | 97 | Callback-Registrierung |
| 5 | `CBOnAddObject` | `0x0056A5E0` | 48 | Callback-Registrierung |
| 6 | `CBOnRemoveObject` | `0x0056A610` | 48 | Callback-Registrierung |

7 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmEventPointLight` (`0x0056A410`), `scalar_deleting_dtor` (`0x0056A640`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB84` | `Zeiger [`ApmEventManager`](ApmEventManager.md)` | `OnAddModule`, `CBOnAddObject` |
| `Ereignis+0x08` | `Zeiger auf die Punktlicht-Daten (`m_pvData`)` | Stream-Rückrufe |

## Vtable und Aufbau

Vtable `0x008B843C`: Slot 0 Löschwrapper (`0x0056A640`), Slot 1 `OnAddModule` (`0x0056A670`), Slot 2 `0x0067AC90`, Slot 3 `0x0067FAB0`. Konstruktor `0x0056A410` (138 Byte): ruft den `ApModule`-Konstruktor (`0x004E4700`), trägt `AgpmEventPointLight` als Modulnamen ein, nullt den Zeiger `m_pcsApmEventManager` (`this+0xB84`) und legt über `SetModuleData` (`0x004E4160`) einen Datenblock von 0x30 Byte (`sizeof(AgpdPointLight)`) mit der Kennung `AGPMPOINTLIGHT_DATA` (0) an.

## Registrierung

`OnAddModule` (`0x0056A670`, 116 Byte) holt `ApmEventManager`, meldet dort die Ereignisfunktion `0x1E` (`APDEVENT_FUNCTION_POINTLIGHT`) mit Konstruktor (`0x0056A4A0`), Destruktor (`0x0056A4F0`), Schreib- (`0x0056A510`) und Lese-Rückruf (`0x0056A570`) an und hängt, falls [`ApmObject`](ApmObject.md) vorhanden ist, `CBOnAddObject` (`0x0056A5E0`) und `CBOnRemoveObject` (`0x0056A610`) als Rückrufe für hinzugefügte bzw. entfernte Objekte an (`ApmObject::SetCallbackAddObject` `0x005766B0`; das Entfernen läuft über den gemeinsamen `SetCallback`-Rumpf `0x0053A200`, Kennung 1).

## Rückrufe

`CBEventPointLightConstructor` (75 Byte) legt den Datenblock des Ereignisses an und kopiert ihn aus dem Quellereignis, falls eines übergeben wird; `CBEventPointLightDestructor` gibt ihn frei. `CBEventPointLightStreamWrite` (84 Byte) schreibt `PointLightStart`, ruft den Datenschreiber (Enum-Rückruf mit Kennung 0) und schreibt `PointLightEnd`; `CBEventPointLightStreamRead` (97 Byte) liest den Wertnamen, vergleicht ihn mit `PointLightStart` und ruft den Leser (Enum-Rückruf 0); die Hinweismeldung der Quelle bei fehlendem Ende ist im Binary nicht vorhanden (`TRACE`).
`CBOnAddObject` und `CBOnRemoveObject` (je 48 Byte) holen das Punktlicht-Ereignis des Objekts und lösen bei Erfolg den Rückruf `AGPMEVENTPOINTLIGHT_ADDOBJECT` bzw. `…REMOVEOBJECT` aus; diese beiden Kennungen belegt [`AgcmEventPointLight`](AgcmEventPointLight.md) (siehe dessen Bericht: Kennung 0 bzw. 1).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind `OnAddModule` und die beiden Stream-Rückrufe; Konstruktor-, Destruktor- und die beiden Objekt-Rückrufe sind über die Registrierung und die Größe zugeordnet.
- Die Bedeutung der Kennungen `AGPMEVENTPOINTLIGHT_ADDOBJECT`/`…REMOVEOBJECT` (0 und 1) beruht auf dem Bericht zu `AgcmEventPointLight`; ihre Werte wurden hier nicht im Header geprüft.
- Die Felder von `AgpdPointLight` (0x30 Byte) wurden nicht vermessen.

## Querverweise

- **Erwähnt Module:** [`AgcmEventPointLight`](AgcmEventPointLight.md), [`ApmEventManager`](ApmEventManager.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcmEventPointLight`](AgcmEventPointLight.md), [`ApmObject`](ApmObject.md)
