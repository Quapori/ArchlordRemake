# AgcmUIChannel (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIChannel` (Chat-Räume: Erstellen, Beitreten, Einladen, Flüstern) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIChannel/AgcmUIChannel.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 57 von 64 Quellmethoden sind zugeordnet (UI-Registrierungen und Aufrufgraph); zusätzlich sind die sieben [`AgpmChannel`](AgpmChannel.md)-Paketbauer benannt.
- **Operationen:** Create 1, Join 3, Leave 4, Invitation 7, Password 8, ChatMsg 9, FindUser 10 über Paket-Typ `0x2C`, wie in der Quelle.
- **Räume:** höchstens fünf gleichzeitig beigetretene Räume, 10 KB Chatpuffer je Raum.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIChannel.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006AB090` | 514 | vtable/String |
| 1 | `OnInit` | `0x006AB2A0` | 1258 | vtable/String |
| 2 | `OnDestroy` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 3 | `OnIdle` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 4 | `AddEvent` | `0x006A8710` | 568 | Zeichenkette |
| 5 | `AddBoolean` | `0x006A91E0` | 31 | Zeichenkette |
| 6 | `AddFunction` | `0x006AACF0` | 705 | Zeichenkette |
| 7 | `AddUserData` | `0x006A9200` | 440 | Zeichenkette |
| 8 | `AddDisplay` | `0x006AA710` | 101 | Zeichenkette |
| 9 | `CreateChannelData` | `0x006AA850` | 429 | von Hand geprüft |
| 10 | `RefreshCreateRoomOption` | `0x006A8950` | 86 | Aufrufgraph (geprüft) |
| 11 | `RefreshAllChatRoom` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 12 | `RefreshChatRoom` | `0x006A9B20` | 195 | Aufrufgraph (geprüft) |
| 13 | `RefreshChatRoomUserList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 14 | `RefreshWhisperBtnStatus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 15 | `SendCreateChannel` | `0x006A89B0` | 155 | von Hand geprüft |
| 16 | `SendPacketChatMsg` | `0x006A8A50` | 173 | Aufrufgraph (geprüft) |
| 17 | `SendPacketJoinChannel` | `0x006A8B00` | 158 | Aufrufgraph (geprüft) |
| 18 | `SendPacketLeaveChannel` | `0x006A8BA0` | 152 | Aufrufgraph (geprüft) |
| 19 | `SendPacketPassword` | `0x006A8C40` | 169 | Aufrufgraph (geprüft) |
| 20 | `SendPacketInvitation` | `0x006A8CF0` | 174 | Aufrufgraph (geprüft) |
| 21 | `SendPacketFindUser` | `0x006A8DA0` | 152 | Aufrufgraph (geprüft) |
| 22 | `CBCloneUI` | `0x006A93C0` | 378 | Callback-Registrierung |
| 23 | `CBDestroyChannel` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 24 | `CBJoin` | `0x006AAA10` | 51 | Callback-Registrierung |
| 25 | `CBLeave` | `0x006AA0F0` | 63 | Callback-Registrierung |
| 26 | `CBInvitation` | `0x006A9BF0` | 123 | Callback-Registrierung |
| 27 | `CBPassword` | `0x006A9C70` | 93 | Callback-Registrierung |
| 28 | `CBChatMsg` | `0x006AA130` | 101 | Callback-Registrierung |
| 29 | `CBFindUserResult` | `0x006A9CD0` | 77 | Callback-Registrierung |
| 30 | `CBAddUser` | `0x006AAFC0` | 200 | Callback-Registrierung |
| 31 | `CBRemoveUser` | `0x006AA780` | 200 | Callback-Registrierung |
| 32 | `CBMsgCode` | `0x006A8E40` | 174 | Callback-Registrierung |
| 33 | `CBCloneUIClear` | `0x006A9540` | 125 | Callback-Registrierung |
| 34 | `OperationJoinChannel` | `0x006AA420` | 339 | von Hand geprüft |
| 35 | `OperationChatMsg` | `0x006A9D20` | 151 | Aufrufgraph (geprüft) |
| 36 | `OperationFindUser` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 37 | `OperationCloseChannel` | `0x006A9DC0` | 215 | Aufrufgraph (geprüft) |
| 38 | `OperationAddUser` | `0x006AAA50` | 172 | Aufrufgraph (geprüft) |
| 39 | `OperationRemoveUser` | `0x006AA580` | 219 | Aufrufgraph (geprüft) |
| 40 | `CBDisplayChatList` | `0x006A95C0` | 116 | UI-Registrierung |
| 41 | `CBDisplayUserList` | `0x006AA660` | 168 | UI-Registrierung |
| 42 | `CBDisplayChannelTitle` | `0x006A9640` | 86 | UI-Registrierung |
| 43 | `CBCreateRoomClear` | `0x006A8F20` | 135 | UI-Registrierung |
| 44 | `CBInviteRoomInit` | `0x006A96A0` | 255 | UI-Registrierung |
| 45 | `CBEditBoxClear` | `0x006A8FB0` | 55 | UI-Registrierung |
| 46 | `CBFindUserClear` | `0x006A8FF0` | 79 | UI-Registrierung |
| 47 | `CBCreateRoom` | `0x006AAB00` | 483 | UI-Registrierung |
| 48 | `CBCheckPulicOptionClick` | `0x006A9040` | 47 | UI-Registrierung |
| 49 | `CBCheckPrivateOptionClick` | `0x006A9070` | 48 | UI-Registrierung |
| 50 | `CBCheckGuildOptionClick` | `0x006A90A0` | 48 | UI-Registrierung |
| 51 | `CBEnterChatMessage` | `0x006A97A0` | 176 | UI-Registrierung |
| 52 | `CBInviteOpen` | `0x006A9EA0` | 113 | UI-Registrierung |
| 53 | `CBInviteSend` | `0x006A9850` | 61 | UI-Registrierung |
| 54 | `CBFindUser` | `0x006A90D0` | 47 | UI-Registrierung |
| 55 | `CBWhiperBtnStatus` | `0x006A9100` | 28 | UI-Registrierung |
| 56 | `CBSendWhisper` | `0x006A9F20` | 136 | UI-Registrierung |
| 57 | `CBJoinRoom` | `0x006A9120` | 89 | UI-Registrierung |
| 58 | `CBInviteJoinRoom` | `0x006A9890` | 31 | UI-Registrierung |
| 59 | `CBLeaveRoom` | `0x006A98B0` | 65 | UI-Registrierung |
| 60 | `CBQueryPassword` | `0x006A9900` | 77 | UI-Registrierung |
| 61 | `CreateChannel` | `0x006A9180` | 25 | as-register |
| 62 | `JoinChannel` | `0x006A91A0` | 25 | as-register |
| 63 | `FindUser` | `0x006A91C0` | 25 | as-register |

57 von 64 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006aa050` (`0x006AA050`), `ctor_or_dtor_006aa1d0` (`0x006AA1D0`), `~AgcmUIChannel` (`0x006AA400`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBA0` | `m_pcsAgcmCharacter` | `+0x1596C` ist der Self-Character-Zeiger (alle Sender) |
| `0xBD0` | `m_eChannelType` | `SendCreateChannel` |
| `0xDCEC` | `Raum-UIs `m_arAgcdUI[5]`` | `OperationJoinChannel` |
| `0x29AC (Stride)` | `Raum-Widget `m_arRoomWidget[n]`` | `OperationJoinChannel` |

## Client → Server (Chat-Channel-Paket, Typ 0x2C)

Das Modul sendet Anfragen über `AgpmChannel`-Paketbauer; alle benutzen den gemeinsamen Baustein `MakePacketChannel` (`0x00560260`) mit Paket-Typ `0x2C` (44). Operation und Funktion (gegen das Dekompilat gelesen, Werte wie `AGPMCHANNEL_OPERATION_*`):

| Sender (AgcmUIChannel) | Bauer (AgpmChannel) | Operation |
|---|---|---|
| `SendCreateChannel` (`0x006A89B0`) | `MakePacketCreateChannel` (`0x00560310`) | 1 CREATE |
| `SendPacketJoinChannel` (`0x006A8B00`) | `MakePacketJoinChannel` (`0x00560380`) | 3 JOIN |
| `SendPacketLeaveChannel` (`0x006A8BA0`) | `MakePacketLeaveChannel` (`0x005603B0`) | 4 LEAVE |
| `SendPacketInvitation` (`0x006A8CF0`) | `MakePacketInvitation` (`0x005604E0`) | 7 INVITATION |
| `SendPacketPassword` (`0x006A8C40`) | `MakePacketPassword` (`0x00560480`) | 8 PASSWORD |
| `SendPacketChatMsg` (`0x006A8A50`) | `MakePacketChatMsg` (`0x00560410`) | 9 CHATMSG |
| `SendPacketFindUser` (`0x006A8DA0`) | `MakePacketFindUser` (`0x00560550`) | 10 FIND_USER |

Jedes Paket wird mit `SendPacket` verschickt. Die Felder der Pakete stehen im Bericht [AgpmChannel](AgpmChannel.md).

## Chat-Räume

`OperationJoinChannel` (`0x006AA420`) sucht unter den fünf Raum-Widgets (`AGPDCHANNEL_MAX_JOIN` = 5, je `0x29AC` Byte, Zeiger bei `+0xDCEC`) das erste im Status „hinzugefügt“, setzt es zurück, öffnet die UI und gibt beim Erstellen eines Raums die Systemmeldung `UI_MESSAGE_CHANNEL_CREATE_MESSAGE` aus. Der Chatpuffer eines Raums fasst 0x2800 (10240) Byte (Anhängen in `0x006A99A0`).
`CreateChannelData` (`0x006AA850`) erzeugt das Channel-Objekt aus den Paketdaten (laut Quelle wird die Benutzerliste an `;` zerlegt).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Sieben Methoden sind nicht zugeordnet (u. a. `OnDestroy`, `OnIdle`, `RefreshChatRoomUserList`, `OperationFindUser`); sie sind klein oder eingefaltet.
- Ein Sequenz-Vorschlag (`RefreshChatRoomUserList` → `0x006A9AC0`) wurde verworfen, weil er auf einen Suchhelfer (`std::find`-Muster) zeigt.
- Die Paketfelder wurden hier nicht erneut geprüft; siehe den Bericht des Moduls `AgpmChannel`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, gemeinsamer Rumpf: 2, nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmChannel`](AgpmChannel.md)
