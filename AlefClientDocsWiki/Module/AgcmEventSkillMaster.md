# AgcmEventSkillMaster (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventSkillMaster` (Fertigkeitenmeister: Ereignis, Lernen, Aufwerten, Zurücksetzen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, drei Rückrufe und vier der fünf Sendefunktionen zugeordnet; `SendBuySkillBook` ist im Binary nicht vorhanden (nicht aufgerufen, vom Linker entfernt).
- **Sendefunktionen** über das Operationsbyte im Paketbauer: `SendRequestEvent` `0x006DE640` (Operation 4 = `REQUEST_EVENT`), `SendLearnSkill` `0x006DE6C0` (1 = `LEARN_SKILL`), `SendRequestSkillUpgrade` `0x006DE750` (2 = `REQUEST_UPGRADE`), `SendRequestSkillInitialize` `0x006DE7F0` (8 = `SKILL_INITIALIZE`); die Zahlen stimmen mit `AGPMEVENT_SKILL_OPERATION_…` überein.
- **OnAddModule:** sechs Module ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventSkillMaster`](AgpmEventSkillMaster.md), `AgcmCharacter`, [`AgcmItem`](AgcmItem.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmEventManager`](AgcmEventManager.md)); Anmeldungen: Ereignis `0x19` → `CBExecuteEvent` (`0x006DE940`), `CBResponseSkillUpgrade` (`0x006DE870`), `CBResponseEvent` (`0x006DE8E0`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventSkillMaster.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DE9D0` | 209 | vtable/String |
| 1 | `SendRequestEvent` | `0x006DE640` | 125 | von Hand geprüft |
| 2 | `SendBuySkillBook` | – | | keine Funktion im Binary, die Operation 0 sendet (nicht aufgerufen, vom Linker entfernt) |
| 3 | `SendLearnSkill` | `0x006DE6C0` | 134 | von Hand geprüft |
| 4 | `SendRequestSkillUpgrade` | `0x006DE750` | 146 | von Hand geprüft |
| 5 | `SendRequestSkillInitialize` | `0x006DE7F0` | 125 | von Hand geprüft |
| 6 | `CBResponseSkillUpgrade` | `0x006DE870` | 99 | Callback-Registrierung |
| 7 | `CBResponseEvent` | `0x006DE8E0` | 96 | Callback-Registrierung |
| 8 | `CBExecuteEvent` | `0x006DE940` | 96 | Callback-Registrierung |
| 9 | `SetCallbackResultSkillUpgrade` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 10 | `SetCallbackResponseGrant` | – | | Einzeiler (`SetCallback`), zusammengefaltet |

8 von 11 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DE5D0`), `~AgcmEventSkillMaster` (`0x006DE9A0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger auf `AgpmCharacter`` | `OnAddModule` |
| `this+0xB9C` | `Zeiger auf `AgpmEventSkillMaster`` | `OnAddModule` |
| `this+0xBA0` | `Zeiger auf `AgcmCharacter`` | `OnAddModule`, Sendefunktionen |
| `this+0xBA4` | `Zeiger auf `AgcmItem`` | `OnAddModule` |
| `this+0xBA8` | `Zeiger auf `AgcmSkill`` | `OnAddModule` |
| `this+0xBAC` | `Zeiger auf `AgcmEventManager`` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- `SendBuySkillBook` ist in der Quelle vorhanden, im 2017er Binary aber nicht (kein Aufrufer, entfernt).

## Grenzen

- Die Ereignis-ID `0x19` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgcmItem`](AgcmItem.md), [`AgcmSkill`](AgcmSkill.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventSkillMaster`](AgpmEventSkillMaster.md)
- **Erwähnt in:** [`AgcmCashMall`](AgcmCashMall.md)
