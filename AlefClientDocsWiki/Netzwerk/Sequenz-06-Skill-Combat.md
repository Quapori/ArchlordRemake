# Winsock Sequenz 06: Skill, Cast und Combat

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Quelle: statische Analyse von `alefclient.pseudocode.c`, besonders [`AgpmSkill`](../Module/AgpmSkill.md), [`AgcmSkill`](../Module/AgcmSkill.md), [`AgpmCombat`](../Module/AgpmCombat.md), UI-Bindings und Sendpfade ueber `FUN_004ea280`/`FUN_004e45d0`. Es wurde kein Live-Traffic mitgeschnitten. Alle DB-Strukturen sind deshalb Inferenz aus Clientfeldern und Paketoperationen.

## Kurzfazit

- `AgpmSkill` ist Netzwerkmodul `0x05`.
- `AgcmSkill` ist die Client-/UI-/Cast-Schicht, die vor einem Cast Ziel, Zustand, Entfernung, Cooldown und Skilldaten prueft.
- `AgpmCombat` ist kein sichtbares eigenes Netzwerkmodul im Konstruktor, sondern ein lokales Berechnungs-/Abhaengigkeitsmodul fuer Faktoren, Character, Item, ItemConvert und Skill.
- Der eigentliche Client-Cast laeuft ueber `FUN_0066d670` -> `FUN_00594a50` -> `FUN_004ea280(..., module 5, op 7, ...)` -> `FUN_004e45d0(...)`.
- `AgpmSkill` verarbeitet serverseitige Skillzustands-Operationen mindestens `0..6`; lokal erzeugte Pakete enthalten sicher die Operationen `7`, `9` und `0x0d`.
- Skillkauf/Skillupgrade ist im Client stark ueber [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md) und UI-Funktionen verdrahtet. Das ist ein eigener Folgebereich, nicht nur normales Casten.

## Modulidentitaet

### AgpmSkill

Konstruktor `FUN_00566670`:

- Modulname: `AgpmSkill`
- Modul-ID: `FUN_004e4540(5)` -> Netzwerkmodul `0x05`
- Registriert vier relevante Layouts:
  - `param_1 + 0x2f1`
  - `param_1 + 0x4d36`
  - `param_1 + 0x977b`
  - `param_1 + 0x12c05`
- Setzt Objekt-/Managerfelder:
  - `+0xb84`/`+0xb88`/`+0xb8c` spaeter Modulreferenzen auf Factors, Character, Union
  - `+0xc44` Callback-/Extension-ID fuer Skilldaten am Character
  - `+0xcfc` Zeitstempel fuer periodische Skill-/Cachepflege
  - `+0x1772b..+0x1772e` Container/Vector fuer Skillobjekte

Layout-Auszug aus `FUN_00566670`:

```text
AgpmSkill +0x0bc4?  wird spaeter von FUN_00594a50 als Sendlayout benutzt
AgpmSkill +0x0d00   Server-Receive-Layout fuer Skillstatus/Synchronisierung
AgpmSkill +0x13614  Nested Skill-Zusatzzustand
AgpmSkill +0x25f28  Nested kleines Statuslayout
```

Wichtig: Der Konstruktor zeigt `+0x2f1`, `+0x4d36`, `+0x977b`, `+0x12c05`. Wegen C-Decompiler-Arithmetik auf `undefined4 *` entsprechen diese Pseudocode-Offsets teilweise nicht 1:1 den spaeteren Byteoffsets in anderen Funktionen. Fuer die Netzwerkzuordnung sind deshalb die direkten `FUN_004ea280`-Aufrufe belastbarer.

### AgcmSkill

Konstruktor-/Initialisierung:

- Konstruktorblock um `FUN_00669ca0`/`FUN_0066cc50`/`FUN_0066de20`.
- Modulname: `AgcmSkill`.
- Wichtige Abhaengigkeiten in `FUN_0066de20`:
  - `+0xb98` -> [`AgpmCharacter`](../Module/AgpmCharacter.md)
  - `+0xb9c` -> [`AgpmItem`](../Module/AgpmItem.md)
  - `+0xba0` -> `AgpmSkill`
  - `+0xba4` -> [`AgpmGrid`](../Module/AgpmGrid.md)
  - `+0xba8` -> [`AgpmPvP`](../Module/AgpmPvP.md)
  - `+0xbac` -> [`ApmEventManager`](../Module/ApmEventManager.md)
  - `+0xbb0` -> `AgcmCharacter`
  - `+0xbb4` -> [`AgpmFactors`](../Module/AgpmFactors.md)
  - `+0xbb8` / dezimal `3000` -> [`AgcmUIControl`](../Module/AgcmUIControl.md)
  - `+0xbbc` -> [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md)
  - `+0xbc0` -> [`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md)

Registrierte lokale Callback-/Extension-Slots:

- `+0xc7c`: `FUN_005876e0(param_1, 0x20, ...)`
- `+0xc7e`: `FUN_0051d210(param_1, 4, ...)`
- `+0xc80`: `FUN_0051d210(param_1, 0x1c, ...)`
- `+0xc82`: `FUN_00561ac0(param_1, 8, ...)`
- `+0xc84`: `FUN_005876e0(param_1, 400, ...)`

Diese Slots sind keine Netzwerk-Opcode-IDs, sondern lokale Callback-/Extension-Indizes, die Skilldaten an Character-/Item-/Effect-Objekte koppeln.

### AgpmCombat

Konstruktor `FUN_005797d0`:

- Modulname: `AgpmCombat`.
- Im sichtbaren Konstruktor kein `FUN_004e4540(...)`; daher kein eigenes gesichertes Netzwerkmodul aus diesem Block.
- Initialisierung `FUN_005798b0` haengt ab von:
  - `AgpmFactors`
  - `AgpmCharacter`
  - `AgpmItem`
  - [`AgpmItemConvert`](../Module/AgpmItemConvert.md)
  - `AgpmSkill`

Interpretation: Combat berechnet lokale oder servernachgebildete Kampf-/Schadenswerte und Skillwirkungen, waehrend das eigentliche Cast-/Skillprotokoll ueber `AgpmSkill` (`0x05`) laeuft.

## Skill-Cast: Client -> Server

### Hauptpfad

Gesicherter Pfad:

```text
UI/Action/Shortcut/AI
  -> AgcmSkill Validierung
  -> FUN_0066d670(...)
  -> FUN_00594a50(...)
  -> FUN_004ea280(AgpmSkill + 0xbc4, 1, packetLen, module 5, op 7, ...)
  -> FUN_004e45d0(packet, len, 0, 3, 0)
  -> AcSocketManager/FUN_006fd8c0
  -> AcClientSocket/send
```

`FUN_0066d670` ist der wichtigste bisher gefundene lokale Skill-Cast-Einstieg. Sie prueft:

- Skillinstanz/-template ueber `FUN_00564cc0(localCharacter, skillOrTemplateId)`.
- Lokalen Character ueber `DAT_0001596c + AgcmCharacter`.
- Block-/Zustandsflags am lokalen Character, u.a. `localCharacter +0x744 & 0x20`.
- Zielzustand und Skilltemplate-Felder unter `skill +0x9c`.
- Falls Cast positioniert ist: uebernimmt Zielposition in `AgcmSkill +0xcb8/+0xcbc/+0xcc0` und in `skill +0x8c/+0x90/+0x94`.
- Prueft lokalen Spezialzustand/Bewegungszustand `FUN_00504fa0(localChar, 4)`.
- Ermittelt Zielcharacter ueber `FUN_0055c820`.
- Prueft Skillbenutzbarkeit/Cooldown/Reichweite:
  - `FUN_00564130(skill)`
  - `FUN_005620e0(skill, &reason)`
  - Tickvergleich: `AgcmCharacter +0x13a1c < skill +0xbc`
  - `FUN_00561e10(skill, target)`
  - `FUN_00566190(skill, target, param_5, local_8c)`

Wenn eine Pruefung scheitert, ruft die Funktion `FUN_004e4070(reason, data, 0)` mit lokalen Fehlercodes auf. Sichtbare Reason-Werte:

| Reason | Beobachtung |
|---:|---|
| `2` | generischer Skill-/Target-Fehler nach fehlgeschlagener Nutzbarkeitspruefung |
| `7` | lokaler Character in einem blockierenden Zustand |
| `8` | `FUN_00564130` fehlgeschlagen; Skill nicht ausfuehrbar/ungueltig |
| `9` | Rueckgabewert aus `FUN_005620e0`; vermutlich Requirement/Cooldown/Resource-Grund |
| `0x0c` | weiterer blockierender Character-/Templatezustand |
| `0x0d` | Sequenz-/Folgecast oder Skill benoetigt vorbereitenden Zustand |
| `0x0f` | Tick/Cooldown noch nicht bereit |

### Paketbau in FUN_00594a50

`FUN_00594a50` baut das eigentliche Modul-`0x05`-Paket:

```text
FUN_00594a50(
    AgpmSkillModule,
    opOrCastType,
    skillIdPtr?,
    casterChar,
    localChar,
    targetChar,
    castPositionPtr,
    extraParam,
    ...
    outLenPtr
)
```

Gesicherte Details aus dem Code:

- `param_5` muss lokalem Character entsprechen; sonst kein Paket.
- `param_15` ist Out-Len und muss gesetzt sein.
- `FUN_00594900(param_5)` erzeugt/serialisiert einen Character-/Actor-Nestedblock.
- Erlaubte `opOrCastType`-Werte:
  - `0`
  - `1`
  - `3`
  - `4`
  - `5`
  - `0x10`
  - `0x13`
- Werte `3`, `4`, `5`, `0x10`, `0x13` nullen mehrere Zusatzparameter. Das sind wahrscheinlich Cast-/Combat-Sondertypen, bei denen Position/Extra-Ziele nicht mitgesendet werden.
- `FUN_00594940(...)` erzeugt einen zweiten Nestedblock fuer Ziel-/Positions-/Wirkungsdaten.
- Danach:

```text
param_5 low byte = 7
FUN_004ea280(AgpmSkill + 0xbc4, 1, outLenPtr, 5,
             &op7, skillOrParam, casterNested, 0,
             casterCharOrSkillId, 0, targetNested, 0, 0, 0)
```

Damit ist Operation `7` fuer Client-Cast/Skillausfuehrung sehr wahrscheinlich.

### Weitere lokale Skill-Sendbuilder

`FUN_00594c70`:

```text
op = 9
FUN_004ea280(AgpmSkill +0xbc4, 1, outLen, 5,
             &op9, param_2, actorNested, 0, 0, 0, 0, ...)
```

Inferenz: Skill-/Combat-Statusnachricht mit Actor-Bezug. Kontext offen.

`FUN_00594cf0`:

```text
op = 0x0d
FUN_004ea280(AgpmSkill +0xbc4, 1, outLen, 5,
             &op0d, &param_3, actorNested, 0, 0, ...)
```

Inferenz: Spezial-/Folgecast oder Skill-Ereignis mit Actor + einem zusaetzlichen Wert.

## Skillzustand: Server -> Client

Wichtigster bisher gefundener Receive-/Apply-Switch: `FUN_00568130`.

Die Funktion liest mit:

```text
FUN_004e9fb0(AgpmSkill +0xd00, 1, packet, len,
             &op, &skillObjId, &smallA, &smallB,
             &relatedObjId, &idListPtr,
             &fieldX, &fieldY, &nestedSkillState,
             &stateA, &fieldZ, &stateB)
```

Danach `switch(op)`:

| Op | Bedeutung/Inferenz |
|---:|---|
| `0` | Skillbeziehung/Skillinstanz erzeugen. Erwartet Skillobjekt, mindestens zwei Character-/Objekt-IDs in einer Liste, erzeugt intern Skilllink ueber `FUN_00567de0`, haengt weitere Ziele an und feuert lokalen Callback `6`. |
| `1` | Skillinstanz entfernen/loeschen. Holt lokale Skillinstanz via `FUN_00566f90(skillObjId)`, entfernt Unterlinks ueber `FUN_005675b0`. |
| `2` | Skillstatus aktualisieren. Setzt ggf. `skill +0x30`, verarbeitet Nestedzustand `FUN_005677d0`, verarbeitet weiteres Statuslayout `FUN_00566fc0`. |
| `3` | Weiteres Ziel/Objekt an Skillinstanz haengen. Nutzt `relatedObjId` -> Character/Objekt und `FUN_00567cd0`. |
| `4` | Ziel/Objekt aus Skillinstanz loesen oder Spezialloeschung. Nutzt lokalen Callback `9`, `FUN_00567bb0`, `FUN_00567ea0`. |
| `5` | Statusfeld `skill +0x70` aktualisieren, danach lokaler Callback `0x0c`. |
| `6` | Statusfeld `skill +0x7c` aktualisieren, danach lokaler Callback `0x0f`. |

Wichtige lokale Skillobjekt-Felder aus den gelesenen Funktionen:

| Offset | Bedeutung/Inferenz |
|---:|---|
| `+0x04` | Skillinstanz-/Owner-ID; wird bei Anlage gesetzt |
| `+0x30` | kurzer Skillstatus/Level/Type |
| `+0x32` | Anzahl verknuepfter IDs/Ziele |
| `+0x34..` | Liste verknuepfter Character-/Objekt-IDs |
| `+0x48` | maximaler Level-/Power-/Range-Wert aus verknuepften Objekten |
| `+0x58` | Zeitstempel fuer Cleanup |
| `+0x5c..+0x6c` | Nested-Zusatzzustand, von `FUN_005677d0` serialisiert |
| `+0x70` | Status A, serverseitig per Op `5` gesetzt |
| `+0x74` | aktueller/erster Skilllink |
| `+0x78` | letzter/zweiter Skilllink |
| `+0x7c` | Status B, serverseitig per Op `6` gesetzt |

## UI-Trigger und Benutzeraktionen

Die UI-Schicht bindet viele Skill-Events und ermoeglicht dadurch eine Zuordnung der Netzwerkpfade zu Spielsituationen.

### Skillfenster

Gefundene UI-Elemente/Events:

- `Skill_NPCDialog_UI_Open`
- `Skill_NPCDialog_UI_Close`
- `Skill_UI_Open`
- `Skill_UI_Close`
- `Skill_Buy_UI_Open`
- `Skill_Buy_UI_Close`
- `Skill_HighLevel_UI_Open`
- `Skill_HighLevel_UI_Close`
- `Skill_HighLevel_Upgrade_UI_Open`
- `Skill_HighLevel_Upgrade_UI_Close`

### Cast-Fehler

Diese UI-Meldungen sind direkt als Skill-Cast-Fehler registriert:

- `Skill_Cast_Failed`
- `Skill_Cast_InvalidTarget`
- `Skill_Cast_NeedRequirement`
- `Skill_Cast_NotEnoughHP`
- `Skill_Cast_NotEnoughSP`
- `Skill_Cast_NotEnoughMP`
- `Skill_Cast_NotEnoughArrow`
- `Skill_Cast_AlreadyUse`
- `Skill_Cast_NotReadyCast`
- `Skill_Cast_Miss`
- `Skill_Cast_InvalidTargetToGather`
- `Skill_Cast_NotEnoughProduct`

Zuordnung: Die lokalen Reason-Werte aus `FUN_0066d670` werden vermutlich ueber Callback `FUN_004e4070(...)` auf diese UI-Meldungen abgebildet. Die exakte Tabelle Reason -> Text ist noch nicht vollstaendig extrahiert.

### Kaufen/Upgrade

Gefundene UI-Events:

- `Skill_SelectBuyGrid`
- `Skill_SelectUpgradeGrid`
- `Skill_Buy`
- `Skill_Upgrade`
- `Skill_ConfirmBuySkill`
- `Skill_ConfirmUpgradeSkill`
- `Skill_BuySuccess`
- `Skill_UpgradeSuccess`
- `Skill_ErrorNotSelectBuySkill`
- `Skill_ErrorNotSelectUpgradeSkill`

High-Level/Heroic/Scion-Varianten:

- `Skill_SelectUpgradeHeroicGrid`
- `Skill_Heroic_Skill_Upgrade`
- `Skill_UIHeroic_Upgrade`
- `Skill_UIScion_Upgrade`
- `Skill_UISlayer_Upgrade`
- `Skill_UIObiter_Upgrade`
- `Skill_UIPassive_Upgrade`
- `Skill_UISummerner_Upgrade`
- `Skill_Scion_Skill_Upgrade`
- `Skill_Slayer_Skill_Upgrade`
- `Skill_Obiter_Skill_Upgrade`
- `Skill_Passive_Skill_Upgrade`
- `Skill_Summerner_Skill_Upgrade`

Zusatzmodul: `AgpmEventSkillMaster` (`FUN_004e4540(0x3b)`) ist sehr wahrscheinlich fuer Skillkauf, Skillmaster-NPC, High-Level-/Heroic-Upgrade und Evolution zustaendig. Das sollte als eigene Sequenz tiefer analysiert werden, weil die Datenbanktabellen fuer Lernkosten, Trainer/NPCs und Voraussetzungen dort sitzen duerften.

## Lokale Skilldaten

Gefundene lokale Datei:

```text
Ini\SkillTemplate.ini
```

Gefundene Template-/Datenklassen:

- `AgpaSkillTemplate`
- `AgpaProductSkillFactor`
- `AgpaSkill`

Gefundene exportierte/skriptnahe Skilldaten:

- `SKILL_ANIMATION_NAME`
- `SKILL_ANIMATION_POINT`
- `SKILL_ANIMATION_FLAGS`
- `SKILL_EFFECT_CONDITION`
- `SKILL_EFFECT_DATA`
- `SKILL_EFFECT_CUST_DATA`
- `SKILL_EFFECT_SOUND`

Damit ist klar: Der Client hat nicht nur IDs, sondern lokale Templates fuer Animationen, Effektbedingungen, Custom-Daten und Sounds. Der Server muss fuer Cast-/Hit-Entscheidungen aber mindestens Skill-ID, Skilllevel, Voraussetzungen, Cooldowns, Zieltyp und Ressourcenverbrauch serverseitig validieren.

## Combat-/Schadenswerte

`AgpmCombat` liest viele Werte ueber `FUN_0050c410`/`FUN_0050c470` aus Character-/Factor-Bloecken. Sichtbare Strings und UI-Exports zeigen u.a.:

- `PhysicalDamage`
- `MagicDamage`
- `WaterDamage`
- `FireDamage`
- `EarthDamage`
- `AirDamage`
- `PoisonDamage`
- `IceDamage`
- `LinghtningDamage` / `ThunderDamage`
- `Heroic_Min_Damage`
- `Heroic_Max_Damage`
- `Attack_Buff`
- `Defense_Buff`
- `Run_Buff`
- `Skill_plus`
- `SkillBlockRate`
- `DurationCastSkill`
- `DurationSkillCoolTime`
- `SpeedAttack`
- `CriticalDamage`
- `AttackRange`
- `ReflectDamageRate`

Inferenz:

- Viele dieser Werte sind Clientanzeige und lokale Vorausberechnung.
- Autoritative Treffer, Schaden, Buffs und Cooldowns muessen serverseitig liegen, weil der Client nur eine Cast-Anfrage sendet und anschliessend serverseitige Character-/Skill-/Factor-Updates empfaengt.
- Der Client fuehrt aber lokale Plausibilitaetschecks aus, damit unmoegliche Casts sofort UI-Fehler erzeugen.

## Wahrscheinliche Serverdatenbank-Strukturen

Aus den Paketfeldern, lokalen Templates und UI-Pfaden lassen sich folgende Tabellen ableiten:

| Tabelle | Zweck | Abgeleitete Felder |
|---|---|---|
| `skill_templates` | statische Skills | `skill_tid`, `name_key`, `class_mask`, `required_level`, `max_level`, `target_type`, `range`, `cast_time`, `cooldown`, `resource_cost_hp`, `resource_cost_mp`, `resource_cost_sp`, `requires_arrow`, `effect_group` |
| `skill_levels` | levelabhaengige Werte | `skill_tid`, `level`, `power`, `duration`, `cooldown`, `range`, `cost`, `required_skill_points`, `required_money`, `required_item_tid` |
| `character_skills` | gelernte Skills pro Character | `character_id`, `skill_tid`, `skill_level`, `slot/mastery_tab`, `learned_at`, `flags` |
| `skill_cooldowns` | serverseitige Cooldowns | `character_id`, `skill_tid`, `cooldown_until`, `last_cast_tick` |
| `active_skill_instances` | laufende Casts/Buffs/Debuffs/DoTs | `skill_instance_id`, `caster_character_id`, `skill_tid`, `level`, `started_at`, `expires_at`, `state_a`, `state_b` |
| `skill_instance_targets` | Ziele einer Skillinstanz | `skill_instance_id`, `target_character_id`, `target_index`, `relation_flags` |
| `character_buffs` | persistente/temporare Buffs | `character_id`, `skill_tid`, `source_character_id`, `stack_count`, `expires_at`, `state` |
| `skill_master_npcs` | Skillmaster-Angebote | `npc_tid`, `class_mask`, `skill_tid`, `min_level`, `upgrade_group` |
| `skill_transactions` | Kaufen/Upgrade/Audit | `account_id`, `character_id`, `npc_id`, `skill_tid`, `old_level`, `new_level`, `cost_money`, `cost_items`, `created_at` |

## Reihenfolge im Spielablauf

1. Nach Character-/World-Entry sendet der Server Skilldaten ueber `AgpmSkill`-Operationen, wahrscheinlich vor oder zusammen mit Character-Factor-Updates.
2. Der Client baut daraus lokale Skillobjekte und verknuepft sie mit Character-/Targetobjekten.
3. Bei Hotkey/UI-Cast prueft `AgcmSkill` lokal den Skill, den Spielerzustand, das Ziel, Position, Range und Cooldown.
4. Wenn alle Checks passen, sendet der Client ein `AgpmSkill`-Paket `module 0x05`, `op 7`.
5. Der Server validiert autoritativ und antwortet mit Skill-/Character-/Factor-Updates:
   - Skillstatus ueber `AgpmSkill` ops `0..6`
   - Movement/Action ueber `AgpmCharacter`
   - HP/MP/Status/Buffs ueber Character-/Factor-Module
6. Skillkauf/Upgrade laeuft separat ueber UI-Events und wahrscheinlich `AgpmEventSkillMaster` (`0x3b`).

## Offene Punkte

- Exakte Feldreihenfolge von `AgpmSkill +0xbc4` und `+0xd00` muss mit extrahierter Type-Size-Tabelle `DAT_008b7698` und einer kleinen Layout-Decoding-Hilfe rekonstruiert werden.
- `FUN_00594900` und `FUN_00594940` muessen einzeln zerlegt werden; sie erzeugen die entscheidenden Nestedbloecke fuer Actor und Ziel/Position.
- Die Tabelle Reason-Code -> UI-Meldung muss ueber die Callback-Registrierungen in `AgcmSkill` vervollstaendigt werden.
- `AgpmEventSkillMaster` sollte als eigene Sequenz folgen, wenn Skillkauf/Upgrade servergenau rekonstruiert werden soll.
