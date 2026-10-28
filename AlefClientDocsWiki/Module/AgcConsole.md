# AgcConsole (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse `AgcConsole` (Konsolenfenster) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIConsole/AgcmUIConsole.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 19 von 23 Quellmethoden sind zugeordnet; viele Zuordnungen stammen aus der Registrierungsreihenfolge in `init` und aus der Vtable.
- **Korrektur:** `0x005C36C0` ist `render` (1982 Byte), nicht `OnInit`.
- **Fenstergröße:** 860 × 510 Pixel.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcConsole.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `init` | `0x005C44A0` | 3137 | ver |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnWindowRender` | `0x005C23D0` | 17 | ver |
| 3 | `OnKeyDown` | `0x005C34F0` | 431 | ver |
| 4 | `OnChar` | `0x005C4320` | 334 | ver |
| 5 | `OnKeyUp` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `OnLButtonDown` | `0x005C23F0` | 20 | ver |
| 7 | `render` | `0x005C36C0` | 1982 | ver (Korrektur: war OnInit) |
| 8 | `searchTextLengthOfGivenExtent` | `0x005C2410` | 162 | ver |
| 9 | `getNumberOfLines` | `0x005C24C0` | 45 | ver |
| 10 | `isVisibleLine` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `DrawOneLine` | `0x005C24F0` | 208 | ver |
| 12 | `DrawFrame` | `0x005C25C0` | 340 | ver |
| 13 | `moveTL` | `0x005C2720` | 20 | ver |
| 14 | `moveTR` | `0x005C2740` | 32 | ver |
| 15 | `moveBL` | `0x005C2760` | 32 | ver |
| 16 | `moveBR` | `0x005C2780` | 40 | ver |
| 17 | `moveCenter` | `0x005C27B0` | 44 | ver |
| 18 | `registerWatch` | `0x005C2B60` | 436 | Zeichenkette |
| 19 | `registerServerKeyword` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `passServerDo` | `0x005C40D0` | 366 | Zeichenkette |
| 21 | `setCallbackPtr` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `DrawWatchList` | `0x005C2D20` | 898 | Zeichenkette |

19 von 23 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x005C3410`), `~AgcConsole` (`0x005C34E0`), `AgcConsole` (`0x005C3F00`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1DC` | `Zeiger auf [`AgcmFont`](AgcmFont.md) (`pAgcmFont_`)` | `searchTextLengthOfGivenExtent` |
| `0x1E8` | `Scroll-Position (`scrollBar_`)` | `DrawOneLine` |

## Umfang

`AgcConsole` (Quelle `AgcmUIConsole.cpp`, 23 Methoden) ist das Konsolenfenster und erbt von `AgcWindow` und `AuConsole`. Die zweite Vtable bei `0x008BBA74` gehört zu `AuConsole`; ihr zweiter Eintrag ist die überschriebene `render` (`0x005C36C0`). Die bisherige Benennung dieser Adresse als `OnInit` war falsch und ist korrigiert: `AgcConsole::OnInit` (3 Zeilen, `return TRUE`) ist im Binary der gemeinsame Rumpf `0x0067AC90`.

## Vtable (Fenster)

Fenster-Vtable bei `0x008BBA84`: Slot 8 `OnWindowRender` (`0x005C23D0`, springt über die zweite Vtable in `render`), Slot 9 `OnKeyDown` (`0x005C34F0`), Slot 28 `OnChar` (`0x005C4320`). `OnChar` behandelt Eingabe (`0xD`) und Esc (`0x1B`); die Eingabetaste ruft `passServerDo` (`0x005C40D0`). `OnLButtonDown` (`0x005C23F0`) macht die Konsole zum aktiven Eingabefeld.

## Skript-Anmeldung (init, 0x005C44A0)

Registriert den Skript-Typ `AgcConsole console` mit den Methoden `moveTL` (`0x005C2720`), `moveTR` (`0x005C2740`), `moveBL` (`0x005C2760`), `moveBR` (`0x005C2780`), `moveCenter` (`0x005C27B0`), `registerWatch` (`0x005C2B60`), `showWatch` (`0x005C1F00`) und `hideWatch` (`0x005C1F10`) sowie der Variablen `bufferForWatching_`. Reihenfolge und Zahl stimmen mit der Quelle überein. Die Fenstergröße der `move…`-Funktionen ist 0x35C × 0x1FE (860 × 510).

## Zeichnen

`render` zeichnet Rahmen (`DrawFrame`, `0x005C25C0`), die Zeilen (`DrawOneLine`, `0x005C24F0`) und die Eingabezeile; Zeilenumbruch nach Pixelbreite über `searchTextLengthOfGivenExtent` (`0x005C2410`, Schriftmodul `+0xB98`) und `getNumberOfLines` (`0x005C24C0`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen; die frühere Namenszuordnung `OnInit` → `0x005C36C0` ist ein Fehler des Namensbestands und wurde berichtigt.

## Grenzen

- `render` und `OnKeyDown` wurden nur über Vtable-Slots, Aufrufer und Größe zugeordnet, nicht verglichen.
- `OnKeyUp`, `isVisibleLine`, `registerServerKeyword`, `setCallbackPtr` und `showWatch`/`hideWatch` sind eingebaut oder nicht als Quellmethoden gelistet.
- Die Konstruktor- und Destruktor-Teile (`0x005C3F00`, `0x005C3410`, `0x005C34E0`) sind nicht Teil der Methodenliste.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmFont`](AgcmFont.md), [`AgcmUIConsole`](AgcmUIConsole.md)
- **Erwähnt in:** [`AgcmUIConsole`](AgcmUIConsole.md)
