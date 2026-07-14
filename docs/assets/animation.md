# Archlord Character Animation — Format, Skeleton & Mesh Binding

Reverse-engineered notes on how Archlord's animation files are structured, how a character's skeleton is defined, how meshes bind to that skeleton, and how an animation file drives it — end to end. Like the [extraction page](extraction.md), this describes **format and process only**, independent of any specific programming language or implementation. Assumes you already have plain (decrypted/unpacked) files to work with.

## 1. Container basics

Model (`.dff`), animation (`.ean`) and several other Archlord asset types share the same underlying binary container: a **RenderWare binary stream**. Every chunk starts with a 12-byte header:

```
uint32  chunk_id
uint32  length          # size of the payload that follows, in bytes
uint32  version         # engine/build version tag, not needed for parsing structure
```

Some chunk IDs are "container" chunks: their payload is itself a sequence of child chunks (same header format, nested, until you've consumed `length` bytes). Others are "leaf" chunks whose payload is a fixed/typed binary struct. The container chunks relevant here are `CLUMP`, `FRAME_LIST`, `GEOMETRY_LIST`, `GEOMETRY`, `ATOMIC` and `EXTENSION` (a generic "attach optional plugin data" wrapper used throughout).

A `.dff` model file is one top-level `CLUMP` chunk. An `.ean` animation file is a single top-level `ANIM_ANIMATION` chunk with no wrapper at all — see section 4.

## 2. The skeleton

Inside a `CLUMP`, a `FRAME_LIST` chunk defines every bone (and non-bone helper frame) as a flat array. Each frame record is 56 bytes:

```
float32[3]  right     # 3x3 rotation matrix, column 1 ("right" axis)
float32[3]  up         # column 2
float32[3]  at         # column 3
float32[3]  position   # translation, relative to the parent frame
int32       parent_index   # index into this same frame array, -1 for the root
uint32      flags
```

This gives you the bone hierarchy (via `parent_index`) and each bone's local transform (rotation matrix + position) relative to its parent — this **is** the bind pose.

Frame records don't carry a stable "bone identity" by themselves — they're just positions in an array specific to this one file. Identity comes from an optional `EXTENSION` attached to individual frames, containing an `H_ANIM_PLUGIN` sub-chunk, which appears in two forms depending on payload size:

- **12 bytes — a per-bone tag**: `version` (uint32), `node_id` (uint32) — an author-assigned bone ID, meaningful across related files (e.g. a body mesh and its matching animation both refer to the same `node_id` for "left elbow") — and `flags` (uint32).
- **20 + 12×N bytes — the hierarchy declaration**, attached to one specific frame (typically the skeleton root): `version`, `hierarchy_id`, `node_count` (uint32, = N), `flags`, `keyframe_size`, followed by N entries of 12 bytes each: `node_id` (int32), `node_index` (int32), `flags` (int32, low 2 bits used as `push_parent`/`pop_parent` markers for an alternative stack-based hierarchy encoding).

This hierarchy declaration is the important one: **the order its N entries are listed in is the canonical "joint order"** used everywhere else (mesh skinning, animation tracks — see sections 3 and 5). Map each hierarchy entry's `node_id` back to the matching per-bone-tag frame to find which `FRAME_LIST` entry (and therefore which bind-pose transform and which `parent_index` chain) that joint actually is.

## 3. Mesh → skeleton binding (skinning)

Meshes live in `GEOMETRY` chunks (inside a `GEOMETRY_LIST`), referenced by an `ATOMIC` chunk that pairs one `frame_index` with one `geometry_index` (a `CLUMP` can contain several atomics — e.g. a body plus an attached weapon, or multiple LOD levels).

A skinned `GEOMETRY` carries a `SKIN_PLUGIN` extension with this payload layout:

```
uint8            bone_count            # number of bones actually used by this mesh
uint8            used_bone_count
uint8            max_weights_per_vertex
uint8            (padding)
uint8[used_bone_count]  used_bone_indices     # padded to a 4-byte boundary
uint8[vertex_count * max_weights]  bone_indices   # per-vertex, up to max_weights entries
float32[vertex_count * max_weights]  bone_weights # per-vertex, matching indices above
mat4x4[bone_count]  inverse_bind_matrices   # (some files use 3x4 matrices instead — 48 bytes/matrix — with an implicit [0 0 0 1] bottom row)
```

Each vertex has up to `max_weights` (bone index, weight) pairs; weights for a vertex should sum to 1.0. Both the per-vertex bone indices and the order of `inverse_bind_matrices` refer to bones **positionally, by the same joint order as the HAnim hierarchy** described in section 2 — not by `node_id`. A bone index of `2` means "the 3rd entry in the hierarchy's joint list," full stop; there's no separate ID lookup at this layer.

The inverse bind matrix is what lets you place a vertex correctly relative to a bone that has since moved: `finalVertexTransform = boneWorldMatrix × inverseBindMatrix`.

## 4. The animation file (`.ean`)

An `.ean` file is nothing but a single top-level `ANIM_ANIMATION` chunk — no clump, no frames, no skeleton data of its own. Its payload:

```
uint32   stream_version
uint32   type_id       # 1 = hierarchical (skeletal) keyframe animation
uint32   num_frames    # total keyframe record count across ALL tracks combined
uint32   flags
float32  duration_seconds
-- if type_id == 1, num_frames records of 36 bytes follow immediately: --
float32  time
float32[4]  rotation     # quaternion x,y,z,w
float32[3]  translation
uint32   previous_offset   # byte offset (from the start of the keyframe array) of the previous keyframe in this same track, or an unlinked/invalid value if this is a track's first keyframe
```

There is **no explicit track or bone index field**. All keyframes for every bone are interleaved in one flat array, and each keyframe instead points backward to the previous keyframe of its own track via `previous_offset` (which must be an exact multiple of 36 to be valid). To reconstruct per-bone tracks:

1. Walk the keyframe array in order.
2. For each keyframe, compute `previous_index = previous_offset / 36`.
3. If `previous_index` refers to an earlier keyframe you've already assigned to a track, this keyframe joins that same track.
4. Otherwise, this keyframe starts a **new** track (using its own array index as an ad-hoc track identifier).

The result is a set of tracks, each an ordered list of (time, rotation, translation) samples — i.e. a local-space bone transform curve, exactly analogous to what a `FRAME_LIST` entry's rotation+position describes statically for the bind pose.

## 5. How it all connects

Three things share one positional index space — the **joint order declared by the HAnim hierarchy** (section 2):

- Skin vertex bone indices (section 3) index into it directly.
- The order of `inverse_bind_matrices` in the `SKIN_PLUGIN` matches it.
- Reconstructed animation tracks (section 4) map to it **by position**: track 0 drives joint order position 0, track 1 drives position 1, and so on.

None of this is cross-checked by any ID inside the `.ean` file itself — an animation file is just an anonymous list of tracks. Applying it to the wrong skeleton (different bone count or authoring order) silently produces a broken/garbled result rather than an error, since there's nothing to validate against.

**Which animation file even belongs to which character?** That association isn't stored in the binary files at all — it comes from external configuration data (INI tables mapping a character/template ID to a set of animation type codes) combined with a fixed file-naming convention that turns an animation reference into an actual filename to load. In other words: pairing a model with its animations is a data-driven, external step, not something you can discover by inspecting the `.dff`/`.ean` files alone.

## 6. Coordinate system note

RenderWare uses a left-handed coordinate system. If your target format/engine is right-handed (a common convention for 3D interchange formats), flip the Z axis on every matrix you build from this data — bone bind-pose matrices, inverse bind matrices, and the rotation/translation you reconstruct per animation keyframe all need the same flip applied consistently, or skeleton and animation will visually mismatch even though each parses "correctly" on its own.

## 7. Practical end-to-end process

1. Parse the chunk tree of the `.dff` (12-byte headers, recursing into container chunks) down to: the `FRAME_LIST` (bind-pose transforms + parent links), the `EXTENSION`/`H_ANIM_PLUGIN` hierarchy declaration (canonical joint order + `node_id`s), and each `GEOMETRY`'s `SKIN_PLUGIN` (vertex bone indices/weights + inverse bind matrices).
2. Build the joint list in hierarchy order, resolve each joint's parent via its underlying frame's `parent_index`, and you have a full rig.
3. Attach mesh vertices to joints using the skin data — indices are already positional against the joint list from step 2.
4. Parse the matching `.ean` file's flat keyframe array and reconstruct per-track keyframe lists via the `previous_offset` chain (section 4).
5. Assign reconstructed tracks to joints by position (track *n* → joint *n*). Apply the Z-flip from section 6 consistently across bind pose, inverse bind matrices and animation keyframes.
6. To find the *right* `.ean` for a given character in the first place, resolve it through the external INI/character-template data described in section 5 rather than guessing from file contents.

Deutsche Version: [animation.de.md](animation.de.md)
