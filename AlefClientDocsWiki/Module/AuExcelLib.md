# AuExcelLib (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuExcelLib` (abstrakte Basisklasse der Tabellen-Leser) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuExcelLib/AuExcelLib.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** keine Quellmethoden (`AuExcelLib.cpp` enthält keine Definitionen); im Binary nur Konstruktor (`0x004EC710`, setzt die Vtable) und Löschwrapper (`0x004EC720`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuExcelLib.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|

0 von 0 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuExcelLib` (`0x004EC710`), `~AuExcelLib` (`0x004EC720`).

## Vtable

Vtable mit acht Einträgen: Löschwrapper `0x004EC720`, die Einträge 1 bis 6 sind rein virtuelle Funktionen (`0x007F39DC`), Eintrag 7 ist der Rumpf `0x0067AC90` (return TRUE). Abgeleitet sind `AuExcelTxtLib` und `AuExcelBinaryLib`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Vtable-Einträge sind aus dem Export (`vtables.tsv`) gelesen, nicht im Code verglichen.
