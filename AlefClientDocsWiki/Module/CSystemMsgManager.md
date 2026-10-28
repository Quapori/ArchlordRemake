# CSystemMsgManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `CSystemMsgManager` (Systemmeldungen des Servers) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `CSystemMsgManager.cpp` (Datei `CSystemMsgManager.cpp`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 12 Quellmethoden sind zugeordnet; die Empfangskette, die Dialog-/Hinweis-Funktionen und die XML-Einträge wurden über die Aufrufer neu zugeordnet.
- **Operationen:** 0 Chat, 1 Dialog modal, 2 Dialog nicht modal, 3 nichts, 4 Hinweis – wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CSystemMsgManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnRegisterSystemMsgCallBack` | `0x007A0050` | 62 | Zeichenkette |
| 1 | `OnReceiveSystemMessage` | `0x0079F4A0` | 214 | ver |
| 2 | `OnMsgDlgModal` | `0x0079EFE0` | 72 | ver |
| 3 | `OnMsgDlgModalless` | `0x0079F030` | 72 | ver |
| 4 | `NoticeMessage` | `0x0079F080` | 67 | ver |
| 5 | `_LoadSystemMsgFormat` | `0x0079FF10` | 307 | Zeichenkette |
| 6 | `_AddSystemMessageEntry` | `0x0079FB50` | 912 | von Hand geprüft |
| 7 | `_AddSystemMessageEntry` | `0x0079FA30` | 149 | von Hand geprüft |
| 8 | `_MakeSystemMessage` | `0x0079F1A0` | 678 | ver |
| 9 | `_GetSystemMessageColor` | `0x0079F450` | 77 | ver |
| 10 | `_MakeColorValue` | `0x0079F0D0` | 151 | ver |
| 11 | `CallBack_OnSystemMessage` | `0x0079F590` | 26 | ver |

12 von 12 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0079fad0` (`0x0079FAD0`), `ctor_or_dtor_0079fb40` (`0x0079FB40`), `~CSystemMsgManager` (`0x0079FEE0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Eintrag +0x4C` | `Farbe (`m_dwColor`) im Map-Eintrag` | `_GetSystemMessageColor` |

## Umfang

`CSystemMsgManager` (`CSystemMsgManager.cpp`, 12 Methoden) verarbeitet Systemmeldungen des Servers. Im Binary bei `0x0079F030`–`0x007A0450`, zusammen mit STL-Hilfen der Map `m_mapSystemMsg`.

## Empfang einer Systemmeldung

`CallBack_OnSystemMessage` (`0x0079F590`) wird von [`AgpmSystemMessage`](AgpmSystemMessage.md):SetCallbackSystemMessage` aufgerufen (registriert in `OnRegisterSystemMsgCallBack`, `0x007A0050`, die danach `INI\SystemMsgFormat.xml` lädt). Er ruft `OnReceiveSystemMessage` (`0x0079F4A0`): Text bauen (`_MakeSystemMessage`, `0x0079F1A0`), Farbe holen (`_GetSystemMessageColor`, `0x0079F450`: Eintrag aus der Map, sonst `0xFFFFFFFF`) und nach der Operation verzweigen:

| Operation | Aktion | Adresse |
|---:|---|---|
| 0 | Chat-Systemmeldung ([`AgcChatManager`](AgcChatManager.md):OnAddSystemMessage`) | `0x005FAFF0` |
| 1 | Dialog mit OK, modal (`OnMsgDlgModal`) | `0x0079EFE0` |
| 2 | Dialog mit OK, nicht modal (`OnMsgDlgModalless`) | `0x0079F030` |
| 3 | nichts | – |
| 4 | Hinweis-Fenster (`NoticeMessage` → [`AgcmUINotice`](AgcmUINotice.md)) | `0x0079F080` |

Die Verzweigung ist identisch zur Quelle.

## Format-Datei

`_LoadSystemMsgFormat` (`0x0079FF10`) liest die XML-Datei; jeder Eintrag geht durch `_AddSystemMessageEntry` (`0x0079FB50`, liest den Knoten, fragt mehrere Attribute ab und baut über `_MakeColorValue` die Farbe `0xFF000000 | R<<16 | G<<8 | B`; `0x0079F0D0` enthält drei `atoi`-Aufrufe) und die Einfüge-Variante `_AddSystemMessageEntry` (`0x0079FA30`, trägt in die Map ein).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `_MakeSystemMessage` (82 Quellzeilen, Nachrichten- und Formatmodus mit Parametertypen) wurde nur nach Aufrufer, Größe (678 Byte) und Aufgerufenen zugeordnet, nicht verglichen.
- Die XML-Attribute und ihre Namen in `_AddSystemMessageEntry` wurden nicht ausgelesen.

## Querverweise

- **Erwähnt Module:** [`AgcChatManager`](AgcChatManager.md), [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgcmUINotice`](AgcmUINotice.md), [`AgpmSystemMessage`](AgpmSystemMessage.md)
