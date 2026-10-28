# AgcmFont (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmFont` (Schriftdarstellung: Glyphen-Textur, 2D-/Welt-Text, Clipping) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmFont/AgcmFont.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Schrift-Erzeugung, die vier Zeichenroutinen, die drei Zwischenschichten (`PrepareIMMode2D`, `RenderIMMode2DSCALE`, `RenderIMMode2DWORLD`) und die öffentlichen Zeichenfunktionen. Nicht zugeordnet sind `RenderMapTool`/`DrawTextMapTool` (Werkzeug), `SetJapaneseTable`, `SJIS_TO_UNICODE`, die `GetTextExtent…`/`GetCharacterWidth…`/`IsLeadByte…`-Familien (Region Kr/Cn/Jp/En), `GetHashKey`, `GetSequence…` und `GetMaxTexSize`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmFont.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `InitFuncPtr` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 1 | `OnAddModule` | `0x005EE710` | 28 | vtable/String |
| 2 | `OnDestroy` | `0x005EAD20` | 235 | vtable/String |
| 3 | `OnInit` | `0x005EFEF0` | 3113 | vtable/String |
| 4 | `OnIdle` | `0x005EAE10` | 143 | vtable/String |
| 5 | `PaintAlphabet` | `0x005EAEA0` | 659 | von Hand geprüft |
| 6 | `MakeFontRasterFromFTBits` | `0x005EB140` | 279 | von Hand geprüft |
| 7 | `MakeFontRasterFromBitMapBits` | `0x005EB260` | 286 | von Hand geprüft |
| 8 | `CreateShareTexture` | `0x005EB380` | 262 | von Hand geprüft |
| 9 | `DrawTextIMMode2DWorld` | `0x005EE730` | 874 | von Hand geprüft |
| 10 | `DrawTextIMMode2DWorldScale` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `DrawCaret` | `0x005EB490` | 230 | von Hand geprüft |
| 12 | `DrawCaretE` | `0x005EB580` | 228 | von Hand geprüft |
| 13 | `DrawTextIM2DEx` | `0x005EEAA0` | 1199 | von Hand geprüft |
| 14 | `DrawTextIM2D` | `0x005EEF50` | 1183 | von Hand geprüft |
| 15 | `DrawTextIM2DScale` | `0x005EF3F0` | 341 | von Hand geprüft |
| 16 | `DrawTextRectIM2D` | `0x005EF550` | 973 | von Hand geprüft |
| 17 | `DrawTextImgFont` | `0x005EB670` | 709 | von Hand geprüft |
| 18 | `FontDrawStart` | `0x005EB940` | 91 | von Hand geprüft |
| 19 | `FontDrawEnd` | `0x005EB9A0` | 236 | vtable/String |
| 20 | `SetClippingArea` | `0x005EBA90` | 65 | von Hand geprüft |
| 21 | `CharToWchar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `CreateFontRaster` | `0x005EBAE0` | 136 | von Hand geprüft |
| 23 | `RenderFont` | `0x005EBB70` | 482 | von Hand geprüft |
| 24 | `RenderFont_CLIP` | `0x005EBD60` | 1701 | von Hand geprüft |
| 25 | `RenderAsciiFont` | `0x005EC410` | 1816 | von Hand geprüft |
| 26 | `RenderAsciiFont_CLIP` | `0x005ECB30` | 2896 | von Hand geprüft |
| 27 | `PrepareIMMode2D` | `0x005ED770` | 614 | von Hand geprüft |
| 28 | `RenderIMMode2DSCALE` | `0x005ED9E0` | 704 | von Hand geprüft |
| 29 | `RenderIMMode2DWORLD` | `0x005EDCA0` | 2290 | von Hand geprüft |
| 30 | `OnCameraStateChange` | `0x005EE5A0` | 8 | vtable/String |
| 31 | `SetWorldCamera` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 32 | `GetHashKey` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 33 | `GetSequenceFont` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `GetSequenceImageFont` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 35 | `CameraStatusChange` | `0x005ED680` | 131 | vtable/String |
| 36 | `DrawTextMapTool` | – | | Werkzeugfunktion, im Binary nicht gefunden |
| 37 | `RenderMapTool` | – | | Werkzeugfunktion, im Binary nicht gefunden |
| 38 | `GetMaxTexSize` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 39 | `SetJapaneseTable` | – | | Regionscode (Japan), im Binary nicht gefunden |
| 40 | `SJIS_TO_UNICODE` | – | | Regionscode (Japan), im Binary nicht gefunden |
| 41 | `GetTextExtentKr` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 42 | `GetTextExtentCn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `GetTextExtentJp` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 44 | `GetTextExtentEn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 45 | `GetCharacterWidthKr` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 46 | `GetCharacterWidthCn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 47 | `GetCharacterWidthJp` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 48 | `GetCharacterWidthEn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 49 | `IsLeadByteKr` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 50 | `IsLeadByteEn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 51 | `IsLeadByteJp` | `0x005ED740` | 26 | von Hand geprüft |
| 52 | `IsLeadByteCn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

30 von 53 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_005efe40` (`0x005EFE40`), `~AgcmFont` (`0x005EFED0`), `ctor_or_dtor_005f1e80` (`0x005F1E80`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x3AD74` | `Merker „Clipping aktiv“; dahinter das Rechteck (`+0x3AD78…0x3AD84`)` | `SetClippingArea` |

## OnAddModule und Kamera

`OnAddModule` (`0x005EE710`, 28 Byte) holt die Kamera (`0x007025E0`) und ruft `CameraStatusChange` (`0x005ED680`, 131 Byte); `OnCameraStateChange` (`0x005EE5A0`, 8 Byte) ruft dieselbe Funktion. `OnInit` (`0x005EFEF0`, 3113 Byte) ist die Entsprechung der 426 Quellzeilen und enthält `InitFuncPtr` offenbar eingebaut.

## Schrift-Erzeugung

`PaintAlphabet` (`0x005EAEA0`, 659 Byte) und `MakeFontRasterFromBitMapBits` (`0x005EB260`) werden von `CreateShareTexture` (`0x005EB380`) gerufen; `CreateFontRaster` (`0x005EBAE0`) ruft `MakeFontRasterFromFTBits` (`0x005EB140`). Die beiden `MakeFontRasterFrom…`-Funktionen haben dieselbe Aufrufmenge und sind nur über diese Aufrufer getrennt.

## Zeichnen

`FontDrawStart` (`0x005EB940`) setzt die Puffer zurück und stellt Textur-Filter (nächster Nachbar) und Adressierung (Clamp) ein; `FontDrawEnd` (`0x005EB9A0`) war schon benannt; `SetClippingArea` (`0x005EBA90`) schreibt das Rechteck und den Merker (`this+0x3AD74`).
Die vier Zeichenroutinen liegen in Quellreihenfolge hintereinander: `RenderFont` (`0x005EBB70`, 482 Byte), `RenderFont_CLIP` (`0x005EBD60`, 1701 Byte), `RenderAsciiFont` (`0x005EC410`, 1816 Byte), `RenderAsciiFont_CLIP` (`0x005ECB30`, 2896 Byte). `PrepareIMMode2D` (`0x005ED770`) und `RenderIMMode2DSCALE` (`0x005ED9E0`) rufen alle vier sowie `FontDrawStart`/`FontDrawEnd`/`CreateFontRaster`; `RenderIMMode2DWORLD` (`0x005EDCA0`, 2290 Byte) ruft nur `FontDrawStart`/`FontDrawEnd`/`CreateFontRaster` (wie in der Quelle ohne die Render-Funktionen).
Die öffentlichen `DrawText…`-Funktionen: `DrawTextIMMode2DWorld` (`0x005EE730`, ruft `RenderIMMode2DWORLD`), `DrawTextIM2DScale` (`0x005EF3F0`, ruft `RenderIMMode2DSCALE`), `DrawTextIM2DEx`, `DrawTextIM2D` und `DrawTextRectIM2D` (`0x005EEAA0`, `0x005EEF50`, `0x005EF550`, rufen `PrepareIMMode2D`). `DrawCaret` (`0x005EB490`), `DrawCaretE` (`0x005EB580`) und `DrawTextImgFont` (`0x005EB670`) haben dieselbe Aufrufmenge (nur Zeichenprimitive).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung stützt sich auf die Aufrufbeziehungen (Prepare/Render-Familie), die Größenverhältnisse zu den Quellzeilen und die Quellreihenfolge; die Rümpfe wurden nicht Zeile für Zeile verglichen.
- Die Reihenfolge `DrawTextIM2DEx`, `DrawTextIM2D`, `DrawTextRectIM2D` bei `0x005EEAA0`, `0x005EEF50`, `0x005EF550` folgt nur der Adressreihenfolge; alle drei rufen `PrepareIMMode2D`.
- `DrawCaret`, `DrawCaretE` und `DrawTextImgFont` sind nur über ihre gemeinsame Aufrufmenge und die Größe zugeordnet; ihre Reihenfolge im Binary entspricht nicht der Quelle und ist unsicher.
- `IsLeadByteJp` (`0x005ED740`, Bereiche `0x81–0x9F`/`0xE0`) ist über die Shift-JIS-Bereiche zugeordnet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 9, nicht im Client: 7, ohne Kandidat: 7.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcConsole`](AgcConsole.md), [`AgcDebugWindow`](AgcDebugWindow.md), [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTuner`](AgcmTuner.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md)
