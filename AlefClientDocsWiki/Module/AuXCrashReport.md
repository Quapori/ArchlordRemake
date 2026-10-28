# AuXCrashReport (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse von `AuXCrashReport` (Absturzbericht: Ausnahmebehandlung, Speicherabbild, Aufrufliste, Systeminformation) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Zeichenketten, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuXCrashReport/ExceptionHandler.cpp, GetWinVer.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 18 freien Funktionen zugeordnet (`hflush`, `hprintf`, `DumpMiniDump`, `FormatTime`, `DumpModuleInfo`, `DumpModuleList`, `DumpSystemInformation`, `GetExceptionDescription`, `GetFilePart`, `DumpStack`, `DumpRegisters`, `RecordExceptionInfo`).
- **Nicht gefunden:** `lstrrchr`, `CheckCurrentThreadCallStack`, `DumpCallStack`, `GetModuleByAddr`, `StreamReadDumpConfig`, `GetWinVer`. Die Quelle hat keine Klasse; es sind statische Funktionen, die Namen im Binary tragen deshalb nur das Präfix `AuXCrashReport::` als Gruppe.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuXCrashReport.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `lstrrchr` | – | | nicht im Binary gefunden; Verbleib offen (kleine statische Funktion, vermutlich eingebaut) |
| 1 | `CheckCurrentThreadCallStack` | – | | nicht im Binary gefunden; Verbleib offen (kleine statische Funktion, vermutlich eingebaut) |
| 2 | `hflush` | `0x004E55D0` | 57 | von Hand geprüft |
| 3 | `hprintf` | `0x004E5610` | 86 | von Hand geprüft |
| 4 | `DumpMiniDump` | `0x004E5670` | 177 | von Hand geprüft |
| 5 | `FormatTime` | `0x004E5750` | 122 | von Hand geprüft |
| 6 | `DumpModuleInfo` | `0x004E57D0` | 685 | von Hand geprüft |
| 7 | `DumpModuleList` | `0x004E5A90` | 155 | von Hand geprüft |
| 8 | `DumpSystemInformation` | `0x004E5B30` | 501 | von Hand geprüft |
| 9 | `GetExceptionDescription` | `0x004E5D30` | 475 | von Hand geprüft |
| 10 | `GetFilePart` | `0x004E5F10` | 38 | von Hand geprüft |
| 11 | `DumpStack` | `0x004E5F40` | 433 | von Hand geprüft |
| 12 | `DumpRegisters` | `0x004E6110` | 170 | von Hand geprüft |
| 13 | `GetModuleByAddr` | – | | nicht im Binary gefunden; Verbleib offen (kleine statische Funktion, vermutlich eingebaut) |
| 14 | `DumpCallStack` | – | | nicht im Binary gefunden; Verbleib offen (kleine statische Funktion, vermutlich eingebaut) |
| 15 | `RecordExceptionInfo` | `0x004E61C0` | 1808 | von Hand geprüft |
| 16 | `StreamReadDumpConfig` | – | | nicht im Binary gefunden; Verbleib offen (kleine statische Funktion, vermutlich eingebaut) |
| 17 | `GetWinVer` | – | | nicht im Binary gefunden; Verbleib offen (kleine statische Funktion, vermutlich eingebaut) |

12 von 18 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Ablauf

`RecordExceptionInfo` (`0x004E61C0`, 1.855 Byte; Zeichenketten `ERRORLOG.TXT`, „… location %08x caused …“) ist der Ausnahmefilter: er legt die Fehlerdatei an und schreibt nacheinander Systeminformation (`DumpSystemInformation` `0x004E5B30`), Ausnahmebeschreibung (`GetExceptionDescription` `0x004E5D30`, Sprungtabelle mit je einem Zeichenkettenrumpf pro Ausnahmecode), Register (`DumpRegisters` `0x004E6110`: EDI/ESI/EAX/EBX/ECX/EDX/EIP/EBP/SegCs …), Stapel (`DumpStack` `0x004E5F40`, Zeichenketten `0x%08x: `, `%08x `) und die Modulliste (`DumpModuleList` `0x004E5A90`, durchläuft den Adressraum mit `VirtualQuery` und ruft `DumpModuleInfo` `0x004E57D0`). Ein Speicherabbild schreibt `DumpMiniDump` (`0x004E5670`, Meldungen „writing minidump“/„raising exception“).
Hilfen: `hprintf` (`0x004E5610`, 45 Aufrufer) formatiert und schreibt in die Datei, `hflush` (`0x004E55D0`) leert sie; `FormatTime` (`0x004E5750`, Format `%d/%d/%d %02d:%02d:%02d`), `GetFilePart` (`0x004E5F10`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Dekompilat) sind `DumpModuleList` und der Anfang von `DumpMiniDump`; die übrigen Funktionen sind über Zeichenketten (`ERRORLOG.TXT`, Registerzeile, Zeitformat, `0x%08x: `) und ihre Rolle in `RecordExceptionInfo` zugeordnet, nicht Zeile für Zeile verglichen. Die Zuordnung von `GetExceptionDescription` folgt aus der Sprungtabelle mit gleich großen Zeichenkettenrümpfen (`0x004E5EA1` bis `0x004E5EF7`).
- In der Quelle ist `RecordExceptionInfo` mit der Fortsetzung von `DumpCallStack` verschränkt; für die Tabelle wurde `DumpCallStack` auf 57 Zeilen und `RecordExceptionInfo` auf den Rest geschätzt.
