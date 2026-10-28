# AgcmEventItemConvert (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventItemConvert` (Umwandlungs-NPC-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vier von fünf Methoden zugeordnet; `CBReceiveReject` hat einen gemeinsamen Rumpf mit anderen Rückrufen, `SetCallbackEventGrant` ist ein zusammengefalteter Einzeiler.
- **OnAddModule:** 5 Module in der Reihenfolge der Quelle ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgpmEventItemConvert`](AgpmEventItemConvert.md), `AgcmCharacter`, [`AgcmEventManager`](AgcmEventManager.md)); Anmeldungen: Ereignis `0x16` → `CBEventItemConvert` (`0x006DF090`), Grant → `CBReceiveGrant` (`0x006DF130`, reicht das Ergebnis über `EnumCallback` weiter), Reject → `CBReceiveReject` (`0x005759F0`, gemeinsamer Rumpf „drei Zeiger gesetzt → `TRUE`“).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventItemConvert.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DF190` | 200 | vtable/String |
| 1 | `CBEventItemConvert` | `0x006DF090` | 151 | Callback-Registrierung |
| 2 | `CBReceiveGrant` | `0x006DF130` | 37 | Callback-Registrierung |
| 3 | `CBReceiveReject` | `0x005759F0` | 30 | gleiche Adresse wie `gemeinsamer Rumpf (drei Zeiger gesetzt → TRUE)` (vom Linker zusammengefaltet) |
| 4 | `SetCallbackEventGrant` | – | | Einzeiler (`SetCallback`), zusammengefaltet |

4 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DF040`), `~AgcmEventItemConvert` (`0x006DF160`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-ID `0x16` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventItemConvert`](AgpmEventItemConvert.md), [`AgpmItemConvert`](AgpmItemConvert.md)
