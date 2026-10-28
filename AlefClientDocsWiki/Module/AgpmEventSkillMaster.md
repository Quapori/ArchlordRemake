# AgpmEventSkillMaster (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventSkillMaster` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventSkillMaster` / `AgpmEventSkillMaster.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00572030` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMEVENT_SKILL_OPERATION_*` kennt 10 Operationen, davon 10 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 10 Operationen liegen 2013er Ereignisse vor; 9 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 1 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`00573f10`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0052BDE0` | `AgpmEventSkillMaster::CBStreamWriteEvent` | stage1 |
| `0x0052BE70` | `AgpmEventSkillMaster::CBStreamReadEvent` | stage1 |
| `0x00570B60` | `AgpmEventSkillMaster::CBActionSkillMaster` | stage1 |
| `0x00570DD0` | `AgpmEventSkillMaster::CBCharTemplateDestructor` | stage1 |
| `0x00570E20` | `AgpmEventSkillMaster::CBEventConstructor` | stage1 |
| `0x00570EB0` | `AgpmEventSkillMaster::CBMakePacketEventData` | stage1 |
| `0x00570EE0` | `AgpmEventSkillMaster::CBParsePacketEventData` | stage1 |
| `0x00570F10` | `AgpmEventSkillMaster::CBCheckJoinItem` | stage1 |
| `0x00571880` | `AgpmEventSkillMaster::CBSetConstFactor` | stage1 |
| `0x005719A0` | `AgpmEventSkillMaster::CBGetInputTotalCostSP` | stage1 |
| `0x005719D0` | `AgpmEventSkillMaster::CBGetInputTotalCostHeroicPoint` | stage1 |
| `0x00572030` | `AgpmEventSkillMaster::OnReceive` | merged |
| `0x005739A0` | `AgpmEventSkillMaster::CBRollbackSkill` | stage1 |
| `0x00573AA0` | `AgpmEventSkillMaster::OnAddModule` | merged |
| `0x00574110` | `AgpmEventSkillMaster::~AgpmEventSkillMaster` | merged |
| `0x00570640` | `AgpmEventSkillMaster::OnOperationBuySkillBook` | casemap:AgpmEventSkillMaster |
| `0x00570690` | `AgpmEventSkillMaster::OnOperationLearnSkill` | casemap:AgpmEventSkillMaster |
| `0x005706E0` | `AgpmEventSkillMaster::OnOperationBuySkillResult` | casemap:AgpmEventSkillMaster |
| `0x00570700` | `AgpmEventSkillMaster::OnOperationRequestUpgrade` | casemap:AgpmEventSkillMaster |
| `0x00570750` | `AgpmEventSkillMaster::OnOperationResponseUpgrade` | casemap:AgpmEventSkillMaster |
| `0x005707A0` | `AgpmEventSkillMaster::OnOperationResponseEvent` | casemap:AgpmEventSkillMaster |
| `0x005707F0` | `AgpmEventSkillMaster::OnOperationLearnResult` | casemap:AgpmEventSkillMaster |
| `0x00571130` | `AgpmEventSkillMaster::OnOperationRequestEvent` | casemap:AgpmEventSkillMaster |
| `0x00571E60` | `AgpmEventSkillMaster::OnOperationSkillInitialize` | casemap:AgpmEventSkillMaster |

24 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 8/8/8 | ja | ja |
| `m_csPacketEventData` | 1/1/1 | 2/2/2 | ja | ja |

**m_csPacket** (8 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | PACKET | 1 | event base packet |
| 2 | `0x4` | INT32 | 1 | Character ID |
| 3 | `0x8` | INT32 | 1 | Skill ID |
| 4 | `0x10` | INT32 | 1 | Skill TID |
| 5 | `0x20` | INT8 | 1 | Operation Result |
| 6 | `0x40` | INT8 | 1 | skill point |
| 7 | `0x80` | INT8 | 1 |    |

**m_csPacketEventData** (2 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | race type |
| 1 | `0x2` | INT8 | 1 | class type |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `BUY_SKILL_BOOK` | `0x00570640` `OnOperationBuySkillBook` | `BUY_SKILL_BOOK` | = (2013 = 2017) |
| 1 | `LEARN_SKILL` | `0x00570690` `OnOperationLearnSkill` | `LEARN_SKILL` | = (2013 = 2017) |
| 2 | `REQUEST_UPGRADE` | `0x00570700` `OnOperationRequestUpgrade` | `REQUEST_UPGRADE` | = (2013 = 2017) |
| 3 | `RESPONSE_UPGRADE` | `0x00570750` `OnOperationResponseUpgrade` | `RESPONSE_UPGRADE` | = (2013 = 2017) |
| 4 | `REQUEST_EVENT` | `0x00571130` `OnOperationRequestEvent` | `REQUEST_EVENT` | = (2013 = 2017) |
| 5 | `RESPONSE_EVENT` | `0x005707A0` `OnOperationResponseEvent` | `RESPONSE_EVENT` | = (2013 = 2017) |
| 6 | `LEARN_RESULT` | `0x005707F0` `OnOperationLearnResult` | `LEARN_RESULT` | = (2013 = 2017) |
| 7 | `BUY_RESULT` | `0x005706E0` `OnOperationBuySkillResult` | `BUY_RESULT` | = (2013 = 2017) |
| 8 | `SKILL_INITIALIZE` | `0x00571E60` `OnOperationSkillInitialize` | `15`, `16`, `END_ALL_SKILL`, `REMOVE_SKILL`, `SAVE_ALL_DATA`, `SKILL_INITIALIZE` … (7) | 2017 ⊃ 2013 |
| 9 | `SKILL_INITIALIZE_RESULT` | `0x00570810` `FUN_00570810` | `SKILL_INITIALIZE_RESULT` | = (2013 = 2017) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 8 | `SKILL_INITIALIZE` | – | 15, 16, AGPMEVENT_SKILL_CB_SKILL_INIT_LOG |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 7, eingebaut: 11, gemeinsamer Rumpf: 15, nicht im Client: 15, ohne Kandidat: 8, zugeordnet: 47.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsUpgradable` | 5 | `0x00571800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetLearnableLevel` | 2 | `0x00570D50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckConditionC` | 64 | `0x005726D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckConditionAB` | 35 | `0x00572610` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckSkillCondition` | 12 | `0x00573400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckHeroicSkillForClass` | 12 | `0x00572DC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHeroicSkillVector` | 9 | `0x00572A90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckConditionD` | 46 | `0x00572910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharacterRaceID` | 23 | `0x00570F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckHighLevelSkillForRollback` | 17 | `0x00573830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckHeroicConditionD` | 29 | `0x00572CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHeroicSkillInfo` | 38 | `0x00572AD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillIndex` | 30 | `0x00572500` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillInfoByIndex` | 15 | `0x00572450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillInfo` | 40 | `0x00572360` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillVector` | 9 | `0x00572320` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSkillAttachTemplateData` | 5 | `0x00570DA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharTID` | 57 | `0x00570C20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnHeroicSkill` | 81 | `0x00572FC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnHighLevelSkill` | 86 | `0x00572E10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUpgradeHeroicSkill` | 72 | `0x005732A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUpgradeHighLevelSkill` | 70 | `0x00573130` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnSkill` | 64 | `0x00573550` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckTargetSkillForRollback` | 32 | `0x00573890` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetMasteryIndex` | 10 | `0x00571830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsFullUpgrade` | 11 | `0x00571770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInputTotalCharismaPoint` | 23 | `0x005716E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInputTotalCostHeroicPoint` | 23 | `0x00571620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInputTotalCostSP` | 21 | `0x00571570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUpgradeCostSP` | 17 | `0x00571400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetOwnSkillCount` | 36 | `0x00571F00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUpgradeSkill` | 69 | `0x005736B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketBuySkill` | 26 | `0x00575910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUpgradeCostCharismaPoint` | 19 | `0x005714F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUpgradeCostHeroicPoint` | 19 | `0x00571470` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckValidRange` | 5 | `0x0055A100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTotalCharismaPointByLearnSkill` | 22 | `0x00571B30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetSkillAttachCharTemplateData` | 5 | `0x00571A00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InitializeSkillTree` | 96 | `0x00571B90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBuyCost` | 2 | `0x00571220` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParseEventDataPacket` | 17 | `0x00570AC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventData` | 12 | `0x00570A70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestSkillInitialize` | 16 | `0x00570A20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestEvent` | 25 | `0x00570990` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestUpgrade` | 28 | `0x005708D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketLearnSkill` | 26 | `0x0056FFB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUpgradeCost` | 30 | `0x00571350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `CheckCharacterStatus` (`0x00570B20`), `GetBuyCost` (`0x00563210`), `GetLearnCostHeroicPoint` (`0x005712F0`), `GetLearnCostCharismaPoint` (`0x005712F0`), `IsUpgradable` (`0x00570D70`), `GetTotalLearnCost` (`0x0052CB30`), `CheckHeroicSkillCondition` (`0x00573450`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md)
