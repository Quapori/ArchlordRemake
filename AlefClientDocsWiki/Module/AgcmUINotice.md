# AgcmUINotice (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUINotice` (Lauftext-Meldungen am Bildschirm) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUINotice/AgcmUINotice.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 12 Quellmethoden sind zugeordnet; neu sind `AddMessage`, `RefreshMessage`, `_RefreshPosition`, `_ClearChildWindow`, `_ParseMessage`; `OnAddModule` und `_HexStringToDWORD` stehen als zusammengefaltete Rümpfe.
- **Zeiten:** 5000 ms bis zum Ausblenden, 8000 ms Lebensdauer, höchstens fünf Meldungen gleichzeitig.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUINotice.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x00676C60` | 845 | vtable/String |
| 1 | `OnAddModule` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnIdle` | `0x006769E0` | 525 | vtable/String |
| 3 | `DBG_Message` | `0x00676BF0` | 103 | as-register |
| 4 | `OnDestroy` | `0x00675FC0` | 67 | vtable/String |
| 5 | `AddMessage` | `0x006768B0` | 289 | ver |
| 6 | `RefreshMessage` | `0x00676840` | 98 | ver |
| 7 | `_RefreshPosition` | `0x00676010` | 102 | ver |
| 8 | `_ClearChildWindow` | `0x00676080` | 49 | ver |
| 9 | `_ParseMessage` | `0x00676240` | 954 | ver |
| 10 | `_HexStringToDWORD` | `0x007A09D0` | 160 | gleiche Adresse wie [`AgcChatMessage`](AgcChatMessage.md):_HexStringToDWORD` (vom Linker zusammengefaltet) |
| 11 | `NoticeMacro` | `0x00676600` | 529 | Zeichenkette |

12 von 12 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006760c0` (`0x006760C0`), `ctor_or_dtor_00676190` (`0x00676190`), `~AgcmUINotice` (`0x00676820`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98` | `Liste der Meldungen (`m_listOriginal`)` | `OnIdle` |
| `0xBC8` | `Zeiger auf [`AgcmUIChatting2`](AgcmUIChatting2.md)` | `_ParseMessage` |

## Vtable

Die Vtable steht bei `0x008CA414`: Slot 0 Destruktor `0x00676820`, 1 und 6 `return TRUE`-Rumpf `0x0067AC90` (u. a. die leere `OnAddModule` der Quelle), 2 `OnInit` (`0x00676C60`), 3 `OnIdle` (`0x006769E0`), 7 `OnDestroy` (`0x00675FC0`).

## Meldungen (AddMessage, 0x006768B0)

Legt je Meldung ein Objekt mit Text, Startzeit (Uhr) und Alpha 1.0 an und hängt es an die Liste. Wird die Liste länger als fünf Einträge, fliegt der älteste heraus (`MAX_NOTICE_MESSAGE_VIEW` = 5). Danach `RefreshMessage` (`0x00676840`): `_RefreshPosition` (`0x00676010`, Fenster nach Bildschirmgröße platzieren), `_ClearChildWindow` (`0x00676080`) und je Meldung `_ParseMessage` (`0x00676240`, zerlegt den Text anhand von Markierungen wie `<H…>`; die Hexfarbe wird mit `_HexStringToDWORD` umgerechnet, das im Binary mit der gleichnamigen Funktion von `AgcChatMessage` bei `0x007A09D0` zusammengefaltet ist).

## Lebensdauer (OnIdle, 0x006769E0)

Meldungen blenden nach 5000 ms aus und verschwinden nach 8000 ms (`NOTICE_MESSAGE_LIFE_TIME` 8000, Ausblendzeit 3000), im Binary als `+5000` und `+8000` sichtbar. Außerdem verarbeitet `OnIdle` die Makro-Liste (`NoticeMacro`, `0x00676600`), die Meldungen aus einer XML-Datei mit `INTERVAL`-Attributen zeitversetzt abspielt.

## Aufrufer

`AddMessage` nutzen u. a. `CSystemMsgManager::NoticeMessage` (Operation 4), `CallBack_OnNoticeMessage` und `OnAddMessage` der Chat-Verwaltung.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`AddMessage`, Zeiten in `OnIdle`).

## Grenzen

- `_ParseMessage` (78 Quellzeilen) wurde nur über Aufrufer, Größe und die Markierung `<H` zugeordnet, nicht verglichen.
- Die Zuordnung von `_HexStringToDWORD` zu `0x007A09D0` beruht auf demselben Muster der Quelle (gleiche Hex-Umrechnung), nicht auf einer Bytefolgen-Prüfung.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcChatMessage`](AgcChatMessage.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
- **Erwähnt in:** [`AgcmUIQuest2`](AgcmUIQuest2.md), [`CSystemMsgManager`](CSystemMsgManager.md)
