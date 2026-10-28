# AgcUIQuestText (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcUIQuestText` (Quest-Text mit Gegenstands-Schaltflächen, Positionslinks und Bildlauf; Hilfsobjekt von [`AgcmUIQuest2`](AgcmUIQuest2.md) und dem Quest-Journal) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly der Funktionen in Export-Lücken (`x86dis.py`), Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcUIQuestText/AgcUIQuestText.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 21 von 27 Quellmethoden sind zugeordnet. Die sechs übrigen sind eingebaut (`GetQuestItemInfo`, `HexStringToDWORD`, `CloseQuestItemTooltip`, `ClearClickSelectButton`) oder im Binary nicht vorhanden und in der Quelle unreferenziert (`DelQuestItemInfo`, `ClearQuestItemInfo`).
- **Besonderheit:** Fünf Rückruf-Funktionen (`0x00764400`, `0x00764460`, `0x00764570`, `0x00764F10`, `0x00765110`) liegen in Lücken des Ghidra-Exports und wurden über Zeiger der Registrierung gefunden und mit einer eigenen Disassembly (`x86dis.py`) gelesen. Die vorherige Benennung von `0x0076614A` als `QuestControlInfo::ctor_or_dtor` war falsch: es ist die Fortsetzung von `MakeTextList`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcUIQuestText.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | `0x00765A90` | 244 | von Hand geprüft |
| 1 | `SetScrollControl` | `0x00764ED0` | 54 | von Hand geprüft |
| 2 | `AddQuestItemInfo` | `0x00765A10` | 57 | von Hand geprüft |
| 3 | `DelQuestItemInfo` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 4 | `GetQuestItemInfo` | – | | in `CBOpenQuestItemTooltip` eingebaut (Map-Suche `0x0053FB90`) |
| 5 | `ClearQuestItemInfo` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 6 | `CBOpenQuestItemTooltip` | `0x00765110` | 127 | von Hand geprüft |
| 7 | `CBCloseQuestItemTooltip` | `0x00764F10` | 27 | von Hand geprüft |
| 8 | `CBRefreshTextScroll` | `0x00764400` | 91 | von Hand geprüft |
| 9 | `CBMouseWheel` | `0x00764460` | 178 | von Hand geprüft |
| 10 | `OpenQuestItemTooltip` | `0x00764520` | 67 | von Hand geprüft |
| 11 | `AddTooltipAction` | `0x00765190` | 98 | von Hand geprüft |
| 12 | `SliceLineByWord` | `0x00765CA0` | 1115 | von Hand geprüft |
| 13 | `InsertQuestControl` | `0x007656A0` | 764 | Zeichenkette |
| 14 | `MakeTextList` | `0x00766100` | 74 | von Hand geprüft |
| 15 | `CBSelectButtonEvent` | `0x00764F60` | 85 | von Hand geprüft |
| 16 | `CBPositionLinkEvent` | `0x00764570` | 329 | von Hand geprüft |
| 17 | `CBQuestRegisterItem` | `0x00765A50` | 62 | von Hand geprüft |
| 18 | `AddPositionLinkEvent` | `0x007646C0` | 135 | von Hand geprüft |
| 19 | `RefreshTextList` | `0x00766DD0` | 255 | von Hand geprüft |
| 20 | `CalcEventType` | `0x00764750` | 1231 | von Hand geprüft |
| 21 | `HexStringToDWORD` | – | | in `MakeTextList` eingebaut (keine eigene Funktion, keine Hex-Konstanten im Bereich) |
| 22 | `AddClickSelectAction` | `0x00765540` | 127 | von Hand geprüft |
| 23 | `CloseQuestItemTooltip` | – | | in `CBCloseQuestItemTooltip` eingebaut |
| 24 | `ClearClickSelectButton` | – | | in `ClearTextList` eingebaut |
| 25 | `ClearTextList` | `0x00765000` | 121 | von Hand geprüft |
| 26 | `SetAlpha` | `0x00764FC0` | 55 | von Hand geprüft |

21 von 27 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `for_each_AddChild` (`0x00764E00`), `for_each_DeleteControl` (`0x00764E60`), `~AgcUIQuestText_body` (`0x00765450`), `AgcUIQuestText` (`0x007655C0`), `~AgcUIQuestText` (`0x00765680`), `MakeTextList_body_0076614a` (`0x0076614A`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | `Zeiger `ownerUI_`` | `RefreshTextList`, Destruktor |
| `this+0x08` | `Zeiger `AgcmCharacter`` | `CBOpenQuestItemTooltip`, `OpenQuestItemTooltip` |
| `this+0x0C` | `Kopfknoten `questTexts_` (std::list)` | `ClearTextList`, `SetAlpha` |
| `this+0x14 / 0x1C` | ``selectButtons_` / `selectButtonIdx_`` | `CBSelectButtonEvent`, `ClearTextList` |
| `this+0x20 / 0x24` | ``questTextUI_` / `textScrollUI_`` | `RefreshTextList`, `SetScrollControl` |
| `this+0x28` | ``questItemInfos_` (std::map TID zu `AgpdItem*`)` | `CBOpenQuestItemTooltip`, `AddQuestItemInfo` |
| `this+0x40..0x64` | `Modulzeiger (Minimap, Worldmap, QuestJournal, UIQuestJournal, AgpmItem, AgcmItem, AgcmUIItem, AgcmUIManager2, AgcmFont, AgcmUIQuest2)` | `Init` |
| `this+0x68` | ``maxScroll_`` | `RefreshTextList`, `CBRefreshTextScroll` |

## Vtable und Aufbau

Die Klasse ist kein `ApModule`, sondern ein Hilfsobjekt der Quest-Oberfläche; Vtable `0x008E0720` (Slot 0: Löschwrapper `0x00765680`). Konstruktor `0x007655C0` (legt `questTextUI_` als `AcUIBase` mit 0x1D04 Byte an und setzt `bClipping`), Destruktorrumpf `0x00765450` (`ClearTextList(TRUE)`, `DeleteChild`, `delete questTextUI_`, Listen und Map leeren). Layout laut Header, im Binary bestätigt: `this+4` `ownerUI_`, `+8` `agcmCharacter_`, `+0xC` `questTexts_` (std::list), `+0x14` `selectButtons_`, `+0x1C` `selectButtonIdx_`, `+0x20` `questTextUI_`, `+0x24` `textScrollUI_`, `+0x28` `questItemInfos_` (std::map), `+0x68` `maxScroll_`.
`Init` (`0x00765A90`) holt per Namen `AgcmQuestJournal`, `AgcmUIQuestJournal`, [`AgcmMinimap`](AgcmMinimap.md), `AgcmUIWorldmap`, [`AgpmItem`](AgpmItem.md), [`AgcmItem`](AgcmItem.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIManager2`](AgcmUIManager2.md), `AgcmCharacter`, [`AgcmFont`](AgcmFont.md), `AgcmUIQuest2` und trägt einmalig (statisches Flag `registCallback`) `CBQuestRegisterItem` (`0x00765A50`) als Rückruf `ItemInformationResult` bei `AgpmItem` ein. `SetScrollControl` (`0x00764ED0`) hängt `CBRefreshTextScroll` (`0x00764400`) und `CBMouseWheel` (`0x00764460`) an.

## Quest-Text aufbauen

`RefreshTextList` (`0x00766DD0`) löst das alte Eltern-Fenster, hängt `questTextUI_` an das neue, ruft `ClearTextList(TRUE)` (`0x00765000`), setzt die Fenstergröße, ruft `MakeTextList` (`0x00766100`, mit der Fortsetzung bei `0x0076614A`, zusammen 3.256 Byte, rekursiv für Zeilenumbrüche), berechnet `maxScroll_` und die Bildlaufeinheit (`_scroll_interval` 10 geteilt durch `maxScroll_`) und hängt alle Steuerelemente über eine `for_each`-Hilfe (`0x00764E00`) an.
`CalcEventType` (`0x00764750`, 1.231 Byte) zerlegt die Steuerzeichenfolgen in `ITEM::…` (Anzahl, TID, Aufwertung, Sockel, Bindung, Auswahl) und `POS::…` (Region, X, Y, Name) an `::` und `>`. `SliceLineByWord` (`0x00765CA0`) teilt eine Zeile bei Leerzeichen (über `StringUtill::split`, `0x00765B90`) und misst mit `AgcmFont::GetTextExtent` (Vtable-Slot, Offset `0xB98`). `InsertQuestControl` (`0x007656A0`) legt Text-, Positionslink- und Gegenstandsschaltflächen an; die Hilfen `AddTooltipAction` (`0x00765190`), `AddPositionLinkEvent` (`0x007646C0`) und `AddClickSelectAction` (`0x00765540`) setzen Rückrufe und Farben (`0x30FFFFFF`/`0x90FFFFFF` für Auswahl, `0x60FFFFFF`/`0xAAFFFFFF` für Positionslinks).

## Rückrufe

`CBOpenQuestItemTooltip` (`0x00765110`) sucht die TID in der Map (`GetQuestItemInfo` ist eingebaut) und öffnet den Tooltip (`OpenQuestItemTooltip`, `0x00764520`), sonst sendet es eine Tooltip-Registrierungsanfrage (Typ 4 = `quest_grid`) über `AgcmItem`. `CBCloseQuestItemTooltip` (`0x00764F10`) schließt den Tooltip über `AgcmUIItem` (`CloseQuestItemTooltip` ist eingebaut). `CBQuestRegisterItem` (`0x00765A50`) legt die Antwort über `AddQuestItemInfo` (`0x00765A10`, Map-Zugriff `0x007659A0`) ab und öffnet den Tooltip, wenn das Typ-Bit `quest_grid` gesetzt ist.
`CBPositionLinkEvent` (`0x00764570`) bildet aus Position und Name eine ID, löscht und setzt die Kartenmarke (`AgcmMinimap::DestroyMapPosition`/`AddMapPosition`, `0x006E2E10`/`0x006E2EC0`) und öffnet die Weltkarte (`0x0067D740`); den Namen holt es über `AgcmUIQuest2::GetQuestPosName` (`0x006B68F0`). `CBSelectButtonEvent` (`0x00764F60`) markiert die angeklickte Schaltfläche in `selectButtons_` und speichert den Index bei `this+0x1C`. `CBRefreshTextScroll`/`CBMouseWheel` verschieben `questTextUI_` um `maxScroll_` mal Bildlaufwert; das Mausrad rechnet Delta durch 40 (Division mit Magic-Konstante `0x99999999`).

## Aufräumen

`ClearTextList` (`0x00765000`, 121 Byte) leert `selectButtons_` und setzt den Auswahlindex auf -1 (`ClearClickSelectButton` ist eingebaut), löscht die Kindfenster und – bei `bDelData` – über die `for_each`-Hilfe `0x00764E60` jedes `m_pUIBase` und jedes `QuestControlInfo`. `SetAlpha` (`0x00764FC0`) setzt den Alpha-Zeiger (`+0x1D8`) aller Steuerelemente. `QuestControlInfo` liegt in einem Pool (`ApMemory<QuestControlInfo,1000>`): `operator new` `0x00764C20`, `operator delete` `0x00764D50`, Löschwrapper `0x00764F30`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind die Rückrufe, `CalcEventType`, `Init`, `ClearTextList` und `RefreshTextList` (Aufbau und Aufrufe); `MakeTextList` (3.256 Byte) und `InsertQuestControl` wurden nur über Aufrufer, Größe und die genannten Zeichenketten (`Quest_Slot.png`, `Quest_ActiveBox.png`) zugeordnet, nicht Zeile für Zeile verglichen.
- Dass `HexStringToDWORD` eingebaut ist, folgt aus dem Fehlen einer eigenen Funktion und einer Suche nach den Konstanten 0x37/0x57 im Bereich `0x00764000`–`0x00767000`; es ist kein Byte-Vergleich mit dem Rumpf.
- Die Offsets stammen aus Header-Reihenfolge und den Zugriffen im Binary; nicht jeder Modulzeiger zwischen `0x40` und `0x64` ist einzeln gegen seinen Namen geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, nicht im Client: 2, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmFont`](AgcmFont.md), [`AgcmItem`](AgcmItem.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgpmItem`](AgpmItem.md)
