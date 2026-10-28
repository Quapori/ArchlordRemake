# AgcmRegistryManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AgcmRegistryManager` (liest den Installationsschlüssel der Registrierungsdatenbank) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat (`FUN_00653500`), Zeichenketten, EP8-Quelle `Modules/AClient/AgcmRegistryManager/AgcmRegistryManager.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Die Quelle hat nur Konstruktor, Destruktor und eine Vorlagen-Hilfe (`set_value` in `AgcmRegistryManager.hpp`); im Binary gefunden ist der Konstruktor (`0x00653500`, 410 Byte).
- **Abweichung von der Quelle:** Der Konstruktor öffnet den Schlüssel `HKEY_LOCAL_MACHINE\SOFTWARE\Webzen\ArchLord` mit `KEY_READ`, wenn **keine** Datei `AlphaTest.arc` im Arbeitsordner liegt; liegt sie dort, öffnet er `SOFTWARE\Webzen\ArchLord_GB_TEST` und schließt die Datei wieder. Die EP8-Quelle öffnet in beiden Zweigen den Testschlüssel (`subKey_alpha`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmRegistryManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|

0 von 0 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmRegistryManager` (`0x00653500`).

## Ablauf

`fopen_s("AlphaTest.arc","rb")` → ohne Datei `RegOpenKeyExA(HKLM, "SOFTWARE\Webzen\ArchLord", 0, 0x20019, &handle)`; schlägt das Öffnen fehl, wird „FAILED - AgcmRegistryManager::RegOpenKey, “ plus Schlüsselname mit `OutputDebugStringA` ausgegeben und das Handle auf 0 gesetzt. Mit Datei wird der Testschlüssel genauso geöffnet. Das Handle liegt bei `this+0`.

## Abweichungen von der EP8-Quelle

- Konstruktor: im Binary Schlüssel `SOFTWARE\Webzen\ArchLord` ohne `AlphaTest.arc`, in der EP8-Quelle immer `ArchLord_GB_TEST`.

## Grenzen

- Gelesen ist nur der Konstruktor. Der Destruktor (`RegCloseKey`) und die Abfragefunktionen aus `AgcmRegistryManager.hpp` (Vorlagen, in den Aufrufern erzeugt) sind nicht einzeln gesucht.
