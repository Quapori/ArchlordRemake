# AlefClient.exe (2017) – Member-Offsets der Modulzeiger

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Quelle: `GetModule("Name")`-Zuweisungen in `OnAddModule` (Binary) gejoint mit den EP8-Quellen über den Modulnamen. Offsets sind relativ zu `this` (x86, dezimal/hex).

## AgcmAdmin
| Offset | Member | Typ |
|---:|---|---|
| `0xB9C` | `m_pagpmAdmin` | [`AgpmAdmin`](../Module/AgpmAdmin.md) |
| `0xBA0` | `m_pagcmCharacter` | `AgcmCharacter` |

## AgcmArchlord
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmArchlord` | [`AgpmArchlord`](../Module/AgpmArchlord.md) |
| `0xB9C` | `m_pcsAgpmCharacter` | [`AgpmCharacter`](../Module/AgpmCharacter.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmEventManager` | [`AgcmEventManager`](../Module/AgcmEventManager.md) |

## AgcmAuction
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pApmMap` | [`ApmMap`](../Module/ApmMap.md) |
| `0xB9C` | `m_pApmEventManager` | [`ApmEventManager`](../Module/ApmEventManager.md) |
| `0xBA0` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pAgpmFactors` | [`AgpmFactors`](../Module/AgpmFactors.md) |
| `0xBA8` | `m_pAgpmItem` | [`AgpmItem`](../Module/AgpmItem.md) |
| `0xBAC` | `m_pAgpmAuction` | [`AgpmAuction`](../Module/AgpmAuction.md) |
| `0xBB0` | `m_pAgcmConnectManager` | [`AgcmConnectManager`](../Module/AgcmConnectManager.md) |
| `0xBB4` | `m_pAgcmEventManager` | `AgcmEventManager` |
| `0xBB8` | `m_pAgcmCharacter` | `AgcmCharacter` |

## AgcmBattleGround
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmBattleGround` | [`AgpmBattleGround`](../Module/AgpmBattleGround.md) |
| `0xB9C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA8` | `m_pcsAgcmUIManager2` | [`AgcmUIManager2`](../Module/AgcmUIManager2.md) |
| `0xBAC` | `m_pcsAgcmUISiegeWar` | [`AgcmUISiegeWar`](../Module/AgcmUISiegeWar.md) |
| `0xBB0` | `m_pcsAgcmWarInfo` | [`AgcmWarInfo`](../Module/AgcmWarInfo.md) |

## AgcmBillInfo
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmBillInfo` | [`AgpmBillInfo`](../Module/AgpmBillInfo.md) |

## AgcmCamera2
| Offset | Member | Typ |
|---:|---|---|
| `0xB9C` | `m_pAgcmRender` | [`AgcmRender`](../Module/AgcmRender.md) |
| `0xBA0` | `m_pAgcmMap` | [`AgcmMap`](../Module/AgcmMap.md) |
| `0xBA4` | `m_pApmObject` | [`ApmObject`](../Module/ApmObject.md) |
| `0xBA8` | `m_pAgcmObject` | [`AgcmObject`](../Module/AgcmObject.md) |
| `0xBAC` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xBB8` | `m_pAgcmCharacter` | `AgcmCharacter` |

## AgcmCashMall
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB9C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA0` | `m_pcsAgpmCashMall` | [`AgpmCashMall`](../Module/AgpmCashMall.md) |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgcmItem` | [`AgcmItem`](../Module/AgcmItem.md) |

## AgcmCharacter
| Offset | Member | Typ |
|---:|---|---|
| `0xD80` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xD84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xD88` | `m_pcsAgpmParty` | [`AgpmParty`](../Module/AgpmParty.md) |
| `0xD8C` | `m_pcsAgpmSkill` | [`AgpmSkill`](../Module/AgpmSkill.md) |
| `0xD90` | `m_pcsAgpmPvP` | [`AgpmPvP`](../Module/AgpmPvP.md) |
| `0xD94` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xD98` | `m_pcsAgcmShadow` | [`AgcmShadow`](../Module/AgcmShadow.md) |
| `0xD9C` | `m_pcsAgcmShadowmap` | [`AgcmShadowmap`](../Module/AgcmShadowmap.md) |
| `0xDA0` | `m_pcsAgcmConnectManager` | `AgcmConnectManager` |
| `0xDA4` | `m_pcsAgpmSummons` | [`AgpmSummons`](../Module/AgpmSummons.md) |
| `0xDB0` | `m_pcsAgpmArchlord` | `AgpmArchlord` |
| `0xDB8` | `m_pcsApmMap` | `ApmMap` |
| `0xDBC` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xDC0` | `m_pcsApmObject` | `ApmObject` |
| `0xDC4` | `m_pcsAgcmObject` | `AgcmObject` |
| `0xDC8` | `m_pcsAgcmLODManager` | [`AgcmLODManager`](../Module/AgcmLODManager.md) |
| `0xDCC` | `m_pcsAgcmShadow2` | [`AgcmShadow2`](../Module/AgcmShadow2.md) |
| `0xDD0` | `m_pcsAgcmFont` | [`AgcmFont`](../Module/AgcmFont.md) |
| `0xDD8` | `m_pcsAgcmResourceLoader` | [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md) |
| `0xDDC` | `m_pcsAgpmOptimizedPacket2` | [`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md) |
| `0xDE0` | `m_pcsAgcmSound` | [`AgcmSound`](../Module/AgcmSound.md) |
| `0xDE4` | `m_pcsAgpmPathFind` | [`AgpmPathFind`](../Module/AgpmPathFind.md) |
| `0xDF4` | `m_pcsAgcmGuild` | [`AgcmGuild`](../Module/AgcmGuild.md) |

## AgcmCustomizeRender
| Offset | Member | Typ |
|---:|---|---|
| `0xBD0` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |

## AgcmDynamicLightmap
| Offset | Member | Typ |
|---:|---|---|
| `0xBB4` | `m_pAgcmRender` | `AgcmRender` |
| `0xBB8` | `m_pAgcmMap` | `AgcmMap` |
| `0xBBC` | `m_pAgcmOcTree` | [`AgcmOcTree`](../Module/AgcmOcTree.md) |
| `0xBC0` | `m_pApmOcTree` | [`ApmOcTree`](../Module/ApmOcTree.md) |

## AgcmEventBank
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmEventBank` | [`AgpmEventBank`](../Module/AgpmEventBank.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmEventManager` | `AgcmEventManager` |

## AgcmEventCharCustomize
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmEventCharCustomize` | [`AgpmEventCharCustomize`](../Module/AgpmEventCharCustomize.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmEventManager` | `AgcmEventManager` |

## AgcmEventEffect
| Offset | Member | Typ |
|---:|---|---|
| `0xBD8` | `m_pcsAgpmArchlord` | `AgpmArchlord` |
| `0xBE0` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |

## AgcmEventGuild
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmEventGuild` | [`AgpmEventGuild`](../Module/AgpmEventGuild.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmEventManager` | `AgcmEventManager` |

## AgcmEventItemConvert
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmItemConvert` | [`AgpmItemConvert`](../Module/AgpmItemConvert.md) |
| `0xBA0` | `m_pcsAgpmEventItemConvert` | [`AgpmEventItemConvert`](../Module/AgpmEventItemConvert.md) |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgcmEventManager` | `AgcmEventManager` |

## AgcmEventItemRepair
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmEventItemRepair` | [`AgpmEventItemRepair`](../Module/AgpmEventItemRepair.md) |
| `0xB9C` | `m_pcsAgcmEventManager` | `AgcmEventManager` |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgcmEventManager
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmObject` | `AgcmObject` |
| `0xB9C` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA0` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgcmEventNPCTrade
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmObject` | `ApmObject` |
| `0xB9C` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA8` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBAC` | `m_pcsAgpmGrid` | [`AgpmGrid`](../Module/AgpmGrid.md) |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmEventManager` | `AgcmEventManager` |

## AgcmEventNature
| Offset | Member | Typ |
|---:|---|---|
| `0xB9C` | `m_pcsApmMap` | `ApmMap` |
| `0xBA0` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xBA4` | `m_pcsAgpmEventNature` | [`AgpmEventNature`](../Module/AgpmEventNature.md) |
| `0xBA8` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xBAC` | `m_pcsAgpmTimer` | [`AgpmTimer`](../Module/AgpmTimer.md) |
| `0xBB0` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBB8` | `m_pcsAgcmEff2` | [`AgcmEff2`](../Module/AgcmEff2.md) |
| `0xBBC` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |
| `0xBC0` | `m_pcsApmObject` | `ApmObject` |
| `0xBC4` | `m_pcsAgcmSound` | `AgcmSound` |
| `0xBC8` | `m_pcsAgcmNatureEffect` | [`AgcmNatureEffect`](../Module/AgcmNatureEffect.md) |

## AgcmEventPointLight
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB9C` | `m_pcsAgpmEventPointLight` | [`AgpmEventPointLight`](../Module/AgpmEventPointLight.md) |
| `0xBA0` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xBA4` | `m_pcsAgcmDynamicLightmap` | [`AgcmDynamicLightmap`](../Module/AgcmDynamicLightmap.md) |

## AgcmEventProduct
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pAgpmEventProduct` | [`AgpmEventProduct`](../Module/AgpmEventProduct.md) |
| `0xBA0` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pAgcmEventManager` | `AgcmEventManager` |

## AgcmEventQuest
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmEventQuest` | `AgpmEventQuest` |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmEventManager` | `AgcmEventManager` |
| `0xBA8` | `m_pcsAgcmObject` | `AgcmObject` |

## AgcmEventRefinery
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pAgpmEventRefinery` | [`AgpmEventRefinery`](../Module/AgpmEventRefinery.md) |
| `0xBA0` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pAgcmEventManager` | `AgcmEventManager` |

## AgcmEventSiegeWarNPC
| Offset | Member | Typ |
|---:|---|---|
| `0xB9C` | `m_pcsAgpmEventSiegeWarNPC` | [`AgpmEventSiegeWarNPC`](../Module/AgpmEventSiegeWarNPC.md) |
| `0xBA0` | `m_pcsAgcmEventManager` | `AgcmEventManager` |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |

## AgcmEventSkillMaster
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmEventSkillMaster` | [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBA8` | `m_pcsAgcmSkill` | [`AgcmSkill`](../Module/AgcmSkill.md) |
| `0xBAC` | `m_pcsAgcmEventManager` | `AgcmEventManager` |

## AgcmEventTeleport
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA0` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBA4` | `m_pcsAgcmEventManager` | `AgcmEventManager` |
| `0xBA8` | `m_pcsAgpmEventTeleport` | [`AgpmEventTeleport`](../Module/AgpmEventTeleport.md) |
| `0xBAC` | `m_pcsAgpmArchlord` | `AgpmArchlord` |

## AgcmGlare
| Offset | Member | Typ |
|---:|---|---|
| `0xB9C` | `m_pcsAgcmRender` | `AgcmRender` |

## AgcmGlyph
| Offset | Member | Typ |
|---:|---|---|
| `0xBEC` | `m_pcmMap` | `AgcmMap` |
| `0xBF0` | `m_pcmRender` | `AgcmRender` |
| `0xBF4` | `m_pcmResourceLoader` | `AgcmResourceLoader` |
| `0xBF8` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBFC` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xC00` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |
| `0xC04` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xC08` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0xC0C` | `m_pApmObject` | `ApmObject` |
| `0xC10` | `m_pcmObject` | `AgcmObject` |
| `0xC14` | `m_pcsAgcmCamera2` | [`AgcmCamera2`](../Module/AgcmCamera2.md) |

## AgcmGrass
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xB9C` | `m_pcsApmMap` | `ApmMap` |
| `0xBA0` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xBA4` | `m_pcsAgcmOcTree` | `AgcmOcTree` |
| `0xBA8` | `m_pcsApmOcTree` | `ApmOcTree` |
| `0xBAC` | `m_pcsAgcmEventNature` | [`AgcmEventNature`](../Module/AgcmEventNature.md) |
| `0xBB0` | `m_pcsAgcmShadow2` | `AgcmShadow2` |

## AgcmGuild
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB9C` | `m_pcsAgpmGuild` | [`AgpmGuild`](../Module/AgpmGuild.md) |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgcmTextBoardMng` | [`AgcmTextBoardMng`](../Module/AgcmTextBoardMng.md) |
| `0xBAC` | `m_pcsAgcmUIControl` | [`AgcmUIControl`](../Module/AgcmUIControl.md) |
| `0xBB0` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |

## AgcmItem
| Offset | Member | Typ |
|---:|---|---|
| `0xC50` | `m_pcsAgpmSystemMessage` | [`AgpmSystemMessage`](../Module/AgpmSystemMessage.md) |
| `0xC54` | `m_pcsApmMap` | `ApmMap` |
| `0xC60` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xC74` | `m_pcsAgcmLODManager` | `AgcmLODManager` |
| `0xC88` | `m_pcsAgcmShadow2` | `AgcmShadow2` |
| `0xC90` | `m_pAgcmUICooldown` | [`AgcmUICooldown`](../Module/AgcmUICooldown.md) |
| `0x1058` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |

## AgcmItemConvert
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |

## AgcmLODManager
| Offset | Member | Typ |
|---:|---|---|
| `0xC88` | `m_pcmRender` | `AgcmRender` |

## AgcmLensFlare
| Offset | Member | Typ |
|---:|---|---|
| `0xDF4` | `m_pcsApmMap` | `ApmMap` |
| `0xDF8` | `m_pcRender` | `AgcmRender` |
| `0xDFC` | `m_pcEventNature` | `AgcmEventNature` |
| `0xE00` | `m_pcAgcmMap` | `AgcmMap` |
| `0xE04` | `m_pcAgpmTimer` | `AgpmTimer` |

## AgcmMinimap
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xB9C` | `m_pcsAgpmParty` | `AgpmParty` |
| `0xBA0` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |
| `0xBA4` | `m_pcsAgcmFont` | `AgcmFont` |
| `0xBA8` | `m_pcsApmMap` | `ApmMap` |
| `0xC34` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xC3C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgcmNatureEffect
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xB9C` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xBA0` | `m_pcsAgpmNatureEffect` | [`AgpmNatureEffect`](../Module/AgpmNatureEffect.md) |

## AgcmObject
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmOcTree` | `ApmOcTree` |
| `0xD20` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xD24` | `m_pcsAgcmLODManager` | `AgcmLODManager` |
| `0xD28` | `m_pcsApmMap` | `ApmMap` |
| `0xD2C` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xD30` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |
| `0xD34` | `m_pcsAgcmShadow` | `AgcmShadow` |
| `0xD38` | `m_pcsAgcmOcTree` | `AgcmOcTree` |
| `0x139A0` | `m_pcsApmObject` | `ApmObject` |

## AgcmOcTree
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pApmOcTree` | `ApmOcTree` |
| `0xBA8` | `m_pApmMap` | `ApmMap` |

## AgcmParty
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pagpmParty` | `AgpmParty` |
| `0xBA0` | `m_pagcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pAgpmFactors` | `AgpmFactors` |

## AgcmPrivateTrade
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_papmMap` | `ApmMap` |
| `0xB9C` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xBA0` | `m_pagcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pagpmFactors` | `AgpmFactors` |
| `0xBA8` | `m_pagpmItem` | `AgpmItem` |
| `0xBAC` | `m_pagcmItem` | `AgcmItem` |
| `0xBB0` | `m_pagpmGrid` | `AgpmGrid` |

## AgcmProduct
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmProduct` | [`AgpmProduct`](../Module/AgpmProduct.md) |
| `0xB9C` | `m_pAgpmCharacter` | `AgpmCharacter` |

## AgcmProductMed
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmSkill` | `AgpmSkill` |
| `0xB9C` | `m_pAgcmSkill` | `AgcmSkill` |
| `0xBA0` | `m_pAgpmProduct` | `AgpmProduct` |
| `0xBA4` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pAgcmProduct` | [`AgcmProduct`](../Module/AgcmProduct.md) |
| `0xBAC` | `m_pAgcmUIProduct` | [`AgcmUIProduct`](../Module/AgcmUIProduct.md) |
| `0xBB0` | `m_pAgcmUIProductSkill` | [`AgcmUIProductSkill`](../Module/AgcmUIProductSkill.md) |
| `0xBB4` | `m_pAgcmUICooldown` | `AgcmUICooldown` |

## AgcmQuest
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmQuest` | `AgpmQuest` |

## AgcmRecruit
| Offset | Member | Typ |
|---:|---|---|
| `0xBA4` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xBA8` | `m_pagcmCharacter` | `AgcmCharacter` |
| `0xBAC` | `m_pagpmFactors` | `AgpmFactors` |
| `0xBB0` | `m_pagpmItem` | `AgpmItem` |
| `0xBB4` | `m_pagcmConnectManager` | `AgcmConnectManager` |

## AgcmRefinery
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmRefinery` | [`AgpmRefinery`](../Module/AgpmRefinery.md) |

## AgcmReturnToLogin
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmReturnToLogin` | [`AgpmReturnToLogin`](../Module/AgpmReturnToLogin.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmConnectManager` | `AgcmConnectManager` |
| `0xBA8` | `m_pcsAgcmLogin` | [`AgcmLogin`](../Module/AgcmLogin.md) |

## AgcmRide
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB88` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xB8C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB90` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xB94` | `m_pcsAgpmRide` | [`AgpmRide`](../Module/AgpmRide.md) |

## AgcmShadow2
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcRender` | `AgcmRender` |
| `0xB9C` | `m_pcApmMap` | `ApmMap` |
| `0xBA0` | `m_pcAgcmMap` | `AgcmMap` |
| `0xBA4` | `m_pcShadow` | `AgcmShadow` |
| `0xBAC` | `m_pcsAgcmOcTree` | `AgcmOcTree` |
| `0xBD4` | `m_pcsApmOcTree` | `ApmOcTree` |

## AgcmShadowmap
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgcmRender` | `AgcmRender` |

## AgcmSiegeWar
| Offset | Member | Typ |
|---:|---|---|
| `0xBA4` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA8` | `m_pcsAgpmSiegeWar` | [`AgpmSiegeWar`](../Module/AgpmSiegeWar.md) |
| `0xBAC` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmMinimap` | [`AgcmMinimap`](../Module/AgcmMinimap.md) |

## AgcmSkill
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA0` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xBA4` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBA8` | `m_pcsAgpmPvP` | `AgpmPvP` |
| `0xBAC` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBB8` | `m_pcsAgcmUIControl` | `AgcmUIControl` |
| `0xBBC` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |
| `0xBC0` | `m_pcsAgpmOptimizedPacket2` | `AgpmOptimizedPacket2` |

## AgcmStartupEncryption
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmStartupEncryption` | [`AgpmStartupEncryption`](../Module/AgpmStartupEncryption.md) |
| `0xB9C` | `m_pcsAgcmLogin` | `AgcmLogin` |
| `0xBA0` | `m_pcsAgcmReturnToLogin` | [`AgcmReturnToLogin`](../Module/AgcmReturnToLogin.md) |
| `0xBA4` | `m_pcsAgcmConnectManager` | `AgcmConnectManager` |
| `0xBA8` | `m_pcsAgcmCharacter` | `AgcmCharacter` |

## AgcmTargeting
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pAgcmGlyph` | [`AgcmGlyph`](../Module/AgcmGlyph.md) |
| `0xBA0` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pApmEventManager` | `ApmEventManager` |
| `0xBA8` | `m_pAgcmEventManager` | `AgcmEventManager` |
| `0xBAC` | `m_pAgcmMap` | `AgcmMap` |
| `0xBB0` | `m_pAgcmSkill` | `AgcmSkill` |
| `0xBB4` | `m_pAgpmItem` | `AgpmItem` |
| `0xBB8` | `m_pAgcmItem` | `AgcmItem` |
| `0xBBC` | `m_pAgcmPrivateTrade` | [`AgcmPrivateTrade`](../Module/AgcmPrivateTrade.md) |
| `0xBC0` | `m_pAgcmRender` | `AgcmRender` |
| `0xBC4` | `m_pAgcmParty` | [`AgcmParty`](../Module/AgcmParty.md) |
| `0xBC8` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xBCC` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xBD0` | `m_pAgcmUILogin` | [`AgcmUILogin`](../Module/AgcmUILogin.md) |
| `0xBD4` | `m_pAgcmUICharacter` | [`AgcmUICharacter`](../Module/AgcmUICharacter.md) |
| `0xBD8` | `m_pAgcmOcTree` | `AgcmOcTree` |
| `0xBE0` | `m_pAgcmTextBoardMng` | `AgcmTextBoardMng` |
| `0xBE4` | `m_pApmMap` | `ApmMap` |
| `0xBE8` | `m_pAgcmShrine` | [`AgcmShrine`](../Module/AgcmShrine.md) |
| `0xBF0` | `m_pAgcmShadow` | `AgcmShadow` |
| `0xBF4` | `m_pAgcmReturnToLogin` | `AgcmReturnToLogin` |
| `0xBF8` | `m_pAgpmSiegeWar` | `AgpmSiegeWar` |
| `0xBFC` | `m_pAgcmSiegeWar` | [`AgcmSiegeWar`](../Module/AgcmSiegeWar.md) |
| `0xC04` | `m_pApmOcTree` | `ApmOcTree` |

## AgcmTextBoardMng
| Offset | Member | Typ |
|---:|---|---|
| `0xFE8` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xFEC` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xFF0` | `m_pcRender` | `AgcmRender` |
| `0xFF8` | `m_pcFont` | `AgcmFont` |
| `0xFFC` | `m_pcApmMap` | `ApmMap` |
| `0x1000` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0x1004` | `m_pcsAgpmItem` | `AgpmItem` |
| `0x1008` | `m_pcsAgcmItem` | `AgcmItem` |
| `0x100C` | `m_pcsApmObject` | `ApmObject` |
| `0x1010` | `m_pcsAgcmObject` | `AgcmObject` |
| `0x1014` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0x101C` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0x1020` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0x1024` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0x1028` | `m_pcsAgpmParty` | `AgpmParty` |
| `0x102C` | `m_pcsAgpmPvP` | `AgpmPvP` |
| `0x1030` | `m_pcsAgpmBillInfo` | `AgpmBillInfo` |
| `0x1034` | `m_pcsAgpmSiegeWar` | `AgpmSiegeWar` |
| `0x1038` | `m_pcsAgcmSiegeWar` | `AgcmSiegeWar` |
| `0x103C` | `m_pcsAgpmBattleGround` | `AgpmBattleGround` |
| `0x1040` | `m_pcsAgcmUIControl` | `AgcmUIControl` |
| `0x1044` | `m_pcsAgcmSound` | `AgcmSound` |

## AgcmTuner
| Offset | Member | Typ |
|---:|---|---|
| `0xBC8` | `m_pcmRender` | `AgcmRender` |
| `0xC9C` | `m_pcmMap` | `AgcmMap` |
| `0xCA0` | `m_pcmLODManager` | `AgcmLODManager` |
| `0xCA4` | `m_pcmFont` | `AgcmFont` |
| `0xCA8` | `m_pcmWater` | [`AgcmWater`](../Module/AgcmWater.md) |
| `0xCAC` | `m_pcmLensFlare` | [`AgcmLensFlare`](../Module/AgcmLensFlare.md) |
| `0xCB0` | `m_pcmShadow` | `AgcmShadow` |
| `0xCB4` | `m_pcmTBoard` | `AgcmTextBoardMng` |

## AgcmUIArchlord
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xB9C` | `m_pcsAgpmArchlord` | `AgpmArchlord` |
| `0xBA0` | `m_pcsAgcmArchlord` | [`AgcmArchlord`](../Module/AgcmArchlord.md) |

## AgcmUIAuction
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBAC` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |
| `0xBB0` | `m_pcsAgpmAuctionCategory` | [`AgpmAuctionCategory`](../Module/AgpmAuctionCategory.md) |
| `0xBB4` | `m_pcsAgpmAuction` | `AgpmAuction` |
| `0xBB8` | `m_pcsAgcmAuction` | [`AgcmAuction`](../Module/AgcmAuction.md) |
| `0xBBC` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBC0` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC4` | `m_pcsAgcmUISplitItem` | [`AgcmUISplitItem`](../Module/AgcmUISplitItem.md) |
| `0xBC8` | `m_pcsAgcmUICooldown` | `AgcmUICooldown` |

## AgcmUIBuddy
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmBuddy` | [`AgpmBuddy`](../Module/AgpmBuddy.md) |
| `0xB9C` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgcmUIMain` | [`AgcmUIMain`](../Module/AgcmUIMain.md) |
| `0xBA8` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBAC` | `m_pcsAgpmChatting` | [`AgpmChatting`](../Module/AgpmChatting.md) |
| `0xBB0` | `m_pcsAgcmUIChatting2` | [`AgcmUIChatting2`](../Module/AgcmUIChatting2.md) |
| `0xBB4` | `m_pcsApmMap` | `ApmMap` |
| `0xBB8` | `m_pcsAgcmParty` | `AgcmParty` |

## AgcmUICashInven
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBA0` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA4` | `m_pcsAgpmCashMall` | `AgpmCashMall` |
| `0xBA8` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xBAC` | `m_pcsAgpmSystemMessage` | `AgpmSystemMessage` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmCashMall` | [`AgcmCashMall`](../Module/AgcmCashMall.md) |
| `0xBB8` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBBC` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBC0` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBC4` | `m_pcsAgcmUIItem` | [`AgcmUIItem`](../Module/AgcmUIItem.md) |
| `0xBC8` | `m_pcsAgcmUIControl` | `AgcmUIControl` |

## AgcmUICashMall
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBA0` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA4` | `m_pcsAgpmCashMall` | `AgpmCashMall` |
| `0xBA8` | `m_pagpmBillInfo` | `AgpmBillInfo` |
| `0xBAC` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB0` | `m_pcsAgcmCashMall` | `AgcmCashMall` |
| `0xBB4` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBB8` | `m_pcsAgcmUIMain` | `AgcmUIMain` |

## AgcmUIChannel
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIChannel` | [`AgcmUIChannel`](../Module/AgcmUIChannel.md) |
| `0xB9C` | `m_pcsAgpmChannel` | [`AgpmChannel`](../Module/AgpmChannel.md) |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA8` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBAC` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBB0` | `m_pcsAgpmChatting` | `AgpmChatting` |
| `0xBB4` | `m_pcsAgcmUIChatting2` | `AgcmUIChatting2` |

## AgcmUIControl
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |

## AgcmUICooldown
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA0` | `m_pAgcmUIControl` | `AgcmUIControl` |

## AgcmUICustomizing
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA0` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA4` | `m_pcsAgpmEventCharCustomize` | `AgpmEventCharCustomize` |
| `0xBA8` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBAC` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBB0` | `m_pcsAgcmCustomizeRender` | [`AgcmCustomizeRender`](../Module/AgcmCustomizeRender.md) |
| `0xBB4` | `m_pcsAgcmEventCharCustomize` | [`AgcmEventCharCustomize`](../Module/AgcmEventCharCustomize.md) |
| `0xBB8` | `m_pcsAgcmUIChatting2` | `AgcmUIChatting2` |
| `0xBBC` | `m_pcsAgcmUIMain` | `AgcmUIMain` |

## AgcmUIDebugInfo
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xCA8` | `m_pcsApmMap` | `ApmMap` |
| `0xCAC` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xCB0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xCB4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xCB8` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xCBC` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xCC0` | `m_pcsApmObject` | `ApmObject` |
| `0xCC4` | `m_pcsAgcmObject` | `AgcmObject` |
| `0xCC8` | `m_pcsAgcmGrass` | [`AgcmGrass`](../Module/AgcmGrass.md) |
| `0xCCC` | `m_pcsAgcmShadow2` | `AgcmShadow2` |
| `0xCD0` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xCD4` | `m_pcsAgcmSound` | `AgcmSound` |
| `0xCD8` | `m_pcsAgcmFont` | `AgcmFont` |
| `0xCDC` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |
| `0xCE0` | `m_pcsAgcmEff2` | `AgcmEff2` |

## AgcmUIEventBank
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBA8` | `m_pcsAgcmEventBank` | [`AgcmEventBank`](../Module/AgcmEventBank.md) |
| `0xBAC` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |

## AgcmUIEventGacha
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB9C` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA0` | `m_pcsAgcmEventGacha` | [`AgcmEventGacha`](../Module/AgcmEventGacha.md) |

## AgcmUIEventItemConvert
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA8` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmItemConvert` | [`AgcmItemConvert`](../Module/AgcmItemConvert.md) |
| `0xBB8` | `m_pcsAgcmEventItemConvert` | [`AgcmEventItemConvert`](../Module/AgcmEventItemConvert.md) |
| `0xBBC` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC0` | `m_pcsAgcmSound` | `AgcmSound` |

## AgcmUIEventItemRepair
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA0` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA4` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBA8` | `m_pcsAgpmEventItemRepair` | `AgpmEventItemRepair` |
| `0xBAC` | `m_pcsAgcmEventItemRepair` | [`AgcmEventItemRepair`](../Module/AgcmEventItemRepair.md) |
| `0xBB0` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBB4` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBB8` | `m_pcsAgcmUIItem` | `AgcmUIItem` |
| `0xBBC` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBC0` | `m_pcsAgcmSkill` | `AgcmSkill` |

## AgcmUIEventTeleport
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB9C` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA0` | `m_pcsAgcmEventTeleport` | [`AgcmEventTeleport`](../Module/AgcmEventTeleport.md) |
| `0xBA4` | `m_pcsAgpmEventTeleport` | `AgpmEventTeleport` |
| `0xBA8` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBAC` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB0` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xBB4` | `m_pcsAgpmSiegeWar` | `AgpmSiegeWar` |

## AgcmUIGuild
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xB9C` | `m_pcsAgpmPvP` | `AgpmPvP` |
| `0xBA0` | `m_pcsAgpmSiegeWar` | `AgpmSiegeWar` |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBAC` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBB0` | `m_pcsAgcmGuild` | `AgcmGuild` |
| `0xBB4` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBB8` | `m_pcsAgcmEventGuild` | [`AgcmEventGuild`](../Module/AgcmEventGuild.md) |
| `0xBBC` | `m_pcsAgcmFont` | `AgcmFont` |
| `0xBC0` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBC4` | `m_pcsAgcmUIPartyOption` | [`AgcmUIPartyOption`](../Module/AgcmUIPartyOption.md) |
| `0xBC8` | `m_pcsAgpmParty` | `AgpmParty` |
| `0xBCC` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBD0` | `m_pcsAgcmUIControl` | `AgcmUIControl` |
| `0xBD4` | `m_pcsAgcmTextBoard` | `AgcmTextBoardMng` |
| `0xBD8` | `m_pcsAgcmUIChatting2` | `AgcmUIChatting2` |

## AgcmUIGuildWarehouse
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xB9C` | `m_pAgpmGrid` | `AgpmGrid` |
| `0xBA0` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pAgpmItem` | `AgpmItem` |
| `0xBA8` | `m_pAgpmGuild` | `AgpmGuild` |
| `0xBAC` | `m_pAgpmGuildWarehouse` | [`AgpmGuildWarehouse`](../Module/AgpmGuildWarehouse.md) |
| `0xBB0` | `m_pAgpmSiegeWar` | `AgpmSiegeWar` |
| `0xBB4` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBB8` | `m_pAgcmEventGuild` | `AgcmEventGuild` |
| `0xBBC` | `m_pAgcmItem` | `AgcmItem` |
| `0xBC0` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC4` | `m_pAgcmUIControl` | `AgcmUIControl` |
| `0xBC8` | `m_pAgcmUIMain` | `AgcmUIMain` |
| `0xBCC` | `m_pAgcmUIItem` | `AgcmUIItem` |

## AgcmUIHelp
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgcmUIManager2` | `AgcmUIManager2` |

## AgcmUIHotkey
| Offset | Member | Typ |
|---:|---|---|
| `0xBA0` | `m_pAgcmUIManager2` | `AgcmUIManager2` |

## AgcmUIItem
| Offset | Member | Typ |
|---:|---|---|
| `0xBA8` | `m_pcsAgcmItemConvert` | `AgcmItemConvert` |
| `0xBB0` | `m_pcsAgpmEventSkillMaster` | `AgpmEventSkillMaster` |
| `0xBC4` | `m_pcsAgcmEventNPCTrade` | `AgcmEventNPCTrade` |
| `0xBD0` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBD4` | `m_pcsAgcmUICharacter` | `AgcmUICharacter` |
| `0xBD8` | `m_pcsAgcmUIAuction` | [`AgcmUIAuction`](../Module/AgcmUIAuction.md) |
| `0xBDC` | `m_pcsAgcmUISplitItem` | `AgcmUISplitItem` |
| `0xBE0` | `m_pcsAgpmBillInfo` | `AgpmBillInfo` |
| `0xBE8` | `m_pcsAgpmCombat` | [`AgpmCombat`](../Module/AgpmCombat.md) |
| `0xBEC` | `m_pcsAgpmEventItemRepair` | `AgpmEventItemRepair` |
| `0xBF0` | `m_pcsAgpmReturnToLogin` | `AgpmReturnToLogin` |
| `0xBF4` | `m_pcsAgpmArchlord` | `AgpmArchlord` |

## AgcmUIMain
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xB9C` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBA0` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA4` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA8` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBAC` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0xBB8` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBBC` | `m_pcsApmMap` | `ApmMap` |
| `0xBC0` | `m_pcsAgcmEff2` | `AgcmEff2` |
| `0x29D8` | `m_pcsAgcmLogin` | `AgcmLogin` |

## AgcmUIManager2
| Offset | Member | Typ |
|---:|---|---|
| `0x25A0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0x4540` | `m_pcsAgcmFont` | `AgcmFont` |
| `0x4544` | `m_pcsAgcmRender` | `AgcmRender` |
| `0x4548` | `m_pcsAgcmSound` | `AgcmSound` |
| `0x454C` | `m_pcsAgcmResourceLoader` | `AgcmResourceLoader` |
| `0x4550` | `m_pcsAgcmUIControl` | `AgcmUIControl` |

## AgcmUIOption
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xB9C` | `m_pcsAgcmTuner` | [`AgcmTuner`](../Module/AgcmTuner.md) |
| `0xBA0` | `m_pcsAgcmShadow` | `AgcmShadow` |
| `0xBA4` | `m_pcsAgcmShadow2` | `AgcmShadow2` |
| `0xBA8` | `m_pcsAgcmSound` | `AgcmSound` |
| `0xBAC` | `m_pcsAgcmEff2` | `AgcmEff2` |
| `0xBB8` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xBBC` | `m_pcsAgcmLogin` | `AgcmLogin` |
| `0xBC0` | `m_pcsAgcmGrass` | `AgcmGrass` |
| `0xBC4` | `m_pcsAgcmLensFlare` | `AgcmLensFlare` |
| `0xBC8` | `m_pcsAgcmEventNature` | `AgcmEventNature` |
| `0xBCC` | `m_pcsAgcmWater` | `AgcmWater` |
| `0xBD0` | `m_pcsAgcmShadowMap` | `AgcmShadowmap` |
| `0xBD4` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xBD8` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBDC` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBE0` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xBE4` | `m_pcsAgcmGuild` | `AgcmGuild` |
| `0xBE8` | `m_pcsAgcmUIParty` | [`AgcmUIParty`](../Module/AgcmUIParty.md) |
| `0xBEC` | `m_pcsAgcmUIStatus` | [`AgcmUIStatus`](../Module/AgcmUIStatus.md) |
| `0xBF8` | `m_pcsAgcmPostFX` | [`AgcmPostFX`](../Module/AgcmPostFX.md) |
| `0xD78` | `m_pcsAgcmTextBoardMng` | `AgcmTextBoardMng` |
| `0xF5C` | `m_pcsAgcmUITips` | [`AgcmUITips`](../Module/AgcmUITips.md) |

## AgcmUIParty
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmMap` | `ApmMap` |
| `0xB9C` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgpmParty` | `AgpmParty` |
| `0xBAC` | `m_pcsAgcmParty` | `AgcmParty` |
| `0xBB0` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBB4` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBB8` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xBBC` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0xBC0` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBC4` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBC8` | `m_pcsAgcmPrivateTrade` | `AgcmPrivateTrade` |

## AgcmUIPartyOption
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB9C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pcsAgpmParty` | `AgpmParty` |
| `0xBA8` | `m_pcsAgcmParty` | `AgcmParty` |
| `0xBAC` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBB4` | `m_pcsAgpmItem` | `AgpmItem` |

## AgcmUIProduct
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xBA0` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBA4` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA8` | `m_pAgpmProduct` | `AgpmProduct` |
| `0xBAC` | `m_pAgcmProduct` | `AgcmProduct` |
| `0xBB0` | `m_pAgpmItem` | `AgpmItem` |
| `0xBB4` | `m_pAgcmItem` | `AgcmItem` |
| `0xBB8` | `m_pAgcmUIControl` | `AgcmUIControl` |
| `0xBBC` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xBC0` | `m_pAgpmSkill` | `AgpmSkill` |
| `0xBC8` | `m_pAgcmUIMain` | `AgcmUIMain` |
| `0xBCC` | `m_pAgcmUICooldown` | `AgcmUICooldown` |
| `0xBD0` | `m_pAgcmUIProductSkill` | `AgcmUIProductSkill` |
| `0x2B54` | `m_pAgcmSkill` | `AgcmSkill` |

## AgcmUIProductSkill
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xBA0` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pAgpmItem` | `AgpmItem` |
| `0xBA8` | `m_pAgpmSkill` | `AgpmSkill` |
| `0xBAC` | `m_pAgpmProduct` | `AgpmProduct` |
| `0xBB0` | `m_pAgpmEventProduct` | `AgpmEventProduct` |
| `0xBB4` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBB8` | `m_pAgcmItem` | `AgcmItem` |
| `0xBBC` | `m_pAgcmSkill` | `AgcmSkill` |
| `0xBC0` | `m_pAgcmProduct` | `AgcmProduct` |
| `0xBC4` | `m_pAgcmEventProduct` | [`AgcmEventProduct`](../Module/AgcmEventProduct.md) |
| `0xBC8` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xBCC` | `m_pAgcmUICharacter` | `AgcmUICharacter` |
| `0xBD0` | `m_pAgcmUIMain` | `AgcmUIMain` |
| `0xBD4` | `m_pAgcmUIItem` | `AgcmUIItem` |
| `0xBD8` | `m_pAgcmUISkill2` | [`AgcmUISkill2`](../Module/AgcmUISkill2.md) |

## AgcmUIPvP
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmMap` | `ApmMap` |
| `0xB9C` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBA8` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBAC` | `m_pcsAgpmPvP` | `AgpmPvP` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmWorld` | [`AgcmWorld`](../Module/AgcmWorld.md) |
| `0xBB8` | `m_pcsAgcmUIControl` | `AgcmUIControl` |
| `0xBBC` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC0` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBC4` | `m_pcsAgcmUICharacter` | `AgcmUICharacter` |

## AgcmUIQuest2
| Offset | Member | Typ |
|---:|---|---|
| `0xBB8` | `m_pcsAgpmQuest` | `AgpmQuest` |
| `0xBBC` | `m_pcsAgcmQuest` | [`AgcmQuest`](../Module/AgcmQuest.md) |
| `0xBC0` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBC4` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC8` | `m_pcsAgcmUIControl` | `AgcmUIControl` |
| `0xBCC` | `m_pcsAgcmEventQuest` | [`AgcmEventQuest`](../Module/AgcmEventQuest.md) |
| `0xBD0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBD4` | `m_pcsAgcmEventEffect` | [`AgcmEventEffect`](../Module/AgcmEventEffect.md) |
| `0xBD8` | `m_pcsAgcmTextBoard` | `AgcmTextBoardMng` |
| `0xBDC` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBE0` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBE4` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBE8` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBEC` | `m_pcsApmMap` | `ApmMap` |
| `0xBF0` | `m_pcsAgcmUICharacter` | `AgcmUICharacter` |
| `0xBF4` | `m_pcsAgcmObject` | `AgcmObject` |
| `0xBF8` | `m_pcsApmObject` | `ApmObject` |
| `0xBFC` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xC00` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0xC04` | `m_pcsAgcmUICooldown` | `AgcmUICooldown` |
| `0x3204` | `m_pcsAgcmUIMain` | `AgcmUIMain` |

## AgcmUIRefinery
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xB9C` | `m_pAgpmGrid` | `AgpmGrid` |
| `0xBA0` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pAgpmItem` | `AgpmItem` |
| `0xBA8` | `m_pAgpmRefinery` | `AgpmRefinery` |
| `0xBAC` | `m_pAgcmCharacter` | `AgcmCharacter` |
| `0xBB0` | `m_pAgcmItem` | `AgcmItem` |
| `0xBB4` | `m_pAgcmRefinery` | [`AgcmRefinery`](../Module/AgcmRefinery.md) |
| `0xBB8` | `m_pAgcmEventRefinery` | [`AgcmEventRefinery`](../Module/AgcmEventRefinery.md) |
| `0xBBC` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC0` | `m_pAgcmUIControl` | `AgcmUIControl` |
| `0xBC4` | `m_pAgcmUIMain` | `AgcmUIMain` |
| `0xBC8` | `m_pAgcmUIItem` | `AgcmUIItem` |
| `0xBCC` | `m_pAgcmUICooldown` | `AgcmUICooldown` |

## AgcmUIRemission
| Offset | Member | Typ |
|---:|---|---|
| `0xBB0` | `m_pAgcmUICooldown` | `AgcmUICooldown` |
| `0xBE0` | `m_pAgcmEventManager` | `AgcmEventManager` |

## AgcmUISearch
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUISearch` | [`AgcmUISearch`](../Module/AgcmUISearch.md) |
| `0xB9C` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA0` | `m_pcsApmMap` | `ApmMap` |
| `0xBA4` | `m_pcsAgpmSearch` | [`AgpmSearch`](../Module/AgpmSearch.md) |

## AgcmUISiegeWar
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmMap` | `ApmMap` |
| `0xB9C` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBA0` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA4` | `m_pcsAgpmSiegeWar` | `AgpmSiegeWar` |
| `0xBA8` | `m_pcsAgpmEventSiegeWarNPC` | `AgpmEventSiegeWarNPC` |
| `0xBAC` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xBB0` | `m_pcsAgpmAdmin` | `AgpmAdmin` |
| `0xBB4` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBB8` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBBC` | `m_pcsAgcmSiegeWar` | `AgcmSiegeWar` |
| `0xBC0` | `m_pcsAgcmEventSiegeWarNPC` | [`AgcmEventSiegeWarNPC`](../Module/AgcmEventSiegeWarNPC.md) |
| `0xBC4` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC8` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xBCC` | `m_pcsAgcmUICharacter` | `AgcmUICharacter` |
| `0xBD0` | `m_pcsAgcmUICooldown` | `AgcmUICooldown` |
| `0xBD4` | `m_pcsAgcmUIItem` | `AgcmUIItem` |
| `0xBD8` | `m_pcsAgcmTextBoard` | `AgcmTextBoardMng` |
| `0x199C` | `m_pcsAgcmUIControl` | `AgcmUIControl` |

## AgcmUISkill2
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xBA4` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA8` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xBAC` | `m_pcsAgpmEventSkillMaster` | `AgpmEventSkillMaster` |
| `0xBB0` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBB4` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBB8` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0xBBC` | `m_pcsAgcmEventSkillMaster` | [`AgcmEventSkillMaster`](../Module/AgcmEventSkillMaster.md) |
| `0xBC0` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBC4` | `m_pcsAgcmUICharacter` | `AgcmUICharacter` |
| `0xBC8` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBCC` | `m_pcsAgcmUIItem` | `AgcmUIItem` |
| `0xBD0` | `m_pcsAgcmUIControl` | `AgcmUIControl` |
| `0xBD4` | `m_pcsAgcmEventEffect` | `AgcmEventEffect` |
| `0xBD8` | `m_pcsAgpmBillInfo` | `AgpmBillInfo` |
| `0xBDC` | `m_pcsAgcmUICashInven` | [`AgcmUICashInven`](../Module/AgcmUICashInven.md) |

## AgcmUISkillDragonScion
| Offset | Member | Typ |
|---:|---|---|
| `0x2554` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0x2558` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0x255C` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0x2560` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0x2564` | `m_pcsAgpmEventSkillMaster` | `AgpmEventSkillMaster` |
| `0x2568` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0x256C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0x2570` | `m_pcsAgpmItem` | `AgpmItem` |
| `0x2574` | `m_pcsAgcmSkill` | `AgcmSkill` |
| `0x2578` | `m_pcsAgcmEventSkillMaster` | `AgcmEventSkillMaster` |
| `0x257C` | `m_pcsAgcmUICharacter` | `AgcmUICharacter` |
| `0x2580` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0x2584` | `m_pcsAgcmUIItem` | `AgcmUIItem` |

## AgcmUISocialAction
| Offset | Member | Typ |
|---:|---|---|
| `0x2938` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0x294C` | `m_pcsAgcmUIMain` | `AgcmUIMain` |

## AgcmUISplitItem
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB9C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA0` | `m_pcsAgcmItem` | `AgcmItem` |
| `0xBA4` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |
| `0xBA8` | `m_pcsAgcmCharacter` | `AgcmCharacter` |

## AgcmUIStatus
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB9C` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xBA0` | `m_pcsAgpmUIStatus` | [`AgpmUIStatus`](../Module/AgpmUIStatus.md) |
| `0xBA4` | `m_pcsAgcmCharacter` | `AgcmCharacter` |
| `0xBA8` | `m_pcsAgcmUIMain` | `AgcmUIMain` |
| `0xBAC` | `m_pcsAgcmItem` | `AgcmItem` |

## AgcmUITips
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pAgcmUIManager2` | `AgcmUIManager2` |
| `0xB9C` | `m_pAgcmLogin` | `AgcmLogin` |
| `0xBA0` | `m_pAgcmResourceLoader` | `AgcmResourceLoader` |

## AgcmUIWarInfo
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `AgcmUIManager2` |

## AgcmWarInfo
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgpmWarInfo` | [`AgpmWarInfo`](../Module/AgpmWarInfo.md) |
| `0xB9C` | `m_pcsAgcmUIWarInfo` | [`AgcmUIWarInfo`](../Module/AgcmUIWarInfo.md) |

## AgcmWater
| Offset | Member | Typ |
|---:|---|---|
| `0xB98` | `m_pcsAgcmMap` | `AgcmMap` |
| `0xB9C` | `m_pcsAgcmRender` | `AgcmRender` |
| `0xBA0` | `m_pcsAgcmOcTree` | `AgcmOcTree` |
| `0xBA4` | `m_pcsApmOcTree` | `ApmOcTree` |
| `0xBA8` | `m_pcsAgcmEventNature` | `AgcmEventNature` |
| `0xBAC` | `m_pcsAgpmReturnToLogin` | `AgpmReturnToLogin` |

## AgpmAdmin
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB8C` | `m_pcsAgpmConfig` | [`AgpmConfig`](../Module/AgpmConfig.md) |

## AgpmArchlord
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmAuctionCategory
| Offset | Member | Typ |
|---:|---|---|
| `0xCEC` | `m_pcsAgpmItem` | `AgpmItem` |

## AgpmBillInfo
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmBuddy
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmCashMall
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB8C` | `m_pcsAgpmItem` | `AgpmItem` |

## AgpmChannel
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_papmMap` | `ApmMap` |
| `0xB90` | `m_pcsAgpmSystemMessage` | `AgpmSystemMessage` |

## AgpmCharacter
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pcsApmMap` | `ApmMap` |
| `0xB8C` | `m_pcsAgpmConfig` | `AgpmConfig` |

## AgpmChatting
| Offset | Member | Typ |
|---:|---|---|
| `0xC3C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xC40` | `m_pcsAgpmParty` | `AgpmParty` |

## AgpmCombat
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB90` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |
| `0xB94` | `m_pcsAgpmSkill` | `AgpmSkill` |

## AgpmEventBank
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgpmEventCharCustomize
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB88` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB8C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB90` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB94` | `m_pcsAgpmGrid` | `AgpmGrid` |

## AgpmEventGacha
| Offset | Member | Typ |
|---:|---|---|
| `0x134B0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0x134B4` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0x134B8` | `m_pcsAgpmFactor` | `AgpmFactors` |
| `0x134BC` | `m_pcsApmObject` | `ApmObject` |

## AgpmEventGuide
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgpmEventGuild
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgpmEventItemConvert
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB90` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |

## AgpmEventItemRepair
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB90` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgpmEventNPCDialog
| Offset | Member | Typ |
|---:|---|---|
| `0xBCC` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBD0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmEventNPCTrade
| Offset | Member | Typ |
|---:|---|---|
| `0xBCC` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBD0` | `m_pcsAgpmGrid` | `AgpmGrid` |

## AgpmEventNature
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB88` | `m_pcsAgpmTimer` | `AgpmTimer` |
| `0xB8C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmEventPointLight
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgpmEventProduct
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pAgpmProduct` | `AgpmProduct` |
| `0xB8C` | `m_pApmEventManager` | `ApmEventManager` |
| `0xB90` | `m_pAgpmEventSkillMaster` | `AgpmEventSkillMaster` |

## AgpmEventQuest
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB8C` | `m_pcsApmObject` | `ApmObject` |

## AgpmEventRefinery
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pApmEventManager` | `ApmEventManager` |
| `0xB88` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pApmObject` | `ApmObject` |

## AgpmEventSiegeWarNPC
| Offset | Member | Typ |
|---:|---|---|
| `0x25DAC` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0x25DB0` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0x25DB4` | `m_pcsAgpmSiegeWar` | `AgpmSiegeWar` |

## AgpmEventSkillMaster
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB88` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB8C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB90` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB94` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB98` | `m_pcsAgpmSkill` | `AgpmSkill` |

## AgpmEventTeleport
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmSiegeWar` | `AgpmSiegeWar` |
| `0xB90` | `m_pcsAgpmArchlord` | `AgpmArchlord` |
| `0xB94` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xBA0` | `m_pcsAgpmFactors` | `AgpmFactors` |

## AgpmGuild
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pagpmItem` | `AgpmItem` |
| `0xB8C` | `m_pagpmGrid` | `AgpmGrid` |

## AgpmItem
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_papmMap` | `ApmMap` |
| `0xB88` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pagpmFactors` | `AgpmFactors` |
| `0xB90` | `m_pagpmBillInfo` | `AgpmBillInfo` |
| `0xB94` | `m_pagpmSystemMessage` | `AgpmSystemMessage` |
| `0xEC0` | `m_pagpmGrid` | `AgpmGrid` |

## AgpmItemConvert
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB90` | `m_pcsAgpmSkill` | `AgpmSkill` |

## AgpmOptimizedPacket2
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB90` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB94` | `m_pcsAgpmItemConvert` | `AgpmItemConvert` |
| `0xB98` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xB9C` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xBA0` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xBA4` | `m_pcsAgpmUIStatus` | `AgpmUIStatus` |
| `0xBA8` | `m_pcsAgpmBillInfo` | `AgpmBillInfo` |

## AgpmParty
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pagpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pagpmUnion` | [`AgpmUnion`](../Module/AgpmUnion.md) |

## AgpmPathFind
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_papmMap` | `ApmMap` |

## AgpmProduct
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pAgpmItem` | `AgpmItem` |
| `0xB88` | `m_pAgpmGrid` | `AgpmGrid` |
| `0xB8C` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xB90` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB94` | `m_pAgpmSkill` | `AgpmSkill` |
| `0xB98` | `m_pApmEventManager` | `ApmEventManager` |

## AgpmPvP
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_papmMap` | `ApmMap` |
| `0xB88` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pagpmFactors` | `AgpmFactors` |
| `0xB90` | `m_pagpmGuild` | `AgpmGuild` |
| `0xB94` | `m_pagpmSkill` | `AgpmSkill` |
| `0xB98` | `m_pagpmSummons` | `AgpmSummons` |
| `0xB9C` | `m_pagpmParty` | `AgpmParty` |

## AgpmQuest
| Offset | Member | Typ |
|---:|---|---|
| `0xCEC` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xCF0` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xCF4` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xCF8` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xCFC` | `m_pcsApmEventManager` | `ApmEventManager` |
| `0xD00` | `m_pcsAgpmGrid` | `AgpmGrid` |

## AgpmRefinery
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pAgpmItem` | `AgpmItem` |
| `0xB88` | `m_pAgpmGrid` | `AgpmGrid` |
| `0xB8C` | `m_pAgpmFactors` | `AgpmFactors` |
| `0xB90` | `m_pAgpmCharacter` | `AgpmCharacter` |

## AgpmRemission
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pAgpmItem` | `AgpmItem` |
| `0xB8C` | `m_pApmEventManager` | `ApmEventManager` |
| `0xB90` | `m_pAgpmGrid` | `AgpmGrid` |

## AgpmReturnToLogin
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmRide
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB88` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB8C` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## AgpmSiegeWar
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmMap` | `ApmMap` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pcsAgpmGuild` | `AgpmGuild` |
| `0xB90` | `m_pcsAgpmAdmin` | `AgpmAdmin` |
| `0xB94` | `m_pcsAgpmEventSpawn` | `AgpmEventSpawn` |
| `0xB98` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB9C` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xBA0` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xBA4` | `m_pcsAgpmPvP` | `AgpmPvP` |
| `0xBA8` | `m_pcsAgpmEventBinding` | `AgpmEventBinding` |
| `0xBAC` | `m_pcsAgpmConfig` | `AgpmConfig` |

## AgpmSkill
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_papmObject` | `ApmObject` |
| `0xB88` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB8C` | `m_pagpmGrid` | `AgpmGrid` |
| `0xB90` | `m_pagpmItem` | `AgpmItem` |
| `0xB94` | `m_pagpmFactors` | `AgpmFactors` |
| `0xB98` | `m_pagpmParty` | `AgpmParty` |
| `0xB9C` | `m_pagpmBillInfo` | `AgpmBillInfo` |
| `0xBA0` | `m_pagpmConfig` | `AgpmConfig` |
| `0xBA4` | `m_papmEventManager` | `ApmEventManager` |

## AgpmSummons
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pagpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pagpmFactors` | `AgpmFactors` |
| `0xB8C` | `m_pagpmSystemMessage` | `AgpmSystemMessage` |

## AgpmUIStatus
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB88` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB8C` | `m_pcsAgpmSkill` | `AgpmSkill` |
| `0xB90` | `m_pcsApmEventManager` | `ApmEventManager` |

## AgpmUnion
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB88` | `m_pcsAgpmCharacter` | `AgpmCharacter` |

## ApmEventManager
| Offset | Member | Typ |
|---:|---|---|
| `0xB84` | `m_pcsApmMap` | `ApmMap` |
| `0xB88` | `m_pcsApmObject` | `ApmObject` |
| `0xB8C` | `m_pcsAgpmGrid` | `AgpmGrid` |
| `0xB90` | `m_pcsAgpmFactors` | `AgpmFactors` |
| `0xB94` | `m_pcsAgpmCharacter` | `AgpmCharacter` |
| `0xB98` | `m_pcsAgpmItem` | `AgpmItem` |
| `0xB9C` | `m_pcsAgpmParty` | `AgpmParty` |

## ApmObject
| Offset | Member | Typ |
|---:|---|---|
| `0xB90` | `m_pcsApmMap` | `ApmMap` |

## ApmOcTree
| Offset | Member | Typ |
|---:|---|---|
| `0xB88` | `m_pApmMap` | `ApmMap` |
