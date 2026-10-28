# AgcmArchlord (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmArchlord` (Archlord-Ernennung und -Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, `CBOperationSetArchlord`, `CBRequestEvent` und `SendRequestEvent` zugeordnet; `CBOperationCancelArchlord` hat einen leeren Rumpf (gemeinsamer Stub), `OperationSetArchlord` ist eingebaut.
- **OnAddModule** (`0x006E01C0`): vier Module in dieser Reihenfolge ([`AgpmArchlord`](AgpmArchlord.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgcmEventManager`](AgcmEventManager.md), wie die Quelle); Anmeldungen: `CBOperationSetArchlord` (`0x006E0120`), der Abbruch-Rückruf über einen gemeinsamen Stub und `RegisterEventCallback(0x24)` → `CBRequestEvent` (`0x006E0150`).
- **Senden:** `SendRequestEvent` (`0x006E0070`) baut das Paket über `0x0057B6F0` und sendet es; `CBRequestEvent` ruft es.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmArchlord.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E01C0` | 172 | vtable/String |
| 1 | `CBOperationSetArchlord` | `0x006E0120` | 37 | Callback-Registrierung |
| 2 | `CBOperationCancelArchlord` | – | | Rumpf in der Quelle leer, gemeinsamer Stub (Anmeldung über `0x0053A200`) |
| 3 | `CBRequestEvent` | `0x006E0150` | 109 | Callback-Registrierung |
| 4 | `OperationSetArchlord` | – | | Einzeiler, eingebaut |
| 5 | `SendRequestEvent` | `0x006E0070` | 124 | von Hand geprüft |

4 von 6 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006E0020`), `~AgcmArchlord` (`0x006E00F0`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-ID `0x24` ist die im Dekompilat sichtbare Zahl für `APDEVENT_FUNCTION_ARCHLORD`; sie wurde nicht in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmArchlord`](AgpmArchlord.md), [`AgpmCharacter`](AgpmCharacter.md)
- **Erwähnt in:** [`AgcmUIArchlord`](AgcmUIArchlord.md)
