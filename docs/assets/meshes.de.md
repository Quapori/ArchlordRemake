# Archlord Charakter-, Item- & Objekt-Meshes — Format & Organisation

Reverse-engineerte Notizen dazu, wie Archlords 3D-Meshes (Charaktere, Items, Objekte) intern aufgebaut sind, und — davon getrennt — wie die Datentabellen des Spiels organisieren und auffindbar machen, *welche* Mesh-Datei zu welchem Charakter/Item/Objekt gehört. Wie die Seiten [Extraktion](extraction.md) und [Animation](animation.md) beschreibt dies **nur Format und Prozess**, unabhängig von einer bestimmten Programmiersprache oder Implementierung. Baut auf den [Container-Grundlagen der Animations-Seite](animation.de.md#1-grundlagen-des-containers) auf (RenderWare-Chunk-Header, `CLUMP`/`GEOMETRY_LIST`/`GEOMETRY`/`ATOMIC`); Skelett- und Skinning-Details stehen dort und werden hier nicht wiederholt.

## 1. Ein Format, drei Rollen

Charaktere, Items und Objekte sind **keine unterschiedlichen Dateiformate** — alle drei sind ganz normale RenderWare-`CLUMP`-Dateien (`.dff`), die genau die unten beschriebenen Geometrie-/Material-Strukturen nutzen. Was sich zwischen ihnen tatsächlich unterscheidet:

- **Ob der Clump ein Skelett trägt.** Charaktere (und am Charakter getragene Items) sind meist geskinnt (siehe [animation.de.md](animation.de.md)); statische Weltobjekte und einfache Item-Pickups meist nicht — nur ein reines Mesh mit einer Bind-Transformation.
- **Wie die Datentabellen des Spiels die Datei referenzieren und benennen** — siehe Abschnitt 5.

## 2. Mesh-Geometrie-Payload

Die Struct-Payload eines `GEOMETRY`-Chunks enthält alles zu den Vertices und rohen Dreiecken eines Meshes:

```
uint16  flags
uint8   tex_coord_sets
uint8   native_flags       # ungleich 0 = plattform-/GPU-natives Layout, NICHT das generische Layout unten
uint32  triangle_count
uint32  vertex_count
uint32  morph_target_count
-- danach, direkt hintereinander: --
[falls PRELIT-Flag gesetzt]  uint8[4] × vertex_count      # Pro-Vertex-RGBA-"Prelit"-Farbe
für jedes UV-Set (tex_coord_sets, oder als 1/2 aus den TEXTURED/TEXTURED2-Flags abgeleitet, falls das Count-Feld 0 ist):
    float32[2] × vertex_count                              # UV-Paare
für jedes Dreieck (triangle_count):
    uint16 × 4                                               # 3 Vertex-Indizes + 1 Material-Index, siehe Vorbehalt unten
für jeden Morph-Target (morph_target_count):
    float32[4]   Bounding-Sphere (Center xyz, Radius)
    uint32       has_vertices
    uint32       has_normals
    [falls has_vertices]  float32[3] × vertex_count          # Positionen
    [falls has_normals]   float32[3] × vertex_count          # Normalen
```

Zwei Dinge an diesem Layout sind leicht falsch zu verstehen:

- **Vertex-Positionen und Normalen sind kein separater Top-Level-Block — sie liegen innerhalb von Morph-Target 0.** Ein nicht-morphendes Mesh hat trotzdem `morph_target_count == 1`; die Vertex-/Normal-Arrays dieses einen Morph-Targets *sind* die Basis-Mesh-Daten. Weitere Morph-Targets (1..N) nur lesen, wenn tatsächlich Blend-Shape-Daten benötigt werden.
- **Das "Prelit"-Flag ist nicht vollständig zuverlässig, und die Feldreihenfolge im Dreiecks-Record ebenfalls nicht.** Manche Dateien setzen das Prelit-Farb-Flag, ohne tatsächlich Farbdaten zu speichern, und (unabhängig davon) wurde beobachtet, dass die Position des Material-Index innerhalb der vier `uint16`-Felder eines Dreiecks variiert — manche Dateien nutzen effektiv `(v0, v1, v2, material)`, andere setzen den Material-Index an den Anfang oder eine andere Stelle. Nicht blind einer einzelnen fest angenommenen Reihenfolge vertrauen; stattdessen prüfen, welche Interpretation Vertex-Indizes `< vertex_count` und einen Material-Index `< material_count` für diese Geometrie ergibt, und bei Werten außerhalb des gültigen Bereichs auf die andere Kandidaten-Reihenfolge ausweichen.

## 3. Materialien & Texturen

Ein `GEOMETRY` referenziert eine benachbarte `MATERIAL_LIST`, deren Struct-Payload lautet:

```
uint32   material_count
int32[material_count]   material_indices   # Index in einen gemeinsam genutzten Material-Pool; normalerweise
                                            # folgt für jeden Eintrag ein echter Pro-Geometrie-MATERIAL-Kind-Chunk
```

Die Struct-Payload jedes `MATERIAL`-Chunks:

```
uint32   flags
uint8[4] color             # RGBA
int32    unused
int32    textured           # ungleich 0 => ein Kind-Chunk TEXTURE folgt, der die zu nutzende Textur benennt
-- an einem festen späteren Offset: --
float32  ambient
float32  specular
float32  diffuse
```

Die Textur selbst wird über einen Namen referenziert (ein String-Chunk innerhalb des `TEXTURE`-Kind-Chunks) — diesen Namen auf eine tatsächliche Bilddatei aufzulösen ist ein eigener Schritt, der von der Textur-Format-Dokumentation abgedeckt wird, nicht von dieser Seite.

## 4. Render-fertige Dreiecks-Batches (nach Material aufgeteilte Index-Buffer)

Die rohe Dreiecksliste aus Abschnitt 2 hat einen eingebetteten Material-Index pro Dreieck, was fürs Rendering nicht direkt nutzbar ist (GPUs zeichnen zusammenhängende Batches pro Material, keine durchmischten Dreiecke). Eine `BIN_MESH_PLUGIN`-Extension am `GEOMETRY` liefert genau diese vorab aufgeteilte, render-fertige Form:

```
uint32   flags         # niedrigstes Byte = Primitiv-Typ (0=tri_list, 1=tri_strip, 2=tri_fan, 4=line_list, 8=polyline, 0x10=point_list); Bit 0x0100 = unindiziert
uint32   mesh_count     # ein Eintrag pro tatsächlich genutztem Material
uint32   total_indices
für jedes Mesh (mesh_count):
    uint32   index_count
    uint32   material_index
    uint32[index_count]   indices    # in dieselben Vertex-Arrays wie Abschnitt 2; je nach Primitiv-Typ
                                       # oben als Dreiecksliste oder -Strip zu interpretieren
```

Wenn beides vorhanden ist, `BIN_MESH_PLUGIN` gegenüber einer selbst rekonstruierten Aufteilung aus der rohen Dreiecksliste bevorzugen — es sind die tatsächlichen Daten, aus denen der originale Renderer zeichnet, bereits pro Material aufgeteilt und geordnet.

## 5. Skinning (Verweis)

Hat ein `GEOMETRY` eine `SKIN_PLUGIN`-Extension, ist das Mesh an ein Skelett gebunden (Pro-Vertex-Knochenindizes/-Gewichte plus Inverse-Bind-Matrizen). Diese Struktur, und wie sie mit der Joint-Reihenfolge eines Skeletts und mit Animationsdateien zusammenhängt, ist vollständig in [animation.de.md](animation.de.md#3-mesh--skelett-bindung-skinning) dokumentiert. Ein `GEOMETRY` ohne `SKIN_PLUGIN` ist schlicht statische Geometrie, platziert über die Frame-Transformation seines zugehörigen `ATOMIC`.

## 6. Wie Charaktere/Items/Objekte gefunden und benannt werden

Nichts davon steht in den `.dff`-Dateien selbst — es wird vollständig von externen Konfigurationstabellen gesteuert (INI-Dateien, die mit dem Client ausgeliefert werden), über eine gemeinsame Dateinamens-Konvention:

```
<prefix><7-stellige-Hex-ID>.dff
```

ein einzelner Kleinbuchstabe, eine 7-stellige hexadezimale numerische ID, und die Endung. Diese numerische ID ist eine eigenständige "Ressourcen-ID", die in einem INI-Feld gespeichert ist — nicht zwangsläufig identisch mit der eigenen Template-ID (TID) des Charakters/Items/Objekts.

**Charaktere** — werden direkt aus einer Charakter-Template-INI aufgelöst, indiziert nach TID. Relevante Felder und ihr Präfix:

| Feld | Präfix | Bedeutung |
|---|---|---|
| `DFF` | `a` | Haupt-Körper-Mesh |
| `DEFAULT_ARMOUR_DFF` | `b` | Standard-Rüstungs-Mesh |
| `PICK_DFF` | `c` | Klick-/Pickup-Ziel-Mesh für den Charakter selbst |

Gesichts- und Haar-Customization-Meshes nutzen statt einer in der INI gespeicherten ID ein anderes, deterministisches Schema — Präfix `v`, mit der numerischen ID berechnet aus der TID des Charakters:

```
face_id = TID × 0x200 + local_index
hair_id = TID × 0x100 + local_index
```

**Items** — werden über einen zweistufigen Lookup aufgelöst: eine Item-Entry-INI bildet eine Item-TID auf einen *Template-Dateinamen* ab, und diese separate Template-Datei enthält dann die eigentlichen Mesh-Felder, wieder indiziert nach TID:

| Feld | Präfix | Bedeutung |
|---|---|---|
| `BASE_DFF` | `d` | Am Charakter getragenes Equip-Mesh |
| `SECOND_DFF` | `e` | Sekundäre Equip-Variante |
| `FIELD_DFF` | `f` | Anzeige-Mesh, wenn das Item am Boden liegt |
| `PICK_DFF` | `g` | Klick-/Pickup-Ziel-Mesh für das Item |

**Objekte** (Weltobjekte, statisch oder einfach animierte Einrichtungen) — werden direkt aus einer Objekt-Template-INI aufgelöst, indiziert nach TID:

| Feld | Präfix | Bedeutung |
|---|---|---|
| `DFF` | `h` | Haupt-Objekt-Mesh |
| (Kollision) | `i` | Reines Kollisions-Mesh, getrennt vom sichtbaren Mesh |
| `ANIMATION` | — | Optional; manche Objekte (Türen, Maschinen, …) referenzieren eine Animationsdatei genau wie Charaktere |

Aus einer dieser Tabellen referenzierte Animationsdateien folgen der bereits in [animation.de.md](animation.de.md#5-wie-alles-zusammenhängt) beschriebenen Namensregel: den Wert nach dem letzten `:` im INI-Eintrag nehmen und `.ean` anhängen, falls noch keine Endung vorhanden ist.

## 7. Praktischer Ablauf von A bis Z

1. Kategorie festlegen (Charakter / Item / Objekt) und die passende(n) Template-INI(s) laden; bei Items zuerst die Entry-INI → Template-Datei-Indirektion auflösen.
2. Den TID-Abschnitt nachschlagen, die relevanten `*_DFF`-Felder lesen, und jede numerische ID über `<prefix><id:07x>.dff` in einen Dateinamen umwandeln.
3. Diesen Dateinamen im (bereits extrahierten/entschlüsselten) Client-Baum lokalisieren und seinen `CLUMP`-Chunk-Baum parsen.
4. `GEOMETRY` lesen (Positionen/Normalen aus Morph-Target 0, UVs, `MATERIAL_LIST`) und `BIN_MESH_PLUGIN` für nach Material aufgeteilte Render-Batches bevorzugen (Abschnitte 2–4).
5. Falls ein `SKIN_PLUGIN` vorhanden ist, das Skelett und optional eine passende Animation wie in [animation.de.md](animation.de.md) beschrieben auflösen.
6. Bei Charakteren zusätzlich `DEFAULT_FACE`/`DEFAULT_HAIR`-Einträge über die TID-basierte Formel aus Abschnitt 6 in `v`-präfixierte Customization-Meshes auflösen.

English version: [meshes.md](meshes.md)
