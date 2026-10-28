# Große unbenannte Funktionen im Spiel- und Engine-Bereich

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Alle Funktionen von mindestens 300 Byte zwischen `0x00401000` und `0x007A0000`, die in `names_all310.tsv` keinen Klassennamen tragen (1237 Stück). Gruppiert nach der Klasse der nächsten benannten Funktion davor und danach; steht auf beiden Seiten dieselbe Klasse, gehört die Funktion mit hoher Wahrscheinlichkeit dazu (Quelle: Adressreihenfolge = Quellreihenfolge). **Das sind Kandidaten für weitere Arbeit, keine Zuordnungen.** Viele sind Vorlagen-Instanzen der STL, Aufräumfunktionen oder Code, der in der EP8-Quelle nicht vorkommt (2017er Zusatz).

| Nachbarklasse | Anzahl | größte Funktionen (Adresse, Byte, erste Zeichenkette) |
|---|---:|---|
| `CSmtpMessage / AuLua` | 321 | `0x004AD16B` 7656; `0x004D5960` 7095; `0x004A57CE` 4604; `0x004A71BE` 4536 |
| `AuHistoryDlg / CSmtpMessage` | 286 | `0x0043D200` 7714 „);
  }
  else if (DAT_0097db38“; `0x0047AF4A` 6223; `0x0046239B` 5701; `0x004756AF` 5621 |
| `~basic_string<char,std / CTestPostEffectFX` | 29 | `0x004041B0` 766; `0x00406090` 765; `0x00403910` 716; `0x00403D80` 716 |
| [`AgcmRender`](../Module/AgcmRender.md) | 22 | `0x005B6070` 1797; `0x005B0880` 1773; `0x005B8FB0` 1421; `0x005B14F0` 861 |
| `AgcmCharacter` | 14 | `0x005A8DD0` 1287 „AgcmCharacter“; `0x0059C470` 1270; `0x0059D7B0` 589 „AGCD_CHARACTER“; `0x0059C970` 501 „AGCD_CHARACTER“ |
| [`AgcUIChatMessage`](../Module/AgcUIChatMessage.md) | 14 | `0x00736230` 1425; `0x00738D10` 1382; `0x00736E50` 991; `0x00738880` 874 |
| `CNpcText / AgcdEffTexInfo` | 14 | `0x0075C3E0` 3940; `0x0075A9A0` 2072 „tweakable“; `0x0075D79D` 1764; `0x0075BDD0` 1255 |
| [`AgpmItemConvert`](../Module/AgpmItemConvert.md) | 12 | `0x0052B0E0` 1059; `0x0052A480` 953 „Spirit1“; `0x005838B0` 569; `0x00594720` 535 |
| `AgpmEventSkillMaster / AgpmSkill` | 11 | `0x0052D590` 1353; `0x0052DAF0` 1152; `0x0052CB30` 914 „Archlord“; `0x0052DF80` 380 |
| `AcUIEdit` | 11 | `0x006FEE20` 1011; `0x006FE740` 920; `0x006FF920` 601; `0x006FD7FD` 530 „%d. %s “ |
| [`AgcmUIManager2`](../Module/AgcmUIManager2.md) | 9 | `0x005E5F50` 1305; `0x005E7890` 1233; `0x005E8DF0` 1047; `0x0062FAB0` 736 „%d:%d:%d:%d:%s“ |
| [`AgcmItem`](../Module/AgcmItem.md) | 9 | `0x006EBDB6` 810 „%s%.*x“; `0x0073AF00` 763 „AgcmUICharacter“; `0x006ED350` 353; `0x006ED180` 333 |
| `AgcuEffIniMng` | 9 | `0x00799690` 694 „%s:%d“; `0x007990F0` 505 „%f:%f:%f“; `0x007992F0` 481 „%f:%f:%f“; `0x00798D60` 465 „%s:%d“ |
| [`AgpmItem`](../Module/AgpmItem.md) | 8 | `0x00544C10` 1819 „AgpmItem“; `0x0053A530` 690; `0x005449A0` 611; `0x0053F550` 377 |
| `AgcEngine` | 8 | `0x00598980` 1243; `0x0059B230` 1011; `0x00598E60` 981; `0x00598210` 643 |
| [`AgcmUIItem`](../Module/AgcmUIItem.md) | 8 | `0x006D83F0` 2668 „AgcmUIItem“; `0x00629870` 1065 „ %s“; `0x00629F20` 853 „%s :“; `0x00740E30` 617 „AutoPickUp“ |
| `MyEngine / AgcEngine` | 7 | `0x00417180` 777 „%f,%f“; `0x00416130` 633 „Portuguese“; `0x00416B50` 581; `0x00416520` 449 |
| `Element / AuAngelScriptEngine` | 7 | `0x004E8EA0` 697; `0x004E95B0` 504; `0x004E8690` 433; `0x004E91F0` 423 |
| `ApmMap / AgpmTimer` | 7 | `0x00518AF0` 1917; `0x005194D0` 844 „rb“; `0x0051A0F0` 740 „rb“; `0x0051BBE8` 640 |
| [`AgpmSkill`](../Module/AgpmSkill.md) | 7 | `0x00530930` 775; `0x00565FD0` 712 „AgpmSkill“; `0x00562C80` 408; `0x00564490` 383 |
| `AgcmEventEffectData` | 7 | `0x00716B90` 1525; `0x00717720` 707; `0x00717570` 421; `0x007163F0` 415 |
| `AgcdEffCtrl_Base` | 7 | `0x0071B7D0` 1368; `0x0071B340` 1148; `0x0071AF70` 954; `0x00718B90` 856 |
| `AgcuEffBaseCtrlCreater / AcUIToolTip` | 7 | `0x00721BC0` 997; `0x00722EB0` 623; `0x00723760` 581; `0x007232E0` 549 |
| [`AgpmCharacter`](../Module/AgpmCharacter.md) | 6 | `0x00506FD0` 594; `0x0050DEA0` 561; `0x00504D00` 545; `0x00504F30` 397 |
| `AgcmRegistryManager / AgcmTitle` | 6 | `0x006548E0` 1194; `0x00654490` 1084; `0x00655210` 1023; `0x00654DA0` 877 |
| [`AgcmUIGuideMessage`](../Module/AgcmUIGuideMessage.md) | 6 | `0x00678910` 581; `0x00679610` 581; `0x00679DF0` 581; `0x006784D0` 338 |
| [`AgcmCamera2`](../Module/AgcmCamera2.md) | 6 | `0x006F2910` 711; `0x006F3B50` 711 „AgcmCamera2“; `0x006F0F00` 637; `0x006F3ED0` 478 |
| `AgcmUISkillDragonScion` | 6 | `0x00784F00` 863; `0x00785700` 641; `0x00785990` 641; `0x00785C20` 641 |
| `CScreenModeManager / ApMemoryPool` | 5 | `0x0040C1E0` 5718; `0x0040EC40` 4506 „Debug“; `0x0040DB10` 4279 „);
    if (pFVar2 != (FILE *)0“; `0x0040BF70` 623 |
| `AgpmRefinery / AgpmItemConvert` | 5 | `0x00529460` 913; `0x00529C40` 880; `0x00529800` 637; `0x00529FC0` 543 |
| `AgpmSkill / AgpmQuest` | 5 | `0x00533C20` 12478 „target“; `0x00537310` 1355 „FACTOR_PERCENT“; `0x005334C0` 948 „FACTOR_PERCENT“; `0x00533880` 633 „FACTOR_PERCENT“ |
| `CMagUnpackManager / AgpmItem` | 5 | `0x0058BAF0` 456; `0x0058AFE0` 441; `0x0058C1C0` 430; `0x0058BF30` 372 |
| `AgcmEventEffect / AgcmEventNature` | 5 | `0x005CF8E0` 568; `0x005CFB30` 441; `0x005CF6B0` 358; `0x005CFE40` 334 |
| `CUiCharacterProperty` | 5 | `0x005FF260` 518 „AgpmItem“; `0x005FF0C0` 406 „AgpmSkill“; `0x005FFD60` 338; `0x005FFEC0` 338 |
| [`AgcmShrine`](../Module/AgcmShrine.md) | 5 | `0x00687B70` 936; `0x006872E0` 581; `0x006892F0` 549; `0x00687F20` 453 |
| [`AgcmUIQuest2`](../Module/AgcmUIQuest2.md) | 5 | `0x006B65F0` 632 „AgcmUIQuest2“; `0x006B4090` 610; `0x006B61C0` 581; `0x006B3990` 395 |
| `AgcdEffCtrl_TerrainBoard / AgcdEffCtrl_Light` | 5 | `0x0071CD90` 879; `0x0071D270` 689; `0x0071D6C0` 466; `0x0071CC40` 335 |
| `AcUIJournal / AcUIGacha` | 5 | `0x00768B00` 1536; `0x00768550` 581; `0x00768160` 360; `0x007683F0` 338 |
| `AgcmHeroicSkill` | 5 | `0x00781DC0` 1332; `0x007824D0` 750; `0x007878E0` 696; `0x00787620` 683 |
| `AgcaItemClump / AgcmItem` | 5 | `0x00792C50` 3366; `0x00793980` 2838; `0x00791930` 338; `0x007920E0` 338 |
| `AuIniManagerA` | 4 | `0x004F0570` 601; `0x004EFED0` 419; `0x004F2930` 396 „.zp“; `0x004F0180` 309 „rb“ |
| `AuSeed / AuRijnDael` | 4 | `0x004FE7C0` 3066; `0x004FF3C0` 2594; `0x004FE2D0` 706; `0x004FE5A0` 530 |
| [`AgpmGuild`](../Module/AgpmGuild.md) | 4 | `0x00552C60` 1059 „AgpmGuild“; `0x0054E120` 336; `0x00552AB0` 313; `0x00550870` 301 |
| [`AgpmPvP`](../Module/AgpmPvP.md) | 4 | `0x0057F630` 514 „AgpmPvP“; `0x00581B50` 315; `0x00581CB0` 313; `0x0057EC20` 308 |
| [`AgcmSkill`](../Module/AgcmSkill.md) | 4 | `0x0066E2A0` 4239; `0x0066F330` 1802; `0x0066FBF0` 557 „vector“; `0x0066C600` 360 „AgcmSkill“ |
| `AgcmUIWorldmap` | 4 | `0x0067EF60` 581 „World“; `0x0067F1B0` 506 „AgcmUIWorldmap“; `0x0067C0E0` 365; `0x0067EC30` 332 |
| [`AgcmUIGuild`](../Module/AgcmUIGuild.md) | 4 | `0x006BA8A0` 2830 „AgcmUIGuild“; `0x007798F0` 327; `0x0077A570` 324; `0x006BB3C0` 320 |
| [`AgcmUISkill2`](../Module/AgcmUISkill2.md) | 4 | `0x006CA5E0` 785 „AgcmUISkill2“; `0x007767E0` 587; `0x00776C10` 569 „%s : %d“; `0x00776A30` 474 „%s : %d“ |
| [`AgcmWorld`](../Module/AgcmWorld.md) | 4 | `0x006DA820` 477; `0x006DBEE0` 466; `0x006DBA70` 340; `0x006DB640` 321 |
| [`AgcChatManager`](../Module/AgcChatManager.md) | 4 | `0x0070D8E0` 1438 „%f“; `0x0070F210` 477; `0x0070F550` 333; `0x0070F400` 302 |
| `AgcdEffCtrl_Camera / AgcdEffCtrl_ParticleSysTem` | 4 | `0x0071ED30` 845; `0x0071F0A0` 712; `0x0071F3E0` 416; `0x0071E1F0` 398 |
| `AgcmUICharacterCreate` | 4 | `0x007451D7` 927; `0x00745DD0` 338; `0x00747730` 338; `0x00747FB0` 338 |
| `AgcmUILoginSetting` | 4 | `0x0074AFF0` 623; `0x0074AAE0` 565 „Race=%s“; `0x0074A180` 425 „Pos : X=%f, Y=%f, Z=%f“; `0x0074A330` 425 „Pos : X=%f, Y=%f, Z=%f“ |
| `AcUIMenu` | 4 | `0x0079AE20` 825; `0x0079B160` 538; `0x0079B380` 412; `0x0079C860` 308 |
| `- / ~basic_string<char,std` | 3 | `0x004013B0` 881 „
                 );
        M“; `0x004017A0` 347; `0x004011B0` 310 |
| `AgcModule / AuSeed` | 3 | `0x004FAD30` 4280; `0x004FC370` 4280; `0x004FA1C3` 2849 |
| `AuSeed` | 3 | `0x004FDD90` 1535; `0x004FDBB0` 1354; `0x004FDFE0` 520 |
| `AgpmCharacter / TiXmlDocument` | 3 | `0x0050FDE0` 1223; `0x0050FA60` 568; `0x0050FCA0` 307 |
| [`ApmMap`](../Module/ApmMap.md) | 3 | `0x005158F0` 338; `0x00515470` 334; `0x005155E0` 323 |
| [`AgpmTax`](../Module/AgpmTax.md) | 3 | `0x00578420` 417; `0x00578830` 396 „AgpmTax“; `0x00577C90` 317 |
| `ApMemory` | 3 | `0x005B24B0` 859; `0x005B2850` 542; `0x00591D50` 325 |
| `AgcModalWindow / CUiCharacterProperty` | 3 | `0x005FE6E0` 1712 „effect.zp“; `0x005FE260` 508; `0x005FDFD0` 361 |
| `AgcmLODManager / AgcmCharacter` | 3 | `0x00618C60` 312; `0x00618DA0` 312; `0x00618EE0` 312 |
| `TiXmlNode / AgcmShadow2` | 3 | `0x00651450` 1392; `0x00651C40` 652; `0x006519C0` 634 |
| [`AgcmTitle`](../Module/AgcmTitle.md) | 3 | `0x006582E0` 385 „);
    if (((iVar3 != 0) && (i“; `0x00657880` 338; `0x0065B8C0` 338 |
| [`AgcmObject`](../Module/AgcmObject.md) | 3 | `0x00675270` 652 „AgcmObject“; `0x00675B50` 495; `0x00673C00` 308 |
| `CChatCmd / AgcmEventEffectData` | 3 | `0x007147E0` 454 „SOIL“; `0x00713E90` 338; `0x007136A0` 331 |
| `AcUIBase` | 3 | `0x00727B90` 801; `0x007274B0` 464; `0x00727680` 331 |
| `AuInputComposer / AcTextureList` | 3 | `0x00733930` 846; `0x007336C0` 616; `0x00733C80` 334 |
| `AgcmUIServerSelect` | 3 | `0x00743460` 338; `0x00744080` 338; `0x00743980` 310 |
| `AgcuPathDoubleSpline / AgcuEffIniMng` | 3 | `0x007980B0` 420; `0x00797F20` 396 „TRANSFORM_DATA“; `0x00797CD0` 321 „%f:%f:%f:%f:%f:%f:%f:%f:%f:%f:“ |
| `CTestPostEffectFX / MainWindow` | 2 | `0x0040A2E0` 773; `0x0040ADF0` 383 |
| `MainWindow / CLogoViewer` | 2 | `0x0040B1B0` 1487 „FPS: %03d“; `0x0040B060` 329 „Archlord“ |
| `ApAdmin` | 2 | `0x004EB4F0` 405; `0x004EAFD0` 383 |
| `AuExcelTxtLib` | 2 | `0x004ECE80` 484 „wb“; `0x004ED1E0` 450 |
| `DebugValueString / AuIniManagerA` | 2 | `0x004F1210` 323; `0x004F13D0` 320 |
| `StackWalker` | 2 | `0x004F5480` 550 „;
    iVar4 = FUN_004f4eb0(par“; `0x004F5BEC` 441 „GetModuleFileNameExA“ |
| `AuMD5Mac / AuBlowFish` | 2 | `0x00500770` 949; `0x005003B0` 947 |
| [`AgpmEventNature`](../Module/AgpmEventNature.md) | 2 | `0x0051EAC0` 371 „Default“; `0x0051EC40` 356 |
| [`AgpmSiegeWar`](../Module/AgpmSiegeWar.md) | 2 | `0x005222E0` 1077 „Castle“; `0x0051FDF0` 806 |
| `AgpmSiegeWar / AgpmEventCharCustomize` | 2 | `0x00524170` 779 „AgpmSiegeWar“; `0x00523EA0` 709 |
| `AgpmCharacter / AgpmItem` | 2 | `0x0054A340` 338; `0x0054A590` 312 |
| `AgpmGuild / AgpmAdmin` | 2 | `0x00554E70` 667; `0x00555110` 371 |
| [`AgpmAdmin`](../Module/AgpmAdmin.md) | 2 | `0x00555D20` 1130; `0x00556190` 447 |
| [`AgpmCashMall`](../Module/AgpmCashMall.md) | 2 | `0x00556E20` 751; `0x005573C0` 326 „AgpmCashMall“ |
| [`AgpmMailBox`](../Module/AgpmMailBox.md) | 2 | `0x005579C0` 344 „AgpmMailBox“; `0x005580E0` 302 |
| [`ApmEventManager`](../Module/ApmEventManager.md) | 2 | `0x0055CFE0` 676; `0x0055C840` 587 |
| [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md) | 2 | `0x00573F10` 511 „,0x27);
  param_1[0x2e1] = 0;
“; `0x00573DB0` 341 |
| [`AgpmSummons`](../Module/AgpmSummons.md) | 2 | `0x00585150` 473; `0x005853E0` 334 |
| `AgpaTitleTemplate / AgpmItemConvert` | 2 | `0x00592960` 336; `0x00592720` 323 |
| `AgcmPostFX / AgcmUIConsole_static` | 2 | `0x005C1C70` 428; `0x005C1A20` 410 |
| [`AgcmEventEffect`](../Module/AgcmEventEffect.md) | 2 | `0x005C70A0` 374; `0x005CB7D0` 346 |
| [`AgcmEventNature`](../Module/AgcmEventNature.md) | 2 | `0x005D4640` 1210; `0x005D0DC0` 323 |
| `AgcmFont / AgcmMap` | 2 | `0x005F0BE0` 4765; `0x005F1E80` 1225 |
| `AgcmCharacter / AgcmUIHelp` | 2 | `0x0061C3B0` 1295 „TYPE“; `0x0061C250` 338 |
| [`AgcmUICharacter`](../Module/AgcmUICharacter.md) | 2 | `0x006214F0` 968 „AgcmUICharacter“; `0x0061ECA0` 534 „%s“ |
| [`AgcmUIControl`](../Module/AgcmUIControl.md) | 2 | `0x0062DFA0` 476; `0x0062E180` 387 |
| [`AgcmNatureEffect`](../Module/AgcmNatureEffect.md) | 2 | `0x0063A360` 313; `0x0063A4C0` 305 „AgcmNatureEffect“ |
| `ApMemory / AgcmGrass` | 2 | `0x00649DB0` 1766; `0x0064A4A0` 652 |
| [`AgcmGrass`](../Module/AgcmGrass.md) | 2 | `0x0064C1F0` 427 „AgcmGrass“; `0x0064BBE0` 313 |
| `AgcSkeleton / AgcAuth` | 2 | `0x0064D870` 604; `0x0064E940` 315 „Failed to read material effect“ |
| `AgcmSkill / AgcmObject` | 2 | `0x006708F0` 601; `0x00670730` 431 |
| [`AgcmUISearch`](../Module/AgcmUISearch.md) | 2 | `0x006934B0` 330; `0x006936D0` 301 „AgcmUISearch“ |
| [`AgcmMinimap`](../Module/AgcmMinimap.md) | 2 | `0x006E3350` 504; `0x006E31F0` 319 |
| [`AgcmGlyph`](../Module/AgcmGlyph.md) | 2 | `0x006E3E50` 853; `0x006E64A0` 446 „AgcmGlyph“ |
| `AgcmShadowmap / AgcmDynamicLightmap` | 2 | `0x006F92F0` 4441; `0x006F8200` 4315 |
| `AgcmItem / AcClientSocket` | 2 | `0x00706470` 380; `0x00705D90` 300 |
| `AgcdEffCtrl_Tail / AgcdEffCtrl_Obj` | 2 | `0x00721010` 1057; `0x00720C80` 681 |
| `AgcUIEffect / AcUISkillTree` | 2 | `0x00731CB0` 375; `0x00731E30` 344 |
| `AuInputComposer` | 2 | `0x00732AE0` 414; `0x007333D0` 351 |
| `AgcmUIItem / AgcmUILoginSelect` | 2 | `0x00741CB0` 644; `0x00742250` 322 |
| `AgcuUILoadingWindow / AgcmUILoginSetting` | 2 | `0x00749BD0` 698 „.zp“; `0x00749600` 338 |
| `AgcdEffTex / AgcdEffCtrlMng` | 2 | `0x0075EB20` 346; `0x0075ED20` 342 |
| `AGCDEFFSET_CBARG / AgcdEffSet` | 2 | `0x00763380` 325; `0x00763140` 315 |
| `AgcuPathWork` | 2 | `0x00796EE0` 686; `0x00796D60` 380 |
| `AgcuPathDoubleSpline` | 2 | `0x00797850` 873; `0x00797650` 498 |
| `MyEngine / AgcmCharacter` | 1 | `0x00410900` 404 „);
    if (BVar4 == 0) {
     “ |
| `AgcEngine / MyEngine` | 1 | `0x004175D0` 450 „archlord_de.dat“ |
| `MyEngine / AuHistoryDlg` | 1 | `0x004178F0` 553 |
| `ApModuleManager / ApMemoryPool` | 1 | `0x004E3C30` 639 |
| `ApMemoryManager / CGetArg2` | 1 | `0x004E7670` 551 „%s-%04d%02d%02d.txt“ |
| `AuPackingManager` | 1 | `0x004EED50` 429 „%s“ |
| `AuCircularBuffer / AuIniManagerA` | 1 | `0x004EF8E0` 672 |
| `CMiniVersion / AuScriptEngine` | 1 | `0x004F6CB0` 733 „%u.%u.%u“ |
| `AuScriptEngine / AuMiniLZO` | 1 | `0x004F8450` 1573 „;
  (**(code **)(*param_1 + 8)“ |
| `AuMD5Encrypt / ApRWLock` | 1 | `0x004F9840` 851 „10.95.“ |
| `ApAutoReaderLock / AgpmCharacter` | 1 | `0x00501C60` 1993 |
| `AgpmCharacter / AgpmFactors` | 1 | `0x0050A150` 798 „AgpmCharacter“ |
| [`AgpmEventCharCustomize`](../Module/AgpmEventCharCustomize.md) | 1 | `0x00524C30` 675 „Type“ |
| `InstanceMemoryBlock / AuExcelBinaryLib` | 1 | `0x005267E0` 555 |
| [`AgpmRefinery`](../Module/AgpmRefinery.md) | 1 | `0x00528C70` 570 |
| `AgpmMailBox / AgpmQuest` | 1 | `0x00558960` 405 „AgpmQuest“ |
| `AgpmQuest / AgpmEventTeleport` | 1 | `0x00559810` 312 |
| [`AgpmEventTeleport`](../Module/AgpmEventTeleport.md) | 1 | `0x0055A9C0` 304 |
| `ApmEventManager / AgpmAuction` | 1 | `0x0055D9A0` 836 |
| [`AgpmProduct`](../Module/AgpmProduct.md) | 1 | `0x0055F9B0` 418 „AgpmProduct“ |
| `AgpmSkill / AgpmParty` | 1 | `0x005665D0` 435 „AgpmParty“ |
| [`AgpmTitle`](../Module/AgpmTitle.md) | 1 | `0x00568D30` 437 |
| [`AgpmEventGacha`](../Module/AgpmEventGacha.md) | 1 | `0x0056A070` 300 |
| [`AgpmBuddy`](../Module/AgpmBuddy.md) | 1 | `0x0056CF80` 334 |
| [`AgpmWorld`](../Module/AgpmWorld.md) | 1 | `0x0056DD70` 367 |
| `AgpmEventNPCTrade / AgpmEventNPCDialog` | 1 | `0x00576170` 316 |
| [`AgpmGuildWarehouse`](../Module/AgpmGuildWarehouse.md) | 1 | `0x00576F50` 343 |
| `AgpmSystemMessage / AgpmOptimizedPacket2` | 1 | `0x0057C540` 776 „AgpmOptimizedPacket2“ |
| [`AgpmScript`](../Module/AgpmScript.md) | 1 | `0x00588160` 316 „AgpmScript“ |
| `AgpmConfig / AgpaCharacter` | 1 | `0x00589C50` 401 |
| `AgpmCharacter / CMagUnpackManager` | 1 | `0x0058A990` 362 „%s%s“ |
| `CMagUnpackManager` | 1 | `0x0058AD70` 584 „MagPack Ver 0.1a“ |
| `AgpaItem / AgpmItem` | 1 | `0x0058D880` 338 |
| `AgpaQuestGroup / AgpdQuestFlag` | 1 | `0x00590840` 326 |
| `AgpdQuestFlag / ApMemory` | 1 | `0x00591140` 397 |
| `AgpmItemConvert / AgpmItem` | 1 | `0x00596670` 503 |
| `AgcmCharacter / DebugValueUINT32` | 1 | `0x005A6C50` 456 |
| `AgcmRender / ApMemory` | 1 | `0x005B20B0` 378 „AgpmCharacter“ |
| `AgcmRender / CUsableRwFrameTable` | 1 | `0x005B5290` 394 |
| `CUsableRwFrameTable / AgcmRender` | 1 | `0x005B5640` 320 |
| `CCSLog / AgcmRender` | 1 | `0x005B75D0` 314 |
| [`AgcmPostFX`](../Module/AgcmPostFX.md) | 1 | `0x005C0720` 468 „AgcmPostFX“ |
| `AgcmUIGuildBattleResult` | 1 | `0x005D8200` 497 |
| `AgcmUIGuildBattleResult / AgcmUIOption` | 1 | `0x005D9370` 324 |
| `AgcmUIManager2 / AgcmFont` | 1 | `0x005EA810` 772 |
| [`AgcmSound`](../Module/AgcmSound.md) | 1 | `0x005F7EA0` 338 |
| `AgcWindow` | 1 | `0x005FCDF0` 351 |
| `AgcWindow / AgcModalWindow` | 1 | `0x005FD850` 976 |
| [`AgcmUIMain`](../Module/AgcmUIMain.md) | 1 | `0x006067B0` 1299 |
| `AgcuUIControlCharacter / AgcmUILogin` | 1 | `0x0060F520` 490 „,0x27);
  FUN_004e45d0(1);
  p“ |
| [`AgcmUIAuction`](../Module/AgcmUIAuction.md) | 1 | `0x006172A0` 803 |
| `AgcmUIHelp / AgcmUITips` | 1 | `0x0061D630` 303 „AgcmUITips“ |
| [`AgcmTargeting`](../Module/AgcmTargeting.md) | 1 | `0x00635EF0` 664 |
| `CNpcTextManager / AgcmLensFlare` | 1 | `0x006412C0` 905 |
| [`AgcmLensFlare`](../Module/AgcmLensFlare.md) | 1 | `0x006416A0` 371 |
| [`AgcSkeleton`](../Module/AgcSkeleton.md) | 1 | `0x0064F9A0` 371 |
| `AgcmTitle / AgcmLogin` | 1 | `0x0065CA70` 429 |
| [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md) | 1 | `0x00663A40` 320 |
| [`AgcmGuild`](../Module/AgcmGuild.md) | 1 | `0x00669190` 570 |
| `AgcmUIQuestJournal` | 1 | `0x0067B3E0` 398 |
| [`AgcmWarInfo`](../Module/AgcmWarInfo.md) | 1 | `0x0068ABD0` 581 |
| [`AgcmUISiegeWar`](../Module/AgcmUISiegeWar.md) | 1 | `0x006908D0` 761 „AgcmUISiegeWar“ |
| [`AgcmUIMailBox`](../Module/AgcmUIMailBox.md) | 1 | `0x0069B500` 422 „AgcmUIMailBox“ |
| [`AgcmUIProduct`](../Module/AgcmUIProduct.md) | 1 | `0x006A2C70` 485 „AgcmUIProduct“ |
| [`AgcmUIProductSkill`](../Module/AgcmUIProductSkill.md) | 1 | `0x006A5260` 465 „AgcmUIProductSkill“ |
| [`AgcmUIChannel`](../Module/AgcmUIChannel.md) | 1 | `0x006AA1D0` 554 |
| [`AgcmUIBuddy`](../Module/AgcmUIBuddy.md) | 1 | `0x006AD550` 536 „AgcmUIBuddy“ |
| [`AgcmUIEventNPCDialog`](../Module/AgcmUIEventNPCDialog.md) | 1 | `0x006BE250` 307 |
| `AgcmUIEventBank / AgcmUIPartyOption` | 1 | `0x006BF600` 407 |
| [`AgcmUIPartyOption`](../Module/AgcmUIPartyOption.md) | 1 | `0x006BFAE0` 406 |
| [`AgcmUIParty`](../Module/AgcmUIParty.md) | 1 | `0x006C1DB0` 484 „AgcmUIParty“ |
| `AgcmUVAnimation / AgcmEventNPCTrade` | 1 | `0x006DCAB0` 312 |
| `AgcmParty / AgcmPrivateTrade` | 1 | `0x006E8DA0` 339 „AgcmPrivateTrade“ |
| `AgcmItemConvert / AgcmItem` | 1 | `0x006EAEC0` 410 „AgcmItem“ |
| `AgcmUICooldown / AgcmCamera2` | 1 | `0x006F0620` 462 |
| `AgcmOcTree / AcSocketManager` | 1 | `0x006FCF00` 348 |
| `AcSocketManager / AcUIEdit` | 1 | `0x006FD4D0` 339 |
| `AgcmUIItem / AcuObjecWire` | 1 | `0x00708360` 1216 |
| `AcuObjecWire / AgcmRenderType` | 1 | `0x00708BB0` 722 |
| `AgcdClumpRenderTypeData / AgcmLODList` | 1 | `0x007092F0` 410 |
| `COptionFlagController` | 1 | `0x0070C0A0` 338 |
| `CChatCmd` | 1 | `0x00710E10` 338 |
| `AgcmEventEffectData / AgcaEffectData2` | 1 | `0x00717B93` 450 „LEFT“ |
| `AgcdEffCtrl_Base / AgcdEffCtrl_Board` | 1 | `0x0071C430` 1148 |
| `AgcdEffCtrl_Board / AgcdEffCtrl_TerrainBoard` | 1 | `0x0071CA20` 303 |
| `AgcdEffCtrl_MFrm / AgcdEffCtrl_Sound` | 1 | `0x0071D9D0` 324 |
| `AgcdEffCtrl_ParticleSyst_SBH / AgcdEffCtrl_ParticleSysTem` | 1 | `0x007201A0` 523 |
| `AgcdEffCtrl_Obj / AgcdEffCtrl_Set` | 1 | `0x00721450` 328 |
| `AcUICombo` | 1 | `0x00724E20` 633 |
| `AcUIScroll / AcUIBase` | 1 | `0x007264F0` 712 |
| `AcUIList` | 1 | `0x00729DB0` 324 |
| `AcUIClock / AcUIGrid` | 1 | `0x0072AE20` 316 |
| `AcUIGrid` | 1 | `0x0072B437` 373 |
| `AcuTextureList` | 1 | `0x0072E010` 315 |
| `AcUIBar` | 1 | `0x0072FE20` 431 |
| `AgcUIChatMessage / AgcmItem` | 1 | `0x0073A8E0` 305 „(%d)“ |
| `CExNPCDialog` | 1 | `0x0073F9F0` 338 |
| `AgcmUIServerSelect / AgcmUICharacterCreate` | 1 | `0x00744FC0` 369 |
| `AgcmUICharacterCreate / AgcmUIAccountCheck` | 1 | `0x00748459` 445 „AgcmUICharacter“ |
| `AgcuUILoadingWindow` | 1 | `0x007490F0` 740 „LG_Slide“ |
| `AgcdPreEffSet / AgcdEffCtrlMng` | 1 | `0x0075F2A0` 338 |
| `AgcdEffSetMng` | 1 | `0x0075FF30` 338 |
| `AgcdEffSetMng / AgcuEffVBMng` | 1 | `0x00760AD0` 323 |
| `AgcuEffVBMng` | 1 | `0x00761B10` 323 |
| `AgcuEffVBMng / AgcdEffSet` | 1 | `0x007624C0` 600 |
| `AgcdEffSet` | 1 | `0x00763770` 730 |
| [`AgcUIQuestText`](../Module/AgcUIQuestText.md) | 1 | `0x00765200` 581 |
| `AgcDebugWindow / AcuBlur` | 1 | `0x0076BE90` 358 |
| `AgcmUISkillDragonScion / AgcmHeroicSkill` | 1 | `0x00787090` 683 |
| `AgcuCamMode` | 1 | `0x0078EC90` 313 |
| `AgcuCamMode / AcUIRecruit` | 1 | `0x0078F6F0` 388 |
| `AcUIBbs` | 1 | `0x00790890` 393 |
| `AcUIBbs / AgcaItemClump` | 1 | `0x007913F0` 615 |
| `AgcdCamConstrain_Terrain / AgcdCamConstrain_Obj` | 1 | `0x00796220` 774 |
| `AgcdCamConstrain_Obj / AgcWindow` | 1 | `0x007967C0` 597 |
| `CSystemMsgManager` | 1 | `0x0079F820` 338 |

Erzeugt mit `mkunnamed.py`.
