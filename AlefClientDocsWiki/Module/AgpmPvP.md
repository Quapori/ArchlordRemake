# AgpmPvP (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmPvP` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmPvP` / `AgpmPvP.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00582A60` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMPVP_PACKET_*` kennt 22 Operationen, davon 22 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 22 Operationen liegen 2013er Ereignisse vor; 22 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0057f630`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0057E450` | `AgpmPvP::ctor_or_dtor_0057e450` | merged |
| `0x0057E4F0` | `AgpmPvP::OnInit` | merged |
| `0x0057E550` | `AgpmPvP::OnDestroy` | merged |
| `0x0057ED60` | `AgpmPvP::~AgpmPvP` | merged |
| `0x0057F630` | `AgpmPvP::ctor_or_dtor_0057f630` | merged |
| `0x0057FBB0` | `AgpmPvP::CBRegionChange` | stage1 |
| `0x005810D0` | `AgpmPvP::CBIsAttackable` | stage1 |
| `0x00581100` | `AgpmPvP::CBIsSkillEnable` | stage1 |
| `0x00582160` | `AgpmPvP::CBInitCharacter` | stage1 |
| `0x005822A0` | `AgpmPvP::CBRemoveCharacter` | stage1 |
| `0x00582340` | `AgpmPvP::OnAddModule` | merged |
| `0x00582A60` | `AgpmPvP::OnReceive` | merged |
| `0x0057E6A0` | `AgpmPvP::OnReceiveRequestDeadType` | casemap:AgpmPvP |
| `0x0057E6D0` | `AgpmPvP::OnReceiveResponseDeadType` | casemap:AgpmPvP |
| `0x0057ED80` | `AgpmPvP::OnReceivePvPInfo` | casemap:AgpmPvP |
| `0x0057EEB0` | `AgpmPvP::OnReceiveCannotUseTeleport` | casemap:AgpmPvP |
| `0x0057EF20` | `AgpmPvP::OnReceiveSystemMessage` | casemap:AgpmPvP |
| `0x00581160` | `AgpmPvP::OnReceiveUpdateFriend` | casemap:AgpmPvP |
| `0x005811E0` | `AgpmPvP::OnReceiveUpdateEnemy` | casemap:AgpmPvP |
| `0x00581270` | `AgpmPvP::OnReceiveUpdateFriendGuild` | casemap:AgpmPvP |
| `0x005812F0` | `AgpmPvP::OnReceiveUpdateEnemyGuild` | casemap:AgpmPvP |
| `0x00581690` | `AgpmPvP::OnReceiveRemoveFriend` | casemap:AgpmPvP |
| `0x00581710` | `AgpmPvP::OnReceiveRemoveEnemy` | casemap:AgpmPvP |
| `0x00581790` | `AgpmPvP::OnReceiveRemoveFriendGuild` | casemap:AgpmPvP |
| `0x00581810` | `AgpmPvP::OnReceiveRemoveEnemyGuild` | casemap:AgpmPvP |
| `0x00581890` | `AgpmPvP::OnReceiveInitEnemyGuild` | casemap:AgpmPvP |
| `0x00581FE0` | `AgpmPvP::OnReceiveInitFriend` | casemap:AgpmPvP |
| `0x00582060` | `AgpmPvP::OnReceiveInitEnemy` | casemap:AgpmPvP |
| `0x005820E0` | `AgpmPvP::OnReceiveInitFriendGuild` | casemap:AgpmPvP |
| `0x00582800` | `AgpmPvP::OnReceiveAddFriend` | casemap:AgpmPvP |
| `0x00582880` | `AgpmPvP::OnReceiveAddEnemy` | casemap:AgpmPvP |
| `0x00582910` | `AgpmPvP::OnReceiveAddFriendGuild` | casemap:AgpmPvP |
| `0x005829B0` | `AgpmPvP::OnReceiveAddEnemyGuild` | casemap:AgpmPvP |

33 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 11/11/11 | ja | ja |

**m_csPacket** (11 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | CID |
| 2 | `0x4` | INT32 | 1 | Target CID |
| 3 | `0x8` | INT32 | 1 | Win |
| 4 | `0x10` | INT32 | 1 | Lose |
| 5 | `0x20` | INT8 | 1 | PvPMode |
| 6 | `0x40` | INT8 | 1 | PvPStatus |
| 7 | `0x80` | INT8 | 1 | Win |
| 8 | `0x100` | CHAR | AGPMGUILD_MAX_GUILD_ID_LENGTH + 1 | GuildID |
| 9 | `0x200` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | For System Message |
| 10 | `0x400` | MEMORY_BLOCK | 1 | PvP Detail |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `PVP_INFO` | `0x0057ED80` `OnReceivePvPInfo` | `PVP_INFO`, `PVP_RESULT` | = (2013 = 2017) |
| 1 | `ADD_FRIEND` | `0x00582800` `OnReceiveAddFriend` | `ADD_FRIEND` | = (2013 = 2017) |
| 2 | `ADD_ENEMY` | `0x00582880` `OnReceiveAddEnemy` | `ADD_ENEMY` | = (2013 = 2017) |
| 3 | `REMOVE_FRIEND` | `0x00581690` `OnReceiveRemoveFriend` | `REMOVE_FRIEND` | = (2013 = 2017) |
| 4 | `REMOVE_ENEMY` | `0x00581710` `OnReceiveRemoveEnemy` | `REMOVE_ENEMY` | = (2013 = 2017) |
| 5 | `INIT_FRIEND` | `0x00581FE0` `OnReceiveInitFriend` | `INIT_FRIEND`, `REMOVE_FRIEND` | = (2013 = 2017) |
| 6 | `INIT_ENEMY` | `0x00582060` `OnReceiveInitEnemy` | `INIT_ENEMY`, `REMOVE_ENEMY` | = (2013 = 2017) |
| 7 | `UPDATE_FRIEND` | `0x00581160` `OnReceiveUpdateFriend` | `UPDATE_FRIEND` | = (2013 = 2017) |
| 8 | `UPDATE_ENEMY` | `0x005811E0` `OnReceiveUpdateEnemy` | `UPDATE_ENEMY` | = (2013 = 2017) |
| 9 | `ADD_FRIEND_GUILD` | `0x00582910` `OnReceiveAddFriendGuild` | `ADD_FRIEND_GUILD` | = (2013 = 2017) |
| 10 | `ADD_ENEMY_GUILD` | `0x005829B0` `OnReceiveAddEnemyGuild` | `ADD_ENEMY_GUILD` | = (2013 = 2017) |
| 11 | `REMOVE_FRIEND_GUILD` | `0x00581790` `OnReceiveRemoveFriendGuild` | `REMOVE_FRIEND_GUILD` | = (2013 = 2017) |
| 12 | `REMOVE_ENEMY_GUILD` | `0x00581810` `OnReceiveRemoveEnemyGuild` | `REMOVE_ENEMY_GUILD` | = (2013 = 2017) |
| 13 | `INIT_FRIEND_GUILD` | `0x005820E0` `OnReceiveInitFriendGuild` | `INIT_FRIEND_GUILD`, `REMOVE_FRIEND_GUILD` | = (2013 = 2017) |
| 14 | `INIT_ENEMY_GUILD` | `0x00581890` `OnReceiveInitEnemyGuild` | `INIT_ENEMY_GUILD`, `REMOVE_ENEMY_GUILD` | = (2013 = 2017) |
| 15 | `UPDATE_FRIEND_GUILD` | `0x00581270` `OnReceiveUpdateFriendGuild` | `UPDATE_FRIEND_GUILD` | = (2013 = 2017) |
| 16 | `UPDATE_ENEMY_GUILD` | `0x005812F0` `OnReceiveUpdateEnemyGuild` | `UPDATE_ENEMY_GUILD` | = (2013 = 2017) |
| 17 | `CANNOT_USE_TELEPORT` | `0x0057EEB0` `OnReceiveCannotUseTeleport` | `RECV_CANNOT_USE_TELEPORT` | = (2013 = 2017) |
| 18 | `SYSTEM_MESSAGE` | `0x0057EF20` `OnReceiveSystemMessage` | `SYSTEM_MESSAGE` | = (2013 = 2017) |
| 19 | `REQUEST_DEAD_TYPE` | `0x0057E6A0` `OnReceiveRequestDeadType` | `REQUEST_DEAD_TYPE` | = (2013 = 2017) |
| 20 | `RESPONSE_DEAD_TYPE` | `0x0057E6D0` `OnReceiveResponseDeadType` | `RESPONSE_DEAD_TYPE` | = (2013 = 2017) |
| 21 | `RACE_BATTLE` | `0x0057F840` `FUN_0057f840` | `RACE_BATTLE_STATUS` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 20, eingebaut: 9, gemeinsamer Rumpf: 35, nicht im Client: 37, ohne Kandidat: 9, zugeordnet: 27.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetPvPModeByRegion` | 16 | `0x0057E760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsInRaceBattle` | 6 | `0x0057E7D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RegionChange` | 71 | `0x0057FA80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsFriendGuild` | 14 | `0x0057FEA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitEnemyGuildList` | 61 | `0x005814E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitFriendGuildList` | 35 | `0x00581AB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitEnemyList` | 35 | `0x00581A10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitFriendList` | 35 | `0x00581970` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 51 | `0x00582180` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCharacter` | 39 | `0x00581E10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEnemyGuild` | 44 | `0x005826C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddFriendGuild` | 36 | `0x005825F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateEnemy` | 15 | `0x0057FCD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEnemy` | 8 | `0x00582540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSkillEnableSummons` | 99 | `0x0057F260` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsAttackableSummons` | 80 | `0x0057E8A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsEnemyCharacter` | 54 | `0x00580020` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateEnemyGuild` | 17 | `0x0057FE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateFriendGuild` | 16 | `0x0057FD80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsInvincible` | 15 | `0x0057F180` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsNowPvP` | 20 | `0x0057F110` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsCombatPvPMode` | 12 | `0x0057F040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsFreePvPMode` | 12 | `0x0057EFE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSafePvPMode` | 12 | `0x0057EF80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSkillEnable` | 297 | `0x005808D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsAttackable` | 254 | `0x005801D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 23 | `0x0057E630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `AddFriend` (`0x0057E800`), `AddFriend` (`0x0057E800`), `RemoveFriend` (`0x0057E800`), `RemoveFriend` (`0x0057E800`), `UpdateFriend` (`0x0057E800`), `AddEnemy` (`0x0057E800`), `RemoveEnemy` (`0x0057E800`), `RemoveEnemy` (`0x0057E800`), `IsEnemy` (`0x0057E800`), `IsEnemy` (`0x0057E800`), `GetEnemyInfo` (`0x0057E800`), `GetEnemyInfo` (`0x0057E800`), `RemoveFriendGuild` (`0x0057E800`), `GetFriendGuildInfo` (`0x0057E800`), `RemoveEnemyGuild` (`0x0057E800`), `IsEnemyGuild` (`0x0057E800`), `IsPC` (`0x0057E800`), `IsFriendCharacter` (`0x0057FF00`), `IsAttackSkill` (`0x0057F240`), `ProcessSystemMessage` (`0x0057FF00`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmMinimap`](AgcmMinimap.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmUIPvP`](AgcmUIPvP.md)
