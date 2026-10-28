# ApMemoryManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `ApMemoryManager` (Speicher-Pools nach Typ; der Wrapper `ApMemoryPool` benutzt sie) aus dem Modul `ApMemory` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionsübersicht (`fcalls.py`), Aufrufer (`ApMemoryPool` aus `ApMemoryPool.h`), Zeichenketten, EP8-Quelle `Modules/APublic/ApMemory/ApMemoryManager.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 10 von 16 Quellmethoden zugeordnet. Zugeordnet sind `GetInstance`, `DestroyInstance`, `Destroy`, `Initialize`, `ReportMemoryInfo`, `AddType`, `InitializeNode`, `NewObject`, `DeleteObject`, `SetEnable`. Dazu kommen die Kopfdatei-Methoden von `ApMemoryPool`: `Initialize` (`0x004E3EE0`), `Alloc` (`0x004E3F80`) und `Free` (`0x0040FEC0`); ihr Destruktor (`0x0040FF60`) trägt die Vtable von `ApMemoryPool`.
- **Nicht gefunden:** `GetAllocatedCount`, `CheckBeginGuardByte`, `CheckEndGuardByte`, `GetAllocated`, `SetAllocation`, `GetEnable` (je 4 bis 11 Zeilen, eingebaut).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApMemoryManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetInstance` | `0x004E72A0` | 64 | von Hand geprüft |
| 1 | `DestroyInstance` | `0x004E72E0` | 68 | von Hand geprüft |
| 2 | `Destroy` | `0x004E70D0` | 159 | von Hand geprüft |
| 3 | `Initialize` | `0x004E6900` | 237 | von Hand geprüft |
| 4 | `ReportMemoryInfo` | `0x004E69F0` | 853 | Zeichenkette |
| 5 | `AddType` | `0x004E7180` | 280 | von Hand geprüft |
| 6 | `GetAllocatedCount` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 7 | `InitializeNode` | `0x004E6D50` | 300 | von Hand geprüft |
| 8 | `CheckBeginGuardByte` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 9 | `CheckEndGuardByte` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 10 | `GetAllocated` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 11 | `SetAllocation` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 12 | `NewObject` | `0x004E6E80` | 149 | von Hand geprüft |
| 13 | `DeleteObject` | `0x004E6F20` | 130 | Zeichenkette |
| 14 | `SetEnable` | `0x004E6FB0` | 281 | von Hand geprüft |
| 15 | `GetEnable` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |

10 von 16 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Aufbau

Der Verwalter ist ein einzelnes Objekt (Zugriff `GetInstance` `0x004E72A0`, 198 Aufrufer; Aufräumen `DestroyInstance` `0x004E72E0`) mit Feldern je Typ, jeweils als Feld von bis zu 1.000 Einträgen zu 4 Byte: Speicherzeiger `+0`, Liste freier Knoten `+4000`, Objektgröße `+8000`, Knotengröße `+12000`, Anzahl `+16000`, Zähler der ausgegebenen Objekte `+20000`, Zähler der Zusatzzuteilungen `+28000`, Merker `+32000`, Freigabe-Schalter `+36000` und dahinter 65.000 Byte Typnamen. `+0x19A28` ist die Zahl der Typen, `+0x19A2C` die kritische Sektion (Schalter `+0x19A44`), `+0x19A48` die Startzeit (`GetLocalTime`).

## Funktionen

`Initialize` (`0x004E6900`, 237 Byte) nullt alle Felder und merkt die Startzeit; `AddType` (`0x004E7180`, 280 Byte) legt einen Typ an (Größe, Anzahl, Name; Fehlermeldung „MAX_TYPE_SIZE …“ bei Überlauf), reserviert den Speicher mit `VirtualAlloc` und baut die Knotenliste (`InitializeNode` `0x004E6D50`). `NewObject` (`0x004E6E80`) gibt den nächsten freien Knoten aus; sind alle vergeben, weicht es auf `malloc` aus und zählt die Zusatzzuteilung (+28000, +32000). `DeleteObject` (`0x004E6F20`, 66 Aufrufer) gibt ein Objekt zurück oder meldet bei fremder Adresse „second delete size : %d“. `SetEnable` (`0x004E6FB0`) schaltet einen Typ ein (`VirtualAlloc`) oder aus (`VirtualFree`); `Destroy` (`0x004E70D0`) gibt alle Typen frei und setzt die Felder zurück; `ReportMemoryInfo` (`0x004E69F0`, 853 Byte) schreibt „--- ApMemory Report ---“ mit Startzeit und Typtabelle in eine Datei `…_ApMemory.log`.
`ApMemoryPool` (Kopfdatei) ruft diese Funktionen unter einer Sperre auf: `Initialize(Größe, Anzahl, Name)` → `AddType`, `Alloc` → `NewObject`, `Free(Objekt)` → `DeleteObject`; der Typindex (`-1` = nicht eingerichtet) liegt im Pool-Objekt (bei `ApAdmin` und anderen Modulen: `this+…+0x1C`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `Initialize`, `NewObject` (Anfang), `SetEnable`, `Destroy` (Anfang) und die drei `ApMemoryPool`-Funktionen als Form; `AddType`, `InitializeNode`, `ReportMemoryInfo` und `DeleteObject` sind über Zeichenketten, Größe und Aufrufbeziehungen zugeordnet, nicht Zeile für Zeile verglichen. Die Feldversätze sind aus den Zugriffen gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht als eigene Funktion: 2, nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->
