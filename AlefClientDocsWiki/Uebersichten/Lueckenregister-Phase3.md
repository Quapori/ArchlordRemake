# Phase 3

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Erzeugt mit `gapclose.py register`. Jede Quellmethode ohne Binary-Adresse bekommt einen Status mit Beleg. **zugeordnet** = eindeutiger Treffer (mindestens zwei unabhängige Belege, Reihenfolge der Quelle passt zur Adressreihenfolge); **gemeinsamer Rumpf** = `SetCallback`-Einzeiler; **nicht im Client** = in der Quelle ruft sie kein Client-Modul (nur Server oder niemand); **eingebaut** = kleine Funktion mit Aufrufer im Client, ohne eigene Adresse; **Kandidat unbestätigt** = Aufrufer im Client und ein Kandidat mit nur einem Beleg oder mehrdeutig (nicht benannt); **ohne Kandidat** / **nicht als eigene Funktion** = Aufrufer im Client, aber keine unbenannte Funktion mit Beleg (bei „nicht als eigene Funktion“ ist im Klassenbereich gar keine unbenannte Funktion mehr übrig); in beiden Fällen ist die Methode vermutlich eingebaut oder entfernt.

Zahlen: Kandidat unbestätigt 4, eingebaut 47, gemeinsamer Rumpf 81, nicht als eigene Funktion 10, nicht im Client 52, ohne Kandidat 36, zugeordnet 24

## AgcmAdmin (gemeinsamer Rumpf 1, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SendAdminClientRequest` | 37 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetUIMessageString` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmArchlord (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBOperationCancelArchlord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmArchlord::OnAddModule |
| `OperationSetArchlord` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmArchlord::CBOperationSetArchlord |

## AgcmAuction (gemeinsamer Rumpf 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackSelect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAuctionUIOpen` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSalesBox2Add` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSalesBox2Remove` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSalesBox2Update` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmBillInfo (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_AddSystemGridHangameS` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo; im Adressbereich der Klasse (0x006DDC30–0x006DDDE0) ist keine unbenannte Funktion mehr übrig |
| `_AddSystemGridHangameTPack` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo; im Adressbereich der Klasse (0x006DDC30–0x006DDDE0) ist keine unbenannte Funktion mehr übrig |

## AgcmCashMall (nicht als eigene Funktion 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SendPacketRefreshCash` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUICashMall::CBCheckCash, AgcmUICashMall::CBReturnRefresh; im Adressbereich der Klasse (0x006E3810–0x006E3C40) ist keine unbenannte Funktion mehr übrig |
| `SendPacketCheckListVersion` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyDummyItem` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCashMall::DestroyAllDummyItem; im Adressbereich der Klasse (0x006E3810–0x006E3C40) ist keine unbenannte Funktion mehr übrig |

## AgcmEventBank (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrantEventBank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventCharCustomize (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrantEvent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventGacha (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnLuaInitialize` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::LuaInitialize |

## AgcmEventGuild (gemeinsamer Rumpf 2, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGrantWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CBEventGrantWorldChampionship` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIGuild::OnInit; im Adressbereich der Klasse (0x006DECD0–0x006DEF60) ist keine unbenannte Funktion mehr übrig |

## AgcmEventItemConvert (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackEventGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventItemRepair (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventManager (gemeinsamer Rumpf 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmEventNPCDialog (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackAriseNPCDialogEvent` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventProduct (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventQuest (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventRefinery (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventSiegeWarNPC (nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBEventGrant` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventBank::OnAddModule, AgcmEventCharCustomize::OnAddModule, AgcmEventCook::OnAddModule; im Adressbereich der Klasse (0x006DEB00–0x006DEBD0) ist keine unbenannte Funktion mehr übrig |

## AgcmEventSkillMaster (gemeinsamer Rumpf 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SendBuySkillBook` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackResultSkillUpgrade` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackResponseGrant` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventTeleport (gemeinsamer Rumpf 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackSelectTeleportPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCannotUseForTransforming` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCannotUseForCombatMode` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmGuild (gemeinsamer Rumpf 3, nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `IsGuildBattle` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBCheckGuildAttackable` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SendHostileLeaveReject` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::CBEventReturnHostileLeaveAccept; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |

## AgcmHeroicSkill (Kandidat unbestätigt 1, eingebaut 2, ohne Kandidat 4, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetHeroicSkillIndex` | 18 | zugeordnet | `0x00782B00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHeroicSkill` | 24 | zugeordnet | `0x00782320` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBBuyHeroicSkillResult` | 10 | zugeordnet | `0x00787EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadHeroicSkill` | 84 | zugeordnet | `0x00787350` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHeroicSkillPoint` | 29 | zugeordnet | `0x00782420` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsActiveUpgradeHeroic` | 24 | zugeordnet | `0x00781C40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadHeroicSkillBuy` | 85 | zugeordnet | `0x007827D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Initialize` | 49 | zugeordnet | `0x00781A40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Destroy` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmItem::ItemDestructorCB, AgcmObject::ReleaseObjectData; kein unbenannter Kandidat mit Beleg unter 627 unbenannten Funktionen im Klassenbereich |
| `UnSelectSkillHeroic` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmHeroicSkill::CBSelectHeroicSkillGrid, AgcmUISkillDragonScion::UnSelectSkillUI |
| `UnSelectSkillHeroicUpgrade` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmHeroicSkill::LoadHeroicSkillBuy, AgcmHeroicSkill::CBSelectUpgradeHeroicSkillGrid, AgcmUISkillDragonScion::UnSelectUpgradeSkillUI |
| `_IsScion` | 16 | Kandidat unbestätigt | `0x00781D60` | Aufrufer im Client: AgcmHeroicSkill::GetHeroicSkillPoint, AgcmHeroicSkill::LoadHeroicSkillBuy, AgcmHeroicSkill::CBSelectUpgradeHeroicSkillGrid; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 11, Belegarten 2) |
| `CBUpgradeHeroicSkillResult` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmHeroicSkill::Initialize; kein unbenannter Kandidat mit Beleg unter 627 unbenannten Funktionen im Klassenbereich |
| `CBUpdateHeroicSkill` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmHeroicSkill::Initialize; kein unbenannter Kandidat mit Beleg unter 627 unbenannten Funktionen im Klassenbereich |
| `CBUpdateFactorHeroicPoint` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmHeroicSkill::Initialize; kein unbenannter Kandidat mit Beleg unter 627 unbenannten Funktionen im Klassenbereich |

## AgcmItem (Kandidat unbestätigt 1, eingebaut 24, gemeinsamer Rumpf 15, nicht im Client 20, ohne Kandidat 10, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCurrentEquipWeapon` | 24 | zugeordnet | `0x0073AAE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetDragonScionItemAgpdTemplate` | 7 | zugeordnet | `0x00707DA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsDisableUnEquipItem` | 59 | zugeordnet | `0x0073E020` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenProgressBarWaitingReturn` | 25 | zugeordnet | `0x0073D410` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenProgressBarWaiting` | 29 | zugeordnet | `0x0073D300` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::CBRegionChange, AgcmCharacter::ShowRegionInfo, AgcmCharacter::CBBindingRegionChange |
| `ItemStreamReadCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule |
| `ItemStreamWriteCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule |
| `FindCharacterDefaultItem` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetClumpAdminData` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::LoadTemplateClump; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `DropItem` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBUIInventoryDropItem; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `SendQuestInfo` | 57 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SendFieldInfo` | 54 | Kandidat unbestätigt | `0x006E9D30` | Aufrufer im Client: AgcmItem::DropItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `SendCancelReturnScroll` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: ApmMap::UpdateItem |
| `UtilCopyAtomic` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UtilSetAtomicCB` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateAtomic` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::CreateSkyAtomic, AgcmEventNature::CreateCloudAtomic, AgcmEventNature::CreateCircumstanceAtomic |
| `LoadAllTemplateData` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DumpTexDict` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetItemTexture` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateInventoryForUI` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUpdateInventory` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule |
| `CBUpdateBank` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule, AgcmUIEventBank::OnAddModule |
| `CBUpdateMoney` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule, AgcmUIEventItemRepair::OnAddModule |
| `CBUpdateBankMoney` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule, AgcmUIEventBank::OnAddModule |
| `CBUpdateEquipment` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule |
| `CBSetSelfCharacter` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmItem::OnAddModule, AgcmMinimap::OnAddModule, AgcmQuestJournal::OnInit |
| `UseItemHPPotionTest` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SplitItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::CBSplitItemInventory, AgpmItem::OnOperationSplitItem |
| `SplitItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::CBSplitItemInventory, AgpmItem::OnOperationSplitItem |
| `BeStackableItem` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetItemCount` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUICustomizing::IsEnoughCost, AgcmUICustomizing::SetFaceDescription, AgcmUICustomizing::SetHairDescription |
| `SetCallbackInitItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEquipItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackFieldItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUnequipItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDetachedItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPreRemoveData` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetupItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReadTemplate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckUseItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackConfirmUseSkillBook` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseMapItem` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUseChargingInventory` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CBActionPickupItem` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBTransformAppear` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmCharacter::CBTransformAppear; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `CBRestoreTransformAppear` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBRestoreEvolution` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::OnAddModule; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `SetCallbackEquipDefaultArmour` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackLoadClump` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetPreLightForAllItem` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetNumAttachedAtomics` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CopyAtomic` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateArmourPartClumpCB` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CreateArmourPartClump; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `CreateArmourPartClump` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::LoadTemplateClump; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `IsItemValid` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsItemValid` | 28 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsItemReady` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::ItemFieldCB, AgcmItem::CBSetItem, AgcmItem::IsItemValid; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `SetItemStatus` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmItem::ItemInitCB, AgcmItem::ItemRemoveCB, AgcmItem::SetFieldItem |
| `ResetItemStatus` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmItem::_UnEquipItem |
| `SetAgcdRide` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRide::OnAddModule |
| `UnuseItem` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::UseItem, AgpmItem::OnOperationUnuseItem, AgpmItem::UnuseItem; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `ReceiveUseItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::ItemUseSuccessCB |
| `ReceivePauseItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::CBPauseItem |
| `IsTeleportScroll` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachCharonToSummoner` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::AttachCharonToSummonerCB; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |
| `AttachItemCheckPartIDCB` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::EquipDefaultArmour, AgcmItem::AttachItem |
| `AttachItemCB` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::EquipDefaultArmour, AgcmItem::AttachItem |
| `AttachCharonToSummonerCB` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::OnAttachCharonToSummoner |
| `DetachItemCB` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::DetachItem, AgcmItem::_EquipItem |
| `OnAttachCharonToSummoner` | 42 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_GetDragonScionItemAgcdTemplate` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmItem::AttachItem, AgcmItem::DetachItem |
| `SetInventoryItem` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::ItemInventoryCB; kein unbenannter Kandidat mit Beleg unter 1554 unbenannten Funktionen im Klassenbereich |

## AgcmItemConvert (nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBResultPhysicalConvert` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmItemConvert::OnAddModule, AgcmUIEventItemConvert::OnAddModule; im Adressbereich der Klasse (0x006EA910–0x006EADF0) ist keine unbenannte Funktion mehr übrig |
| `CBResultSocketConvert` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmItemConvert::OnAddModule, AgcmUIEventItemConvert::OnAddModule; im Adressbereich der Klasse (0x006EA910–0x006EADF0) ist keine unbenannte Funktion mehr übrig |
| `CBResultRuneConvert` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmItemConvert::OnAddModule, AgcmUIEventItemConvert::OnAddModule; im Adressbereich der Klasse (0x006EA910–0x006EADF0) ist keine unbenannte Funktion mehr übrig |

## AgcmObjectList (ohne Kandidat 4, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RemoveAllObjectTemplateGroup` | 21 | zugeordnet | `0x00764320` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetObjectTemplateGroup` | 17 | zugeordnet | `0x00764220` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllObjectGroup` | 21 | zugeordnet | `0x00764180` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddObjectGroup` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::GetObjectGroupData; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `GetObjectGroup` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmAmbOcclMap::searchAtomicById, AgcmObject::GetObjectGroupData; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `AddObjectTemplateGroup` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::GetObjectTemplateGroupData, AgcmObject::CopyObjectTemplateGroup; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `RemoveObjectTemplateGroup` | 53 | ohne Kandidat |  | Aufrufer im Client: AgcmObject::OnObjectTemplateDestroy; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |

## AgcmProduct (gemeinsamer Rumpf 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmQuest (gemeinsamer Rumpf 3, nicht im Client 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetAcceptQuestNameColor` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMainQuestNameColor` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCustomColor` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmQuestJournal (Kandidat unbestätigt 2, eingebaut 1, gemeinsamer Rumpf 3, ohne Kandidat 2, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_QueueProcess` | 10 | zugeordnet | `0x00613170` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsQuestJournal` | 10 | zugeordnet | `0x00612310` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddQuestJournal` | 58 | zugeordnet | `0x00612E80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DelQuestJournal` | 31 | zugeordnet | `0x00612490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReadJournalText` | 46 | zugeordnet | `0x00612C00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Clear` | 17 | zugeordnet | `0x00612710` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `DelQuestJournal` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmUIQuestJournal::CBClickJournalButton3, AgcmUIQuest2::CBCheckJournal, AgcmUIQuest2::CompleteQuestResult; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `GetQuestCount` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmQuestJournal::AddQuestJournal; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `GetQuestJournal` | 17 | Kandidat unbestätigt | `0x006122B0` | Aufrufer im Client: AgcmUIQuestJournal::RefreshJournalInfo, AgcmUIQuestJournal::CBClickJournalButton2, AgcmUIQuestJournal::CBClickJournalButton3; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetQuestJournal` | 11 | Kandidat unbestätigt | `0x006122B0` | Aufrufer im Client: AgcmUIQuestJournal::RefreshJournalInfo, AgcmUIQuestJournal::CBClickJournalButton2, AgcmUIQuestJournal::CBClickJournalButton3; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetCallbackRefresh` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `_GetQuestJournalText` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmQuestJournal::MakeJournalText |

## AgcmReturnToLogin (eingebaut 1, gemeinsamer Rumpf 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackRequestFailed` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackEndProcess` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallBackReconnectLoginServer` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmStartupEncryption::OnAddModule |

## AgcmRide (eingebaut 1, gemeinsamer Rumpf 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CBRideTimeOut` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRide::OnAddModule |

## AgcmSiegeWar (gemeinsamer Rumpf 1, nicht im Client 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SendCancelAttackApplication` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSiegeWarDisplayInfo` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmSiegeWar::CBInitCharacter, AgcmSiegeWar::CBUpdateCharStatus, AgcmSiegeWar::CBRemoveCharacter; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SetCallbackOpenCheckResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmSkill (eingebaut 11, gemeinsamer Rumpf 15, nicht im Client 13, ohne Kandidat 13, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetAgcdSkill` | 5 | zugeordnet | `0x0066AD40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBuffSkillSmallTexture` | 20 | zugeordnet | `0x0066C120` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnDestroy` | 4 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `ProcessStartEffect` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::ProcessNoticeEffect; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `ProcessSkillEffectIdleEvent` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::ProcessStartEffect; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `CastSkillTest` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CastSkillTest` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CastSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CastSkillTest, AgcmSkill::CastSkillTest, AgcmSkill::CBActionSkill |
| `CastSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CastSkillTest, AgcmSkill::CastSkillTest, AgcmSkill::CBActionSkill |
| `CastSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CastSkillTest, AgcmSkill::CastSkillTest, AgcmSkill::CBActionSkill |
| `CastSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CastSkillTest, AgcmSkill::CastSkillTest, AgcmSkill::CBActionSkill |
| `CastSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CastSkillTest, AgcmSkill::CastSkillTest, AgcmSkill::CBActionSkill |
| `CastSkill` | 273 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CastSkillTest, AgcmSkill::CastSkillTest, AgcmSkill::CBActionSkill; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `CastSkillCheck` | 103 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCharacterTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIScreamEditDlg::OnInitDialog, AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcuCamMode::SetCameraInfo |
| `DesAgcdSkillAttachData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::OnAddModule |
| `DesAgcdSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::OnAddModule |
| `ParseTemplateString` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CheckVisualInfo` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::GetUsableSkillTNameIndex; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `SetCallbackNoAnimSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMissCastSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCheckCastSkillResult` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddBuffedSkillList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveBuffedSkillList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddtionalHitEffect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddHpBar` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCastFailForTransform` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCastFailForRide` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPreProcessSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetRegisteredMPPotionTID` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackBlockCastSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackStartGroundTargetSkill` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `UpdateSkillPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CBLearnSkill, AgpmCharacter::UpdateSkillPoint, AgpmSkill::AddSkillPoint |
| `UpdateSkillPoint` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::CBLearnSkill, AgpmCharacter::UpdateSkillPoint, AgpmSkill::AddSkillPoint; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `UpdateDIRTPoint` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateDIRTPoint` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkillRaster` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSmallSkillRaster` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkillTexture` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSmallSkillTexture` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmSkill::GetBuffSkillSmallTexture |
| `GetSkillFactor` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkillTotalPoint` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBInitSkillTemplate` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::OnAddModule; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `CBUpdateSkillPoint` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::OnAddModule, AgcmUIProductSkill::OnAddModule, AgcmUISkill2::OnAddModule; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `GetAgcdSkillTemplate` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::GetSkillRaster, AgcmSkill::GetSmallSkillRaster, AgcmSkill::GetSkillTexture; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `SkillTest` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnumCallbackNoAnimSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::ProcessReceiveCastSkill |
| `SetCallbackStartCastSelfCharacter` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCurrentSkillUsableIndex` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmSkill::SetCurrentSkill, AgcmUIProduct::CastAnimation, AgcmUIQuest2::StartAnimation; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `ShowAffectedTargetCount` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadTemplateSkill` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::StreamReadTemplate, AgcmExportResource::ReadCharacterTemplate, AgcmSkill::StreamReadTemplateSkillSound; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplateSkill` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `StreamReadTemplateSkillSound` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ReadCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplateSkillSound` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate; kein unbenannter Kandidat mit Beleg unter 394 unbenannten Funktionen im Klassenbereich |

## AgcmTuner (gemeinsamer Rumpf 1, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetVariableByOption` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmWarInfo (eingebaut 1, gemeinsamer Rumpf 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `UpdatePvPInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmWarInfo::CBOperationUpdateCharacterPvPInfo, AgcmWarInfo::CBOperationUpdateRacePvPInfo |
| `ReadStreamWarInfo` | 107 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmWorld (ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DesAgcdWorld` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmWorld::OnAddModule; kein unbenannter Kandidat mit Beleg unter 34 unbenannten Funktionen im Klassenbereich |

## AgpmBattleGround (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCallbackSystemMessage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmEventNPCTrade (eingebaut 1, gemeinsamer Rumpf 1, nicht im Client 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::CBRegionChange, AgcmCharacter::ShowRegionInfo, AgcmCharacter::CBBindingRegionChange |
| `GetNPCTradeTemplate` | 13 | nicht im Client |  | Aufrufer nur im Server (3); kein Treffer im Binary |
| `GetGroupItemTemplate` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadNPCTradeRes` | 92 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsItemInGrid` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `SetCallbackDeleteGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgpmLogin (eingebaut 1, gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `GetNextCharCn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmLogin::InitFuncPtr |

## AgpmResourceInfo (nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CheckValidVersion` | 16 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AgpmUnion (eingebaut 1, gemeinsamer Rumpf 4, nicht als eigene Funktion 1, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetCallbackUpdateUnionRank` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateUnionRankPoint` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetUnionRankPoint` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmUnion::GetUnionRank, AgpmUnion::UpdateUnionRankPoint; im Adressbereich der Klasse (0x00585E70–0x00585F30) ist keine unbenannte Funktion mehr übrig |
| `SetUnionRankPoint` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmUnion::UpdateUnionRankPoint |
| `UpdateUnionRankPoint` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadUnionRankTable` | 62 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
