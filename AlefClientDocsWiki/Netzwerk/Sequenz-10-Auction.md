# Winsock-Sequenz 10: Auction / Auktionshaus

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei dokumentiert den bisher statisch rekonstruierten Auction-Teil aus `alefclient.exe`. Quellen sind `alefclient.pseudocode.c`, besonders [`AgpmAuction`](../Module/AgpmAuction.md), [`AgcmAuction`](../Module/AgcmAuction.md), [`AgcmUIAuction`](../Module/AgcmUIAuction.md) und die UI-Commands `AC_*`. Es wurde kein Live-Traffic mitgeschnitten; Serverdatenbank-Strukturen sind Inferenz aus Clientpaketen und UI-/Datenfeldern.

## Kurzfazit

- Das eigentliche Auktionsmodul heisst `AgpmAuction` und registriert Modul-ID `0x0b`.
- Das Client-/UI-Modul heisst `AgcmAuction`; die sichtbare UI-Schicht heisst `AgcmUIAuction`.
- `AgcmAuction` sendet mehrere konkrete Client-Ops ueber `AgpmAuction + 0xb9c`:
  - `0x05`
  - `0x06`
  - `0x07`
  - `0x08`
  - `0x0a`
  - `0x0d`
  - `0x0f`
- `AgpmAuction` empfaengt Server-Ops `1..0xf` und verteilt sie in Callbacks.
- Die Auction-UI arbeitet mit 15 sichtbaren Board-Zeilen pro Seite, 10 Page-Buttons, Kategorien, Suchfeld, Itemtemplate-Vorschau, Preis, Menge und Sellername.
- Der Client prueft Kaufpreis gegen lokales Geld, aber der Server muss Kauf, Listing, Cancel und Itemausgabe erneut transaktional validieren.

## Abgrenzung zu Fehlspur `0x15`

In der Naehe der Auction-Funktionen liegen sehr viele Paketfunktionen mit Modul `0x15`. Diese gehoeren nach dem Konstruktor bei `0x005537...` zu [`AgpmGuild`](../Module/AgpmGuild.md), nicht zu Auction:

```text
strncpy(..., "AgpmGuild", ...)
FUN_004e4540(0x15)
```

Fuer Auction sind daher in dieser Datei nur `AgpmAuction`/`AgcmAuction` mit Modul `0x0b` belastbar.

## AgpmAuction: Konstruktor und Layouts

Konstruktor: `FUN_0055e090`

Wichtige Punkte:

- VTable: `AgpmAuction::vftable`
- Modulname: `AgpmAuction`
- Modul-ID: `FUN_004e4540(0xb)` -> `0x0b`
- Objekt initialisiert viele Paketlayouts ueber `FUN_004e9f30`.

Wichtige Layout-Offets:

| Offset | Nutzung |
|---:|---|
| `+0xb9c` | Hauptlayout fuer Modul-`0x0b` Pakete; wird von `AgcmAuction` fuer Client-Sends genutzt und von `AgpmAuction` im Receive-Switch geparst |
| `+0x386d8` | Nested-Layout fuer Op `0x0d` |
| `+0x4afec` | Nested-Layout fuer Op `0x05` |
| `+0x5d900` | Nested-Layout fuer Op `0x06` |
| `+0x70214` | Nested-Layout fuer Op `0x07` |
| `+0x82b28` | Nested-Layout fuer Op `0x08` |

Weitere Layouts im Konstruktor liegen bei `+0x9771`, `+0xe1b6`, `+0x12bfb`, `+0x17640`, `+0x1c085`, `+0x20aca`, `+0x29f54`. Ihre genaue semantische Zuordnung ist noch offen, aber sie bilden wahrscheinlich Auktionsdatensaetze, Such-/Filterdaten, Itemdaten und Ergebnislisten ab.

## AgcmAuction: Abhaengigkeiten

`FUN_006e0410` verdrahtet `AgcmAuction` mit:

| Offset | Modul |
|---:|---|
| `+0xb98` | [`ApmMap`](../Module/ApmMap.md) |
| `+0xb9c` | [`ApmEventManager`](../Module/ApmEventManager.md) |
| `+0xba0` | [`AgpmCharacter`](../Module/AgpmCharacter.md) |
| `+0xba4` | [`AgpmFactors`](../Module/AgpmFactors.md) |
| `+0xba8` | [`AgpmItem`](../Module/AgpmItem.md) |
| `+0xbac` | `AgpmAuction` |
| `+0xbb0` | [`AgcmConnectManager`](../Module/AgcmConnectManager.md) |
| `+0xbb4` | [`AgcmEventManager`](../Module/AgcmEventManager.md) |
| `+0xbb8` / `+3000` | `AgcmCharacter` |

Zusatz: `AgcmUIAuction` bindet ausserdem [`AgpmGrid`](../Module/AgpmGrid.md), [`AgpmItemConvert`](../Module/AgpmItemConvert.md), [`AgcmItem`](../Module/AgcmItem.md), [`AgcmUIManager2`](../Module/AgcmUIManager2.md), [`AgcmUISplitItem`](../Module/AgcmUISplitItem.md) und [`AgcmUICooldown`](../Module/AgcmUICooldown.md).

## Client -> Server: gesendete Auction-Aktionen

Alle gesicherten Auction-Sends benutzen:

```text
FUN_004ea280(*(AgcmAuction + 0xbac) + 0xb9c, 1, ..., module 0x0b, ...)
FUN_004e45d0(...)
```

Dabei ist `AgcmAuction + 0xbac` der Pointer auf `AgpmAuction`.

### Op `0x05`

Funktion: `FUN_006dfea0`

Payload:

- Nested-Paket aus `AgpmAuction + 0x4afec`
- aeusseres Hauptpaket `AgpmAuction + 0xb9c`
- Op-Byte `5`

Bekannter UI-Aufrufer:

- `FUN_0078c630` ruft `FUN_006dfea0(localCID, itemIdOrTemplate, quantity, price)`.
- Vorher wird ein vom Spieler eingegebener Preis geprueft: `1 <= price < 499999999`.
- Wenn die Itemanzahl kleiner als die angeforderte Menge ist, wird Menge auf vorhandene Anzahl gekappt.

Wahrscheinliche Bedeutung: Item zum Verkauf einstellen oder Listing mit Preis/Menge erzeugen.

### Op `0x06`

Funktion: `FUN_006dff60`

Payload:

- Nested-Paket aus `AgpmAuction + 0x5d900`
- aeusseres Hauptpaket `AgpmAuction + 0xb9c`
- Op-Byte `6`

Bekannter UI-Aufrufer:

- `FUN_0078ca00` ruft `FUN_006dff60(localCID, auctionEntry)` wenn ein lokales Auction-Objekt Status `0` hat.

Wahrscheinliche Bedeutung: Auktionseintrag abbrechen, loeschen oder vom Verkauf zuruecknehmen.

### Op `0x07`

Funktion: `FUN_006e0010`

Payload:

- Nested-Paket aus `AgpmAuction + 0x70214`
- aeusseres Hauptpaket `AgpmAuction + 0xb9c`
- Op-Byte `7`

Bekannter UI-Aufrufer:

- `FUN_0078ca00` ruft `FUN_006e0010(localCID, auctionEntry)` wenn ein lokales Auction-Objekt Status `1` hat.

Wahrscheinliche Bedeutung: zweite Verwaltungsaktion fuer eigenen Eintrag, etwa Auszahlung/Abholung/Cancel nach Statuswechsel.

### Op `0x08`

Funktion: `FUN_006e00c0`

Bekannter UI-Aufrufer:

- `AC_BuyItem` -> `FUN_00615500` -> `AC_BuyMessageBox` -> `FUN_00616240` -> `FUN_006e00c0(...)`.

Ablauf in der UI:

1. Gewaehlter Board-Eintrag wird gelesen.
2. Sellername wird mit lokalem Charakternamen verglichen; bei eigenem Eintrag wird Kauf verhindert.
3. Preis wird in `+0x5a50/+0x5a54` als 64-bit Wert gehalten.
4. Lokales Geld liegt beim Character in `+0x538/+0x53c`.
5. Wenn Geld nicht reicht, wird `AC_NotEnoughMoney` ausgelöst.
6. Sonst erscheint `AC_BuyMessageBox`.
7. Bei Bestaetigung sendet `FUN_006e00c0(localCID, auctionIdLow, auctionIdHigh, quantity, priceLow, priceHigh, categoryOrTemplate)`.

Wahrscheinliche Bedeutung: Kauf eines Auktionslistings.

### Op `0x0a`

Funktion: `FUN_006e0180`

Bekannte Aufrufer:

- `FUN_006e02d0`: wird ueber Eventmanager-Registrierung `FUN_006e0860(0x1c, FUN_006e02d0, param_1)` getriggert.
- Ruft `FUN_006e0180(localCID, eventParam, FUN_0055e620(param_3))`.

Wahrscheinliche Bedeutung: Auction-NPC/Event-Interaktion oder initiales Oeffnen/Request gegen ein Eventobjekt.

### Op `0x0d`

Funktion: `FUN_006dfde0`

Payload:

- Nested-Paket aus `AgpmAuction + 0x386d8`
- aeusseres Hauptpaket `AgpmAuction + 0xb9c`
- Op-Byte `0x0d`

Wahrscheinliche Bedeutung: Such-/Listenrequest oder Kategorie-/Page-Request mit groesserem Parameterblock.

### Op `0x0f`

Funktion: `FUN_006e0220`

Bekannter UI-Aufrufer:

- `AC_OpenAnywhere` -> `FUN_006149a0`
- prueft lokalen Character/Event-Kontext ueber `FUN_004ede40(...)`
- sendet dann `FUN_006e0220(localCID)`

Payload:

- aeusseres Hauptpaket `AgpmAuction + 0xb9c`
- Op-Byte `0x0f`
- kein sichtbares Nested-Paket

Wahrscheinliche Bedeutung: Auktionsfenster global/ueberall oeffnen oder Server nach Auction-Status fragen.

## Server -> Client: empfangene Auction-Ops

Receive-/Dispatchfunktion: `FUN_0055ed20`

Sie parst das Hauptlayout:

```text
FUN_004e9fb0(param_1 + 0xb9c, 1, packet, packetLen,
  &op,
  &characterId,
  &nestedPacket,
  &local_88)
```

Danach wird die Character-ID aufgeloest (`FUN_005035d0(characterId)`) und ueber `op` verzweigt.

| Server-Op | Client-Reaktion | Interpretation |
|---:|---|---|
| `0x01` | nested `+0x134b0` parsen, neues Auction-Objekt allokieren, Sellername max. `0x20`, in lokale Liste einfuegen, Callback `1` | neuer Auktionsdatensatz / Listing hinzugefuegt |
| `0x02` | nested `+0x134b0` parsen, Auction-Objekt suchen, aus lokaler Liste entfernen, Callback `2` | Listing geloescht/verkauft/cancelled |
| `0x03` | nested `+0x134b0` parsen, Feld `+0x22` an bestehendem Objekt setzen, Callback `3` | Statusupdate fuer Listing |
| `0x04` | Fehlerpfad | ungueltig oder nicht verarbeitet |
| `0x05` | nested `+0x4afec` parsen, Callback `5` | Ergebnis-/Statusblock fuer Op 5 |
| `0x06` | nested `+0x5d900` parsen, Callback `6` | Ergebnis-/Statusblock fuer Op 6 |
| `0x07` | nested `+0x70214` parsen, Callback `7` | Ergebnis-/Statusblock fuer Op 7 |
| `0x08` | nested `+0x82b28` parsen, Callback `8` | Ergebnis-/Statusblock fuer Kauf/Op 8 |
| `0x09` | Callback `9` | Status-/Ack-Event |
| `0x0a` | Auction-Objekt suchen, Item/Inventory-Zustand pruefen, Callback `10` | Itemausgabe/Transfer/Listing-Status |
| `0x0b` | Auction-Objekt suchen, Callback `10` | zweite Variante desselben Statuspfads |
| `0x0c` | Callback `0x0b` ohne Objekt | globaler UI-/Status-Event |
| `0x0d` | nested `+0x386d8` parsen, Callback `0x0c` | grosser Ergebnisblock |
| `0x0e` | Callback `0x0d` | Status-/Fehlercode |
| `0x0f` | Callback `0x0e` mit `local_88` | Status-/Text-/Objektantwort |

## Auktionsobjekt / lokaler Datensatz

`FUN_0055e590` allokiert `0x50` Bytes fuer ein Auction-Objekt.

Aus dem Parser fuer Server-Op `0x01`:

| Offset | Nutzung |
|---:|---|
| `+0x00` | wird gegen `3` geprueft; Objekttyp |
| `+0x04` | ID oder Auction-Record-ID |
| `+0x08` | weiterer ID-/Template-/Owner-Wert |
| `+0x10` | Preis oder 64-bit-naher Wertbestandteil |
| `+0x14` | Menge / Quantity |
| `+0x20/+0x22` | Status/kleines Feld; `+0x22` wird bei Op `0x03` aktualisiert |
| `+0x24` bis ca. `+0x44` | Sellername/String, max. `0x20` |
| `+0x48` | Itemtemplate-ID oder Anzeigeitem |

Die Objektverwaltung nutzt eine Liste mit bis zu 10 verknuepften/assoziierten Objekten (`+0x38` bis `+0x5c`) fuer Unterobjekte oder zugehoerige Items.

## AgcmUIAuction: sichtbare UI-Daten

Registrierte Datenfelder:

| UI-Datenname | Bedeutung |
|---|---|
| `AuctionTreeData` | Kategorienbaum, bis `5000` Eintraege |
| `AuctionTreeDepthData` | Tiefe/Level je Kategorie |
| `AuctionCategory` | Kategorieeintraege, bis `5000 x 0x40` |
| `Auction_BoardCategoryName` | sichtbarer Kategoriename |
| `AC_BoardItemTemplateGrid` | Itemtemplate-Vorschaugrid |
| `Auction_BoardPageInfo` | Seitentext |
| `AuctionBoard` | Board-Liste, `0x0f` sichtbare Zeilen |
| `AC_PageInfoUD_1..10` | 10 Pagebutton-Werte |
| `AC_CategorySearchEdit` | Such-/Filtereingabe |

Registrierte Display-Felder:

```text
Auction_Tree_Display
Auction_Category
Auction_BoardCategoryName
Auction_PageIngfo
Auction_PageInfo_1..10
Auction_BoardDoc
Auction_BoardItemName
Auction_BoardPrice
Auction_BoardQuantity
Auction_BoardSellerName
```

Registrierte UI-Commands:

```text
AC_OpenUI
AC_SetFocusOnBoard
AC_KillFocusOnBoard
AC_SelectCategory
AC_BackToParent
AC_SearchTID
AC_BuyItem
AC_PrevPage
AC_NextPage
AC_OpenAnywhere
```

Registrierte Events/Messages:

```text
AC_OpenEvent
AC_CloseEvent
AC_BuyMessageBox
AC_NotEnoughMoney
AC_EnableCategoryItem
AC_DisableCategoryItem
AC_EP0
AC_EP1
AC_EP2
AC_EPage1..AC_EPage10
AC_ListButtonOn
AC_ListButtonOff
```

## Board-Liste und Paging

`FUN_00615650` verarbeitet Ergebnisdaten fuer das Board:

- Berechnet Seitenzahl aus Ergebnisanzahl:

```text
pageCount = (resultCount - 1) / 0x0f + 1
```

- Loescht 15 alte Board-Items.
- Loescht 15 alte Board-Datensaetze.
- Liest erste und letzte Ergebnis-ID/Preiswerte mit `_atoi64`.
- Baut fuer jeden sichtbaren Eintrag ein lokales `0x20`-Byte-Datenelement.
- Liest Itemtemplate-ID und baut daraus Anzeigename.
- Haengt Enhancement-/Durability-Text an:
  - `" + %d"`
  - `" [%d/%d]"`
- Parst comma-separierte Optionslisten:
  - `"%d,%d,%d,%d,%d"` fuer bis zu 5 Werte.
  - `"%d,%d,%d"` fuer bis zu 3 Werte.
- Aktualisiert 10 Pagebuttons und Boardanzeige.

Daraus folgt: Der Server liefert Auction-Board-Daten offenbar in tabellarischer/stringbasierter Form, die der Client zeilenweise parst. Werte fuer Preis und Grenzen werden als 64-bit Zahlen per `_atoi64` verarbeitet.

## Kaufablauf

1. Spieler markiert Board-Zeile.
2. `AC_BuyItem` ruft `FUN_00615500`.
3. Client verhindert Kauf eigener Listings durch Vergleich Sellername mit lokalem Charakternamen.
4. Preis/Menge werden aus dem Board-Datensatz gelesen.
5. Geldvergleich gegen lokale Character-Offets:
   - Low: `character + 0x538`
   - High: `character + 0x53c`
6. Bei zu wenig Geld: `AC_NotEnoughMoney`.
7. Sonst: `AC_BuyMessageBox`.
8. Bei Bestaetigung: `FUN_00616240`.
9. Sendet Op `0x08` ueber `FUN_006e00c0`.
10. Danach wird eine neue Listenanfrage fuer die naechste/aktuelle Seite ausgeloest.

## Verkauf / eigenes Listing

Der Verkaufsdialog prueft:

- Preis im Bereich `1..499999998`.
- Item muss aus gueltigem Item-/Grid-Kontext kommen.
- Wenn Stack-Menge vorhanden ist, wird die gewuenschte Menge auf vorhandene Menge gekappt.

Danach sendet `FUN_006dfea0` Op `0x05`.

Ein eigener Eintrag kann spaeter ueber `FUN_0078ca00` weiterverwaltet werden:

- Status `0` -> Op `0x06` (`FUN_006dff60`)
- Status `1` -> Op `0x07` (`FUN_006e0010`)

## Server-Datenbank-Inferenz

### Permanente Tabellen

`auction_listings`

- `auction_id`
- `seller_character_id`
- `seller_name`
- `item_instance_id`
- `template_id`
- `quantity`
- `price`
- `status`: active, sold, cancelled, expired, claimed
- `category_id`
- `created_at`
- `expires_at`
- `sold_at`
- `buyer_character_id`

`auction_categories`

- `category_id`
- `parent_category_id`
- `depth`
- `name`
- `sort_order`
- `template_filter` oder `item_type_filter`

`auction_listing_search_index`

- `auction_id`
- `template_id`
- `item_name`
- `category_id`
- `seller_name`
- `price`
- `created_at`
- `expires_at`

`auction_delivery`

- `delivery_id`
- `auction_id`
- `character_id`
- `type`: item, money, unsold_item
- `amount`
- `item_instance_id`
- `status`: pending, claimed, expired
- `created_at`
- `claimed_at`

`money_ledger`

- `ledger_id`
- `character_id`
- `delta`
- `reason = auction_buy | auction_sell | auction_fee | auction_refund`
- `auction_id`
- `balance_before`
- `balance_after`
- `created_at`

`item_locks`

- `item_instance_id`
- `lock_type = auction`
- `auction_id`
- `owner_character_id`
- `created_at`
- `expires_at`

### Warum diese Tabellen naheliegen

- Der Client zeigt Sellername, Itemname, Preis, Menge und Kategorie im Board.
- Kauf und Verkauf arbeiten mit 64-bit Geldwerten.
- Itemdaten muessen nach Listing-Erstellung reserviert sein, sonst waere paralleler Verkauf/Trade/Drop moeglich.
- Nach Kauf/Cancel gibt es unterschiedliche Statuspfade (`0x06`, `0x07`, Server-Ops `0x0a/0x0b`), was auf Claim-/Delivery-Zustaende hindeutet.
- Kategorienbaum und Depth-Daten werden separat in der UI gehalten.

## Sicherheitsrelevante Punkte

- Der Client verhindert Kauf eigener Auktionen ueber Sellername-Vergleich. Server muss das ueber Character-ID erzwingen.
- Client prueft Geld gegen lokale Werte, aber Server muss Saldo und Preis erneut pruefen.
- Preislimit `499999999` ist UI-seitig sichtbar, darf aber serverseitig nicht als einzige Grenze gelten.
- Server muss beim Listing Itembesitz, Tradeability, Stackmenge, Container und Lockstatus pruefen.
- Kauf muss atomar sein: Geld abbuchen, Item an Buyer liefern, Seller-Geld gutschreiben oder Delivery erzeugen.
- Cancel/Claim darf nur vom Seller bzw. berechtigten Character ausfuehrbar sein.
- Such-/Kategorieparameter duerfen keine direkten SQL-Strings werden; der Client sendet IDs/Textfilter, aber Server muss diese normalisieren.

## Noch offene Detailarbeit

- Die Label-Handler fuer `AC_SelectCategory`, `AC_SearchTID`, `AC_PrevPage`, `AC_NextPage` sollten im Controlflow weiter aufgeloest werden.
- Die Nested-Layout-Felder bei `+0x386d8`, `+0x4afec`, `+0x5d900`, `+0x70214`, `+0x82b28` sollten einzeln gegen ihre `FUN_004e9f30`-Typcodes gemappt werden.
- Die Server-Ops `0x05..0x0f` muessen noch mit UI-Callbacknummern und sichtbaren Messages verbunden werden.
- Eine spaetere Live-Paketprobe waere fuer die exakte Feldreihenfolge besonders wertvoll.
