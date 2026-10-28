# StackWalker (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse von `StackWalker` (Aufrufliste über dbghelp (Klasse mit Rückruffunktionen; `AuStackWalker` leitet sie ab)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Zeichenketten, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuXCrashReport/StackWalker.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 8 von 8 Quellmethoden zugeordnet, dazu Konstruktor und Destruktor. `AuStackWalker` (abgeleitet) überschreibt `OnOutput` (`0x004E54B0`) und hat den Konstruktor `0x004E54E0`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`StackWalker.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `LoadModules` | `0x004F5DD0` | 841 | Zeichenkette |
| 1 | `ShowCallstack` | `0x004F5100` | 892 | von Hand geprüft |
| 2 | `myReadProcMem` | `0x004F50C0` | 25 | von Hand geprüft |
| 3 | `OnLoadModule` | `0x004F5740` | 248 | vtable/String |
| 4 | `OnCallstackEntry` | `0x004F5840` | 284 | vtable/String |
| 5 | `OnDbgHelpErr` | `0x004F5960` | 74 | vtable/String |
| 6 | `OnSymInit` | `0x004F59B0` | 210 | vtable/String |
| 7 | `OnOutput` | `0x004F5080` | 62 | vtable/String |

8 von 8 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_004e54d0` (`0x004E54D0`), `ctor_or_dtor_004f4f70` (`0x004F4F70`), `StackWalker` (`0x004F56D0`), `~StackWalker` (`0x004F5DB0`).

## Funktionen

Vtable `StackWalker` mit sechs Einträgen: Löschwrapper `0x004F5DB0`, `OnLoadModule` (`0x004F5740`), `OnCallstackEntry` (`0x004F5840`), `OnDbgHelpErr` (`0x004F5960`), `OnSymInit` (`0x004F59B0`) und `OnOutput` (`0x004F5080`); `AuStackWalker` ersetzt den letzten durch `0x004E54B0`. `LoadModules` (`0x004F5DD0`, 547 Byte; Zeichenkette `_NT_SYMBOL_PATH`) lädt die Symbole der Module; `ShowCallstack` (`0x004F5100`, 896 Byte; `StackWalk64`) läuft über den Stapel und ruft `OnCallstackEntry`; `myReadProcMem` (`0x004F50C0`) ist die Rückruffunktion zum Lesen fremden Speichers.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Vtable-Zuordnung stammt aus dem Export (RTTI); `ShowCallstack` und `myReadProcMem` sind über Zeichenkette `StackWalk64`/Größe/Aufruf (`myReadProcMem` einmal aus `ShowCallstack`) zugeordnet, nicht Zeile für Zeile verglichen.
