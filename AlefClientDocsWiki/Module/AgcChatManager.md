# AgcChatManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `AgcChatManager` (Chat-Verwaltung: Empfang, Fenster, Tabs, Docking) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `AgcChatManager.cpp` und `AgcChatManagerCB.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 44 von 70 Quellmethoden sind zugeordnet; in diesem Durchgang kamen 20 hinzu (alle Fenster-Callbacks, Docking, `ChatIdle`, `OnAddMessage`).
- **Empfang:** Alle Nachrichtenarten laufen über einen einzigen Handler `CallBack_RecvMsgChatting`, wie in der Quelle.
- **Zahlen:** Mindestgröße 200, Abtrenn-Abstand 30, Docking-Dauer 300 ms, Ein-/Ausblenden 500 ms, 12 Nachrichtenarten – alle im Binary bestätigt.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcChatManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `CreateUIChatMessage` | `0x0070D790` | 336 | Zeichenkette |
| 1 | `AddUIChatMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `DestroyUIChatMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 3 | `ChatIdle` | `0x0070F6A0` | 1937 | ver |
| 4 | `LoadBaseFile` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 5 | `LoadChatFile` | `0x0070FF20` | 858 | Zeichenkette |
| 6 | `SaveChatFile` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 7 | `OnRegisterUIEvent` | `0x0070EA10` | 209 | ver |
| 8 | `OnRegisterCallBack` | `0x0070E630` | 782 | Zeichenkette |
| 9 | `OnRegisterTextFormat` | `0x0070C760` | 80 | Zeichenkette |
| 10 | `OnAddMessage` | `0x0070DE90` | 706 | ver |
| 11 | `AddDockingEvent` | `0x0070F060` | 143 | ver |
| 12 | `OnCollectControls` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 13 | `_ItemEvent` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `_MapPosEvent` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `_ParseMessageText` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `_LoadChatSetting` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `_DefaultChatSetting` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `_WhisperEvent` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `GetChatMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `GetUIChatMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `_DockingCheck` | `0x0070CA80` | 225 | ver |
| 22 | `_CombineDockingUI` | `0x0070CB70` | 93 | ver |
| 23 | `_DockingPreEventStart` | `0x0070CBD0` | 40 | ver |
| 24 | `_DockingPreEventEnd` | `0x0070CC00` | 40 | ver |
| 25 | `ShowChatUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `HideChatUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `AllForceDetailShow` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `AllForceDetailHide` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `AllShowChatUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `AllHideChatUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 31 | `AllClearChatUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 32 | `AllClearMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 33 | `SetEmptyUIData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `GetEmptyUIData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 35 | `_CopyUIChatMessage` | `0x0070E2D0` | 180 | ver |
| 36 | `CBOptionOK` | `0x0070E390` | 405 | UI-Registrierung |
| 37 | `CBTabOptionFlagCheck` | `0x0070CCA0` | 132 | UI-Registrierung |
| 38 | `CBTabAllOptionFlagCheck` | `0x0070CD30` | 157 | UI-Registrierung |
| 39 | `CBDisplayCheck` | `0x0070CDD0` | 84 | UI-Registrierung |
| 40 | `CBDisplayAllCheck` | `0x0070CE30` | 95 | UI-Registrierung |
| 41 | `CBDisplayName` | `0x0070E530` | 173 | UI-Registrierung |
| 42 | `CBDisplayColor` | `0x0070E5E0` | 65 | UI-Registrierung |
| 43 | `_AddOptionTab` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 44 | `_EditOptionTab` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 45 | `_GetDisplayName` | `0x0070D0C0` | 400 | ver |
| 46 | `_GetDisplayColor` | `0x0070D370` | 343 | Zeichenkette |
| 47 | `CBInitOpenAddTab` | `0x0070D510` | 132 | UI-Registrierung |
| 48 | `CBInitOpenEditTab` | `0x0070D5A0` | 179 | UI-Registrierung |
| 49 | `CallBack_RecvMsgChatting` | `0x005FB420` | 744 | Zeichenkette |
| 50 | `CallBack_WhisperOffline` | `0x005FB760` | 157 | Zeichenkette |
| 51 | `CAllBack_WhisperBlock` | `0x005FB800` | 157 | Zeichenkette |
| 52 | `GetTextColor` | `0x005FAF60` | 64 | ver |
| 53 | `OnAddChattingMessage` | `0x005FAFA0` | 72 | ver |
| 54 | `OnAddSystemMessage` | `0x005FAFF0` | 90 | Zeichenkette |
| 55 | `OnAddNoticeMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 56 | `OnAddQuestMessage` | `0x005FB050` | 87 | Zeichenkette |
| 57 | `OnAddShrineMessage` | `0x005FB0B0` | 90 | Zeichenkette |
| 58 | `CBDragCallback` | `0x005FB8A0` | 556 | ver |
| 59 | `CBEventCallback` | `0x005FBCE0` | 322 | ver |
| 60 | `CBDockingCallback` | `0x005FBAD0` | 264 | ver |
| 61 | `CBDockingPreEvent` | `0x005FBBE0` | 147 | ver |
| 62 | `CBScrollRefresh` | `0x005FB110` | 31 | ver |
| 63 | `CBResizeEvent` | `0x005FB130` | 186 | ver |
| 64 | `CBMoveEvent` | `0x005FB1F0` | 114 | ver |
| 65 | `CBSetupEvent` | `0x005FB270` | 29 | ver |
| 66 | `CBTabDeleteEvent` | `0x005FBF50` | 97 | ver |
| 67 | `CBTabEditEvent` | `0x005FB290` | 94 | ver |
| 68 | `CBAddTab` | `0x005FB2F0` | 87 | ver |
| 69 | `_ParseMessageData` | `0x005FB350` | 196 | ver |

44 von 70 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0070f400` (`0x0070F400`), `~AgcChatManager` (`0x0070F540`), `ctor_or_dtor_0070f550` (`0x0070F550`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1F8 / 0x1FC` | `bearbeitetes Fenster / Tab (`m_pOperationChatUI`, `m_pOperationChatTab`)` | `CBTabEditEvent`, `CBAddTab` |
| `0x20C / 0x210 / 0x214` | `Ereignis-IDs TabOptionAdd / TabOptionEdit / TabOption_CloseUI` | `OnRegisterCallBack`, `CBAddTab` |
| `0x218` | `Tab-Flags (12 × 4 Byte)` | `OnRegisterCallBack` (`Chat_DisplayUserData`) |

## Umfang

`AgcChatManager` ist die Basisklasse von [`AgcmUIChatting2`](AgcmUIChatting2.md) (Chat-Fenster, Tabs, Docking). Die Quelle verteilt sie auf `AgcChatManager.cpp` und `AgcChatManagerCB.cpp` (70 Methoden). Die Funktionen liegen im Binary in zwei Gruppen: `0x005FAF60`–`0x005FBF50` (Callbacks) und `0x0070C760`–`0x00710280`.

## Callback-Registrierung (OnRegisterCallBack, 0x0070E630)

Fünfzehn Registrierungen in der Reihenfolge der Quelle: dreizehn Mal derselbe Empfangs-Handler `CallBack_RecvMsgChatting` (`0x005FB420`) für Normal-, Betonungs-, Gebiets-, Weltweit-, Sprechblasen-, Gilden-, Gilden-Bündnis-, Gruppen-, System-Stufe 1–3-, Aktions- und Flüster-Nachrichten, dazu `CAllBack_WhisperBlock` (`0x005FB800`) und `CallBack_WhisperOffline` (`0x005FB760`).
Danach UI: Funktionen `Chat_OptionOK`, `Chat_FlagCheck`, `Chat_FlagAllCheck`, `Chat_InitOpenAddTab`, `Chat_InitOpenEditTab`; Anzeigen `Chat_CheckDisplay`, `Chat_NameDisplay`, `Chat_ColorDisplay`, `Chat_AllCheckDisplay`; Benutzerdaten `Chat_DisplayUserData` (12 Einträge, `CHAT_MESSAGE_COUNT`) und `Chat_AllDisplayUserData`; Ereignisse `TabOptionAdd_OpenUI`, `TabOptionEdit_OpenUI`, `TabOption_CloseUI`. Alle Namen stimmen mit der Quelle überein.

## Fenster-Callbacks (AgcUIChatMessage → AgcChatManager)

Die Callbacks, die [`AgcUIChatMessage`](AgcUIChatMessage.md) beim Aufbau eines Chat-Fensters setzt, sind über ihre Registrierungsstellen (`0x007368E0`, `0x00739DB0`, `0x0070D790`) und das Dekompilat zugeordnet. Bei `CBMoveEvent`, `CBSetupEvent`, `CBScrollRefresh` und `CBTabDeleteEvent` stützt sich die Zuordnung auf die Registrierungsreihenfolge und die Größe; ihre Rümpfe sind sehr kurz und wurden nur grob gelesen:

| Callback | Adresse | Befund |
|---|---|---|
| `CBResizeEvent` | `0x005FB130` | Mindestgröße **200** (`MIN_CHAT_SIZE_X/Y`), setzt das Speicher-Flag (`+0x1C0`) |
| `CBMoveEvent` | `0x005FB1F0` | verschiebt das Fenster |
| `CBSetupEvent` | `0x005FB270` | öffnet das Einstellungsmenü |
| `CBScrollRefresh` | `0x005FB110` | aktualisiert das Fenster |
| `CBTabEditEvent` | `0x005FB290` | merkt Fenster (`+0x1F8`) und Tab (`+0x1FC`), wirft `TabOptionEdit_OpenUI` (`+0x210`) |
| `CBAddTab` | `0x005FB2F0` | Tab-Zeiger 0, wirft `TabOptionAdd_OpenUI` (`+0x20C`) |
| `CBTabDeleteEvent` | `0x005FBF50` | löscht den Tab |
| `CBDragCallback` | `0x005FB8A0` | trennt ein Fenster ab, wenn der Abstand **> 30** (`DRAG_START_DISTANCE`) ist und mehrere Tabs vorhanden sind; kopiert es mit `_CopyUIChatMessage` |
| `CBDockingCallback` | `0x005FBAD0` | wählt das nächste andockbare Fenster, Ereignisdauer **300 ms** (Kombinieren) |
| `CBDockingPreEvent` | `0x005FBBE0` | färbt das Zielfenster ein |

`_DockingPreEventStart` (`0x0070CBD0`) setzt die Fensterfarbe auf `0x500000FF` (blau), `_DockingPreEventEnd` (`0x0070CC00`) auf `0x50000000`; beide Konstanten wurden im Maschinencode gelesen und stimmen mit der Quelle überein.

## Leerlauf (ChatIdle, 0x0070F6A0)

Größte Funktion der Klasse (1937 Byte). Sie erzeugt Docking-Ereignisse zum Ein- und Ausblenden (Dauer **500 ms**) und zur Trennung von Tabs (500 ms) und führt das Kombinieren (300 ms, aus `CBDockingCallback`) aus. Die Zeiten stimmen mit der Quelle überein.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Konfigurationsfunktionen (`LoadBaseFile`, `SaveChatFile`, `_LoadChatSetting`, `_DefaultChatSetting`) und viele kleine Listenfunktionen sind nicht zugeordnet; sie bestehen überwiegend aus STL-Code ohne eindeutige Anker.
- `ChatIdle` wurde nur nach Größe, Aufrufen und Zeitkonstanten zugeordnet, nicht Zeile für Zeile verglichen.
- Weitere Klassen des Verzeichnisses (`AgcUIChatMessage`, [`AgcChatMessage`](AgcChatMessage.md), `CChattingInputController`, `CSystemMsgManager`, `CTextFilter`) sind nicht abgeglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 1, nicht im Client: 3, ohne Kandidat: 11, zugeordnet: 8.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `_ItemEvent` | 20 | `0x0070C7B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ParseMessageText` | 22 | `0x0070C920` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_AddOptionTab` | 13 | `0x0070CE90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `HideChatUI` | 16 | `0x0070E220` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadBaseFile` | 93 | `0x0070ECF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ShowChatUI` | 19 | `0x0070CC30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_WhisperEvent` | 27 | `0x0070C9C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_MapPosEvent` | 16 | `0x0070C820` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SaveChatFile` (`0x0070D8E0`), `_LoadChatSetting` (`0x0070F210`), `_DefaultChatSetting` (`0x0070F210`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcChatMessage`](AgcChatMessage.md), [`AgcUIChatMessage`](AgcUIChatMessage.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
- **Erwähnt in:** [`AgcUIChatMessage`](AgcUIChatMessage.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`CSystemMsgManager`](CSystemMsgManager.md)
