# Archlord Client Data — Extraction & Decryption Format

Reverse-engineered notes on how Archlord's client data is packed and encrypted, and what's necessary to unlock it. This describes the **format and process only** — it is independent of any specific programming language or implementation. This page covers **extraction and decryption only**; interpreting individual unpacked formats (models, textures, terrain, etc.) is a separate topic.

## 1. Three kinds of packed data

An Archlord client installation contains three categories of files that need to be unlocked, each with a different mechanism:

1. **Loose files** sitting directly in the client directory tree — configuration/text data (`.ini`, `.txt`, `.xml`) plus already-plain assets (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`).
2. **DAT archives** — pairs of a `data.dat` (raw payload blob) and a `reference.dat` (encrypted file table) that bundle many files together.
3. **MagPack archives** (`.ma1`/`.ma2`, used for world/terrain data) — a separate, compressed (not RC4-encrypted) container format, see section 5.

Alternate-quality asset variants tend to live in sibling folders named `low` / `medium` and can generally be skipped if you only care about the primary assets.

## 2. Encryption scheme (loose files & DAT archives)

Everything RC4-encrypted uses the same primitive: **RC4**, keyed with the **full MD5 hash of a fixed password** (16 bytes, used directly as the RC4 key). RC4 is symmetric, so the same operation both encrypts and decrypts:

```
key   = MD5(password)        # 16-byte digest, used whole as the RC4 key
plain = RC4(key, encrypted_bytes)
```

Two passwords have been identified, used in different contexts:

| Password | Used for |
|---|---|
| `"1111"` | Loose `.ini`/`.txt`/`.xml` files, the file table inside every DAT archive, and `.ini`/`.txt`/`.xml` entries packed inside a DAT archive |
| `"asdfqwer"` | `.tx1` entries — both loose and packed inside a DAT archive |

There is no per-file salt or nonce — the same password/key is reused for every file of a given kind, which is what makes bulk decryption possible at all. This scheme does **not** apply to MagPack archives (section 5), which use a different, non-RC4 mechanism.

## 3. Loose files

Not every loose file is actually encrypted, even when its extension suggests it should be — some `.ini`/`.txt`/`.xml` files are stored as plain text already. Rather than relying on a fixed list of filenames (which is brittle and likely incomplete), the reliable approach is a **content check after attempting decryption**:

1. Skip archive files themselves (`data.dat`, `reference.dat`) and anything that's clearly not game data (executables, DLLs, system files).
2. For files with a "relevant" extension, only `.ini` / `.txt` / `.xml` / `.tx1` are candidates for decryption; other relevant extensions (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`) are already stored as plain data and just need to be picked up as-is.
3. Run the RC4 decryption for candidates. Then sanity-check the result: does it look like plausible plaintext (starts with a typical marker like `[` for an INI section, `<` for XML, a comment character, or a byte-order-mark; or simply has a low ratio of non-printable bytes in the first chunk)? If yes, keep the decrypted output. If the "decrypted" result still looks like noise, the file was actually already plaintext (or decrypting it with this key was wrong) — fall back to the original raw bytes instead of writing garbage.

This heuristic-based approach is more robust than hardcoding which specific filenames are pre-plaintext, since it self-corrects instead of silently corrupting files that don't match an assumed list.

## 4. DAT archives

For every `data.dat` that has a sibling `reference.dat` next to it:

1. Read `reference.dat` fully and RC4-decrypt it with the password `"1111"`.
2. Parse the decrypted bytes as a little-endian binary table:
   - `uint32` — number of files
   - `uint32` — length of a folder name, followed by that many bytes (the name of the subfolder everything in this archive should be extracted into)
   - then, repeated once per file: `uint32` name length + name bytes, `uint32` offset, `uint32` size — pointing into `data.dat`
3. For each entry, read `size` bytes out of `data.dat` starting at `offset`.
4. Decrypt that chunk if its extension calls for it, using the same extension → password mapping as loose files (`.ini`/`.txt`/`.xml` → `"1111"`, `.tx1` → `"asdfqwer"`). Every other extension is written out exactly as stored (not encrypted at the archive level either).
5. Two extensions get **renamed** on output, without any decryption — this looks like a historical/tooling quirk rather than actual encryption: `.bm1` → `.bmp`, `.pk` → `.wav`.

## 5. MagPack archives (`.ma1` / `.ma2`)

World/terrain data is packed in a completely separate container format, identified by the magic string `"MagPack Ver 0.1a"` at the start of the file. It does **not** use RC4 — instead it combines a simple XOR obfuscation with real compression:

1. **Header** — 50 bytes total, starting with the `"MagPack Ver 0.1a"` magic.
2. **Directory** — immediately follows the header, one variable-length entry per packed file, terminated by a zero-length entry:
   - `uint8` — name length; a value of `0` marks the end of the directory
   - name bytes (ASCII, that many bytes long)
   - `uint32` (little-endian) — packed size of this entry's data, **XOR-obfuscated with the mask `0x6969`**
3. **Data blobs** — follow the directory, one per directory entry, in the same order, back-to-back:
   - first `uint32` of the blob — unpacked (decompressed) size, again XOR-obfuscated with `0x6969`
   - the rest of the blob (`packed_size` bytes, including that leading size field) is a raw **aPLib**-compressed stream (aPLib is a general-purpose compression library historically used for size-constrained/obfuscated packing; it is not something you'd reimplement from scratch — use an existing aPLib decompressor)
   - immediately after each blob, a `uint32` **parity/checksum** value follows — its exact validation algorithm hasn't been confirmed, but it doesn't need to be checked to successfully unpack the data

In short: `directory entry → locate the blob → aPLib-decompress it → done`. No password/key is involved at all for this format, only the fixed XOR mask.

## 6. Practical process

A complete extraction needs to cover all three mechanisms — they are logically separate and files are distributed across all of them, so implementing only one (e.g. just the DAT archives) will silently leave data behind:

1. Locate the client installation directory.
2. Walk it recursively to find: loose files, `reference.dat`/`data.dat` pairs, and `.ma1`/`.ma2` files (skip `low`/`medium` variant folders if not needed).
3. For loose files: attempt decryption per extension and verify with the content-check from section 3.
4. For each DAT archive pair: decrypt the reference table, parse it, then extract and selectively decrypt each entry as described in section 4.
5. For each MagPack file: parse the directory, aPLib-decompress each entry as described in section 5.

A reference implementation of this whole process exists in the project's tooling (see [../tools/](../tools/README.md)).

Deutsche Version: [extraction.de.md](extraction.de.md)
