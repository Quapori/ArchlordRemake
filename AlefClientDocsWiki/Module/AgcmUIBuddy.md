# AgcmUIBuddy (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIBuddy` (Freundesliste, Bannliste, Mentor-System) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Übersetzungseinheit-Reihenfolge, Vtable und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIBuddy/AgcmUIBuddy.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 92 von 97 Quellmethoden sind zugeordnet; in diesem Durchgang kamen 26 Funktionen hinzu (alle zehn `Send…`, die `Operation…`-Handler, Block- und Mentor-Funktionen), geprüft gegen Dekompilat und Aufrufer.
- **Pakete:** Zehn Sender (fünf Freunde/Bann, vier Mentor, eine Region) in der Reihenfolge der Paketfunktionen von [`AgpmBuddy`](AgpmBuddy.md).
- **Sperroptionen:** Bits 1/2/4 für Flüstern/Handel/Einladung, Meldungen wie in der Quelle.
- **Abweichungen:** keine festgestellt.
- **AgcmUICastle:** Die Quelldatei besteht nur aus dem Include (`AgcmUICastle.cpp`, 2 Zeilen); im Binary gibt es weder eine Klasse noch eine Vtable dazu. Es gibt daher nichts zuzuordnen.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIBuddy.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006AEE00` | 720 | vtable/String |
| 1 | `OnInit` | `0x006AF0D0` | 3276 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `OnIdle` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 4 | `AddEvent` | `0x006AE700` | 710 | Zeichenkette |
| 5 | `AddFunction` | `0x006AE9D0` | 856 | Zeichenkette |
| 6 | `AddUserData` | `0x006AC530` | 436 | Zeichenkette |
| 7 | `AddDisplay` | `0x006AD770` | 327 | Zeichenkette |
| 8 | `CBMentorListRefresh` | `0x006AD8C0` | 22 | UI-Registrierung |
| 9 | `CBBuddyListMemberClear` | `0x006AD8E0` | 137 | UI-Registrierung |
| 10 | `CBBanListMemberClear` | `0x006AD970` | 74 | UI-Registrierung |
| 11 | `CBBuddyUIKeydownESC` | `0x006AD9C0` | 196 | ver |
| 12 | `CBAddBuddy` | `0x006AED30` | 35 | Callback-Registrierung |
| 13 | `CBAddBuddyRequest` | `0x006ADA90` | 35 | Callback-Registrierung |
| 14 | `CBAddBuddyReject` | `0x006AC6F0` | 35 | Callback-Registrierung |
| 15 | `CBRemoveBuddy` | `0x006AED60` | 71 | Callback-Registrierung |
| 16 | `CBOptionsBuddy` | `0x006AEDB0` | 35 | Callback-Registrierung |
| 17 | `CBOnlineBuddy` | `0x006AEDE0` | 26 | Callback-Registrierung |
| 18 | `CBMsgCodeBuddy` | `0x006AC720` | 24 | Callback-Registrierung |
| 19 | `CBRegionInfo` | `0x006ADAC0` | 35 | Callback-Registrierung |
| 20 | `CBInitEnd` | `0x006AB7F0` | 25 | Callback-Registrierung |
| 21 | `CBMentorUIOpen` | `0x006AC740` | 22 | Callback-Registrierung |
| 22 | `CBMentorRequestConfirm` | `0x006ADAF0` | 32 | Callback-Registrierung |
| 23 | `CBMentorDelete` | `0x006ADB10` | 32 | Callback-Registrierung |
| 24 | `CBMentorRequestAccept` | `0x006ADB30` | 32 | Callback-Registrierung |
| 25 | `OperationAddBuddy` | `0x006ADF90` | 163 | ver |
| 26 | `OperationAddRequest` | `0x006AC760` | 87 | ver |
| 27 | `OperationAddReject` | `0x006AB810` | 51 | ver |
| 28 | `OperationRemoveBuddy` | `0x006AE040` | 163 | ver |
| 29 | `OperationOptionsBuddy` | `0x006AE0F0` | 47 | ver |
| 30 | `BlockOptionUpdate` | `0x006ADB50` | 381 | ver |
| 31 | `RefreshBlockOptions` | `0x006AB850` | 83 | ver |
| 32 | `OperationOnlineBuddy` | `0x006AE120` | 247 | ver |
| 33 | `OperationMsgCodeBuddy` | `0x006AB8B0` | 174 | ver |
| 34 | `OperationRegionInfo` | `0x006AC7C0` | 299 | ver |
| 35 | `CBCheckBlockWhisper` | `0x006AE220` | 117 | Callback-Registrierung |
| 36 | `CBCheckBlockTrade` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 37 | `CBCheckBlockInvitation` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 38 | `BuddyListUpdate` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 39 | `RefreshFriendList` | `0x006AC8F0` | 76 | as-register |
| 40 | `RefreshMentorList` | `0x006AC940` | 76 | ver |
| 41 | `RefreshBanList` | `0x006AC990` | 76 | as-register |
| 42 | `RefreshBuddyDetailInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 43 | `CBReturnBuddyOkCancelDelete` | `0x006AC9E0` | 192 | UI-Registrierung |
| 44 | `CBReturnBanOkCancelDelete` | `0x006ACAA0` | 133 | UI-Registrierung |
| 45 | `CBReturnOkCancelBuddyAddRequest` | `0x006AE2A0` | 154 | UI-Registrierung |
| 46 | `CBDisplayFriendList` | `0x006ACB30` | 113 | UI-Registrierung |
| 47 | `CBDisplayFriendSelect` | `0x006AB990` | 110 | UI-Registrierung |
| 48 | `CBDisplayMentorSelect` | `0x006ABA00` | 110 | UI-Registrierung |
| 49 | `CBDisplayMentorRelation` | `0x006ACBB0` | 117 | UI-Registrierung |
| 50 | `CBDisplayAddRequestBuddy` | `0x006ABA70` | 44 | UI-Registrierung |
| 51 | `CBDisplayBanList` | `0x006ACC30` | 116 | UI-Registrierung |
| 52 | `CBDisplayFriendStatus` | `0x006ACCB0` | 162 | UI-Registrierung |
| 53 | `CBDisplayFriendDetailInfo` | `0x006ABAA0` | 179 | UI-Registrierung |
| 54 | `CBDisplayBanSelect` | `0x006ABB60` | 110 | UI-Registrierung |
| 55 | `CBBtnAddDlgOpenClick` | `0x006ABBD0` | 68 | UI-Registrierung |
| 56 | `CBBtnAddBuddyClick` | `0x006AE340` | 223 | UI-Registrierung |
| 57 | `CBBtnDeleteBuddyClick` | `0x006ABC20` | 85 | UI-Registrierung |
| 58 | `CBBtnInviteBuddyClick` | `0x006ADCD0` | 282 | UI-Registrierung |
| 59 | `CBBtnWhisperMsgBuddyClick` | `0x006ADDF0` | 270 | UI-Registrierung |
| 60 | `CBBuddySelect` | `0x006ACD60` | 135 | UI-Registrierung |
| 61 | `CBMentorSelect` | `0x006ACDF0` | 276 | UI-Registrierung |
| 62 | `CBBuddyAddDlgSetFocus` | `0x006ABC80` | 64 | ver |
| 63 | `CBBtnBlockWhisperClick` | `0x006ACF10` | 232 | UI-Registrierung |
| 64 | `CBBtnBlockTradeClick` | `0x006AD000` | 232 | UI-Registrierung |
| 65 | `CBBtnBlockInvitationClick` | `0x006AD0F0` | 232 | UI-Registrierung |
| 66 | `CBBtnAddBanDlgOpenClick` | `0x006ABCC0` | 68 | UI-Registrierung |
| 67 | `CBBtnAddRejectionListClick` | `0x006AE420` | 223 | UI-Registrierung |
| 68 | `CBBtnDeleteRejectionListClick` | `0x006ABD10` | 85 | UI-Registrierung |
| 69 | `CBBanListSelect` | `0x006ADF00` | 140 | UI-Registrierung |
| 70 | `CBBanAddDlgSetFocus` | `0x006ABC80` | 64 | gleiche Adresse wie `CBBuddyAddDlgSetFocus` (vom Linker zusammengefaltet) |
| 71 | `SendAddBuddy` | `0x006ABD70` | 141 | ver |
| 72 | `SendAddRequest` | `0x006ABE00` | 141 | ver |
| 73 | `SendAddReject` | `0x006ABE90` | 141 | ver |
| 74 | `SendRemoveBuddy` | `0x006ABF20` | 141 | ver |
| 75 | `SendRegion` | `0x006ABFB0` | 143 | ver |
| 76 | `SendOption` | `0x006AC040` | 141 | ver |
| 77 | `SendMentorRequestAccept` | `0x006AC0D0` | 141 | ver |
| 78 | `SendMentorRequestReject` | `0x006AC160` | 141 | ver |
| 79 | `SendMentorDelete` | `0x006AC1F0` | 141 | ver |
| 80 | `SendMentorRequest` | `0x006AC280` | 141 | ver |
| 81 | `AddFriend` | `0x006AE500` | 118 | as-register |
| 82 | `RemoveFriend` | `0x006AE580` | 118 | as-register |
| 83 | `AddBan` | `0x006AE600` | 118 | as-register |
| 84 | `RemoveBan` | `0x006AE680` | 118 | as-register |
| 85 | `OpenAddDialog` | `0x006AC310` | 25 | as-register |
| 86 | `OpenFriendList` | `0x006AC330` | 25 | as-register |
| 87 | `OpenBanList` | `0x006AC350` | 25 | as-register |
| 88 | `CBNotInBuddyList` | `0x006AC370` | 81 | UI-Registrierung |
| 89 | `CBNotInBanList` | `0x006AC3D0` | 81 | UI-Registrierung |
| 90 | `CBMentorAddAndDel` | `0x006AD1E0` | 357 | UI-Registrierung |
| 91 | `OperationMentorUIOpen` | `0x006AC430` | 134 | as-register |
| 92 | `OperationMentorUIClose` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 93 | `OperationMentorRequestConfirm` | `0x006AD350` | 132 | ver |
| 94 | `OperationMentorDelete` | `0x006AD3E0` | 141 | ver |
| 95 | `OperationMentorRequestAccept` | `0x006AD470` | 141 | ver |
| 96 | `CBDisplayMentorBtnText` | `0x006AC4C0` | 49 | UI-Registrierung |

92 von 97 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmUIBuddy` (`0x006AC500`), `ctor_or_dtor` (`0x006AD550`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB9C` | `Zeiger auf `AgcmCharacter`` | `+0x1596C` ist der Self-Character (`Send…`) |
| `0xBD8 / 0xBDC / 0xBE0` | `zuletzt gemeldete Sperroptionen Flüstern / Handel / Einladung` | `BlockOptionUpdate` |
| `0xC14 / 0xC18` | `Ereignis-IDs „Anfrage“ / „Ablehnung“` | `OperationAddRequest`, `OperationAddReject` |
| `0xC44` | `Flag `m_bInitEnd`` | `OperationAddBuddy`, `OperationRemoveBuddy` |
| `0xC48…` | `Zwischenspeicher der Regionsinfo (Name und Region)` | `OperationRegionInfo` |

## Adressbereich

`AgcmUIBuddy.cpp` liegt im Binary bei `0x006AB790`–`0x006AF0D0` (`OnAddModule` `0x006AEE00`, `OnInit` `0x006AF0D0` zuletzt). Die Vtable steht bei `0x008D063C`; `OnIdle` und `OnDestroy` (Slots 6 und 7) zeigen beide auf den gemeinsamen `return TRUE`-Rumpf `0x0067AC90`.

## Pakete an den Server

Alle zehn `Send…`-Funktionen haben dieselbe Form: ohne Self-Character Abbruch, sonst Paket über eine `AgpmBuddy::MakePacket…`-Funktion bauen und mit `SendPacket` (`0x004E45A0`) senden. Reihenfolge und Zuordnung (Quellreihenfolge = Adressreihenfolge, gegen den Aufruf der Paketfunktionen geprüft):

| Sender | Adresse | Paketfunktion in `AgpmBuddy` |
|---|---|---|
| `SendAddBuddy` | `0x006ABD70` | `0x0056CDE0` (AddBuddy) |
| `SendAddRequest` | `0x006ABE00` | `0x0056CE00` (AddRequest) |
| `SendAddReject` | `0x006ABE90` | `0x0056CE20` (AddReject) |
| `SendRemoveBuddy` | `0x006ABF20` | `0x0056CE40` (RemoveBuddy) |
| `SendOption` | `0x006AC040` | `0x0056CE60` (UpdateOptions) |
| `SendRegion` | `0x006ABFB0` | `0x0056CE80` (Region, mit Regionsindex 0) |
| `SendMentorRequest` | `0x006AC280` | `0x0056CEB0` |
| `SendMentorDelete` | `0x006AC1F0` | `0x0056CED0` |
| `SendMentorRequestAccept` | `0x006AC0D0` | `0x0056CEF0` |
| `SendMentorRequestReject` | `0x006AC160` | `0x0056CF10` |

Die vier Mentor-Funktionen folgen im Binary derselben Reihenfolge wie `MakePacketMentorRequest/Delete/RequestAccept/RequestReject` in der Quelle.

## Sperroptionen der Bannliste

`BlockOptionUpdate` (`0x006ADB50`) vergleicht die drei Bits des Elements (1 Flüstern, 2 Handel, 4 Einladung) mit dem gespeicherten Zustand (`+0xBD8`, `+0xBDC`, `+0xBE0`) und gibt bei Änderung eine Systemnachricht mit den UI-Texten `BanList_WhisperOption_Enable/Disable`, `BanList_TradeOption_…` und `BanList_InviteOption_…` aus. `OperationOptionsBuddy` (`0x006AE0F0`) ruft vorher `AgpmBuddy::OptionsBuddy`. Das entspricht der Quelle.
`OperationOnlineBuddy` (`0x006AE120`) sucht das Element in beiden Listen (Freunde ab `+0x04`, Bannliste ab `+0x12C4`, je 0x30 Byte) und setzt oder löscht das Online-Bit `0x100000`.

## Callback-Registrierung in OnAddModule (0x006AEE00)

Die 14 Registrierungen stehen im Binary in der Reihenfolge der Quelle (14 von 14); alle Handler sind benannt.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006AE9D0`, `0x006AD770`, `0x006AC530`, `0x006AE700`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (20)

| Name | Id | Handler |
|---|---:|---|
| `BuddyList_Clear` |  | `CBBuddyListMemberClear` |
| `BuddyAddFriend_Click` |  | `CBBtnAddBuddyClick` |
| `BuddyAddDlgOpen_Click` |  | `CBBtnAddDlgOpenClick` |
| `BuddyDeleteList_Click` |  | `CBBtnDeleteBuddyClick` |
| `BuddyInviteFriend_Click` |  | `CBBtnInviteBuddyClick` |
| `BuddyWhiperMsgFriend_Click` |  | `CBBtnWhisperMsgBuddyClick` |
| `BuddyList_Item_Selected` |  | `CBBuddySelect` |
| `BuddyAddDlg_SetFocus` |  | `FUN_006abc80` |
| `BanList_Clear` |  | `CBBanListMemberClear` |
| `BanAdd_Click` |  | `CBBtnAddRejectionListClick` |
| `BanAddDlgOpen_Click` |  | `CBBtnAddBanDlgOpenClick` |
| `BanBlockWhisper_Click` |  | `CBBtnBlockWhisperClick` |
| `BanBlockTrade_Click` |  | `CBBtnBlockTradeClick` |
| `BanBlockInvitation_Click` |  | `CBBtnBlockInvitationClick` |
| `BanDeleteList_Click` |  | `CBBtnDeleteRejectionListClick` |
| `BanList_Item_Selected` |  | `CBBanListSelect` |
| `BanAddDlg_SetFocus` |  | `FUN_006abc80` |
| `Mentor_AddAndDel` |  | `CBMentorAddAndDel` |
| `Mentor_Item_Selected` |  | `CBMentorSelect` |
| `MentorList_Refresh` |  | `CBMentorListRefresh` |

**Anzeige** (10)

| Name | Id | Handler |
|---|---:|---|
| `BuddyFriend_Display` | 0 | `CBDisplayFriendList` |
| `BuddyFriendStatus_Display` | 0 | `CBDisplayFriendStatus` |
| `BuddyFriendDetaulInfo_Display` | 0 | `CBDisplayFriendDetailInfo` |
| `BuddyFriendSelect_Display` | 0 | `CBDisplayFriendSelect` |
| `AddRequestBuddy_Display` | 0 | `CBDisplayAddRequestBuddy` |
| `Ban_Display` | 0 | `CBDisplayBanList` |
| `Ban_Display_Select` | 0 | `CBDisplayBanSelect` |
| `Mentor_BtnText` | 0 | `CBDisplayMentorBtnText` |
| `MentorSelect_Display` | 0 | `CBDisplayMentorSelect` |
| `Mentor_Relation` | 0 | `CBDisplayMentorRelation` |

**UserData** (10)

| Name | Id | Handler |
|---|---:|---|
| `BuddyFriendList_UD` |  | – |
| `BanList_UD` |  | – |
| `AddRequest_UD` |  | – |
| `BuddyDetailInfo_UD` |  | – |
| `BanBlockWhisper_UD` |  | – |
| `BanBlockTrade_UD` |  | – |
| `BanBlockInvitation_UD` |  | – |
| `MentorList_UD` |  | – |
| `Mentor_Btn` |  | – |
| `Mentor_Enable_Invite_Button` |  | – |

**Ereignis** (21)

| Name | Id | Handler |
|---|---:|---|
| `BuddyMain_Open` | 0 | – |
| `BuddyMain_Close` | 0 | – |
| `BuddyAddDlg_Open` | 0 | – |
| `BanList_Open` | 0 | – |
| `BanList_Close` | 0 | – |
| `BuddyBanAddDlg_Open` | 0 | – |
| `AddRejectDlg_Open` | 0 | – |
| `BuddyAlreayExist_MsgBox` | 0 | – |
| `BuddyFullFriendList_MsgBox` | 0 | – |
| `BuddyFullBanList_MsgBox` | 0 | – |
| `BuddyOfflineOrNotExist_MsgBox` | 0 | – |
| `BuddyBanUser_MsgBox` | 0 | – |
| `BuddyInvalidUser_MsgBox` | 0 | – |
| `BuddyIDLengthWarning_Open` | 0 | – |
| `FriendAddDlg_SetFocus` | 0 | – |
| `BanAddDlg_SetFocus` | 0 | – |
| `MentorUI_Open` | 0 | – |
| `MentorUI_Close` | 0 | – |
| `BuddyDeleteBuddyUserConfirm_MsgBox` |  | `CBReturnBuddyOkCancelDelete` |
| `BuddyDeleteBanUserConfirm_MsgBox` |  | `CBReturnBanOkCancelDelete` |
| `BuddyAddRequestConfirm_Open` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`Send…`, `BlockOptionUpdate`, `OperationOnlineBuddy`, `OperationMentorRequestConfirm`).

## Grenzen

- Fünf Methoden sind nicht zugeordnet (`CBCheckBlockTrade`, `CBCheckBlockInvitation`, `BuddyListUpdate`, `RefreshBuddyDetailInfo`, `OperationMentorUIClose`); sie haben keine eindeutigen Aufrufbeziehungen im Binary.
- Die Anzeigefunktionen und die Mentor-Dialoge wurden nur auf Struktur geprüft.
- Die Paketfelder stehen im Bericht des Moduls `AgpmBuddy`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 1, gemeinsamer Rumpf: 2, nicht im Client: 3, ohne Kandidat: 1.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `BuddyListUpdate` (`0x006AD500`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmBuddy`](AgpmBuddy.md)
