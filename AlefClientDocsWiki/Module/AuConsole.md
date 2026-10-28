# AuConsole (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuConsole` (Textkonsole mit Eingabezeile und Verlauf) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuConsole/AuConsole.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 3 von 9 Quellmethoden zugeordnet (`print`, `passDo`, `passTab`), dazu Konstruktor und Destruktorrumpf.
- **Nicht gefunden:** `passKey`, `passBackspace`, `passLeft`, `passRight`, `passUp`, `passDown` (sieben bis 16 Zeilen, vermutlich eingebaut).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuConsole.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `print` | `0x00879A10` | 783 | von Hand geprüft |
| 1 | `passKey` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 2 | `passBackspace` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 3 | `passDo` | `0x00879D30` | 270 | von Hand geprüft |
| 4 | `passLeft` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 5 | `passRight` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 6 | `passUp` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 7 | `passDown` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 8 | `passTab` | `0x00879E60` | 814 | von Hand geprüft |

3 von 9 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `render` (`0x007F39DC`), `AuConsole` (`0x008797D0`), `~AuConsole_body` (`0x00879940`), `~AuConsole` (`0x00879E40`).

## Funktionen

Vtable mit zwei Einträgen: Löschwrapper `0x00879E40` und `render` (`0x007F39DC`, rein virtuell). Konstruktor `0x008797D0` (368 Byte), Destruktorrumpf `0x00879940`. `print` (`0x00879A10`, 783 Byte, 18 Aufrufer) zerlegt den Text mit einem Zeichenkettenstrom und hängt die Zeilen an den Verlauf; `passDo` (`0x00879D30`) führt die Eingabezeile aus (ruft `print`, legt sie in die Verlaufsliste bei `this+0xC0` und setzt den Cursor zurück); `passTab` (`0x00879E60`, 814 Byte) vervollständigt die Eingabe aus der Befehlsliste.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind nur die Köpfe von `print`, `passDo` und `passTab`; ihre Zuordnung folgt aus Größe, den Zeichenkettenströmen, dem Aufruf von `print` in `passDo` und der Rolle in der Quelle (Zeilenverlauf bei `+0xC0`), nicht aus einem Zeilenvergleich.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, ohne Kandidat: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->
