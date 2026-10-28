# Winsock Sequenz 05: AgpmItem, Inventory, Equipment, Bank und Trade

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei dokumentiert den Item-/Inventory-Teil des Clientprotokolls. Grundlage sind [`AgpmItem`](../Module/AgpmItem.md), [`AgcmItem`](../Module/AgcmItem.md), UI-Bindings fuer Inventory/Equip/Bank/Trade und die statisch sichtbaren Send-/Receive-Pfade.

## Kurzfazit

- `AgpmItem` ist Modul-ID `0x04`.
- Hauptlayout fuer Item-Netzwerkpakete liegt bei `AgpmItem + 0xec4`.
- Der Client hat lokale Strukturen fuer:
  - Inventory
  - SubInventory
  - ExpandedInventoryA/B
  - Equipment
  - Bank
  - SalesBox
  - PrivateTradeGrid
  - PrivateTradeClientGrid
  - NPCTradeGrid
  - CashInventory
- Item-Serverpakete legen Items an, aktualisieren Itemdaten, verschieben Items zwischen Containern, equippen/unequippen Items und aktualisieren Options-/Rune-/Status-Blobs.
- Client->Server Sends gehen fast immer ueber `FUN_004e45d0(..., 0, 3, 0)`, also ueber den aktiven Game-/Worldsocket.

## AgpmItem Konstruktor und Modul-ID

### `FUN_00545380` (`0x00545380`)

Der Konstruktor initialisiert `AgpmItem`:

```c
strncpy(moduleName, "AgpmItem", 0x27);
FUN_004e4620(1);
FUN_004e4190(800, 0);
FUN_004e4190(0x340, 1);
FUN_004e4190(0x234, 3);
FUN_004e4540(4);
FUN_0053aab0();
```

Sicher:

- Modulname: `AgpmItem`
- Modul-ID: `0x04`
- lokale Objekt-/Poolgroessen: `800`, `0x340`, `0x234`
- danach werden viele `AuPacket`-Layouts registriert

## Wichtige Paketlayouts

### Hauptlayout `+0xec4`

Viele Builder und Receive-Pfade nutzen:

```c
FUN_004ea280(param_1 + 0xec4, 1, ..., 4, ...);
FUN_004e9fb0(param_1 + 0xec4, 1, packet, len, ...);
```

`+0xec4` ist damit das Hauptlayout fuer `AgpmItem` Modul `0x04`.

### Weitere Layouts

Aus dem Konstruktor:

| Offset | Layout | Beobachtung |
|---:|---|---|
| `+0x1770a * 4 = +0x5dc28` | `10,1` | einzelnes 64-bit/large value Feld |
| `+0x983b * 4 = +0x260ec` | `3,1, 3,1, 3,1` | Grid-Koordinaten oder Slotposition |
| `+0xe280 * 4 = +0x38a00` | `3,1, 3,1, 3,1` | weiteres Koordinatenlayout |
| `+0x12cc5 * 4 = +0x4b314` | `3,1, 3,1, 3,1` | weiteres Koordinatenlayout |
| `+0x4df6 * 4 = +0x137d8` | leer/Marker | verschachtelter leerer Block |
| `+0x1c14f * 4 = +0x7053c` | komplex | Haupt-Itemdatenblock/Item-Optionen |
| `+0x20b94 * 4 = +0x82e50` | `1,1,5,1,5,1,5,1` | kurzer Status-/ID-Block |
| `+0x255d9 * 4 = +0x95764` | fuenf `4,1` | Equip-/Socket-/Option-ID-Liste |
| `+0x2a01e * 4 = +0xa8078` | drei `4,1` | Rune-/Option-Subblock |
| `+0x2ea63 * 4 = +0xba98c` | `1,1,7,1,6,1,5,1,7,1` | Status-/Timer-/Bindungsblock |
| `+0x334a8 * 4 = +0xcd2a0` | `3,1` | kurzer Wertblock |
| `+0x37eed * 4 = +0xdfbb4` | String `0x40` | Text-/Name-/Customdatenblock |

Die Decompiler-Typen sind nicht benannt, aber die Verwendung zeigt, dass `+0x260ec`, `+0x38a00`, `+0x4b314` jeweils Tripel speichern. In Containerlogik werden diese Tripel als Grid-/Layer-/Slot-Koordinaten gelesen.

## Item-Objekt: wichtige Offsets

Aus `FUN_00541de0`, `FUN_00541f30`, Equip-/Gridfunktionen:

| Offset | Bedeutung |
|---:|---|
| `item + 0x04` | Item-Instanz-ID |
| `item + 0x30` | ItemTemplate-ID oder Template-Key |
| `item + 0x34` | Pointer auf ItemTemplate |
| `item + 0x3c` | Owner-ID / Character-ID des Besitzers |
| `item + 0x40` | Owner-Character-Pointer |
| `item + 0x4c` | Stackcount |
| `item + 0x50..0x58` | Positions-/World-Koordinaten oder Drop-Position |
| `item + 0x5c` | Grid/Factor/Position Block A |
| `item + 0xa0` | Grid/Factor/Position Block B |
| `item + 0xe4` | Grid/Factor/Position Block C |
| `item + 0x128` | Container-/Operation-Ort, aus Server-Op gesetzt |
| `item + 0x12a` | lokaler Containerstatus: Inventory/Equip/Bank/Trade/... |
| `item + 0x138..0x13c` | letzte Gridposition |
| `item + 0x13e..0x142` | vorherige/gespiegelte Gridposition |
| `item + 0x184..0x1a4` | Status-/Fehlertext, z.B. `Inventory:stackcount == 0` |
| `item + 0x1a8` | weiterer Statuswert |
| `item + 0x1b0..0x1b8` | bis zu 5 ushort IDs, vermutlich Socket/Option/Link-Items |
| `item + 0x220..0x230` | Pointer/aufgeloeste Objekte zu den IDs ab `0x1b0` |
| `item + 0x2fc..0x300` | kurzer 3-Wert-Subblock |
| `item + 0x302..0x318` | Status-/Timer-/Bindungsblock |

## Client->Server Item-Sends

### Basis-Builder in `AgpmItem`

#### `FUN_0053b7b0` (`0x0053b7b0`) - Operation `3`

```c
op = 3;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op,
                      0,
                      item + 4,     // Item-ID
                      0,
                      item + 0x3c,  // Owner/CID/String/ID-Kontext
                      ...
                      optional &param_4);
```

Interpretation:

- Client sendet eine itembezogene Aktion fuer ein existierendes Item.
- Da Op `3` serverseitig `FUN_0058fe50`/Equip-Logik ausloesen kann, ist dies wahrscheinlich Equip oder "Item an Character/Ort binden".

#### `FUN_0053b830` (`0x0053b830`) - Operation `0x0f`

```c
op = 0x0f;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op,
                      0,0,0,
                      &itemOrId,
                      &count,
                      ...);
```

Interpretation:

- Sendet Item-ID plus Count.
- Naheliegend: Stack split, drop count, use count oder consume count.

#### `FUN_0053b8b0` (`0x0053b8b0`) - Operation `0x11`

Diese Funktion baut zuerst ein Nested-Paket mit `+0x260ec`:

```c
grid = FUN_004ea280(AgpmItem + 0x260ec, 0, &len, 0,
                    &a, &b, &c);
op = 0x11;
packet = FUN_0053ab40(..., &op, item+4, 0, item+0x3c, &count, ..., grid, ...);
```

Interpretation:

- Itemaktion mit Ziel-Gridposition.
- Sehr wahrscheinlich Move/Split/DragDrop innerhalb von Inventory/Bank/Trade.

#### `FUN_0053b9a0` (`0x0053b9a0`) - Operation `0x15`

```c
op = 0x15;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op, 0, &param_3, 0, &param_2, ...);
```

Interpretation:

- Itemaktion mit zwei IDs/Werten.
- Naheliegend: pickup, trade add/remove, or container transfer.

#### `FUN_0053ba20` (`0x0053ba20`) - Operation `0x16`

```c
op = 0x16;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op, 0,0,0, &param_2, ...);
```

Interpretation:

- Einfache Itemaktion mit einer ID.
- Wird in `FUN_006ebec0` direkt gesendet.

#### `FUN_0053ba90` (`0x0053ba90`) - Operation `0x17`

```c
op = 0x17;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op, 0, item+4, 0, item+0x3c, ...);
```

Interpretation:

- Itemaktion fuer bestehendes Item plus Owner-Kontext.

#### `FUN_0053bb00` (`0x0053bb00`) - Operation `0x1e`

```c
nested = FUN_004ea280(AgpmItem + 0xcd2a0, 0, &len, 0, param_4);
op = 0x1e;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op, 0, &param_3, 0, &param_2,
                      ..., nested, ...);
```

Interpretation:

- Itemaktion mit kurzem Zusatzwert.
- Bedingung erlaubt nur `*param_4 == 0` oder `1`; wahrscheinlich bool/slot-state.

### AgcmItem-Sends

`AgcmItem` liegt als Client-/UI-Schicht ueber `AgpmItem`.

#### Konstruktor `FUN_006eb4d0` (`0x006eb4d0`)

Setzt Modulname `AgcmItem`, speichert globale Referenz `DAT_00c307d8` und verwaltet UI-/Render-/Clientdaten. Wichtige Referenzen:

- `AgcmItem + 0xc5c`: Pointer auf `AgpmItem`
- `AgcmItem + 0xc68`: Pointer auf `AgcmCharacter` oder Character-Kontext
- `AgcmItem + 0xc9a/+0xc9c`: lokale Attach-/Item-Modulextension IDs

#### `FUN_006ebbb0`

```c
main op = 2;
sub op/local_6 = 3;
nested = FUN_004ea280(AgpmItem + 0x137d8, 0, &len, 4);
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op2, &sub3, itemId, 0, ownerId, ..., nested);
FUN_004e45d0(packet, len, 0, 3, 0);
```

Interpretation:

- Item-Hauptoperation `2`, Untertyp `3`.
- Wahrscheinlich Equip/Use/Move-Aktion mit leerem Zusatzblock.

#### `FUN_006ebcb0`

```c
main op = 2;
sub op/local_6 = 100;
nested = FUN_004ea280(AgpmItem + 0x38a00, 0, &len, 0, &x, &y, &z);
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op2, &sub100, &param_2, 0, &param_3, ..., nested);
```

Interpretation:

- Item-Hauptoperation `2`, Untertyp `100`.
- Enthält Zielkoordinaten/Tripel.
- Naheliegend: Item in speziellen Container/Bank/Cash/Avatar-Set verschieben.

#### `FUN_006ebde0` - Operation `0x0b`

```c
op = 0x0b;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op, 0, &param_2, 0, &param_3, ...);
```

Interpretation:

- einfache Itemaktion mit zwei IDs.
- Wird aus Autopickup-/Nahe-Item-Pfaden erreicht.

#### `FUN_006ebf30` - Operation `6`

```c
op = 6;
packet = FUN_004ea280(AgpmItem + 0xec4, 1, &len, 4,
                      &op, 0,0,0, localChar + 4, ...);
```

Interpretation:

- Charakterbezogene Itemaktion, ausgelost wenn `local inventory state +0x19c != 0`.
- Wahrscheinlich Pickup/auto-pickup oder Itemstatus-Abfrage.

## UI-Ausloeser

[`AgcmUIItem`](../Module/AgcmUIItem.md) bindet sehr viele UI-Callbacks:

| UI-Funktion | Beobachtung |
|---|---|
| `Inventory_MoveItem` | Drag/Move im Inventory |
| `Inventory_MoveEndItem` | Abschluss einer Move-Aktion |
| `Inventory_UseItem` | Item benutzen |
| `Inventory_DragDropItem` | Drag/Drop Item |
| `InventoryWaste_DragDropItem` | Item wegwerfen/Trash |
| `Equip_MoveItem` | Equipment-Slot bewegen |
| `Equip_DragDropBase` | Drag/Drop auf Equipment |
| `Equip_DoubleClick` | Equip/Unequip per Doppelklick |
| `SubInventory_*` | weitere Inventory-Layer |
| `ExpandedInventoryA/B_*` | erweiterte Inventory-Slots |
| `NPCT_MoveItem` | NPC Trade |
| `Bank_MoveItem` | Bank/Grid |
| `Item_RequestBuyBankSlot` | Bank-Slot kaufen anfragen |
| `Item_BuyBankSlot` | Bank-Slot kaufen bestaetigen |
| `Item_BankDragDropItem` | Drag/Drop in Bank |
| `ItemAutoPickup` | Auto-Pickup |
| `PT_RequestTrade` | Private Trade Request |

Diese UI-Funktionen landen nicht immer direkt im Netzwerkbuilder; haeufig pruefen sie zuerst lokale Zustandsregeln und rufen dann `AgcmItem`/`AgpmItem`-Builder auf.

## Server->Client: Item Receive

Der sichtbare Kern liegt in `FUN_00541f30` und `FUN_00542a00`.

### `FUN_00542a00`

Wrapper:

```c
item = FUN_00592680(itemId);
if (item exists)
    FUN_00540d80(... existing item update ...);
else if (templateOrItemData)
    FUN_00541f30(... add item ...);
```

Bedeutung:

- Wenn Item-Instanz existiert: aktualisieren.
- Wenn nicht: neu anlegen.

### `FUN_00541de0` - Item anlegen

```c
item = FUN_0053dc40();
item->id = itemId;
item->templateId = templateKey;
item->template = resolvedTemplate;
item->stackCount = min(requestedCount, template.maxStack);
item->owner = owner/context;
copy template factors to item;
FUN_004e4070(1, item, 0);
```

Sicher:

- Item-Instanz-ID und Template-ID sind getrennt.
- Stackcount wird gegen Template-Maximum begrenzt.
- Template-Factor/Position-Daten werden in die Iteminstanz kopiert.
- Event `1` bedeutet "Item hinzugefuegt".

### `FUN_00541f30` - grosses Add/Update mit Serverdaten

Diese Funktion verarbeitet Itemdaten aus dem Serverpaket:

- legt Item ggf. an
- setzt Owner/Character
- setzt Container-/Operationstyp in `item +0x128`
- setzt Stackcount
- verarbeitet optionale Blobs:
  - Factor/Option Block nach `item +0x5c`
  - zweiter Factor/Option Block nach `item +0xa0`
  - dritter Factor/Option Block nach `item +0xe4`
  - Socket-/Linked-Item IDs nach `item +0x1b0..0x1b8`
  - Rune-/Optionblock nach `item +0x2fc..0x300`
  - Status-/Timer-/Bindungsblock nach `item +0x302..0x318`
  - String/Customblock nach Event `0x65`

Danach entscheidet ein Switch anhand der Operation, wohin das Item gehoert.

## Server-Operationen im Item-Switch

| Op | Sichtbarer Effekt | Interpretation |
|---:|---|---|
| `0x00` | kein Spezialpfad nach Add | Item allgemein anlegen/aktualisieren |
| `0x01` | `FUN_00590100`, Event `8`, `0x3d` | Item in Welt/Drop/Spawn setzen |
| `0x02` | `FUN_0058cce0` mit Gridtripel | Item in Inventory/Container bewegen |
| `0x03` | `FUN_0058fe50` | EquipItem |
| `0x06` | `FUN_0058ffe0` | Item in Containerstatus `6` |
| `0x07` | `FUN_0058feb0` | Item in Containerstatus `7` |
| `0x08` | `FUN_0058ed00`, danach Stack/Owner update | SalesBox/Trade/Grid-Status `8` |
| `0x0c` | `FUN_006cfc60` mit `+0x4b314` Tripel | Sondercontainer/Bank/Cash/Trade |
| `0x0d` | `FUN_0058e490` | Bank/Containerstatus `0x0d` |
| `0x0e` | Event `0x30` mit Character/Item | Pickup/Notify/Item-to-character Event |
| `0x0f` | `FUN_0058df00` | Inventory/Grid-Status `0x0f` |
| `0x33` | `FUN_0058d3a0` | Spezialitem/Avatar/Cash/Pet-artiger Status |
| `0x35` | Event `0x55`, `FUN_0053ea60` | Move/Update mit Gridtripel |
| `0x64` (`'d'`) | `FUN_0058e740` | hoher Sonderstatus, vermutlich Cash/Bank/Eventcontainer |

Die Operationen `0x02`, `0x06`, `0x07`, `0x0d`, `0x0f`, `0x35`, `0x64` nutzen Grid- oder Containertripel. Das bestaetigt, dass der Server nicht nur "Item exists" sendet, sondern den konkreten Containerplatz.

## Container und lokale Statuswerte

Die Itemfunktionen setzen `item +0x12a` auf verschiedene Werte. Aus Debugstrings und UI-Bindings:

| Status | Beobachtung | Bedeutung |
|---:|---|---|
| `1` | `FUN_00590100`, Weltposition/Event `0x3d` | Welt-/Drop-Item |
| `2` | Inventory-Funktionen, Stackcount | Inventory |
| `3` | `EquipItem()` | Equipped |
| `6` | `FUN_0058ffe0` | ClientTrade/Trade-Container |
| `7` | `FUN_0058feb0` | Trade-/ClientTrade-Variante |
| `8` | SalesBox/TradeGrid Entfernen | SalesBox oder TradeGrid |
| `0x0d` | Bank-Funktionen | Bank |
| `0x0f` | weiterer Bank/SubInventory/Cash-Status | Sonderinventory |
| `0x33` | UI-/Avatar-/Spezialstatus | Avatar/Cash/Spezial |
| `100` | Bank/temporärer Status in `FUN_0058e9f0` | Bank-Zwischenstatus |
| `0xffff` | entfernt/kein Container | removed/unassigned |

## Inventory/Grid-Funktionen

### Inventory

Debugstrings:

- `Inventory:stackcount == 0`
- `AgpmItem::RemoveItemFromInventory() Error`

Relevante Funktionen:

- `FUN_0058c930`: entfernt Item aus Inventory, setzt `item +0x12a = 0xffff`, reduziert Geld-/Stack-Zaehlungen und feuert Event `0x4d`.
- `FUN_0058cce0`: fuegt Item in Inventory/Grid ein, ggf. mit Koordinaten.
- `FUN_0058cbb0`: prueft Itemnutzung/Container und ruft Insert-Funktionen.

### Equipment

Debugstrings:

- `AgpmItem::EquipItem() Error`
- `AgpmItem::UnEquipItem() Error`
- UI-Events `EquipStatusHeadOn`, `EquipStatusWeaponOn`, usw.

Relevante Funktionen:

- `FUN_0058fe50`: Wrapper fuer Equip.
- `FUN_0058ef30`: eigentliche Equip-Validierung.
- `FUN_0058f530`: UnEquip.

Equipment-Slots werden ueber Werte `2..0x1e` gesucht:

```c
FUN_0058ee40(character, slotId)
```

Sichtbare UI-Slots:

- Head
- Hands
- Body
- Legs
- Foot
- Shield
- Weapon
- Ring1
- Ring2
- Necklace
- Ride
- Lancer

### Bank

Debugstrings/UI:

- `Bank_OpenUI`
- `Bank_CloseUI`
- `Bank_ItemUpdate`
- `BankGrid`
- `BankMoney`
- `BankLayerIndex`
- `Item_RequestBuyBankSlot`
- `Item_BuyBankSlot`
- `BankSlotFull`

Relevante Funktionen:

- `FUN_0058e890`: `RemoveItemFromBank`
- `FUN_0058e9f0`: Bank-/Sondercontainer-Insert
- `FUN_006bf280`, `FUN_006bf200` als UI-Callbacks fuer BankSlot-Kauf, noch nicht tief zerlegt

### Trade

Debugstrings/UI:

- `PrivateTradeGrid`
- `PrivateTradeClientGrid`
- `PrivateTradeGhelld`
- `PT_RequestTrade`
- `PTMSG_TradeComplete`
- `PTMSG_TradeCancel`
- `Item_TradeFailForBoundItem`
- `Item_TradeFailForUsingCashItem`
- `CannotTradeCashItem`
- `OP_RefuseTrade`

Relevante Funktionen:

- `FUN_0058ff60`: `RemoveItemFromClientTradeGrid`
- `FUN_005900a0`: `RemoveItemFromTradeGrid`
- `FUN_0058ffe0` / `FUN_0058feb0`: setzen Trade-nahe Containerstatuswerte `6` und `7`

## Lokale Item-Templates

Lokale Datenquellen:

- `Ini\\ItemTemplate`
- `INI\\ItemTemplate\\%08d.ini`
- `Ini\\%sItemOptionTable.txt`
- `Ini\\%sItemRuneAttributeTable.txt`
- `ini_tradeBlockItems.txt`
- `INI\\ItemEvolutionTable.txt`

Das heisst:

- Der Server muss nicht jeden statischen Itemwert senden.
- Der Server sendet mindestens ItemTemplate-ID plus dynamische Instanzdaten.
- Client loest Template-ID lokal gegen ItemTemplate/Option/Rune-Tabellen auf.
- Dynamische Werte wie Stackcount, Besitzer, Gridposition, Bindung, Sockets, Runen, Timer und Status kommen vom Server.

## Was wird wann gesendet?

| Zeitpunkt/Ausloeser | Client-Funktion | Paket |
|---|---|---|
| Item benutzen/equippen/kontextbezogen aktivieren | `FUN_0053b7b0`, `FUN_006ebbb0` | `AgpmItem` Op `3` oder Haupt-Op `2/Sub3` |
| Item mit Menge bewegen/teilen/droppen | `FUN_0053b830` | `AgpmItem` Op `0x0f`, Item/Count |
| Item auf Zielgrid bewegen | `FUN_0053b8b0` | `AgpmItem` Op `0x11`, Nested Gridtripel |
| Itemaktion mit zwei IDs | `FUN_0053b9a0` | `AgpmItem` Op `0x15` |
| einfache Itemaktion | `FUN_0053ba20` / `FUN_006ebec0` | `AgpmItem` Op `0x16` |
| Itemaktion mit Owner-Kontext | `FUN_0053ba90` | `AgpmItem` Op `0x17` |
| bool/kurzer Zusatzwert | `FUN_0053bb00` | `AgpmItem` Op `0x1e` |
| Pickup/nahe Itemaktion | `FUN_006ebde0`, `FUN_006ebf30` | `AgpmItem` Op `0x0b` oder `0x06` |
| Spezialmove mit Koordinaten | `FUN_006ebcb0` | `AgpmItem` Haupt-Op `2`, Sub `100`, Nested Koordinaten |

## Was sendet der Server?

Server sendet `AgpmItem` Pakete, die:

- Iteminstanzen neu anlegen
- vorhandene Iteminstanzen aktualisieren
- Items entfernen
- Stackcounts korrigieren
- Containerstatus setzen
- Gridpositionen setzen
- Equip/Unequip bestaetigen
- Bank-/Trade-/SalesBox-Status setzen
- Options-/Rune-/Socket-Blobs mitsenden
- Tradeblock/Bind-/CashItem-Status durchsetzen

Der Client fuehrt nach Serverpaketen lokale Events aus, z.B. UI refresh, Equipstatusanzeigen, InventoryFull/BankSlotFull-Meldungen, TradeComplete/TradeCancel.

## Server-Datenbank: belastbare Ableitungen

### `item_templates`

Viele Template-Daten sind lokal vorhanden, muessen serverseitig aber ebenfalls existieren.

| Feld | Grund |
|---|---|
| `template_id` | Client laedt `ItemTemplate\\%08d.ini` |
| `name` | Drop-/UI-Strings, Tooltipdaten |
| `type` | `template +0x8c`, `+0x2a8`, `+0x2ac`, `+0x2d0` steuern Container/Equipregeln |
| `max_stack` | `item +0x4c` wird gegen Template-Maximum begrenzt |
| `equip_slot` | Head/Body/Weapon/Ring usw. |
| `bind_rule` | `Item_Bind_On_Equip`, Tradeblock |
| `cash_flag` | `CannotTradeCashItem`, CashInventory |
| `option_group_id` | ItemOptionTable |
| `rune_group_id` | ItemRuneAttributeTable |

### `character_items`

Persistente Iteminstanzen.

| Feld | Grund |
|---|---|
| `item_id` | `item +0x04` |
| `character_id` | `item +0x3c`, Owner-Kontext |
| `template_id` | `item +0x30` |
| `stack_count` | `item +0x4c` |
| `container_type` | `item +0x12a` |
| `slot_layer` | Gridtripel |
| `slot_x` | Gridtripel |
| `slot_y` | Gridtripel |
| `bound_state` | Trade-/Bind-/Cash-Regeln |
| `created_at`, `updated_at` | Server muss Itemmutationen persistieren |

### `character_equipment`

Kann als View auf `character_items` oder eigene Tabelle existieren.

| Feld | Grund |
|---|---|
| `character_id` | Equip gehoert Character |
| `slot_id` | `FUN_0058ee40(character, slotId)` |
| `item_id` | Iteminstanz |
| `equipped_at` | Bind-on-equip/Status |

### `character_bank_items`

| Feld | Grund |
|---|---|
| `account_id` oder `character_id` | Bank kann account- oder characterweit sein |
| `item_id` | Iteminstanz |
| `bank_layer` | `BankLayerIndex` |
| `slot_x`, `slot_y` | Gridtripel |
| `stack_count` | Stack |

### `trade_sessions`

| Feld | Grund |
|---|---|
| `trade_id` | PrivateTrade braucht Session |
| `character_a_id`, `character_b_id` | zwei Partner |
| `state` | request, open, locked, accepted, canceled, completed |
| `money_a`, `money_b` | `PrivateTradeGhelld`, `PrivateTradeClientGhelld` |
| `created_at`, `updated_at` | Sessionzustand |

### `trade_session_items`

| Feld | Grund |
|---|---|
| `trade_id` | Tradecontainer |
| `item_id` | Iteminstanz |
| `owner_character_id` | urspruenglicher Besitzer |
| `side` | eigener/Client-TradeGrid |
| `slot_x`, `slot_y` | Gridposition |
| `locked_snapshot` | verhindert Itemaenderung nach Accept |

### `item_dynamic_options`

| Feld | Grund |
|---|---|
| `item_id` | Instanz |
| `option_slot` | Blobs bei `+0x1b0..0x1b8`, `+0x2fc..0x300` |
| `option_id` | OptionTable |
| `value` | Optionswert |
| `expires_at` | Status-/Timerblock `+0x302..0x318` |

### `item_runes`

| Feld | Grund |
|---|---|
| `item_id` | Instanz |
| `rune_slot` | RuneAttributeTable |
| `rune_id` | Rune-ID |
| `attribute_id` | Rune-Attribut |
| `value` | dynamische Staerke |

## Validierung / Serverautoritaet

Der Server muss bei Itempaketen sehr streng validieren:

- Item-ID gehoert zur Socket-Session/Character-ID.
- Template-ID passt zur existierenden Iteminstanz.
- Stackcount darf nicht clientseitig erhoeht werden.
- Move-Zielslot muss frei und gueltig sein.
- Itemgroesse muss ins Zielgrid passen.
- Equipment-Slot muss zum Itemtyp passen.
- Klasse/Rasse/Level/Statusanforderungen muessen passen.
- Bound/Cash/Tradeblock-Regeln muessen vor Trade/Bank/SalesBox greifen.
- Trade darf Items nach Lock/Accept nicht mehr veraendern.
- Bank-Slot-Kauf muss Geld und Slotlimit serverseitig pruefen.
- Drop/Pickup muss Weltposition, Distanz und Ownership/Lootrechte pruefen.

## Noch offen

- `FUN_0053aab0` sollte separat zerlegt werden, um das Hauptlayout `+0xec4` bytegenau zu mappen.
- UI-Callbacks `FUN_0078bb10`, `FUN_0078b610`, `FUN_0078b6b0`, `FUN_006d47d0`, `FUN_006d48c0` sollten einzeln zurueckverfolgt werden, um jede Nutzeraktion einem Paketbuilder zuzuordnen.
- Bank-Slot-Kauf (`FUN_006bf280`, `FUN_006bf200`) ist noch nicht auf Paketebene dokumentiert.
- Trade/PrivateTrade hat eigene Module ([`AgcmPrivateTrade`](../Module/AgcmPrivateTrade.md), [`AgpmEventNPCTrade`](../Module/AgpmEventNPCTrade.md)) und sollte als eigene Sequenz folgen.

## Relevante Funktionen

| Funktion | Adresse | Rolle |
|---|---:|---|
| `FUN_00545380` | `0x00545380` | `AgpmItem` Konstruktor, Modul `0x04`, Layouts |
| `FUN_006eb4d0` | `0x006eb4d0` | `AgcmItem` Konstruktor |
| `FUN_0053b7b0` | `0x0053b7b0` | Item Send Op `3` |
| `FUN_0053b830` | `0x0053b830` | Item Send Op `0x0f`, Item/Count |
| `FUN_0053b8b0` | `0x0053b8b0` | Item Send Op `0x11`, Nested Grid |
| `FUN_0053b9a0` | `0x0053b9a0` | Item Send Op `0x15` |
| `FUN_0053ba20` | `0x0053ba20` | Item Send Op `0x16` |
| `FUN_0053ba90` | `0x0053ba90` | Item Send Op `0x17` |
| `FUN_0053bb00` | `0x0053bb00` | Item Send Op `0x1e`, kurzer Nested-Wert |
| `FUN_006ebbb0` | `0x006ebbb0` | AgcmItem Send Haupt-Op `2`, Sub `3` |
| `FUN_006ebcb0` | `0x006ebcb0` | AgcmItem Send Haupt-Op `2`, Sub `100`, Koordinaten |
| `FUN_006ebde0` | `0x006ebde0` | AgcmItem Send Op `0x0b` |
| `FUN_006ebf30` | `0x006ebf30` | AgcmItem Send Op `6` |
| `FUN_00542a00` | `0x00542a00` | Item Receive Wrapper |
| `FUN_00541de0` | `0x00541de0` | Iteminstanz anlegen |
| `FUN_00541f30` | `0x00541f30` | grosser Server-Add/Update-Switch |
| `FUN_0058c930` | `0x0058c930` | RemoveItemFromInventory |
| `FUN_0058fe50` | `0x0058fe50` | EquipItem Wrapper |
| `FUN_0058ef30` | `0x0058ef30` | EquipItem Validierung |
| `FUN_0058f530` | `0x0058f530` | UnEquipItem |
| `FUN_0058e890` | `0x0058e890` | RemoveItemFromBank |
| `FUN_0058ff60` | `0x0058ff60` | RemoveItemFromClientTradeGrid |
| `FUN_005900a0` | `0x005900a0` | RemoveItemFromTradeGrid |
