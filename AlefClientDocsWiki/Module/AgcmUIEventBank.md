# AgcmUIEventBank (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIEventBank` (Bank-Oberfläche: Gegenstände, Geld, zusätzliche Fächer) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIEventBank/AgcmUIEventBank.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 31 von 31 Quellmethoden sind zugeordnet; neu sind `CBAddItemToBank`/`CBRemoveItemFromBank` (gleiche Adresse) und `CBDisplayBankMoney`; `CBCancelBankSlot` steht als gemeinsamer Rumpf.
- **UI:** 10 Funktionen, 4 Boolean-Werte, 3 Anzeigen, 4 Benutzerdaten, 5 Ereignisse – wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIEventBank.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006BF440` | 438 | vtable/String |
| 1 | `AddEvent` | `0x006BE580` | 164 | Zeichenkette |
| 2 | `AddFunction` | `0x006BF210` | 548 | Zeichenkette |
| 3 | `AddDisplay` | `0x006BF080` | 104 | Zeichenkette |
| 4 | `AddUserData` | `0x006BE630` | 178 | Zeichenkette |
| 5 | `CBSetSelfCharacter` | `0x006BE6F0` | 133 | Callback-Registrierung |
| 6 | `CBSelfUpdatePosition` | `0x006BE780` | 136 | Callback-Registrierung |
| 7 | `CBUpdateBank` | `0x006BE810` | 66 | Callback-Registrierung |
| 8 | `CBUpdateBankUI` | `0x006BE860` | 35 | Callback-Registrierung |
| 9 | `CBAddItemToBank` | `0x006BE890` | 48 | ver |
| 10 | `CBRemoveItemFromBank` | `0x006BE890` | 48 | gleiche Adresse wie `CBAddItemToBank` (vom Linker zusammengefaltet) |
| 11 | `CBUpdateBankMoney` | `0x006BE8C0` | 86 | Callback-Registrierung |
| 12 | `CBGrantBankEvent` | `0x006BE920` | 112 | Callback-Registrierung |
| 13 | `CBBankMoveItem` | `0x006BF0F0` | 276 | UI-Registrierung |
| 14 | `CBInputMoneyToBank` | `0x006BE990` | 235 | UI-Registrierung |
| 15 | `CBSetInputMoneyToBank` | `0x006BEA80` | 45 | UI-Registrierung |
| 16 | `CBSetOutputMoneyFromBank` | `0x006BEAB0` | 45 | UI-Registrierung |
| 17 | `CBDisplayBankMoney` | `0x006BEAE0` | 64 | ver |
| 18 | `CBDisplayConfirmMessage` | `0x006BEB20` | 85 | UI-Registrierung |
| 19 | `CBUpdateBankSize` | `0x006BEB80` | 66 | Callback-Registrierung |
| 20 | `CBBuyBankSlot` | `0x006BEBD0` | 121 | UI-Registrierung |
| 21 | `CBCancelBankSlot` | `0x0078B6A0` | 10 | gleiche Adresse wie `gemeinsamer Rumpf (return pClass != 0)` (vom Linker zusammengefaltet) |
| 22 | `CBRequestBuyBankSlot` | `0x006BEC50` | 64 | UI-Registrierung |
| 23 | `CBSetBankPrice` | `0x006BEC90` | 345 | UI-Registrierung |
| 24 | `CBBankUpdateLayer` | `0x006BEDF0` | 111 | UI-Registrierung |
| 25 | `CBBankDragDropItem` | `0x006BEE60` | 168 | UI-Registrierung |
| 26 | `CBIsActiveBuyBankSlot` | `0x006BEF10` | 94 | UI-Registrierung |
| 27 | `CBIsActiveBankSlot1` | `0x006BEF70` | 42 | UI-Registrierung |
| 28 | `CBIsActiveBankSlot2` | `0x006BEFA0` | 42 | UI-Registrierung |
| 29 | `CBIsActiveBankSlot3` | `0x006BEFD0` | 42 | UI-Registrierung |
| 30 | `CBDisplayBuyBankSlotTitle` | `0x006BF000` | 75 | UI-Registrierung |

31 von 31 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIEventBank` (`0x006BE4E0`), `~AgcmUIEventBank` (`0x006BF050`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBBC` | `Benutzerdaten Bank-Ebenenindex` | `CBRequestBuyBankSlot` |
| `0xBDC / 0xBE0 / 0xBE4` | `Ereignis-IDs Bank öffnen / schließen / aktualisieren` | `AddEvent`, `CBAddItemToBank` |
| `0xBE8` | `Ereignis „Kauf des Fachs bestätigen“` | `CBRequestBuyBankSlot` |

## Vtable

Vtable bei `0x008D3E9C`: Slot 0 Destruktor `0x006BF050`, 1 `OnAddModule` (`0x006BF440`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`, `OnDestroy`).

## Callbacks (OnAddModule, 0x006BF440)

Sechs Module (u. a. [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md), [`AgcmItem`](AgcmItem.md), [`AgcmEventBank`](AgcmEventBank.md), [`AgcmUIManager2`](AgcmUIManager2.md)). Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| Bankgeld geändert | `CBUpdateBankMoney` | `0x006BE8C0` |
| Bankgröße geändert | `CBUpdateBankSize` | `0x006BEB80` |
| Bank aktualisiert | `CBUpdateBank` | `0x006BE810` |
| Bank-UI aktualisieren | `CBUpdateBankUI` | `0x006BE860` |
| Gegenstand in die Bank | `CBAddItemToBank` | `0x006BE890` |
| Gegenstand aus der Bank | `CBRemoveItemFromBank` | `0x006BE890` |
| Self-Character gesetzt | `CBSetSelfCharacter` | `0x006BE6F0` |
| Eigene Position geändert | `CBSelfUpdatePosition` | `0x006BE780` |
| Bank-Ereignis gewährt | `CBGrantBankEvent` | `0x006BE920` |

`CBAddItemToBank` und `CBRemoveItemFromBank` haben in der Quelle denselben Rumpf (Ereignis „Bank aktualisiert“ werfen, wenn beide Zeiger gesetzt sind); das Binary meldet dieselbe Adresse zweimal an. Danach `AddEvent`, `AddFunction`, `AddDisplay`, `AddUserData`.

## Ohne Wirkung

`Item_CancelBankSlot` zeigt auf `0x0078B6A0`, einen Rumpf `return pClass != 0`. Das entspricht `CBCancelBankSlot` der Quelle (prüft nur `pClass` und liefert TRUE) und teilt sich die Adresse mit einer gleichförmigen Funktion anderer Module (im Namensbestand fälschlich [`AgcmShrine`](AgcmShrine.md):CBShrineTapScroe`).

## Anzeige Bankgeld

`CBDisplayBankMoney` (`0x006BEAE0`) verlangt Datentyp `0x100` (64-Bit-Zahl), Anzeige-ID 0 und einen Zielpuffer und schreibt `%I64d`. Entspricht der Quelle.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006BF210`, `0x006BF080`, `0x006BE630`, `0x006BE580`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (10)

| Name | Id | Handler |
|---|---:|---|
| `Bank_MoveItem` |  | `CBBankMoveItem` |
| `Bank_Money_Input` |  | `CBInputMoneyToBank` |
| `Bank_Money_Set_Input` |  | `CBSetInputMoneyToBank` |
| `Bank_Money_Set_Output` |  | `CBSetOutputMoneyFromBank` |
| `Item_RequestBuyBankSlot` |  | `CBRequestBuyBankSlot` |
| `Item_BuyBankSlot` |  | `CBBuyBankSlot` |
| `Item_CancelBankSlot` |  | `AgcmShrine::CBShrineTapScroe` |
| `Item_SetBankPrice` |  | `CBSetBankPrice` |
| `Item_BankUpdateLayer` |  | `CBBankUpdateLayer` |
| `Item_BankDragDropItem` |  | `CBBankDragDropItem` |

**Boolean** (4)

| Name | Id | Handler |
|---|---:|---|
| `IsActiveBuyBankSlot` |  | `CBIsActiveBuyBankSlot` |
| `IsActiveBankSlot1` |  | `CBIsActiveBankSlot1` |
| `IsActiveBankSlot2` |  | `CBIsActiveBankSlot2` |
| `IsActiveBankSlot3` |  | `CBIsActiveBankSlot3` |

**Anzeige** (3)

| Name | Id | Handler |
|---|---:|---|
| `BankMoney` | 0 | `FUN_006beae0` |
| `BankMoneyConfirm` | 1 | `CBDisplayConfirmMessage` |
| `ItemBankBuySlotTitle` | 2 | `CBDisplayBuyBankSlotTitle` |

**UserData** (4)

| Name | Id | Handler |
|---|---:|---|
| `BankGrid` |  | – |
| `BankMoney` |  | – |
| `BankDummy` |  | – |
| `BankLayerIndex` |  | – |

**Ereignis** (5)

| Name | Id | Handler |
|---|---:|---|
| `Bank_OpenUI` | 0 | – |
| `Bank_CloseUI` | 0 | – |
| `Bank_ItemUpdate` | 0 | – |
| `Item_ConfirmBuyBankSlot` | 0 | – |
| `Bank_NotEnoughBuyCost` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die größeren Handler (`CBBankMoveItem`, `CBInputMoneyToBank`, `CBSetBankPrice`) waren bereits zugeordnet und wurden hier nicht neu gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventBank`](AgcmEventBank.md), [`AgcmItem`](AgcmItem.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md)
- **Erwähnt in:** [`AgcmItem`](AgcmItem.md)
