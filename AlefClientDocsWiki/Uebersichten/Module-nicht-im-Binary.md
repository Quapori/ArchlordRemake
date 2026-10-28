# Module der EP8-Quelle ohne Entsprechung im 2017er Client

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Für jedes Modul der Inventur (AClient, APublic, AUtility), zu dem es keine eigene Modulanalyse gibt, sind hier die Belege gesammelt. Methode: (1) kommt der Modulname als Zeichenkette im Binary vor (jede `ApModule`-Klasse trägt ihren Namen im Konstruktor und wird bei `GetModule` mit dem Namen gesucht); (2) kommen RTTI-Namen (`.?AV<Klasse>@@`) vor; (3) welche Module der Quelle binden die Kopfdatei ein. **Aussage:** Ist ein `ApModule`-Modul weder als Name noch als RTTI im Binary und binden es nur Module ein, die ebenfalls fehlen oder es nicht per `GetModule` suchen, ist es in diesem Build nicht enthalten. Bei Hilfsbibliotheken ohne eigene Klasse (reine Funktionen) beweist das Fehlen von Namen nichts; sie stehen mit „Verbleib offen“.

| Gruppe | Modul | Art | Name im Binary | RTTI im Binary | Zeichenketten der Quelle im Binary | bindet ein (Quelle) | Befund |
|---|---|---|---:|---|---:|---|---|
| AClient | `AgcSplashWindow` | Hilfsbibliothek | 0 | `XPngStream` | 3 von 3 | – | Klassen teilweise vorhanden: XPngStream – SplashWindow, XPng, XBitmap, XInflate fehlen (kein Name, kein RTTI, keine Zeichenkette der Quelle); vorhanden sind nur XPngStream/XPngStreamImpl/XBitmapStream (anderer Code, 0x00713200-0x00713900). |
| AClient | `AgcmAIDlg` | Modul (`ApModule`) | 0 | – | 13 von 36 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmAnimation` | Hilfsbibliothek | 0 | [`AgcaAnimation2`](../Module/AgcaAnimation2.md), `AgcdAnimationCallbackList` | 1 von 3 | `AgcmCharacter`, [`AgcmObject`](../Module/AgcmObject.md), [`AgcmSkill`](../Module/AgcmSkill.md) | Klassen teilweise vorhanden: AgcaAnimation2, AgcdAnimationCallbackList – Modulklasse fehlt; die Verwaltung AgcaAnimation2 ist vorhanden (Bericht AgcaAnimation2). |
| AClient | `AgcmEffectDataAdmin` | Hilfsbibliothek | 0 | [`AgcaEffectData2`](../Module/AgcaEffectData2.md) | 1 von 1 | [`AgcmEventEffect`](../Module/AgcmEventEffect.md), `AgcmSkill` | Klassen teilweise vorhanden: AgcaEffectData2 – Bericht AgcaEffectData2. |
| AClient | `AgcmEventCook` | Modul (`ApModule`) | 0 | – | 3 von 5 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmEventQuestDlg` | Modul (`ApModule`) | 0 | – | 0 von 3 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmEventShrine` | Modul (`ApModule`) | 0 | – | 2 von 3 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmExportResource` | Modul (`ApModule`) | 0 | – | 58 von 322 | `AgcmCharacter`, `AgcmObject` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmFPSManager` | Hilfsbibliothek | 0 | – | 0 von 0 | [`AgcSkeleton`](../Module/AgcSkeleton.md), [`AgcmUIOption`](../Module/AgcmUIOption.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AClient | `AgcmGeometryDataManager` | Modul (`ApModule`) | 0 | – | 12 von 14 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmGlobalAuth` | Hilfsbibliothek | 0 | – | 3 von 4 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AClient | `AgcmPreLODManager` | Modul (`ApModule`) | 0 | – | 14 von 37 | `AgcmCharacter`, `AgcmObject` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | [`AgcmRegistryManager`](../Module/AgcmRegistryManager.md) | Hilfsbibliothek | 0 | – | 4 von 5 | [`AgcAuth`](../Module/AgcAuth.md), `AgcSkeleton`, [`AgcmLogin`](../Module/AgcmLogin.md), [`AgcmUILogin`](../Module/AgcmUILogin.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AClient | `AgcmUICastle` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AClient | `AgcmUIChatting` | Modul (`ApModule`) | 0 | – | 2 von 12 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AClient | `AgcmUISystemMessage` | Hilfsbibliothek | 0 | – | 0 von 0 | [`AgcmUIItem`](../Module/AgcmUIItem.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `AgpmAI` | Modul (`ApModule`) | 0 | – | 5 von 10 | `AgsmAI` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmAI2` | Modul (`ApModule`) | 0 | – | 7 von 9 | [`AgpmShrineBattle`](../Module/AgpmShrineBattle.md), `AgsmAI2`, `AgsmAdmin`, `AgsmCharacter`, `AgsmCombat`, `AgsmDeath` … | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmCastle` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `AgpmDropItem` | Modul (`ApModule`) | 0 | – | 1 von 2 | `AgsmDropItem`, `AgsmEventSpawn` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmDropItem2` | Modul (`ApModule`) | 0 | – | 8 von 23 | [`AgpmEventGacha`](../Module/AgpmEventGacha.md), `AgsmDropItem2`, `AgsmEventGacha`, `AgsmEventNPCTrade`, `AgsmEventSpawn`, `AgsmGamble` … | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmEpicZone` | Modul (`ApModule`) | 0 | – | 1 von 2 | `AgsmAdmin`, `AgsmCharacter`, `AgsmDeath`, `AgsmEpicZone`, `AgsmNpcManager`, `AgsmParty` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmEventBinding` | Modul (`ApModule`) | 1 | – | 7 von 13 | [`AgpmSiegeWar`](../Module/AgpmSiegeWar.md), `AgsmArchlord`, `AgsmCharManager`, `AgsmCharacter`, `AgsmDeath`, `AgsmEventTeleport` … | nicht enthalten (kein RTTI der Klasse; der Name steht nur in einer Tabelle angeforderter Module und wird nie registriert) |
| APublic | `AgpmEventCook` | Modul (`ApModule`) | 0 | – | 2 von 3 | `AgsmEventCook` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmEventFactors` | Modul (`ApModule`) | 0 | – | 3 von 4 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmEventSpawn` | Modul (`ApModule`) | 1 | – | 3 von 6 | `AgpmSiegeWar`, `AgsmAI`, `AgsmAI2`, `AgsmArchlord`, `AgsmBattleGround`, `AgsmEpicZone` … | nicht enthalten (kein RTTI der Klasse; der Name steht nur in einer Tabelle angeforderter Module und wird nie registriert) |
| APublic | `AgpmEventUvUReward` | Modul (`ApModule`) | 0 | – | 4 von 5 | `AgsmEventUvUReward` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmGamble` | Modul (`ApModule`) | 0 | – | 5 von 11 | `AgsmGamble` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmLog` | Modul (`ApModule`) | 0 | – | 4 von 125 | [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md), `AgsmAdmin`, `AgsmAreaChatting`, `AgsmAuctionRelay`, `AgsmBattleGround`, `AgsmCharManager` … | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmMonsterPath` | Modul (`ApModule`) | 0 | – | 0 von 1 | `AgsmAI2` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmPathManager` | Hilfsbibliothek | 0 | – | 3 von 8 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `AgpmRecruit` | Hilfsbibliothek | 0 | – | 0 von 0 | [`AgcmRecruit`](../Module/AgcmRecruit.md), `AgsmRecruit`, `AgsmRecruitClient`, `AgsmRecruitServer` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `AgpmShrine` | Modul (`ApModule`) | 0 | – | 9 von 24 | `AgsmDeath`, `AgsmShrine`, `AgsmSkill` | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `AgpmTransform` | Modul (`ApModule`) | 0 | – | 0 von 0 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `ApBase` | Hilfsbibliothek | 0 | `ApAutoReaderLock`, `ApAutoWriterLock`, `ApBase`, `ApBaseExLock`, `ApLockManager`, `ApRWLock`, `CCSLog`, `CGetArg2`, `DebugValue`, `DebugValueINT32`, `DebugValueString`, `DebugValueUINT32` | 8 von 36 | [`AgcModule`](../Module/AgcModule.md), `AgcSkeleton`, [`AgcUIQuestText`](../Module/AgcUIQuestText.md), [`AgcmAuction`](../Module/AgcmAuction.md), `AgcmCharacter`, [`AgcmConnectManager`](../Module/AgcmConnectManager.md) … | Klassen teilweise vorhanden: ApAutoReaderLock, ApAutoWriterLock, ApBase, ApBaseExLock, ApLockManager, ApRWLock, CCSLog, CGetArg2, DebugValue, DebugValueINT32, DebugValueString, DebugValueUINT32 |
| APublic | `ApIOCPDispatcher` | Hilfsbibliothek | 0 | – | 0 von 1 | `AgsmCharacter`, `AgsmDBPool`, `AgsmDatabasePool` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `ApMemory` | Hilfsbibliothek | 0 | `ApMemoryPool` | 13 von 20 | [`AgcmAmbOcclMap`](../Module/AgcmAmbOcclMap.md), [`AgcmEff2`](../Module/AgcmEff2.md), [`AgcmGrass`](../Module/AgcmGrass.md), `AgcmObject`, [`AgcmQuest`](../Module/AgcmQuest.md), [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md) … | Klassen teilweise vorhanden: ApMemoryPool – Bericht ApMemoryManager. |
| APublic | `ApMemoryTracker` | Hilfsbibliothek | 0 | – | 2 von 7 | `AgcModule`, `AgcmCharacter`, [`AgcmDynamicLightmap`](../Module/AgcmDynamicLightmap.md), `AgcmEff2`, `AgcmEventEffect`, [`AgcmEventGuild`](../Module/AgcmEventGuild.md) … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `ApServerMonitor` | Hilfsbibliothek | 0 | – | 3 von 10 | `AgsmAdmin`, `AgsmServerStatus`, `AuXCrashReport` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `ApSingleton` | Hilfsbibliothek | 0 | – | 0 von 0 | `AgcmEff2`, [`AgpmSystemMessage`](../Module/AgpmSystemMessage.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| APublic | `ApmEventManagerDlg` | Modul (`ApModule`) | 0 | – | 21 von 33 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `ApmFactors` | Modul (`ApModule`) | 0 | `AgpdFactor` | 3 von 9 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| APublic | `ApmProfiler` | Modul (`ApModule`) | 0 | – | 3 von 6 | – | nicht enthalten (kein RTTI der Klasse, kein Modulname) |
| AUtility | `AuBplusTree` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuCrypt` | Hilfsbibliothek | 0 | `AuCryptActor`, `AuCryptCell`, `AuCryptManager` | 0 von 0 | `AgcModule`, `AuPacket` | Klassen teilweise vorhanden: AuCryptActor, AuCryptCell, AuCryptManager – Bericht AuCryptManager. |
| AUtility | `AuCryptAlgorithm` | Hilfsbibliothek | 0 | `AuCryptAlgorithmBase`, `BASE_CTX` | 0 von 0 | – | Klassen teilweise vorhanden: AuCryptAlgorithmBase, BASE_CTX |
| AUtility | `AuDatabase` | Hilfsbibliothek | 0 | – | 4 von 91 | `AgsmAuctionRelay`, `AgsmDBPool`, `AgsmDatabasePool`, `AgsmRelay2`, `ApModule` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuDatabase2` | Hilfsbibliothek | 0 | – | 0 von 3 | `AgsmCharacter`, `AgsmGuild`, `AgsmItem`, `AgsmLoginDB`, `AgsmQuest`, `AgsmSkill` … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuEtcUtil` | Hilfsbibliothek | 0 | – | 0 von 0 | [`AgcmUIMailBox`](../Module/AgcmUIMailBox.md), `AgsmBattleGround`, `AgsmConfig`, `AgsmEpicZone`, `AgsmNpcManager` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuExportedFileDic` | Hilfsbibliothek | 0 | – | 0 von 2 | `AgcmResourceLoader` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuGameEnv` | Hilfsbibliothek | 0 | – | 3 von 3 | [`AgpmConfig`](../Module/AgpmConfig.md), `AgsmAdmin`, `AgsmBilling`, `AgsmBillingJapan`, `AgsmCharManager`, `AgsmCharacter` … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuGameGuard` | Hilfsbibliothek | 0 | `AuNPBase`, `AuNPWrapper` | 2 von 12 | `AgcSkeleton`, `AgcmCharacter`, [`AgpmCharacter`](../Module/AgpmCharacter.md), `AgsmCharacter` | Klassen teilweise vorhanden: AuNPBase, AuNPWrapper – Bericht AuNPWrapper (Schutz nicht gelinkt). |
| AUtility | `AuIgnoringHelper` | Hilfsbibliothek | 0 | – | 3 von 3 | `AgcAuth`, `AgcmUILogin`, [`AgpmAdmin`](../Module/AgpmAdmin.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuIniFile` | Hilfsbibliothek | 0 | – | 0 von 1 | `AgpmCharacter`, [`AgpmFactors`](../Module/AgpmFactors.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuIniManager` | Hilfsbibliothek | 0 | – | 4 von 6 | `AgcmEff2`, [`AgcmEventNature`](../Module/AgcmEventNature.md), [`AgcmUIControl`](../Module/AgcmUIControl.md), `AgpmEventGacha`, `ApModule` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuIniPackingManager` | Hilfsbibliothek | 0 | – | 2 von 2 | `AgcmUIControl`, [`ApmMap`](../Module/ApmMap.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuJapan` | Hilfsbibliothek | 0 | – | 0 von 7 | `AgcmLogin`, `AgcmUILogin`, `AgsmBillingJapan` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuKbHook` | Hilfsbibliothek | 0 | – | 1 von 2 | `AgcSkeleton` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuLocalize` | Hilfsbibliothek | 0 | – | 1 von 19 | [`AgcmMinimap`](../Module/AgcmMinimap.md), [`AgcmUIBuddy`](../Module/AgcmUIBuddy.md), [`AgcmUIEventTeleport`](../Module/AgcmUIEventTeleport.md), [`AgcmUIMain`](../Module/AgcmUIMain.md), [`AgcmUISearch`](../Module/AgcmUISearch.md), [`AgcmUITax`](../Module/AgcmUITax.md) … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuLog` | Hilfsbibliothek | 0 | – | 0 von 1 | `AgcmLogin`, `AgcmUILogin` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuMD5EnCrypt` | Hilfsbibliothek | 0 | – | 2 von 2 | `AgcAuth`, [`AgcmItem`](../Module/AgcmItem.md), `AgcmLogin`, [`AgcmPostFX`](../Module/AgcmPostFX.md), `AgcmResourceLoader`, [`AgcmTextBoard`](../Module/AgcmTextBoard.md) … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuMailClient` | Hilfsbibliothek | 0 | – | 2 von 60 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuMappedPool` | Hilfsbibliothek | 0 | – | 0 von 0 | [`AgcmUIGuideMessage`](../Module/AgcmUIGuideMessage.md) | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuMath` | Hilfsbibliothek | 0 | – | 0 von 0 | `AgcmCharacter`, `AgcmEventEffect`, `AgcmUIControl`, `AgpmCharacter`, `AgpmFactors`, `AgsmAI` … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuParallel` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuPatchCheckCode` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuProcessManager` | Hilfsbibliothek | 0 | – | 1 von 1 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuProfileManager` | Hilfsbibliothek | 0 | – | 0 von 0 | `AgcModule`, `AgcSkeleton`, `ApModule`, `AuPacket` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuRandomNumberGenerator` | Hilfsbibliothek | 0 | – | 0 von 0 | `AgcmCharacter`, `AgcmEventEffect`, `AgcmItem`, [`AgcmStartupEncryption`](../Module/AgcmStartupEncryption.md), [`AgcmUIChatting2`](../Module/AgcmUIChatting2.md), [`AgcmUIHelp`](../Module/AgcmUIHelp.md) … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuRegistry` | Hilfsbibliothek | 0 | – | 1 von 1 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuResourceKeeper` | Hilfsbibliothek | 0 | – | 6 von 30 | `AgcModule`, `AgcSkeleton`, `AgsmPacketMonitor`, `AuExcelLib` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuSendDebugInfo` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuService` | Hilfsbibliothek | 0 | – | 0 von 38 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuSnappy` | Hilfsbibliothek | 0 | – | 0 von 7 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuStaticPool` | Hilfsbibliothek | 0 | – | 0 von 0 | [`AgcmRender`](../Module/AgcmRender.md), `AgcmResourceLoader` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuStrTable` | Hilfsbibliothek | 0 | – | 1 von 2 | [`AgcmBattleGround`](../Module/AgcmBattleGround.md), [`AgcmGuild`](../Module/AgcmGuild.md), `AgcmMinimap`, [`AgcmProductMed`](../Module/AgcmProductMed.md), `AgcmRecruit`, [`AgcmShrine`](../Module/AgcmShrine.md) … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuStringConv` | Hilfsbibliothek | 0 | – | 0 von 0 | `AgcmUIChatting2`, `AgcmUIControl`, [`AgcmUIManager2`](../Module/AgcmUIManager2.md), `AgsmChatting`, `AgsmLoginClient` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuThread` | Hilfsbibliothek | 0 | – | 0 von 0 | – | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuTimeStamp` | Hilfsbibliothek | 0 | – | 1 von 2 | [`AgcmSiegeWar`](../Module/AgcmSiegeWar.md), [`AgcmUICashInven`](../Module/AgcmUICashInven.md), [`AgcmUICashItemCabient`](../Module/AgcmUICashItemCabient.md), `AgcmUIMain`, [`AgcmUISiegeWar`](../Module/AgcmUISiegeWar.md), `AgcmUITax` … | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |
| AUtility | `AuZpackLoader` | Hilfsbibliothek | 0 | – | 0 von 0 | `AgcmEff2`, `AgcmResourceLoader`, `AgcmUILogin`, [`AgpmItem`](../Module/AgpmItem.md), `AuExcelTxtLib` | Verbleib offen (Funktionen ohne eigene Klasse; nicht beweisbar) |

Zahlen: nicht enthalten: 24, nicht enthalten (Name nur als Verweis): 2, offen: 46, teilweise: 8
