# AgcmUIItem (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIItem` (Inventar, Ausrüstung, Untergegenstände, privater Handel, NPC-Handel, Verkaufsbox, Erweitertes Inventar, Item-Tooltips) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIItem` (13 Quelldateien, eine Klasse). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 208 von 295 Quellmethoden sind zugeordnet (siehe Tabelle); die Zuordnung stützt sich auf bereits vorhandene Namen, Zeichenketten (Tooltip), den Aufrufgraphen und die Callback-Reihenfolge. Von den in diesem Durchgang neu zugeordneten Methoden (Zeichenketten und Graph) wurden 17 gegen Dekompilat und Quelle gelesen, darunter alle Preis- und Erweitertes-Inventar-Funktionen; die gelesenen waren ausnahmslos richtig, die übrigen sind nur über die Methode abgesichert.
- **NPC-Preis:** Die Anzeige rechnet `Preis × Anzahl`, schlägt den Steuersatz des Charakters auf und verdoppelt bei Mörder-Level `> 0` (Details unten).
- **UI-Namen:** Die Registrierungen der UI-Funktionen (69), Anzeigen (17) und Boolean-Werte (2) stimmen in Anzahl und Namen mit der Quelle überein; die Namen stehen in der Tabelle „UI-Namen“. Sechs Quellhandler des erweiterten Inventars und des Unterinventars teilen sich drei Binary-Adressen (identische Rümpfe).
- **Registrierungen:** Das Binary registriert 71 statt 75 Callbacks; es fehlen `SetSelfCharacterCB`, `ReleaseSelfCharacterCB`, `SelfUpdatePositionCB` und `CBRefreshUpdateCharStatus`.
- **Erweitertes Inventar:** UI-Namen `UI_ExpandedInventoryA/B` und Umschaltlogik wie in der Quelle.
- **Abweichungen:** die vier nicht registrierten Callbacks; sonst keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIItem.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006D7490` | 2875 | vtable/String |
| 1 | `OnDestroy` | `0x006D1250` | 75 | vtable/String |
| 2 | `OnInit` | `0x006D6EE0` | 1270 | vtable/String |
| 3 | `OnIdle` | `0x006D46E0` | 211 | vtable/String |
| 4 | `AddEvent` | `0x006D12A0` | 3487 | Zeichenkette |
| 5 | `AddFunction` | `0x006D47C0` | 2895 | Zeichenkette |
| 6 | `AddDisplay` | `0x006D6140` | 568 | Zeichenkette |
| 7 | `AddUserData` | `0x006D2040` | 1763 | Zeichenkette |
| 8 | `AddBoolean` | `0x006D5310` | 65 | Zeichenkette |
| 9 | `SetSelfCharacterCB` | `0x006D5360` | 799 | Callback-Registrierung |
| 10 | `CBReturnToLoginEnd` | `0x006D2730` | 91 | Callback-Registrierung |
| 11 | `ReleaseSelfCharacterCB` | `0x006D2790` | 455 | Callback-Registrierung |
| 12 | `CBRefreshUpdateCharStatus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 13 | `CBInventoryQuestAdd` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 14 | `CBInventoryQuestUpdate` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 15 | `CBUseItemResult` | `0x006D2960` | 159 | Callback-Registrierung |
| 16 | `CBInventoryQuestRemove` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 17 | `CBUIUpdateInventory` | `0x006D2A40` | 57 | Callback-Registrierung |
| 18 | `CBUIUpdateSubInventory` | `0x006D2A80` | 57 | Callback-Registrierung |
| 19 | `CBUIUpdateChargingInventoryA` | `0x006D2AC0` | 57 | Callback-Registrierung |
| 20 | `CBUIUpdateChargingInventoryB` | `0x006D2B00` | 57 | Callback-Registrierung |
| 21 | `CBUIUpdateInventoryQuest` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 22 | `CBUIUpdateEquip` | `0x006D2B40` | 49 | Callback-Registrierung |
| 23 | `CBUIUpdateTrade` | `0x006D2B80` | 94 | Callback-Registrierung |
| 24 | `CBUIUpdateTradeClient` | `0x006D2BE0` | 40 | Callback-Registrierung |
| 25 | `CBUIUpdateNPCTradeGrid` | `0x006D2C10` | 130 | Callback-Registrierung |
| 26 | `CBRemoveItemFromInventory` | `0x006D2CA0` | 68 | Callback-Registrierung |
| 27 | `CBRemoveItem` | `0x006D2CF0` | 47 | Callback-Registrierung |
| 28 | `CBOpenQuickBeltToolTip` | `0x006D2D20` | 42 | Callback-Registrierung |
| 29 | `CBCloseQuickBeltToolTip` | `0x006D2D50` | 33 | Callback-Registrierung |
| 30 | `CBCloseAllUIToolTip` | `0x006D2D80` | 62 | Callback-Registrierung |
| 31 | `CBUpdateItemFactor` | `0x006D6380` | 26 | Callback-Registrierung |
| 32 | `CheckItemLevel` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 33 | `IsItemDurable` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 34 | `IsItemPartDurable` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 35 | `CheckItemDurability` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 36 | `CheckItemDurability` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 37 | `GetADItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 38 | `GetADItemTemplate` | `0x006D31D0` | 38 | Aufrufgraph (geprüft) |
| 39 | `AddItemDurabilityZeroList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 40 | `RemoveItemDurabilityZeroList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 41 | `AddItemDurabilityUnder5PercentList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 42 | `RemoveItemDurabilityUnder5PercentList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 43 | `CBUpdateAlarmGrid` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 44 | `CBChangeOwner` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 45 | `CBPickupItemResult` | `0x006D33C0` | 203 | Callback-Registrierung |
| 46 | `CBAutoPickupItem` | `0x006D3490` | 20 | UI-Registrierung |
| 47 | `CBSetupItem` | `0x006D34B0` | 257 | Callback-Registrierung |
| 48 | `CBCheckUseItem` | `0x006D35E0` | 1319 | Callback-Registrierung |
| 49 | `CBIsActivePrivateTradeMemu` | `0x006D3B10` | 153 | UI-Registrierung |
| 50 | `CBRequestPrivateTrade` | `0x006D3BB0` | 288 | UI-Registrierung |
| 51 | `CBOpenReturnScroll` | `0x006D3CD0` | 36 | UI-Registrierung |
| 52 | `CBUseReturnScroll` | `0x006D3D00` | 20 | UI-Registrierung |
| 53 | `CBCancelReturnScroll` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 54 | `CBUpdateReturnScrollStatus` | `0x006D5710` | 254 | Callback-Registrierung |
| 55 | `CBUseReturnScrollResultFailed` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 56 | `CBUseReturnScroll` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 57 | `CBDisplayMessageData` | `0x006D5810` | 719 | UI-Registrierung |
| 58 | `CBKeydownESC` | `0x006D3D40` | 37 | Callback-Registrierung |
| 59 | `CBUseItemSuccess` | `0x006D5AF0` | 38 | Callback-Registrierung |
| 60 | `CBUseItemByTID` | `0x006D5B20` | 727 | Callback-Registrierung |
| 61 | `CBUseItemFailedByTID` | `0x006D3D70` | 98 | Callback-Registrierung |
| 62 | `CBUpdateReuseTimeForReverseOrb` | `0x006D5E00` | 149 | Callback-Registrierung |
| 63 | `CBUpdateReuseTimeForTransform` | `0x006D3DE0` | 252 | Callback-Registrierung |
| 64 | `CBInitReuseTimeForTransform` | `0x006D3EF0` | 249 | Callback-Registrierung |
| 65 | `CBUpdateFactorDurability` | `0x006D5EA0` | 68 | Callback-Registrierung |
| 66 | `SetCallbackSetTooltip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 67 | `SetCallbackMovedFromGuildWarehouse` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 68 | `SetCallbackRemoveSiegeWarGrid` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 69 | `SetCallbackGetItemTimeInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 70 | `SetCallbackGetItemStaminaTime` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 71 | `CBUpdateActionStatus` | `0x006D3FF0` | 293 | Callback-Registrierung |
| 72 | `CBUseReverseOrb` | `0x006D4120` | 59 | UI-Registrierung |
| 73 | `CBInventoryDoubleClick` | `0x006D4160` | 236 | UI-Registrierung |
| 74 | `CBEquipDoubleClick` | `0x006D4250` | 151 | UI-Registrierung |
| 75 | `CBDisplayUseAddMovementSkill` | `0x006D42F0` | 47 | UI-Registrierung |
| 76 | `CBDisplayUseAddAtkSpeedSkill` | `0x006D4320` | 47 | UI-Registrierung |
| 77 | `SetUseItemTime` | `0x006D4350` | 171 | Aufrufgraph (geprüft) |
| 78 | `CBUpdateCooldown` | `0x006D5EF0` | 392 | Callback-Registrierung |
| 79 | `UpdateCooldown` | `0x006D4400` | 212 | Aufrufgraph (geprüft) |
| 80 | `CBCharacterLevelUp` | `0x006D44E0` | 57 | Callback-Registrierung |
| 81 | `CBTooltipRegisterItem` | `0x006D73E0` | 127 | Callback-Registrierung |
| 82 | `CBUpdateTradeOptionGrid` | `0x006D4520` | 244 | Callback-Registrierung |
| 83 | `AddTooltipRegisterItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 84 | `GetTooltipRegisterItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 85 | `GetTooltipRegisterItemByTID` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 86 | `GetTooltipRegisterItemIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 87 | `ClearTooltipRegisterItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 88 | `SendChatRegisterItemRequest` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 89 | `OpenChattingItemTooltip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 90 | `StreamReadTooltipData` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 91 | `StreamReadTooltipDescData` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 92 | `SetTooltipList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 93 | `OpenToolTip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 94 | `OpenToolTip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 95 | `CloseToolTip` | `0x00626440` | 52 | Aufrufgraph (geprüft) |
| 96 | `CBOpenGridItemToolTip` | `0x0062BE20` | 133 | UI-Registrierung |
| 97 | `CBCloseGridItemToolTip` | `0x00626480` | 54 | UI-Registrierung |
| 98 | `SetItemToolTipInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 99 | `_SetItemToolTipEquip` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 100 | `_SetItemToolTipUsable` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 101 | `_SetItemToolTipDetailName` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 102 | `_SetItemToolTipDetailPrice` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 103 | `_SetItemToolTipDetailType` | `0x006264C0` | 257 | Zeichenketten/Konstanten (geprüft) |
| 104 | `_SetItemToolTipDetailRank` | `0x00628620` | 640 | Zeichenketten/Konstanten (geprüft) |
| 105 | `_SetItemToolTipDetailRequireLevel` | `0x006265D0` | 397 | Zeichenketten/Konstanten (geprüft) |
| 106 | `_SetItemToolTipDetailRequireRace` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 107 | `_SetItemToolTipDetailRequireClass` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 108 | `_SetItemToolTipDetailEnableEquipRace` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 109 | `_SetItemToolTipDetailEnableEquipClass` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 110 | `_SetItemToolTipDetailWeaponDamage` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 111 | `_SetItemToolTipDetailWeaponSpeed` | `0x006268B0` | 375 | Zeichenketten/Konstanten (geprüft) |
| 112 | `_SetItemToolTipDetailDurability` | `0x00626A30` | 441 | Zeichenketten/Konstanten (geprüft) |
| 113 | `_SetItemToolTipDetailHeroicDamage` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 114 | `_SetItemToolTipDetailHeroicDefense` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 115 | `SetItemToolTipDetail` | `0x0062A280` | 5267 | Zeichenkette |
| 116 | `SetItemToolTipName` | `0x00628940` | 1538 | Zeichenketten/Konstanten (geprüft) |
| 117 | `SetItemToolTipPrice` | `0x00626E70` | 816 | Zeichenkette |
| 118 | `SetItemToolTipConvertAttrInfo` | `0x00628F50` | 1695 | Zeichenketten/Konstanten (geprüft) |
| 119 | `SetItemConvertIcon` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 120 | `SetItemToolTipSpiritStoneInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 121 | `SetItemToolTipRingInfo` | `0x00627850` | 714 | Zeichenketten/Konstanten (geprüft) |
| 122 | `SetItemToolTipAmuletInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 123 | `SetItemToolTipCashInfo` | `0x006297E0` | 132 | Zeichenkette |
| 124 | `SetItemToolTipTimeInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 125 | `_GetItemSecondCategoryName` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 126 | `_CollectClassNames` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 127 | `_IsEnableRace` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 128 | `_IsEnableClass` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 129 | `_InitTooltipColor` | `0x00627F40` | 253 | Zeichenkette |
| 130 | `IsCashItemByPPCard` | `0x00628040` | 56 | Aufrufgraph (geprüft) |
| 131 | `GetToolTipColor` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 132 | `CalcTooltipPos` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 133 | `CBEquipMoveItem` | `0x00707C00` | 171 | UI-Registrierung |
| 134 | `CBEquipDragDropBase` | `0x00707CB0` | 147 | UI-Registrierung |
| 135 | `CBEquipItem` | `0x00707D50` | 47 | Callback-Registrierung |
| 136 | `CBUnEquipItem` | `0x00707D80` | 31 | Callback-Registrierung |
| 137 | `SetUpdateCharStatus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 138 | `UpdateEquipSlotGrid` | `0x00708270` | 237 | Aufrufgraph (geprüft) |
| 139 | `UpdateEquipSlot` | `0x00708190` | 209 | Aufrufgraph (geprüft) |
| 140 | `UpdateEquipSlotEnable` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 141 | `UpdateEquipSlotEnable` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 142 | `IsUsableItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 143 | `IsAlertItemDurationUnder20` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 144 | `GetEquipSlotMaskEvent` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 145 | `IsEnableUnEquipItem` | `0x00707F80` | 235 | Zeichenketten/Konstanten (geprüft) |
| 146 | `CBInventoryMoveItem` | `0x0078ABB0` | 1521 | UI-Registrierung |
| 147 | `CBInventoryMoveEndItem` | `0x0078A4D0` | 173 | UI-Registrierung |
| 148 | `CBInventoryUIUpdate` | `0x0078AB30` | 126 | UI-Registrierung |
| 149 | `OpenInventory` | `0x0078A580` | 71 | Aufrufgraph (geprüft) |
| 150 | `CBInventoryOpenInvenLayer` | `0x0078A5D0` | 102 | UI-Registrierung |
| 151 | `CBDisplayInventoryMoney` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 152 | `CBUpdateInventoryMoney` | `0x0078A640` | 106 | Callback-Registrierung |
| 153 | `CBUseItem` | `0x0078A6B0` | 151 | UI-Registrierung |
| 154 | `CBUIInventoryFull` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 155 | `CBUIInventoryNotEnoughSpaceToGetGhelld` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 156 | `CBUIInventoryDropItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 157 | `CBUIInventoryDropGhelld` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 158 | `CBUIInventoryDropGhelld` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 159 | `CBDragDropItem` | `0x0078A750` | 139 | UI-Registrierung |
| 160 | `CBDropMoneyToField` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 161 | `CBDropMoneyToFieldYes` | `0x0078A7E0` | 134 | UI-Registrierung |
| 162 | `CBDropMoneyToFieldCancel` | `0x0078A870` | 69 | UI-Registrierung |
| 163 | `CBReturnConfirmCancelItemFromAuction` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 164 | `CBSplitItemInventory` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 165 | `CBWasteDragDropItem` | `0x0078A930` | 376 | UI-Registrierung |
| 166 | `CBUIInventoryDestroyItem` | `0x0078AAF0` | 61 | UI-Registrierung |
| 167 | `CBInventorySmallLayer0` | `0x0078BF00` | 214 | UI-Registrierung |
| 168 | `CBInventorySmallLayer1` | `0x0078BFE0` | 214 | UI-Registrierung |
| 169 | `CBInventorySmallLayer2` | `0x0078C0C0` | 214 | UI-Registrierung |
| 170 | `CBInventorySmallLayer3` | `0x0078C1A0` | 214 | UI-Registrierung |
| 171 | `CBSubInventoryMoveItem` | `0x007405B0` | 1401 | UI-Registrierung |
| 172 | `CBSubInventoryMoveEndItem` | `0x00740320` | 121 | uireg |
| 173 | `CBSubInventoryUIUpdate` | `0x00740BA0` | 126 | UI-Registrierung |
| 174 | `CBSubInventoryOpenInvenLayer` | `0x007403A0` | 102 | UI-Registrierung |
| 175 | `CBDragDropItemToSubInventory` | `0x00740410` | 139 | UI-Registrierung |
| 176 | `CBToggleAutoGetDropItem` | `0x00741380` | 274 | UI-Registrierung |
| 177 | `CBGetBtnAutoPickUp` | `0x00741800` | 46 | UI-Registrierung |
| 178 | `IsPetItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 179 | `InitializeAutoPickup` | `0x007414A0` | 77 | Aufrufgraph (geprüft) |
| 180 | `OpenSubInventory` | `0x00740B30` | 100 | Aufrufgraph (geprüft) |
| 181 | `CloseSubInventory` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 182 | `EnableSubInventory` | `0x00740510` | 86 | as-register |
| 183 | `DisableSubInventory` | `0x00740570` | 62 | as-register |
| 184 | `CBClosePrivateTradeUI` | `0x0074CFC0` | 56 | Callback-Registrierung |
| 185 | `CBDisplayPrivateTraderName` | `0x0074D000` | 88 | UI-Registrierung |
| 186 | `CBDisplayRequestPrivateTrade` | `0x0074D060` | 88 | UI-Registrierung |
| 187 | `CBDisplayPrivateTradeSetName` | `0x0074D0C0` | 65 | UI-Registrierung |
| 188 | `CBDisplayPrivateTradeSetClientName` | `0x0074D110` | 65 | UI-Registrierung |
| 189 | `CBDisplayPrivateTradeGhelld` | `0x0074D160` | 64 | UI-Registrierung |
| 190 | `CBDisplayPrivateTradeClientGhelld` | `0x0074D1A0` | 64 | UI-Registrierung |
| 191 | `CBUIOpenPrivateTradeYesNo` | `0x0074D1E0` | 97 | Callback-Registrierung |
| 192 | `CBUIClosePrivateTradeYesNo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 193 | `CBUIOpenPrivateTrade` | `0x0074D250` | 363 | Callback-Registrierung |
| 194 | `CBUIClosePrivateTrade` | `0x0074D3C0` | 323 | Callback-Registrierung |
| 195 | `CBRequestCancel` | `0x0074D510` | 84 | UI-Registrierung |
| 196 | `CBPrivateTradeAccept` | `0x0074D570` | 249 | UI-Registrierung |
| 197 | `CBPrivateTradeReject` | `0x0074D670` | 77 | UI-Registrierung |
| 198 | `CBPrivateTradeMoveItem` | `0x0074DB40` | 802 | UI-Registrierung |
| 199 | `CBPrivateTradeUpdateMoney` | `0x0074D6C0` | 117 | UI-Registrierung |
| 200 | `CBPrivateTradeLock` | `0x0074D740` | 15 | UI-Registrierung |
| 201 | `CBPrivateTradeUnlock` | `0x0074D750` | 15 | UI-Registrierung |
| 202 | `CBPrivateTradeCancel` | `0x0074D760` | 42 | UI-Registrierung |
| 203 | `CBPrivateTradeUpdateClientLock` | `0x0074D790` | 63 | Callback-Registrierung |
| 204 | `CBPrivateTradeActiveReadyToExchange` | `0x0074D7D0` | 32 | Callback-Registrierung |
| 205 | `CBPrivateTradeReadyToExchange` | `0x0074D7F0` | 70 | UI-Registrierung |
| 206 | `CBPrivateTradeClientReadyToExchange` | `0x0074D840` | 32 | Callback-Registrierung |
| 207 | `CBPrivateTradeRequestRefuseUser` | `0x0074DE70` | 257 | Callback-Registrierung |
| 208 | `CBPrivateTradeMSGComplete` | `0x0074DF80` | 44 | Callback-Registrierung |
| 209 | `CBPrivateTradeMSGCancel` | `0x0074DFB0` | 44 | Callback-Registrierung |
| 210 | `CBPrivateTradeUpdateGhelld` | `0x0074D860` | 63 | Callback-Registrierung |
| 211 | `CBPrivateTradeUpdateClientGhelld` | `0x0074D8A0` | 63 | Callback-Registrierung |
| 212 | `_CheckBoundItemReleaseTradeCheck` | `0x0074D8E0` | 216 | Aufrufgraph (geprüft) |
| 213 | `_CheckSupportItemDuplicate` | `0x0074D9C0` | 111 | Aufrufgraph (geprüft) |
| 214 | `_AddSupportItem` | `0x0074DFE0` | 111 | Aufrufgraph (geprüft) |
| 215 | `_SupportItemCount` | `0x0074DA30` | 69 | Aufrufgraph (geprüft) |
| 216 | `_InitPrivateOptionItem` | `0x0074DA80` | 114 | Aufrufgraph (geprüft) |
| 217 | `OnSendPrivateTradeCancel` | `0x0074DB00` | 63 | Zeichenketten/Konstanten (geprüft) |
| 218 | `CBNPCTradeUIOpen` | `0x007894C0` | 137 | von Hand geprüft |
| 219 | `CBNPCTradeMoveItem` | `0x00789550` | 163 | UI-Registrierung |
| 220 | `CBNPCTradeUIOpen` | `0x00789600` | 157 | von Hand geprüft |
| 221 | `CBNPCTradeUIClose` | `0x007896A0` | 161 | UI-Registrierung |
| 222 | `CBNPCTradeOpenNextLayer` | `0x00789750` | 152 | UI-Registrierung |
| 223 | `CBNPCTradeOpenPrevLayer` | `0x007897F0` | 87 | UI-Registrierung |
| 224 | `CBNPCTradeInitLayer` | `0x00789850` | 63 | UI-Registrierung |
| 225 | `CBUINPCTradeMSGFullInven` | `0x00789890` | 32 | Callback-Registrierung |
| 226 | `CBUINPCTradeMSGConfirmBuy` | `0x0078A220` | 257 | von Hand geprüft |
| 227 | `CBUINPCTradeMSGConfirmBuy` | `0x007898B0` | 140 | von Hand geprüft |
| 228 | `CBUINPCTradeMSGConfirmBuyStackCountOK` | `0x00789940` | 223 | UI-Registrierung |
| 229 | `CBUINPCTradeMSGConfirmBuyStackCountCancel` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 230 | `CBUINPCTradeMSGConfirmSell` | `0x00789A20` | 266 | UI-Registrierung |
| 231 | `CBUINPCTradeMSGConfirmSell` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 232 | `CBUINPCTradeMSGNotEnoughGhelld` | `0x00789B30` | 32 | Callback-Registrierung |
| 233 | `CBUINPCTradeMSGNotEnoughCharisma` | `0x00789B50` | 39 | Callback-Registrierung |
| 234 | `CBUINPCTradeMSGNotEnoughShrineCoin` | `0x00789B80` | 39 | Callback-Registrierung |
| 235 | `CBUINPCTradeMSGNotEnoughSpaceToGetGhelld` | `0x00789BB0` | 32 | Callback-Registrierung |
| 236 | `SelfUpdatePositionCB` | `0x00789BD0` | 253 | Callback-Registrierung |
| 237 | `CBBuyItemDirect` | `0x0078A330` | 131 | UI-Registrierung |
| 238 | `CBNPCTradeSuccess` | `0x00789CD0` | 39 | Callback-Registrierung |
| 239 | `CBSplitItemNPCTrade` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 240 | `CBNPCTradeDeleteGrid` | `0x00789D00` | 69 | Callback-Registrierung |
| 241 | `OnOpenMsgBoxConfirmBuyNPCTradeItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 242 | `OnSendBuyNPCTradeItem` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 243 | `OnCheckEquipEnable` | `0x0078A3C0` | 86 | Aufrufgraph (geprüft) |
| 244 | `OnCheckUseEnable` | `0x0078A420` | 75 | von Hand geprüft |
| 245 | `OnCheckUseEnable` | `0x0078A470` | 84 | von Hand geprüft |
| 246 | `GetPriceNPCTradeItem` | `0x00789D50` | 226 | von Hand geprüft |
| 247 | `IsHaveMurdererLevel` | `0x0078A040` | 93 | von Hand geprüft |
| 248 | `GetMurdererLevel` | `0x00789E40` | 67 | Aufrufgraph (geprüft) |
| 249 | `_CheckEnableNPCTradeItem` | `0x00789E90` | 166 | Zeichenkette |
| 250 | `_CheckIsMurderer` | `0x00789F40` | 85 | von Hand geprüft |
| 251 | `_MakeConfirmMsgBuyNPCTradeItem` | `0x0078A0A0` | 369 | Zeichenkette |
| 252 | `_CalcItemPriceByMurdererLevel` | `0x00789FA0` | 78 | von Hand geprüft |
| 253 | `_NoticeBySystemMessage` | `0x00789FF0` | 76 | von Hand geprüft |
| 254 | `CBSalesBox2Add` | `0x0078B7F0` | 389 | Callback-Registrierung |
| 255 | `CBSalesBox2Remove` | `0x0078B3E0` | 312 | Callback-Registrierung |
| 256 | `CBSalesBox2Update` | `0x0078B520` | 100 | Callback-Registrierung |
| 257 | `CBSetFocusOnBoard` | `0x0078B590` | 62 | Callback-Registrierung |
| 258 | `CBKillFocusOnBoard` | `0x0078B5D0` | 15 | Callback-Registrierung |
| 259 | `CBSalesBox2Open` | `0x0078B5E0` | 121 | UI-Registrierung |
| 260 | `CBSalesBoxMoveItem` | `0x0078B980` | 301 | UI-Registrierung |
| 261 | `CBSalesBox2ClickCancelCompleteButton` | `0x0078BAB0` | 153 | UI-Registrierung |
| 262 | `CBSalesBox2Add` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 263 | `CBSalesBox2Remove` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 264 | `CBSalesBox2Update` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 265 | `CBUpdateSalesBoxGrid` | `0x0078B6B0` | 35 | Callback-Registrierung |
| 266 | `CBSetQuantity4SalesBox` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 267 | `CBSetPrice4SalesBox` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 268 | `GetSalesOfIndex` | `0x0078BB50` | 65 | Aufrufgraph (geprüft) |
| 269 | `CBDisplaySalesBox2ItemName` | `0x0078BBA0` | 95 | UI-Registrierung |
| 270 | `CBDisplaySalesBox2ItemPrice` | `0x0078BC00` | 71 | UI-Registrierung |
| 271 | `CBDisplaySalesBox2ItemTime` | `0x0078BC50` | 228 | UI-Registrierung |
| 272 | `CBDisplaySalesBox2OkCancel` | `0x0078BD40` | 126 | UI-Registrierung |
| 273 | `CBDisplaySalesBox2SalesOn` | `0x0078BDC0` | 138 | UI-Registrierung |
| 274 | `CBDisplaySalesBox2SalesComplete` | `0x0078BE60` | 138 | UI-Registrierung |
| 275 | `CBIsEnableSalesBox2Button` | `0x0078B780` | 60 | UI-Registrierung |
| 276 | `CBChargingInventoryAMoveItem` | `0x00788E20` | 1303 | uireg |
| 277 | `CBChargingInventoryAMoveEndItem` | `0x00740320` | 121 | gleiche Adresse wie `CBSubInventoryMoveEndItem` (vom Linker zusammengefaltet) |
| 278 | `CBChargingInventoryUIUpdate` | `0x00789450` | 107 | UI-Registrierung |
| 279 | `CBChargingInventoryAOpenInvenLayer` | `0x00788B40` | 102 | UI-Registrierung |
| 280 | `CBDragDropItemToChargingInventoryA` | `0x00788CF0` | 139 | uireg |
| 281 | `OpenChargingInventory` | `0x00789340` | 266 | Zeichenkette |
| 282 | `CloseChargingInventory` | `0x00788BB0` | 78 | Aufrufgraph (geprüft) |
| 283 | `EnableChargingInventoryA` | `0x00788DD0` | 69 | von Hand geprüft |
| 284 | `DisableChargingInventory` | `0x00788C00` | 119 | von Hand geprüft |
| 285 | `CBChargingInventoryBMoveItem` | `0x00788E20` | 1303 | gleiche Adresse wie `CBChargingInventoryAMoveItem` (vom Linker zusammengefaltet) |
| 286 | `CBChargingInventoryBMoveEndItem` | `0x00740320` | 121 | gleiche Adresse wie `CBSubInventoryMoveEndItem` (vom Linker zusammengefaltet) |
| 287 | `CBChargingInventoryBOpenInvenLayer` | `0x00788C80` | 102 | UI-Registrierung |
| 288 | `CBDragDropItemToChargingInventoryB` | `0x00788CF0` | 139 | gleiche Adresse wie `CBDragDropItemToChargingInventoryA` (vom Linker zusammengefaltet) |
| 289 | `EnableChargingInventoryB` | `0x00788D80` | 69 | von Hand geprüft |
| 290 | `CBAskReallyConvert` | `0x0078B1B0` | 95 | Callback-Registrierung |
| 291 | `CBConvertResult` | `0x0078B210` | 164 | Callback-Registrierung |
| 292 | `CBSendConvertItem` | `0x0078B2F0` | 181 | UI-Registrierung |
| 293 | `CBCancelConvertItem` | `0x0078B3B0` | 37 | UI-Registrierung |
| 294 | `CBOpenDuplicateInven` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |

208 von 295 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `unk_00626290` (`0x00626290`), `unk_006281a0` (`0x006281A0`), `ctor_or_dtor_006d82c0` (`0x006D82C0`), `ctor_or_dtor_006d83f0` (`0x006D83F0`), `~AgcmUIItem` (`0x006D8E60`), `CBNPCTradeUIOpen_007894c0` (`0x007894C0`), `CBNPCTradeUIOpen_00789600` (`0x00789600`), `CBUINPCTradeMSGConfirmBuy_0078a220` (`0x0078A220`), `OnCheckUseEnable_0078a420` (`0x0078A420`), `OnCheckUseEnable_0078a470` (`0x0078A470`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB9C` | `m_pcsAgcmCharacter` | `+0x1596C` ist der Self-Character-Zeiger (`OpenSubInventory`, `_SupportItemCount`) |
| `0xED0` | `Grid des privaten Handels` | `_CheckBoundItemReleaseTradeCheck` (Gegenstände durchlaufen) |
| `0xF20 + Slot × 0x24` | `Ausrüstungs-Grids (AgpdGrid je Slot)` | `UpdateEquipSlot` |
| `0x4E9C / 0x4EA0` | `m_bUIOpenInventory / Ereignis „Inventar öffnen“` | `OpenInventory` |
| `0x4F50 / 0x4F54` | `m_bUIOpenSubInventory / Ereignis „Unterinventar öffnen“` | `OpenSubInventory` |
| `0x11068 / 0x1106C` | `m_pcsUIChargingInventoryA / B` | `EnableChargingInventoryA/B`, `DisableChargingInventory` |

## Adressbereiche

Die Klasse ist auf mehrere Übersetzungseinheiten verteilt; die Bereiche ergeben sich aus gemeinsamen Zeichenketten und den benachbarten Klassen:

| Quelldatei | Adressbereich |
|---|---|
| `AgcmUIItemTooltip.cpp` | `0x00626290`–`0x0062C110` |
| `AgcmUIItem.cpp` | `0x006D1250`–`0x006D8E80` |
| `AgcmUIEquip.cpp` | `0x00707C00`–`0x00708A70` |
| `AgcmUISubInventory.cpp` | `0x007403A0`–`0x00742610` |
| `AgcmUIPrivateTrade.cpp` | `0x0074CFC0`–`0x0074EBD0` |
| `AgcmUIInventory/ChargingInventory/NPCTrade/SalesBox.cpp` | `0x00788B40`–`0x0078C280` (gemeinsamer Bereich) |

## NPC-Preisanzeige (AgcmUINPCTrade)

Der Client zeigt beim NPC-Handel den Preis nach dieser Rechnung an (`GetPriceNPCTradeItem`, `0x00789D50`, gegen die Quelle gelesen):

1. Einzelpreis = `AgpmItem::GetNPCPrice(item)` (`0x0053B500`, bit-gecastet als Float, siehe Bericht NPC-Handel); mit Stapelzahl `> 0`: `(int)(Preis × Anzahl)`.
2. Steuersatz = `AgpmCharacter::GetTaxRatio(self)` (`0x0058A7F0`, löst `EnumCallback(0x61)` aus); bei Satz `> 0`: `Summe + Summe × Satz / 100`.
3. `_CalcItemPriceByMurdererLevel` (`0x00789FA0`) verdoppelt den Preis, wenn der eigene Charakter einen Mörder-Level `> 0` hat (`_CheckIsMurderer`, `0x00789F40`; `GetMurdererLevel`, `0x00789E40`).

Wer den Serverpreis gegen die Anzeige prüft, muss also Steuer und Mörder-Faktor einrechnen; `IsHaveMurdererLevel` (`0x0078A040`) vergleicht den eigenen Level mit einer Mindestgrenze, `_NoticeBySystemMessage` (`0x00789FF0`) zeigt den Text zu einer Meldungs-ID im Chat.

## Erweitertes Inventar (AgcmUIChargingInventory)

`EnableChargingInventoryA` (`0x00788DD0`) und `…B` (`0x00788D80`) holen bei Bedarf die UIs `UI_ExpandedInventoryA` bzw. `UI_ExpandedInventoryB` (Zeiger `+0x11068`/`+0x1106C`), rufen `DisableChargingInventory` (`0x00788C00`, deaktiviert beide Fenster über `[+0x98]+0x1A0`) und aktivieren dann das gewählte Fenster. Stimmt mit der Quelle überein.

## Callback-Registrierung in OnAddModule (0x006D7490)

Die Registrierungen stehen im Binary in der Reihenfolge der Quelle, es fehlen aber vier Einträge: Die Quelle meldet **75** Callbacks an, das Binary **71**. Nicht registriert werden im 2017er Build:

| Quelle | Wirkung |
|---|---|
| `SetSelfCharacterCB` | Registrierung bei `AgcmCharacter` (Eigener Charakter gesetzt) fehlt |
| `ReleaseSelfCharacterCB` | Registrierung (Eigener Charakter freigegeben) fehlt |
| `SelfUpdatePositionCB` | Registrierung (Position des eigenen Charakters) fehlt |
| `CBRefreshUpdateCharStatus` | Registrierung bei [`AgcmUICharacter`](AgcmUICharacter.md) fehlt |

Mehrere Quellhandler sind im Binary mit anderen Funktionen identisch zusammengefaltet: `CBInventoryQuestAdd/Remove/Update` zeigen alle auf `0x006D2A10`, `CBUseReturnScrollResultFailed` auf eine Stub-Funktion. Das ändert das Verhalten nicht.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006D12A0`, `0x006D2040`, `0x006D47C0`, `0x006D5310`, `0x006D6140`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Ereignis** (102)

| Name | Id | Handler |
|---|---:|---|
| `INV_OpenEvent` | 0 | – |
| `INV_CloseEvent` | 0 | – |
| `INV_OpenDropMoney` | 0 | – |
| `INV_CloseDropMoney` | 0 | – |
| `INV_EnableDropGhelld` | 0 | – |
| `INV_DisableDropGhelld` | 0 | – |
| `AC_CancelMessageBox` |  | [`AgcmShrine`](AgcmShrine.md):CBShrineTapScroe` |
| `INV_MSG_Full` | 0 | – |
| `INV_MSG_NOT_ENOUGH_SPACE_TO_GET_GHELLD` | 0 | – |
| `INV_MSG_GET_ITEM` | 0 | – |
| `INV_MSG_Drop_ITEM` |  | `CBUIInventoryDestroyItem` |
| `INV_MSG_Drop_Ghelld` |  | `Element::GetSize` |
| `Bank_OpenEvent` | 0 | – |
| `Bank_CloseEvent` | 0 | – |
| `PT_OpenRequest` | 0 | – |
| `PT_CloseRequest` | 0 | – |
| `PT_OpenConfirmEvent` | 0 | – |
| `PT_CloseConfirmEvent` | 0 | – |
| `PT_OpenUIEvent` | 0 | – |
| `PT_CloseUIEvent` | 0 | – |
| `PT_ClientLock` | 0 | – |
| `PT_ClientUnlock` | 0 | – |
| `PT_ActiveReadyToExchange` | 0 | – |
| `PT_ClientReadyToExchange` | 0 | – |
| `PTMSG_InvenFull` | 0 | – |
| `PTMSG_TradeComplete` | 0 | – |
| `PTMSG_TradeCancel` | 0 | – |
| `PTMSG_Error` | 0 | – |
| `NPCT_OpenUI` | 0 | – |
| `NPCT_CloseUI` | 0 | – |
| `NPCT_InitLayer` | 0 | – |
| `SalesBox_Open` | 0 | – |
| `SalesBox_Close` | 0 | – |
| `SalesBox2_Add` | 0 | – |
| `SalesBox2_Remove` | 0 | – |
| `SalesBox2_Update` | 0 | – |
| `SalesBox2_ButtonOn` | 0 | – |
| `SalesBox2_ButtonOff` | 0 | – |
| `SubInv_OpenEvent` | 0 | – |
| `SubInv_CloseEvent` | 0 | – |
| `ExpandedInvA_OpenEvent` | 0 | – |
| `ExpandedInvA_CloseEvent` | 0 | – |
| `ExpandedInvB_OpenEvent` | 0 | – |
| `ExpandedInvB_CloseEvent` | 0 | – |
| `NPCTMSG_InvenFull` | 0 | – |
| `NPCTMSG_ConfirmBuy` |  | – |
| `NPCTMSG_ConfirmBuyStackCount` | 0 | – |
| `NPCTMSG_ConfirmSell` |  | – |
| `NPCTMSG_NotEnoughGhelld` | 0 | – |
| `NPCTMSG_NotEnoughCharisma` | 0 | – |
| `NPCTMSG_NotEnoughShrineCoin` | 0 | – |
| `NPCTMSG_NotEnoughSpaceToGetGhelld` | 0 | – |
| `NPCTMSG_TradeSuccess` | 0 | – |
| `Shrine_ItemBuyConfirmOpen_Event` | 0 | – |
| `Shrine_ItemBuyConfirmClose_Event` | 0 | – |
| `IC_ASK_CONVERT` | 0 | – |
| `IC_RESULT_SUCCESS` | 0 | – |
| `IC_RESULT_FAIL` | 0 | – |
| `IC_RESULT_RUIN` | 0 | – |
| `IC_RESULT_DESTROY_ITEM` | 0 | – |
| `IC_RESULT_DIFFER_RANK` | 0 | – |
| `IC_RESULT_DIFFER_TYPE` | 0 | – |
| `IC_RESULT_ALREADY_FULL` | 0 | – |
| `IC_RESULT_NOT_EQUIP_ITEM` | 0 | – |
| `IC_RESULT_EGO_ITEM` | 0 | – |
| `Item_GetItem` | 0 | – |
| `Item_GetMoney` | 0 | – |
| `Item_SuccessPickupItem` | 0 | – |
| `Item_SuccessPickupMoney` | 0 | – |
| `Item_SuccessPickupPCBangBonusMoney` | 0 | – |
| `Item_FailPickupItem` | 0 | – |
| `Item_FailPickupMoney` | 0 | – |
| `Item_AutoPickupItem` | 0 | – |
| `Item_UseSuccessReverseOrb` | 0 | – |
| `Item_UseFailReverseOrb` | 0 | – |
| `Item_UseAddMovementSkill` | 0 | – |
| `Item_UseAddAtkSpeedSkill` | 0 | – |
| `Item_ExchangeBuffSkill` | 0 | – |
| `Item_IgnoreBuffSkill` | 0 | – |
| `Item_TradeFailForBoundItem` | 0 | – |
| `Item_ConfirmDestroyItem` |  | – |
| `Item_ConfirmDestroyCashItem` |  | `CBUIInventoryDestroyItem` |
| `Item_TradeFailForUsingCashItem` | 0 | – |
| `EquipStatusHeadOn` | 0 | – |
| `EquipStatusHandOn` | 0 | – |
| `EquipStatusBodyOn` | 0 | – |
| `EquipStatusLegsOn` | 0 | – |
| `EquipStatusFootOn` | 0 | – |
| `EquipStatusShieldOn` | 0 | – |
| `EquipStatusWeaponOn` | 0 | – |
| `EquipStatusHeadOff` | 0 | – |
| `EquipStatusHandOff` | 0 | – |
| `EquipStatusBodyOff` | 0 | – |
| `EquipStatusLegsOff` | 0 | – |
| `EquipStatusFootOff` | 0 | – |
| `EquipStatusShieldOff` | 0 | – |
| `EquipStatusWeaponOff` | 0 | – |
| `EquipStatusOpen` | 0 | – |
| `EquipStatusClose` | 0 | – |
| `BankSlotFull` | 0 | – |
| `ReverseOrbError` | 0 | – |
| `SubInven_GetBtnAutoPickUp` | 0 | – |

**UserData** (41)

| Name | Id | Handler |
|---|---:|---|
| `InventoryGrid` |  | – |
| `EquipGrid` |  | – |
| `InventoryQuestGrid` |  | – |
| `SalesBoxGrid` |  | – |
| `SalesBox2Grid` |  | – |
| `SalesBox2SalesOn` |  | – |
| `SalesBox2SalesComplete` |  | – |
| `SalesBox2SalesButtonEnable` |  | – |
| `NPCTradeGrid` |  | – |
| `PrivateTradeGrid` |  | – |
| `PrivateTradeGridEx` |  | – |
| `PrivateTradeClientGridEx` |  | – |
| `PrivateTradeClientGrid` |  | – |
| `InventoryMoney` |  | – |
| `PrivateTraderName` |  | – |
| `PT_Request` |  | – |
| `PrivateTradeSetName` |  | – |
| `PrivateTradeSetClientName` |  | – |
| `PrivateTradeGhelld` |  | – |
| `PrivateTradeClientGhelld` |  | – |
| `InventoryLayerIndex` |  | – |
| `SubInventoryLayerIndex` |  | – |
| `ExpandedInventoryALayerIndex` |  | – |
| `ExpandedInventoryBLayerIndex` |  | – |
| `아이템 메시지 데이타들` |  | – |
| `EquipSlotGridBody` |  | – |
| `EquipSlotGridHead` |  | – |
| `EquipSlotGridHands` |  | – |
| `EquipSlotGridLegs` |  | – |
| `EquipSlotGridFoot` |  | – |
| `EquipSlotGridHandLeft` |  | – |
| `EquipSlotGridHandRight` |  | – |
| `EquipSlotGridRing1` |  | – |
| `EquipSlotGridRing2` |  | – |
| `EquipSlotGridNecklace` |  | – |
| `EquipSlotGridRide` |  | – |
| `EquipSlotGridLancer` |  | – |
| `IsActiveReverseOrb` |  | – |
| `SubInventoryGrid` |  | – |
| `ExpandedInventoryAGrid` |  | – |
| `ExpandedInventoryBGrid` |  | – |

**Funktion** (69)

| Name | Id | Handler |
|---|---:|---|
| `Inventory_MoveItem` |  | `CBInventoryMoveItem` |
| `Inventory_MoveEndItem` |  | `CBInventoryMoveEndItem` |
| `Inventory_UIUpdate` |  | `CBInventoryUIUpdate` |
| `Inventory_UIUpdateLayer` |  | `CBInventoryOpenInvenLayer` |
| `Inventory_UseItem` |  | `CBUseItem` |
| `Inventory_DragDropItem` |  | `CBDragDropItem` |
| `Inventory_OpenDropMoneyUI` |  | `Element::GetSize` |
| `Inventory_DropMoneyYes` |  | `CBDropMoneyToFieldYes` |
| `Inventory_DropMoneyCancel` |  | `CBDropMoneyToFieldCancel` |
| `InventorySmall_Layer0` |  | `CBInventorySmallLayer0` |
| `InventorySmall_Layer1` |  | `CBInventorySmallLayer1` |
| `InventorySmall_Layer2` |  | `CBInventorySmallLayer2` |
| `InventorySmall_Layer3` |  | `CBInventorySmallLayer3` |
| `InventoryDoubleClick` |  | `CBInventoryDoubleClick` |
| `InventoryWaste_DragDropItem` |  | `CBWasteDragDropItem` |
| `Equip_MoveItem` |  | `CBEquipMoveItem` |
| `Equip_DragDropBase` |  | `CBEquipDragDropBase` |
| `Equip_DoubleClick` |  | `CBEquipDoubleClick` |
| `SubInventory_MoveItem` |  | `CBSubInventoryMoveItem` |
| `SubInventory_MoveEndItem` |  | `FUN_00740320` |
| `SubInventory_UIUpdate` |  | `CBSubInventoryUIUpdate` |
| `SubInventory_UIUpdateLayer` |  | `CBSubInventoryOpenInvenLayer` |
| `SubInventory_DragDropItem` |  | `CBDragDropItemToSubInventory` |
| `SubInventory_ToggleAutoGetDropItem` |  | `CBToggleAutoGetDropItem` |
| `ExpandedInventoryA_MoveItem` |  | `FUN_00788e20` |
| `ExpandedInventoryA_MoveEndItem` |  | `FUN_00740320` |
| `ExpandedInventory_UIUpdate` |  | `CBChargingInventoryUIUpdate` |
| `ExpandedInventoryA_UIUpdateLayer` |  | `CBChargingInventoryAOpenInvenLayer` |
| `ExpandedInventoryA_DragDropItem` |  | `FUN_00788cf0` |
| `ExpandedInventoryB_MoveItem` |  | `FUN_00788e20` |
| `ExpandedInventoryB_MoveEndItem` |  | `FUN_00740320` |
| `ExpandedInventoryB_UIUpdateLayer` |  | `CBChargingInventoryBOpenInvenLayer` |
| `ExpandedInventoryB_DragDropItem` |  | `FUN_00788cf0` |
| `NPCT_MoveItem` |  | – |
| `NPCT_UIOpen` |  | – |
| `NPCT_UIClose` |  | – |
| `NPCT_MoveNextLayer` |  | `CBNPCTradeOpenNextLayer` |
| `NPCT_MovePrevLayer` |  | `CBNPCTradeOpenPrevLayer` |
| `NPCT_InitLayer` |  | – |
| `NPCT_BuyStackCountOK` |  | `CBUINPCTradeMSGConfirmBuyStackCountOK` |
| `NPCT_BuyStackCountCancel` |  | `Element::GetSize` |
| `NPCT_BuyItemDirect` |  | `CBBuyItemDirect` |
| `PT_RequestCancel` |  | `CBRequestCancel` |
| `PT_Accept` |  | – |
| `PT_Reject` |  | – |
| `PT_MoveItem` |  | – |
| `PT_UpdateMoney` |  | – |
| `PT_Lock` |  | – |
| `PT_Unlock` |  | – |
| `PT_ReadyToExchange` |  | `CBPrivateTradeReadyToExchange` |
| `PT_Cancel` |  | – |
| `ItemAutoPickup` |  | – |
| `AC_SalesBox2Open` |  | `CBSalesBox2Open` |
| `AC_MoveToSalesBox` |  | – |
| `AC_SalesBox2CancelComplete` |  | `CBSalesBox2ClickCancelCompleteButton` |
| `AC_SalesBox2Add` |  | `FUN_0078b660` |
| `AC_SalesBox2Remove` |  | `FUN_0078b660` |
| `AC_SalesBox2Update` |  | `AgcmShrine::CBShrineTapScroe` |
| `AC_FunctionUIOpen` |  | `Element::GetSTRING` |
| `IC_ConvertItem` |  | – |
| `IC_CancelConvertItem` |  | `CBCancelConvertItem` |
| `Grid_OpenItemToolTip` |  | `CBOpenGridItemToolTip` |
| `Grid_CloseItemToolTip` |  | `CBCloseGridItemToolTip` |
| `PT_RequestTrade` |  | – |
| `Item_OpenReturnScrollUI` |  | `CBOpenReturnScroll` |
| `Item_UseReturnScroll` |  | `CBUseReturnScroll` |
| `Item_CancelReturnScroll` |  | `Element::GetSize` |
| `Item_UseReverseOrb` |  | `CBUseReverseOrb` |
| `Item_GetBtnAutoPickUp` |  | `CBGetBtnAutoPickUp` |

**Boolean** (2)

| Name | Id | Handler |
|---|---:|---|
| `IsActivePrivateTradeMemu` |  | `CBIsActivePrivateTradeMemu` |
| `IsEnableSalesBox2Button` |  | `CBIsEnableSalesBox2Button` |

**Anzeige** (17)

| Name | Id | Handler |
|---|---:|---|
| `InventoryMoney` | 0 | `FUN_006beae0` |
| `PrivateTraderName` | 1 | `CBDisplayPrivateTraderName` |
| `Diaplay_PT_Request` | 2 | `CBDisplayRequestPrivateTrade` |
| `ItemPickupName` | 3 | `CBDisplayMessageData` |
| `ItemPickupBonusMoney` | 4 | `CBDisplayMessageData` |
| `PrivateTradeSetName` | 5 | `CBDisplayPrivateTradeSetName` |
| `PrivateTradeSetClientName` | 6 | `CBDisplayPrivateTradeSetClientName` |
| `PrivateTradeGhelld` | 7 | `CBDisplayPrivateTradeGhelld` |
| `PrivateTradeClientGhelld` | 8 | `CBDisplayPrivateTradeClientGhelld` |
| `ItemUseAddMovementSkill` | 9 | `CBDisplayUseAddMovementSkill` |
| `ItemUseAddAtkSpeedSkill` | 10 | `CBDisplayUseAddAtkSpeedSkill` |
| `SalesBox2ItemName` | 0xb | `CBDisplaySalesBox2ItemName` |
| `SalesBox2ItemPrice` | 0xc | `CBDisplaySalesBox2ItemPrice` |
| `SalesBox2ItemTime` | 0xd | `CBDisplaySalesBox2ItemTime` |
| `SalesBox2SalesOn` | 0xe | `CBDisplaySalesBox2SalesOn` |
| `SalesBox2SalesComplete` | 0xf | `CBDisplaySalesBox2SalesComplete` |
| `SalesBox2SalesOkCancel` | 0x10 | `CBDisplaySalesBox2OkCancel` |


## Abweichungen von der EP8-Quelle

- `OnAddModule` registriert vier Callbacks der Quelle nicht (`SetSelfCharacterCB`, `ReleaseSelfCharacterCB`, `SelfUpdatePositionCB`, `CBRefreshUpdateCharStatus`).
- Ansonsten keine Abweichung in den gelesenen Funktionen.

## Grenzen

- Etwa ein Drittel der Methoden ist nicht zugeordnet, überwiegend Tooltip-Teilfunktionen (`_SetItemToolTipDetail*`, `SetItemToolTip*Info`), Haltbarkeitslisten und kleine UI-Callbacks; sie haben wenige Zeichenketten und keine eindeutigen Aufrufbeziehungen.
- Die Tooltip-Texte (Reihenfolge der Zeilen, Farben) wurden nicht verglichen.
- Die Adressbereiche der Quelldateien sind aus Zeichenketten und Nachbarklassen abgeleitet und nicht lückenlos belegt; Funktionen außerhalb der genannten Bereiche werden nicht erfasst.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 14, eingebaut: 10, gemeinsamer Rumpf: 5, nicht im Client: 13, ohne Kandidat: 27, zugeordnet: 26.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SendChatRegisterItemRequest` | 7 | `0x006D4620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTooltipRegisterItem` | 9 | `0x006D6760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAlertItemDurationUnder20` | 6 | `0x00708070` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemToolTipAmuletInfo` | 79 | `0x00627B20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemToolTipSpiritStoneInfo` | 144 | `0x006271A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipUsable` | 29 | `0x0062B8A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipEquip` | 79 | `0x0062B7A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsItemPartDurable` | 33 | `0x006D2EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnCheckUseEnable` | 22 | `0x0067D740` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipDetailEnableEquipClass` | 6 | `0x006288F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipDetailEnableEquipRace` | 6 | `0x006288A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemToolTipInfo` | 29 | `0x0062BA80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenChattingItemTooltip` | 17 | `0x006D6C90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckItemLevel` | 8 | `0x006D2DC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPetItem` | 5 | `0x007404A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBSetPrice4SalesBox` | 30 | `0x0078B6E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemConvertIcon` | 102 | `0x00629600` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipDetailHeroicDefense` | 47 | `0x00626D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenToolTip` | 2 | `0x0062BAD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ClearTooltipRegisterItem` | 14 | `0x006D6990` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddTooltipRegisterItem` | 30 | `0x006D6CF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsItemDurable` | 33 | `0x006D2E20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateEquipSlotEnable` | 18 | `0x00708110` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemDurabilityUnder5PercentList` | 33 | `0x006D32E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemDurabilityZeroList` | 33 | `0x006D3200` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckItemDurability` | 20 | `0x006D2FD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `IsUsableItem` (`0x0073AF00`), `CheckItemDurability` (`0x006D5680`), `StreamReadTooltipData` (`0x00717B93`), `StreamReadTooltipDescData` (`0x00717B93`), `_SetItemToolTipDetailRequireRace` (`0x00629F20`), `_SetItemToolTipDetailRequireClass` (`0x00629F20`), `_SetItemToolTipDetailWeaponDamage` (`0x00626760`), `_SetItemToolTipDetailHeroicDamage` (`0x00626760`), `SetItemToolTipTimeInfo` (`0x00629F20`), `_CollectClassNames` (`0x00629F20`), `CBUINPCTradeMSGConfirmBuy` (`0x0072B6D0`), `CBUINPCTradeMSGConfirmSell` (`0x0073AF00`), `OnSendBuyNPCTradeItem` (`0x00748459`), `OnCheckUseEnable` (`0x00748459`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmShrine`](AgcmShrine.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIChargingInventory`](AgcmUIChargingInventory.md), [`AgcmUINPCTrade`](AgcmUINPCTrade.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md)
- **Erwähnt in:** [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmItem`](AgcmItem.md), [`AgcmUIBank`](AgcmUIBank.md), [`AgcmUIChargingInventory`](AgcmUIChargingInventory.md), [`AgcmUIEventItemRepair`](AgcmUIEventItemRepair.md), [`AgcmUINPCTrade`](AgcmUINPCTrade.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md), [`AgcmUIRefinery`](AgcmUIRefinery.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUISplitItem`](AgcmUISplitItem.md), [`AgpmEventNPCTrade`](AgpmEventNPCTrade.md)
