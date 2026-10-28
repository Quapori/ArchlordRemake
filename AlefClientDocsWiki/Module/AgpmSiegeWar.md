# AgpmSiegeWar (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmSiegeWar` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmSiegeWar` / `AgpmSiegeWar.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00523670` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMSIEGE_OPERATION_*` kennt 30 Operationen, davon 30 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 27 Operationen liegen 2013er Ereignisse vor; 27 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 7 Paketdefinition(en) in der Quelle, 7 davon im 2017er Konstruktor (`00524170`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0051F080` | `AgpmSiegeWar::CharacterImportDataReadCB` | stage1 |
| `0x0051F120` | `AgpmSiegeWar::CBCheckDestroy` | stage1 |
| `0x0051F250` | `AgpmSiegeWar::CBDestroyGuild` | stage1 |
| `0x005202E0` | `AgpmSiegeWar::DesCharAttachData` | stage1 |
| `0x00520700` | `AgpmSiegeWar::CBInitCharacter` | stage1 |
| `0x00520790` | `AgpmSiegeWar::CBCheckNPCAttackableTarget` | stage1 |
| `0x00520A10` | `AgpmSiegeWar::CBIsInSiegeWarIngArea` | stage1 |
| `0x00522720` | `AgpmSiegeWar::CBIsStaticCharacter` | stage1 |
| `0x00522750` | `AgpmSiegeWar::CBIsAttackableTime` | stage1 |
| `0x00523420` | `AgpmSiegeWar::OnAddModule` | merged |
| `0x00523670` | `AgpmSiegeWar::OnReceive` | merged |
| `0x00523D10` | `AgpmSiegeWar::ctor_or_dtor_00523d10` | merged |
| `0x00523E10` | `AgpmSiegeWar::~AgpmSiegeWar` | merged |
| `0x00524170` | `AgpmSiegeWar::ctor_or_dtor_00524170` | merged |
| `0x0051F350` | `AgpmSiegeWar::OnOperationAttackApplGuildList` | casemap:AgpmSiegeWar |
| `0x0051F3E0` | `AgpmSiegeWar::OnOperationDefenseApplGuildList` | casemap:AgpmSiegeWar |
| `0x0051F470` | `AgpmSiegeWar::OnOperationRequestOpenAttackObject` | casemap:AgpmSiegeWar |
| `0x0051F4F0` | `AgpmSiegeWar::OnOperationRequestUseAttackObject` | casemap:AgpmSiegeWar |
| `0x0051F570` | `AgpmSiegeWar::OnOperationRequestRepairAttackObject` | casemap:AgpmSiegeWar |
| `0x0051F5F0` | `AgpmSiegeWar::OnOperationResponseRepairAttackObject` | casemap:AgpmSiegeWar |
| `0x0051F640` | `AgpmSiegeWar::OnOperationAddItemResult` | casemap:AgpmSiegeWar |
| `0x0051F780` | `AgpmSiegeWar::OnOperationCarveASeal` | casemap:AgpmSiegeWar |
| `0x0051F800` | `AgpmSiegeWar::OnOperationStatusInfo` | casemap:AgpmSiegeWar |
| `0x00520A90` | `AgpmSiegeWar::OnOperationDefenseApplication` | casemap:AgpmSiegeWar |
| `0x00520B40` | `AgpmSiegeWar::OnOperationCancelDefenseApplication` | casemap:AgpmSiegeWar |
| `0x00520BF0` | `AgpmSiegeWar::OnOperationAttackApplication` | casemap:AgpmSiegeWar |
| `0x00520CA0` | `AgpmSiegeWar::OnOperationCancelAttackApplication` | casemap:AgpmSiegeWar |
| `0x00520D50` | `AgpmSiegeWar::OnOperationRequestAttackApplGuildList` | casemap:AgpmSiegeWar |
| `0x00520E30` | `AgpmSiegeWar::OnOperationRequestDefenseApplGuildList` | casemap:AgpmSiegeWar |
| `0x00520F00` | `AgpmSiegeWar::OnOperationResult` | casemap:AgpmSiegeWar |
| `0x00520F40` | `AgpmSiegeWar::OnOperationRequestAttackGuildList` | casemap:AgpmSiegeWar |
| `0x00520FB0` | `AgpmSiegeWar::OnOperationRequestDefenseGuildList` | casemap:AgpmSiegeWar |
| `0x00521020` | `AgpmSiegeWar::OnOperationAttackGuildList` | casemap:AgpmSiegeWar |
| `0x005211A0` | `AgpmSiegeWar::OnOperationDefenseGuildList` | casemap:AgpmSiegeWar |
| `0x00521320` | `AgpmSiegeWar::OnOperationRemoveItemToAttackObject` | casemap:AgpmSiegeWar |
| `0x005227A0` | `AgpmSiegeWar::OnOperationUpdate` | casemap:AgpmSiegeWar |
| `0x00522AF0` | `AgpmSiegeWar::OnOperationSetNextSiegeWarTime` | casemap:AgpmSiegeWar |
| `0x00522CB0` | `AgpmSiegeWar::OnOperationSelectDefenseGuild` | casemap:AgpmSiegeWar |
| `0x00522EC0` | `AgpmSiegeWar::OnOperationUpdateAttackObject` | casemap:AgpmSiegeWar |
| `0x00523090` | `AgpmSiegeWar::OnOperationResponseOpenAttackObject` | casemap:AgpmSiegeWar |
| `0x005230F0` | `AgpmSiegeWar::OnOperationResponseUseAttackObject` | casemap:AgpmSiegeWar |
| `0x00523150` | `AgpmSiegeWar::OnOperationAddItemToAttackObject` | casemap:AgpmSiegeWar |

42 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 11/11/11 | ja | ja |
| `m_csPacketCastleInfo` | 2/2/2 | 11/11/11 | ja | ja |
| `m_csPacketGuildList` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketGuildInfo` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketAttackObjectInfo` | 2/2/2 | 14/14/14 | ja | ja |
| `m_csPacketStatusInfo` | 1/1/1 | 7/7/7 | ja | ja |
| `m_csPacketSyncMessage` | 1/1/1 | 5/5/5 | ja | ja |

**m_csPacket** (11 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | packet operation |
| 1 | `0x2` | INT8 | 1 | result |
| 2 | `0x4` | PACKET | 1 | castle information packet |
| 3 | `0x8` | INT32 | 1 | operator cid |
| 4 | `0x10` | PACKET | 1 | guild list packet |
| 5 | `0x20` | INT32 | 1 | target cid |
| 6 | `0x40` | PACKET | 1 | attack object information packet |
| 7 | `0x80` | INT32 | 1 | item id |
| 8 | `0x100` | PACKET | 1 | status information packet |
| 9 | `0x200` | UINT32 | 1 | current time stamp : AuTimeStamp::GetCurrentTimeStamp() |
| 10 | `0x400` | PACKET | 1 | sync message |

**m_csPacketCastleInfo** (11 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | MEMORY_BLOCK | 1 |  |
| 1 | `0x2` | MEMORY_BLOCK | 1 |  |
| 2 | `0x4` | MEMORY_BLOCK | 1 |   |
| 3 | `0x8` | UINT8 | 1 |   |
| 4 | `0x10` | UINT64 | 1 |     |
| 5 | `0x20` | UINT64 | 1 |    |
| 6 | `0x40` | UINT8 | 1 |   |
| 7 | `0x80` | UINT8 | 1 |     |
| 8 | `0x100` | UINT8 | 1 |     |
| 9 | `0x200` | UINT8 | 1 | /  () |
| 10 | `0x400` | MEMORY_BLOCK | 1 |   |

**m_csPacketGuildList** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT16 | 1 | page  |
| 1 | `0x2` | INT16 | 1 | total page  |
| 2 | `0x4` | PACKET | AGPMSIEGEWAR_MAX_GUILD_LIST_PER_PAGE |    |

**m_csPacketGuildInfo** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | MEMORY_BLOCK | 1 |   |
| 1 | `0x2` | MEMORY_BLOCK | 1 |   |
| 2 | `0x4` | UINT32 | 1 |   |

**m_csPacketAttackObjectInfo** (14 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | UINT8 | 1 |  |
| 1 | `0x2` | INT32 | 1 |  |
| 2 | `0x4` | UINT8 | 1 |  () |
| 3 | `0x8` | UINT8 | 1 |   |
| 4 | `0x10` | INT32 | 1 | 1 |
| 5 | `0x20` | INT32 | 1 | 2 |
| 6 | `0x40` | INT32 | 1 | 3 |
| 7 | `0x80` | INT32 | 1 | 4 |
| 8 | `0x100` | INT32 | 1 | 5 |
| 9 | `0x200` | INT32 | 1 | 6 |
| 10 | `0x400` | INT32 | 1 | 7 |
| 11 | `0x800` | INT32 | 1 | 8 |
| 12 | `0x1000` | UINT8 | 1 |    () |
| 13 | `0x2000` | MEMORY_BLOCK | 1 |     |

**m_csPacketStatusInfo** (7 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | UINT8 | 1 | information type |
| 1 | `0x2` | MEMORY_BLOCK | 1 |  |
| 2 | `0x4` | MEMORY_BLOCK | 1 |  |
| 3 | `0x8` | MEMORY_BLOCK | 1 | ,   |
| 4 | `0x10` | UINT8 | 1 | Object type |
| 5 | `0x20` | UINT32 | 1 |  () |
| 6 | `0x40` | UINT8 | 1 |   |

**m_csPacketSyncMessage** (5 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | UINT8 | 1 | message type |
| 1 | `0x2` | UINT16 | 1 | time (second) |
| 2 | `0x4` | MEMORY_BLOCK | 1 |  |
| 3 | `0x8` | MEMORY_BLOCK | 1 |  |
| 4 | `0x10` | MEMORY_BLOCK | 1 | ,   |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `UPDATE` | `0x005227A0` `OnOperationUpdate` | `UPDATE_CASTLE_INFO` | = (2013 = 2017) |
| 1 | `SET_NEXT_SIEGEWAR_TIME` | `0x00522AF0` `OnOperationSetNextSiegeWarTime` | `SET_NEXT_SIEGEWAR_TIME` | = (2013 = 2017) |
| 2 | `RESULT` | `0x00520F00` `OnOperationResult` | `RECEIVE_RESULT` | = (2013 = 2017) |
| 3 | `DEFENSE_APPLICATION` | `0x00520A90` `OnOperationDefenseApplication` | `ADD_DEFENSE_APPLICATION` | = (2013 = 2017) |
| 4 | `CANCEL_DEFENSE_APPLICATION` | `0x00520B40` `OnOperationCancelDefenseApplication` | `REMOVE_DEFENSE_APPLICATION` | = (2013 = 2017) |
| 5 | `ATTACK_APPLICATION` | `0x00520BF0` `OnOperationAttackApplication` | `ADD_ATTACK_APPLICATION` | = (2013 = 2017) |
| 6 | `CANCEL_ATTACK_APPLICATION` | `0x00520CA0` `OnOperationCancelAttackApplication` | `REMOVE_ATTACK_APPLICATION` | = (2013 = 2017) |
| 7 | `REQUEST_ATTACK_APPL_GUILD_LIST` | `0x00520D50` `OnOperationRequestAttackApplGuildList` | `REQUEST_ATTACK_APPL_GUILD_LIST` | = (2013 = 2017) |
| 8 | `REQUEST_DEFENSE_APPL_GUILD_LIST` | `0x00520E30` `OnOperationRequestDefenseApplGuildList` | `REQUEST_DEFENSE_APPL_GUILD_LIST` | = (2013 = 2017) |
| 9 | `ATTACK_APPL_GUILD_LIST` | `0x0051F350` `OnOperationAttackApplGuildList` | `RECEIVE_ATTACK_APPL_GUILD_LIST` | = (2013 = 2017) |
| 10 | `DEFENSE_APPL_GUILD_LIST` | `0x0051F3E0` `OnOperationDefenseApplGuildList` | `RECEIVE_DEFENSE_APPL_GUILD_LIST` | = (2013 = 2017) |
| 11 | `SELECT_DEFENSE_GUILD` | `0x00522CB0` `OnOperationSelectDefenseGuild` | `ADD_DEFENSE_GUILD` | = (2013 = 2017) |
| 12 | `REQUEST_ATTACK_GUILD_LIST` | `0x00520F40` `OnOperationRequestAttackGuildList` | `REQUEST_ATTACK_GUILD_LIST` | = (2013 = 2017) |
| 13 | `REQUEST_DEFENSE_GUILD_LIST` | `0x00520FB0` `OnOperationRequestDefenseGuildList` | `REQUEST_DEFENSE_GUILD_LIST` | = (2013 = 2017) |
| 14 | `ATTACK_GUILD_LIST` | `0x00521020` `OnOperationAttackGuildList` | `RECEIVE_ATTACK_GUILD_LIST` | = (2013 = 2017) |
| 15 | `DEFENSE_GUILD_LIST` | `0x005211A0` `OnOperationDefenseGuildList` | `RECEIVE_DEFENSE_GUILD_LIST` | = (2013 = 2017) |
| 16 | `REQUEST_OPEN_ATTACK_OBJECT` | `0x0051F470` `OnOperationRequestOpenAttackObject` | `RECEIVE_OPEN_ATTACK_OBJECT` | = (2013 = 2017) |
| 17 | `RESPONSE_OPEN_ATTACK_OBJECT` | `0x00523090` `OnOperationResponseOpenAttackObject` | `RESPONSE_OPEN_ATTACK_OBJECT` | = (2013 = 2017) |
| 18 | `REQUEST_USE_ATTACK_OBJECT` | `0x0051F4F0` `OnOperationRequestUseAttackObject` | `RECEIVE_USE_ATTACK_OBJECT` | = (2013 = 2017) |
| 19 | `RESPONSE_USE_ATTACK_OBJECT` | `0x005230F0` `OnOperationResponseUseAttackObject` | `RESPONSE_USE_ATTACK_OBJECT` | = (2013 = 2017) |
| 20 | `REQUEST_REPAIR_ATTACK_OBJECT` | `0x0051F570` `OnOperationRequestRepairAttackObject` | `RECEIVE_REPAIR_ATTACK_OBJECT` | = (2013 = 2017) |
| 21 | `RESPONSE_REPAIR_ATTACK_OBJECT` | `0x0051F5F0` `OnOperationResponseRepairAttackObject` | `RESPONSE_REPAIR_ATTACK_OBJECT` | = (2013 = 2017) |
| 22 | `ADD_ITEM_TO_ATTACK_OBJECT` | `0x00523150` `OnOperationAddItemToAttackObject` | `ADD_ITEM_TO_ATTACK_OBJECT` | = (2013 = 2017) |
| 23 | `REMOVE_ITEM_TO_ATTACK_OBJECT` | `0x00521320` `OnOperationRemoveItemToAttackObject` | – | keine Callback-Ereignisse (beide) |
| 24 | `ADD_ITEM_RESULT` | `0x0051F640` `OnOperationAddItemResult` | `ADD_ITEM_RESULT` | = (2013 = 2017) |
| 25 | `AGPMSIEGE_OEPRATION_UPDATE_SIEGEWAR_STATUS` | inline | – | keine Callback-Ereignisse (beide) |
| 26 | `UPDATE_ATTACK_OBJECT` | `0x00522EC0` `OnOperationUpdateAttackObject` | – | keine Callback-Ereignisse (beide) |
| 27 | `CARVE_A_SEAL` | `0x0051F780` `OnOperationCarveASeal` | `CARVE_A_SEAL` | = (2013 = 2017) |
| 28 | `STATUS_INFO` | `0x0051F800` `OnOperationStatusInfo` | `STATUS_INFO` | = (2013 = 2017) |
| 29 | `MESSAGE` | `0x0051F820` `FUN_0051f820` | `SYNC_MESSAGE` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 11, eingebaut: 15, gemeinsamer Rumpf: 34, nicht im Client: 46, ohne Kandidat: 40, zugeordnet: 28.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetDurationMSec` | 6 | `0x00520170` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsCastleOwner` | 11 | `0x00521D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSiegeWarInfo` | 6 | `0x00520590` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckValidRepairAttackObject` | 41 | `0x00523320` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckValidUseAttackObject` | 41 | `0x005231D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckNeedItemForUse` | 32 | `0x00521490` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCarveASeal` | 20 | `0x0051FB80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRemoveItemToAttackObject` | 21 | `0x0051FB20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketAddItemToAttackObject` | 21 | `0x0051FAC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestRepairAttackObject` | 20 | `0x0051FA60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestUseAttackObject` | 20 | `0x0051FA00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestOpenAttackObject` | 20 | `0x0051F9A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketSelectDefenseGuild` | 40 | `0x00521C40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestDefenseGuildList` | 40 | `0x00521B70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestDefenseApplGuildList` | 46 | `0x00521A60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestAttackApplGuildList` | 46 | `0x00521950` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketAttackApplication` | 38 | `0x00521880` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCancelDefenseApplication` | 38 | `0x005217B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketDefenseApplication` | 38 | `0x005216E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketSetNextSiegeWarTime` | 38 | `0x00521610` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsGuildSiegeWarEntry` | 27 | `0x00520450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetAttachTemplateData` | 5 | `0x0051EEE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckCarveASeal` | 82 | `0x00521F00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsAttackGuild` | 18 | `0x0051FDA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsDefenseGuild` | 18 | `0x0051FD50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemToAttackObject` | 26 | `0x0051F840` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToAttackObject` | 44 | `0x005213A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetAttachCharacterData` | 5 | `0x0051EEB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetSiegeWarMonsterType` (`0x00521EB0`), `GetSiegeWarInfoIndex` (`0x005204C0`), `GetSiegeWarInfo` (`0x00521EB0`), `GetSiegeWarInfo` (`0x005205E0`), `GetNextSiegeWarFirstTime` (`0x0051FC70`), `GetFirstSiegeWarTime` (`0x0051FC70`), `IsOwnerGuild` (`0x00521E10`), `IsOwnerGuild` (`0x00521E10`), `IsSiegeWarMonster` (`0x00521EB0`), `SetDefenseGuildTargetPosition` (`0x00521D70`), `CheckApplicationRequirement` (`0x005205E0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIEventTeleport`](AgcmUIEventTeleport.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUITax`](AgcmUITax.md)
