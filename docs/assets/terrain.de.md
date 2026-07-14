# Archlord Terrain & Weltdaten — Format & Organisation

Reverse-engineerte Notizen dazu, wie Archlord seine offene Welt organisiert: das Block-/Sektor-Koordinatensystem, das Terrain-Mesh selbst, terrainspezifisches Textur-Blending, sowie die Sidecar-Daten (Objekt-Culling, Gras, Wasser), die an jedem Sektor hängen. Wie die anderen Asset-Seiten beschreibt dies **nur Format und Prozess**, unabhängig von einer bestimmten Programmiersprache oder Implementierung. Baut auf [extraction.de.md](extraction.de.md) (MagPack-Archive) und [meshes.de.md](meshes.de.md) (`GEOMETRY`/`MATERIAL`/`BIN_MESH_PLUGIN`) auf — beides wird hier wiederverwendet statt wiederholt.

## 1. Welt-Koordinatensystem

Die Welt ist in ein Raster aus **Blöcken** unterteilt, jeder Block ein 16×16-Raster aus **Sektoren**. Ein Sektor ist ein festes 6400-Einheiten-Quadrat. Weltkoordinaten ergeben sich aus der Sektor-Rasterposition über:

```
world_x = (sector_x - 400) * 6400
world_z = (sector_z - 400) * 6400
```

(400 ist der Sektor-Index, der auf den Weltursprung 0,0 abbildet.) Das tatsächlich befüllte Welt-Raster umfasst einen bestimmten Bereich an Block-Koordinaten (beobachtet: grob 17–32 auf jeder Achse) — der Großteil des theoretischen Rasters ist schlicht leer/ungenutzt.

Je nachdem, welche Daten man betrachtet (Terrain-Mesh-Archive vs. Sidecar-`.dat`-Dateien, Abschnitt 4), tauchen zwei unterschiedliche Text-Kodierungen für "welcher Block" auf — beide lösen letztlich zum selben `(block_x, block_z)`-Paar auf, nur unterschiedlich formatiert (z.B. eine 4-stellige Dezimalzahl wie `1717` vs. eine 6-stellige-plus-Suffix-Form wie `0017017x`). Kein einheitliches, universelles Block-ID-String-Format über den gesamten Asset-Bestand hinweg annehmen.

## 2. Terrain-Oberflächen-Mesh

Die Terrain-Oberfläche jedes Blocks wird als zwei **MagPack-Archive** ausgeliefert (siehe [extraction.de.md § MagPack-Archive](extraction.de.md#5-magpack-archive-ma1--ma2) für das Container-Format selbst):

- `a<block-id>.ma2` — "Rough"-/Low-Detail-Variante
- `b<block-id>.ma2` — "Detail"-Variante, das tatsächliche Terrain-Mesh in voller Auflösung

Innerhalb jedes Archivs ist jeder Eintrag das Terrain eines Sektors, benannt `D<x>,<z>.dff` (Detail) oder `R<x>,<z>.dff` (Rough) — `x`,`z` sind absolute (vorzeichenbehaftete) Sektor-Rasterkoordinaten, durch Komma getrennt.

Nach der MagPack-Dekompression ist ein Eintrag ein **"DWSector"-Stream**: fast immer schlicht ein nackter RenderWare-`ATOMIC` + `GEOMETRY` (gelegentlich vorangestellt von einem `TEXTURE_DICTIONARY`-Chunk mit eingebetteten Texturen — Abschnitt 3 — und/oder einem kleinen 4-Byte-Marker vor dem `ATOMIC`-Header). Einen solchen Wrapper entfernen, und was übrig bleibt wird exakt wie ein normales Mesh geparst — gleiches `GEOMETRY`-Vertex-/Dreiecks-Layout, gleiche `MATERIAL_LIST`/`MATERIAL`, gleiche `BIN_MESH_PLUGIN`-Render-Batches wie in [meshes.de.md](meshes.de.md) beschrieben.

Vertex-Positionen innerhalb der Geometrie eines Sektors sind **sektor-lokal** gespeichert (relativ zum eigenen Ursprung dieses Sektors). Um einen Sektor korrekt in der Welt zu platzieren: den `D`/`R`-Dateinamen nach `(sector_x, sector_z)` parsen, den Weltursprung mit der Formel aus Abschnitt 1 berechnen, und das gesamte Mesh um diesen Offset verschieben (äquivalent: dem umschließenden Node diese Translation geben und die Mesh-Daten unangetastet lassen).

## 3. Terrainspezifische Materialien & Texturen

Terrain nutzt dieselbe `MATERIAL`-Struktur wie jedes andere Mesh, aber mit zwei Ergänzungen, die spezifisch fürs Boden-Rendering sind:

**Multi-Textur-Blending.** Ein Terrain-`MATERIAL` kann eine Archlord-proprietäre Extension tragen (eigener ID-Bereich, getrennt von Standard-RenderWare-Plugins) mit bis zu 5 fest zugeordneten Textur-Slots:

| Slot | Rolle |
|---|---|
| 0 | `alpha0` — Blend-Maske für `color0` |
| 1 | `color0` — erste Bodentextur |
| 2 | `alpha1` — Blend-Maske für `color1` |
| 3 | `color1` — zweite Bodentextur |
| 4 | `extra1` — eine zusätzliche Overlay-Textur (genaue Nutzung variiert) |

So blendet ein Terrain-Patch zwei (oder mehr) Bodentexturen weich ineinander — einfaches "eine Textur pro Material"-Rendering, wie bei Charakteren/Items/Objekten, greift hier nicht. Jeder vorhandene Slot referenziert einen normalen `TEXTURE`-Kind-Chunk (Namens-String), genau wie die Textur-Verknüpfung eines gewöhnlichen Materials.

**Eingebettete native Texturen.** Statt immer eine externe Texturdatei über einen Namen zu referenzieren, kann ein Terrain-Texture-Dictionary eine **vorkomprimierte, GPU-native Textur direkt einbetten**: ein Chunk mit einem kleinen Header (Texturname, ein wörtlicher `"DXT1"`-Marker, Breite/Höhe, Größe der komprimierten Daten), gefolgt von rohen **DXT1-blockkomprimierten** Pixeldaten. DXT1 kodiert jeden 4×4-Pixel-Block als:

- zwei RGB565-Referenzfarben
- eine daraus abgeleitete 4-Farben- (oder 3-Farben-plus-transparent-, je nach Farbreihenfolge) interpolierte Palette
- 16 × 2-Bit-Paletten-Indizes (einer pro Texel), gepackt in einen 32-Bit-Wert

Das Dekodieren ist ein einfaches Pro-Block-Paletten-Lookup; sobald diese eingebetteten Daten lokalisiert sind, wird keine externe Texturdatei benötigt. Dieser eingebettete native Pfad existiert zusätzlich zur (nicht anstelle der) gewöhnlichen externen-Texturdatei-Konvention, die sonst im Client üblich ist.

## 4. Sidecar-Weltdaten pro Sektor

Über das Terrain-Oberflächen-Mesh selbst hinaus existieren drei weitere Pro-Sektor-Datensätze als reine (nicht MagPack-gepackte) `.dat`-Dateien, eine Datei pro **Block**, organisiert unter `world/<art>/<prefix><block-id>.dat`:

| Art | Ordner | Präfix |
|---|---|---|
| Octree (Culling) | `world/octree/` | `ot` |
| Gras (Streu-Dekoration) | `world/grass/` | `gr` |
| Wasser | `world/water/` | `wt` |

Alle drei teilen dieselbe äußere Struktur: ein optionales `uint32`-Versionsfeld, gefolgt von einem festen 16×16-Raster (ein Slot pro Sektor im Block) aus `(offset, size)`-`int32`-Paaren, die in den Rest der Datei zeigen — also eine Index-Tabelle, die auf die nachfolgenden Pro-Sektor-Payload-Blöcke verweist. Was innerhalb der Payload jedes Sektors steht, unterscheidet sich je nach Art:

**Octree** — ein rekursiver räumlicher Partitionierungsbaum fürs Objekt-Culling. Pro Sektor: eine Anzahl Wurzelknoten, dann pro Wurzel ein `center_y`-Float gefolgt von einem Baum aus Knoten, jeder:

```
uint32   node_id
uint32   object_count
uint32   has_child        # ungleich 0 => 8 Kindknoten folgen, rekursiv
float32  bounding_sphere_radius
float32[3]  bounding_sphere_center
uint32   half_size
uint32   level
```

**Gras** — verstreute Dekorations-Instanzen (Grasbüschel usw.), gruppiert in kleinen Octree-artigen Clustern. Pro Sektor: eine Gruppenanzahl, dann pro Gruppe eine Bounding-Sphere + eine Octree-Querreferenz + eine Liste von Instanzen, jede:

```
uint32     grass_template_id     # Nachschlagen in einer Gras-Template-Tabelle (Textur-/Form-/Animationsinfo)
float32[3] position
float32[2] rotation
float32    scale
```

**Wasser** — flache Wasser-Tiles plus animierte "Wave"-Regionen. Pro Sektor: eine Wasser-Tile-Anzahl, dann pro Tile eine Status-ID (in eine Wasser-Status-/Textur-Tabelle), ein Raster-Offset/Größe (Tile-Position und -Ausdehnung in festen Schrittweiten) und eine Höhe; gefolgt von einer Wave-Anzahl und Pro-Wave-Records (Status-ID, Offset, Breite/Höhe, Spawn-Anzahl, Rotation, Translationsgeschwindigkeit, und ein präziser 3D-Ursprung).

## 5. Vorgerenderte Minimap-Kacheln (separates, einfacheres System)

Unabhängig von allem oben Genannten liefert der Client auch **vorgerenderte Raster-Bildkacheln** für die Weltkarten-UI im Spiel aus — nicht aus dem Terrain-Mesh rekonstruiert, sondern schlicht statische Bilder. Ein Kachel-Set pro Block, benannt `map<block_x><block_z><part>.<ext>`, wobei `part` einer von vier Buchstaben ist (`a`/`b`/`c`/`d`), die ein 2×2-Raster bilden, das sich zu einer größeren Pro-Block-Kachel zusammensetzt. Fügt man die zusammengesetzten Kacheln aller Blöcke in Rasterreihenfolge zusammen, ergibt sich ein vollständiges Welt-Übersichtsbild.

## 6. Praktischer Ablauf von A bis Z

1. Die benötigten Block(s) bestimmen und deren beide Terrain-Archive (`a`/`b`-Präfix) sowie die drei Sidecar-`.dat`-Dateien (`ot`/`gr`/`wt`-Präfix) unter `world/` lokalisieren.
2. Die MagPack-Terrain-Archive entpacken (gemäß [extraction.de.md](extraction.de.md#5-magpack-archive-ma1--ma2)); für jeden `D`/`R`-Eintrag den DWSector-Wrapper entfernen und den verbleibenden `ATOMIC`+`GEOMETRY`-Stream wie ein gewöhnliches Mesh parsen ([meshes.de.md](meshes.de.md)).
3. Das Mesh jedes Sektors anhand von `(sector_x, sector_z)` aus dem Dateinamen und der Formel aus Abschnitt 1 in den Weltraum verschieben.
4. Terrain-Materialien auflösen: zuerst auf die 5-Slot-Multi-Textur-Extension prüfen (Abschnitt 3), bevor man von einer einzelnen Textur ausgeht; Texture-Dictionaries auf eingebettete native DXT1-Daten prüfen, bevor man eine externe Texturdatei-Referenz annimmt.
5. Die Offset-/Größen-Tabelle in jeder Sidecar-`.dat`-Datei parsen, dann die Octree-/Gras-/Wasser-Payload jedes befüllten Sektors bei Bedarf dekodieren (Abschnitt 4).
6. Optional die vorgerenderten Minimap-Kacheln (Abschnitt 5) zu einer schnellen Weltübersicht zusammensetzen, ohne irgendetwas vom Obigen anzufassen.

English version: [terrain.md](terrain.md)
