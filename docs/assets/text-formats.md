# Archlord Client Text Files — INI, TXT & XML: Structure, Purpose and Relationships

Reverse-engineered notes on how the Archlord client's loose text configuration files (`.ini`, `.txt`, `.xml`) are internally structured, what each file family is for, and how they reference each other. Like the other asset pages, this describes **only format and structure**, independent of any particular programming language or implementation. Builds on [extraction.md](extraction.md) — that page covers *how* these files are decrypted/unpacked; this one covers only what's *inside* them once they're plaintext.

## 1. Three extensions, but not three formats

The file extension says almost nothing about the actual content — both `.ini` and `.txt` are used for several fundamentally different structures. Which format a given file uses can only be told from its content, not its name:

| Format | Example files | How to recognize it |
|---|---|---|
| Classic INI | `grasstemplate.ini`, `waterstatust1.ini`, `worldmap.ini`, `teleportpoint.ini`, `skyset.ini`, `ArchlordColor.ini`, `uidatalist.ini` | `[Section]` + `Key=Value`; the keys are already the real field names |
| Indexed ("template") INI | `charactertemplateclient.ini`, `charactertemplateanimation.ini`, `charactertemplatepublic.ini`, `charactertemplatecustomize.ini`, `charactertemplateeventeffect.ini`, `itemtemplateentry.ini`, `ini/ItemTemplate/*.ini`, `objecttemplate.ini`, `effect/ini/new/<id>_eff.ini` | A header block before the first `[Section]` maps position numbers to field names; every `[N]` section then holds `Position=Value` lines |
| TSV table (despite a `.txt` or even `.ini` extension) | `itemdatatable.txt`, `itemtooltip.txt`, `skill_*.txt`, `questtemplate.ini`, `questgroup.ini` | first non-blank line is a tab-separated header row, every following line a tab-separated data row |
| One-off special formats | `growupfactor.txt`, `XlsTxtInfo.Txt` | their own, file-specific block structure — see section 3 |
| XML | loose `.xml` files in the client tree | see section 4 — not yet structurally reverse-engineered |

Practical detection order: first rule out the handful of named special cases, then check the first non-blank line — if it contains a tab and does *not* look like `number=...`, it's a TSV table; otherwise the file is parsed with the INI grammar (section 2). Without that ordering, files like `questtemplate.ini` would be misread as INI when they're actually tables.

## 2. The INI grammar: one syntax, two usage patterns

Every file recognized as INI shares the same simple grammar:

- Blank lines, and lines starting with `;` or `#`, are ignored.
- `[Name]` opens a new section.
- `Key=Value` inside a section is a field of that section (whitespace around `Key` and `Value` is trimmed).

Two completely different usage patterns are built on top of this one grammar:

**a) Classic form.** The key *is* the field name already. `waterstatust1.ini`, for example, has sections like `[WaterTextures]`, `[WaveTextures]` and `[Setting]` with directly readable keys. One quirk: a single section can hold several logical records back-to-back, separated not by additional `[Section]` markers but by the repeated occurrence of an "ID-like" key (e.g. `GRASS_ID=` in `grasstemplate.ini`, `ID=` in `waterstatust1.ini`). Every re-occurrence of that key starts a new record within the same section — a compact way to pack a small table into a single section.

**b) Indexed ("template") form.** Before the first `[Section]`, a header block maps position numbers to field names. After that, every `[N]` section is one data row (usually named after a numeric TID), whose lines read `Position=Value` — the position has to be resolved through the header block first to know which field it is. Schematically:

```
; Header block — still outside any section, maps position -> field name
0=TID
1=Name
2=DFF
3=DEFAULT_ARMOUR_DFF

; Records — each [N] section is one "row"
[1042]
0=1042
1=SampleName
2=1234567
3=0

[1043]
0=1043
2=2345678
```

The benefit: thousands of near-identical rows stay compact (no repeated field names per row) while still being self-describing via the shared header block. If a record omits a position (like `1=` in `[1043]` above), that field is simply empty for that record.

Notably, a file with no header block before its first section is just the classic form — the position-to-field-name map is empty, so every key passes through unchanged as its own field name. It's the same grammar producing two different outcomes, not two separate parsers.

Two things hold true for both forms:

- **Duplicate keys are not overwritten.** If a field name (or, in the indexed form, a position) appears more than once within a record, all values are collected as an ordered list instead of silently replacing the previous one. This matters for things like repeated effect slots or multiple `FN` texture entries.
- **No declared encoding.** Files ship as `utf-8-sig`, `cp949` (Korean) or Latin-1 depending on the language build; with no BOM/declaration, the only reliable approach is a fallback chain across those encodings. And a file with an `.ini` extension can still be RC4-encrypted — the only way to tell is to attempt decryption and check plausibility of the result (see [extraction.md § Loose Files](extraction.md#3-loose-files)).

## 3. TXT: mostly tables, occasionally INI, rarely a special case

Most `.txt` files (`itemdatatable.txt`, `itemtooltip.txt`, `skill_const.txt`, `npcdialog.txt`, etc.) are plain TSV tables: first line = tab-separated column headers, every following line a record. The first column typically holds the record's TID/ID.

Some `.txt` files use the indexed-INI grammar from section 2b instead. `charactercustomizelist.txt` is the example: the header block maps positions to field names like `Type`, `Number`, `Sell Name`, `Case`, `CharacterTID`, `UseLevel`, `Price(Money)` and `Price(Skull)`; each `[N]` section is one purchasable character customization option that references back to a character template TID via `CharacterTID`.

Two files are genuine one-off cases with their own block structure:

- **`growupfactor.txt`** — repeating blocks: a line consisting of a single number starts a new block for that character TID; the next line starting with `LV` is that block's column header row; tab-separated rows follow with the per-level stat-growth values for that character TID — until the next lone-number marker opens the next block.
- **`XlsTxtInfo.Txt`** — a flat, comma-separated manifest (path, byte size, row count, column count per source table). It describes the *other* text files (which source spreadsheet each was exported from), not game data itself.

`questtemplate.ini` and `questgroup.ini` are the clearest proof that the extension can't be trusted: both are named `.ini` but are, content-wise, TSV tables as described in section 1.

## 4. XML — present, but not (yet) reverse-engineered

Loose `.xml` files sit in the client tree alongside `.ini`/`.txt` and go through the same decrypt-or-plaintext path as those (RC4 with the `"1111"` password, keeping the result only if it plausibly looks like text — leading `<`, BOM, etc. — see [extraction.md § Loose Files](extraction.md#3-loose-files)).

Unlike INI/TXT, **no internal XML structure** has been reverse-engineered for this project, nor has any existing tool parsed XML content structurally — every extraction and database step in the project treats XML purely as opaque pass-through text (decrypt/copy, never interpret). This section deliberately documents a known gap rather than inventing a format; once someone works out concrete `.xml` contents, that finding belongs here.

## 5. How the files reference each other

None of the files from sections 1–3 stand alone — most of the value on this layer comes from the links between files. A few recurring patterns:

**a) One record, many files — the character case.** `charactertemplatepublic.ini`, `charactertemplateclient.ini`, `charactertemplateanimation.ini`, `charactertemplatecustomize.ini`, `charactertemplateeventeffect.ini` (plus the skill variants) are independent indexed-INI files sharing the same `[TID]` section space. None is complete on its own — a character only exists as the join of all these files over the same TID. What individual fields (`DFF`, `ANIMATION_NAME0`, `DEFAULT_FACE…`) actually mean and how they resolve to filenames is covered in [meshes.md § 6](meshes.md) and [animation.md § 5](animation.md#5-how-it-all-connects).

**b) Two-level indirection — the item case.** `itemtemplateentry.ini` doesn't map an item TID to fields directly; it only maps to `TemplateName` and `TemplateFileName` — the latter a relative path to a second, also indexed, INI file under `ini/ItemTemplate/`, which holds the actual fields (again keyed by the same TID). Unlike the character case (pure TID matching across independently named files), here a field value itself points to the second file's filename.

**c) Template vs. placed instance — the object case.** `objecttemplate.ini` describes *what* an object is (mesh, collision, event effect) — once per object TID. Each world block additionally has its own `obj<blockid>.ini`, using the same block addressing as the world grid in [terrain.md § 1](terrain.md#1-world-coordinate-system); every row in it is a placed instance (position, scale, rotation, octree references) that points back to `objecttemplate.ini` via a `tid` field. Same split as the character case between "what it looks like" and "where" — except here "where" lives in a separate file per world block instead of a global field.

**d) A third table for "what happens when" — event effects.** The field `AGCMEVENTEFFECT_EFFECT_DATA` (shape: `slot:effect_id:offset_x:offset_y:offset_z:scale:parent_node_id:start_gap`) shows up independently inside `charactertemplateeventeffect.ini`, `objecttemplate.ini`, and every file under `ini/ItemTemplate/`. None of these files stores an effect asset filename directly — `effect_id` instead points into `effect/ini/new/<effect_id>_eff.ini`, itself another indexed-INI holding the actual effect assets. Three entirely unrelated "owner" categories (character, object, item) converge on one shared effect-definition namespace this way.

**e) TSV tables carry the foreign key as a column instead of a section.** Since TSV tables have no `[TID]` sections, the cross-reference shows up as an ordinary column instead (`Tid`, `TID`, `CharTID`, etc.). The per-block `CharTID` lines in `growupfactor.txt`, for instance, reference the same TID space as `charactertemplatepublic.ini` — just column-based instead of section-based.

**f) Common denominator: the numeric TID is the universal foreign key.** Regardless of which of the four formats from section 1 a file uses, the join key across almost the entire text-file layer is the same plain integer (or a colon-separated value embedding one). Nothing on this layer uses XML-style nested references or GUIDs — everything ultimately resolves through flat numeric IDs into either another `[section]` or another table row.

## 6. Practical workflow for classifying an unknown file

1. Determine the format from content, not the extension: first rule out the handful of named special cases (`growupfactor.txt`, `XlsTxtInfo.Txt`), then apply the tab-in-first-line heuristic from section 1.
2. If INI grammar is detected: check whether lines exist before the first `[Section]` — if so, that's the position-to-field-name header block (indexed form); if not, keys are already the field names (classic form).
3. Identify the file's ID scheme (section number for indexed INI, a named ID column for TSV) and follow it into whichever file/table actually "owns" that ID to assemble the full picture (section 5).
4. Treat duplicate keys within one record as a list of values, not as values overwriting each other.
5. Decode with a fallback chain (`utf-8-sig`, `cp949`, Latin-1), since no file declares its own encoding — and when in doubt, check whether the file is still RC4-encrypted despite a plaintext-looking extension ([extraction.md § 1](extraction.md#1-three-kinds-of-packed-data)).

A reference implementation of this entire process exists in the project's tooling (see [../tools/](../tools/README.md)).

Deutsche Version: [text-formats.de.md](text-formats.de.md)
