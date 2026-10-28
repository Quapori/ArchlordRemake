# AgcmEventBank (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventBank` (Bank-NPC-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule` und die drei Ereignis-Rückrufe sind zugeordnet; `SetCallbackGrantEventBank` ist ein zusammengefalteter Einzeiler.
- **OnAddModule:** vier Module ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventBank`](AgpmEventBank.md), [`AgcmEventManager`](AgcmEventManager.md), `AgcmCharacter`) in `this+0xB98/0xB9C/0xBA4/0xBA0`; Rückrufe: `RegisterEventCallback(0x14)` → `CBEventBank` (`0x006DF2D0`), `AgpmEventBank` Grant → `CBEventGrant` (`0x006DF370`), Grant-Anywhere → `CBEventGrantAnywhere` (`0x006DF3B0`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventBank.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DF420` | 172 | vtable/String |
| 1 | `CBEventBank` | `0x006DF2D0` | 151 | Callback-Registrierung |
| 2 | `CBEventGrant` | `0x006DF370` | 64 | Callback-Registrierung |
| 3 | `CBEventGrantAnywhere` | `0x006DF3B0` | 49 | Callback-Registrierung |
| 4 | `SetCallbackGrantEventBank` | – | | Einzeiler (`SetCallback`), zusammengefaltet |

4 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DF260`), `~AgcmEventBank` (`0x006DF3F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger auf `AgpmCharacter`` | `OnAddModule` |
| `this+0xB9C` | `Zeiger auf `AgpmEventBank`` | `OnAddModule` |
| `this+0xBA0` | `Zeiger auf `AgcmCharacter`` | `OnAddModule` |
| `this+0xBA4` | `Zeiger auf `AgcmEventManager`` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle.

## Grenzen

- Die Ereignis-ID `0x14` ist die im Dekompilat sichtbare Zahl für `APDEVENT_FUNCTION_BANK`; der Aufzählungswert wurde nicht in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventBank`](AgpmEventBank.md)
- **Erwähnt in:** [`AgcmUIEventBank`](AgcmUIEventBank.md)
