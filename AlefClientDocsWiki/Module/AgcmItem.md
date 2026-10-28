# AgcmItem (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmItem` (Gegenstände: Vorlagen, Modelle/Texturen, Benutzen, Ausrüsten, Pakete senden) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Aufrufer, EP8-Quelle `Modules/AClient/AgcmItem/` (`AgcmItem.cpp`, `AgcmItemEquip.cpp`, `AgcmItemInventory.cpp`, `AgcmItemStream.cpp`). Das Paketformat steht im Bericht [AgpmItem](AgpmItem.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Der Abgleich ist unvollständig; 134 von 199 Quellmethoden sind zugeordnet (zuletzt ergänzt: `LoadTemplateData`, `ReleaseTemplateData`, `RemoveClumpData`, `ReleaseItemData`, `MakeItemClump`, `SetFieldItem`, `RemoveAllAttachedAtomics`, `SendUseReturnScroll`, `ReceiveUnuseItem`, `UseChargingInventory`, `CancelCoolDown`, `ViewHelmet`). Die Funktionen liegen im Binary stark verstreut, viele kleine Methoden sind eingebaut oder zusammengefaltet.
- **OnAddModule:** gleiche 17 Module und gleiche Rückruf-Reihenfolge wie die Quelle; sechs leere Rückrufe zeigen auf den `return TRUE`-Rumpf, zwei Evolutions-Rückrufe teilen einen Rumpf.
- **Pakete:** 15 Sendefunktionen zugeordnet; `SendFieldInfo`, `SendQuestInfo`, `SendCancelReturnScroll` nicht gefunden.
- **Abweichungen:** keine festgestellt; `IsNoneDurabilityItem` enthält die japanische Sonderregel wie die Quelle.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmItem.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnLuaInitialize` | `0x006ED5E0` | 151 | vtable/String |
| 1 | `OnInit` | `0x006EB110` | 51 | vtable/String |
| 2 | `OnAddModule` | `0x006EF990` | 1334 | vtable/String |
| 3 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `OnIdle-Rumpf` (vom Linker zusammengefaltet) |
| 4 | `OnDestroy` | `0x006EB150` | 11 | vtable/String |
| 5 | `GetItem` | `0x006EB160` | 27 | von Hand geprüft |
| 6 | `GetItemData` | `0x006EB180` | 27 | von Hand geprüft |
| 7 | `GetTemplate` | – | | Einzeiler (Elterndaten), kein eigener Rumpf gefunden |
| 8 | `GetTemplateData` | `0x006EB1A0` | 27 | von Hand geprüft |
| 9 | `EquipDefaultArmour` | `0x006EB1C0` | 134 | von Hand geprüft |
| 10 | `InitCharacterCB` | `0x006ED680` | 313 | Callback-Registrierung |
| 11 | `PreRemoveCharacterCB` | `0x006EB250` | 26 | Callback-Registrierung |
| 12 | `ItemInitCB` | `0x006ED7C0` | 228 | Callback-Registrierung |
| 13 | `ItemAddCB` | `0x006ED8B0` | 44 | Callback-Registrierung |
| 14 | `ItemRemoveCB` | `0x006ED8E0` | 172 | Callback-Registrierung |
| 15 | `ItemConstructorCB` | `0x006EB270` | 93 | Callback-Registrierung |
| 16 | `ItemDestructorCB` | `0x006EF2F0` | 26 | Callback-Registrierung |
| 17 | `ItemTemplateConstructorCB` | `0x006EF7B0` | 213 | Callback-Registrierung |
| 18 | `DeleteTemplatePreData` | `0x006EB2D0` | 244 | von Hand geprüft |
| 19 | `ItemTemplateDestructorCB` | `0x006EF890` | 255 | Callback-Registrierung |
| 20 | `ItemStreamReadCB` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 21 | `ItemStreamWriteCB` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 22 | `ParseValueFieldTransform` | `0x006EB3D0` | 150 | von Hand geprüft |
| 23 | `ItemFieldCB` | `0x006EF310` | 113 | Callback-Registrierung |
| 24 | `SetFieldItem` | `0x006ED990` | 189 | von Hand geprüft |
| 25 | `ItemUseSuccessCB` | `0x006EDA50` | 64 | Callback-Registrierung |
| 26 | `ItemUseByTIDCB` | `0x006EDA90` | 495 | Callback-Registrierung |
| 27 | `FindCharacterDefaultItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `AddClumpToWorld` | `0x006EB470` | 67 | von Hand geprüft |
| 29 | `RemoveClumpFromWorld` | `0x006EB4C0` | 73 | von Hand geprüft |
| 30 | `GetClumpAdminData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 31 | `RemoveClumpAdminData` | `0x006EB510` | 66 | von Hand geprüft |
| 32 | `GetTexture` | `0x006EB560` | 49 | von Hand geprüft |
| 33 | `DropItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `PickupItem` | `0x006EDC90` | 83 | von Hand geprüft |
| 35 | `AutoPickupItem` | `0x006EDCF0` | 384 | von Hand geprüft |
| 36 | `SendInventoryInfo` | `0x006EDE70` | 541 | von Hand geprüft |
| 37 | `SendSubInventoryInfo` | `0x006EE090` | 541 | von Hand geprüft |
| 38 | `SendChargingInventoryInfo` | `0x006EE2B0` | 541 | von Hand geprüft |
| 39 | `SendEquipInfo` | `0x006EB5A0` | 251 | von Hand geprüft |
| 40 | `SendBankInfo` | `0x006EB6A0` | 299 | von Hand geprüft |
| 41 | `SendQuestInfo` | – | | kein Aufrufer, vermutlich entfernt |
| 42 | `SendFieldInfo` | – | | kein Aufrufer, vermutlich entfernt |
| 43 | `SendPickupItem` | `0x006EB7D0` | 217 | von Hand geprüft |
| 44 | `SendBuyBankSlot` | `0x006EB8B0` | 105 | von Hand geprüft |
| 45 | `SendUseReturnScroll` | `0x006EB920` | 243 | von Hand geprüft |
| 46 | `SendCancelReturnScroll` | – | | kein Aufrufer, vermutlich entfernt |
| 47 | `SendSplitItem` | `0x006EBA20` | 134 | von Hand geprüft |
| 48 | `SendSplitItem` | `0x006EC880` | 5 | von Hand geprüft |
| 49 | `SendRequestConvert` | `0x006EBAB0` | 135 | von Hand geprüft |
| 50 | `SendDropMoneyToField` | `0x006EBB40` | 208 | von Hand geprüft |
| 51 | `SendRequestDestroyItem` | `0x006EBC10` | 120 | von Hand geprüft |
| 52 | `SendAutoPickItem` | `0x006EBC90` | 133 | von Hand geprüft |
| 53 | `SendTooltipRegisterItemRequest` | `0x006EBD20` | 119 | von Hand geprüft |
| 54 | `UpdateItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 55 | `UtilCopyAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 56 | `UtilSetAtomicCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 57 | `CreateAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 58 | `LoadTemplateClump` | `0x006EE4D0` | 1466 | von Hand geprüft |
| 59 | `LoadTemplateTexture` | `0x006EBDA0` | 22 | von Hand geprüft |
| 60 | `LoadTemplateData` | `0x006EEA90` | 308 | von Hand geprüft |
| 61 | `ReleaseTemplateClump` | `0x006EC0E0` | 165 | von Hand geprüft |
| 62 | `ReleaseTemplateTexture` | `0x006EC190` | 157 | von Hand geprüft |
| 63 | `ReleaseTemplateData` | `0x006EC230` | 231 | von Hand geprüft |
| 64 | `LoadAllTemplateData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 65 | `CopyClump` | `0x006ECB90` | 114 | von Hand geprüft |
| 66 | `RemoveClumpData` | `0x006EC320` | 124 | von Hand geprüft |
| 67 | `ReleaseItemData` | `0x006EEBD0` | 258 | von Hand geprüft |
| 68 | `MakeItemClump` | `0x006EC3A0` | 935 | von Hand geprüft |
| 69 | `DumpTexDict` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 70 | `GetItemTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 71 | `UpdateInventoryForUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 72 | `CBUpdateInventory` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 73 | `CBUpdateBank` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 74 | `CBUpdateMoney` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 75 | `CBUpdateBankMoney` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 76 | `CBUpdateEquipment` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 77 | `CBSetSelfCharacter` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 78 | `UseItem` | `0x006EF700` | 36 | von Hand geprüft |
| 79 | `UseItem` | `0x006EF390` | 832 | von Hand geprüft |
| 80 | `CBAfterCooldown` | `0x006EC750` | 149 | Callback-Registrierung |
| 81 | `UseItemSkillBook` | `0x006EF230` | 181 | von Hand geprüft |
| 82 | `UseItemHPPotionTest` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 83 | `CheckReUseInterval` | `0x006EECE0` | 491 | von Hand geprüft |
| 84 | `SplitItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 85 | `SplitItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 86 | `BeStackableItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 87 | `GetItemCount` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 88 | `SetCallbackInitItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 89 | `SetCallbackEquipItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 90 | `SetCallbackFieldItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 91 | `SetCallbackUnequipItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 92 | `SetCallbackDetachedItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 93 | `SetCallbackPreRemoveData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 94 | `SetCallbackSetupItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 95 | `SetCallbackReadTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 96 | `SetCallbackCheckUseItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 97 | `SetCallbackConfirmUseSkillBook` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 98 | `SetCallbackUseMapItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 99 | `SetCallbackUseChargingInventory` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 100 | `SetGridItemAttachedTexture` | `0x006EC890` | 91 | von Hand geprüft |
| 101 | `SetGridItemTemplateAttachedTexture` | `0x006EC8F0` | 92 | von Hand geprüft |
| 102 | `SetGridItemAttachedSmallTexture` | `0x006EC950` | 92 | von Hand geprüft |
| 103 | `CBActionPickupItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 104 | `CBTransformAppear` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 105 | `CBRestoreTransformAppear` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 106 | `CBEvolutionAppear` | `0x006EC9B0` | 78 | von Hand geprüft |
| 107 | `CBRestoreEvolution` | `0x006EC9B0` | 78 | gleiche Adresse wie `identischer Rumpf wie CBEvolutionAppear` (vom Linker zusammengefaltet) |
| 108 | `SetCallbackEquipDefaultArmour` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 109 | `SetCallbackLoadClump` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 110 | `SetPreLightForAllItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 111 | `AddAttachedAtomic` | `0x006ECA00` | 170 | von Hand geprüft |
| 112 | `RemoveAllAttachedAtomics` | `0x006ECAB0` | 50 | von Hand geprüft |
| 113 | `GetNumAttachedAtomics` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 114 | `CopyAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 115 | `CreateArmourPartClumpCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 116 | `CreateArmourPartClump` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 117 | `CBLoadTemplate` | `0x006EEED0` | 141 | Callback-Registrierung |
| 118 | `CBMakeItemClump` | `0x006EEF60` | 230 | Callback-Registrierung |
| 119 | `CBSetItem` | `0x006EF050` | 292 | Callback-Registrierung |
| 120 | `ReleaseGridItemAttachedTexture` | `0x006ECC10` | 129 | von Hand geprüft |
| 121 | `SetGridItemAttachedTexture` | `0x006ECCA0` | 260 | von Hand geprüft |
| 122 | `IsItemValid` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 123 | `IsItemValid` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 124 | `IsItemReady` | `0x006EF180` | 69 | von Hand geprüft |
| 125 | `IsItemReady` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 126 | `SetItemStatus` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 127 | `SetItemStatus` | `0x006ECDB0` | 18 | von Hand geprüft |
| 128 | `ResetItemStatus` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 129 | `ResetItemStatus` | `0x006ECDD0` | 20 | von Hand geprüft |
| 130 | `SetAgcdRide` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 131 | `CancelCoolDown` | `0x006ECE00` | 19 | von Hand geprüft |
| 132 | `CBUnuseItem` | `0x006EF1D0` | 32 | Callback-Registrierung |
| 133 | `CBPauseItem` | `0x006EF1F0` | 50 | Callback-Registrierung |
| 134 | `ReceiveUnuseItem` | `0x006ECE20` | 106 | von Hand geprüft |
| 135 | `UnuseItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 136 | `ReceiveUseItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 137 | `ReceivePauseItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 138 | `IsTeleportScroll` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 139 | `OpenProgressBarWaiting` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 140 | `OpenProgressBarWaitingReturn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 141 | `IsNoneDurabilityItem` | `0x006ECE90` | 67 | von Hand geprüft |
| 142 | `CBAfterCoolDownWaitUseItem` | `0x006ECEE0` | 233 | Callback-Registrierung |
| 143 | `CBAfterCoolDownWaitUseItemReturn` | `0x006ECFD0` | 138 | Callback-Registrierung |
| 144 | `CBAddItemExtraData` | `0x006ED060` | 108 | Callback-Registrierung |
| 145 | `IsDisableUnEquipItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 146 | `UseChargingInventory` | `0x006ED0D0` | 174 | von Hand geprüft |
| 147 | `ReleaseEquipItems` | `0x007026E0` | 112 | von Hand geprüft |
| 148 | `RefreshEquipItems` | `0x00705670` | 189 | von Hand geprüft |
| 149 | `AttachNodeIndex` | `0x00702750` | 442 | von Hand geprüft |
| 150 | `AttachItem` | `0x00703D30` | 210 | von Hand geprüft |
| 151 | `AttachCharonToSummoner` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 152 | `AttachItemCheckPartIDCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 153 | `AttachItemCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 154 | `AttachCharonToSummonerCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 155 | `DetachNodeIndex` | `0x00702910` | 131 | von Hand geprüft |
| 156 | `DetachItem` | `0x007029A0` | 346 | von Hand geprüft |
| 157 | `DetachItemCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 158 | `AttachItem` | `0x00703EF0` | 666 | von Hand geprüft |
| 159 | `DetachItem` | `0x00704190` | 410 | von Hand geprüft |
| 160 | `UnEquipItem` | `0x00704D40` | 128 | von Hand geprüft |
| 161 | `ItemUnequipCB` | `0x00705740` | 124 | Callback-Registrierung |
| 162 | `EquipItem` | `0x00704DC0` | 138 | von Hand geprüft |
| 163 | `ItemEquipCB` | `0x00702B20` | 126 | Callback-Registrierung |
| 164 | `SetEquipAnimType` | `0x00704330` | 475 | von Hand geprüft |
| 165 | `ViewHelmet` | `0x007057C0` | 20 | von Hand geprüft |
| 166 | `GetAnimDefaultRide` | `0x00702BA0` | 51 | von Hand geprüft |
| 167 | `GetAnimWeaponRide` | `0x00702BF0` | 51 | von Hand geprüft |
| 168 | `GetAnimStandardRide` | `0x00702C40` | 51 | von Hand geprüft |
| 169 | `CBUpdateFactorDurability` | `0x00704E50` | 191 | Callback-Registrierung |
| 170 | `CBUpdateFactor` | `0x00704F10` | 261 | Callback-Registrierung |
| 171 | `OnEquipItemNecklace` | `0x00702C90` | 401 | von Hand geprüft |
| 172 | `OnUnEquipItemNecklace` | `0x00702E30` | 427 | von Hand geprüft |
| 173 | `OnAttachCharonToSummoner` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 174 | `GetCurrentEquipWeapon` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 175 | `GetCurrentEquipWeapon` | `0x00704510` | 109 | von Hand geprüft |
| 176 | `OnAttachWeapon` | `0x00705020` | 288 | von Hand geprüft |
| 177 | `OnDetachWeapon` | `0x00705140` | 254 | von Hand geprüft |
| 178 | `OnAttachPart` | `0x00705240` | 286 | von Hand geprüft |
| 179 | `OnDetachPart` | `0x00705360` | 286 | von Hand geprüft |
| 180 | `OnUpdateHairAndFace` | `0x00702FE0` | 396 | von Hand geprüft |
| 181 | `OnUpdateViewHelmet` | `0x00705496` | 466 | von Hand geprüft |
| 182 | `_GetDragonScionItemAgpdTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 183 | `_GetDragonScionItemAgpdTemplate` | `0x00703170` | 97 | von Hand geprüft |
| 184 | `_GetDragonScionItemAgcdTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 185 | `_GetDragonScionItemAgcdTemplate` | `0x007031E0` | 29 | von Hand geprüft |
| 186 | `_GetDragonScionItemAgcdItem` | `0x00703200` | 121 | von Hand geprüft |
| 187 | `_IsMatrixValid` | `0x00703280` | 109 | von Hand geprüft |
| 188 | `_AttachItemArmor` | `0x007032F0` | 575 | von Hand geprüft |
| 189 | `_AttachItemWeapon` | `0x00703530` | 379 | von Hand geprüft |
| 190 | `_AttachItemShield` | `0x007036B0` | 213 | von Hand geprüft |
| 191 | `_EquipItem` | `0x00704580` | 1174 | von Hand geprüft |
| 192 | `_UnEquipItem` | `0x00704A20` | 795 | Zeichenkette |
| 193 | `_SetEquipAnimType` | `0x00703790` | 876 | von Hand geprüft |
| 194 | `_IsWearAvatarItem` | `0x00703C20` | 264 | von Hand geprüft |
| 195 | `ItemInventoryCB` | `0x00795620` | 67 | Callback-Registrierung |
| 196 | `SetInventoryItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 197 | `ItemTemplateStreamReadCB` | `0x00794560` | 2919 | Callback-Registrierung |
| 198 | `ItemTemplateStreamWriteCB` | `0x007950D0` | 1351 | Callback-Registrierung |

134 von 199 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006eaec0` (`0x006EAEC0`), `ctor_or_dtor_006eb060` (`0x006EB060`), `~AgcmItem` (`0x006EB0F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xC9A / 0xC9C` | `Indizes der Zusatzdaten für Gegenstand / Vorlage` | `OnAddModule`, `GetItemData`, `GetTemplateData` |
| `0xC9E` | `Clump-Pfad (Puffer)` | `RemoveClumpAdminData` |
| `0xF58` | `Pfad der Symbol-Texturen` | `GetTexture` |
| `0xC8C` | `Zeiger auf [`AgcmRide`](AgcmRide.md)` | `SetAgcdRide` |
| `0xE3C` | `Zeiger auf [`AgcmUICooldown`](AgcmUICooldown.md)` | `CancelCoolDown` |

## Vtable und Quelldateien

Vtable bei `0x008D95AC`: Slot 0 Destruktor `0x006EB0F0`, 1 `OnAddModule` (`0x006EF990`), 2 `OnInit` (`0x006EB110`, liest `INI\ItemEvolutionTable.txt`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (`OnIdle`), 6 `0x0067AC90`, 7 `OnDestroy` (`0x006EB150`), 14 `OnLuaInitialize` (`0x006ED5E0`).
Die Klasse `AgcmItem` besteht in der Quelle aus vier Dateien: `AgcmItem.cpp` (147 Methoden, im Binary bei `0x006EB160`–`0x006EF990`), `AgcmItemEquip.cpp` (Anlegen/Ablegen von Ausrüstung, `0x00702B20`–`0x00705740`), `AgcmItemInventory.cpp` (`ItemInventoryCB`, `0x00795620`) und `AgcmItemStream.cpp` (`0x00794560`/`0x007950D0`). Die Funktionen liegen im Binary nicht in Quellreihenfolge (profilgesteuerte Sortierung); der Bereich `0x006F0000` danach gehört bereits zu `AgcmUICooldown`.

## OnAddModule (0x006EF990)

Holt 17 Module wie die Quelle: [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgpmGrid`](AgpmGrid.md), [`AgpmSkill`](AgpmSkill.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmRender`](AgcmRender.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmMap`](AgcmMap.md), [`AgcmLODManager`](AgcmLODManager.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`ApmMap`](ApmMap.md), [`AgcmShadow2`](AgcmShadow2.md), `AgcmUICooldown` und [`AgpmSystemMessage`](AgpmSystemMessage.md). Danach hängt es Zusatzdaten an Gegenstände (0x90 Byte, Konstruktor `0x006EB270`, Destruktor `0x006EF2F0`) und Vorlagen (0xD8 Byte, `0x006EF7B0`/`0x006EF890`); die Indizes liegen in `this+0xC9A` und `this+0xC9C`.
Rückrufe in Registrierungsreihenfolge: Init `ItemInitCB` (`0x006ED7C0`), Add `ItemAddCB` (`0x006ED8B0`), Remove `ItemRemoveCB` (`0x006ED8E0`), Equip `ItemEquipCB` (`0x00702B20`), Unequip `ItemUnequipCB` (`0x00705740`), Field `ItemFieldCB` (`0x006EF310`), Inventory `ItemInventoryCB` (`0x00795620`), Bank/Inventar-Aktualisierung (gemeinsamer Rumpf `0x0067AC90`), `AgcmCharacter`: `InitCharacterCB` (`0x006ED680`) und `PreRemoveCharacterCB` (`0x006EB250`), Evolution/Rückkehr (gemeinsamer Rumpf `0x006EC9B0`), `ItemUseSuccessCB` (`0x006EDA50`), `CBUnuseItem` (`0x006EF1D0`), `CBPauseItem` (`0x006EF1F0`), `ItemUseByTIDCB` (`0x006EDA90`), `CBUpdateFactorDurability` (`0x00704E50`), `CBUpdateFactor` (`0x00704F10`), `CBAddItemExtraData` (`0x006ED060`), zwei Stream-Rückrufe (Gegenstand: Stub, Vorlage: `0x00794560`/`0x007950D0`), zwei Lader (`CBLoadTemplate` `0x006EEED0`, `CBMakeItemClump`/`CBSetItem` `0x006EEF60`/`0x006EF050`) und drei Abklingzeiten (`CBAfterCooldown` `0x006EC750`, `CBAfterCoolDownWaitUseItem` `0x006ECEE0`, `…Return` `0x006ECFD0`).
Die sechs in der Quelle leeren Rückrufe `CBUpdateInventory`, `CBUpdateBank`, `CBUpdateMoney`, `CBUpdateBankMoney`, `CBUpdateEquipment` und `CBSetSelfCharacter` zeigen im Binary alle auf den gemeinsamen `return TRUE`-Rumpf `0x0067AC90`; die zwei Evolutions-Rückrufe (`CBEvolutionAppear`, `CBRestoreEvolution`) sind identisch und teilen sich `0x006EC9B0`.

## Pakete senden (Send…)

Die Sendefunktionen bauen das Paket (`AgpmItem::MakePacket…`/inline über `0x004EA2D0`) und rufen `SendPacket` (`0x004E45A0`). Zuordnung über die Aufrufer im UI-Code und die Quellreihenfolge:

| Funktion | Adresse | Aufrufer (Beleg) |
|---|---|---|
| `SendEquipInfo` | `0x006EB5A0` | [`AgcmUIItem`](AgcmUIItem.md):CBEquipMoveItem`, `CBInventoryDoubleClick`, Quick-Gürtel-Reittier |
| `SendBankInfo` | `0x006EB6A0` | [`AgcmUIEventBank`](AgcmUIEventBank.md):CBBankDragDropItem`, `CBBankMoveItem` |
| `SendPickupItem` | `0x006EB7D0` | `PickupItem` (`0x006EDC90`) |
| `SendBuyBankSlot` | `0x006EB8B0` | `AgcmUIEventBank::CBBuyBankSlot` |
| `SendUseReturnScroll` | `0x006EB920` | `CBAfterCoolDownWaitUseItemReturn` |
| `SendSplitItem` | `0x006EBA20` (+ Thunk `0x006EC880`) | `AgcmUIItem` über den Thunk |
| `SendRequestConvert` | `0x006EBAB0` | `AgcmUIItem::CBSendConvertItem` |
| `SendDropMoneyToField` | `0x006EBB40` | `AgcmUIItem::CBDropMoneyToFieldYes` |
| `SendRequestDestroyItem` | `0x006EBC10` | `AgcmUIItem::CBUIInventoryDestroyItem` |
| `SendAutoPickItem` | `0x006EBC90` | `AgcmUIItem::CBToggleAutoGetDropItem`, `UseItem` |
| `SendTooltipRegisterItemRequest` | `0x006EBD20` | `0x006D4620`, `0x00765110` |
| `SendInventoryInfo` / `SendSubInventoryInfo` / `SendChargingInventoryInfo` | `0x006EDE70` / `0x006EE090` / `0x006EE2B0` | `AgcmUIItem::CBInventoryMoveItem` / `…SubInventory…` / `…ChargingInventoryA…` |

`SendFieldInfo`, `SendQuestInfo` und `SendCancelReturnScroll` sind im Binary nicht einzeln zu finden (kein Aufrufer; vermutlich vom Linker entfernt oder zusammengefaltet).

## Gegenstand benutzen

`UseItem(AgpdItem*, AgpdCharacter*)` (`0x006EF390`, 832 Byte) wird von den Quick-Gürtel-Handlern (HP-/MP-Trank), dem Cash-Inventar und [`AgcmUIMain`](AgcmUIMain.md):OnIdle` gerufen; es fragt `AgcmUIItem::OnCheckUseEnable` und [`ApmEventManager`](ApmEventManager.md) ab, ruft für Fertigkeitsbücher `UseItemSkillBook` (`0x006EF230`) und für Wiederverwendungssperren `CheckReUseInterval` (`0x006EECE0`, 491 Byte) auf. Die Überladung mit Gegenstands-ID (`0x006EF700`) holt den Gegenstand und ruft `0x006EF390`. `UseChargingInventory` (`0x006ED0D0`) wird in `ItemAddCB` gerufen. Die drei Abklingzeit-Rückrufe senden nach Ablauf das Benutzungspaket.
`IsNoneDurabilityItem` (`0x006ECE90`) liefert TRUE für Halsketten, Ringe und – im japanischen Dienstgebiet (`g_eServiceArea == 3`) – für Reittiere, wie in der Quelle; `CBUpdateFactor` (`0x00704F10`) ruft sie auf. `ReceiveUnuseItem` (`0x006ECE20`) setzt Zustandsbits zurück, `CancelCoolDown` (`0x006ECE00`) bricht die Abklingzeit im Cooldown-Modul ab.

## Vorlagen, Texturen und Clumps

Laden und Freigeben: `LoadTemplateTexture` (`0x006EBDA0`, Dateinamen `%s%.*x`, 7 Hexstellen), `LoadTemplateClump` (`0x006EE4D0`, 1466 Byte, Zeichenketten `%s%.*x.%s`, `LODIndex`), `LoadTemplateData` (`0x006EEA90`), `ReleaseTemplateClump` (`0x006EC0E0`), `ReleaseTemplateTexture` (`0x006EC190`), `ReleaseTemplateData` (`0x006EC230`), `MakeItemClump` (`0x006EC3A0`, 935 Byte), `RemoveClumpData` (`0x006EC320`), `ReleaseItemData` (`0x006EEBD0`) und `CopyClump` (`0x006ECB90`). `GetTexture` (`0x006EB560`) lädt über den Resource-Loader mit dem Symbolpfad (`this+0xF58`) und setzt Filter „nearest“ und Adressierung „clamp“.
Raster-Texturen: `SetGridItemAttachedTexture(AgpdItem*)` (`0x006EC890`), `…TemplateAttachedTexture` (`0x006EC8F0`), `…AttachedSmallTexture` (`0x006EC950`), die Vorlagen-Überladung (`0x006ECCA0`, lädt bei Bedarf und zählt `m_lAttachedToGrid`) und `ReleaseGridItemAttachedTexture` (`0x006ECC10`). `AddAttachedAtomic` (`0x006ECA00`) und `RemoveAllAttachedAtomics` (`0x006ECAB0`) verwalten die angehängten Atomics.

## Ausrüstung (AgcmItemEquip.cpp)

`_EquipItem` (`0x00704580`, 1174 Byte, Zeichenkette `AgcmUIItem`) und `_UnEquipItem` (`0x00704A20`) sind die Kernfunktionen; `EquipItem` (`0x00704DC0`) und `UnEquipItem` (`0x00704D40`) rufen sie. `AttachItem(Charaktervorlage…)` (`0x00703EF0`) und `DetachItem(Charakter…)` (`0x00704190`) hängen die Teile an das Skelett. `OnAttachWeapon`/`OnDetachWeapon`/`OnAttachPart`/`OnDetachPart` sind die vier Rückrufe bei `0x00705020`, `0x00705140`, `0x00705240`, `0x00705360` (Zeichenketten `AgpmItem`, `AgpmGrid`; die Paare unterscheiden sich durch den Aufruf von `_EquipItem` bzw. `_UnEquipItem`). `_IsWearAvatarItem` (`0x00703C20`) prüft Avatar-Gegenstände, `ReleaseEquipItems` (`0x007026E0`) gibt die Ausrüstung eines Charakters frei.

## Ausrüstung: Anhängen, Animationstypen, Hilfsfunktionen

`AttachItem(Atomic…)` (`0x00703D30`) verteilt auf `_AttachItemArmor` (`0x007032F0`), `_AttachItemWeapon` (`0x00703530`) und `_AttachItemShield` (`0x007036B0`); `AttachNodeIndex` (`0x00702750`) und `DetachNodeIndex` (`0x00702910`) setzen die Skelett-Knoten, `DetachItem(Atomic…)` (`0x007029A0`) entfernt Atomics aus der Welt. `RefreshEquipItems` (`0x00705670`) gibt die Ausrüstung frei, baut Clumps neu und legt sie wieder an (Aufrufer: Evolutions-Rückruf).
`SetEquipAnimType` (`0x00704330`) liest die Waffen in beiden Händen und das Lanzenteil (Teile 9, 10 und 15) und wählt den Animationstyp; `_SetEquipAnimType` (`0x00703790`, 876 Byte) setzt ihn und benutzt die drei Reittier-Tabellen `GetAnimDefaultRide`/`…WeaponRide`/`…StandardRide` (`0x00702BA0`, `0x00702BF0`, `0x00702C40`; reine `switch`-Tabellen). `GetCurrentEquipWeapon(Charakter, Hand)` ist `0x00704510`; die Einhand-Überladung ist eingebaut.
`OnEquipItemNecklace` (`0x00702C90`) und `OnUnEquipItemNecklace` (`0x00702E30`) fragen [`AgcmEventEffect`](AgcmEventEffect.md) ab und starten bzw. beenden die Halsketten-Effekte (Zeichenketten und Aufrufstruktur gleich, die Zuordnung der beiden Richtungen folgt der Quellreihenfolge). `OnUpdateHairAndFace` (`0x00702FE0`) und `OnUpdateViewHelmet` (`0x00705496`) aktualisieren Frisur, Gesicht und Helmanzeige. Die vier Hilfsfunktionen der Drachenabkömmling-Gegenstände liegen bei `0x00703170` (Vorlage), `0x007031E0`, `0x00703200` (legt bei Bedarf einen Hilfsgegenstand an) und `_IsMatrixValid` bei `0x00703280` (drei Matrixwerte ungleich null).

## Lua-Funktionen (OnLuaInitialize, 0x006ED5E0)

`OnLuaInitialize` registriert Lua-Befehle, u. a. `EquipItem`, `UnEquipItem`, `SetAvatarItem` und `EquipAvatarSet`. Die zugehörigen Funktionen (`0x006ED180`, `0x006ED350`, `0x006ED4C0`, `0x006ED550`; Zeichenketten `CID not found`, `Item Creation Fail`, `Invalid Part Index`) sind freie Funktionen, keine Methoden der Klasse.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, `IsNoneDurabilityItem`, `GetTexture`, Grid-Texturen).

## Grenzen

- Die zwölf `SetCallback…`-Setter (`SetCallbackInitItem` … `SetCallbackLoadClump`) sind im Binary zu einem gemeinsamen Rumpf zusammengefaltet und lassen sich nicht einzeln zuordnen; `ViewHelmet` (`0x007057C0`) ist nur über die Form (Feld setzen, dann `OnUpdateViewHelmet`) zugeordnet, der Quelltext ist größtenteils auskommentiert.
- Die Zuordnung der Sendefunktionen stützt sich auf Aufrufer im UI-Code und die Quellreihenfolge, nicht auf einen Vergleich der Paketoperationen; `SendSplitItem` (zwei Überladungen) ist über einen Thunk und einen gemeinsamen Rumpf zugeordnet und unsicher.
- `CheckReUseInterval`, `UseItem`, `UseItemSkillBook`, `ReleaseEquipItems`, `_IsWearAvatarItem` und die vier `OnAttach…`/`OnDetach…`-Rückrufe sind über Größe, Zeichenketten und Aufrufer zugeordnet, nicht Zeile für Zeile verglichen.
- Der Ausrüstungsblock `0x00702B20`–`0x00705740` wurde über Aufrufgraph und Zeichenketten zugeordnet; die Funktionen `_AttachItem…`, `_SetEquipAnimType`, `OnUpdateHairAndFace`, `OnUpdateViewHelmet`, `RefreshEquipItems` und die beiden Halsketten-Funktionen wurden nicht Zeile für Zeile verglichen. Die kleinen Rückruf-Wrapper (`AttachItemCB` usw.), `ViewHelmet`, `OnEquipItem…`-Randfälle und `SetInventoryItem` sind nicht gefunden.
- Die Lua-Funktionen (`0x006ED180`…) sind keine Klassenmethoden und zählen nicht in die Abdeckung.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 24, gemeinsamer Rumpf: 15, nicht im Client: 20, ohne Kandidat: 10, zugeordnet: 5.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetCurrentEquipWeapon` | 24 | `0x0073AAE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetDragonScionItemAgpdTemplate` | 7 | `0x00707DA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsDisableUnEquipItem` | 59 | `0x0073E020` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenProgressBarWaitingReturn` | 25 | `0x0073D410` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenProgressBarWaiting` | 29 | `0x0073D300` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SendFieldInfo` (`0x006E9D30`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmLODManager`](AgcmLODManager.md), [`AgcmMap`](AgcmMap.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmRide`](AgcmRide.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIEventBank`](AgcmUIEventBank.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgpmSkill`](AgpmSkill.md), [`AgpmSystemMessage`](AgpmSystemMessage.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmCashMall`](AgcmCashMall.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmRide`](AgcmRide.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIChargingInventory`](AgcmUIChargingInventory.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIEventBank`](AgcmUIEventBank.md), [`AgcmUIRefinery`](AgcmUIRefinery.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md), [`AgcmUIStatus`](AgcmUIStatus.md)
