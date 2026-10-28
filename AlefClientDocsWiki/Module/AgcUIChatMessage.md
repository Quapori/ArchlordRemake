# AgcUIChatMessage (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `AgcUIChatMessage` (Chat-Fenster: Tabs, Liste, Menü) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `AgcUIChatMessage.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 37 von 59 Quellmethoden sind zugeordnet; zugeordnet wurde über Aufrufketten (`Refresh`), Aufrufer im [`AgcChatManager`](AgcChatManager.md), Registrierungen und Zeichenketten.
- **Nachrichtenarten:** zwölf Formate mit Kopftext und Farbe, alle identisch zur Quelle.
- **Fenstergröße:** Start 50/50, 335×335 Pixel.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcUIChatMessage.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Initialize` | `0x00739DB0` | 1671 | ver |
| 1 | `Clear` | `0x00735930` | 190 | ver |
| 2 | `ClearUI` | `0x00735060` | 381 | ver |
| 3 | `OpenSetupMenu` | `0x0073A880` | 94 | ver |
| 4 | `Refresh` | `0x00739C00` | 54 | ver |
| 5 | `AddMessage` | `0x00739C40` | 140 | ver |
| 6 | `AddTab` | `0x007376B0` | 265 | ver |
| 7 | `DelTab` | `0x007367D0` | 183 | ver |
| 8 | `GetTabCount` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `GetTab` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `IsUseMessageType` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `IsUsing` | `0x007368B0` | 35 | ver |
| 12 | `SetFontSize` | `0x00739CD0` | 186 | ver |
| 13 | `SetTabInput` | `0x00734C20` | 58 | ver |
| 14 | `MoveChatWindow` | `0x007351E0` | 211 | ver |
| 15 | `GetUIPos` | `0x00734C60` | 64 | ver |
| 16 | `GetUISize` | `0x00734CA0` | 64 | ver |
| 17 | `GetMessageInstance` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `GetMessageInstanceCount` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `DestroyMessageInstance` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `DestroyMessageInstance` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `AllDestroyMessageInstance` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `SetListItemMaxCount` | `0x007352C0` | 263 | ver |
| 23 | `ForceDetailShow` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `ForceDetailHide` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 25 | `AttachScroll` | `0x00734CE0` | 11 | ver |
| 26 | `DetachScroll` | `0x00734CF0` | 11 | ver |
| 27 | `AttachResize` | `0x00734D00` | 11 | ver |
| 28 | `DetachResize` | `0x00734D10` | 11 | ver |
| 29 | `AttachMove` | `0x00734D20` | 11 | ver |
| 30 | `DetachMove` | `0x00734D30` | 11 | ver |
| 31 | `AttachSetup` | `0x00734D40` | 11 | ver |
| 32 | `DetachSetup` | `0x00734D50` | 11 | ver |
| 33 | `ShowTabButton` | `0x00734D60` | 54 | ver |
| 34 | `HideTabButton` | `0x00734DA0` | 51 | ver |
| 35 | `AllDeleteListItem` | `0x00734DE0` | 84 | ver |
| 36 | `RefreshTabButton` | `0x007368E0` | 976 | ver |
| 37 | `RefreshList` | `0x00739A50` | 422 | ver |
| 38 | `RefreshResize` | `0x00734E40` | 131 | ver |
| 39 | `RefreshSetup` | `0x00734ED0` | 101 | ver |
| 40 | `RefreshScroll` | `0x007359F0` | 435 | ver |
| 41 | `_InitUIList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 42 | `_InitUIScroll` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `_InitUITab` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 44 | `_InitMenuEvent` | `0x0073A440` | 1075 | ver |
| 45 | `_RefreshMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 46 | `_GetUsingMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 47 | `CBTabClickEvent` | `0x00735BB0` | 38 | ver |
| 48 | `CBMenuEventDocking` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 49 | `CBMenuEventFontSize` | `0x00739D90` | 29 | ver |
| 50 | `CBMenuEventTabEnable` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 51 | `SetLastButton` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 52 | `AddUsingMessage` | `0x007399B0` | 157 | ver |
| 53 | `SetScrollValue` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 54 | `GetScrollValue` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 55 | `IsUsableType` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 56 | `InitMessageInstance` | `0x007377C0` | 1225 | Zeichenkette |
| 57 | `GetChatMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 58 | `SelectTab` | `0x007356B0` | 74 | ver |

37 von 59 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x16FAC` | `Sichtbarkeit der Scrollleiste` | `AttachScroll`/`DetachScroll` |
| `0x1338C` | `Sichtbarkeit des Einstellungsknopfs` | `AttachSetup`/`DetachSetup` |
| `0x1E778` | `Zeiger auf `AgcdUI` (`m_pUI`)` | `GetUIPos`, `GetUISize`, `ClearUI` |
| `0x1E77C` | `Liste der Nachrichten-Objekte (`m_listChatMessage`)` | `InitMessageInstance` |
| `0x1E7B8` | `Zeiger auf den Manager (`m_pManagerClass`)` | `Initialize`, `RefreshTabButton` |
| `0x1E7CC` | `Tab-Eingabe-Flag (`m_bTabInput`)` | `SetTabInput` |

## Umfang

Die Klasse `AgcUIChatMessage` ist ein einzelnes Chat-Fenster mit Tabs, Liste, Scrollleiste und Menü (`AgcUIChatMessage.cpp`, 59 Methoden). Im Binary liegt sie bei `0x00734C20`–`0x0073A880`, durchsetzt mit Funktionen anderer UI-Klassen und STL-Hilfen. Viele Methoden sind 4–12 Zeilen lang und im Binary eingebaut oder zusammengefaltet.

## Aufbau des Fensters (Initialize, 0x00739DB0)

Wird von `AgcChatManager::CreateUIChatMessage` aufgerufen, setzt das Fenster auf Position 50/50 und Größe 335×335 (`MAX_LISTBOX_STRING` = `0x14F`) und legt Liste, Scrollleiste, Größen-, Verschiebe- und Einstellungsknopf an. Die Callbacks zum `AgcChatManager` (Größe, Verschieben, Andocken, Einstellungen, Scroll-Aktualisierung, Tab-Löschen/-Bearbeiten, Ziehen) werden hier gesetzt; die Zuordnung dieser Callbacks steht im Bericht `AgcChatManager`.

## Nachrichtenarten (InitMessageInstance, 0x007377C0)

Die Funktion legt zwölf [`AgcChatMessage`](AgcChatMessage.md)-Objekte an (Nachrichtenart = `1 << i`, `CHAT_MESSAGE_COUNT` = 12) und setzt über `SetTextFormat` (`0x007A1FD0`) Format, Kopftext und Farbe. Alle zwölf Zeilen stimmen mit der Quelle überein:

| Art (Bit) | Format | Kopftext (UI-Text) | Farbe |
|---|---|---|---|
| Normal (`0x1`) | `[%s] %s` | – | `NORMAL_CHAT` |
| Gilde (`0x2`) | `%s[%s] %s` | `Chat_Guild_Header` | `GUILD_CHAT` |
| Gruppe (`0x4`) | `%s[%s] %s` | `Chat_Party_Header` | `PARTY_CHAT` |
| Flüstern (`0x8`) | `%s[%s] %s` | `Chat_Whisper_Header` | `WHISPER_RECV` |
| System (`0x10`) | `%s %s` | `Chat_System_Header` | `SYSTEM_CHAT2` |
| Hinweis (`0x20`) | `%s %s` | `Chat_Notice_Header` | `NOTICE_CHAT1` |
| Quest (`0x40`) | `%s %s` | `Chat_Quest_Header` | `QUEST_CHAT` |
| Belagerung/Schrein (`0x80`) | `%s %s` | `Chat_Shrine_Header` | `SHRINE_CHAT` |
| Archlord (`0x100`) | Standardformat | – | `Yellow` |
| Rufen (`0x200`) | `%s[%s] %s` | `Chat_Area_Header` | `WORD_BALLON` |
| Rasse (`0x400`) | Standardformat | – | `RACE_TRUMPET` |
| Elementar (`0x800`) | Standardformat | – | `Yellow` |

## Aktualisierung (Refresh, 0x00739C00)

Reihenfolge wie in der Quelle: `RefreshTabButton` (`0x007368E0`), `RefreshResize` (`0x00734E40`), `RefreshSetup` (`0x00734ED0`), `SetListItemMaxCount` (`0x007352C0`), `RefreshList` (`0x00739A50`), `RefreshScroll` (`0x007359F0`). Diese Reihenfolge ist die Grundlage der Zuordnung; `CBResizeEvent` des Managers ruft `MoveChatWindow` (`0x007351E0`), `SetListItemMaxCount` und `Refresh(TRUE)` in derselben Folge wie die Quelle.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`InitMessageInstance`-Tabelle, `Refresh`-Kette, `SetTabInput`, `Attach…/Detach…`, `ShowTabButton`/`HideTabButton`).

## Grenzen

- 22 von 59 Methoden sind nicht zugeordnet, vor allem kleine Listen-Zugriffe (`GetTab`, `GetTabCount`, `GetMessageInstance`, `Destroy…`), die Menü-Callbacks `CBMenuEventDocking`/`CBMenuEventTabEnable` und die kleinen `_InitUI…`-Hilfen.
- `AddUsingMessage` (`0x007399B0`) und `CBMenuEventFontSize` (`0x00739D90`) sind nur über den Aufrufgraphen und kurze Rümpfe zugeordnet.
- Der Inhalt von `Initialize` und `_InitMenuEvent` wurde nicht Zeile für Zeile verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 7, nicht im Client: 10, ohne Kandidat: 3, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `_RefreshMessage` | 34 | `0x00739830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTab` | 14 | `0x00735660` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcChatManager`](AgcChatManager.md), [`AgcChatMessage`](AgcChatMessage.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
- **Erwähnt in:** [`AgcChatManager`](AgcChatManager.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
