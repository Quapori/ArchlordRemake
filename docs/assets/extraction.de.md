# Archlord-Client-Daten extrahieren & entschlüsseln

Wie Archlords Client-Daten gepackt und verschlüsselt sind, und wie man sie mit dem Rust-Code aus [Archlord-AIO](https://github.com/Quapori/Archlord-AIO) entpackt. Diese Seite behandelt **ausschließlich Extraktion und Entschlüsselung** — die Konvertierung einzelner Formate (`.txd` → `.png`, `.dff` → `.gltf` usw.) wird von den anderen Archlord-AIO-Tools übernommen, nicht hier.

Alle Quellcode-Verweise unten beziehen sich auf `libs/shared_utils/src/*.rs` und `apps/extractor/src/main.rs` in Archlord-AIO.

## 1. Zwei Arten gepackter Daten

Eine Archlord-Client-Installation enthält zwei Kategorien von Dateien, die entschlüsselt/entpackt werden müssen:

1. **Lose Dateien**, die direkt im Client-Verzeichnisbaum liegen — `.ini`, `.txt`, `.xml`, sowie bereits unverschlüsselte Assets wie `.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`.
2. **Gepackte DAT-Archive** — Paare aus `data.dat` (Rohdaten) + `reference.dat` (verschlüsselte Dateitabelle), die viele Dateien bündeln, sowie `.ma1`/`.ma2`-Dateien.

`find_files()` (`file_utils.rs`) durchsucht das Client-Verzeichnis rekursiv nach beiden Arten und überspringt dabei Unterordner namens `low` oder `medium` (alternative Qualitätsvarianten der Assets).

## 2. Verschlüsselungsschema

Alles Verschlüsselte nutzt dasselbe Prinzip: **RC4**, geschlüsselt mit dem **MD5-Hash eines festen Passworts** (`decryption.rs`):

| Key | Passwort | Verwendet für |
|---|---|---|
| `DecryptKey::Default` | `"1111"` | Lose `.ini`/`.txt`/`.xml`-Dateien, die `reference.dat`-Tabelle jedes DAT-Archivs, sowie `.ini`-Einträge innerhalb eines DAT-Archivs |
| `DecryptKey::Texture` | `"asdfqwer"` | `.tx1`-Einträge innerhalb eines DAT-Archivs |

```rust
let key_hash = Md5::digest(password_bytes);
let mut cipher: Rc4<U16> = Rc4::new_from_slice(&key_hash).unwrap();
cipher.apply_keystream(buffer); // entschlüsselt in place
```

Es gibt kein dateispezifisches Salt/Nonce — dasselbe Passwort/Key wird für jede Datei einer Art wiederverwendet.

## 3. Lose Dateien

`process_regular_files()` (`file_utils.rs`) entscheidet pro Datei anhand ihres Namens, was zu tun ist (`should_skip_decryption()`):

| Regel | Dateien | Aktion |
|---|---|---|
| Ignorieren | `archlordgb.ini` | wird gar nicht kopiert |
| Nur kopieren | `ggpoint.ini`, `coption.ini`, `autopickup.xml`, `loginsettings.txt`, sowie jede `obj#####.ini` / `obs####.ini` (Regex `^obj\d{5}\.ini$\|^obs\d{4}\.ini$`) | unverändert kopiert — diese liegen schon als Klartext vor |
| Entschlüsseln | alles andere | RC4-entschlüsselt **nur wenn** die Endung `.ini`, `.txt` oder `.xml` ist (`FileExtension::should_decrypt()`); andere "relevante" Endungen (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`) werden unverändert kopiert, da sie ohnehin nicht verschlüsselt sind |

## 4. DAT-Archive

`extract_from_dat()` (`extraction.rs`), aufgerufen von `process_dat_files()` (`dat_utils.rs`), greift nur, wenn zu einer `data.dat` eine `reference.dat` im selben Ordner existiert:

1. `reference.dat` wird vollständig eingelesen und mit dem **Default**-Key RC4-entschlüsselt.
2. Die entschlüsselte Tabelle wird als Little-Endian-Binärdaten geparst: `u32` Dateianzahl → `u32` Länge des Ordnernamens + Ordnername (das Extraktions-Unterverzeichnis) → danach, pro Datei wiederholt: `u32` Namenslänge + Name, `u32` Offset, `u32` Größe.
3. Für jeden Eintrag werden `size` Bytes aus `data.dat` ab `offset` gelesen.
4. Nur zwei Endungen werden auf dieser Stufe entschlüsselt: `.ini` (Default-Key) und `.tx1` (Texture-Key). Alle anderen Endungen werden exakt so geschrieben, wie sie gespeichert sind.
5. Zwei Endungen werden beim Schreiben umbenannt (nicht entschlüsselt, nur umbenannt): `.bm1` → `.bmp`, `.pk` → `.wav`.
6. `.ma1`/`.ma2`-Dateien werden von `find_files()` erfasst, aber von diesem Code-Pfad **nicht** verarbeitet — dafür gibt es aktuell keine Entpack-Logik.

## 5. Extraktion durchführen

1. `extractor` (oder `core_main`) einmal starten — dabei wird automatisch eine `config.ini` neben der Binary erzeugt und in Notepad geöffnet:
   ```ini
   [PATHS]
   SOURCE=D:\Archlord-EMU\Webzen\Archlord
   DESTINATION=D:\Archlord-EMU\Rust-Export-Test
   ```
   `SOURCE` (deine Client-Installation) und `DESTINATION` eintragen, speichern, Enter drücken um fortzufahren.
2. Erneut starten, um die eigentliche Extraktion durchzuführen:
   ```bash
   cargo run -p extractor --release
   ```

> **Hinweis:** `extractor` ruft nur `process_dat_files()` auf — es entpackt und entschlüsselt die `data.dat`/`reference.dat`-Paare, ruft aber **nicht** `process_regular_files()` auf. Lose `.ini`/`.txt`/`.xml`-Dateien direkt im Client-Verzeichnisbaum bleiben von dieser Binary also unangetastet. Aktuell werden lose Dateien *und* DAT-Archive nur gemeinsam entschlüsselt, wenn man die komplette `core_main`-Pipeline laufen lässt — die aber zusätzlich fachfremde Konvertierungstools (`minimap`, `obj_checker`, `txd_converter`, `dff2gltf`) startet, was außerhalb des Fokus reiner Extraktion/Entschlüsselung liegt.

English version: [extraction.md](extraction.md)
