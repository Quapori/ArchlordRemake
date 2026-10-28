# AuScriptEngine (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuScriptEngine` (abstrakte Basisklasse der Skript-Maschinen (AngelScript)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuScriptEngine/AuScriptEngine.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** keine Quellmethoden in `AuScriptEngine.cpp`; im Binary nur zwei Konstruktorrümpfe (`0x004F6F90`, `0x004F6FA0`) und der Löschwrapper (`0x004F6FB0`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuScriptEngine.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|

0 von 0 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuScriptEngine` (`0x004F6F90`), `~AuScriptEngine_body` (`0x004F6FA0`), `~AuScriptEngine` (`0x004F6FB0`).

## Vtable

Vtable mit vier Einträgen: Löschwrapper `0x004F6FB0` und drei rein virtuelle Funktionen (`0x007F39DC`). Die Konstruktoren werden je einmal aus `0x004E9DAF` und `0x004E9EB1` gerufen (nicht weiter untersucht).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Aufrufer der Konstruktoren sind nicht untersucht.
