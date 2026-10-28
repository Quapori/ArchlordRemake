# AgcmEventCharCustomize (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventCharCustomize` (Aussehen-ändern-NPC-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule` und beide Rückrufe zugeordnet; `SetCallbackGrantEvent` ist ein zusammengefalteter Einzeiler.
- **OnAddModule:** 4 Module in der Reihenfolge der Quelle ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventCharCustomize`](AgpmEventCharCustomize.md), `AgcmCharacter`, [`AgcmEventManager`](AgcmEventManager.md)); Anmeldungen: Ereignis `0x1D` → `CBEventCharCustomize` (`0x00683980`), Grant → `CBEventGrant` (`0x00683940`, über `0x006DA540` angemeldet).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventCharCustomize.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00683A50` | 152 | vtable/String |
| 1 | `CBEventGrant` | `0x00683940` | 59 | Callback-Registrierung |
| 2 | `CBEventCharCustomize` | `0x00683980` | 151 | Callback-Registrierung |
| 3 | `SetCallbackGrantEvent` | – | | Einzeiler (`SetCallback`), zusammengefaltet |

3 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006838F0`), `~AgcmEventCharCustomize` (`0x00683A20`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-ID `0x1d` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventCharCustomize`](AgpmEventCharCustomize.md)
- **Erwähnt in:** [`AgcmUICustomizing`](AgcmUICustomizing.md)
