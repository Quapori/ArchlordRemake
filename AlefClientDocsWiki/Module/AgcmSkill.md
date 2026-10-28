# AgcmSkill (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmSkill` (Fertigkeiten wirken, Warteschlange, Rasterfelder, Stream-Laden) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Aufrufer, EP8-Quelle `Modules/AClient/AgcmSkill/` (`AgcmSkill.cpp`, `AgcmSkillMastery.cpp`, `AgcmSkillStream.cpp`). Das Paketformat steht im Bericht [AgpmSkill](AgpmSkill.md), die Oberfläche in [AgcmUISkill2](AgcmUISkill2.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 83 von 141 Quellmethoden sind zugeordnet; die Rückrufe in `OnAddModule` und die Stream-Funktionen waren schon benannt, neu sind Rasterfelder, Warteschlange, Wirk-Verarbeitung und Hilfsfunktionen.
- **OnAddModule:** gleiche 11 Module und gleiche Reihenfolge der Rückrufe wie die Quelle; Mastery-Rückrufe sind in der Quelle auskommentiert und fehlen im Binary.
- **Warteschlange:** höchstens vier Wirker je Ziel (`AddCastQueue`), Standard-Wirkzeit 1400 ms.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmSkill.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0066D9E0` | 1250 | vtable/String |
| 1 | `OnInit` | `0x0066FF20` | 1321 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 3 | `GetADSkillTemplate` | `0x00669830` | 27 | von Hand geprüft |
| 4 | `GetADSpecializeTemplate` | `0x00669850` | 27 | von Hand geprüft |
| 5 | `SetSelectedBase` | `0x00669870` | 65 | von Hand geprüft |
| 6 | `SetSelectedPos` | `0x006698C0` | 61 | von Hand geprüft |
| 7 | `CBReceiveAction` | `0x0066CFD0` | 335 | Callback-Registrierung |
| 8 | `ProcessReceiveCastSkill` | `0x0066C770` | 1679 | von Hand geprüft |
| 9 | `CBActionSkillResult` | `0x0066B5C0` | 1204 | Callback-Registrierung |
| 10 | `CBActionProductSkill` | `0x0066CE10` | 73 | Callback-Registrierung |
| 11 | `CBAdditionalEffect` | `0x00669900` | 134 | Callback-Registrierung |
| 12 | `CBCheckNowUpdateActionFactor` | `0x00669990` | 73 | Callback-Registrierung |
| 13 | `GetMaxSkillPreserveTime` | `0x006699E0` | 94 | von Hand geprüft |
| 14 | `ProcessNoticeEffect` | `0x0066D170` | 120 | von Hand geprüft |
| 15 | `ProcessStartEffect` | `0x0067AC90` | 6 | gleiche Adresse wie `beginnt mit return TRUE (Rest toter Code)` (vom Linker zusammengefaltet) |
| 16 | `ProcessEndEffect` | `0x0066BA80` | 114 | von Hand geprüft |
| 17 | `ProcessSkillEffectIdleEvent` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `CastSkillTest` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `CastSkillTest` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `PreProcessSkill` | `0x00669A40` | 180 | von Hand geprüft |
| 21 | `CastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `CastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `CastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `CastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 25 | `CastSkill` | `0x0066DED0` | 43 | von Hand geprüft |
| 26 | `CastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `CastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `DebugSkill_Render` | `0x0066DF00` | 165 | von Hand geprüft |
| 29 | `CastSkillCheck` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `CastSkill` | `0x0066D1F0` | 1482 | von Hand geprüft |
| 31 | `GetCharacterAttachData` | `0x00669C70` | 41 | von Hand geprüft |
| 32 | `GetAttachTemplateData` | `0x00669CA0` | 48 | von Hand geprüft |
| 33 | `GetCharacterTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `ConAgcdSkillAttachData` | `0x00669CD0` | 77 | Callback-Registrierung |
| 35 | `DesAgcdSkillAttachData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 36 | `ConTemplateAttachData` | `0x00669D20` | 86 | Callback-Registrierung |
| 37 | `DesTemplateAttachData` | `0x0066BB00` | 570 | Callback-Registrierung |
| 38 | `ConAgcdSkill` | `0x0066BD40` | 65 | Callback-Registrierung |
| 39 | `DesAgcdSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 40 | `AttachedTemplateAnimationWrite` | `0x00669D80` | 481 | von Hand geprüft |
| 41 | `AttachedTemplateEffectWrite` | `0x00669F70` | 481 | von Hand geprüft |
| 42 | `AttachedTemplateEffectSoundWrite` | `0x0066A160` | 236 | von Hand geprüft |
| 43 | `CheckVisualInfo` | `0x0066BD90` | 221 | von Hand geprüft |
| 44 | `ParseTemplateString` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 45 | `GetUsableSkillTNameIndex` | `0x0066BE90` | 145 | von Hand geprüft |
| 46 | `_CheckVisualInfo` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 47 | `GetUsableSkillTNameIndex` | `0x0066BF30` | 62 | von Hand geprüft |
| 48 | `SetSkillEffectData` | `0x0066BF70` | 427 | von Hand geprüft |
| 49 | `CBActionSkill` | `0x0066D7C0` | 75 | Callback-Registrierung |
| 50 | `SetCallbackNoAnimSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 51 | `SetCallbackMissCastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 52 | `SetCallbackCheckCastSkillResult` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 53 | `SetCallbackAddBuffedSkillList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 54 | `SetCallbackRemoveBuffedSkillList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 55 | `SetCallbackAddtionalHitEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 56 | `SetCallbackAddHpBar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 57 | `SetCallbackCastFailForTransform` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 58 | `SetCallbackCastFailForRide` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 59 | `SetCallbackPreProcessSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 60 | `SetCallbackGetRegisteredMPPotionTID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 61 | `SetCallbackBlockCastSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 62 | `SetCallbackStartGroundTargetSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 63 | `UpdateSkillPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 64 | `UpdateSkillPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 65 | `UpdateDIRTPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 66 | `UpdateDIRTPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 67 | `ConAgcdSkillTemplate` | `0x0066A2A0` | 71 | Callback-Registrierung |
| 68 | `DesAgcdSkillTemplate` | `0x0066A2F0` | 183 | Callback-Registrierung |
| 69 | `ConAgcdSkillSpecialize` | `0x0066A3B0` | 56 | Callback-Registrierung |
| 70 | `DesAgcdSkillSpecialize` | `0x0066A3F0` | 99 | Callback-Registrierung |
| 71 | `GetSkillRaster` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 72 | `GetSmallSkillRaster` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 73 | `GetSkillTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 74 | `GetSmallSkillTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 75 | `GetBuffSkillSmallTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 76 | `SetGridSkillAttachedTexture` | `0x0066A490` | 175 | von Hand geprüft |
| 77 | `SetGridSkillAttachedUnableTexture` | `0x0066A540` | 176 | von Hand geprüft |
| 78 | `SetGridSkillAttachedUnableTexture` | `0x0066A5F0` | 170 | von Hand geprüft |
| 79 | `SetGridSkillAttachedSmallTexture` | `0x0066A6A0` | 170 | von Hand geprüft |
| 80 | `SetGridSkillAttachedTexture` | `0x0066A750` | 169 | von Hand geprüft |
| 81 | `SetGridSpecializeAttachedTexture` | `0x0066A800` | 160 | von Hand geprüft |
| 82 | `GetSkillFactor` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 83 | `GetSkillTotalPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 84 | `CBUpdateSkillPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 85 | `CSUpdateSkillDIRT` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 86 | `CBLearnSkill` | `0x0066A8A0` | 314 | Callback-Registrierung |
| 87 | `CBForgetSkill` | `0x0066A9E0` | 93 | Callback-Registrierung |
| 88 | `CBSetSelfCharacter` | `0x0066C1B0` | 300 | Callback-Registrierung |
| 89 | `CBInitSkill` | `0x0066AA40` | 430 | Callback-Registrierung |
| 90 | `CBRemoveSkill` | `0x0066ABF0` | 149 | Callback-Registrierung |
| 91 | `CBInitSkillTemplate` | `0x00561430` | 23 | gleiche Adresse wie `gemeinsamer Rumpf (pData && pClass)` (vom Linker zusammengefaltet) |
| 92 | `CBInitSpecialize` | `0x0066AC90` | 26 | Callback-Registrierung |
| 93 | `CBAddBuffedSkillList` | `0x0066C2E0` | 187 | Callback-Registrierung |
| 94 | `CBRemoveBuffedSkillList` | `0x0066ACB0` | 42 | Callback-Registrierung |
| 95 | `CBUpdateSkill` | `0x0066ACE0` | 95 | von Hand geprüft |
| 96 | `CBUpdateSkillPoint` | `0x0066ACE0` | 95 | von Hand geprüft |
| 97 | `GetAgcdSkillTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 98 | `GetAgcdSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 99 | `SkillTest` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 100 | `EnumCallbackNoAnimSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 101 | `IsExistCastQueue` | `0x0066AD70` | 93 | von Hand geprüft |
| 102 | `AddCastQueue` | `0x0066ADD0` | 75 | von Hand geprüft |
| 103 | `RemoveCastQueue` | `0x0066AE20` | 138 | von Hand geprüft |
| 104 | `CBSkillStruckAnimation` | `0x0066AEB0` | 38 | Callback-Registrierung |
| 105 | `CBProcessSkillStruck` | `0x0066AEE0` | 38 | Callback-Registrierung |
| 106 | `SetIconTexturePath` | `0x0066AF10` | 33 | von Hand geprüft |
| 107 | `CBReservedActionSkill` | `0x0066D810` | 77 | Callback-Registrierung |
| 108 | `SetCallbackStartCastSelfCharacter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 109 | `AddIdleEventTwicePacketSkill` | `0x0066C3A0` | 87 | von Hand geprüft |
| 110 | `CBProcessTwicePacketSkill` | `0x0066AF40` | 133 | von Hand geprüft |
| 111 | `GetTwicePacketInteval` | `0x0066C400` | 201 | von Hand geprüft |
| 112 | `GetNumVisualInfo` | `0x0066AFD0` | 40 | von Hand geprüft |
| 113 | `CBLoadCharacterTemplate` | `0x0066B010` | 221 | Callback-Registrierung |
| 114 | `CBReleaseCharacterTemplate` | `0x0066B0F0` | 202 | Callback-Registrierung |
| 115 | `CBMoveActionSkill` | `0x0066B1C0` | 79 | Callback-Registrierung |
| 116 | `CBMoveActionRelease` | `0x0066B210` | 61 | Callback-Registrierung |
| 117 | `CBStopSelfCharacter` | `0x0066B250` | 37 | Callback-Registrierung |
| 118 | `SetCurrentSkill` | `0x0066B280` | 57 | von Hand geprüft |
| 119 | `SetCurrentSkillUsableIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 120 | `SendRequestRollback` | `0x0066B2C0` | 118 | von Hand geprüft |
| 121 | `CastGroundTargetSkill` | `0x0066D860` | 89 | von Hand geprüft |
| 122 | `ProcessAffectedTarget` | `0x0066C4D0` | 291 | von Hand geprüft |
| 123 | `ShowAffectedTargetCount` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 124 | `CBSkillStatusUpdate` | `0x0066B340` | 327 | von Hand geprüft |
| 125 | `CBMasteryResult` | – | | Registrierung in der Quelle auskommentiert, nicht im Binary |
| 126 | `SendMasterySkillSelect` | – | | Aufrufer ist auskommentiert, nicht im Binary gefunden |
| 127 | `SendAddSPToMastery` | – | | Aufrufer ist auskommentiert, nicht im Binary gefunden |
| 128 | `SendSubSPFromMastery` | – | | Aufrufer ist auskommentiert, nicht im Binary gefunden |
| 129 | `StreamReadTemplateSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 130 | `StreamWriteTemplateSkill` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 131 | `StreamReadTemplateSkillSound` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 132 | `StreamWriteTemplateSkillSound` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 133 | `AttachedTemplateReadCB` | `0x0062C110` | 2642 | Callback-Registrierung |
| 134 | `AttachedTemplateWriteCB` | `0x0062CB70` | 455 | Callback-Registrierung |
| 135 | `AttachedSoundTemplateReadCB` | `0x0062CD40` | 580 | Callback-Registrierung |
| 136 | `AttachedSoundTemplateWriteCB` | `0x0062CF90` | 231 | Callback-Registrierung |
| 137 | `AgcdSkillTemplateReadCB` | `0x0062D080` | 768 | Callback-Registrierung |
| 138 | `AgcdSkillTemplateWriteCB` | `0x0062D380` | 198 | Callback-Registrierung |
| 139 | `AgcdSkillSpecializeReadCB` | `0x0062D450` | 291 | Callback-Registrierung |
| 140 | `AgcdSkillSpecializeWriteCB` | `0x0062D580` | 67 | Callback-Registrierung |

85 von 141 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ToggleAffectedTargetCount` (`0x0063B250`), `DebugSkill_On` (`0x006697A0`), `DebugSkill_Off` (`0x006697B0`), `ctor_or_dtor_006697c0` (`0x006697C0`), `~AgcmSkill` (`0x0066B5A0`), `ctor_or_dtor_0066c600` (`0x0066C600`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xC7C` | `Zusatzdaten Wirk-Warteschlange (Zähler + bis zu 4 Wirker)` | `IsExistCastQueue`, `AddCastQueue` |
| `0xC7E` | `Index der Zusatzdaten der Charaktervorlage` | `GetUsableSkillTNameIndex`-Hilfe `0x0066A250` |
| `0xBB0` | `Zeiger auf `AgcmCharacter`` | `SendRequestRollback`, `CBSkillStatusUpdate`-Umfeld |

## Vtable und Quelldateien

Vtable bei `0x008C9F74`: Slot 0 Destruktor `0x0066B5A0`, 1 `OnAddModule` (`0x0066D9E0`), 2 `OnInit` (`0x0066FF20`, 1321 Byte), 3–5 gemeinsamer Rumpf `0x0067FAB0`, 6 und 7 `0x0067AC90`.
Die Klasse besteht aus `AgcmSkill.cpp` (125 Methoden), `AgcmSkillMastery.cpp` (4) und `AgcmSkillStream.cpp` (12); die Stream-Funktionen liegen bei `0x0062C110`–`0x0062D580`, der Rest bei `0x006697C0`–`0x0066FF20`.

## OnAddModule (0x0066D9E0)

Holt 11 Module wie die Quelle: [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md), [`AgpmSkill`](AgpmSkill.md), [`ApmEventManager`](ApmEventManager.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmPvP`](AgpmPvP.md), `AgcmCharacter`, [`AgpmFactors`](AgpmFactors.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmResourceLoader`](AgcmResourceLoader.md) und [`AgpmOptimizedPacket2`](AgpmOptimizedPacket2.md). Die Rückrufe werden in der Reihenfolge der Quelle angemeldet:

| Anmeldung | Rückruf | Adresse |
|---|---|---|
| `AgpmSkill`: Aktion empfangen | `CBReceiveAction` | `0x0066CFD0` |
| `AgpmSkill`: Aktionsergebnis | `CBActionSkillResult` | `0x0066B5C0` |
| `AgpmSkill`: Aktionsfaktor aktuell? | `CBCheckNowUpdateActionFactor` | `0x00669990` |
| `AgpmCharacter`: Fertigkeitsaktion | `CBActionSkill` | `0x0066D7C0` |
| `AgpmCharacter`: Produktions-Fertigkeit | `CBActionProductSkill` | `0x0066CE10` |
| Fertigkeit gelernt / vergessen | `CBLearnSkill` / `CBForgetSkill` | `0x0066A8A0` / `0x0066A9E0` |
| Fertigkeit angelegt / entfernt | `CBInitSkill` / `CBRemoveSkill` | `0x0066AA40` / `0x0066ABF0` |
| Fertigkeitsvorlage angelegt | `CBInitSkillTemplate` | gemeinsamer Rumpf `0x00561430` |
| Spezialisierung angelegt | `CBInitSpecialize` | `0x0066AC90` |
| Fertigkeit / Punkte aktualisiert | `CBUpdateSkill` / `CBUpdateSkillPoint` | beide `0x0066ACE0` |
| Buff-Liste ergänzt / entfernt | `CBAddBuffedSkillList` / `CBRemoveBuffedSkillList` | `0x0066C2E0` / `0x0066ACB0` |
| Zusatzeffekt empfangen | `CBAdditionalEffect` | `0x00669900` |
| `AgcmCharacter`: eigener Charakter gesetzt | `CBSetSelfCharacter` | `0x0066C1B0` |
| Fertigkeits-Treffer-Animation / -Verarbeitung | `CBSkillStruckAnimation` / `CBProcessSkillStruck` | `0x0066AEB0` / `0x0066AEE0` |
| vorgemerkte Fertigkeitsaktion | `CBReservedActionSkill` | `0x0066D810` |
| Charaktervorlage geladen / freigegeben | `CBLoadCharacterTemplate` / `CBReleaseCharacterTemplate` | `0x0066B010` / `0x0066B0F0` |
| eigener Charakter stoppt | `CBStopSelfCharacter` | `0x0066B250` |
| `AgpmOptimizedPacket2`: Bewegungs-Fertigkeit | `CBMoveActionSkill` / `CBMoveActionRelease` | `0x0066B1C0` / `0x0066B210` |

Die in der Quelle auskommentierten Mastery-Rückrufe (`CBMasterySpecialize`, `CBMasteryRollbackResult`, `CBAddSPToMasteryResult`, `CBMasteryNodeUpdate` u. a.) werden auch im Binary nicht angemeldet; dementsprechend sind `CBMasteryResult` und die drei `SendMastery…`-Funktionen dort nicht zu finden.

## OnInit (0x0066FF20)

`OnInit` registriert die AngelScript-Klasse `AgcmSkill` (u. a. `DebugSkill_On`, `DebugSkill_Off`, `ToggleAffectedTargetCount`; Zeichenketten [`AgcmUIConsole`](AgcmUIConsole.md), `AgcmSkill`) und meldet bei [`ApmMap`](ApmMap.md) die drei Debug-Rückrufe für die Monsterliste an; zuletzt hängt es `CBSkillStatusUpdate` an `AgpmCharacter` (Sonderstatus aktualisiert).

## Fertigkeit wirken (CastSkill, ProcessReceiveCastSkill)

`CastSkill` mit Ziel und Ziel-Position (`0x0066D1F0`, 1482 Byte, Zeichenkette `ApmMap`) ist die große Überladung der Quelle; sie wird von `CBActionSkill`, `CBReservedActionSkill`, `0x0066D860` und `0x0066DED0` gerufen. Die dünne Überladung `CastSkill(lSkillID, lTargetCID, bForce)` (`0x0066DED0`) wird von [`AgcmUIMain`](AgcmUIMain.md):ProcessSkill` genutzt. `PreProcessSkill` (`0x00669A40`) entscheidet vor dem Wirken, ob eine automatische Angriffs-Fertigkeit direkt als Angriff gewertet wird (Ziel sperren, Angriff) oder ob der Rückruf `PRE_PROCESS_SKILL` das Wirken verhindert.
`ProcessReceiveCastSkill` (`0x0066C770`, 1679 Byte) verarbeitet empfangene Aktionen und wird von `CBReceiveAction` und `CBActionProductSkill` gerufen; `ProcessEndEffect` (`0x0066BA80`) reiht den Wirker in die Warteschlange ein, wenn `ProcessActionQueue` noch nicht möglich ist. Die Warteschlange (`this+0xC7C`, höchstens vier Wirker je Ziel) wird von `IsExistCastQueue` (`0x0066AD70`), `AddCastQueue` (`0x0066ADD0`) und `RemoveCastQueue` (`0x0066AE20`) verwaltet.
`GetMaxSkillPreserveTime` (`0x006699E0`) liefert die Wirkzeit-Konstante der Fertigkeitsstufe, bei ungültiger ID/Stufe den Standardwert 1400 ms (`0x578`); `AddIdleEventTwicePacketSkill` (`0x0066C3A0`) und `GetTwicePacketInteval` (`0x0066C400`) steuern Fertigkeiten, die zwei Pakete senden. `SendRequestRollback` (`0x0066B2C0`) schickt die Rücksetz-Anfrage, `SetCurrentSkill` (`0x0066B280`) setzt die aktuelle Fertigkeit (aufgerufen von der Produktions- und Quest-Animation).

## Effekt-Verarbeitung

`ProcessNoticeEffect` (`0x0066D170`) ist der Effekt-Rückruf (wirkt nur bei Typ 3; Besitzer, Ziel, Fertigkeit); er ruft `ProcessEndEffect` (`0x0066BA80`) und, wenn die Fertigkeit Daten hat, `ProcessAffectedTarget` (`0x0066C4D0`, 291 Byte), das die betroffenen Ziele der Fertigkeit am eigenen Charakter einträgt. `ProcessStartEffect` beginnt in der Quelle mit `return TRUE;`; der Rest ist toter Code, daher teilt sich die Funktion im Binary vermutlich den `return TRUE`-Rumpf `0x0067AC90` (nicht beweisbar, da der Rumpf identisch ist).
`CastGroundTargetSkill` (`0x0066D860`) holt die vorgemerkte Bodenziel-Fertigkeit (`this+0xE60`), wirkt sie über `CastSkill` mit der Position und setzt die ID zurück. `CBProcessTwicePacketSkill` (`0x0066AF40`) ist der Idle-Rückruf, der das zweite Paket der Doppelpaket-Fertigkeit sendet. `CBSkillStatusUpdate` (`0x0066B340`) reagiert auf Sonderstatus-Änderungen (Module [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmItem`](AgcmItem.md): Blind-Ausrüstungsplatz ausblenden, `AgcmItem::OnAttachPart`/`OnDetachPart`).
`GetNumVisualInfo` (`0x0066AFD0`) liefert je nach Rasse 5 oder 0x82 Einträge; `CheckVisualInfo` (`0x0066BD90`) legt die Tabelle an, `SetSkillEffectData` (`0x0066BF70`, Format `%d:%d:%d:%d:%f:%f:%f:%f:%d:%d`) liest einen Effekt-Eintrag aus dem Stream.

## Rasterfelder und Symbole

Die sechs Rasterfeld-Funktionen liegen in Quellreihenfolge hintereinander und rufen alle `GetAttachGridItemTextureData`, `SetTexturePath` und `RwTextureRead`: `SetGridSkillAttachedTexture(AgpdSkill*)` (`0x0066A490`, von `CBInitSkill`), `SetGridSkillAttachedUnableTexture` für Fertigkeit und Vorlage (`0x0066A540`, `0x0066A5F0`), `…SmallTexture` (`0x0066A6A0`, von Buff-Anzeige und Ziel-Fenster), `SetGridSkillAttachedTexture(Vorlage)` (`0x0066A750`, von `CBSetSelfCharacter`) und `SetGridSpecializeAttachedTexture` (`0x0066A800`, von `CBInitSpecialize`).

## Streams

Die Schreib-Funktionen für Animation, Effekt und Effekt-Ton liegen bei `0x00669D80` (Zeichenketten `SKILL_ANIMATION_NAME`, `%s%d%d`, `%d:%d:%s`), `0x00669F70` (`SKILL_EFFECT_CONDITION`) und `0x0066A160` (`SKILL_EFFECT_SOUND`); die Rückrufe der `AgcmSkillStream.cpp` sind bereits über Vtable-/Zeichenketten-Zuordnung benannt (`AttachedTemplateReadCB` `0x0062C110`, `…WriteCB` `0x0062CB70`, Ton `0x0062CD40`/`0x0062CF90`, Vorlage `0x0062D080`/`0x0062D380`, Spezialisierung `0x0062D450`/`0x0062D580`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, `OnInit`, Warteschlange, Wirkzeit).

## Grenzen

- `ProcessReceiveCastSkill` (1679 Byte) und `CastSkill` (1482 Byte) wurden über Größe, Zeichenketten (`ApmMap`) und Aufrufer zugeordnet, nicht Zeile für Zeile verglichen; welche der dünnen `CastSkill`-Überladungen bei `0x0066D860` liegt, ist offen.
- Die Zuordnung der Rasterfeld-Funktionen und der Warteschlange stützt sich auf Quellreihenfolge, Aufrufer und die gelesenen Dekompilate.
- `ProcessNoticeEffect`, `ProcessAffectedTarget`, `CBSkillStatusUpdate`, `SetSkillEffectData` und `CheckVisualInfo` sind über Aufrufgraph, Zeichenketten und Signatur zugeordnet, nicht Zeile für Zeile verglichen; `ProcessStartEffect` ist nur als vermutlicher Stub eingetragen.
- Nicht gefunden: `ProcessSkillEffectIdleEvent`, `CastSkillCheck`, `CastSkillTest`, `SkillTest` (vermutlich Testcode), `ShowAffectedTargetCount` (die Zeichenkette `Affected count` fehlt im Binary), `GetSkillFactor`, `GetSkillTotalPoint`, `UpdateSkillPoint`/`UpdateDIRTPoint` und die `SetCallback…`-Einzeiler.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 11, gemeinsamer Rumpf: 15, nicht im Client: 13, ohne Kandidat: 13, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetAgcdSkill` | 5 | `0x0066AD40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBuffSkillSmallTexture` | 20 | `0x0066C120` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmItem`](AgcmItem.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIConsole`](AgcmUIConsole.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUISkill2`](AgcmUISkill2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgpmOptimizedPacket2`](AgpmOptimizedPacket2.md), [`AgpmPvP`](AgpmPvP.md), [`AgpmSkill`](AgpmSkill.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmProductMed`](AgcmProductMed.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIEventItemRepair`](AgcmUIEventItemRepair.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIQuest2`](AgcmUIQuest2.md)
