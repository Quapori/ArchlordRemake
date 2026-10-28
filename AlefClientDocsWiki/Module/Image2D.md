# Image2D (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `Image2D` (Vierecke in Bildschirmkoordinaten für Bretter über Charakteren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Disassembly (`x86dis.py`), Aufrufer in den Brett-Klassen, EP8-Quelle `Modules/AClient/AgcmTextBoard/Image2D.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 6 von 8 Quellmethoden sind zugeordnet. Die zwei Fassungen von `SetPos` und `SetUV` mit `RwV2d`-Parametern fehlen im Binary: in den Brett-Klassen steht nirgends ein Aufruf mit `RwV2d`-Argumenten.
- **Abweichungen:** keine festgestellt; die Quelle schreibt in der `RwV2d`-Fassung von `SetPos` für die Y-Werte der Vertices 1 bis 3 irrtümlich `.x` (Fehler der Quelle, ohne Auswirkung, weil nie aufgerufen).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`Image2D.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetCameraTrans` | `0x007B3DE0` | 35 | von Hand geprüft |
| 1 | `SetPos` | `0x007B3E10` | 60 | von Hand geprüft |
| 2 | `SetUV` | `0x007B3E50` | 43 | von Hand geprüft |
| 3 | `SetPos` | – | | nicht im Binary: Fassung mit `RwV2d`-Parametern, in den Brett-Klassen ohne Aufrufer |
| 4 | `SetUV` | – | | nicht im Binary: Fassung mit `RwV2d`-Parametern, in den Brett-Klassen ohne Aufrufer |
| 5 | `SetColor` | `0x007B3E80` | 45 | von Hand geprüft |
| 6 | `SetColor` | `0x007B3EB0` | 72 | von Hand geprüft |
| 7 | `Render` | `0x007B3F00` | 50 | von Hand geprüft |

6 von 8 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `SetColor_argb` (`0x007B3E80`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x00..0x6F` | `vier `RwIm2DVertex` zu je 0x1C Byte` | alle Funktionen |
| `Vertex+0x08 / 0x0C` | `Bildschirm-Z / Kehrwert z` | `SetCameraTrans` |
| `Vertex+0x10` | `Farbe (BGRA, 32 Bit)` | `SetColor` |
| `Vertex+0x14 / 0x18` | `U / V` | `SetUV` |

## Aufbau

`Image2D` ist ein Vierecks-Zeichner (vier `RwIm2DVertex` zu je 28 Byte, 112 Byte) und als statisches Objekt [`AgcmBaseBoard`](AgcmBaseBoard.md):ms_Image2D` von allen Brettern benutzt. Die Funktionen liegen im Binary als Block bei `0x007B3DE0` bis `0x007B3F00` und sind in Lücken des Ghidra-Exports (nur über Disassembly mit `x86dis.py` lesbar).
Vertex-Layout (aus den Schreibzugriffen): Bildschirm-X `+0`, -Y `+4`, -Z `+8`, Kehrwert z `+0xC`, Farbe `+0x10`, U `+0x14`, V `+0x18`; die Vertices folgen im Abstand 0x1C.

## Funktionen

`SetCameraTrans` (`0x007B3DE0`) schreibt Kehrwert z und Bildschirm-Z in alle vier Vertices; die Kamera-Koordinaten setzen die RenderWare-Makros im D3D9-Treiber nicht (nur zwei Felder je Vertex werden geschrieben). `SetPos(x, y, w, h)` (`0x007B3E10`) und `SetUV` (`0x007B3E50`) setzen die Ecken (oben links, oben rechts, unten rechts, unten links). `SetColor(a, r, g, b)` (`0x007B3E80`) und `SetColor(RwRGBA&)` (`0x007B3EB0`) schreiben die Farbe in alle vier Vertices.
`Render` (`0x007B3F00`) setzt, falls ein Raster angegeben ist, den Render-Zustand „Textur-Raster“ (Zustand 1) und zeichnet über den Treiber `Im2DRenderPrimitive` (Vtable-Slot `+0x34` der Treibertabelle `0x00980F80`) ein Dreiecksfächer aus vier Vertices; der Parameter für die Primitivart wird, wie in der Quelle, ignoriert.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass die `RwV2d`-Fassungen im Binary fehlen, folgt aus dem Fehlen von Aufrufen in den Quelldateien des Verzeichnisses; ein Abgleich mit anderen Modulen, die `Image2D` benutzen, wurde nicht gemacht (die Klasse liegt in [`AgcmTextBoard`](AgcmTextBoard.md)).
- Konstruktor und Destruktor der Klasse (nullen der 112 Byte) wurden nicht gesucht; sie sind keine Quellmethoden der Zählung.
- Die Zuordnung von `SetColor(a, r, g, b)` zu `0x007B3E80` und der `RwRGBA`-Fassung zu `0x007B3EB0` folgt aus der Parameterform (vier Byte-Argumente gegenüber einem Zeiger).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht als eigene Funktion: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md)
