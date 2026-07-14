# Archlord-Client-Daten — Format für Extraktion & Entschlüsselung

Reverse-engineerte Notizen dazu, wie Archlords Client-Daten gepackt und verschlüsselt sind und was nötig ist, um sie zu entschlüsseln. Dies beschreibt **nur das Format und den Prozess** — unabhängig von einer bestimmten Programmiersprache oder Implementierung. Diese Seite behandelt **ausschließlich Extraktion und Entschlüsselung**; die Interpretation der einzelnen entpackten Formate (Modelle, Texturen, Terrain usw.) ist ein eigenes Thema.

## 1. Drei Arten gepackter Daten

Eine Archlord-Client-Installation enthält drei Kategorien von Dateien, die entschlüsselt/entpackt werden müssen, jede mit einem anderen Mechanismus:

1. **Lose Dateien**, die direkt im Client-Verzeichnisbaum liegen — Konfigurations-/Textdaten (`.ini`, `.txt`, `.xml`) sowie bereits unverschlüsselte Assets (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`).
2. **DAT-Archive** — Paare aus `data.dat` (Roh-Nutzdaten) und `reference.dat` (verschlüsselte Dateitabelle), die viele Dateien bündeln.
3. **MagPack-Archive** (`.ma1`/`.ma2`, für Welt-/Terrain-Daten) — ein eigenständiges, komprimiertes (nicht RC4-verschlüsseltes) Containerformat, siehe Abschnitt 5.

Alternative Qualitätsvarianten der Assets liegen meist in Nachbarordnern namens `low` / `medium` und können in der Regel übersprungen werden, wenn nur die primären Assets relevant sind.

## 2. Verschlüsselungsschema (lose Dateien & DAT-Archive)

Alles RC4-Verschlüsselte nutzt dasselbe Prinzip: **RC4**, geschlüsselt mit dem **vollen MD5-Hash eines festen Passworts** (16 Bytes, direkt als RC4-Key verwendet). RC4 ist symmetrisch, die gleiche Operation ver- und entschlüsselt also:

```
key    = MD5(passwort)        # 16-Byte-Digest, komplett als RC4-Key verwendet
klar   = RC4(key, verschlüsselte_bytes)
```

Zwei Passwörter wurden identifiziert, die in unterschiedlichen Kontexten verwendet werden:

| Passwort | Verwendet für |
|---|---|
| `"1111"` | Lose `.ini`/`.txt`/`.xml`-Dateien, die Dateitabelle in jedem DAT-Archiv, sowie `.ini`/`.txt`/`.xml`-Einträge innerhalb eines DAT-Archivs |
| `"asdfqwer"` | `.tx1`-Einträge — sowohl lose als auch innerhalb eines DAT-Archivs |

Es gibt kein dateispezifisches Salt/Nonce — dasselbe Passwort/Key wird für jede Datei einer Art wiederverwendet, was Massenentschlüsselung überhaupt erst praktikabel macht. Dieses Schema gilt **nicht** für MagPack-Archive (Abschnitt 5), die einen anderen, nicht-RC4-basierten Mechanismus nutzen.

## 3. Lose Dateien

Nicht jede lose Datei ist tatsächlich verschlüsselt, auch wenn die Endung es vermuten lässt — manche `.ini`/`.txt`/`.xml`-Dateien liegen bereits als Klartext vor. Statt sich auf eine feste Liste von Dateinamen zu verlassen (brüchig und vermutlich unvollständig), ist der zuverlässige Ansatz eine **Inhaltsprüfung nach einem Entschlüsselungsversuch**:

1. Archivdateien selbst überspringen (`data.dat`, `reference.dat`) sowie alles, was eindeutig keine Spieldaten sind (Programme, DLLs, Systemdateien).
2. Bei Dateien mit "relevanter" Endung kommen nur `.ini` / `.txt` / `.xml` / `.tx1` als Entschlüsselungskandidaten infrage; andere relevante Endungen (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`) liegen bereits als Klardaten vor und müssen nur unverändert übernommen werden.
3. Für Kandidaten die RC4-Entschlüsselung durchführen. Danach das Ergebnis prüfen: Sieht es wie plausibler Klartext aus (beginnt mit einem typischen Marker wie `[` für eine INI-Sektion, `<` für XML, einem Kommentarzeichen oder einem Byte-Order-Mark; oder hat schlicht einen niedrigen Anteil nicht druckbarer Bytes im ersten Abschnitt)? Wenn ja, das entschlüsselte Ergebnis behalten. Sieht das "entschlüsselte" Ergebnis weiterhin nach Rauschen aus, lag die Datei bereits als Klartext vor (oder die Entschlüsselung mit diesem Key war falsch) — dann auf die ursprünglichen Rohdaten zurückfallen, statt Datenmüll zu schreiben.

Dieser heuristische Ansatz ist robuster als eine feste Liste vermeintlich bereits unverschlüsselter Dateinamen zu hinterlegen, da er sich selbst korrigiert statt Dateien, die nicht auf einer angenommenen Liste stehen, stillschweigend zu beschädigen.

## 4. DAT-Archive

Für jede `data.dat`, zu der eine `reference.dat` im selben Ordner existiert:

1. `reference.dat` vollständig einlesen und mit dem Passwort `"1111"` RC4-entschlüsseln.
2. Die entschlüsselten Bytes als Little-Endian-Binärtabelle parsen:
   - `uint32` — Anzahl der Dateien
   - `uint32` — Länge eines Ordnernamens, gefolgt von entsprechend vielen Bytes (der Name des Unterordners, in den alles aus diesem Archiv extrahiert werden soll)
   - danach, einmal pro Datei wiederholt: `uint32` Namenslänge + Name-Bytes, `uint32` Offset, `uint32` Größe — verweisen in `data.dat`
3. Für jeden Eintrag `size` Bytes aus `data.dat` ab `offset` lesen.
4. Diesen Block entschlüsseln, wenn die Endung es verlangt — dieselbe Endung-zu-Passwort-Zuordnung wie bei losen Dateien (`.ini`/`.txt`/`.xml` → `"1111"`, `.tx1` → `"asdfqwer"`). Alle anderen Endungen werden exakt so geschrieben, wie gespeichert (auch auf Archiv-Ebene nicht verschlüsselt).
5. Zwei Endungen werden beim Schreiben **umbenannt**, ohne jede Entschlüsselung — wirkt eher wie eine historische Tooling-Eigenheit als echte Verschlüsselung: `.bm1` → `.bmp`, `.pk` → `.wav`.

## 5. MagPack-Archive (`.ma1` / `.ma2`)

Welt-/Terrain-Daten liegen in einem komplett eigenständigen Containerformat, erkennbar am Magic-String `"MagPack Ver 0.1a"` am Dateianfang. Es nutzt **kein** RC4 — stattdessen kombiniert es eine einfache XOR-Verschleierung mit echter Kompression:

1. **Header** — 50 Bytes insgesamt, beginnend mit dem Magic-String `"MagPack Ver 0.1a"`.
2. **Directory** — folgt direkt auf den Header, ein Eintrag variabler Länge pro gepackter Datei, terminiert durch einen Eintrag der Länge Null:
   - `uint8` — Namenslänge; der Wert `0` markiert das Ende des Directory
   - Name-Bytes (ASCII, entsprechend lang)
   - `uint32` (Little-Endian) — gepackte Größe dieses Eintrags, **XOR-verschleiert mit der Maske `0x6969`**
3. **Daten-Blobs** — folgen nach dem Directory, einer pro Directory-Eintrag, in derselben Reihenfolge, direkt hintereinander:
   - erstes `uint32` des Blobs — entpackte (dekomprimierte) Größe, ebenfalls XOR-verschleiert mit `0x6969`
   - der Rest des Blobs (`packed_size` Bytes, inklusive dieses führenden Größenfelds) ist ein roher **aPLib**-komprimierter Stream (aPLib ist eine allgemeine Kompressionsbibliothek, historisch für platzsparendes/verschleiertes Packen genutzt; nicht etwas, das man von Grund auf neu implementieren sollte — einen vorhandenen aPLib-Dekompressor verwenden)
   - direkt nach jedem Blob folgt ein `uint32`-**Paritäts-/Prüfsummenwert** — dessen genauer Validierungsalgorithmus ist nicht bestätigt, muss zum erfolgreichen Entpacken aber nicht geprüft werden

Kurz gesagt: `Directory-Eintrag → Blob lokalisieren → aPLib-dekomprimieren → fertig`. Für dieses Format ist kein Passwort/Key nötig, nur die feste XOR-Maske.

## 6. Praktischer Ablauf

Eine vollständige Extraktion muss alle drei Mechanismen abdecken — sie sind logisch getrennt, und Daten verteilen sich auf alle drei, sodass die Implementierung von nur einem (z.B. nur der DAT-Archive) stillschweigend Daten zurücklässt:

1. Client-Installationsverzeichnis lokalisieren.
2. Rekursiv durchsuchen und dabei erfassen: lose Dateien, `reference.dat`/`data.dat`-Paare, sowie `.ma1`/`.ma2`-Dateien (Ordner `low`/`medium` überspringen, falls nicht benötigt).
3. Für lose Dateien: Entschlüsselung pro Endung versuchen und mit der Inhaltsprüfung aus Abschnitt 3 verifizieren.
4. Für jedes DAT-Archiv-Paar: die Referenztabelle entschlüsseln, parsen, dann jeden Eintrag wie in Abschnitt 4 beschrieben extrahieren und selektiv entschlüsseln.
5. Für jede MagPack-Datei: das Directory parsen, jeden Eintrag wie in Abschnitt 5 beschrieben aPLib-dekomprimieren.

Eine Referenzimplementierung dieses gesamten Prozesses existiert im Tooling des Projekts (siehe [../tools/](../tools/README.de.md)).

English version: [extraction.md](extraction.md)
