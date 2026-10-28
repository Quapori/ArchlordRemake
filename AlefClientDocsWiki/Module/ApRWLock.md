# ApRWLock (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `ApRWLock` (Leser-Schreiber-Sperre mit Ereignis und Mutex) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/APublic/ApBase/ApRWLock.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 5 von 5 Quellmethoden zugeordnet, dazu Konstruktor/Destruktor.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApRWLock.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Initialize` | `0x004F9F10` | 73 | von Hand geprüft |
| 1 | `LockReader` | `0x004F9FA0` | 83 | von Hand geprüft |
| 2 | `UnlockReader` | `0x004FA000` | 40 | von Hand geprüft |
| 3 | `LockWriter` | `0x004FA030` | 63 | von Hand geprüft |
| 4 | `UnlockWriter` | `0x004FA070` | 11 | von Hand geprüft |

5 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_004f9f60` (`0x004F9F60`), `ctor_or_dtor_004fa080` (`0x004FA080`), `~ApRWLock` (`0x004FA0D0`).

## Funktionen

Vtable mit dem Löschwrapper `0x004FA0D0`. Der Destruktor (`0x004F9F60`) schließt Ereignis (`+4`), Mutex (`+8`) und die kritische Sektion (`+0xC`). `Initialize` (`0x004F9F10`) legt Ereignis (manuell zurückgesetzt, zunächst gesetzt), Mutex und Sektion an und setzt Leserzahl (`+0x24`) auf 0. `LockReader` (`0x004F9FA0`) wartet auf den Mutex, zählt den Leser hoch und setzt bei dem ersten das Ereignis zurück; `UnlockReader` (`0x004FA000`) zählt herunter und setzt bei 0 das Ereignis. `LockWriter` (`0x004FA030`) wartet auf Mutex und auf das Ereignis (keine Leser); `UnlockWriter` (`0x004FA070`) gibt den Mutex frei.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Alle fünf Funktionen sind im Dekompilat vollständig gelesen; die Namen folgen aus dem Verhalten.
