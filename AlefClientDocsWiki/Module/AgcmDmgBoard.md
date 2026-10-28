# AgcmDmgBoard (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmDmgBoard` (Schadenszahlen und kritische Treffer über Charakteren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmDmgBoard.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle vier Methoden sind zugeordnet; dazu Konstruktor und Löschwrapper.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmDmgBoard.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Render` | `0x00758240` | 102 | von Hand geprüft |
| 1 | `Update` | `0x00757C80` | 303 | von Hand geprüft |
| 2 | `_DrawDamage` | `0x00757DB0` | 513 | von Hand geprüft |
| 3 | `_DrawCriticalDamage` | `0x00757FC0` | 535 | von Hand geprüft |

4 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmDmgBoard` (`0x007581E0`), `~AgcmDmgBoard` (`0x00758230`), `scalar_deleting_dtor` (`0x007582E0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | ``m_Type` (3 = Schaden, 4 = kritischer Schaden)` | `Render` |

## Vtable und Aufbau

`AgcmDmgBoard` (Schadenszahlen über Charakteren, abgeleitet von [`AgcmBaseBoard`](AgcmBaseBoard.md)) hat die Vtable `0x008DFD2C`: Slot 0 Löschwrapper (`0x007582E0`), Slot 1 `Render` (`0x00758240`), Slot 2 `Update` (`0x00757C80`). Konstruktor `0x007581E0` (66 Byte, ruft `AgcmBaseBoard::AgcmBaseBoard` `0x00751C40`), Destruktorrumpf `0x00758230`; Pool `ApMemory<AgcmDmgBoard,1000>` (`0x007582B0`).

## Zeichnen und Aktualisieren

`Render` (`0x00758240`, 102 Byte) schaltet Z-Schreiben und Z-Test aus, wählt nach der Brett-Art (`this+4`, Art 3 = Schaden, Art 4 = kritischer Schaden) `_DrawDamage` (`0x00757DB0`, 513 Byte) oder `_DrawCriticalDamage` (`0x00757FC0`, 535 Byte) und schaltet Z-Schreiben wieder ein. Beide zeichnen die Ziffern einzeln von rechts nach links (`GetDamageUVW`, `Image2D`); der kritische Schaden skaliert Größe und Alpha über den Animationsverlauf (Grenzen 0,15 und 0,85).
`Update` (`0x00757C80`, 303 Byte) zählt den Animationszähler hoch, endet bei Ablauf (FALSE) und rechnet sonst – wenn der Klumpen kürzlich berechnet wurde – die Position des Charakters um (bei Art „Schaden“ steigt die Zahl mit dem Animationsanteil um bis zu 40 Einheiten).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Brett-Art-Werte 3 und 4 folgen aus den Vergleichen in `Render` (Abzug von 3 und 1); ihre Namen (`AGCM_BOARD_DAMAGE`, `AGCM_BOARD_CRITICALDAMAGE`) stammen aus der Quelle.
- `Update`, `_DrawDamage` und `_DrawCriticalDamage` wurden über Vtable-Slot, Aufruf aus `Render` und Größe zugeordnet, nicht Zeile für Zeile verglichen.

## Querverweise

- **Erwähnt Module:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md)
- **Erwähnt in:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md)
