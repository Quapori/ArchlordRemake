# Archlord Terrain & World Data — Format & Organization

Reverse-engineered notes on how Archlord organizes its open world: the block/sector coordinate system, the terrain surface mesh itself, terrain-specific texture blending, and the sidecar data (object culling, grass, water) attached to each sector. Like the other asset pages, this describes **format and process only**, independent of any specific programming language or implementation. Builds on [extraction.md](extraction.md) (MagPack archives) and [meshes.md](meshes.md) (`GEOMETRY`/`MATERIAL`/`BIN_MESH_PLUGIN`) — both are reused here rather than repeated.

## 1. World coordinate system

The world is divided into a grid of **blocks**, each block a 16×16 grid of **sectors**. A sector is a fixed 6400-unit square. World-space coordinates are derived from a sector's grid position via:

```
world_x = (sector_x - 400) * 6400
world_z = (sector_z - 400) * 6400
```

(400 is the sector index that maps to world origin 0,0.) The populated world grid spans a specific range of block coordinates (observed: roughly 17–32 on each axis) — most of the theoretical grid is simply empty/unused.

Two different textual encodings for "which block" show up depending on which data you're looking at (terrain mesh archives vs. sidecar `.dat` files, section 4) — both ultimately resolve to the same `(block_x, block_z)` pair, just formatted differently (e.g. a 4-digit decimal like `1717` vs. a 6-digit-plus-suffix form like `0017017x`). Don't assume one universal block-ID string format across the whole asset set.

## 2. Terrain surface mesh

Each block's terrain surface is shipped as two **MagPack archives** (see [extraction.md § MagPack archives](extraction.md#5-magpack-archives-ma1--ma2) for the container format itself):

- `a<block-id>.ma2` — "rough" / low-detail variant
- `b<block-id>.ma2` — "detail" variant, the actual full-resolution terrain mesh

Inside each archive, every entry is one sector's terrain, named `D<x>,<z>.dff` (detail) or `R<x>,<z>.dff` (rough) — `x`,`z` being absolute (signed) sector grid coordinates, comma-separated.

Once MagPack-decompressed, an entry is a **"DWSector" stream**: almost always just a bare RenderWare `ATOMIC` + `GEOMETRY` (occasionally preceded by a `TEXTURE_DICTIONARY` chunk holding embedded textures — section 3 — and/or a small 4-byte marker before the `ATOMIC` header). Strip any such wrapper and what remains is parsed exactly like a regular mesh — same `GEOMETRY` vertex/triangle layout, same `MATERIAL_LIST`/`MATERIAL`, same `BIN_MESH_PLUGIN` render batches described in [meshes.md](meshes.md).

Vertex positions inside a sector's geometry are stored **sector-local** (relative to that sector's own origin). To place a sector correctly in the world: parse the `D`/`R` filename for `(sector_x, sector_z)`, compute the world origin with the formula in section 1, and translate the whole mesh by that offset (equivalently: give the containing node that translation and keep the mesh data untouched).

## 3. Terrain-specific materials & textures

Terrain uses the same `MATERIAL` structure as any other mesh, but with two additions specific to ground rendering:

**Multi-texture blending.** A terrain `MATERIAL` can carry an Archlord-proprietary extension chunk (distinct ID space from standard RenderWare plugins) with up to 5 fixed-role texture slots:

| Slot | Role |
|---|---|
| 0 | `alpha0` — blend mask for `color0` |
| 1 | `color0` — first ground texture |
| 2 | `alpha1` — blend mask for `color1` |
| 3 | `color1` — second ground texture |
| 4 | `extra1` — an additional overlay texture (exact use varies) |

This is how one terrain patch blends two (or more) ground textures smoothly — plain "one texture per material" rendering, as used for characters/items/objects, doesn't apply here. Each present slot references a normal `TEXTURE` sub-chunk (name string) just like a regular material's texture link.

**Embedded native textures.** Rather than always referencing an external texture file by name, a terrain texture dictionary can embed a **pre-compressed, GPU-native texture directly**: a chunk holding a small header (texture name, a literal `"DXT1"` marker, width/height, compressed data size) followed by raw **DXT1 block-compressed** pixel data. DXT1 encodes each 4×4 pixel block as:

- two RGB565 reference colors
- a derived 4-color (or 3-color-plus-transparent, depending on color ordering) interpolated palette
- 16 × 2-bit palette indices (one per texel), packed into a 32-bit value

Decoding it is a straightforward per-block palette lookup; no external texture file is needed once you've located this embedded data. This embedded-native path exists alongside (not instead of) the regular external-texture-file convention used elsewhere in the client.

## 4. Sidecar per-sector world data

Beyond the terrain surface mesh itself, three more per-sector data sets exist as plain (not MagPack-packed) `.dat` files, one file per **block**, organized under `world/<kind>/<prefix><block-id>.dat`:

| Kind | Folder | Prefix |
|---|---|---|
| Octree (culling) | `world/octree/` | `ot` |
| Grass (scatter decoration) | `world/grass/` | `gr` |
| Water | `world/water/` | `wt` |

All three share the same outer structure: an optional `uint32` version field, followed by a fixed 16×16 grid (one slot per sector in the block) of `(offset, size)` `int32` pairs pointing into the rest of the file — i.e. an index table addressing per-sector payload blocks that follow. What's inside each sector's payload differs per kind:

**Octree** — a recursive spatial partitioning tree used for object culling. Per sector: a count of root nodes, then per root a `center_y` float followed by a tree of nodes, each:

```
uint32   node_id
uint32   object_count
uint32   has_child        # non-zero => 8 child nodes follow, recursively
float32  bounding_sphere_radius
float32[3]  bounding_sphere_center
uint32   half_size
uint32   level
```

**Grass** — scattered decoration instances (grass patches etc.), grouped by small octree-like clusters. Per sector: a group count, then per group a bounding sphere + an octree cross-reference + a list of instances, each:

```
uint32     grass_template_id     # looked up in a grass-template table (texture/shape/animation info)
float32[3] position
float32[2] rotation
float32    scale
```

**Water** — flat water tiles plus animated "wave" regions. Per sector: a water-tile count, then per tile a status ID (into a water-status/texture table), a grid offset/size (tile position and extent in fixed-size steps), and a height; followed by a wave count and per-wave records (status ID, offset, width/height, spawn count, rotation, translation speed, and a precise 3D origin).

## 5. Pre-rendered minimap tiles (separate, simpler system)

Independently of everything above, the client also ships **pre-rendered raster image tiles** for the in-game world map UI — not reconstructed from the terrain mesh, just static images. One tile set per block, named `map<block_x><block_z><part>.<ext>`, where `part` is one of four letters (`a`/`b`/`c`/`d`) forming a 2×2 grid that assembles into one larger per-block tile. Stitching all blocks' assembled tiles together in grid order reconstructs a full world overview image.

## 6. Practical end-to-end process

1. Determine the block(s) you need and locate their two terrain archives (`a`/`b` prefix) plus the three sidecar `.dat` files (`ot`/`gr`/`wt` prefix) under `world/`.
2. Unpack the MagPack terrain archives (per [extraction.md](extraction.md#5-magpack-archives-ma1--ma2)); for each `D`/`R` entry, strip the DWSector wrapper and parse the remaining `ATOMIC`+`GEOMETRY` stream as a regular mesh ([meshes.md](meshes.md)).
3. Translate each sector's mesh into world space using the filename's `(sector_x, sector_z)` and the formula in section 1.
4. Resolve terrain materials: check for the 5-slot multi-texture extension (section 3) before falling back to a single-texture assumption; check texture dictionaries for embedded native DXT1 data before assuming an external texture file reference.
5. Parse the offset/size table in each sidecar `.dat` file, then decode each populated sector's octree/grass/water payload as needed (section 4).
6. Optionally, stitch the pre-rendered minimap tiles (section 5) for a quick world overview without touching any of the above.

Deutsche Version: [terrain.de.md](terrain.de.md)
