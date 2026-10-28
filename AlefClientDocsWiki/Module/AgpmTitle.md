# AgpmTitle (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmTitle` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmTitle` / `AgpmTitle.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00568FD0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMTITLE_PACKET_OPERATION_TITLE_*` kennt 11 Operationen, davon 11 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 11 Operationen liegen 2013er Ereignisse vor; 11 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 0 Paketdefinition(en) in der Quelle, 0 davon im 2017er Konstruktor (`None`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00568310` | `AgpmTitle::OnInit` | merged |
| `0x005683F0` | `AgpmTitle::OnDestroy` | merged |
| `0x00568FD0` | `AgpmTitle::OnReceive` | merged |
| `0x00569120` | `AgpmTitle::ctor_or_dtor_00569120` | merged |
| `0x00569200` | `AgpmTitle::ctor_or_dtor_00569200` | merged |
| `0x005692C0` | `AgpmTitle::~AgpmTitle` | merged |
| `0x00568490` | `AgpmTitle::OnOperationTitleUseNear` | casemap:AgpmTitle |
| `0x005684C0` | `AgpmTitle::OnOperationTitleAddResult` | casemap:AgpmTitle |
| `0x00568530` | `AgpmTitle::OnOperationTitleListResult` | casemap:AgpmTitle |
| `0x00568620` | `AgpmTitle::OnOperationTitleDeleteResult` | casemap:AgpmTitle |
| `0x00568A00` | `AgpmTitle::OnOperationTitleUseResult` | casemap:AgpmTitle |
| `0x00568EF0` | `AgpmTitle::OnOperationTitleQuest` | casemap:AgpmTitle |

12 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | inline | `TITLE_ADD` | = (2013 = 2017) |
| 1 | `ADD_RESUILT` | `0x005684C0` `OnOperationTitleAddResult` | `TITLE_ADD_RESULT` | = (2013 = 2017) |
| 2 | `USE` | inline | `TITLE_USE` | = (2013 = 2017) |
| 3 | `USE_RESULT` | `0x00568A00` `OnOperationTitleUseResult` | `TITLE_USE_RESULT` | = (2013 = 2017) |
| 4 | `LIST` | inline | `TITLE_LIST` | = (2013 = 2017) |
| 5 | `LIST_RESULT` | `0x00568530` `OnOperationTitleListResult` | `TITLE_LIST_RESULT` | = (2013 = 2017) |
| 6 | `QUEST` | `0x00568EF0` `OnOperationTitleQuest` | `TITLE_QUEST_CHECK`, `TITLE_QUEST_CHECK_RESULT`, `TITLE_QUEST_COMPLETE`, `TITLE_QUEST_COMPLETE_RESULT`, `TITLE_QUEST_LIST`, `TITLE_QUEST_LIST_RESULT` … (8) | = (2013 = 2017) |
| 7 | `DELETE` | inline | `TITLE_DELETE` | = (2013 = 2017) |
| 8 | `DELETE_RESULT` | `0x00568620` `OnOperationTitleDeleteResult` | `TITLE_DELETE_RESULT` | = (2013 = 2017) |
| 9 | `USE_NEAR` | `0x00568490` `OnOperationTitleUseNear` | `TITLE_USE_NEAR` | = (2013 = 2017) |
| 10 | `UI_OPEN` | inline | `TITLE_UI_OPEN` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 11, gemeinsamer Rumpf: 1, nicht im Client: 15, ohne Kandidat: 15, zugeordnet: 4.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `CheckItemCount` | 20 | `0x00568830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SatisfyTitleQuestCompleteCondition` | 16 | `0x00568780` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsGuildMaster` | 9 | `0x005687E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxTitleTemplate` | 7 | `0x00568450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmTitle`](AgcmTitle.md)
