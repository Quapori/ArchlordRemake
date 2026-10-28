# AgcmUICharacter (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUICharacter` (Charakter-Fenster, Ziel-Anzeige, Wiederbelebung, Buff-Liste, Minimap-Marker) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmUICharacter`. Alle Adressen gelten nur für den 2017er Build; die Klasse erbt zusätzlich `CUiCharacterProperty` (eigene Quelldatei, nicht Teil dieser Analyse).

## Kernbefund

- **Abdeckung:** 88 von 122 Quellmethoden sind zugeordnet. 25 davon ergeben sich aus der Callback-Registrierung in `OnAddModule`, 13 aus dem Aufrufgraphen, weitere aus Zeichenketten und UI-Registrierungen; die graphbasierten und die Registrierungs-Zuordnungen wurden gegen das Dekompilat gelesen.
- **Client → Server:** Die Wiederbelebungsanfragen senden `AGPMCHAR_PACKET_OPERATION_REQUEST_RESURRECTION_TOWN` (9), `…SIEGE_INNER` (19), `…SIEGE_OUTER` (20) und `RESURRECTION_BY_OTHER` (24) mit denselben Werten wie die EP8-Quelle; die Operation 10 (`…_NOW`) ist im Binary nicht zugeordnet.
- **UI-Anzeigen:** Alle 61 Charakter-Anzeigen (Name und ID, 0 bis 0x3C und weitere) sind identisch zur Quelle; die Anzeigenamen sind teils koreanisch (Codepage 949) und stehen in der Tabelle „UI-Namen“. 27 UI-Funktionen und 3 Boolean-Werte stimmen ebenfalls.
- **Callbacks:** Die drei Callback-IDs `AGCMUICHAR_CB_*` (0, 1, 2) stimmen mit der Quelle überein; die Registrierungen bei den Charakter-, Item-, Skill- und Summons-Modulen stehen in gleicher Reihenfolge wie in der Quelle.
- **Verhalten:** `CBUpdatePosition`, `CharacterBlockByPenalty`, `SetEditTextType1/4`, die Wiederbelebungsfunktionen, `SetCharacter`/`ReleaseCharacter`, die Ziel- und Buff-Funktionen sowie `OnHideBlindEquipSlot` folgen der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUICharacter.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00625C80` | 1501 | Zeichenketten/Konstanten (geprüft) |
| 1 | `OnDestroy` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 2 | `OnInit` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 3 | `OnIdle` | `0x0061E810` | 605 | Zeichenkette |
| 4 | `CBConstBase` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 5 | `CBDestBase` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 6 | `CBDesCharTemplate` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 7 | `AddEvent` | `0x006218E0` | 2236 | Zeichenkette |
| 8 | `AddFunction` | `0x00625080` | 1152 | Zeichenkette |
| 9 | `AddDisplay` | `0x00625500` | 1916 | Zeichenkette |
| 10 | `AddUserData` | `0x006221A0` | 389 | Zeichenkette |
| 11 | `AddDisplay` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 12 | `AddDisplay` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 13 | `AddUserData` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 14 | `AddBoolean` | `0x00622330` | 98 | Zeichenkette |
| 15 | `SetCharacter` | `0x00624880` | 190 | Aufrufgraph (geprüft) |
| 16 | `ReleaseCharacter` | `0x00624940` | 60 | Aufrufgraph (geprüft) |
| 17 | `CharacterStatusCB` | `0x006223A0` | 170 | UI-Registrierung |
| 18 | `CBTargetCharName` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 19 | `CBDisplayMessageData` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 20 | `CBTargetAttributeType` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 21 | `CharacterUpdateFactorCB` | `0x00624980` | 225 | cbreg:AgcmUICharacter |
| 22 | `CharacterLevelUp` | `0x0061F030` | 228 | cbreg:AgcmUICharacter |
| 23 | `CharacterUpdateFactorBonusExpCB` | `0x0061F120` | 328 | cbreg:AgcmUICharacter |
| 24 | `CharacterUpdateFactorMurdererPointCB` | `0x00624A70` | 361 | cbreg:AgcmUICharacter |
| 25 | `CharacterUpdateFactorCharismaPointCB` | `0x00624BE0` | 111 | cbreg:AgcmUICharacter |
| 26 | `CharacterUpdateCriminalStatusCB` | `0x00624C50` | 132 | cbreg:AgcmUICharacter |
| 27 | `CharacterBlockByPenalty` | `0x0061F270` | 199 | Zeichenketten/Konstanten (geprüft) |
| 28 | `SetSelfCharacterCB` | `0x00624CE0` | 193 | cbreg:AgcmUICharacter |
| 29 | `ReleaseSelfCharacterCB` | `0x00624DB0` | 70 | cbreg:AgcmUICharacter |
| 30 | `UpdateEquipItemCB` | `0x00624E00` | 86 | cbreg:AgcmUICharacter |
| 31 | `CBLockTarget` | `0x00624E60` | 94 | cbreg:AgcmUICharacter |
| 32 | `CBUnlockTarget` | `0x0061F340` | 48 | cbreg:AgcmUICharacter |
| 33 | `CBSelectTarget` | `0x00624EC0` | 90 | cbreg:AgcmUICharacter |
| 34 | `CBUnSelectTarget` | `0x00624F20` | 29 | cbreg:AgcmUICharacter |
| 35 | `CBCancelTransform` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 36 | `CBCancelEvolution` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 37 | `CBAttackResultNotEnoughArrow` | `0x0061F3F0` | 74 | cbreg:AgcmUICharacter |
| 38 | `CBAttackResultNotEnoughBolt` | `0x0061F440` | 74 | cbreg:AgcmUICharacter |
| 39 | `CBAttackResultNotEnoughMP` | `0x0061F490` | 74 | cbreg:AgcmUICharacter |
| 40 | `RefreshUserDataTargetCharacter` | `0x0061F4E0` | 47 | Aufrufgraph (geprüft) |
| 41 | `SetTargetCharacter` | `0x00623720` | 1201 | Aufrufgraph (geprüft) |
| 42 | `ResetTargetCharacter` | `0x00623C00` | 196 | Aufrufgraph (geprüft) |
| 43 | `CBSelfUpdatePosition` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 44 | `CBUpdatePosition` | `0x00623CD0` | 334 | cbreg:AgcmUICharacter |
| 45 | `CBInitCharacter` | `0x00623E20` | 110 | cbreg:AgcmUICharacter |
| 46 | `CBRemoveCharacter` | `0x00623E90` | 131 | cbreg:AgcmUICharacter |
| 47 | `CBUpdateActionStatus` | `0x00623F20` | 305 | cbreg:AgcmUICharacter |
| 48 | `OpenCharacterMenu` | `0x00624060` | 203 | Aufrufgraph (geprüft) |
| 49 | `CloseCharacterMenu` | `0x0061F510` | 50 | Aufrufgraph (geprüft) |
| 50 | `ResetDisplayCharacterStatus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 51 | `SetCallbackUpdateResurrectStatus` | – | | identischer Setter, vom Linker mit anderen Modulen zusammengefaltet (ICF) |
| 52 | `SetCallbackSetTargetCharacter` | – | | wie oben (ICF) |
| 53 | `SetCallbackResetTargetCharacter` | – | | wie oben (ICF) |
| 54 | `SetTransformDurationMSec` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 55 | `CBRefreshTargetName` | `0x0061F5E0` | 966 | UI-Registrierung |
| 56 | `CBToggleTargetUserMenu` | `0x0061F9B0` | 52 | UI-Registrierung |
| 57 | `CBToggleTargetAttrTooltip` | `0x00624130` | 175 | UI-Registrierung |
| 58 | `CBCloseTargetAttrTooltip` | `0x0061F9F0` | 51 | UI-Registrierung |
| 59 | `CBToggleTargetSummonsMenu` | `0x0061FA30` | 135 | UI-Registrierung |
| 60 | `CBDisplaySummonsPropensity` | `0x00624F40` | 224 | UI-Registrierung |
| 61 | `CBDisplaySiegeResurrection` | `0x006241E0` | 73 | UI-Registrierung |
| 62 | `CBSummonsPropensityAttackClick` | `0x00624230` | 69 | UI-Registrierung |
| 63 | `CBSummonsPropensityDefenseClick` | `0x00624280` | 69 | UI-Registrierung |
| 64 | `CBSummonsPropensityShadowClick` | `0x006242D0` | 69 | UI-Registrierung |
| 65 | `SendSummonsSetPropenstiy` | `0x0061FAC0` | 105 | Aufrufgraph (geprüft) |
| 66 | `CBReceiveSummonsSetPropensity` | `0x0061FB30` | 76 | cbreg:AgcmUICharacter |
| 67 | `CBToggleExpType` | `0x00625030` | 60 | UI-Registrierung |
| 68 | `SetTargetAttrToolTipInfo` | `0x0061FB80` | 1384 | Aufrufgraph (geprüft) |
| 69 | `SetTargetSummonsToolTipInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 70 | `AddTargetBuffedSkill` | `0x00620120` | 107 | Aufrufgraph (geprüft) |
| 71 | `RemoveTargetBuffedSkill` | `0x00620190` | 58 | Aufrufgraph (geprüft) |
| 72 | `ResetTargetBuffedSkill` | `0x006201D0` | 43 | von Hand geprüft |
| 73 | `CBAddBuffedSkill` | `0x00620200` | 176 | cbreg:AgcmUICharacter |
| 74 | `CBRemoveBuffedSkill` | `0x006202B0` | 80 | cbreg:AgcmUICharacter |
| 75 | `CBRideAck` | `0x00625070` | 16 | cbreg:AgcmUICharacter |
| 76 | `SendRequestResurrectionToTown` | `0x00620300` | 223 | Aufrufgraph (geprüft) |
| 77 | `SendRequestResurrectionNow` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 78 | `SendRequestResurrectionSiege` | `0x006203E0` | 232 | Aufrufgraph (geprüft) |
| 79 | `SendRequestResurrectionByOther` | `0x006204D0` | 274 | Aufrufgraph (geprüft) |
| 80 | `CBResurrectionToTown` | `0x006205F0` | 16 | UI-Registrierung |
| 81 | `CBResurrectionNow` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 82 | `CBResurrectionSiege` | `0x00620600` | 130 | UI-Registrierung |
| 83 | `CBResurrectionSiegeInner` | `0x00620690` | 19 | UI-Registrierung |
| 84 | `CBResurrectionSiegeOuter` | `0x006206B0` | 19 | UI-Registrierung |
| 85 | `CBResurrectionByOther` | `0x006206D0` | 168 | cbreg:AgcmUICharacter |
| 86 | `CBResurrectionByOtherConfirm` | `0x00620780` | 36 | UI-Registrierung |
| 87 | `CBDisplayOtherName` | `0x006207B0` | 69 | UI-Registrierung |
| 88 | `CBOpenTargetNameTooltip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 89 | `CBCloseTargetNameTooltip` | `0x00620800` | 26 | UI-Registrierung |
| 90 | `CBCheckResurrectionToTown` | `0x00624320` | 259 | UI-Registrierung |
| 91 | `CBCheckResurrectionNow` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 92 | `CBIsExpPenalty` | `0x00620820` | 36 | UI-Registrierung |
| 93 | `CBIsActiveFollowMenu` | `0x00620850` | 69 | UI-Registrierung |
| 94 | `CBIsActiveSiegeResurrection` | `0x006208A0` | 101 | UI-Registrierung |
| 95 | `CBSetFollowTarget` | `0x00620910` | 59 | UI-Registrierung |
| 96 | `GetEditCon` | `0x00620950` | 31 | UI-Registrierung |
| 97 | `GetEditWis` | `0x00620970` | 31 | UI-Registrierung |
| 98 | `GetEditDex` | `0x00620990` | 31 | UI-Registrierung |
| 99 | `GetEditStr` | `0x006209B0` | 31 | UI-Registrierung |
| 100 | `GetEditInt` | `0x006209D0` | 31 | UI-Registrierung |
| 101 | `GetEditChar` | `0x006209F0` | 31 | UI-Registrierung |
| 102 | `SetEditTextType1` | `0x00620A10` | 179 | Zeichenketten/Konstanten (geprüft) |
| 103 | `SetEditTextType4` | `0x00620AD0` | 165 | Zeichenketten/Konstanten (geprüft) |
| 104 | `RefreshCharacterStatus` | `0x00624430` | 826 | Aufrufgraph (geprüft) |
| 105 | `StreamReadLevelupMessages` | `0x00620B80` | 588 | vtable/String |
| 106 | `AddBaseMinimapType` | `0x00620DD0` | 198 | Aufrufgraph (geprüft) |
| 107 | `RemoveBaseMinimapType` | `0x00620EA0` | 132 | Aufrufgraph (geprüft) |
| 108 | `ChangeBaseMinimapType` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 109 | `GetBaseMinimapInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 110 | `_UpdateTargetPlayerRaceAndClass` | `0x00620FB0` | 507 | von Hand geprüft |
| 111 | `OnToggleBtnRestoreTransform` | – | | inline/klein |
| 112 | `OnShowBtnRestoreTransform` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 113 | `OnHideBtnRestoreTransform` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 114 | `OnToggleBtnRestoreEvolution` | – | | inline/klein |
| 115 | `OnShowBtnRestoreEvolution` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 116 | `OnHideBtnRestoreEvolution` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 117 | `OnShowBlindEquipSlot` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 118 | `OnHideBlindEquipSlot` | `0x00621400` | 166 | Zeichenketten/Konstanten (geprüft) |
| 119 | `OnShowUIResurrection` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 120 | `CallBack_OnSelectPropertyAttack` | `0x006247D0` | 60 | UI-Registrierung |
| 121 | `CallBack_OnSelectPropertyTab` | `0x00624810` | 107 | UI-Registrierung |

88 von 122 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0061e670` (`0x0061E670`), `~AgcmUICharacter` (`0x006214E0`), `ctor_or_dtor_006214f0` (`0x006214F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xC28` | `m_pcsAgpmCharacter` | `[+0xDE4]` ist dessen `m_csPacket` (Resurrection-Pakete) |
| `0xC44` | `m_pcsAgcmCharacter` | `+0x1596C` ist der Self-Character-Zeiger (wie in [`AgcmUIMain`](AgcmUIMain.md)) |
| `0xC50` | `m_pcsAgcmMinimap` | `AddBaseMinimapType`, `CBUpdatePosition` |
| `0xC90 / 0xC94` | `Minimap-Typtabellen (Index je Basistyp 1 / 3)` | `RemoveBaseMinimapType`, `CBUpdatePosition` |
| `0xC9C` | `m_pcsTargetCharacter` | `RefreshUserDataTargetCharacter`, `ResetTargetCharacter`, `AddTargetBuffedSkill` |
| `0xCA0 / 0xCA4 / 0xCA8` | `Userdata Selbst-Charakter (Faktoren, …)` | `SetCharacter`: `+0x44` wird mit Charakterdaten gesetzt, danach `SetUserDataRefresh` |
| `0xCAC` | `m_pstUserDataTargetCharacter` | `RefreshUserDataTargetCharacter` |
| `0xCB4` | `m_pstUserDataTargetBuffGrid` | Buff-Grid-Funktionen |
| `0x168C` | `m_csTargetBuffGrid (AgpdGrid)` | `AddTargetBuffedSkill`, `RemoveTargetBuffedSkill`, `ResetTargetBuffedSkill` |
| `0x1664` | `m_bIsOpenedCharacterMenu` | `CloseCharacterMenu`, `OpenCharacterMenu` |
| `0x1684` | `m_ulCriminalNotifyClock` | `SetCharacter` setzt Tick, `ReleaseCharacter` löscht |
| `0x16B0 / 0x16B4 / 0x16B8` | `m_bIsOpenedTargetAttrInfo / UserMenu / SummonsMenu` | `CBUpdatePosition` schließt die Fenster, wenn der eigene Charakter sich bewegt |
| `0x15D4 … 0x15DC` | `Eingabefelder der Statusanzeige` | `RefreshCharacterStatus` (`+0xF4` = m_pcsBase) |

## Callback-Registrierung in OnAddModule (0x00625C80)

Die 28 `SetCallback…`-Aufrufe stehen im Binary in derselben Reihenfolge wie in der Quelle; die Übergabe der Funktionszeiger ist dadurch Position für Position zuordenbar. Bestätigt wird das durch zwei Stellen, an denen die Quelle dieselbe Funktion zweimal registriert (`Equip`/`UnEquip` und `RideAck`/`DismountAck`): im Binary sind es jeweils dieselben Adressen.

| Callback-Setter | Handler | Adresse |
|---|---|---|
| `AgcmCharacter: UpdateFactor` | `CharacterUpdateFactorCB` | `0x00624980` |
| `UpdateLevel` | `CharacterLevelUp` | `0x0061F030` |
| `UpdateFactorBonusExp` | `CharacterUpdateFactorBonusExpCB` | `0x0061F120` |
| `UpdateFactorMurdererPoint` | `CharacterUpdateFactorMurdererPointCB` | `0x00624A70` |
| `UpdateFactorCharismaPoint` | `CharacterUpdateFactorCharismaPointCB` | `0x00624BE0` |
| `UpdateCriminalStatus` | `CharacterUpdateCriminalStatusCB` | `0x00624C50` |
| `BlockByPenalty` | `CharacterBlockByPenalty` | `0x0061F270` |
| `SetSelfCharacter` | `SetSelfCharacterCB` | `0x00624CE0` |
| `ReleaseSelfCharacter` | `ReleaseSelfCharacterCB` | `0x00624DB0` |
| `ActionResultNotEnoughArrow` | `CBAttackResultNotEnoughArrow` | `0x0061F3F0` |
| `ActionResultNotEnoughBolt` | `CBAttackResultNotEnoughBolt` | `0x0061F440` |
| `ActionResultNotEnoughMP` | `CBAttackResultNotEnoughMP` | `0x0061F490` |
| `InitChar` | `CBInitCharacter` | `0x00623E20` |
| `UpdatePosition` | `CBUpdatePosition` | `0x00623CD0` |
| `RemoveChar` | `CBRemoveCharacter` | `0x00623E90` |
| `UpdateActionStatus` | `CBUpdateActionStatus` | `0x00623F20` |
| `ResurrectionByOther` | `CBResurrectionByOther` | `0x006206D0` |
| `Equip` | `UpdateEquipItemCB` | `0x00624E00` |
| `UnEquip` | `UpdateEquipItemCB` | `0x00624E00` |
| `LockTarget` | `CBLockTarget` | `0x00624E60` |
| `UnlockTarget` | `CBUnlockTarget` | `0x0061F340` |
| `SelectTarget` | `CBSelectTarget` | `0x00624EC0` |
| `UnSelectTarget` | `CBUnSelectTarget` | `0x00624F20` |
| `AddBuffedList` | `CBAddBuffedSkill` | `0x00620200` |
| `RemoveBuffedList` | `CBRemoveBuffedSkill` | `0x006202B0` |
| `RideAck` | `CBRideAck` | `0x00625070` |
| `DismountAck` | `CBRideAck` | `0x00625070` |
| `(AgpmSummons) SetPropensity` | `CBReceiveSummonsSetPropensity` | `0x0061FB30` |

## Pakete an den Server (aus diesem Modul)

Das Modul baut diese Pakete über [`AgpmCharacter`](AgpmCharacter.md):m_csPacket` (Typ `0x01`; Feld 2 = Operation) und sendet sie mit `SendPacket`; Operation und Felder wurden gegen das Dekompilat gelesen:

| Funktion | Adresse | Operation (Wert) | Felder |
|---|---|---|---|
| `SendRequestResurrectionToTown` | `0x00620300` | `REQUEST_RESURRECTION_TOWN` (9) | Operation, Charakter-ID |
| `SendRequestResurrectionSiege` | `0x006203E0` | `…SIEGE_INNER` (19) bzw. `…SIEGE_OUTER` (20) | Operation, Charakter-ID |
| `SendRequestResurrectionByOther` | `0x006204D0` | `RESURRECTION_BY_OTHER` (24) | Operation, Charakter-ID, Flag = 1, Name des Helfers |
| `SendSummonsSetPropenstiy` | `0x0061FAC0` | [`AgpmSummons`](AgpmSummons.md):MakeSetPropensityPacket` (Selbst-ID, Beschwörungs-ID, Neigung) | Paket von `AgpmSummons` |

Die Operationsnummern stimmen mit `AGPMCHAR_PACKET_OPERATION_*` der EP8-Quelle überein. `SendRequestResurrectionNow` (Operation 10) ist im Binary nicht zugeordnet.

## UI-Registrierung

Die Hilfsfunktionen `AddFunction` (`0x00625080`, 1152 Byte), `AddDisplay` (`0x00625500`, 1916 Byte), `AddEvent` (`0x006218E0`, 2236 Byte), `AddUserData` (`0x006221A0`) und `AddBoolean` (`0x00622330`) rufen die Registrierungsfunktionen von [`AgcmUIManager2`](AgcmUIManager2.md) (siehe dort). Namen und Anzahl der registrierten Funktionen (27), Boolean-Werte (3) und Charakter-Anzeigen (61) stimmen mit der Quelle überein; die Namen (teils koreanisch) stehen in der Tabelle „UI-Namen“.

## Callbacks (EnumCallback)

| ID | Name (Quelle) | Auslöser im Binary |
|---:|---|---|
| 0 | `UPDATE_RESURRECT_STATUS` | `CBUpdateActionStatus` (`0x00623F20`) |
| 1 | `SET_TARGET_CHARACTER` | `SetTargetCharacter` (`0x00623720`) |
| 2 | `RESET_TARGET_CHARACTER` | `ResetTargetCharacter` (`0x00623C00`) |

## Anzeigeregeln

- **Werteänderung (`SetEditTextType1`, `0x00620A10`):** gleiche Werte werden als `%d` gezeigt; ist der aktuelle Wert höher als der Ausgangswert, steht er mit Farbe `65280` (grün) und `(+Differenz)`, sonst mit `16711680` (rot) und `(−Differenz)`; die Differenz ist weiß (`16777215`).
- **Strafe (`CharacterBlockByPenalty`, `0x0061F270`):** Nur für den eigenen Charakter; die Strafart (< 11) bildet den Schlüssel `CharacterPenalty` + `_CantPT…`-Suffix (Tabelle mit 20 Byte Stride), dessen Text im Meldungsdialog angezeigt wird (`ActionMessageOKDialog`).
- **Angriffs-/Zauberwerte (`SetTargetAttrToolTipInfo`, `0x0061FB80`):** Texte aus den Schlüsseln `CharacterAttrDamage`, `CharacterAttr`, `CharacterAttrMagic`, `CharacterAttrWater` usw.; Wortreihenfolge und Format hängen vom Sprach-/Regionsflag `DAT_008AD470` ab (Wert 4 gibt Magie vor Schaden aus).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00625080`, `0x00625500`, `0x006218E0`, `0x006221A0`, `0x00622330`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (27)

| Name | Id | Handler |
|---|---:|---|
| `RefreshTargetName` |  | `CBRefreshTargetName` |
| `ToggleTargetUserMenu` |  | `CBToggleTargetUserMenu` |
| `ToggleTargetAttrTooltip` |  | `CBToggleTargetAttrTooltip` |
| `CloseTargetAttrTooltip` |  | `CBCloseTargetAttrTooltip` |
| `ToggleTargetSummonsMenu` |  | `CBToggleTargetSummonsMenu` |
| `SummonsPropensityAttackClick` |  | `CBSummonsPropensityAttackClick` |
| `SummonsPropensityDefenseClick` |  | `CBSummonsPropensityDefenseClick` |
| `SummonsPropensityShadowClick` |  | `CBSummonsPropensityShadowClick` |
| `CharToggleExpType` |  | `CBToggleExpType` |
| `CharResurrectionToTown` |  | `CBResurrectionToTown` |
| `CharResurrectionNow` |  | [`AgcmShrine`](AgcmShrine.md):CBShrineTapScroe` |
| `CharResurrectionSiege` |  | `CBResurrectionSiege` |
| `CharCheckResurrectionToTown` |  | `CBCheckResurrectionToTown` |
| `CharCheckResurrectionNow` |  | `Element::GetSize` |
| `CharResurrectionSiegeInner` |  | `CBResurrectionSiegeInner` |
| `CharResurrectionSiegeOuter` |  | `CBResurrectionSiegeOuter` |
| `CharOpenTargetNameTooltip` |  | `Element::GetSize` |
| `CharCloseTargetNameTooltip` |  | `CBCloseTargetNameTooltip` |
| `CharSetFollowTarget` |  | `CBSetFollowTarget` |
| `CharGetEditCon` |  | `GetEditCon` |
| `CharGetEditWis` |  | `GetEditWis` |
| `CharGetEditDex` |  | `GetEditDex` |
| `CharGetEditStr` |  | `GetEditStr` |
| `CharGetEditInt` |  | `GetEditInt` |
| `CharGetEditChar` |  | `GetEditChar` |
| `UiCharacterStatusDialog_OnSelectPropertyAttack` |  | `CallBack_OnSelectPropertyAttack` |
| `UiCharacterStatusDialog_OnSelectPropertyTab` |  | `CallBack_OnSelectPropertyTab` |

**Anzeige** (68)

| Name | Id | Handler |
|---|---:|---|
| `캐릭터 이름` | 1 | `CharacterStatusCB` |
| `클래스 이름` | 2 | `CharacterStatusCB` |
| `레이스 이름` | 3 | `CharacterStatusCB` |
| `젠더 이름` | 4 | `CharacterStatusCB` |
| `레이스,클레스 이름` | 5 | `CharacterStatusCB` |
| `현재 레벨` | 6 | `CharacterStatusCB` |
| `현재 경험치` | 7 | `CharacterStatusCB` |
| `현 레벨 최대 경험치` | 8 | `CharacterStatusCB` |
| `경험치(%)` | 9 | `CharacterStatusCB` |
| `경험치(%)2` | 10 | `CharacterStatusCB` |
| `EXP_Bar` | 0xb | `CharacterStatusCB` |
| `생명` | 0xc | `CharacterStatusCB` |
| `지혜` | 0xd | `CharacterStatusCB` |
| `민첩` | 0xe | `CharacterStatusCB` |
| `힘` | 0xf | `CharacterStatusCB` |
| `지식` | 0x10 | `CharacterStatusCB` |
| `카리스마` | 0x11 | `CharacterStatusCB` |
| `HP` | 0x12 | `CharacterStatusCB` |
| `HP_Max` | 0x13 | `CharacterStatusCB` |
| `HP_All` | 0x14 | `CharacterStatusCB` |
| `HP_Bar` | 0x15 | `CharacterStatusCB` |
| `MP` | 0x16 | `CharacterStatusCB` |
| `MP_Max` | 0x17 | – |
| `MP_All` | 0x18 | – |
| `MP_Percent` | 0x19 | – |
| `MP_Bar` | 0x1a | – |
| `SP` | 0x1b | – |
| `SP_Max` | 0x1c | – |
| `SP_All` | 0x1d | – |
| `SP_Percent` | 0x1e | – |
| `AR` | 0x1f | `CharacterStatusCB` |
| `DR` | 0x20 | – |
| `AttackSpeed` | 0x22 | – |
| `MoveFast` | 0x21 | – |
| `물리 방어력` | 0x23 | – |
| `마법 방어력` | 0x24 | – |
| `불 방어력` | 0x25 | `CharacterStatusCB` |
| `물 방어력` | 0x26 | – |
| `공기 방어력` | 0x27 | – |
| `땅 방어력` | 0x28 | – |
| `파티 방어력` | 0x29 | – |
| `물리 공격력 최소` | 0x2a | – |
| `물리 공격력 최대` | 0x2b | `CharacterStatusCB` |
| `물리 공격력 모두` | 0x2c | – |
| `마법 공격력 최소` | 0x2d | – |
| `마법 공격력 최대` | 0x2e | – |
| `마법 공격력 모두` | 0x2f | – |
| `불 공격력 최소` | 0x30 | – |
| `불 공격력 최대` | 0x31 | `CharacterStatusCB` |
| `불 공격력 모두` | 0x32 | – |
| `공기 공격력 최소` | 0x36 | – |
| `공기 공격력 최대` | 0x37 | – |
| `공기 공격력 모두` | 0x38 | – |
| `물 공격력 최소` | 0x33 | – |
| `물 공격력 최대` | 0x34 | `CharacterStatusCB` |
| `물 공격력 모두` | 0x35 | – |
| `땅 공격력 최소` | 0x39 | – |
| `땅 공격력 최대` | 0x3a | – |
| `땅 공격력 모두` | 0x3b | – |
| `파티 공격력` | 0x3c | – |
| `스킬 기본 공격력` | 0x3d | `CharacterStatusCB` |
| `캐릭터메뉴 타겟 이름` | 0x3e | `FUN_0061eca0` |
| `레벨 변경값` | 0x3f | `FUN_0061eec0` |
| `보너스 EXP` | 0x40 | `FUN_0061eec0` |
| `보너스 EXP (PC방)` | 0x41 | `FUN_0061eec0` |
| `SummonsPropensity` | 0 | `CBDisplaySummonsPropensity` |
| `SiegeResurrection` | 0 | – |
| `OtherName` | 0 | – |

**Ereignis** (66)

| Name | Id | Handler |
|---|---:|---|
| `레벨업` | 0 | – |
| `Exp_획득` | 0 | – |
| `Exp_획득_(PC방_보너스)` | 0 | – |
| `CharacterAtkResultNotEnoughArrow` | 0 | – |
| `CharacterAtkResultNotEnoughBolt` | 0 | – |
| `CharacterAtkResultNotEnoughMP` | 0 | – |
| `CharacterMenuOpen` | 0 | – |
| `CharacterMenuClose` | 0 | – |
| `TargetInfoOpen` | 0 | – |
| `TargetInfoClose` | 0 | – |
| `TargetInfoAttrNone` | 0 | – |
| `TargetInfoAttrAir` | 0 | – |
| `TargetInfoAttrFire` | 0 | – |
| `TargetInfoAttrWater` | 0 | – |
| `TargetInfoAttrMagic` | 0 | – |
| `TargetInfoAttrEarth` | 0 | – |
| `TargetInfoAttrPoison` | 0 | – |
| `TargetInfoAttrIce` | 0 | – |
| `TargetInfoAttrLightening` | 0 | – |
| `TargetPKCriminal` | 0 | – |
| `TargetPKMurdererLevel1` | 0 | – |
| `TargetPKMurdererLevel2` | 0 | – |
| `TargetPKMurdererLevel3` | 0 | – |
| `TargetInfoOn` | 0 | – |
| `TargetInfoOff` | 0 | – |
| `RefreshTargetName` | 0 | – |
| `TargetAttrMenuOpen` | 0 | – |
| `TargetAttrMenuClose` | 0 | – |
| `TargetUserMenuOpen` | 0 | – |
| `TargetUserMenuClose` | 0 | – |
| `TargetUserSummonsMenuOpen` | 0 | – |
| `TargetUserSummonsMenuClose` | 0 | – |
| `TargetUserSummonsMenu2Open` | 0 | – |
| `TargetUserSummonsMenu2Close` | 0 | – |
| `DisplaySummmonsPropensity` | 0 | – |
| `OpenResurrectionUI` | 0 | – |
| `CloseResurrectionUI` | 0 | – |
| `OpenConfirmResurrectTownUI` | 0 | – |
| `OpenConfirmResurrectUI` | 0 | – |
| `CloseTargetAllWindow` | 0 | – |
| `CharacterMurdererPointUp` | 0 | – |
| `TargetRace_Human` | 0 | – |
| `TargetRace_Orc` | 0 | – |
| `TargetRace_MoonElf` | 0 | – |
| `TargetRace_DragonScion` | 0 | – |
| `TargetClass_Knight` | 0 | – |
| `TargetClass_Archer` | 0 | – |
| `TargetClass_Mage` | 0 | – |
| `TargetClass_Berserker` | 0 | – |
| `TargetClass_Hunter` | 0 | – |
| `TargetClass_Socerer` | 0 | – |
| `TargetClass_SwashBuckler` | 0 | – |
| `TargetClass_Ranger` | 0 | – |
| `TargetClass_Elementalist` | 0 | – |
| `TargetClass_Scion` | 0 | – |
| `TargetClass_Slayer` | 0 | – |
| `TargetClass_Obiter` | 0 | – |
| `TargetClass_Summerner` | 0 | – |
| `Char_Get_Edit_Con` | 0 | – |
| `Char_Get_Edit_Wis` | 0 | – |
| `Char_Get_Edit_Dex` | 0 | – |
| `Char_Get_Edit_Str` | 0 | – |
| `Char_Get_Edit_Int` | 0 | – |
| `Char_Get_Edit_Char` | 0 | – |
| `Char_OpenSelectSiegeResurrect` | 0 | – |
| `Char_OpenResurrectionByOther` |  | `CBResurrectionByOtherConfirm` |

**UserData** (7)

| Name | Id | Handler |
|---|---:|---|
| `캐릭터 메뉴 대상 캐릭터` |  | – |
| `캐릭터 메시지 데이타들` |  | – |
| `TargetBuffGrid` |  | – |
| `SelfCharacterDead` |  | – |
| `SummonsPropensityUD` |  | – |
| `ExpPenalty` |  | – |
| `OtherNameUD` |  | – |

**Boolean** (3)

| Name | Id | Handler |
|---|---:|---|
| `IsActiveFollowMenu` |  | `CBIsActiveFollowMenu` |
| `IsExpPenalty` |  | `CBIsExpPenalty` |
| `IsActiveSiegeResurrection` |  | `CBIsActiveSiegeResurrection` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Rund ein Viertel der Methoden ist nicht zugeordnet, meist kleine Funktionen (Setter, Ein-/Ausblenden von Schaltflächen) oder Funktionen, die der Compiler in andere eingefaltet hat; die drei `SetCallback…`-Setter sind mit gleichartigen Funktionen anderer Module zusammengefaltet.
- Die Anzeigenamen sind nun über die Daten des Binary aufgelöst und gegen die Makros der Quelle verglichen (61 von 61 gleich); die Ereignisnamen sind in der Tabelle, aber nicht einzeln gegen die Quelle verglichen.
- `StreamReadLevelupMessages`, `RefreshCharacterStatus` und `SetTargetAttrToolTipInfo` wurden nur teilweise gegen die Quelle gelesen.
- Nicht untersucht sind `CUiCharacterProperty` und `CharacterPropertyCallBack.cpp` sowie die UI-Skripte.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 2, ohne Kandidat: 6, zugeordnet: 6.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `OnShowUIResurrection` | 5 | `0x006214B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowBlindEquipSlot` | 14 | `0x006213C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowBtnRestoreEvolution` | 31 | `0x006212F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnHideBtnRestoreTransform` | 15 | `0x006212A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowBtnRestoreTransform` | 31 | `0x006211D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBaseMinimapInfo` | 5 | `0x00620F30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmShrine`](AgcmShrine.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmSummons`](AgpmSummons.md)
- **Erwähnt in:** [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUISkill2`](AgcmUISkill2.md), [`AgcmUITax`](AgcmUITax.md)
