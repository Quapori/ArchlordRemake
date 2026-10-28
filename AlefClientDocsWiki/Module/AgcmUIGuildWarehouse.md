# AgcmUIGuildWarehouse (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIGuildWarehouse` (Gilden-Lager: Fenster, Gegenstände und Geld ein- und auslagern, Lager erweitern) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Übersetzungseinheit-Reihenfolge und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIGuildWarehouse/AgcmUIGuildWarehouse.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 42 von 45 Quellmethoden sind zugeordnet; in diesem Durchgang kamen elf hinzu (`Open`, `SetGrid`, die sechs `Send…`, `AddEvent`, `OnItemMovedIn`, `OnItemMovedOut`), jeweils anhand der Übersetzungseinheit-Reihenfolge und des Dekompilats.
- **Pakete:** Operationen 1, 2, 3/4, 5, 6, 7 über Typ `0x54` wie in der Quelle.
- **UI-Schnittstelle:** 6 Funktionen, 3 Anzeigen, 6 Boolean-Werte (Anzahl wie in der Quelle), 2 Ereignisse `GWARE_OPEN` und `GWARE_CLOSE`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIGuildWarehouse.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00695030` | 750 | vtable/String |
| 1 | `OnInit` | – | | nicht zugeordnet (Debug-Code, klein oder eingefaltet) |
| 2 | `TestOpen` | – | | nicht zugeordnet (Debug-Code, klein oder eingefaltet) |
| 3 | `Open` | `0x00693B50` | 124 | ver |
| 4 | `SetGrid` | `0x00693BD0` | 106 | ver |
| 5 | `OnItemMovedIn` | `0x006947F0` | 168 | ver |
| 6 | `OnItemMovedOut` | `0x006948A0` | 329 | ver |
| 7 | `CBSetSelfCharacter` | `0x00693C40` | 76 | Callback-Registrierung |
| 8 | `CBReleaseSelfCharacter` | `0x00693C90` | 46 | Callback-Registrierung |
| 9 | `CBBaseInfo` | `0x00693CC0` | 99 | Callback-Registrierung |
| 10 | `CBOpenResult` | `0x00693D30` | 42 | Callback-Registrierung |
| 11 | `CBExpandResult` | `0x006949F0` | 152 | Callback-Registrierung |
| 12 | `CBItemMovedToInventory` | `0x00694A90` | 85 | Callback-Registrierung |
| 13 | `CBSelfUpdatePosition` | `0x00694AF0` | 137 | Callback-Registrierung |
| 14 | `CBAddItemToGuildWarehouse` | `0x00693D60` | 172 | Callback-Registrierung |
| 15 | `CBRemoveItemFromGuildWarehouse` | `0x00693E10` | 96 | Callback-Registrierung |
| 16 | `CBGrant` | `0x00694B80` | 204 | Callback-Registrierung |
| 17 | `CBKeydownESC` | `0x00693E70` | 25 | Callback-Registrierung |
| 18 | `CBMoveItem` | `0x00694C50` | 127 | UI-Registrierung |
| 19 | `CBClickLayer` | `0x00693E90` | 107 | UI-Registrierung |
| 20 | `CBClickMoneyIn` | `0x00693F00` | 77 | UI-Registrierung |
| 21 | `CBClickMoneyOut` | `0x00693F50` | 77 | UI-Registrierung |
| 22 | `CBClickMoneyConfirm` | `0x00694CD0` | 95 | UI-Registrierung |
| 23 | `CBClickExpansion` | `0x00694D30` | 261 | UI-Registrierung |
| 24 | `CBDisplayCaption` | `0x00694E40` | 118 | UI-Registrierung |
| 25 | `CBDisplayMoney` | `0x00693FA0` | 78 | UI-Registrierung |
| 26 | `CBDisplayMoneyConfirm` | `0x00693FF0` | 66 | UI-Registrierung |
| 27 | `CBIsActiveMoneyInButton` | `0x00694040` | 44 | UI-Registrierung |
| 28 | `CBIsActiveMoneyOutButton` | `0x00694070` | 44 | UI-Registrierung |
| 29 | `CBIsActiveExpandSlot` | `0x006940A0` | 85 | UI-Registrierung |
| 30 | `CBIsActiveSlot1` | `0x00694100` | 55 | UI-Registrierung |
| 31 | `CBIsActiveSlot2` | `0x00694140` | 55 | UI-Registrierung |
| 32 | `CBIsActiveSlot3` | `0x00694180` | 55 | UI-Registrierung |
| 33 | `SendOpen` | `0x006941C0` | 155 | ver |
| 34 | `SendClose` | `0x00694260` | 155 | ver |
| 35 | `SendItemIn` | `0x00694300` | 180 | ver |
| 36 | `SendItemOut` | `0x006943C0` | 182 | ver |
| 37 | `SendMoneyChange` | `0x00694480` | 164 | ver |
| 38 | `SendExpandSlot` | `0x00694530` | 155 | ver |
| 39 | `GetMessageTxt` | – | | nicht zugeordnet (Debug-Code, klein oder eingefaltet) |
| 40 | `AddEvent` | `0x006945D0` | 67 | ver |
| 41 | `AddFunction` | `0x00694EC0` | 249 | Zeichenkette |
| 42 | `AddDisplay` | `0x00694FC0` | 104 | Zeichenkette |
| 43 | `AddUserData` | `0x00694620` | 212 | Zeichenkette |
| 44 | `AddBoolean` | `0x00694700` | 179 | Zeichenkette |

42 von 45 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIGuildWarehouse` (`0x00693AC0`), `~AgcmUIGuildWarehouse` (`0x006947C0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBAC` | `Zeiger auf [`AgpmGuildWarehouse`](AgpmGuildWarehouse.md)` | `+0xB98` ist dessen Paketdefinition (`Send…`) |
| `0xBB4` | `Zeiger auf `AgcmCharacter`` | `+0x1596C` ist der Self-Character (`OnItemMovedIn`) |
| `0xBD0 / 0xBD4` | `Ereignis-IDs GWARE_OPEN / GWARE_CLOSE` | `AddEvent`, `Open` |
| `0xBD8` | `Zeiger auf das Lager-Grid` | `SetGrid` (`+0x4C` im Lagerobjekt) |
| `0xC04` | `Flag „Grid gesetzt“` | `SetGrid` |
| `0xC0C` | `Flag „Fenster offen“` | `Open` |

## Adressbereich

`AgcmUIGuildWarehouse.cpp` liegt im Binary zusammenhängend bei `0x00693AC0`–`0x00695030` (`OnAddModule` zuletzt).

## Pakete an den Server (Typ 0x54)

Alle Sender bauen Pakete des Typs `0x54` (84) mit `MakePacket` (`0x004EA2D0`) über die Paketdefinition des Moduls `AgpmGuildWarehouse` (`+0xB98` hinter dem Modulzeiger bei `+0xBAC`). Das erste Byte ist die Operation; die Werte entsprechen `eAGPMGUILDWAREHOUSE_OPERATION` der Quelle:

| Sender | Adresse | Operation |
|---|---|---|
| `SendOpen` | `0x006941C0` | 1 OPEN |
| `SendClose` | `0x00694260` | 2 CLOSE |
| `SendMoneyChange` | `0x00694480` | 3 MONEY_IN bzw. 4 MONEY_OUT (je nach Parameter) |
| `SendItemIn` | `0x00694300` | 5 ITEM_IN |
| `SendItemOut` | `0x006943C0` | 6 ITEM_OUT |
| `SendExpandSlot` | `0x00694530` | 7 EXPAND |

Die Operation 0 (BASE_INFO) kommt vom Server und löst `CBBaseInfo` aus.

## Gegenstand ein- und auslagern

`OnItemMovedIn` (`0x006947F0`) sendet nur, wenn der Gegenstand im Inventar, Unter-Inventar oder Chargen-Inventar liegt (Status 2, 0xD, 0xF), keine Ablaufzeit hat, das Zielfeld frei ist und der Gegenstand nicht gebunden ist (`GetBoundType`). `OnItemMovedOut` (`0x006948A0`) verlangt Status `0x35` (Gilden-Lager) und prüft je Zielinventar, ob es nicht voll und das Zielfeld frei ist. Beides entspricht der Quelle.

## Callback-Registrierung in OnAddModule (0x00695030)

Die elf Registrierungen stehen im Binary in der Reihenfolge der Quelle (11 von 11); alle Handler sind bereits benannt.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00694EC0`, `0x00694FC0`, `0x00694620`, `0x00694700`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (6)

| Name | Id | Handler |
|---|---:|---|
| `GWARE_MOVEITEM` |  | `CBMoveItem` |
| `GWARE_ClickLayer` |  | `CBClickLayer` |
| `GWARE_MONEY_IN` |  | `CBClickMoneyIn` |
| `GWARE_MONEY_OUT` |  | `CBClickMoneyOut` |
| `GWARE_MONEY_CONF` |  | `CBClickMoneyConfirm` |
| `GWARE_EXPAND` |  | `CBClickExpansion` |

**Anzeige** (3)

| Name | Id | Handler |
|---|---:|---|
| `GWARE_CAPTION` | 0 | `CBDisplayCaption` |
| `GWARE_MONEY` | 0 | `CBDisplayMoney` |
| `GWARE_CONFIRM` | 0 | `CBDisplayMoneyConfirm` |

**UserData** (5)

| Name | Id | Handler |
|---|---:|---|
| `GWARE_Grid` |  | – |
| `GWARE_LayerIndex` |  | – |
| `GWARE_Money` |  | – |
| `GWARE_ACTIVE_BTN` |  | – |
| `GWARE_DUMMY` |  | – |

**Boolean** (6)

| Name | Id | Handler |
|---|---:|---|
| `GWARE_ACT_MONEYIN` |  | `CBIsActiveMoneyInButton` |
| `GWARE_ACT_MONEYOUT` |  | `CBIsActiveMoneyOutButton` |
| `GWARE_ACT_EXPAND` |  | `CBIsActiveExpandSlot` |
| `GWARE_ACT_SLOT1` |  | `CBIsActiveSlot1` |
| `GWARE_ACT_SLOT2` |  | `CBIsActiveSlot2` |
| `GWARE_ACT_SLOT3` |  | `CBIsActiveSlot3` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`Open`, `SetGrid`, `Send…`, `OnItemMovedIn`, `OnItemMovedOut`, `CBMoveItem`).

## Grenzen

- Drei Methoden sind nicht zugeordnet: `OnInit` und `TestOpen` haben in der Quelle nur im Debug-Build Inhalt (`OnInit` ist im Release ein `return TRUE`), `GetMessageTxt` ist klein.
- Die Handler wurden nur auf Struktur und Operationen geprüft, nicht Zeile für Zeile.
- Die Paketfelder stehen im Bericht des Moduls `AgpmGuildWarehouse`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht als eigene Funktion: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmGuildWarehouse`](AgpmGuildWarehouse.md)
