# AgpmCombat (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmCombat` (Kampfwerte: Angriffs-/Verteidigungswert, Widerstände, Block, Schadensberechnung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Faktorkennungen gegen `AgpdFactors.h`, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmCombat/AgpmCombat.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 25 von 51 Quellmethoden sind zugeordnet (24 Funktionen plus `OnInit`/`OnDestroy` am gemeinsamen Rumpf). Die übrigen 26 sind im Binary nicht gefunden: in der Quelle ruft sie nur der Server auf (`ProcessCombat`, `ProcessEvade`, `IsAttackSuccess`, `CalcAtkPenaltyLevelGap` u. a.) oder niemand.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmCombat.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00579350` | 133 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `GetAR` | `0x005793E0` | 210 | von Hand geprüft |
| 4 | `GetBaseAR` | `0x00579B30` | 215 | von Hand geprüft |
| 5 | `GetDR` | `0x005794C0` | 209 | von Hand geprüft |
| 6 | `GetBaseDR` | `0x00579C10` | 215 | von Hand geprüft |
| 7 | `GetPhysicalDefense` | `0x005795A0` | 51 | von Hand geprüft |
| 8 | `GetHeroicDefense` | `0x005795E0` | 51 | von Hand geprüft |
| 9 | `GetHeroicDamageMin` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 10 | `GetHeroicDamageMax` | `0x00579620` | 51 | von Hand geprüft |
| 11 | `GetHeroicMeleeResistance` | `0x00579660` | 51 | von Hand geprüft |
| 12 | `GetHeroicRangedResistance` | `0x005796A0` | 51 | von Hand geprüft |
| 13 | `GetHeroicMagicResistance` | `0x005796E0` | 51 | von Hand geprüft |
| 14 | `GetHeroicResistanceByHeroicClass` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 15 | `GetHeroicResistanceByAttackerHeroicClass` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 16 | `GetPhysicalResistance` | `0x00579720` | 81 | von Hand geprüft |
| 17 | `GetPhysicalBlockRate` | `0x00579780` | 66 | von Hand geprüft |
| 18 | `GetSkillBlockRate` | `0x005797D0` | 66 | von Hand geprüft |
| 19 | `GetPhysicalResistance` | `0x00579820` | 147 | von Hand geprüft |
| 20 | `GetPhysicalBlockRate` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 21 | `GetSkillBlockRate` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 22 | `GetAdditionalHitRate` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 23 | `GetAdditionalEvadeRate` | `0x005798C0` | 66 | von Hand geprüft |
| 24 | `GetAdditionalDodgeRate` | `0x00579910` | 66 | von Hand geprüft |
| 25 | `GetAdditionalEvadeRate` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 26 | `GetAdditionalDodgeRate` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 27 | `IsShieldDefenseSuccess` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 28 | `IsAttackSuccess` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 29 | `IsFirstSpiritAttackSuccess` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 30 | `IsSecondSpiritAttackSuccess` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 31 | `CalcPhysicalAttack` | `0x00579CF0` | 826 | von Hand geprüft |
| 32 | `CalcHeroicAttack` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 33 | `CalcHeroicAttackForSkill` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 34 | `CalcBasePhysicalAttack` | `0x0057A030` | 446 | von Hand geprüft |
| 35 | `CalcPhysicalAttackForSkill` | `0x0057A1F0` | 463 | von Hand geprüft |
| 36 | `CalcBasePhysicalAttackForSkill` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 37 | `CalcFirstSpiritAttack` | `0x0057A3C0` | 478 | von Hand geprüft |
| 38 | `CalcSecondSpiritAttack` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 39 | `CalcItemFirstSpiritAttack` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 40 | `CalcFirstSpiritDefense` | `0x00579960` | 130 | von Hand geprüft |
| 41 | `CalcItemFirstSpiritDefense` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 42 | `CalcItemSecondSpiritAttack` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 43 | `GetWeaponTypeValue` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 44 | `GetCharacterTypeValue` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 45 | `GetArmourAttributeInfo` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 46 | `ProcessCombat` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 47 | `ProcessEvade` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 48 | `CalcPenaltyExp` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |
| 49 | `CalcDefPenaltyLevelGap` | `0x005799F0` | 283 | von Hand geprüft |
| 50 | `CalcAtkPenaltyLevelGap` | – | | nicht im Binary gefunden: in der Quelle nur von Server-Funktionen (z. B. `ProcessCombat`) oder gar nicht gerufen |

25 von 51 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmCombat` (`0x00579270`), `~AgpmCombat_body` (`0x005792F0`), `GetPhysicalResistance_pair` (`0x00579820`), `scalar_deleting_dtor` (`0x00579B10`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB84` | `Zeiger [`AgpmFactors`](AgpmFactors.md)` | `OnAddModule` |
| `this+0xB88` | `Zeiger [`AgpmCharacter`](AgpmCharacter.md)` | `OnAddModule`, `CalcDefPenaltyLevelGap` |
| `this+0xB8C` | `Zeiger [`AgpmItem`](AgpmItem.md)` | `OnAddModule` |
| `this+0xB90` | `Zeiger [`AgpmItemConvert`](AgpmItemConvert.md)` | `OnAddModule` |
| `this+0xB94` | `Zeiger [`AgpmSkill`](AgpmSkill.md)` | `OnAddModule` |
| `Charakter+0x3F0` | `Faktorblock `m_csFactor`` | alle Lesefunktionen |

## Vtable und Aufbau

Vtable `0x008B90C0`: Slot 0 Löschwrapper (`0x00579B10`), Slot 1 `OnAddModule` (`0x00579350`), Slot 2 (`OnInit`) und Slot 7 (`OnDestroy`) am gemeinsamen Rumpf `0x0067AC90`. Konstruktor `0x00579270` (128 Byte, trägt `AgpmCombat` ein), Destruktorrumpf `0x005792F0`. `OnAddModule` (133 Byte) holt `AgpmFactors` (`this+0xB84`), `AgpmCharacter` (`+0xB88`), `AgpmItem` (`+0xB8C`), `AgpmItemConvert` (`+0xB90`) und `AgpmSkill` (`+0xB94`) und verlangt alle außer `AgpmFactors`.
Im Client ist nur ein Teil des Kampfmoduls enthalten (die Rechenfunktionen für Anzeige und Skill-Berechnung); die Kampfabwicklung (`ProcessCombat`, `ProcessEvade`, die `IsAttackSuccess`-Familie) fehlt, weil sie in der Quelle nur der Server aufruft.

## Werte aus Faktoren

Die kleinen Lesefunktionen lesen je einen Faktor über `AgpmFactors::GetValue` (`0x0050BB30` für Gleitkomma, `0x0050BAD0` für ganze Zahlen) aus dem Faktorblock des Charakters (`+0x3F0`): `GetPhysicalDefense` (`0x005795A0`), `GetHeroicDefense` (`0x005795E0`), `GetHeroicDamageMax` (`0x00579620`), `GetHeroicMeleeResistance` (`0x00579660`), `GetHeroicRangedResistance` (`0x005796A0`), `GetHeroicMagicResistance` (`0x005796E0`) und `GetPhysicalResistance` (`0x00579720`, mit Ersatzwert, wenn der Faktor 0 ist); `GetPhysicalBlockRate` (`0x00579780`), `GetSkillBlockRate` (`0x005797D0`), `GetAdditionalEvadeRate` (`0x005798C0`) und `GetAdditionalDodgeRate` (`0x00579910`) liefern ganze Zahlen. `GetPhysicalResistance(Angreifer, Ziel)` (`0x00579820`, 147 Byte) verknüpft die Werte beider Seiten. Die Faktorkennungen im Binary stimmen mit den Aufzählungen aus `AgpdFactors.h` überein (z. B. Heroic = 11, Nahkampf/Fernkampf/Magie = 12/13/14, Block = 9 und 10).
`GetAR` (`0x005793E0`) und `GetDR` (`0x005794C0`) lesen den Angriffs- bzw. Verteidigungswert (Charakterpunkt-Maximum, Unterart 8 bzw. 9): bei Monstern direkt, sonst aus Geschicklichkeit und Stufe; `GetBaseAR` (`0x00579B30`) und `GetBaseDR` (`0x00579C10`) rechnen dasselbe aus den Stufenfaktoren der Vorlage (bei Verwandlung der Ursprungsvorlage).

## Schaden und Stufenabstand

`CalcDefPenaltyLevelGap` (`0x005799F0`, 283 Byte) liefert aus dem Stufenabstand der beiden Charaktere eine Abwehrstrafe (Abstand 1 oder weniger: 0; danach Stufen 2, 4, 6, 8, 12, 16, höchstens 20); sie gilt nur, wenn mindestens einer ein Spieler ist. `CalcFirstSpiritDefense` (`0x00579960`) liest die Verteidigung gegen ein Element (bei Spielern höchstens 80 ab einem Grenzwert, sonst der abgerundete Wert). `CalcFirstSpiritAttack` (`0x0057A3C0`, 478 Byte, acht Aufrufer in einer Folge gleichgebauter Funktionen bei `0x0073C520` bis `0x0073D080`) berechnet den Elementarschaden aus Minimum und Maximum, der Verteidigung des Ziels und der Stufenstrafe mit Zufallszahl.
`CalcPhysicalAttack` (`0x00579CF0`, 826 Byte) berechnet den Waffenschaden gegen Verteidigung und Widerstand des Ziels (`GetPhysicalResistance` `0x00579820`, Stufenstrafe); `CalcPhysicalAttackForSkill` (`0x0057A1F0`) ruft ihn zweimal (physische und heroische Verteidigung); `CalcBasePhysicalAttack` (`0x0057A030`, 446 Byte) bildet den Grundschaden aus Stufe und Vorlage (Minimum/Maximum).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `OnAddModule`, `GetAR`/`GetDR` (Faktorkennungen), `CalcDefPenaltyLevelGap`, `CalcFirstSpiritDefense` und `CalcFirstSpiritAttack` (Dekompilat) sowie die Kennungen aller kleinen Lesefunktionen; `CalcPhysicalAttack`, `CalcPhysicalAttackForSkill`, `CalcBasePhysicalAttack`, `GetBaseAR`/`GetBaseDR` und `GetPhysicalResistance(Angreifer, Ziel)` sind über Aufrufbeziehungen, Größe und Faktorkennungen zugeordnet, nicht Zeile für Zeile verglichen.
- Die Aussage „Aufrufer nur im Server oder keine“ beruht auf einer Textsuche in den Quellen (Variablennamen mit „Combat“); Aufrufe über andere Namen wären so nicht erfasst. Für die 26 Methoden gilt deshalb: nicht im Binary gefunden; Einbau in andere Funktionen ist nicht ausgeschlossen.
- `GetHeroicDamageMin` und `GetAdditionalHitRate` fehlen im Binary, obwohl `GetHeroicDamageMax` und die Ausweich-/Block-Raten vorhanden sind; ob das an fehlenden Aufrufern oder Einbau liegt, ist nicht geklärt.
- Die Zuordnung `GetAdditionalEvadeRate`/`GetAdditionalDodgeRate` folgt aus den Unterartnummern 6 und 7 der Angriffsfaktoren (Aufzählung `AGPD_FACTORS_ATTACK_TYPE_…`), nicht aus Aufrufern.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2, nicht als eigene Funktion: 12, nicht im Client: 15.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgpmSkill`](AgpmSkill.md)
