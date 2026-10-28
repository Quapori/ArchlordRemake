# Karte: Sektordaten (Compact) und ihre Verpackung

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Formate und Werkzeugcode](Index.md) · [Modul AgcmMap](../Module/AgcmMap.md)*

Dieser Artikel beschreibt, was der **Editor-/Werkzeugcode** der EP8-Quelle über die Kartendateien verrät, und gleicht es mit dem 2017er Client-Binary ab. Der Schreibcode steckt im Client-Binary nicht (der Linker hat ihn entfernt, siehe [AgcmMap](../Module/AgcmMap.md)); die Quelle zeigt, **wie** die Dateien entstehen, das Binary beweist, **dass** der Client sie so liest.

Quellen: `Modules/AClient/AgcmMap/AgcmMap.cpp` (`SaveAll`), `Modules/APublic/ApmMap/ApWorldSector.cpp` (`SaveCompactData`, `_LoadCompactData_FromBuffer`), Header `Include/ApWorldSector.h` und `Include/ApmMap.h`. Binary: `FUN_0051BBE8` (Lader der Compact-Daten, 640 Byte), Build 2017-08-15. Die Zahlen und Formate der installierten Dateien stehen in [Welt-MA1-MA2-Materialien](../Welt-und-Engine/Welt-MA1-MA2-Materialien.md).

## Weltraster

| Größe | Wert | Quelle |
|---|---:|---|
| Sektoren je Achse | 800 (`MAP_WORLD_INDEX_WIDTH`) | `ApmMap.h` |
| Breite eines Sektors | 6400 Einheiten (`MAP_SECTOR_WIDTH`) | `ApmMap.h` |
| Compact-Raster je Sektor | 16 × 16 Segmente (`ALEF_COMPACT_DATA_DEFAULT_DEPTH`) | `ApWorldSector.h` |
| Schrittweite eines Segments | 400 Einheiten (`MAP_STEPSIZE`, 6400 / 16) | `ApmMap.h` |
| Sektoren je Division | 16 × 16 (`MAP_DEFAULT_DEPTH`) | `ApmMap.h` |
| Array-Index eines Sektors | Sektorindex + 400 | `SectorIndexToArrayIndexX` |

Division eines Sektors: `GetDivisionIndex(arrayX, arrayZ) = (arrayX / 16) * 100 + (arrayZ / 16)`. Das stimmt mit der Formel der Dateinamen im Bericht [Welt-MA1-MA2-Materialien](../Welt-und-Engine/Welt-MA1-MA2-Materialien.md) überein (`((sectorX + 400) >> 4) * 100 + ((sectorZ + 400) >> 4)`).

## Was `SaveAll` schreibt

`AgcmMap::SaveAll(bGeometry, bTile, bCompact, …)` läuft über alle Sektoren des Ladebereichs (nur Vielfache einer Division) und tut zweierlei:

1. **Pro Sektor** speichert es drei Einzeldateien über `ApWorldSector` (`SaveCompactData`, `SaveDetailDataGeometry`, `SaveDetailDataTile`). Die Einzeldateien heißen nach Array-Index:
   - Compact: `c<x>,<z>.amf` (Client-Fassung) bzw. `s<x>,<z>.amf` (Serverfassung, ohne Sperrlinien);
   - Geometrie: `G<x>,<z>.amf`; Kachel („Moonee“): `T<x>,<z>.amf`.
2. **Pro Division** (16 × 16 Sektoren) packt es die Einzeldateien mit `PackFiles` in einen Container, über eine temporäre Datei `test.tmp` (danach alte Datei löschen, `test.tmp` umbenennen, optional Kopie in ein Sicherungsverzeichnis). Containernamen laut Quelle: `c%04d.mpf` (Compact), `g%04d.mpf` (Geometrie), `m%04d.mpf` (Kachel), `%04d` = Division.

Die Einträge im Container heißen nach den Mustern `C%d,%d.amf`, `G%d,%d.amf`, `T%d,%d.amf` (Großbuchstabe, Array-Index). Die ausgelieferten Dateien `a<division>x.ma1` enthalten laut Bericht `C*.amf`-Einträge; die Umbenennung von `.mpf` in `.ma1`/`.ma2` und die Aufteilung auf `a…` und `b…` ist in dieser Quelle nicht belegt und geschieht offenbar in einem späteren Export-Schritt.

## Format einer Compact-Datei (`C…amf`)

Aufbau laut `SaveCompactData` (Version `0x1003`, `ALEF_COMPACT_FILE_VERSION4`), alle Werte Little Endian:

| Offset | Größe | Inhalt |
|---:|---:|---|
| 0 | 4 | Version (`0x1003`) |
| 4 | 4 | Sektor-Flags (`m_uFlag`) |
| 8 | 4 | Tiefe `nDepth` (16) |
| 12 | `nDepth² × 4` | Segmentfeld, Zeile für Zeile (`z` außen, `x` innen), je 4 Byte `ApCompactSegment` |
| danach | 4 | Anzahl Sperrlinien (nur Client-Fassung; die Serverfassung endet davor) |
| danach | Anzahl × 28 | Sperrlinien `AuLineBlock`: Anfang und Ende je 3 `float` (24 Byte) und eine 32-Bit-Seriennummer |

Bei 16 × 16 Segmenten ist das Feld 1024 Byte groß, die Datei ohne Sperrlinien 1036 Byte.

**Ein Segment (4 Byte):**

| Byte | Bits | Feld | Bedeutung |
|---:|---|---|---|
| 0 | 0 | `bEdgeTurn` | Diagonalrichtung der Kachel |
| 0 | 1–7 | `tiletype` | Kachelart |
| 1 | 0–3 | `geometryblock` | Sperrung: Bit 0 = Boden (`GB_GROUND`), Bit 1 = Himmel (`GB_SKY`) |
| 1 | 4 | `bNoLayer` | keine Schicht; die Höhe wird dann aus befahrbaren Objekten genommen |
| 1 | 5–7 | reserviert | |
| 2–3 | 16 Bit | `uRegioninfo` | Region des Segments |

Die Bitreihenfolge folgt der Deklaration (C++-Bitfelder, MSVC: niederwertige Bits zuerst); das Binary bestätigt sie nur indirekt (siehe unten).

**Sektor-Flags** (`ApWorldSector::SECTOR_OPTIONS`, Auszug): `OP_DONOTLOADSECTOR = 0x0002` (der Client lädt diesen Sektor nicht), `OP_HEIGHTUPDATEAFTERLOAD = 0x0004` (nach dem Laden Höhe neu abfragen; wird zur Laufzeit von `AgcmMap::GetHeight` gesetzt).

### Ältere Versionen (nur zum Lesen)

| Version | Aufbau |
|---|---|
| `0x1000` | Tiefe, dann Segmente zu je **6 Byte** (alte Form `ApCompactSegment_20040917`, ohne Flag-Feld) |
| `0x1001` | Flags, Tiefe, Segmente zu 6 Byte |
| `0x1002` | Flags, Tiefe, Segmente zu 4 Byte, Sperrlinien; beim Lesen werden `bNoLayer` und Reserve-Bits zurückgesetzt |
| `0x1003` | aktuell (siehe oben) |

## Abgleich mit dem 2017er Binary

Der Lader `FUN_0051BBE8` (Aufbau: `switch` über die Version) bestätigt jeden Punkt:

- Versionen `0x1000`, `0x1001`, `0x1002`, `0x1003` kommen vor, jeder andere Wert liefert FALSE.
- Ab `0x1001` wird das Flag-Feld nach `this+0x30` gespeichert; `Flag & 2` (`OP_DONOTLOADSECTOR`) bricht das Laden mit FALSE ab.
- Das Segmentfeld ist bei `0x1002`/`0x1003` ein einziges `memcpy` über `Tiefe² × 4` Byte (Segmente zu 4 Byte); bei `0x1000`/`0x1001` werden 6-Byte-Einträge einzeln auf 4 Byte gekürzt (2 Byte Kachelinfo + 1 Byte Region).
- Nach dem Feld liest er nur dann Sperrlinien, wenn noch Daten übrig sind (`gelesen < Gesamtgröße`): erst ein 32-Bit-Zähler, dann Einträge zu **7 Doppelwörtern (28 Byte)** – genau `AuLineBlock`.
- Bei `0x1002` löscht er in Byte 1 jedes Segments Bit 4 (`& 0xEF`) und die Bits 5–7 (`& 0x1F`), also `bNoLayer` und die Reserve: das bestätigt die Lage von `bNoLayer` (Bit 4) in Byte 1.

## Zusammenhang mit der Laufzeit

- `AgcmMap::GetHeight` (`0x005F6040`) liest `bEdgeTurn` und `bNoLayer` aus dem Compact-Segment, wenn die Detailstufe nicht geladen ist, und nutzt `bNoLayer`, um bei befahrbaren Objekten die Höhe von oben zu bestimmen.
- Die Sperrlinien (`AuLineBlock`) sind die Blockierungs-Linien, die Server und Client zur Wegprüfung benutzen.

## Noch nicht dokumentiert

Aus der Quelle noch nicht gelesen und mit dem Binary nicht abgeglichen: `SaveDetailDataGeometry` / `SaveDetailDataTile` (Dateien `G…amf`, `T…amf`), `BspExport` (erzeugt die `R…dff`/`D…dff`-Sektoren) und `CreateCompactDataFromDetailInfo` (leitet das Compact-Feld aus den Detaildaten ab). Offen ist auch die Frage, wie aus `c%04d.mpf` die ausgelieferten `.ma1`-Dateien werden.
