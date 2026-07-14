# Archlord-Charakteranimation — Format, Skelett & Mesh-Bindung

Reverse-engineerte Notizen dazu, wie Archlords Animationsdateien aufgebaut sind, wie das Skelett eines Charakters definiert wird, wie Meshes an dieses Skelett gebunden werden und wie eine Animationsdatei das Ganze steuert — von A bis Z. Wie die [Extraktions-Seite](extraction.md) beschreibt dies **nur Format und Prozess**, unabhängig von einer bestimmten Programmiersprache oder Implementierung. Setzt voraus, dass bereits entschlüsselte/entpackte Dateien vorliegen.

## 1. Grundlagen des Containers

Modell- (`.dff`), Animations- (`.ean`) und mehrere andere Archlord-Asset-Typen teilen sich denselben binären Container: einen **RenderWare-Binärstream**. Jeder Chunk beginnt mit einem 12-Byte-Header:

```
uint32  chunk_id
uint32  length          # Größe der nachfolgenden Payload in Bytes
uint32  version         # Engine-/Build-Versionskennung, für die Struktur nicht relevant
```

Manche Chunk-IDs sind "Container"-Chunks: ihre Payload ist selbst eine Folge von Kind-Chunks (gleiches Header-Format, verschachtelt, bis `length` Bytes aufgebraucht sind). Andere sind "Leaf"-Chunks, deren Payload ein fester/typisierter Binär-Struct ist. Die hier relevanten Container-Chunks sind `CLUMP`, `FRAME_LIST`, `GEOMETRY_LIST`, `GEOMETRY`, `ATOMIC` und `EXTENSION` (ein generischer Wrapper für "optionale Plugin-Daten anhängen", der durchgängig verwendet wird).

Eine `.dff`-Modelldatei ist ein einzelner Top-Level-`CLUMP`-Chunk. Eine `.ean`-Animationsdatei ist ein einzelner Top-Level-`ANIM_ANIMATION`-Chunk ganz ohne Wrapper — siehe Abschnitt 4.

## 2. Das Skelett

Innerhalb eines `CLUMP` definiert ein `FRAME_LIST`-Chunk jeden Knochen (und jeden Nicht-Knochen-Hilfs-Frame) als flaches Array. Jeder Frame-Record ist 56 Bytes groß:

```
float32[3]  right      # 3x3-Rotationsmatrix, Spalte 1 ("right"-Achse)
float32[3]  up          # Spalte 2
float32[3]  at          # Spalte 3
float32[3]  position    # Translation, relativ zum Parent-Frame
int32       parent_index    # Index in dasselbe Frame-Array, -1 für die Wurzel
uint32      flags
```

Das liefert die Knochenhierarchie (über `parent_index`) und die lokale Transformation jedes Knochens (Rotationsmatrix + Position) relativ zu seinem Parent — das **ist** die Bind-Pose.

Frame-Records tragen für sich genommen keine stabile "Knochen-Identität" — sie sind nur Positionen in einem Array, spezifisch für genau diese eine Datei. Identität kommt von einer optionalen `EXTENSION`, die an einzelne Frames angehängt ist und einen `H_ANIM_PLUGIN`-Sub-Chunk enthält, der je nach Payload-Größe in zwei Formen auftritt:

- **12 Bytes — ein Pro-Knochen-Tag**: `version` (uint32), `node_id` (uint32) — eine vom Autor vergebene Knochen-ID, die über zusammengehörige Dateien hinweg bedeutungsvoll ist (z.B. verweisen ein Körper-Mesh und die dazu passende Animation beide mit derselben `node_id` auf "linker Ellbogen") — sowie `flags` (uint32).
- **20 + 12×N Bytes — die Hierarchie-Deklaration**, angehängt an einen bestimmten Frame (typischerweise die Skelett-Wurzel): `version`, `hierarchy_id`, `node_count` (uint32, = N), `flags`, `keyframe_size`, gefolgt von N Einträgen à 12 Bytes: `node_id` (int32), `node_index` (int32), `flags` (int32, die unteren 2 Bits werden als `push_parent`/`pop_parent`-Marker für eine alternative Stack-basierte Hierarchie-Kodierung genutzt).

Diese Hierarchie-Deklaration ist die entscheidende: **die Reihenfolge ihrer N Einträge ist die kanonische "Joint-Reihenfolge"**, die überall sonst verwendet wird (Mesh-Skinning, Animations-Tracks — siehe Abschnitte 3 und 5). Um herauszufinden, welcher `FRAME_LIST`-Eintrag (und damit welche Bind-Pose-Transformation und welche `parent_index`-Kette) zu welchem Joint gehört, wird die `node_id` jedes Hierarchie-Eintrags mit dem passenden Pro-Knochen-Tag-Frame abgeglichen.

## 3. Mesh → Skelett-Bindung (Skinning)

Meshes liegen in `GEOMETRY`-Chunks (innerhalb einer `GEOMETRY_LIST`), referenziert über einen `ATOMIC`-Chunk, der einen `frame_index` mit einem `geometry_index` paart (ein `CLUMP` kann mehrere Atomics enthalten — z.B. Körper plus angehängte Waffe, oder mehrere LOD-Stufen).

Ein geskinntes `GEOMETRY` trägt eine `SKIN_PLUGIN`-Extension mit folgendem Payload-Layout:

```
uint8            bone_count             # Anzahl der von diesem Mesh tatsächlich genutzten Knochen
uint8            used_bone_count
uint8            max_weights_per_vertex
uint8            (Padding)
uint8[used_bone_count]  used_bone_indices     # auf 4-Byte-Grenze aufgefüllt
uint8[vertex_count * max_weights]  bone_indices   # pro Vertex, bis zu max_weights Einträge
float32[vertex_count * max_weights]  bone_weights # pro Vertex, passend zu obigen Indizes
mat4x4[bone_count]  inverse_bind_matrices   # (manche Dateien nutzen stattdessen 3x4-Matrizen — 48 Bytes/Matrix — mit impliziter [0 0 0 1]-Bodenzeile)
```

Jeder Vertex hat bis zu `max_weights` (Knochenindex, Gewicht)-Paare; die Gewichte eines Vertex sollten sich zu 1.0 aufsummieren. Sowohl die Pro-Vertex-Knochenindizes als auch die Reihenfolge der `inverse_bind_matrices` beziehen sich auf Knochen **positionell, in derselben Joint-Reihenfolge wie die HAnim-Hierarchie** aus Abschnitt 2 — nicht über `node_id`. Ein Knochenindex von `2` bedeutet "der 3. Eintrag in der Joint-Liste der Hierarchie", Punkt; auf dieser Ebene gibt es kein separates ID-Lookup.

Die Inverse-Bind-Matrix ist das, was einen Vertex korrekt relativ zu einem Knochen platziert, der sich inzwischen bewegt hat: `finaleVertexTransformation = KnochenWeltmatrix × InverseBindMatrix`.

## 4. Die Animationsdatei (`.ean`)

Eine `.ean`-Datei ist nichts weiter als ein einzelner Top-Level-`ANIM_ANIMATION`-Chunk — kein Clump, keine Frames, keine eigenen Skelettdaten. Ihre Payload:

```
uint32   stream_version
uint32   type_id        # 1 = hierarchische (skelettale) Keyframe-Animation
uint32   num_frames     # Gesamtzahl der Keyframe-Records über ALLE Tracks zusammen
uint32   flags
float32  duration_seconds
-- falls type_id == 1, folgen direkt num_frames Records à 36 Bytes: --
float32  time
float32[4]  rotation      # Quaternion x,y,z,w
float32[3]  translation
uint32   previous_offset    # Byte-Offset (ab Beginn des Keyframe-Arrays) des vorherigen Keyframes in diesem Track, oder ein ungültiger/unverknüpfter Wert, falls dies der erste Keyframe eines Tracks ist
```

Es gibt **kein explizites Track- oder Knochenindex-Feld**. Alle Keyframes aller Knochen liegen verschachtelt in einem flachen Array, und jeder Keyframe verweist stattdessen über `previous_offset` rückwärts auf den vorherigen Keyframe seines eigenen Tracks (muss ein exaktes Vielfaches von 36 sein, um gültig zu sein). Um Pro-Knochen-Tracks zu rekonstruieren:

1. Das Keyframe-Array der Reihe nach durchlaufen.
2. Für jeden Keyframe `previous_index = previous_offset / 36` berechnen.
3. Verweist `previous_index` auf einen früheren Keyframe, der bereits einem Track zugeordnet wurde, gehört dieser Keyframe zu demselben Track.
4. Andernfalls beginnt dieser Keyframe einen **neuen** Track (mit seinem eigenen Array-Index als Ad-hoc-Track-Kennung).

Das Ergebnis ist eine Menge von Tracks, jeder eine geordnete Liste von (Zeit, Rotation, Translation)-Samples — also eine lokale Knochen-Transformationskurve, genau analog zu dem, was ein `FRAME_LIST`-Eintrag mit Rotation+Position statisch für die Bind-Pose beschreibt.

## 5. Wie alles zusammenhängt

Drei Dinge teilen sich einen gemeinsamen positionellen Index-Raum — die **von der HAnim-Hierarchie deklarierte Joint-Reihenfolge** (Abschnitt 2):

- Skin-Vertex-Knochenindizes (Abschnitt 3) indizieren direkt hinein.
- Die Reihenfolge der `inverse_bind_matrices` im `SKIN_PLUGIN` entspricht ihr.
- Rekonstruierte Animations-Tracks (Abschnitt 4) werden **positionell** zugeordnet: Track 0 steuert Joint-Position 0, Track 1 steuert Position 1, und so weiter.

Nichts davon wird durch irgendeine ID innerhalb der `.ean`-Datei selbst gegengeprüft — eine Animationsdatei ist schlicht eine anonyme Liste von Tracks. Wendet man sie auf das falsche Skelett an (andere Knochenanzahl oder andere Autoren-Reihenfolge), entsteht stillschweigend ein kaputtes/verzerrtes Ergebnis statt eines Fehlers, da es nichts gibt, wogegen validiert werden könnte.

**Welche Animationsdatei überhaupt zu welchem Charakter gehört?** Diese Zuordnung steht nicht in den Binärdateien selbst — sie ergibt sich aus externen Konfigurationsdaten (INI-Tabellen, die eine Charakter-/Template-ID auf eine Menge von Animations-Typ-Codes abbilden) kombiniert mit einer festen Dateinamens-Konvention, die aus einer Animations-Referenz einen tatsächlichen zu ladenden Dateinamen macht. Mit anderen Worten: Ein Modell mit seinen Animationen zu paaren ist ein datengetriebener, externer Schritt — nicht etwas, das sich allein durch Inspektion der `.dff`-/`.ean`-Dateien erschließen lässt.

## 6. Hinweis zum Koordinatensystem

RenderWare nutzt ein linkshändiges Koordinatensystem. Ist das Zielformat/die Ziel-Engine rechtshändig (eine übliche Konvention bei 3D-Austauschformaten), muss die Z-Achse bei jeder aus diesen Daten gebauten Matrix gespiegelt werden — Knochen-Bind-Pose-Matrizen, Inverse-Bind-Matrizen und die pro Animations-Keyframe rekonstruierte Rotation/Translation brauchen alle konsistent dieselbe Spiegelung, sonst passen Skelett und Animation optisch nicht zusammen, obwohl beide für sich "korrekt" geparst wurden.

## 7. Praktischer Ablauf von A bis Z

1. Den Chunk-Baum der `.dff` parsen (12-Byte-Header, rekursiv in Container-Chunks absteigen) bis zu: der `FRAME_LIST` (Bind-Pose-Transformationen + Parent-Verknüpfungen), der `EXTENSION`/`H_ANIM_PLUGIN`-Hierarchie-Deklaration (kanonische Joint-Reihenfolge + `node_id`s), sowie dem `SKIN_PLUGIN` jeder `GEOMETRY` (Vertex-Knochenindizes/-Gewichte + Inverse-Bind-Matrizen).
2. Die Joint-Liste in Hierarchie-Reihenfolge aufbauen, den Parent jedes Joints über den `parent_index` seines zugrundeliegenden Frames auflösen — fertig ist das Rig.
3. Mesh-Vertices anhand der Skin-Daten an Joints binden — die Indizes sind bereits positionell gegen die Joint-Liste aus Schritt 2 gültig.
4. Das flache Keyframe-Array der passenden `.ean`-Datei parsen und Pro-Track-Keyframe-Listen über die `previous_offset`-Kette rekonstruieren (Abschnitt 4).
5. Rekonstruierte Tracks positionell den Joints zuordnen (Track *n* → Joint *n*). Die Z-Spiegelung aus Abschnitt 6 konsistent auf Bind-Pose, Inverse-Bind-Matrizen und Animations-Keyframes anwenden.
6. Um die *richtige* `.ean` für einen gegebenen Charakter überhaupt erst zu finden: über die externen INI-/Charakter-Template-Daten aus Abschnitt 5 auflösen, statt anhand des Dateiinhalts zu raten.

English version: [animation.md](animation.md)
