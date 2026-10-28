# AgcmUIShrineShop (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIShrineShop` (Schrein-Shop: Kaufbestätigung mit Charisma, Schreinmünzen und Ghelld) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIShrineShop/AgcmUIShrineShop.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 17 von 17 Quellmethoden sind zugeordnet; neu sind `SetBuyItem` und `ItemBuy`.
- **UI:** 3 Funktionen, 9 Anzeigen, 1 Benutzerdatum, 1 Ereignis – wie in der Quelle.
- **Querprüfung:** Die Offsets in `AgcmUIItem` (`+0x4E88`…`+0x4E98`) sind dieselben wie im NPC-Handel (Bericht [AgcmUINPCTrade](AgcmUINPCTrade.md)).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIShrineShop.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x00677870` | 797 | vtable/String |
| 1 | `CBOpenBuyConfirmUI` | `0x00677770` | 180 | UI-Registrierung |
| 2 | `CBCloseBuyConfirmUI` | `0x00677060` | 25 | UI-Registrierung |
| 3 | `CBItemBuyClick` | `0x00677830` | 60 | UI-Registrierung |
| 4 | `CBItemName` | `0x00677080` | 57 | UI-Registrierung |
| 5 | `CBItemCount` | `0x006770C0` | 63 | UI-Registrierung |
| 6 | `CBItemImage` | `0x00677100` | 183 | UI-Registrierung |
| 7 | `CBItemCharismaPrice` | `0x006771C0` | 86 | UI-Registrierung |
| 8 | `CBItemShrineCoinPrice` | `0x00677220` | 36 | UI-Registrierung |
| 9 | `CBItemGheldPrice` | `0x00677280` | 153 | UI-Registrierung |
| 10 | `CBItemCharismaRest` | `0x00677320` | 187 | UI-Registrierung |
| 11 | `CBItemShrineCoinRest` | `0x006773E0` | 187 | UI-Registrierung |
| 12 | `CBItemGheldRest` | `0x006774A0` | 232 | UI-Registrierung |
| 13 | `SetBuyItem` | `0x00677590` | 101 | ver |
| 14 | `ItemBuy` | `0x00677600` | 127 | ver |
| 15 | `UserInputMessageProc` | `0x00677680` | 114 | vtable/String |
| 16 | `CBKeydownESC` | `0x00677700` | 49 | Callback-Registrierung |

17 von 17 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIShrineShop` (`0x00676FB0`), `~AgcmUIShrineShop` (`0x00677740`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBC0` | `gewählter Gegenstand (`m_pcsSelectItem`)` | `SetBuyItem`, `ItemBuy` |
| `0xBC4…0xBD0` | `Zielstatus / Ebene / Zeile / Spalte des Kaufs` | `SetBuyItem`, `ItemBuy` |
| `0xBD4` | `Flag „Kaufdialog offen“` | `CBOpenBuyConfirmUI`, `UserInputMessageProc` |
| `0xBBC` | `Ereignis „Bestätigung schließen“` | `CBItemBuyClick` |

## Vtable

Vtable bei `0x008CA534`: Slot 0 Destruktor `0x00677740`, 2 `OnInit` (`0x00677870`), 1/6/7 `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnAddModule`, `OnDestroy`).

## Registrierung (OnInit, 0x00677870)

Holt [`AgcmUIManager2`](AgcmUIManager2.md), `AgcmCharacter`, [`AgpmItem`](AgpmItem.md), [`AgcmItem`](AgcmItem.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgcmUIItem`](AgcmUIItem.md), `AgcmEventNPCTrade` und [`AgcmUIMain`](AgcmUIMain.md), meldet `CBKeydownESC` an und legt an: Benutzerdaten `Shrine_ComfirmUI_Refresh`, Ereignis `Shrine_ItemBuyConfirmClose_Event2`, Funktionen `Shrine_ItemBuyComfirmUI_Open`, `…_Close` und `Shrine_ItemBuyClick` sowie neun Anzeigen (`Shrine_Item…_Display`: Name, Bild, Anzahl, Preis in Charisma/Schreinmünzen/Ghelld und Rest davon). Reihenfolge und Zahl wie in der Quelle.

## Kauf (SetBuyItem / ItemBuy)

`CBOpenBuyConfirmUI` (`0x00677770`) ruft `SetBuyItem` (`0x00677590`): Es übernimmt von `AgcmUIItem` die zu kaufende Gegenstands-ID (`+0x4E88`) sowie Zielstatus, Ebene, Zeile und Spalte (`+0x4E8C`…`+0x4E98`) und sucht den Gegenstand (`AgpmItem::GetItem`); erst bei Erfolg wird das Bestätigungsfenster geöffnet und mittig auf dem Bildschirm platziert.
`ItemBuy` (`0x00677600`) sendet die Kaufanfrage (`AgcmEventNPCTrade::SendBuy`, `0x006DCFE0`) mit Charakter-ID, Gegenstand, Anzahl, Status, Ebene, Zeile und Spalte und setzt danach den Gegenstandszeiger auf 0 und die vier Zielwerte auf −1. `CBItemBuyClick` (`0x00677830`) schließt zuerst das Bestätigungsfenster und kauft dann.
`UserInputMessageProc` (`0x00677680`) löst denselben Kauf auf Eingabe-, Zahlenblock-Eingabe- oder Leertaste aus, wenn das Fenster offen ist (Ereignis „Taste gedrückt“ = `0x18`; Tasten `0xAB`, `0xA6`, `0x20`).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00677870`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `Shrine_ComfirmUI_Refresh` | 0 | – |

**Ereignis** (1)

| Name | Id | Handler |
|---|---:|---|
| `Shrine_ItemBuyConfirmClose_Event2` | 0 | – |

**Funktion** (3)

| Name | Id | Handler |
|---|---:|---|
| `Shrine_ItemBuyComfirmUI_Open` |  | – |
| `Shrine_ItemBuyComfirmUI_Close` |  | – |
| `Shrine_ItemBuyClick` |  | – |

**Anzeige** (9)

| Name | Id | Handler |
|---|---:|---|
| `Shrine_ItemName_Display` | 0 | – |
| `Shrine_ItemImage_Display` | 0 | – |
| `Shrine_ItemCount_Display` | 0 | – |
| `Shrine_ItemCharismaPrice_Display` | 0 | – |
| `Shrine_ItemShrineCoinPrice_Display` | 0 | – |
| `Shrine_ItemGheldPrice_Display` | 0 | – |
| `Shrine_ItemCharismaRest_Display` | 0 | – |
| `Shrine_ItemShrineCoinRest_Display` | 0 | – |
| `Shrine_ItemGheldRest_Display` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Anzeigefunktionen (`CBItemName`, `CBItemImage`, Preise und Reste) waren bereits zugeordnet und wurden hier nicht einzeln gelesen.

## Querverweise

- **Erwähnt Module:** [`AgcmItem`](AgcmItem.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUINPCTrade`](AgcmUINPCTrade.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md)
