# AgcmEventGuild (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventGuild` (Gilden-, Lager- und Weltmeisterschafts-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule` und sechs der sieben Rückrufe sind zugeordnet; `CBEventGrantWorldChampionship` ist in der Quelle definiert, wird aber nirgends angemeldet und fehlt im Binary.
- **OnAddModule:** vier Module ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventGuild`](AgpmEventGuild.md), `AgcmCharacter`, [`AgcmEventManager`](AgcmEventManager.md)); Anmeldungen: Ereignis `0x17` → `CBEventRequest` (`0x006DECD0`), Grant → `CBEventGrant` (`0x006DED70`), Ereignis `0x23` → `CBEventRequestWarehouse` (`0x006DEDB0`), Grant-Warehouse → `CBEventGrantWarehouse` (`0x006DEE50`), Ereignis `0x27` → `CBEventRequestWorldChampionship` (`0x006DEE90`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventGuild.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DEF60` | 223 | vtable/String |
| 1 | `SetCallbackGrant` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 2 | `SetCallbackGrantWarehouse` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 3 | `CBEventRequest` | `0x006DECD0` | 151 | Callback-Registrierung |
| 4 | `CBEventGrant` | `0x006DED70` | 64 | Callback-Registrierung |
| 5 | `CBEventRequestWarehouse` | `0x006DEDB0` | 151 | Callback-Registrierung |
| 6 | `CBEventGrantWarehouse` | `0x006DEE50` | 64 | Callback-Registrierung |
| 7 | `CBEventRequestWorldChampionship` | `0x006DEE90` | 152 | Callback-Registrierung |
| 8 | `CBEventGrantWorldChampionship` | – | | in der Quelle nicht angemeldet, im Binary keine Funktion |

6 von 9 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DEC60`), `~AgcmEventGuild` (`0x006DEF30`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger auf `AgpmCharacter`` | `OnAddModule` |
| `this+0xB9C` | `Zeiger auf `AgpmEventGuild`` | `OnAddModule` |
| `this+0xBA0` | `Zeiger auf `AgcmCharacter`` | `OnAddModule` |
| `this+0xBA4` | `Zeiger auf `AgcmEventManager`` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-IDs `0x17`, `0x23`, `0x27` sind die im Dekompilat sichtbaren Zahlen; sie wurden nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2, nicht als eigene Funktion: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventGuild`](AgpmEventGuild.md)
