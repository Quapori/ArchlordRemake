# AgcmUILogin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUILogin` (Login-Oberfläche: Anmeldung, Charakterauswahl/-erstellung, Server- und Welt-Auswahl, Fehlermeldungen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmUILogin/AgcmUILogin.cpp`. Die anderen Dateien im Ordner (`AgcmUIServerSelect`, `AgcmUILoginSetting`, `AgcuUI…`) sind eigene Klassen und nicht Teil dieser Analyse. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 78 von 106 Quellmethoden sind zugeordnet; die Anker sind die UI-Registrierungen, die Callback-Reihenfolge und der Aufrufgraph.
- **Login-Ergebnisse:** Alle 21 Ergebniscodes mit Reaktion des Clients stehen in der Tabelle unten (Codes 13 und 14 haben auch in der Quelle keinen Case). Für den Login-Server wichtig: Falsche Konto- oder Passwortdaten, zu viele Fehlversuche und Doppelanmeldung beenden den Client.
- **Regionen:** Der Client enthält die Region-Zweige für Korea, China, Taiwan und Global (siehe unten); das Verhalten richtet sich nach `DAT_008AD470`.
- **Registrierungen:** 24 statt 27 Callbacks erkennbar, drei davon nicht zuordenbar.
- **Abweichungen:** keine bestätigte; die Zahl der Registrierungen (24/27) ist ein Registrierungsbefund, keine nachgewiesene Verhaltensänderung.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUILogin.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00610180` | 854 | Zeichenketten/Konstanten (geprüft) |
| 1 | `OnInit` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 2 | `OnIdle` | `0x0060EB60` | 1470 | Zeichenkette |
| 3 | `AddEvent` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 4 | `AddFunction` | `0x0060FE30` | 837 | Zeichenkette |
| 5 | `AddUserData` | `0x00609E70` | 177 | Zeichenkette |
| 6 | `AddDisplay` | `0x0060C160` | 615 | Zeichenkette |
| 7 | `InitAgcmUILogin` | `0x0060C3D0` | 74 | Aufrufgraph (geprüft) |
| 8 | `LoadTemplates` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 9 | `SetLoginMode` | `0x0060CD90` | 297 | Aufrufgraph (geprüft) |
| 10 | `GetLoginMode` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 11 | `LoadLoginMap` | `0x0060C420` | 422 | Aufrufgraph (geprüft) |
| 12 | `LoadSelectMap` | `0x0060C5D0` | 242 | Zeichenketten/Konstanten (geprüft) |
| 13 | `LoadCreateMap` | `0x0060C6D0` | 360 | Zeichenketten/Konstanten (geprüft) |
| 14 | `SetLoginProcess` | `0x0060C840` | 227 | Zeichenkette |
| 15 | `StartLoginProcess` | `0x0060F900` | 435 | Aufrufgraph (geprüft) |
| 16 | `OpenMoveToHangame` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 17 | `CharacterClick` | `0x0060C930` | 296 | Aufrufgraph (geprüft) |
| 18 | `UpdateCompenInfo` | `0x00609F30` | 340 | Aufrufgraph (geprüft) |
| 19 | `CharacterDoubleClick` | `0x0060F120` | 247 | Aufrufgraph (geprüft) |
| 20 | `SelectCharacterAtLoginMain` | `0x0060CEC0` | 429 | Aufrufgraph (geprüft) |
| 21 | `CreateCharacter` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 22 | `AddMyCharacterInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 23 | `RemoveMyCharacterInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 24 | `UpdateSlotCharInfo` | `0x0060A220` | 355 | Aufrufgraph (geprüft) |
| 25 | `GetMyCharacterCount` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 26 | `GetMyCharacterInfoIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 27 | `GetMyCharacterInfoIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 28 | `MyCharacterAllUpdatePosition` | `0x0060A410` | 336 | Aufrufgraph (geprüft) |
| 29 | `DeleteAllMyCharacter` | `0x0060A560` | 175 | Aufrufgraph (geprüft) |
| 30 | `RemoveSelectedMyCharacter` | `0x0060FAC0` | 402 | Aufrufgraph (geprüft) |
| 31 | `OpenLoadingWindow` | `0x0060A610` | 196 | Zeichenkette |
| 32 | `CloseLoadingWindow` | `0x0060A6F0` | 102 | Zeichenkette |
| 33 | `OnLoginResult` | `0x0060D070` | 1816 | Zeichenketten/Konstanten (geprüft) |
| 34 | `CalcMurdererLevelByPoint` | `0x0060A760` | 49 | Aufrufgraph (geprüft) |
| 35 | `CBLoginMainCreateButtonClick` | `0x0060D7F0` | 807 | UI-Registrierung |
| 36 | `CBLoginMainCancelButtonClick` | `0x0060DB20` | 499 | UI-Registrierung |
| 37 | `CBLoginMainSelectButtonClick` | `0x0060DD20` | 214 | UI-Registrierung |
| 38 | `CBLoginMainDeleteButtonClick` | `0x0060A7A0` | 357 | UI-Registrierung |
| 39 | `CBCharInfoClick01` | `0x0060CAC0` | 88 | UI-Registrierung |
| 40 | `CBCharInfoClick02` | `0x0060CB20` | 88 | UI-Registrierung |
| 41 | `CBCharInfoClick03` | `0x0060CB80` | 88 | UI-Registrierung |
| 42 | `CBCompensationClick01` | `0x0060CBE0` | 19 | UI-Registrierung |
| 43 | `CBCompensationClick02` | `0x0060CC00` | 19 | UI-Registrierung |
| 44 | `CBCompensationClick03` | `0x0060CC20` | 19 | UI-Registrierung |
| 45 | `OnCompensationClick` | `0x0060A910` | 384 | Aufrufgraph (geprüft) |
| 46 | `CBCompensationSetFocus` | `0x0060AA90` | 178 | UI-Registrierung |
| 47 | `CBCompensationKillFocus` | `0x0060AB50` | 36 | UI-Registrierung |
| 48 | `CBOpenHangameWeb` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 49 | `CBUnionSelectWindowReturnIDPassworldInput` | `0x0060CC40` | 76 | UI-Registrierung |
| 50 | `CBConfirmPassword` | `0x0060ABB0` | 130 | UI-Registrierung |
| 51 | `CBConfirmDeleteChar` | `0x0060FC60` | 50 | UI-Registrierung |
| 52 | `CBCancelDeleteConfirm` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 53 | `CBCharRenameOkButtonClick` | `0x0060AC40` | 106 | UI-Registrierung |
| 54 | `CBCharRenameCancelButtonClick` | `0x0060ACB0` | 62 | UI-Registrierung |
| 55 | `CBOpenExitWindow` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 56 | `CBReturnGame` | `0x0060ACF0` | 235 | UI-Registrierung |
| 57 | `CBReturnLoginCharacterSelectMode` | `0x0060F220` | 523 | UI-Registrierung |
| 58 | `CBLoginReturnRemoveCharacter` | `0x0060FCA0` | 57 | Aufrufgraph (geprüft) |
| 59 | `CBLoginReturnRemoveDuplicateAccount` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 60 | `CBLoginReturnDisconnect` | `0x0060ADE0` | 103 | Zeichenkette |
| 61 | `CBReturnNotTester` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 62 | `CBResultNotApplied` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 63 | `CBIDFailed` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 64 | `CBPasswordFailed` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 65 | `CBEncryptCode` | `0x0060AF10` | 83 | cbreg:AgcmUILogin |
| 66 | `CBInvalidClientVersion` | `0x0060AF70` | 47 | cbreg:AgcmUILogin |
| 67 | `CBGetUnionInfo` | `0x0060DE00` | 284 | cbreg:AgcmUILogin |
| 68 | `CBGetMyCharacterName` | `0x0060AFA0` | 47 | cbreg:AgcmUILogin |
| 69 | `CBGetMyCharacterNameFinish` | `0x0060DF20` | 391 | cbreg:AgcmUILogin |
| 70 | `CBGetMyCharacterInfoFinish` | `0x0060E0B0` | 291 | Aufrufgraph (geprüft) |
| 71 | `CBEnterGameEnd` | `0x0060E1E0` | 681 | Zeichenketten/Konstanten (geprüft) |
| 72 | `CBGetNewCharacterName` | `0x0060E490` | 287 | cbreg:AgcmUILogin |
| 73 | `CBGetNewCharacterInfoFinish` | `0x0060E5B0` | 214 | Aufrufgraph (geprüft) |
| 74 | `CBRemoveCharacter` | `0x0060CC90` | 132 | cbreg:AgcmUILogin |
| 75 | `CBLoginResult` | `0x0060E690` | 33 | Aufrufgraph (geprüft) |
| 76 | `CBCompensationInfo` | `0x0060AFD0` | 248 | cbreg:AgcmUILogin |
| 77 | `CBMapSectorChangePreCallback` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 78 | `CBMapSectorChangeCallback` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 79 | `CBMapLoadSector` | `0x0060B200` | 168 | Zeichenketten/Konstanten (geprüft) |
| 80 | `CBAddCharacter` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 81 | `CBGameServerError` | `0x0060E6C0` | 326 | Aufrufgraph (geprüft) |
| 82 | `CBResultDisconnectByAnotherUser` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 83 | `CBDisconnectGameServer` | `0x0060B610` | 68 | cbreg:AgcmUILogin |
| 84 | `CBLoadingComplete` | `0x0060B660` | 35 | cbreg:AgcmUILogin |
| 85 | `CBSetSelfCharacter` | `0x0060E810` | 259 | cbreg:AgcmUILogin |
| 86 | `CBReturnToLoginEndProcess` | `0x0060E920` | 446 | Zeichenketten/Konstanten (geprüft) |
| 87 | `CBGetWorldAll` | `0x0060B690` | 135 | cbreg:AgcmUILogin |
| 88 | `CBUpdateWorld` | `0x0060B720` | 26 | cbreg:AgcmUILogin |
| 89 | `CBGetCharCount` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 90 | `CBKeydownCloseAllUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 91 | `CBDisplaySlotCharName` | `0x0060B770` | 161 | UI-Registrierung |
| 92 | `CBDisplaySlotCharLevel` | `0x0060B820` | 213 | UI-Registrierung |
| 93 | `CBDisplaySlotCharExp` | `0x0060B900` | 392 | UI-Registrierung |
| 94 | `CBDisplaySlotCharGuild` | `0x0060BA90` | 352 | UI-Registrierung |
| 95 | `CBDisplaySlotCharVillian` | `0x0060BBF0` | 276 | UI-Registrierung |
| 96 | `CBDisplayGameServerName` | `0x0060BD10` | 88 | UI-Registrierung |
| 97 | `CBDisplayOldCharID` | `0x0060BD70` | 82 | UI-Registrierung |
| 98 | `CBDisplayCompenCaption` | `0x0060BDD0` | 128 | UI-Registrierung |
| 99 | `CBDisplayConnectRename` | `0x0060BE50` | 175 | UI-Registrierung |
| 100 | `CBPing` | `0x0060BF00` | 202 | cbreg:AgcmUILogin |
| 101 | `PreLoadAllCharacterTypes` | `0x0060BFD0` | 88 | Aufrufgraph (geprüft) |
| 102 | `ParsePatchCodeString` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 103 | `ParseChannelingCodeString` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 104 | `ConnectLoginServer` | `0x0060C030` | 122 | Aufrufgraph (geprüft) |
| 105 | `ReConnectLoginServer` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |

78 von 106 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x0060F520`), `~AgcmUILogin` (`0x0060F730`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `AgcmLogin +0xC14` | `Login-Modus` | `SelectCharacterAtLoginMain`, `CBGameServerError`, `OnLoginResult` |
| `0x119C` | `Umbenennen-Sperre (m_bRenameBlock)` | `OnLoginResult` (Codes 9–11) |
| `0xCAC` | `Server-Auswahl abgeschlossen` | `OnLoginResult` (Code 16) |
| `0x1158` | `Verweis auf AgcmLogin-Daten (Konto/Welt/Charakter)` | `OnLoginResult` (Codes 21/22) |

## Reaktion auf Login-Ergebnisse (OnLoginResult 0x0060D070)

Der Client behandelt die Ergebniscodes `AGPMLOGIN_RESULT_*` des Login-Servers in einem Switch (1816 Byte). Codes, Namen und Verhalten im 2017er Binary (gegen die Quelle gelesen); „Quit“ = `RsEventHandler(rsQUITAPP)` (`FUN_0064D1E0(0x23)`), das Programm beendet sich:

| Code | Name (Quelle) | Reaktion im Binary |
|---:|---|---|
| 0 | `INVALID_ACCOUNT` | UI-Ereignis „Fehlgeschlagen“ (`+0xF30`), Quit, danach Browser je nach Region |
| 1 | `INVALID_PASSWORD` | Zähler der Fehlversuche erhöhen (`0x007486E0`), Quit, Browser je nach Region |
| 2 | `INVALID_PASSWORD_LIMIT_EXCEED` | UI-Ereignis „Trennung wegen falschen Passworts“ (`+0xE38`), Quit, Browser je nach Region |
| 3 | `NOT_APPLIED` | UI-Ereignis (`+0xF3C`) |
| 4 | `NOT_ENOUGH_AGE` | nur Region Korea (`0`): Hinweis über [`AgcmWorld`](AgcmWorld.md); sonst UI-Ereignis (`+0xEFC`) |
| 5 | `NOT_BETA_TESTER` | UI-Ereignis (`+0xF38`) |
| 6 | `DISCONNECTED_BY_DUPLICATE_ACCOUNT` | UI-Ereignis (`+0xEF0`), Quit |
| 7 | `CHAR_NAME_ALREADY_EXIST` | UI-Ereignis (`+0xE14`), Modus zurück auf Charakter-Erstellung (4), sofern kein Umbenennen läuft |
| 8 | `FULL_SLOT` | keine Reaktion |
| 9 | `RENAME_SUCCESS` | Ereignis „Umbenennen schließen“ (`+0xF04`), Umbenennen-Sperre gesetzt (`+0x119C = 1`) |
| 10 | `RENAME_FAIL` | Ereignis „Umbenennen fehlgeschlagen“ (`+0xF08`) und „schließen“ (`+0xF04`), Sperre gelöscht |
| 11 | `RENAME_SAME_OLD_NEW_ID` | Ereignis (`+0xF0C`), Sperre gelöscht |
| 12 | `UNMAKABLE_CHAR_NAME` | Ereignis „Ungültiger Name“ (`+0xE34`), Modus Charakter-Erstellung (4) |
| 13, 14 | `NEED_EKEY`, `CANNOT_DISCONNECT_TRY_LATER` | kein Case (wie in der Quelle) |
| 15 | `GAMESERVER_NOT_READY` | Hinweis-Dialog + Ereignis (`+0xE24`) |
| 16 | `GAMESERVER_FULL` | Server-Auswahl zurückgesetzt (`+0xCAC = 0`), Ereignis (`+0xEF4`) |
| 17 | `ACCOUNT_BLOCKED` | Meldung `LoginAccountBlocked` mit eingesetztem Zahlenwert im OK-Dialog |
| 18 | `CANT_DELETE_CHAR_B4_1DAY` | OK-Dialog `LoginCantDelete1Day` |
| 19 | `CANT_DELETE_CHAR_GUILD_MASTER` | OK-Dialog `GuildBattleMember_NotEraseMaster` |
| 20 | `NOT_BETAKEY` | OK-Dialog `Aleart_Login_NotBetaKeyUser` |
| 21 | `CHECK_CREATE_JUMPING_CHARACTER_SUCCESS` | Bestätigungsdialog `JumpingPromotion`, dann `SendCreateCharacter`; Modus 5 (Warten auf eigene Charaktere), Meldung `LOGIN_WAITING` |
| 22 | `CHECK_CREATE_JUMPING_CHARACTER_FAIL` | wie 21 ohne Bestätigungsdialog |

Damit lässt sich ein privater Login-Server gezielt prüfen: Die Codes 0, 1, 2 und 6 beenden den Client, 7 und 12 führen in die Charaktererstellung zurück, 15/16 melden den Spielserver als nicht bereit/voll.

## Regionen-Flag (DAT_008AD470)

Der Client unterscheidet im Code die Dienstregionen `ApServiceArea`: 0 Korea, 1 China, 2 Taiwan, 3 Japan, 4 Global. Dasselbe Flag steuert z. B. die Anti-Sucht-Anzeige ([`AgcmUIMain`](AgcmUIMain.md), Region 1) und die Wortreihenfolge der Attributtexte ([`AgcmUICharacter`](AgcmUICharacter.md), Region 4). Bei Fehlanmeldungen öffnet der Client regionsabhängig diese Seiten: China `reg.sdo.com`, Global `www.webzen.com`, Taiwan `archlord.wpark.com.tw`, sonst `id.naver.com/help/work.php?work=pwinquiry`.

## Login-Modi (AgcmLogin +0xC14)

Das Modul liest und setzt den Modus des [`AgcmLogin`](AgcmLogin.md) (Offset `+0xC14`), Werte wie `AGCMLOGIN_MODE_*` der Quelle: 0 PRE_LOGIN, 1 ID_PASSWORD_INPUT, 2 UNION_SELECT, 3 SERVER_SELECT, 4 CHARACTER_CREATE, 5 WAIT_MY_CHARACTER, 6 WAIT_MY_NEW_CHARACTER, 7 CHARACTER_SELECT, 8 POST_LOGIN_LOADING, 9 POST_LOGIN, 10 WAIT_DISCONNECT, 11 LOGIN_SERVER_SELECT. `SelectCharacterAtLoginMain` (`0x0060CEC0`) arbeitet nur im Modus 7, `CBGameServerError` (`0x0060E6C0`) nur im Modus 10.

## Callback-Registrierung in OnAddModule (0x00610180)

Die Quelle meldet 27 Callbacks an, im Binary sind 24 erkennbar. Die Handler 0–11 und 18–26 stehen in gleicher Reihenfolge; sechs Quelleinträge (`CBAddCharacter`, `CBResultDisconnectByAnotherUser`, `CBMapSectorChangePreCallback`, `CBMapSectorChangeCallback`, `CBMapLoadSector`, `CBKeydownCloseAllUI`) stehen nur mit drei Einträgen (`0x0060B2B0`, `0x0060B5D0`, `0x0060B740`) im Binary; die Zuordnung dieser drei ist offen.

| Setter (Quelle) | Handler | Adresse |
|---|---|---|
| `EncryptCodeSuccess` | `CBEncryptCode` | `0x0060AF10` |
| `InvalidClientVersion` | `CBInvalidClientVersion` | `0x0060AF70` |
| `UnionInfo` | `CBGetUnionInfo` | `0x0060DE00` |
| `CharacterName` | `CBGetMyCharacterName` | `0x0060AFA0` |
| `CharacterNameFinish` | `CBGetMyCharacterNameFinish` | `0x0060DF20` |
| `CharacterInfoFinish` | `CBGetMyCharacterInfoFinish` | `0x0060E0B0` |
| `EnterGameEnd` | `CBEnterGameEnd` | `0x0060E1E0` |
| `NewCharacterName` | `CBGetNewCharacterName` | `0x0060E490` |
| `NewCharacterInfoFinish` | `CBGetNewCharacterInfoFinish` | `0x0060E5B0` |
| `RemoveCharacter` | `CBRemoveCharacter` | `0x0060CC90` |
| `LoginResult` | `CBLoginResult` | `0x0060E690` |
| `CompensationInfo` | `CBCompensationInfo` | `0x0060AFD0` |
| `GameServerError` | `CBGameServerError` | `0x0060E6C0` |
| `GameServerDisconnect` | `CBDisconnectGameServer` | `0x0060B610` |
| `LoadingComplete` | `CBLoadingComplete` | `0x0060B660` |
| `SetSelfCharacter` | `CBSetSelfCharacter` | `0x0060E810` |
| `ResultGetWorldAll` | `CBGetWorldAll` | `0x0060B690` |
| `UpdateWorld` / `GetCharCount` | `CBUpdateWorld` / `CBGetCharCount` | `0x0060B720` (beide, gleicher Rumpf) |
| `EndProcess` | `CBReturnToLoginEndProcess` | `0x0060E920` |
| `Ping` | `CBPing` | `0x0060BF00` |

## Murderer-Stufen

`CalcMurdererLevelByPoint` (`0x0060A760`): Punktestand 40 → Stufe 1, 60 → Stufe 2, 100 → Stufe 3, sonst 0; entspricht `AGPMCHAR_MURDERER_LEVEL1/2/3_POINT`.

## Abweichungen von der EP8-Quelle

- Keine bestätigte Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnLoginResult`, `ConnectLoginServer`, `CBGameServerError`, `CalcMurdererLevelByPoint`, `SelectCharacterAtLoginMain`, `CBEncryptCode`, `CBLoadingComplete`, `CBDisconnectGameServer`).

## Grenzen

- Rund ein Viertel der Methoden ist nicht zugeordnet (Kartenladen, Charakter-Listen, Hangame-Fenster u. a.).
- Die Zuordnung der UI-Ereignisse zu Offsets (`+0xF30` usw.) folgt der Reihenfolge der Quelle und ist nicht durch die Ereignisnamen im Binary bestätigt.
- Die Regionsabhängigkeit wurde nur an `OnLoginResult` gelesen; in welcher Region der Client läuft, ergibt sich aus Konfiguration/Start und wurde nicht untersucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 8, nicht im Client: 4, ohne Kandidat: 9, zugeordnet: 6.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `CBResultDisconnectByAnotherUser` | 8 | `0x0060B5D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddMyCharacterInfo` | 19 | `0x0060A1A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEvent` | 45 | `0x0060FCE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBAddCharacter` | 86 | `0x0060B2B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CBMapSectorChangePreCallback` | 30 | `0x0060B0D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateCharacter` | 22 | `0x0060A090` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmLogin`](AgcmLogin.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmWorld`](AgcmWorld.md)
- **Erwähnt in:** [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmTargeting`](AgcmTargeting.md)
