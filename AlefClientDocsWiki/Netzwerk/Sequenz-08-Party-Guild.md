# Winsock Sequenz 08: Party und Guild

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Quelle: statische Analyse von `alefclient.pseudocode.c`, besonders [`AgpmParty`](../Module/AgpmParty.md), [`AgcmParty`](../Module/AgcmParty.md), [`AgpmGuild`](../Module/AgpmGuild.md), [`AgcmGuild`](../Module/AgcmGuild.md), UI-Bindings und `FUN_004ea280`-Sendpfade.

## Kurzfazit

- `AgpmParty` ist Modul `0x08`.
- `AgcmParty` ist Modul `0x09` und sendet die sichtbaren Party-Aktionen wie Invite, Reject, Accept, Leave, Banish, InviteByCharID und Leader/Option-Aenderungen.
- `AgpmGuild` ist Modul `0x15`.
- `AgcmGuild` ist die grosse UI-/Clientlogik fuer Gildenfenster, Create/Destroy, Notice, Memberliste, Invite, Join/Leave, Battle, Member-Increase, Rename, GuildMark, Joint/Hostile Relations und WorldChampionship.
- Guild ist zu gross fuer eine einzige finale Datei; diese Sequenz dokumentiert die Kernstruktur. Guild-Battle und GuildMark sollten separat tief zerlegt werden.

## AgpmParty

Konstruktor `FUN_00566c70`:

- Modulname: `AgpmParty`
- Modul-ID: `FUN_004e4540(8)` -> Netzwerkmodul `0x08`
- Layouts:

```text
AgpmParty +0x0d00:
  1,1, 5,1, 1,1, 1,1, 5,1, 0xd,1,
  0xc,1, 0xc,1, 1,1, 0xc,1, 1,1

AgpmParty +0x13614:
  1,1, 1,1, 1,1, 1,1

AgpmParty +0x25f28:
  1,1, 3,1, 3,1
```

Inferenz:

- Das grosse Layout enthaelt Party-ID/Member-ID/Status/Teilungsoptionen/Positionen oder Factorwerte.
- Die kleinen Layouts sind Status-/Options-Subpakete.
- `FUN_005670c0` und `FUN_00567110` bauen Party-Pakete mit `AgpmParty +0xd00`, Modul `0x08`, internen Ops `6` und `5`. Diese werden von `AgcmParty` ueber `FUN_006e8860`/`FUN_006e87e0` direkt gesendet.

## AgcmParty

Konstruktor `FUN_006e85c0`:

- Modulname: `AgcmParty`
- Modul-ID: `FUN_004e4540(9)` -> Netzwerkmodul `0x09`
- Layout:

```text
AgcmParty +0x0ba8:
  1,1, 5,1, 5,1, 0,0x31
```

Abhaengigkeiten in `FUN_006e8a00`:

- `+0xb98` -> [`AgpmCharacter`](../Module/AgpmCharacter.md)
- `+0xb9c` -> `AgpmParty`
- `+0xba0` -> `AgcmCharacter`
- `+0xba4` -> [`AgpmFactors`](../Module/AgpmFactors.md)

### Party Client -> Server Ops

Alle folgenden Builder nutzen:

```text
FUN_004ea280(AgcmParty +0xba8, 1, &len, 9,
             &op, &fieldA, &fieldB, optionalField)
FUN_004e45d0(packet, len, 0, 3, 0)
```

| Funktion | Op | Debugstring / Inferenz |
|---|---:|---|
| `FUN_006e8e10` | `0` | `SendPacketInvite`; Party-Einladung an Ziel |
| `FUN_006e8eb0` | `1` | `SendPacketReject`; Einladung ablehnen |
| `FUN_006e8f50` | `2` | `SendPacketAccept`; Einladung akzeptieren |
| `FUN_006e8ff0` | `3` | `SendPacketLeave`; Party verlassen |
| `FUN_006e9080` | `4` | `SendPacketBanish`; Member entfernen/kicken |
| `FUN_006e9120` | low byte aus Param, effektiv InviteByCharID | `SendPacketInviteByCharID`; Ziel ist Character-ID statt Name/Objekt |
| `FUN_006e91b0` | `0x0b` | weitere Partyaktion mit zwei IDs |
| `FUN_006e9250` | `0x10` | lokale Character-ID + Zielwert; vermutlich Leader Delegation oder Option |
| `FUN_006e92f0` | `0x11` | lokale Character-ID + Zielwert; vermutlich zweite Leader/Option-Aktion |

Die UI-Strings stuetzen diese Semantik:

- `Party_Invite_Failed_Self`
- `Party_Invite_Failed_No_Leader`
- `Party_InviteMemeberLevelDiff`
- `Party_DelegationLeader`
- `Party_DelegationLeaderFailed`
- `Party_Item_Division_Sequence`
- `Party_Item_Division_Free`
- `Party_Item_Division_Damage`
- `Party_Exp_Division_Damage`
- `Party_Exp_Division_Level`

## AgpmGuild

Konstruktor `FUN_005533a0`:

- Modulname: `AgpmGuild`
- Modul-ID: `FUN_004e4540(0x15)` -> Netzwerkmodul `0x15`
- Registriert viele Datenbloecke:

```text
FUN_004e4190(0x1d8, 0)
FUN_004e4190(0x5c, 1)
FUN_004e4190(8, 2)
FUN_004e4190(0x20, 4)
```

Wichtige Layouts:

- `AgpmGuild +0x0e7c`: grosses Hauptlayout mit Guild-ID, Name, Master, Memberdaten, Statuswerten, Guild-Battle/Relation/Option-Feldern.
- `AgpmGuild +0x13790`: Nestedblock fuer kurze Gilden-/Memberdaten.
- `AgpmGuild +0x260a4`: grosser Nestedblock mit vielen 32-bit-Werten; wahrscheinlich Memberliste oder Battle-/Relation-Daten.
- `AgpmGuild +0x389b8`: kleiner Nestedblock.
- `AgpmGuild +0x4de4`, `+0x9829`, `+0xe26e`, `+0x12cb3`, `+0x176f8`, `+0x1c13d`, `+0x20b82`: weitere Subpakete fuer Listen, Notice, GuildMark, Battle/Relations.

`FUN_0054e8b0` ist ein generischer Wrapper um `FUN_004ea280(AgpmGuild +0xe7c, ...)`. Viele spezialisierte Funktionen setzen nur das erste Opcode-Byte und haengen passende Nestedbloecke an.

### Gesicherte Guild-Sendbuilder

Gelesener Bereich `FUN_0054ea90` bis `FUN_0054f100`:

| Funktion | Op | Beobachtung |
|---|---:|---|
| `FUN_0054ea90` | `1` | Hauptpaket + Nested `+0x13790`; mehrere IDs/Strings |
| `FUN_0054eb40` | `2` | Hauptpaket + Nested `+0x13790` |
| `FUN_0054ebf0` | `3` | Hauptpaket + Nested `+0x13790` mit mehr Feldern |
| `FUN_0054ed60` | `4` | Hauptpaket + Nested `+0x13790` |
| `FUN_0054ee10` | `5` | Hauptpaket + Nested `+0x13790` |
| `FUN_0054eec0` | `6` | Hauptpaket ohne lokalen Nestedblock, nutzt spaeteres Feld |
| `FUN_0054ef30` | `7` | Hauptpaket ohne lokalen Nestedblock, anderer Zusatzparameter |
| `FUN_0054eff0` | nicht low-byte gesetzt sichtbar | Hauptpaket + grosses Nested `+0x260a4`, wahrscheinlich Member-/Battleliste |
| `FUN_0054f100` | `0x0e` | Hauptpaket + Nested `+0x389b8` |

Weil die Funktionsnamen fehlen, erfolgt die genaue Semantik ueber UI-Trigger und Felder:

- Create/Destroy Guild
- Notice lesen/senden
- Memberliste/Membersuche
- Invite/Allow/Leave/ForcedLeave
- GuildList/Search/Join
- GuildBattle request/accept/cancel/time
- MaxMemberIncrease
- Rename Guild
- GuildMark create/update/buy
- Joint/Hostile Relations
- WorldChampionship request/enter
- Appoint/Succession

## AgcmGuild UI-Felder

Sehr aussagekraeftige UserData-Felder:

- `Guild_Notice_UD`
- `Guild_Record_UD`
- `Guild_DetailInfo_UD`
- `Guild_Member_DetailInfo_UD`
- `Guild_List_DetailInfo_UD`
- `Guild_List_Index`
- `Guild_Member_Index`
- `Guild_Selected_MemberID_UD`
- `Guild_Join_GuildID`
- `Guild_Join_GuildMasterID`
- `Guild_Battle_Enemy_GuildID`
- `Guild_Battle_Type`
- `Guild_Battle_Duration`
- `Guild_Battle_Person`
- `Guild_Enable_Inc_Max_Member`
- `Guild_Enable_GuildBattle`
- `Guild_Guild_List_Page`
- `Guild_Guild_List_MaxPage`
- `Guild_Member_List_Page`
- `Guild_Member_List_MaxPage`
- `Guild_Enable_Invite_Party`
- `Guild_Enable_Chat_Whisper`
- `Guild_Enable_Allow_Button`
- `Guild_Enable_Appoint_Button`
- `Guild_Enable_Succession_Button`
- `Guild_Enable_Create_Guild`
- `Guild_Enable_Guild_Master`
- `Guild_Enable_RenameGuildID`
- `Guild_GuildMarkGrid`
- `Guild_GuildMarkLayerIndex`
- `Guild_GuildMarkColorGrid`
- `Guild_RelationGuildID`
- `Guild_RelationMasterID`
- `Guild_JointRequestBtnUD`
- `Guild_HostileRequestBtnUD`

Diese Felder bilden fast direkt Serverdaten ab: Guild-ID, Master-ID, Member-ID, Rechte/Rang, Pagination, Relations, Battle-Parameter, GuildMark-Layer/Farbe.

## Gildenfehler und Serverstatus

Sichtbare Status-/Fehlerstrings:

- `Guild_Msg_ExistGuildID`
- `Guild_Msg_NeedMoreLevel`
- `Guild_Msg_NeedMoreMoney`
- `Guild_Msg_NeedItem`
- `Guild_Msg_UseSpecialChar`
- `Guild_Msg_AlreadyMember`
- `Guild_Msg_MaxMember`
- `Guild_Msg_JoinFail`
- `Guild_Msg_InvalidPassword`
- `Guild_Msg_CreateComplete`
- `Guild_Msg_Destroy`
- `Guild_Msg_Join`
- `Guild_Msg_JoinReject`
- `Guild_Msg_Leave`
- `Guild_Msg_ForcedLeave`
- `Guild_Msg_Battle_Not_Enough_Member`
- `Guild_Msg_Battle_Not_Enough_Level`
- `Guild_Msg_Battle_Master_Offline`
- `Guild_Msg_Battle_Not_Exist_Guild`
- `Guild_Msg_Battle_Request`
- `Guild_Msg_Battle_Accept`
- `Guild_Joint_Already_Joint`
- `Guild_Joint_Max`
- `Guild_Joint_Wait`
- `Guild_Joint_Success`
- `Guild_Hostile_Already_Hostile`
- `Guild_Hostile_Max`
- `Guild_Hostile_Wait`
- `Guild_Hostile_Success`
- `Guild_Archlord_Defense_Success`
- `Guild_Archlord_Attack_Success`
- `Guild_Not_Enought_Gheld`
- `Guild_Not_Enought_Skull`

## Wahrscheinliche Serverdatenbank-Strukturen

| Tabelle | Zweck | Abgeleitete Felder |
|---|---|---|
| `parties` | aktive Parties | `party_id`, `leader_character_id`, `loot_mode`, `exp_mode`, `created_at` |
| `party_members` | Party-Mitglieder | `party_id`, `character_id`, `joined_at`, `online_state`, `map_id`, `position`, `role` |
| `party_invites` | Einladungen | `invite_id`, `from_character_id`, `to_character_id`, `party_id`, `state`, `expires_at` |
| `guilds` | Gildenstamm | `guild_id`, `name`, `master_character_id`, `notice`, `level`, `max_members`, `mark_id`, `created_at`, `destroy_requested_at` |
| `guild_members` | Gildenmitglieder | `guild_id`, `character_id`, `rank`, `joined_at`, `last_online`, `contribution`, `allow_flags` |
| `guild_join_requests` | Join/Allow Workflow | `guild_id`, `character_id`, `state`, `requested_at`, `handled_by` |
| `guild_battles` | Gildenkaempfe | `battle_id`, `guild_id`, `enemy_guild_id`, `type`, `duration`, `person_limit`, `state`, `starts_at`, `ends_at`, `result` |
| `guild_relations` | Joint/Hostile | `guild_id`, `other_guild_id`, `relation_type`, `state`, `created_at`, `expires_at` |
| `guild_marks` | GuildMark | `guild_id`, `layer_index`, `pattern_id`, `symbol_id`, `color_id`, `purchased_at` |
| `guild_transactions` | Kosten/Audit | `guild_id`, `character_id`, `action`, `money_delta`, `item_tid`, `item_count`, `created_at` |

## Offene Punkte

- `AgpmGuild` braucht einen eigenen Deep-Dive fuer Opcode-Mapping `1..0x0e+` auf Create/Destroy/Notice/Member/GuildList/Battle/Mark.
- `AgcmGuild` UI-Callback-Ziele wie `FUN_0077ed10`, `FUN_0077eae0`, `FUN_0077e640`, `FUN_0077dbe0`, `FUN_0077d7e0` sollten einzeln gelesen werden, weil sie die Guild-Sendbuilder eindeutig triggern.
- `AgcmParty` Receive-Switch `FUN_006e8ab0` springt ueber `PTR_LAB_006e8dbc` fuer Ops `<0x15`; die Jump-Tabelle sollte ueber Disassembly nachgezogen werden.
