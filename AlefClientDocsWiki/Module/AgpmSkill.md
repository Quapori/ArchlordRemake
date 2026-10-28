# AgpmSkill (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Paketmoduls `AgpmSkill` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, EP8-Quelle (`Modules/APublic/AgpmSkill`), Vergleich mit den Berichten zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Protokoll unverändert:** Paket-Typ `0x05` (Konstruktor: `SetPacketType(5)`), die vier Pakete `m_csPacket` (10 Felder, Flag-Länge 2), `m_csPacketBase` (2, Flag-Länge 1), `m_csPacketAction` (12, Flag-Länge 2) und `m_csPacketBuff` (6, Flag-Länge 2) stimmen in Feldtypen, Anzahlen und Flag-Längen mit der EP8-Quelle und der 2013er Doku überein. `m_csPacketMastery` und `m_csPacketMasteryNode` haben in der Quelle keine Felder (auskommentiert) und werden im Binary nicht aufgebaut; auch 2013 ohne Felder.
- **Opcodes unverändert:** `OnReceive` (`0x005663F0`, vtable-Slot 9) liest 11 Felder per `GetField`, prüft Sender und Sperrstatus und ruft für Operationen `< 17` die Switch-Funktion `OnReceiveSkill` bei `0x00564C40` auf. Operationen ab dem `SEPARATOR` (17, Mastery-Pfad) werden wie in der Quelle verworfen (`return 0`). 16 der 17 Operationen haben einen Case; `3` (`UPDATE_ATTACH_DATA`) hat in Quelle, 2013 und 2017 keinen und endet im `default`.
- **Ereignisse:** Alle 15 einzeln vergleichbaren Opcodes (1, 2, 4–16) lösen im 2017er Binary exakt dieselben Callback-IDs aus wie in der 2013er Messung. Op 0 (`ADD`) hat einen zu großen Aufrufbaum für den Mengenvergleich (2017 findet zusätzlich `GET_MODIFIED_SKILL_LEVEL` und `UPDATE_SKILL_POINT`, vermutlich Suchradius).
- **Keine Callback-ID-Verschiebung** (anders als bei [`AgpmItem`](AgpmItem.md)): die IDs stimmen ohne Umrechnung mit EP8 überein.
- **Adressen verschoben:** `OnReceive` bei `0x005663F0` (2013: `0x00566A90`), Switch-Funktion bei `0x00564C40` (2013: Hilfsfunktion `0x005652D0`).

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0052E100` | `AgpmSkill::TemplateWriteCB` | stage1 |
| `0x0052E140` | `AgpmSkill::TemplateReadCB` | stage1 |
| `0x0052E1D0` | `AgpmSkill::SpecializeWriteCB` | stage1 |
| `0x0052E260` | `AgpmSkill::SpecializeReadCB` | stage1 |
| `0x005332A0` | `AgpmSkill::AttachedTemplateWriteCB` | stage1 |
| `0x005333A0` | `AgpmSkill::AttachedTemplateReadCB` | stage1 |
| `0x00560E80` | `AgpmSkill::OnInit` | merged |
| `0x00561230` | `AgpmSkill::GetAttachSkillData` | onreceive-struktur |
| `0x00562A90` | `AgpmSkill::OnDestroy` | merged |
| `0x00562C60` | `AgpmSkill::OnIdle2` | merged |
| `0x00562E20` | `AgpmSkill::ConAgpdSkillAttachData` | stage1 |
| `0x00562FD0` | `AgpmSkill::DesAgpdSkillAttachData` | stage1 |
| `0x00563060` | `AgpmSkill::ConAgpdSkillTemplateAttachData` | stage1 |
| `0x00563350` | `AgpmSkill::CBRemoveCharacter` | stage1 |
| `0x005633C0` | `AgpmSkill::CBUpdateActionStatus` | stage1 |
| `0x005634D0` | `AgpmSkill::CBGetPetTIDByItemFromSkill` | stage1 |
| `0x00563500` | `AgpmSkill::GetBaseFromPacket` | onreceive-struktur |
| `0x00564740` | `AgpmSkill::OnAddModule` | merged |
| `0x00564C40` | `AgpmSkill::OnReceiveSkill` | onreceive-struktur |
| `0x00565FD0` | `AgpmSkill::ctor_or_dtor_00565fd0` | merged |
| `0x005662A0` | `AgpmSkill::ctor_or_dtor_005662a0` | merged |
| `0x005663F0` | `AgpmSkill::OnReceive` | merged |
| `0x005665B0` | `AgpmSkill::~AgpmSkill` | merged |

`OnReceive` = vtable-Slot 9 (`0x005663F0`); der Konstruktor liegt bei `0x00565FD0`. Die vier Datenpools des Konstruktors (`FUN_004E4160` mit `0x100`, `0x9F18`, `0x158`, `0x2B0` Byte) sind nicht weiter belegt. Die Funktionen `OnReceiveSkill`, `GetBaseFromPacket` (`0x563500`) und `GetAttachSkillData` (`0x561230`) sind aus der Struktur von `OnReceive` abgeleitet (Aufruf mit `pvPacketBase`/Basisobjekt).

## Paketlayout

Typcodes wie bei [`AgpmCharacter`](AgpmCharacter.md). Verglichen wurden Quelle (`SetFieldType`), 2017er Konstruktor (`FUN_004E9F80`) und die 2013er Tabellen. Bei `m_csPacketMastery`/`…Node` fehlt der Binary-Aufruf, weil die Quelle dort keine Felder definiert.

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 10/10/10 | ja | ja |
| `m_csPacketBase` | 1/1/1 | 2/2/2 | ja | ja |
| `m_csPacketAction` | 2/2/2 | 12/12/12 | ja | ja |
| `m_csPacketBuff` | 2/2/2 | 6/6/6 | ja | ja |
| `m_csPacketMastery` | 1/None/1 | 0/None/0 | NEIN | ja |
| `m_csPacketMasteryNode` | 1/None/1 | 0/None/0 | NEIN | ja |

**m_csPacket** (10 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | skill id |
| 2 | `0x4` | PACKET | 1 | Base Packet |
| 3 | `0x8` | PACKET | 1 | factor packet |
| 4 | `0x10` | INT32 | 1 | template id |
| 5 | `0x20` | INT8 | 1 | status (eAgpmSkillStatus) |
| 6 | `0x40` | PACKET | 1 | action packet |
| 7 | `0x80` | UINT8 | 1 | skill point |
| 8 | `0x100` | PACKET | AGPMSKILL_MAX_SKILL_BUFF | AUTYPE_PACKET,		1,			// mastery packet |
| 9 | `0x200` | MEMORY_BLOCK | 1 | AUTYPE_UINT8,		1,			// skillÀÇ mastery index |

**m_csPacketBase** (2 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | base type |
| 1 | `0x2` | INT32 | 1 | base id |

**m_csPacketAction** (12 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | action type |
| 1 | `0x2` | PACKET | 1 | target base packet |
| 2 | `0x4` | PACKET | 1 | cast result factor packet |
| 3 | `0x8` | POS | 1 | destination position packet |
| 4 | `0x10` | INT8 | 1 | °­Á¦¾îÅÃ ¿©ºÎ (Ctrl + ½ºÅ³) : °­Á¦¾îÅÃÀÌ¸é 1, ¾Æ´Ï¸é ÇÊµå¸¦ »«´Ù. |
| 5 | `0x20` | UINT32 | 1 | cast delay |
| 6 | `0x40` | UINT32 | 1 | duration |
| 7 | `0x80` | UINT32 | 1 | recast delay |
| 8 | `0x100` | UINT8 | 1 | skill level |
| 9 | `0x200` | UINT8 | 1 | result factor queueing ¿©ºÎ (µ¥¹ÌÁö¸¦ ¹Ù·Î º¸¿©ÁÙÁö Å¥¿¡ ³ÖÀ»Áö ¿©ºÎ. º¸Åë¶§´Â ¾Ï°Íµµ ¾Èº¸³»°í ¹Ù·Î º¸¿©Áà¾ß ÇÒ¶§¸¸ ÇÃ·¡±×¸¦ 1·Î ¼¼ÆÃÇØ¼­ º¸³½´Ù.) |
| 10 | `0x400` | UINT32 | 1 | additional effect. 2005.12.15. steeple |
| 11 | `0x800` | MEMORY_BLOCK | 1 | target character id |

**m_csPacketBuff** (6 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | buffed skill tid |
| 1 | `0x2` | UINT32 | 1 | buffed skill end time |
| 2 | `0x4` | INT32 | 1 | caster tid |
| 3 | `0x8` | UINT8 | 1 | charge level |
| 4 | `0x10` | UINT32 | 1 | expired time |
| 5 | `0x20` | MEMORY_BLOCK | 1 | BuffedSkillCombatArg |

## Opcode-Tabelle

Alle Cases stehen inline in `OnReceiveSkill`. Ereignisse = Menge der `EnumCallback`-IDs (Tiefe 3). Op 17 ist nur der `SEPARATOR`-Wert, kein Opcode.

| Op | Name | 2017-Handler | Ereignisse 2017 (auf EP8-IDs umgerechnet) | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | inline in `OnReceiveSkill` (`0x564C40`) | `ADD_BUFF`, `CHECK_NOW_UPDATE_ACTION_FACTOR`, `DELETE_SKILL`, `GET_MODIFIED_SKILL_LEVEL`, `INIT_COOLTIME`, `INIT_SKILL` … (19) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 1 | `REMOVE` | inline in `OnReceiveSkill` (`0x564C40`) | `DELETE_SKILL`, `REMOVE_ID`, `REMOVE_SKILL` | = (2013 = 2017) |
| 2 | `UPDATE` | inline in `OnReceiveSkill` (`0x564C40`) | `UPDATE_SKILL` | = (2013 = 2017) |
| 3 | `UPDATE_ATTACH_DATA` | – (default) | – | kein Case (default) – wie 2013 |
| 4 | `ADD_BUFFED_LIST` | inline in `OnReceiveSkill` (`0x564C40`) | `ADD_BUFF` | = (2013 = 2017) |
| 5 | `REMOVE_BUFFED_LIST` | inline in `OnReceiveSkill` (`0x564C40`) | `REMOVE_BUFF` | = (2013 = 2017) |
| 6 | `ALL_BUFFED_SKILL` | inline in `OnReceiveSkill` (`0x564C40`) | `ADD_BUFF` | = (2013 = 2017) |
| 7 | `CAST_SKILL` | inline in `OnReceiveSkill` (`0x564C40`) | `RECEIVE_ACTION` | = (2013 = 2017) |
| 8 | `CAST_SKILL_RESULT` | inline in `OnReceiveSkill` (`0x564C40`) | `CHECK_NOW_UPDATE_ACTION_FACTOR`, `RECEIVE_ACTION_RESULT` | = (2013 = 2017) |
| 9 | `REAL_HIT` | inline in `OnReceiveSkill` (`0x564C40`) | `RECEIVE_REAL_HIT` | = (2013 = 2017) |
| 10 | `ADDITIONAL_EFFECT` | inline in `OnReceiveSkill` (`0x564C40`) | `RECEIVE_ADDITIONAL_EFFECT` | = (2013 = 2017) |
| 11 | `UPDATE_DIRT_POINT` | inline in `OnReceiveSkill` (`0x564C40`) | `UPDATE_DIRT_POINT` | = (2013 = 2017) |
| 12 | `UPDATE_SKILL_POINT` | inline in `OnReceiveSkill` (`0x564C40`) | `GET_MODIFIED_SKILL_LEVEL`, `UPDATE_SKILL_POINT` | = (2013 = 2017) |
| 13 | `REQUEST_SKILL_ROLLBACK` | inline in `OnReceiveSkill` (`0x564C40`) | `ROLLBACK_SKILL` | = (2013 = 2017) |
| 14 | `MODIFIED_SKILL_LEVEL` | inline in `OnReceiveSkill` (`0x564C40`) | `MODIFIED_SKILL_LEVEL` | = (2013 = 2017) |
| 15 | `INIT_COOLTIME` | inline in `OnReceiveSkill` (`0x564C40`) | `INIT_COOLTIME` | = (2013 = 2017) |
| 16 | `SPECIFIC_SKILL_LEVEL` | inline in `OnReceiveSkill` (`0x564C40`) | `SPECIFIC_SKILL_LEVEL` | = (2013 = 2017) |

## Abgleich mit EP8-Quelle und Besonderheiten

- `OnReceive`: 11 `GetField`-Felder (Operation, Skill-ID, Basis-Paket, Faktor-Paket, TID, Status, Aktions-Paket, Skillpunkte, Buff-Pufferfeld, Buffed-Combat-Argument, Buff-Länge), identisch zur Quelle.
- Das Puffer-Array hat `AGPMSKILL_MAX_SKILL_BUFF` = 96 Einträge (Quelle) und entspricht dem `memset(…, 0x180)` im Binary (96 × 4 Byte).
- Das Buffed-Combat-Argument (152 Byte = 0x26 DWORDs) wird, falls vorhanden, in die angehängten Skill-Daten des Basisobjekts bei `+0x1840` kopiert, genau wie die Quelle `m_stBuffedSkillCombatEffectArg` setzt.
- Prüfungen für Zeichen: bei Paketen vom Client muss die CID zum Socket-Besitzer passen und der Charakter darf nicht `AllBlock` sein (`FUN_00505A70`); die Basis wird per Mutex (`FUN_004E7CF0`) gesperrt und am Ende freigegeben (`FUN_004E7C70`).
- Die Mastery-Operationen (> 17) sind auch in der Quelle auskommentiert; ein Server darf sie nicht senden.

## Grenzen

- Die Cases innerhalb von `OnReceiveSkill` wurden nicht Zeile für Zeile gegen die Quelle gelesen; verglichen wurden die ausgelösten Callback-IDs (Tiefe 3). Eine Zuordnung der inline Case-Blöcke zu Funktionsnamen war nicht möglich, weil die Quelle keine `OnOperation…`-Handler benutzt.
- Der Aufrufbaum von Op 0 (`ADD`, bis `AddSkill` `0x005630D0`) ist nicht im Detail verglichen.
- Weitere Dateien des Moduls (`AgpmSkillMakePacket`, `AgpmSkillMastery`, `AgpmSkillStream`) liegen teils an anderen Adressen und sind nur teilweise benannt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 20, eingebaut: 16, gemeinsamer Rumpf: 29, nicht im Client: 89, ohne Kandidat: 62, zugeordnet: 42.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsETCSkill` | 8 | `0x00562730` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSelfBuffSkill` | 14 | `0x005626C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsProductSkill` | 5 | `0x00561D00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPassiveSkill_2` | 0 | `0x00561CD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetSkillType` | 2266 | `0x0052E510` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTooptipType` | 487 | `0x00530CA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveOwnSkillList` | 25 | `0x00563920` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRemoveSkill` | 23 | `0x005629B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsDeadTarget` | 12 | `0x00564C00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetWeaponDamageType` | 7 | `0x005628A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSummonsTIDByItem` | 13 | `0x00562850` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsEvolutionSkill` | 15 | `0x005643B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsOwnSkill` | 36 | `0x00564070` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckLearnableSkill` | 6 | `0x005649F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSufficientCost` | 104 | `0x00561A70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTargetType` | 17 | `0x00561720` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsVisibleEffectTypeSelfOnly` | 8 | `0x005642F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSummonsSkill` | 17 | `0x005642B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAttackSkill` | 2 | `0x00564200` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPassiveSkill` | 5 | `0x00563E10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckRequireClass` | 124 | `0x00562340` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakeBasePacket` | 10 | `0x0055C310` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSkillPoint` | 9 | `0x005622C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSkillLevel` | 40 | `0x00562240` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetAdjustCastDelay` | 15 | `0x00561D60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidTarget` | 210 | `0x00565AF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveUsePassiveList` | 27 | `0x005637F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddUsePassiveList` | 23 | `0x00563780` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckHaveAnySkill` | 36 | `0x005636C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyTooltipTemplate` | 7 | `0x00561200` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroySpecialize` | 10 | `0x00561100` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroySkillTemplate` | 12 | `0x005610A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateSkill` | 47 | `0x00560FA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalUsedHeroicPoint` | 35 | `0x005640E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetRange` | 76 | `0x00563E40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateDIRT` | 45 | `0x005620B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsSatisfyRequirement` | 137 | `0x00563AB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckTargetRestriction` | 41 | `0x005639E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessRemove` | 28 | `0x00566B10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateSkillPoint` | 60 | `0x00563FA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBase` | 26 | `0x00561450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetAttachSkillTemplateData` | 15 | `0x00561260` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `DestroySkill` (`0x00541580`), `CreateSkillTemplate` (`0x00562C80`), `CreateSpecialize` (`0x00562C80`), `AddSkill` (`0x00563170`), `RemoveSkill` (`0x00563170`), `GetSkill` (`0x00564AB0`), `GetCostHP` (`0x00561950`), `GetCostSP` (`0x00561950`), `GetCostMP` (`0x00561950`), `GetRecastDelay` (`0x00561DE0`), `GetRecastDelay` (`0x00561DE0`), `GetTargetArea1` (`0x00561E30`), `AddSkillPoint` (`0x005649A0`), `SubtractSkillPoint` (`0x005649A0`), `GetTotalSkillPoint` (`0x00564AB0`), `IsArchlordSkill` (`0x00563210`), `GetSkillByTID` (`0x00564630`), `GetModifiedSkillLevel` (`0x00563210`), `AdjustSkillPoint` (`0x00563170`), `AdjustHeroicPoint` (`0x00563170`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md)
- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmItem`](AgcmItem.md), [`AgcmProductMed`](AgcmProductMed.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIStatus`](AgcmUIStatus.md), [`AgpmCombat`](AgpmCombat.md)
