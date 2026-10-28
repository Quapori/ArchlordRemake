# AgcmUIChatting2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIChatting2` (Chat-Oberfläche: Eingabe, Flüstern, Chat-Dateien) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIChatting2/AgcmUIChatting2.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 14 Quellmethoden der Klasse sind zugeordnet; neu sind `OnInit`, `OnIdle`, `OnDestroy`, `OnSendMessage` und `SetLastWhisper`, über die Vtable und das Dekompilat.
- **Chat senden:** höchstens 128 Zeichen pro Nachricht, Filter vor dem Senden.
- **UI:** fünf Funktionen, keine Anzeigen und keine Boolean-Werte (wie in der Quelle).
- **Abweichungen:** keine festgestellt.
- **Weitere Klassen:** [`AgcChatManager`](AgcChatManager.md), `CChatCmd` und [`AcUIChattingEdit`](AcUIChattingEdit.md) haben eigene Berichte (siehe „Umfang“).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIChatting2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x005BE400` | 48 | ver |
| 1 | `OnIdle` | `0x005BE430` | 24 | ver |
| 2 | `OnDestroy` | `0x005BE450` | 17 | ver |
| 3 | `OnAddModule` | `0x005BEB50` | 297 | Zeichenkette |
| 4 | `OnSendMessage` | `0x005BE470` | 335 | ver |
| 5 | `IsEnableSendAreaChatting` | – | | nicht zugeordnet (klein, im Aufrufer eingebaut oder ohne eindeutigen Anker) |
| 6 | `UpdateTimeLastSendAreaMsg` | – | | nicht zugeordnet (klein, im Aufrufer eingebaut oder ohne eindeutigen Anker) |
| 7 | `CBSetSelfCharacter` | `0x005BE5C0` | 348 | Zeichenkette |
| 8 | `CBActiveChatInput` | `0x005BE720` | 37 | UI-Registrierung |
| 9 | `CBCheckNCloseInput` | `0x005BE750` | 179 | UI-Registrierung |
| 10 | `CBClickSyncPosBtn` | `0x005BE810` | 229 | UI-Registrierung |
| 11 | `CBClickEscapeConfirmOk` | `0x005BE900` | 222 | UI-Registrierung |
| 12 | `CBSendWhisper` | `0x005BE9E0` | 178 | UI-Registrierung |
| 13 | `SetLastWhisper` | `0x005BEAA0` | 48 | ver |

12 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_005be230` (`0x005BE230`), `ctor_or_dtor_005be340` (`0x005BE340`), `~AgcmUIChatting2` (`0x005BEB10`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBD4` | `Zeiger auf den Befehlsparser (Vtable-Aufruf `+0xC` in `OnSendMessage`)` | `OnSendMessage` |

## Umfang

Analysiert ist nur die Klasse `AgcmUIChatting2` selbst (`AgcmUIChatting2.cpp`, 277 Zeilen, 14 Methoden). Im selben Quellverzeichnis liegen weitere Klassen. Drei davon haben eigene Berichte: [AgcChatManager](AgcChatManager.md), [CChatCmd](CChatCmd.md) (Datei `CChattingCommander.cpp`) und [AcUIChattingEdit](AcUIChattingEdit.md). Nicht abgeglichen sind `AgcUIChatMessage`, `AgcChatMessage`, `CChattingInputController`, `CSystemMsgManager`, `CTextFilter` u. a.

## Vtable

Die Hauptvtable steht bei `0x008BB514`. Zuordnung der Slots:

| Slot | Adresse | Funktion |
|---:|---|---|
| 1 | `0x005BEB50` | `OnAddModule` |
| 2 | `0x005BE400` | `OnInit` (ruft vier Funktionen der Chat-Klassen auf) |
| 3 | `0x005BE430` | `OnIdle` (ruft `ChatIdle`) |
| 7 | `0x005BE450` | `OnDestroy` (ruft `OnDestroyEditChatting`) |

Die Mehrfachvererbung erzeugt weitere Vtables (`0x008BB4D4`–`0x008BB508`) für die Chat-Basisklassen.

## Nachricht senden (OnSendMessage, 0x005BE470)

Bricht ab bei leerem Text oder Länge ≤ 0 und ohne `AgcmCharacter`, [`AgpmChatting`](AgpmChatting.md) oder Self-Character. Die Länge wird auf **128** (`0x80`) begrenzt. Mit gesetztem `bParse` läuft der Text zuerst durch den Befehlsparser der Chat-Klasse (Vtable-Aufruf `+0xC`); wurde er als Befehl erkannt, wird nichts gesendet. Danach folgen `OnFiltering` (`0x00609070`) und `AgpmChatting::MakePacketChatting` (`0x0056E480`), das Ziel (Name) nur für Typ 5 (Flüstern). Bei Typ 5 und 6 mit Zielname wird der Name als Antwortziel gemerkt. Das entspricht der Quelle.

## Callback- und UI-Registrierung in OnAddModule (0x005BEB50)

Die Reihenfolge entspricht der Quelle: `SetCallbackSetSelfCharacter` (`CBSetSelfCharacter`), danach fünf UI-Funktionen `Chat_CheckNCloseInput` (5 Parameter, „Edit Control“), `Chat_SendWhisper`, `Chat_Active_Input`, `SyncPosBtn_Click`, `EscapeConfirmOk_Click`. Zwei Hilfsaufrufe (`OnAddCustomControl`, `OnReadyBGMTitle`) stehen davor.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x005BEB50`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (5)

| Name | Id | Handler |
|---|---:|---|
| `Chat_CheckNCloseInput` |  | `CBCheckNCloseInput` |
| `Chat_SendWhisper` |  | `CBSendWhisper` |
| `Chat_Active_Input` |  | `CBActiveChatInput` |
| `SyncPosBtn_Click` |  | `CBClickSyncPosBtn` |
| `EscapeConfirmOk_Click` |  | `CBClickEscapeConfirmOk` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, `OnSendMessage`, Vtable).

## Grenzen

- `IsEnableSendAreaChatting` und `UpdateTimeLastSendAreaMsg` (je 4–5 Zeilen, 5000 ms Sperre) sind im Binary nicht als eigene Funktionen zu finden; sie sind offenbar in die Aufrufer eingebaut.
- `SetLastWhisper` (`0x005BEAA0`) enthält `SetAutoReplyWhisperTarget` bereits eingebaut.
- Die übrigen Klassen des Verzeichnisses ([`AgcUIChatMessage`](AgcUIChatMessage.md), [`AgcChatMessage`](AgcChatMessage.md) u. a.) wurden nicht untersucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AcUIChattingEdit`](AcUIChattingEdit.md), [`AgcChatManager`](AgcChatManager.md), [`AgcChatMessage`](AgcChatMessage.md), [`AgcUIChatMessage`](AgcUIChatMessage.md), [`AgpmChatting`](AgpmChatting.md)
- **Erwähnt in:** [`AcUIChattingEdit`](AcUIChattingEdit.md), [`AgcChatManager`](AgcChatManager.md), [`AgcChatMessage`](AgcChatMessage.md), [`AgcUIChatMessage`](AgcUIChatMessage.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmUICustomizing`](AgcmUICustomizing.md), [`AgcmUINotice`](AgcmUINotice.md), [`CBGMTitleViewer`](CBGMTitleViewer.md), [`CChatCmd`](CChatCmd.md), [`CChattingInputController`](CChattingInputController.md), [`COptionFlagController`](COptionFlagController.md), [`CSystemMsgManager`](CSystemMsgManager.md), [`CTextFilter`](CTextFilter.md)
