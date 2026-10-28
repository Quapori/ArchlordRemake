# Phase 1

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Erzeugt mit `gapclose.py register`. Jede Quellmethode ohne Binary-Adresse bekommt einen Status mit Beleg. **zugeordnet** = eindeutiger Treffer (mindestens zwei unabhängige Belege, Reihenfolge der Quelle passt zur Adressreihenfolge); **gemeinsamer Rumpf** = `SetCallback`-Einzeiler; **nicht im Client** = in der Quelle ruft sie kein Client-Modul (nur Server oder niemand); **eingebaut** = kleine Funktion mit Aufrufer im Client, ohne eigene Adresse; **Kandidat unbestätigt** = Aufrufer im Client und ein Kandidat mit nur einem Beleg oder mehrdeutig (nicht benannt); **ohne Kandidat** / **nicht als eigene Funktion** = Aufrufer im Client, aber keine unbenannte Funktion mit Beleg (bei „nicht als eigene Funktion“ ist im Klassenbereich gar keine unbenannte Funktion mehr übrig); in beiden Fällen ist die Methode vermutlich eingebaut oder entfernt.

Zahlen: Kandidat unbestätigt 235, eingebaut 440, gemeinsamer Rumpf 877, nicht als eigene Funktion 22, nicht im Client 885, ohne Kandidat 660, zugeordnet 705

## AgcmBattleGround (eingebaut 7, gemeinsamer Rumpf 3, nicht im Client 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `BattleGroundNotice` | 45 | zugeordnet | `0x0067FC70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 4 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `IsBattleGournd` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBattleGround::IsMyBattleGround, AgcmBattleGround::IsOtherRace, AgcmUIItem::CBCheckUseItem |
| `IsMyBattleGround` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StartBattleGround` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBattleGround::BattleGroundNotice |
| `EndBattleGround` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBattleGround::BattleGroundNotice |
| `StartEventBattleGround` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBattleGround::BattleGroundNotice |
| `EndEventBattleGround` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBattleGround::BattleGroundNotice |
| `_BattleGroundEffectText` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmBattleGround::StartBattleGround, AgcmBattleGround::EndBattleGround, AgcmBattleGround::StartEventBattleGround |
| `_EpicZoneEffectText` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmBattleGround::BattleGroundNotice |
| `IsOtherRace` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmCharacter (Kandidat unbestätigt 12, eingebaut 37, gemeinsamer Rumpf 51, nicht im Client 47, ohne Kandidat 42, zugeordnet 102)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DropAnimation` | 14 | zugeordnet | `0x0059C230` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AdminChangeAnim` | 93 | zugeordnet | `0x0059D630` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AttachHair` | 64 | zugeordnet | `0x00707440` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AttachFace` | 62 | zugeordnet | `0x00707310` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateMainAnimation` | 178 | zugeordnet | `0x0059D1E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetBlendingAnimation` | 50 | zugeordnet | `0x0059D0C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetSkillStruckAnimation` | 81 | zugeordnet | `0x0059CB70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DeleteTemplateAnimation` | 67 | zugeordnet | `0x0059F9D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetNextAnimation` | 46 | zugeordnet | `0x0059DA00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TemplateAnimationAttachedDataStreamWrite` | 118 | zugeordnet | `0x00619C80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GeneralizeAttachedAtomicsNormals` | 55 | zugeordnet | `0x00707560` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetAnimSpeed` | 112 | zugeordnet | `0x0059BDC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReleaseTemplateAnimation` | 48 | zugeordnet | `0x005A19E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UnLockTarget` | 14 | zugeordnet | `0x0059EAE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSelfNID` | 6 | zugeordnet | `0x0059FEC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ResetCastSkill` | 11 | zugeordnet | `0x0059EC70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSelectTarget` | 9 | zugeordnet | `0x0059EBD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UnSelectTarget` | 13 | zugeordnet | `0x0059EB40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReleaseTemplateData` | 26 | zugeordnet | `0x005A8AD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `QueueCharPolyMorphByTID` | 46 | zugeordnet | `0x005ACF30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetCurrentEvolutionSkillTemplate` | 19 | zugeordnet | `0x005A4830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsNonPickingTID` | 5 | zugeordnet | `0x005A69A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsCharacterTransforming` | 5 | zugeordnet | `0x005A2130` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessNextAction` | 19 | zugeordnet | `0x005AAE20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StartAnimation` | 61 | zugeordnet | `0x00706A90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendCancelEvolution` | 34 | zugeordnet | `0x005A5F20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCharacter` | 36 | zugeordnet | `0x005AA190` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetHair` | 41 | zugeordnet | `0x00707720` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetFace` | 43 | zugeordnet | `0x007076D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_UpdateFactorCharacterType` | 13 | zugeordnet | `0x005A28A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateAnimationTimeForAllCharacter` | 78 | zugeordnet | `0x0059C090` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StartAnimation` | 61 | zugeordnet | `0x0059DC60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SearchSituation` | 184 | zugeordnet | `0x0059CDF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckCharacterPolyMorph` | 25 | zugeordnet | `0x005AD240` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ShowMyCID` | 8 | zugeordnet | `0x005A2040` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadCharacterData` | 47 | zugeordnet | `0x005AA0A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadTemplateData` | 20 | zugeordnet | `0x005A46A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetNextReceivedActionDamageFactor` | 34 | zugeordnet | `0x005A14E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetReceivedAction` | 46 | zugeordnet | `0x005A3CF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddReceivedAction` | 29 | zugeordnet | `0x005A3C00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MoveReservedPath` | 35 | zugeordnet | `0x005AAB00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `BlockingPositionCheck` | 313 | zugeordnet | `0x005A8140` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetValidDestination` | 420 | zugeordnet | `0x005A76D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendMoveCharacter` | 90 | zugeordnet | `0x005A0080` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendEnterGameWorld` | 24 | zugeordnet | `0x005A39E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCharacterMainThread` | 207 | zugeordnet | `0x005A7310` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCharacterBackThread` | 363 | zugeordnet | `0x005A5770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyCharacter` | 188 | zugeordnet | `0x005AA280` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 117 | zugeordnet | `0x005A6700` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SelectTarget` | 24 | zugeordnet | `0x005A2E70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LockTarget` | 56 | zugeordnet | `0x005A2D70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `KeyboardIdleProcess` | 60 | zugeordnet | `0x005AC4E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CharacterPosIdleProcess` | 52 | zugeordnet | `0x005A2BA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StopSelfCharacter` | 9 | zugeordnet | `0x005A4ED0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ActionSelfCharacter` | 143 | zugeordnet | `0x005A4F30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestoryCustomize` | 57 | zugeordnet | `0x00707080` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `BuildActionQueue` | 22 | zugeordnet | `0x005A1F30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DetachHair` | 59 | zugeordnet | `0x00707250` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DetachFace` | 59 | zugeordnet | `0x00707190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetHPZero` | 13 | zugeordnet | `0x005AD810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `PolymorphIdleProcess` | 84 | zugeordnet | `0x005AD570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCharacterPolyMorph` | 66 | zugeordnet | `0x005AD0D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseTemplateClump` | 96 | zugeordnet | `0x005A89A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseTemplateDefaultHair` | 16 | zugeordnet | `0x005A8920` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseTemplateDefaultFace` | 16 | zugeordnet | `0x005A88A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessActionQueue` | 26 | zugeordnet | `0x005A40D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ApplyActionData` | 86 | zugeordnet | `0x005A3E40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `TemplateHairStreamWrite` | 21 | zugeordnet | `0x0061B0A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `TemplateFaceStreamWrite` | 22 | zugeordnet | `0x0061AF50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `TemplateEtcDataStreamWrite` | 86 | zugeordnet | `0x0061A0A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `TemplateAnimationStreamWrite` | 68 | zugeordnet | `0x00619EF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `TemplatePreDataStreamWrite` | 45 | zugeordnet | `0x00619B40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AttachRideClump` | 118 | zugeordnet | `0x005FF7D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnUpdateCharacterCustomize` | 60 | zugeordnet | `0x005A27C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetPlayerAttackDirection` | 55 | zugeordnet | `0x005A2290` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadTemplateAnimation` | 75 | zugeordnet | `0x005A18A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseSelfCharacter` | 18 | zugeordnet | `0x005A1820` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveActionData` | 32 | zugeordnet | `0x005A1690` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InclinePlaneBiped` | 63 | zugeordnet | `0x0059F2A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InclinePlaneQuadruped` | 92 | zugeordnet | `0x0059EF60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCastSkill` | 12 | zugeordnet | `0x0059EC10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSendActionTime` | 57 | zugeordnet | `0x0059E960` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `TurnSelfCharacter` | 12 | zugeordnet | `0x0059E8D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnEquipItemByEvolution` | 34 | zugeordnet | `0x005A48A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StartAnimation` | 61 | zugeordnet | `0x005A9530` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetClassTypeByTID` | 6 | zugeordnet | `0x005A2790` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StartAnimation` | 61 | zugeordnet | `0x005AB1F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnPolyMorph` | 75 | zugeordnet | `0x005AB050` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnEquipCharonForSummoner` | 44 | zugeordnet | `0x005A6050` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnChagneEquipItemByEvolution` | 49 | zugeordnet | `0x005A49F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveDuplicateSiegeWarObject` | 41 | zugeordnet | `0x005A4700` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `KillGameServer1` | 9 | zugeordnet | `0x005A2590` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRequestClientConnection` | 25 | zugeordnet | `0x005A21F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendPacketOptionFlag` | 13 | zugeordnet | `0x005A2170` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ClearActionFactor` | 66 | zugeordnet | `0x005A1280` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadAtomic` | 19 | zugeordnet | `0x005A0F50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendMoveMoneyFromInventoryToBank` | 58 | zugeordnet | `0x005A0E10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendActionInfo` | 85 | zugeordnet | `0x005A0520` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendStopCharacter` | 71 | zugeordnet | `0x005A03C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendMoveFollowCharacter` | 68 | zugeordnet | `0x005A0270` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendLoadingComplete` | 24 | zugeordnet | `0x0059FEF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateTransparent` | 117 | zugeordnet | `0x0059ECB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CharacterKeyDownMove` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::UserInputMessageProc; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CharacterKeyUpMove` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::UserInputMessageProc; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBSelfCharacterKeyMove` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnInit; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetWorld` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmItem::OnAddModule |
| `SetClumpPath` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmExportResource::SetSourcePath |
| `SetAnimationPath` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmExportResource::SetSourcePath |
| `SetMaxAnimations` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSendMoveDelay` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTexDictFile` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTexturePath` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEff2::OnInit, CExNPC::OnMakeResource, AgcmExportResource::ExportDDSPath |
| `GetCharacterData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::CBOnTargetSet, AgcmCamera2::OnIdle, AgcuCamMode::SetCameraInfo |
| `GetCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::CBOnTargetSet, AgcmCharacter::ActionSelfCharacter, AgcmCharacter::LockTarget |
| `GetTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcuCamMode::SetCameraInfo, AgcmCharacter::LoadCharacterData, AgcmCharacter::InitCharacter |
| `GetTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::CBRegionChange, AgcmCharacter::ShowRegionInfo, AgcmCharacter::CBBindingRegionChange |
| `SetHierarchyForSkinAtomic` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCharacter::SetDeadAnimation, AgcmCharacter::UpdateMainAnimation, AgcmCharacter::DropAnimation |
| `MoveSelfCharacter` | 369 | Kandidat unbestätigt | `0x005051A0` | Aufrufer im Client: AgcmCharacter::SelfMoveDirection, AgcmCharacter::CBUpdateCharacter2, AgcmCharacter::CBUpdatePositionCheck; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `MoveTurnSelfCharacter` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearMoveKey` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `MoveForward` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcuUIControlCharacter::CallBackSelectAnimationEnd |
| `MoveBackward` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcuUIControlCharacter::_UnSelectCharacter |
| `MoveLeft` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MoveRight` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StopForward` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StopBackward` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StopLeft` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StopRight` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsSelectTarget` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBUpdateStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmUISiegeWar::OnAddModule |
| `CBUpdateLevel` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnAddModule, AgpmSkill::OnAddModule; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `GetChildFrameHierarchy` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::GetHierarchy, AgcmResourceLoader::GetHierarchy, AgcmResourceLoader::GetChildFrameHierarchy; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `GetHierarchy` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCharacter::InitCharacterBackThread, AgcmCharacter::UpdateMainAnimation, AgcmCharacter::LoadTemplateDefaultFace |
| `DestroyTextBoard` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::DestroyCharacter |
| `RemovePreData` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateDestructor, AgcmExportResource::ExportCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBRemoveCheckAtomic` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ConvertAnimType2` | 66 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcmCharacter::AnimationStreamReadCB, AgcmEventEffect::StreamReadCharacterAnimationAttachedData, AgcmSkill::SetSkillEffectData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `UnHookLODAtomic` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBTextureRead` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::OnAddModule, AgcmResourceLoader::CBTextureRead; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CheckCustAnimType` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SetNextAnimData; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetNextAnimData` | 82 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CheckStartAnimCallback; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `OnPreReceive` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SendCancelTransform` | 51 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SendRequestCouponInfo` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUICouponBox::Open |
| `SendRequestCouponUse` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUICouponBox::CBCashInvenClickUseItem; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CollisionWorldFirstCallback` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateSubHierarchy` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::InitCharacterBackThread |
| `FindNodeIndexFromSubAnimType` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DumpTexDict` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackInitCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnim` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimWait` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimWalk` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimRun` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimAttack` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimStruck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimDead` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEndSocialAnim` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAnimSocial` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAttackSuccess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStruckCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackProcessSkillStruckCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSkillStruckCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSelfUpdatePosition` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSelfStopCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetSelfCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReleaseSelfCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPreRemoveCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSettingCharacterOK` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadClump` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadDefaultArmourClump` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDisplayActionResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLockTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnlockTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSelectTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnSelectTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGameServerDisconnect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGameServerError` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionResultNotEnoughArrow` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionResultNotEnoughBolt` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionResultNotEnoughMP` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCharHP` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCharMP` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMovement` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackKillCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadTemplate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReleaseTemplate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSelfRegionChange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadingComplete` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateOptionFlag` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackWaveFxTrigger` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTransparent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSocketOnConnect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsCameraMoving` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTurnCamera` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDestroyBoard` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetAnimationPath` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SendMoveMoneyFromBankToInventory` | 57 | Kandidat unbestätigt | `0x006E9D30` | Aufrufer im Client: AgcmUIEventBank::CBInputMoneyToBank; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CBUpdateMoney` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::OnAddModule, AgcmUIEventItemRepair::OnAddModule; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBUpdateBankMoney` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::OnAddModule, AgcmUIEventBank::OnAddModule; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `LoadAllTemplateClump` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBDisconnectByAnotherUser` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnAddModule; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetPreLightForAllCharacter` | 49 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetHeadActionData` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveHeadActionData` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetNextReceivedActionResult` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SearchSituation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `GetSequenceActionData` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CBUpdateCharacter2, AgcmCharacter::IsReceivedDeadAction; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `IsReceivedDeadAction` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ProcessStruckIdleEvent` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ProcessSkillStruckIdleEvent` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SetSkillStruckAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBSocketOnConnect` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendEnterGameWorld, AgcmReturnToLogin::ReconnectLoginServer; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBSocketOnDisConnect` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendEnterGameWorld; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBSocketOnError` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendEnterGameWorld; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CBRemoveCharacterLoader` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTemplateClumpRenderType` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::LoadTemplateClump; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `ProcessReservedAction` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetFollowTarget` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseFollowTarget` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::MoveSelfCharacter, AgcmCharacter::LockTarget, AgcmCharacter::SelectTarget |
| `SetNextAction` | 9 | Kandidat unbestätigt | `0x00502E00` | Aufrufer im Client: AgcmCharacter::MoveSelfCharacter, AgcmCharacter::ActionSelfCharacter, AgcmSkill::CastSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `GetNextAction` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBUpdateCharacter2, AgcmSkill::CBReservedActionSkill |
| `ShowPickingInfo` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnInit, AgcmObject::OnInit; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `HidePickingInfo` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnInit, AgcmObject::OnInit; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `ShowBoundingSphere` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::OnInit |
| `HideBoundingSphere` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::OnInit |
| `ClearActionQueue` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::OnInit |
| `IsValidCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::CBMoveCharacter, AgcmCharacter::CBUpdatePosition, AgcmItem::DetachItem |
| `IsValidCharacter` | 8 | Kandidat unbestätigt | `0x005BC170` | Aufrufer im Client: AgcmCharacter::CBMoveCharacter, AgcmCharacter::CBUpdatePosition, AgcmItem::DetachItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsValidLOD` | 39 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLodClumpPolyNum` | 46 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EndCharPolyMorph` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EndCharEvolution` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StartCharPolyMorphByTID` | 67 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StartCharEvolutionByTID` | 64 | Kandidat unbestätigt | `0x005AAEE0` | Aufrufer im Client: AgcmCharacter::CBEvolutionAppear; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetMovementKeys` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIHotkey::ApplyPlayerMovementKeys; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetPlayerLookAtFactor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnIdle, AgcmTargeting::OnIdle, AgcUIManager::PreTranslateInputMessage |
| `SetPlayerLookAtTarget` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::UpdateLookAt, AgcmTargeting::OnIdle |
| `GetPlayerLookAtFactor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnIdle, AgcUIManager::OnIdle |
| `ShowClumpForced` | 58 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CheckStartAnimCallback, AgcmCharacter::OnAnimCB; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `LoadTemplatePickingClump` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseTemplatePickingClump` | 46 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetNonPickingTID` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamReadCB |
| `SendGameGuardAuth` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetAttackStatus` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::ActionSelfCharacter, AgcmCharacter::CBUpdateCharacter2, AgcmCharacter::CBActionAttack |
| `SetSubAnimation` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SetSubStruckAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetSubStruckAnimation` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetStruckAnimation` | 106 | Kandidat unbestätigt | `0x0059C970` | Aufrufer im Client: AgcmCharacter::AdminChangeAnim, AgcmEventEffect::NoticeEffectSetTargetStruckAnimCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |
| `SetDeadAnimation` | 36 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::UpdateMainAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StopAnimation` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::CallBack_Open |
| `StopAnimation` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::CallBack_Open |
| `StopAnimation` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::CallBack_Open |
| `SkipSearchSituation` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckStartAnimCallback` | 152 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::StartAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetAnimOption` | 23 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::StartAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StartAnimation` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::ActionSelfCharacter, AgcmCharacter::CBMoveCharacter, AgcmCharacter::CBStopCharacter |
| `UpdateSubAnimation` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetEndThenChangeAnimation` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CheckStartAnimCallback, AgcmCharacter::StartAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `InitAnimData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::CheckStartAnimCallback |
| `GetCurrentAnimDuration` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnIdle |
| `GetAnimDuration` | 10 | Kandidat unbestätigt | `0x0059E810` | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUIProduct::CastAnimation, AgcmUIQuest2::StartAnimation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAnimType2Num` | 23 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcmCharacter::DeleteTemplateAnimation, AgcmCharacter::LoadTemplateAnimation, AgcmCharacter::ReleaseTemplateAnimation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AllocateAnimationData` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::AnimationStreamReadCB; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetAnimCBData` | 11 | Kandidat unbestätigt | `0x00702400` | Aufrufer im Client: AgcmCharacter::SetBlendingAnimation, AgcmCharacter::SetNextAnimation, AgcmCharacter::SetEndThenChangeAnimation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddAnimCallback` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::SetStruckAnimation, AgcmCharacter::SetSkillStruckAnimation, AgcmCharacter::SetBlendingAnimation |
| `RemoveAnimAttachedDataCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnInit |
| `OnAnimCB` | 70 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SetStruckAnimation, AgcmCharacter::SetSkillStruckAnimation, AgcmCharacter::SetBlendingAnimation; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `OnAnimEndCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnAnimEndThenChangeCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSubAnimEndCB` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSubAnimEndThenChangeCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IntervalMainAnimCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IntervalSubAnimCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CopyAnimAttachedData` | 85 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnumCallbackStruckChar` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::SetSkillStruckAnimation |
| `UpdateLookAt` | 213 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateBendOver` | 217 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CBUpdateCharacter; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `SetCustomizeRenderType` | 20 | Kandidat unbestätigt | `0x005B3D40` | Aufrufer im Client: AgcmCharacter::LoadTemplateDefaultFace, AgcmCharacter::LoadTemplateDefaultHair; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SaveEditHairAtomic` | 45 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GenerateRideCID` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::AttachRide; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `CreateRideCharacter` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyRideCharacter` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::DetachRide; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `DetachRide` | 83 | Kandidat unbestätigt | `0x00706E00` | Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmCharacter::AttachRide, AgcmCharacter::CBRemoveRide; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 16, Belegarten 3) |
| `SetSelfRideClump` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmCharacter::DetachRide |
| `StreamReadTemplate` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::StreamReadTemplateAnimation, AgcmCharacter::StreamReadTemplateCustomize, AgcmExportResource::ReadCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplate` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StreamReadTemplateAnimation` | 47 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplateAnimation` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StreamReadTemplateCustomize` | 46 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplateCustomize` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 5711 unbenannten Funktionen im Klassenbereich |

## AgcmConnectManager (eingebaut 1, nicht als eigene Funktion 1, nicht im Client 3, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Disconnect` | 14 | zugeordnet | `0x006F4F60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetLoginServerNID` | 8 | zugeordnet | `0x006F50D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendZoningMessage` | 24 | zugeordnet | `0x006F4FC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DisconnectAll` | 10 | nicht als eigene Funktion |  | Aufrufer im Client: AgcEngine::OnTerminate; im Adressbereich der Klasse (0x006F4EC0–0x006F5110) ist keine unbenannte Funktion mehr übrig |
| `GetControlServerID` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmRecruit::SendRegisterToLFP, AgcmRecruit::SendRegisterToLFM, AgcmRecruit::SendCancelFromLFP |
| `GetControlServerNID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetDealServerNID` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRecruitServerNID` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmEventNPCTrade (eingebaut 1, gemeinsamer Rumpf 11, nicht als eigene Funktion 1, nicht im Client 1, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakeBasePacket` | 47 | zugeordnet | `0x006DCED0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRequestItemList` | 61 | zugeordnet | `0x006DD2D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendSell` | 78 | zugeordnet | `0x006DD170` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendBuy` | 78 | zugeordnet | `0x006DCFE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCallbackUpdateNPCTradeGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateInventoryGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOpenUINPCTrade` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAriseNPCTradeEvent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInvenFull` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuyItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSellItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNotEnoughGhelld` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNotEnoughSpaceToReturnGhelld` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNotEnoughCharisma` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNotEnoughShrineCoin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetNPCInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEventNPCTrade::CBRequestNPCItemList |
| `ResetNPCInfo` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ProcessSellItem` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNPCTrade::OnReceive; im Adressbereich der Klasse (0x006DCC60–0x006DD560) ist keine unbenannte Funktion mehr übrig |

## AgcmLogin (Kandidat unbestätigt 1, eingebaut 1, gemeinsamer Rumpf 17, nicht im Client 2, ohne Kandidat 5, zugeordnet 17)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DisconnectLoginServer` | 11 | zugeordnet | `0x0065CD60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendRenameCharacter` | 53 | zugeordnet | `0x0065DAB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendEnterGame` | 66 | zugeordnet | `0x0065D450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenameCharacter` | 13 | zugeordnet | `0x0065DF10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SelectCharacter` | 31 | zugeordnet | `0x0065DE40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ConnectLoginServer` | 16 | zugeordnet | `0x0065E5A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendAccount` | 82 | zugeordnet | `0x0065E660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendCharacter4Compensation` | 53 | zugeordnet | `0x0065DBB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRemoveCharacter` | 61 | zugeordnet | `0x0065D990` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendCreateCharacter` | 62 | zugeordnet | `0x0065D860` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendCreateCharacter` | 62 | zugeordnet | `0x0065D730` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetBaseCharacterOfRace` | 50 | zugeordnet | `0x0065D640` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendReturnToSelectServer` | 39 | zugeordnet | `0x0065D570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetCharacters` | 40 | zugeordnet | `0x0065D390` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetUnion` | 34 | zugeordnet | `0x0065D2F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendEKey` | 39 | zugeordnet | `0x0065D210` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetEncryptCode` | 56 | zugeordnet | `0x0065D100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ConnectLoginServer` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcAuth::login, AgcGPAuth::login, AgcmUIAccountCheck::CB_OnSubmit |
| `InitRegistry` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmLogin::ConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `SetMainWindow` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetIDPassword` | 8 | Kandidat unbestätigt | `0x0065D0A0` | Aufrufer im Client: AgcAuth::login, AgcGPAuth::login, AgcmUIAccountCheck::CB_OnSubmit; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CBSocketConnect` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmLogin::ConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `CBSocketDisConnect` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmLogin::ConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `CBSocketError` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmLogin::ConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `SetCallbackConnectLoginServer` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDisconnectLoginServer` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEncryptCodeSuccess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInvalidClientVersion` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSignOnSuccess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnionInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharacterName` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharacterNameFinish` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharacterInfoFinish` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEnterGameEnd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRaceBase` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNewCharacterName` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNewCharacterInfoFinish` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoginResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEKeyActive` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCompensationInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetLoginServer` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMakingCharacterInfo` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacterCreate::CB_OnCharacterCreateOK; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |

## AgcmObject (Kandidat unbestätigt 3, eingebaut 9, gemeinsamer Rumpf 6, nicht im Client 25, ohne Kandidat 15, zugeordnet 18)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RemoveObjectTemplateGroup` | 12 | zugeordnet | `0x006737F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SectorRidableObjectIndexUpdate` | 20 | zugeordnet | `0x00673EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetAllOcTreeIDs` | 45 | zugeordnet | `0x00673A70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBOnAddObject` | 223 | zugeordnet | `0x00673F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SectorObjectIndexUpdate` | 22 | zugeordnet | `0x006736E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `WaitForQueueFlush` | 28 | zugeordnet | `0x00674D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ObjectTemplateGroupStreamWrite` | 72 | zugeordnet | `0x006719B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ObjectTemplateGroupStreamRead` | 109 | zugeordnet | `0x00670F30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetupObjectClump2` | 135 | zugeordnet | `0x00674550` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetupObjectClump` | 9 | zugeordnet | `0x00674B60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GroupDelete` | 38 | zugeordnet | `0x006739A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetupObjectClump1` | 375 | zugeordnet | `0x00672D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseObjectTemplateData` | 54 | zugeordnet | `0x00671FC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadAtomic` | 14 | zugeordnet | `0x00671D80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadClump` | 19 | zugeordnet | `0x00670DE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ObjectDeleteIdleProcess` | 45 | zugeordnet | `0x006747C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseObjectData` | 155 | zugeordnet | `0x006734B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadTemplateData` | 61 | zugeordnet | `0x00671E90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddObjectTemplateCreateCallBack` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddObjectCreateCallBack` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcuCamMode::SetCameraInfo, AgcmCharacter::LoadCharacterData, AgcmCharacter::InitCharacter |
| `GetObjectData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::searchAtomicById, AgcdCamConstrain_Obj::bIntsct, AgcmCharacter::GetValidDestination |
| `GetObjectData` | 41 | Kandidat unbestätigt | `0x00670D70` | Aufrufer im Client: AgcmAmbOcclMap::searchAtomicById, AgcdCamConstrain_Obj::bIntsct, AgcmCharacter::GetValidDestination; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `GetObject` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcaAnimation2::GetRtAnim, AgcdCamConstrain_Obj::bIntsct, AgcmCharacter::GetValidDestination |
| `CBInitTemplateAtomic` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::LoadClump; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `SaveClump` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetObjectTemplateGroupData` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmObject::ObjectTemplateGroupStreamRead |
| `SetClumpPath` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmExportResource::SetSourcePath |
| `SetAnimationPath` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmExportResource::SetSourcePath |
| `SetRpWorld` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmObject::OnAddModule, AgcmTargeting::OnAddModule |
| `SetTexDictFile` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTexturePath` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEff2::OnInit, CExNPC::OnMakeResource, AgcmExportResource::ExportDDSPath |
| `GetObjectGroupData` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::SetupObjectClump_TransformOnly, AgcmObject::SetupObjectClump2, AgcmObject::SetupObjectClump1; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `SetupObjectClump_TransformOnly` | 270 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRange` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::EnumLoadedDivisionObject, CProgressBar::Create, CProgressBar::SetRange; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `UseRange` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmMap::EnumLoadedDivisionObject |
| `CheckingRange` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::SetupObjectClump_TransformOnly, AgcmObject::SetupObjectClump2; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `DumpTexDict` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateAmbient` | 52 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateAlpha` | 52 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateObjectType` | 32 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReloadObjectClump` | 79 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxAnimation` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackInitObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackWorkObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuffObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadClump` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPreRemoveData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRidableUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `ForceEnumCallback` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUpdateStatus` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmUISiegeWar::OnAddModule; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `CBGetCollisionAtomic` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBGetCollisionAtomicFromAtomic` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GroupAdd` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::ObjectStreamReadCB; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `ClumpDelete` | 59 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetEnumValue` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetGroupCount` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::ObjectStreamWriteCB, AgcmUILoginSelect::OpenLoginSelect, AgcmUILoginSelect::_LoginSelectWindowInit; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `FindGroupStart` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindGroupStart` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadAllTemplateData` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RefreshObjects` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetAnimation` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::SetupObjectClump1; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `CBUpdateAnimation` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::SetupObjectClump_TransformOnly, AgcmObject::SetupObjectClump2, AgcmObject::ShowPickingInfo; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `GetDeleteObjectQueue` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::ObjectDeleteIdleProcess; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `AddDeleteObjectQueue` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::CBUnLoadMap; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `ObjectExport` | 53 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBEventObjectOnly` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::ServerExport; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `ServerExport` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPreLightForAllObject` | 58 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CopyObjectTemplateGroup` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CopyObjectTemplateGroupData` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::CopyObjectTemplateGroup; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `RemoveObjectTemplateGroupData` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::RemoveObjectTemplateGroup; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `GetBoundingSphereRange` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmEventQuest::CBEventRequest; kein unbenannter Kandidat mit Beleg unter 40 unbenannten Funktionen im Klassenbereich |
| `IsValidLOD` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsInValidOctreeData` | 19 | Kandidat unbestätigt | `0x00672730` | Aufrufer im Client: AgcmObject::ObjectTemplateStreamWriteCB, AgcmObject::SetupObjectClump1; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ReCalulateOctreeData` | 63 | Kandidat unbestätigt | `0x00672730` | Aufrufer im Client: AgcmObject::ObjectTemplateStreamWriteCB, AgcmObject::SetupObjectClump1; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AgcmParty (eingebaut 1, gemeinsamer Rumpf 24, nicht im Client 1, ohne Kandidat 15, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SendPacketDelegationLeader` | 12 | zugeordnet | `0x006E8BC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SendPacketFailed` | 17 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SendPacketUpdateExpType` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::CBPartyOptionAply; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SendPacketUpdateExpType` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::CBPartyOptionAply; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SendPacketUpdateItemDivision` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::CBPartyOptionAply; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SendPacketAcceptRecall` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::CBAcceptRecall; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SendPacketRejectRecall` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::CBRejectRecall; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketInvite` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketInvite; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketReject` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketReject; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketAccept` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketAccept; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketLeave` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketLeave; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketBanish` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketBanish; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketFailed` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketFailed; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketInviteByCharID` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketInviteByCharID; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketDelegationLeader` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketDelegationLeader; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketAcceptRecall` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketAcceptRecall; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketRejectRecall` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketRejectRecall; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBRemoveMember` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmParty::OnAddModule, AgcmUIParty::OnAddModule |
| `SetCallbackReceiveInvite` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteAccept` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveLeave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveBanish` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedAlreadyOtherPartyMember` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedAlreadyPartyMember` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedPartyMemberIsFull` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedNotLeader` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveOperationFailed` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedNoLoginMember` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveDelegationLeader` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveDelegationLeaderFailed` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedLevelDiff` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedRefuse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestRecall` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAcceptRecall` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRejectRecall` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedMurdererOperator` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveInviteFailedMurdererTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveLeaveByMurderer` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmPrivateTrade (gemeinsamer Rumpf 17, nicht als eigene Funktion 9, nicht im Client 6, zugeordnet 11)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ProcessCancel` | 29 | zugeordnet | `0x006E9810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessLockButton` | 26 | zugeordnet | `0x006E9790` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendReadyToExchange` | 39 | zugeordnet | `0x006E96F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeUnlock` | 39 | zugeordnet | `0x006E9650` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeLock` | 39 | zugeordnet | `0x006E95B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeRemoveItemFromTradeGrid` | 60 | zugeordnet | `0x006E9470` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeAddItemToTradeGrid` | 57 | zugeordnet | `0x006E9350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeUpdateMoney` | 46 | zugeordnet | `0x006E9280` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeCancel` | 39 | zugeordnet | `0x006E91E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeRequestConfirm` | 29 | zugeordnet | `0x006E9160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeRequest` | 47 | zugeordnet | `0x006E9080` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCallbackUpdateLockButton` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTargetLockButton` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTradeMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTargetTradeMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeStart` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeEnd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeCancel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeOpenUIYesNo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeOpenUI` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeCloseUI` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeUpdateTargetLockButton` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeActiveReadyToExchange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeReadyToExchange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeClientReadyToExchange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeMSGComplete` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeMSGCancel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTradeRequestRefuseUser` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetAgpdCharacter` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::AddItemToTradeGrid, AgcmPrivateTrade::RemoveItemFromTradeGrid, AgcmPrivateTrade::AddItemToTargetTradeGrid; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `ParseGridPos` | 24 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::AddItemToTradeGrid, AgcmPrivateTrade::RemoveItemFromTradeGrid, AgcmPrivateTrade::AddItemToTargetTradeGrid; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `AddItemToTradeGrid` | 61 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::OnOperationUpdate, AgpmItem::SplitItem; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `RemoveItemFromTradeGrid` | 60 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmItem::RemoveStatus, AgpmItem::RemoveItemFromTradeGrid, AgpmItem::RemoveItemFromTradeGrid; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `AddItemToTargetTradeGrid` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveItemFromTargetTradeGrid` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ProcessTargetLockButton` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::OnReceive; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `ProcessActiveReadyToExchange` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::OnReceive; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `ProcessReadyToExchange` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::OnReceive; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `ProcessClientReadyToExchange` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::OnReceive; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `OnTradeStart` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnUpdateLockButton` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmPrivateTrade::ProcessLockButton; im Adressbereich der Klasse (0x006E8F70–0x006E9880) ist keine unbenannte Funktion mehr übrig |
| `OnUpdateTradeMoney` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnUpdateMyTradeMoney` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnUpdateHisTradeMoney` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmRecruit (Kandidat unbestätigt 3, eingebaut 5, nicht im Client 13, ohne Kandidat 2, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SendCancelFromLFP` | 47 | zugeordnet | `0x006EA060` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendRegisterToLFM` | 51 | zugeordnet | `0x006E9F00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendRegisterToLFP` | 47 | zugeordnet | `0x006E9E20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessSearchLFPResult` | 62 | zugeordnet | `0x006EA1C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessSearchLFMResult` | 70 | zugeordnet | `0x006EA320` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetControlServerID` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRecruit::SendRegisterToLFP, AgcmRecruit::SendRegisterToLFM, AgcmRecruit::SendCancelFromLFP |
| `GetControlServerNID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRecruitServerNID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetControlServerID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetControlServerNID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRecruitServerNID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SendAddToRecruitServer` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SendCancelFromLFM` | 51 | Kandidat unbestätigt | `0x006E9D30` | Aufrufer im Client: AgcmRecruit::UIClickDeleteLFM; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `SendSearchLFPByPage` | 69 | Kandidat unbestätigt | `0x006E9D30` | Aufrufer im Client: AgcmRecruit::CBBbsChangePage, AgcmRecruit::UILFPSearch, AgcmRecruit::UILFPPageChange; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `SendSearchLFMByPage` | 69 | Kandidat unbestätigt | `0x006E9D30` | Aufrufer im Client: AgcmRecruit::UILFMSearch, AgcmRecruit::UILFMPageChange; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CBBbsClickContent` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBBbsChangePage` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBBbsWindowClose` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClickMercenaryBbsContent` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClickPartyBbsContent` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UIClickRegisterLFP` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UIClickDeleteLFP` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UIClickRegisterLFM` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIRecruitWrite::OnClickWriteButton; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `UIClickDeleteLFM` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIRecruitWrite::OnCommand; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `UILFPSearch` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIRecruit::OnCommand |
| `UILFMSearch` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIRecruit::OnCommand |
| `UILFPPageChange` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIRecruit::OnCommand |
| `UILFMPageChange` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIRecruit::OnCommand |

## AgcmUICashInven (eingebaut 1, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CashInvenOpenUI` | 27 | zugeordnet | `0x006D05F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RefreshItemGrid` | 8 | zugeordnet | `0x006D0500` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSelfOperation` | 9 | zugeordnet | `0x006D0770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetItemStaminaTime` | 48 | zugeordnet | `0x006CFDE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckPetStateGrid` | 71 | zugeordnet | `0x006D0B70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveCashItem` | 26 | zugeordnet | `0x006D0A60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddCashItem` | 14 | zugeordnet | `0x006D09C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetItemInfoTime` | 123 | zugeordnet | `0x006CFA90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddBoolean` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIBuddy::OnAddModule, AgcmUICashInven::OnAddModule |

## AgcmUIPartyOption (eingebaut 1, gemeinsamer Rumpf 1, ohne Kandidat 6, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddUserData` | 42 | zugeordnet | `0x006BF800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetPartyOption` | 32 | zugeordnet | `0x006C0570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBPartyOptionInviteMember` | 61 | zugeordnet | `0x006BFC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `AddFunction` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::OnLuaInitialize, AgcmCharacter::OnLuaInitialize, AgcmEventNature::OnLuaInitialize; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `AddEvent` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddEvent, AgcmMinimap::OnAddModule; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `InitUIMessage` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::EnableUIForPartyLeader; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `CBPartyOptionAply` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::AddFunction; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `EnableUIForPartyLeader` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::SetPartyOption; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `CBPartyOptionOpenUI` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmUIPartyOption::AddFunction; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `CBPartyOptionOpenUIClick` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIPartyOption::AddFunction |

## AgpmAdmin (Kandidat unbestätigt 2, eingebaut 9, gemeinsamer Rumpf 27, nicht im Client 34, ohne Kandidat 19, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnOperationRemoveAdmin` | 36 | zugeordnet | `0x00555BE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePingPacket` | 11 | zugeordnet | `0x005559E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `AdminLock` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmAdmin::OnOperationAddAdmin, AgpmAdmin::OnOperationRemoveAdmin, AgpmAdmin::GetAdminLevel |
| `AdminUnlock` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmAdmin::OnOperationAddAdmin, AgpmAdmin::OnOperationRemoveAdmin, AgpmAdmin::GetAdminLevel |
| `OnOperationAddAdmin` | 50 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnOperationLogin; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationConnect` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationNumCurrentUser` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationServerInfo` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationSearch` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationSearchResult` | 74 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationSearchCharData` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationSearchCharItem` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationSearchCharSkill` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationSearchCustom` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationCharMove` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationCharEdit` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationGuild` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationBan` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationPing` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationItem` | 33 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnOperationTitle` | 22 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnReceive; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `GetADCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo, AgcmCashMall::SendPacketRefreshCash, AgcmCharacter::UpdateTransparent |
| `GetAdminInfo` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnOperationAddAdmin, AgpmAdmin::GetAdminLevel; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `GetAdminIDList` | 18 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetAdminInfoList` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetAdminCharacter` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsAdminCharacter` | 16 | nicht im Client |  | Aufrufer nur im Server (10); kein Treffer im Binary |
| `IsAdminCharacter` | 10 | nicht im Client |  | Aufrufer nur im Server (10); kein Treffer im Binary |
| `GetAdminLevel` | 16 | Kandidat unbestätigt | `0x00555970` | Aufrufer im Client: AgcmAdmin::SendAdminClientRequest, AgcmUISiegeWar::CBOpenSiegeWarTimeSetUI, AgpmAdmin::OnOperationAdminClient; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAdminLevel` | 21 | Kandidat unbestätigt | `0x00555970` | Aufrufer im Client: AgcmAdmin::SendAdminClientRequest, AgcmUISiegeWar::CBOpenSiegeWarTimeSetUI, AgpmAdmin::OnOperationAdminClient; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetCurrentTimeStamp` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmTitle::_CheckTitleExchangeTimeLimit, AgcmUIGuild::CBJoin, AgcmUIGuild::CBReceiveLeaveRequestSelf |
| `GetCurrentTimeDate` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `DecodingItemPos` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `DecodingItemConvertHistory` | 65 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `DecodingItemOption` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `DecodingItemSkillPlus` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeAdminPacket` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmAdmin::SendAdminClientRequest, AgpmAdmin::MakeLoginPacket, AgpmAdmin::MakeConnectPacket |
| `MakeLoginPacket` | 2 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `MakeLoginPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `MakeConnectPacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeNumCurrentUserPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeSearchPacket` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISearch::SendSearchCondition |
| `MakeSearchPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISearch::SendSearchCondition |
| `MakeSearchResultPacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeSearchResultPacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCharDataSubPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeCharDataSubPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeCharItemPacket` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCharItemPacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCharSkillPacket` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCharSkillPacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCustomPacket` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeCustomPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeCharMovePacket` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCharMovePacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeCharEditPacket` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakeCharEditPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakeBanPacket` | 4 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeBanPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeItemPacket` | 2 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `MakeItemPacket` | 3 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `MakeServerInfoPacket` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAdmin::SendAdminClientRequest |
| `MakeServerInfoPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmAdmin::SendAdminClientRequest |
| `MakeTitlePacket` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeTitlePacket` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackAddAdmin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveAdmin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNumCurrentUser` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUserPosition` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUserPositionInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackServerInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackConnect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSearchCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSearchResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCustom` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharMove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharEdit` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBan` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemCreate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPing` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAdminClientLogin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTitleEdit` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `PrintAdminList` | 22 | ohne Kandidat |  | Aufrufer im Client: AgpmAdmin::OnOperationAddAdmin, AgpmAdmin::OnOperationRemoveAdmin; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |

## AgpmArchlord (Kandidat unbestätigt 1, eingebaut 2, gemeinsamer Rumpf 15, nicht im Client 9, ohne Kandidat 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 25 | zugeordnet | `0x0057B6F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackOperationSetArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOperationCancelArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOperationSetGuard` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOperationCancelGuard` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOperationGuardInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOperationCurrentStep` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOperationMessageId` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCancelArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventNoticeNewArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetCurrentStep` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventTeleport::OnReceive, AgpmEventTeleport::IsArchlordDungeonPoint |
| `SetCurrentStep` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmArchlord::OnReceive |
| `OnOperationEventRequest` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `OnOperationEventGrant` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `IsArchlord` | 10 | Kandidat unbestätigt | `0x0057B880` | Aufrufer im Client: AgcmCharacter::SendSocialAnimation, AgcmEventEffect::SetBaseSkillEventEffect, AgcmEventEffect::SetPassiveSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `MakePacketSetArchlord` | 13 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketCancelArchlord` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketGuardInfo` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSetGuard` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketCancelGuard` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketCurrentStep` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakepacketMessageID` | 15 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketEventGrant` | 23 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `MakePacketNoticeNewArchlord` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmAreaChatting (gemeinsamer Rumpf 4, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackRecvSendMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketSendMessage` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: CChatCmd::CallBack_OnSendMsgShout; im Adressbereich der Klasse (0x0056E160–0x0056E270) ist keine unbenannte Funktion mehr übrig |

## AgpmAuction (eingebaut 6, gemeinsamer Rumpf 14, nicht im Client 4, ohne Kandidat 5, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RemoveAllSales` | 38 | zugeordnet | `0x0055E330` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseRowsetPacket` | 42 | zugeordnet | `0x0055E470` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DestroySales` | 6 | zugeordnet | `0x0055DED0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCAD` | 5 | zugeordnet | `0x0055DF00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxSales` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSales` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIAuction::CBUpdateUI, AgcmUIItem::CBSalesBox2ClickCancelCompleteButton, AgcmUIItem::GetSalesOfIndex |
| `AddSales` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `RemoveSales` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmAuction::RemoveAllSales |
| `ConAgpdAuctionCAD` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `DesAgpdAuctionCAD` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `MakeEventPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmAuction::SendOpenAuction |
| `UpdateSalesStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmAuction::OnReceive |
| `UpdateSalesStatus` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnReceive; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `AddSalesToCAD` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnReceive; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `RemoveSalesFromCAD` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnReceive; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `RemoveSalesFromCAD` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmAuction::OnReceive |
| `FindSalesFromCAD` | 23 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckTicket` | 34 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsAbleToOpenAnywhere` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIAuction::CBOpenAnywhere |
| `SetCallbackAddSales` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveSales` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateSales` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSelect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSelect2` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSell` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCancel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackConfirm` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNotify` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOpenAuction` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLogin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestAllSales` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOpenAnywhere` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmBillInfo (Kandidat unbestätigt 1, eingebaut 1, gemeinsamer Rumpf 3, nicht im Client 3, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetADCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo, AgcmCashMall::SendPacketRefreshCash, AgcmCharacter::UpdateTransparent |
| `MakePacketBillInfo` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `UpdateIsPCRoom` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::SetCharBitFlag; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `SetCallbackUpdateBillInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `IsPCBang` | 7 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `SetCashGlobal` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmBillInfo::OnReceive; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetCashGlobal` | 12 | Kandidat unbestätigt | `0x00587D40` | Aufrufer im Client: AgcmUICashMall::RefreshCashEdit, AgcmUICashMall::CBIsActiveBuy, AgcmUICashMall::CBDisplayBuyProductDetailValueUseCash; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetGUIDGlobal` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmBillInfo::OnReceive; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetGUIDGlobal` | 9 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |

## AgpmBuddy (Kandidat unbestätigt 1, eingebaut 11, gemeinsamer Rumpf 17, nicht im Client 12, ohne Kandidat 8, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsExistBuddy` | 26 | zugeordnet | `0x0056D5D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MentorBuddy` | 18 | zugeordnet | `0x0056D730` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle2` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetAttachAgpdBuddyData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIBuddy::OperationOnlineBuddy, AgcmUIBuddy::CBCheckBlockWhisper, AgcmUIBuddy::CBCheckBlockTrade |
| `MakePacketBuddy` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmBuddy::MakePacketAddBuddy, AgpmBuddy::MakePacketAddRequest, AgpmBuddy::MakePacketAddReject; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `MakePacketAddBuddy` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendAddBuddy |
| `MakePacketAddRequest` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendAddRequest |
| `MakePacketAddReject` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendAddReject |
| `MakePacketRemoveBuddy` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendRemoveBuddy |
| `MakePacketUpdateOptions` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendOption |
| `MakePacketOnline` | 6 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakePacketMsgCode` | 6 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketRegion` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendRegion |
| `MakePacketInitEnd` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketMentorRequest` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendMentorRequest |
| `MakePacketMentorDelete` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendMentorDelete |
| `MakePacketMentorRequestAccept` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendMentorRequestAccept |
| `MakePacketMentorRequestReject` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIBuddy::SendMentorRequestReject |
| `MakePacketMentorUIOpen` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOptions` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOnline` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMsgCode` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRegion` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitEnd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMentorRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMentorDelete` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMentorRequestAccept` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMentorRequestReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMentorUIOpen` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `_AddBuddy` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmBuddy::AddBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `_RemoveBuddy` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmBuddy::RemoveBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `_OptionsBuddy` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmBuddy::OptionsBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `_MentorBuddy` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmBuddy::MentorBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `AddBuddy` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIBuddy::OperationAddBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `IsFullBuddyList` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `RemoveBuddy` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIBuddy::OperationRemoveBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `OptionsBuddy` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIBuddy::OperationOptionsBuddy; kein unbenannter Kandidat mit Beleg unter 24 unbenannten Funktionen im Klassenbereich |
| `IsAlreadyMentor` | 10 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsAlreadyMentee` | 15 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `OverMenteeNumber` | 10 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `UnderMentorLevel` | 7 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `OverMenteeLevel` | 7 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetMentorStatus` | 17 | Kandidat unbestätigt | `0x0056CCA0` | Aufrufer im Client: AgcmUIBuddy::CBDisplayMentorRelation, AgcmUIBuddy::CBMentorSelect, AgcmUIBuddy::CBMentorAddAndDel; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `GetMentorCID` | 22 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `ReadMentorConstrinctFile` | 41 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmCashMall (eingebaut 4, gemeinsamer Rumpf 9, nicht im Client 5, ohne Kandidat 10, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DecodeProductList` | 58 | zugeordnet | `0x00557120` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashItem` | 6 | zugeordnet | `0x00556BF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetADCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo, AgcmCashMall::SendPacketRefreshCash, AgcmCharacter::UpdateTransparent |
| `OnOperationResponseBuyResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCashMall::OnReceive |
| `OnOperationCheckListVersion` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmCashMall::OnReceive; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `GetCashMallInfo` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCashMall::DestroyAllDummyItem, AgcmCashMall::CBUpdateMallList, AgcmUICashMall::SetItemGrid |
| `SetMaxProduct` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddCashItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICashInven::CBAddCashItem, AgpmCashMall::DecodeProductList, AgpmCashMall::StreamReadCashMallItemList |
| `RefreshMallList` | 12 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackRequestMallProductList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestBuyItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseBuyResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMallList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRefreshCash` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckListVersion` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDisableForaWhile` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `EncodeTabList` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmCashMall::StreamReadCashMallTab; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `DecodeTabList` | 92 | ohne Kandidat |  | Aufrufer im Client: AgpmCashMall::OnOperationResponseMallList; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `EncodeProductList` | 38 | ohne Kandidat |  | Aufrufer im Client: AgpmCashMall::StreamReadCashMallItemList; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `MakePacketRequestMallInfo` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmCashMall::SendPacketRequestMallList; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `MakePacketMallTabInfo` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketMallProductInfo` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketBuyProduct` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmCashMall::SendPacketBuyProduct; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `MakePacketBuyResult` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketRefreshCash` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmCashMall::SendPacketRefreshCash; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `MakePacketCheckListVersion` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmCashMall::SendPacketCheckListVersion; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `StreamReadCashMallTab` | 73 | ohne Kandidat |  | Aufrufer im Client: AgpmCashMall::RefreshMallList; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `StreamReadCashMallItemList` | 133 | ohne Kandidat |  | Aufrufer im Client: AgpmCashMall::RefreshMallList; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |

## AgpmCasper (gemeinsamer Rumpf 4, nicht im Client 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketMemoryOverflow` | 9 | zugeordnet | `0x0056A3C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestConnection` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketConnectionSuccess` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketConnectionFail` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackRequestConnection` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackConnectionSuccess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackConnectionFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMemoryOverflow` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmChannel (eingebaut 4, gemeinsamer Rumpf 14, nicht im Client 5, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CreateChannelData` | 19 | zugeordnet | `0x00560D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxChannel` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle2` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `DestroyChannelData` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIChannel::OperationCloseChannel |
| `AgpdJoinChannelDestructor` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmChannel::OnAddModule |
| `GetAttachAgpdJoinChannelData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmChannel::AgpdJoinChannelConstructor |
| `SetCallbackCreateChannel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDestroyChannel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackJoin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLeave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInvitation` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPassword` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChatMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackFindUser` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddUser` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveUser` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMsgCode` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketCreateChannel` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIChannel::SendCreateChannel |
| `MakePacketDestroyChannel` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketMsgCode` | 6 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketAddUser` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketRemoveUser` | 3 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmCharacter (Kandidat unbestätigt 37, eingebaut 57, gemeinsamer Rumpf 121, nicht im Client 96, ohne Kandidat 56, zugeordnet 89)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetVehicleTID` | 25 | zugeordnet | `0x00504CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAttackable` | 18 | zugeordnet | `0x00505CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckNormalAttack` | 31 | zugeordnet | `0x00505F60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadTemplate` | 76 | zugeordnet | `0x00525150` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TransformCharacterAppear` | 16 | zugeordnet | `0x0050E1F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsTargetable` | 18 | zugeordnet | `0x00505D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateTemplate` | 37 | zugeordnet | `0x00505470` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateBankSize` | 9 | zugeordnet | `0x00501B20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateCustomizeIndex` | 13 | zugeordnet | `0x00501AC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SubMoney` | 2 | zugeordnet | `0x0058A300` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetWorldDirection` | 16 | zugeordnet | `0x0050E5A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TransformCharacter` | 5 | zugeordnet | `0x0050E6C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckStopFollow` | 13 | zugeordnet | `0x0050E0E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `HasPenalty` | 32 | zugeordnet | `0x00505A00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckCharName` | 7 | zugeordnet | `0x00504A10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetAttackIntervalMSec` | 9 | zugeordnet | `0x00504580` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsHitHeroic` | 12 | zugeordnet | `0x00503D60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharacterTemplate` | 4 | zugeordnet | `0x0058A130` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCharacterTemplate` | 15 | zugeordnet | `0x005055B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCharacter` | 69 | zugeordnet | `0x00502DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsShrineTypifier` | 7 | zugeordnet | `0x00502CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsGuard` | 7 | zugeordnet | `0x00502CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsGM` | 7 | zugeordnet | `0x00502C80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsCreature` | 7 | zugeordnet | `0x00502C30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusTame` | 7 | zugeordnet | `0x00502C00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusGo` | 9 | zugeordnet | `0x00502BD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusSleep` | 9 | zugeordnet | `0x00502BA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusDisableNormalATK` | 9 | zugeordnet | `0x00502B70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusDisableSkill` | 9 | zugeordnet | `0x00502B40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusFullTransparent` | 6 | zugeordnet | `0x00502AF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusHalfTransparent` | 9 | zugeordnet | `0x00502AC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusInvincible` | 9 | zugeordnet | `0x00502A90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusTransparent` | 9 | zugeordnet | `0x00502A60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusFixed` | 10 | zugeordnet | `0x00502A10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsStatusSummoner` | 7 | zugeordnet | `0x005029E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsNPC` | 7 | zugeordnet | `0x005029B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPC` | 7 | zugeordnet | `0x00502980` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsMonster` | 7 | zugeordnet | `0x00502950` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPolyMorph` | 15 | zugeordnet | `0x00502920` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTypePolyMorph` | 7 | zugeordnet | `0x00502900` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateCharismaPoint` | 18 | zugeordnet | `0x00501860` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 36 | zugeordnet | `0x005060F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRegionNPC` | 24 | zugeordnet | `0x0057F0A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCharismaPoint` | 7 | zugeordnet | `0x005018F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateStatus` | 4 | zugeordnet | `0x005014B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateRegion` | 31 | zugeordnet | `0x005013C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdatePosition` | 4 | zugeordnet | `0x005010A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateInit` | 30 | zugeordnet | `0x00501040` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TransformCharacterStatus` | 35 | zugeordnet | `0x0050E250` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MoveCharacter` | 2 | zugeordnet | `0x0050EAD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MoveCharacterFollow` | 159 | zugeordnet | `0x0050EF30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetValidDestination` | 228 | zugeordnet | `0x00507230` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCharGrowUpFactor` | 229 | zugeordnet | `0x00503DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetMurdererLevel` | 2 | zugeordnet | `0x00505880` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUnion` | 9 | zugeordnet | `0x00505830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessActionPacket` | 39 | zugeordnet | `0x005056D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessMovePacket` | 107 | zugeordnet | `0x00508590` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllCharactersExceptOne` | 32 | zugeordnet | `0x00506290` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllCharacters` | 12 | zugeordnet | `0x005061E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 36 | zugeordnet | `0x00506160` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyTemplate` | 15 | zugeordnet | `0x00505540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessIdleMove` | 349 | zugeordnet | `0x00507CC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TurnCharacter` | 2 | zugeordnet | `0x0050E360` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SyncMoveStartPosition` | 15 | zugeordnet | `0x0050DE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckStopFollow` | 13 | zugeordnet | `0x005053C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsInPvPDanger` | 14 | zugeordnet | `0x00504800` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketOptionFlag` | 41 | zugeordnet | `0x00504770` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddCharacterToMap` | 68 | zugeordnet | `0x00503930` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessRemove` | 89 | zugeordnet | `0x005044C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTaxRatio` | 13 | zugeordnet | `0x0058A7F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `PayTax` | 10 | zugeordnet | `0x0058A780` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StopCharacter` | 2 | zugeordnet | `0x0050E8A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RestoreTransformCharacter` | 2 | zugeordnet | `0x0050E760` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MoveCharacterFollow` | 159 | zugeordnet | `0x005079D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharacterRace` | 5 | zugeordnet | `0x00505330` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSameRace` | 18 | zugeordnet | `0x005051D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsActionBlockCondition` | 42 | zugeordnet | `0x005046F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetActionBlockTime` | 13 | zugeordnet | `0x005046A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetHeroicPoint` | 9 | zugeordnet | `0x00504330` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetSkillPoint` | 9 | zugeordnet | `0x005042E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharismaPoint` | 13 | zugeordnet | `0x00503AE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMurdererPoint` | 2 | zugeordnet | `0x00503A60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveCharacterFromMap` | 59 | zugeordnet | `0x00503870` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReflectFactorPacket` | 9 | zugeordnet | `0x00503830` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTemplateSequence` | 7 | zugeordnet | `0x00502FB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharSequence` | 7 | zugeordnet | `0x00502F90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsInSiege` | 16 | zugeordnet | `0x00502DA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DestroyCharacter` | 29 | zugeordnet | `0x00502760` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateCharacter` | 109 | zugeordnet | `0x00502540` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnValid` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetCharacterType` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmCharacter::IsPolyMorph, AgpmCharacter::IsMonster, AgpmCharacter::IsPC |
| `SetTypeMonster` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTypePC` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTypeNPC` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTypeTrap` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTypeGuard` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetShrineTypifier` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetStatusTame` | 15 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SetStatusSummoner` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::RemoveSummons; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SetStatusFixed` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::RemoveSummons; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SetTypeAttackable` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTypeTargetable` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsStatusWasTamed` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSpawn::RemoveMonsterFromSpawnList; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `IsStatusAttrInvincible` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsStatusNormalATKInvincible` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsStatusSkillATKInvincible` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsCreature` | 8 | Kandidat unbestätigt | `0x0057FF00` | Aufrufer im Client: AgpmCharacter::RemoveCharacterFromMap, AgpmCharacter::AddCharacterToMap, AgpmCharacter::UpdatePosition; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsPet` | 8 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsMovable` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsTrap` | 15 | Kandidat unbestätigt | `0x00584320` | Aufrufer im Client: AgcmCharacter::CBUpdatePosition, AgcmEventEffect::EventInitCB, AgcmTargeting::OnLButtonDown; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsInDungeon` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIGuild::CBGuildListToggle |
| `GetCharacter` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCamera2::CBOnTargetSet, AgcmCharacter::ActionSelfCharacter, AgcmCharacter::LockTarget |
| `GetCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::CBOnTargetSet, AgcmCharacter::ActionSelfCharacter, AgcmCharacter::LockTarget |
| `GetCharacterLock` | 13 | Kandidat unbestätigt | `0x00502E50` | Aufrufer im Client: AgcmGuild::RenameGuild, AgcmTextBoardMng::GetGuildIDColor, AgcmUIGuild::CBReceiveLeaveRequestSelf; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetCharacterLock` | 13 | Kandidat unbestätigt | `0x00502E50` | Aufrufer im Client: AgcmGuild::RenameGuild, AgcmTextBoardMng::GetGuildIDColor, AgcmUIGuild::CBReceiveLeaveRequestSelf; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetCharacterLock` | 35 | Kandidat unbestätigt | `0x0058B350` | Aufrufer im Client: AgcmGuild::RenameGuild, AgcmTextBoardMng::GetGuildIDColor, AgcmUIGuild::CBReceiveLeaveRequestSelf; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetCharacterLockByPointer` | 69 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ResetMonsterData` | 46 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCharacterTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIScreamEditDlg::OnInitDialog, AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcuCamMode::SetCameraInfo |
| `GetCharacterTemplateUseCID` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveCharacterTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::RemoveAllCharacterTemplate |
| `RemoveCharacterTemplate` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::RemoveAllCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `RemoveAllCharacterTemplate` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetRaceCharacterTemplate` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRaceFromTemplate` | 5 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `IsCharacter` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsCharacter` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxCharacter` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxCharacterTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CharacterLoader::Initialize, AgpmCharacter::StreamReadTemplate |
| `GetMaxCharacterTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxCharacterRemove` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetIdleIntervalMSec` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetProcessMoveFollowInterval` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachCharacterData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmEventEffect::OnAddModule, AgcmSkill::OnAddModule |
| `AttachCharacterTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmEventEffect::OnAddModule, SequenceNumberManager::AttachTemplateSequenceData |
| `InitFactor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::ClearActionFactor, AgcmCharacter::GetNextReceivedActionDamageFactor, AgcmCharacter::ApplyActionData |
| `CheckActionStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::MoveCharacterFollow, AgpmCharacter::MoveCharacter, AgpmCharacter::MoveCharacterFollow |
| `CheckActionStatus` | 31 | Kandidat unbestätigt | `0x0050EA40` | Aufrufer im Client: AgpmCharacter::MoveCharacterFollow, AgpmCharacter::MoveCharacter, AgpmCharacter::MoveCharacterFollow; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CheckVaildNormalAttackTarget` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::ActionSelfCharacter; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CheckActionRequirement` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::ActionSelfCharacter; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `PayActionCost` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackInitChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNewCreatedCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddCharPost` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResetMonster` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDeleteChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoveChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStopChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateActionStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateActionStatusCheck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateSpecialStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCriminalStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdatePositionCheck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdatePosition` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPreUpdatePosition` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckIsActionMove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionAttack` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionAttackMiss` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionPickupItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventTeleport` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventNPCTrade` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventItemConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventGuildWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventProduct` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventNPCDialog` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventSkillMaster` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventRefinery` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionProductSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventCharCustomize` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventItemRepair` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventRemission` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventWantedCriminal` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventSiegeWar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventTax` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventGamble` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionEventGacha` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionUseSiegeWarAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionCarveASeal` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTransformAppear` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTransformStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRestoreTransform` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCancelTransform` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEvolution` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRestoreEvolution` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMurdererPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMukzaPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCharismaPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateSkillPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveRide` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAlreadyExistChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateEventStatusFlag` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitTemplateDefaultValue` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReadAllCharacterTemplate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckAllBlockStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddStaticCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveProtectedNPC` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsStaticCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsArchlord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetBonusDropRate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetBonusDropRate2` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetBonusMoneyRate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetBonusCharismaRate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateNickName` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOnlineTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGameguardAuth` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResurrectionByOther` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventEffectID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPinchWantedAnswer` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPinchWantedRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckPCRoomType` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestCoupon` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallBackRecieveCouponInfo` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICouponBox::OnAddModule |
| `SetCallBackRecieveCouponUse` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICouponBox::OnAddModule |
| `SetCallBackCheckTeleportBlock` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackUpdateIgnoreStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule |
| `SetCallbackUpdateLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckRemoveChar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckRemoveChar2` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddAttackerToList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveAction` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckNowUpdateActionFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckValidNormalAttack` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckActionRequirement` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckActionAttackTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPayActionCost` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveCharacterData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDisconnectByAnotherUser` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMonsterAIPathFind` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStreamReadImportData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStreamReadImportDataErrorReport` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestResurrection` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetNewCID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsPlayerCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddCharacterToMap` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveCharacterFromMap` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetCombatMode` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResetCombatMode` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckProcessIdle` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBindingRegionChange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSocialAnimation` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReleaseActionMoveLock` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCustomize` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateOptionFlag` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateBankSize` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetItemLancer` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseEffect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `OnOperationTransform` | 12 | Kandidat unbestätigt | `0x00563170` | Aufrufer im Client: AgpmCharacter::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `ReceiveAddCharacter` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetUnion` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventUvUReward::IsValidSkull, AgpmSkill::OnReceiveSkill |
| `GetMurdererPoint` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBDisplaySlotCharVillian, AgcmUIRemission::CBDisplayCurrentPoint, AgpmCharacter::GetRemainedMurdererTime; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetRemainedCriminalTime` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmIDBoard::_IsCheckDrawByPVP; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetRemainedMurdererTime` | 20 | nicht im Client |  | Aufrufer nur im Server (6); kein Treffer im Binary |
| `SetLastCriminalTime` | 16 | Kandidat unbestätigt | `0x0058A520` | Aufrufer im Client: AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetLastMurdererTime` | 16 | Kandidat unbestätigt | `0x0058A520` | Aufrufer im Client: AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetLastUseEscapeTime` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetLastKilledTimeInBattleSquare` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SetLastUseEscapeTime` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationAdd; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SetLastKilledTimeInBattleSquare` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationAdd; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetMurdererLevel` | 7 | Kandidat unbestätigt | `0x0054DE60` | Aufrufer im Client: AcUIRaider::_CharacterType, AgcmIDBoard::_GetIDColorByPVP, AgcmTextBoardMng::CB_UpdateIDMurderIconFlag; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetMurdererLevelOfPoint` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::GetMurdererLevel; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetMukzaPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::IsMukza |
| `GetMukzaPoint` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::IsMukza; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `IsMurderer` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::UpdateMurdererPoint, AgpmDropItem2::ProcessDropItem |
| `IsMurderer` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::UpdateMurdererPoint, AgpmDropItem2::ProcessDropItem; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `IsMukza` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsMukza` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsHitHeroic` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::KeyboardIdleProcess, AgcmTargeting::OnLButtonDown, AgpmCharacter::MoveCharacter |
| `GetLevelUpExp` | 5 | nicht im Client |  | Aufrufer nur im Server (8); kein Treffer im Binary |
| `GetLevelUpExp` | 5 | nicht im Client |  | Aufrufer nur im Server (8); kein Treffer im Binary |
| `GetCharGrowUpTemplate` | 36 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetExp` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacter::CharacterStatusCB, AgcmUILogin::CBDisplaySlotCharExp, AgcmUIMain::CBDisplayExp; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetLevel` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmQuest::GetMainQuestNameColor, AgcmRecruit::SendSearchLFPByPage, AgcmRecruit::SendSearchLFMByPage |
| `GetLevelBefore` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::GetLevelOriginal, AgpmCharacter::SetCharacterLevelLimit, AgpmCharacter::GetCharacterLevelLimit |
| `GetLevelLimited` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::GetCharacterLevelLimit |
| `GetLevelFromTemplate` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetHP` | 5 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `GetMaxHP` | 5 | nicht im Client |  | Aufrufer nur im Server (9); kein Treffer im Binary |
| `AddAttackerToList` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationAddAttacker; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `IsInAttackerList` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearAttackerToList` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::UpdateActionStatus, AgpmCharacter::UpdateMurdererPoint; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetMoveSpeed` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::ProcessIdleMove, AgpmCharacter::AdjustMoveSpeed, AgpmCharacter::MoveCharacter |
| `GetMoveSpeed` | 26 | Kandidat unbestätigt | `0x00504440` | Aufrufer im Client: AgpmCharacter::ProcessIdleMove, AgpmCharacter::AdjustMoveSpeed, AgpmCharacter::MoveCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetFastMoveSpeed` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::ProcessIdleMove, AgpmCharacter::MoveCharacterFollow, AgpmCharacter::AdjustMoveSpeed |
| `GetFastMoveSpeed` | 26 | Kandidat unbestätigt | `0x00504440` | Aufrufer im Client: AgpmCharacter::ProcessIdleMove, AgpmCharacter::MoveCharacterFollow, AgpmCharacter::AdjustMoveSpeed; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `IsCombatMode` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmEventTeleport::CBExecuteEvent, AgcmItem::SendUseReturnScroll, AgcmUIItem::CBCheckUseItem |
| `SetCombatMode` | 16 | Kandidat unbestätigt | `0x0050E440` | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgpmCharacter::ActionCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ResetCombatMode` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::CharacterIdle; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `ClearActionBlockTime` | 9 | nicht im Client |  | Aufrufer nur im Server (6); kein Treffer im Binary |
| `PvPModeOn` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PvPModeOff` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRegionRefreshInterval` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRegionRefreshInterval` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::MoveCharacterFollow, AgpmCharacter::MoveCharacter, AgpmCharacter::MoveCharacterFollow |
| `MakePacketCharView` | 90 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakePacketCharView; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `MakeGameID` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckNameKr` | 47 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CheckNameCn` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CheckNameTw` | 113 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CheckNameJp` | 75 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CheckNameEn` | 35 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckFilterText` | 28 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `IsOptionFlag` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIOption::RefreshRefuseControl |
| `IsOptionFlag` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIOption::RefreshRefuseControl |
| `SetOptionFlag` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: COptionFlagController::OnRequestChangeOptionFlag, AgcmUIOption::SendOptionFlag, AgcmUIOption::SendOptionFlag |
| `SetOptionFlag` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: COptionFlagController::OnRequestChangeOptionFlag, AgcmUIOption::SendOptionFlag, AgcmUIOption::SendOptionFlag |
| `UnsetOptionFlag` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: COptionFlagController::OnRequestChangeOptionFlag, AgcmUIOption::SendOptionFlag, AgcmUIOption::CBSystemMessage |
| `UnsetOptionFlag` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: COptionFlagController::OnRequestChangeOptionFlag, AgcmUIOption::SendOptionFlag, AgcmUIOption::CBSystemMessage |
| `SetCallbackUpdateLevelPost` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketCharLevel` | 46 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCharAction` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendActionInfo; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SetCallbackBlockByPenalty` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `IsRideOn` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::CBOnTargetSet, AgcuCamMode::SetCameraInfo, AgcmCharacter::SelfMoveDirection |
| `GetRemovePoolCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::AddRemoveCharacter |
| `AddGameBonusExp` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SubGameBonusExp` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetGameBonusExp` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddGameBonusMoney` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SubGameBonusMoney` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetGameBonusMoney` | 8 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `AddGameBonusDropRate` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddGameBonusDropRate2` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SubGameBonusDropRate` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SubGameBonusDropRate2` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetGameBonusDropRate` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessDropItem; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetGameBonusDropRate2` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessDropItem2; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `AddGameBonusCharismaRate` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SubGameBonusCharismaRate` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetGameBonusCharismaRate` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsAllBlockStatus` | 15 | Kandidat unbestätigt | `0x0055D8C0` | Aufrufer im Client: AgpmAuction::OnReceive, AgpmCashMall::OnOperationRequestMallProductList, AgpmCashMall::OnOperationRequestBuyItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CollisionCylinder` | 69 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::GetValidDestination; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CollisionBox` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::GetValidDestination; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `IsDisableCharacter` | 8 | Kandidat unbestätigt | `0x0057FF00` | Aufrufer im Client: AgpmCharacter::CharacterIdle, AgpmCharacter::IsAllBlockStatus, AgpmPvP::IsAttackable; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsUseCharacter` | 8 | Kandidat unbestätigt | `0x005204C0` | Aufrufer im Client: AgcmTextBoardMng::GetStateTexture, AgcmUISiegeWar::OpenCatapultUI, AgcmUISiegeWar::OpenAtkResTowerUI; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsRepairCharacter` | 8 | Kandidat unbestätigt | `0x005204C0` | Aufrufer im Client: AgcmTextBoardMng::GetStateTexture, AgcmUISiegeWar::OpenCatapultUI, AgcmUISiegeWar::OpenAtkResTowerUI; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsArchlord` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::SendSocialAnimation, AgcmEventEffect::SetBaseSkillEventEffect, AgcmEventEffect::SetPassiveSkill |
| `IsArchlord` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::SendSocialAnimation, AgcmEventEffect::SetBaseSkillEventEffect, AgcmEventEffect::SetPassiveSkill |
| `GetBlockingType` | 24 | Kandidat unbestätigt | `0x005051A0` | Aufrufer im Client: AgcmCharacter::MoveSelfCharacter, AgcmCharacter::GetValidDestination, AgcmCharacter::CBUpdatePositionCheck; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `IsSameRace` | 12 | Kandidat unbestätigt | `0x0057FF00` | Aufrufer im Client: AgcmShrine::_ReservePrintMessage, AgcmShrine::IsOtherRace, AgcmTargeting::TargetNear; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetCharismaTitle` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmTextBoardMng::_CreateIDBoard; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetCharismaStep` | 10 | Kandidat unbestätigt | `0x00551CA0` | Aufrufer im Client: AgcmHPBar::SetData, AgcmIDBoard::_DrawFlag, AgcmIDBoard::_DrawCharisma; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsInJail` | 10 | nicht im Client |  | Aufrufer nur im Server (8); kein Treffer im Binary |
| `IsInConsulationOffice` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketGameguardAuth` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendGameGuardAuth; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `MakePacketOnlineTime` | 40 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResurrectionByOther` | 40 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketEventEffectID` | 40 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `InitFuncPtr` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::AgcmFont, AcUIEdit::AcUIEdit, AgpmCharacter::AgpmCharacter; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetCharacterRaceString` | 27 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsDisableChattingCharacter` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmChatting::OnReceive; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SetNationFlag` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckEnableActionCharacter` | 13 | Kandidat unbestätigt | `0x00505A70` | Aufrufer im Client: AgpmCharacter::ActionCharacter, AgpmItem::OnOperationUseItem, AgpmOptimizedPacket2::OnReceiveCharMove; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `StreamReadMurderPenalty` | 80 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `NegligiblePosition` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::MoveCharacter; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `AdjustMoveSpeed` | 62 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::ProcessMovePacket; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `MoveCharacter` | 211 | Kandidat unbestätigt | `0x00570B20` | Aufrufer im Client: AgcmCharacter::MoveSelfCharacter, AgcmCharacter::CBUpdateFactorMovement, AgcmSkill::ProcessReceiveCastSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `MoveCharacterToPositionWithDistance` | 124 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MoveCharacterHorizontal` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MoveCharacterHorizontal` | 71 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `TransformCharacter` | 37 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationTransform, AgpmCharacter::OnOperationTransform; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `EvolutionCharacter` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationEvolution; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `RestoreTransformCharacter` | 46 | Kandidat unbestätigt | `0x00502F80` | Aufrufer im Client: AgpmCharacter::RemoveCharacter, AgpmCharacter::OnOperationRestoreTransform; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `RestoreEvolutionCharacter` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationRestoreEvolution; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `StopCharacter` | 75 | Kandidat unbestätigt | `0x0050E440` | Aufrufer im Client: AgcmCharacter::SelfMoveDirection, AgcmCharacter::LockTarget, AgcmCharacter::SelectTarget; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `TurnCharacter` | 47 | Kandidat unbestätigt | `0x0050E440` | Aufrufer im Client: AgcmCharacter::TurnSelfCharacter, AgcmSkill::ProcessReceiveCastSkill, AgcmUICharacterSelect::_MakeCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `MoveTurnCharacter` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MoveTurnCharacter` | 125 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SyncActionPosition` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ActionCharacter` | 475 | Kandidat unbestätigt | `0x0053D540` | Aufrufer im Client: AgcmCharacter::ActionSelfCharacter, AgpmCharacter::ProcessActionPacket, AgpmCharacter::StopCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `GetSelfCharacterTurnAngle` | 34 | Kandidat unbestätigt | `0x0050EA40` | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUIQuest2::StartAnimation, AgpmCharacter::MoveCharacterFollow; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsSufficientCost` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkillCheck, AgcmSkill::CastSkill, AgcmUISkill2::IsEnableSkill; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetMeleeActionCostMP` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::CBCheckActionRequirement; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `CheckLockAction` | 17 | Kandidat unbestätigt | `0x0050EA40` | Aufrufer im Client: AgpmCharacter::MoveCharacterFollow, AgpmCharacter::MoveCharacter, AgpmCharacter::MoveCharacterFollow; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate |
| `SetMoney` | 15 | Kandidat unbestätigt | `0x0058A520` | Aufrufer im Client: AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::SendMoveMoneyFromInventoryToBank, AgcmItem::SendDropMoneyToField, AgcmPrivateTrade::SendTradeUpdateMoney |
| `GetMoney` | 7 | Kandidat unbestätigt | `0x0058A3F0` | Aufrufer im Client: AgcmCharacter::SendMoveMoneyFromInventoryToBank, AgcmItem::SendDropMoneyToField, AgcmPrivateTrade::SendTradeUpdateMoney; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CheckMoneySpace` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::InitializeSkillTree |
| `CheckMoneySpace` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::InitializeSkillTree |
| `AddMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::OnOperationMoveBankMoney, AgpmEventSkillMaster::InitializeSkillTree, AgpmGuildWarehouse::AddMoney |
| `AddMoney` | 22 | Kandidat unbestätigt | `0x0058A270` | Aufrufer im Client: AgpmCharacter::OnOperationMoveBankMoney, AgpmEventSkillMaster::InitializeSkillTree, AgpmGuildWarehouse::AddMoney; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SubMoney` | 15 | Kandidat unbestätigt | `0x0058A200` | Aufrufer im Client: AgcmUIRefinery::CBRefine, AgpmCharacter::OnOperationMoveBankMoney, AgpmEventCharCustomize::OnOperationBuy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetBankMoney` | 14 | Kandidat unbestätigt | `0x0058A520` | Aufrufer im Client: AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetBankMoney` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::SendMoveMoneyFromBankToInventory, AgcmUIEventBank::CBUpdateBankMoney, AgpmCharacter::OnOperationMoveBankMoney |
| `AddBankMoney` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationMoveBankMoney; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SubBankMoney` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationMoveBankMoney; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `SetCash` | 14 | Kandidat unbestätigt | `0x0058A520` | Aufrufer im Client: AgpmBillInfo::OnReceive, AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetCash` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmTitle::_CheckIsValidRequireCash, AgcmUICashMall::RefreshCashEdit, AgcmUICashMall::CBIsActiveBuy |
| `AddCash` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SubCash` | 27 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `SetCallbackUpdateMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateBankMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCash` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoveBankMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUISetMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPayTax` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetTaxRatio` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `StreamRead` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamReadCB, AgcmExportResource::ReadUIINI, AgcmItem::ItemTemplateStreamReadCB |
| `StreamWrite` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB |
| `StreamWriteTemplate` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `StreamReadStaticCharacter` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadOneStaticCharacter` | 51 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `PrintRegionNPCList` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWriteStaticCharacter` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StaticOneCharacterWriteCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::OnAddModule |
| `CharacterReadCB` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmCharacter::OnAddModule |
| `CharacterWriteCB` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmCharacter::OnAddModule |
| `StreamWriteCharKind` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadCharKind` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadLevelUpExpTxt` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadCharGrowUpTxt` | 58 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadImportData` | 980 | Kandidat unbestätigt | `0x00546C70` | Aufrufer im Client: AgcmUILogin::LoadTemplates, AgpmItem::StreamReadImportData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `StreamReadCharismaTitle` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateFactor` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmEventFactors::ProcessUpdateEventFactors, AgpmEventFactors::ProcessUpdateFactor, AgpmFactors::UpdateFactor |
| `UpdateFactor` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmEventFactors::ProcessUpdateEventFactors, AgpmEventFactors::ProcessUpdateFactor, AgpmFactors::UpdateFactor; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdatePosition` | 127 | Kandidat unbestätigt | `0x0051A750` | Aufrufer im Client: AgcmCharacter::CharacterPosIdleProcess, AgcmCharacter::InitCharacterMainThread, AgcmCharacter::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `UpdateStatus` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::OnReceive, AgpmCharacter::OnOperationUpdate, AgpmCharacter::MoveTurnCharacter; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateActionStatus` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::CBUpdateCharacter2, AgpmCharacter::OnOperationUpdate, AgpmCharacter::MoveCharacterFollow |
| `UpdateActionStatus` | 31 | Kandidat unbestätigt | `0x0050EA40` | Aufrufer im Client: AgcmCharacter::CBUpdateCharacter2, AgpmCharacter::OnOperationUpdate, AgpmCharacter::MoveCharacterFollow; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `UpdateSpecialStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::OnOperationUpdate |
| `UpdateSpecialStatus` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateSetSpecialStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::SetCharacterLevelLimit |
| `UpdateSetSpecialStatus` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::SetCharacterLevelLimit; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateUnsetSpecialStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::ReleaseCharacterLevelLimit, AgpmSiegeWar::CheckCarveASeal |
| `UpdateUnsetSpecialStatus` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::ReleaseCharacterLevelLimit, AgpmSiegeWar::CheckCarveASeal; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateCriminalStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::OnOperationUpdate |
| `UpdateCriminalStatus` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateMurdererPoint` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::AddMurdererPoint, AgpmCharacter::SubMurdererPoint; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `AddMurdererPoint` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SubMurdererPoint` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `UpdateMukzaPoint` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SubCharismaPoint` | 9 | nicht im Client |  | Aufrufer nur im Server (6); kein Treffer im Binary |
| `UpdateLevel` | 2 | nicht im Client |  | Aufrufer nur im Server (6); kein Treffer im Binary |
| `UpdateLevel` | 7 | nicht im Client |  | Aufrufer nur im Server (6); kein Treffer im Binary |
| `ChangedLevel` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationLevelUp; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateSkillPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::UpdateSkillPoint, AgcmSkill::CBLearnSkill, AgpmSkill::AddSkillPoint |
| `UpdateSkillPoint` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::UpdateSkillPoint, AgcmSkill::CBLearnSkill, AgpmSkill::AddSkillPoint; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateHeroicPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::AdjustHeroicPoint |
| `UpdateHeroicPoint` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::AdjustHeroicPoint; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateHeroicPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::AdjustHeroicPoint |
| `UpdateHeroicPoint` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::AdjustHeroicPoint; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateMoney` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::AddItemToInventory, AgpmItem::AddItemToInventory |
| `UpdateMoney` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToInventory, AgpmItem::AddItemToInventory; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `UpdateEventStatusFlag` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetLevelOriginal` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCharacterLevelLimit` | 17 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `ReleaseCharacterLevelLimit` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::SetCharacterLevelLimit; kein unbenannter Kandidat mit Beleg unter 1084 unbenannten Funktionen im Klassenbereich |
| `GetCharacterLevelLimit` | 17 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |

## AgpmChatting (eingebaut 4, gemeinsamer Rumpf 17, nicht im Client 9, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketChatting` | 38 | zugeordnet | `0x0056E480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OperationChat` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnOperationOfflineWhisperTarget` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmChatting::OnReceive |
| `MakePacketSetBlockWhisper` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketReleaseBlockWhisper` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketReplyBlockWhisper` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketOfflineWhisperTarget` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackRecvNormalMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvWordBalloonMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvUnionMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvGuildMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvPartyMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvWhisperMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvWholeWorldMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvSystemLevel1Msg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvSystemLevel2Msg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvSystemLevel3Msg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckEnable` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckBlockWhisper` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvReplyBlockWhisper` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvOfflineWhisperTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvGuildJointMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvEmphasisMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `DesAgpdCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmChatting::OnAddModule |
| `GetADCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo, AgcmCashMall::SendPacketRefreshCash, AgcmCharacter::UpdateTransparent |
| `GetLastWhisperSenderID` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddCommand` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCommand` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmChatting::DispatchCommand |
| `RemoveCommand` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DispatchCommand` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmConfig (eingebaut 5, gemeinsamer Rumpf 3, nicht im Client 50, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle2` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SendConfigPacket` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetEventNumber` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetEventNumber` | 2 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `SetExpAdjustmentRatio` | 9 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetExpAdjustmentRatio` | 7 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `SetDropAdjustmentRatio` | 9 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetDropAdjustmentRatio` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessDropItem, AgpmDropItem2::GetDropRate; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetDrop2AdjustmentRatio` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetDrop2AdjustmentRatio` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessDropItem2; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetGheldDropAdjustmentRatio` | 9 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetGheldDropAdjustmentRatio` | 7 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `SetCharismaDropAdjustmentRatio` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetCharismaDropAdjustmentRatio` | 7 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SetAdultServer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsAdultServer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetAllAdmin` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsAllAdmin` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmAdmin::IsAdminCharacter, AgpmAdmin::IsAdminCharacter, AgpmAdmin::GetAdminLevel |
| `SetNewServer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsNewServer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetEventServer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEventServer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetAimEventServer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsAimEventServer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPCDropItemOnDeath` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `DoesPCDropItemOnDeath` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetExpPenaltyOnDeath` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `DoesExpPenaltyOnDeath` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetIniDir` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetIniDir` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetAccountAuth` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsNoAccountAuth` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmConfig::IsWebAccountAuth; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `IsIgnoreAccountAuth` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsWebAccountAuth` | 4 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsDBAccountAuth` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmConfig::IsWebAccountAuth |
| `SetIgnoreLogFail` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsIgnoreLogFail` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetFileLog` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsFileLog` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetEventChatting` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsEventChatting` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::IsDurationUnlimited |
| `SetEventResurrect` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEventResurrect` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetEventItemDrop` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEventItemDrop` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetServerStatusFlag` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `ResetServerStatusFlag` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsSetServerStatusFlag` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetMaxUserCount` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetMaxUserCount` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetEnableAuction` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsEnableAuction` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetEnableQuest` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetEnableEventItemEffect` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEnableEventItemEffect` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetEnablePvP` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEnablePvP` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmPvP::IsAttackable, AgpmPvP::IsSkillEnable |
| `IsPromotionServer` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSiegeWar::OnOperationDefenseApplication, AgpmSiegeWar::OnOperationAttackApplication, AgpmSiegeWar::OnOperationRequestAttackApplGuildList |
| `SetPromotionServer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmEventBank (gemeinsamer Rumpf 3, nicht als eigene Funktion 2, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnOperationGrant` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmEventBank::OnReceive, AgpmEventCook::OnReceive, AgpmEventGuild::OnReceive; im Adressbereich der Klasse (0x005750A0–0x00575310) ist keine unbenannte Funktion mehr übrig |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrantAnywhere` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventRequest` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmArchlord::SendRequestEvent, AgcmEventBank::CBEventBank, AgcmEventCook::CBEventRequest; im Adressbereich der Klasse (0x005750A0–0x00575310) ist keine unbenannte Funktion mehr übrig |
| `MakePacketEventGrant` | 18 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `MakePacketGrantAnywhere` | 12 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmEventCharCustomize (eingebaut 2, gemeinsamer Rumpf 2, nicht im Client 2, ohne Kandidat 1, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `StreamReadCustomizeList` | 72 | zugeordnet | `0x005265B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketRequestCustomize` | 23 | zugeordnet | `0x00524570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestEvent` | 20 | zugeordnet | `0x005244E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UsingCustomizingItem` | 43 | zugeordnet | `0x00524780` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationBuy` | 94 | zugeordnet | `0x00524A10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetItemCount` | 31 | zugeordnet | `0x005246D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketResponseEvent` | 20 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetCustomizeCase` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckCharacterStatus` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmEventCharCustomize::OnOperationRequest, AgpmEventSkillMaster::OnOperationRequestEvent; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CheckValidRange` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmArchlord::OnOperationEventRequest, AgpmAuction::OnReceive, AgpmEventBank::OnOperationRequest |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAfterUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetPriceWithTax` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventCharCustomize::OnOperationBuy |

## AgpmEventGacha (nicht im Client 7, ohne Kandidat 1, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventGacha` | 34 | zugeordnet | `0x00569550` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequest` | 33 | zugeordnet | `0x00569480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamReadGachaTypeTable` | 79 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketEventRequestGranted` | 61 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketEventResult` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `BuildGachaItemTable` | 142 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReportGachaTable` | 110 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetGachaTypeInfo` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmEventGacha::MakePacketEventRequestGranted, AgpmEventGacha::BuildGachaItemTable, AgpmEventGacha::GetGachaItem; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `GetGachaItem` | 57 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckProperGacha` | 102 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |

## AgpmEventGuide (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBEventConstructor` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; im Adressbereich der Klasse (0x0056EB40–0x0056ECC0) ist keine unbenannte Funktion mehr übrig |
| `CBEventDestructor` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; im Adressbereich der Klasse (0x0056EB40–0x0056ECC0) ist keine unbenannte Funktion mehr übrig |

## AgpmEventGuild (gemeinsamer Rumpf 6, nicht im Client 3, ohne Kandidat 3, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequestWorldChampionship` | 18 | zugeordnet | `0x005746B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequestWarehouse` | 18 | zugeordnet | `0x00574630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequest` | 18 | zugeordnet | `0x005745B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationGrant` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventBank::OnReceive, AgpmEventCook::OnReceive, AgpmEventGuild::OnReceive; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `OnOperationGrantWarehouse` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventGuild::OnReceive; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `OnOperationGrantWorldChampionship` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventGuild::OnReceive; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrantWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestWorldChampionship` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrantWorldChampionship` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 18 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `MakePacketEventGrantWarehouse` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketEventGrantWorldChampionship` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmEventItemConvert (gemeinsamer Rumpf 3, nicht als eigene Funktion 1, nicht im Client 1, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketRequest` | 18 | zugeordnet | `0x00574C60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationRequest` | 31 | zugeordnet | `0x00574B60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketGrant` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketReject` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmParty::SendPacketReject; im Adressbereich der Klasse (0x00574B60–0x00574E20) ist keine unbenannte Funktion mehr übrig |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmEventItemRepair (eingebaut 1, gemeinsamer Rumpf 7, nicht im Client 1, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 21 | zugeordnet | `0x00575190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketItemRepair` | 23 | zugeordnet | `0x005755E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetItemRepairPrice` | 41 | zugeordnet | `0x00575670` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackRepairReq` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRepairAck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRepairResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventReq` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CBEmbeddedReceiveEventPacket` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmEventItemRepair::OnAddModule, AgpmEventQuest::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketEventData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventItemRepair::CBEmbeddedMakeEventPacket, AgpmEventNPCDialog::CBMakePacketEventData, AgpmEventProduct::CBEmbeddedPacketEncode |
| `ParseEventDataPacket` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmEventItemRepair::CBEmbeddedReceiveEventPacket, AgpmEventNPCDialog::CBParsePacketEventData, AgpmEventQuest::CBEmbeddedReceiveEventPacket; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `MakePacketEventGrant` | 20 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |

## AgpmEventNPCDialog (gemeinsamer Rumpf 2, nicht im Client 4, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 18 | zugeordnet | `0x005766D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParseEventDataPacket` | 18 | zugeordnet | `0x005764F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventData` | 12 | zugeordnet | `0x005764B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMobKeyDialogTemplate` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNPCDialog::GetMobDialog; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetMobDialogTemplate` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNPCDialog::LoadMobDialogRes, AgpmEventNPCDialog::GetMobDialog; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `LoadMobDialogRes` | 210 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMobTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMobDialog` | 44 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 18 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |

## AgpmEventNature (eingebaut 13, gemeinsamer Rumpf 5, nicht im Client 18, ohne Kandidat 5, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetSkySet` | 15 | zugeordnet | `0x0051E960` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 4 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetWeather` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackNature` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallback_AddSky` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallback_RemoveSky` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CreateSkySet` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNature::AddSkySet, AgpmEventNature::SkySet_StreamRead; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `DeleteSkySet` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmEventNature::AddSkySet, AgpmEventNature::RemoveSkySet, AgpmEventNature::SkySet_StreamRead |
| `AddSkySet` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNature::SkySet_StreamRead, AgpmEventNature::AddDefaultSkySet; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `AddSkySet` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNature::SkySet_StreamRead, AgpmEventNature::AddDefaultSkySet; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetEmptySkySetIndex` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveSkySet` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveSkySet` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SkySet_StreamWrite` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SkySet_StreamRead` | 54 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachSkySetData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::OnAddModule |
| `RemoveAllSkySet` | 22 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNature::OnDestroy, AgpmEventNature::SkySet_StreamRead, AgpmEventNature::AddDefaultSkySet; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `AddDefaultSkySet` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventNature::SkySet_StreamRead; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `CBEventNatureDestructor` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventNature::OnAddModule |
| `SetSpeedRate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSpeedRate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ConvertRealtoGameTime` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ConvertGametoRealTime` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetTimer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StartTimer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StopTimer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ToggleTimer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTime` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::OnInit, AgcmEventNature::OnIdle, AgcmEventNature::SetTime |
| `SetTime` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::OnInit, AgcmEventNature::OnIdle, AgcmEventNature::SetTime |
| `GetGameTime` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::OnInit, AgcmEventNature::OnIdle, AgcmEventNature::ApplySkySetting |
| `GetYear` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, CProgressDlg::ProcessAddFile, CProgressDlg::DirectoryCopy |
| `GetMonth` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, CProgressDlg::ProcessAddFile, CProgressDlg::DirectoryCopy |
| `GetDay` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, AgpmTimer::GetMonth, CProgressDlg::ProcessAddFile |
| `GetHour` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce |
| `IsPM` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMinute` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce, AgcmEventNature::ApplySkySetting |
| `GetSecond` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CProgressDlg::ProcessAddFile, CProgressDlg::DirectoryCopy, CRKEntryManager::AddEntry |
| `GetMS` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetDayTimeDWORD` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetHourTimeDWORD` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce |
| `GetDayMiliSecond` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmEventProduct (eingebaut 5, gemeinsamer Rumpf 6, nicht im Client 3, ohne Kandidat 4, zugeordnet 7)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetBuyCost` | 5 | zugeordnet | `0x0056FC30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidLearnSkill` | 36 | zugeordnet | `0x00570570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketLearnSkill` | 19 | zugeordnet | `0x00570830` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParsePacketEventData` | 13 | zugeordnet | `0x005701E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventData` | 10 | zugeordnet | `0x005701A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketBuyCompose` | 19 | zugeordnet | `0x0056FF30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequest` | 20 | zugeordnet | `0x0056FEB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsValidLearnSkill` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIProductSkill::IsActiveBuyItem |
| `IsValidBuyCompose` | 46 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProductSkill::IsActiveBuyItem; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `GetBuyCost` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIProductSkill::CBDisplayBuyPrice, AgcmUISkill2::CBDisplaySkillPrice, AgcmUISkill2::IsActiveBuyItem |
| `GetLearnableLevel` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIProductSkill::CBDisplayBuyPrice, AgpmEventProduct::IsValidLearnSkill, AgpmEventSkillMaster::CheckLearnSkill |
| `GetLearnableLevel` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIProductSkill::CBDisplayBuyPrice, AgpmEventProduct::IsValidLearnSkill, AgpmEventSkillMaster::CheckLearnSkill |
| `OnOperationGrant` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmEventBank::OnReceive, AgpmEventCook::OnReceive, AgpmEventGuild::OnReceive |
| `OnOperationBuyComposeResult` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmEventProduct::OnReceive; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuyCompose` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuyComposeResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLearnSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLearnSkillResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 19 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `MakePacketBuyComposeResult` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketLearnSkillResult` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CBEventConstructor` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBEventDestructor` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgpmEventQuest (gemeinsamer Rumpf 2, nicht im Client 1, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 19 | zugeordnet | `0x0056F730` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParseEventDataPacket` | 14 | zugeordnet | `0x0056F220` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventData` | 10 | zugeordnet | `0x0056F1E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 19 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `CBEventConstructor` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `CBEventDestructor` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |

## AgpmEventRefinery (eingebaut 1, gemeinsamer Rumpf 2, nicht im Client 5, ohne Kandidat 4, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 19 | zugeordnet | `0x0056EFB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationGrant` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventBank::OnReceive, AgpmEventCook::OnReceive, AgpmEventGuild::OnReceive; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 18 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `CBEventConstructor` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `CBEventDestructor` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `CBEventStreamWrite` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBEventStreamRead` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBEventPacketMake` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBEventPacketReceive` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketCustomEvent` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmEventRefinery::CBEventPacketMake |
| `ParsePacketCustomEvent` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventRefinery::CBEventPacketReceive; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |

## AgpmEventSiegeWarNPC (gemeinsamer Rumpf 1, nicht im Client 1, ohne Kandidat 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 20 | zugeordnet | `0x00577B50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCallbackEventGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 19 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `GetSiegeWarInfo` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::RemoveDuplicateSiegeWarObject, AgcmEventEffect::StartEventEffect, AgcmUIWorldmap::GetCastleInfomation; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |

## AgpmEventSkillMaster (Kandidat unbestätigt 7, eingebaut 11, gemeinsamer Rumpf 15, nicht im Client 15, ohne Kandidat 8, zugeordnet 47)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsUpgradable` | 5 | zugeordnet | `0x00571800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetLearnableLevel` | 2 | zugeordnet | `0x00570D50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckConditionC` | 64 | zugeordnet | `0x005726D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckConditionAB` | 35 | zugeordnet | `0x00572610` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckSkillCondition` | 12 | zugeordnet | `0x00573400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckHeroicSkillForClass` | 12 | zugeordnet | `0x00572DC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHeroicSkillVector` | 9 | zugeordnet | `0x00572A90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckConditionD` | 46 | zugeordnet | `0x00572910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharacterRaceID` | 23 | zugeordnet | `0x00570F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckHighLevelSkillForRollback` | 17 | zugeordnet | `0x00573830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CheckHeroicConditionD` | 29 | zugeordnet | `0x00572CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHeroicSkillInfo` | 38 | zugeordnet | `0x00572AD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillIndex` | 30 | zugeordnet | `0x00572500` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillInfoByIndex` | 15 | zugeordnet | `0x00572450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillInfo` | 40 | zugeordnet | `0x00572360` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHighLevelSkillVector` | 9 | zugeordnet | `0x00572320` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSkillAttachTemplateData` | 5 | zugeordnet | `0x00570DA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharTID` | 57 | zugeordnet | `0x00570C20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnHeroicSkill` | 81 | zugeordnet | `0x00572FC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnHighLevelSkill` | 86 | zugeordnet | `0x00572E10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUpgradeHeroicSkill` | 72 | zugeordnet | `0x005732A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUpgradeHighLevelSkill` | 70 | zugeordnet | `0x00573130` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnSkill` | 64 | zugeordnet | `0x00573550` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckTargetSkillForRollback` | 32 | zugeordnet | `0x00573890` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetMasteryIndex` | 10 | zugeordnet | `0x00571830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsFullUpgrade` | 11 | zugeordnet | `0x00571770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInputTotalCharismaPoint` | 23 | zugeordnet | `0x005716E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInputTotalCostHeroicPoint` | 23 | zugeordnet | `0x00571620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInputTotalCostSP` | 21 | zugeordnet | `0x00571570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUpgradeCostSP` | 17 | zugeordnet | `0x00571400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetOwnSkillCount` | 36 | zugeordnet | `0x00571F00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUpgradeSkill` | 69 | zugeordnet | `0x005736B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketBuySkill` | 26 | zugeordnet | `0x00575910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUpgradeCostCharismaPoint` | 19 | zugeordnet | `0x005714F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUpgradeCostHeroicPoint` | 19 | zugeordnet | `0x00571470` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckValidRange` | 5 | zugeordnet | `0x0055A100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTotalCharismaPointByLearnSkill` | 22 | zugeordnet | `0x00571B30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetSkillAttachCharTemplateData` | 5 | zugeordnet | `0x00571A00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InitializeSkillTree` | 96 | zugeordnet | `0x00571B90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBuyCost` | 2 | zugeordnet | `0x00571220` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParseEventDataPacket` | 17 | zugeordnet | `0x00570AC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventData` | 12 | zugeordnet | `0x00570A70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestSkillInitialize` | 16 | zugeordnet | `0x00570A20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestEvent` | 25 | zugeordnet | `0x00570990` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestUpgrade` | 28 | zugeordnet | `0x005708D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketLearnSkill` | 26 | zugeordnet | `0x0056FFB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUpgradeCost` | 30 | zugeordnet | `0x00571350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationSkillInitializeResult` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::OnReceive |
| `MakePacketResponseUpgrade` | 27 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseEvent` | 26 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketBuySkillResult` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketLearnResult` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseSkillInitialize` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckCharacterStatus` | 11 | Kandidat unbestätigt | `0x00570B20` | Aufrufer im Client: AgpmEventCharCustomize::OnOperationRequest, AgpmEventSkillMaster::OnOperationRequestEvent; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CheckBuySkillBook` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckBuySkillBook` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackBuySkillBook` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLearnSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestUpgrade` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseUpgrade` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestEvent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseEvent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuyResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSaveAllData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEndAllSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEndSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitSkillLog` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLearnResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSkillInitialize` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSkillInitializeResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetMastery` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::SetBuyMastery; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `GetSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmProductMed::CBActionSkillResult, AgcmProductMed::OnResult, AgcmSkill::ProcessReceiveCastSkill |
| `GetBuyCost` | 20 | Kandidat unbestätigt | `0x00563210` | Aufrufer im Client: AgcmUIProductSkill::CBDisplayBuyPrice, AgcmUISkill2::CBDisplaySkillPrice, AgcmUISkill2::IsActiveBuyItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetLearnCostSP` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::CheckLearnSkill, AgpmEventSkillMaster::GetInputTotalCostSP, AgpmEventSkillMaster::CheckTargetSkillForRollback |
| `GetLearnCostSP` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::CheckLearnSkill, AgpmEventSkillMaster::GetInputTotalCostSP, AgpmEventSkillMaster::CheckTargetSkillForRollback; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `GetLearnCostHeroicPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::CheckLearnHeroicSkill, AgpmEventSkillMaster::GetInputTotalCostHeroicPoint, AgpmEventSkillMaster::CheckTargetSkillForRollback |
| `GetLearnCostHeroicPoint` | 9 | Kandidat unbestätigt | `0x005712F0` | Aufrufer im Client: AgpmEventSkillMaster::CheckLearnHeroicSkill, AgpmEventSkillMaster::GetInputTotalCostHeroicPoint, AgpmEventSkillMaster::CheckTargetSkillForRollback; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetLearnCostCharismaPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::CheckLearnHeroicSkill, AgpmEventSkillMaster::CheckTargetSkillForRollback |
| `GetLearnCostCharismaPoint` | 7 | Kandidat unbestätigt | `0x005712F0` | Aufrufer im Client: AgpmEventSkillMaster::CheckLearnHeroicSkill, AgpmEventSkillMaster::CheckTargetSkillForRollback; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetLearnableLevel` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIProductSkill::CBDisplayBuyPrice, AgpmEventProduct::IsValidLearnSkill, AgpmEventProduct::GetLearnableLevel |
| `IsUpgradable` | 8 | Kandidat unbestätigt | `0x00570D70` | Aufrufer im Client: AgcmUISkill2::SetBuyMastery, AgcmUISkill2::CBDisplaySkillLevel, AgcmUISkill2::CBDisplaySkillPointHighLevel0; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `IsCurrentClassSkill` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsLimitedMaxLevel` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::CBSetConstFactor; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `CBCharTemplateConstructor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::OnAddModule |
| `CBEventDestructor` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `GetTotalLearnCost` | 32 | Kandidat unbestätigt | `0x0052CB30` | Aufrufer im Client: AgpmEventSkillMaster::InitializeSkillTree; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `GetInitializeCost` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsHighLevelSkill` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISkill2::CBSetSelfCharacter, AgcmUISkill2::CBAddSkill, AgcmUISkill2::CBRemoveSkill |
| `CheckSkillCondition` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventSkillMaster::CheckHighLevelSkillForRollback |
| `CheckHeroicSkillCondition` | 8 | Kandidat unbestätigt | `0x00573450` | Aufrufer im Client: AgcmHeroicSkill::CBHeroicSkillRollBack, AgcmHeroicSkill::CBSelectHeroicSkillGrid, AgpmEventSkillMaster::CheckTargetSkillForRollback; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `CheckHeroicSkillCondition` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmHeroicSkill::CBHeroicSkillRollBack, AgcmHeroicSkill::CBSelectHeroicSkillGrid, AgpmEventSkillMaster::CheckTargetSkillForRollback |
| `GetHeroicSkillInfoByIndex` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetHeroicSkillIndex` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmHeroicSkill::CBSelectHeroicSkillGrid, AgcmHeroicSkill::CBSelectUpgradeHeroicSkillGrid; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `IsHeroicSkill` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISkill2::CBSetSelfCharacter, AgcmUISkill2::CBAddSkill, AgcmUISkill2::CBRemoveSkill |
| `_CheckHeroicConditionA` | 36 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::CheckHeroicSkillCondition; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `StreamReadMasteryTxt` | 133 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadMasteryEvolution` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadDefaultSkill` | 65 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadHighLevelSkill` | 135 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadHeroicSkill` | 112 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadArchlordSkill` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::StreamReadMasteryTxt; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |
| `StreamReadRaceSkill` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::StreamReadMasteryTxt; kein unbenannter Kandidat mit Beleg unter 586 unbenannten Funktionen im Klassenbereich |

## AgpmEventTeleport (Kandidat unbestätigt 2, eingebaut 12, gemeinsamer Rumpf 14, nicht im Client 12, ohne Kandidat 10, zugeordnet 14)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetTargetPointList` | 24 | zugeordnet | `0x0055A490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSequenceTargetGroup` | 13 | zugeordnet | `0x0055A450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadFee` | 44 | zugeordnet | `0x0054CD00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsArchlordDungeonPoint` | 43 | zugeordnet | `0x0055A210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsDisablePoint` | 29 | zugeordnet | `0x0055B230` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendTeleportStart` | 20 | zugeordnet | `0x00559F10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTargetPoint` | 65 | zugeordnet | `0x0055B070` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveFee` | 17 | zugeordnet | `0x00559A90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRequestTeleportGranted` | 69 | zugeordnet | `0x0055B320` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetFee` | 24 | zugeordnet | `0x0055A170` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTeleportLoading` | 24 | zugeordnet | `0x0055A040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRequestTeleport` | 26 | zugeordnet | `0x00559F90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTeleportReturn` | 30 | zugeordnet | `0x00559DF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTeleportInfo` | 22 | zugeordnet | `0x00559D50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxTeleportPoint` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxTeleportGroup` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateTeleportPoint` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::AddTeleportPoint; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `DestroyTeleportPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventTeleport::AddTeleportPoint, AgpmEventTeleport::RemoveTeleportPoint |
| `CreateTeleportGroup` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmEventTeleport::AddTeleportGroup |
| `DestroyTeleportGroup` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventTeleport::OnDestroy, AgpmEventTeleport::AddTeleportGroup, AgpmEventTeleport::RemoveTeleportGroup |
| `AddTeleportPoint` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::StreamReadPoint; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `RemoveTeleportPoint` | 22 | Kandidat unbestätigt | `0x0055A9C0` | Aufrufer im Client: AgpmEventTeleport::OnDestroy, AgpmEventTeleport::CBEventDestructor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetTeleportPoint` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmEventTeleport::OnReceive, AgpmEventTeleport::CBStreamReadEvent |
| `ChangeTeleportPointName` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSequencePoint` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmEventTeleport::RemoveTeleportGroup |
| `GetSequencePointInGroup` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::RemoveTeleportGroup, AgpmEventTeleport::DeleteAllPointInGroup, AgpmEventTeleport::GetTargetPointList; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `AddTeleportGroup` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::StreamReadGroup; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `RemoveTeleportGroup` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetTeleportGroup` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmEventTeleport::PointReadCB |
| `GetTeleportGroup` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmEventTeleport::PointReadCB |
| `ChangeTeleportGroupName` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSequenceGroup` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSequenceGroupInPoint` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::RemoveTeleportPoint, AgpmEventTeleport::DeleteAllGroupInPoint, AgpmEventTeleport::CheckValidTeleport; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `DeleteAllGroupInPoint` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteAllPointInGroup` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckValidTeleport` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::OnReceive; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `CheckBaseStatus` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::OnReceive, AgpmEventTeleport::CBActionEventTeleport; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `Teleport` | 55 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventTeleport::AddFunctions, AgpmCharacter::ActionCharacter, AgpmEventTeleport::OnReceive; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `AddPointToGroup` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::PointReadCB; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `AddTargetGroupToPoint` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmEventTeleport::PointReadCB |
| `RemovePointNGroup` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::RemoveTeleportPoint, AgpmEventTeleport::RemoveTeleportGroup, AgpmEventTeleport::DeleteAllGroupInPoint; kein unbenannter Kandidat mit Beleg unter 159 unbenannten Funktionen im Klassenbereich |
| `RemoveTargetGroupFromPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventTeleport::RemoveTeleportGroup, AgpmEventTeleport::DeleteAllGroupInPoint |
| `SetCallbackTeleport` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCalcPos` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceivedRequestResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceivedTeleportStart` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceivedTeleportCanceled` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckUsableTeleport` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReturnTown` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTeleportLoading` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSyncTeleportLoading` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTeleportLog` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleGroundTeleportLog` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackArchlordMessageId` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetBattleGroundState` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetTeleportBlock` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SendTeleportCanceled` | 20 | Kandidat unbestätigt | `0x00559E90` | Aufrufer im Client: AgpmEventTeleport::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CheckValidRange` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmArchlord::OnOperationEventRequest, AgpmAuction::OnReceive, AgpmEventBank::OnOperationRequest |
| `DesAgpdTeleportAttachToChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventTeleport::OnAddModule |
| `GetADCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo, AgcmCashMall::SendPacketRefreshCash, AgcmCharacter::UpdateTransparent |
| `DungeonTeleportDisable` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ActiveTeleportCastleToDungeon` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWriteGroup` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWritePoint` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmGuild (Kandidat unbestätigt 18, eingebaut 32, gemeinsamer Rumpf 70, nicht im Client 40, ohne Kandidat 33, zugeordnet 41)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetJointGuildMarkID` | 5 | zugeordnet | `0x00550170` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsDuplicatedCharacterOfMigration` | 13 | zugeordnet | `0x0054FAB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCurrentBattleInfo` | 9 | zugeordnet | `0x0054E050` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCharAD` | 30 | zugeordnet | `0x0054DE90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateGuildMember` | 15 | zugeordnet | `0x0054DCA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsBattleStatus` | 5 | zugeordnet | `0x005517D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetRequireIncreaseMaxMember` | 7 | zugeordnet | `0x0054F7E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReReadGuildMarkTemplate` | 63 | zugeordnet | `0x0054CD7E` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyGuildMarkTemplate` | 16 | zugeordnet | `0x0054FCA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateGuildMarkTemplate` | 13 | zugeordnet | `0x0054FCF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateMemberStatus` | 38 | zugeordnet | `0x00552110` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ForcedLeaveMember` | 48 | zugeordnet | `0x00551F90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LeaveMember` | 45 | zugeordnet | `0x00551E40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyGuild` | 9 | zugeordnet | `0x00553090` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateGuild` | 67 | zugeordnet | `0x00553760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveMember` | 5 | zugeordnet | `0x0054DE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `JoinMember` | 39 | zugeordnet | `0x0054DD10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildListRequestPacket` | 36 | zugeordnet | `0x0054F660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileLeavePacket` | 16 | zugeordnet | `0x0054F3E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileLeaveRequestPacket` | 16 | zugeordnet | `0x0054F310` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostilePacket` | 17 | zugeordnet | `0x0054F230` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileRejectPacket` | 16 | zugeordnet | `0x0054F160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildHostileRequestPacket` | 17 | zugeordnet | `0x0054F090` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointLeavePacket` | 16 | zugeordnet | `0x0054EFD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointPacket` | 17 | zugeordnet | `0x0054EEF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointRejectPacket` | 16 | zugeordnet | `0x0054EE20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJointRequestPacket` | 17 | zugeordnet | `0x0054ED50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildBattlePersonPacket` | 13 | zugeordnet | `0x0054E970` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildForcedLeavePacket` | 19 | zugeordnet | `0x0054E680` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildLeavePacket` | 19 | zugeordnet | `0x0054E5D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJoinPacket` | 19 | zugeordnet | `0x0054E460` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJoinRejectPacket` | 19 | zugeordnet | `0x0054E3B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildJoinRequestPacket` | 19 | zugeordnet | `0x0054E300` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMaster` | 13 | zugeordnet | `0x0054DA30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DeleteAllGuildMark` | 18 | zugeordnet | `0x0054FE50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RenameCharID` | 40 | zugeordnet | `0x0054FB30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeGuildMemberPacket` | 18 | zugeordnet | `0x0054E520` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetOnlineMemberCount` | 23 | zugeordnet | `0x0054DAF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMemberCount` | 23 | zugeordnet | `0x0054DA70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetMember` | 9 | zugeordnet | `0x0054DA00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 4 | zugeordnet | `0x0054D230` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxGuild` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DesAgpdGuildADChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmGuild::OnAddModule |
| `AttachGuildData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmGuildWarehouse::OnAddModule, AgpmSiegeWar::OnAddModule |
| `AttachMemberData` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AttachGuildMarkTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmGuild::OnAddModule |
| `OnOperationCreateCheck` | 45 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnOperationUpdateMaxMemberCount` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnReceive; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `AddGuild` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmGuild::CreateGuild, AgpmGuild::DestroyGuild, AgpmGuild::RenameGuildID |
| `RemoveGuild` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmGuild::DestroyGuild, AgpmGuild::DestroyGuildFromRemoveAdmin, AgpmGuild::RenameGuildID |
| `GetGuild` | 9 | Kandidat unbestätigt | `0x00552280` | Aufrufer im Client: AgcmGuild::IsGuildBattle, AgcmGuild::IsGuildBattleMember, AgcmUIWorldmap::GetCastleOwnerGuild; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuild` | 9 | Kandidat unbestätigt | `0x00552280` | Aufrufer im Client: AgcmGuild::IsGuildBattle, AgcmGuild::IsGuildBattleMember, AgcmUIWorldmap::GetCastleOwnerGuild; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuildLock` | 18 | Kandidat unbestätigt | `0x00551550` | Aufrufer im Client: AgcmGuild::GetSelfGuildLock, AgcmTextBoardMng::GetGuildIDColor, AgcmUIGuild::CBJoin; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuildLock` | 15 | Kandidat unbestätigt | `0x00551550` | Aufrufer im Client: AgcmGuild::GetSelfGuildLock, AgcmTextBoardMng::GetGuildIDColor, AgcmUIGuild::CBJoin; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuildLock` | 9 | Kandidat unbestätigt | `0x00551550` | Aufrufer im Client: AgcmGuild::GetSelfGuildLock, AgcmTextBoardMng::GetGuildIDColor, AgcmUIGuild::CBJoin; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuildCount` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetGuildSequence` | 9 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `CheckCreateGuildEnable` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnOperationCreate; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `DestroyGuild` | 68 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnDestroy, AgpmGuild::OnOperationDestroy, AgpmGuild::CreateGuild; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `DestroyGuildFromRemoveAdmin` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnIdle2, AgpmGuild::OnDestroy; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetAllMemberCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuild::CBMainToggle, AgcmUIGuild::RefreshMemberPageUI, AgpmSiegeWar::CheckGuildRequirement |
| `SetMaster` | 37 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsMaster` | 13 | Kandidat unbestätigt | `0x00552280` | Aufrufer im Client: AgcmGuild::SendNotice, AgcmGuild::SendBattlePerson, AgcmGuild::SendBattleRequest; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsMaster` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmGuild::SendNotice, AgcmGuild::SendBattlePerson, AgcmGuild::SendBattleRequest |
| `IsSubMaster` | 11 | Kandidat unbestätigt | `0x005515A0` | Aufrufer im Client: AgcmGuild::SendJoinAllow, AgcmUIGuild::CBIsActiveGuildInviteMemu, AgcmUIGuild::CBLeave; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsSubMaster` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmGuild::SendJoinAllow, AgcmUIGuild::CBIsActiveGuildInviteMemu, AgcmUIGuild::CBLeave |
| `IsExceptionCharacterOfGuildRankSystem` | 23 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetMemberLevelSum` | 22 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::GetMinimumWinPoint; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `AddMember` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmGuild::JoinMember, AgpmGuild::RenameCharID, AgpmParty::AddMember |
| `JoinMember` | 27 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnOperationJoin, AgpmGuild::UpdateMemberStatus; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `CheckJoinEnable` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnOperationJoin; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `UpdateMemberStatus` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnOperationCharacterGuildData; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetMemberCIDList` | 12 | nicht im Client |  | Aufrufer nur im Server (11); kein Treffer im Binary |
| `GetMemberCIDList` | 17 | nicht im Client |  | Aufrufer nur im Server (11); kein Treffer im Binary |
| `GetMemberCIDList` | 23 | nicht im Client |  | Aufrufer nur im Server (11); kein Treffer im Binary |
| `IsAnyGuildMember` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBDisplaySlotCharGuild; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetJoinedGuildID` | 9 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AgcmGuild::IsGuildBattle, AgcmGuild::IsGuildBattleMember, AcUIRaider::_CharacterType; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `FindCharGuildID` | 65 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindGuildLockFromCharID` | 46 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `IsBattleDeclareStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmGuild::IsBattleStatus |
| `IsBattleReadyStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuild::OpenBattleCancelRequestConfirmUI, AgcmUIGuild::OpenBattleCancelAcceptConfirmUI, AgcmUIGuild::DrawBattleInfoTime |
| `IsBattleIngStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmGuild::IsGuildBattle, AgcmGuild::IsGuildBattleMember, AgcmUIGuild::DrawBattleInfoTime |
| `CheckBattleType` | 15 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEnemyGuild` | 15 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AgcmTextBoardMng::ChangeGuildIDColor, AgcmTextBoardMng::CB_PvPRefreshGuild, AgcmUIGuild::CBReceiveBattleCancelRequest; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEnemyGuild` | 10 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AgcmTextBoardMng::ChangeGuildIDColor, AgcmTextBoardMng::CB_PvPRefreshGuild, AgcmUIGuild::CBReceiveBattleCancelRequest; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetMinimumWinPoint` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetBattlePoint` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::GetMinimumWinPoint; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `SetMaxBattlePointAdmin` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadBattlePointTxt` | 55 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddJointGuild` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBJoint; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `IsJointGuild` | 12 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild, AgcmTextBoardMng::GetGuildIDColor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsJointGuild` | 8 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild, AgcmTextBoardMng::GetGuildIDColor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsJointLeader` | 17 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `RemoveJointGuild` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBJointLeave; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `ClearJointGuild` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIGuild::CBJointLeave |
| `GetJointGuild` | 11 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetJointGuildCount` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuild::CBOnJointRequestBtnClick |
| `AddHostileGuild` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBHostile; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `IsHostileGuild` | 12 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AcUIRaider::_CharacterType, AgcmTextBoardMng::GetTargetIDColor, AgcmTextBoardMng::ChangeGuildIDColor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsHostileGuild` | 8 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AcUIRaider::_CharacterType, AgcmTextBoardMng::GetTargetIDColor, AgcmTextBoardMng::ChangeGuildIDColor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsHostileGuild` | 10 | Kandidat unbestätigt | `0x005526C0` | Aufrufer im Client: AcUIRaider::_CharacterType, AgcmTextBoardMng::GetTargetIDColor, AgcmTextBoardMng::ChangeGuildIDColor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveHostileGuild` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBHostileLeave; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetHostileGuild` | 11 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetHostileGuildCount` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetLastRelationWaitGuildID` | 5 | nicht im Client |  | Aufrufer nur im Server (9); kein Treffer im Binary |
| `GetLastRelationWaitGuildID` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsLastRelationWaitGuildID` | 5 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetCurrentTimeStamp` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmTitle::_CheckTitleExchangeTimeLimit, AgcmUIGuild::CBJoin, AgcmUIGuild::CBReceiveLeaveRequestSelf |
| `GetCurrentTimeDate` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `WriteGuildLog` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnOperationCreate, AgpmGuild::OnOperationCreateCheck; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `IsSameGuild` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::IsAttackable; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildPacket` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::MakeGuildCreatePacket, AgpmGuild::MakeGuildJoinRequestPacket, AgpmGuild::MakeGuildJoinRejectPacket; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildCreatePacket` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendCreateGuild; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildLeaveAllowPacket` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeGuildDestroyPacket` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendDestroy; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildUpdateMaxMemberCountPacket` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendMaxMemberCount; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildCharDataPacket` | 19 | nicht im Client |  | Aufrufer nur im Server (7); kein Treffer im Binary |
| `MakeGuildUpdateNoticePacket` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendNotice; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildSystemMessagePacket` | 7 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakeGuildBattlePacket` | 43 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::MakeGuildBattleRequestPacket, AgpmGuild::MakeGuildBattleAcceptPacket, AgpmGuild::MakeGuildBattleRejectPacket; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildBattleRequestPacket` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleRequest |
| `MakeGuildBattleAcceptPacket` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleAccept |
| `MakeGuildBattleRejectPacket` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleReject |
| `MakeGuildBattleCancelPacket` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmGuild::MakeGuildBattleCancelReqeustPacket, AgpmGuild::MakeGuildBattleCancelAcceptPacket, AgpmGuild::MakeGuildBattleCancelRejectPacket |
| `MakeGuildBattleCancelReqeustPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleCancelRequest |
| `MakeGuildBattleCancelAcceptPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleCancelAccept |
| `MakeGuildBattleCancelRejectPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleCancelReject |
| `MakeGuildBattleStartPacket` | 4 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeGuildBattleUpdateTimePacket` | 4 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeGuildBattleUpdateScorePacket` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeGuildBattleWithdrawPacket` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmGuild::SendBattleWithdraw |
| `MakeGuildBattleMemberPacket` | 15 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeGuildBattleMemberListPacket` | 43 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeGuildBuyGuildMarkPacket` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendGuildBuyGuildMark; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildBuyGuildMarkForcePacket` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendGuildBuyGuildMark; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildHostileLeaveRejectPacket` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackGuildCreate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildCreateCheck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildCreateEnableCheck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildCreateFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildJoinRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildJoinEnableCheck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildJoinFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildJoinReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildJoin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildLeave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildLeaveFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildForcedLeave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildForcedLeaveFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildDestroyPreProcess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildDestroy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildDestroyFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildCheckDestroy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildUpdateMaxMemberCount` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckPassword` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCharData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMemberStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateNotice` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSystemMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateRecord` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattlePerson` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleAccept` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleCancelRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleCancelAccept` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleCancelReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleStart` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleUpdateTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleUpdateScore` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleWithdraw` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleMember` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleMemberList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBattleRound` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRenameGuildID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRenameCharID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildMarkTemplateLoad` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuyGuildMark` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBuyGuildMarkForce` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetGuildMarkTexture` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetGuildMarkSmallTexture` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackJointRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackJointReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackJoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackJointLeave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostileRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostileReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostile` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostileLeaveRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostileLeaveReject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostileLeave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackJointDetail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackHostileDetail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetJointMark` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetJointColor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildAppointmentAsk` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildSuccessionAsk` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildAppointmentSysMsg` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGuildMemberRankUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `PrintGuildInfo` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeGuildListPacket` | 94 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `MakeGuildListPacket` | 7 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `MakeGuildListPacket` | 22 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `SetCallbackReceiveGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveLeaveRequestSelf` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveJoinRequestSelf` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakeGuildListRequestFindPacket` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendGuildListRequestFind; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildRenameGuildIDPacket` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::SendGuildRenameGuildID; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `MakeGuildRenameCharacterIDPacket` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackDestroyGuildCheckTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `RenameGuildID` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::RenameGuild; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `AddGuildMarkTemplate` | 36 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::ReadGuildMarkTemplate; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetGuildMarkTemplate` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawFlag, AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild |
| `GetGuildMarkTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawFlag, AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild |
| `GetGuildMarkTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawFlag, AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild |
| `GetMaxGuildMarkGridItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuild::InitGuildMarkGridItem |
| `GetMaxGuildMarkColorGridItem` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetGuildMarkID` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBGuildMarkGridLClickDown; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetGuildMarkID` | 9 | Kandidat unbestätigt | `0x0054FF70` | Aufrufer im Client: AgcmUIGuild::CBGuildGuildMarkUIInit, AgcmUIGuild::CBGuildMarkGridLClickDown, AgcmUIGuild::CBGuildGuildMarkClickBuy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuildMarkID` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuild::CBGuildGuildMarkUIInit, AgcmUIGuild::CBGuildMarkGridLClickDown, AgcmUIGuild::CBGuildGuildMarkClickBuy |
| `SetGuildMarkColor` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBGuildMarkColorGridLClickDown; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetGuildMarkColorID` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::InitSeletedGridItem, AgpmGuild::GetGuildMarkColor; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `GetGuildMarkColor` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild, AgcmUIGuild::CBGuildGuildMarkUIInit |
| `GetGuildMarkColor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild, AgcmUIGuild::CBGuildGuildMarkUIInit |
| `GetGuildMarkColor` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild, AgcmUIGuild::CBGuildGuildMarkUIInit |
| `GetJointGuildMarkColor` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild |
| `GetGuildMarkTexture` | 9 | Kandidat unbestätigt | `0x00551CA0` | Aufrufer im Client: AgcmUIWorldmap::GetCastleOwnerGuildMarkBG, AgcmUIWorldmap::GetCastleOwnerGuildMarkPattern, AgcmUIWorldmap::GetCastleOwnerGuildMarkSimbol; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGuildMarkTexture` | 9 | Kandidat unbestätigt | `0x00551CA0` | Aufrufer im Client: AgcmUIWorldmap::GetCastleOwnerGuildMarkBG, AgcmUIWorldmap::GetCastleOwnerGuildMarkPattern, AgcmUIWorldmap::GetCastleOwnerGuildMarkSimbol; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEnableBuyGuildMark` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::SetPreviewGuildMark; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |
| `IsDuplicateGuildMark` | 24 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OnOperationClassSocietySystem` | 42 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::OnReceive; kein unbenannter Kandidat mit Beleg unter 88 unbenannten Funktionen im Klassenbereich |

## AgpmGuildWarehouse (eingebaut 9, gemeinsamer Rumpf 11, ohne Kandidat 6, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CheckPreviledge` | 21 | zugeordnet | `0x005770D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItem` | 44 | zugeordnet | `0x00577550` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItem` | 49 | zugeordnet | `0x005773F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetGuildWarehouse` | 5 | zugeordnet | `0x00576EF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetGuildWarehouse` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::SetGrid, AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBAddItemToGuildWarehouse |
| `GetGuildWarehouse` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildWarehouse::SetGrid, AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBAddItemToGuildWarehouse; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `AddItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmItem::_GetDragonScionItemAgcdItem, AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBAddConvertGridItem |
| `AddItem` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::_GetDragonScionItemAgcdItem, AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBAddConvertGridItem; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `AddItem` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::_GetDragonScionItemAgcdItem, AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBAddConvertGridItem; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `RemoveItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBRemoveItem, AgcmUIEventItemRepair::CBMoveEndItem |
| `AddMoney` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::AddMoney, AgpmCharacter::OnOperationMoveBankMoney, AgpmEventSkillMaster::InitializeSkillTree; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `AddMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::AddMoney, AgpmCharacter::OnOperationMoveBankMoney, AgpmEventSkillMaster::InitializeSkillTree |
| `AddMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::AddMoney, AgpmCharacter::OnOperationMoveBankMoney, AgpmEventSkillMaster::InitializeSkillTree |
| `SubMoney` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUIRefinery::CBRefine, AgpmCharacter::SubMoney, AgpmCharacter::OnOperationMoveBankMoney; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SubMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIRefinery::CBRefine, AgpmCharacter::SubMoney, AgpmCharacter::OnOperationMoveBankMoney |
| `SubMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIRefinery::CBRefine, AgpmCharacter::SubMoney, AgpmCharacter::OnOperationMoveBankMoney |
| `ClearAllItems` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildWarehouse::CBGrant; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `ClearAllItems` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::CBGrant |
| `CheckPreviledge` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::CBIsActiveMoneyInButton, AgcmUIGuildWarehouse::CBIsActiveMoneyOutButton |
| `SetCallbackBaseInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOpen` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackClose` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoneyIn` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoneyOut` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemIn` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemOut` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackExpand` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmItem (Kandidat unbestätigt 52, eingebaut 45, gemeinsamer Rumpf 98, nicht im Client 112, ohne Kandidat 95, zugeordnet 100)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `StreamReadTransformData` | 101 | zugeordnet | `0x005454C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetItemDurabilityPercent` | 24 | zugeordnet | `0x0053B730` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitTradeBlockItems` | 78 | zugeordnet | `0x005429B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetEquipWeapon` | 30 | zugeordnet | `0x0058F3E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ChangeItemOwner` | 2 | zugeordnet | `0x0053F4A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitItem` | 12 | zugeordnet | `0x0053A3E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInventory` | 18 | zugeordnet | `0x0053D400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckBuyBankSlotCost` | 15 | zugeordnet | `0x0058E8C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsBuyBankSlot` | 8 | zugeordnet | `0x0058E620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUsableType` | 4 | zugeordnet | `0x0058D210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalBoltCountInInventory` | 11 | zugeordnet | `0x0053E460` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalArrowCountInInventory` | 11 | zugeordnet | `0x0053E410` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAvatarItem` | 17 | zugeordnet | `0x0053CC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsUsingStamina` | 8 | zugeordnet | `0x0053C330` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsQuestItem` | 5 | zugeordnet | `0x0053BBD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetBoundType` | 12 | zugeordnet | `0x0053BAC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ResetTradeStats` | 9 | zugeordnet | `0x0058FC70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInventoryItemByTID` | 29 | zugeordnet | `0x0058C6A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemOption` | 5 | zugeordnet | `0x00596870` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AutoInsertStackMerge` | 89 | zugeordnet | `0x00596F90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemFromField` | 13 | zugeordnet | `0x0058FE70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsEquipWeapon` | 19 | zugeordnet | `0x0058FA60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EquipItem` | 5 | zugeordnet | `0x0058EC00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadItemTemplateEntryINI` | 50 | zugeordnet | `0x0054A6D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadImportData` | 1694 | zugeordnet | `0x00545820` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadOneTemplate` | 61 | zugeordnet | `0x0054ABA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseQuestPacket` | 13 | zugeordnet | `0x0058E9A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseInventoryPacket` | 13 | zugeordnet | `0x0058C760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetShrineCoinPrice` | 6 | zugeordnet | `0x0053B570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharismaPrice` | 6 | zugeordnet | `0x0053B540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetItemPrice` | 16 | zugeordnet | `0x0053B390` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetPCPrice` | 13 | zugeordnet | `0x0053E4B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetBuyBankSlotCost` | 22 | zugeordnet | `0x0058E650` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToBank` | 2 | zugeordnet | `0x0058C4A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemFromInventory` | 16 | zugeordnet | `0x0058C600` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToChargingInventory` | 2 | zugeordnet | `0x0058E0B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToInventory` | 2 | zugeordnet | `0x0058C880` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SplitItem_field` | 0 | zugeordnet | `0x0053FA20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SplitItem` | 101 | zugeordnet | `0x0053F750` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessRemove` | 26 | zugeordnet | `0x0053B960` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUseItem` | 89 | zugeordnet | `0x0053E4F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketItemInforMation` | 33 | zugeordnet | `0x0053AC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItem` | 59 | zugeordnet | `0x0053D440` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyTemplate` | 37 | zugeordnet | `0x005628E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateTemplate` | 51 | zugeordnet | `0x00542CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateItem` | 65 | zugeordnet | `0x0053D180` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToChargingInventoryResult` | 54 | zugeordnet | `0x0058DEA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsEnableEquipItemInMyRegion` | 17 | zugeordnet | `0x0053CCC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddRemoveItem` | 12 | zugeordnet | `0x0053B9F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBoltItemFromInventory` | 29 | zugeordnet | `0x0053B8D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetArrowItemFromInventory` | 29 | zugeordnet | `0x0053B840` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashItemByTID` | 6 | zugeordnet | `0x0058D0D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetEquipSlotItem` | 15 | zugeordnet | `0x0058FAC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `EquipItem` | 5 | zugeordnet | `0x0058E430` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToClientTradeGrid` | 2 | zugeordnet | `0x0058E160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemFromCashInventory` | 12 | zugeordnet | `0x0058D7A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharShrineCoinCount` | 33 | zugeordnet | `0x0053CF40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemStackCount` | 39 | zugeordnet | `0x0053B670` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetItemStackCount` | 39 | zugeordnet | `0x0053B5A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetItemPrice` | 14 | zugeordnet | `0x0053B340` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketChangeAutoPickItem` | 40 | zugeordnet | `0x0053B040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestBuyBankSlot` | 34 | zugeordnet | `0x0053AF60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestDestroyItem` | 35 | zugeordnet | `0x0053AEE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketDropMoneyToField` | 35 | zugeordnet | `0x0053AD70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToSalesBox` | 2 | zugeordnet | `0x0058FB80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToChargingInventory` | 2 | zugeordnet | `0x0058DB30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInBank` | 2 | zugeordnet | `0x0058CB90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToBank` | 2 | zugeordnet | `0x0058C9B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InsertStackMerge` | 51 | zugeordnet | `0x00596D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Insert` | 39 | zugeordnet | `0x00596C10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetEquipItem` | 15 | zugeordnet | `0x0058EB10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInChargingInventory` | 2 | zugeordnet | `0x0058E250` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToChargingInventory` | 2 | zugeordnet | `0x0058DBD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamReadAvatarSet` | 64 | zugeordnet | `0x00544610` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckUpdateStatus` | 40 | zugeordnet | `0x0053EE10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GefEffectedSkillPlusLevel` | 40 | zugeordnet | `0x0053EC90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToTradeGrid` | 2 | zugeordnet | `0x0058FCB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToSalesBox` | 2 | zugeordnet | `0x0058E9F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInInventory` | 2 | zugeordnet | `0x0058E6E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemFromClientTradeGrid` | 16 | zugeordnet | `0x0058E000` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetChargingInvectoryColumn` | 26 | zugeordnet | `0x0058DB00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetChargingInvectoryRow` | 26 | zugeordnet | `0x0058DAC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetChargingInvectoryLayer` | 26 | zugeordnet | `0x0058DA90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemFromChargingInventory` | 2 | zugeordnet | `0x0058D9E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUsingCashPetItemInvolveSubInventory` | 33 | zugeordnet | `0x0058D320` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUsingCashItemBySkillTID` | 25 | zugeordnet | `0x0058D250` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashItemUsableByType` | 23 | zugeordnet | `0x0058D160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AutoInsert` | 23 | zugeordnet | `0x00596EB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParseFieldPacket` | 15 | zugeordnet | `0x0058FEE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToField` | 22 | zugeordnet | `0x0058FDD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInChargingInventory` | 2 | zugeordnet | `0x0058DCC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashInventoryItemByTID` | 29 | zugeordnet | `0x0058D570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetExistReverseOrb` | 165 | zugeordnet | `0x0053C6A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetExistCatalyst` | 100 | zugeordnet | `0x0053C360` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketItemUse` | 33 | zugeordnet | `0x0053ACF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetItemSequence` | 9 | zugeordnet | `0x0053A510` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacterTemplate` | 5 | zugeordnet | `0x0053A4B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 5 | zugeordnet | `0x0053A480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateOptionTemplate` | 14 | zugeordnet | `0x0053A190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DestroyItem` | 26 | zugeordnet | `0x0053A100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsTradeBlockItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::CBPrivateTradeMoveItem |
| `GetTemplateDataSize` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AgpmItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `OnValid` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetEquipIndexFromTable` | 7 | Kandidat unbestätigt | `0x0058EB80` | Aufrufer im Client: AgpmItem::CharacterForAllItems, AgpmItem::GetEquipItem, AgpmItem::EquipItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CreateCopyItem` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyAllTemplate` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadItemTemplate, AgcmExportResource::ReadObjectTemplate, AgcmObject::ReloadObjectClump; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `DestroyOptionTemplate` | 13 | Kandidat unbestätigt | `0x00541580` | Aufrufer im Client: AgpmItem::OnDestroy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `GetInventory` | 14 | Kandidat unbestätigt | `0x005403E0` | Aufrufer im Client: AgpmEventCharCustomize::GetItemCount, AgpmEventCharCustomize::UsingCustomizingItem, AgpmEventTeleport::IsArchlordDungeonPoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetEquipGrid` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetEquipGrid` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetBank` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToBank, AgpmItem::LockGrid, AgpmItem::ReleaseGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetBank` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToBank, AgpmItem::LockGrid, AgpmItem::ReleaseGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetTradeGrid` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::LockGrid, AgpmItem::ReleaseGrid, AgpmItem::AddItemToTradeGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetTradeGrid` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::LockGrid, AgpmItem::ReleaseGrid, AgpmItem::AddItemToTradeGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetClientTradeGrid` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToClientTradeGrid, AgpmItem::LockGrid, AgpmItem::ReleaseGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetClientTradeGrid` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToClientTradeGrid, AgpmItem::LockGrid, AgpmItem::ReleaseGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetSalesBox` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::LockGrid, AgpmItem::ReleaseGrid, AgpmItem::AddItemToSalesBox; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetSalesBox` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::LockGrid, AgpmItem::ReleaseGrid, AgpmItem::AddItemToSalesBox; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetQuestGrid` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetQuestGrid` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCashInventoryGrid` | 9 | Kandidat unbestätigt | `0x005403E0` | Aufrufer im Client: AgcmUICashMall::CBBuyProductConfirm, AgcmUICashMall::CBBuyProduct, AgpmEventCharCustomize::GetItemCount; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetCashInventoryGrid` | 14 | Kandidat unbestätigt | `0x005403E0` | Aufrufer im Client: AgcmUICashMall::CBBuyProductConfirm, AgcmUICashMall::CBBuyProduct, AgpmEventCharCustomize::GetItemCount; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DesAgpdItemADCharTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnAddModule |
| `SetCallbackInit` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNewItemToClient` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDelete` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTradeGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTargetTradeGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeItemOwner` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseItemByTID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseItemFailedByTID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseItemSuccess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateReturnTeleportStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseReturnScroll` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseReturnScrollResultFailed` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckPickupItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPickupItemMoney` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPickupItemResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIconSlotInput` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateEquip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateTrade` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateTradeClient` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateSubInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateChargingInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateTradeOption` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUIUpdateSalesBox` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateStackCount` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateRequireLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveItemData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReadTemplate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStreamReadImportDataErrorReport` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStreamReadOptionTable` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveInventoryGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSalesBoxRemoveUIUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDropMoneyToField` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemToMap` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItemFromMap` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestSpiritStoneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemToBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItemFromBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemToGuildWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItemFromGuildWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSplitItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckJoinItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateReuseTimeForReverseOrb` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateReuseTimeForTransform` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitReuseTimeForTransform` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateItemStatusFlag` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStreamReadImportData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInventoryQuestAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInventoryQuestUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInventoryQuestRemove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnuseItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseItemResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveGuildWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemOption` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCooldown` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeAutoPickUp` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemExtraData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemInformation` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddGachaItemUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemInformationResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `AddItem` | 10 | Kandidat unbestätigt | `0x005873E0` | Aufrufer im Client: AgcmItem::_GetDragonScionItemAgcdItem, AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBAddConvertGridItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveItem` | 7 | Kandidat unbestätigt | `0x0053D510` | Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBRemoveItem, AgcmUIEventItemRepair::CBMoveEndItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `RemoveAllItems` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnChagneEquipItemByEvolution, AgcmCharacter::OnEquipCharonForSummoner, AgcmCharacter::AttachRideClump |
| `GetItem` | 8 | Kandidat unbestätigt | `0x0053BA30` | Aufrufer im Client: AgcmCharacter::OnChagneEquipItemByEvolution, AgcmCharacter::OnEquipCharonForSummoner, AgcmCharacter::AttachRideClump; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetItemLock` | 9 | Kandidat unbestätigt | `0x0053F550` | Aufrufer im Client: AgpmItem::OnOperationPickupItem, AgpmItem::CBPickupItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetItemLock` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmItem::OnOperationPickupItem, AgpmItem::CBPickupItem |
| `GetItemTemplate` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmAIUseItemEdit::OnInitDialog, AgcmAIUseItemEdit::OnAiUseItemAddButton, AgcmCashMall::CreateDummyItem |
| `GetItemTemplate` | 13 | Kandidat unbestätigt | `0x0058EB80` | Aufrufer im Client: AgcmAIUseItemEdit::OnInitDialog, AgcmAIUseItemEdit::OnAiUseItemAddButton, AgcmCashMall::CreateDummyItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetItemTemplateUseIID` | 12 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetMaxItem` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxItemRemove` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachItemData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::OnAddModule, AgcmItem::OnAddModule, AgcmUIItem::OnAddModule |
| `AttachItemTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::OnAddModule, SequenceNumberManager::AttachTemplateSequenceData, AgcmGeometryDataManager::OnAddModule |
| `GetItemOptionTemplate` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: CUiCharacterProperty::_GetItemOptionValuePoint, CUiCharacterProperty::_GetItemOptionValueSkill, AgcmUIItem::SetItemToolTipConvertAttrInfo |
| `CBRemoveChar` | 180 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnAddModule, AgpmItem::OnAddModule, AgpmParty::OnAddModule; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `ProcessRefreshUI` | 118 | Kandidat unbestätigt | `0x0053A530` | Aufrufer im Client: AgcmItem::ReceiveUnuseItem, AgcmItem::ReceiveUseItem, AgcmItem::ReceivePauseItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ProcessRefreshCount` | 12 | Kandidat unbestätigt | `0x0053E0E0` | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::OnOperationRemove, AgpmItem::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ProcessRefreshCount` | 40 | Kandidat unbestätigt | `0x0053A530` | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::OnOperationRemove, AgpmItem::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `OnOperationUpdate` | 642 | Kandidat unbestätigt | `0x0058FB20` | Aufrufer im Client: AgpmCharacter::OnReceive, AgpmCharacter::OnOperationAdd, AgpmCharacter::OnOperationUpdate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `OnOperationDropMoney` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsProgressingCooldown` | 10 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `ProcessAllItemCooldown` | 65 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCooldownByTID` | 39 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdateCooldown; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetCooldownPause` | 19 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetRemainTimeByTID` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetCooldownPause` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdateCooldown; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetCooldownBase` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CheckReUseInterval; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `CallCooldownCallback` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::ProcessAllItemCooldown, AgpmItem::OnOperationUpdateCooldown; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `MakePacketItem` | 155 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::AddItemPacketToBuffer; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `MakePacketItemInforMationResult` | 156 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemInforMationResult` | 50 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemView` | 246 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `MakePacketItemPickup` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketItemPickupResult` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSplitItem` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::SendSplitItem, AgcmItem::SendSplitItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `MakePacketSplitItem` | 44 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::SendSplitItem, AgcmItem::SendSplitItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `MakePacketUpdateReuseTimeForReverseOrb` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketUpdateReuseTimeForTransform` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketInitReuseTimeForTransform` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemUnuse` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::UnuseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `MakePacketItemUnuseFailed` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemPause` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemUpdateItemUseTime` | 43 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemUpdateItemStaminaRemainTime` | 43 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemUpdateCooldown` | 33 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketExtra` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::MakePacketItem, AgpmItem::MakePacketItemInforMationResult, AgpmItem::MakePacketItemView; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `ChangeItemOwner` | 35 | ohne Kandidat |  | Aufrufer im Client: AgpmGuildWarehouse::AddItem, AgpmItem::OnOperationUpdate, AgpmItem::AddItemToCashInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `LockAdminItem` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseAdminItem` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `HasItemTemplate` | 15 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CharacterForAllItems` | 31 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `UseItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmItem::UseItem, AgcmUICashInven::CBCashInvenClickUseItem, AgcmUIItem::CBUseItem |
| `UseItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::UseItem, AgcmUICashInven::CBCashInvenClickUseItem, AgcmUIItem::CBUseItem |
| `CheckUseValidArea` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBCheckUseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `CheckAreaUsePotion` | 63 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::CheckUseValidArea; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetMoneyTID` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::CBPickupItemResult, AgcmUIItem::CBDisplayMessageData, AgcmUIPartyOption::CBDisplayPartyOptionGetItemMember |
| `GetArrowTID` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMain::SetArrow, AgpmItem::SetItemStackCount, AgpmItem::AddItemStackCount |
| `GetBoltTID` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMain::SetBolt, AgpmItem::SetItemStackCount, AgpmItem::AddItemStackCount |
| `GetHumanSkullTID` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetHumanSkullTID` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::StreamReadImportData |
| `GetOrcSkullTID` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetOrcSkullTID` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::StreamReadImportData |
| `GetSkullTID` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetSkullTID` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetCatalystTID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCatalystTID` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::StreamReadImportData |
| `GetLuckyScrollTID` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetLuckyScrollTID` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::StreamReadImportData |
| `GetChattingEmphasisTID` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetChattingEmphasisTID` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::StreamReadImportData |
| `GetSkillBookTID` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetSkillBookTID` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetItemMoney` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetItemMoney` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToInventory, AgpmItem::AddItemToInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetItemRank` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddItemMoney` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckUseItem` | 33 | Kandidat unbestätigt | `0x0057C190` | Aufrufer im Client: AgpmDropItem2::GetDropRate, AgpmItem::GefEffectedSkillPlusLevel, AgpmItem::CheckUpdateStatus; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SaveItemStatus` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RestoreItemStatus` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetItemStackCount` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetItemDurabilityCurrent` | 8 | nicht im Client |  | Aufrufer nur im Server (10); kein Treffer im Binary |
| `GetItemDurabilityMax` | 8 | nicht im Client |  | Aufrufer nur im Server (12); kein Treffer im Binary |
| `GetItemDurabilityMax` | 8 | nicht im Client |  | Aufrufer nur im Server (12); kein Treffer im Binary |
| `PickupItem` | 87 | Kandidat unbestätigt | `0x0053F550` | Aufrufer im Client: AgcmItem::AutoPickupItem, AgcmItem::CBActionPickupItem, AgcmTargeting::OnLButtonDown; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 13, Belegarten 2) |
| `GetHPPotionInInventory` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMPPotionInInventory` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSPPotionInInventory` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckMovableItemBetweenGrid` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RequireLevelUp` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RequireLevelDown` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRemovePolearm` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SplitItem` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBSplitItemInventory, AgpmItem::OnOperationSplitItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `CheckJoinItem` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetBoundType` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::SplitItem, AgpmItem::SplitItem, AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetBoundType` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::SplitItem, AgpmItem::SplitItem, AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetBoundType` | 12 | Kandidat unbestätigt | `0x0053EAD0` | Aufrufer im Client: AgcmUIGuildWarehouse::OnItemMovedIn, AgcmUIItem::SetItemToolTipName, AgcmUIItem::CBPrivateTradeMoveItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetShrineType` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetShrineType` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmItem::StreamReadImportData |
| `IsShrineType` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsShrineType` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsNotBound` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::CheckMovableItemBetweenGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `CheckBoundType` | 30 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::PickupItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsBoundOnOwner` | 8 | Kandidat unbestätigt | `0x0058D410` | Aufrufer im Client: AgcmUIItem::SetItemToolTipName, AgcmUIItem::CBPrivateTradeMoveItem, AgcmUIItem::_CheckBoundItemReleaseTradeCheck; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEventItem` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBPrivateTradeMoveItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetBoundOnOwner` | 10 | Kandidat unbestätigt | `0x0053EAD0` | Aufrufer im Client: AgpmItem::ChangeItemOwner, AgpmItem::PickupItem, AgpmItem::SplitItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `UpdateItemStatusFlag` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdate, AgpmItem::SetBoundType, AgpmItem::SetBoundOnOwner; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetQuestType` | 9 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `ResetQuestType` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetNearPosition` | 18 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsProperPart` | 75 | Kandidat unbestätigt | `0x00595300` | Aufrufer im Client: AgcmItemConvert::IsRuneConvertable, AgpmDropItem2::ProcessConvertItemOption, AgpmItem::AddItemOption; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsAlreadySetType` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessConvertItemOption, AgpmItem::AddItemOption, AgpmItem::AddRefineItemOption; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemOption` | 41 | Kandidat unbestätigt | `0x00582EE0` | Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgpmDropItem2::ProcessConvertItemOption; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `AddRefineItemOption` | 37 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessConvertItemOptionRefinery, AgpmDropItem2::ProcessConvertItemOptionGacha; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `CalcItemOptionFactor` | 23 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddItemSkillPlus` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIAuction::CBBoardSelect; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RemoveStatus` | 155 | Kandidat unbestätigt | `0x00591FF0` | Aufrufer im Client: AgpmGuildWarehouse::AddItem, AgpmItem::RemoveItem, AgpmItem::OnOperationRemove; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `SetCompareTemplate` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsFirstLooterOnly` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OnOperationUseItemResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnReceive |
| `UnuseItem` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmItem::UseItem, AgpmItem::OnOperationUnuseItem |
| `UnuseItem` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::UseItem, AgpmItem::OnOperationUnuseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StartCashItemTimer` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::ReceiveUseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StopCashItemTimer` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::ReceiveUnuseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `PauseCashItemTimer` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationPauseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetInitialStamina` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StartCashItemTimer; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetExistPrivateTradeOptionItem` | 28 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetFitLinkTemplate` | 16 | ohne Kandidat |  | Aufrufer im Client: CUiCharacterProperty::_GetItemOptionValuePoint, CUiCharacterProperty::_GetItemOptionValueSkill, AgcmUIItem::SetItemToolTipConvertAttrInfo; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetAvatarSetTemplate` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::Debug_EquipAvatarSet, AgpmItem::Debug_UnEquipAvatarSet; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetAvatarSetTemplateByBase` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::IsEnableEquipAvatarItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `Debug_EquipAvatarSet` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Debug_EquipAvatarSet` | 46 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Debug_UnEquipAvatarSet` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Debug_UnEquipAvatarSet` | 38 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetEquipAvatarSet` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetEquipAvatarSet` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsBaseAvatarItem` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::IsEnableEquipAvatarItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEnableEquipAvatarItem` | 32 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEnableEquipAvatarItem` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetItemSectionNum` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmItem::IsEquipUnableItemInEpicZone |
| `GetWeaponType` | 8 | Kandidat unbestätigt | `0x0058EB80` | Aufrufer im Client: AgcmEventEffect::EventCharAnimAttackCB, AgcmEventEffect::SetTargetStruckEffect, AgpmItem::AdjustDragonScionWeaponFactor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsReverseOrbTypeItem` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::CheckUseItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetItemTotalCountFromGrid` | 57 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMain::GetItemTotalCount, AgpmEventGacha::CheckProperGacha, AgpmItem::RemoveItemCompleteFromGrid; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RemoveItemCompleteFromGrid` | 70 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsContinuousOffItem` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetReuseInterval` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIItem::UpdateCooldown, AgpmItem::CheckReuseIntervalWithCooldown |
| `CheckReuseIntervalWithCooldown` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::ProcessAllItemCooldown; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsUsingItem` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBPrivateTradeMoveItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `MakeAndSendPacketEquipInfo` | 69 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_AddPrivateTradeItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnOperationAdd |
| `ItemTimeUpdate` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipUnableItemInEpicZone` | 24 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `AdjustDragonScionWeaponFactor` | 38 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `StreamReadClassfyID` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsSameClassfyID` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::IsCharacterUsingCashItemOfSameClassifyIDorTID; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StreamReadGachaDropPointTable` | 70 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `UpdateItemInBank` | 40 | Kandidat unbestätigt | `0x0053D510` | Aufrufer im Client: AgpmItem::OnOperationUpdate, AgpmItem::OnOperationStackItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `RemoveItemFromBank` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::RemoveStatus; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `ParseBankPacket` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetCallbackAddItemCashInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItemCashInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateItemCashInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseCashItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnUseCashItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPauseCashItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetPetTIDByItemFromSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `IsAnyEmptyCashInventory` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddItemToCashInventory` | 24 | Kandidat unbestätigt | `0x0053D2C0` | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::OnOperationUpdate, AgpmItem::AddItemToChargingInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `GetCashItemByTID` | 21 | Kandidat unbestätigt | `0x0053BA30` | Aufrufer im Client: AgpmItem::ProcessAllItemCooldown, AgpmItem::RemoveItemFromCashInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `GetUsingCashItemUsableByType` | 25 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `IsMarvelScroll` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::_CheckBoundItemReleaseTradeCheck |
| `RemoveItemFromCashInventory` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationRemove, AgpmItem::RemoveStatus; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RemoveItemFromCashInventory` | 10 | Kandidat unbestätigt | `0x0053BA30` | Aufrufer im Client: AgpmItem::OnOperationRemove, AgpmItem::RemoveStatus; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `ArrangeCashItemGridPos` | 20 | Kandidat unbestätigt | `0x0053BA30` | Aufrufer im Client: AgpmItem::RemoveItemFromCashInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `IsCharacterUsingCashItem` | 36 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `IsCharacterUsingCashItemOfSameClassifyIDorTID` | 42 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `UseAllAleadyInUseCashItem` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetUsingItemInvolveChargingInventory` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SubCashItemStackCountOnAttack` | 37 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `CheckEnableStopCashItem` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::UseItem, AgcmUICashInven::CBDisplayCashInvenUseItemButtonText; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetCashSkillRollbackScroll` | 22 | Kandidat unbestätigt | `0x00564630` | Aufrufer im Client: AgcmHeroicSkill::CBHeroicSkillRollBack, AgcmHeroicSkill::CBSelectHeroicSkillGrid, AgcmUISkill2::CBIsActiveRollbackButton; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetCashInventoryItemByType` | 40 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackChargingInventoryCheckAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChargingInventoryAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChargingInventoryUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChargingInventoryRemove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetChargingInventory` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmItem::AddItemToChargingInventory, AgpmItem::AddItemToChargingInventory |
| `GetChargingInventory` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToChargingInventory, AgpmItem::AddItemToChargingInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemCheckToChargingInventory` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddItemCheckToChargingInventory` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveItemFromChargingInventory` | 27 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::RemoveStatus; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemToClientTradeGrid` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::OnOperationUpdate; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetCallbackEquip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEquipForAdmin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnEquip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveForNearCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetEquipItem` | 24 | Kandidat unbestätigt | `0x0053BA30` | Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmEventEffect::EventCharAnimWaitCB, AgcmEventEffect::EventCharAnimRunCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `EquipItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmItem::OnLuaInitialize, AgcmItem::CBSetItem |
| `EquipItem` | 18 | Kandidat unbestätigt | `0x0058FB20` | Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmItem::OnLuaInitialize, AgcmItem::CBSetItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `EquipItem` | 248 | Kandidat unbestätigt | `0x0053A440` | Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmItem::OnLuaInitialize, AgcmItem::CBSetItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `UnEquipItem` | 58 | Kandidat unbestätigt | `0x0053A440` | Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmItem::OnLuaInitialize, AgcmItem::UnEquipItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `IsEquipOneHandSword` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipOneHandAxe` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipBlunt` | 33 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipTwoHandBlunt` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipTwoHandSlash` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipStaff` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmCombat::ProcessEvade, AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipWand` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmCombat::ProcessEvade, AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipBow` | 13 | Kandidat unbestätigt | `0x0058F900` | Aufrufer im Client: AgpmCombat::ProcessEvade, AgpmSkill::IsSufficientCost, AgpmSkill::IsSatisfyRequirement; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEquipCrossBow` | 13 | Kandidat unbestätigt | `0x0058F900` | Aufrufer im Client: AgpmCombat::ProcessEvade, AgpmSkill::IsSufficientCost, AgpmSkill::IsSatisfyRequirement; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEquipShield` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEquipKatariya` | 13 | Kandidat unbestätigt | `0x0058F900` | Aufrufer im Client: AgpmCombat::ProcessEvade, AgpmSkill::IsSufficientCost, AgpmSkill::IsSatisfyRequirement; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEquipChakram` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmCombat::ProcessEvade, AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipStandard` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsEquipRightHandOnly` | 20 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipCharon` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `IsEquipZenon` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSatisfyRequirement; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `ParseEquipPacket` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetEquipItems` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `EquipAvatarItem` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EquipAvatarItem` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UnEquipAvatarItem` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UnEquipAvatarItem` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackField` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `LockGrid` | 40 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseGrid` | 32 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInventoryForAdmin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveFromInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `AddItemToInventory` | 82 | Kandidat unbestätigt | `0x0053D510` | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::RestoreItemStatus, AgpmItem::SplitItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `AddItemToInventory` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::RestoreItemStatus, AgpmItem::SplitItem |
| `AddItemToInventory` | 57 | Kandidat unbestätigt | `0x0053D510` | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::RestoreItemStatus, AgpmItem::SplitItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `AddItemToInventoryResult` | 57 | Kandidat unbestätigt | `0x0058D880` | Aufrufer im Client: AgpmItem::AddItemToInventory, AgpmItem::AddItemToInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `UpdateItemInInventory` | 63 | Kandidat unbestätigt | `0x0053D510` | Aufrufer im Client: AgcmItem::UpdateInventoryForUI, AgpmItem::OnOperationUpdate, AgpmItem::OnOperationStackItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `RemoveItemFromInventory` | 26 | Kandidat unbestätigt | `0x0053B200` | Aufrufer im Client: AgcmPrivateTrade::AddItemToTradeGrid, AgpmItem::RemoveStatus, AgpmItem::RemoveItemFromChargingInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `GetInventoryPotionItem` | 38 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::GetHPPotionInInventory, AgpmItem::GetMPPotionInInventory, AgpmItem::GetSPPotionInInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `GetSkillRollbackScroll` | 28 | Kandidat unbestätigt | `0x00564630` | Aufrufer im Client: AgcmHeroicSkill::CBHeroicSkillRollBack, AgcmHeroicSkill::CBSelectHeroicSkillGrid, AgcmUISkill2::CBIsActiveRollbackButton; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetCallbackQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `AddItemToQuest` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::OnOperationAdd |
| `AddItemToQuest` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::OnOperationAdd |
| `RemoveItemFromQuest` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::RemoveStatus |
| `RemoveItemFromQuest` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::RemoveStatus |
| `UpdateQuest` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::OnOperationUpdate |
| `UpdateQuest` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItem::OnOperationUpdate |
| `SetCallbackSalesBox` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `RemoveItemFromSalesBox` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::RemoveStatus, AgpmItem::SetSalesBoxBackOut; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetSalesBoxBackOut` | 28 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ParseADCharTemplate` | 38 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::CharTemplateReadCB; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `ItemWriteCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnAddModule |
| `ItemReadCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnAddModule |
| `StreamWriteTemplate` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplates` | 44 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportItemTemplates; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StreamWriteOneTemplate` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamWriteTemplates, AgpmItem::StreamWriteModifiedTemplates; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StreamWrite` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB |
| `StreamRead` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamReadCB, AgcmExportResource::ReadUIINI, AgcmItem::ItemTemplateStreamReadCB |
| `SetDefaultEquipments` | 11 | Kandidat unbestätigt | `0x0054B260` | Aufrufer im Client: AgpmItem::CharacterImportDataReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SetDefaultEquipments` | 15 | Kandidat unbestätigt | `0x0054B260` | Aufrufer im Client: AgpmItem::CharacterImportDataReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SetDefaultInventoryItems` | 11 | Kandidat unbestätigt | `0x0054B260` | Aufrufer im Client: AgpmItem::CharacterImportDataReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SetDefaultInventoryItems` | 19 | Kandidat unbestätigt | `0x0054B260` | Aufrufer im Client: AgpmItem::CharacterImportDataReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SetDefaultMoney` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `StreamReadOptionData` | 819 | Kandidat unbestätigt | `0x00547A40` | Aufrufer im Client: AgcmUILogin::LoadTemplates; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `StreamReadBankSlotPrice` | 32 | Kandidat unbestätigt | `0x00546C70` | Aufrufer im Client: AgcmUILogin::LoadTemplates; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `StreamReadLotteryBox` | 72 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadOptionTID` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StreamReadLinkID` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `StreamReadSkillPlusTID` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamReadImportData; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `ClearItemTemplateEntry` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::LoadItemTemplateEntryINI |
| `AddItemTemplateEntry` | 30 | Kandidat unbestätigt | `0x0054A590` | Aufrufer im Client: AgpmItem::StreamWriteOneTemplate, AgpmItem::StreamReadTemplate, AgpmItem::StreamReadOneTemplate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetItemTemplateName` | 10 | Kandidat unbestätigt | `0x0054A590` | Aufrufer im Client: AgpmItem::StreamReadTemplate, AgpmItem::StreamReadOneTemplate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `LoadItemTemplateEntryXML` | 64 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveItemTemplateEntryINI` | 38 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::StreamWriteTemplates, AgpmItem::StreamWriteModifiedTemplates; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SaveItemTemplateEntryXML` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearModifiedTemplate` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmItem::StreamWriteModifiedTemplates |
| `AddModifiedTemplate` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWriteModifiedTemplates` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_LoadXmlFile` | 47 | ohne Kandidat |  | Aufrufer im Client: CFlagImoticon::LoadFlagFromFile, AgpmItem::LoadItemTemplateEntryXML; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `_SaveXmlFile` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::SaveItemTemplateEntryXML; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetCallbackSubInventoryCheckAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSubInventoryAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSubInventoryUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSubInventoryRemove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetSubInventory` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmItem::AddItemToSubInventory, AgpmItem::AddItemToSubInventory, AgpmItem::GetUnseenInventory |
| `GetSubInventory` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToSubInventory, AgpmItem::AddItemToSubInventory, AgpmItem::GetUnseenInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemCheckToSubInventory` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddItemCheckToSubInventory` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddItemToSubInventory` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::RestoreItemStatus, AgpmItem::SplitItem |
| `AddItemToSubInventory` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::RestoreItemStatus, AgpmItem::SplitItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemToSubInventory` | 29 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::RestoreItemStatus, AgpmItem::SplitItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemToSubInventoryResult` | 54 | Kandidat unbestätigt | `0x0058D880` | Aufrufer im Client: AgpmItem::AddItemToSubInventory, AgpmItem::AddItemToSubInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `UpdateItemInSubInventory` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::OnOperationUpdate, AgpmItem::OnOperationStackItem |
| `UpdateItemInSubInventory` | 61 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationUpdate, AgpmItem::OnOperationStackItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RemoveItemFromSubInventory` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItem::RemoveStatus |
| `RemoveItemFromSubInventory` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::RemoveStatus; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetCallbackTradeGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveTradeGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `AddItemToTradeGrid` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::OnOperationAdd, AgpmItem::OnOperationUpdate, AgpmItem::SplitItem; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `RemoveItemFromTradeGrid` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::RemoveStatus; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `CheckTradeCondition` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CheckInvenCondition` | 43 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::CheckTradeCondition; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `SetCallbackUnseenInventoryAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetUnseenInventory` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmItem::AddItemToUnseenInventory, AgpmItem::AddItemAutoToUnSeenInventory |
| `GetUnseenInventory` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::AddItemToUnseenInventory, AgpmItem::AddItemAutoToUnSeenInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemToUnseenInventory` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddItemToUnseenInventory` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddItemAutoToUnSeenInventory` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmItem::UpdateItemInUnseenInventory; kein unbenannter Kandidat mit Beleg unter 921 unbenannten Funktionen im Klassenbereich |
| `AddItemToUnseenInventoryResult` | 54 | Kandidat unbestätigt | `0x0058D880` | Aufrufer im Client: AgpmItem::AddItemToUnseenInventory, AgpmItem::AddItemAutoToUnSeenInventory; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `RemoveItemFromUnSeenInventory` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveItemFromUnSeenInventory` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateItemInUnseenInventory` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateItemInUnseenInventory` | 60 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmItemConvert (Kandidat unbestätigt 19, eingebaut 9, gemeinsamer Rumpf 18, nicht im Client 10, ohne Kandidat 46, zugeordnet 25)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsSocketInitializable` | 23 | zugeordnet | `0x00594B20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessSpiritStoneConvert` | 23 | zugeordnet | `0x005942D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSpiritStoneConvertable` | 31 | zugeordnet | `0x00593750` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBRequestSpiritStoneConvert` | 64 | zugeordnet | `0x00593E40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SpiritStoneConvert` | 50 | zugeordnet | `0x005939C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetNumSpiritStone` | 37 | zugeordnet | `0x005938C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSocketConvertable` | 60 | zugeordnet | `0x00594EA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidCatalyst` | 14 | zugeordnet | `0x005960A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPhysicalConvertable` | 29 | zugeordnet | `0x00596280` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalConvertPoint` | 12 | zugeordnet | `0x00583F10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DecodeConvertHistory` | 90 | zugeordnet | `0x00583490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidSpiritStone` | 16 | zugeordnet | `0x00593800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsWeapon` | 11 | zugeordnet | `0x00594A80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitializeSpiritStoneConvert` | 116 | zugeordnet | `0x00596450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ApplyPhysicalConvert` | 58 | zugeordnet | `0x00593F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitializePhysicalConvert` | 72 | zugeordnet | `0x00593B00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBRequestRuneConvert` | 81 | zugeordnet | `0x00595810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RuneConvert` | 116 | zugeordnet | `0x005954D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsProperLevel` | 16 | zugeordnet | `0x00595190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketSocketInitialize` | 20 | zugeordnet | `0x00594570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCheckCashRuneConvert` | 20 | zugeordnet | `0x00594510` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestSpiritStoneConvert` | 20 | zugeordnet | `0x005944B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestRuneConvert` | 20 | zugeordnet | `0x00594450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestSocketAdd` | 19 | zugeordnet | `0x005943F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestPhysicalConvert` | 20 | zugeordnet | `0x00594390` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItemConvert::ConAgpdItemConvertADChar, AgpmItemConvert::CBEquipItem, AgpmItemConvert::CBUnEquipItem |
| `GetADItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::GetMaxSpiritStoneType, AgcmGlyph::StartEnemyTarget, AgcmUIAuction::CBBoardSelect |
| `GetADItemTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::StreamReadTooltipDescData, AgcmUIItem::SetItemToolTipDetail, AgcmUIItem::SetItemToolTipName |
| `DesAgpdItemConvertADChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItemConvert::OnAddModule |
| `DesAgpdItemConvertADItem` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmItemConvert::OnAddModule |
| `DesAgpdItemConvertADItemTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmItemConvert::OnAddModule |
| `DispatchAddPacket` | 28 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackProcessPhysicalConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackProcessSocketConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackProcessSpiritStoneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackProcessRuneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackProcessSocketInitialize` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResultPhysicalConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResultSocketConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResultSpiritStoneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResultRuneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSendUpdateFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAskReallySpiritStoneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSpiritStoneCheckResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAskReallyRuneConvert` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRuneCheckResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAdd` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAdjustSuccessProb` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackConvertAsDrop` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CalcConvertFactor` | 11 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `EncodeConvertHistory` | 17 | nicht im Client |  | Aufrufer nur im Server (9); kein Treffer im Binary |
| `GetTotalPhysicalConvertPoint` | 13 | Kandidat unbestätigt | `0x00583740` | Aufrufer im Client: AgcmEventEffect::GetMaxSpiritStoneType, AgpmItemConvert::GetTotalConvertPoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetTotalSocketConvertPoint` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::GetTotalConvertPoint; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetTotalSpiritStoneConvertPoint` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::GetTotalConvertPoint; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetTotalRuneConvertPoint` | 26 | Kandidat unbestätigt | `0x00583740` | Aufrufer im Client: AgcmEventEffect::GetMaxSpiritStoneType, AgpmItemConvert::GetTotalConvertPoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSpiritStoneAttrConvertPoint` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::GetMaxSpiritStoneType; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `MakePacketAdd` | 47 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::AddItemConvertPacketToBuffer; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `MakePacketResponsePhysicalConvert` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseSocketAdd` | 18 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketResponseSpiritStoneConvert` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseRuneConvert` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseSpiritStoneCheckResult` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseRuneCheckResult` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetPhysicalConvertLevel` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::StartConvertedWeaponGradeEventEffect, AgpmItemConvert::PhysicalConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `PhysicalConvert` | 46 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventItemConvert::StartPhysicalConvert, AgpmItemConvert::ProcessPhysicalConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `CalcPhysicalConvertFactor` | 59 | Kandidat unbestätigt | `0x00596670` | Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgpmItemConvert::CalcConvertFactor, AgpmItemConvert::SetPhysicalConvert; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ProcessPhysicalConvert` | 59 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnOperationRequestPhysicalConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetNumPhysicalConvert` | 7 | Kandidat unbestätigt | `0x00596120` | Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBDisplayConvertItemName, AgcmUIEventItemConvert::StartPhysicalConvert; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `OnOperationRequestPhysicalConvert` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationResponsePhysicalConvert` | 51 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `SetPhysicalConvert` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessConvertItemPhysical; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetPhysicalItemRank` | 11 | Kandidat unbestätigt | `0x005961E0` | Aufrufer im Client: AgcmUIItem::_SetItemToolTipDetailRank, AgpmItemConvert::OnOperationAdd, AgpmItemConvert::GetTotalPhysicalConvertPoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetPhysicalItemRank` | 11 | Kandidat unbestätigt | `0x005961E0` | Aufrufer im Client: AgcmUIItem::_SetItemToolTipDetailRank, AgpmItemConvert::OnOperationAdd, AgpmItemConvert::GetTotalPhysicalConvertPoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetPhysicalItemRankName` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIItem::_SetItemToolTipDetailRank |
| `GetNumRune` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::RuneConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `IsRuneConvertable` | 27 | Kandidat unbestätigt | `0x00595430` | Aufrufer im Client: AgcmItemConvert::IsRuneConvertable, AgcmItemConvert::RuneConvert, AgcmUIEventItemConvert::CBAddConvertGridItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsValidRuneItem` | 13 | Kandidat unbestätigt | `0x00595430` | Aufrufer im Client: AgcmItemConvert::IsRuneConvertable, AgcmUIEventItemConvert::CBAddConvertGridItemSocket, AgpmItemConvert::CBRequestConvert; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsProperPart` | 58 | Kandidat unbestätigt | `0x00595300` | Aufrufer im Client: AgcmItemConvert::IsRuneConvertable, AgpmDropItem2::ProcessConvertItemOption, AgpmItem::AddItemOption; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsAntiNumber` | 22 | Kandidat unbestätigt | `0x00595430` | Aufrufer im Client: AgpmItemConvert::RuneConvert, AgpmItemConvert::CBRequestRuneConvert; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `InitializeRuneConvert` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::InitializeSocket; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `AddRuneConvert` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmItemConvert::DecodeConvertHistory, AgpmItemConvert::ProcessRuneConvert |
| `AddRuneConvert` | 30 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::DecodeConvertHistory, AgpmItemConvert::ProcessRuneConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationRequestRuneConvert` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationResponseRuneConvert` | 54 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationCheckCashRuneConvert` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationResponseRuneCheckResult` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `IsConvertedAttribute` | 19 | Kandidat unbestätigt | `0x00595990` | Aufrufer im Client: AgcmItem::OnEquipItemNecklace, AgcmItem::OnUnEquipItemNecklace; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetConvertedExtraType` | 19 | Kandidat unbestätigt | `0x00595990` | Aufrufer im Client: AgcmItem::OnEquipItemNecklace, AgcmItem::OnUnEquipItemNecklace; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CalcRuneConvertFactor` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::CalcConvertFactor; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `AddItemOptionRune` | 62 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::AddRuneConvert, AgpmItemConvert::CalcRuneConvertFactor; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `RemoveItemOptionRune` | 42 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::InitializeRuneConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetNumSocket` | 7 | Kandidat unbestätigt | `0x00596120` | Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBDisplayConvertItemName, AgcmUIEventItemConvert::UpdatePhysicalConvertConfirm; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetNumConvertedSocket` | 7 | Kandidat unbestätigt | `0x00596120` | Aufrufer im Client: AgcmUIAuction::CBBoardSelect, CUiCharacterProperty::_GetItemOptionValuePoint, CUiCharacterProperty::_GetItemOptionValueSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSocketCost` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::GetNextSocketCost, AgpmItemConvert::ProcessSocketConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetSocketCost` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::GetNextSocketCost, AgpmItemConvert::ProcessSocketConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetNextSocketCost` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventItemConvert::RecalcConvertCost; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `IsEnoughSocketCost` | 45 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::IsSocketConvertable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `IsArmour` | 14 | Kandidat unbestätigt | `0x00594AE0` | Aufrufer im Client: AgcmUIItem::_SetItemToolTipEquip, AgpmItemConvert::GetSocketCost, AgpmItemConvert::IsEnoughSocketCost; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsEtc` | 13 | Kandidat unbestätigt | `0x00594AE0` | Aufrufer im Client: AgpmItemConvert::GetSocketCost, AgpmItemConvert::IsEnoughSocketCost, AgpmItemConvert::IsSocketConvertable; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SocketConvert` | 78 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventItemConvert::StartSocketConvert, AgpmItemConvert::ProcessSocketConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `InitializeSocket` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::ProcessRuneConvert, AgpmItemConvert::ProcessSocketConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `AddSocketConvert` | 27 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::ProcessSocketConvert; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `ProcessSocketConvert` | 66 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnOperationRequestAddSocket; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationRequestAddSocket` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationResponseAddSocket` | 40 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `SetSocketConvert` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmDropItem2::ProcessConvertItemSocket; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `GetNumConvertAttr` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::GetSpiritStoneInfo, AgpmCombat::IsFirstSpiritAttackSuccess, AgpmCombat::GetArmourAttributeInfo; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `AddSpiritStoneConvert` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmItemConvert::DecodeConvertHistory, AgpmItemConvert::ProcessSpiritStoneConvert |
| `AddSpiritStoneConvert` | 76 | Kandidat unbestätigt | `0x00596670` | Aufrufer im Client: AgpmItemConvert::DecodeConvertHistory, AgpmItemConvert::ProcessSpiritStoneConvert; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CalcSpiritStoneConvertFactor` | 110 | Kandidat unbestätigt | `0x00596670` | Aufrufer im Client: AgpmItemConvert::CalcConvertFactor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `OnOperationRequestSpiritStoneConvert` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationResponseSpiritStoneConvert` | 43 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `OnOperationResponseSpiritStoneCheckResult` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::OnReceive; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamReadConvertTable` | 80 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::LoadTemplates, AgpmItemConvert::StreamReadRuneAttribute, AgpmItemConvert::StreamReadConvertPointTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertPhysicalTable` | 83 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertPhysicalSuccessTable` | 42 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertPhysicalFailTable` | 42 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertPhysicalInitTable` | 43 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertPhysicalDestroyTable` | 43 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertSpiritStoneTable` | 42 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertAddBonusTable` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertRuneTable` | 40 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamConvertRuneFailTable` | 58 | ohne Kandidat |  | Aufrufer im Client: AgpmItemConvert::StreamReadConvertTable; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamReadRuneAttribute` | 217 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::LoadTemplates; kein unbenannter Kandidat mit Beleg unter 278 unbenannten Funktionen im Klassenbereich |
| `StreamReadConvertPointTable` | 45 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsEgoItem` | 14 | Kandidat unbestätigt | `0x00594AE0` | Aufrufer im Client: AgcmUIItem::CBDisplayMessageData, AgcmUIItem::SetItemToolTipName, AgcmUIItem::SetItemToolTipPrice; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AgpmMailBox (eingebaut 4, gemeinsamer Rumpf 5, nicht im Client 5, ohne Kandidat 2, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsValidAttachItem` | 54 | zugeordnet | `0x00558380` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketMail` | 39 | zugeordnet | `0x00557D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketMailOnlyID` | 18 | zugeordnet | `0x00557E40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetLetterCount` | 32 | zugeordnet | `0x00557C80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCAD` | 5 | zugeordnet | `0x00557C50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxMail` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyMail` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIMailBox::CBAddMail, AgcmUIMailBox::CBRemoveMail, AgpmMailBox::OnReceive |
| `GetMail` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMailBox::OnIdle, AgcmUIMailBox::CBRemoveMail, AgcmUIMailBox::CBItemSave |
| `AddMail` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMailBox::CBAddMail |
| `RemoveMail` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMailBox::CBAddMail, AgcmUIMailBox::CBRemoveMail, AgpmMailBox::AddMailToCAD |
| `AddMailToCAD` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMailBox::CBAddMail; kein unbenannter Kandidat mit Beleg unter 333 unbenannten Funktionen im Klassenbereich |
| `RemoveMailFromCAD` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `RemoveMailFromCAD` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `FindMailFromCAD` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SubLetter` | 26 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsWesterPreOrderItem` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmMailBox::IsValidAttachItem; kein unbenannter Kandidat mit Beleg unter 333 unbenannten Funktionen im Klassenbereich |
| `SetCallbackAddMail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveMail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReadMail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackWriteMail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackItemSave` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmNatureEffect (gemeinsamer Rumpf 3, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `MakePacket` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAuction::SendSelect, AgcmAuction::SendSell, AgcmAuction::SendCancel; im Adressbereich der Klasse (0x00576D30–0x00576D90) ist keine unbenannte Funktion mehr übrig |
| `SetNatureEffect` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmNatureEffect::OnInit, AgcmNatureEffect::OnLuaInitialize; im Adressbereich der Klasse (0x00576D30–0x00576D90) ist keine unbenannte Funktion mehr übrig |

## AgpmOptimizedPacket2 (gemeinsamer Rumpf 4, nicht im Client 9, ohne Kandidat 14, zugeordnet 7)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketCharMove` | 33 | zugeordnet | `0x0057D2E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessItemPacket` | 111 | zugeordnet | `0x0057D400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessCharacterPacket` | 131 | zugeordnet | `0x0057CD80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnReceiveCharAction` | 74 | zugeordnet | `0x0057D7A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnReceiveCharView` | 100 | zugeordnet | `0x0057CBF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCharAction` | 23 | zugeordnet | `0x0057D350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnReceiveCharMove` | 63 | zugeordnet | `0x0057CA50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetMaxMemoryPoolCount` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ProcessBuffedSkillPacket` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::OnReceiveCharView; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ProcessEventPacket` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::OnReceiveCharView; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ProcessCharAllItemPacket` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::OnReceiveCharView; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ProcessCharAllItemConvertPacket` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::OnReceiveCharView; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ProcessCharAllSkillPacket` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::OnReceiveCharView; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakePacketCharView` | 310 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCharMove` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendMoveCharacter; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakePacketCharMoveContainAction` | 58 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketReleaseMoveAction` | 24 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCharAction` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendActionInfo; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `AddItemPacketToBuffer` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakeBufferCharAllItem, AgpmOptimizedPacket2::MakeBufferCharAllBankItem, AgpmOptimizedPacket2::MakeBufferCharAllCashItem; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `AddItemConvertPacketToBuffer` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakeBufferCharAllItem, AgpmOptimizedPacket2::MakeBufferCharAllBankItem, AgpmOptimizedPacket2::MakeBufferCharAllCashItem; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakeBufferCharAllItem` | 126 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakePacketCharAllItemExceptBankCash; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakeBufferCharAllBankItem` | 51 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakePacketCharAllBankItem; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakeBufferCharAllCashItem` | 51 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakePacketCharAllCashItem; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakeBufferCharAllSkill` | 40 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakePacketCharAllSkill; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MakePacketCharAllItemExceptBankCash` | 42 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCharAllSkill` | 41 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCharAllBankItem` | 42 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCharAllCashItem` | 42 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackMoveActionAttack` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoveActionSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMoveActionRelease` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetCharBitFlag` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCharBitFlag` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::ProcessCharacterPacket; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |

## AgpmParty (Kandidat unbestätigt 4, eingebaut 17, nicht im Client 30, ohne Kandidat 20, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DestroyPartyData` | 4 | zugeordnet | `0x005668B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveParty` | 30 | zugeordnet | `0x00566DA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRemoveParty` | 23 | zugeordnet | `0x00566BB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ArrangeHighestUnionRank` | 33 | zugeordnet | `0x005673A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreatePartyData` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::AddParty; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `SetMaxParty` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxPartyRemove` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddParty` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::CreateParty; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetParty` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmUIWorldmap::OnIdle, AgcmHPBar::SetData |
| `GetParty` | 12 | Kandidat unbestätigt | `0x00566ED0` | Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmUIWorldmap::OnIdle, AgcmHPBar::SetData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetPartyLock` | 13 | Kandidat unbestätigt | `0x00566E50` | Aufrufer im Client: AcUIMinimap::RenderPartyMember, AgcmUIParty::CBReceiveDelegationLeader, AgpmParty::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetLeaderCID` | 7 | Kandidat unbestätigt | `0x00566AC0` | Aufrufer im Client: CChatCmd::CallBack_OnInviteParty, AgcmUIPartyOption::CBPartyOptionInviteMember, AgpmParty::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddMember` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmGuild::JoinMember, AgpmGuild::RenameCharID, AgpmParty::CreateParty |
| `AddMember` | 49 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::JoinMember, AgpmGuild::RenameCharID, AgpmParty::CreateParty; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `RemoveMember` | 88 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::LeaveMember, AgpmGuild::ForcedLeaveMember, AgpmGuild::RenameCharID; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `DelegationLeader` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::CBReceiveDelegationLeader; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `ChangeLeader` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::RemoveMember, AgpmParty::DelegationLeader; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `IsMember` | 11 | Kandidat unbestätigt | `0x00566ED0` | Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmGuild::IsGuildBattle, AgcmGuild::IsGuildBattleMember; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsFull` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::AddMember, AuGenerateID::AddRemoveID, AuRemovePool::AddData; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `IsNeedDestroy` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::RemoveMember; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `CalcPartyFactor` | 120 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CreateParty` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::OnReceive; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `CreateParty` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmParty::OnReceive |
| `CreateParty` | 30 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::OnReceive; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `DestroyParty` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::RemoveMember, AgpmParty::OnReceive; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetNextGetItemMember` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmParty::DelegationLeader, AgpmParty::ReSetCurrentGetItemMember |
| `GetNextGetItemMember` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::DelegationLeader, AgpmParty::ReSetCurrentGetItemMember; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `ReSetCurrentGetItemMember` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmParty::RemoveMember |
| `ReSetFinishGetItemMember` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::RemoveMember; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `SetCBRemoveParty` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTextBoardMng::OnAddModule, AgcmUIParty::OnAddModule, AgcmUIPartyOption::OnAddModule |
| `SetCBRemoveID` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCBChangeLeader` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIParty::OnAddModule, AgcmUIPartyOption::OnAddModule |
| `SetCBAddMember` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTextBoardMng::OnAddModule, AgcmUIParty::OnAddModule |
| `SetCBRemoveMember` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmParty::OnAddModule, AgcmTextBoardMng::OnAddModule, AgcmUIParty::OnAddModule |
| `SetCBSyncRemoveCharacter` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCBCreateParty` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCBResetEffectArea` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIParty::OnAddModule |
| `SetCBAddParty` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTextBoardMng::OnAddModule, AgcmUIParty::OnAddModule, AgcmUIPartyOption::OnAddModule |
| `SetCBUpdateFactor` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCBCheckDestroyParty` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmParty::OnAddModule |
| `SetCBCharLevelUp` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCBUpdateExpType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIParty::OnAddModule, AgcmUIPartyOption::OnAddModule |
| `SetCBUpdateBonusStats` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIParty::OnAddModule |
| `SetCBUpdatePartyFactor` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCBUpdateItemDivision` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIPartyOption::OnAddModule |
| `AttachPartyData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketParty` | 37 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketAddMember` | 32 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketRemoveMember` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketRemoveParty` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSyncMemberHP` | 47 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSyncMemberHPMax` | 47 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketEffectArea` | 55 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketItemDivision` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmParty::SendPacketUpdateItemDivision |
| `MakePacketItemDivision` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketUpdateItemDivision; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `MakePacketExpDivision` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmParty::SendPacketUpdateExpType, AgcmParty::SendPacketUpdateExpType |
| `MakePacketExpDivision` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmParty::SendPacketUpdateExpType, AgcmParty::SendPacketUpdateExpType; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `MakePacketBonusStatus` | 52 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetNumPartyMember` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetNumPartyMember` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetPartyHighestLevel` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetPartyHighestLevel` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetPartyLowerLevel` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetPartyLowerLevel` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetPartyHighestUnionRank` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetPartyHighestUnionRank` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `ArrangeHighestLevel` | 33 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::RemoveMember; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `ArrangeLowerLevel` | 34 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::RemoveMember; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `ArrangeLevel` | 35 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::CBCharLevelUp; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetPartyAvrMemberLevel` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetPartyTotalMemberLevel` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetPartyTotalMemberLevel` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `ProcessRemove` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmCharacter::OnIdle2, AgpmCharacter::ProcessRemove, AgpmItem::OnIdle2; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `SetEffectArea` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmParty::AddMember, AgpmParty::ChangeLeader; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetPartySequence` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmProduct (Kandidat unbestätigt 2, eingebaut 8, gemeinsamer Rumpf 5, nicht im Client 8, ohne Kandidat 10, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetExpOfCurrLevel` | 22 | zugeordnet | `0x0055F000` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckTargetStatus` | 23 | zugeordnet | `0x0055EFB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsComposeSkill` | 12 | zugeordnet | `0x0055F390` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetMaxExpOfCurrLevel` | 15 | zugeordnet | `0x0055F090` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidItemStatus` | 37 | zugeordnet | `0x0055EEF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetComposeList` | 16 | zugeordnet | `0x0055EE50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsValidStatus` | 41 | zugeordnet | `0x0055FE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsValidStatus` | 41 | zugeordnet | `0x0055FD60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetMaxSkillFactor` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxComposeTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetProductSkillFactor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmProduct::AddSkillExp, AgpmProduct::GetLevelOfExp, AgpmProduct::GetExpOfCurrLevel |
| `GetComposeTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIProduct::CBDisplayMakeEdit, AgcmUIProduct::OnPostResult, AgcmUIProduct::DisplaySourceItem |
| `GetComposeList` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProduct::Open, AgcmUIProductSkill::SetBuyList; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetSkillList` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProductSkill::SetBuyList, AgpmProduct::IsSatisfyPrerequisites, AgpmProduct::IsValidComposeLevel; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `DesAgpdGatherCharacterTAD` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmProduct::OnAddModule |
| `InitGatherData` | 12 | Kandidat unbestätigt | `0x0055F430` | Aufrufer im Client: AgpmProduct::CBResetMonster, AgpmProduct::ConAgpdGatherCharacterAD; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `InitComposeData` | 11 | Kandidat unbestätigt | `0x0055F480` | Aufrufer im Client: AgpmProduct::CBResetMonster, AgpmProduct::ConAgpdComposeCharacterAD; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGatherCharacterTAD` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmProduct::ConAgpdGatherCharacterTAD, AgpmProduct::CheckTargetGatherApplicable, AgpmProduct::StreamReadGatherCharacterTAD |
| `GetGatherCharacterAD` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmProduct::InitGatherData, AgpmProduct::ConAgpdGatherCharacterAD, AgpmProduct::DesAgpdGatherCharacterAD |
| `GetComposeCharacterAD` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmProduct::GetComposeList, AgpmProduct::InitComposeData, AgpmProduct::ConAgpdComposeCharacterAD |
| `IsOwnCompose` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmEventProduct::IsValidBuyCompose, AgpmProduct::IsValidStatus, AgpmProduct::LearnCompose; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `IsSatisfyPrerequisites` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmEventProduct::IsValidBuyCompose; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `IsValidComposeLevel` | 31 | ohne Kandidat |  | Aufrufer im Client: AgpmEventProduct::IsValidBuyCompose, AgpmProduct::IsValidStatus; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `CheckTargetGatherApplicable` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmProduct::IsValidStatus; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `CheckTargetHasProduct` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddSkillExp` | 42 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetLevelOfExp` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmProduct::AddSkillExp, AgpmProduct::SetSkillLevel; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetLevelOfExp` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmProduct::AddSkillExp, AgpmProduct::SetSkillLevel; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `SetSkillLevel` | 27 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `LearnCompose` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmEventProduct::OnOperationBuyComposeResult; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `LearnCompose` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmEventProduct::OnOperationBuyComposeResult |
| `SetCallbackCompose` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGather` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackComposeInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `IsActiveRequireTitle` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIProduct::OnMake |
| `StreamReadCategory` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadCompose` | 135 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadFactor` | 67 | ohne Kandidat |  | Aufrufer im Client: AgpmFactors::StreamRead, AgpmFactors::StreamReadFactor; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `StreamReadGatherCharacterTAD` | 62 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmPvP (Kandidat unbestätigt 20, eingebaut 9, gemeinsamer Rumpf 35, nicht im Client 37, ohne Kandidat 9, zugeordnet 27)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetPvPModeByRegion` | 16 | zugeordnet | `0x0057E760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsInRaceBattle` | 6 | zugeordnet | `0x0057E7D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RegionChange` | 71 | zugeordnet | `0x0057FA80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsFriendGuild` | 14 | zugeordnet | `0x0057FEA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitEnemyGuildList` | 61 | zugeordnet | `0x005814E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitFriendGuildList` | 35 | zugeordnet | `0x00581AB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitEnemyList` | 35 | zugeordnet | `0x00581A10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitFriendList` | 35 | zugeordnet | `0x00581970` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCharacter` | 51 | zugeordnet | `0x00582180` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitCharacter` | 39 | zugeordnet | `0x00581E10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEnemyGuild` | 44 | zugeordnet | `0x005826C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddFriendGuild` | 36 | zugeordnet | `0x005825F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateEnemy` | 15 | zugeordnet | `0x0057FCD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEnemy` | 8 | zugeordnet | `0x00582540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSkillEnableSummons` | 99 | zugeordnet | `0x0057F260` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsAttackableSummons` | 80 | zugeordnet | `0x0057E8A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsEnemyCharacter` | 54 | zugeordnet | `0x00580020` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateEnemyGuild` | 17 | zugeordnet | `0x0057FE30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateFriendGuild` | 16 | zugeordnet | `0x0057FD80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsInvincible` | 15 | zugeordnet | `0x0057F180` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsNowPvP` | 20 | zugeordnet | `0x0057F110` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsCombatPvPMode` | 12 | zugeordnet | `0x0057F040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsFreePvPMode` | 12 | zugeordnet | `0x0057EFE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSafePvPMode` | 12 | zugeordnet | `0x0057EF80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSkillEnable` | 297 | zugeordnet | `0x005808D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsAttackable` | 254 | zugeordnet | `0x005801D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 23 | zugeordnet | `0x0057E630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `ConAgpdPvPADChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmPvP::OnAddModule |
| `DesAgpdPvPADChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmPvP::OnAddModule |
| `AddRaceWinResult` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddRaceLoseResult` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetRaceWinResult` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRaceLoseResult` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnReceiveRaceBattle` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::OnReceive; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `AddFriend` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgcmUIBuddy::OnInit, AgpmPvP::OnReceiveAddFriend; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `AddFriend` | 39 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgcmUIBuddy::OnInit, AgpmPvP::OnReceiveAddFriend; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `RemoveFriend` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgcmUIBuddy::OnInit, AgpmPvP::OnReceiveRemoveFriend; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `RemoveFriend` | 34 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgcmUIBuddy::OnInit, AgpmPvP::OnReceiveRemoveFriend; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `UpdateFriend` | 13 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::OnReceiveUpdateFriend; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `IsFriend` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIBuddy::CBRemoveBuddy, AgcmUIBuddy::BuddyListUpdate, AgpmBuddy::AddBuddy; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `IsFriend` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIBuddy::CBRemoveBuddy, AgcmUIBuddy::BuddyListUpdate, AgpmBuddy::AddBuddy; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `GetFriendInfo` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::UpdateFriend, AgpmPvP::IsFriend; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `GetFriendInfo` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::UpdateFriend, AgpmPvP::IsFriend; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `AddEnemy` | 41 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::OnReceiveAddEnemy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `RemoveEnemy` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::OnReceiveRemoveEnemy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `RemoveEnemy` | 30 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::OnReceiveRemoveEnemy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `IsEnemy` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::AddEnemy, AgpmPvP::IsEnemyCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `IsEnemy` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::AddEnemy, AgpmPvP::IsEnemyCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetEnemyInfo` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::UpdateEnemy, AgpmPvP::IsEnemy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetEnemyInfo` | 17 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::UpdateEnemy, AgpmPvP::IsEnemy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `RemoveFriendGuild` | 30 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::OnReceiveRemoveFriendGuild; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `GetFriendGuildInfo` | 19 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::UpdateFriendGuild, AgpmPvP::IsFriendGuild; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `RemoveEnemyGuild` | 36 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgpmPvP::OnReceiveRemoveEnemyGuild; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `IsEnemyGuild` | 8 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgcmTextBoardMng::ChangeGuildIDColor, AgcmTextBoardMng::CB_PvPRefreshGuild, AgcmUIGuild::CBReceiveBattleCancelRequest; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetEnemyGuildInfo` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::UpdateEnemyGuild, AgpmPvP::IsEnemyGuild; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `GetItemDropProbability` | 89 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkullDropLevel` | 47 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetAreaDrop` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmPvP::GetItemDropProbability |
| `GetItemDrop` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkullDrop` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::GetSkullDropLevel; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `GetPvPModeByPosition` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmPvP::RegionChange |
| `UpdatePvPStatus` | 21 | nicht im Client |  | Aufrufer nur im Server (16); kein Treffer im Binary |
| `SetDeadInCombatArea` | 14 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetRaceBattleStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIPvP::OnRaceBattleStatus, AgpmPvP::IsInRaceBattle, AgpmPvP::IsInRaceBattleReward |
| `SetRaceBattleStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIPvP::OnRaceBattleStatus |
| `IsInRaceBattleReward` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmPvP::GetRaceBattleWinner |
| `SetRaceBattleResult` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::OnReceiveRaceBattle; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `GetRaceBattleWinner` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIPvP::DrawBattleInfoResult |
| `IsPC` | 9 | Kandidat unbestätigt | `0x0057E800` | Aufrufer im Client: AgcmBattleGround::IsOtherRace, AgcmCharacter::CBUpdateCharacter2, AgcmCharacter::CBUpdatePosition; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `IsFriendCharacter` | 28 | Kandidat unbestätigt | `0x0057FF00` | Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmTextBoardMng::GetTargetIDColor, AgpmPvP::IsAttackable; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsAttackSkill` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUISkill2::IsUsableSkill, AgpmPvP::IsSkillEnable |
| `IsAttackSkill` | 13 | Kandidat unbestätigt | `0x0057F240` | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUISkill2::IsUsableSkill, AgpmPvP::IsSkillEnable; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `ProcessSystemMessage` | 12 | Kandidat unbestätigt | `0x0057FF00` | Aufrufer im Client: AgcmItem::UnuseItem, AgcmUIAuction::CBBuyItemFromAuction, AgcmUIAuction::CBSellUI; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetCallbackPvPInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddFriend` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddEnemy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveFriend` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveEnemy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPvPResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitFriend` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitEnemy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFriend` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateEnemy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddFriendGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddEnemyGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveFriendGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveEnemyGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitFriendGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitEnemyGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFriendGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateEnemyGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRecvCannotUseTeleport` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEnterSafePvPArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEnterFreePvPArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEnterCombatPvPArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLeaveSafePvPArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLeaveFreePvPArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLeaveCombatPvPArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSystemMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestDeadType` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseDeadType` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsFriendSiegeWar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsEnemySiegeWar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsInSiegeWarIngArea` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckNPCAttackableTarget` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsAttackableTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRaceBattleStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePvPPacket` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::MakePvPInfoPacket, AgpmPvP::MakePvPResultPacket, AgpmPvP::MakeAddFriendPacket; kein unbenannter Kandidat mit Beleg unter 38 unbenannten Funktionen im Klassenbereich |
| `MakePvPInfoPacket` | 10 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakePvPResultPacket` | 12 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakeAddFriendPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeAddEnemyPacket` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeRemoveFriendPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeRemoveEnemyPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeInitFriendPacket` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakeInitEnemyPacket` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeUpdateFriendPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeUpdateEnemyPacket` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeAddFriendGuildPacket` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeAddEnemyGuildPacket` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeRemoveFriendGuildPacket` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeRemoveEnemyGuildPacket` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeInitFriendGuildPacket` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeInitEnemyGuildPacket` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeUpdateFriendGuildPacket` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeUpdateEnemyGuildPacket` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeCannotUseTeleportPacket` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeSystemMessagePacket` | 9 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakeRequestDeadTypePacket` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeResponseDeadTypePacket` | 8 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakeRaceBattlePacket` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetMaxAreaDropAdmin` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxItemDropAdmin` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxSkullDropAdmin` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadItemDropTxt` | 108 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSkullDropTxt` | 92 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmQuest (Kandidat unbestätigt 1, gemeinsamer Rumpf 15, nicht im Client 13, ohne Kandidat 16, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `StreamReadGroup` | 48 | zugeordnet | `0x00539D50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateTemplate` | 12 | zugeordnet | `0x00558C80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `PrevNextQuestDataSetting` | 24 | zugeordnet | `0x00537AD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EvaluationCompleteCondition` | 66 | zugeordnet | `0x00558DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EvaluationStartCondition` | 60 | zugeordnet | `0x00558CC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetTemplateSequence` | 7 | zugeordnet | `0x00558C60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackRequireQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequireQuestResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCompleteQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCompleteQuestResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCancelQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCancelQuestResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInventoryFull` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackQuestInventoryFull` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckPointResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDisableForaWhile` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackQuestRegisterJournalChange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitQuest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetMaxTemplateCount` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxGroupCount` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddTemplate` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmShrine::AddShrineTemplate, ApmMap::LoadTemplate; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `DeleteTemlate` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyTemplate` | 7 | Kandidat unbestätigt | `0x00541580` | Aufrufer im Client: AgpmCharacter::OnDestroy, AgpmCharacter::AddCharacterTemplate, AgpmCharacter::RemoveCharacterTemplate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `AddGroup` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSpawn::AddSpawnGroup, AgpmEventSpawn::ChangeGroupName, AgpmQuest::StreamReadGroup; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `DeleteGroup` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetGroupSequence` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSpawn::OnDestroy, AgpmEventSpawn::StreamWriteGroup, AgpmEventSpawn::GetSpawnByMonsterTID; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `CreateGroup` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmQuest::AddGroup; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `DestroyGroup` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmQuest::OnDestroy, AgpmQuest::AddGroup, AgpmQuest::DeleteGroup; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `IsHaveQuest` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::GetAcceptQuestNameColor; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `MakePacketEmbeddedQuest` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmQuest::MakePacketInitQuest, AgpmQuest::MakePacketUpdateQuest, AgpmQuest::MakePacketQuestRegisterJournal; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `GetFieldEmbeddedPacket` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIQuest2::CBRequireQuestResult, AgcmUIQuest2::CBUpdateQuest, AgpmQuest::OnReceive; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `MakePacketInitQuest` | 20 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketRequireQuest` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::SendPacketRequireQuest; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `MakePacketRequireQuestResult` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketQuestComplete` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::SendPacketCompleteQuest; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `MakePacketQuestCompleteResult` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketInitFlag` | 19 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketQuestCancel` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::SendPacketQuestCancel; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `MakePacketQuestCancelResult` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketInventoryFull` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketQuestInventoryFull` | 17 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketUpdateQuest` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketRequireCheckPoint` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::SendPacketCheckPoint; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `MakePacketQuestRegisterJournal` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::SendPacketQuestJournalRegisterChange; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `CharReplace` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmQuest::StreamReadTemplate; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `StreamReadTemplateFileList` | 122 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadQuestList` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmQuest::StreamReadGroup; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |
| `StreamReadCheckPoint` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmQuest::StreamReadGroup; kein unbenannter Kandidat mit Beleg unter 270 unbenannten Funktionen im Klassenbereich |

## AgpmRefinery (gemeinsamer Rumpf 4, nicht im Client 3, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakeResKey` | 15 | zugeordnet | `0x005290D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidStatusRefine` | 10 | zugeordnet | `0x005293A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetRefineResultItems` | 52 | zugeordnet | `0x00529180` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInit` | 8 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetMaxRefineItem` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRefineItem` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsValidStatusRefine` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmUIRefinery::CBClickRefineButton; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `SetCallbackResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRefineItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBadboy` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `OnOperationRefineItem` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmRefinery::OnReceive; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `StreamReadRefineItem2` | 110 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmRemission (gemeinsamer Rumpf 3, nicht im Client 1, ohne Kandidat 6, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketEventRequest` | 17 | zugeordnet | `0x0056B9F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidStatus` | 61 | zugeordnet | `0x0056C540` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationEventRequest` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `OnOperationEventGrant` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `IsValidItem` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIRemission::CBDisplayIndulCount, AgpmRemission::IsValidStatus; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `GetRemissionItemCountFromInventory` | 47 | ohne Kandidat |  | Aufrufer im Client: AgpmRemission::IsValidItem; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `GetRemissionItemCountFromCashInventory` | 47 | ohne Kandidat |  | Aufrufer im Client: AgpmRemission::IsValidItem; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemit` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketEventGrant` | 16 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `CBEventDestructor` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmAuction::OnAddModule, AgpmEventBinding::OnAddModule, AgpmEventGuide::OnAddModule; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |

## AgpmReturnToLogin (eingebaut 4, gemeinsamer Rumpf 7, nicht im Client 5, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketReconnectLoginServer` | 13 | zugeordnet | `0x0057BF60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequest` | 13 | zugeordnet | `0x0057BF10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationRequestFailed` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmReturnToLogin::OnReceive |
| `OnOperationResponseKey` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmReturnToLogin::OnReceive |
| `OnOperationSendKeyAddr` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmReturnToLogin::OnReceive |
| `OnOperationEndProcess` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmReturnToLogin::OnReceive |
| `SetCallbackRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestFailed` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestKey` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseKey` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSendKeyAddr` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReconnectLoginServer` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEndProcess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketRequestFailed` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketRequestKey` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResponseKey` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketReceivedAuthKey` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketEndProcess` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmRide (gemeinsamer Rumpf 8, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackRideReq` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRideAck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDismountReq` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDismountAck` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackTimeout` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRideTID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakePacketRide` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmScript (gemeinsamer Rumpf 7, nicht im Client 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakeScriptPacket` | 13 | zugeordnet | `0x00588100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle2` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackKeywords` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackIsAdmin` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `MakeScriptKeywordPacket` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `TestMessage` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmSearch (eingebaut 2, gemeinsamer Rumpf 6, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnReceiveSearchName` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmSearch::OnReceive |
| `OnReceiveFail` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmSearch::OnReceive |
| `MakeSearchPacket` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUISearch::SendSearchCondition; im Adressbereich der Klasse (0x0056B450–0x0056B560) ist keine unbenannte Funktion mehr übrig |
| `SetCallbackSearchName` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSearchTID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSearchLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSearchTIDLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackFail` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmShrineBattle (Kandidat unbestätigt 2, eingebaut 20, gemeinsamer Rumpf 2, nicht im Client 9, ohne Kandidat 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 9 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `IsInShrineRegion` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmShrine::CBShrineMessage |
| `IsInShrineRegion` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::CBShrineMessage; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `OnProcessShrinePointInformationRequest` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointTimeBarUpdate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointStatusUpdate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointTryImprint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointTryImprintResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointJoinAnswer` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointReadyToStart` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointMessageCode` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointPvPRecord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `OnProcessShrinePointRaceRecord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmShrineBattle::OnReceive |
| `SetCallBackShrinePointInformationRequest` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackShrinePointInformation` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointInformationTotal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointTimeBarUpdate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointStatusUpdate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointTryImprint` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackShrinePointTryImprintResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointMessageCode` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointJoinAnswer` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackShrinePointReadyToStart` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointPvPRecord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `SetCallBackShrinePointRaceRecord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::OnAddModule |
| `StreamReadShrineRegionData` | 69 | ohne Kandidat |  | Aufrufer im Client: AgpmShrineBattle::LoadShrineBattleData; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `StreamReadShrinePointData` | 43 | ohne Kandidat |  | Aufrufer im Client: AgpmShrineBattle::LoadShrineBattleData; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `StreamReadShrineMessageData` | 56 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ShuffleShrineRegion` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmShrineBattle::LoadShrineBattleData; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `RandomPlaceShrineRegion` | 83 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsInShrineRegionByIndex` | 58 | Kandidat unbestätigt | `0x0056A950` | Aufrufer im Client: AgcmEventEffect::SetCommonCharEffect, AgcmEventEffect::CBRestoreCommonEffectsByEvolution, AgcmShrine::IsOtherRace; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `IsInShrineRegionByIndex` | 56 | Kandidat unbestätigt | `0x0056A950` | Aufrufer im Client: AgcmEventEffect::SetCommonCharEffect, AgcmEventEffect::CBRestoreCommonEffectsByEvolution, AgcmShrine::IsOtherRace; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `FindResurrectionIndexInShrineArea` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmEventBinding::GetBindingPositionForResurrection, AgpmEventBinding::GetBindingPositionForShrineBattleArea; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `FindResurrectionIndexInShrineArea` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmEventBinding::GetBindingPositionForResurrection, AgpmEventBinding::GetBindingPositionForShrineBattleArea; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `IsInShrineRegionPast` | 11 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsInShrineRegionPast` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `FindShrinePointAreaInvalveCharacter` | 15 | ohne Kandidat |  | Aufrufer im Client: AgpmShrineBattle::FindResurrectionIndexInShrineArea, AgpmShrineBattle::FindResurrectionIndexInShrineArea, AgpmShrineBattle::IsShrineBattleOpenAtThisArea; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `IsShrineBattleOpenAtThisArea` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsInTryImprintRange` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::ClickShrine; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `LoadShrineBattleData` | 236 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpmSiegeWar (Kandidat unbestätigt 11, eingebaut 15, gemeinsamer Rumpf 34, nicht im Client 46, ohne Kandidat 40, zugeordnet 28)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetDurationMSec` | 6 | zugeordnet | `0x00520170` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsCastleOwner` | 11 | zugeordnet | `0x00521D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSiegeWarInfo` | 6 | zugeordnet | `0x00520590` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckValidRepairAttackObject` | 41 | zugeordnet | `0x00523320` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckValidUseAttackObject` | 41 | zugeordnet | `0x005231D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckNeedItemForUse` | 32 | zugeordnet | `0x00521490` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCarveASeal` | 20 | zugeordnet | `0x0051FB80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRemoveItemToAttackObject` | 21 | zugeordnet | `0x0051FB20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketAddItemToAttackObject` | 21 | zugeordnet | `0x0051FAC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestRepairAttackObject` | 20 | zugeordnet | `0x0051FA60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestUseAttackObject` | 20 | zugeordnet | `0x0051FA00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestOpenAttackObject` | 20 | zugeordnet | `0x0051F9A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketSelectDefenseGuild` | 40 | zugeordnet | `0x00521C40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestDefenseGuildList` | 40 | zugeordnet | `0x00521B70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestDefenseApplGuildList` | 46 | zugeordnet | `0x00521A60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestAttackApplGuildList` | 46 | zugeordnet | `0x00521950` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketAttackApplication` | 38 | zugeordnet | `0x00521880` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCancelDefenseApplication` | 38 | zugeordnet | `0x005217B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketDefenseApplication` | 38 | zugeordnet | `0x005216E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketSetNextSiegeWarTime` | 38 | zugeordnet | `0x00521610` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsGuildSiegeWarEntry` | 27 | zugeordnet | `0x00520450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetAttachTemplateData` | 5 | zugeordnet | `0x0051EEE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckCarveASeal` | 82 | zugeordnet | `0x00521F00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsAttackGuild` | 18 | zugeordnet | `0x0051FDA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsDefenseGuild` | 18 | zugeordnet | `0x0051FD50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemToAttackObject` | 26 | zugeordnet | `0x0051F840` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToAttackObject` | 44 | zugeordnet | `0x005213A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetAttachCharacterData` | 5 | zugeordnet | `0x0051EEB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetGuildWarPoint` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::GetGuildPoint |
| `GetGuildDuration` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::GetGuildPoint |
| `GetGuildArchon` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::GetGuildPoint |
| `GetGuildMasterLevel` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::GetGuildPoint; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetGuildTotalPoint` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::MakePacketGuildInfo; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetAttachGuildData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::GetGuildTotalPoint, AgpmSiegeWar::SortAttackGuild, AgpmSiegeWar::SortDefenseGuild |
| `GetSiegeWarMonsterType` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::RemoveDuplicateSiegeWarObject, AgcmSiegeWar::ClickCharacter, AgcmSiegeWar::CBInitCharacter |
| `GetSiegeWarMonsterType` | 13 | Kandidat unbestätigt | `0x00521EB0` | Aufrufer im Client: AgcmCharacter::RemoveDuplicateSiegeWarObject, AgcmSiegeWar::ClickCharacter, AgcmSiegeWar::CBInitCharacter; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetSiegeWarMonsterType` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCurrentStatus` | 48 | nicht im Client |  | Aufrufer nur im Server (12); kein Treffer im Binary |
| `SetStatusOff` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusProclaimWar` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusReady` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusStart` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusBreakASeal` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusOpenEyes` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusTimeOver` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusArchlordBattle` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetStatusTimeOverArchlordBattle` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetCurrentStatus; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetCallbackUpdateStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCarveAGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetNewOwner` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCastleInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetNextSiegeWarTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddDefenseApplication` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveDefenseApplication` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddAttackApplication` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveAttackApplication` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestAttackApplGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestDefenseApplGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveAttackApplGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveDefenseApplGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddAttackGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddDefenseGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestAttackGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestDefenseGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveAttackGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveDefenseGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveOpenAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseOpenAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveUseAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseUseAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveRepairAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseRepairAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveItemToAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemToAttackObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddItemResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCarveASeal` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStatusInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateReverseAttack` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSyncMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddArchlordCastleAttackGuild` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetCurrentSiegeWarType` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCurrentSiegeWarType` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCurrentStatus` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::IsGuildSiegeWarEntry; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetSiegeWarInfoIndex` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventSiegeWarNPC::GetSiegeWarInfo, AgpmEventTeleport::IsDisablePoint, AgpmSiegeWar::GetSiegeWarInfo |
| `GetSiegeWarInfoIndex` | 14 | Kandidat unbestätigt | `0x005204C0` | Aufrufer im Client: AgpmEventSiegeWarNPC::GetSiegeWarInfo, AgpmEventTeleport::IsDisablePoint, AgpmSiegeWar::GetSiegeWarInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSiegeWarByOwner` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::IsCastleOwnerGuildMember; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetSiegeWarInfo` | 13 | Kandidat unbestätigt | `0x00521EB0` | Aufrufer im Client: AgcmCharacter::RemoveDuplicateSiegeWarObject, AgcmEventEffect::StartEventEffect, AgcmUIWorldmap::GetCastleInfomation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSiegeWarInfo` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::RemoveDuplicateSiegeWarObject, AgcmEventEffect::StartEventEffect, AgcmUIWorldmap::GetCastleInfomation |
| `GetSiegeWarInfo` | 45 | Kandidat unbestätigt | `0x005205E0` | Aufrufer im Client: AgcmCharacter::RemoveDuplicateSiegeWarObject, AgcmEventEffect::StartEventEffect, AgcmUIWorldmap::GetCastleInfomation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetSiegeWarInfoOfGuild` | 23 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::GetSiegeWarInfoOfCharacter; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetSiegeWarInfoOfCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::CBIsInSiegeWarIngArea |
| `UpdateCarveAGuild` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetNewOwner` | 18 | nicht im Client |  | Aufrufer nur im Server (7); kein Treffer im Binary |
| `ReadSiegeInfo` | 87 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsRespawnMonster` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnOperationMessage` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::OnReceive |
| `CheckOpenAttackObjectEvent` | 53 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `CheckStartCondition` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `PayCostForUse` | 68 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SetNextSiegeWarTime` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::OnOperationSetNextSiegeWarTime; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsValidSiegeWarTime` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetNextSiegeWarTime; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `MakePacketCastleInfo` | 26 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketCastleInfoPacket` | 55 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::MakePacketCastleInfo; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `MakePacketCarveGuildInfo` | 39 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketResult` | 39 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketSiegeWarStatus` | 40 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketDefenseApplGuildList` | 66 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketCancelAttackApplication` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcmSiegeWar::SendCancelAttackApplication; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `MakePacketAttackApplGuildList` | 147 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketRequestAttackGuildList` | 40 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakePacketAttackGuildList` | 83 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakePacketDefenseGuildList` | 68 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `MakePacketGuildInfo` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::MakePacketDefenseApplGuildList, AgpmSiegeWar::MakePacketAttackApplGuildList, AgpmSiegeWar::MakePacketAttackGuildList; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `MakePacketResponseUseAttackObject` | 74 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketAddItemResult` | 21 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketStatusInfo` | 53 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketUpdateAttackObject` | 72 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakePacketUpdateReverseAttack` | 39 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSyncMessage` | 27 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `GetNextSiegeWarFirstTime` | 19 | Kandidat unbestätigt | `0x0051FC70` | Aufrufer im Client: AgcmUISiegeWar::SetComboBoxData, AgcmUISiegeWar::GetComboTime; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetFirstSiegeWarTime` | 18 | Kandidat unbestätigt | `0x0051FC70` | Aufrufer im Client: AgcmUISiegeWar::SetComboBoxData, AgcmUISiegeWar::GetComboTime; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsResurrectableInCastle` | 39 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetSiegeWar` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBGuildListToggle, AgpmCharacter::IsInSiege; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetSiegeWar` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsOwnerGuild` | 8 | Kandidat unbestätigt | `0x00521E10` | Aufrufer im Client: AgcmUIEventTeleport::CBSelectTeleportPoint, AgpmEventTeleport::IsDisablePoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsOwnerGuild` | 9 | Kandidat unbestätigt | `0x00521E10` | Aufrufer im Client: AgcmUIEventTeleport::CBSelectTeleportPoint, AgpmEventTeleport::IsDisablePoint; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetRepairCount` | 5 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetRepairCost` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::CheckValidRepairAttackObject |
| `GetRepairDuration` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::MakePacketUpdateAttackObject |
| `SetRepairStartTime` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `ReadSiegeWarObjectInfo` | 71 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckActiveCondition` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsSiegeWarMonster` | 10 | Kandidat unbestätigt | `0x00521EB0` | Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmCharacter::CBAddChar; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `StartCarveASeal` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CancelCarveASeal` | 10 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `EndCarveASeal` | 22 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetUseCharacterName` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsDoingSiegeWar` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateReverseAttack` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::UpdateCarveAGuild; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsEndArchlordSiegeWar` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::CBIsAttackableTime; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetArchlord` | 2 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `AddArchlordCastleAttackGuild` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::IsArchlordDungeonPoint; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetDayOfSiegeWar` | 61 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsDayOfSiegeWar` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetGuildTargetPosition` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetAttackGuildTargetPosition` | 63 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetGuildTargetPosition; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetDefenseGuildTargetPosition` | 34 | Kandidat unbestätigt | `0x00521D70` | Aufrufer im Client: AgpmSiegeWar::SetGuildTargetPosition; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `IsInSecretDungeon` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::OnReceive; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsCastleOwnerGuildMember` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsThisRegionCastleOwnerGuildMember` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::OnReceive; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsThisRegionCastleInSiegeWar` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmEventTeleport::OnReceive; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsSiegeWarRegion` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckGuildRequirement` | 30 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::CBApplicationDefense, AgcmUISiegeWar::CBApplicationAttack, AgpmSiegeWar::CheckApplicationRequirement; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `CheckApplicationRequirement` | 21 | Kandidat unbestätigt | `0x005205E0` | Aufrufer im Client: AgcmUISiegeWar::CBApplicationDefense, AgcmUISiegeWar::CBApplicationAttack, AgpmSiegeWar::OnOperationDefenseApplication; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsAlreadyApplGuild` | 33 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::AddDefenseApplicationGuild, AgpmSiegeWar::AddAttackApplicationGuild; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `AddDefenseApplicationGuild` | 36 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::OnOperationDefenseApplication; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `RemoveDefenseApplicationGuild` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::CBDestroyGuild, AgpmSiegeWar::OnOperationCancelDefenseApplication; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `AddAttackApplicationGuild` | 33 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::OnOperationAttackApplication, AgpmSiegeWar::AddArchlordCastleAttackGuild; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `RemoveAttackApplicationGuild` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::CBDestroyGuild, AgpmSiegeWar::OnOperationCancelAttackApplication; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SortAttackGuild` | 34 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SortDefenseGuild` | 34 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ResetAttackGuildTotalPoint` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::SortAttackGuild |
| `ResetDefenseGuildTotalPoint` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::SortDefenseGuild |
| `ResetGuildTotalPoint` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::ResetAttackGuildTotalPoint, AgpmSiegeWar::ResetDefenseGuildTotalPoint; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `CalcGuilPoint` | 29 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SortAttackGuild, AgpmSiegeWar::SortDefenseGuild; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetGuildPoint` | 29 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::CalcGuilPoint, AgpmSiegeWar::IsSamePoint; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `IsSamePoint` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearAttackGuild` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::SetStatusProclaimWar |
| `ClearDefenseGuild` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSiegeWar::SetStatusProclaimWar |
| `ClearAttackApplGuild` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetStatusProclaimWar; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `ClearDefenseApplGuild` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::SetStatusProclaimWar; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetAttackGuild` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::AddArchlordCastleAttackGuild; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SetDefenseGuild` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmSiegeWar::OnOperationSelectDefenseGuild; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |

## AgpmSkill (Kandidat unbestätigt 20, eingebaut 16, gemeinsamer Rumpf 29, nicht im Client 89, ohne Kandidat 62, zugeordnet 42)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsETCSkill` | 8 | zugeordnet | `0x00562730` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSelfBuffSkill` | 14 | zugeordnet | `0x005626C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsProductSkill` | 5 | zugeordnet | `0x00561D00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPassiveSkill_2` | 0 | zugeordnet | `0x00561CD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetSkillType` | 2266 | zugeordnet | `0x0052E510` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTooptipType` | 487 | zugeordnet | `0x00530CA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveOwnSkillList` | 25 | zugeordnet | `0x00563920` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRemoveSkill` | 23 | zugeordnet | `0x005629B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsDeadTarget` | 12 | zugeordnet | `0x00564C00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetWeaponDamageType` | 7 | zugeordnet | `0x005628A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSummonsTIDByItem` | 13 | zugeordnet | `0x00562850` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsEvolutionSkill` | 15 | zugeordnet | `0x005643B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsOwnSkill` | 36 | zugeordnet | `0x00564070` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnableSkill` | 6 | zugeordnet | `0x005649F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSufficientCost` | 104 | zugeordnet | `0x00561A70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTargetType` | 17 | zugeordnet | `0x00561720` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsVisibleEffectTypeSelfOnly` | 8 | zugeordnet | `0x005642F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSummonsSkill` | 17 | zugeordnet | `0x005642B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAttackSkill` | 2 | zugeordnet | `0x00564200` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPassiveSkill` | 5 | zugeordnet | `0x00563E10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckRequireClass` | 124 | zugeordnet | `0x00562340` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakeBasePacket` | 10 | zugeordnet | `0x0055C310` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSkillPoint` | 9 | zugeordnet | `0x005622C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSkillLevel` | 40 | zugeordnet | `0x00562240` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetAdjustCastDelay` | 15 | zugeordnet | `0x00561D60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidTarget` | 210 | zugeordnet | `0x00565AF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveUsePassiveList` | 27 | zugeordnet | `0x005637F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddUsePassiveList` | 23 | zugeordnet | `0x00563780` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckHaveAnySkill` | 36 | zugeordnet | `0x005636C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyTooltipTemplate` | 7 | zugeordnet | `0x00561200` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroySpecialize` | 10 | zugeordnet | `0x00561100` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroySkillTemplate` | 12 | zugeordnet | `0x005610A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateSkill` | 47 | zugeordnet | `0x00560FA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalUsedHeroicPoint` | 35 | zugeordnet | `0x005640E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetRange` | 76 | zugeordnet | `0x00563E40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateDIRT` | 45 | zugeordnet | `0x005620B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSatisfyRequirement` | 137 | zugeordnet | `0x00563AB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckTargetRestriction` | 41 | zugeordnet | `0x005639E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessRemove` | 28 | zugeordnet | `0x00566B10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateSkillPoint` | 60 | zugeordnet | `0x00563FA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBase` | 26 | zugeordnet | `0x00561450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetAttachSkillTemplateData` | 15 | zugeordnet | `0x00561260` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxSkill` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxSkillTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxSkillTooltipTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxSkillSpecializeTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxSkillRemove` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroySkill` | 16 | Kandidat unbestätigt | `0x00541580` | Aufrufer im Client: AgpmSkill::OnDestroy, AgpmSkill::RemoveSkill, AgpmSkill::ProcessRemove; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CreateSkillTemplate` | 74 | Kandidat unbestätigt | `0x00562C80` | Aufrufer im Client: AgpmGuild::AddGuildMarkTemplate, AgpmSkill::AddSkillTemplate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CreateSpecialize` | 17 | Kandidat unbestätigt | `0x00562C80` | Aufrufer im Client: AgpmSkill::AddSpecialize; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CreateTooltipTemplate` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::AddTooltipTemplate; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `DesAgpdSkillTemplateAttachData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::OnAddModule |
| `AddSkill` | 23 | Kandidat unbestätigt | `0x00563170` | Aufrufer im Client: AgcmSkill::CBLearnSkill, AgpmSkill::OnReceiveSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddSkill` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmSkill::CBLearnSkill, AgpmSkill::OnReceiveSkill |
| `RemoveSkill` | 42 | Kandidat unbestätigt | `0x00563170` | Aufrufer im Client: AgcmSkill::CBLearnSkill, AgcmSkill::CBForgetSkill, AgpmEventSkillMaster::CBRollbackSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmProductMed::CBActionSkillResult, AgcmProductMed::OnResult, AgcmSkill::ProcessReceiveCastSkill |
| `GetSkill` | 32 | Kandidat unbestätigt | `0x00564AB0` | Aufrufer im Client: AgcmProductMed::CBActionSkillResult, AgcmProductMed::OnResult, AgcmSkill::ProcessReceiveCastSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSkillLock` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::OnReceiveSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `InitSkill` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmSkill::CBLearnSkill, AgpmSkill::OnReceiveSkill |
| `InitSkillCoolTime` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::OnReceiveSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `AddSkillTemplate` | 37 | ohne Kandidat |  | Aufrufer im Client: AgpmGuild::AddGuildMarkTemplate, AgpmSkill::StreamReadTemplate; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `RemoveSkillTemplate` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::RemoveAllSkillTemplate; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `RemoveAllSkillTemplate` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadSkillTemplate; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetSkillTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIUseSkillEdit::OnInitDialog, AgcmAIUseSkillEdit::OnAiUseSkillAddButton, AgcmCharacter::_GetCurrentEvolutionSkillTemplate |
| `GetSkillTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIUseSkillEdit::OnInitDialog, AgcmAIUseSkillEdit::OnAiUseSkillAddButton, AgcmCharacter::_GetCurrentEvolutionSkillTemplate |
| `GetSkillTemplateSequence` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportSkillTemplate_; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `AddSpecialize` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::StreamReadSpecialize; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetSpecialize` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::RemoveSpecialize |
| `RemoveSpecialize` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddTooltipTemplate` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ReadSkillTooltipTxt; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetTooltipTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::SetSkillToolTipDescription, AgcmUISkill2::SetSkillToolTipCurrentLevel, AgcmUISkill2::SetSkillToolTipNextLevel |
| `RemoveTooltipTemplate` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachSkillData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::OnAddModule |
| `AttachSkillTemplateData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::OnAddModule, AgpmEventSkillMaster::OnAddModule |
| `AttachSpecializeData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::OnAddModule |
| `SetSkillStatus` | 11 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `CBUpdateSkillPoint` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::OnAddModule, AgcmUIProductSkill::OnAddModule, AgcmUISkill2::OnAddModule; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `CBUpdateLevel` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnAddModule, AgpmSkill::OnAddModule; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `CBInitCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmGuild::OnAddModule, AgcmRide::OnAddModule |
| `GetBaseLock` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OnReceiveAddBuffedList` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::ProcessBuffedSkillPacket, AgpmSkill::OnReceiveSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `SetCallbackInitSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitSkillTemplate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveAction` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveActionResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveRealHit` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveAdditionalEffect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckNowUpdateActionFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackChangeStatus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddBuffedList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveBuffedList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDeleteSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateSkillPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateDIRTPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetInputTotalCostSP` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetInputTotalCostHeroicPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLearnSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackForgetSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetConstFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateSkillExp` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitSpecialize` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckSkillPvP` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRollbackSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackModifiedSkillLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetModifiedSkillLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInitCoolTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSpecificSkillLevel` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `AddBuffedList` | 38 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::OnReceiveAddBuffedList; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `RemoveBuffedList` | 16 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::OnReceiveSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `RemoveBuffedListByIndex` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::RemoveBuffedList; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetBuffedList` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::SetBuffedAttackEffect; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetBuffedSkillCount` | 22 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsBuffedSkillByTID` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AddDefaultSkillTID` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveDefaultSkillTID` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CleanDefaultSkillTID` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddUseList` | 23 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `RemoveUseList` | 27 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckSkillInUseList` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddOwnSkillList` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::OnReceiveSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `CheckSkillPvP` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmSkill::CastSkillCheck, AgcmSkill::CastSkill |
| `GetCostHP` | 29 | Kandidat unbestätigt | `0x00561950` | Aufrufer im Client: AgpmSkill::IsSufficientCost; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetCostSP` | 29 | Kandidat unbestätigt | `0x00561950` | Aufrufer im Client: AgpmSkill::IsSufficientCost; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetCostMP` | 35 | Kandidat unbestätigt | `0x00561950` | Aufrufer im Client: AgpmSkill::IsSufficientCost; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetCostArrow` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSufficientCost; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsPassiveSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CBInitSkill, AgcmSkill::CBRemoveSkill, AgcmUISkill2::IsUsableSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsActionPassiveSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsActionPassiveSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsCriticalUpPassiveSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsNormalAttack` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::GetTotalSkillPoint; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetCastDelay` | 35 | ohne Kandidat |  | Aufrufer im Client: AgpmAI2::SetSkill, AgpmSkill::GetSkillDurationTime; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetCastDelay` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmAI2::SetSkill, AgpmSkill::GetSkillDurationTime |
| `GetRecastDelay` | 21 | Kandidat unbestätigt | `0x00561DE0` | Aufrufer im Client: AgcmItem::CheckReUseInterval, AgcmUIItem::SetUseItemTime, AgpmAI2::SetSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetRecastDelay` | 22 | Kandidat unbestätigt | `0x00561DE0` | Aufrufer im Client: AgcmItem::CheckReUseInterval, AgcmUIItem::SetUseItemTime, AgpmAI2::SetSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAdjustRecastDelay` | 15 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetSemiRecastDelay` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkillDurationTime` | 85 | nicht im Client |  | Aufrufer nur im Server (16); kein Treffer im Binary |
| `GetSkillInterval` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::GetSkillDurationTime; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetModifiedSkillDurationTime` | 107 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::GetSkillDurationTime; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetTargetArea1` | 48 | Kandidat unbestätigt | `0x00561E30` | Aufrufer im Client: AgcmSkill::CastSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `GetTargetArea2` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetMaxInputSkillPoint` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddSkillPoint` | 34 | Kandidat unbestätigt | `0x005649A0` | Aufrufer im Client: AgpmSkill::OnReceiveSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |
| `SubtractSkillPoint` | 16 | Kandidat unbestätigt | `0x005649A0` | Aufrufer im Client: AgpmSkill::OnReceiveSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `UpdateSkillLevelAndExp` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmProduct::AddSkillExp, AgpmProduct::SetSkillLevel; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetSkillExp` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmProduct::AddSkillExp, AgpmProduct::GetExpOfCurrLevel; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `SetSkillPoint` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSkillExp` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmProduct::AddSkillExp, AgpmProduct::SetSkillLevel; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `CheckLearnableSkill` | 64 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::CheckLearnSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetTotalSkillPoint` | 56 | Kandidat unbestätigt | `0x00564AB0` | Aufrufer im Client: AgcmUISkill2::SetSkillToolTipBuyCost, AgpmEventSkillMaster::CheckLearnHighLevelSkill, AgpmEventSkillMaster::CheckUpgradeHighLevelSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 13, Belegarten 2) |
| `IsWantedRaceClassSkill` | 121 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSkillMaster::_CheckConditionC, AgpmSkill::GetTotalSkillPoint; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `LearnSkill` | 6 | nicht im Client |  | Aufrufer nur im Server (8); kein Treffer im Binary |
| `LearnSkill` | 12 | nicht im Client |  | Aufrufer nur im Server (8); kein Treffer im Binary |
| `ForgetSkill` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `ForgetSkill` | 5 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsStatusActionOnActionType4` | 12 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetTimeBuffType` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::SetSkillToolTipFactorPoint; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `ChangeSkillTemplateName` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetDivideDMGNumForShow` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CBActionSkillResult; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetDivideDMGNumForShow` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmSkill::CBActionSkillResult |
| `GetDivideDMGNumForShow` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CBActionSkillResult |
| `IsAttackSkill` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUISkill2::IsUsableSkill, AgpmPvP::IsSkillEnable; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsAreaSkill` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::IsSkillEnable; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsDebuffSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::IsUsableSkill, AgpmSkill::GetModifiedSkillDurationTime; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsDurationByDistanceSkill` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBUpdateAlarmGrid; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsDurationUnlimited` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBUpdateAlarmGrid; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsTameSkill` | 10 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `IsFixedSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `IsTransparentSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsNotAddAgroAtCast` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsATFieldAttackSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsMutationSkill` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsReleaseTargetSkill` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsSubCashItemStackCountOnSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsGameBonusExpSkill` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsGameBonusMoneySkill` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsCashSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsLevelDiffSkill` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsUnlimitedTargetSiegeWarSkill` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkillCheck, AgcmSkill::CastSkill, AgpmSkill::IsValidTarget; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsUnlimitedTargetRaceSkill` | 11 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsPartySkill` | 11 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsInvolveParentRegionSkill` | 15 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsSphereRangeSiegeWarSkill` | 11 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsValidTarget; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsSummonsSkillForSiegeWar` | 11 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsDetectSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmPvP::IsSkillEnable, AgpmSkill::GetDetectType; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsRideSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkillCheck, AgcmSkill::CastSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsArchlordSkill` | 9 | Kandidat unbestätigt | `0x00563210` | Aufrufer im Client: AgcmUISkill2::CBSetSelfCharacter, AgcmUISkill2::CBAddSkill, AgcmUISkill2::CBRemoveSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsGroundTargetSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkillCheck, AgcmSkill::CastSkill, AgpmSkill::IsValidTarget; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsDOTSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::GetSkillDurationTime; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `IsSleepSkill` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsDispelAllBuffSkill` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsForceSkill` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsForceSetSkill` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsForceCastSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsForceTransparentSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsResurrectionSkill` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsSkillUnionType1` | 11 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsSkillUnionType2` | 11 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsMovePosTarget` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsMovePosSelf` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsTransformSkill` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsBattleGroundRaceSkill` | 23 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetActionOnActionType` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, AgpmPvP::IsAttackSkill, AgpmSkill::IsNotAddAgroAtCast; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetSummonsType` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::IsSummonsSkillForSiegeWar; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetDetectType` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetSkillLevelUpType` | 8 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetSkillByAction` | 70 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::SetActionResultSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetRandomCreatureTID` | 19 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetBonusExpRate` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetBonusMoneyRate` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetBonusCharismaRate` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkillByTID` | 18 | Kandidat unbestätigt | `0x00564630` | Aufrufer im Client: AgcmCharacter::SendCancelEvolution, AgcmProductMed::CBPreProcessSkill, AgcmSkill::PreProcessSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetModifiedHitRate` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetModifiedBlockRate` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetModifiedHPRegen` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetModifiedMPRegen` | 7 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetModifiedSkillLevel` | 9 | Kandidat unbestätigt | `0x00563210` | Aufrufer im Client: CUiCharacterProperty::_GetZeroBasePropertyByPassive, CUiCharacterProperty::_GetZeroBasePropertyByBuff, AgcmUISkill2::CBDisplaySkillLevel; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddEventSkillTID` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsCharacterConfigSkill` | 9 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetSkillTemplateDurationTime` | 11 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetCharacterSkillRoleType` | 32 | ohne Kandidat |  | Aufrufer im Client: AgpmCombat::GetHeroicResistanceByHeroicClass, AgpmCombat::GetHeroicResistanceByAttackerHeroicClass; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakeActionPacket` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::MakeCastPacket, AgpmSkill::MakeCastResultPacket; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakeCastPacket` | 51 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SendCancelEvolution, AgcmSkill::CastSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakeCastResultPacket` | 33 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketRealHit` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CBProcessTwicePacketSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakePacketAdditionalEffect` | 23 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketBuffedList` | 74 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSkillRemove` | 25 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketAllBuffedList` | 62 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSkill` | 45 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::MakeBufferCharAllSkill; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakePacketSkillDIRT` | 33 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketUpdateSkillPoint` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::UpdateSkillPoint; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakePacketUpdateDIRTPoint` | 48 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::UpdateDIRTPoint; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakePacketOperation` | 23 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketRequestRollback` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::SendRequestRollback; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `MakePacketModifiedSkillLevel` | 27 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketInitCoolTime` | 27 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacketSpecificSkillLevel` | 23 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `AdjustSkillPoint` | 57 | Kandidat unbestätigt | `0x00563170` | Aufrufer im Client: AgpmEventSkillMaster::CBRollbackSkill, AgpmEventSkillMaster::InitializeSkillTree; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `AdjustHeroicPoint` | 58 | Kandidat unbestätigt | `0x00563170` | Aufrufer im Client: AgpmEventSkillMaster::CBRollbackSkill, AgpmEventSkillMaster::InitializeSkillTree; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `CheckOwnerSP` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWriteTemplate` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `StreamReadTemplate` | 57 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::StreamReadTemplate, AgcmCharacter::StreamReadTemplateAnimation, AgcmCharacter::StreamReadTemplateCustomize; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `StreamWriteSpecialize` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadSpecialize` | 35 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSkillConstTxt` | 209 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSkillConst2Txt` | 154 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSkillSpecTxt` | 82 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSkillTooltipTxt` | 94 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSkillConstCreatureTID` | 30 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ReadSkillConstTxt; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `ReadSkillConstAdditionalSkillTID` | 33 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ReadSkillConstTxt; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `ReadSkillConstLevelUpSkillTID` | 30 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ReadSkillConst2Txt; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `GetConstFactorIndex` | 496 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ReadSkillConstTxt, AgpmSkill::ReadSkillConst2Txt; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `SetSpecialStatus` | 109 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::SetSkillType; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |
| `ConvertFactorMagnifyIndex` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmSkill::ReadSkillConstTxt; kein unbenannter Kandidat mit Beleg unter 404 unbenannten Funktionen im Klassenbereich |

## AgpmStartupEncryption (gemeinsamer Rumpf 9, nicht als eigene Funktion 1, nicht im Client 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakeStartupPacket` | 9 | zugeordnet | `0x0056C960` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnReceiveAlgorithmType` | 10 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmStartupEncryption::OnReceive; im Adressbereich der Klasse (0x0056C7E0–0x0056C9E0) ist keine unbenannte Funktion mehr übrig |
| `SetCallbackAlgorithmType` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestPublic` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPublic` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMakePrivate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackComplete` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckComplete` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDynCodePublic` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDynCodePrivate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CheckCompleteStartupEncryption` | 4 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |

## AgpmSummons (Kandidat unbestätigt 2, gemeinsamer Rumpf 8, nicht im Client 18, ohne Kandidat 16, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetMaxSummonsCount` | 15 | zugeordnet | `0x00584270` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsMySummons` | 18 | zugeordnet | `0x00584C80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `NewFixed` | 57 | zugeordnet | `0x00584AB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `NewTaming` | 58 | zugeordnet | `0x005848E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `NewSummons` | 67 | zugeordnet | `0x00585990` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetADCharacter` | 9 | zugeordnet | `0x00584110` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnIdle2` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnReceiveSetMaxTame` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::OnReceive; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `SetOwnerAndLifeTime` | 21 | Kandidat unbestätigt | `0x00584470` | Aufrufer im Client: AgpmSummons::NewSummons, AgpmSummons::NewTaming, AgpmSummons::NewFixed; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveSummons` | 69 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::OnReceiveRemoveSummons; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `RemoveSummonsInOwner` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::RemoveSummons; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `RemoveTameInOwner` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::RemoveSummons; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `RemoveFixedInOwner` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::RemoveSummons; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `RemoveOwner` | 14 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::RemoveSummons; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `IsSummonsEnable` | 33 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `IsSummonsEnableRegion` | 30 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::UpdateAllSummonsPosToOwner; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `GetSummonsCount` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::NewSummons, AgpmSummons::IsSummonsEnable; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `GetMaxSummonsCount` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::IsSummonsEnable; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `AddMaxSummonsCount` | 13 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `GetSummonsTIDCount` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `UpdateAllSummonsPosToOwner` | 63 | nicht im Client |  | Aufrufer nur im Server (7); kein Treffer im Binary |
| `IsTameEnable` | 37 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetTameCount` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::NewTaming, AgpmSummons::IsTameEnable; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `GetMaxTameCount` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::IsTameEnable; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `SetMaxTameCount` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::OnReceiveSetMaxTame; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `GetTameTIDCount` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsFixedEnable` | 17 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetAllFixedCount` | 13 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::NewFixed, AgpmSummons::IsFixedEnable; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `GetEachFixedCount` | 25 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetMaxFixedCount` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFixedTIDCount` | 19 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetOwnerCID` | 13 | Kandidat unbestätigt | `0x00584320` | Aufrufer im Client: AgcmCharacter::CBUpdatePosition, AgpmPvP::IsSkillEnable, AgpmSummons::IsTameEnable; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsPet` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetPropensity` | 13 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetPropensity` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::OnReceiveSetPropensity; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `GetSummonsCIDByTID` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakePacket` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmAuction::SendSelect, AgcmAuction::SendSell, AgcmAuction::SendCancel; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |
| `MakeNewSummonsPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeRemoveSummonsPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeSetPropensityPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeSetMaxSummonsPacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `MakeSetMaxTamePacket` | 6 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackNewSummons` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveSummons` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetPropensity` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetMaxSummons` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetMaxTame` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveSummonsByLevelLimitRegion` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetItemSummonsCount` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmSummons::IsSummonsEnable; kein unbenannter Kandidat mit Beleg unter 35 unbenannten Funktionen im Klassenbereich |

## AgpmSystemMessage (Kandidat unbestätigt 2, gemeinsamer Rumpf 6, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 7 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle2` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnReceive` | 25 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `ProcessSystemMessage` | 14 | Kandidat unbestätigt | `0x0057C210` | Aufrufer im Client: AgcmItem::UnuseItem, AgcmUIAuction::CBBuyItemFromAuction, AgcmUIAuction::CBSellUI; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ProcessSystemMessage` | 12 | Kandidat unbestätigt | `0x0057C210` | Aufrufer im Client: AgcmItem::UnuseItem, AgcmUIAuction::CBBuyItemFromAuction, AgcmUIAuction::CBSellUI; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `MakeSystemMessagePacket` | 12 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `MakeSystemMessagePacketWithType` | 12 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackSystemMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmTax (Kandidat unbestätigt 6, eingebaut 1, gemeinsamer Rumpf 4, nicht im Client 4, ohne Kandidat 5, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsCastleOwner` | 12 | zugeordnet | `0x00577DF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCastle` | 9 | zugeordnet | `0x00577DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetRegion` | 10 | zugeordnet | `0x00577A00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketEventRequest` | 22 | zugeordnet | `0x00578FC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationEventRequest` | 28 | zugeordnet | `0x005778D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationEventGrant` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `GetTax` | 12 | Kandidat unbestätigt | `0x00578070` | Aufrufer im Client: AgcmUITax::GetTax, AgcmUITax::GetRegionTax, AgcmUITax::CBClickReset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetTax` | 14 | Kandidat unbestätigt | `0x00578070` | Aufrufer im Client: AgcmUITax::GetTax, AgcmUITax::GetRegionTax, AgcmUITax::CBClickReset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetTax` | 10 | Kandidat unbestätigt | `0x00578070` | Aufrufer im Client: AgcmUITax::GetTax, AgcmUITax::GetRegionTax, AgcmUITax::CBClickReset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetRegionTax` | 12 | Kandidat unbestätigt | `0x00578070` | Aufrufer im Client: AgcmUITax::CBDisplayRegion1, AgcmUITax::CBDisplayRegion2, AgcmUITax::CBDisplayRegion3; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `UpdateCastleTax` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUITax::UpdateTax; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `UpdateRegionTax` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmUITax::UpdateTax, AgpmTax::OnReceive; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `GetTaxRatio` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUICustomizing::PriceWithTax, AgcmUIGuild::CBMainToggle, AgcmUIGuild::CBDisplayGuildMarkInfo; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `GetTaxRatio` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUICustomizing::PriceWithTax, AgcmUIGuild::CBMainToggle, AgcmUIGuild::CBDisplayGuildMarkInfo; kein unbenannter Kandidat mit Beleg unter 18 unbenannten Funktionen im Klassenbereich |
| `GetTaxRatioArchlordCastle` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUITax::CBDisplayViewRatio5, AgcmUITax::CBDisplayIncome5 |
| `GetRegionIndex` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsValidRatio` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsValidDate` | 41 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `ParseCastleTax` | 18 | Kandidat unbestätigt | `0x00577AD0` | Aufrufer im Client: AgpmTax::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `ParseRegionTax` | 19 | Kandidat unbestätigt | `0x00577AD0` | Aufrufer im Client: AgpmTax::OnReceive; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `MakePacketEventGrant` | 21 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `SetCallbackEventRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackModifyRatio` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackInquireTax` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmTimer (eingebaut 14, gemeinsamer Rumpf 3, nicht als eigene Funktion 1, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackCheckHour` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetYear` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, AgpmEventNature::GetYear, CProgressDlg::ProcessAddFile |
| `GetMonth` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, AgpmEventNature::GetMonth, CProgressDlg::ProcessAddFile |
| `GetDay` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip, AgpmEventNature::GetDay, AgpmTimer::GetMonth |
| `GetHour` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce |
| `GetMinute` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce, AgcmEventNature::ApplySkySetting |
| `GetSecond` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventNature::GetSecond, CProgressDlg::ProcessAddFile, CProgressDlg::DirectoryCopy |
| `GetMS` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventNature::GetMS |
| `IsPM` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmEventNature::IsPM |
| `GetDayTimeDWORD` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventNature::GetDayTimeDWORD |
| `GetHourTimeDWORD` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce, AgpmEventNature::GetHourTimeDWORD |
| `SetSpeedRate` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgpmEventNature::SetSpeedRate |
| `ConvertRealtoGameTime` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventNature::ConvertRealtoGameTime |
| `ConvertGametoRealTime` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmEventNature::ConvertGametoRealTime |
| `SetTime` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmEventNature::OnInit, AgcmEventNature::OnIdle, AgcmEventNature::SetTime |
| `SetTime` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::OnInit, AgcmEventNature::OnIdle, AgcmEventNature::SetTime; im Adressbereich der Klasse (0x0051C440–0x0051C500) ist keine unbenannte Funktion mehr übrig |
| `MakePacketTime` | 7 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |

## AgpmTitle (eingebaut 11, gemeinsamer Rumpf 1, nicht im Client 15, ohne Kandidat 15, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CheckItemCount` | 20 | zugeordnet | `0x00568830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SatisfyTitleQuestCompleteCondition` | 16 | zugeordnet | `0x00568780` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsGuildMaster` | 9 | zugeordnet | `0x005687E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMaxTitleTemplate` | 7 | zugeordnet | `0x00568450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetTitleTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_CheckIsValidTitleRequirement, AgpmTitle::OnOperationTitleAddResult, AgpmTitle::OnOperationTitleUseResult |
| `OnOperationTitleQuestRequestResult` | 35 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::OnOperationTitleQuest; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `OnOperationTitleQuestCheckResult` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::OnOperationTitleQuest; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `OnOperationTitleQuestCompleteResult` | 27 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::OnOperationTitleQuest; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `OnOperationTitleQuestListResult` | 55 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::OnOperationTitleQuest; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `SatisfyTitleQuestRequireCondition` | 129 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CheckSameItemGroup` | 36 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetGroupItemCount; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetGroupItemCount` | 25 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetItemCountFromCharacter; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetItemCountFromCharacter` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetEffectValue` | 24 | nicht im Client |  | Aufrufer nur im Server (7); kein Treffer im Binary |
| `GetFactorItemOptionValue` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetItemOptionValue` | 12 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetCharacterStatusByItem; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetCharacterStatusByItem` | 36 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetCharacterStatusItemAndInitialValue; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetInitialCharacterStatus` | 22 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetCharacterStatusItemAndInitialValue; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetProductSkillLevel` | 18 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetTitleQuestCheckValueInStatus; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetCharacterStatusItemAndInitialValue` | 10 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::GetTitleQuestCheckValueInStatus; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetTitleQuestCheckValueInStatus` | 41 | nicht im Client |  | Aufrufer nur im Server (4); kein Treffer im Binary |
| `GetHaveTitleNumber` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `SetTitleQuestCheckValue` | 22 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `TitleUse` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::OnOperationTitleUseResult; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `TitleUnUse` | 19 | ohne Kandidat |  | Aufrufer im Client: AgpmTitle::OnOperationTitleUseResult; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `SetCallBackTitleAdd` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleUse` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleList` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleUseNear` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleUIOpen` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleQuestRequest` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleQuestCheck` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleQuestComplete` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleQuestList` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleAddResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleUseResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleListResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleQuestRequestResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleQuestCheckResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleQuestCompleteResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleQuestListResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `SetCallBackTitleDelete` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallBackTitleDeleteResult` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::_RegisterCallBack |
| `StreamReadTitleDataTemplate` | 115 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnInitialize; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `StreamReadTitleStringTemplate` | 53 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnInitialize; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |

## AgpmUIStatus (gemeinsamer Rumpf 6, nicht im Client 4, ohne Kandidat 1, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MakePacketUpdateViewHelmetOption` | 19 | zugeordnet | `0x0057DD80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketUpdateQuickBeltItem` | 44 | zugeordnet | `0x0057DC40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 5 | zugeordnet | `0x0057DC10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `MakePacketWholeQuickBeltInfo` | 37 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `MakePacketQBeltString` | 20 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OnOperationUpdateViewHelmetOption` | 9 | ohne Kandidat |  | Aufrufer im Client: AgpmOptimizedPacket2::ProcessCharacterPacket, AgpmUIStatus::OnReceive; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetCallbackAddQuickBeltInformation` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateQuickBeltItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceivedEncodedQBeltString` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateViewHelmetOption` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetQBeltEncodedString` | 25 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `SetCooldownEncodedString` | 19 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |

## AgpmWantedCriminal (Kandidat unbestätigt 3, eingebaut 4, gemeinsamer Rumpf 9, nicht im Client 9, ohne Kandidat 3, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetFinalAttacker` | 4 | zugeordnet | `0x0056B950` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketEventRequest` | 20 | zugeordnet | `0x0056C1C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateWantedCriminal` | 9 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `DestroyWantedCriminal` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgpmWantedCriminal::OnDestroy |
| `SetMaxWantedCriminal` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddWantedCriminal` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `RemoveWantedCriminal` | 5 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `GetWantedCriminal` | 6 | nicht im Client |  | Aufrufer nur im Server (15); kein Treffer im Binary |
| `GetWantedCriminal` | 5 | nicht im Client |  | Aufrufer nur im Server (15); kein Treffer im Binary |
| `GetCAD` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIItem::CBSalesBox2Add, AgcmUIItem::CBSalesBox2ClickCancelCompleteButton, AgcmUIItem::GetSalesOfIndex |
| `OnOperationEventRequest` | 28 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `OnOperationEventGrant` | 7 | ohne Kandidat |  | Aufrufer im Client: AgpmEventSiegeWarNPC::OnReceive, AgpmGamble::OnReceive, AgpmRemission::OnReceive; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `IsEnoughBaseBounty` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWantedCriminal::CBClickArrange1OK, AgcmUIWantedCriminal::CBClickArrange2OK, AgcmUIWantedCriminal::CBClickArrange3OK |
| `IsEnoughBounty` | 10 | Kandidat unbestätigt | `0x0056BD20` | Aufrufer im Client: AgcmUIWantedCriminal::CBClickArrange2OK, AgcmUIWantedCriminal::CBClickArrange3OK, AgpmWantedCriminal::IsEnoughBaseBounty; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetFinalAttacker` | 7 | Kandidat unbestätigt | `0x0056BC70` | Aufrufer im Client: AgcmUIWantedCriminal::OpenArrange, AgcmUIWantedCriminal::CBResultArrange, AgcmUIWantedCriminal::CBClickArrange3OK; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `IsFinalAttacker` | 10 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetBaseBounty` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIWantedCriminal::CBResultArrange, AgcmUIWantedCriminal::CBClickArrange1OK, AgcmUIWantedCriminal::CBClickArrange2OK |
| `GetBaseBounty` | 16 | Kandidat unbestätigt | `0x0056BD20` | Aufrufer im Client: AgcmUIWantedCriminal::CBResultArrange, AgcmUIWantedCriminal::CBClickArrange1OK, AgcmUIWantedCriminal::CBClickArrange2OK; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `MakePacketWC` | 12 | nicht im Client |  | Aufrufer nur im Server (2); kein Treffer im Binary |
| `ParsePacketWC` | 21 | ohne Kandidat |  | Aufrufer im Client: AgpmWantedCriminal::OnReceive; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `MakePacketEventGrant` | 19 | nicht im Client |  | Aufrufer nur im Server (14); kein Treffer im Binary |
| `SetCallbackEventRequest` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEventGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackArrange` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMyRank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateKiller` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateFlag` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackNotify` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmWarInfo (gemeinsamer Rumpf 11)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackUpdateWarState` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRequestWarInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateTimeInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateAddInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateCharacterPvPInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateRacePvPInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEndWar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackFactor` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmWorld (eingebaut 1, gemeinsamer Rumpf 6, nicht im Client 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `_CreateWorldData` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_DestroyWorldData` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmWorld::OnDestroy |
| `SetCallbackUpdateWorld` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResultGetWorldAll` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetWorld` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetCharacterCount` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResultGetCharacterCount` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `_OnResultGetWorldAll` | 27 | ohne Kandidat |  | Aufrufer im Client: AgpmWorld::OnReceive; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## ApmEventManager (Kandidat unbestätigt 3, eingebaut 7, gemeinsamer Rumpf 4, nicht im Client 5, ohne Kandidat 16, zugeordnet 10)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RegisterPacketFunction` | 10 | zugeordnet | `0x0055CFA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EventConstructor` | 2 | zugeordnet | `0x0055C3F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckValidRange` | 9 | zugeordnet | `0x0055C380` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamRead` | 118 | zugeordnet | `0x0055CA90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetEventData` | 59 | zugeordnet | `0x0055C5F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEvent` | 92 | zugeordnet | `0x0055C4B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `EventDestructor` | 15 | zugeordnet | `0x0055D290` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetEventFromBasePacket` | 26 | zugeordnet | `0x0055D900` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InitObject` | 49 | zugeordnet | `0x0055CE80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBase` | 27 | zugeordnet | `0x0055C130` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetCondition` | 30 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBChargingInventoryAMoveItem, AgcmUIItem::CBChargingInventoryBMoveItem, AgcmUIItem::CBInventoryMoveItem; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `DestroyCondition` | 17 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::CopyCondition, ApmEventManager::RemoveEvent; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `CopyCondition` | 37 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::InitObject; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetRandomPos` | 108 | ohne Kandidat |  | Aufrufer im Client: AgpmEventBinding::GetBindingPositionForResurrection, AgpmEventBinding::GetBindingPositionForNewCharacter, AgpmEventBinding::GetBindingPositionForSiegeWarResurrection; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetRandomPos` | 42 | ohne Kandidat |  | Aufrufer im Client: AgpmEventBinding::GetBindingPositionForResurrection, AgpmEventBinding::GetBindingPositionForNewCharacter, AgpmEventBinding::GetBindingPositionForSiegeWarResurrection; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetRandomPos4MobWander` | 75 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetAreaCharacters` | 57 | ohne Kandidat |  | Aufrufer im Client: AgpmEventFactors::ProcessUpdateEventFactors; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetAreaCharacters` | 55 | ohne Kandidat |  | Aufrufer im Client: AgpmEventFactors::ProcessUpdateEventFactors; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetTargetFactorCharacters` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmEventFactors::ProcessUpdateEventFactors; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetTargetItemCharacters` | 24 | ohne Kandidat |  | Aufrufer im Client: AgpmEventFactors::ProcessUpdateEventFactors; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `IsTargetFactorCharacter` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: ApmEventManager::GetTargetFactorCharacters |
| `IsTargetItemCharacter` | 40 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::GetTargetItemCharacters; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `IsActiveSkillTIme` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsEndSkillTIme` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnIdle` | 6 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `EventConstructor` | 18 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::CBEventConstructorCharacter, ApmEventManager::CBEventConstructorCharacterTemplate, ApmEventManager::CBEventConstructorItem; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `SetMaxEvent` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsRegistered` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: ApmEventListDlg::OnInitDialog |
| `AddEvent` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddEvent, AgcmMinimap::OnAddModule |
| `GetEventSquence` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `GetEvent` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBOnRemoveObject |
| `GetEvent` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBOnRemoveObject |
| `GetEvent` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBOnRemoveObject |
| `GetEvent` | 21 | Kandidat unbestätigt | `0x0055D8C0` | Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBOnRemoveObject; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `CheckEventAvailable` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::CBEventObjectOnly; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `RemoveEvent` | 35 | ohne Kandidat |  | Aufrufer im Client: ApmEventManager::EventDestructor, ApmEventListDlg::OnEventAdd, ApmEventListDlg::OnEventRemove; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `RemoveEvent` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApmEventManager::EventDestructor, ApmEventListDlg::OnEventAdd, ApmEventListDlg::OnEventRemove |
| `GetBasePos` | 67 | Kandidat unbestätigt | `0x0055C2D0` | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUIEventItemConvert::CBReceiveGrant, AgcmUIQuest2::StartAnimation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `GetBasePos` | 9 | Kandidat unbestätigt | `0x0055C2D0` | Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill, AgcmUIEventItemConvert::CBReceiveGrant, AgcmUIQuest2::StartAnimation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `StreamWrite` | 86 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `MakeBasePacket` | 30 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNPCTrade::MakeBasePacket, AgcmEventNPCTrade::SendBuy, AgcmEventNPCTrade::SendSell; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `MakePacketEventData` | 26 | ohne Kandidat |  | Aufrufer im Client: AgpmEventItemRepair::CBEmbeddedMakeEventPacket, AgpmEventNPCDialog::CBMakePacketEventData, AgpmEventProduct::CBEmbeddedPacketEncode; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `SetCallbackInitObject` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddEvent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
