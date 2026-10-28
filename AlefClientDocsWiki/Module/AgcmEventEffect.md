# AgcmEventEffect (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmEventEffect` (Ereignis-Effekte für Charaktere, Gegenstände und Objekte: Animationen, Töne, Dauer-Effekte, Himmel) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten und Registrierungsreihenfolge, EP8-Quelle `Modules/AClient/AgcmEventEffect/` (`AgcmEventEffect.cpp`, `AgcmEventEffectStream.cpp`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Die Ereignis-Rückrufe sind jetzt fast vollständig zugeordnet (Zahl oben in der Karte); auch die Spirit-Stone-/Konvertierungs-Effekte, die Ton-Hilfen, die Check-Zeit-Zuordnung und die Anim-Stream-Funktionen sind jetzt zugeordnet (142 von 185); offen sind nur dünne Weiterleitungen, die Ausschluss-Effekt-Funktionen und zwei `Notice…CB`.
- **OnAddModule:** gleiche 18 Module wie die Quelle; die Anmeldereihenfolge im Binary weicht von der Quellreihenfolge ab, die Zusatzdaten-Größen (`0x18`, `0x1C`, 4, `0x10`) stimmen.
- **Zuordnungsmethode:** Inhalt der Rückrufe (Status-Bits, `switch`-Werte, Konstante 3633, Flag `NO_UNEQUIP`) und Mehrfach-Anmeldungen statt der Setter-Adresse.
- **Nicht angemeldet:** `EventCharCreate`, `EventCharDamageCB` und die `EventSkill…`-Stubs fehlen im Binary bzw. werden nirgends registriert.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventEffect.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x005CEC10` | 168 | vtable/String |
| 1 | `OnAddModule` | `0x005CF080` | 1510 | vtable/String |
| 2 | `OnIdle` | `0x005C5890` | 18 | gleiche Adresse wie `eigener Rumpf (leer)` (vom Linker zusammengefaltet) |
| 3 | `OnDestroy` | `0x005C58B0` | 17 | vtable/String |
| 4 | `SetStandardEffectUseInfo` | `0x005C5950` | 972 | von Hand geprüft |
| 5 | `SetBaseEffectUseInfo` | `0x005C5D20` | 524 | von Hand geprüft |
| 6 | `CheckCustomData` | `0x005CD2C0` | 1239 | von Hand geprüft |
| 7 | `StartEffect` | `0x005CD7C0` | 566 | von Hand geprüft |
| 8 | `StartEventEffect` | `0x005C7E70` | 564 | von Hand geprüft |
| 9 | `EventInitCB` | `0x005CECC0` | 867 | von Hand geprüft |
| 10 | `SetBaseEffectParams` | `0x005C5F30` | 89 | von Hand geprüft |
| 11 | `SetBaseEffectParams` | `0x005C5F90` | 223 | von Hand geprüft |
| 12 | `SetBaseEffectParams` | `0x005C6070` | 139 | von Hand geprüft |
| 13 | `SetBaseEffect` | `0x005CDA00` | 351 | von Hand geprüft |
| 14 | `SetBaseObjectEventEffect` | `0x005C80B0` | 277 | von Hand geprüft |
| 15 | `SetCommonCharacterEffect` | `0x005CE230` | 22 | von Hand geprüft |
| 16 | `RemoveCommonCharacterEffect` | `0x005CB950` | 515 | von Hand geprüft |
| 17 | `SetBaseCharacterEventEffect` | `0x005C9700` | 98 | von Hand geprüft |
| 18 | `SetBaseCharacterEventEffect` | `0x005C9540` | 441 | von Hand geprüft |
| 19 | `SetBaseEquipItemEventEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `SetBaseEquipItemEventEffect` | `0x005C81D0` | 353 | von Hand geprüft |
| 21 | `SetBaseUsableItemEventEffect` | `0x005C8340` | 284 | von Hand geprüft |
| 22 | `CBCheckSkipSkillEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `SetBaseCustomEventEffect` | `0x005C6130` | 182 | von Hand geprüft |
| 24 | `SetBaseSkillEventEffect` | `0x005C9770` | 1036 | von Hand geprüft |
| 25 | `SetPassiveSkill` | `0x005C9B80` | 335 | von Hand geprüft |
| 26 | `RemoveAllConvertedItemGradeEventEffect` | `0x005C61F0` | 130 | Aufrufgraph (geprüft) |
| 27 | `RemoveAllContinuativeSkillEventEffect` | `0x005C8460` | 56 | von Hand geprüft |
| 28 | `RemoveContinuativetSkillEventEffect` | `0x005C6280` | 180 | von Hand geprüft |
| 29 | `EventObjectWorkCB` | `0x005C84A0` | 28 | von Hand geprüft |
| 30 | `EventObjectCheckHourCB` | `0x005CE250` | 57 | von Hand geprüft |
| 31 | `EventCharAnimCB` | `0x005CBB60` | 237 | von Hand geprüft |
| 32 | `EventCharAnimWaitCB` | `0x005CB110` | 232 | von Hand geprüft |
| 33 | `EventCharAnimWalkCB` | `0x005C9CD0` | 76 | von Hand geprüft |
| 34 | `EventCharAnimRunCB` | `0x005C9D20` | 229 | von Hand geprüft |
| 35 | `GetSkillUseEffectSet` | `0x005C6340` | 118 | Aufrufgraph (geprüft) |
| 36 | `SetBuffedAttackEffect` | `0x005C84C0` | 484 | von Hand geprüft |
| 37 | `SetOnlySoundSkill` | `0x005C86B0` | 150 | Aufrufgraph (geprüft) |
| 38 | `EventCharAnimAttackCB` | `0x005C9E10` | 982 | von Hand geprüft |
| 39 | `SetCharTargetStruck` | `0x005C8750` | 355 | Aufrufgraph (geprüft) |
| 40 | `EventCharAttackSuccessCB` | `0x005CF030` | 71 | von Hand geprüft |
| 41 | `EventCharAnimSocialCB` | `0x005CDB60` | 58 | von Hand geprüft |
| 42 | `GetSpiritStoneInfo` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `GetSpiritStoneHitEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 44 | `SetTargetStruckEffect` | `0x005CE290` | 697 | Zeichenkette |
| 45 | `EventCharLevelUPCB` | `0x005CE550` | 46 | von Hand geprüft |
| 46 | `EventCharCreate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 47 | `SetActionResultSkill` | `0x005CA1F0` | 162 | von Hand geprüft |
| 48 | `EventCharActionResult` | `0x005CE580` | 186 | von Hand geprüft |
| 49 | `EventCharUpdateMovemenntCB` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (mit Element::GetSize angemeldet)` (vom Linker zusammengefaltet) |
| 50 | `EventCharSpecialStatus` | `0x005CE670` | 388 | von Hand geprüft |
| 51 | `EventCharAdditionalEffect` | `0x005CE800` | 247 | von Hand geprüft |
| 52 | `CharaterEquipEffectRemove` | `0x005CCBF0` | 73 | Aufrufgraph (geprüft) |
| 53 | `CharaterEquipEffectUpdate` | `0x005C64D0` | 83 | von Hand geprüft |
| 54 | `EventCharEndSocialAnimCB` | `0x005CD010` | 37 | von Hand geprüft |
| 55 | `EventCharTransform` | `0x005CE920` | 30 | von Hand geprüft |
| 56 | `EventCharUpdateActionStatus` | `0x005CE940` | 58 | von Hand geprüft |
| 57 | `EventCharAnimDeadCB` | `0x005CB200` | 56 | von Hand geprüft |
| 58 | `EventCharDamageCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 59 | `EventItemEquipCB` | `0x005CD040` | 190 | von Hand geprüft |
| 60 | `EventItemDetachedCB` | `0x005CA2A0` | 112 | von Hand geprüft |
| 61 | `EventItemUnequipCB` | `0x005CCC40` | 77 | von Hand geprüft |
| 62 | `EventItemUseCB` | `0x005C88C0` | 40 | von Hand geprüft |
| 63 | `EventSkillCB` | `0x005CA310` | 26 | von Hand geprüft |
| 64 | `EventSkillAdditionalEffectCB` | `0x005CC790` | 62 | von Hand geprüft |
| 65 | `CharacterSetSelfCB` | `0x005C6530` | 51 | von Hand geprüft |
| 66 | `AttachedDataEffectListConstructCB` | `0x005C88F0` | 32 | von Hand geprüft |
| 67 | `AttachedDataEffectListDestructCB` | `0x005C8910` | 32 | von Hand geprüft |
| 68 | `AttachedDataObjUseEffectSetConstructCB` | `0x005C8930` | 50 | von Hand geprüft |
| 69 | `AttachedDataCharUseEffectSetConstructCB` | `0x005C8970` | 50 | von Hand geprüft |
| 70 | `AttachedDataItemUseEffectSetConstructCB` | `0x005C89B0` | 50 | von Hand geprüft |
| 71 | `AttachedDataUseEffectSetDestructCB` | `0x005C89F0` | 52 | von Hand geprüft |
| 72 | `GetEventEffectList` | `0x005C6570` | 99 | von Hand geprüft |
| 73 | `GetUseEffectSet` | `0x005C65E0` | 27 | von Hand geprüft |
| 74 | `GetUseEffectSet` | `0x005C6600` | 27 | von Hand geprüft |
| 75 | `GetUseEffectSet` | `0x005C6620` | 27 | von Hand geprüft |
| 76 | `GetUseEffectSet` | `0x005C6640` | 95 | von Hand geprüft |
| 77 | `UseEffectSetStreamRead` | `0x005C66A0` | 1527 | von Hand geprüft |
| 78 | `UseEffectSetStreamWrite` | `0x005C6CA0` | 692 | von Hand geprüft |
| 79 | `RemoveEquipmentsEffect` | `0x005C6F60` | 106 | Aufrufgraph (geprüft) |
| 80 | `PlaySocialSound` | `0x005C8A30` | 144 | Aufrufgraph (geprüft) |
| 81 | `RemoveAllEffect` | `0x005CC7F0` | 554 | Zeichenkette |
| 82 | `PreRemoveCharacterCB` | `0x005C6FD0` | 55 | von Hand geprüft |
| 83 | `PreStop3DSound` | `0x005C7010` | 144 | von Hand geprüft |
| 84 | `RemoveCommonObjectCB` | `0x005CCA20` | 29 | von Hand geprüft |
| 85 | `RemoveEffectCB` | `0x005CCA40` | 312 | von Hand geprüft |
| 86 | `SetSoundDataNum` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 87 | `ReadMovingSoundData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 88 | `ReadConvertedItemGradeEffectData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 89 | `ReadConvertedArmourAttrEffectData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 90 | `ReadSpiritStoneHitEffectData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 91 | `ReadSpiritStoneAttrEffectData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 92 | `ReadCommonCharEffectData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 93 | `ReadSocialAnimationData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 94 | `SetAttrDamageEffect` | `0x005CDBA0` | 620 | von Hand geprüft |
| 95 | `SetAttrDamageEffect` | `0x005CDE10` | 500 | von Hand geprüft |
| 96 | `SetSpiritStoneHitEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 97 | `SetConvertedItemGradeEffect` | `0x005C8AC0` | 100 | Aufrufgraph (geprüft) |
| 98 | `StopConvertedWeaponGradeEventEffect` | `0x005C8B30` | 82 | Aufrufgraph (geprüft) |
| 99 | `StartConvertedWeaponGradeEventEffect` | `0x005C8B90` | 83 | Aufrufgraph (geprüft) |
| 100 | `SetConvertedItemEffect` | `0x005CCC90` | 154 | von Hand geprüft |
| 101 | `ReleaseConvertedItemEffect` | `0x005CA330` | 61 | von Hand geprüft |
| 102 | `ResetConvertedItemEffect` | `0x005CCD30` | 71 | Aufrufgraph (geprüft) |
| 103 | `StartConvertedWeaponAttrEventEffect` | `0x005CCB80` | 97 | Aufrufgraph (geprüft) |
| 104 | `StopConvertedWeaponAttrEventEffect` | `0x005C8BF0` | 95 | Aufrufgraph (geprüft) |
| 105 | `ReleaseConvertedArmourAttrEffectCB` | `0x005C7290` | 75 | Aufrufgraph (geprüft) |
| 106 | `SetConvertedArmourEffectData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 107 | `SetConvertedArmourAttrEffectCB` | `0x005C72E0` | 90 | Aufrufgraph (geprüft) |
| 108 | `GetMaxSpiritStoneType` | `0x005C8C50` | 590 | Aufrufgraph (geprüft) |
| 109 | `GetConvertedArmourEffectMaterial` | `0x005C8EA0` | 81 | Aufrufgraph (geprüft) |
| 110 | `SetConvertedArmourAttrEventEffect` | `0x005C8F00` | 90 | Aufrufgraph (geprüft) |
| 111 | `StartConvertedArmourAttrEventEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 112 | `StopConvertedArmourAttrEventEffect` | `0x005C7340` | 79 | Aufrufgraph (geprüft) |
| 113 | `UpdateConvertedItemEventEffect` | `0x005CCD80` | 77 | von Hand geprüft |
| 114 | `EventItemUpdateConvertHistoryCB` | `0x005CCDD0` | 26 | von Hand geprüft |
| 115 | `AttachedDataEventEffectDataConstructCB` | `0x005C8F60` | 92 | von Hand geprüft |
| 116 | `AttachedDataEventEffectDataDestructCB` | `0x005C8FC0` | 49 | von Hand geprüft |
| 117 | `GetEventEffectData` | `0x005C7390` | 71 | von Hand geprüft |
| 118 | `EventItemSpiritStoneAttrCB` | `0x005C9000` | 241 | Aufrufgraph (geprüft) |
| 119 | `NoticeEffectSetTargetStruckAnimCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 120 | `EventWaveFxTrigger` | `0x005C7450` | 41 | von Hand geprüft |
| 121 | `GetSkySetFlagData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 122 | `CBSkyChange` | `0x005C9100` | 27 | Callback-Registrierung |
| 123 | `UpdateNatureStatus` | `0x005C7480` | 129 | von Hand geprüft |
| 124 | `NoticeEffectDestroyMatchCB` | `0x005C9120` | 490 | von Hand geprüft |
| 125 | `NoticeEffectSkillDestroyMatchCB` | `0x005CBC50` | 832 | von Hand geprüft |
| 126 | `NoticeEffectHitEffectCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 127 | `GetWeaponType` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 128 | `PlaySound` | `0x005C7550` | 304 | von Hand geprüft |
| 129 | `PlayHitSound` | `0x005CBF90` | 295 | Aufrufgraph (geprüft) |
| 130 | `PlayAttackSound` | `0x005C7680` | 142 | Aufrufgraph (geprüft) |
| 131 | `PlayAnimLoopSound` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 132 | `PlayCharacterMovingSound` | `0x005C9310` | 384 | von Hand geprüft |
| 133 | `AnimSoundCB` | `0x005C7710` | 71 | Aufrufgraph (geprüft) |
| 134 | `AddCustData` | `0x005C7760` | 449 | von Hand geprüft |
| 135 | `GetCustDataIndex` | `0x005C7930` | 143 | von Hand geprüft |
| 136 | `GetCustDataIndex` | `0x005C7A00` | 255 | von Hand geprüft |
| 137 | `GetCustDataIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 138 | `EventSkillChargeThirdAttackCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 139 | `EventSkillConsumeThirdAttackCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 140 | `EventSkillEvationCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 141 | `EventSkillDamageReflectionCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 142 | `EventSkillChangeVelocityCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 143 | `EventSkillAbsorbDamageCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 144 | `EventSkillAddBuffedListCB` | `0x005CA370` | 591 | von Hand geprüft |
| 145 | `EventSkillAddPreengagedPassiveSkillEffect` | `0x005CA5C0` | 419 | von Hand geprüft |
| 146 | `EventSkillRemoveBuffedListCB` | `0x005C7B00` | 60 | von Hand geprüft |
| 147 | `CBRemoveAnimation` | `0x005CC760` | 35 | Callback-Registrierung |
| 148 | `StreamWriteCharacterAnimationAttachedData` | `0x005CC0C0` | 605 | Aufrufgraph (geprüft) |
| 149 | `StreamReadCharacterAnimationAttachedData` | `0x005CC320` | 685 | Aufrufgraph (geprüft) |
| 150 | `CBStreamReadCharacterAnimationAttachedData` | `0x005CC5D0` | 20 | Aufrufgraph (geprüft) |
| 151 | `GetCheckTimeDataList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 152 | `RemoveAllCheckTimeData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 153 | `ReleaseCheckTimeDataList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 154 | `AddEffectSet` | `0x005CE010` | 108 | von Hand geprüft |
| 155 | `RemoveEffectSet` | `0x005C7B40` | 216 | von Hand geprüft |
| 156 | `RemoveCheckTimeDataList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 157 | `AddCheckTimeData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 158 | `SetCheckTimeDataList` | `0x005C7C20` | 367 | von Hand geprüft |
| 159 | `SetStatus` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 160 | `SetCommonCharEffect` | `0x005CE080` | 431 | von Hand geprüft |
| 161 | `StartSelectionAnimation` | `0x005C7DA0` | 195 | von Hand geprüft |
| 162 | `StartSocialAnimation` | `0x005CB240` | 474 | von Hand geprüft |
| 163 | `HideShieldAndWeaponsWhileCurrentAnimationDuration` | `0x005CD100` | 442 | von Hand geprüft |
| 164 | `AttachShieldAndWeapons` | `0x005CCDF0` | 410 | von Hand geprüft |
| 165 | `AttachShieldAndWeapons` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 166 | `AttachShieldAndWeapons` | `0x005CCF90` | 68 | von Hand geprüft |
| 167 | `CBAttachShieldAndWeapons` | `0x005CCFE0` | 38 | von Hand geprüft |
| 168 | `CopyCharAnimAttachedData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 169 | `CBCharUseEffect` | `0x005CE980` | 453 | von Hand geprüft |
| 170 | `CBRestoreCommonEffectsByEvolution` | `0x005CEB70` | 146 | Callback-Registrierung |
| 171 | `SaveCurrentEffectEvolution` | `0x005CC5F0` | 35 | von Hand geprüft |
| 172 | `RemoveCurrentEffectEvolution` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 173 | `StreamReadTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 174 | `StreamWriteTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 175 | `CharTemplateStreamReadCB` | `0x00608380` | 47 | von Hand geprüft |
| 176 | `CharTemplateStreamWriteCB` | `0x006083B0` | 59 | von Hand geprüft |
| 177 | `ObjTemplateStreamReadCB` | `0x006083F0` | 42 | von Hand geprüft |
| 178 | `ObjTemplateStreamWriteCB` | `0x00608420` | 38 | von Hand geprüft |
| 179 | `ItemTemplateStreamReadCB` | `0x00608450` | 42 | von Hand geprüft |
| 180 | `ItemTemplateStreamWriteCB` | `0x00608480` | 38 | von Hand geprüft |
| 181 | `StreamReadExclusiveEffectMappingTable` | `0x00608980` | 650 | vtable/String |
| 182 | `CheckExclusiveEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 183 | `IsExclusiveEffect` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 184 | `ClearExclusiveEffectInfoPerFrame` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

142 von 185 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_005cb5d0` (`0x005CB5D0`), `ctor_or_dtor_005cb7d0` (`0x005CB7D0`), `~AgcmEventEffect` (`0x005CB930`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1E0A` | `Index der Objektvorlagen-Zusatzdaten` | `AttachedDataObjUseEffectSetConstructCB` |

## Vtable und Quelldateien

Vtable bei `0x008BBFAC`: Slot 0 Destruktor `0x005CB930`, 1 `OnAddModule` (`0x005CF080`, 1510 Byte), 2 `OnInit` (`0x005CEC10`), 3 `OnIdle` (`0x005C5890`), 4/5 gemeinsamer Rumpf `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x005C58B0`, ruft `0x00608D10`).
Die Klasse `AgcmEventEffect` besteht in der Quelle aus `AgcmEventEffect.cpp` (173 Methoden) und `AgcmEventEffectStream.cpp` (12); die Stream-Funktionen liegen bei `0x00608380`–`0x00608980`, der Rest bei `0x005C5890`–`0x005CF080`. Die Hilfsklassen `AgcmEventEffectData`, `AgcmEventEffectList`, `AgcaEventEffectData`, `AgcaEffectSet` und `AgcuEventEffect` sind eigene Klassen und nicht Teil dieses Berichts. Das Modul ist stark in sich verzahnt; viele kleine Rückrufe sind zusammengefaltet oder eingebaut.

## OnInit und OnAddModule

`OnInit` (`0x005CEC10`) legt die Zeichenkette `AGCD_EVENT_EFFECT` an, holt [`AgcmEventNature`](AgcmEventNature.md) und meldet zwei Rückrufe an (Setter `0x00503160`, `0x00503180`).
`OnAddModule` holt 18 Module wie die Quelle: [`AgcmSound`](AgcmSound.md), [`ApmMap`](ApmMap.md), [`AgpmFactors`](AgpmFactors.md), [`ApmEventManager`](ApmEventManager.md), [`AgpmTimer`](AgpmTimer.md), [`ApmObject`](ApmObject.md), [`AgcmObject`](AgcmObject.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgpmItem`](AgpmItem.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgcmItem`](AgcmItem.md), [`AgpmSkill`](AgpmSkill.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md) und [`AgpmArchlord`](AgpmArchlord.md).
Zusatzdaten (Attach): Charakter `0x18` Byte (Konstruktor `0x005C8F60`, Destruktor `0x005C8FC0`), Effektliste 4 Byte (`0x005C88F0`/`0x005C8910`), Himmel-Flag 4 Byte ohne Rückruf, Charaktervorlage `0x10` Byte (`0x005C8970`/`0x005C89F0`); Gegenstand `0x1C` Byte (gleiche Rückrufe wie Charakter), Effektliste, Gegenstandsvorlage (`0x005C89B0`); Objekt: Effektliste und Objektvorlage (`0x005C8930`). Drei Stream-Paare: Charaktervorlage (`0x00608380`/`0x006083B0`), Gegenstandsvorlage (`0x00608450`/`0x00608480`) und Objektvorlage (`0x006083F0`/`0x00608420`); das gemeinsame Lesen/Schreiben der Effektdaten sind `UseEffectSetStreamRead` (`0x005C66A0`, 1527 Byte, Zeichenketten `AGCMEVENTEFFECT_CONDITION_FLAGS`, `%d:%d`) und `…Write` (`0x005C6CA0`). Reihenfolge der Anmeldungen und Größen entsprechen der Quelle.

## Rückrufe (zugeordnet)

Die Ereignis-Rückrufe wurden diesmal nicht über die Setter-Adresse, sondern über den Inhalt zugeordnet (Fallunterscheidungen, Flag-Bits, Konstanten, Aufrufe), und die Mehrfach-Anmeldungen als Gegenprobe benutzt (`EventInitCB` und `RemoveCommonObjectCB` je dreimal, `EventSkillCB` und `EventItemUpdateConvertHistoryCB` je zweimal).

| Rückruf | Adresse | Beleg |
|---|---|---|
| `EventInitCB` | `0x005CECC0` | dreifach angemeldet (Objekt, Charakter, Boden-Gegenstand), 867 Byte |
| `EventObjectWorkCB` / `EventObjectCheckHourCB` | `0x005C84A0` / `0x005CE250` | zweiter nutzt die Stunden-Tabellen `this+0x1E24` (Ein) und `+0x1E84` (Aus) mit `AddEffectSet`/`RemoveEffectSet` |
| `PreRemoveCharacterCB` / `CharacterSetSelfCB` | `0x005C6FD0` / `0x005C6530` | Anmeldereihenfolge |
| `RemoveCommonObjectCB` | `0x005CCA20` | dreifach angemeldet, ruft `RemoveAllEffect` |
| `RemoveEffectCB` | `0x005CCA40` | Anmeldung bei `AgcmEff2` |
| `EventCharAnimCB` | `0x005CBB60` | holt die angehängten Animationsdaten, spielt Ton (`PlaySound`) |
| `EventCharAnimWaitCB` / `…WalkCB` / `…RunCB` | `0x005CB110` / `0x005C9CD0` / `0x005C9D20` | Warte-/Lauf-Animation; Walk und Run rufen `PlayCharacterMovingSound` (`0x005C9310`) |
| `EventCharAnimAttackCB` | `0x005C9E10` (982 Byte) | Angriffsanimation (155 Quellzeilen) |
| `EventCharAttackSuccessCB` | `0x005CF030` | ruft `SetTargetStruckEffect` |
| `EventCharAnimSocialCB` | `0x005CDB60` | prüft/löscht das Flag `AGCMCHAR_AF_NO_UNEQUIP` (Bit 4 bei `+0x74`) und ruft sonst `HideShieldAndWeaponsWhileCurrentAnimationDuration` (`0x005CD100`) |
| `EventCharEndSocialAnimCB` | `0x005CD010` | ruft `AttachShieldAndWeapons` (`0x005CCDF0`) |
| `EventCharAnimDeadCB` | `0x005CB200` | `SetBaseCharacterEventEffect(…, 0x200)` |
| `EventCharActionResult` | `0x005CE580` | Fallunterscheidung nach Ergebnisart, ruft `SetActionResultSkill` (`0x005CA1F0`) |
| `EventCharLevelUPCB` / `EventCharUpdateActionStatus` / `EventCharTransform` | `0x005CE550` / `0x005CE940` / `0x005CE920` | je ein `SetCommonCharEffect`-Aufruf, Anmeldereihenfolge und Größe |
| `EventCharSpecialStatus` | `0x005CE670` | vergleicht die Status-Bits (`+0x740`: 0x1, 0x4, 0x200, 0x200000, 0x8000 …) und startet/stoppt Effekte |
| `EventCharAdditionalEffect` | `0x005CE800` | `switch` über die Zusatzeffekt-ID (1, 2, 3, 4, 6, 8, 9, 10) mit `SetCommonCharEffect` |
| `CBCharUseEffect` | `0x005CE980` | `switch` über die Benutzungsart (1, 2, 4, 8, 0x10, 0x20 …) |
| `EventWaveFxTrigger` | `0x005C7450` | enthält die Konstante 3633 (Quelle: `SetBaseCustomEventEffect(…, 3633, …)`) |
| `EventItemEquipCB` / `EventItemDetachedCB` / `EventItemUnequipCB` | `0x005CD040` / `0x005CA2A0` / `0x005CCC40` | Rüstungsteile außer Körper/Kopf (Art 1, Teil ≠ 2, 3) bzw. Entfernen aller Effekte und Spirit-Stone-Effekt freigeben (`0x005CA330`) |
| `EventItemUseCB` | `0x005C88C0` | Anmeldung `UseItemSuccess` |
| `EventItemUpdateConvertHistoryCB` | `0x005CCDD0` | zweifach angemeldet (Add/Update), ruft `UpdateConvertedItemEventEffect` (`0x005CCD80`) |
| `EventSkillCB` | `0x005CA310` | zweifach angemeldet (Anim/ohne Anim), ruft `SetBaseSkillEventEffect` (`0x005C9770`, 1036 Byte, [`AgcmUIOption`](AgcmUIOption.md)) |
| `EventSkillAdditionalEffectCB` | `0x005CC790` | kopiert Effekt-IDs in den Vektor bei `this+0x1F9C` |
| `EventSkillAddBuffedListCB` / `…RemoveBuffedListCB` | `0x005CA370` / `0x005C7B00` | rufen `SetPassiveSkill` (`0x005C9B80`) bzw. `RemoveContinuativetSkillEventEffect` (`0x005C6280`) |

Nicht angemeldet bzw. ohne eigene Funktion sind `EventCharCreate` und `EventCharDamageCB` (in der Quelle nirgends registriert); `EventCharUpdateMovemenntCB` ist die `return TRUE`-Hülle (`0x0067AC90`). Die sechs `EventSkill…ThirdAttack/Evation/…CB`-Stubs wurden nicht gefunden.

## Gemeinsame Charakter-Effekte

`SetCommonCharEffect` (`0x005CE080`, 431 Byte) ruft zuerst `RemoveCommonCharacterEffect` (`0x005CB950`, 515 Byte) auf. Für Drachenabkömmlinge (Rasse 4) wird innerhalb einer Schreinzone zusätzlich `SaveCurrentEffectEvolution` (`0x005CC5F0`) gerufen (Modul [`AgpmShrineBattle`](AgpmShrineBattle.md)). Hat der Charakter noch keinen Clump, wird der Effekt als vorab eingeplant (bis zu 20 Einträge, je 0x10 Byte) vermerkt; sonst werden die Effektdaten der Art nacheinander gestartet. `CBRestoreCommonEffectsByEvolution` (`0x005CEB70`) stellt die gespeicherten Effekte nach der Rückverwandlung wieder her.
`SetTargetStruckEffect` (`0x005CE290`, 697 Byte) enthält die Debug-Zeichenketten `Attacker TID = %d`/`Target TID = %d`. `RemoveAllEffect` (`0x005CC7F0`, 554 Byte) entfernt alle Effekte einer Basis (Zeichenkette `AgcmEventEffect::RemoveAllEffect`, Modul `AgcmItem`).

## Starten und Hilfsfunktionen

`StartEventEffect` (`0x005C7E70`, 564 Byte; Zeichenketten [`AgpmSiegeWar`](AgpmSiegeWar.md), `AgcmUIOption`, `SOUND\EFFECT\`) wird von den drei `SetBaseEffectParams`-Varianten (`0x005C80B0`, `0x005C81D0`, `0x005C8340`) gerufen. `PlaySound` (`0x005C7550`, Format `%s%s`) spielt Effekt-Töne über `AgcmSound`; `AddCustData` (`0x005C7760`, Formate `0%c%c` und `%s%s%s`) fügt Kunden-Daten-Marken an.
Die Hilfsklassen für Himmel-Effekte (`UpdateNatureStatus`, `CBSkyChange` `0x005C9100`) und der Stream für das Ausschluss-Mapping (`StreamReadExclusiveEffectMappingTable` `0x00608980`, Zeichenkette `ExcEffID`) sind benannt.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Modulliste, `SetCommonCharEffect`, Zusatzdaten-Größen).

## Grenzen

- Die Registrierungsreihenfolge im Binary entspricht nicht der Quellreihenfolge, und die Setter für Rückruf-ID 0 sind zusammengefaltet; die Zuordnung der Rückrufe beruht deshalb auf dem Inhalt der Funktionen, nicht auf der Setter-Adresse.
- Die Zuordnung ist über Fallunterscheidungen, Konstanten, Aufrufer und Größen erfolgt, nicht Zeile für Zeile verglichen; am unsichersten sind `EventCharLevelUPCB`/`EventCharTransform`/`EventCharUpdateActionStatus` (nur Größe und Reihenfolge), `SetStandardEffectUseInfo`/`SetBaseEffectUseInfo` (Größenverhältnis) und die zwei `SetAttrDamageEffect`-Überladungen (Adressreihenfolge).
- Zugeordnet im Nachgang (Inhalt, Aufrufer, Quellreihenfolge): die Spirit-Stone- und Konvertierungs-Funktionen (`GetMaxSpiritStoneType` `0x005C8C50` mit 7 Gewichtungswerten, `EventItemSpiritStoneAttrCB` `0x005C9000`, `…ConvertedWeaponGrade…`/`…Attr…`, `…ConvertedArmour…` mit Vertex-Shader-Prüfung), die Sound-Hilfen (`PlayAttackSound`, `PlayHitSound`, `AnimSoundCB`, `SetOnlySoundSkill`, `PlaySocialSound`), `SetCheckTimeDataList`, `GetCustDataIndex` (Zeichen- und Zeichenketten-Überladung), die drei `SetBaseEffectParams`, `SetBuffedAttackEffect`, `StartSelectionAnimation`/`StartSocialAnimation`, `NoticeEffectDestroyMatchCB`/`…SkillDestroyMatchCB` und die Anim-Stream-Lese-/Schreibfunktionen.
- Weiterhin nicht zugeordnet: `NoticeEffectSetTargetStruckAnimCB`, `NoticeEffectHitEffectCB`, `GetSpiritStone…`/`ReadSpiritStone…`/`Read…Data` (dünne Weiterleitungen in `AgcmEventEffectData`, ohne eigenen Anker), die Ausschluss-Effekt-Funktionen (std::map-Code ohne Zeichenkette), `StreamRead/WriteTemplate`, `CopyCharAnimAttachedData`, `SetStatus` (eingebaut) und `EventSkill…ThirdAttack/Evation/…` (nicht angemeldet).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 10, nicht im Client: 20, ohne Kandidat: 12, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetWeaponType` | 9 | `0x005C7510` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SetSpiritStoneHitEffect` (`0x005C5860`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEff2`](AgcmEff2.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmItem`](AgcmItem.md), [`AgcmObject`](AgcmObject.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmSound`](AgcmSound.md), [`AgcmUIOption`](AgcmUIOption.md), [`AgpmArchlord`](AgpmArchlord.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgpmShrineBattle`](AgpmShrineBattle.md), [`AgpmSiegeWar`](AgpmSiegeWar.md), [`AgpmSkill`](AgpmSkill.md), [`AgpmTimer`](AgpmTimer.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcmCharacter_Angriff`](AgcmCharacter_Angriff.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmItem`](AgcmItem.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmSound`](AgcmSound.md), [`AgcmUIQuest2`](AgcmUIQuest2.md)
