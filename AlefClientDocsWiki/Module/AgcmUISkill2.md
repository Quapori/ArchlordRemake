# AgcmUISkill2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUISkill2` (Skill-Fenster: Kaufen, Hochstufen, Mastery-Seiten, Skill-Tooltips) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmUISkill2` (`AgcmUISkill2.cpp`, `AgcmUISkill2Tooltip.cpp`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 145 von 173 Quellmethoden sind zugeordnet; die Zuordnung stützt sich auf bereits vorhandene Namen, Zeichenketten (Tooltip), den Aufrufgraphen und die Callback-Reihenfolge. 12 der in diesem Durchgang neu zugeordneten Methoden wurden gegen Dekompilat und Quelle gelesen; keine war falsch, ein Sequenz-Vorschlag (`SetSkillToolTipEADamageAttribute`) wurde verworfen, weil er auf eine Template-Hilfsfunktion zeigt.
- **UI-Namen:** 48 Funktionen, 24 Anzeigen (IDs 0–23, `SkillPoint` bis `SkillPointHighLevel10`) und 4 Boolean-Werte entsprechen in Anzahl und Namen der Quelle (siehe Tabelle „UI-Namen“); `CBDisplaySkillName` (`0x006C7FE0`) ist neu zugeordnet. Zwei Quellhandler-Paare teilen sich je eine Adresse.
- **Mastery-Seiten:** Indizes 0–4, 6 (Hochstufen), 7 (Heroic), 100 (Archlord) wie in der Quelle.
- **Abweichung Skill-Kauf:** Der Handler für das Kaufergebnis ist im Binary ein leerer Stub; das Erfolgs-Ereignis `SkillBuySuccess` der Quelle wird nicht ausgelöst.
- **Registrierungen:** 35 statt 37 Callbacks (siehe unten).
- **Fehlerprotokoll:** Eine Tooltip-Hilfsfunktion schreibt „GetAdditionalSkillTID is empty - TID:%d, Level:%d“ nach `LOG\SkillError.txt`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUISkill2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006CEF50` | 1490 | vtable/String |
| 1 | `OnInit` | `0x006C6D90` | 347 | vtable/String |
| 2 | `OnDestroy` | `0x006C6EF0` | 120 | vtable/String |
| 3 | `AddFunction` | `0x006CDD10` | 2056 | Zeichenkette |
| 4 | `AddEvent` | `0x006CA920` | 2367 | Zeichenkette |
| 5 | `AddUserData` | `0x006C6F70` | 699 | Zeichenkette |
| 6 | `AddDisplay` | `0x006CB260` | 834 | Zeichenkette |
| 7 | `AddBoolean` | `0x006CCE00` | 129 | Zeichenkette |
| 8 | `SetMastery` | `0x006CD0D0` | 551 | Aufrufgraph (geprüft) |
| 9 | `SetBuyMastery` | `0x006CB5B0` | 532 | Aufrufgraph (geprüft) |
| 10 | `SetUpgradeMastery` | `0x006CB7D0` | 408 | Aufrufgraph (geprüft) |
| 11 | `SetMasteryArchlord` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 12 | `SetMasteryHighLevel` | `0x006CB970` | 738 | Aufrufgraph (geprüft) |
| 13 | `SetMasteryHeroic` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 14 | `SetUpgradeMasteryHighLevel` | `0x006CBC60` | 633 | Aufrufgraph (geprüft) |
| 15 | `SetUpgradeMasteryHeroic` | `0x006C7230` | 31 | Aufrufgraph (geprüft) |
| 16 | `CBSetMastery0` | `0x006CD300` | 175 | UI-Registrierung |
| 17 | `CBSetMastery1` | `0x006CD3B0` | 175 | UI-Registrierung |
| 18 | `CBSetMastery2` | `0x006CD460` | 175 | UI-Registrierung |
| 19 | `CBSetMastery3` | `0x006CD510` | 175 | UI-Registrierung |
| 20 | `CBSetMastery4` | `0x006CD5C0` | 184 | UI-Registrierung |
| 21 | `CBSetMasteryHighLevel` | `0x006CD680` | 168 | UI-Registrierung |
| 22 | `CBSetMasteryHeroic` | `0x006CD730` | 209 | UI-Registrierung |
| 23 | `CBSetBuyMastery0` | `0x006CBEF0` | 184 | UI-Registrierung |
| 24 | `CBSetBuyMastery1` | `0x006CBFB0` | 184 | UI-Registrierung |
| 25 | `CBSetBuyMastery2` | `0x006CC070` | 184 | UI-Registrierung |
| 26 | `CBSetBuyMastery3` | `0x006CC130` | 184 | UI-Registrierung |
| 27 | `CBSetUpgradeMastery0` | `0x006CC380` | 34 | uireg |
| 28 | `CBSetUpgradeMastery1` | `0x006CC1F0` | 69 | UI-Registrierung |
| 29 | `CBSetUpgradeMastery2` | `0x006CC240` | 34 | UI-Registrierung |
| 30 | `CBSetUpgradeMastery3` | `0x006CC270` | 34 | UI-Registrierung |
| 31 | `CBOpenSkillUI` | `0x006CD810` | 463 | UI-Registrierung |
| 32 | `CBOpenSkillBuyUI` | `0x006CC2A0` | 213 | UI-Registrierung |
| 33 | `CBOpenSkillUpgradeUI` | `0x006CC380` | 34 | gleiche Adresse wie `CBSetUpgradeMastery0` (vom Linker zusammengefaltet) |
| 34 | `CBOpenSkillHighLevelUI` | `0x006CD9E0` | 267 | UI-Registrierung |
| 35 | `CBOpenSkillHighLevelSkillUpgradeUI` | `0x006CC3B0` | 306 | UI-Registrierung |
| 36 | `CBOpenSkillHeroicUI` | `0x006CDAF0` | 260 | UI-Registrierung |
| 37 | `CBOpenSkillHeroicSkillUpgradeUI` | `0x006CC4F0` | 374 | UI-Registrierung |
| 38 | `CBCloseSkillHighLevelUI` | `0x006C7250` | 42 | UI-Registrierung |
| 39 | `CBCloseSkillHeroicUI` | `0x006C7280` | 42 | UI-Registrierung |
| 40 | `CBSelectSkillGrid` | `0x006C72B0` | 319 | UI-Registrierung |
| 41 | `CBSelectBuySkillGrid` | `0x006C73F0` | 344 | UI-Registrierung |
| 42 | `CBSelectUpgradeSkillGrid` | `0x006C7550` | 131 | UI-Registrierung |
| 43 | `CBBuySkill` | `0x006C75E0` | 154 | UI-Registrierung |
| 44 | `CBUpgradeSkill` | `0x006C7680` | 93 | UI-Registrierung |
| 45 | `CBUpdateListItemStatus` | `0x006C76E0` | 114 | UI-Registrierung |
| 46 | `CBUpdateBuyListItemStatus` | `0x006CC670` | 150 | UI-Registrierung |
| 47 | `CBUpdateUpgradeListItemStatus` | `0x006CC710` | 150 | UI-Registrierung |
| 48 | `CBCloseSkillEventUI` | `0x006C7760` | 25 | UI-Registrierung |
| 49 | `CBToggleSkillUI` | `0x006C7780` | 231 | UI-Registrierung |
| 50 | `CBSkillInitialize` | `0x006C7870` | 131 | UI-Registrierung |
| 51 | `CBSetFailInitializeText` | `0x006C7900` | 149 | UI-Registrierung |
| 52 | `CBSetConfirmInitializeText` | `0x006C79A0` | 149 | UI-Registrierung |
| 53 | `CBSetSelfCharacter` | `0x006CE950` | 337 | Callback-Registrierung |
| 54 | `CBReleaseSelfCharacter` | `0x006C7A40` | 153 | Callback-Registrierung |
| 55 | `CBSelfUpdatePosition` | `0x006C7AF0` | 193 | Callback-Registrierung |
| 56 | `CBAddSkill` | `0x006CECD0` | 316 | Callback-Registrierung |
| 57 | `CBRemoveSkill` | `0x006CEE10` | 310 | Callback-Registrierung |
| 58 | `AddHighLevelSkill` | `0x006CC7B0` | 39 | Aufrufgraph (geprüft) |
| 59 | `RemoveHighLevelSkill` | `0x006CEAB0` | 97 | Aufrufgraph (geprüft) |
| 60 | `AddArchlordSkill` | `0x006CEB20` | 55 | Aufrufgraph (geprüft) |
| 61 | `RemoveArchlordSkill` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 62 | `AddHeroicSkill` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 63 | `RemoveHeroicSkill` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 64 | `CBUpdateSkillPoint` | `0x006CC7E0` | 436 | Callback-Registrierung |
| 65 | `CBCheckCastSkillResult` | `0x006C7BC0` | 209 | Callback-Registrierung |
| 66 | `CBReceiveSkillAction` | `0x006CC9A0` | 98 | Callback-Registrierung |
| 67 | `CBAddBuffedList` | `0x006C7CD0` | 75 | Callback-Registrierung |
| 68 | `CBRemoveBuffedList` | `0x006C7D20` | 36 | Callback-Registrierung |
| 69 | `CBConfirmUseSkillBook` | `0x006C7D50` | 50 | Callback-Registrierung |
| 70 | `CBSetItemTooltip` | `0x006C7D90` | 88 | Callback-Registrierung |
| 71 | `CBUpdateAlarmGrid` | `0x006CCA10` | 234 | Callback-Registrierung |
| 72 | `CBRefreshUpdateCharStatus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 73 | `CBUpdateCharFactorSkillPoint` | `0x006C7DF0` | 139 | Callback-Registrierung |
| 74 | `CBUpdateActionStatus` | `0x006CCB00` | 156 | Callback-Registrierung |
| 75 | `CBUpdateCharSkillPoint` | `0x006C7E80` | 61 | Callback-Registrierung |
| 76 | `CBUpdateInvenMoney` | `0x006C7EC0` | 62 | Callback-Registrierung |
| 77 | `CBResponseGrant` | `0x006C7F00` | 164 | Callback-Registrierung |
| 78 | `CBUpdateCost` | `0x006CEC30` | 96 | Callback-Registrierung |
| 79 | `CBUpdateItem` | `0x006CEC90` | 49 | Callback-Registrierung |
| 80 | `RefreshUsableOwnSkill` | `0x006CE8A0` | 171 | Aufrufgraph (geprüft) |
| 81 | `CBDisplaySkillPoint` | `0x006C7FB0` | 41 | UI-Registrierung |
| 82 | `CBDisplaySkillName` | `0x006C7FE0` | 144 | uireg |
| 83 | `CBDisplaySkillLevel` | `0x006C8070` | 374 | UI-Registrierung |
| 84 | `CBDisplaySkillPrice` | `0x006C81F0` | 253 | UI-Registrierung |
| 85 | `CBDisplaySkillTrainerClass` | `0x006C82F0` | 91 | UI-Registrierung |
| 86 | `CBDisplaySkillMainDialog` | `0x006C8350` | 76 | UI-Registrierung |
| 87 | `CBDisplayInvenMoney` | `0x006C83A0` | 48 | UI-Registrierung |
| 88 | `CBDisplaySkillBuyButton` | `0x006C83D0` | 201 | UI-Registrierung |
| 89 | `CBDisplaySelectedSkillName` | `0x006C84A0` | 153 | UI-Registrierung |
| 90 | `CBDisplaySkillPointHighLevel0` | `0x006C8540` | 402 | UI-Registrierung |
| 91 | `CBDisplaySkillPointHighLevel1` | `0x006C86E0` | 402 | UI-Registrierung |
| 92 | `CBDisplaySkillPointHighLevel2` | `0x006C8880` | 402 | UI-Registrierung |
| 93 | `CBDisplaySkillPointHighLevel3` | `0x006C8A20` | 402 | UI-Registrierung |
| 94 | `CBDisplaySkillPointHighLevel4` | `0x006C8BC0` | 402 | UI-Registrierung |
| 95 | `CBDisplaySkillPointHighLevel5` | `0x006C8D60` | 402 | UI-Registrierung |
| 96 | `CBDisplaySkillPointHighLevel6` | `0x006C8F00` | 402 | UI-Registrierung |
| 97 | `CBDisplaySkillPointHighLevel7` | `0x006C90A0` | 402 | UI-Registrierung |
| 98 | `CBDisplaySkillPointHighLevel8` | `0x006C9240` | 402 | UI-Registrierung |
| 99 | `CBDisplaySkillPointHighLevel9` | `0x006C93E0` | 402 | UI-Registrierung |
| 100 | `CBDisplaySkillPointHighLevel10` | `0x006C9580` | 402 | UI-Registrierung |
| 101 | `CBDisplaySkillLevelExp` | `0x006C9720` | 148 | UI-Registrierung |
| 102 | `CBDisplaySkillExpDegree` | `0x006C97C0` | 134 | UI-Registrierung |
| 103 | `CBIsActiveBuyButton` | `0x006CCBA0` | 40 | UI-Registrierung |
| 104 | `CBIsActiveUpgradeButton` | `0x006CCBD0` | 72 | UI-Registrierung |
| 105 | `CBIsActiveRollbackButton` | `0x006C9850` | 200 | UI-Registrierung |
| 106 | `CBIsActiveRollbackButton2` | `0x006C9920` | 54 | UI-Registrierung |
| 107 | `GetUpdateFactor` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 108 | `SetRecastSkillTimeToGridItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 109 | `CBReturnConfirmBuySkill` | `0x006C9960` | 99 | UI-Registrierung |
| 110 | `CBReturnConfirmLearnSkill` | `0x006C99D0` | 213 | UI-Registrierung |
| 111 | `CBBuySkillResult` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 112 | `CBUpgradeSkillResult` | `0x006CCC20` | 248 | Callback-Registrierung |
| 113 | `CBLearnSkillResult` | `0x006C9AC0` | 180 | Callback-Registrierung |
| 114 | `CBSkillInitializeResult` | `0x006CCD30` | 204 | Callback-Registrierung |
| 115 | `CBInitCoolTime` | `0x006C9B90` | 75 | Callback-Registrierung |
| 116 | `CBGetSkillLevel` | `0x006C9BE0` | 57 | Callback-Registrierung |
| 117 | `CBReturnConfirmUpgradeSkill` | `0x006C9C20` | 240 | UI-Registrierung |
| 118 | `CBSkillInitializeOK` | `0x006C9D10` | 69 | UI-Registrierung |
| 119 | `CBSkillRollback` | `0x006C9D60` | 215 | UI-Registrierung |
| 120 | `CBReturnConfirmSkillRollback` | `0x006C9E40` | 228 | UI-Registrierung |
| 121 | `IsActiveBuyItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 122 | `IsActiveUpgradeItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 123 | `IsActiveUpgradeHighLevelItem` | `0x006CA280` | 431 | Aufrufgraph (geprüft) |
| 124 | `SetStatusActiveBuyItem` | `0x006C9F30` | 481 | Aufrufgraph (geprüft) |
| 125 | `SetStatusActiveUpgradeItem` | `0x006CA120` | 338 | Aufrufgraph (geprüft) |
| 126 | `OpenSkillUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 127 | `OnShowMsgBox` | `0x006CA430` | 61 | Aufrufgraph (geprüft) |
| 128 | `IsUsableSkill` | `0x006CE780` | 280 | Aufrufgraph (geprüft) |
| 129 | `IsEnableSkill` | `0x006CA470` | 71 | Aufrufgraph (geprüft) |
| 130 | `_IsUsableSkillForMyRaceAndClass` | `0x006CE590` | 454 | Zeichenketten/Konstanten (geprüft) |
| 131 | `RefreshInitButton` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 132 | `_MoveSkillWindow` | `0x006CA4E0` | 256 | Zeichenkette |
| 133 | `CBOpenSkillToolTip` | `0x007770B0` | 28 | UI-Registrierung |
| 134 | `CBOpenButtonSkillToolTip` | `0x007770D0` | 90 | UI-Registrierung |
| 135 | `CBOpenBuySkillToolTip` | `0x00777130` | 91 | UI-Registrierung |
| 136 | `CBOpenBuyButtonSkillToolTip` | `0x00777190` | 137 | UI-Registrierung |
| 137 | `CBOpenUpgradeSkillToolTip` | `0x00777220` | 28 | UI-Registrierung |
| 138 | `CBOpenUpgradeButtonSkillToolTip` | `0x00777240` | 90 | UI-Registrierung |
| 139 | `OpenSkillToolTip` | `0x00776FB0` | 241 | Aufrufgraph (geprüft) |
| 140 | `CloseSkillToolTip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 141 | `CBCloseSkillToolTip` | `0x0076C0E0` | 36 | uireg |
| 142 | `CBOpenQuickBeltToolTip` | `0x007772A0` | 28 | Callback-Registrierung |
| 143 | `CBCloseQuickBeltToolTip` | `0x0076C110` | 36 | Callback-Registrierung |
| 144 | `CBCloseAllUIToolTip` | `0x0076C140` | 62 | Callback-Registrierung |
| 145 | `SetSkillToolTipInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 146 | `SetSkillTemplateToolTipInfo` | `0x00776E50` | 187 | Aufrufgraph (geprüft) |
| 147 | `SetSkillToolTipName` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 148 | `SetSkillToolTipAttribute` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 149 | `SetSkillToolTipDescription` | `0x00772EE0` | 490 | Zeichenketten/Konstanten (geprüft) |
| 150 | `SetSkillToolTipCurrentLevel` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 151 | `SetSkillToolTipNextLevel` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 152 | `SetSkillToolTipUpgradeInfo` | `0x007730D0` | 1091 | Zeichenketten/Konstanten (geprüft) |
| 153 | `SetSkillToolTipInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 154 | `SetSkillToolTipBasicAttribute` | `0x0076C460` | 2462 | Zeichenketten/Konstanten (geprüft) |
| 155 | `SetSkillToolTipBasicEffect` | `0x0076CE00` | 1519 | Zeichenketten/Konstanten (geprüft) |
| 156 | `SetSkillToolTipCostAttribute` | `0x0076D3F0` | 854 | Zeichenketten/Konstanten (geprüft) |
| 157 | `SetSkillToolTipDamageAttribute` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 158 | `SetSkillToolTipSpecialEffect` | `0x00773520` | 5891 | Zeichenketten/Konstanten (geprüft) |
| 159 | `SetSkillToolTipFactorPoint` | `0x0076E870` | 8332 | Zeichenkette |
| 160 | `SetSkillToolTipFactorPercent` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 161 | `SetSkillToolTipEADamageAttribute` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 162 | `SetSkillToolTipBuyCost` | `0x00774C30` | 1839 | Zeichenkette |
| 163 | `SetSkillToolTipSpecificLevelUp` | `0x00775370` | 364 | Zeichenketten/Konstanten (geprüft) |
| 164 | `SetSummonsSkillToolTip` | `0x00775AA0` | 3386 | Zeichenketten/Konstanten (geprüft) |
| 165 | `SetSkillBookTooltip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 166 | `SetSkillScrollTooltip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 167 | `CBOpenSkillDescToolTip` | `0x007754E0` | 1278 | UI-Registrierung |
| 168 | `CBCloseSkillDescToolTip` | `0x0076C0E0` | 36 | gleiche Adresse wie `CBCloseSkillToolTip` (vom Linker zusammengefaltet) |
| 169 | `GetCostWithTax` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 170 | `_GetDurationTime` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 171 | `_GetBuffedSkill` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 172 | `_InitSkillTooltipColor` | `0x00772E80` | 91 | Zeichenkette |

145 von 173 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006c6cf0` (`0x006C6CF0`), `ctor_or_dtor_006ca5e0` (`0x006CA5E0`), `~AgcmUISkill2` (`0x006CA900`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBB0` | `m_pcsAgcmCharacter` | `+0x1596C` ist der Self-Character-Zeiger (`IsEnableSkill`) |
| `0xBC0` | `Verweis, dessen Vorhandensein `OnShowMsgBox` prüft` | `OnShowMsgBox` |
| `0xC00` | `Userdata/Steuerelement „Kaufen“` | `SetBuyMastery`: `[+0x50]` = Mastery-Index |
| `0x3074` | `m_pcsSelfCharacter` | `AddArchlordSkill` |
| `0x30D8` | `m_lLastSetMasteryIndex` | `SetUpgradeMasteryHeroic` setzt 7 |
| `0x30E0` | `Flag in `RefreshUsableOwnSkill` (Bedeutung vermutet)` | `RefreshUsableOwnSkill` |
| `0x3120 / 0x3122` | `Tooltip-Position (x, y; je 16 Bit)` | `OpenSkillToolTip` |

## Adressbereiche

| Quelldatei | Adressbereich |
|---|---|
| `AgcmUISkill2.cpp` | `0x006C6CF0`–`0x006CF530` |
| `AgcmUISkill2Tooltip.cpp` | `0x0076C110`–`0x0076E870` und `0x00772E80`–`0x007772C0` |

`AgcmHeroicSkill` (`0x00781060`–`0x00781980`) und `AgcmUISkillDragonScion` (`0x00782EE0`–`0x00784320`, `0x00788580`) sind eigene Klassen und nicht Teil dieser Analyse.

## Mastery-Indizes

`SetMastery` (`0x006CD0D0`) und `SetBuyMastery` (`0x006CB5B0`) verzweigen nach dem Mastery-Index: 0–4 normale Mastery-Fenster (`SetBuyMastery` verwirft Werte `> 4`), **6** Hochstufen-Skills (`SetMasteryHighLevel`, `0x006CB970`), **7** Heroic (ruft die Heroic-Funktionen `0x007824D0` in `SetMastery` bzw. `0x007827D0` in `SetUpgradeMasteryHeroic`, letztere speichert den Index in `+0x30D8`), **100** Archlord-Skills (`0x006CCE90`). Die Werte entsprechen `AGPMEVENT_SKILL_HIGHLEVEL/HEROIC/ARCHLORD_MASTERY_INDEX` der Quelle.
`AddHighLevelSkill` (`0x006CC7B0`) ruft `SetMasteryHighLevel(6)` und `SetUpgradeMasteryHighLevel`; `AddArchlordSkill` (`0x006CEB20`) ruft `SetMastery(100)` und `RefreshUsableOwnSkill(+0x3074)`.

## Callback-Registrierung in OnAddModule (0x006CEF50)

Die Reihenfolge entspricht der Quelle. Die Quelle meldet 37 Callbacks an, das Binary 35:

| Quelle | Binary |
|---|---|
| `CBBuySkillResult` (`SetCallbackBuyResult`) | registriert die Funktion `0x005759F0`, die nur prüft, dass alle drei Argumente gesetzt sind, und `TRUE` zurückgibt. Die Quelle löst im Erfolgsfall das UI-Ereignis `m_lEventSkillBuySuccess` aus; im Binary findet sich dieser Aufruf nicht. |
| `CBRefreshUpdateCharStatus` (Registrierung bei [`AgcmUICharacter`](AgcmUICharacter.md)) | nicht registriert |
| `CBUpdateSkillPoint` / `CBUpdateSkillExp` / `CBUpdateSkillPoint` | im Binary nur zwei Registrierungen mit `CBUpdateSkillPoint` |

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006C6F70`, `0x006CA920`, `0x006CB260`, `0x006CCE00`, `0x006CDD10`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**UserData** (12)

| Name | Id | Handler |
|---|---:|---|
| `SkillListGrid` |  | – |
| `SkillBuyListGrid` |  | – |
| `SkillUpgradeListGrid` |  | – |
| `SkillPoint` |  | – |
| `Skill_InvenMoney` |  | – |
| `Skill_ActiveBuyButton` |  | – |
| `Skill_ActiveUpgradeButton` |  | – |
| `Skill_ActiveTabButton` |  | – |
| `Skill_ActiveBuyTabButton` |  | – |
| `Skill_ActiveUpgradeTabButton` |  | – |
| `Skill_MainDialogMsg` |  | – |
| `Skill_IsActiveInitialize` |  | – |

**Ereignis** (56)

| Name | Id | Handler |
|---|---:|---|
| `Skill_NPCDialog_UI_Open` | 0 | – |
| `Skill_NPCDialog_UI_Close` | 0 | – |
| `Skill_UI_Open` | 0 | – |
| `Skill_UI_Close` | 0 | – |
| `Skill_Buy_UI_Open` | 0 | – |
| `Skill_Buy_UI_Close` | 0 | – |
| `Skill_HighLevel_UI_Open` | 0 | – |
| `Skill_HighLevel_UI_Close` | 0 | – |
| `Skill_HighLevel_Upgrade_UI_Open` | 0 | – |
| `Skill_HighLevel_Upgrade_UI_Close` | 0 | – |
| `Skill_Cast_Failed` | 0 | – |
| `Skill_Cast_InvalidTarget` | 0 | – |
| `Skill_Cast_NeedRequirement` | 0 | – |
| `Skill_Cast_NotEnoughHP` | 0 | – |
| `Skill_Cast_NotEnoughSP` | 0 | – |
| `Skill_Cast_NotEnoughMP` | 0 | – |
| `Skill_Cast_NotEnoughArrow` | 0 | – |
| `Skill_Cast_AlreadyUse` | 0 | – |
| `Skill_Cast_NotReadyCast` | 0 | – |
| `Skill_Cast_Miss` | 0 | – |
| `Skill_Cast_InvalidTargetToGather` | 0 | – |
| `Skill_Cast_NotEnoughProduct` | 0 | – |
| `Skill_SetMasteryTab_5` | 0 | – |
| `Skill_SelectedItem` | 0 | – |
| `Skill_UnSelectedItem` | 0 | – |
| `Skill_ActiveItem` | 0 | – |
| `Skill_DisableItem` | 0 | – |
| `Skill_BuySelectedItem` | 0 | – |
| `Skill_BuyUnSelectedItem` | 0 | – |
| `Skill_BuyActiveItem` | 0 | – |
| `Skill_BuyDisableItem` | 0 | – |
| `Skill_UpgradeSelectedItem` | 0 | – |
| `Skill_UpgradeUnSelectedItem` | 0 | – |
| `Skill_UpgradeActiveItem` | 0 | – |
| `Skill_UpgradeDisableItem` | 0 | – |
| `Skill_BuySuccess` | 0 | – |
| `Skill_LearnSuccess` | 0 | – |
| `Skill_UpgradeSuccess` | 0 | – |
| `Skill_ErrorNotEnoughMoney` | 0 | – |
| `Skill_ErrorInvalidClass` | 0 | – |
| `Skill_ErrorLowLevel` | 0 | – |
| `Skill_ErrorNotEnoughSkillPoint` | 0 | – |
| `Skill_ErrorNotSelectBuySkill` | 0 | – |
| `Skill_ErrorNotSelectUpgradeSkill` | 0 | – |
| `Skill_ErrorAlreadyLearnSkill` | 0 | – |
| `Skill_ConfirmBuySkill` |  | – |
| `Skill_ConfirmLearnSkill` |  | – |
| `Skill_ConfirmUpgradeSkill` |  | – |
| `Skill_ConfirmSkillInitialize` | 0 | – |
| `Skill_FailSkillInitialize` | 0 | – |
| `Skill_SkillInitialize_Success` | 0 | – |
| `Skill_SkillInitialize_Failed` | 0 | – |
| `Skill_SkillInitialize_MoneyFull` | 0 | – |
| `Skill_RollbackConfirm` |  | – |
| `Skill_ErrorNotEnoughHeroicPoint` | 0 | – |
| `Skill_ErrorNotEnoughCharismaPoint` | 0 | – |

**Anzeige** (24)

| Name | Id | Handler |
|---|---:|---|
| `SkillPoint` | 0 | `CBDisplaySkillPoint` |
| `SkillName` | 1 | `FUN_006c7fe0` |
| `SkillLevel` | 2 | `CBDisplaySkillLevel` |
| `SkillLevel2` | 3 | `CBDisplaySkillLevel` |
| `SkillPrice` | 4 | `CBDisplaySkillPrice` |
| `SkillTrainerClass` | 9 | `CBDisplaySkillTrainerClass` |
| `SkillMainDialog` | 10 | `CBDisplaySkillMainDialog` |
| `SkillInvenMoney` | 5 | `CBDisplayInvenMoney` |
| `SkillBuyButton` | 0xb | `CBDisplaySkillBuyButton` |
| `SkillSelectedName` | 0xc | `CBDisplaySelectedSkillName` |
| `SkillPointHighLevel0` | 0xd | `CBDisplaySkillPointHighLevel0` |
| `SkillPointHighLevel1` | 0xe | `CBDisplaySkillPointHighLevel1` |
| `SkillPointHighLevel2` | 0xf | `CBDisplaySkillPointHighLevel2` |
| `SkillPointHighLevel3` | 0x10 | `CBDisplaySkillPointHighLevel3` |
| `SkillPointHighLevel4` | 0x11 | `CBDisplaySkillPointHighLevel4` |
| `SkillPointHighLevel5` | 0x12 | `CBDisplaySkillPointHighLevel5` |
| `SkillPointHighLevel6` | 0x13 | `CBDisplaySkillPointHighLevel6` |
| `SkillPointHighLevel7` | 0x14 | `CBDisplaySkillPointHighLevel7` |
| `SkillPointHighLevel8` | 0x15 | – |
| `SkillPointHighLevel9` | 0x16 | – |
| `SkillPointHighLevel10` | 0x17 | – |
| `SkillLevelExp` | 6 | – |
| `SkillExpDegree` | 7 | – |
| `SkillExpDegreeMax` | 8 | – |

**Boolean** (4)

| Name | Id | Handler |
|---|---:|---|
| `Skill_ActiveBuyButton` |  | `CBIsActiveBuyButton` |
| `Skill_ActiveUpgradeButton` |  | `CBIsActiveUpgradeButton` |
| `Skill_ActiveRollbackButton` |  | `CBIsActiveRollbackButton` |
| `Skill_ActiveRollbackButton2` |  | `CBIsActiveRollbackButton2` |

**Funktion** (48)

| Name | Id | Handler |
|---|---:|---|
| `SkillSetMastery0` |  | `CBSetMastery0` |
| `SkillSetMastery1` |  | `CBSetMastery1` |
| `SkillSetMastery2` |  | `CBSetMastery2` |
| `SkillSetMastery3` |  | `CBSetMastery3` |
| `SkillSetMastery4` |  | `CBSetMastery4` |
| `SkillSetMasteryHighLevel` |  | `CBSetMasteryHighLevel` |
| `SkillSetMasteryHeroic` |  | `CBSetMasteryHeroic` |
| `SkillSetBuyMastery0` |  | `CBSetBuyMastery0` |
| `SkillSetBuyMastery1` |  | `CBSetBuyMastery1` |
| `SkillSetBuyMastery2` |  | `CBSetBuyMastery2` |
| `SkillSetBuyMastery3` |  | `CBSetBuyMastery3` |
| `SkillSetUpgradeMastery0` |  | `FUN_006cc380` |
| `SkillSetUpgradeMastery1` |  | `CBSetUpgradeMastery1` |
| `SkillSetUpgradeMastery2` |  | `CBSetUpgradeMastery2` |
| `SkillSetUpgradeMastery3` |  | `CBSetUpgradeMastery3` |
| `Skill_UI_Open` |  | `CBOpenSkillUI` |
| `Skill_BuyUI_Open` |  | `CBOpenSkillBuyUI` |
| `Skill_UpgradeUI_Open` |  | `FUN_006cc380` |
| `Skill_HighLevelUI_Open` |  | `CBOpenSkillHighLevelUI` |
| `Skill_HighLevelUpgradeUI_Open` |  | – |
| `Skill_HeroicUI_Open` |  | `CBOpenSkillHeroicUI` |
| `Skill_HeroicUpgradeUI_Open` |  | `CBOpenSkillHeroicSkillUpgradeUI` |
| `Skill_HighLevelUI_Close` |  | – |
| `Skill_HeroicUI_Close` |  | – |
| `Skill_SelectGrid` |  | – |
| `Skill_SelectBuyGrid` |  | `CBSelectBuySkillGrid` |
| `Skill_SelectUpgradeGrid` |  | `CBSelectUpgradeSkillGrid` |
| `Skill_Buy` |  | `CBBuySkill` |
| `Skill_Upgrade` |  | – |
| `Skill_Open_Tooltip` |  | `CBOpenSkillToolTip` |
| `Skill_Open_ButtonTooltip` |  | `CBOpenButtonSkillToolTip` |
| `Skill_Open_Buy_Tooltip` |  | `CBOpenBuySkillToolTip` |
| `Skill_Open_Buy_ButtonTooltip` |  | `CBOpenBuyButtonSkillToolTip` |
| `Skill_Open_Upgrade_Tooltip` |  | `CBOpenUpgradeSkillToolTip` |
| `Skill_Open_Upgrade_ButtonTooltip` |  | `CBOpenUpgradeButtonSkillToolTip` |
| `Skill_Close_Tooltip` |  | `FUN_0076c0e0` |
| `Skill_UpdateListItemStatus` |  | `CBUpdateListItemStatus` |
| `Skill_UpdateBuyListItemStatus` |  | `CBUpdateBuyListItemStatus` |
| `Skill_UpdateUpgradeListItemStatus` |  | `CBUpdateUpgradeListItemStatus` |
| `Skill_CloseSkillEventUI` |  | `CBCloseSkillEventUI` |
| `Skill_ToggleUI` |  | – |
| `Skill_OpenDescTooltip` |  | `CBOpenSkillDescToolTip` |
| `Skill_CloseDescTooltip` |  | `FUN_0076c0e0` |
| `Skill_TreeInitialize` |  | `CBSkillInitialize` |
| `Skill_SetFailInitializeText` |  | `CBSetFailInitializeText` |
| `Skill_SetConfirmInitializeText` |  | `CBSetConfirmInitializeText` |
| `Skill_InitializeOK` |  | `CBSkillInitializeOK` |
| `Skill_Rollback` |  | – |


## Abweichungen von der EP8-Quelle

- `CBBuySkillResult` ist im Binary ein Stub (kein `ThrowEvent` bei Erfolg).
- `CBRefreshUpdateCharStatus` wird nicht registriert; `CBUpdateSkillExp` hat keine eigene Registrierung.

## Grenzen

- Ein großer Teil der Methoden (Listen- und Fensterlogik, `CB…`-Callbacks der UI-Skripte, Tooltip-Teilfunktionen) ist nicht zugeordnet; sie haben wenige Zeichenketten und keine eindeutigen Aufrufbeziehungen.
- Der Stub-Befund beruht auf dem Dekompilat von `0x005759F0` und der Registrierung an dieser Stelle; ob der Compiler dort mehrere gleichartige Handler zusammengefaltet hat, ist nicht ausgeschlossen, ändert aber nichts am fehlenden Ereignis.
- Die Tooltip-Texte und ihre Reihenfolge wurden nicht verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 4, nicht im Client: 2, ohne Kandidat: 10, zugeordnet: 10.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SetSkillToolTipInfo` | 25 | `0x00776F10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCostWithTax` | 11 | `0x00772DC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillBookTooltip` | 108 | `0x00772920` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipEADamageAttribute` | 129 | `0x007723A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipFactorPercent` | 624 | `0x00770900` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipDamageAttribute` | 503 | `0x0076D750` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipName` | 81 | `0x0076C180` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveHeroicSkill` | 15 | `0x006CEBC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveArchlordSkill` | 10 | `0x006CEB60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMasteryArchlord` | 69 | `0x006CCE90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SetSkillToolTipInfo` (`0x007767E0`), `SetSkillToolTipCurrentLevel` (`0x00776C10`), `SetSkillToolTipNextLevel` (`0x00776C10`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUICharacter`](AgcmUICharacter.md)
- **Erwähnt in:** [`AgcmSkill`](AgcmSkill.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md)
