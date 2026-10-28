# ApLockManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `ApLockManager` (Verwaltung der gehaltenen Sperren zur Verklemmungsprüfung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/APublic/ApBase/ApLockManager.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 3 von 17 Quellmethoden zugeordnet (`Instance`, `RemoveUnlock`, `InsertLock`). Die übrigen sind kleine Funktionen (4 bis 14 Zeilen) und in `ApMutualEx` und den Aufrufern eingebaut oder entfernt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApLockManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Instance` | `0x004F4B70` | 73 | von Hand geprüft |
| 1 | `DeleteInstance` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 2 | `GetCount` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 3 | `Lock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 4 | `Unlock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 5 | `InsertLock` | `0x004F4D90` | 288 | Zeichenkette |
| 6 | `RemoveUnlock` | `0x004F4D40` | 76 | von Hand geprüft |
| 7 | `SafeRemoveUnlock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 8 | `RemoveCheck` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 9 | `SequenceLockforMultiple` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 10 | `SequenceUnlockforMultiple` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 11 | `SequenceLock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 12 | `SequenceUnlock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 13 | `IsExistData` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 14 | `AllUnlock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 15 | `RecursionLock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 16 | `RecursionUnlock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |

3 von 17 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x004F4AF0`), `~ApLockManager` (`0x004F4B50`).

## Funktionen

Vtable mit dem Löschwrapper `0x004F4B50`; Konstruktor `0x004F4AF0`. `Instance` (`0x004F4B70`, 13 Aufrufer) liefert den einzigen Lock-Manager (anlegen bei Bedarf); `InsertLock` (`0x004F4D90`, 288 Byte) trägt die Sperre des aufrufenden Threads in die Verwaltung ein; `RemoveUnlock` (`0x004F4D40`) nimmt sie wieder heraus.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen ist nur die Verwendung in `ApMutualEx` (Reihenfolge `Instance`, dann `InsertLock` bzw. `RemoveUnlock`); `InsertLock` ist durch den Anker (Export-Name) belegt, `Instance` und `RemoveUnlock` durch die Form des Aufrufs. Die Funktionen `0x004F4A10`, `0x004F4BC0`, `0x004F4C20`, `0x004F4C90`, `0x004F4EB0` liegen im Bereich und gehören vermutlich zu den Sequenzfunktionen, sind aber nicht zugeordnet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, nicht im Client: 2, ohne Kandidat: 8.

<!-- LUECKENREGISTER-NACHTRAG-END -->
