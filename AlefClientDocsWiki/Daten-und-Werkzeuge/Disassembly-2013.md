# alefclient.exe – statische Disassembly

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Daten, Auslese und Werkzeuge](Index.md)*

Die Originaldatei `C:\Spiele\Archlord\alefclient.exe` wurde nur gelesen und nicht ausgeführt oder verändert.

## Dateien

- `alefclient.disasm.txt` – vollständige x86-Disassembly aus Microsoft `dumpbin` (ca. 92 MB)
- `alefclient.pseudocode.c` – mit Ghidra 12.1.3 rekonstruierter, C-ähnlicher Pseudocode (ca. 30 MB)
- `functions.tsv` – Funktionsindex mit Adresse, Name, Größe und Decompiler-Status
- `headers.txt` – PE-Header, Abschnitte und Data Directories
- `imports.txt` – importierte DLLs und Funktionen
- `ghidra_scripts/ExportDecompiled.java` – reproduzierbares Exportskript

## Identifikation

- SHA-256: `F951E56DB985BA57FB9BA547FAD9984F9F21D5F3BB7367E58F22D6A84814B176`
- Format: PE32, Intel x86, Windows-GUI-Anwendung
- Image Base: `0x00400000`
- Entry Point RVA: `0x003FF11E`
- Entry Point VA: `0x007FF11E`
- Linker-Zeitstempel: `2013-04-02 08:01:38 UTC`
- Eingebetteter PDB-Pfad: `D:\branch\Global\Release\Release_Global_Code\Bin\AlefClient.pdb`

## Erste Orientierung

Der Einstiegspunkt steht in `alefclient.disasm.txt` bei Adresse `007FF11E`. Er ruft zunächst `007FF9E3` auf und springt anschließend nach `007FEE5D`. Die Datei importiert unter anderem Direct3D 9, WinMM, Winsock 2, FreeType und FMOD Ex.

Die Disassembly-Datei enthält Assembler. Die zusätzliche Ghidra-Ausgabe rekonstruiert daraus C-ähnlichen Pseudocode, jedoch nicht den ursprünglichen C++-Quellcode. Die ursprüngliche `AlefClient.pdb` wäre besonders wertvoll, falls sie noch vorhanden ist, weil sie Symbolnamen und möglicherweise Quelldateizuordnungen liefern kann.

## Ghidra-Ergebnis

- 22.711 Funktionen insgesamt erkannt, einschließlich externer/importierter Funktionen
- 22.060 interne Funktionen exportiert
- 22.059 interne Funktionen erfolgreich dekompiliert
- 1 Funktion (`00410e20`) überschritt das Zeitlimit
- 16.992 interne Funktionen besitzen mangels PDB weiterhin automatische Namen wie `FUN_00651520`
- 5.068 Funktionen erhielten aussagekräftigere Namen, überwiegend Bibliotheks- und Laufzeitfunktionen

Der Einstiegspunkt `entry` initialisiert den Stack-Sicherheitscookie und ruft `___tmainCRTStartup` auf. Die Laufzeitinitialisierung ruft anschließend `FUN_00651520` auf; diese Funktion entspricht sehr wahrscheinlich `WinMain`. Sie verarbeitet die Kommandozeile, initialisiert das Hauptfenster, zeigt und zentriert es und betreibt anschließend die Windows-Nachrichtenschleife sowie die Spiel-Updatefunktion.

`alefclient.pseudocode.c` ist bewusst eine große Such- und Analyseausgabe. Sie ist nicht direkt kompilierbar: Klassen, Typen, globale Variablen und aussagekräftige Namen müssen durch weitere manuelle Reverse-Engineering-Arbeit rekonstruiert werden.
