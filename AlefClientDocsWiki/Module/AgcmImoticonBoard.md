# AgcmImoticonBoard (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmImoticonBoard` (Symbol-Animationen über Charakteren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmImoticonBoard.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: `Update` und `Render` sind zugeordnet; dazu Konstruktor und Löschwrapper.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmImoticonBoard.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Update` | `0x00756F20` | 239 | von Hand geprüft |
| 1 | `Render` | `0x00757010` | 2946 | von Hand geprüft |

2 von 2 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmImoticonBoard` (`0x00757BB0`), `~AgcmImoticonBoard` (`0x00757C00`), `scalar_deleting_dtor` (`0x00757C40`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | ``m_Type` (Brett-Art, [`AgcmBaseBoard`](AgcmBaseBoard.md))` | `Render` |

## Vtable und Aufbau

`AgcmImoticonBoard` (animierte Symbole über Charakteren: Fehlschlag, Ausweichen, Block, Kritisch, Charisma) ist von `AgcmBaseBoard` abgeleitet; Vtable `0x008DFCCC`: Slot 0 Löschwrapper (`0x00757C40`), Slot 1 `Render` (`0x00757010`), Slot 2 `Update` (`0x00756F20`). Konstruktor `0x00757BB0` (74 Byte, ruft `AgcmBaseBoard::AgcmBaseBoard` und nullt Charakter, Bild, Animationsart, -zähler und beide Parameterfelder; einziger Aufrufer ist [`AgcmTextBoardMng`](AgcmTextBoardMng.md):_CreateImoticon` `0x0063EA10`), Destruktorrumpf `0x00757C00`; Pool `ApMemory<AgcmImoticonBoard,1000>` (`0x00757C10`).

## Aktualisieren und Zeichnen

`Update` (`0x00756F20`, 239 Byte) zählt den Animationszähler hoch, endet bei Ablauf mit FALSE und rechnet sonst – wenn der Klumpen kürzlich berechnet wurde – die Position des Charakters (Mittelpunkt der Pick-Hülle, sonst Charakterposition plus Höhe) in Bildschirmkoordinaten um (`AgcmCharacter::GetCharacterData`, `Trans3DTo2D` `0x0063D810`).
`Render` (`0x00757010`, 2.946 Byte) verzweigt nach der Brett-Art: Fehlschlag, Ausweichen, Dodge und Reflex skalieren das Symbol mit nachlaufendem Echo; Kritisch, Angriff und die drei Charisma-Arten zeichnen es in zwei Hälften mit zufälligem Wackeln (`rand`); Block lässt es nach rechts und links schwingen und zerlegt es in der zweiten Hälfte in Streifen von vier Bildpunkten Höhe. Gezeichnet wird über `Image2D` (`0x007B3DE0` bis `0x007B3F00`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `Render` (2.946 Byte) wurde über Vtable-Slot, Größe und die Aufrufe der `Image2D`-Funktionen zugeordnet, nicht Zeile für Zeile verglichen; die Zuordnung der Brett-Arten zu den drei Zweigen folgt der Quelle.
- `Update` wurde über Vtable-Slot, Größe und die Aufrufe (`GetCharacterData`, `Trans3DTo2D`) zugeordnet.
- Die Feldoffsets hinter `+0x40` (Animationsfelder) wurden nicht vermessen.

## Querverweise

- **Erwähnt Module:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md)
- **Erwähnt in:** [`AgcmTextBoard`](AgcmTextBoard.md)
