# Extracting & Decrypting Archlord Client Data

How Archlord's client data is packed and decrypted, and how to unpack it using the Rust code in [Archlord-AIO](https://github.com/Quapori/Archlord-AIO). This page covers **extraction and decryption only** — conversion of individual formats (`.txd` → `.png`, `.dff` → `.gltf`, etc.) is covered by the other Archlord-AIO tools, not here.

All source references below point to `libs/shared_utils/src/*.rs` and `apps/extractor/src/main.rs` in Archlord-AIO.

## 1. Two kinds of packed data

An Archlord client installation contains two categories of files that need to be unlocked:

1. **Loose files** sitting directly in the client directory tree — `.ini`, `.txt`, `.xml`, plus already-plain assets like `.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`.
2. **Packed DAT archives** — pairs of `data.dat` (raw payload) + `reference.dat` (encrypted file table) that bundle many files together, plus `.ma1`/`.ma2` files.

`find_files()` (`file_utils.rs`) walks the client directory recursively to collect both kinds, skipping any subfolder named `low` or `medium` (alternate-quality asset variants).

## 2. Encryption scheme

Everything encrypted uses the same primitive: **RC4**, keyed with the **MD5 hash of a fixed password** (`decryption.rs`):

| Key | Password | Used for |
|---|---|---|
| `DecryptKey::Default` | `"1111"` | Loose `.ini`/`.txt`/`.xml` files, and every DAT archive's `reference.dat` table, and `.ini` entries packed inside a DAT archive |
| `DecryptKey::Texture` | `"asdfqwer"` | `.tx1` entries packed inside a DAT archive |

```rust
let key_hash = Md5::digest(password_bytes);
let mut cipher: Rc4<U16> = Rc4::new_from_slice(&key_hash).unwrap();
cipher.apply_keystream(buffer); // decrypts in place
```

There is no per-file salt or nonce — the same password/key is reused for every file of a given kind.

## 3. Loose files

`process_regular_files()` (`file_utils.rs`) decides per file, based on its name, what to do (`should_skip_decryption()`):

| Rule | Files | Action |
|---|---|---|
| Ignore | `archlordgb.ini` | not copied at all |
| Copy only | `ggpoint.ini`, `coption.ini`, `autopickup.xml`, `loginsettings.txt`, and any `obj#####.ini` / `obs####.ini` (regex `^obj\d{5}\.ini$\|^obs\d{4}\.ini$`) | copied unmodified — these are already plaintext |
| Decrypt | everything else | RC4-decrypted **only if** the extension is `.ini`, `.txt` or `.xml` (`FileExtension::should_decrypt()`); other "relevant" extensions (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`) are copied as-is since they aren't encrypted to begin with |

## 4. DAT archives

`extract_from_dat()` (`extraction.rs`), driven by `process_dat_files()` (`dat_utils.rs`), only fires for a `data.dat` that has a sibling `reference.dat` next to it:

1. `reference.dat` is read fully into memory and RC4-decrypted with the **Default** key.
2. The decrypted table is parsed as little-endian binary: `u32` file count → `u32` folder-name length + folder name (the extraction subfolder) → then, repeated per file: `u32` name length + name, `u32` offset, `u32` size.
3. For each entry, `size` bytes are read out of `data.dat` at `offset`.
4. Only two extensions get decrypted at this stage: `.ini` (Default key) and `.tx1` (Texture key). Every other extension is written out exactly as stored.
5. Two extensions get renamed on output (not decrypted, just relabelled): `.bm1` → `.bmp`, `.pk` → `.wav`.
6. `.ma1`/`.ma2` files are picked up by `find_files()` but are **not** processed by this code path — there is currently no unpacking logic for them.

## 5. Running the extraction

1. Run `extractor` (or `core_main`) once — it auto-creates `config.ini` next to the binary and opens it in Notepad:
   ```ini
   [PATHS]
   SOURCE=D:\Archlord-EMU\Webzen\Archlord
   DESTINATION=D:\Archlord-EMU\Rust-Export-Test
   ```
   Fill in `SOURCE` (your client installation) and `DESTINATION`, save, press Enter to continue.
2. Run it again to perform the extraction:
   ```bash
   cargo run -p extractor --release
   ```

> **Note:** `extractor` only calls `process_dat_files()` — it unpacks and decrypts the `data.dat`/`reference.dat` pairs, but it does **not** call `process_regular_files()`, so loose `.ini`/`.txt`/`.xml` files sitting directly in the client tree are left untouched by this binary. Today, decrypting *both* loose files and DAT archives in one pass only happens as part of `core_main`'s full pipeline, which additionally launches unrelated conversion tools (`minimap`, `obj_checker`, `txd_converter`, `dff2gltf`) — out of scope for pure extraction/decryption.

Deutsche Version: [extraction.de.md](extraction.de.md)
