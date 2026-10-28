# AuPackingManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuPackingManager` (Dateien aus gepackten Ordnern lesen: `Data.Dat` je Ordner mit Verweisdatei) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionsübersicht (`fcalls.py`), Zeichenketten (`root`, `Data.Dat`, `rb+`, `%s\%s`), EP8-Quelle `Modules/AUtility/AuPackingManager/AuPackingManager.cpp`. Alle Adressen gelten nur für den 2017er Build. Die Klasse hat keine Vtable (kein RTTI). Die JZP-Patchdateien (`Patch%04d.JZP`, `ZipDirs`) kommen im Binary nicht vor: der Client benutzt nur den Lesepfad.

## Kernbefund

- **Abdeckung:** 9 von 63 Quellmethoden zugeordnet (Lesepfad: `OpenFile` (beide), `ReadFile`, `SetPos`, `GetFileSize(ApdFile)`, `CloseFile`, `Lock`, `SetFilePointer`, `ResizeDatFile`), dazu `ResizeDatFile`, das `Data.Dat` auf die Sollgröße kürzt.
- **Nicht gefunden:** alle Bau- und Pflegefunktionen (`BuildJZPFile`, `BuildReferenceFile`, `CompletePacking`, `ReadBakReference`, `UpdateDatAndRefFileFromJZP` …), die Ignorier- und Cracked-Listen, die Singleton-Funktionen und `LoadReferenceFile`/`ReadReferenceFile` (die Verweisdatei wird im 2017er Client nicht über diese Funktionen gelesen – die Zeichenketten der Packer sind im Binary nicht vorhanden).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuPackingManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Destroy` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 1 | `GetFolderInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 2 | `GetPatchList` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 3 | `IsCheckedBuildJZP` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 4 | `IsCheckedBuildDat` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 5 | `IsCheckedCopyRawFiles` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 6 | `SetBuildJZP` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 7 | `SetBuildDat` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 8 | `SetCopyRawFiles` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 9 | `MakeInstance` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 10 | `DestroyInstance` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 11 | `GetSingletonPtr` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 12 | `LoadIgnoreFileInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 13 | `AddIgnoreFileName` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 14 | `RemoveIgnoreFileName` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 15 | `IsIgnoreFileName` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 16 | `GetIgnoreFileInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 17 | `AddCrackedFolderName` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 18 | `RemoveCrackedFolderName` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 19 | `GetCrackedFolderInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 20 | `GetLastVersion` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 21 | `GetPatchInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 22 | `AddFolder` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 23 | `AddFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 24 | `AddPackingFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 25 | `GetFolder` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 26 | `GetFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 27 | `AddPatch` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 28 | `BuildJZPFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 29 | `LoadResFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 30 | `BuildReferenceFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 31 | `MarkPacking` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 32 | `MarkPackingComplete` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 33 | `LoadReferenceFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 34 | `LoadReferenceFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 35 | `ReadReferenceFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 36 | `SetFilePointer` | `0x004EE1A0` | 265 | von Hand geprüft |
| 37 | `CloseAllFileHandle` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 38 | `BuildDatFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 39 | `UpdateDatAndRefFileFromJZP` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 40 | `GetFolderName` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 41 | `CreateFolder` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 42 | `GetJZPInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 43 | `GetFileSize` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 44 | `GetFileSize` | `0x004EE2B0` | 245 | von Hand geprüft |
| 45 | `OpenFile` | `0x004EEF00` | 208 | von Hand geprüft |
| 46 | `OpenFile` | `0x004EEA00` | 336 | von Hand geprüft |
| 47 | `ReadFile` | `0x004EE3B0` | 139 | von Hand geprüft |
| 48 | `SetPos` | `0x004EE440` | 133 | von Hand geprüft |
| 49 | `CloseFile` | `0x004EEB50` | 76 | von Hand geprüft |
| 50 | `Lock` | `0x004EE4D0` | 30 | von Hand geprüft |
| 51 | `Unlock` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 52 | `CreateEmptyFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 53 | `ReadyPacking` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 54 | `CompletePacking` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 55 | `CompletePacking` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 56 | `BuildPackingFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 57 | `BuildPackingFile` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 58 | `ReadBakReference` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 59 | `AddEmptyPackingFileInfo` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 60 | `ResizeFileSize` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |
| 61 | `ResizeDatFile` | `0x004EE4F0` | 355 | von Hand geprüft |
| 62 | `CompleteCurrentFolderProcess` | – | | nicht im Binary gefunden; Verbleib offen (Bau- und Pflegefunktionen des Packers gehören in der Quelle zum Editor und zum Patcher) |

9 von 63 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `GetFileSize_apd` (`0x004EE2B0`), `OpenFile_name` (`0x004EEA00`).

## Lesepfad

Die Funktionen liegen im Block `0x004EE000`–`0x004EF400`, gleich hinter `AuNPWrapper`. Ein Ordner hat den Namen bei `+0xF0` (`root` für den Wurzelordner), das Handle der Datei `Data.Dat` bei `+0xF4` und die Größe bei `+0xF8`. `SetFilePointer` (`0x004EE1A0`, 265 Byte) öffnet für alle Ordner der Verwaltung (`ApAdmin::GetObjectSequence`) die Datei `Ordner/Data.Dat` (Wurzel: ohne Ordner) mit `rb+` oder `rb`, je nach Schalter. `OpenFile(Pfad, Datei)` (`0x004EEF00`) zerlegt den Pfad (`_splitpath`) und ruft `OpenFile(Ordner, Name, Datei, Pfad)` (`0x004EEA00`, 336 Byte): bei vorhandenem Verweis wird die Lage in `Data.Dat` übernommen (Startposition `Verweis+0x14`), sonst die Datei lose geöffnet (`fopen`).
`ReadFile` (`0x004EE3B0`, 22 Aufrufer) liest aus `Data.Dat` des Ordners oder aus der losen Datei (`+0x214`) und zählt die gelesene Länge; `SetPos` (`0x004EE440`) setzt die Position in der gepackten oder losen Datei; `GetFileSize(ApdFile)` (`0x004EE2B0`) liefert die gepackte Größe (Verweis `+4`) oder die Größe der losen Datei; `Lock` (`0x004EE4D0`) betritt die Sperre des Ordners (`ApMutualEx::RLock`); `CloseFile` (`0x004EEB50`, 32 Aufrufer) gibt sie wieder frei. Namen werden dabei klein geschrieben (`_strlwr`) und über `ApAdmin::GetObject` (Zeichenkette) in der Ordner- und Dateiverwaltung gesucht.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Dekompilat) sind `SetFilePointer`, `GetFileSize`, `ReadFile`, `SetPos`, `Lock`, `ResizeDatFile` (vollständig) und `OpenFile` (beide). `CloseFile` ist nur über die Form (`SafeRelease`, 32 Aufrufer) zugeordnet. Die Zeichenkette `1111` und `rb+` der Quelle erscheinen nur bei `SetFilePointer`, die Zeichenketten der Packfunktionen (`__e_%05d__.__`, `archlord`, `.JZP`) fehlen.
- Die Funktion `0x004EED50` (429 Byte, Muster `%s\*.*`, rekursiv, 38 Aufrufer) durchsucht Ordner und gehört vermutlich zum Packer (`CreateFolder`/`AddFolder`), ist aber nicht sicher zugeordnet. `0x004EE080`/`0x004EE120`/`0x004EF240`/`0x004EF370` sind die Konstruktoren/Destruktoren der Hilfsklassen (`CPackingFolder`, `CPackingFile`) und der Verwaltung selbst.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 1, nicht im Client: 32, ohne Kandidat: 11, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `ReadReferenceFile` | 152 | `0x004EE6C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Destroy` | 31 | `0x004EEC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetFileSize` (`0x004EF4E0`), `Unlock` (`0x004EF4E0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->
