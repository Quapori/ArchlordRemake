# ApMutualEx (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `ApMutualEx` (rekursive Sperre mit Sperrverwaltung (Lock-Manager)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/APublic/ApBase/ApMutualEx.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 5 von 7 Quellmethoden zugeordnet (`Init`, `Destroy`, `RLock`, `RemoveLock`, `SafeRelease`). Zusätzlich im Binary: `0x004E7B70` (Init mit Anfangszähler) und `0x004E7C60` (Destruktor, ruft `Destroy` wenn die Sperre erzeugt wurde). **Nicht gefunden:** `ResetRemoveLock`, `SetNotUseLockManager`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApMutualEx.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | `0x004E7B40` | 46 | von Hand geprüft |
| 1 | `Destroy` | `0x004E7BB0` | 169 | von Hand geprüft |
| 2 | `RLock` | `0x004E7CF0` | 98 | von Hand geprüft |
| 3 | `RemoveLock` | `0x004E7D60` | 24 | von Hand geprüft |
| 4 | `ResetRemoveLock` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 5 | `SafeRelease` | `0x004E7C70` | 65 | von Hand geprüft |
| 6 | `SetNotUseLockManager` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |

5 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `InitSpin` (`0x004E7B70`), `~ApMutualEx` (`0x004E7C60`).

## Funktionen

`ApMutualEx` ist eine `CRITICAL_SECTION` (Windows-Struktur, bei `this+0x00`) mit angehängten Feldern: Erzeugt-Flag `+0x18` (`DebugInfo` der Struktur), Zähler `+0x1C`, Eigentümer-Handle `+0x20` und Sperrverwaltung-Schalter `+0x24`. `Init` (`0x004E7B40`, 16 Zeilen) setzt die Felder und ruft `InitializeCriticalSectionAndSpinCount(…, 4000)`; die Fassung `0x004E7B70` setzt zusätzlich den Zähler. `Destroy` (`0x004E7BB0`, 169 Byte) wechselt zwischen Betreten und Verlassen über den Lock-Manager (`ApLockManager::Instance` `0x004F4B70`, `InsertLock` `0x004F4D90`, `RemoveUnlock` `0x004F4D40`), bevor es die Sektion löscht. `RLock` (`0x004E7CF0`, 98 Byte, 108 Aufrufer) betritt die Sektion, zunächst über `InsertLock`, wenn die Sperrverwaltung aktiv ist, sonst direkt. `SafeRelease` (`0x004E7C70`, 470 Aufrufer) verlässt sie wieder (`RemoveUnlock` oder `LeaveCriticalSection`). `RemoveLock` (`0x004E7D60`) ruft `RLock` und setzt bei Erfolg das Entfernen-Flag `+0x20`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `Init`, `Destroy` (Anfang), `RLock`, `SafeRelease` und `RemoveLock`. Die Namen folgen aus der Form (Betreten/Verlassen, Aufruf von `RLock` in `RemoveLock`) und den Aufrufzahlen. Die Bedeutung der Felder `+0x1C`/`+0x24` ist aus dem Dekompilat geschlossen, nicht aus der Kopfdatei geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht als eigene Funktion: 1, nicht im Client: 1, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `Release` | 22 | `0x004E7CC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->
