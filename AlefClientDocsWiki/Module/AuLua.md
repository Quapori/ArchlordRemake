# AuLua (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuLua` (Hülle um die Lua-Laufzeit) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuLua/AuLua.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 5 von 17 Quellmethoden zugeordnet (`RunString`, `GetStringArgument`, `AddFunction`, `GetNumberArgument`, `PushNumber`), dazu Konstruktor und Destruktorrumpf.
- **Nicht gefunden:** `RunScript`, `GetErrorString`, `PushString`/`PushInteger`/`PushNumber64`, alle `CallLuaFunction…` (vermutlich eingebaut oder entfernt).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuLua.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `RunScript` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 1 | `RunString` | `0x004E31B0` | 224 | Zeichenkette |
| 2 | `GetErrorString` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 3 | `AddFunction` | `0x004E32C0` | 27 | von Hand geprüft |
| 4 | `GetStringArgument` | `0x004E3290` | 47 | von Hand geprüft |
| 5 | `GetNumberArgument` | `0x004E32E0` | 30 | von Hand geprüft |
| 6 | `PushString` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 7 | `PushNumber` | `0x004E3300` | 25 | von Hand geprüft |
| 8 | `PushInteger` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 9 | `PushNumber64` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 10 | `CallLuaFunction` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 11 | `CallLuaFunction` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 12 | `CallLuaFunction` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 13 | `CallLuaFunction` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 14 | `CallLuaFunctionInt` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 15 | `CallLuaFunctionFloat` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 16 | `CallLuaFunctionString` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |

5 von 17 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuLua` (`0x004E3120`), `~AuLua_body` (`0x004E3180`), `~AuLua` (`0x004E3320`).

## Funktionen

Der Konstruktor `0x004E3120` öffnet einen Lua-Zustand (`0x007DF900`) und lädt die Standardbibliotheken (fünf Aufrufe `0x007DF030` bis `0x007DAC30`); `this+8` ist der Zustand, `+0xC` der Fehlerausgabe-Rückruf, `+4` ein Flag. Der Destruktorrumpf `0x004E3180` schließt den Zustand (`0x007E0440`). `RunString` (`0x004E31B0`, 224 Byte) lädt und führt eine Zeichenkette aus (`0x007DF870`, `0x007E13D0`); bei Fehlern erzeugt es „Lua Error - String Load/Run“ mit der Fehlermeldung und ruft den Rückruf.
Die vier Einzeiler dahinter sind die Hüllen um die Lua-Programmierschnittstelle: `GetStringArgument` (`0x004E3290`), `AddFunction` (`0x004E32C0`), `GetNumberArgument` (`0x004E32E0`, 71 Aufrufer) und `PushNumber` (`0x004E3300`, 42 Aufrufer); die Zuordnung folgt aus der Argumentform (Nummer plus Zeiger, zwei Zeiger, Nummer plus Double, nur Double).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind Konstruktor, Destruktorrumpf und `RunString`; die vier Einzeiler sind nur im Disassembly auf die Argumentform geprüft, nicht gegen die Lua-Funktionsnamen (die Lua-Funktionen `0x007Dxxxx` sind nicht benannt).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 1, nicht im Client: 11.

<!-- LUECKENREGISTER-NACHTRAG-END -->
