# AuExcelTxtLib (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuExcelTxtLib` (Tabellen-Leser für die Textdateien der Daten (Tabulator getrennt, optional verschlüsselt)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuExcelTxtLib/AuExcelTxtLib.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 15 Quellmethoden zugeordnet (`Reset`, `OpenExcelFile`, `CloseFile`, `GetColumnFromFile`, `GetRowFromFile`, `GetColumn`, `GetRow`, `GetData` (Spalte, Zeile), `GetDataToInt`, `GetDataToFloat`, `IsEmpty`, `ReadRow`), dazu Konstruktor und Destruktorrumpf.
- **Nicht gefunden:** `GetData` mit Zeiger-Feld und Index, `ResetRowData`, `EncryptSave`; die Kopfzeile der verschlüsselten Datei schreibt `0x004ECD00` (Zeichenkette `<@!#_AeTlHhT_#!@>`, 16-Bit-Wert `0x1234`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuExcelTxtLib.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Reset` | `0x004EC7B0` | 218 | von Hand geprüft |
| 1 | `OpenExcelFile` | `0x004ED870` | 1114 | von Hand geprüft |
| 2 | `CloseFile` | `0x004EC8F0` | 96 | vtable/String |
| 3 | `GetColumnFromFile` | `0x004EC950` | 110 | von Hand geprüft |
| 4 | `GetRowFromFile` | `0x004EC9C0` | 63 | von Hand geprüft |
| 5 | `GetColumn` | `0x00526A30` | 4 | von Hand geprüft |
| 6 | `GetRow` | `0x004ECA00` | 4 | vtable/String |
| 7 | `GetData` | – | | nicht im Binary gefunden; Verbleib offen |
| 8 | `GetData` | `0x004ECA10` | 43 | von Hand geprüft |
| 9 | `GetDataToInt` | `0x004ECA40` | 37 | vtable/String |
| 10 | `GetDataToFloat` | `0x004ECA70` | 47 | vtable/String |
| 11 | `IsEmpty` | `0x004ECAA0` | 25 | vtable/String |
| 12 | `ResetRowData` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 13 | `ReadRow` | `0x004ECAC0` | 397 | von Hand geprüft |
| 14 | `EncryptSave` | – | | nicht im Binary gefunden (nur die Kopfzeilenfunktion `0x004ECD00` ist vorhanden; die Speicherfunktion gehört zum Editor) |

12 von 15 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuExcelTxtLib` (`0x004EC740`), `~AuExcelTxtLib_body` (`0x004EC890`), `WriteEncryptHeader` (`0x004ECD00`), `~AuExcelTxtLib` (`0x004ECDA0`).

## Funktionen

Vtable `AuExcelTxtLib`: 0 Löschwrapper `0x004ECDA0`, 1 `GetColumn` (gemeinsamer Rumpf `0x00526A30`, gibt `this+0x14` zurück; der frühere Name `AuExcelBinaryLib::GetDataToInt` für diese Adresse war falsch), 2 `GetRow` (`0x004ECA00`, gibt `+0x18` zurück), 3 `IsEmpty`, 4 `GetData`, 5 `GetDataToInt`, 6 `GetDataToFloat`, 7 `CloseFile`. Das Objekt hält den Dateipuffer bei `+8`, seine Länge `+0xC`, die Lesemarke `+0x10`, die Spaltenzahl `+0x14`, die Zeilenzahl `+0x18` und ein Zeilenfeld bei `+4` (Zeiger auf Zeilen aus Zeigern auf Zellen).
`OpenExcelFile` (`0x004ED870`, 1.114 Byte, Zeichenkette `.zp` u. a.) liest die Datei (auf Wunsch entschlüsselt), bestimmt mit `GetColumnFromFile` (`0x004EC950`, zählt die Tabulatoren der ersten Zeile) und `GetRowFromFile` (`0x004EC9C0`, zählt die Zeilenumbrüche) die Größe und liest Zeile für Zeile mit `ReadRow` (`0x004ECAC0`, 397 Byte). `Reset` (`0x004EC7B0`) gibt alle Zellen frei; `CloseFile` (`0x004EC8F0`) schließt die Datei. `GetData` (`0x004ECA10`) liefert den Zeiger der Zelle (Spalte, Zeile; Prüfung der Grenzen), `GetDataToInt`/`GetDataToFloat` (`0x004ECA40`/`0x004ECA70`) rufen es über die Vtable und wandeln mit `atoi`/`atof`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `GetData`, `GetDataToInt`/`Float`, `GetRow`, `IsEmpty`, `GetColumnFromFile`, `GetRowFromFile`, der Anfang von `ReadRow`, `Reset`, `CloseFile` (Anfang) und der Konstruktor. `OpenExcelFile` ist über die Aufrufe (`Reset`, die beiden Zähler, `ReadRow`) und die Zeichenkette `.zp` zugeordnet, nicht im Ganzen gelesen. Daneben liegt die Klasse `AuExcelBinaryLib` (`0x00526A20` ff.), die nicht Teil dieses Berichts ist.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, nicht im Client: 1, ohne Kandidat: 1.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetData` (`0x004EFB80`).

<!-- LUECKENREGISTER-NACHTRAG-END -->
