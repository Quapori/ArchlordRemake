# AgcmMinimap (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmMinimap` (Minimap, Raider-Karte, Weltkarte, Markierungspunkte) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmMinimap/AgcmMinimap.cpp`. Die Fensterklassen `AcUIMinimap`, `AcUIRaider`, `AcUIWorldmap` und `AGUIDrawMark` aus derselben Quelle sind hier nicht abgeglichen. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, UI-Anmeldungen, Textur-Getter, Punkteverwaltung und Kartenpositionen. Nicht zugeordnet sind `InitMinimapTextureBuffer`, `GetMinimapDummyTexture`, `GetWorldMapTexture`, `GetPcPosTexture`, `GetPoint`, die Namensüberladungen von `DestroyMapPosition`/`GetMapPosition`, `ClearMapPosition`, `ToggleCameraView` und die Einzeiler (eingebaut oder zusammengefaltet).
- **Modulaufbau:** sieben Module in `OnAddModule`, fünf in `OnInit`, alle UI-Namen wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmMinimap.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `InitMinimapTextureBuffer` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 1 | `GetMinimapDummyTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `GetMinimapTexture` | `0x006E1790` | 564 | von Hand geprüft |
| 3 | `FlushMinimapTexture` | `0x006E19E0` | 55 | von Hand geprüft |
| 4 | `OnAddModule` | `0x006E2530` | 1206 | vtable/String |
| 5 | `OnInit` | `0x006E1A20` | 98 | vtable/String |
| 6 | `OnDestroy` | `0x006E1A90` | 269 | vtable/String |
| 7 | `CBSelfCharacterPositionCallback` | `0x006E1BA0` | 129 | Callback-Registrierung |
| 8 | `CBBindingRegionChange` | `0x006E1C30` | 203 | Callback-Registrierung |
| 9 | `CBSetSelfCharacter` | `0x006E1D00` | 111 | Callback-Registrierung |
| 10 | `GetCursorTexture` | `0x006E1D70` | 67 | von Hand geprüft |
| 11 | `GetWorldMapTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `GetMemberPosTexture` | `0x006E1DC0` | 67 | von Hand geprüft |
| 13 | `GetRegisterPosTexture` | `0x006E1E10` | 66 | von Hand geprüft |
| 14 | `GetPcPosTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `GetNpcNormalTexture` | `0x006E1E60` | 67 | von Hand geprüft |
| 16 | `GetNpcQuestNewTexture` | `0x006E1EB0` | 67 | von Hand geprüft |
| 17 | `GetNpcQuestIncompleteTexture` | `0x006E1F00` | 67 | von Hand geprüft |
| 18 | `GetTextureSiegeNormal` | `0x006E1F50` | 67 | von Hand geprüft |
| 19 | `GetTextureSiegeDestroied` | `0x006E1FA0` | 67 | von Hand geprüft |
| 20 | `CBDisplayPos` | `0x006E1FF0` | 66 | UI-Registrierung |
| 21 | `CBToggleRaiderUI` | `0x006E2040` | 105 | UI-Registrierung |
| 22 | `CBToggleMiniMapUI` | `0x006E20B0` | 166 | UI-Registrierung |
| 23 | `CBToggleWorldMapUI` | – | | Rumpf in der Quelle leer (`return TRUE`), im Binary nicht einzeln gefunden |
| 24 | `GetDisabledIndex` | `0x006E29F0` | 103 | von Hand geprüft |
| 25 | `GetPoint` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `AddPoint` | `0x006E3640` | 355 | von Hand geprüft |
| 27 | `RemovePoint` | `0x006E2A60` | 130 | von Hand geprüft |
| 28 | `RemovePointGroup` | `0x006E2AF0` | 237 | von Hand geprüft |
| 29 | `GetPointInfo` | `0x006E2BE0` | 75 | von Hand geprüft |
| 30 | `UpdatePointPosition` | `0x006E2C30` | 96 | von Hand geprüft |
| 31 | `CBUseMapItem` | – | | Rumpf in der Quelle leer (`return TRUE`), im Binary nicht einzeln gefunden |
| 32 | `OnLuaInitialize` | `0x006E2390` | 87 | vtable/String |
| 33 | `CBClickPlusButton` | `0x006E2160` | 28 | UI-Registrierung |
| 34 | `CBClickMinusButton` | `0x006E2180` | 28 | UI-Registrierung |
| 35 | `CBClickCameraView` | `0x006E23F0` | 70 | UI-Registrierung |
| 36 | `CBClickMapToggle` | `0x006E2440` | 22 | UI-Registrierung |
| 37 | `CBDisplayRegionName` | `0x006E21A0` | 239 | UI-Registrierung |
| 38 | `SetCallbackRegisterMapPos` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 39 | `OpenDlgAndAddPos` | `0x006E3080` | 314 | von Hand geprüft |
| 40 | `AddMapPosition` | `0x006E2EC0` | 363 | von Hand geprüft |
| 41 | `AddMapPosition` | `0x006E3030` | 55 | von Hand geprüft |
| 42 | `DestroyMapPosition` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `DestroyMapPosition` | `0x006E2E10` | 113 | von Hand geprüft |
| 44 | `GetMapPositionIndex` | `0x006E2C90` | 65 | von Hand geprüft |
| 45 | `GetMapPosition` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 46 | `GetMapPosition` | `0x006E2CE0` | 61 | von Hand geprüft |
| 47 | `ClearMapPosition` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 48 | `ToggleCameraView` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 49 | `ToggleMinimapSize` | `0x006E2290` | 126 | von Hand geprüft |

38 von 50 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006e3350` (`0x006E3350`), `ctor_or_dtor_006e3550` (`0x006E3550`), `~AgcmMinimap` (`0x006E3620`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xC38 / 0xC3C` | `Ereignis-IDs `Minimap_Map_ON` / `…OFF`` | `ToggleMinimapSize` |
| `this+0xC58` | `Merker „Minimap an“` | `ToggleMinimapSize` |
| `this+0xC5C` | `Kopf der Liste der registrierten Kartenpositionen` | `GetMapPosition…`, `DestroyMapPosition` |
| `this+0xED0 / 0xED4` | `Anfang / Ende der Punkteliste (Element `0x60` Byte)` | `GetDisabledIndex`, `GetPointInfo` |
| `this+0xBE0…0xBF4` | `Zeiger auf die NPC- und Siege-Texturen` | Textur-Getter |

## OnAddModule (0x006E2530)

Holt [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmParty`](AgpmParty.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmFont`](AgcmFont.md), [`ApmMap`](ApmMap.md), [`AgpmCharacter`](AgpmCharacter.md) und `AgcmCharacter` (Zeichenketten im Dekompilat, gleiche Reihenfolge wie die Quelle). Bei `AgcmCharacter` werden „eigene Position geändert“ (`CBSelfCharacterPositionCallback` `0x006E1BA0`), „eigener Charakter gesetzt“ (`CBSetSelfCharacter` `0x006E1D00`) und „eigene Region geändert“ (`CBBindingRegionChange` `0x006E1C30`) angemeldet.
UI-Anmeldungen (Zeichenketten im Binary, gleiche Namen wie in der Quelle): Steuerelement `MiniMap1`, Anzeige und Benutzerdaten `MiniMap_Pos1` bzw. `Raider_Pos`, Funktionen `MiniMap_ToggleUI`, `WorldMap_ToggleUI`, `Raider_ToggleUI`, `Minimap_Plus_Click`, `Minimap_Minus_Click`, `Minimap_CameraView_Click`, `Minimap_Map_Toggle`, Anzeige `Minimap_Region_Name` mit Benutzerdaten `Minimap_Region_Name_UD` und die Ereignisse `MiniMap_OpenUI`, `MiniMap_CloseUI`, `Raider_OpenUI`, `Raider_CloseUI`, `MiniMap_ForcedClose`, `MiniMap_YouCanOpenUI`, `WorldMap_OpenUI`, `WorldMap_NoItem`, `WorldMap_CloseUI`, `Minimap_Map_ON`, `Minimap_Map_OFF`. Zuletzt wird bei [`AgcmItem`](AgcmItem.md) der Rückruf „Kartengegenstand benutzt“ angemeldet.

## OnInit und Lua

`OnInit` (`0x006E1A20`) holt [`AgpmPvP`](AgpmPvP.md), `AgcmCharacter`, [`AgpmGuild`](AgpmGuild.md), [`AgpmBattleGround`](AgpmBattleGround.md) und [`AgcmUIChatting2`](AgcmUIChatting2.md). `OnLuaInitialize` (`0x006E2390`) legt die Lua-Funktionen an.

## Texturen

Die zehn Textur-Getter liegen in Quellreihenfolge bei `0x006E1D70`–`0x006E1FA0`; sie laden die Dateien `Main_Minimap_Cursor` (Pfad `texture\UI\`), `mempos`, `Main_Minimap_Pos_Siege1`, `…NPC0`, `…NPC2`, `…NPC1`, `…Siege0`, `…Siege1` über den gemeinsamen Lader `0x006E1750` (bis zu drei Versuche) und setzen im Textur-Objekt das Byte `+0x51` auf `0x33`. Die Zuordnung von NPC1/NPC2 folgt den `#define`s der Quelle (NPC1 = Quest unvollständig, NPC2 = Quest neu). `GetRegisterPosTexture` und `GetTextureSiegeDestroied` laden dieselbe Datei `Siege1` in verschiedene Felder (`this+0xBF4`, `this+0xBF0`). `GetMinimapTexture` (`0x006E1790`) bildet den Dateinamen `MAP%04d%c`; `FlushMinimapTexture` (`0x006E19E0`) zerstört die 30 Puffertexturen und setzt den Index auf −1.

## Markierungspunkte und Kartenpositionen

`AddPoint` (`0x006E3640`) sucht über `GetDisabledIndex` (`0x006E29F0`) einen freien Platz in der Punkteliste (Elementgröße `0x60`) oder hängt an (`0x006E31F0`) und meldet den Punkt bei `AgcmUIWorldmap` an. `RemovePoint` (`0x006E2A60`) und `RemovePointGroup` (`0x006E2AF0`) setzen das Feld `bDisabled` (`+0x58`) und melden bei `AgcmUIWorldmap` ab; `GetPointInfo` (`0x006E2BE0`) liefert `NULL` für deaktivierte Punkte, `UpdatePointPosition` (`0x006E2C30`) schreibt die drei Positionswerte (`+0x44…0x4C`).
Die Liste der registrierten Kartenpositionen liegt bei `this+0xC5C` (Listenkopf); `GetMapPositionIndex` (`0x006E2C90`), `GetMapPosition` (nach ID, `0x006E2CE0`) und `DestroyMapPosition` (nach ID, `0x006E2E10`, meldet über `AgcmUIWorldmap` ab) laufen diese Liste ab. `AddMapPosition` (`0x006E2EC0`) und die Überladung mit Koordinaten (`0x006E3030`) sowie `OpenDlgAndAddPos` (`0x006E3080`, Meldungsschlüssel `Position_NameInput_Message`) sind über Zeichenketten und Aufrufbeziehungen bestätigt.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, `OnInit`, UI-Namen, Texturnamen).

## Grenzen

- Die Textur-Getter und die Punkteverwaltung sind über Zeichenketten, Feldzugriffe und die Quellreihenfolge zugeordnet, nicht Zeile für Zeile verglichen.
- `ToggleCameraView` ist wahrscheinlich in `CBClickCameraView` (`0x006E23F0`) eingebaut.
- Die Hilfsfunktionen `0x006E1670` und `0x006E16D0` (Kachelkoordinaten aus der Kartennummer) gehören zu keiner Quellmethode.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht im Client: 4, ohne Kandidat: 6.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmFont`](AgcmFont.md), [`AgcmItem`](AgcmItem.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmBattleGround`](AgpmBattleGround.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmGuild`](AgpmGuild.md), [`AgpmParty`](AgpmParty.md), [`AgpmPvP`](AgpmPvP.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmUIQuest2`](AgcmUIQuest2.md)
