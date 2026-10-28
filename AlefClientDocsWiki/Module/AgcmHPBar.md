# AgcmHPBar (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmHPBar` (Lebens-/Manabalken des Hauptcharakters und fremder Charaktere) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmHPBar.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle sieben Methoden sind zugeordnet (`SetData`, `Update`, `Render`, `_HPBarUpdate`, `_HPMPBarUpdate`, `_DrawHPBar`, `_DrawHPMPBar`); dazu Konstruktor und Löschwrapper.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmHPBar.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetData` | `0x00755B60` | 720 | von Hand geprüft |
| 1 | `Update` | `0x00755E30` | 59 | von Hand geprüft |
| 2 | `Render` | `0x00755E70` | 24 | von Hand geprüft |
| 3 | `_HPBarUpdate` | `0x007552F0` | 366 | von Hand geprüft |
| 4 | `_HPMPBarUpdate` | `0x00755460` | 411 | von Hand geprüft |
| 5 | `_DrawHPBar` | `0x00755600` | 488 | von Hand geprüft |
| 6 | `_DrawHPMPBar` | `0x007557F0` | 782 | von Hand geprüft |

7 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmHPBar` (`0x00755B00`), `~AgcmHPBar` (`0x00755B50`), `scalar_deleting_dtor` (`0x00755EC0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | ``m_Type` (5 = HP-Balken, 6 = HP/MP-Balken)` | `Update`, `Render` |

## Vtable und Aufbau

`AgcmHPBar` (Lebens- und Manabalken, abgeleitet von [`AgcmIDBoard`](AgcmIDBoard.md)) hat die Vtable `0x008DFBC4`: Slot 0 Löschwrapper (`0x00755EC0`, ruft den `AgcmIDBoard`-Destruktorrumpf `0x00753610` und den Pool-Löscher `0x0063C780`), Slot 1 `Render` (`0x00755E70`), Slot 2 `Update` (`0x00755E30`). Konstruktor `0x00755B00` (77 Byte, ruft den `AgcmIDBoard`-Konstruktor `0x00754010`), Destruktorrumpf `0x00755B50`; der Pool ist `ApMemory<AgcmHPBar,1000>` (Vtable `0x008DFBB4`).
`Update` und `Render` verzweigen nach der Brett-Art (`m_Type` bei `this+4`): Art 5 (`AGCM_BOARD_HPBAR`) ruft `_HPBarUpdate` (`0x007552F0`) bzw. `_DrawHPBar` (`0x00755600`), Art 6 (`AGCM_BOARD_HPMPBAR`) `_HPMPBarUpdate` (`0x00755460`) bzw. `_DrawHPMPBar` (`0x007557F0`).

## Daten und Balken

`SetData` (`0x00755B60`, 720 Byte) kopiert die Anzeigedaten eines `AgcmIDBoard` (Position, Kamera- und Bildschirmposition, Klumpen, Schriftart, Versatz, Farbe, Gruppe, Gilde, Charisma, alle Texte) und setzt die ID-Art auf „Hauptcharakter“; zum Schluss ruft es `ReCalulateOffsetX` (`0x00753D40`). Aufrufer ist `0x0063E680` im Bereich des Textbrett-Managers.
`_HPBarUpdate` und `_HPMPBarUpdate` rechnen die Position um (`Trans3DTo2D`), blenden bei toten Charakteren den Nachbild-Balken aus (Geschwindigkeit und Beschleunigung als Konstanten `AGCM_TEXT_BOARD_AFTERIMAGE_DECREASE_SPEED`/`…ACCELERATION`) und verkleinern ihn mit der Tick-Differenz bis zum Ergebnis. `_DrawHPBar` (488 Byte) zeichnet Rahmen (120 × 7) und Füllung mit `Image2D`; `_DrawHPMPBar` (782 Byte) zeichnet Lebens- und Manabalken über `AgcEngine::DrawIm2D` und ruft zum Schluss `DrawChar` (`0x00755250`) für den Namen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der vier Rümpfe `0x007552F0`, `0x00755460`, `0x00755600` und `0x007557F0` folgt aus den Sprüngen in `Update`/`Render` (Art 5 bzw. 6), aus ihrer Größe und aus dem Aufruf von `DrawChar` in der größten Funktion; sie wurden nicht Zeile für Zeile verglichen.
- Die Feldnamen (Nachbild, Ergebnisanteil) stammen aus der Quelle; ihre Offsets in `AgcmHPBar` wurden nicht vermessen.

## Querverweise

- **Erwähnt Module:** [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md)
- **Erwähnt in:** [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md)
