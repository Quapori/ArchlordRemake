# AgcmUIAuction (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIAuction` (Auktionshaus-Oberfläche: Kategoriebaum, Angebotsliste, Kaufen/Verkaufen/Abbrechen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIAuction/AgcmUIAuction.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 51 von 56 Quellmethoden sind zugeordnet; Grundlage sind Callback-Registrierung, Aufrufgraph und Zeichenketten.
- **Wartezeit:** Jede Auktionsanfrage wird mit 2,5 Sekunden Fortschrittsbalken und höchstens einer gleichzeitigen Anfrage ausgelöst.
- **Kategorien:** höchstens 5000 Einträge, dreistufig; Auswahl auf der letzten Stufe lädt das Angebotsbrett.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIAuction.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00616E60` | 697 | vtable/String |
| 1 | `OnDestroy` | `0x00613CF0` | 24 | vtable/String |
| 2 | `OnInit` | `0x00613D10` | 89 | vtable/String |
| 3 | `AddEvent` | `0x006160E0` | 706 | Zeichenkette |
| 4 | `AddFunction` | `0x00616CC0` | 411 | Zeichenkette |
| 5 | `AddDisplay` | `0x006163B0` | 633 | Zeichenkette |
| 6 | `AddUserData` | `0x00614A70` | 787 | Zeichenkette |
| 7 | `CBBuyItemFromAuction` | `0x00614D90` | 326 | UI-Registrierung |
| 8 | `CBBoardSelect` | `0x00614EE0` | 2244 | Zeichenketten/Konstanten (geprüft) |
| 9 | `CBOpenAuctionUI` | `0x00613D70` | 187 | Zeichenkette |
| 10 | `CBSellUI` | `0x006157B0` | 326 | cbalign:AgcmUIAuction |
| 11 | `CBCancelUI` | `0x00616630` | 262 | cbalign:AgcmUIAuction |
| 12 | `CBSelfUpdatePosition` | `0x006149A0` | 94 | cbalign:AgcmUIAuction |
| 13 | `CBConfirmUI` | `0x00616740` | 213 | cbalign:AgcmUIAuction |
| 14 | `CBBuyUI` | `0x006169A0` | 258 | cbalign:AgcmUIAuction |
| 15 | `CBUpdateUI` | `0x00613E30` | 136 | cbalign:AgcmUIAuction |
| 16 | `GetCategoryText` | `0x00613EC0` | 732 | Aufrufgraph (geprüft) |
| 17 | `SetCategoryText` | `0x006178D0` | 474 | Aufrufgraph (geprüft) |
| 18 | `GetItemInstanceOnBoard` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 19 | `SetCallbackSetFocus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 20 | `SetCallbackKillFocus` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 21 | `CBOpenUI` | `0x006141A0` | 141 | UI-Registrierung |
| 22 | `CBOpenAnywhere` | `0x00614230` | 65 | UI-Registrierung |
| 23 | `CBDisplayAuctionTree` | `0x00615900` | 450 | UI-Registrierung |
| 24 | `CBDisplayCategory` | `0x00614280` | 59 | UI-Registrierung |
| 25 | `CBDisplayBoardCategoryName` | `0x006142C0` | 80 | UI-Registrierung |
| 26 | `CBDisplayDoc` | `0x00614310` | 60 | UI-Registrierung |
| 27 | `CBDisplayItemName` | `0x00614350` | 60 | UI-Registrierung |
| 28 | `CBDisplayPrice` | `0x00614390` | 60 | UI-Registrierung |
| 29 | `CBDisplayQuantity` | `0x006143D0` | 60 | UI-Registrierung |
| 30 | `CBDisplaySellerName` | `0x00614410` | 60 | UI-Registrierung |
| 31 | `CBReturnConfirmBuyItemFromAuction` | `0x00615AD0` | 198 | UI-Registrierung |
| 32 | `CBSetFocusOnACBoard` | `0x00614450` | 57 | UI-Registrierung |
| 33 | `CBKillFocusOnACBoard` | `0x00614490` | 58 | UI-Registrierung |
| 34 | `CBSelectCategory` | `0x00616AB0` | 86 | UI-Registrierung |
| 35 | `SelectCategory` | `0x00615BA0` | 362 | Aufrufgraph (geprüft) |
| 36 | `CBBackToParentButton` | `0x006144D0` | 193 | UI-Registrierung |
| 37 | `CBSearchCategoryButton` | `0x00616B10` | 429 | UI-Registrierung |
| 38 | `CBPrevPage` | `0x00615D10` | 402 | UI-Registrierung |
| 39 | `CBNextPage` | `0x00615ED0` | 382 | UI-Registrierung |
| 40 | `CBPageInfo` | `0x006145A0` | 86 | UI-Registrierung |
| 41 | `CBPageInfo1` | `0x00614600` | 72 | UI-Registrierung |
| 42 | `CBPageInfo2` | `0x00614650` | 72 | UI-Registrierung |
| 43 | `CBPageInfo3` | `0x006146A0` | 72 | UI-Registrierung |
| 44 | `CBPageInfo4` | `0x006146F0` | 72 | UI-Registrierung |
| 45 | `CBPageInfo5` | `0x00614740` | 72 | UI-Registrierung |
| 46 | `CBPageInfo6` | `0x00614790` | 72 | UI-Registrierung |
| 47 | `CBPageInfo7` | `0x006147E0` | 72 | UI-Registrierung |
| 48 | `CBPageInfo8` | `0x00614830` | 72 | UI-Registrierung |
| 49 | `CBPageInfo9` | `0x00614880` | 72 | UI-Registrierung |
| 50 | `CBPageInfo10` | `0x006148D0` | 72 | UI-Registrierung |
| 51 | `SetCooldown` | `0x00614920` | 123 | Aufrufgraph (geprüft) |
| 52 | `CBAfterCooldown` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 53 | `_GetAuctionQuantity` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 54 | `_SortCategoryItemByLevel` | `0x00617760` | 367 | Aufrufgraph (geprüft) |
| 55 | `_GetItemLevelByTID` | `0x00614A00` | 108 | Zeichenketten/Konstanten (geprüft) |

51 von 56 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006172a0` (`0x006172A0`), `ctor_or_dtor_006175d0` (`0x006175D0`), `~AgcmUIAuction` (`0x006176F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBA4` | `m_pcsAgcmCharacter` | `+0x15964` ist die eigene Charakter-ID (`SelectCategory`) |
| `0x195E4` | `Ereignis „Kategorie-Eintrag aktivieren“` | `GetCategoryText` |
| `0x19648` | `Cooldown-ID (`m_lCooldownID`)` | `SetCooldown` |
| `0x1964C` | `m_bNowProgress` | `SetCooldown` |
| `0x5A58 / 0x5A5C` | `zuletzt/aktuell gewählte Item-TID im Board` | `SelectCategory` |
| `0x5A74` | `Board-Item-Template-Grid` | `SelectCategory` |

## Callback-Registrierung in OnAddModule (0x00616E60)

Die acht Registrierungen stehen im Binary in der Reihenfolge der Quelle; sieben Handler sind zugeordnet:

| Setter (Quelle) | Handler | Adresse |
|---|---|---|
| `SetCallbackSelect` | `CBBoardSelect` | `0x00614EE0` |
| `SetCallbackSell` | `CBSellUI` | `0x006157B0` |
| `SetCallbackCancel` | `CBCancelUI` | `0x00616630` |
| `SetCallbackConfirm` | `CBConfirmUI` | `0x00616740` |
| `SetCallbackBuy` | `CBBuyUI` | `0x006169A0` |
| `SetCallbackSalesBox2Update` | `CBUpdateUI` | `0x00613E30` |
| `SetCallbackSelfUpdatePosition` | `CBSelfUpdatePosition` | `0x006149A0` |

## Anfragen und Wartezeit

Das Modul sendet keine Pakete selbst; `SendOpenAnywhere`, `SendBuy` und `SendSelect` gehören zu [`AgcmAuction`](AgcmAuction.md). Jede Anfrage läuft über `SetCooldown` (`0x00614920`): Es darf nur eine Anfrage gleichzeitig laufen (Flag `+0x1964C`), sie wird als Fortschrittsobjekt (24 Byte: Charakter-ID, Template-ID, Dokument-ID, Flag, Zusatzwert) an den Cooldown-Timer von [`AgcmUICooldown`](AgcmUICooldown.md) (`+0x19648`) übergeben, Dauer **2500 ms** (`0x9C4`, `PROGRESS_COOLTIME`). Erst danach wird laut Quelle die eigentliche Anfrage gesendet (`CBAfterCooldown` → `SendSelect`; diese Funktion ist im Binary nicht zugeordnet).

## Kategorien

`GetCategoryText` (`0x00613EC0`) setzt zuerst für alle 5000 möglichen Kategorie-Einträge (`AGCM_UI_AUCTION_MAX_CATEGORY_COUNT`) das Ereignis „Eintrag aktivieren“ (`+0x195E4`) zurück und füllt dann je nach Tiefe die Kategorien (Tiefe 0 aus [`AgpmAuctionCategory`](AgpmAuctionCategory.md)). `SelectCategory` (`0x00615BA0`) wählt bei der dritten Stufe das Item-Template, setzt die Seite auf 1, leert und füllt das Board-Grid und aktualisiert die Anzeige.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`SetCooldown`, `GetCategoryText`, `SelectCategory`).

## Grenzen

- Fünf kleine Methoden sind nicht zugeordnet (u. a. `GetItemInstanceOnBoard`, `CBAfterCooldown`, `_GetAuctionQuantity`).
- Die Anzeigen (`AddDisplay`, 19 in der Quelle) wurden nicht zugeordnet, weil das Binary sie über abweichende Aufrufformen registriert; die Seitenanzeigen `CBPageInfo1..10` sind unverifiziert.
- Die Netzwerkfunktionen liegen in `AgcmAuction`, nicht in diesem Modul.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2, nicht im Client: 1, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmAuction`](AgcmAuction.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgpmAuctionCategory`](AgpmAuctionCategory.md)
- **Erwähnt in:** [`AgcmUICooldown`](AgcmUICooldown.md)
