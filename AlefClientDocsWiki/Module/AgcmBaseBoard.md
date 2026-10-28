# AgcmBaseBoard (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Basisklasse `AgcmBaseBoard` (gemeinsame Felder und Standardwerte aller Bretter über Charakteren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Disassembly (`x86dis.py`), Vtable, EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmBaseBoard.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 0 von 1 Quellmethoden als eigene Funktion: `SetScreenPos(x, y, z)` ist eine Inline-Funktion und eingebaut; Konstruktor, Destruktorrumpf und Löschwrapper sind zugeordnet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmBaseBoard.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetScreenPos` | – | | eingebaut: Inline-Funktion, im Binary keine eigene Funktion gefunden (ihr Rumpf steckt im Konstruktor und in den Aufrufern) |

0 von 1 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00751c30` (`0x00751C30`), `AgcmBaseBoard` (`0x00751C40`), `~AgcmBaseBoard` (`0x00751C90`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | ``m_Type`` | Konstruktor |
| `this+0x08 / 0x14` | `Kameraposition / Bildschirmposition` | Konstruktor |
| `this+0x20 / 0x24` | `Versatz (x, y)` | Konstruktor |
| `this+0x28 / 0x2C` | `Höhe / Kehrwert z` | Konstruktor |
| `this+0x30 / 0x34 / 0x38 / 0x3C` | ``Draw` / Klumpen / sichtbar / Alpha` | Konstruktor, [`AgcmIDBoard`](AgcmIDBoard.md):Render` |

## Vtable und Aufbau

`AgcmBaseBoard` ist die abstrakte Basisklasse aller Bretter (Vtable `0x008DFA94`, deren Einträge für `Render` und `Update` auf `_purecall` `0x007F39DC` zeigen). Konstruktor `0x00751C40` (80 Byte): speichert die Brett-Art (`this+4`), nullt Versatz, Höhe, Kehrwert z (`+0x20`, `+0x24`, `+0x28`, `+0x2C`), Kamera- und Bildschirmposition (`+0x14`/`+0x18`/`+0x1C`), `Draw` (`+0x30`), Klumpen (`+0x34`) und Alpha (`+0x3C`). Der Destruktorrumpf (`0x00751C30`, 7 Byte) setzt nur die Vtable zurück; der Löschwrapper ist `0x00751C90`.
Das Layout aus `AgcmBaseBoard.h` ist damit bestätigt: Art `+4`, Kameraposition `+8`, Bildschirmposition `+0x14`, Versatz `+0x20`, Höhe `+0x28`, Kehrwert z `+0x2C`, `Draw` `+0x30`, Klumpen `+0x34`, sichtbar `+0x38`, Alpha `+0x3C`. Die abgeleiteten Klassen beginnen ab `+0x40` (bei [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmDmgBoard`](AgcmDmgBoard.md): Vtable des Pools).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass `SetScreenPos` eingebaut ist, folgt aus dem Fehlen einer eigenen Funktion und dem Nullen der Bildschirmposition im Konstruktor; ein Aufruferabgleich wurde nicht gemacht.
- Offsets `+0x08` bis `+0x10` (Kameraposition) und `+0x38` sind aus der Header-Reihenfolge und der Verwendung in `AgcmIDBoard::Render` abgeleitet, nicht im Konstruktor gesetzt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmDmgBoard`](AgcmDmgBoard.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md)
- **Erwähnt in:** [`AgcmDmgBoard`](AgcmDmgBoard.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmImoticonBoard`](AgcmImoticonBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`Image2D`](Image2D.md)
