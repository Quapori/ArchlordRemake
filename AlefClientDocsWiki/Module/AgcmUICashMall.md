# AgcmUICashMall (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUICashMall` (Cash-Shop-Oberfläche: Registerkarten, Warenliste, Seiten, Kaufbestätigung, Cash-Anzeige) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Übersetzungseinheit-Reihenfolge und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUICashMall/AgcmUICashMall.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 44 von 45 Quellmethoden sind zugeordnet; neu sind `SetSelectPageSlot`, `CBCheckCash`, `SetItemGrid` und `RefreshCashEdit`. `CBSetSelfCharacter` und `CBIsShowChargeButton` sind im `_AREA_GLOBAL_`-Build reine `return TRUE`-Rümpfe und teilen sich mit anderen gleichen Funktionen die Adresse `0x0067AC90` (Linker-Faltung, im Namensbestand fälschlich `Element::GetSize`).
- **UI-Schnittstelle:** 13 Funktionen, 11 Anzeigen und 4 Boolean-Werte (Anzahl wie in der Quelle), siehe Tabelle „UI-Namen“.
- **Cash-Anfrage:** höchstens eine pro Sekunde, wie bei `SendPacketRefreshCash` in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUICashMall.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0069F5B0` | 432 | vtable/String |
| 1 | `OnInit` | `0x0069D340` | 49 | vtable/String |
| 2 | `OnDestroy` | `0x0069D380` | 43 | vtable/String |
| 3 | `AddFunction` | `0x0069EF30` | 552 | Zeichenkette |
| 4 | `AddBoolean` | `0x0069E3F0` | 123 | Zeichenkette |
| 5 | `AddUserData` | `0x0069D3B0` | 252 | Zeichenkette |
| 6 | `AddDisplay` | `0x0069F360` | 361 | Zeichenkette |
| 7 | `AddEvent` | `0x0069E470` | 1012 | Zeichenkette |
| 8 | `SetItemGrid` | `0x0069E870` | 839 | ver |
| 9 | `CBUpdateMallList` | `0x0069F4D0` | 159 | Callback-Registrierung |
| 10 | `CBSetSelfCharacter` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 11 | `CBResponseBuyResult` | `0x0069D4B0` | 359 | Callback-Registrierung |
| 12 | `CBKeydownESC` | `0x0069D650` | 25 | Callback-Registrierung |
| 13 | `CBUpdateCash` | `0x0069F570` | 50 | Callback-Registrierung |
| 14 | `RefreshCashEdit` | `0x0069F160` | 343 | ver |
| 15 | `CBGetEditControl` | `0x0069D670` | 37 | UI-Registrierung |
| 16 | `CBGetEditControl2` | `0x0069D6A0` | 37 | UI-Registrierung |
| 17 | `CBGetEditControl3` | `0x0069D6D0` | 37 | UI-Registrierung |
| 18 | `CBGetListControl` | `0x0069D700` | 37 | UI-Registrierung |
| 19 | `CBCashCharge` | `0x0069D730` | 95 | UI-Registrierung |
| 20 | `CBCheckCash` | `0x0069E150` | 173 | ver |
| 21 | `CBBuyProductConfirm` | `0x0069D790` | 369 | UI-Registrierung |
| 22 | `CBBuyProduct` | `0x0069D910` | 169 | UI-Registrierung |
| 23 | `CBOpenCashMallUI` | `0x0069D9C0` | 136 | UI-Registrierung |
| 24 | `CBSelectTab` | `0x0069DA50` | 27 | UI-Registrierung |
| 25 | `CBPageLeft` | `0x0069EBD0` | 61 | UI-Registrierung |
| 26 | `CBPageRight` | `0x0069EC10` | 168 | UI-Registrierung |
| 27 | `CBGoPage` | `0x0069ECC0` | 87 | UI-Registrierung |
| 28 | `CBIsShowTabButton` | `0x0069DA70` | 70 | UI-Registrierung |
| 29 | `CBIsShowChargeButton` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 30 | `CBIsActivePage` | `0x0069DAC0` | 105 | UI-Registrierung |
| 31 | `CBIsActiveBuy` | `0x0069DB30` | 158 | UI-Registrierung |
| 32 | `CBDisplayProductName` | `0x0069DBD0` | 291 | UI-Registrierung |
| 33 | `CBDisplayProductDesc` | `0x0069ED20` | 155 | UI-Registrierung |
| 34 | `CBDisplayProductPrice` | `0x0069DD00` | 147 | UI-Registrierung |
| 35 | `CBDisplayTabName` | `0x0069EDC0` | 128 | UI-Registrierung |
| 36 | `CBDisplayPageNumber` | `0x0069DDA0` | 233 | UI-Registrierung |
| 37 | `CBDisplayMaxPageNumber` | `0x0069DE90` | 110 | UI-Registrierung |
| 38 | `CBDisplayBuyProductDetailList` | `0x0069F2C0` | 154 | UI-Registrierung |
| 39 | `CBDisplayBuyProductDetailValuePrice` | `0x0069DF00` | 60 | UI-Registrierung |
| 40 | `CBDisplayBuyProductDetailValueUseCash` | `0x0069DF40` | 192 | UI-Registrierung |
| 41 | `CBDisplayBuyProductDetailValueRemainCash` | `0x0069E000` | 246 | UI-Registrierung |
| 42 | `CBDisplayBuyMessage` | `0x0069EE40` | 71 | UI-Registrierung |
| 43 | `SetSelectPageSlot` | `0x0069E100` | 69 | ver |
| 44 | `CBReturnRefresh` | – | | nicht zugeordnet (klein oder eingefaltet) |

44 von 45 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUICashMall` (`0x0069E170`), `~AgcmUICashMall` (`0x0069E3C0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBAC` | `Zeiger auf `AgcmCharacter`` | `+0x1596C` ist der Self-Character (`RefreshCashEdit`) |
| `0xBB0` | `Zeiger auf [`AgcmCashMall`](AgcmCashMall.md)` | `CBCheckCash` |
| `0xCCC` | `Zeiger/Flag, ohne das `RefreshCashEdit` abbricht` | `RefreshCashEdit` |
| `0xD08…` | `Ereignis-IDs der Seiten 1–9` | `SetSelectPageSlot` |

## Adressbereich

`AgcmUICashMall.cpp` liegt zusammenhängend bei `0x0069D340`–`0x0069F5B0` (`OnAddModule` zuletzt).

## Cash-Aktualisierung

`CBCheckCash` (`0x0069E150`) enthält die Anfrage „Cash aktualisieren“ inline (`AgcmCashMall::SendPacketRefreshCash`): höchstens eine Anfrage pro Sekunde (Zeitstempel +1000 ms), danach Paket über `0x0087C400`. `RefreshCashEdit` (`0x0069F160`) schreibt drei Zeilen „%s : %d“ mit den UI-Texten `CCash`, `PCash` und `KeepCash` (Summe der beiden Cash-Arten).

## Seiten und Waren

`SetItemGrid` (`0x0069E870`) füllt das Warenraster einer Registerkarte (sechs Waren je Seite, `param_4 * 6 - 6` als Startindex); `SetSelectPageSlot` (`0x0069E100`) wirft für die gewählte Seite 1–9 das zugehörige Ereignis.

## Callback-Registrierung in OnAddModule (0x0069F5B0)

Die fünf Registrierungen stehen im Binary in der Reihenfolge der Quelle (5 von 5); alle Handler sind benannt.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x0069EF30`, `0x0069F360`, `0x0069D3B0`, `0x0069E3F0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (13)

| Name | Id | Handler |
|---|---:|---|
| `CashMallGetEdit` |  | `CBGetEditControl` |
| `CashMallGetEdit2` |  | `CBGetEditControl2` |
| `CashMallGetEdit3` |  | `CBGetEditControl3` |
| `CashMallGetList` |  | `CBGetListControl` |
| `CashMallCashCharge` |  | `CBCashCharge` |
| `CashMallCheckCash` |  | `FUN_0069e150` |
| `CashMallBuyProductConfirm` |  | `CBBuyProductConfirm` |
| `CashMallBuyProduct` |  | `CBBuyProduct` |
| `CashMallOpenUI` |  | `CBOpenCashMallUI` |
| `CashMallSelectTab` |  | `CBSelectTab` |
| `CashMallPageLeft` |  | `CBPageLeft` |
| `CashMallPageRight` |  | `CBPageRight` |
| `CashMallGoPage` |  | `CBGoPage` |

**Anzeige** (11)

| Name | Id | Handler |
|---|---:|---|
| `CashMallProductName` | 0 | `CBDisplayProductName` |
| `CashMallProductDesc` | 0 | `CBDisplayProductDesc` |
| `CashMallProductPrice` | 0 | `CBDisplayProductPrice` |
| `CashMallDisplayTabName` | 0 | `CBDisplayTabName` |
| `CashMallDisplayPageNumber` | 0 | `CBDisplayPageNumber` |
| `CashMallDisplayMaxPageNumber` | 0 | `CBDisplayMaxPageNumber` |
| `CashMallDetailList` | 0 | `CBDisplayBuyProductDetailList` |
| `CashMallDetailValuePrice` | 0 | `CBDisplayBuyProductDetailValuePrice` |
| `CashMallDetailValueUseCash` | 0 | `CBDisplayBuyProductDetailValueUseCash` |
| `CashMallDetailValueRemainCash` | 0 | `CBDisplayBuyProductDetailValueRemainCash` |
| `CashMallBuyMessage` | 0 | `CBDisplayBuyMessage` |

**UserData** (6)

| Name | Id | Handler |
|---|---:|---|
| `CashMallCurrentTab` |  | – |
| `CashMallCurrentPage` |  | – |
| `CashMallListItemGrid` |  | – |
| `CashMallCash` |  | – |
| `CashMallBuyProduct` |  | – |
| `CashMallMaxPage` |  | – |

**Boolean** (4)

| Name | Id | Handler |
|---|---:|---|
| `CashMall_ShowTabButton` |  | `CBIsShowTabButton` |
| `CashMall_IsActivePage` |  | `CBIsActivePage` |
| `CashMall_IsActiveBuy` |  | `CBIsActiveBuy` |
| `CashMall_ShowChargeButton` |  | `Element::GetSize` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Eine Methode ist nicht zugeordnet: `CBReturnRefresh` (ruft in der Quelle `SendPacketRefreshCash`; im Binary keine Registrierung gefunden).
- Die Anzeige- und Kauf-Handler wurden nur auf Struktur geprüft, nicht Zeile für Zeile.
- Das Netzwerkmodul `AgcmCashMall` ist ein eigener Bericht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmCashMall`](AgcmCashMall.md)
