# AgcmUINPCTrade (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Teilbericht zu `AgcmUINPCTrade.cpp` (NPC-Handelsfenster) der Klasse [`AgcmUIItem`](AgcmUIItem.md) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Offsets, EP8-Quelle `Modules/AClient/AgcmUIItem/AgcmUINPCTrade.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 32 von 36 Quellmethoden sind einer Adresse zugeordnet; in diesem Durchgang kamen die beiden Fassungen von `CBNPCTradeUIOpen`, die erste Fassung von `CBUINPCTradeMSGConfirmBuy` (`0x0078A220`), beide `OnCheckUseEnable` und `CBUINPCTradeMSGConfirmBuyStackCountCancel` (gemeinsamer Rumpf) hinzu.
- **Preis:** NPC-Preis × Anzahl + Steuer; doppelter Preis für Mörder; Reittiere ab Mörder-Stufe 2 gesperrt.
- **Hinweis:** `AgcmUIEventNPCTrade` existiert nicht; die Oberfläche ist `AgcmUINPCTrade.cpp` in `AgcmUIItem`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUINPCTrade.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `CBNPCTradeUIOpen` | `0x007894C0` | 137 | von Hand geprüft |
| 1 | `CBNPCTradeMoveItem` | `0x00789550` | 163 | von Hand geprüft |
| 2 | `CBNPCTradeUIOpen` | `0x00789600` | 157 | von Hand geprüft |
| 3 | `CBNPCTradeUIClose` | `0x007896A0` | 161 | von Hand geprüft |
| 4 | `CBNPCTradeOpenNextLayer` | `0x00789750` | 152 | von Hand geprüft |
| 5 | `CBNPCTradeOpenPrevLayer` | `0x007897F0` | 87 | von Hand geprüft |
| 6 | `CBNPCTradeInitLayer` | `0x00789850` | 63 | von Hand geprüft |
| 7 | `CBUINPCTradeMSGFullInven` | `0x00789890` | 32 | von Hand geprüft |
| 8 | `CBUINPCTradeMSGConfirmBuy` | `0x0078A220` | 257 | von Hand geprüft |
| 9 | `CBUINPCTradeMSGConfirmBuy` | `0x007898B0` | 140 | von Hand geprüft |
| 10 | `CBUINPCTradeMSGConfirmBuyStackCountOK` | `0x00789940` | 223 | von Hand geprüft |
| 11 | `CBUINPCTradeMSGConfirmBuyStackCountCancel` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 12 | `CBUINPCTradeMSGConfirmSell` | – | | nicht zugeordnet (klein, eingebaut oder vermutlich entfernt) |
| 13 | `CBUINPCTradeMSGConfirmSell` | `0x00789A20` | 266 | von Hand geprüft |
| 14 | `CBUINPCTradeMSGNotEnoughGhelld` | `0x00789B30` | 32 | von Hand geprüft |
| 15 | `CBUINPCTradeMSGNotEnoughCharisma` | `0x00789B50` | 39 | von Hand geprüft |
| 16 | `CBUINPCTradeMSGNotEnoughShrineCoin` | `0x00789B80` | 39 | von Hand geprüft |
| 17 | `CBUINPCTradeMSGNotEnoughSpaceToGetGhelld` | `0x00789BB0` | 32 | von Hand geprüft |
| 18 | `SelfUpdatePositionCB` | `0x00789BD0` | 253 | von Hand geprüft |
| 19 | `CBBuyItemDirect` | `0x0078A330` | 131 | von Hand geprüft |
| 20 | `CBNPCTradeSuccess` | `0x00789CD0` | 39 | von Hand geprüft |
| 21 | `CBSplitItemNPCTrade` | – | | nicht zugeordnet (klein, eingebaut oder vermutlich entfernt) |
| 22 | `CBNPCTradeDeleteGrid` | `0x00789D00` | 69 | von Hand geprüft |
| 23 | `OnOpenMsgBoxConfirmBuyNPCTradeItem` | – | | nicht zugeordnet (klein, eingebaut oder vermutlich entfernt) |
| 24 | `OnSendBuyNPCTradeItem` | – | | nicht zugeordnet (klein, eingebaut oder vermutlich entfernt) |
| 25 | `OnCheckEquipEnable` | `0x0078A3C0` | 86 | von Hand geprüft |
| 26 | `OnCheckUseEnable` | `0x0078A420` | 75 | von Hand geprüft |
| 27 | `OnCheckUseEnable` | `0x0078A470` | 84 | von Hand geprüft |
| 28 | `GetPriceNPCTradeItem` | `0x00789D50` | 226 | von Hand geprüft |
| 29 | `IsHaveMurdererLevel` | `0x0078A040` | 93 | von Hand geprüft |
| 30 | `GetMurdererLevel` | `0x00789E40` | 67 | von Hand geprüft |
| 31 | `_CheckEnableNPCTradeItem` | `0x00789E90` | 166 | von Hand geprüft |
| 32 | `_CheckIsMurderer` | `0x00789F40` | 85 | von Hand geprüft |
| 33 | `_MakeConfirmMsgBuyNPCTradeItem` | `0x0078A0A0` | 369 | von Hand geprüft |
| 34 | `_CalcItemPriceByMurdererLevel` | `0x00789FA0` | 78 | von Hand geprüft |
| 35 | `_NoticeBySystemMessage` | `0x00789FF0` | 76 | von Hand geprüft |

32 von 36 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x4E84` | `ID des zu verkaufenden Gegenstands` | `CBUINPCTradeMSGConfirmSell` |
| `0x4E88` | `ID des zu kaufenden Gegenstands` | `CBUINPCTradeMSGConfirmBuy`, `_CheckEnableNPCTradeItem` |
| `0x4E8C` | `Zielstatus des Kaufs` | `CBUINPCTradeMSGConfirmBuy` |
| `0x4E90 / 0x4E94 / 0x4E98` | `Zielebene / -zeile / -spalte des Kaufs` | `CBBuyItemDirect` |
| `0x4F1C` | `Flag „NPC-Handelsfenster offen“` | `CBBuyItemDirect` |
| `0x4FAC` | `Ereignis „Kaufbestätigung“` | `CBUINPCTradeMSGConfirmBuy` |

## Umfang

`AgcmUINPCTrade.cpp` enthält 36 Methoden der Klasse `AgcmUIItem` (NPC-Handelsfenster: Kaufen, Verkaufen, Preis). Eine eigene Klasse `AgcmUIEventNPCTrade` gibt es weder in der Quelle noch im Binary; die Netzwerkseite (`SendBuy`, `SendSell`) steht im Modul `AgcmEventNPCTrade` ([NPC_Trade_Dialog](NPC_Trade_Dialog.md)). Alle Funktionen sind auch im Bericht [AgcmUIItem](AgcmUIItem.md) enthalten; dieser Teilbericht ergänzt die bisher offenen Zuordnungen.

## Öffnen (zwei Überladungen CBNPCTradeUIOpen)

Die Quelle hat zwei Fassungen: das Modul-Callback (`pData, pClass, pCustData`, `0x007894C0`: öffnet das Handelsfenster, falls noch zu, merkt die Position, öffnet das Inventar und wirft `NPCTrade_InitLayer`) und die UI-Funktion (`0x00789600`: stoppt erst den Self-Character, öffnet dasselbe und aktualisiert dann die Benutzerdaten des Handelsgitters). Beide sind über ihre Aufrufe unterschieden (`StopCharacter` nur in der zweiten, Ereignis `InitLayer` nur in der ersten).

## Kaufbestätigung

Die Quelle hat zwei Fassungen von `CBUINPCTradeMSGConfirmBuy`: Die erste (`pData, pClass, pCustData`, `0x0078A220`, in `_AREA_GLOBAL_` verwendet) prüft `_CheckEnableNPCTradeItem`, baut die Bestätigungsfrage (`_MakeConfirmMsgBuyNPCTradeItem`, `0x0078A0A0`) und wirft das Ereignis „Kaufbestätigung“ (`+0x4FAC`); sie wird von `CBBuyItemDirect` (`0x0078A330`), den Inventar-Verschiebe-Callbacks und `CBChargingInventoryAMoveItem` aufgerufen. Die zweite (`pClass, lTrueCancel, Text`, `0x007898B0`) sendet bei „Ja“ die Kaufanfrage (`AgcmEventNPCTrade::SendBuy`, `0x006DCFE0`) mit Gegenstand, Zahl, Zielstatus und Position und setzt den Zielstatus zurück (−1).
`OnOpenMsgBoxConfirmBuyNPCTradeItem` und `OnSendBuyNPCTradeItem` (jeweils nur Hilfen mit denselben Aufrufen) sind im Binary nicht als eigene Funktionen zu finden.

## Verkaufen

`CBUINPCTradeMSGConfirmSell` (`0x00789A20`, 266 Byte) ist die lange Fassung der Quelle (Prüfung des Gegenstands, Meldungen, `AgcmEventNPCTrade::SendSell`, `0x006DD170`). Die kurze Fassung, die nur das Ereignis wirft, ist nicht als eigene Funktion zu finden; `CBSplitItemNPCTrade` (sendet Verkauf für geteilte Stapel) ebenfalls nicht. `SendSell` hat im Binary nur einen Aufrufer.

## Preis und Mörder-Regeln

`GetPriceNPCTradeItem` (`0x00789D50`): NPC-Preis × Anzahl (abgerundet), dazu der Steuersatz des Charakters in Prozent des Betrags. `_CalcItemPriceByMurdererLevel` (`0x00789FA0`) verdoppelt den Preis für Charaktere mit Mörder-Level (nur wenn der Parameter gesetzt ist). Beides entspricht der Quelle.
`_CheckEnableNPCTradeItem` (`0x00789E90`): Bei Mörder-Punkten 60 oder 100 (Stufe 2 und 3) ist der Kauf von Reittieren (Ausrüstungsart `0x20` = `AGPMITEM_EQUIP_KIND_RIDE`) gesperrt; es erscheint der UI-Text `Alert_NPCTrade_MurdererRejectBuyItem`. Bei Stufe 1 (40) und darunter ist alles erlaubt. Das stimmt mit der Quelle überein.
`OnCheckUseEnable` hat zwei Überladungen: `0x0078A420` (nur Gegenstand: Teleport-Schriftrollen sind ab Mörder-Stufe 2 gesperrt, Meldung `Alert_CannotUseContents_ByMurderer`) und `0x0078A470` (mit Charakter: nur für den eigenen Charakter prüfen, sonst erlaubt). `OnCheckEquipEnable` (`0x0078A3C0`) nutzt dieselben Hilfen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`GetPriceNPCTradeItem`, `_CalcItemPriceByMurdererLevel`, `_CheckEnableNPCTradeItem`, `CBUINPCTradeMSGConfirmBuy`).

## Grenzen

- Die erste Fassung von `CBUINPCTradeMSGConfirmSell`, `CBSplitItemNPCTrade`, `OnOpenMsgBoxConfirmBuyNPCTradeItem` und `OnSendBuyNPCTradeItem` sind im Binary nicht als eigene Funktionen zu finden.
- Die Zuordnung der Überladungen stützt sich auf Aufrufe und Aufrufer; sie wurde nicht Byte für Byte geprüft.

## Querverweise

- **Erwähnt Module:** [`AgcmUIItem`](AgcmUIItem.md)
- **Erwähnt in:** [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md)
