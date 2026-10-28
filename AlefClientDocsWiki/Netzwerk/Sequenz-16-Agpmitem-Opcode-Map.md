# Winsock Sequenz 16: AgpmItem Opcode-Karte

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Diese Datei kartiert das allgemeine [`AgpmItem`](../Module/AgpmItem.md)-Netzwerkmodul, weil Bank, Inventory, Trade, Auction, Repair und Convert alle darauf aufbauen. Quellen sind `alefclient.pseudocode.c`. Bedeutungen sind statische Inferenz, keine Live-Traffic-Auswertung.

## Kurzfazit

- `AgpmItem` nutzt Modul-ID `0x04`.
- Das zentrale Layout fuer viele Itempakete liegt bei `AgpmItem + 0xec4`.
- Der Receive-Switch decodiert rund 29 Felder und dispatcht Subops `0..0x20`.
- Bank-Slot-Kauf ist sicher `AgpmItem` Subop `0x16`.
- Bank-Itembewegung nutzt sicher `AgpmItem` Subop `2` mit Containerkennung `100` und einem verschachtelten Move-Paket.
- Mehrere Itemsendefunktionen setzen den Subopcode in das Lowbyte eines ID-Feldes, typisch `CONCAT31(oldHighBytes, subop)`.

## Zentrales Receive-Layout

Der Parser um die `FUN_004e9fb0(AgpmItem + 0xec4, ...)`-Stelle decodiert:

```text
FUN_004e9fb0(AgpmItem + 0xec4, 1, packet, len,
             &subop,
             &local_58, &local_60, &local_5c, &characterId,
             &local_48, &local_4c, &local_54, &local_50,
             &local_30, &local_34, &local_38, &local_44,
             &local_14, &local_10, &local_4, &local_3c,
             &local_18, &local_28, &local_1c, &local_2c,
             &local_20, &local_8, &local_40, &local_24)
```

Danach:

- `characterId` wird mit `FUN_005035f0(characterId)` aufgeloest.
- Bei lokalem Empfang wird geprueft, ob die Message zum lokalen Charakter gehoert.
- Nach erfolgreicher Verarbeitung wird `FUN_004e7c30(0)` aufgerufen, falls ein Characterobjekt vorhanden ist.

## Receive-Subops

| Subop | Handler | Beobachtung |
|---:|---|---|
| `0` | `FUN_00541f30(...)` | nur wenn Kontextflag `*param_6 != 0`; voller Item-Create/Sync-artiger Datensatz |
| `1` | `FUN_0053faf0(...)` | voller Itemdatenblock, wahrscheinlich Add/Update |
| `2` | `FUN_00542a00(...)` + Callback `0x38` | Itemmove/-containerupdate; fuer Bank relevant |
| `3` | `FUN_0053eb40(...)` | Itemupdate mit Extra `local_44` |
| `4` | `FUN_00544420(...)` | Itemzustand/Container- oder Positionupdate |
| `5` | `FUN_0053b2b0(...)` | Callback `0x1d`, Character/Item-bezogen |
| `6` | `FUN_0053b3c0(...)` | Callback `0x20` bei gesetztem Itemstatus |
| `7` | `FUN_0053b410(...)` | Callback `0x21` |
| `8` | `FUN_0053b380(...)` | setzt Statusfeld `itemExt + 0x19c = 0` |
| `9` | `FUN_0053b330(..., 1)` | setzt Statusfeld `itemExt + 0x19c = 1`, Callback `0x1f` |
| `10` | `FUN_0053b330(..., 0)` | setzt Statusfeld `itemExt + 0x19c = 0`, Callback `0x1f` |
| `0x0b` | `FUN_00540670(...)` | Distanz/Position/Objektaktion |
| `0x0c` | `FUN_00541a30(...)` | Item-/Characterupdate |
| `0x0e` | `FUN_0053b430(...)` | Container/Grid-bezogene Aktion fuer Status `2`, `100`, `0x0d`, `0x0f` |
| `0x0f` | return `1` | Ack/no-op |
| `0x10` | `FUN_0053b5d0(...)` | Callback `0x1e` mit Itemobjekt |
| `0x11` | `FUN_005407f0(...)` | Itemstatus mit mehreren Parametern |
| `0x12` | `FUN_0053b610(...)` | setzt Timer `itemExt + 0x1b8`, Callback `0x46` |
| `0x13` | `FUN_0053b680(...)` | setzt Timer `itemExt + 0x1bc`, Callback `0x47` |
| `0x14` | `FUN_0053b6f0(...)` | loescht Timer `itemExt + 0x1bc`, Callback `0x48` |
| `0x15` | `FUN_0053ec90(...)` | Itemstatus/Result |
| `0x16` | `FUN_0058ec20(...)` | Bank-Slot-Kauf/Bankstatus im Bank-Kontext sicher relevant |
| `0x17` | `FUN_0053f880(...)` | Itemdatenupdate |
| `0x19` | `FUN_0053f8c0(...)` | Itemdatenupdate |
| `0x1a` | `FUN_0053ca90(...)` | Itemstatus mit `local_40` |
| `0x1b` | Callback `0x57` | nur wenn Kontextflag gesetzt; nutzt `(char)local_58` |
| `0x1c` | `FUN_00544310(...)` | Itemstatus/update |
| `0x1d` | `FUN_0053cb20(...)` | Itemstatus mit `local_40` |
| `0x1e` | `FUN_0053cba0(...)` | Itemstatus mit `local_2c`; besitzt eigenen Sendebuilder |
| `0x1f` | `FUN_00541c60(...)` | Itemstatus/update |
| `0x20` | `FUN_00542cc0(...)` | voller Datensatz wie Subop `0`, vermutlich erweiterter Sync |

Nicht sichtbarer Fall `0x0d`: Im Switch nicht als Handler vorhanden; bei unerwartetem Subop wird `AgpmCharacter::OnReceive() Error (19) !!!` ausgegeben. Die Layout-/Sendefunktionen kennen aber `0x0d` in Containerkontexten.

## Sendefunktionen

### `FUN_0053b7b0`: Subop `3`

```text
subop = 3
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, 0, item + 4, 0, item + 0x3c,
             ..., optionalExtra)
```

Wird mehrfach aus [`AgcmItem`](../Module/AgcmItem.md)-Wrappern gesendet. Enthalten sind Item-ID und ein Itemdatenblock bei `item + 0x3c`.

### `FUN_0053b8b0`: nested Move, Subop `0x11`

```text
nested = FUN_004ea280(AgpmItem + 0x260ec, 0, nestedLen, 0, ...)
outerSubop = 0x11
FUN_0053ab40(..., module 0x04, &outerSubop, item + 4, item + 0x3c, index, nested)
```

Interpretation:

- Komplexer Itemmove oder Split/Stack/Containerwechsel.
- Baut bewusst ein verschachteltes Unterpaket.

### `FUN_0053b9a0`: Subop `0x15`

```text
subop = 0x15
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, 0, &characterId, 0, &itemId, ...)
```

### `FUN_0053ba20`: Subop `0x16`

```text
subop = 0x16
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, 0, 0, 0, &characterId, ...)
```

Dieser Builder wird von `FUN_006ebec0(characterId)` gesendet und im Bank-UI-Kontext von `Item_BuyBankSlot` erreicht. Bedeutung: Bank-Slot kaufen/freischalten.

### `FUN_0053ba90`: Subop `0x17`

```text
subop = 0x17
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, 0, item + 4, 0, item + 0x3c, ...)
```

### `FUN_0053bb00`: Subop `0x1e`

```text
nested = FUN_004ea280(AgpmItem + 0xcd2a0, 0, outLen, 0, statusBlock)
subop = 0x1e
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, 0, &characterId, 0, &itemId, ..., nested)
```

Nur bei `*statusBlock == 0` oder `1`. Das ist ein Status-/Flagupdate mit verschachteltem Payload.

### `FUN_006ebcb0`: Bank-Move, Subop `2`

Bank-spezifischer Wrapper:

```text
nested = FUN_004ea280(AgpmItem + 0x38a00, 0, nestedLen, 0,
                      &arg0, &arg1, &arg2)

subop = 2
container = 100
FUN_004ea280(AgpmItem + 0xec4, 1, outLen, 0x04,
             &subop, &container, &characterId, 0,
             &bankLayer, ..., nested)
```

Dieser Pfad wird von `Item_BankDragDropItem` erreicht und ist der wichtigste bekannte Bank-Itemmove.

## Container-/Statuskennungen

`FUN_0053aff0` ordnet Container-/Statuswerte auf lokale Callbacks:

| Wert | Callback | Inferenz |
|---:|---:|---|
| `2` | `0x2c` | Inventar-/normaler Itemcontainer |
| `3` | `0x2d` | Equip/anderer Container |
| `6` | `0x2e` | Spezialcontainer |
| `7` | `0x2f` | Spezialcontainer |
| `100` | `0x31` | Bankcontainer sehr wahrscheinlich |
| `8` | `0x32` | Spezialcontainer |
| `0x0d` | `0x33` | Spezialcontainer |
| `0x0f` | `0x34` | Spezialcontainer |
| `0x33` | `0x50` | Spezialcontainer |

Bank-Relevanz:

- `100` taucht explizit in `FUN_006ebcb0` als Konstante auf.
- Deshalb ist `100` sehr wahrscheinlich Bank oder banknaher Containerstatus.

## Server-Datenbank-Inferenz

`AgpmItem` ist das zentrale Persistenzprotokoll fuer Iteminstanzen. Der Server braucht mindestens:

### `item_instances`

- `item_id`
- `owner_character_id`
- `template_id`
- `container_type`
- `container_slot_or_layer`
- `grid_x`
- `grid_y`
- `stack_count`
- `durability_current`
- `durability_max`
- `enhancement_level`
- `socket_count`
- `flags`

### `item_container_positions`

- `item_id`
- `character_id`
- `container_type`
- `container_index`
- `x`
- `y`
- `updated_at`

### `item_state_history`

- `item_id`
- `character_id`
- `opcode`
- `old_container`
- `new_container`
- `old_state`
- `new_state`
- `reason`
- `created_at`

## Warum das fuer andere Systeme wichtig ist

- Bank: nutzt `0x04` Subop `2` und `0x16`.
- PrivateTrade: verschiebt/lockt Items ueber `AgpmItem`-IDs und Containerstatus.
- Auction: Listing/Claim/Bid muessen Item-Containerstatus und Locks setzen.
- Repair: arbeitet auf Item-IDs und schreibt Haltbarkeit.
- Convert/Refinery/Product: verbrauchen und erzeugen Items, daher muessen ihre Resultate ueber Iteminstanzen/Container gebucht werden.

## Noch offene Detailarbeit

- Die Handler `FUN_00541f30`, `FUN_00542a00`, `FUN_0053faf0`, `FUN_0053eb40`, `FUN_00544420`, `FUN_00542cc0` sollten einzeln benannt werden.
- Nested Layouts `AgpmItem + 0x260ec`, `AgpmItem + 0x38a00`, `AgpmItem + 0xcd2a0` muessen feldweise extrahiert werden.
- Die Containerwerte `3`, `6`, `7`, `8`, `0x0d`, `0x0f`, `0x33` sollten gegen UI-Kontexte abgeglichen werden.
