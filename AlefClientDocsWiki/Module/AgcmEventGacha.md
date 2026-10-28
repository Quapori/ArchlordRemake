# AgcmEventGacha (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventGacha` (Gacha-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle Rückrufe und `OnAddModule` zugeordnet; `OnLuaInitialize` hat in der Quelle nur auskommentierten Inhalt und fehlt im Binary.
- **OnAddModule:** holt [`AgcmEventManager`](AgcmEventManager.md) und [`AgpmEventGacha`](AgpmEventGacha.md) (Zeiger in einer globalen Variable `DAT_00C23B7C`), registriert `RegisterEventCallback(0x26)` → `CBEventRequest` (`0x006809F0`) und zwei Rückrufe bei `AgpmEventGacha` (Grant `0x00680AD0`, Result `0x00680B10`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventGacha.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnLuaInitialize` | – | | Quelle: Inhalt auskommentiert, im Binary keine Funktion |
| 1 | `OnAddModule` | `0x00680B60` | 111 | vtable/String |
| 2 | `CBEventRequest` | `0x006809F0` | 211 | Callback-Registrierung |
| 3 | `CBEventGrant` | `0x00680AD0` | 53 | Callback-Registrierung |
| 4 | `CBEventResult` | `0x00680B10` | 29 | Callback-Registrierung |

4 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006809A0`), `~AgcmEventGacha` (`0x00680B30`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `DAT_00C23B7C` | `Zeiger auf `AgpmEventGacha` (globale Variable)` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle.

## Grenzen

- `OnLuaInitialize` (Quelle: Inhalt in `/* */`) ist im Binary nicht vorhanden.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmEventGacha`](AgpmEventGacha.md)
- **Erwähnt in:** [`AgcmUIEventGacha`](AgcmUIEventGacha.md), [`AgpmBattleGround`](AgpmBattleGround.md)
