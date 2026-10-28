# Winsock Sequenz 07: Chatting und Channels

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Quelle: statische Analyse von `alefclient.pseudocode.c`, besonders [`AgpmChatting`](../Module/AgpmChatting.md), [`AgcmUIChatting2`](../Module/AgcmUIChatting2.md), [`AgcmUIChannel`](../Module/AgcmUIChannel.md), Sendbuilder um `FUN_0056eac0` und Channel-Wrapper um `FUN_005609c0` bis `FUN_00560c00`.

## Kurzfazit

- Chat laeuft ueber `AgpmChatting`, Netzwerkmodul `0x0f`.
- Der direkte Chat-Sendbuilder ist `FUN_0056eac0`.
- Textnachrichten sind clientseitig auf `< 0x100` Bytes begrenzt; ein UI-Wrapper fuer normale Eingabe kuerzt zusaetzlich auf `0x80`.
- Der Chattyp muss `< 0x15` sein.
- Channel-/Whisper-Verwaltung nutzt zusaetzliche Builder im Umfeld von Modul `0x2c` ([`AgpmChannel`](../Module/AgpmChannel.md)/Channel-Logik), nicht nur `AgpmChatting`.
- Sichtbare Chatklassen: Normal, Guild, Party, Whisper, System, Notice, Shrine, Quest, Area, Race Trumpet.

## AgpmChatting Modul

Konstruktor `FUN_0056e8d0`:

- Modulname: `AgpmChatting`
- Modul-ID: `FUN_004e4540(0xf)` -> Netzwerkmodul `0x0f`
- Paketlayout:

```text
FUN_004e9f30(param_1 + 0x312,
             1,1, 5,1, 1,1, 6,1,
             0,0x31, 0,0x31,
             0xd,1,
             0xff,0)
```

Direkte Offsets/Felder:

- `+0xc48`: Byteoffset von `param_1 + 0x312` im Decompiler; dieses Layout wird in `FUN_0056eac0` direkt benutzt.
- `+0xc44`: lokale Character-Extension-ID, registriert in `FUN_0056ec90`.
- `+0xc3c`: Referenz auf [`AgpmCharacter`](../Module/AgpmCharacter.md).
- `+0xc40`: Referenz auf [`AgpmParty`](../Module/AgpmParty.md).
- `+0xc38`: in `FUN_0056ea30` als Timer/Callback-Kontext benutzt.
- `+0xc44`-Extension enthaelt pro Character mindestens ein Flag bei Offset `+4`, gesetzt durch `FUN_0056ebf0`/`FUN_0056ec20`.

## Direct Chat Send: FUN_0056eac0

Signatur nach Decompiler:

```text
FUN_0056eac0(
    AgpmChattingModule,
    senderCharacterId,
    chatType,
    contextA,
    contextB,
    messagePtr,
    messageLen,
    outLenPtr
)
```

Guards:

- `senderCharacterId != 0`
- `messagePtr != NULL`
- `messageLen > 0`
- String darf nicht leer sein.
- `messageLen < 0x100`
- `chatType < 0x15`

Vor dem Paketbau wird aus dem Sender-Character ein Typ-/Statusflag bestimmt:

```text
uVar3 = FUN_00503000(senderCharacter)
if (uVar3 & 1) local_4 = 1
else if (uVar3 & 2) local_4 = 2
else if (uVar3 & 4) local_4 = 4
else local_4 = 0
```

Paketbau:

```text
FUN_004ea280(AgpmChatting +0xc48, 1, outLenPtr, 0x0f,
             &opOrUnknownByte,
             &senderCharacterId,
             &chatType,
             &senderTypeFlag,
             contextA,
             contextB,
             messagePtr,
             &messageLen)
```

Wichtig: `local_5` ist im Decompiler ein Stack-Byte und wird als erstes Feld uebergeben. Weil sie aus der NUL-Terminierungsschleife stammt, ist wahrscheinlich entweder der Opcode im Layout implizit/immer `0`, oder der Decompiler hat das eigentliche Operation-Byte schlecht rekonstruiert. Sicher ist aber: Das aeussere Modul ist `0x0f`, und die Chatart steht separat in `chatType`.

## Normaler Chat: UI -> Server

`FUN_005be890` ist ein klarer UI-/Input-Wrapper:

```text
FUN_005be890(uiObj, senderCharacterId, text, textLen, context, enableFilter)
```

Ablauf:

1. Leeren Text verwerfen.
2. `AgcmCharacter` und `AgpmChatting` suchen.
3. Lokalen Character ueber `DAT_0001596c + AgcmCharacter` holen.
4. `textLen` auf `0x80` begrenzen.
5. Optional lokalen Filter/Hook ueber `param_1 +0xbd4`.
6. Text durch `FUN_006097b0(text)` normalisieren/filtern.
7. `FUN_0056eac0(localChar +4, senderCharacterId, 0, contextIfType5, text, textLen, &len)`.
8. Bei Erfolg `FUN_004e45d0(packet, len, 0, 3, 0)` senden.

Damit ist normaler Chat wahrscheinlich:

```text
module 0x0f, chatType 0
fields: senderCID, chatType, senderTypeFlag, contextA, contextB, message, messageLen
```

Sonderkommandos:

- `FUN_005bec30` sendet lokal den Text `_syncpos` als Chatnachricht mit Laenge `9`.
- `FUN_005bed20` sendet lokal den Text `_escape` als Chatnachricht mit Laenge `8`.

Diese sehen wie Debug-/GM-/Support-Kommandos aus. Sie laufen trotzdem ueber den normalen Chatbuilder.

## Chat-Eingabe und Private Message UI

`AgcmUIChatting2` registriert:

- `Chat_InputNormalUIOpen`
- `Chat_InputStart`
- `Chat_InputEndMessage`
- `Chat_InputEndPrivateMessage`
- `Chat_ReplyImmediate`
- `Chat_InputStatusClick`
- `Chat_DisplayStatus`
- `Chat_InputUserData`

Interpretation:

- `Chat_InputEndMessage` endet im normalen Sendpfad.
- `Chat_InputEndPrivateMessage`/`Chat_ReplyImmediate` liefern Zielnamen/-IDs fuer Whisper.
- Die UI haelt UserData bei `AgcmUIChatting2 +0x4f8c` und Status-/Reply-Daten bei `+0x4f6c/+0x4f70`.

## Chat-Anzeigearten

Gefundene Anzeige-/Filtermasken:

| Maske | Name/String | Bedeutung |
|---:|---|---|
| `0x001` | `NORMAL_CHAT` | normaler lokaler Chat |
| `0x002` | `GUILD_CHAT` / `Chat_Guild_Header` | Gildenchat |
| `0x004` | `PARTY_CHAT` / `Chat_Party_Header` | Partychat |
| `0x008` | `WHISPER_RECV` / `Chat_Whisper_Header` | Whisper empfangen |
| `0x010` | `SYSTEM_CHAT2` / `Chat_System_Header` | Systemnachricht |
| `0x020` | `NOTICE_CHAT1` / `Chat_Notice_Header` | Notice/Ankuendigung |
| `0x040` | `QUEST_CHAT` / `Chat_Quest_Header` | Questmeldung |
| `0x080` | `SHRINE_CHAT` / `Chat_Shrine_Header` | Shrine-/Eventmeldung |
| `0x100` | `Yellow` | spezielle farbige Ausgabe |
| `0x200` | `WORD_BALLON` / `Chat_Area_Header` | Area-/Sprechblasenchat |
| `0x400` | `RACE_TRUMPET` | Race-Trumpet/Broadcast |

Diese Masken sind Anzeige-/Filtermasken. Sie muessen nicht identisch mit dem `chatType` im Netzwerkpaket sein, helfen aber bei der Semantik.

## Channel-Modul und Channel-Aktionen

Neben `AgpmChatting` gibt es `AgpmChannel`/`AgcmUIChannel`. Die Sendbuilder liegen bei `FUN_005609c0` bis `FUN_00560c00` und bauen Pakete mit Modul `0x2c`.

Gesicherte Builder:

| Funktion | Op/Typ im ersten Feld | Beobachtung |
|---|---:|---|
| `FUN_005609c0` | `1` | Channel erstellen/konfigurieren; nutzt Name, Optionen, Passwort/Meta |
| `FUN_00560a30` | `3` | Channel join oder Anfrage ohne Zusatzdaten |
| `FUN_00560a60` | `4` | Channel leave/close |
| `FUN_00560ac0` | `9` | Channel-Chatnachricht, aus `ChannelSend_ChatMessage` |
| `FUN_00560b30` | `8` | Whisper/Invite/FindUser-nahe Aktion |
| `FUN_00560b90` | `7` | Invite/Whisper-nahe Aktion mit Zusatzparametern |
| `FUN_00560c00` | `10` | Channel/Whisper-Spezialaktion |

Alle diese Builder rufen:

```text
FUN_004ea280(AgpmChannel +0xb94, 1, outLen, 0x2c,
             &op, &channelNameOrId, fieldA, fieldB, fieldC,
             fieldD, fieldE, fieldF, 0)
```

`FUN_006a9df0` (`ChannelSend_ChatMessage`) liest den aktiven Channel-Tab, den Text aus dem UI und ruft:

```text
FUN_006a90a0(channelNamePtr, textPtr)
  -> FUN_00560ac0(&len, localCharacterId, channelName, AgpmChannel +0x3c, text)
  -> FUN_004e45d0(...)
```

Damit ist Channel-Chat wahrscheinlich nicht Modul `0x0f`, sondern Modul `0x2c`, Op `9`.

## Channel UI und Fehler

Gefundene UI-Aktionen:

- `CreateChannel`
- `CreateChannelOption_PuplicCLick`
- `CreateChannelOption_PrivateCLick`
- `CreateChannelOption_GuildCLick`
- `Channeljoin_click`
- `ChannelLeave_click`
- `ChannelSend_ChatMessage`
- `InviteChannelSend`
- `InviteJoinChannel_Click`
- `FindUser_Click`
- `SendWhisper_Click`
- `PasswordOK_click`
- `BanBlockWhisper_Click`

Gefundene UI-Meldungen:

- `ChannelAlreadyExist_MsgUI`
- `ChannelNotExist_MsgUI`
- `NotExistCharacter_MsgUI`
- `ChannelCountFull_MsgUI`
- `NotGuildMaster_MsgUI`
- `NOtGuildMember_MsgUI`
- `GuildChannelAlreadyExist_MsgUI`
- `InvalidPassword_MsgUI`
- `Channel_Create_Message`
- `Channel_Join_Message`
- `Channel_Leave_Message`

## Server -> Client

`AgpmChatting` Receive-/Apply-Funktion `FUN_0056efc0` liest das gleiche Layout `AgpmChatting +0xc48`:

```text
FUN_004e9fb0(AgpmChatting +0xc48, 1, packet, len,
             &opOrType,
             &senderCharacterId,
             &chatSubType,
             &contextB,
             &contextA,
             &messagePtr,
             &messageLen)
```

Guards:

- Paketlaenge muss zum String passen: `layoutHeader + 0x0d + messageLen <= packetLen`.
- `messageLen < 0x81` beim Empfang.
- Sender wird ueber `FUN_005035f0(senderCharacterId)` aufgeloest.
- Servernachrichten fuer lokale/remote Characters werden je nach Characterstatus verworfen oder angezeigt.

`FUN_0056ecf0` verteilt Chattypen/Events auf lokale Callbacks:

| Chat/Subtype | Lokaler Callback | Inferenz |
|---:|---:|---|
| `0` | `0` | normaler Chat |
| `1` | `1` | Gilden-/Gruppenchat |
| `2` | `2` | Party-/Gruppenchat |
| `3` | `3` | Whisper/System-Untertyp |
| `4` | `4` | weiterer Chatkanal |
| `5` | `5` nach Zusatzpruefung `0x0d` | Whisper/gerichtete Nachricht oder Spezialnachricht |
| `7` | `6` | System/Notice-nahe |
| `8..10` | `7` | Broadcast/Systemvarianten |
| `0x0e` | `0x10` | Spezialkanal |
| `0x0f` | `0x11` | Spezialkanal |

Die exakte Textklasse entsteht danach in `AgcmUIChatting2` ueber Anzeigeheader und Masken.

## Wahrscheinliche Serverdatenbank-Strukturen

| Tabelle | Zweck | Abgeleitete Felder |
|---|---|---|
| `chat_messages` | optionales Chatlogging | `message_id`, `server_id`, `channel_type`, `sender_character_id`, `sender_name`, `target_character_id`, `target_name`, `text`, `created_at` |
| `chat_channels` | benutzerdefinierte Channels | `channel_id`, `name`, `owner_character_id`, `type_public_private_guild`, `password_hash`, `created_at`, `closed_at` |
| `chat_channel_members` | Mitglieder/Userliste | `channel_id`, `character_id`, `joined_at`, `role`, `muted` |
| `chat_invites` | Channel-Einladungen | `invite_id`, `channel_id`, `from_character_id`, `to_character_id`, `state`, `created_at` |
| `whisper_blocks` | Whisper-/Ignore-Optionen | `character_id`, `blocked_character_id`, `mode`, `created_at` |
| `notice_messages` | System-/GM-/Servermeldungen | `notice_id`, `scope`, `text`, `priority`, `starts_at`, `ends_at` |

## Offene Punkte

- Die genaue Zuordnung `chatType` -> Normal/Guild/Party/Whisper muss ueber Callbacks in `AgcmUIChatting2` fertig gemappt werden.
- `AgpmChannel` (`0x2c`) sollte separat vertieft werden, weil dort Channel-Erstellung, Join/Leave, Invite, Passwort und Channel-Chat gebuendelt sind.
- Die Decompiler-Anomalie beim ersten Feld von `FUN_0056eac0` (`local_5`) sollte im Disassembly oder Ghidra-P-Code kontrolliert werden.
