# Alefclient Datenentschluesselung - Fortschritt

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Daten, Auslese und Werkzeuge](Index.md)*

Stand: 2026-09-05

## Kurzstatus

Die erste Stufe der Datenentschluesselung ist identifiziert und praktisch bestaetigt. Fuer Texture-Dictionary-/TX1-Daten ist zusaetzlich ein zweiter RC4-Key gefunden und praktisch bestaetigt.

- Der Client verwendet Windows CryptoAPI, nicht ein simples eigenes XOR.
- Der konstante Daten-Key liegt in `alefclient.exe` bei VA `0x008B77EC`.
- Der Key ist die ASCII-Zeichenfolge `1111`.
- Algorithmus fuer verschluesselte Configs und `Reference.Dat`:
  - Provider: `Microsoft Base Cryptographic Provider v1.0`
  - Provider Type: `PROV_RSA_FULL` (`1`)
  - Hash: `CALG_MD5` (`0x8003`)
  - Cipher: `CALG_RC4` (`0x6801`)
  - `CryptDeriveKey(..., flags=4, ...)`
  - `CryptDecrypt(..., Final=false, ...)`
- `ini\worldmap.ini` wurde damit erfolgreich entschluesselt.
- `ini\grasstemplate.ini` wurde damit erfolgreich entschluesselt.
- `ini\waterstatust1.ini` wurde damit erfolgreich entschluesselt.
- `world\octree\Reference.Dat` wurde damit erfolgreich entschluesselt und als Pack-Index gelesen.
- `world\water\Reference.Dat` wurde damit erfolgreich entschluesselt und als Pack-Index gelesen.
- `world\grass\Reference.Dat` wurde damit erfolgreich entschluesselt und als Pack-Index gelesen.
- `world\octree\Data.Dat` ist danach roh adressierbar: Offset/Laenge aus `Reference.Dat` reichen zum Extrahieren.
- Texture-Streams aus `texture\world` mit Endung `.tx1` werden mit dem zweiten Key `asdfqwer` entschluesselt.
- Ein wiederverwendbarer Decoder/Extractor liegt in `tools\decode_archlord_data.ps1`.
- Detailnotizen zu Welt-, Octree-, Wasser- und Graskonfigurationen liegen in `WORLD_OCTREE_WATER_GRASS_CONFIGS.md`.
- Detailnotizen zu Vertex- und Pixel-Shadern liegen in `VERTEX_PIXEL_SHADER_FINDINGS.md`.
- Detailnotizen zu World-Dateien, `ma1`/`ma2`, 3D-Sektordaten und Materials liegen in `WORLD_MA1_MA2_3D_MATERIALS.md`.

## Relevante Client-Funktionen

### CryptoAPI-Wrapper

`FUN_004f9f00`

- Initialisiert einen Crypto-Provider-Kontext.
- Ruft intern `FUN_004f9cf0`.
- `FUN_004f9cf0` setzt/oeffnet `Microsoft Base Cryptographic Provider v1.0` mit Provider-Typ `1`.

`FUN_004f9e40`

- Dekodierfunktion.
- Ablauf:
  - `CryptCreateHash(provider, 0x8003, ...)`
  - `CryptHashData(hash, key, strlen(key), 0)`
  - `CryptDeriveKey(provider, 0x6801, hash, 4, &keyHandle)`
  - `CryptDecrypt(keyHandle, 0, false, 0, buffer, &length)`
- Assembly-Calling-Convention ist wichtig:
  - `ecx` zeigt auf den lokalen Provider-Kontext.
  - Stack-Parameter sind `key`, `buffer`, `length`.
  - Die meisten Aufrufe pushen `0x008B77EC` als `key`.

`FUN_004f9d80`

- Gegenstueck zum Verschluesseln.
- Nutzt denselben Key-Ablauf, aber `CryptEncrypt`.
- Wird beim Schreiben/Packen von Index-/Textdaten benutzt.

`FUN_004f9f10`

- Gibt den Crypto-Provider-Kontext mit `CryptReleaseContext` frei.

### Texture-Dictionary-/TX1-Loader

`FUN_00665010`

- Wird fuer TXD-basierte Ressourcen aufgerufen, unter anderem:
  - `Character.txd`
  - `Item.txd`
- Liest entweder gepackte Daten ueber den Packing-Manager oder bereits vorhandene Memory-Daten.
- Oeffnet danach einen RenderWare-Memory-Stream via `FUN_004c9610(3, 1, &buffer)`.
- Bei Modus/Parameter `3` entschluesselt der Loader die gelesenen Bytes vor dem eigentlichen RenderWare-Parsing:

```text
00665D4F  push 8D4030h
00665D5D  call 004F9E40

006662C0  push 8D4030h
006662D1  call 004F9E40
```

- `0x008D4030` liegt in `.rdata`; der String dort ist:

```text
asdfqwer
```

- Danach werden die entschluesselten Bytes als RenderWare-Stream-Chunks gelesen:
  - Chunk `0x10`: Clump
  - Chunk `0x14`: Atomic
  - Chunk `0x2b`: UVAnim

`FUN_00662340`

- Sucht in einem RenderWare-Stream nach Texture-Dictionary-artigen Chunks.
- Relevante Chunk-IDs:
  - `0x16`: RenderWare Texture Dictionary, gelesen ueber `FUN_004ce5c0`
  - `0x23`: Native/Extension-Pfad, gelesen ueber `FUN_0086b290`

`FUN_004ce5c0`

- Liest ein RenderWare-Texture-Dictionary.
- Erwartet danach einzelne Texture-Chunks `0x15`.
- Akzeptierter Versionsbereich: grob `0x35000` bis `0x37002`.

## Key-Fundstelle

Aus `C:\Spiele\Archlord\alefclient.exe`:

- ImageBase: `0x00400000`
- VA: `0x008B77EC`
- RVA: `0x004B77EC`
- Section: `.rdata`
- File offset: `0x004B77EC`
- Bytes:

```text
31 31 31 31 00 00 00 00 ...
```

ASCII:

```text
1111
```

## Zweiter Key fuer TXD/TX1

### Bestaetigter Key

Aus `C:\Spiele\Archlord\alefclient.exe`:

- ImageBase: `0x00400000`
- VA: `0x008D4030`
- RVA: `0x004D4030`
- Section: `.rdata`
- File offset: `0x004D4030`
- Bytes:

```text
61 73 64 66 71 77 65 72 00 ...
```

ASCII:

```text
asdfqwer
```

Dieser Key wird im Resource-Loader `FUN_00665010` genau an den zwei Decrypt-Call-Sites benutzt, die in den TXD-/Texture-Dictionary-Ladepfaden liegen.

### Praktische Validierung

Probe:

```powershell
.\tools\decode_archlord_data.ps1 `
  -Mode decode `
  -Key 'asdfqwer' `
  -InputPath 'extract_texture_world_sample\a090100t.tx1' `
  -OutputPath 'decoded_a090100t_key_asdfqwer.bin'
```

Ergebnisanfang nach der Entschluesselung:

```text
16 00 00 00 2C 56 01 00 2D 00 02 1C ...
```

Als Little-Endian-RenderWare-Chunkheader:

```text
chunk id = 0x00000016
size     = 0x0001562C
version  = 0x1C02002D
```

Damit ist die entschluesselte Datei ein RenderWare Texture Dictionary.

Massentest gegen alle extrahierten `.tx1` aus `texture\world`:

```text
tx1_total=776
rw_chunk16_ok=776
bad=0
0x00000016/0x0000AB74/0x1C02002D => 1
0x00000016/0x0001562C/0x1C02002D => 752
0x00000016/0x00055630/0x1C02002D => 20
0x00000016/0x00155634/0x1C02002D => 3
```

### Falsche Spur: `<@!#_AeTlHhT_#!@>`

Direkt neben `1111` liegt bei VA `0x008B77F4` die Zeichenfolge:

```text
<@!#_AeTlHhT_#!@>
```

Diese Zeichenfolge ist nach aktuellem Stand kein TXD/TX1-Key:

- Im Disasm gibt es nur einen direkten `push 8B77F4h`.
- Dieser Aufruf liegt in `FUN_004ecc90`.
- `FUN_004ecc90` schreibt die Zeichenfolge als Datei-/Header-Marker, danach den 2-Byte-Wert `0x1234` und `\r\n`.
- Das anschliessende Verschluesseln dieser Index-/Textdaten benutzt wieder `1111`, nicht diese Header-Zeichenfolge.
- Ein Test mit derselben CryptoAPI-RC4-Methode gegen `.tx1` erzeugt damit keinen gueltigen RenderWare- oder DDS-Header.

## Verschluesselte Config-Dateien

Die losen Konfigurationsdateien im Spielverzeichnis sind nicht plaintext, z.B.:

- `C:\Spiele\Archlord\ini\worldmap.ini`
- `C:\Spiele\Archlord\ini\charactertemplatecustomize.ini`
- `C:\Spiele\Archlord\ini\waterstatust1.ini`
- `C:\Spiele\Archlord\ini\grasstemplate.ini`

Beispiel: `worldmap.ini` beginnt verschluesselt mit:

```text
E1 09 2F 0B 09 5E 79 08 1A B6 46 9A A0 51 28 25 ...
```

Nach CryptoAPI-Decode mit Key `1111`:

```ini
[1]
Comment=Chantra Continent
XStart=-409677
ZStart=-206464
XEnd=409741
ZEnd=204455
ItemID=-1
ParentGroupID=
GroupID=Chantra Continent
RegionTexture=wmap0001.png
RegionRoadTexture=
UIActiveAreaSX=46
UIActiveAreaSY=83
UIActiveAreaEX=777
UIActiveAreaEY=470
```

Lokale Testausgabe:

- `decoded_worldmap.ini.txt`
- `decoded_grasstemplate.ini.txt`
- `decoded_waterstatust1.ini.txt`

`grasstemplate.ini` beginnt nach Decode mit:

```ini
; maxID=125

[Textures]
TEXTURE_NAME=0:GRASS_HU_01.tif
TEXTURE_NAME=1:GRASS_HU_02.tif
TEXTURE_NAME=2:GRASS_HU_03.tif
```

Hinweis: Der erste Kommentar enthaelt koreanische/Codepage-Zeichen und wird in der Konsole nicht sauber dargestellt; der Inhalt selbst ist entschluesselt.

`waterstatust1.ini` beginnt nach Decode mit:

```ini
[WaterTextures]
NUM=3
FN=0:water_nomal_01.bmp
FN=1:water_nomal_02.bmp
FN=2:WATER_NOMAL_02.BMP
[WaveTextures]
NUM=4
FN=0:water_wave.tif
FN=1:water_oceangradient_01_.bmp
FN=2:WATER_WAVE.TIF
FN=3:WATER_OCEANGRADIENT_01.BMP
```

## Packformat `Data.Dat` / `Reference.Dat`

### Loader-Pfad

`FUN_004ef570`

- Sucht rekursiv nach `Reference.Dat`.
- Ruft `FUN_004eeee0(path\Reference.Dat, ...)`.

`FUN_004eeee0`

- Liest `Reference.Dat` komplett.
- Dekodiert den Buffer mit `FUN_004f9e40`.
- Interpretiert danach einen binaeren Index:
  - `int32 entryCount`
  - `int32 rootLen`
  - `rootLen` Bytes Root-String
  - pro Eintrag:
    - `int32 nameLen`
    - `nameLen` Bytes Dateiname
    - `int32 offset`
    - `int32 size`
- Speichert Root und Dateinamen lowercase in internen Maps.
- Trackt `max(offset + size)` als verwendete Groesse von `Data.Dat`.

`FUN_004ef220`

- Oeffnet eine virtuelle Datei.
- Sucht Root + Dateiname im dekodierten Index.
- Falls gefunden:
  - setzt Package-Pointer
  - setzt Entry-Pointer
  - `fseek(Data.Dat, offset, SEEK_SET)`
- Falls nicht gefunden:
  - faellt auf direkten Dateizugriff zurueck.

`FUN_004eead0`

- Gibt die virtuelle Dateigroesse zurueck.
- Im Packfall ist das `size` aus dem Index.

`FUN_004eebd0`

- Liest rohe Bytes aus `Data.Dat` via `fread`.
- Es passiert dabei keine weitere CryptoAPI-Entschluesselung auf dieser Stufe.

`FUN_004eec60`

- Seek innerhalb einer virtuellen Datei.
- Im Packfall: `fseek(packageDataDat, entryOffset + localOffset, SEEK_SET)`.

### Bestaetigtes Beispiel: `world\octree`

Dateien:

- `C:\Spiele\Archlord\world\octree\Reference.Dat`
- `C:\Spiele\Archlord\world\octree\Data.Dat`

`Reference.Dat` verschluesselt:

```text
16 38 72 06 0E 1D 16 65 00 BC 5A 82 F9 4E 2F 27 ...
```

Nach CryptoAPI-Decode:

- `entryCount = 172`
- `rootLen = 13`
- `root = world\octree`

Erste Eintraege:

| Index | Name | Offset | Size |
|---:|---|---:|---:|
| 0 | `ot1831.dat` | `0x09B75C7C` | `1133972` |
| 1 | `ot1928.dat` | `0x02031DF0` | `1338940` |
| 2 | `ot2020.dat` | `0x03F932AC` | `1034580` |
| 3 | `ot2024.dat` | `0x026CEA3C` | `1013756` |
| 4 | `ot2031.dat` | `0x02178C2C` | `1236644` |
| 5 | `ot2120.dat` | `0x05B0805C` | `1074268` |
| 6 | `ot2124.dat` | `0x06947860` | `1040260` |
| 7 | `ot2125.dat` | `0x03174368` | `1225788` |
| 8 | `ot2126.dat` | `0x03914820` | `1207068` |
| 9 | `ot2128.dat` | `0x08B4E05C` | `1283292` |

Lokale Testausgaben:

- `decoded_world_octree_Reference.Dat.bin`
- `extracted_ot1831.dat`

`extracted_ot1831.dat` beginnt mit einer weiteren binaeren Tabelle:

```text
01 00 00 00 04 08 00 00 2C 0C 00 00 30 14 00 00
8C 0F 00 00 BC 23 00 00 8C 0F 00 00 48 33 00 00
```

Interpretation bisher:

- `Data.Dat` ist die aeussere Containerstufe.
- Die extrahierten `ot*.dat`-Dateien enthalten noch eigene interne Chunk-/Sector-Tabellen.
- Diese interne Struktur ist die naechste RE-Aufgabe fuer Octree-Daten.

### Bestaetigtes Beispiel: `world\water`

Dateien:

- `C:\Spiele\Archlord\world\water\Reference.Dat`
- `C:\Spiele\Archlord\world\water\Data.Dat`

Nach CryptoAPI-Decode:

- `entryCount = 137`
- `root = world\water`

Erste Eintraege:

| Index | Name | Offset | Size |
|---:|---|---:|---:|
| 0 | `wt2024.dat` | `0x0025B834` | `24820` |
| 1 | `wt2125.dat` | `0x0030CE78` | `96844` |
| 2 | `wt2126.dat` | `0x00261928` | `17636` |
| 3 | `wt2627.dat` | `0x003248C4` | `78796` |
| 4 | `wt2727.dat` | `0x00121094` | `8116` |
| 5 | `wt3118.dat` | `0x00337C90` | `56796` |
| 6 | `wt1728.dat` | `0x002F6FE4` | `4196` |
| 7 | `wt2818.dat` | `0x002F8048` | `55900` |
| 8 | `wt2917.dat` | `0x00305AA4` | `4116` |
| 9 | `wt3031.dat` | `0x00306AB8` | `21372` |

Lokale Testausgabe:

- `decoded_world_water_Reference.Dat.bin`

### Bestaetigtes Beispiel: `world\grass`

Dateien:

- `C:\Spiele\Archlord\world\grass\Reference.Dat`
- `C:\Spiele\Archlord\world\grass\Data.Dat`

Nach CryptoAPI-Decode:

- `entryCount = 174`
- `root = world\grass`

Erste Eintraege:

| Index | Name | Offset | Size |
|---:|---|---:|---:|
| 0 | `gr1831.dat` | `0x0002AB74` | `467308` |
| 1 | `gr1928.dat` | `0x00448DF8` | `872272` |
| 2 | `gr2020.dat` | `0x007E66E0` | `219644` |
| 3 | `gr2024.dat` | `0x011B5350` | `4328072` |
| 4 | `gr2120.dat` | `0x011AFFB4` | `12176` |
| 5 | `gr2124.dat` | `0x019B0360` | `438160` |
| 6 | `gr2125.dat` | `0x040761F4` | `777064` |
| 7 | `gr2126.dat` | `0x0460E324` | `6393816` |
| 8 | `gr2128.dat` | `0x021FCDC4` | `866720` |
| 9 | `gr2129.dat` | `0x03829EF4` | `85268` |

Lokale Testausgabe:

- `decoded_world_grass_Reference.Dat.bin`

## Weitere Container- und Paketspuren

### `MagPack Ver 0.1a`

`FUN_0058b170` parst ein separates Format mit Header:

```text
MagPack Ver 0.1a
```

Formatbeobachtung:

- Headerlaenge: `0x32` Bytes.
- Danach eine Tabelle aus bis zu `0x100` Eintraegen.
- Pro Eintrag:
  - `uint8 nameLen`
  - `nameLen` Bytes Name
  - `uint32 encodedSize`
  - `size = encodedSize ^ 0x6969`
- Danach folgen die Payloads.
- Nach jedem Payload wird ein `uint32` gelesen, der `0` sein muss.
- Der Parser verlangt am Ende exakt `0x100` Eintraege, wenn Eintraege vorhanden sind.

Gefundene Kandidaten:

- `C:\Spiele\Archlord\texture\etc\af1.grp`
- `C:\Spiele\Archlord\texture\notpacked\af1.grp`

Hinweis: `texture\notpacked\af1.grp` beginnt im Hexdump sichtbar mit Font-/TrueType-aehnlichen Tags wie `DSIG`, `LTSH`, `OS/2`, `cmap`, nicht mit `MagPack Ver 0.1a`. Der MagPack-Pfad ist daher ein separates Format und nicht zwingend fuer alle `.grp` gueltig.

## Bekannte Datenpakete im Spielverzeichnis

Auswahl relevanter `Data.Dat` / `Reference.Dat` Paare:

- `C:\Spiele\Archlord\world\octree\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\world\water\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\world\grass\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\texture\world\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\texture\worldmap\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\character\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\character\defaulthead\face\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\character\defaulthead\hair\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\object\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\texture\character\Data.Dat` / `Reference.Dat`
- `C:\Spiele\Archlord\texture\object\Data.Dat` / `Reference.Dat`

## Direkte Befehlsnotizen

Wiederverwendbares lokales Werkzeug:

```powershell
tools\decode_archlord_data.ps1
```

Beispiele:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\decode_archlord_data.ps1 `
  -Mode decode `
  -InputPath 'C:\Spiele\Archlord\ini\worldmap.ini' `
  -OutputPath 'decoded_worldmap.ini.txt'

powershell -ExecutionPolicy Bypass -File .\tools\decode_archlord_data.ps1 `
  -Mode list-ref `
  -InputPath 'C:\Spiele\Archlord\world\octree\Reference.Dat'

powershell -ExecutionPolicy Bypass -File .\tools\decode_archlord_data.ps1 `
  -Mode extract-pack `
  -InputPath 'C:\Spiele\Archlord\world\octree\Reference.Dat' `
  -DataPath 'C:\Spiele\Archlord\world\octree\Data.Dat' `
  -OutputPath 'extract_world_octree'
```

Key aus EXE lesen:

```powershell
$path='C:\Spiele\Archlord\alefclient.exe'
$b=[IO.File]::ReadAllBytes($path)
# VA 0x008B77EC -> ImageBase 0x00400000 -> RVA 0x004B77EC -> fileOffset 0x004B77EC
[Text.Encoding]::ASCII.GetString($b[0x4B77EC..(0x4B77EC+15)])
```

Referenz-Index nach erfolgreicher Entschluesselung parsen:

```powershell
$b=[IO.File]::ReadAllBytes('decoded_world_octree_Reference.Dat.bin')
$pos=0
$count=[BitConverter]::ToInt32($b,$pos); $pos+=4
$rootLen=[BitConverter]::ToInt32($b,$pos); $pos+=4
$root=[Text.Encoding]::ASCII.GetString($b,$pos,$rootLen).TrimEnd([char]0); $pos+=$rootLen
```

## Naechste Schritte

1. Einen wiederverwendbaren Decoder/Extractor fuer alle `Reference.Dat` + `Data.Dat` Paare schreiben.
2. Alle relevanten Configs entschluesseln:
   - `worldmap.ini`
   - `charactertemplatecustomize.ini`
   - `waterstatust1.ini`
   - `hwaterstatus.ini`
   - `grasstemplate.ini`
   - `skyset.ini`
   - `natureeffect.ini`
3. `world\octree`, `world\water`, `world\grass` komplett indexieren und die virtuellen Dateinamen/Offsets dokumentieren.
4. Interne Struktur der extrahierten `ot*.dat`-Dateien analysieren.
5. Danach die bekannten Engine-Themen mit echten entschluesselten Daten verbinden:
   - Octree-Sektoren
   - Wasserkonfigurationen
   - Grass-/Nature-Daten
   - Weltkarte
   - Charakteranpassung
