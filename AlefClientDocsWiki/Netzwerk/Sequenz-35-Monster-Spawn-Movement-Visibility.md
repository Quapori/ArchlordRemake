# WINSOCK_SEQUENCE_35: Echte Monsterdaten, Bewegung und fortlaufende Sichtbarkeit

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

## Kontext

Fortsetzung der Monster-Arbeiten nach `WINSOCK_SEQUENCE_30`. Ausgangszustand: Monster wurden aus einem groben, von `characterdatatable.txt` abgeleiteten Regelsatz erzeugt, einmalig bei `LOADING_COMPLETE` gesendet und bewegten sich nicht. Das Hauptproblem: Es wurden nur etwa 0 bis 1 Monster dargestellt, egal wie viele der Server sendete.

## Ursache 1: Namenskollision im Client (warum fast keine Monster erschienen)

Beleg: Disassembly/Pseudocode von `alefclient.exe` (nicht allein die Referenzquelle).

- `AgpmCharacter::AddCharacter` (`FUN_00507110`) legt jede neue Figur und jedes Monster in eine interne Hashtabelle nach CID **und Name** ein (`FUN_004ec3f0`, über `FUN_0058a420`).
- `FUN_004ec3f0` schlägt die eingehende GameID-**Zeichenkette** zuerst im Namensindex nach. Trägt ein anderes sichtbares Objekt bereits genau diesen Namen, wird das Hinzufügen stillschweigend verworfen (`goto LAB_004ec514; return 0;`), auch wenn die CID eindeutig ist. Deshalb erschienen von 97 bis 114 gesendeten Monstern mit eindeutiger CID nur etwa 0 bis 1: Sie trugen alle denselben allgemeinen Platzhalternamen.
- Umgehung (ebenfalls im Disassembly gefunden): In `FUN_00507110` erreicht der Namenszeiger die Kollisionsprüfung nur, wenn das erste Byte des Namenspuffers ungleich null ist. Eine **leere GameID** (Länge 0) macht den Zeiger zu NULL, `FUN_004ec3f0` überspringt die Namenssuche, und der Client zeigt den eigenen Vorlagennamen der Art (TID).

Das ist die umgesetzte Lösung: `build_monster_add_packet` (`monsters.rs`) sendet für jedes Monster eine leere GameID. Live bestätigt: Es erscheinen der richtige Artname und das Level, ohne sichtbare Indexnummern. Ein früheres Ergebnis „leerer Name bricht Yellow Worm“ war ein Störfaktor durch veraltete Positionsdaten, keine echte Regression (mit bereinigtem Zustand erneut getestet).

## Ursache 2: Echte Spawn- und Monsterdaten aus `worldmap-web/data.json`

Neue maßgebliche Datenquelle: `data.json` eines Weltkarten-Werkzeugs (`worldmap-web`; externe Datei, nicht Teil dieses Wikis) mit `npcs` (598 Zeilen) und `monsters` (12.411 Zeilen: `instance_id, spawn_name, tid, name, level, total_mob_count, is_boss, element, radius, x, z`).

Vor der Verwendung gegengeprüft: Die `npcs`-Koordinaten der Datei stimmen mit der bereits live bestätigten `npcs`-Tabelle des Projekts exakt überein (5 Stichproben-TIDs: 174, 175, 178, 582, 597). Das belegt dasselbe Koordinatensystem und stützt die `monsters`-Daten derselben Datei.

Übernommen über drei Migrationen (`crates/aleflogin-server/migrations/`):
- `0037_monster_spawn_rules_from_worldmap.sql` ersetzt den alten Regelsatz durch alle 12.404 echten Spawnpunkte (Position, Radius, echter Artname, echte Platzzahl). `position_y` ist 0 (die Datei enthält keine Höhendaten; dokumentierte Vereinfachung).
- `0038_monster_templates_from_worldmap.sql` beschränkt `monster_templates` auf die 1.265 TIDs, die die neuen Spawnregeln tatsächlich verwenden; Quelle ist die `CharacterDataTable.txt` der EP8-Server-Quelle.
- `0039_monster_move_speed.sql` ergänzt `move_walk`/`move_run` in `monster_templates`.

`MONSTER_VISIBILITY_RADIUS` (`monsters.rs`) steht nach erneuten Tests mit dem dichteren echten Datensatz bei `20_000.0` (Verlauf als Kommentar an der Konstante).

## Ursache 3: Monster hatten keine Bewegung

`AgpmCharacter::GetMoveSpeed` liest ein Bewegungsfeld aus dem Factor-Paket; fehlt es, verwendet der Client einen allgemeinen Ersatzwert. Das Monster-Factor-Paket des Projekts hatte **nie Bewegungsfelder gesendet**. Das wurde als eigentliche Ursache (kein Fehler im CharMove-Handler) bestätigt, nachdem der Bericht `WINSOCK_SEQUENCE_30` erneut gelesen und serverseitige Fehler über `gameserver.log` ausgeschlossen waren (Wanderberechnung und Socket-Schreibzugriffe des Servers waren korrekt).

Nach der Behebung bewegten sich die Monster viel zu schnell. Korrektur: Import der **echten `Movement Walk`/`Movement Run`-Werte je TID** aus der entschlüsselten `characterdatatable.txt` des Clients (RC4-Schlüssel `1111`, siehe [Datenentschlüsselung](../Daten-und-Werkzeuge/Datenentschluesselung.md)) statt eines festen Spieler-Platzhalters (`2000`/`6000`). Beispiel: Die echte Gehgeschwindigkeit von Green/Yellow Worm ist `450`, etwa 4,4-mal langsamer als der Platzhalter. Die Werte stimmen mit der Kopie derselben Tabelle in der EP8-Server-Quelle überein.

Bewegungsstrecke (aus `WINSOCK_SEQUENCE_30`, dort per Disassembly bestätigt): `distance = elapsed_ms * (moveSpeed / 10000.0)`, umgesetzt als `combat::wander_step_distance(move_walk)`.

## Grundsatz: Client-Daten 1:1 in die Datenbank übernehmen

Daten, die bereits in den Dateien des Clients stehen (`characterdatatable.txt`, `charactertemplate*.ini`), werden 1:1 in die Server-Datenbank übernommen, statt neu erfunden zu werden; so passen die gesendeten Pakete zu den Werten, die der Client erwartet. Das gilt für Monster- und Charakter-Statuswerte (Fortschrittstabellen bleiben serverseitig maßgeblich). Weitere entschlüsselte `charactertemplate*.ini`-Dateien (public, client, animation, customize, eventeffect, skill, skillsound) sind über die Bewegungsgeschwindigkeit hinaus noch nicht ausgewertet.

## Fortlaufende Sichtbarkeit beim Laufen

Zuvor wurden Monster nur einmal bei `LOADING_COMPLETE` gesendet; beim Weglaufen vom Spawnpunkt erschienen keine neuen Monster. Neue Architektur:
- `ConnState` (`net.rs`) hat zusätzlich `known_monster_cids: HashSet<i64>` und `last_monster_refresh: Option<Instant>`.
- `movement::handle_optimized_char_move` ruft `ensure_and_list_monsters_near` an der aktuellen Spielerposition erneut auf (gedrosselt auf alle 3 s, `MONSTER_REFRESH_INTERVAL`), vergleicht mit `known_monster_cids` und sendet ADD+HP für neu sichtbare und `REMOVE_FOR_VIEW` für nicht mehr sichtbare Monster.

Live bestätigt: Monster erscheinen fortlaufend beim Laufen, auch eine bisher nicht gesehene Art (Flame Bat, Feuerelement-Monster) mit korrekt gefüllten Angriffs- und Resistenzangaben und korrekter Zielinfobox. Damit ist die Kette Spawn, Vorlage, Anzeige durchgehend stimmig.

## Wanderbewegung im Leerlauf

Echte Wegpunktdaten je Spawn liegen nicht vor (das `AgpmMonsterPath`-System der Referenzquelle existiert, ein passender Wegpunktdatensatz fehlt). Umgesetzt ist eine dokumentierte Vereinfachung: `combat::spawn_wander_sweep` wählt einen Zufallspunkt innerhalb von `spawn_radius` um die Spawnposition und läuft mit der echten Geschwindigkeit je TID darauf zu, per `CharMove`-Paketen. Das ist ausdrücklich keine Nachbildung echter Wegfindung.

## Offen / zurückgestellt

- **Angriffs-Zielsperre** („Fertigkeit unmöglich bei diesem Ziel“): Per Disassembly ist belegt, dass `m_unActionStatus` (Offset `+0x52A`) standardmäßig `3` ist (nicht `NORMAL=0` wie in der Referenzquelle). Der Server sendet nun `MONSTER_ACTION_STATUS_ALIVE = 3` ausdrücklich, das allein löste die Sperre nicht. Weitere Disassembly-Arbeit am Prüfpfad für Angriff/Fertigkeitsziel ist nötig.
- **Monster-Aggro und KI**: Echte Daten (`MonsterAI.txt`, 7.678 Zeilen) und echte Serverlogik (`AgsmAI2.cpp`: `GetTargetPC`, `FindEnemyTarget`, `PreemptiveType`, `PreemptiveRange`) sind als Quellen identifiziert, aber nicht umgesetzt (vorerst nur spielerinitiierter Kampf).
- **Echte Wegpunkt-Patrouillen**: keine Wegpunktdaten vorhanden; die Wanderbewegung ist eine Vereinfachung.
- **Übrige `charactertemplate*.ini`**: entschlüsselt, aber nicht auf weitere importierbare Daten untersucht (z. B. Animations-Abspielraten, die den Eindruck „Animation etwas zu schnell“ verfeinern könnten).
