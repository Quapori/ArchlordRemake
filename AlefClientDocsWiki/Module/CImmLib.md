# CImmLib (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `CImmLib` (dynamischer Zugriff auf die IME-Funktionen von `imm32.dll`, aus `AgcSkeleton/ImmLib.cpp`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionsübersicht (`fcalls.py`), Zeichenketten (`ImmLockIMC`, `GetReadingString`), EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 2 von 2 Quellmethoden zugeordnet (`Init`, `SetupImeApi`), dazu Konstruktor und Destruktor.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CImmLib.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | `0x007B1FF0` | 410 | von Hand geprüft |
| 1 | `SetupImeApi` | `0x007B2190` | 159 | Zeichenkette |

2 von 2 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_007b1fc0` (`0x007B1FC0`), `ctor_or_dtor_007b1fd0` (`0x007B1FD0`), `~CImmLib` (`0x007B2230`).

## Funktionen

Vtable mit dem Löschwrapper `0x007B2230`. Konstruktorrümpfe `0x007B1FC0` (setzt nur die Vtable) und `0x007B1FD0` (holt die Bibliothek). `Init` (`0x007B1FF0`, 410 Byte) lädt die Funktionszeiger der Bibliothek per `GetProcAddress` (`ImmLockIMC`, `ImmUnlockIMC`, `ImmLockIMCC`, …); `SetupImeApi` (`0x007B2190`) holt die IME-spezifischen Funktionen (`GetReadingString`, `ShowReadingWindow`) aus dem aktuellen IME der Tastaturbelegung.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind nur die Köpfe und die Zeichenketten; die Zuordnung folgt aus diesen Namen der Windows-Funktionen. `SetupImeApi` ist bereits durch den Export (Zeichenkettentreffer) benannt.

## Querverweise

- **Erwähnt Module:** [`AgcSkeleton`](AgcSkeleton.md)
