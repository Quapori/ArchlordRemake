# AgpmCharacter (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Paketmoduls `AgpmCharacter` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, EP8-Quelle (`Modules/APublic/AgpmCharacter`), Vergleich mit den Berichten zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Protokoll unverändert:** Paket-Typ `0x02`, 31-Felder-Hauptpaket, Move-/Action-/IgnoreStatus-Teilpakete und alle 35 Operationen (0–34) stimmen im 2017er Binary mit der EP8-Quelle **und** mit dem 2013er Build überein. Ein Server, der den 2013er `AgpmCharacter`-Verkehr spricht, bleibt für dieses Modul kompatibel.
- **Ereignisse:** Von 30 vergleichbaren Opcodes stimmen 26 mit der 2013er Messung überein. Die 4 Unterschiede (3, 11, 12, 32) sind Messartefakte: Die 2013er Auswertung hatte einen kleineren Suchradius bzw. nannte die ID `CB#124` statt `REQUEST_COUPON_USE`. Echte Verhaltensunterschiede wurden nicht gefunden.
- **Adressen verschoben, Code gleich:** `OnReceive` liegt jetzt bei `0x005093C0` (2013: `0x00509CB0`), `EnumCallback` bei `0x004E4040` (2013: `0x004E4070`).

## Identifikation und Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00502430` | `AgpmCharacter::OnAddModule` | merged |
| `0x005024D0` | `AgpmCharacter::OnInit` | merged |
| `0x00503440` | `AgpmCharacter::OnOperationTransform` | case-map |
| `0x005034B0` | `AgpmCharacter::OnOperationRestoreTransform` | case-map |
| `0x00503500` | `AgpmCharacter::OnOperationEvolution` | case-map |
| `0x00503570` | `AgpmCharacter::OnOperationRestoreEvolution` | case-map |
| `0x005035E0` | `AgpmCharacter::OnOperationSocialAnimation` | case-map |
| `0x00503640` | `AgpmCharacter::OnOperationOnlineTime` | case-map |
| `0x005036B0` | `AgpmCharacter::OnOperationGameguardAuth` | case-map |
| `0x005036D0` | `AgpmCharacter::OnOperationResurrectionByOther` | case-map |
| `0x00503760` | `AgpmCharacter::OnOperationEventEffectID` | case-map |
| `0x00503790` | `AgpmCharacter::OnOperationRequestPinchWantedCharacter` | case-map |
| `0x005037B0` | `AgpmCharacter::OnOperationRequestCouponInfo` | case-map |
| `0x005037D0` | `AgpmCharacter::OnOperationRequestCouponUse` | case-map |
| `0x005037F0` | `AgpmCharacter::OnOperationAnswerCouponUse` | case-map |
| `0x00503810` | `AgpmCharacter::OnOperationRecieveCouponInfo` | case-map |
| `0x00504A60` | `AgpmCharacter::StreamReadChatFilterText` | merged |
| `0x00505450` | `AgpmCharacter::OnIdle2` | merged |
| `0x005055F0` | `AgpmCharacter::OnOperationLevelUp` | strmatch |
| `0x00505680` | `AgpmCharacter::OnOperationAddAttacker` | case-map |
| `0x005058C0` | `AgpmCharacter::AddRemoveCharacter` | merged |
| `0x00505B20` | `AgpmCharacter::OnDestroy` | merged |
| `0x00505DA0` | `AgpmCharacter::RemoveCharacter` | strmatch |
| `0x00506000` | `AgpmCharacter::OnOperationCancelTransform` | case-map |
| `0x005063A0` | `AgpmCharacter::OnOperationRemove` | strmatch |
| `0x00506450` | `AgpmCharacter::OnOperationRemoveForView` | case-map |
| `0x00506820` | `AgpmCharacter::AddCharacter` | strmatch |
| `0x005069C0` | `AgpmCharacter::OnOperationAdd` | strmatch |
| `0x00508840` | `AgpmCharacter::CharacterIdle` | merged |
| `0x00508950` | `AgpmCharacter::OnOperationUpdate` | strmatch |
| `0x00509310` | `AgpmCharacter::OnIdle` | merged |
| `0x005093C0` | `AgpmCharacter::OnReceive` | merged |
| `0x00509FD0` | `AgpmCharacter::ctor_or_dtor` | merged |
| `0x0050A0D0` | `AgpmCharacter::~AgpmCharacter` | merged |
| `0x0050A150` | `AgpmCharacter::ctor_or_dtor` | merged |
| `0x005252E0` | `AgpmCharacter::StaticCharacterWriteCB` | stage1 |
| `0x00525420` | `AgpmCharacter::StaticCharacterReadCB` | stage1 |
| `0x00525710` | `AgpmCharacter::StaticOneCharacterReadCB` | stage1 |
| `0x00525A10` | `AgpmCharacter::TemplateReadCB` | stage1 |
| `0x00525FA0` | `AgpmCharacter::TemplateWriteCB` | stage1 |
| `0x00526470` | `AgpmCharacter::SetStreamFactor` | strmatch |
| `0x00526D30` | `AgpmCharacter::StreamReadImportData` | merged |
| `0x00547A40` | `AgpmCharacter::StreamReadImportData` | merged |
| `0x0058A5F0` | `AgpmCharacter::OnOperationMoveBankMoney` | case-map |

`OnReceive` = vtable-Slot 9. Der Konstruktor `0x0050A150` setzt Modulname, Idle-Flags und die vier Pakete. Der Destruktor-Pfad liegt bei `0x00509FD0`/`0x0050A0D0`.

## Objektlayout (aus Konstruktor und `OnAddModule`)

| Offset | Inhalt |
|---:|---|
| `+0x008` | Modulname `"AgpmCharacter"` (0x27 Bytes) |
| `+0xB84` | `m_pcsAgpmFactors` |
| `+0xB88` | `m_pcsApmMap` |
| `+0xB8C` | `m_pcsAgpmConfig` |
| `+0xDE4` | `m_csPacket` (Hauptpaket, Flag-Länge 4) |
| `+0x136F8` | `m_csPacketMove` (Flag-Länge 1) |
| `+0x2600C` | `m_csPacketAction` (Flag-Länge 2) |
| `+0x38920` | `m_csPacketIgnoreStatus` (Flag-Länge 2) |

Der Konstruktor legt außerdem zwei Pools an (`FUN_004E4160(0x818,0)` und `(0x22C0,1)`; vermutlich Zeichen- und Template-Datensatzgröße, nicht weiter belegt).

## Paketlayout (identisch zu 2013 und EP8)

Typcodes: `0`=CHAR, `1`=INT8, `2`=UINT8, `4`=UINT16, `5`=INT32, `6`=UINT32, `7`=INT64, `8`=UINT64, `9`=FLOAT, `10`=POS, `12`=PACKET, `13`=MEMORY_BLOCK.

**Hauptpaket** (31 Felder, `FUN_004EA680(4)` + `FUN_004E9F80(&packet, …)` bei `0x50A150`):

| # | Maske | Typ | Anzahl | Feld |
|---:|---|---:|---:|---|
| 0 | `0x1` | 1 | 1 | Operation |
| 1 | `0x2` | 5 | 1 | Character ID |
| 2 | `0x4` | 5 | 1 | Template ID |
| 3 | `0x8` | 13 | 1 | Game ID |
| 4 | `0x10` | 1 | 1 | Status |
| 5 | `0x20` | 12 | 1 | Move-Paket |
| 6 | `0x40` | 12 | 1 | Action-Paket |
| 7 | `0x80` | 12 | 1 | Factor-Paket |
| 8 | `0x100` | 7 | 1 | Geld |
| 9 | `0x200` | 7 | 1 | Bankgeld |
| 10 | `0x400` | 7 | 1 | Cash |
| 11 | `0x800` | 1 | 1 | Action-Status |
| 12 | `0x1000` | 1 | 1 | Criminal-Status |
| 13 | `0x2000` | 5 | 1 | Attacker-ID |
| 14 | `0x4000` | 1 | 1 | Neu erzeugt |
| 15 | `0x8000` | 2 | 1 | Region-Index |
| 16 | `0x10000` | 2 | 1 | Social-Animation |
| 17 | `0x20000` | 8 | 1 | Special-Status |
| 18 | `0x40000` | 1 | 1 | Transform |
| 19 | `0x80000` | 0 | 32 | Skill-Init-Text |
| 20 | `0x100000` | 1 | 1 | Face |
| 21 | `0x200000` | 1 | 1 | Hair |
| 22 | `0x400000` | 5 | 1 | Option-Flag |
| 23 | `0x800000` | 1 | 1 | Bankgröße |
| 24 | `0x1000000` | 4 | 1 | Event-Status |
| 25 | `0x2000000` | 5 | 1 | Rest Criminal-Zeit |
| 26 | `0x4000000` | 5 | 1 | Rest Murderer-Zeit |
| 27 | `0x8000000` | 0 | 16 | Nickname |
| 28 | `0x10000000` | 13 | 1 | GameGuard-Daten |
| 29 | `0x20000000` | 6 | 1 | Letzter Kill (BattleSquare) |
| 30 | `0x40000000` | 6 | 1 | Letzter Escape |

Move (8 Felder): POS, POS, INT32, INT32, FLOAT, FLOAT, INT8, INT8. Action (10 Felder): INT8, INT32, INT32, INT8, PACKET, POS, UINT8, INT8, UINT32, UINT8. IgnoreStatus (7 Felder): 7× INT32. Alle drei stimmen mit Quelle und 2013 überein.

## Opcode-Tabelle

Handler im 2017er Binary; Ereignisse = Menge der `EnumCallback`-IDs. `4` (SELECT) hat keinen Case und endet in `default` (`OutputDebugString("… Error (7)")`), wie in Quelle und 2013.

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | `0x005069C0` `OnOperationAdd` | `ACTION_ATTACK`, `ADD_CHARACTER_TO_MAP`, `ALREADY_EXIST_CHAR`, `BINDING_REGION_CHANGE`, `CANCEL_TRANSFORM`, `CHECK_ACTION_ATTACK_TARGET`, `CHECK_ALL_BLOCK_STATUS`, `CHECK_IS_ACTION_MOVE` … | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 1 | `UPDATE` | `0x00508950` `OnOperationUpdate` | `ACTION_ATTACK`, `ADD_CHARACTER_TO_MAP`, `ALREADY_EXIST_CHAR`, `BINDING_REGION_CHANGE`, `CANCEL_TRANSFORM`, `CHECK_ACTION_ATTACK_TARGET`, `CHECK_ALL_BLOCK_STATUS`, `CHECK_IS_ACTION_MOVE` … | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 2 | `REMOVE` | `0x005063A0` `OnOperationRemove` | `ADD_CHARACTER_TO_MAP`, `ALREADY_EXIST_CHAR`, `BINDING_REGION_CHANGE`, `CANCEL_TRANSFORM`, `CHECK_ALL_BLOCK_STATUS`, `CHECK_NOW_UPDATE_ACTION_FACTOR`, `CHECK_REMOVE_CHAR`, `CHECK_REMOVE_CHAR2` … | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 3 | `REMOVE_FOR_VIEW` | `0x00506450` `OnOperationRemoveForView` | `CHECK_REMOVE_CHAR`, `CHECK_REMOVE_CHAR2`, `DELETE`, `REMOVE`, `REMOVE_CHARACTER_FROM_MAP`, `REMOVE_ID`, `REMOVE_RIDE`, `RESTORE_TRANSFORM` | 2017 ⊃ 2013 |
| 5 | `LEVEL_UP` | `0x005055F0` `OnOperationLevelUp` | `ADD_CHARACTER_TO_MAP`, `ALREADY_EXIST_CHAR`, `BINDING_REGION_CHANGE`, `CANCEL_TRANSFORM`, `CHECK_ALL_BLOCK_STATUS`, `CHECK_NOW_UPDATE_ACTION_FACTOR`, `CHECK_REMOVE_CHAR`, `CHECK_REMOVE_CHAR2` … | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 6 | `ADD_ATTACKER` | `0x00505680` `OnOperationAddAttacker` | – | = (2013 = 2017) |
| 7 | `MOVE_BANKMONEY` | `0x0058A5F0` `OnOperationMoveBankMoney` | – | = (2013 = 2017) |
| 8 | `DISCONNECT_BY_ANOTHER_USER` | inline: `EnumCallback(DISCONNECT_BY_ANOTHER_USER)` | `DISCONNECT_BY_ANOTHER_USER` | = (2013 = 2017) |
| 9 | `REQUEST_RESURRECTION_TOWN` | inline: GetCharacterLock + `EnumCallback(REQUEST_RESURRECTION, 1)` | `REQUEST_RESURRECTION` | = (2013 = 2017) |
| 10 | `REQUEST_RESURRECTION_NOW` | inline: nur CID-Prüfung, `return TRUE` (wie Quelle) | – | = (2013 = 2017) |
| 11 | `TRANSFORM` | `0x00503440` `OnOperationTransform` | `INIT`, `NEW_CREATED_CHAR`, `TRANSFORM_APPEAR`, `TRANSFORM_STATUS` | 2017 ⊃ 2013 |
| 12 | `RESTORE_TRANSFORM` | `0x005034B0` `OnOperationRestoreTransform` | `RESTORE_TRANSFORM`, `TRANSFORM_APPEAR` | 2017 ⊃ 2013 |
| 13 | `CANCEL_TRANSFORM` | `0x00506000` `OnOperationCancelTransform` | `CANCEL_TRANSFORM`, `CHECK_ALL_BLOCK_STATUS` | = (2013 = 2017) |
| 14 | `RIDABLE` | inline: nur CID-Prüfung | – | = (2013 = 2017) |
| 15 | `RESTORE_RIDABLE` | inline: nur Server-Prüfung | – | = (2013 = 2017) |
| 16 | `SOCIAL_ANIMATION` | `0x005035E0` `OnOperationSocialAnimation` | `SOCIAL_ANIMATION` | = (2013 = 2017) |
| 17 | `OPTION_UPDATE` | inline: Option-Flag vergleichen, `EnumCallback(UPDATE_OPTION_FLAG)` | `UPDATE_OPTION_FLAG` | = (2013 = 2017) |
| 18 | `BLOCK_BY_PENALTY` | inline: `EnumCallback(BLOCK_BY_PENALTY)` | `BLOCK_BY_PENALTY` | = (2013 = 2017) |
| 19 | `REQUEST_RESURRECTION_SIEGE_INNER` | inline: `EnumCallback(REQUEST_RESURRECTION, 2)` | `REQUEST_RESURRECTION` | = (2013 = 2017) |
| 20 | `REQUEST_RESURRECTION_SIEGE_OUTER` | inline: `EnumCallback(REQUEST_RESURRECTION, 3)` | `REQUEST_RESURRECTION` | = (2013 = 2017) |
| 21 | `ONLINE_TIME` | `0x00503640` `OnOperationOnlineTime` | `ONLINE_TIME` | = (2013 = 2017) |
| 22 | `NPROTECT_AUTH` | `0x005036B0` `OnOperationGameguardAuth` | `GAMEGUARD_AUTH` | = (2013 = 2017) |
| 23 | `UPDATE_SKILLINIT_STRING` | inline: `strncpy(m_szSkillInit, …, 0x20)` unter Lock | – | = (2013 = 2017) |
| 24 | `RESURRECTION_BY_OTHER` | `0x005036D0` `OnOperationResurrectionByOther` | `RESURRECTION_BY_OTHER` | = (2013 = 2017) |
| 25 | `EVENT_EFFECT_ID` | `0x00503760` `OnOperationEventEffectID` | `EVENT_EFFECT_ID` | = (2013 = 2017) |
| 26 | `EVOLUTION` | `0x00503500` `OnOperationEvolution` | `EVOLUTION` | = (2013 = 2017) |
| 27 | `RESTORE_EVOLUTION` | `0x00503570` `OnOperationRestoreEvolution` | `CHECK_TELEPORTBLOCK`, `RESTORE_EVOLUTION` | = (2013 = 2017) |
| 28 | `REQUEST_PINCHWANTED_CHARACTER` | `0x00503790` `OnOperationRequestPinchWantedCharacter` | `PINCHWANTED_REQUEST` | = (2013 = 2017) |
| 29 | `AGPMCHAR_PACKET_OPERATUIN_ANSWER_PINCHWANTED_CHARACTER` | inline: `EnumCallback(PINCHWANTED_ANSWER)` | `PINCHWANTED_ANSWER` | = (2013 = 2017) |
| 30 | `REQUEST_COUPON` | `0x005037B0` `OnOperationRequestCouponInfo` | `REQUEST_COUPON` | = (2013 = 2017) |
| 31 | `COUPON_INFO` | `0x00503810` `OnOperationRecieveCouponInfo` | `RECIEVE_COUPON_INFO` | = (2013 = 2017) |
| 32 | `REQUEST_COUPON_USE` | `0x005037D0` `OnOperationRequestCouponUse` | `REQUEST_COUPON_USE` | 2017 ⊃ 2013 |
| 33 | `ANSWER_COUPON_USE` | `0x005037F0` `OnOperationAnswerCouponUse` | `RECIEVE_COUPON_USE` | = (2013 = 2017) |
| 34 | `UPDATE_IGNORE_STATUS` | inline: 7 Felder kopieren, `EnumCallback(UPDATE_IGNORE_STATUS)` | `UPDATE_IGNORE_STATUS` | = (2013 = 2017) |

Bei 0, 1, 2 und 5 (`Add`, `Update`, `Remove`, `LevelUp`) ist der Aufrufbaum zu groß für einen Mengenvergleich (siehe auch `ALEFCLIENT_OPCODE_AUFRUFBAEUME.md`). Op 7 (`MoveBankMoney`) liegt in `AgpmCharacterMoney.cpp` und damit außerhalb des Hauptblocks bei `0x0058A5F0`.

## Abgleich mit EP8-Quelle

- `OnReceive`: Feldlesen (`GetField`) mit 31 Feldern, danach CID-Prüfung für Nicht-Server-Pakete. Ausgenommen sind exakt die Operationen 28–32 (Pinchwanted/Coupon), genau wie in der Quelle.
- Name-Puffer: bei bis zu 0x30 Bytes kopiert (`AGPDCHARACTER_MAX_ID_LENGTH` = 48), nullterminiert.
- `ADD` nur vom Server akzeptiert (`bReceivedFromServer`), sonst `Add Character Fail : bReceivedFromServer is FALSE`; `REMOVE` ebenso. `OnOperationAdd` erhält zusätzlich `0xFFFFFFFF`, `1`, `1` als feste Argumente.
- `UPDATE` ruft nach `OnOperationUpdate` direkt `EnumCallback(RECEIVE_CHARACTER_DATA)` (ID 64).
- `REQUEST_RESURRECTION_NOW` (10) kehrt wie in der Quelle früh mit `TRUE` zurück, ohne Callback (toter Code hinter dem `return`).
- `UPDATE_SKILLINIT_STRING` (23) kopiert 0x20 Bytes (`AGPACHARACTER_MAX_CHARACTER_SKILLINIT`) in `m_szSkillInit` an `+0xA4` des Zeichens.
- `UPDATE_IGNORE_STATUS` (34) liest 7 INT32 aus dem Teilpaket ab `+0x14` und löst ID 127 aus.

## Grenzen

- Aufrufbäume der Operationen 0/1/2/5 sind nicht tief verglichen; `OnOperationAdd/Update` (mehrere KB) wurden nicht Zeile für Zeile gegen die Quelle gelesen.
- Ereignismengen stammen aus `EnumCallback`-Aufrufen mit literaler ID in Tiefe 3 innerhalb des Moduls; indirekte Aufrufe und IDs aus Variablen fehlen. Op 8, 9, 10, 17–20, 29 und 34 sind inline in `OnReceive` und wurden von Hand aus dem Dekompilat gelesen.
- Funktionen in `AgpmCharacter*.cpp` außerhalb von `0x502000–0x50A200` (Stream-/Template-Code, Geldlogik, Update-/Action-Dateien) sind nur teilweise benannt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 37, eingebaut: 57, gemeinsamer Rumpf: 121, nicht im Client: 96, ohne Kandidat: 56, zugeordnet: 89.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetVehicleTID` | 25 | `0x00504CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAttackable` | 18 | `0x00505CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckNormalAttack` | 31 | `0x00505F60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadTemplate` | 76 | `0x00525150` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TransformCharacterAppear` | 16 | `0x0050E1F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsTargetable` | 18 | `0x00505D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateTemplate` | 37 | `0x00505470` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateBankSize` | 9 | `0x00501B20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateCustomizeIndex` | 13 | `0x00501AC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SubMoney` | 2 | `0x0058A300` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetWorldDirection` | 16 | `0x0050E5A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TransformCharacter` | 5 | `0x0050E6C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckStopFollow` | 13 | `0x0050E0E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `HasPenalty` | 32 | `0x00505A00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckCharName` | 7 | `0x00504A10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetAttackIntervalMSec` | 9 | `0x00504580` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsHitHeroic` | 12 | `0x00503D60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharacterTemplate` | 4 | `0x0058A130` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCharacterTemplate` | 15 | `0x005055B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCharacter` | 69 | `0x00502DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsShrineTypifier` | 7 | `0x00502CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsGuard` | 7 | `0x00502CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsGM` | 7 | `0x00502C80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsCreature` | 7 | `0x00502C30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusTame` | 7 | `0x00502C00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusGo` | 9 | `0x00502BD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusSleep` | 9 | `0x00502BA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusDisableNormalATK` | 9 | `0x00502B70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusDisableSkill` | 9 | `0x00502B40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusFullTransparent` | 6 | `0x00502AF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusHalfTransparent` | 9 | `0x00502AC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusInvincible` | 9 | `0x00502A90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusTransparent` | 9 | `0x00502A60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusFixed` | 10 | `0x00502A10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusSummoner` | 7 | `0x005029E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsNPC` | 7 | `0x005029B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPC` | 7 | `0x00502980` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsMonster` | 7 | `0x00502950` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPolyMorph` | 15 | `0x00502920` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTypePolyMorph` | 7 | `0x00502900` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateCharismaPoint` | 18 | `0x00501860` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 36 | `0x005060F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRegionNPC` | 24 | `0x0057F0A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCharismaPoint` | 7 | `0x005018F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateStatus` | 4 | `0x005014B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateRegion` | 31 | `0x005013C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdatePosition` | 4 | `0x005010A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateInit` | 30 | `0x00501040` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TransformCharacterStatus` | 35 | `0x0050E250` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MoveCharacter` | 2 | `0x0050EAD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MoveCharacterFollow` | 159 | `0x0050EF30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetValidDestination` | 228 | `0x00507230` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCharGrowUpFactor` | 229 | `0x00503DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetMurdererLevel` | 2 | `0x00505880` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUnion` | 9 | `0x00505830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessActionPacket` | 39 | `0x005056D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessMovePacket` | 107 | `0x00508590` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllCharactersExceptOne` | 32 | `0x00506290` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllCharacters` | 12 | `0x005061E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 36 | `0x00506160` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyTemplate` | 15 | `0x00505540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessIdleMove` | 349 | `0x00507CC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TurnCharacter` | 2 | `0x0050E360` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SyncMoveStartPosition` | 15 | `0x0050DE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckStopFollow` | 13 | `0x005053C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsInPvPDanger` | 14 | `0x00504800` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketOptionFlag` | 41 | `0x00504770` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddCharacterToMap` | 68 | `0x00503930` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessRemove` | 89 | `0x005044C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTaxRatio` | 13 | `0x0058A7F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `PayTax` | 10 | `0x0058A780` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StopCharacter` | 2 | `0x0050E8A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RestoreTransformCharacter` | 2 | `0x0050E760` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MoveCharacterFollow` | 159 | `0x005079D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharacterRace` | 5 | `0x00505330` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSameRace` | 18 | `0x005051D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsActionBlockCondition` | 42 | `0x005046F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetActionBlockTime` | 13 | `0x005046A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetHeroicPoint` | 9 | `0x00504330` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetSkillPoint` | 9 | `0x005042E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharismaPoint` | 13 | `0x00503AE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMurdererPoint` | 2 | `0x00503A60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveCharacterFromMap` | 59 | `0x00503870` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReflectFactorPacket` | 9 | `0x00503830` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTemplateSequence` | 7 | `0x00502FB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharSequence` | 7 | `0x00502F90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsInSiege` | 16 | `0x00502DA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DestroyCharacter` | 29 | `0x00502760` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateCharacter` | 109 | `0x00502540` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `IsCreature` (`0x0057FF00`), `IsTrap` (`0x00584320`), `GetCharacterLock` (`0x00502E50`), `GetCharacterLock` (`0x00502E50`), `GetCharacterLock` (`0x0058B350`), `CheckActionStatus` (`0x0050EA40`), `OnOperationTransform` (`0x00563170`), `SetLastCriminalTime` (`0x0058A520`), `SetLastMurdererTime` (`0x0058A520`), `GetMurdererLevel` (`0x0054DE60`), `GetMoveSpeed` (`0x00504440`), `GetFastMoveSpeed` (`0x00504440`), `SetCombatMode` (`0x0050E440`), `IsAllBlockStatus` (`0x0055D8C0`), `IsDisableCharacter` (`0x0057FF00`), `IsUseCharacter` (`0x005204C0`), `IsRepairCharacter` (`0x005204C0`), `GetBlockingType` (`0x005051A0`), `IsSameRace` (`0x0057FF00`), `GetCharismaStep` (`0x00551CA0`), `CheckEnableActionCharacter` (`0x00505A70`), `MoveCharacter` (`0x00570B20`), `RestoreTransformCharacter` (`0x00502F80`), `StopCharacter` (`0x0050E440`), `TurnCharacter` (`0x0050E440`), `ActionCharacter` (`0x0053D540`), `GetSelfCharacterTurnAngle` (`0x0050EA40`), `CheckLockAction` (`0x0050EA40`), `SetMoney` (`0x0058A520`), `GetMoney` (`0x0058A3F0`), `AddMoney` (`0x0058A270`), `SubMoney` (`0x0058A200`), `SetBankMoney` (`0x0058A520`), `SetCash` (`0x0058A520`), `StreamReadImportData` (`0x00546C70`), `UpdatePosition` (`0x0051A750`), `UpdateActionStatus` (`0x0050EA40`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmArchlord`](AgcmArchlord.md), [`AgcmAuction`](AgcmAuction.md), [`AgcmCamera2`](AgcmCamera2.md), [`AgcmCharacter_Angriff`](AgcmCharacter_Angriff.md), [`AgcmEventBank`](AgcmEventBank.md), [`AgcmEventCharCustomize`](AgcmEventCharCustomize.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventGuild`](AgcmEventGuild.md), [`AgcmEventItemConvert`](AgcmEventItemConvert.md), [`AgcmEventItemRepair`](AgcmEventItemRepair.md), [`AgcmEventProduct`](AgcmEventProduct.md), [`AgcmEventQuest`](AgcmEventQuest.md), [`AgcmEventRefinery`](AgcmEventRefinery.md), [`AgcmEventSiegeWarNPC`](AgcmEventSiegeWarNPC.md), [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md), [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgcmGuild`](AgcmGuild.md), [`AgcmItem`](AgcmItem.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmProduct`](AgcmProduct.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmRide`](AgcmRide.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUICashItemCabient`](AgcmUICashItemCabient.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUICustomizing`](AgcmUICustomizing.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIEventBank`](AgcmUIEventBank.md), [`AgcmUIEventItemRepair`](AgcmUIEventItemRepair.md), [`AgcmUIGuideMessage`](AgcmUIGuideMessage.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIOption`](AgcmUIOption.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIRemission`](AgcmUIRemission.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUITax`](AgcmUITax.md), [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md), [`AgpmBattleGround`](AgpmBattleGround.md), [`AgpmCombat`](AgpmCombat.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmParty`](AgpmParty.md), [`AgpmSkill`](AgpmSkill.md), [`AgpmUnion`](AgpmUnion.md), [`COptionFlagController`](COptionFlagController.md)
