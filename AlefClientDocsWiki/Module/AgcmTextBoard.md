# AgcmTextBoard (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmTextBoard` (Sprechblasen über Charakteren; abgeleitet von [`AgcmBaseBoard`](AgcmBaseBoard.md), Pool `ApMemory<AgcmTextBoard,1000>`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtables, EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmTextBoard.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: `Render`, `Update` und `InitText` sind zugeordnet; dazu Konstruktor, Destruktor und Löschwrapper.
- **Nicht Teil dieses Berichts:** die übrigen Klassen des Verzeichnisses (`AgcmBaseBoard`, [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmHPBar`](AgcmHPBar.md), [`AgcmDmgBoard`](AgcmDmgBoard.md), [`AgcmImoticonBoard`](AgcmImoticonBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), `CFlagImoticon`, `Image2D`) haben noch keinen eigenen Bericht.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmTextBoard.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Render` | `0x00758320` | 2025 | von Hand geprüft |
| 1 | `Update` | `0x00758B10` | 293 | von Hand geprüft |
| 2 | `InitText` | `0x00758C40` | 20 | von Hand geprüft |

3 von 3 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmTextBoard` (`0x00758C60`), `~AgcmTextBoard` (`0x00758CD0`), `scalar_deleting_dtor` (`0x00758D10`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x08 / 0x14` | `Kameraposition / Bildschirmposition (je 3 Float)` | `Update`, `Render` |
| `this+0x28 / 0x2C` | `Höhe / Kehrwert z (Name nach Quelle)` | `Update` |
| `this+0x30` | ``Draw`-Flag` | `Update`, `Render` |
| `this+0x34` | `Klumpen des Charakters` | `Update` |
| `this+0x40` | `Vtable des Pools `ApMemory<AgcmTextBoard,1000>`` | Konstruktor |
| `this+0x44 / 0x48 / 0x4C / 0x50` | `Breite / Höhe / Lebenszähler / Schriftart (Reihenfolge nach Header; Lebenszähler an `Update` belegt)` | Konstruktor, `Update` |
| `this+0x54` | `Textzeilen (249 Byte)` | `InitText` |
| `this+0x150 / 0x154 / 0x158` | `Textfarbe / Schwanzart / Zeilenzahl (nach Header)` | Konstruktor |
| `this+0x15C / 0x160` | `Charakter / `AgcmIDBoard`` | `Update`, `Render` |

## Vtable und Aufbau

`AgcmTextBoard` (Sprechblase über Charakteren) ist eine von mehreren Brett-Klassen in `Modules/AClient/AgcmTextBoard/` (`AgcmBaseBoard`, `AgcmIDBoard`, `AgcmHPBar`, `AgcmDmgBoard`, `AgcmTextBoardMng` u. a.); dieser Bericht behandelt nur `AgcmTextBoard.cpp`. Vtable `0x008DFD74`: Slot 0 Löschwrapper (`0x00758D10`, setzt die Vtables zurück, ruft den `AgcmBaseBoard`-Destruktor `0x00751C30` und bei Bit 0 den Pool-Löscher `0x0063CB00`), Slot 1 `Render` (`0x00758320`), Slot 2 `Update` (`0x00758B10`). Der Destruktor `~AgcmTextBoard` (`0x00758CD0`) ruft nur den Löschwrapper. Die zweite Vtable `0x008DFD64` gehört dem Pool `ApMemory<AgcmTextBoard,1000>` (`0x00758CE0`).
Konstruktor (`0x00758C60`, 101 Byte): ruft den `AgcmBaseBoard`-Konstruktor (`0x00751C40`) mit der Brett-Art, setzt die Vtables und nullt Breite, Höhe, Lebenszähler, Schriftart, Textfarbe, Schwanzart, Zeilenzahl, Charakter und `AgcmIDBoard`-Zeiger; `InitText` ist darin eingebaut (`memset` der 249 Byte Text ab `this+0x54`). Die freie Fassung `InitText` (`0x00758C40`, 20 Byte) macht dasselbe und wird von `0x0063F460` gerufen.

## Aktualisieren

`Update` (`0x00758B10`, 293 Byte) bricht ohne `AgcmIDBoard` (`this+0x160`) mit FALSE ab. Es zieht die Tick-Differenz vom Lebenszähler (`this+0x4C`) ab. Solange der Zähler nicht negativ ist, rechnet es – wenn der Klumpen des Charakters in den letzten zwei Takten berechnet wurde (Vergleich mit dem Engine-Takt `+0x11B0`) – die Weltposition des Charakters (`m_pCharacter+0xD8`, Höhe plus Konstante) in Bildschirmkoordinaten um (`AgcmTextBoardMng::Trans3DTo2D`, `0x0063D810`) und setzt `Draw` (`this+0x30`); sonst löscht es `Draw`.
Läuft der Zähler ab, schaltet es je nach ID-Art des Namensbretts (Bits 2, 8 und 1 von `IDType` bei `+0xBC`; die Quelle unterscheidet Monster, andere und eigenen Charakter, die Zuordnung der Bits zu diesen drei Arten ist nicht einzeln belegt) die Namensanzeige wieder ein (`SetEnabled`, `+0x48`), sofern die entsprechende Option des Managers (`Mng+0x11B8/0x11BC/0x11CC`) gesetzt ist, und setzt Gruppen- und Gildenanzeige (`IDBoard+0x1C4`/`+0x1CC`) von 2 auf 1 zurück, wenn die Optionen `Mng+0x11C4`/`+0x11C0` aktiv sind; Ergebnis FALSE.

## Zeichnen

`Render` (`0x00758320`, 2.025 Byte) wählt das Namensbrett (eigenes, sonst das des Hauptcharakters aus dem Manager `Mng+0x11DC`), prüft `Draw` und die Sichtbarkeit, setzt die Farbe (210, 215, 148; Alpha = Lebenszähler · 255 / 1000, höchstens 255), zeichnet die neun Teile der Blase (vier Ecken, vier Ränder, Mitte; Texturen des Managers über `GetImgBalloon(0..8)`) und den Schwanz (`GetImgBalloonTail(Schwanzart)`) mit `Image2D` (`0x007B3DE0` bis `0x007B3F00`) und schreibt dann Name, Kampf-/Gildentext und die Textzeilen mit [`AgcmFont`](AgcmFont.md):DrawTextIMMode2DWorld`. Die Aufrufe von `0x005EB940`, `0x005EB9A0` und `0x005EE730` gehören nach der Quelle zu Schriftstart, Schriftende und Textausgabe (nicht einzeln geprüft).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `Render` (2.025 Byte) wurde über Vtable-Slot, Farbwerte, Alpha-Formel und die Aufrufe der Bildfunktionen zugeordnet, nicht Zeile für Zeile verglichen; die Texturreihenfolge der neun Blasenteile ist nicht geprüft.
- Die Feldnamen der Basisklasse (Höhe, Kehrwert z, Offset) stammen aus der Quelle; die Offsets `0x08` bis `0x34` sind nur teilweise an Zugriffen belegt.
- Die Bedeutung der Manager-Felder (`Mng+0x11B0` bis `0x11DC`) ist aus den Zugriffen und den Namen in der Quelle gefolgert und nicht mit `AgcmTextBoardMng` abgeglichen.

## Querverweise

- **Erwähnt Module:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmDmgBoard`](AgcmDmgBoard.md), [`AgcmFont`](AgcmFont.md), [`AgcmHPBar`](AgcmHPBar.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmImoticonBoard`](AgcmImoticonBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md)
- **Erwähnt in:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmDmgBoard`](AgcmDmgBoard.md), [`AgcmHPBar`](AgcmHPBar.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmImoticonBoard`](AgcmImoticonBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`CFlagImoticon`](CFlagImoticon.md), [`Image2D`](Image2D.md)
