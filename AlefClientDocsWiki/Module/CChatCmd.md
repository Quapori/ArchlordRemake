# CChatCmd (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `CChatCmd` (Chat-Befehle mit „/“) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `CChattingCommander.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 54 von 55 Quellmethoden sind zugeordnet; die Befehls-Callbacks ergeben sich aus ihren Namen (Zeichenketten bei der Registrierung).
- **Registrierung:** alle 46 aktiven Befehle der Quelle (`OnReloadNPCDialog` ist dort auskommentiert).
- **Abweichungen:** keine (Shout ist auch in der Quelle abgeschaltet).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CChatCmd.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnRegisterCmdCallBack` | `0x00712440` | 814 | vtable/String |
| 1 | `OnLoadChatCmd` | `0x007130C0` | 307 | vtable/String |
| 2 | `OnParseCommand` | `0x00711D20` | 350 | vtable/String |
| 3 | `_AddChatCmd` | `0x00712D80` | 626 | ver |
| 4 | `_AddCmdCallBack` | `0x00712250` | 279 | ver |
| 5 | `_GetCmdCallBack` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `_ParseParamType` | `0x00710420` | 186 | Zeichenkette |
| 7 | `_ParseParamValue` | `0x00711010` | 219 | ver |
| 8 | `_RunCmdCallBack` | `0x007104E0` | 29 | ver |
| 9 | `CallBack_OnTestEditChatting` | `0x007111A0` | 9 | UI-Registrierung |
| 10 | `CallBack_OnAddTextFilter` | `0x007112B0` | 82 | UI-Registrierung |
| 11 | `CallBack_OnSocialAnimation` | `0x00711310` | 64 | UI-Registrierung |
| 12 | `CallBack_OnFlagImoticon` | `0x00711350` | 48 | UI-Registrierung |
| 13 | `CallBack_OnDrawOcclusion` | `0x00710500` | 44 | UI-Registrierung |
| 14 | `CallBack_OnReloadTitle` | `0x00710530` | 39 | UI-Registrierung |
| 15 | `CallBack_OnChangeCameraMode` | `0x00711380` | 74 | UI-Registrierung |
| 16 | `CallBack_OnReportModule` | `0x007113D0` | 140 | UI-Registrierung |
| 17 | `CallBack_OnCheckMemory` | `0x00710560` | 58 | UI-Registrierung |
| 18 | `CallBack_OnGuildBattleRequest` | `0x00711460` | 146 | UI-Registrierung |
| 19 | `CallBack_OnGuildBattleCancel` | `0x007105A0` | 265 | UI-Registrierung |
| 20 | `CallBack_OnGuildBattleSurrender` | `0x007105C0` | 28 | UI-Registrierung |
| 21 | `CallBack_OnGuildLeaveOut` | `0x007105E0` | 150 | UI-Registrierung |
| 22 | `CallBack_OnChangePerspective` | `0x00711500` | 169 | UI-Registrierung |
| 23 | `CallBack_OnChangeWideScreen` | `0x00710600` | 100 | UI-Registrierung |
| 24 | `CallBack_OnChangeSoundEffect` | `0x007115B0` | 68 | gleiche Adresse wie `CallBack_OnTest3DSound` (vom Linker zusammengefaltet) |
| 25 | `CallBack_OnScriptLua` | `0x00711600` | 199 | UI-Registrierung |
| 26 | `CallBack_OnViewFPS` | `0x00710670` | 33 | UI-Registrierung |
| 27 | `CallBack_OnTest3DSound` | `0x007115B0` | 68 | gleiche Adresse wie `CallBack_OnChangeSoundEffect` (vom Linker zusammengefaltet) |
| 28 | `CallBack_OnChangeTime` | `0x007116D0` | 197 | UI-Registrierung |
| 29 | `CallBack_OnToggleMatD3DFX` | `0x007106A0` | 90 | UI-Registrierung |
| 30 | `CallBack_OnInviteParty` | `0x007117A0` | 384 | UI-Registrierung |
| 31 | `CallBack_OnSendMsgShout` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 32 | `CallBack_OnSendMsgJoin` | `0x00711920` | 104 | UI-Registrierung |
| 33 | `CallBack_OnSendMsgLeave` | `0x00711990` | 104 | UI-Registrierung |
| 34 | `CallBack_OnMoveToPosition` | `0x00711A00` | 183 | UI-Registrierung |
| 35 | `CallBack_OnRejectTradeOn` | `0x00710700` | 37 | UI-Registrierung |
| 36 | `CallBack_OnRejectTradeOff` | `0x00710730` | 37 | UI-Registrierung |
| 37 | `CallBack_OnRejectPartyOn` | `0x00710760` | 37 | UI-Registrierung |
| 38 | `CallBack_OnRejectPartyOff` | `0x00710790` | 37 | UI-Registrierung |
| 39 | `CallBack_OnRejectGuildOn` | `0x007107C0` | 37 | UI-Registrierung |
| 40 | `CallBack_OnRejectGuildOff` | `0x007107F0` | 37 | UI-Registrierung |
| 41 | `CallBack_OnRejectGuildBattleOn` | `0x00710820` | 37 | UI-Registrierung |
| 42 | `CallBack_OnRejectGuildBattleOff` | `0x00710850` | 37 | UI-Registrierung |
| 43 | `CallBack_OnRejectGuildRelationOn` | `0x00710880` | 37 | UI-Registrierung |
| 44 | `CallBack_OnRejectGuildRelationOff` | `0x007108B0` | 37 | UI-Registrierung |
| 45 | `CallBack_OnRejectBattleOn` | `0x007108E0` | 37 | UI-Registrierung |
| 46 | `CallBack_OnRejectBattleOff` | `0x00710910` | 37 | UI-Registrierung |
| 47 | `CallBack_OnRejectBuddyOn` | `0x00710940` | 40 | UI-Registrierung |
| 48 | `CallBack_OnRejectBuddyOff` | `0x00710970` | 40 | UI-Registrierung |
| 49 | `CallBack_OnReloadGuide` | `0x007109A0` | 75 | UI-Registrierung |
| 50 | `CallBack_OnReloadCamSetting` | `0x007109F0` | 144 | UI-Registrierung |
| 51 | `CallBack_OnNoticeMessage` | `0x00711AC0` | 194 | UI-Registrierung |
| 52 | `CallBack_OnNoticeMessageTest` | `0x00711B90` | 194 | UI-Registrierung |
| 53 | `CallBack_OnReloadQuest` | `0x00710A80` | 216 | UI-Registrierung |
| 54 | `CallBack_OnReloadWorldmap` | `0x00710B60` | 41 | UI-Registrierung |

54 von 55 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00712cb0` (`0x00712CB0`), `ctor_or_dtor_00712d20` (`0x00712D20`), `~CChatCmd` (`0x007130A0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Befehlseintrag +0x18` | `Zeiger auf den Handler (`m_fnCallBack`)` | `_RunCmdCallBack` |

## Umfang

`CChatCmd` ist die Klasse hinter den Chat-Befehlen mit `/` (`CChattingCommander.cpp`, 55 Methoden). Der Name der Datei und der Klasse unterscheiden sich; im Binary liegt sie bei `0x00710290`–`0x00713200`.

## Befehlsverarbeitung

`OnParseCommand` (`0x00711D20`) verlangt ein führendes `/`, trennt Befehl und Parameter am ersten Leerzeichen (laut Quelle höchstens 64 bzw. 256 Zeichen), sucht den Befehl in der Tabelle, parst die Parameter (`_ParseParamValue`, `0x00711010`: Typ 1 `atoi`, Typ 2 `atof` u. a.) und ruft den Handler (`_RunCmdCallBack`, `0x007104E0`, Zeiger bei `+0x18` des Befehlseintrags). `_AddCmdCallBack` (`0x00712250`) trägt die Handler ein, `_AddChatCmd` (`0x00712D80`) liest laut Quelle einen Befehl samt Parametern aus einem XML-Knoten (`Param`, `ParamType`, `DefaultValue`); im Binary ruft es `_ParseParamType` (`0x00710420`) auf.

## Registrierte Befehls-Callbacks (OnRegisterCmdCallBack, 0x00712440)

Im Binary werden **46** Callbacks registriert, in derselben Reihenfolge und mit denselben Namen wie in der Quelle. `CallBack_OnReloadNPCDialog` ist in der Quelle auskommentiert (Registrierung und Funktion) und fehlt deshalb auch im Binary. Besonderheiten:
- `CallBack_OnSendMsgShout` (Handler `0x0067AC90`): ein reiner `return TRUE`-Rumpf. Die Quelle beginnt die Funktion mit `return TRUE;`, der Rest ist toter Code – das Binary stimmt damit überein.
- `CallBack_OnChangeSoundEffect` und `CallBack_OnTest3DSound` haben denselben Rumpf in der Quelle und teilen sich im Binary die Adresse `0x007115B0` (ruft [`AgcmSound`](AgcmSound.md):SetRoom`).

| Chat-Befehl-Callback | Handler | Adresse |
|---|---|---|
| `CallBack_OnTestEditChatting` | `CallBack_OnTestEditChatting` | `0x007111A0` |
| `CallBack_OnAddTextFilter` | `CallBack_OnAddTextFilter` | `0x007112B0` |
| `CallBack_OnSocialAnimation` | `CallBack_OnSocialAnimation` | `0x00711310` |
| `CallBack_OnReloadQuest` | `CallBack_OnReloadQuest` | `0x00710A80` |
| `CallBack_OnFlagImoticon` | `CallBack_OnFlagImoticon` | `0x00711350` |
| `CallBack_OnDrawOcclusion` | `CallBack_OnDrawOcclusion` | `0x00710500` |
| `CallBack_OnReloadTitle` | `CallBack_OnReloadTitle` | `0x00710530` |
| `CallBack_OnChangeCameraMode` | `CallBack_OnChangeCameraMode` | `0x00711380` |
| `CallBack_OnReportModule` | `CallBack_OnReportModule` | `0x007113D0` |
| `CallBack_OnCheckMemory` | `CallBack_OnCheckMemory` | `0x00710560` |
| `CallBack_OnGuildBattleRequest` | `CallBack_OnGuildBattleRequest` | `0x00711460` |
| `CallBack_OnGuildBattleCancel` | `CallBack_OnGuildBattleCancel` | `0x007105A0` |
| `CallBack_OnGuildBattleSurrender` | `CallBack_OnGuildBattleSurrender` | `0x007105C0` |
| `CallBack_OnGuildLeaveOut` | `CallBack_OnGuildLeaveOut` | `0x007105E0` |
| `CallBack_OnChangePerspective` | `CallBack_OnChangePerspective` | `0x00711500` |
| `CallBack_OnChangeWideScreen` | `CallBack_OnChangeWideScreen` | `0x00710600` |
| `CallBack_OnChangeSoundEffect` | – | `0x007115B0` |
| `CallBack_OnScriptLua` | `CallBack_OnScriptLua` | `0x00711600` |
| `CallBack_OnViewFPS` | `CallBack_OnViewFPS` | `0x00710670` |
| `CallBack_OnTest3DSound` | – | `0x007115B0` |
| `CallBack_OnChangeTime` | `CallBack_OnChangeTime` | `0x007116D0` |
| `CallBack_OnToggleMatD3DFX` | `CallBack_OnToggleMatD3DFX` | `0x007106A0` |
| `CallBack_OnInviteParty` | `CallBack_OnInviteParty` | `0x007117A0` |
| `CallBack_OnSendMsgShout` | `Element::GetSize` | `0x0067AC90` |
| `CallBack_OnSendMsgJoin` | `CallBack_OnSendMsgJoin` | `0x00711920` |
| `CallBack_OnSendMsgLeave` | `CallBack_OnSendMsgLeave` | `0x00711990` |
| `CallBack_OnMoveToPosition` | `CallBack_OnMoveToPosition` | `0x00711A00` |
| `CallBack_OnNoticeMessage` | `CallBack_OnNoticeMessage` | `0x00711AC0` |
| `CallBack_OnNoticeMessageTest` | `CallBack_OnNoticeMessageTest` | `0x00711B90` |
| `CallBack_OnRejectTradeOn` | `CallBack_OnRejectTradeOn` | `0x00710700` |
| `CallBack_OnRejectTradeOff` | `CallBack_OnRejectTradeOff` | `0x00710730` |
| `CallBack_OnRejectPartyOn` | `CallBack_OnRejectPartyOn` | `0x00710760` |
| `CallBack_OnRejectPartyOff` | `CallBack_OnRejectPartyOff` | `0x00710790` |
| `CallBack_OnRejectGuildOn` | `CallBack_OnRejectGuildOn` | `0x007107C0` |
| `CallBack_OnRejectGuildOff` | `CallBack_OnRejectGuildOff` | `0x007107F0` |
| `CallBack_OnRejectGuildBattleOn` | `CallBack_OnRejectGuildBattleOn` | `0x00710820` |
| `CallBack_OnRejectGuildBattleOff` | `CallBack_OnRejectGuildBattleOff` | `0x00710850` |
| `CallBack_OnRejectGuildRelationOn` | `CallBack_OnRejectGuildRelationOn` | `0x00710880` |
| `CallBack_OnRejectGuildRelationOff` | `CallBack_OnRejectGuildRelationOff` | `0x007108B0` |
| `CallBack_OnRejectBattleOn` | `CallBack_OnRejectBattleOn` | `0x007108E0` |
| `CallBack_OnRejectBattleOff` | `CallBack_OnRejectBattleOff` | `0x00710910` |
| `CallBack_OnRejectBuddyOn` | `CallBack_OnRejectBuddyOn` | `0x00710940` |
| `CallBack_OnRejectBuddyOff` | `CallBack_OnRejectBuddyOff` | `0x00710970` |
| `CallBack_OnReloadCamSetting` | `CallBack_OnReloadCamSetting` | `0x007109F0` |
| `CallBack_OnReloadGuide` | `CallBack_OnReloadGuide` | `0x007109A0` |
| `CallBack_OnReloadWorldmap` | `CallBack_OnReloadWorldmap` | `0x00710B60` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Befehls-XML-Datei und ihr Inhalt wurden nicht untersucht.
- `_GetCmdCallBack` ist offenbar in `_AddChatCmd` eingebaut und nicht als eigene Funktion zu finden.
- Die einzelnen Befehls-Handler wurden nur über ihre Registrierung zugeordnet, nicht gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 1, ohne Kandidat: 1.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `CallBack_OnChangeSoundEffect` (`0x007115B0`), `CallBack_OnTest3DSound` (`0x007115B0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmSound`](AgcmSound.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
