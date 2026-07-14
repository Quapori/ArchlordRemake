# Archlord-Client-Daten — Format für Extraktion & Entschlüsselung

Reverse-engineerte Notizen dazu, wie Archlords Client-Daten gepackt und verschlüsselt sind und was nötig ist, um sie zu entschlüsseln. Dies beschreibt **nur das Format und den Prozess** — unabhängig von einer bestimmten Programmiersprache oder Implementierung. Diese Seite behandelt **ausschließlich Extraktion und Entschlüsselung**; die Interpretation der einzelnen entpackten Formate (Modelle, Texturen, Terrain usw.) ist ein eigenes Thema.

## 1. Zwei Arten gepackter Daten

Eine Archlord-Client-Installation enthält zwei Kategorien von Dateien, die entschlüsselt/entpackt werden müssen:

1. **Lose Dateien**, die direkt im Client-Verzeichnisbaum liegen — Konfigurations-/Textdaten (`.ini`, `.txt`, `.xml`) sowie bereits unverschlüsselte Assets (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`).
2. **Gepackte Archive** — Paare aus `data.dat` (Roh-Nutzdaten) und `reference.dat` (verschlüsselte Dateitabelle), die viele Dateien bündeln. Daneben existieren auch `.ma1`/`.ma2`-Dateien, deren internes Format bisher nicht reverse-engineert wurde — dafür gibt es bislang keine bekannte Entpack-Methode.

Beim Durchsuchen einer Client-Installation nach diesen Dateien liegen alternative Qualitätsvarianten der Assets meist in Nachbarordnern namens `low` / `medium` und können in der Regel übersprungen werden, wenn nur die primären Assets relevant sind.

## 2. Verschlüsselungsschema

Alles Verschlüsselte nutzt dasselbe Prinzip: **RC4**, geschlüsselt mit dem **MD5-Hash eines festen Passworts**. RC4 ist symmetrisch, die gleiche Operation ver- und entschlüsselt also:

```
key    = MD5(passwort)
klar   = RC4(key, verschlüsselte_bytes)
```

Zwei Passwörter wurden identifiziert, die in unterschiedlichen Kontexten verwendet werden:

| Passwort | Verwendet für |
|---|---|
| `"1111"` | Lose `.ini`/`.txt`/`.xml`-Dateien, die Dateitabelle in jedem Archiv (siehe unten), sowie `.ini`-Einträge innerhalb eines Archivs |
| `"asdfqwer"` | `.tx1`-Einträge innerhalb eines Archivs |

Es gibt kein dateispezifisches Salt/Nonce — dasselbe Passwort/Key wird für jede Datei einer Art wiederverwendet, was Massenentschlüsselung überhaupt erst praktikabel macht.

## 3. Lose Dateien

Nicht jede lose Datei braucht dieselbe Behandlung; die Regeln scheinen auf Dateiname und Endung zu basieren:

| Regel | Dateien | Aktion |
|---|---|---|
| Ignorieren | eine bestimmte Datei (eine `.ini` mit Region-/Build-Info) | wird komplett übersprungen |
| Nur kopieren | eine Handvoll bestimmter Konfigurationsdateien (z.B. Login-/UI-Einstellungen), sowie jede Datei, die dem Muster eines Objektvorlagen-Index entspricht (`obj#####.ini` / `obs####.ini`) | unverändert kopiert — liegen trotz der Endung schon als Klartext vor |
| Entschlüsseln | alles andere mit "relevanter" Endung | nur `.ini` / `.txt` / `.xml` sind tatsächlich verschlüsselt und brauchen den RC4-Schritt; andere relevante Endungen (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`) liegen bereits als Klardaten vor und müssen nur unverändert übernommen werden |

Kurz gesagt: Verschlüsselung im losen Dateibaum beschränkt sich auf Text-/Konfigurationsdaten — binäre Assets sind nicht verschlüsselt, sondern liegen nur neben den verschlüsselten Dateien.

## 4. Gepackte Archive

Für jede `data.dat`, zu der eine `reference.dat` im selben Ordner existiert:

1. `reference.dat` vollständig einlesen und mit dem Passwort `"1111"` RC4-entschlüsseln.
2. Die entschlüsselten Bytes als Little-Endian-Binärtabelle parsen:
   - `uint32` — Anzahl der Dateien
   - `uint32` — Länge eines Ordnernamens, gefolgt von entsprechend vielen Bytes (der Name des Unterordners, in den alles aus diesem Archiv extrahiert werden soll)
   - danach, einmal pro Datei wiederholt: `uint32` Namenslänge + Name-Bytes, `uint32` Offset, `uint32` Größe — verweisen in `data.dat`
3. Für jeden Eintrag `size` Bytes aus `data.dat` ab `offset` lesen.
4. Diesen Block nur entschlüsseln, wenn die Endung es verlangt: `.ini` → RC4 mit `"1111"`, `.tx1` → RC4 mit `"asdfqwer"`. Alle anderen Endungen werden exakt so geschrieben, wie gespeichert (auch auf Archiv-Ebene nicht verschlüsselt).
5. Zwei Endungen werden beim Schreiben **umbenannt**, ohne jede Entschlüsselung — wirkt eher wie eine historische Tooling-Eigenheit als echte Verschlüsselung: `.bm1` → `.bmp`, `.pk` → `.wav`.

## 5. Praktischer Ablauf

1. Client-Installationsverzeichnis lokalisieren.
2. Rekursiv durchsuchen und dabei sowohl lose Dateien als auch Archiv-Paare erfassen (Ordner `low`/`medium` überspringen, falls nicht benötigt).
3. Für lose Dateien: die Ignorieren-/Nur-kopieren-/Entschlüsseln-Regeln aus Abschnitt 3 anwenden.
4. Für jedes `data.dat` + `reference.dat`-Paar: die Referenztabelle entschlüsseln, parsen, dann jeden Eintrag wie in Abschnitt 4 beschrieben extrahieren und selektiv entschlüsseln.

> **Worauf zu achten ist:** Es passiert leicht, dass ein Tool nur die Hälfte davon umsetzt (z.B. nur die Archive entpackt) und man annimmt, der Client sei vollständig extrahiert. Lose Konfigurationsdateien und archivierte Dateien sind zwei getrennte Verarbeitungswege — stelle sicher, dass beide tatsächlich abgedeckt sind, sonst landet man bei einer unvollständigen Extraktion, die auf den ersten Blick vollständig aussieht.

Eine Referenzimplementierung dieses gesamten Prozesses existiert im Tooling des Projekts (siehe [../tools/](../tools/README.de.md)).

English version: [extraction.md](extraction.md)
