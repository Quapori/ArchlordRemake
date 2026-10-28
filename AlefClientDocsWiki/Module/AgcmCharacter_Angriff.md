# AgcmCharacter und Angriffsanimation (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmCharacter` samt Angriffspfad [`AgpmCharacter`](AgpmCharacter.md):ActionCharacter` → `CBActionAttack` → `StartAnimation` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, EP8-Quelle (`Modules/AClient/AgcmCharacter`, `Modules/APublic/AgpmCharacter`) und die 2013er Berichte (`F951E56D…`). Alle Adressen und Offsets gelten nur für den 2017er Build.

## Kernbefund

- **Netzwerkseite unverändert:** `AgcmCharacter::OnReceive` (`0x005A3860`, vtable-Slot 9) verarbeitet im 2017er wie im 2013er Build genau drei Operationen: `7` `SETTING_CHARACTER_OK`, `8` `CHARACTER_POSITION`, `11` `AUTH_KEY`. Das ist die Quellvariante `__ATTACH_LOGINSERVER__` (zweites Enum im Header). Das Paket `m_csPacket` hat 7 Felder (INT8, CHAR[12], INT32, CHAR[49], INT32, POS, INT32), Flag-Länge 1; Quelle, 2017 und 2013 stimmen überein.
- **Angriffspfad entspricht der EP8-Quelle Schritt für Schritt.** `AgpmCharacter::ActionCharacter` liegt bei `0x0050F220`. Die Gates, ihre Reihenfolge, die Callback-IDs (`GET_ITEM_LANCER` 85, `CHECK_ACTION_ATTACK_TARGET` 62, `CHECK_IS_ACTION_MOVE` 18, `ACTION_ATTACK` 19) und die Puffer-Struktur für `CBActionAttack` sind identisch; die AgpmCharacter-Callback-IDs sind (anders als bei [`AgpmItem`](AgpmItem.md)) **nicht** verschoben.
- **Bestätigung der Ursache für die fehlende Monster-Angriffsanimation** (siehe Commit `66d1ca7`): `OnReceive` initialisiert das Flag-Byte `cIsTransform` mit `0xFF`. `OnOperationAdd` leitet daraus `+0x4C4` (Transform, Bit 0), `+0x790` (Ridable, Bit 1) und `+0x4C8` (Evolution, Bit 2) ab. Fehlt das Feld im ADD-Paket, sind alle drei Bits gesetzt, `m_bRidable` ist 1, und `ActionCharacter` ruft für den Akteur `GET_ITEM_LANCER` auf. Der Handler `AgpmItem::CBGetItemLancer` (`0x0058EBC0`) prüft, ob an Slot `0xF` (Lanze) ein Item ausgerüstet ist. Bei einem Monster ist das nie der Fall, der Angriff wird abgelehnt, bevor `ACTION_ATTACK` feuert.
- **Für Nicht-Self-Zeichen entfällt die Reichweitenprüfung:** `AgcmCharacter::CBCheckISActionMove` (`0x0059F4B0`) setzt `bIsActionMove = 0`, sobald der Akteur nicht der eigene Charakter ist. Ein vom Server gesendeter Monster-Angriff löst die Animation deshalb sofort aus, ohne Anlauf oder Reichweitenvergleich.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00410C90` | `AgcmCharacter::CBGameguardAuth` | stage1 |
| `0x0050F220` | `AgpmCharacter::ActionCharacter` | id-signatur |
| `0x0059E3D0` | `AgcmCharacter::ToggleStrafeMove` | strmatch |
| `0x0059E480` | `AgcmCharacter::ShowRegionInfo` | strmatch |
| `0x0059F4B0` | `AgcmCharacter::CBCheckISActionMove` | stage1 |
| `0x0059F4F0` | `AgcmCharacter::CBActionAttack` | stage1 |
| `0x0059F5A0` | `AgcmCharacter::CBCheckNowUpdateActionFactor` | stage1 |
| `0x0059F5E0` | `AgcmCharacter::CBNewCreateCharacter` | stage1 |
| `0x0059F630` | `AgcmCharacter::CBBindingRegionChange` | stage1 |
| `0x0059F6E0` | `AgcmCharacter::CharacterConstructor` | stage1 |
| `0x0059F7F0` | `AgcmCharacter::TemplateConstructor` | stage1 |
| `0x0059FBD0` | `AgcmCharacter::LoadClump` | strmatch |
| `0x005A0A00` | `AgcmCharacter::CBRemoveChar` | stage1 |
| `0x005A0A30` | `AgcmCharacter::CBUpdateFactor` | stage1 |
| `0x005A1020` | `AgcmCharacter::CBLoadMap` | stage1 |
| `0x005A1190` | `AgcmCharacter::CBSocialAnimation` | stage1 |
| `0x005A11D0` | `AgcmCharacter::CBUpdateCustomize` | stage1 |
| `0x005A1240` | `AgcmCharacter::CBUpdateOptionFlag` | stage1 |
| `0x005A1B10` | `AgcmCharacter::CBMoveActionAttack` | stage1 |
| `0x005A1B50` | `AgcmCharacter::CBMoveActionRelease` | stage1 |
| `0x005A1B80` | `AgcmCharacter::CBRidableUpdate` | stage1 |
| `0x005A1D90` | `AgcmCharacter::ShowNextAction` | strmatch |
| `0x005A1E10` | `AgcmCharacter::ShowActionQueue` | strmatch |
| `0x005A2910` | `AgcmCharacter::CBUpdateIgnoreStatus` | stage1 |
| `0x005A2B10` | `AgcmCharacter::OnLuaInitialize` | merged |
| `0x005A2B70` | `AgcmCharacter::UserInputMessageProc` | merged |
| `0x005A2F10` | `AgcmCharacter::CBMoveCharacter` | stage1 |
| `0x005A3070` | `AgcmCharacter::CBUpdatePosition` | stage1 |
| `0x005A3680` | `AgcmCharacter::SetSelfCharacter` | strmatch |
| `0x005A3860` | `AgcmCharacter::OnReceive` | merged |
| `0x005A3AC0` | `AgcmCharacter::CBCustomizeLoader` | stage1 |
| `0x005A3B20` | `AgcmCharacter::CBUpdateFactorMovement` | stage1 |
| `0x005A3BA0` | `AgcmCharacter::CBUpdateFactorMP` | stage1 |
| `0x005A4350` | `AgcmCharacter::LoadTemplateClump` | strmatch |
| `0x005A5330` | `AgcmCharacter::CBUpdateActionStatusCheck` | stage1 |
| `0x005A5470` | `AgcmCharacter::CBReceiveAction` | stage1 |
| `0x005A6030` | `AgcmCharacter::CBInitCharacterBackThread` | stage1 |
| `0x005A6AF0` | `AgcmCharacter::CBRemoveCharacter` | stage1 |
| `0x005A6B10` | `AgcmCharacter::CBAddChar` | stage1 |
| `0x005A6FA0` | `AgcmCharacter::CBUpdateCharacter` | strmatch |
| `0x005A8860` | `AgcmCharacter::CBInitCharacterMainThread` | stage1 |
| `0x005A8DD0` | `AgcmCharacter::ctor_or_dtor_005a8dd0` | merged |
| `0x005A92E0` | `AgcmCharacter::ctor_or_dtor_005a92e0` | merged |
| `0x005A9470` | `AgcmCharacter::OnDestroy` | merged |
| `0x005A9C60` | `AgcmCharacter::SelfMoveDirection` | strmatch |
| `0x005AA600` | `AgcmCharacter::CBUpdatePositionCheck` | stage1 |
| `0x005AABB0` | `AgcmCharacter::CBCheckRemoveChar` | stage1 |
| `0x005AACC0` | `AgcmCharacter::CBAlreadyExistChar` | stage1 |
| `0x005AB370` | `AgcmCharacter::~AgcmCharacter` | merged |
| `0x005AB390` | `AgcmCharacter::OnInit` | merged |
| `0x005AC600` | `AgcmCharacter::CBInitCharacter` | stage1 |
| `0x005AC7B0` | `AgcmCharacter::CBStopCharacter` | stage1 |
| `0x005AC930` | `AgcmCharacter::CBUpdateCharacter2` | stage1 |
| `0x005ACE00` | `AgcmCharacter::CharacterDestructor` | stage1 |
| `0x005ACE10` | `AgcmCharacter::TemplateDestructor` | stage1 |
| `0x005ACEC0` | `AgcmCharacter::CBEvolutionAppear` | stage1 |
| `0x005AD070` | `AgcmCharacter::CBTransformAppear` | stage1 |
| `0x005AD2F0` | `AgcmCharacter::CBUpdateFactorHP` | stage1 |
| `0x005AD870` | `AgcmCharacter::OnIdle` | merged |
| `0x005AD990` | `AgcmCharacter::CBUpdateActionStatus` | stage1 |
| `0x005ADA20` | `AgcmCharacter::OnAddModule` | merged |
| `0x00619020` | `AgcmCharacter::TemplateStreamReadCB` | stage1 |
| `0x0061A3C0` | `AgcmCharacter::TemplateStreamWriteCB` | stage1 |
| `0x0061A420` | `AgcmCharacter::AnimationStreamReadCB` | stage1 |
| `0x0061AE30` | `AgcmCharacter::AnimationStreamWriteCB` | stage1 |
| `0x0061AE60` | `AgcmCharacter::CharacterImportDataReadCB` | stage1 |
| `0x0061B1F0` | `AgcmCharacter::CustomizeStreamWriteCB` | stage1 |
| `0x0061B4E0` | `AgcmCharacter::StreamReadPolyMorphTable` | merged |
| `0x0061B8F0` | `AgcmCharacter::CustomizeStreamReadCB` | stage1 |
| `0x00706F80` | `AgcmCharacter::CBRemoveRide` | stage1 |
| `0x00706FB0` | `AgcmCharacter::AttachRide` | strmatch |
| `0x00707770` | `AgcmCharacter::LoadTemplateDefaultFace` | strmatch |
| `0x00707950` | `AgcmCharacter::LoadTemplateDefaultHair` | strmatch |

Die vtable-Slots von `AgcmCharacter` (17 Einträge) stimmen in der Länge mit der Quelle überein. Der Konstruktor liegt bei `0x005A8DD0`, `OnAddModule` bei `0x005ADA20` (registriert 26 `AgpmCharacter`-Callbacks, `AttachCharacterData`/`AttachCharacterTemplateData` und die Stream-Callbacks; Handler siehe Tabelle oben, Zuordnung per Aufrufsequenz).

## Objektlayout (AgcmCharacter, aus OnAddModule/OnReceive)

| Offset | Inhalt |
|---:|---|
| `+0x1038` | Auth-Key (Op 11) |
| `+0x1108` | `m_csPacket` (7 Felder) |
| `+0xD80` | `m_pcsAgpmFactors` |
| `+0xD84` | `m_pcsAgpmCharacter` |
| `+0xD88` | `m_pcsAgpmParty` |
| `+0xD8C` | `m_pcsAgpmSkill` |
| `+0xD90` | `m_pcsAgpmPvP` |
| `+0xDB8` | `m_pcsApmMap` |
| `+0xDEC` | Index der angehängten Zeichen-Daten (`AttachCharacterData`) |
| `+0xDEE` | Index der angehängten Template-Daten |
| `+0x15964` | `m_lSelfCID` (eigene Charakter-ID) |

## Opcodes von `AgcmCharacter::OnReceive`

| Op | Name (Variante `__ATTACH_LOGINSERVER__`) | Verhalten im 2017er Binary | Ereignis | Vergleich 2013 |
|---:|---|---|---|---|
| 7 | `SETTING_CHARACTER_OK` | `m_lSelfCID` setzen, `SetSelfCID`, Zeichen holen, `SetSelfCharacter`, `UpdatePosition`, NID im AgcdCharacter ablegen | `SETTING_CHARACTER_OK` (ID 21) und `SET_SELF_CHARACTER` (ID 15) | = |
| 8 | `CHARACTER_POSITION` | `SetSelfCID`, Karte um die Position laden (`LoadTargetPosition`), `RemoveAllCharacters`, `SendLoadingComplete` | – | = |
| 11 | `AUTH_KEY` | Auth-Key in `+0x1038` speichern | – | = |
| sonst | `default` | `return 0` | – | = |

Die 2013er Doku führt zusätzlich die Operationen 1, 3, 5 der anderen Enum-Variante auf; sie sind im Binary nicht im Dispatch und bleiben `fehlt` (2013 und 2017).

## Angriffspfad: Voraussetzungen im 2017er Binary

`AgpmCharacter::ActionCharacter(ATTACK, Akteur, Ziel, …)` bei `0x0050F220`. Der Akteur ist bei einem Monster-Angriff das Monster. Die Prüfungen laufen in dieser Reihenfolge; jede Verletzung bricht ohne Animation ab:

| # | Prüfung | Quelle | Binary (Offset im Zeichen) |
|---:|---|---|---|
| 1 | Aktionstyp `NONE` → sofort `TRUE` | `ActionCharacter` | `param_2 == 0` → `return 1` |
| 2 | Akteur vorhanden | `!pcsCharacter` → `FALSE` | `param_3 == 0` → `return 0` |
| 3 | Akteur nicht betäubt (Special-Status-Bit 0 `STUN`) | `m_ulSpecialStatus & STUN` | `+0x740` Bit 0 |
| 4 | Akteur nicht im Schlaf (`IsStatusSleep`) | `IsStatusSleep` | `FUN_00502BA0`: `+0x744` Bit 1 (Special-Status Bit 33) |
| 5 | Akteur nicht `AllBlock` (`IsAllBlockStatus`) | `IsReturnToLoginServerStatus`, `IsDisableCharacter`, sonst Callback `CHECK_ALL_BLOCK_STATUS` | `FUN_00505A70`: `+0x528` (Current-Status) `== 3` oder `+0x740` Bit 18 (`0x40000`) → blockiert; sonst `EnumCallback(94)`. Auf dem Client registriert niemand diesen Callback → nicht blockiert |
| 6 | Nicht durch eine Störung am Angriff gehindert (`CheckEnableActionCharacter(ATTACK)`) | `CheckEnableActionCharacter` | `FUN_005053A0`: `(+0x7E4 & 1) == 0` |
| 7 | Akteur-Aktionsstatus erlaubt Angriff (`CheckActionStatus(ATTACK)`) | `CheckActionStatus`: `NOT_ACTION`/`MOVE`/`NORMAL` | `FUN_00505EF0`: `+0x52A` ∈ {`0` NORMAL, `3` NOT_ACTION, `4` MOVE}, sonst nur, wenn `AllBlock` |
| 8 | Ziel vorhanden und vom Typ Charakter | `m_eType == APBASE_TYPE_CHARACTER` | `*param_4 == 3` |
| 9 | Akteur nicht „ridable“, sonst Lanze ausgerüstet | `m_bRidable` → `GET_ITEM_LANCER` | `+0x790 == 0` oder `EnumCallback(85)` → `AgpmItem::CBGetItemLancer` (`0x58EBC0`, Slot `0xF`) |
| 10 | Ziel per CID gefunden (`GetCharacterLock`) und nicht `AllBlock` | `GetCharacterLock`, `IsAllBlockStatus` | `FUN_00502E20(param_4[1])`, `FUN_00505A70` |
| 11 | Weder Akteur noch Ziel sind tot | `m_unActionStatus == DEAD` | `+0x52A != 2` für beide (`DEAD` = 2) |
| 12 | Gültiges Angriffsziel (`CHECK_ACTION_ATTACK_TARGET`) | Callback `bIsValidAttack` | `EnumCallback(62)`; auf dem Client ohne Registrant → bleibt gültig |
| 13 | Reichweite nur, wenn `bIsActionMove` | `CHECK_IS_ACTION_MOVE`, `IsInRange` | `EnumCallback(18)`; `CBCheckISActionMove` setzt es für Nicht-Self auf 0 → Reichweite entfällt |
| 14 | Angriff auslösen | `EnumCallback(ACTION_ATTACK, Akteur, {Ziel, Result, FactorDamage, Combo})` | `EnumCallback(19)` → `AgcmCharacter::CBActionAttack` (`0x59F4F0`) |

**`CBActionAttack` (`0x0059F4F0`):** holt die angehängten `AgcdCharacter`-Daten von Akteur und Ziel (Index bei `+0xDEC`), setzt bei Fremd-PCs mit Combo-Info das Combo-Flag (`+0xA80`), ruft zweimal `SetAttackStatus` (`FUN_0059BC60`) und startet `StartAnimation(Akteur, ATTACK = 3)` (`FUN_0059DF50` → `FUN_0059DC60`).

**`StartAnimation` (`0x0059DC60`)** bricht ab, wenn (a) kein Template an den Zeichen-Daten hängt (`+0x08`), (b) der Typ `< 0` ist oder die aktuelle Anim-Variante (`+0x8C`) `< 0`, (c) das Template keine Animationstabelle hat (`+0x48`), oder (d) für `[ATTACK][Variante]` keine vollständige RtAnim-Kette existiert und auch der Fallback auf Variante 0 fehlt. Für diese Kette ist die Animationsdatei des Monster-Templates verantwortlich, nicht der Server.

## Checkliste für den Server (Monster als Angriffs-Akteur)

- Monster-ADD: `IsTransform`/Flag-Byte **explizit 0** senden (nicht weglassen). Sonst `m_bRidable = 1` und Gate 9 verwirft den Angriff.
- Aktionsstatus des Monsters ∈ {0, 3, 4}; nicht 1/2 (Vor-Tod/Tod). Gleiches gilt für das Ziel (nicht 2).
- Special-Status des Monsters ohne Bit 0 (Stun), Bit 33 (Schlaf) und Bit 18 (`0x40000`, deaktiviert); Current-Status nicht 3.
- Das Ziel muss dem Client bereits bekannt sein (CID im lokalen Zeichenpool), sonst scheitert `GetCharacterLock`.
- Das Monster-Template braucht eine Attack-Animation (`AgcdCharacterTemplate`-Animationsdaten, Variante 0 als Fallback).
- Die Reichweite spielt für Fremd-Zeichen keine Rolle (`bIsActionMove` = 0); die Action-Paketfelder (Ziel-CID, Ergebnistyp, Faktor, Combo) werden unverändert in den Callback-Puffer übernommen.

## Abgleich mit EP8 und 2013

- `ActionCharacter(ATTACK)`: Reihenfolge und Bedingungen entsprechen der Quelle (`AgpmCharacterAction.cpp`). Die weiteren Aktionstypen (Fall `3…0x23`) lösen jeweils `FUN_0050E8A0(Akteur, 0, 0)` und einen festen Callback aus (z. B. Typ 3 → ID 0x15, 4 → 0x16, 5 → 0x17).
- `AgpmCharacter`-Status-Enums: `CurrentStatus` `LOGOUT`=0, `IN_LOGIN_PROCESS`=1, `IN_GAME_WORLD`=2, `RETURN_TO_LOGIN_SERVER`=3; `ActionStatus` `NORMAL`=0, `PREDEAD`=1, `DEAD`=2, `NOT_ACTION`=3, `MOVE`=4, `ATTACK`=5, `READY_SKILL`=6, `TRADE`=7, `PARTY`=8. Das Binary verwendet exakt diese Werte (`DEAD` = 2, Wartezustand = 3).
- `CBCheckISActionMove`, `CBActionAttack` und `StartAnimation` entsprechen der Quelle bis auf die inlinierten Getter.

## Grenzen

- `AgcmCharacter::OnAddModule` registriert 26 Callbacks; bei der Zuordnung der Handler-Adressen wurde nur die Reihenfolge gegen die Quelle ausgerichtet (mit mehrfacher Bestätigung durch `CBInitCharacter`/`CBMoveCharacter` etc.). Weitere AgcmCharacter-Dateien (`…Animation`, `…Customize`, `…Ride`, `…Stream`) sind nur teilweise benannt.
- Die Zuordnung von `ActionCharacter` stützt sich auf die Kombination der fünf Callback-IDs in genau einer Funktion plus Vergleich der Gate-Struktur; ein Quellvergleich Zeile für Zeile wurde nur für den Angriffszweig durchgeführt.
- Die Animationsdaten (Template-Inhalt) und der Weg vom `ACTION_ATTACK`-Callback zu Effekten/Sound ([`AgcmEventEffect`](AgcmEventEffect.md)) sind nicht analysiert.
- `CHECK_ALL_BLOCK_STATUS` und `CHECK_ACTION_ATTACK_TARGET` haben in der EP8-Quelle nur Server-Registranten; dass auch der 2017er Client keine hat, ist aus der Quelle abgeleitet und nicht für alle Client-Module einzeln im Binary nachgewiesen.

## Querverweise

- **Erwähnt Module:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md)
