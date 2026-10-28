# AuFileFind (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuFileFind` (Hülle um FindFirstFile/FindNextFile) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuFileFind/AuFileFind.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 5 von 20 Quellmethoden zugeordnet (`FindFile`, `FindNextFile`, `IsDirectory`, `IsHidden`, `GetFileName`), dazu Konstruktor und Destruktorrumpf (`Close` ist im Destruktor eingebaut).
- **Nicht gefunden:** die übrigen `Is…`-Abfragen, `Get…Time` und `Initialize` (je 2 bis 7 Zeilen, in den Aufrufern eingebaut).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuFileFind.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Initialize` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 1 | `FindFile` | `0x004EDCE0` | 67 | von Hand geprüft |
| 2 | `FindNextFile` | `0x004EDD90` | 83 | von Hand geprüft |
| 3 | `Close` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 4 | `IsNormal` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 5 | `IsArchive` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 6 | `IsCompressed` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 7 | `IsDirectory` | `0x004EDD30` | 10 | von Hand geprüft |
| 8 | `IsEncrypted` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 9 | `IsHidden` | `0x004EDD40` | 9 | von Hand geprüft |
| 10 | `IsOffLine` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 11 | `IsReadOnly` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 12 | `IsReparsePoint` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 13 | `IsSparseFile` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 14 | `IsSystem` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 15 | `IsTemporary` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 16 | `GetCreationTime` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 17 | `GetLastAccessTime` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 18 | `GetLastWriteTime` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 19 | `GetFileName` | `0x004EDD50` | 31 | von Hand geprüft |

5 von 20 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuFileFind` (`0x004EDCD0`), `~AuFileFind_body` (`0x004EDD70`), `~AuFileFind` (`0x004EDE60`).

## Funktionen

Vtable mit dem Löschwrapper `0x004EDE60`. Das Objekt hält den Suchgriff bei `this+8`, die Daten (`WIN32_FIND_DATA`, `0x140` Byte) ab `+0xC` (Attribute `+0xC`, Dateiname ab `+0x38`). `FindFile` (`0x004EDCE0`) nullt die Daten und ruft `FindFirstFileA`; `FindNextFile` (`0x004EDD90`) ruft `FindNextFileA` und überspringt bei gesetztem Schalter (`+4`) Verzeichnisse; `IsDirectory` (`0x004EDD30`, Attributbit 4) und `IsHidden` (`0x004EDD40`, Bit 1) sind Einzeiler; `GetFileName` (`0x004EDD50`) kopiert den Namen; der Destruktorrumpf (`0x004EDD70`) schließt den Suchgriff (`FindClose`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Attributbits sind aus den Verschiebungen (`>> 4` = Verzeichnis, `>> 1` = versteckt) gegen die Windows-Konstanten gelesen. Die Funktion `0x004EDDF0` (112 Byte, 3 Aufrufer) benutzt das Objekt ebenfalls, ist aber keine Quellmethode und nicht benannt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht im Client: 13.

<!-- LUECKENREGISTER-NACHTRAG-END -->
