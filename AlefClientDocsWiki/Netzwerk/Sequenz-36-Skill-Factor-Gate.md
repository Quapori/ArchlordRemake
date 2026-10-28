# Skill-Faktoren und blockierte Angriffe — 2026-09-23

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

## Auftrag und Beweismaßstab

Vorhandenen Client-Pseudocode mit Laufzeitmessungen und den tatsächlich
verwendeten Daten verbinden. EMU-Quellen dienen zum Vergleich; sie sind keine
Original-Serverquellen. Ein plausibler Funktionsname allein ist kein Laufzeitbeweis.

## Reproduzierter Fehler vor der Korrektur

Client PID 40944, Charakter-CID 3, Ziel-CID 7420004. Der Benutzer stand neben
einem anvisierten Monster und betätigte normalen Angriff, Dual Slash und Skill 57.
Messungen: `analysis/skill_gate_20260923_live_before.jsonl` und
`analysis/skill_gate_20260923_factor_location.jsonl` (UTC-Zeitstempel).

Installierte EXE: `C:\Spiele\Archlord\alefclient.exe`, SHA-256
`0336f7978c258c3121d115c0bdc14be410f85003ebc8dd8181c276cde13d4fbc`.
Imagebase zur Laufzeit: `0x400000`, Architektur ia32.
Keine EXE-Datei und keine Spielwerte wurden für diese Messungen verändert.
Frida setzt temporäre Hooks ausschließlich an Funktionseinstiegen und entfernt
sie beim Detach. Keine Hooks mitten in Instruktionen, keine ersetzten Rückgaben.

### 1. DIRT landet im falschen Teil des Skillobjekts

Direkte Speicherbeobachtung bei `GetSkillByTID` und der Zielprüfung:

| TID | Instanz-CID | direktes DIRT | Result/DIRT Level | Result/DIRT Punkte |
| --- | --- | --- | --- | --- |
| 1 | 6030001 | NULL | 1 | 1 |
| 57 | 6030057 | NULL | 1 | 1 |
| 222 | 6030222 | NULL | 0 | 0 |

`AgpdSkill` enthält den Faktor bei `skill+0x30`. `GetFactor` (`0050bc00`)
liefert `*(factor+8+type*4)` ohne automatischen Wechsel zum Result-Faktor.
DIRT ist Typ 11; direkter DIRT-Zeiger somit `*(skill+0x64)`.
Result ist Typ 0 (`*(skill+0x38)`).

Rust hatte den Skill-Faktor wie einen Charakter-Faktor aufgebaut:
`Factor -> Result -> DIRT`. Die untersuchten Skillfunktionen lesen dagegen
`Factor -> DIRT`. Das Paket war syntaktisch lesbar, legte die Werte aber an
der falschen Stelle ab. Das erklärt, warum ein Skill sichtbar sein konnte,
während sein Level für die Reichweitenberechnung fehlte.

### 2. Nachgewiesene Ablehnungskette für Skill 57

Beispiel erster Trace, 20:09:01 UTC, Ereignisse 13–16:

1. `0066d670` (CastSkill) fordert TID 57 für Ziel 7420004 an.
2. `00566190` (IsValidTarget) prüft Instanz 6030057.
3. `005644c0` (GetRange) ruft Callback-ID 31 auf Modul `0x10bb0048` auf.
4. Die registrierte Callback-Kette enthält `006ca220`, Objekt `0x1180a4c0`.
5. Dieser Callback ruft `0050c410(skill+0x30, out, 11, 4, -1, -1)` auf.
6. GetValue liefert **0 = fehlgeschlagen**. Der vorher auf 0 gesetzte
   Ausgabeparameter bleibt 0. Der Callback selbst liefert trotzdem 1.
7. GetRange liefert 0; IsValidTarget liefert Byte 1; CastSkill liefert 0.

Damit ist die frühere Deutung in `combat.rs` widerlegt: Callback 31 beantwortet
hier keine Frage nach einem gültigen Ziel. Er liefert die wirksame Skillstufe.
Die ID ist außerdem nur zusammen mit dem jeweiligen Modul aussagekräftig.
`006ca220` ist in der Disassembly vorhanden, obwohl der Pseudocode diesen
Eintritt als `LAB_006ca220` referenziert. Das ist ein Beispiel dafür, warum die
Anzahl exportierter FUN-Funktionen nicht der Zahl aller untersuchten Routinen
gleichgesetzt werden darf.

### 3. Kostenloser normaler Angriff benötigt getrennte Werte

Nur lesende DB-Abfrage während des Tests:

```sql
BEGIN READ ONLY;
SELECT cs.character_id, cs.skill_tid, cs.level,
       SUM(st.require_point) AS sent_level_and_points
FROM character_skills cs
LEFT JOIN skill_templates st
  ON st.tid = cs.skill_tid AND st.level <= cs.level
WHERE cs.character_id = 3
GROUP BY cs.character_id, cs.skill_tid, cs.level
ORDER BY cs.skill_tid;
COMMIT;
```

Ergebnis: TID 1: Level 1 / Kosten 1; TID 57: Level 1 / Kosten 1;
TID 222: Level 1 / Kosten 0. Die bisherige Paketfunktion verwendete die
aufsummierten Kosten sowohl als SkillLevel als auch als SkillPoint.
Die Gleichsetzung ist für TID 222 bereits anhand dieser Daten falsch.

**Abgrenzung:** Der normale Angriff erreichte in diesen beiden Messungen die
Skill-Zielprüfung nicht. Sein Skillobjekt existiert und zeigt ebenfalls das
falsche Faktorlayout. Die anschließende Paket- und Codeanalyse erklärt den
separaten Pfad; siehe unten. `CastSkill=true` allein beweist keinen Paketversand.

## Korrektur

- `skills.rs`: Skill-ADD sendet DIRT direkt im Faktor-Envelope (Bit 11).
- SkillLevel wird aus dem gespeicherten Rang gesetzt, SkillPoint aus den
  investierten Punkten. Beim erstmaligen Lernen ist der Rang 1.
- `session.rs`: übergibt beim Login/Re-ADD beide Werte getrennt.
- Regressionstest prüft im vollständigen ADD-Paket die festen Wire-Bytes für
  einen kostenlosen Skill: direktes DIRT, Level 1, Punkte 0, TID 222.
- Charakter-Faktorpakete und vorhandenes REMOVE-vor-ADD bleiben unverändert.

Die EMU-Vergleichsquelle auf D: bestätigt die direkte DIRT-Abfrage in
[`AgcmUISkill2`](../Module/AgcmUISkill2.md):CBGetSkillLevel` (Zeile 4525). [`AgpmSkill`](../Module/AgpmSkill.md):MakePacketSkill`
serialisiert `m_csFactor` direkt. Maßgeblicher Nachweis ist jedoch die oben
aufgeführte Disassembly plus Laufzeitmessung, nicht die Gleichheit der EMU-Versionen.

## Validierung und offene Fortsetzung

`cargo test --workspace --offline --locked` nach der Korrektur: **39 Tests
erfolgreich** (18 Gameserver, 8 Crypto, 9 Proto, 4 Loginserver).
Vollständiges Ergebnis: `analysis/skill_gate_workspace_tests.txt`.
`cargo build -p alefgame-server --offline --locked` erfolgreich, 27 bestehende
Dead-Code-Warnungen; `analysis/skill_gate_build.txt`. `git diff --check` ohne
Whitespace-Fehler.

### Gegenprobe nach Neustart: bestätigt

Benutzer regulär ausgeloggt; alter lokaler Gameserver PID 31248 beendet,
korrigierter Build als PID 11484 mit unverändertem Standardport 11008 gestartet.
Client PID 40944 blieb derselbe. Benutzer erneut eingeloggt und gleiche drei
Skills gegen Ziel 7420004 versucht. Neue Logs:

- `analysis/skill_gate_20260923_after.jsonl` (20:16:30–20:18:30 UTC).
- `analysis/skill_gate_gameserver.log` (Server einschließlich empfangener Frames).
- `analysis/skill_gate_packets_after.json` (gezielter Auszug eingehender
  Pakete 0x05 und 0x41 im Messfenster).

Alle drei Skills besitzen jetzt direktes DIRT. Level/Punkte: TID 1 = 1/1,
TID 57 = 1/1, TID 222 = 1/0. Bei den 17 gemessenen Skill-Zielprüfungen:
GetValue erfolgreich; Callback-Level immer 1; Reichweite neunmal 200 und
achtmal 500; IsValidTarget sechzehnmal 2 (nicht in Reichweite), einmal 0
(gültig), **keinmal 1**. Alle 17 Aufrufe erzeugen ein Aktionspaket.
Der Client lässt sowohl 0 als auch 2 zum Versand passieren; dies beweist
noch keine serverseitige Bewegung zum Ziel oder Schadensberechnung.

Der Server empfängt im gleichen Messfenster **17 Pakete 0x05, Operation 7**,
TIDs 1 und 57. Beispiel 20:16:59.874043 UTC, Quelllog Zeile 9561:

```text
d6 3b 00 05 00 03 00 00 00 5c 02 0c 00 57 00 07
b1 02 5c 00 06 00 03 03 03 00 00 00 01 00 00 00
18 00 0b 02 00 06 00 03 03 64 38 71 00 15 0f d0
c8 49 72 64 45 7d 1d 85 47 01 6b
```

Länge 59, Modul 5, Maske 0x57, Operation 7, Skillinstanz 6030001,
Owner ApBase Typ 3 / CID 3, Skill-TID 1, Action-Teilpaket. Die nach dem
Frame im ursprünglichen Decrypt-Log stehenden fünf Padding-Bytes gehören
nicht zur Paketlänge. Die Position und weiteren Action-Bits sind im Auszug
verlustfrei erhalten; daraus wird hier keine Schadensregel abgeleitet.

### Normaler Angriff: eigener Weg, schon vorher auf dem Server angekommen

`00669f20` entspricht der Vorverarbeitung des Skills. Beim Auto-Attack-Flag
an `template+0x9948` erfolgt Zielbindung über `005a30e0` und
Charakteraktion über `005a52c0`, anschließend Rückgabe 1. Dieser Weg umgeht
die oben untersuchte Skill-Zielprüfung absichtlich.

Statische Kette im Client: `005a52c0 -> 005a0860 -> 0057d890`.
Letztere Funktion baut ausdrücklich Opcode **0x41**. Die EMU-Vergleichsquelle
[`AgcmSkill`](../Module/AgcmSkill.md):PreProcessSkill` beschreibt denselben Auto-Attack-Zweig;
[`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md):MakePacketCharAction` dieselbe Paketmaske.

Nach Neustart um 20:16:50.088918 UTC, während der normalen Angriffsversuche:

```text
d6 19 00 41 00 03 00 00 00 23 dc 0b 00 23 00 03
00 00 00 64 38 71 00 01 6b
```

Länge 25, Opcode 0x41, Maske 0x23: CharacterID=3, TargetID=7420004,
ComboInfo=1. Kein ForceAttack-, Schadens- oder HP-Feld in diesem Request.
Im Nachher-Messfenster liegen insgesamt 70 eingehende 0x41-Frames vor.
Diese Gesamtzahl umfasst auch Pakete außerhalb einzelner manueller Klicks.

Entscheidend: Ein gezielter Auszug aus dem **vorherigen** Gameserverlog für
20:08:49–20:13:07 UTC enthält bereits **298 Pakete 0x41, aber kein Paket 0x05**.
Gesichert in `analysis/skill_gate_packets_before.json`.
Die frühere pauschale Aussage „kein Angriffspaket erreicht den Server“ ist
damit widerlegt. Für Skills 1/57 war die Faktorblockade real; normaler Angriff
hatte bereits einen anderen, empfangenen Netzwerkpfad.

### Nächste belegte Baustelle

`dispatch.rs::decrypt_and_respond` besitzt weder einen Zweig für Opcode 0x05
noch für 0x41. Beide fallen durch `_ => Ok(())`. Deshalb führt der Eingang
dieser Pakete derzeit keine Kampfverarbeitung aus. Es fehlt kein unbekannter
Opcode mehr für diese beiden beobachteten Request-Pfade.

Noch umzusetzen und gegen Code/Daten zu verifizieren:

1. Begrenzte, robuste Parser für beide beobachteten Request-Formate; Owner
   gegen authentifizierte Arbeitsphase, Skillbesitz und Zielinstanz prüfen.
2. Serverseitige Reichweite, Bewegung zum Ziel, Aktionsreihenfolge und
   Zeitbedingungen rekonstruieren. Ergebnis 2 bedeutet keine Trefferfreigabe.
3. Die benötigten Serverantworten samt Animation/HP-Update am Client prüfen.
4. Erst danach Schadens-, Kosten-, Cooldown-, Todes- und Belohnungsregeln
   anbinden. Die vorhandenen `combat.rs`-Hilfsfunktionen sind hierfür kein
   Nachweis originalgetreuer Regeln.

Keine unbewiesene Kampfantwort wurde implementiert. Die bisherige Änderung
behebt nachweislich die Skill-Faktorübertragung; vollständiger Kampf ist offen.

## Reproduzierbare Messung

`AlefLogin/tools/observe_skill_gate.py` und gleichnamige `.js`-Datei.
Python benötigt `frida` und `pefile`. Beispiel (aktuelle PID einsetzen):

```powershell
& 'C:\Program Files\Python313\python.exe' AlefLogin/tools/observe_skill_gate.py `
  --pid 40944 --seconds 90 --output analysis/skill_gate_retest.jsonl
```

Der Outputpfad darf noch nicht existieren. Alle Hook-Adressen werden vor dem
Attach mit den ersten acht Bytes der angegebenen lokalen EXE verglichen.
Das schützt gegen bereits veränderte Einstiegspunkte, ersetzt aber keine
Prüfung, ob eine andere EXE-Version dieselben Funktionsadressen verwendet.
Die erste Sandbox-Ausführung scheiterte am Prozesszugriff und erzeugte nur
Metadaten (`skill_gate_20260923_before.jsonl`). Die beiden vollständigen
Vorher-Messungen und die Nachher-Messung liefen mit genehmigtem Prozesszugriff
außerhalb der Sandbox. Alle drei endeten mit Detach, ohne Frida-Fehlermeldung.

Gezielte Paketextraktion ohne Login-/Authentifizierungsframes:

```powershell
& 'C:\Program Files\Python313\python.exe' AlefLogin/tools/extract_combat_packets.py `
  analysis/skill_gate_gameserver.log --since 2026-09-23T20:16:30 `
  --until 2026-09-23T20:18:30 --output analysis/skill_gate_packets_after.json
```

Auch dieses Werkzeug überschreibt keine bestehende Ausgabedatei. Die angegebenen
Messfenster sind verschieden lang; die Paketzahlen sind keine Ratenmessung.
