# AuXmlParser (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuXmlParser` (Hülle um den TinyXML-Dokumentparser) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuXmlParser/AuXmlParser.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 2 von 2 Quellmethoden zugeordnet (`LoadXMLFile`, `LoadXMLMemory`), dazu Konstruktor und Destruktorrumpf.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuXmlParser.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `LoadXMLFile` | `0x00878D20` | 670 | von Hand geprüft |
| 1 | `LoadXMLMemory` | `0x00878C40` | 180 | von Hand geprüft |

2 von 2 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuXmlParser` (`0x00878BD0`), `~AuXmlParser_body` (`0x00878BF0`), `~AuXmlParser` (`0x00878D00`).

## Funktionen

`AuXmlParser` erbt von `TiXmlDocument`; die Vtable hat 18 Einträge (Löschwrapper `0x00878D00`, die übrigen sind TinyXML-Funktionen). Konstruktor `0x00878BD0` (ruft den Konstruktor von `TiXmlDocument` `0x008737F0`), Destruktorrumpf `0x00878BF0`. `LoadXMLMemory` (`0x00878C40`) parst einen Puffer (`0x008725D0`); `LoadXMLFile` (`0x00878D20`, 670 Byte) prüft zuerst den Speicher-Pool für das Laden (einmalig `0x004E3EE0`), liest die Datei über einen `filebuf` in einen Puffer und ruft `LoadXMLMemory`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `LoadXMLFile` ist nur im Kopf gelesen; die Zuordnung folgt aus Größe, dem Dateistrom und dem Aufruf von `0x00878C40`. Die TinyXML-Klassen selbst (`TiXml…`) sind nicht Teil des Berichts.
