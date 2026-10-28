# AuCircularBuffer (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuCircularBuffer` (Ringpuffer für verschlüsselte Pakete) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/AUtility/AuPacket/AuCircularBuffer.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 2 von 4 Quellmethoden zugeordnet (`Init`, `Alloc`), dazu Konstruktor und Destruktorrumpf. **Nicht gefunden:** `Destroy` (im Destruktorrumpf `0x004EF750` eingebaut) und `Free`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuCircularBuffer.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | `0x004EF530` | 186 | von Hand geprüft |
| 1 | `Destroy` | – | | eingebaut im Destruktorrumpf `0x004EF750` |
| 2 | `Alloc` | `0x004EF5F0` | 342 | von Hand geprüft |
| 3 | `Free` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |

2 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuCircularBuffer` (`0x004EF500`), `~AuCircularBuffer_body` (`0x004EF750`), `~AuCircularBuffer` (`0x004EF7D0`).

## Funktionen

Vtable mit dem Löschwrapper `0x004EF7D0` (Destruktorrumpf `0x004EF750`). Der Konstruktor `0x004EF500` richtet die kritische Sektion (`this+0x10`, Schalter `+0x28`) ein und nullt Puffer und Zeiger (`+4` bis `+0xC`). `Init` (`0x004EF530`, 186 Byte) legt unter der Sperre den Puffer der übergebenen Größe an (`+8` Größe, `+4` Zeiger); `Alloc` (`0x004EF5F0`, 352 Byte, 6 Aufrufer) reserviert einen Abschnitt am Ring (u. a. von `AuPacket::EncryptPacket`/`DecryptPacket` benutzt).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind Konstruktor und der Anfang von `Init`; `Alloc` ist über Größe, Sperre und die Aufrufer in `AuPacket` zugeordnet, nicht gelesen. Die Funktion `0x004EF470` (Singleton einer 0x37C-Byte-Klasse) gehört nicht zu diesem Modul.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, nicht als eigene Funktion: 1.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `Free` (`0x004EF4E0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->
