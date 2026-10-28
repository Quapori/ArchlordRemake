# AgpmGuild (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmGuild` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmGuild` / `AgpmGuild.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00553D80` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMGUILD_PACKET_*` kennt 48 Operationen, davon 48 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 48 Operationen liegen 2013er Ereignisse vor; 44 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 3 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 8 Paketdefinition(en) in der Quelle, 8 davon im 2017er Konstruktor (`00552c60`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0054D1A0` | `AgpmGuild::OnInit` | merged |
| `0x0054D260` | `AgpmGuild::ConAgpdGuildADChar` | stage1 |
| `0x0054F820` | `AgpmGuild::ReadRequireItemIncreaseMaxMember` | merged |
| `0x00550350` | `AgpmGuild::CBChangeItemOwner` | stage1 |
| `0x005509A0` | `AgpmGuild::OnAddModule` | merged |
| `0x00550A30` | `AgpmGuild::OnIdle2` | merged |
| `0x00551880` | `AgpmGuild::ReadGuildMarkTemplate` | merged |
| `0x00552940` | `AgpmGuild::ctor_or_dtor_00552940` | merged |
| `0x00552A50` | `AgpmGuild::~AgpmGuild` | merged |
| `0x00552C60` | `AgpmGuild::ctor_or_dtor_00552c60` | merged |
| `0x00553280` | `AgpmGuild::OnDestroy` | merged |
| `0x00553D80` | `AgpmGuild::OnReceive` | merged |
| `0x0054D300` | `AgpmGuild::OnOperationJoinRequest` | casemap:AgpmGuild |
| `0x0054D380` | `AgpmGuild::OnOperationJoinReject` | casemap:AgpmGuild |
| `0x0054D3B0` | `AgpmGuild::OnOperationLeave` | casemap:AgpmGuild |
| `0x0054D410` | `AgpmGuild::OnOperationSystemMessage` | casemap:AgpmGuild |
| `0x0054D470` | `AgpmGuild::OnOperationBattleRequest` | casemap:AgpmGuild |
| `0x0054D510` | `AgpmGuild::OnOperationBattleAccept` | casemap:AgpmGuild |
| `0x0054D600` | `AgpmGuild::OnOperationBattleReject` | casemap:AgpmGuild |
| `0x0054D680` | `AgpmGuild::OnOperationBattleCancelRequest` | casemap:AgpmGuild |
| `0x0054D700` | `AgpmGuild::OnOperationBattleCancelAccept` | casemap:AgpmGuild |
| `0x0054D780` | `AgpmGuild::OnOperationBattleCancelReject` | casemap:AgpmGuild |
| `0x0054D800` | `AgpmGuild::OnOperationBattleMember` | casemap:AgpmGuild |
| `0x0054D850` | `AgpmGuild::OnOperationBattleMemberList` | casemap:AgpmGuild |
| `0x0054D890` | `AgpmGuild::OnOperationBattleRound` | casemap:AgpmGuild |
| `0x0054D8C0` | `AgpmGuild::OnOperationGuildList` | casemap:AgpmGuild |
| `0x0054FA00` | `AgpmGuild::OnOperationRenameGuildID` | casemap:AgpmGuild |
| `0x0054FAE0` | `AgpmGuild::OnOperationRenameCharacterID` | casemap:AgpmGuild |
| `0x005501B0` | `AgpmGuild::OnOperationBuyGuildMark` | casemap:AgpmGuild |
| `0x005501F0` | `AgpmGuild::OnOperationBuyGuildMarkForce` | casemap:AgpmGuild |
| `0x00550440` | `AgpmGuild::OnOperationJointRequest` | casemap:AgpmGuild |
| `0x00550490` | `AgpmGuild::OnOperationJointReject` | casemap:AgpmGuild |
| `0x005504C0` | `AgpmGuild::OnOperationJoint` | casemap:AgpmGuild |
| `0x00550530` | `AgpmGuild::OnOperationJointLeave` | casemap:AgpmGuild |
| `0x00550580` | `AgpmGuild::OnOperationHostileRequest` | casemap:AgpmGuild |
| `0x005505D0` | `AgpmGuild::OnOperationHostileReject` | casemap:AgpmGuild |
| `0x00550600` | `AgpmGuild::OnOperationHostile` | casemap:AgpmGuild |
| `0x00550670` | `AgpmGuild::OnOperationHostileLeaveRequest` | casemap:AgpmGuild |
| `0x005506C0` | `AgpmGuild::OnOperationHostileLeaveReject` | casemap:AgpmGuild |
| `0x005506F0` | `AgpmGuild::OnOperationHostileLeave` | casemap:AgpmGuild |
| `0x00550730` | `AgpmGuild::OnOperationJointDetail` | casemap:AgpmGuild |
| `0x00550750` | `AgpmGuild::OnOperationHostileDetail` | casemap:AgpmGuild |
| `0x00550770` | `AgpmGuild::OnOperationWorldChampionship` | casemap:AgpmGuild |
| `0x00550AE0` | `AgpmGuild::OnOperationUpdateNotice` | casemap:AgpmGuild |
| `0x00550BD0` | `AgpmGuild::OnOperationUpdateStatus` | casemap:AgpmGuild |
| `0x00550C30` | `AgpmGuild::OnOperationBattleRecord` | casemap:AgpmGuild |
| `0x00550CB0` | `AgpmGuild::OnOperationBattleInfo` | casemap:AgpmGuild |
| `0x00550E50` | `AgpmGuild::OnOperationBattlePerson` | casemap:AgpmGuild |
| `0x00551010` | `AgpmGuild::OnOperationBattleStart` | casemap:AgpmGuild |
| `0x00551160` | `AgpmGuild::OnOperationBattleUpdateTime` | casemap:AgpmGuild |
| `0x00551260` | `AgpmGuild::OnOperationBattleUpdateScore` | casemap:AgpmGuild |
| `0x00551360` | `AgpmGuild::OnOperationBattleWithdraw` | casemap:AgpmGuild |
| `0x00551460` | `AgpmGuild::OnOperationBattleResult` | casemap:AgpmGuild |
| `0x00551DC0` | `AgpmGuild::OnOperationJoin` | casemap:AgpmGuild |
| `0x005522F0` | `AgpmGuild::OnOperationLeaveAllow` | casemap:AgpmGuild |
| `0x00552370` | `AgpmGuild::OnOperationForcedLeave` | casemap:AgpmGuild |
| `0x00552400` | `AgpmGuild::OnOperationCharacterGuildData` | casemap:AgpmGuild |
| `0x005533B0` | `AgpmGuild::OnOperationDestroy` | casemap:AgpmGuild |
| `0x00553B90` | `AgpmGuild::OnOperationCreate` | casemap:AgpmGuild |

59 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 4/4/4 | 25/25/25 | ja | ja |
| `m_csMemberPacket` | 1/1/1 | 6/6/6 | ja | ja |
| `m_csBattlePacket` | 2/2/2 | 15/15/15 | ja | ja |
| `m_csBattlePersonPacket` | 4/4/4 | 2/2/2 | ja | ja |
| `m_csBattleMemberPacket` | 2/2/2 | 5/5/5 | ja | ja |
| `m_csBattleMemberListPacket` | 4/4/4 | 4/4/4 | ja | ja |
| `m_csGuildListPacket` | 4/4/4 | 22/22/22 | ja | ja |
| `m_csGuildListItemPacket` | 2/2/2 | 11/11/11 | ja | ja |

**m_csPacket** (25 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | CID |
| 2 | `0x4` | CHAR | AGPMGUILD_MAX_GUILD_ID_LENGTH + 1 | Guild ID |
| 3 | `0x8` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Master ID |
| 4 | `0x10` | INT32 | 1 | Guild TID |
| 5 | `0x20` | INT32 | 1 | Guild Rank |
| 6 | `0x40` | INT32 | 1 | Creation Date |
| 7 | `0x80` | INT32 | 1 | Max Member Count |
| 8 | `0x100` | INT32 | 1 | Union ID |
| 9 | `0x200` | CHAR | AGPMGUILD_MAX_PASSWORD_LENGTH + 1 | Password |
| 10 | `0x400` | MEMORY_BLOCK | 1 | Notice |
| 11 | `0x800` | INT8 | 1 | Status |
| 12 | `0x1000` | INT32 | 1 | Win |
| 13 | `0x2000` | INT32 | 1 | Draw |
| 14 | `0x4000` | INT32 | 1 | Lose |
| 15 | `0x8000` | INT32 | 1 | Guild Point |
| 16 | `0x10000` | PACKET | 1 | Member Packet |
| 17 | `0x20000` | PACKET | 1 | Battle Packet |
| 18 | `0x40000` | PACKET | 1 | BattlePerson Packet |
| 19 | `0x80000` | PACKET | 1 | BattleMember Packet |
| 20 | `0x100000` | PACKET | 1 | BattleMemberList Packet |
| 21 | `0x200000` | PACKET | 1 | GuildList Packet |
| 22 | `0x400000` | INT32 | 1 | GuildMark TID |
| 23 | `0x800000` | INT32 | 1 | GuildMark COlor |
| 24 | `0x1000000` | INT32 | 1 | Winner Guild (BOOL) |

**m_csMemberPacket** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Member ID |
| 1 | `0x2` | INT32 | 1 | Member Rank |
| 2 | `0x4` | INT32 | 1 | Join Date |
| 3 | `0x8` | INT32 | 1 | Member Level |
| 4 | `0x10` | INT32 | 1 | Member TID |
| 5 | `0x20` | INT8 | 1 | Status |

**m_csBattlePacket** (15 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPMGUILD_MAX_GUILD_ID_LENGTH + 1 | Enemy Guild ID |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Enemy Guild Master ID |
| 2 | `0x4` | UINT32 | 1 | Battle Accept Time |
| 3 | `0x8` | UINT32 | 1 | Battle Ready Time |
| 4 | `0x10` | UINT32 | 1 | Battle Start Time |
| 5 | `0x20` | UINT32 | 1 | Battle Mode |
| 6 | `0x40` | UINT32 | 1 | Battle Duration |
| 7 | `0x80` | UINT32 | 1 | Battle Person() |
| 8 | `0x100` | UINT32 | 1 | Battle Current Time |
| 9 | `0x200` | INT32 | 1 | MyScore |
| 10 | `0x400` | INT32 | 1 | EnemyScore |
| 11 | `0x800` | INT32 | 1 | MyUpScore |
| 12 | `0x1000` | INT32 | 1 | EnemyUpScore |
| 13 | `0x2000` | INT8 | 1 | Battle Result |
| 14 | `0x4000` | UINT32 | 1 | Round |

**m_csBattlePersonPacket** (2 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT16 | 1 |   (100) |
| 1 | `0x2` | MEMORY_BLOCK | 1 |   AGPACHARACTER_MAX_ID_STRING + 1   |

**m_csBattleMemberPacket** (5 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPMGUILD_MAX_GUILD_ID_LENGTH + 1 | Guild ID |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Char ID |
| 2 | `0x4` | UINT32 | 1 | Score |
| 3 | `0x8` | UINT32 | 1 | Kill |
| 4 | `0x10` | UINT32 | 1 | Death |

**m_csBattleMemberListPacket** (4 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | UINT32 | 1 | My Member Count |
| 1 | `0x2` | MEMORY_BLOCK | 1 | My Battle    ~~~ |
| 2 | `0x4` | UINT32 | 1 | Enemy Member Count |
| 3 | `0x8` | MEMORY_BLOCK | 1 | Enemy Battle    ~~~ |

**m_csGuildListPacket** (22 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Total Guild Count |
| 1 | `0x2` | INT32 | 1 | Page Count |
| 2 | `0x4` | INT16 | 1 | Item Count |
| 3 | `0x8` | PACKET | 1 | 1 GuildList Item |
| 4 | `0x10` | PACKET | 1 | 2 GuildList Item |
| 5 | `0x20` | PACKET | 1 | 3 GuildList Item |
| 6 | `0x40` | PACKET | 1 | 4 GuildList Item |
| 7 | `0x80` | PACKET | 1 | 5 GuildList Item |
| 8 | `0x100` | PACKET | 1 | 6 GuildList Item |
| 9 | `0x200` | PACKET | 1 | 7 GuildList Item |
| 10 | `0x400` | PACKET | 1 | 8 GuildList Item |
| 11 | `0x800` | PACKET | 1 | 9 GuildList Item |
| 12 | `0x1000` | PACKET | 1 | 10 GuildList Item |
| 13 | `0x2000` | PACKET | 1 | 11 GuildList Item |
| 14 | `0x4000` | PACKET | 1 | 12 GuildList Item |
| 15 | `0x8000` | PACKET | 1 | 13 GuildList Item |
| 16 | `0x10000` | PACKET | 1 | 14 GuildList Item |
| 17 | `0x20000` | PACKET | 1 | 15 GuildList Item |
| 18 | `0x40000` | PACKET | 1 | 16 GuildList Item |
| 19 | `0x80000` | PACKET | 1 | 17 GuildList Item |
| 20 | `0x100000` | PACKET | 1 | 18 GuildList Item |
| 21 | `0x200000` | PACKET | 1 | 19 GuildList Item |

**m_csGuildListItemPacket** (11 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPMGUILD_MAX_GUILD_ID_LENGTH + 1 | Guild ID |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Master ID |
| 2 | `0x4` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | SubMaster ID |
| 3 | `0x8` | INT32 | 1 | Level; |
| 4 | `0x10` | UINT32 | 1 | WinPoint; |
| 5 | `0x20` | INT32 | 1 | MemberCount; |
| 6 | `0x40` | INT32 | 1 | MaxMemberCount; |
| 7 | `0x80` | INT32 | 1 | lGuildBattle; |
| 8 | `0x100` | INT32 | 1 | lGuildMarkTID; |
| 9 | `0x200` | INT32 | 1 | lGuildMarkColor; |
| 10 | `0x400` | INT32 | 1 | IsWinner |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `CREATE` | `0x00553B90` `OnOperationCreate` | `CREATE`, `CREATE_ENABLE_CHECK` | = (2013 = 2017) |
| 1 | `JOIN_REQUEST` | `0x0054D300` `OnOperationJoinRequest` | `JOIN_REQUEST` | = (2013 = 2017) |
| 2 | `JOIN_REJECT` | `0x0054D380` `OnOperationJoinReject` | `JOIN_REJECT` | = (2013 = 2017) |
| 3 | `JOIN` | `0x00551DC0` `OnOperationJoin` | `JOIN`, `JOIN_ENABLE_CHECK`, `JOIN_REQUEST_SELF` | = (2013 = 2017) |
| 4 | `LEAVE` | `0x0054D3B0` `OnOperationLeave` | `LEAVE_REQUEST_SELF` | = (2013 = 2017) |
| 5 | `FORCED_LEAVE` | `0x00552370` `OnOperationForcedLeave` | `CHECK_LEAVE_POSSIBLE`, `FORCED_LEAVE`, `FORCED_LEAVE_FAIL`, `SYSTEM_MESSAGE` | 2017 ⊃ 2013 |
| 6 | `DESTROY` | `0x005533B0` `OnOperationDestroy` | `CHECK_DESTROY`, `CHECK_PASSWORD`, `DESTROY`, `DESTROY_FAIL`, `DESTROY_GUILD_CHECK_TIME`, `DESTROY_PREPROCESS` … (7) | = (2013 = 2017) |
| 8 | `CHAR_DATA` | `0x00552400` `OnOperationCharacterGuildData` | `CHAR_DATA`, `UPDATE_MEMBER_STATUS` | = (2013 = 2017) |
| 9 | `UPDATE_NOTICE` | `0x00550AE0` `OnOperationUpdateNotice` | `UPDATE_NOTICE` | = (2013 = 2017) |
| 10 | `SYSTEM_MESSAGE` | `0x0054D410` `OnOperationSystemMessage` | `SYSTEM_MESSAGE` | = (2013 = 2017) |
| 11 | `UPDATE_STATUS` | `0x00550BD0` `OnOperationUpdateStatus` | `UPDATE_STATUS` | = (2013 = 2017) |
| 12 | `UPDATE_RECORD` | `0x00550C30` `OnOperationBattleRecord` | `UPDATE_RECORD` | = (2013 = 2017) |
| 13 | `BATTLE_INFO` | `0x00550CB0` `OnOperationBattleInfo` | `BATTLE_INFO` | = (2013 = 2017) |
| 14 | `BATTLE_PERSON` | `0x00550E50` `OnOperationBattlePerson` | `BATTLE_PERSON` | = (2013 = 2017) |
| 15 | `BATTLE_REQUEST` | `0x0054D470` `OnOperationBattleRequest` | `BATTLE_REQUEST` | = (2013 = 2017) |
| 16 | `BATTLE_ACCEPT` | `0x0054D510` `OnOperationBattleAccept` | `BATTLE_ACCEPT` | = (2013 = 2017) |
| 17 | `BATTLE_REJECT` | `0x0054D600` `OnOperationBattleReject` | `BATTLE_REJECT` | = (2013 = 2017) |
| 18 | `BATTLE_CANCEL_REQUEST` | `0x0054D680` `OnOperationBattleCancelRequest` | `BATTLE_CANCEL_REQUEST` | = (2013 = 2017) |
| 19 | `BATTLE_CANCEL_ACCEPT` | `0x0054D700` `OnOperationBattleCancelAccept` | `BATTLE_CANCEL_ACCEPT` | = (2013 = 2017) |
| 20 | `BATTLE_CANCEL_REJECT` | `0x0054D780` `OnOperationBattleCancelReject` | `BATTLE_CANCEL_REJECT` | = (2013 = 2017) |
| 21 | `BATTLE_START` | `0x00551010` `OnOperationBattleStart` | `BATTLE_START` | = (2013 = 2017) |
| 22 | `BATTLE_UPDATE_TIME` | `0x00551160` `OnOperationBattleUpdateTime` | `BATTLE_UPDATE_TIME` | = (2013 = 2017) |
| 23 | `BATTLE_UPDATE_SCORE` | `0x00551260` `OnOperationBattleUpdateScore` | `BATTLE_UPDATE_SCORE` | = (2013 = 2017) |
| 24 | `BATTLE_WITHDRAW` | `0x00551360` `OnOperationBattleWithdraw` | `BATTLE_WITHDRAW`, `SYSTEM_MESSAGE` | = (2013 = 2017) |
| 25 | `BATTLE_RESULT` | `0x00551460` `OnOperationBattleResult` | `BATTLE_RESULT` | = (2013 = 2017) |
| 26 | `BATTLE_MEMBER` | `0x0054D800` `OnOperationBattleMember` | `BATTLE_MEMBER` | = (2013 = 2017) |
| 27 | `BATTLE_MEMBER_LIST` | `0x0054D850` `OnOperationBattleMemberList` | `BATTLE_MEMBER_LIST` | = (2013 = 2017) |
| 28 | `GUILDLIST` | `0x0054D8C0` `OnOperationGuildList` | `GUILDLIST` | = (2013 = 2017) |
| 29 | `LEAVE_ALLOW` | `0x005522F0` `OnOperationLeaveAllow` | `CHECK_LEAVE_POSSIBLE`, `LEAVE`, `LEAVE_FAIL`, `SYSTEM_MESSAGE` | 2017 ⊃ 2013 |
| 30 | `RENAME_GUILDID` | `0x0054FA00` `OnOperationRenameGuildID` | `RENAME_GUILDID` | = (2013 = 2017) |
| 31 | `RENAME_CHARACTERID` | `0x0054FAE0` `OnOperationRenameCharacterID` | `RENAME_CHARID` | = (2013 = 2017) |
| 32 | `BUY_GUILDMARK` | `0x005501B0` `OnOperationBuyGuildMark` | `BUY_GUILDMARK` | = (2013 = 2017) |
| 33 | `BUY_GUILDMARK_FORCE` | `0x005501F0` `OnOperationBuyGuildMarkForce` | `BUY_GUILDMARK_FORCE` | = (2013 = 2017) |
| 34 | `JOINT_REQUEST` | `0x00550440` `OnOperationJointRequest` | `JOINT_REQUEST` | = (2013 = 2017) |
| 35 | `JOINT_REJECT` | `0x00550490` `OnOperationJointReject` | `JOINT_REJECT` | = (2013 = 2017) |
| 36 | `JOINT` | `0x005504C0` `OnOperationJoint` | `JOINT` | = (2013 = 2017) |
| 37 | `JOINT_LEAVE` | `0x00550530` `OnOperationJointLeave` | `JOINT_LEAVE` | = (2013 = 2017) |
| 38 | `HOSTILE_REQUEST` | `0x00550580` `OnOperationHostileRequest` | `HOSTILE_REQUEST` | = (2013 = 2017) |
| 39 | `HOSTILE_REJECT` | `0x005505D0` `OnOperationHostileReject` | `HOSTILE_REJECT` | = (2013 = 2017) |
| 40 | `HOSTILE` | `0x00550600` `OnOperationHostile` | `HOSTILE` | = (2013 = 2017) |
| 41 | `HOSTILE_LEAVE_REQUEST` | `0x00550670` `OnOperationHostileLeaveRequest` | `HOSTILE_LEAVE_REQUEST` | = (2013 = 2017) |
| 42 | `HOSTILE_LEAVE_REJECT` | `0x005506C0` `OnOperationHostileLeaveReject` | `HOSTILE_LEAVE_REJECT` | = (2013 = 2017) |
| 43 | `HOSTILE_LEAVE` | `0x005506F0` `OnOperationHostileLeave` | `HOSTILE_LEAVE` | = (2013 = 2017) |
| 44 | `JOINT_DETAIL` | `0x00550730` `OnOperationJointDetail` | `JOINT_DETAIL` | = (2013 = 2017) |
| 45 | `HOSTILE_DETAIL` | `0x00550750` `OnOperationHostileDetail` | `HOSTILE_DETAIL` | = (2013 = 2017) |
| 46 | `BATTLE_ROUND` | `0x0054D890` `OnOperationBattleRound` | `BATTLE_ROUND` | = (2013 = 2017) |
| 47 | `WORLD_CHAMPIONSHIP` | `0x00550770` `OnOperationWorldChampionship` | `WORLD_CHAMPIONSHIP_ENTER`, `WORLD_CHAMPIONSHIP_REQUEST`, `WORLD_CHAMPIONSHIP_RESULT` | 2017 ⊃ 2013 |
| 48 | `CLASS_SOCIETY_SYSTEM` | `0x005507B0` `FUN_005507b0` | `CLASSSOCIETY_APPOINTMENT_ANSWER`, `CLASSSOCIETY_APPOINTMENT_ASK`, `CLASSSOCIETY_APPOINTMENT_REQUEST`, `CLASSSOCIETY_MEMBERRANK_UPDATE`, `CLASSSOCIETY_SUCCESSION_ANSWER`, `CLASSSOCIETY_SUCCESSION_ASK` … (8) | 2017 ⊃ 2013 |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 5 | `FORCED_LEAVE` | – | AGPMGUILD_CB_CHECK_LEAVE_POSSIBLE, AGPMGUILD_CB_SYSTEM_MESSAGE |
| 29 | `LEAVE_ALLOW` | – | AGPMGUILD_CB_CHECK_LEAVE_POSSIBLE, AGPMGUILD_CB_SYSTEM_MESSAGE |
| 48 | `CLASS_SOCIETY_SYSTEM` | – | AGPMGUILD_CB_CLASSSOCIETY_APPOINTMENT_ANSWER, AGPMGUILD_CB_CLASSSOCIETY_APPOINTMENT_REQUEST, AGPMGUILD_CB_CLASSSOCIETY_SUCCESSION_ANSWER, AGPMGUILD_CB_CLASSSOCIETY_SUCCESSION_REQUEST |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 18, eingebaut: 32, gemeinsamer Rumpf: 70, nicht im Client: 40, ohne Kandidat: 33, zugeordnet: 41.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetJointGuildMarkID` | 5 | `0x00550170` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsDuplicatedCharacterOfMigration` | 13 | `0x0054FAB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCurrentBattleInfo` | 9 | `0x0054E050` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCharAD` | 30 | `0x0054DE90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateGuildMember` | 15 | `0x0054DCA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsBattleStatus` | 5 | `0x005517D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetRequireIncreaseMaxMember` | 7 | `0x0054F7E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReReadGuildMarkTemplate` | 63 | `0x0054CD7E` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyGuildMarkTemplate` | 16 | `0x0054FCA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateGuildMarkTemplate` | 13 | `0x0054FCF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateMemberStatus` | 38 | `0x00552110` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ForcedLeaveMember` | 48 | `0x00551F90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LeaveMember` | 45 | `0x00551E40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyGuild` | 9 | `0x00553090` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateGuild` | 67 | `0x00553760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveMember` | 5 | `0x0054DE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `JoinMember` | 39 | `0x0054DD10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildListRequestPacket` | 36 | `0x0054F660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileLeavePacket` | 16 | `0x0054F3E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileLeaveRequestPacket` | 16 | `0x0054F310` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostilePacket` | 17 | `0x0054F230` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileRejectPacket` | 16 | `0x0054F160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileRequestPacket` | 17 | `0x0054F090` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointLeavePacket` | 16 | `0x0054EFD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointPacket` | 17 | `0x0054EEF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointRejectPacket` | 16 | `0x0054EE20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointRequestPacket` | 17 | `0x0054ED50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildBattlePersonPacket` | 13 | `0x0054E970` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildForcedLeavePacket` | 19 | `0x0054E680` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildLeavePacket` | 19 | `0x0054E5D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJoinPacket` | 19 | `0x0054E460` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJoinRejectPacket` | 19 | `0x0054E3B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJoinRequestPacket` | 19 | `0x0054E300` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMaster` | 13 | `0x0054DA30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DeleteAllGuildMark` | 18 | `0x0054FE50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RenameCharID` | 40 | `0x0054FB30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildMemberPacket` | 18 | `0x0054E520` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetOnlineMemberCount` | 23 | `0x0054DAF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMemberCount` | 23 | `0x0054DA70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMember` | 9 | `0x0054DA00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 4 | `0x0054D230` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetGuild` (`0x00552280`), `GetGuild` (`0x00552280`), `GetGuildLock` (`0x00551550`), `GetGuildLock` (`0x00551550`), `GetGuildLock` (`0x00551550`), `IsMaster` (`0x00552280`), `IsSubMaster` (`0x005515A0`), `GetJoinedGuildID` (`0x005526C0`), `IsEnemyGuild` (`0x005526C0`), `IsEnemyGuild` (`0x005526C0`), `IsJointGuild` (`0x005526C0`), `IsJointGuild` (`0x005526C0`), `IsHostileGuild` (`0x005526C0`), `IsHostileGuild` (`0x005526C0`), `IsHostileGuild` (`0x005526C0`), `GetGuildMarkID` (`0x0054FF70`), `GetGuildMarkTexture` (`0x00551CA0`), `GetGuildMarkTexture` (`0x00551CA0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmGuild`](AgcmGuild.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmUIGuild`](AgcmUIGuild.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md)
