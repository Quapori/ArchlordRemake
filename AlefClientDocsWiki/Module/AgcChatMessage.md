# AgcChatMessage (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `AgcChatMessage` (Nachrichtenspeicher je Nachrichtenart, Textzerlegung) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `AgcChatMessage.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 11 von 21 Quellmethoden sind zugeordnet; neu sind `AddMessage`, `RefreshMessageEntry`, `SetTextFormat`, `SetFontType`, `_PushAndParseString` und die Hilfen darum.
- **Klickfarben:** drei Ereignisarten mit festen Farbwerten, identisch zur Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcChatMessage.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Initialize` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 1 | `Clear` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `SliceLineByWord` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 3 | `AddMessage` | `0x007A3080` | 523 | ver |
| 4 | `GetMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 5 | `GetMessageCount` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `ClearMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 7 | `RefreshMessageEntry` | `0x007A3290` | 786 | ver |
| 8 | `SetTextFormat` | `0x007A1FD0` | 380 | ver |
| 9 | `GetTextFormat` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `_StringCombination` | `0x007A0450` | 174 | ver |
| 11 | `_PushAndParseString` | `0x007A25D0` | 2489 | ver |
| 12 | `PushNewMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 13 | `PopNewMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `_CalcEventType` | `0x007A0500` | 1055 | Zeichenkette |
| 15 | `_AddClickAction` | `0x007A0920` | 171 | ver |
| 16 | `_OverFlowMessageDelete` | `0x007A2200` | 556 | ver |
| 17 | `_ClearEntryMessage` | `0x007A2430` | 284 | ver |
| 18 | `ClearOriginalMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `SetFontType` | `0x007A35B0` | 22 | ver |
| 20 | `_HexStringToDWORD` | `0x007A09D0` | 160 | ver |

11 von 21 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x8` | `Nachrichtenart (Bit, `m_unMessageType`)` | `AddMessage` |

## Umfang

`AgcChatMessage` hält die Nachrichten einer Nachrichtenart (`AgcChatMessage.cpp`, 21 Methoden); im Binary bei `0x0079FA00`–`0x007A3600`, gemischt mit `CSystemMsgManager` und STL-Code.

## Nachricht aufnehmen (AddMessage, 0x007A3080)

Ablauf wie in der Quelle: Puffer von 520 Byte (`MAX_PATH*2`) leeren, Textformat der Art holen, `_StringCombination` (`0x007A0450`, vier `sprintf_s`-Varianten je nach Kopftext/Absender), Farbe (eigene, sonst die des Formats), `_PushAndParseString` (`0x007A25D0`), Originalnachricht in der Warteschlange ablegen, dann `_OverFlowMessageDelete` (`0x007A2200`).
`_PushAndParseString` ist mit 2489 Byte die größte Funktion der Klasse, ruft sich selbst auf und nutzt `_CalcEventType` (`0x007A0500`) und `_AddClickAction`.

## Klickbare Textteile

`_AddClickAction` (`0x007A0920`) macht Textteile zu Schaltflächen mit dem Manager-Callback `CBEventCallback` (`0x005FBCE0`). Die Farben im Binary stimmen mit der Quelle überein:

| Ereignis | Hintergrund | Linie |
|---|---|---|
| Gegenstand | `0x400D4EF9` | `0x400D4EF9` |
| Kartenposition | `0x40E43251` | `0x40E43251` |
| Flüstern | `0x406084D7` | `0xEE6084D7` |

`_HexStringToDWORD` (`0x007A09D0`) wandelt Hex-Zeichenfolgen (`0-9`, `A-F`, `a-f`) in Zahlen um.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `_PushAndParseString` (244 Quellzeilen) wurde nur nach Aufrufern, Größe und Aufgerufenen zugeordnet, nicht verglichen.
- Die kleinen Zugriffe (`GetMessage`, `GetMessageCount`, `GetTextFormat`, `Push/PopNewMessage`) sind im Binary eingebaut oder STL-Aufrufe und nicht als eigene Funktionen zugeordnet; `ClearMessage` und `Clear` sind vermutlich im Destruktor (`0x007A2F90`) aufgegangen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 6, ohne Kandidat: 2, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SliceLineByWord` | 22 | `0x007A0100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetTextFormat` (`0x007A1550`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIChatting2`](AgcmUIChatting2.md)
- **Erwähnt in:** [`AgcChatManager`](AgcChatManager.md), [`AgcUIChatMessage`](AgcUIChatMessage.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgcmUINotice`](AgcmUINotice.md)
