# AuTickCounter (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuTickCounter` (Zeitgeber mit QueryPerformanceCounter) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuTickCounter/AuTickCounter.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 2 von 3 Quellmethoden zugeordnet (`Initialize`, `GetTickCount`), dazu Konstruktor und Destruktor.
- **Nicht gefunden:** `GetElapsedTime`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuTickCounter.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Initialize` | `0x004F4950` | 58 | von Hand geprüft |
| 1 | `GetTickCount` | `0x004F4990` | 59 | von Hand geprüft |
| 2 | `GetElapsedTime` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |

2 von 3 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuTickCounter` (`0x004F4920`), `ctor_or_dtor_004f4940` (`0x004F4940`), `~AuTickCounter` (`0x004F49D0`).

## Funktionen

Vtable mit dem Löschwrapper `0x004F49D0` (Destruktor setzt nur die Vtable zurück). Der Konstruktor `0x004F4920` setzt Vtable und vier Felder (`+8` bis `+0x14`) auf 0. `Initialize` (`0x004F4950`) holt die Zählerfrequenz (`QueryPerformanceFrequency`, 64 Bit bei `+8`/`+0xC`) und den Anfangswert (`QueryPerformanceCounter` bei `+0x10`/`+0x14`); `GetTickCount` (`0x004F4990`) liefert `Zähler · 1000 / Frequenz` (Millisekunden, 64-Bit-Rechnung `__allmul`/`__aulldiv`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind alle genannten Funktionen vollständig. `GetElapsedTime` (52 Zeilen) hat keine eigene Funktion im Bereich `0x004F4900`–`0x004F4A00`; Aufrufe aus anderen Modulen wurden nicht einzeln gesucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->
