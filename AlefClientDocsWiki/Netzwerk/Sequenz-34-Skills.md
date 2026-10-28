# Sequenz 34: Skills (Skill-Trainer-NPC)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-14

Drittes NPC-Service-Feature nach Dialoge (kein Zusatzcode nötig) und Repair. Begonnen, nachdem Quests wegen des fehlenden Kampfsystems (Monster-Kill-Objectives nicht live testbar) pausiert wurden — Skills sind komplett ohne Kampf testbar: Trainer-NPC anklicken, Skill lernen, im Skillfenster/Quickbelt sichtbar.

## Zwei Quellbäume

Erste Nutzung der EP8-Server-Quelle (eine weitere Quelle, nicht als vollständig verlässlich eingestuft) neben der EP8-C++-Quelle. Enthält zusätzlich einen `EP8 Server\`-Ordner mit echten Server-Laufzeitdaten (`INI\NPCManager\*`, `INI\SKILL_CONST.TXT` usw.), die der andere Baum nicht hat. Dabei nebenbei geklärt: die generischen NPC-Dialoge brauchen wirklich keinen Server-Code (nur 111 Spezial-NPCs nutzen ein Lua-Skriptsystem, keine gewöhnlichen Dialog-NPCs) — live bestätigt.

## Protokoll

Zwei getrennte Module, gleiches Namensmuster-Verwechslungsrisiko wie [`AgpmCharacter`](../Module/AgpmCharacter.md)(`0x02`)/`AgcmCharacter`(`0x03`):

- **[`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md)** (Opcode `0x3B`, `APDEVENT_FUNCTION_SKILLMASTER = 25`): die Trainer-Interaktion. 1-Byte-Maske, Felder Operation/EventBase/CID/SkillID/SkillTID/Result/SkillPoint/InitFlag. Umgesetzte Operationen: `REQUEST_EVENT`/`RESPONSE_EVENT` (Trainer öffnen), `LEARN_SKILL`/`LEARN_RESULT` (Skill lernen). Bewusst nicht umgesetzt in dieser Runde: `BUY_SKILL_BOOK`, `REQUEST_UPGRADE`/`RESPONSE_UPGRADE`, `SKILL_INITIALIZE`/`_RESULT` (Respec) — nächste Schritte.
- **[`AgpmSkill`](../Module/AgpmSkill.md)** (Opcode `0x05`): die eigentliche "Charakter hat jetzt Skill X"-Synchronisation. 2-Byte-Maske, `ADD`-Operation mit SkillID/BasePacket/FactorPacket/TemplateID/Status. **Anfangs bewusst weggelassen** (das verschachtelte Factor-Unterpaket ist dieselbe Art Paket, die beim Monster-Rendering schon mal alles kaputt gemacht hat, siehe `monsters.rs`), dann nachgezogen, nachdem Live-Tests zeigten: ohne dieses Paket lernt der Client nie, dass ein Skill existiert — selbst der Default-Skill "Normal Attack" erschien nirgends. Risiko gemindert durch ein **komplett leeres** Factor-Unterpaket (Envelope-Maske 0, keine Felder) statt eines befüllten — architektonisch die einfachstmögliche Nutzlast. Live bestätigt: 37 gelernte Skills + der Default-Skill korrekt im Skillfenster sichtbar, in den Quickbelt ziehbar, mit Lern-Effektanimation.

NPC-Bindung läuft wie bei Repair/Dialog über [`ApmEventManager`](../Module/ApmEventManager.md), aber die Skillliste selbst kommt **nie über die Leitung** — der Client baut sie komplett lokal aus der eigenen `skillmastery.txt` auf, nur gekeyt über das Rasse+Klasse-Paar, das dem Trainer-NPC beim Binden als CustomData mitgegeben wird (`AgpdSkillEventAttachData`). Gleiches "Client weiß es schon"-Muster wie bei den generischen Dialogen.

## Echte Daten

Entschlüsselt aus `ini\skilltemplate.ini` (TID→Name-Register), `ini\skill_const.txt` (3,6 MB, ~270 Spalten Kampf-/Anforderungsdaten — nur Level-1-Zeile pro Skill importiert, siehe unten), `ini\skillmastery.txt` (10 echte Rasse+Klasse-Bäume, exakt deckungsgleich mit diesem Projekts bestehendem `character_templates`-Schema — Rasse 1-4/Klasse 1-4 bilden 1:1 auf "Human Knight/Archer/Mage", "Orc Berserker/Hunter/Sorcerer" usw. ab, keine Mapping-Tabelle nötig). Ergebnis: 220 echte Skills, 353 Baum-Zuordnungen, importiert in Migration `0028`.

40 echte Skill-Trainer-NPCs extrahiert aus `npc.ini`'s `Function=25`-Unterblöcken (gleiche Technik wie Repair/Trade) — jeder trägt sein eigenes `SkillRaceType`/`SkillClassType`-Paar (immer genau eins pro NPC, nie eine Liste).

## Zwei Vorbedingungs-Lücken, live gefunden und nachgezogen (gleiches Muster wie Repairs Haltbarkeit)

1. **`characters.skill_point` wurde nie befüllt** (Spalte seit Migration `0004`, Default 0) — kein Level-Up-Fluss existiert (kein Kampf → kein EXP-Gewinn → Level ist statisch). Migration `0029`: Backfill `level * 3` (echter Quellcode-Anker `AGPMCHAR_LEVELUP_SKILL_POINT = 3`, aber nur als GM-Tool-Sanity-Grenze bestätigt, nicht als echter Pro-Level-Betrag — versteht sich als Näherung, siehe "Offene Punkte").
2. **Der DIRT-Factor (Envelope-Bit 11, `AGPD_FACTORS_DIRT_TYPE_SKILL_POINT` = Bit 5 darin, unskalierter INT32) wurde nie gesendet** — live gemeldeter Bug: "keine Fertigkeitspunkte, alle skills inaktiv" trotz korrekt befülltem DB-Wert. Der Client hatte den Wert schlicht nie erhalten. Nachgezogen in `character.rs::build_factor_packet`.
3. **Kein Default-Skill** — `SKILL_DEFAULTOWN.TXT` bestätigt: jede der 13 echten CharTIDs bekommt genau "Normal Attack" (TID 222) als Startskill. Migration `0030` vergibt ihn an alle bestehenden Charaktere.

## Live bestätigt 2026-09-14

Blacksmith-artiger Test am Trainer: 37 Skills gelernt, exakte Übereinstimmung Log/DB:
- Skillpunkte: 99999 → 99962 (−37, genau 1 SP/Skill)
- Gold: 300478 → 88078 (−212400, exakte Summe aller `skill_cost`-Werte)
- `character_skills`: 38 Zeilen (37 gelernte + 1 Default)
- Normal Attack im Skillfenster sichtbar, in Quickbelt ziehbar, Lern-Animation ausgelöst
- 2 harmlose `WARN`-Zeilen für Skill-TID 526 (ein High-Level-Skill aus `SkillMastery_High.txt`, bewusst nicht importiert)

## Client-Start-Tooling

Neues `AlefLogin/tools/start_client.cmd`: startet `alefclient.exe` mit der Autologin-Bootstrap-Kommandozeile und führt danach `alef_login_tool.py login` aus (mit Retry-Logik, da der Kaltstart bis zur echten Login-Server-Verbindung länger dauern kann als das bloße Erscheinen des [`AgcmLogin`](../Module/AgcmLogin.md)-Moduls im Speicher).

## Migrationen

| # | Zweck |
|---|---|
| 0028 | `skill_templates`/`skill_mastery`/`character_skills`-Tabellen, 220 echte Skills, 353 Baum-Zuordnungen, 40 echte Trainer-NPCs |
| 0029 | Rückwirkende Skillpunkte-Vergabe (`level * 3`, Näherung) für bestehende Charaktere |
| 0030 | Default-Skill "Normal Attack" für alle bestehenden Charaktere |

## Offene Punkte

- **Echte Skillpunkte pro Level** statt der `level*3`-Näherung — der exakte Vergabe-Code wurde im echten Quellcode nicht gefunden (nur die GM-Tool-Sanity-Grenze).
- **Lernbare Skills mit echtem Level/Stufe** — aktuell wird nur Level 1 jedes Skills importiert (`skill_const.txt`s Level-1-Zeile); echte Skills haben bis zu 16 Stufen mit eigenen Anforderungen/Kosten pro Stufe. `REQUEST_UPGRADE`/`RESPONSE_UPGRADE` noch nicht implementiert.
- **Skill-Reset (Respec) über den Trainer-Dialog** — `SKILL_INITIALIZE`/`SKILL_INITIALIZE_RESULT` noch nicht implementiert.
- Skill-TID 526 (und generell alle High-Level-Skills aus `SkillMastery_High.txt`) nicht importiert.
- `BUY_SKILL_BOOK` (Skillbücher als Item statt Direktlernen) nicht implementiert.
- Quests bleiben pausiert bis zu einer Entscheidung zum Kampfsystem.
