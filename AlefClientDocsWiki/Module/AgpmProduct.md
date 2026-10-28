# AgpmProduct (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmProduct` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmProduct` / `AgpmProduct.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0055FB60` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMPRODUCT_PACKET_OPERATION_*` kennt 4 Operationen, davon 4 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 4 Operationen liegen 2013er Ereignisse vor; 4 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0055f9b0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0055ECA0` | `AgpmProduct::ctor_or_dtor_0055eca0` | merged |
| `0x0055ED30` | `AgpmProduct::OnInit` | merged |
| `0x0055ED90` | `AgpmProduct::OnDestroy` | merged |
| `0x0055F270` | `AgpmProduct::~AgpmProduct` | merged |
| `0x0055F3E0` | `AgpmProduct::ConAgpdGatherCharacterTAD` | stage1 |
| `0x0055F4D0` | `AgpmProduct::ConAgpdGatherCharacterAD` | stage1 |
| `0x0055F520` | `AgpmProduct::DesAgpdGatherCharacterAD` | stage1 |
| `0x0055F580` | `AgpmProduct::ConAgpdComposeCharacterAD` | stage1 |
| `0x0055F5D0` | `AgpmProduct::DesAgpdComposeCharacterAD` | stage1 |
| `0x0055F9B0` | `AgpmProduct::ctor_or_dtor_0055f9b0` | merged |
| `0x0055FB60` | `AgpmProduct::OnReceive` | merged |
| `0x0055FD30` | `AgpmProduct::CBResetMonster` | stage1 |
| `0x0055FF80` | `AgpmProduct::OnAddModule` | merged |
| `0x0055F0F0` | `AgpmProduct::OnOperationCompose` | casemap:AgpmProduct |
| `0x0055F1B0` | `AgpmProduct::OnOperationGather` | casemap:AgpmProduct |
| `0x0055F900` | `AgpmProduct::OnOperationComposeInfo` | casemap:AgpmProduct |

16 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 8/8/8 | ja | ja |

**m_csPacket** (8 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | CID |
| 2 | `0x4` | INT32 | 1 | Skill ID |
| 3 | `0x8` | INT32 | 1 | Item TID/Target ID |
| 4 | `0x10` | INT32 | 1 | Receipe ID |
| 5 | `0x20` | INT32 | 1 | Result |
| 6 | `0x40` | INT32 | 1 | Result Exp. |
| 7 | `0x80` | MEMORY_BLOCK | 1 | Compose Info |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `COMPOSE` | `0x0055F0F0` `OnOperationCompose` | `COMPOSE` | = (2013 = 2017) |
| 1 | `COMPOSE_INFO` | `0x0055F900` `OnOperationComposeInfo` | `COMPOSE_INFO` | = (2013 = 2017) |
| 2 | `GATHER` | `0x0055F1B0` `OnOperationGather` | `GATHER` | = (2013 = 2017) |
| 3 | `RESULT` | inline | `RESULT` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 8, gemeinsamer Rumpf: 5, nicht im Client: 8, ohne Kandidat: 10, zugeordnet: 8.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetExpOfCurrLevel` | 22 | `0x0055F000` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckTargetStatus` | 23 | `0x0055EFB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsComposeSkill` | 12 | `0x0055F390` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetMaxExpOfCurrLevel` | 15 | `0x0055F090` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidItemStatus` | 37 | `0x0055EEF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetComposeList` | 16 | `0x0055EE50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsValidStatus` | 41 | `0x0055FE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsValidStatus` | 41 | `0x0055FD60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `InitGatherData` (`0x0055F430`), `InitComposeData` (`0x0055F480`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmProduct`](AgcmProduct.md), [`AgcmProductMed`](AgcmProductMed.md), [`AgcmUIProduct`](AgcmUIProduct.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md)
