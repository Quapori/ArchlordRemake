# Archlord Character, Item & Object Meshes — Format & Organization

Reverse-engineered notes on how Archlord's 3D meshes (characters, items, objects) are structured internally, and — separately — how the game's data tables organize and let you discover *which* mesh file belongs to which character/item/object. Like the [extraction](extraction.md) and [animation](animation.md) pages, this describes **format and process only**, independent of any specific programming language or implementation. Builds on the [container basics from the animation page](animation.md#1-container-basics) (RenderWare chunk headers, `CLUMP`/`GEOMETRY_LIST`/`GEOMETRY`/`ATOMIC`); skeleton and skinning internals are covered there too and aren't repeated here.

## 1. One format, three roles

Characters, items and objects are **not different file formats** — all three are ordinary RenderWare `CLUMP` (`.dff`) files using exactly the geometry/material structures described below. What actually differs between them:

- **Whether the clump carries a skeleton.** Characters (and items worn on a character) are typically skinned (see [animation.md](animation.md)); static world objects and simple item pickups typically are not — just a plain mesh with a bind transform.
- **How the game's data tables reference and name the file** — covered in section 5.

## 2. Mesh geometry payload

A `GEOMETRY` chunk's struct payload holds everything about one mesh's vertices and raw triangles:

```
uint16  flags
uint8   tex_coord_sets
uint8   native_flags       # non-zero = platform/GPU-native layout, NOT the generic layout below
uint32  triangle_count
uint32  vertex_count
uint32  morph_target_count
-- then, back-to-back: --
[if PRELIT flag set]  uint8[4] × vertex_count      # per-vertex RGBA "prelit" color
for each UV set (tex_coord_sets, or inferred as 1/2 from the TEXTURED/TEXTURED2 flags if the count field is 0):
    float32[2] × vertex_count                       # UV pairs
for each triangle (triangle_count):
    uint16 × 4                                       # 3 vertex indices + 1 material index, see caveat below
for each morph target (morph_target_count):
    float32[4]   bounding sphere (center xyz, radius)
    uint32       has_vertices
    uint32       has_normals
    [if has_vertices]  float32[3] × vertex_count      # positions
    [if has_normals]   float32[3] × vertex_count      # normals
```

Two things about this layout are easy to get wrong:

- **Vertex positions and normals are not a separate top-level block — they live inside morph target 0.** A non-morphing mesh still has `morph_target_count == 1`; that single morph target's vertex/normal arrays *are* the base mesh data. Only read further morph targets (1..N) if you actually need blend-shape data.
- **The "prelit" flag isn't fully reliable, and the triangle record's field order isn't either.** Some files set the prelit-color flag without actually storing color data, and (independently) the position of the material index within each triangle's four `uint16` fields has been observed to vary — some files effectively use `(v0, v1, v2, material)`, others put the material index first or in another slot. Don't trust a single fixed assumption blindly; validate by checking which interpretation produces vertex indices `< vertex_count` and a material index `< material_count` for that geometry, and fall back to the other candidate layout if the first one produces out-of-range values.

## 3. Materials & textures

A `GEOMETRY` references a sibling `MATERIAL_LIST`, whose struct payload is:

```
uint32   material_count
int32[material_count]   material_indices   # index into a shared material pool; a real per-geometry
                                            # MATERIAL child chunk normally follows for each entry
```

Each `MATERIAL` chunk's struct payload:

```
uint32   flags
uint8[4] color            # RGBA
int32    unused
int32    textured          # non-zero => a child TEXTURE chunk follows, naming the texture to sample
-- at a fixed later offset: --
float32  ambient
float32  specular
float32  diffuse
```

The texture itself is referenced by name (a string chunk inside the `TEXTURE` child) — resolving that name to an actual image file is a separate step covered by texture-format documentation, not this page.

## 4. Render-ready triangle batches (material-split index buffers)

The raw triangle list in section 2 has an inline material index per triangle, which isn't directly usable for rendering (GPUs draw contiguous batches per material, not intermixed triangles). A `BIN_MESH_PLUGIN` extension on the `GEOMETRY` provides that pre-split, ready-to-draw form:

```
uint32   flags        # low byte = primitive type (0=tri_list, 1=tri_strip, 2=tri_fan, 4=line_list, 8=polyline, 0x10=point_list); bit 0x0100 = unindexed
uint32   mesh_count    # one entry per material actually used
uint32   total_indices
for each mesh (mesh_count):
    uint32   index_count
    uint32   material_index
    uint32[index_count]   indices    # into the same vertex arrays as section 2; interpreted as a
                                       # triangle list or triangle strip depending on the primitive type above
```

When both are present, prefer `BIN_MESH_PLUGIN` over reconstructing batches yourself from the raw triangle list — it's the actual data the original renderer draws from, already split and ordered per material.

## 5. Skinning (pointer)

If a `GEOMETRY` has a `SKIN_PLUGIN` extension, the mesh is bound to a skeleton (per-vertex bone indices/weights plus inverse bind matrices). That structure, and how it lines up with a skeleton's joint order and with animation files, is documented in full in [animation.md](animation.md#3-mesh--skeleton-binding-skinning). A `GEOMETRY` without a `SKIN_PLUGIN` is just static geometry, placed by its owning `ATOMIC`'s frame transform.

## 6. How characters/items/objects are found and named

None of this lives in the `.dff` files themselves — it's entirely driven by external configuration tables (INI files shipped with the client), using one shared file-naming convention:

```
<prefix><7-hex-digit-id>.dff
```

a single lowercase letter, an 7-digit hexadecimal numeric ID, and the extension. That numeric ID is a distinct "resource ID" stored in an INI field — not necessarily the same as the character/item/object's own template ID (TID).

**Characters** — resolved directly from a character-template INI, keyed by TID. Relevant fields and their prefix:

| Field | Prefix | Meaning |
|---|---|---|
| `DFF` | `a` | Main body mesh |
| `DEFAULT_ARMOUR_DFF` | `b` | Default armour mesh |
| `PICK_DFF` | `c` | Click/pickup target mesh for the character itself |

Face and hair customization meshes use a different, deterministic scheme instead of an INI-stored ID — prefix `v`, with the numeric ID computed from the character's TID:

```
face_id = TID × 0x200 + local_index
hair_id = TID × 0x100 + local_index
```

**Items** — resolved via a two-step lookup: an item-entry INI maps an item TID to a *template file name*, and that separate template file then holds the actual mesh fields, keyed again by TID:

| Field | Prefix | Meaning |
|---|---|---|
| `BASE_DFF` | `d` | Equip mesh worn on the character |
| `SECOND_DFF` | `e` | Secondary equip variant |
| `FIELD_DFF` | `f` | Display mesh when the item lies on the ground |
| `PICK_DFF` | `g` | Click/pickup target mesh for the item |

**Objects** (world props, static or simple animated fixtures) — resolved directly from an object-template INI, keyed by TID:

| Field | Prefix | Meaning |
|---|---|---|
| `DFF` | `h` | Main object mesh |
| (collision) | `i` | Collision-only mesh, separate from the visual mesh |
| `ANIMATION` | — | Optional; some objects (doors, machinery, …) reference an animation file the same way characters do |

Animation files referenced from any of these tables follow the naming rule already covered in [animation.md](animation.md#5-how-it-all-connects): take the value after the last `:` in the INI entry and append `.ean` if it has no extension yet.

## 7. Practical end-to-end process

1. Decide which category you're after (character / item / object) and load the corresponding template INI(s); for items, resolve the entry INI → template file indirection first.
2. Look up the TID's section, read the relevant `*_DFF` field(s), and turn each numeric ID into a filename via `<prefix><id:07x>.dff`.
3. Locate that filename on disk (in the already-extracted/decrypted client tree) and parse its `CLUMP` chunk tree.
4. Read `GEOMETRY` (positions/normals from morph target 0, UVs, `MATERIAL_LIST`) and prefer `BIN_MESH_PLUGIN` for material-split render batches (sections 2–4).
5. If a `SKIN_PLUGIN` is present, resolve the skeleton and (optionally) a matching animation as described in [animation.md](animation.md).
6. For characters, also resolve `DEFAULT_FACE`/`DEFAULT_HAIR` entries into `v`-prefixed customization meshes using the TID-based formula in section 6.

Deutsche Version: [meshes.de.md](meshes.de.md)
