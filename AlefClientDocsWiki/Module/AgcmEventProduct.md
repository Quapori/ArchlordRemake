# AgcmEventProduct (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventProduct` (Herstellungs-NPC-Ereignis (Fertigkeit lernen, Rezept kaufen)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, beide Rückrufe und beide Sendefunktionen zugeordnet; `SetCallbackGrant` ist ein zusammengefalteter Einzeiler.
- **OnAddModule:** 4 Module in der Reihenfolge der Quelle ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventProduct`](AgpmEventProduct.md), `AgcmCharacter`, [`AgcmEventManager`](AgcmEventManager.md)); Anmeldungen: Ereignis `0x18` → `CBEventRequest` (`0x006DE300`), Grant → `CBEventGrant` (`0x006DE3A0`).
- **Sendefunktionen** über das Operationsbyte im Paketbauer: `SendLearnSkill` `0x006DE3E0` (Operation 2 = `LEARN_SKILL`, Bauer `0x0056FFB0`) und `SendBuyCompose` `0x006DE470` (4 = `BUY_COMPOSE`, Bauer `0x0056FF30`); beide Zahlen stimmen mit `AGPMEVENT_PRODUCT_PACKET_…` überein.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventProduct.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DE530` | 152 | vtable/String |
| 1 | `SetCallbackGrant` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 2 | `CBEventRequest` | `0x006DE300` | 151 | Callback-Registrierung |
| 3 | `CBEventGrant` | `0x006DE3A0` | 64 | Callback-Registrierung |
| 4 | `SendLearnSkill` | `0x006DE3E0` | 130 | von Hand geprüft |
| 5 | `SendBuyCompose` | `0x006DE470` | 130 | von Hand geprüft |

5 von 6 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DE2B0`), `~AgcmEventProduct` (`0x006DE500`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-ID `0x18` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventProduct`](AgpmEventProduct.md)
- **Erwähnt in:** [`AgcmUIProduct`](AgcmUIProduct.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md)
