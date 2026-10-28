# Modulübersicht AlefClient.exe 2017-08-15 gegen die EP8-Quelle

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Alle Module der EP8-Quelle (`Modules/*/*`) gegen das 2017er Binary. „vtable“ = Anzahl der Slots, die im Binary per RTTI der Klasse zugeordnet sind (0 = Klasse hat im Binary keine eigene vtable bzw. kommt nicht vor). „benannt“ = Funktionen dieses Moduls mit Namen in `rea_export/names_all310.tsv`. „Quelle“ = Funktionsdefinitionen in `<Modul>.cpp`. „Bericht“ verweist auf die Modulanalyse (Pakete, Opcodes, Abweichungen von EP8, Abgleich mit 2013), soweit das Modul Pakete verarbeitet (`OnReceive`).

## Zusammenfassung

| Gruppe | Module in der Quelle | davon mit vtable im Binary | davon mit Modulbericht |
|---|---:|---:|---:|
| AClient | 144 | 126 | 129 |
| APublic | 101 | 74 | 74 |
| AServer | 121 | 0 | 0 |
| AUtility | 49 | 9 | 13 |

`AServer` enthält die Server-Module; der Client enthält sie nicht (Ausnahmen sind mitkompilierte Hilfsklassen).

## Alle Module

| Gruppe | Modul | vtable | benannt | Quelle | OnReceive | Bericht |
|---|---|---:|---:|---:|---|---|
| AClient | `AgcAuth` | 6 | 12 | 10 |  | [AgcAuth](../Module/AgcAuth.md) |
| AClient | `AgcModule` | 17 | 9 | 9 |  | [AgcModule](../Module/AgcModule.md) |
| AClient | `AgcSkeleton` | 0 | 9 | 0 |  | [AgcSkeleton](../Module/AgcSkeleton.md) |
| AClient | `AgcSplashWindow` | 0 | 0 | 0 |  | – |
| AClient | `AgcUIQuestText` | 1 | 27 | 27 |  | [AgcUIQuestText](../Module/AgcUIQuestText.md) |
| AClient | `AgcmAIDlg` | 0 | 0 | 5 |  | – |
| AClient | `AgcmAdmin` | 17 | 8 | 9 |  | [AgcmAdmin](../Module/AgcmAdmin.md) |
| AClient | `AgcmAmbOcclMap` | 17 | 9 | 10 |  | [AgcmAmbOcclMap](../Module/AgcmAmbOcclMap.md) |
| AClient | `AgcmAnimation` | 0 | 0 | 7 |  | – |
| AClient | `AgcmArchlord` | 17 | 6 | 6 |  | [AgcmArchlord](../Module/AgcmArchlord.md) |
| AClient | `AgcmAuction` | 17 | 17 | 20 |  | [AgcmAuction](../Module/AgcmAuction.md) |
| AClient | `AgcmBattleGround` | 17 | 5 | 15 | ja | [AgcmBattleGround](../Module/AgcmBattleGround.md) |
| AClient | `AgcmBillInfo` | 17 | 6 | 6 |  | [AgcmBillInfo](../Module/AgcmBillInfo.md) |
| AClient | `AgcmCamera2` | 17 | 27 | 54 |  | [AgcmCamera2](../Module/AgcmCamera2.md) |
| AClient | `AgcmCashMall` | 17 | 9 | 10 |  | [AgcmCashMall](../Module/AgcmCashMall.md) |
| AClient | `AgcmCharacter` | 17 | 175 | 280 | ja | [AgcmCharacter_Angriff](../Module/AgcmCharacter_Angriff.md) |
| AClient | `AgcmConnectManager` | 17 | 9 | 11 | ja | [AgcmConnectManager](../Module/AgcmConnectManager.md) |
| AClient | `AgcmCustomizeRender` | 17 | 31 | 55 |  | [AgcmCustomizeRender](../Module/AgcmCustomizeRender.md) |
| AClient | `AgcmDynamicLightmap` | 17 | 13 | 16 |  | [AgcmDynamicLightmap](../Module/AgcmDynamicLightmap.md) |
| AClient | `AgcmEff2` | 17 | 21 | 27 |  | [AgcmEff2](../Module/AgcmEff2.md) |
| AClient | `AgcmEffectDataAdmin` | 0 | 0 | 0 |  | – |
| AClient | `AgcmEventBank` | 17 | 6 | 5 |  | [AgcmEventBank](../Module/AgcmEventBank.md) |
| AClient | `AgcmEventCharCustomize` | 17 | 5 | 4 |  | [AgcmEventCharCustomize](../Module/AgcmEventCharCustomize.md) |
| AClient | `AgcmEventCook` | 0 | 0 | 4 |  | – |
| AClient | `AgcmEventEffect` | 17 | 145 | 162 |  | [AgcmEventEffect](../Module/AgcmEventEffect.md) |
| AClient | `AgcmEventGacha` | 17 | 6 | 5 |  | [AgcmEventGacha](../Module/AgcmEventGacha.md) |
| AClient | `AgcmEventGuild` | 17 | 8 | 9 |  | [AgcmEventGuild](../Module/AgcmEventGuild.md) |
| AClient | `AgcmEventItemConvert` | 17 | 6 | 5 |  | [AgcmEventItemConvert](../Module/AgcmEventItemConvert.md) |
| AClient | `AgcmEventItemRepair` | 17 | 5 | 4 |  | [AgcmEventItemRepair](../Module/AgcmEventItemRepair.md) |
| AClient | `AgcmEventManager` | 17 | 7 | 7 |  | [AgcmEventManager](../Module/AgcmEventManager.md) |
| AClient | `AgcmEventNPCDialog` | 17 | 6 | 4 |  | [AgcmEventNPCDialog](../Module/AgcmEventNPCDialog.md) |
| AClient | `AgcmEventNPCTrade` | 17 | 12 | 22 | ja | [NPC_Trade_Dialog](../Module/NPC_Trade_Dialog.md) |
| AClient | `AgcmEventNature` | 17 | 58 | 93 |  | [AgcmEventNature](../Module/AgcmEventNature.md) |
| AClient | `AgcmEventPointLight` | 17 | 18 | 16 |  | [AgcmEventPointLight](../Module/AgcmEventPointLight.md) |
| AClient | `AgcmEventProduct` | 17 | 7 | 6 |  | [AgcmEventProduct](../Module/AgcmEventProduct.md) |
| AClient | `AgcmEventQuest` | 17 | 5 | 4 |  | [AgcmEventQuest](../Module/AgcmEventQuest.md) |
| AClient | `AgcmEventQuestDlg` | 0 | 0 | 3 |  | – |
| AClient | `AgcmEventRefinery` | 17 | 5 | 4 |  | [AgcmEventRefinery](../Module/AgcmEventRefinery.md) |
| AClient | `AgcmEventShrine` | 0 | 0 | 4 |  | – |
| AClient | `AgcmEventSiegeWarNPC` | 17 | 4 | 3 |  | [AgcmEventSiegeWarNPC](../Module/AgcmEventSiegeWarNPC.md) |
| AClient | `AgcmEventSkillMaster` | 17 | 10 | 11 |  | [AgcmEventSkillMaster](../Module/AgcmEventSkillMaster.md) |
| AClient | `AgcmEventTeleport` | 17 | 8 | 11 |  | [AgcmEventTeleport](../Module/AgcmEventTeleport.md) |
| AClient | `AgcmExportResource` | 0 | 0 | 67 |  | – |
| AClient | `AgcmFPSManager` | 0 | 0 | 3 |  | – |
| AClient | `AgcmFont` | 17 | 33 | 52 |  | [AgcmFont](../Module/AgcmFont.md) |
| AClient | `AgcmGeometryDataManager` | 0 | 0 | 24 |  | – |
| AClient | `AgcmGlare` | 17 | 7 | 4 |  | [AgcmGlare](../Module/AgcmGlare.md) |
| AClient | `AgcmGlobalAuth` | 0 | 0 | 2 |  | – |
| AClient | `AgcmGlyph` | 17 | 24 | 32 |  | [AgcmGlyph](../Module/AgcmGlyph.md) |
| AClient | `AgcmGrass` | 17 | 22 | 36 |  | [AgcmGrass](../Module/AgcmGrass.md) |
| AClient | `AgcmGuild` | 17 | 67 | 71 |  | [AgcmGuild](../Module/AgcmGuild.md) |
| AClient | `AgcmItem` | 17 | 132 | 137 |  | [AgcmItem](../Module/AgcmItem.md) |
| AClient | `AgcmItemConvert` | 17 | 15 | 16 |  | [AgcmItemConvert](../Module/AgcmItemConvert.md) |
| AClient | `AgcmLODManager` | 17 | 17 | 20 |  | [AgcmLODManager](../Module/AgcmLODManager.md) |
| AClient | `AgcmLensFlare` | 17 | 17 | 20 |  | [AgcmLensFlare](../Module/AgcmLensFlare.md) |
| AClient | `AgcmLogin` | 17 | 30 | 53 | ja | [AgcmLogin](../Module/AgcmLogin.md) |
| AClient | `AgcmMap` | 23 | 70 | 145 |  | [AgcmMap](../Module/AgcmMap.md) |
| AClient | `AgcmMinimap` | 17 | 41 | 50 |  | [AgcmMinimap](../Module/AgcmMinimap.md) |
| AClient | `AgcmNatureEffect` | 17 | 19 | 19 |  | [AgcmNatureEffect](../Module/AgcmNatureEffect.md) |
| AClient | `AgcmObject` | 17 | 47 | 102 | ja | [AgcmObject](../Module/AgcmObject.md) |
| AClient | `AgcmOcTree` | 17 | 25 | 44 |  | [AgcmOcTree](../Module/AgcmOcTree.md) |
| AClient | `AgcmParty` | 17 | 17 | 55 | ja | [AgcmParty](../Module/AgcmParty.md) |
| AClient | `AgcmPostFX` | 17 | 22 | 29 |  | [AgcmPostFX](../Module/AgcmPostFX.md) |
| AClient | `AgcmPreLODManager` | 0 | 0 | 22 |  | – |
| AClient | `AgcmPrivateTrade` | 17 | 15 | 44 | ja | [AgcmPrivateTrade](../Module/AgcmPrivateTrade.md) |
| AClient | `AgcmProduct` | 17 | 4 | 4 |  | [AgcmProduct](../Module/AgcmProduct.md) |
| AClient | `AgcmProductMed` | 17 | 9 | 7 |  | [AgcmProductMed](../Module/AgcmProductMed.md) |
| AClient | `AgcmQuest` | 17 | 11 | 14 |  | [AgcmQuest](../Module/AgcmQuest.md) |
| AClient | `AgcmRecruit` | 17 | 11 | 31 | ja | [AgcmRecruit](../Module/AgcmRecruit.md) |
| AClient | `AgcmRefinery` | 17 | 4 | 2 |  | [AgcmRefinery](../Module/AgcmRefinery.md) |
| AClient | `AgcmRegistryManager` | 0 | 1 | 0 |  | [AgcmRegistryManager](../Module/AgcmRegistryManager.md) |
| AClient | `AgcmRender` | 19 | 49 | 201 |  | [AgcmRender](../Module/AgcmRender.md) |
| AClient | `AgcmResourceLoader` | 17 | 38 | 48 |  | [AgcmResourceLoader](../Module/AgcmResourceLoader.md) |
| AClient | `AgcmReturnToLogin` | 17 | 10 | 11 |  | [AgcmReturnToLogin](../Module/AgcmReturnToLogin.md) |
| AClient | `AgcmRide` | 13 | 7 | 8 |  | [AgcmRide](../Module/AgcmRide.md) |
| AClient | `AgcmShadow` | 17 | 19 | 19 |  | [AgcmShadow](../Module/AgcmShadow.md) |
| AClient | `AgcmShadow2` | 17 | 20 | 23 |  | [AgcmShadow2](../Module/AgcmShadow2.md) |
| AClient | `AgcmShadowmap` | 17 | 34 | 34 |  | [AgcmShadowmap](../Module/AgcmShadowmap.md) |
| AClient | `AgcmShrine` | 21 | 62 | 78 |  | [AgcmShrine](../Module/AgcmShrine.md) |
| AClient | `AgcmSiegeWar` | 17 | 36 | 36 |  | [AgcmSiegeWar](../Module/AgcmSiegeWar.md) |
| AClient | `AgcmSkill` | 17 | 89 | 124 |  | [AgcmSkill](../Module/AgcmSkill.md) |
| AClient | `AgcmSound` | 17 | 40 | 44 |  | [AgcmSound](../Module/AgcmSound.md) |
| AClient | `AgcmStartupEncryption` | 17 | 14 | 11 |  | [AgcmStartupEncryption](../Module/AgcmStartupEncryption.md) |
| AClient | `AgcmTargeting` | 17 | 38 | 48 |  | [AgcmTargeting](../Module/AgcmTargeting.md) |
| AClient | `AgcmTextBoard` | 4 | 6 | 3 |  | [AgcmTextBoard](../Module/AgcmTextBoard.md) |
| AClient | `AgcmTitle` | 1 | 102 | 130 |  | [AgcmTitle](../Module/AgcmTitle.md) |
| AClient | `AgcmTuner` | 17 | 5 | 5 |  | [AgcmTuner](../Module/AgcmTuner.md) |
| AClient | `AgcmUIArchlord` | 17 | 14 | 12 |  | [AgcmUIArchlord](../Module/AgcmUIArchlord.md) |
| AClient | `AgcmUIAuction` | 17 | 54 | 56 |  | [AgcmUIAuction](../Module/AgcmUIAuction.md) |
| AClient | `AgcmUIBuddy` | 17 | 91 | 97 |  | [AgcmUIBuddy](../Module/AgcmUIBuddy.md) |
| AClient | `AgcmUICashInven` | 17 | 37 | 36 | ja | [AgcmUICashInven](../Module/AgcmUICashInven.md) |
| AClient | `AgcmUICashItemCabient` | 0 | 0 | 0 |  | [AgcmUICashItemCabient](../Module/AgcmUICashItemCabient.md) |
| AClient | `AgcmUICashMall` | 17 | 44 | 45 |  | [AgcmUICashMall](../Module/AgcmUICashMall.md) |
| AClient | `AgcmUICastle` | 0 | 0 | 0 |  | – |
| AClient | `AgcmUIChannel` | 17 | 60 | 64 |  | [AgcmUIChannel](../Module/AgcmUIChannel.md) |
| AClient | `AgcmUICharacter` | 14 | 97 | 122 |  | [AgcmUICharacter](../Module/AgcmUICharacter.md) |
| AClient | `AgcmUIChatting` | 0 | 0 | 19 |  | – |
| AClient | `AgcmUIChatting2` | 26 | 15 | 14 |  | [AgcmUIChatting2](../Module/AgcmUIChatting2.md) |
| AClient | `AgcmUIConsole` | 17 | 9 | 7 |  | [AgcmUIConsole](../Module/AgcmUIConsole.md) |
| AClient | `AgcmUIControl` | 18 | 15 | 15 |  | [AgcmUIControl](../Module/AgcmUIControl.md) |
| AClient | `AgcmUICooldown` | 17 | 17 | 18 |  | [AgcmUICooldown](../Module/AgcmUICooldown.md) |
| AClient | `AgcmUICustomizing` | 17 | 38 | 37 |  | [AgcmUICustomizing](../Module/AgcmUICustomizing.md) |
| AClient | `AgcmUIDebugInfo` | 17 | 7 | 6 |  | [AgcmUIDebugInfo](../Module/AgcmUIDebugInfo.md) |
| AClient | `AgcmUIEventBank` | 17 | 31 | 31 |  | [AgcmUIEventBank](../Module/AgcmUIEventBank.md) |
| AClient | `AgcmUIEventGacha` | 17 | 15 | 14 |  | [AgcmUIEventGacha](../Module/AgcmUIEventGacha.md) |
| AClient | `AgcmUIEventItemConvert` | 17 | 58 | 33 |  | [AgcmUIEventItemConvert](../Module/AgcmUIEventItemConvert.md) |
| AClient | `AgcmUIEventItemRepair` | 17 | 29 | 28 |  | [AgcmUIEventItemRepair](../Module/AgcmUIEventItemRepair.md) |
| AClient | `AgcmUIEventNPCDialog` | 18 | 15 | 13 |  | [AgcmUIEventNPCDialog](../Module/AgcmUIEventNPCDialog.md) |
| AClient | `AgcmUIEventTeleport` | 17 | 23 | 24 |  | [AgcmUIEventTeleport](../Module/AgcmUIEventTeleport.md) |
| AClient | `AgcmUIGuideMessage` | 17 | 31 | 35 |  | [AgcmUIGuideMessage](../Module/AgcmUIGuideMessage.md) |
| AClient | `AgcmUIGuild` | 17 | 220 | 40 |  | [AgcmUIGuild](../Module/AgcmUIGuild.md) |
| AClient | `AgcmUIGuildWarehouse` | 17 | 44 | 45 |  | [AgcmUIGuildWarehouse](../Module/AgcmUIGuildWarehouse.md) |
| AClient | `AgcmUIHelp` | 17 | 11 | 10 |  | [AgcmUIHelp](../Module/AgcmUIHelp.md) |
| AClient | `AgcmUIHotkey` | 17 | 24 | 32 |  | [AgcmUIHotkey](../Module/AgcmUIHotkey.md) |
| AClient | `AgcmUIItem` | 13 | 234 | 90 |  | [AgcmUIItem](../Module/AgcmUIItem.md) |
| AClient | `AgcmUILogin` | 21 | 87 | 106 |  | [AgcmUILogin](../Module/AgcmUILogin.md) |
| AClient | `AgcmUIMailBox` | 13 | 61 | 62 |  | [AgcmUIMailBox](../Module/AgcmUIMailBox.md) |
| AClient | `AgcmUIMain` | 17 | 111 | 134 |  | [AgcmUIMain](../Module/AgcmUIMain.md) |
| AClient | `AgcmUIManager2` | 17 | 75 | 172 |  | [AgcmUIManager2](../Module/AgcmUIManager2.md) |
| AClient | `AgcmUINotice` | 17 | 13 | 12 |  | [AgcmUINotice](../Module/AgcmUINotice.md) |
| AClient | `AgcmUIOption` | 17 | 107 | 135 |  | [AgcmUIOption](../Module/AgcmUIOption.md) |
| AClient | `AgcmUIParty` | 17 | 84 | 88 |  | [AgcmUIParty](../Module/AgcmUIParty.md) |
| AClient | `AgcmUIPartyOption` | 17 | 21 | 26 | ja | [AgcmUIPartyOption](../Module/AgcmUIPartyOption.md) |
| AClient | `AgcmUIProduct` | 17 | 37 | 40 |  | [AgcmUIProduct](../Module/AgcmUIProduct.md) |
| AClient | `AgcmUIPvP` | 17 | 20 | 18 |  | [AgcmUIPvP](../Module/AgcmUIPvP.md) |
| AClient | `AgcmUIQuest2` | 17 | 83 | 88 |  | [AgcmUIQuest2](../Module/AgcmUIQuest2.md) |
| AClient | `AgcmUIRefinery` | 17 | 39 | 44 |  | [AgcmUIRefinery](../Module/AgcmUIRefinery.md) |
| AClient | `AgcmUIRemission` | 17 | 26 | 28 |  | [AgcmUIRemission](../Module/AgcmUIRemission.md) |
| AClient | `AgcmUISearch` | 17 | 12 | 18 |  | [AgcmUISearch](../Module/AgcmUISearch.md) |
| AClient | `AgcmUIShrineShop` | 17 | 19 | 17 |  | [AgcmUIShrineShop](../Module/AgcmUIShrineShop.md) |
| AClient | `AgcmUISiegeWar` | 17 | 92 | 120 |  | [AgcmUISiegeWar](../Module/AgcmUISiegeWar.md) |
| AClient | `AgcmUISkill2` | 17 | 156 | 133 |  | [AgcmUISkill2](../Module/AgcmUISkill2.md) |
| AClient | `AgcmUISocialAction` | 17 | 15 | 18 |  | [AgcmUISocialAction](../Module/AgcmUISocialAction.md) |
| AClient | `AgcmUISplitItem` | 17 | 26 | 26 |  | [AgcmUISplitItem](../Module/AgcmUISplitItem.md) |
| AClient | `AgcmUIStatus` | 17 | 15 | 14 |  | [AgcmUIStatus](../Module/AgcmUIStatus.md) |
| AClient | `AgcmUISystemMessage` | 0 | 0 | 0 |  | – |
| AClient | `AgcmUITax` | 13 | 54 | 58 |  | [AgcmUITax](../Module/AgcmUITax.md) |
| AClient | `AgcmUITips` | 17 | 17 | 14 |  | [AgcmUITips](../Module/AgcmUITips.md) |
| AClient | `AgcmUIWantedCriminal` | 13 | 58 | 60 |  | [AgcmUIWantedCriminal](../Module/AgcmUIWantedCriminal.md) |
| AClient | `AgcmUIWarInfo` | 17 | 18 | 20 |  | [AgcmUIWarInfo](../Module/AgcmUIWarInfo.md) |
| AClient | `AgcmUVAnimation` | 17 | 20 | 20 |  | [AgcmUVAnimation](../Module/AgcmUVAnimation.md) |
| AClient | `AgcmWarInfo` | 17 | 14 | 14 |  | [AgcmWarInfo](../Module/AgcmWarInfo.md) |
| AClient | `AgcmWater` | 17 | 46 | 76 |  | [AgcmWater](../Module/AgcmWater.md) |
| AClient | `AgcmWorld` | 17 | 13 | 11 |  | [AgcmWorld](../Module/AgcmWorld.md) |
| APublic | `AgpmAI` | 0 | 0 | 41 | ja | – |
| APublic | `AgpmAI2` | 0 | 0 | 41 |  | – |
| APublic | `AgpmAdmin` | 13 | 14 | 102 | ja | [AgpmAdmin](../Module/AgpmAdmin.md) |
| APublic | `AgpmArchlord` | 14 | 10 | 36 | ja | [AgpmArchlord](../Module/AgpmArchlord.md) |
| APublic | `AgpmAreaChatting` | 13 | 4 | 6 | ja | [AgpmAreaChatting](../Module/AgpmAreaChatting.md) |
| APublic | `AgpmAuction` | 13 | 18 | 42 | ja | [AgpmAuction](../Module/AgpmAuction.md) |
| APublic | `AgpmAuctionCategory` | 13 | 8 | 3 |  | [AgpmAuctionCategory](../Module/AgpmAuctionCategory.md) |
| APublic | `AgpmBattleGround` | 13 | 6 | 5 |  | [AgpmBattleGround](../Module/AgpmBattleGround.md) |
| APublic | `AgpmBillInfo` | 13 | 7 | 13 | ja | [AgpmBillInfo](../Module/AgpmBillInfo.md) |
| APublic | `AgpmBuddy` | 13 | 9 | 55 | ja | [AgpmBuddy](../Module/AgpmBuddy.md) |
| APublic | `AgpmCashMall` | 13 | 12 | 28 | ja | [AgpmCashMall](../Module/AgpmCashMall.md) |
| APublic | `AgpmCasper` | 13 | 5 | 9 | ja | [AgpmCasper](../Module/AgpmCasper.md) |
| APublic | `AgpmCastle` | 0 | 0 | 0 |  | – |
| APublic | `AgpmChannel` | 13 | 14 | 34 | ja | [AgpmChannel](../Module/AgpmChannel.md) |
| APublic | `AgpmCharacter` | 13 | 135 | 371 | ja | [AgpmCharacter](../Module/AgpmCharacter.md) |
| APublic | `AgpmChatting` | 13 | 12 | 39 | ja | [AgpmChatting](../Module/AgpmChatting.md) |
| APublic | `AgpmCombat` | 13 | 26 | 51 |  | [AgpmCombat](../Module/AgpmCombat.md) |
| APublic | `AgpmConfig` | 13 | 6 | 64 | ja | [AgpmConfig](../Module/AgpmConfig.md) |
| APublic | `AgpmDropItem` | 0 | 0 | 5 |  | – |
| APublic | `AgpmDropItem2` | 0 | 0 | 34 |  | – |
| APublic | `AgpmEpicZone` | 0 | 0 | 5 |  | – |
| APublic | `AgpmEventBank` | 13 | 7 | 11 | ja | [AgpmEventBank](../Module/AgpmEventBank.md) |
| APublic | `AgpmEventBinding` | 0 | 0 | 24 |  | – |
| APublic | `AgpmEventCharCustomize` | 13 | 14 | 18 | ja | [AgpmEventCharCustomize](../Module/AgpmEventCharCustomize.md) |
| APublic | `AgpmEventCook` | 0 | 0 | 9 | ja | – |
| APublic | `AgpmEventFactors` | 0 | 0 | 9 |  | – |
| APublic | `AgpmEventGacha` | 13 | 10 | 15 | ja | [AgpmEventGacha](../Module/AgpmEventGacha.md) |
| APublic | `AgpmEventGuide` | 13 | 5 | 17 | ja | [AgpmEventGuide](../Module/AgpmEventGuide.md) |
| APublic | `AgpmEventGuild` | 13 | 13 | 22 | ja | [AgpmEventGuild](../Module/AgpmEventGuild.md) |
| APublic | `AgpmEventItemConvert` | 13 | 8 | 10 | ja | [AgpmEventItemConvert](../Module/AgpmEventItemConvert.md) |
| APublic | `AgpmEventItemRepair` | 13 | 11 | 19 | ja | [AgpmEventItemRepair](../Module/AgpmEventItemRepair.md) |
| APublic | `AgpmEventNPCDialog` | 13 | 20 | 21 | ja | [NPC_Trade_Dialog](../Module/NPC_Trade_Dialog.md) |
| APublic | `AgpmEventNPCTrade` | 13 | 8 | 9 |  | [AgpmEventNPCTrade](../Module/AgpmEventNPCTrade.md) |
| APublic | `AgpmEventNature` | 13 | 11 | 54 | ja | [AgpmEventNature](../Module/AgpmEventNature.md) |
| APublic | `AgpmEventPointLight` | 13 | 9 | 7 |  | [AgpmEventPointLight](../Module/AgpmEventPointLight.md) |
| APublic | `AgpmEventProduct` | 13 | 21 | 36 | ja | [AgpmEventProduct](../Module/AgpmEventProduct.md) |
| APublic | `AgpmEventQuest` | 13 | 15 | 17 | ja | [Quest](../Module/Quest.md) |
| APublic | `AgpmEventRefinery` | 13 | 8 | 17 | ja | [AgpmEventRefinery](../Module/AgpmEventRefinery.md) |
| APublic | `AgpmEventSiegeWarNPC` | 13 | 9 | 9 | ja | [AgpmEventSiegeWarNPC](../Module/AgpmEventSiegeWarNPC.md) |
| APublic | `AgpmEventSkillMaster` | 13 | 72 | 117 | ja | [AgpmEventSkillMaster](../Module/AgpmEventSkillMaster.md) |
| APublic | `AgpmEventSpawn` | 0 | 0 | 38 |  | – |
| APublic | `AgpmEventTeleport` | 13 | 36 | 70 | ja | [AgpmEventTeleport](../Module/AgpmEventTeleport.md) |
| APublic | `AgpmEventUvUReward` | 0 | 0 | 12 | ja | – |
| APublic | `AgpmFactors` | 13 | 61 | 120 |  | [AgpmFactors](../Module/AgpmFactors.md) |
| APublic | `AgpmGamble` | 0 | 0 | 20 | ja | – |
| APublic | `AgpmGrid` | 13 | 36 | 44 |  | [AgpmGrid](../Module/AgpmGrid.md) |
| APublic | `AgpmGuild` | 13 | 100 | 285 | ja | [AgpmGuild](../Module/AgpmGuild.md) |
| APublic | `AgpmGuildWarehouse` | 13 | 11 | 34 | ja | [AgpmGuildWarehouse](../Module/AgpmGuildWarehouse.md) |
| APublic | `AgpmItem` | 13 | 172 | 327 | ja | [AgpmItem](../Module/AgpmItem.md) |
| APublic | `AgpmItemConvert` | 13 | 42 | 44 | ja | [AgpmItemConvert](../Module/AgpmItemConvert.md) |
| APublic | `AgpmLog` | 0 | 0 | 59 |  | – |
| APublic | `AgpmLogin` | 13 | 8 | 7 |  | [AgpmLogin](../Module/AgpmLogin.md) |
| APublic | `AgpmMailBox` | 13 | 17 | 30 | ja | [AgpmMailBox](../Module/AgpmMailBox.md) |
| APublic | `AgpmMonsterPath` | 0 | 0 | 29 |  | – |
| APublic | `AgpmNatureEffect` | 13 | 4 | 6 | ja | [AgpmNatureEffect](../Module/AgpmNatureEffect.md) |
| APublic | `AgpmOptimizedPacket2` | 13 | 11 | 37 | ja | [AgpmOptimizedPacket2](../Module/AgpmOptimizedPacket2.md) |
| APublic | `AgpmParty` | 13 | 27 | 92 | ja | [AgpmParty](../Module/AgpmParty.md) |
| APublic | `AgpmPathFind` | 13 | 6 | 13 |  | [AgpmPathFind](../Module/AgpmPathFind.md) |
| APublic | `AgpmPathManager` | 0 | 0 | 1 |  | – |
| APublic | `AgpmProduct` | 13 | 24 | 50 | ja | [AgpmProduct](../Module/AgpmProduct.md) |
| APublic | `AgpmPvP` | 13 | 60 | 138 | ja | [AgpmPvP](../Module/AgpmPvP.md) |
| APublic | `AgpmQuest` | 13 | 17 | 37 | ja | [Quest](../Module/Quest.md) |
| APublic | `AgpmRecruit` | 0 | 0 | 0 |  | – |
| APublic | `AgpmRefinery` | 13 | 9 | 15 | ja | [AgpmRefinery](../Module/AgpmRefinery.md) |
| APublic | `AgpmRemission` | 13 | 10 | 16 | ja | [AgpmRemission](../Module/AgpmRemission.md) |
| APublic | `AgpmResourceInfo` | 13 | 6 | 5 |  | [AgpmResourceInfo](../Module/AgpmResourceInfo.md) |
| APublic | `AgpmReturnToLogin` | 13 | 10 | 23 | ja | [AgpmReturnToLogin](../Module/AgpmReturnToLogin.md) |
| APublic | `AgpmRide` | 13 | 5 | 11 | ja | [AgpmRide](../Module/AgpmRide.md) |
| APublic | `AgpmScript` | 13 | 5 | 11 | ja | [AgpmScript](../Module/AgpmScript.md) |
| APublic | `AgpmSearch` | 13 | 8 | 14 | ja | [AgpmSearch](../Module/AgpmSearch.md) |
| APublic | `AgpmShrine` | 0 | 0 | 60 | ja | – |
| APublic | `AgpmShrineBattle` | 13 | 7 | 45 | ja | [AgpmShrineBattle](../Module/AgpmShrineBattle.md) |
| APublic | `AgpmSiegeWar` | 13 | 70 | 192 | ja | [AgpmSiegeWar](../Module/AgpmSiegeWar.md) |
| APublic | `AgpmSkill` | 13 | 65 | 238 | ja | [AgpmSkill](../Module/AgpmSkill.md) |
| APublic | `AgpmStartupEncryption` | 13 | 11 | 19 | ja | [AgpmStartupEncryption](../Module/AgpmStartupEncryption.md) |
| APublic | `AgpmSummons` | 13 | 19 | 60 | ja | [AgpmSummons](../Module/AgpmSummons.md) |
| APublic | `AgpmSystemMessage` | 14 | 1 | 10 | ja | [AgpmSystemMessage](../Module/AgpmSystemMessage.md) |
| APublic | `AgpmTax` | 13 | 14 | 29 | ja | [AgpmTax](../Module/AgpmTax.md) |
| APublic | `AgpmTimer` | 13 | 5 | 21 | ja | [AgpmTimer](../Module/AgpmTimer.md) |
| APublic | `AgpmTitle` | 13 | 16 | 53 | ja | [AgpmTitle](../Module/AgpmTitle.md) |
| APublic | `AgpmTransform` | 0 | 0 | 4 |  | – |
| APublic | `AgpmUIStatus` | 13 | 13 | 21 | ja | [AgpmUIStatus](../Module/AgpmUIStatus.md) |
| APublic | `AgpmUnion` | 13 | 4 | 10 |  | [AgpmUnion](../Module/AgpmUnion.md) |
| APublic | `AgpmWantedCriminal` | 13 | 12 | 37 | ja | [AgpmWantedCriminal](../Module/AgpmWantedCriminal.md) |
| APublic | `AgpmWarInfo` | 13 | 4 | 12 | ja | [AgpmWarInfo](../Module/AgpmWarInfo.md) |
| APublic | `AgpmWorld` | 13 | 5 | 14 | ja | [AgpmWorld](../Module/AgpmWorld.md) |
| APublic | `ApAdmin` | 1 | 23 | 35 |  | [ApAdmin](../Module/ApAdmin.md) |
| APublic | `ApBase` | 0 | 0 | 0 |  | – |
| APublic | `ApIOCPDispatcher` | 0 | 0 | 5 |  | – |
| APublic | `ApMemory` | 0 | 20 | 0 |  | – |
| APublic | `ApMemoryTracker` | 0 | 0 | 13 |  | – |
| APublic | `ApModule` | 13 | 40 | 59 |  | [ApModule](../Module/ApModule.md) |
| APublic | `ApServerMonitor` | 0 | 0 | 0 |  | – |
| APublic | `ApSingleton` | 0 | 0 | 0 |  | – |
| APublic | `ApmEventManager` | 13 | 27 | 45 | ja | [ApmEventManager](../Module/ApmEventManager.md) |
| APublic | `ApmEventManagerDlg` | 0 | 0 | 7 |  | – |
| APublic | `ApmFactors` | 0 | 0 | 9 |  | – |
| APublic | `ApmMap` | 13 | 71 | 143 |  | [ApmMap](../Module/ApmMap.md) |
| APublic | `ApmObject` | 13 | 30 | 53 |  | [ApmObject](../Module/ApmObject.md) |
| APublic | `ApmOcTree` | 13 | 28 | 40 |  | [ApmOcTree](../Module/ApmOcTree.md) |
| APublic | `ApmProfiler` | 0 | 0 | 10 |  | – |
| AServer | `AgsmAI` | 0 | 0 | 20 |  | Server |
| AServer | `AgsmAI2` | 0 | 0 | 65 |  | Server |
| AServer | `AgsmAOIFilter` | 0 | 0 | 37 |  | Server |
| AServer | `AgsmAccountManager` | 0 | 0 | 35 |  | Server |
| AServer | `AgsmAdmin` | 0 | 0 | 112 | ja | Server |
| AServer | `AgsmArchlord` | 0 | 0 | 56 |  | Server |
| AServer | `AgsmAreaChatting` | 0 | 0 | 22 |  | Server |
| AServer | `AgsmAuction` | 0 | 0 | 56 |  | Server |
| AServer | `AgsmAuctionClient` | 0 | 0 | 25 | ja | Server |
| AServer | `AgsmAuctionRelay` | 0 | 0 | 49 | ja | Server |
| AServer | `AgsmAuctionServer` | 0 | 0 | 20 | ja | Server |
| AServer | `AgsmAuctionServerDB` | 0 | 0 | 3 |  | Server |
| AServer | `AgsmBattleGround` | 0 | 0 | 32 | ja | Server |
| AServer | `AgsmBillInfo` | 0 | 0 | 5 |  | Server |
| AServer | `AgsmBilling` | 0 | 0 | 50 | ja | Server |
| AServer | `AgsmBillingChina` | 0 | 0 | 13 |  | Server |
| AServer | `AgsmBillingGlobal` | 0 | 0 | 19 |  | Server |
| AServer | `AgsmBillingJapan` | 0 | 0 | 5 |  | Server |
| AServer | `AgsmBuddy` | 0 | 0 | 59 |  | Server |
| AServer | `AgsmCashMall` | 0 | 0 | 16 |  | Server |
| AServer | `AgsmCasper` | 0 | 0 | 5 |  | Server |
| AServer | `AgsmCastle` | 0 | 0 | 0 |  | Server |
| AServer | `AgsmChannel` | 0 | 0 | 38 |  | Server |
| AServer | `AgsmCharManager` | 0 | 0 | 56 | ja | Server |
| AServer | `AgsmCharacter` | 0 | 0 | 187 | ja | Server |
| AServer | `AgsmChatting` | 0 | 0 | 46 |  | Server |
| AServer | `AgsmCombat` | 0 | 0 | 27 |  | Server |
| AServer | `AgsmConfig` | 0 | 0 | 12 |  | Server |
| AServer | `AgsmConnectionSetupGame` | 0 | 0 | 19 | ja | Server |
| AServer | `AgsmConnectionSetupLogin` | 0 | 0 | 8 | ja | Server |
| AServer | `AgsmConnectionSetupRelay` | 0 | 0 | 11 | ja | Server |
| AServer | `AgsmDBPool` | 0 | 0 | 8 |  | Server |
| AServer | `AgsmDatabaseConfig` | 0 | 0 | 14 |  | Server |
| AServer | `AgsmDatabasePool` | 0 | 0 | 9 |  | Server |
| AServer | `AgsmDeath` | 0 | 0 | 61 | ja | Server |
| AServer | `AgsmDropItem` | 0 | 0 | 14 |  | Server |
| AServer | `AgsmDropItem2` | 0 | 0 | 7 |  | Server |
| AServer | `AgsmEpicZone` | 0 | 0 | 26 |  | Server |
| AServer | `AgsmEventBank` | 0 | 0 | 3 |  | Server |
| AServer | `AgsmEventCharCustomize` | 0 | 0 | 3 |  | Server |
| AServer | `AgsmEventCook` | 0 | 0 | 2 |  | Server |
| AServer | `AgsmEventGacha` | 0 | 0 | 7 |  | Server |
| AServer | `AgsmEventGuild` | 0 | 0 | 4 |  | Server |
| AServer | `AgsmEventItemConvert` | 0 | 0 | 2 |  | Server |
| AServer | `AgsmEventItemRepair` | 0 | 0 | 7 |  | Server |
| AServer | `AgsmEventManager` | 0 | 0 | 3 |  | Server |
| AServer | `AgsmEventNPCDialog` | 0 | 0 | 3 |  | Server |
| AServer | `AgsmEventNPCTrade` | 0 | 0 | 22 | ja | Server |
| AServer | `AgsmEventNature` | 0 | 0 | 5 |  | Server |
| AServer | `AgsmEventProduct` | 0 | 0 | 6 |  | Server |
| AServer | `AgsmEventQuest` | 0 | 0 | 2 |  | Server |
| AServer | `AgsmEventRefinery` | 0 | 0 | 2 |  | Server |
| AServer | `AgsmEventSiegeWarNPC` | 0 | 0 | 2 |  | Server |
| AServer | `AgsmEventSkillMaster` | 0 | 0 | 24 |  | Server |
| AServer | `AgsmEventSpawn` | 0 | 0 | 17 |  | Server |
| AServer | `AgsmEventSystem` | 0 | 0 | 24 |  | Server |
| AServer | `AgsmEventTeleport` | 0 | 0 | 12 |  | Server |
| AServer | `AgsmEventUvUReward` | 0 | 0 | 6 |  | Server |
| AServer | `AgsmFactors` | 0 | 0 | 24 |  | Server |
| AServer | `AgsmGKforPCRoom` | 0 | 0 | 0 | ja | Server |
| AServer | `AgsmGamble` | 0 | 0 | 9 |  | Server |
| AServer | `AgsmGameholic` | 0 | 0 | 6 |  | Server |
| AServer | `AgsmGlobalChatting` | 0 | 0 | 12 | ja | Server |
| AServer | `AgsmGuild` | 0 | 0 | 288 | ja | Server |
| AServer | `AgsmGuildWarehouse` | 0 | 0 | 40 |  | Server |
| AServer | `AgsmIPBlockingManager` | 0 | 0 | 0 |  | Server |
| AServer | `AgsmInterServerLink` | 0 | 0 | 38 | ja | Server |
| AServer | `AgsmItem` | 0 | 0 | 136 | ja | Server |
| AServer | `AgsmItemConvert` | 0 | 0 | 22 |  | Server |
| AServer | `AgsmItemManager` | 0 | 0 | 29 |  | Server |
| AServer | `AgsmLog` | 0 | 0 | 31 | ja | Server |
| AServer | `AgsmLogin` | 0 | 0 | 4 | ja | Server |
| AServer | `AgsmLoginClient` | 0 | 0 | 58 | ja | Server |
| AServer | `AgsmLoginDB` | 0 | 0 | 72 |  | Server |
| AServer | `AgsmLoginServer` | 0 | 0 | 7 |  | Server |
| AServer | `AgsmMailBox` | 0 | 0 | 35 |  | Server |
| AServer | `AgsmMakeSQL` | 0 | 0 | 44 |  | Server |
| AServer | `AgsmMap` | 0 | 0 | 10 |  | Server |
| AServer | `AgsmNotification` | 0 | 0 | 0 |  | Server |
| AServer | `AgsmNpcManager` | 0 | 1 | 80 |  | Server |
| AServer | `AgsmObject` | 0 | 0 | 11 | ja | Server |
| AServer | `AgsmPacketMonitor` | 0 | 0 | 8 |  | Server |
| AServer | `AgsmParty` | 0 | 0 | 96 | ja | Server |
| AServer | `AgsmPrivateTrade` | 0 | 0 | 52 | ja | Server |
| AServer | `AgsmProduct` | 0 | 0 | 23 |  | Server |
| AServer | `AgsmPvP` | 0 | 0 | 133 |  | Server |
| AServer | `AgsmQuest` | 0 | 0 | 46 |  | Server |
| AServer | `AgsmRecruit` | 0 | 0 | 9 | ja | Server |
| AServer | `AgsmRecruitClient` | 0 | 0 | 20 | ja | Server |
| AServer | `AgsmRecruitServer` | 0 | 0 | 19 | ja | Server |
| AServer | `AgsmRecruitServerDB` | 0 | 0 | 13 |  | Server |
| AServer | `AgsmRefinery` | 0 | 0 | 14 |  | Server |
| AServer | `AgsmRelay` | 0 | 0 | 27 | ja | Server |
| AServer | `AgsmRelay2` | 0 | 0 | 66 | ja | Server |
| AServer | `AgsmRemission` | 0 | 0 | 8 |  | Server |
| AServer | `AgsmReturnToLogin` | 0 | 0 | 17 |  | Server |
| AServer | `AgsmRide` | 0 | 0 | 25 |  | Server |
| AServer | `AgsmSearch` | 0 | 0 | 7 |  | Server |
| AServer | `AgsmServerManager` | 0 | 0 | 68 | ja | Server |
| AServer | `AgsmServerManager2` | 0 | 0 | 33 |  | Server |
| AServer | `AgsmServerStatus` | 0 | 0 | 28 |  | Server |
| AServer | `AgsmShrine` | 0 | 0 | 15 |  | Server |
| AServer | `AgsmShrineBattle` | 0 | 0 | 77 |  | Server |
| AServer | `AgsmSiegeWar` | 0 | 0 | 161 |  | Server |
| AServer | `AgsmSkill` | 0 | 0 | 300 | ja | Server |
| AServer | `AgsmSkillManager` | 0 | 0 | 27 |  | Server |
| AServer | `AgsmStartupEncryption` | 0 | 0 | 14 |  | Server |
| AServer | `AgsmSummons` | 0 | 0 | 37 |  | Server |
| AServer | `AgsmSystemInfo` | 0 | 0 | 4 | ja | Server |
| AServer | `AgsmSystemMessage` | 0 | 0 | 16 |  | Server |
| AServer | `AgsmTax` | 0 | 0 | 29 |  | Server |
| AServer | `AgsmTimer` | 0 | 0 | 5 |  | Server |
| AServer | `AgsmTitle` | 0 | 0 | 81 |  | Server |
| AServer | `AgsmTrade` | 0 | 0 | 15 |  | Server |
| AServer | `AgsmUIStatus` | 0 | 0 | 16 |  | Server |
| AServer | `AgsmUnion` | 0 | 0 | 10 |  | Server |
| AServer | `AgsmUsedCharDataPool` | 0 | 0 | 15 |  | Server |
| AServer | `AgsmWantedCriminal` | 0 | 0 | 41 |  | Server |
| AServer | `AgsmWarInfo` | 0 | 0 | 22 |  | Server |
| AServer | `AgsmWorld` | 0 | 0 | 14 |  | Server |
| AServer | `AgsmZoning` | 0 | 0 | 35 | ja | Server |
| AUtility | `AuBplusTree` | 0 | 0 | 0 |  | – |
| AUtility | `AuConsole` | 2 | 7 | 9 |  | [AuConsole](../Module/AuConsole.md) |
| AUtility | `AuCrypt` | 0 | 0 | 0 |  | – |
| AUtility | `AuCryptAlgorithm` | 0 | 0 | 0 |  | – |
| AUtility | `AuDatabase` | 0 | 0 | 0 |  | – |
| AUtility | `AuDatabase2` | 0 | 0 | 26 |  | – |
| AUtility | `AuEtcUtil` | 0 | 0 | 0 |  | – |
| AUtility | `AuExcelLib` | 8 | 2 | 0 |  | [AuExcelLib](../Module/AuExcelLib.md) |
| AUtility | `AuExcelTxtLib` | 8 | 16 | 13 |  | [AuExcelTxtLib](../Module/AuExcelTxtLib.md) |
| AUtility | `AuExportedFileDic` | 0 | 0 | 0 |  | – |
| AUtility | `AuFileFind` | 1 | 8 | 20 |  | [AuFileFind](../Module/AuFileFind.md) |
| AUtility | `AuGameEnv` | 0 | 1 | 2 |  | [AuGameEnv](../Module/AuGameEnv.md) |
| AUtility | `AuGameGuard` | 0 | 0 | 0 |  | – |
| AUtility | `AuGenerateID` | 1 | 6 | 4 |  | [AuGenerateID](../Module/AuGenerateID.md) |
| AUtility | `AuIgnoringHelper` | 0 | 0 | 3 |  | – |
| AUtility | `AuIniFile` | 0 | 0 | 37 |  | – |
| AUtility | `AuIniManager` | 0 | 0 | 0 |  | – |
| AUtility | `AuIniPackingManager` | 0 | 0 | 0 |  | – |
| AUtility | `AuJapan` | 0 | 0 | 0 |  | – |
| AUtility | `AuKbHook` | 0 | 0 | 0 |  | – |
| AUtility | `AuLocalize` | 0 | 0 | 0 |  | – |
| AUtility | `AuLog` | 0 | 0 | 4 |  | – |
| AUtility | `AuLua` | 1 | 8 | 17 |  | [AuLua](../Module/AuLua.md) |
| AUtility | `AuMD5EnCrypt` | 0 | 0 | 0 |  | – |
| AUtility | `AuMailClient` | 0 | 0 | 4 |  | – |
| AUtility | `AuMappedPool` | 0 | 0 | 0 |  | – |
| AUtility | `AuMath` | 0 | 0 | 20 |  | – |
| AUtility | `AuPacket` | 0 | 12 | 14 |  | [AuPacket](../Module/AuPacket.md) |
| AUtility | `AuPackingManager` | 0 | 11 | 55 |  | [AuPackingManager](../Module/AuPackingManager.md) |
| AUtility | `AuParallel` | 0 | 0 | 0 |  | – |
| AUtility | `AuPatchCheckCode` | 0 | 0 | 4 |  | – |
| AUtility | `AuProcessManager` | 0 | 0 | 3 |  | – |
| AUtility | `AuProfileManager` | 0 | 0 | 6 |  | – |
| AUtility | `AuRandomNumberGenerator` | 0 | 0 | 0 |  | – |
| AUtility | `AuRegistry` | 0 | 0 | 19 |  | – |
| AUtility | `AuResourceKeeper` | 0 | 0 | 0 |  | – |
| AUtility | `AuScriptEngine` | 4 | 3 | 0 |  | [AuScriptEngine](../Module/AuScriptEngine.md) |
| AUtility | `AuSendDebugInfo` | 0 | 0 | 3 |  | – |
| AUtility | `AuService` | 0 | 0 | 28 |  | – |
| AUtility | `AuSnappy` | 0 | 0 | 0 |  | – |
| AUtility | `AuStaticPool` | 0 | 0 | 0 |  | – |
| AUtility | `AuStrTable` | 0 | 0 | 5 |  | – |
| AUtility | `AuStringConv` | 0 | 0 | 0 |  | – |
| AUtility | `AuThread` | 0 | 0 | 6 |  | – |
| AUtility | `AuTickCounter` | 1 | 5 | 3 |  | [AuTickCounter](../Module/AuTickCounter.md) |
| AUtility | `AuTimeStamp` | 0 | 0 | 7 |  | – |
| AUtility | `AuXCrashReport` | 0 | 12 | 0 |  | [AuXCrashReport](../Module/AuXCrashReport.md) |
| AUtility | `AuXmlParser` | 18 | 5 | 2 |  | [AuXmlParser](../Module/AuXmlParser.md) |
| AUtility | `AuZpackLoader` | 0 | 0 | 0 |  | – |

## Grenzen

- Module ohne Bericht (Rendering, UI, Hilfsklassen ohne Paketverarbeitung) sind nur über vtable-Slots, Aufrufstellen und die übrigen Namensquellen (Zeichenketten, Callback-Registrierung) benannt; ihre Funktionen wurden nicht einzeln gegen die Quelle abgeglichen.
- „benannt“ zählt nur Namen mit Modulpräfix; Hilfsfunktionen ohne Modulzuordnung und generische Namen (`ctor_or_dtor_…`) zählen mit.
