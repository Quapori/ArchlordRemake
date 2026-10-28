# Winsock Sequenz 15: Bank-Geld- und Itemtransaktionen

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Diese Datei vertieft die Bank aus [`WINSOCK_SEQUENCE_13_SERVICE_NPCS.md`](Sequenz-13-Service-Npcs.md) und [`WINSOCK_SEQUENCE_14_SERVICE_NPC_RECEIVE_SWITCHES.md`](Sequenz-14-Service-Npc-Receive-Switches.md). Fokus sind die tatsaechlichen Buchungspakete fuer Geld, Bankitems und Bank-Slots. Quellen sind `alefclient.pseudocode.c`. Kein Live-Traffic wurde mitgeschnitten; Datenbankstrukturen sind Inferenz.

## Kurzfazit

- [`AgpmEventBank`](../Module/AgpmEventBank.md) Modul `0x36` oeffnet/steuert den Bank-NPC, aber die eigentlichen Buchungen laufen nicht nur ueber `0x36`.
- Bank-Geldtransfers laufen ueber [`AgpmCharacter`](../Module/AgpmCharacter.md) Modul `0x02`, Subop `7`.
- Bank-Itembewegungen und Bank-Slot-Kauf laufen ueber [`AgpmItem`](../Module/AgpmItem.md) Modul `0x04`.
- Die UI prueft Geld, aktiven Banklayer und Itemstatus, aber der Server muss alles erneut validieren.
- Besonders wichtig fuer Serverrekonstruktion: Bank ist ein Zusammenspiel aus Character-Wallet, Itemcontainer/Grid und Event-Bankstatus.

## UI-Ausloeser

[`AgcmUIEventBank`](../Module/AgcmUIEventBank.md) registriert diese relevanten Commands:

| UI-Command | Funktion | Zweck |
|---|---|---|
| `Bank_Money_Input` | `FUN_006befc0` | Deposit/Withdraw Betrag aus Edit-Control |
| `Item_RequestBuyBankSlot` | `FUN_006bf280` | Confirm-Dialog fuer Slotkauf |
| `Item_BuyBankSlot` | `FUN_006bf200` | Bank-Slot kaufen |
| `Item_BankDragDropItem` | `FUN_006bf490` | Item in/aus Bank bzw. Layer verschieben |
| `Item_BankUpdateLayer` | `FUN_006bf420` | Banklayer im UI wechseln |
| `Bank_MoveItem` | `LAB_006bf720` | Bank-Grid-Itembewegung, Ziel nicht direkt benannt |

Die UI-Datenfelder sind:

- `BankGrid`
- `BankMoney`
- `BankDummy`
- `BankLayerIndex`

## Geldtransfer: Deposit/Withdraw

### Eingabe

`FUN_006befc0`:

- Wird von `Bank_Money_Input` aufgerufen.
- Liest den String aus dem Edit-Control bei `control + 0x1d04`.
- Konvertiert ueber `atof(...)` und `FUN_007fecc6()` zu einem 64-bit Geldwert.
- Nutzt `param_1 + 0xbd0` als Richtung:
  - `0`: eine Richtung, im UI-Kontext wahrscheinlich Einzahlung in die Bank.
  - nicht `0`: Gegenrichtung, wahrscheinlich Auszahlung aus der Bank.

Der Client prueft:

- Betrag muss groesser `0` sein.
- Bei einer Richtung wird `betrag + characterMoney < 0x3b9aca01` geprueft.
- Bei Fehler wird Message-ID `0x2d1` angezeigt.

### Paketbuilder `FUN_005a10f0`

Aufruf aus `FUN_006befc0`:

```text
FUN_005a10f0(character, amountLow, amountHigh)
```

Paket:

```text
subop = 7
delta = -amount
FUN_004ea280(AgpmCharacter + 0xde4, 1, &outLen, 0x02,
             &subop, character + 4,
             ..., &deltaLow, ...)
FUN_004e45d0(packet, outLen, 0, 0xffffffff, FUN_005a0200())
```

Interpretation:

- Sendet ein negatives Geld-Delta.
- Sehr wahrscheinlich "Geld aus Inventory in Bank" oder die Richtung, bei der Inventory-Geld sinkt.
- Der Betrag wird vorher gegen `FUN_0058a7e0(character)` begrenzt, also wahrscheinlich verfuegbares Geld fuer diese Richtung.

### Paketbuilder `FUN_005a0fd0`

Aufruf aus `FUN_006befc0`:

```text
FUN_005a0fd0(character, amountLow, amountHigh)
```

Paket:

```text
subop = 7
delta = +amount
FUN_004ea280(AgpmCharacter + 0xde4, 1, &outLen, 0x02,
             &subop, character + 4,
             ..., &amountLow, ...)
FUN_004e45d0(packet, outLen, 0, 0xffffffff, FUN_005a0200())
```

Interpretation:

- Sendet ein positives Geld-Delta.
- Sehr wahrscheinlich die Gegenrichtung zu `FUN_005a10f0`, also Bank -> Inventory oder Inventory -> Bank je nach interner Semantik.
- Betrag wird gegen `FUN_0058a5f0(character, &available)` begrenzt.

### Wichtige Protokollfolge

```text
Bank_Money_Input
  -> FUN_006befc0
     -> Betrag lesen
     -> Richtung aus UI-State
     -> FUN_005a10f0 oder FUN_005a0fd0
        -> AgpmCharacter Modul 0x02 / Subop 7
        -> FUN_004e45d0(...)
```

Server-Inferenz:

- Bankgeld ist entweder im Characterdatensatz als eigenes 64-bit Feld gespeichert oder in einer Wallet-Tabelle mit Wallet-Typ.
- Beide Richtungen muessen atomar mit Inventar-Geld und Bank-Geld gebucht werden.
- Der Client sendet nur ein Delta; die serverseitige Richtung muss aus Session/Bankzustand/Subkontext abgeleitet werden.

## Bank-Slot kaufen

### UI-Pfad

`FUN_006bf200`:

- Wird von `Item_BuyBankSlot` aufgerufen.
- Holt lokalen Charakter.
- Vergleicht verfuegbares Geld mit Slotpreis aus `FUN_0058e960(character, 0)`.
- Bei zu wenig Geld: `Bank_NotEnoughBuyCost`.
- Bei Erfolg: ruft `FUN_006ebec0(characterId)`.

### Paketbuilder `FUN_006ebec0`

```text
FUN_006ebec0(characterId)
  -> FUN_0053ba20(characterId, &outLen)
  -> FUN_004e45d0(packet, outLen, 0, 3, 0)
```

`FUN_0053ba20` baut ein `AgpmItem`-Paket:

```text
subop = 0x16
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, 0, 0, 0, &characterId, ...)
```

Interpretation:

- Modul `0x04`, Subop `0x16`.
- Parameter ist Character-ID.
- Sehr wahrscheinlich "Bank-Slot kaufen/freischalten".

Server-Inferenz:

- Tabelle `character_bank_slots` mit aktuellem Layer/Slot-Level.
- Slotpreis wird serverseitig anhand aktuellem Slotstatus berechnet.
- Server muss Geld abziehen und Slot freischalten in einer Transaktion.

## Bank-Itembewegung

### UI-Pfad

`FUN_006bf490`:

- Wird von `Item_BankDragDropItem` aufgerufen.
- Liest selektiertes Item aus Drag-Drop-Kontext.
- Prueft, ob das selektierte Objekt ein Item ist.
- Bestimmt aktiven Banklayer aus UI-Control `control + 0x130`.
- Prueft gegen `character + 0x550`, das wie freigeschalteter Banklayer/Slotindex wirkt.
- Ruft:

```text
FUN_006ebcb0(itemId, localCharacterCid, bankLayer, -1, -1)
```

Die Dekompiler-Signatur von `FUN_006ebcb0` zeigt nur drei formale Parameter, aber der Aufruf nutzt weitere Stackargumente. Fuer die Semantik sind mindestens `itemId`, `characterId` und `bankLayer` sicher sichtbar.

### Paketbuilder `FUN_006ebcb0`

`FUN_006ebcb0` baut zuerst ein verschachteltes Unterpaket:

```text
FUN_004ea280(AgpmItem + 0x38a00, 0, &nestedLen, 0,
             &arg0, &arg1, &arg2)
```

Danach ein aeusseres Item-Paket:

```text
local_5 = 2
local_6 = 100
FUN_004ea280(AgpmItem + 0xec4, 1, &outLen, 0x04,
             &subop2, &constant100, &characterId,
             0, &bankLayer, ..., nestedPacket, ...)
FUN_004e45d0(packet, outLen, 0, 3, 0)
```

Interpretation:

- Modul `0x04`, Subop `2`.
- Konstante `100` ist wahrscheinlich Container-/Statuskennung fuer Bank oder eine Item-Move-Operation.
- Nested-Paket enthaelt genaue Grid-/Move-Details.
- `bankLayer` wird explizit uebergeben.

Server-Inferenz:

- Itemmove ist nicht nur "item_id -> container", sondern ein verschachtelter Move mit Quelle/Ziel/Grid.
- Bankcontainer wird vermutlich als spezieller Itemcontainerstatus `100` modelliert.
- Tabelle `character_bank_items` braucht mindestens `character_id`, `item_id`, `layer`, `grid_x`, `grid_y`.

## Weitere Itemmodul-Builder im gleichen Bereich

Diese Funktionen gehoeren zum allgemeinen Itemmodul `0x04` und werden von Bank/Inventory/Item-UI wiederverwendet:

| Funktion | Subop | Beobachtung |
|---|---:|---|
| `FUN_0053b7b0` | `3` | Item-Paket mit `item + 4`, `item + 0x3c` und optionalem Extra |
| `FUN_0053b8b0` | `0x11` im inneren Kontext | baut nested `AgpmItem + 0x260ec`, dann aeusseres `FUN_0053ab40(...)` |
| `FUN_0053b9a0` | `0x15` | Item-Paket mit Character/Item-ID |
| `FUN_0053ba20` | `0x16` | Bank-Slot-Kauf ueber Character-ID |
| `FUN_0053ba90` | `0x17` | Item-Paket mit `item + 4`, `item + 0x3c` |
| `FUN_0053bb00` | `0x1e` | Item-Paket mit zusaetzlichem nested Statusblock |

Diese Subops sollten in einem spaeteren allgemeinen `AgpmItem`-Deep-Dive vollstaendig gemappt werden.

## Was wann zum Server geht

### Bank oeffnen

```text
NPC anklicken
  -> AgcmEventBank / Event-Funktion 0x14
  -> AgpmEventBank Modul 0x36, Subop 0
  -> Server bestaetigt/oeffnet Bank UI
```

### Geld einzahlen/auszahlen

```text
Betrag eingeben
  -> Bank_Money_Input
  -> FUN_006befc0
  -> FUN_005a10f0 oder FUN_005a0fd0
  -> AgpmCharacter Modul 0x02, Subop 7, signed 64-bit Delta
  -> Server bucht Wallets
  -> Server sendet Character-/Bank-Geldsync
```

### Bank-Slot kaufen

```text
Item_RequestBuyBankSlot
  -> Confirm UI
Item_BuyBankSlot
  -> FUN_006bf200
  -> FUN_006ebec0
  -> AgpmItem Modul 0x04, Subop 0x16, Character-ID
  -> Server prueft Preis, bucht Geld, schaltet Slot/Layer frei
```

### Item in Bank bewegen

```text
DragDrop Item
  -> Item_BankDragDropItem
  -> FUN_006bf490
  -> FUN_006ebcb0(itemId, characterId, bankLayer, ...)
  -> AgpmItem Modul 0x04, Subop 2, Containerkennung 100, nested Move
  -> Server prueft Besitzer, Lock, Layer, Grid und bucht Containerposition
```

## Server-Datenbank-Inferenz

Wahrscheinliche Tabellen:

### `character_wallets`

- `character_id`
- `wallet_type`: `inventory`, `bank`
- `amount_low`, `amount_high` oder 64-bit `amount`
- `updated_at`

### `character_bank_slots`

- `character_id`
- `layer_index`
- `slot_count` oder `unlocked`
- `purchase_step`
- `purchased_at`

### `character_bank_items`

- `character_id`
- `item_id`
- `layer_index`
- `grid_x`
- `grid_y`
- `width`
- `height`
- `updated_at`

### `item_locks`

- `item_id`
- `lock_type`: `bank_move`, `trade`, `auction`, `repair`, `convert`
- `owner_character_id`
- `expires_at`

### `economic_ledger`

- `ledger_id`
- `character_id`
- `transaction_type`: `bank_deposit`, `bank_withdraw`, `bank_slot_buy`, `bank_item_move`
- `amount`
- `item_id`
- `before_inventory_money`
- `after_inventory_money`
- `before_bank_money`
- `after_bank_money`
- `created_at`

## Sicherheitsrelevante Serverregeln

- Geld-Delta nie blind anwenden. Richtung, Limit und Quelle/Ziel muessen aus serverseitigem Bankzustand kommen.
- Bankzugriff nur erlauben, wenn der Charakter beim passenden Bank-NPC/Event ist oder der Server eine gueltige Banksession fuehrt.
- Bank-Slot-Kauf muss anhand des aktuellen Serverzustands bepreist werden.
- Itemmove muss pruefen: Besitzer, Container, Gridplatz, Itemgroesse, Stackregeln, Lockstatus, equipped-Status, Trade/Auction/Repair/Convert-Status.
- Alle Bankoperationen sollten unter Character- und Item-Locks laufen.

## Noch offene Detailarbeit

- `AgpmItem` Modul `0x04` allgemein opcodeweise mappen; Bank nutzt nur einen Ausschnitt.
- Nested-Paket `AgpmItem + 0x38a00` bei `FUN_006ebcb0` disassemblieren, um Quelle/Ziel/Gridfelder exakt zu benennen.
- Server-Receive fuer Character Modul `0x02` Subop `7` suchen, um beide Geldrichtungen eindeutig zu benennen.
