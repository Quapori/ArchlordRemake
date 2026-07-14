# Archlord Client Data — Extraction & Decryption Format

Reverse-engineered notes on how Archlord's client data is packed and encrypted, and what's necessary to unlock it. This describes the **format and process only** — it is independent of any specific programming language or implementation. This page covers **extraction and decryption only**; interpreting individual unpacked formats (models, textures, terrain, etc.) is a separate topic.

## 1. Two kinds of packed data

An Archlord client installation contains two categories of files that need to be unlocked:

1. **Loose files** sitting directly in the client directory tree — configuration/text data (`.ini`, `.txt`, `.xml`) plus already-plain assets (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`).
2. **Packed archives** — pairs of a `data.dat` (raw payload blob) and a `reference.dat` (encrypted file table) that bundle many files together. `.ma1`/`.ma2` files also exist alongside these but their internal format has not been reverse-engineered yet — no known way to unpack them so far.

When scanning a client installation for these files, alternate-quality asset variants tend to live in sibling folders named `low` / `medium` and can generally be skipped if you only care about the primary assets.

## 2. Encryption scheme

Everything encrypted uses the same primitive: **RC4**, keyed with the **MD5 hash of a fixed password**. RC4 is symmetric, so the same operation both encrypts and decrypts:

```
key   = MD5(password)
plain = RC4(key, encrypted_bytes)
```

Two passwords have been identified, used in different contexts:

| Password | Used for |
|---|---|
| `"1111"` | Loose `.ini`/`.txt`/`.xml` files, the file table inside every archive (see below), and `.ini` entries packed inside an archive |
| `"asdfqwer"` | `.tx1` entries packed inside an archive |

There is no per-file salt or nonce — the same password/key is reused for every file of a given kind, which is what makes bulk decryption possible at all.

## 3. Loose files

Not every loose file needs the same treatment; the rules appear to be based on the file name and extension:

| Rule | Files | Action |
|---|---|---|
| Ignore | one specific file (an `.ini` holding region/build info) | left alone entirely |
| Copy only | a handful of specific config files (e.g. login/UI settings), and any file matching the pattern of an object-template index (`obj#####.ini` / `obs####.ini`) | copied unmodified — these are already plaintext despite the extension |
| Decrypt | everything else with a "relevant" extension | only `.ini` / `.txt` / `.xml` are actually encrypted and need the RC4 step; other relevant extensions (`.wav`, `.dds`, `.bmp`, `.png`, `.jpg`, `.tif`, `.pk`, `.mp3`) are already stored as plain data and just need to be picked up as-is |

In short: encryption in the loose-file tree is limited to text/config data — binary assets are not encrypted, just distributed alongside the encrypted files.

## 4. Packed archives

For every `data.dat` that has a sibling `reference.dat` next to it:

1. Read `reference.dat` fully and RC4-decrypt it with the password `"1111"`.
2. Parse the decrypted bytes as a little-endian binary table:
   - `uint32` — number of files
   - `uint32` — length of a folder name, followed by that many bytes (the name of the subfolder everything in this archive should be extracted into)
   - then, repeated once per file: `uint32` name length + name bytes, `uint32` offset, `uint32` size — pointing into `data.dat`
3. For each entry, read `size` bytes out of `data.dat` starting at `offset`.
4. Decrypt that chunk only if its extension calls for it: `.ini` → RC4 with `"1111"`, `.tx1` → RC4 with `"asdfqwer"`. Every other extension is written out exactly as stored (not encrypted at the archive level either).
5. Two extensions get **renamed** on output, without any decryption — this looks like a historical/tooling quirk rather than actual encryption: `.bm1` → `.bmp`, `.pk` → `.wav`.

## 5. Practical process

1. Locate the client installation directory.
2. Walk it recursively, collecting both loose files and archive pairs (skip `low`/`medium` variant folders if not needed).
3. For loose files: apply the ignore/copy/decrypt rules from section 3.
4. For each `data.dat` + `reference.dat` pair: decrypt the reference table, parse it, then extract and selectively decrypt each entry as described in section 4.

> **Watch out for:** it's easy to build a tool that only implements one half of this (e.g. only unpacking the archives) and assume the client is fully extracted. Loose configuration files and archive-packed files are two separate code paths — make sure both are actually covered, or you'll end up with an incomplete/partial extraction that looks complete at a glance.

A reference implementation of this whole process exists in the project's tooling (see [../tools/](../tools/README.md)).

Deutsche Version: [extraction.de.md](extraction.de.md)
