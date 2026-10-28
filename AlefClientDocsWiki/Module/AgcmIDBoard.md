# AgcmIDBoard (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmIDBoard` (Namens-, Gilden-, Titel- und Symbolanzeige über Charakteren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph (Aufrufreihenfolge in `_Draw_Normal`), EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmIDBoard.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 18 von 24 Quellmethoden sind zugeordnet. Nicht im Binary sind die vier älteren Fassungen von `_DrawName`, `_DrawTitleName`, `_DrawNameEx` und `_DrawGuild` (Parameter `fPosX, fPosY`; die Quelle ruft nur die Fassungen mit `RwReal* pfPosY` auf) und die zwei Hilfen `_IsCheckDrawByPVP` und `_IsPlayerInBattleGround` (nur von den älteren Fassungen bzw. gar nicht aufgerufen).
- **Besonderheit:** Drei Funktionen sind in Ghidra in zwei Teile zerlegt (Prologstück und Rumpf): `_DrawGuildCompetition` (`0x00753A40` + `0x00753A4A`) und `_Draw_InGuildStadium` (`0x007549F0` + `0x007549FA`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmIDBoard.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Update` | `0x00753620` | 127 | vtable/String |
| 1 | `Render` | `0x007552A0` | 72 | vtable/String |
| 2 | `_DrawName` | – | | nicht im Binary: ältere Fassung (`fPosX, fPosY`), in der Quelle ohne Aufrufer |
| 3 | `_DrawName` | `0x007542D0` | 660 | von Hand geprüft |
| 4 | `_DrawTitleName` | – | | nicht im Binary: ältere Fassung (`fPosX, fPosY`), in der Quelle ohne Aufrufer |
| 5 | `_DrawTitleName` | `0x007536A0` | 285 | von Hand geprüft |
| 6 | `_DrawNameEx` | – | | nicht im Binary: ältere Fassung (`fPosX, fPosY`), in der Quelle ohne Aufrufer |
| 7 | `_DrawNameEx` | `0x007537C0` | 419 | von Hand geprüft |
| 8 | `_DrawGoMark` | `0x00753970` | 196 | von Hand geprüft |
| 9 | `_DrawFlag` | `0x00754AD0` | 522 | von Hand geprüft |
| 10 | `_DrawGuildCompetition` | `0x00753A40` | 10 | von Hand geprüft |
| 11 | `_DrawGuild` | – | | nicht im Binary: ältere Fassung (`fPosX, fPosY`), in der Quelle ohne Aufrufer |
| 12 | `_DrawGuild` | `0x00754590` | 1097 | von Hand geprüft |
| 13 | `_DrawMonsterAbility` | `0x00753B70` | 256 | von Hand geprüft |
| 14 | `_DrawCharisma` | `0x00754CE0` | 501 | von Hand geprüft |
| 15 | `DrawItem` | `0x00753C70` | 193 | von Hand geprüft |
| 16 | `DrawChar` | `0x00755250` | 67 | von Hand geprüft |
| 17 | `ReCalulateOffsetX` | `0x00753D40` | 450 | von Hand geprüft |
| 18 | `_Draw_Normal` | `0x00754EE0` | 866 | von Hand geprüft |
| 19 | `_Draw_InGuildStadium` | `0x007549F0` | 10 | von Hand geprüft |
| 20 | `_IsInGuildStadium` | `0x00753F10` | 95 | von Hand geprüft |
| 21 | `_IsPlayerInBattleGround` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 22 | `_IsCheckDrawByPVP` | – | | nicht im Binary: nur von der älteren Fassung von `_DrawName` aufgerufen |
| 23 | `_GetIDColorByPVP` | `0x00753F70` | 145 | Zeichenkette |

18 von 24 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmIDBoard_body` (`0x00753610`), `_DrawGuildCompetition_body_00753a4a` (`0x00753A4A`), `AgcmIDBoard` (`0x00754010`), `~AgcmIDBoard` (`0x007542A0`), `_Draw_InGuildStadium_body_007549fa` (`0x007549FA`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | ``m_Type` (Brett-Art, [`AgcmBaseBoard`](AgcmBaseBoard.md))` | `Render`, `Update` |
| `this+0x08 / 0x14` | `Kameraposition / Bildschirmposition (je 3 Float)` | `Update` |
| `this+0x20` | `Versatz (x, y)` | `_Draw_Normal` |
| `this+0x30 / 0x34 / 0x38 / 0x3C` | ``Draw` / Klumpen / sichtbar / Alpha (Reihenfolge nach `AgcmBaseBoard.h`)` | `Render`, `_Draw_Normal` |
| `this+0xBC` | ``IDType` (Bitfeld; nach den Zugriffen in [`AgcmTextBoard`](AgcmTextBoard.md):Update`)` | `AgcmTextBoard::Update` |
| `this+0x1C4 / 0x1CC` | `Gruppen- / Gildenanzeige (`EnableParty` / `EnableGuild`, 2 = zeitweise aus)` | `AgcmTextBoard::Update` |

## Vtable und Aufbau

`AgcmIDBoard` (Namensbrett über Charakteren und Gegenständen; abgeleitet von `AgcmBaseBoard`) hat die Vtable `0x008DFB04`: Slot 0 Löschwrapper (`0x007542A0`), Slot 1 `Render` (`0x007552A0`), Slot 2 `Update` (`0x00753620`). Konstruktor `0x00754010` (644 Byte, ruft `AgcmBaseBoard::AgcmBaseBoard` `0x00751C40`, setzt Standardwerte: Typ „andere“, Anzeige an, Texte leer, Flag-Feld 0, Wechseldauer 1000 ms); die Konstruktor-Hülle `0x00753610` ist der Destruktorrumpf. [`AgcmHPBar`](AgcmHPBar.md) (Hauptcharakter-Brett) erbt von dieser Klasse.

## Aktualisieren und Zeichnen

`Update` (`0x00753620`, 127 Byte) nullt die Zeilenhöhen (`m_TBOffsetY`); nur beim Gegenstandsbrett (`AGCM_BOARD_ITEMID`) rechnet es die Position in Bildschirmkoordinaten um ([`AgcmTextBoardMng`](AgcmTextBoardMng.md):Trans3DTo2D`, `0x0063D810`) und setzt `Draw`. `Render` (`0x007552A0`, 72 Byte) bricht ab, wenn es keinen eigenen Charakter gibt oder das Brett unsichtbar bzw. abgeschaltet ist, und ruft je nach Brett-Art (`m_Type`: 1 = Namensbrett, 2 = Gegenstandsbrett) `DrawChar` (`0x00755250`, 67 Byte; danach wird das Brett auf unsichtbar gesetzt, `this+0x38`) oder per Sprung `DrawItem` (`0x00753C70`). `DrawChar` wird auch von `AgcmHPBar::_DrawHPMPBar` gerufen; `this+0x48` ist das Anzeige-Flag (`m_bEnabled`).
`DrawChar` prüft Anzeige, Sichtbarkeit des Charakters (`AgcmTextBoardMng::IsRender`, `0x0063C190`) und `_IsInGuildStadium` (`0x00753F10`, Region-Nummern 89, 90, 91, 92 und 162 über [`ApmMap`](ApmMap.md)) und ruft `_Draw_InGuildStadium` (`0x007549F0` mit Rumpf `0x007549FA`) oder `_Draw_Normal` (`0x00754EE0`, 866 Byte).
`_Draw_Normal` zeichnet in der Reihenfolge der Quelle: Statussymbol und Burgbesitzer-Symbol, dann `_DrawName` (`0x007542D0`), `_DrawTitleName` (`0x007536A0`), `_DrawGoMark` (`0x00753970`) und – falls erlaubt – `_DrawGuild` (`0x00754590`), `_DrawGuildCompetition` (`0x00753A40` mit Rumpf `0x00753A4A`), `_DrawNameEx` (`0x007537C0`), `_DrawCharisma` (`0x00754CE0`), `_DrawMonsterAbility` (`0x00753B70`) und `_DrawFlag` (`0x00754AD0`), danach die Etiketten (`GetImgIDTag`). Die Namensfarbe holt `_DrawName` über `_GetIDColorByPVP` (`0x00753F70`, Farben `IDColor_MurdererLevel1..3` und `IDColor_FirstAttacker` aus dem [`AgcmResourceLoader`](AgcmResourceLoader.md)). `ReCalulateOffsetX` (`0x00753D40`) misst Name, Spitzname, Gildenname und Titel mit [`AgcmFont`](AgcmFont.md):GetTextExtent` und setzt die linke und rechte Versatzkante; es wird von `AgcmHPBar::SetData` gerufen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der neun Zeichenfunktionen zu den Adressen beruht auf der Aufrufreihenfolge in `_Draw_Normal` (`0x00754EE0`), den Rückgabewerten und je einer Zeichenkette oder einem Aufruf (`GetBuffSkillSmallTexture` für `_DrawMonsterAbility`, [`AgpmBattleGround`](AgpmBattleGround.md) für `_DrawGuildCompetition`, Gildenmarken für `_DrawCharisma` und `_DrawFlag`); die Rümpfe wurden nicht Zeile für Zeile verglichen.
- `_DrawFlag` (`0x00754AD0`) und `_DrawCharisma` (`0x00754CE0`) unterscheiden sich nur durch die Reihenfolge ihrer Aufrufe in `_Draw_Normal` (Charisma vor Flag); beide benutzen [`AgpmGuild`](AgpmGuild.md).
- Die Offsets stammen aus der Quelle und aus Zugriffen in `AgcmTextBoard::Update`; die Felder zwischen `0x40` und `0x1C0` wurden nicht einzeln vermessen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 5, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmFont`](AgcmFont.md), [`AgcmHPBar`](AgcmHPBar.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgpmBattleGround`](AgpmBattleGround.md), [`AgpmGuild`](AgpmGuild.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmHPBar`](AgcmHPBar.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgpmBattleGround`](AgpmBattleGround.md), [`CFlagImoticon`](CFlagImoticon.md)
