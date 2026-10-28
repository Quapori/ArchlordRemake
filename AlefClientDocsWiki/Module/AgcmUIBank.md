# AgcmUIBank (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Teilbericht zu `AgcmUIBank.cpp` der Klasse [`AgcmUIItem`](AgcmUIItem.md) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: EP8-Quelle `Modules/AClient/AgcmUIItem/AgcmUIBank.cpp`, Importtabelle und Maschinencode des Binarys. Alle Aussagen gelten nur für den 2017er Build.

## Kernbefund

- **Inhalt der Quelldatei:** `AgcmUIBank.cpp` hat 9 Zeilen und enthält nur die freie Funktion `DummyFunction4()`, die `DebugBreak()` aufruft; es gibt keine Methode einer Klasse `AgcmUIBank`. Die Datei `AgcmUIBank.asp` im selben Verzeichnis ist leer (0 Byte), und kein anderer Client-Quelltext erwähnt `AgcmUIBank`.
- **Im Binary:** `DebugBreak` ist in der Importtabelle der Exe nicht enthalten, und es gibt keine Stelle im Code, die sie aufruft. `DummyFunction4` wurde also nicht ins Binary übernommen (vermutlich vom Linker entfernt, weil nichts sie aufruft).
- **Bank-Logik:** Die Oberfläche der Bank liegt nicht in dieser Datei. Der Bank-Status (100) taucht beim Verschieben ins erweiterte Inventar auf, siehe [AgcmUIChargingInventory](AgcmUIChargingInventory.md) und [AgcmUIItem](AgcmUIItem.md).
- **Abweichungen:** keine.

## Grenzen

- Das Fehlen von `DummyFunction4` im Binary ist aus der fehlenden Import- und Aufrufstelle geschlossen. Eine eigene Adresse der Funktion gibt es nicht zu prüfen.

## Querverweise

- **Erwähnt Module:** [`AgcmUIChargingInventory`](AgcmUIChargingInventory.md), [`AgcmUIItem`](AgcmUIItem.md)
