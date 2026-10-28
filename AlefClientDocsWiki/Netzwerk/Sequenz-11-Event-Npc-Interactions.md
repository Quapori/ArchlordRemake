# Winsock-Sequenz 11: Event-, NPC- und Interaktionssystem

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei dokumentiert den generischen Event-Hub und die wichtigsten NPC-/Event-Interaktionen im `alefclient.exe`. Quellen sind `alefclient.pseudocode.c`, besonders [`ApmEventManager`](../Module/ApmEventManager.md), [`AgcmEventManager`](../Module/AgcmEventManager.md), `AgpmEventNPCDialog`, [`AgcmEventNPCDialog`](../Module/AgcmEventNPCDialog.md), [`AgpmEventNPCTrade`](../Module/AgpmEventNPCTrade.md), `AgcmEventNPCTrade`, [`AgpmEventTeleport`](../Module/AgpmEventTeleport.md) und [`AgcmEventTeleport`](../Module/AgcmEventTeleport.md). Es wurde kein Live-Traffic mitgeschnitten; Serverdatenbank-Strukturen sind Inferenz.

## Kurzfazit

- Interaktionen laufen nicht nur ueber einzelne NPC-Funktionen, sondern ueber ein generisches Eventsystem.
- Der zentrale Eventcontainer heisst `ApmEventManager` und registriert Modul-ID `0x3c`.
- Eventobjekte speichern bis zu 5 Funktions-/Eventeintraege mit `Function`, `EventID` und optionalen Bedingungen.
- Wichtige Eventmodule:
  - `AgcmEventNPCTrade`: Modul `0x32`
  - `AgpmEventTeleport`: Modul `0x31`
  - `AgpmEventNPCDialog`: Modul `0x37`
  - `AgpmEventQuest`: Modul `0x3e`
  - [`AgpmEventBank`](../Module/AgpmEventBank.md): Modul `0x36`
  - [`AgpmEventItemRepair`](../Module/AgpmEventItemRepair.md): Modul `0x34`
  - [`AgpmEventItemConvert`](../Module/AgpmEventItemConvert.md): Modul `0x38`
  - [`AgpmEventRefinery`](../Module/AgpmEventRefinery.md): Modul `0x3f`
  - [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md): Modul `0x3b`
  - [`AgpmEventGuild`](../Module/AgpmEventGuild.md): Modul `0x39`
  - [`AgpmEventProduct`](../Module/AgpmEventProduct.md): Modul `0x3a`
- `AgcmEventManager` ist der Client-Dispatcher: andere Clientmodule registrieren Handler fuer Event-Funktionsnummern, z. B. Auction ueber `0x1c`, NPCTrade ueber `9`, Teleport ueber `8`, NPCDialog ueber `0x15`.

## ApmEventManager

Konstruktor: `FUN_0055d6d0`

Wichtige Punkte:

- Modulname: `ApmEventManager`
- Modul-ID: `FUN_004e4540(0x3c)`
- Hauptlayout `+0x43d`:

```text
1,1
5,1
5,1
5,1
0xff,0
```

- weiteres Layout `+0x4e82`:

```text
0xc,1
0xc,1
0xff,0
```

- Intern werden Callbacktabellen fuer bis zu `0x2a` Eventfunktionen aufgebaut.

## Eventeintraege und Bedingungen

`FUN_0055cb30` registriert pro Eventfunktion mehrere Callbacks:

```text
eventFunction -> create/read callback
eventFunction -> destroy/write callback
eventFunction -> condition callback
eventFunction -> extra callback
eventFunction -> context
```

`FUN_0055cba0` fuegt einem Objekt einen Eventeintrag hinzu. Ein Objekt kann bis zu 5 Eventfunktionen enthalten.

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| `Function` | Eventfunktion/Subtyp, `0..0x29` |
| `EventID` | konkrete Event-ID |
| `CondStart` / `CondEnd` | Beginn/Ende der Bedingungen |
| `CondType` | Bedingungstyp |
| `CondTargetItemTID` | erforderliches Itemtemplate |
| `CondAreaType` | Area-Trigger-Typ |
| `CondAreaSphereRadius` | Kugelradius |
| `CondAreaFanRadius` | Faecheradius |
| `CondAreaAngle` | Faecherwinkel |
| `CondAreaBoxInf` | Box-Minimum |
| `CondAreaBoxSup` | Box-Maximum |

Das ist ein klarer Hinweis, dass der Server Interaktionen nicht nur per NPC-ID prueft, sondern gegen Eventfunktion, Event-ID, Conditions, Itembesitz und Positions-/Area-Bedingungen.

## Objektarten im EventManager

`FUN_0055c820` loest Event-Ziele je nach Typ auf:

| Typ | Zielauflösung |
|---:|---|
| `1` | Map-/Object-Funktion `FUN_0051d130` |
| `2` | Map-/Object-Funktion `FUN_0051d240` |
| `3` | Character `FUN_005035d0` |
| `4` | Character-nahe Funktion `FUN_00503750` |
| `5` | Iteminstanz `FUN_00558380` |
| `6` | Itemtemplate `FUN_00540d20` |
| `0x0b` | weitere Objekt-/Eventstruktur `FUN_00566f80` |

`FUN_0055c920` extrahiert aus Zielobjekten Positions-/Eventdaten. Fuer Items mit Status `2..3` wird zunaechst der Besitzer-Character aufgeloest.

## Generische Event-Payloads

`FUN_0055ca00` baut ein Nested-Eventpaket aus einem Eventeintrag. Es unterscheidet:

- Event-ID direkt, wenn kein High-Bit gesetzt ist.
- Sonderfall mit `0x40000000`, bei dem eine runtime-generierte ID ueber `FUN_007e36f0()` genutzt wird.
- Eintraege mit Zusatzdaten (`param_2[4]`) werden mit ID und Pointerbereich serialisiert.

Viele Eventmodule packen dieses Nested-Paket in ihr eigenes Modulpaket. Damit ist der grobe Frameaufbau:

```text
Spezialmodul, z. B. Teleport/NPCTrade/Auction
  -> Nested EventID/EventFunction aus ApmEventManager
  -> Zielobjekt oder Character-ID
  -> optionale Item-/Grid-/Dialogdaten
```

## AgcmEventManager

`FUN_006e0860(functionId, callback, context)` registriert Clienthandler fuer Eventfunktionen und begrenzt `functionId < 0x2a`.

Beispiele:

| Eventfunktion | Registrierender Clientteil |
|---:|---|
| `8` | `AgcmEventTeleport` |
| `9` | `AgcmEventNPCTrade` |
| `0x15` | `AgcmEventNPCDialog` |
| `0x1c` | [`AgcmAuction`](../Module/AgcmAuction.md) |
| `0x1d` | [`AgcmEventCharCustomize`](../Module/AgcmEventCharCustomize.md) |
| `0x1f` | [`AgcmEventRefinery`](../Module/AgcmEventRefinery.md) |
| `0x20` | [`AgcmEventProduct`](../Module/AgcmEventProduct.md) |
| `0x22` | [`AgcmEventGuild`](../Module/AgcmEventGuild.md) |
| `0x26` | [`AgcmEventGacha`](../Module/AgcmEventGacha.md) |
| `0x28` | weiterer Eventclient |

## NPCDialog

### AgpmEventNPCDialog

Konstruktor: `FUN_00576770`

- Modulname: `AgpmEventNPCDialog`
- Modul-ID: `0x37`
- Hauptlayout `+0x350`:

```text
1,1
0xc,1
5,1
0xff,0
```

- Nested-/Hilfslayout `+0x4d95`:

```text
5,1
0xff,0
```

### AgcmEventNPCDialog

`FUN_006ddbe0` konstruiert `AgcmEventNPCDialog`.

`FUN_006dde10` registriert:

- `AgcmEventManager` Eventfunktion `0x15`
- Callback `LAB_006ddcc0`
- zusaetzlicher Hook in `AgpmEventNPCDialog` ueber `FUN_005781f0(FUN_006ddda0, ...)`

`FUN_006ddda0` prueft, ob ein empfangenes/ausgeloestes NPCDialog-Event zum lokalen Character gehoert. Wenn ja:

```text
FUN_004e4070(0, event, localCharacter)
```

UI-Funde:

- `NPCDialog_OpenUI`
- `NPCDialog_CloseUI`
- `NPCDialog_Buttons`, bis 10 Buttons
- `NPCDialog_DisplayDialog`
- `NPCDialog_SelectButton`
- `NPCDialog_Button`
- Dialogdatei-Pfadmuster: `Ini\\%sNPCDialog.txt`

Interpretation:

- Der Server bzw. Eventdaten liefern Dialog-ID, Buttonliste und Ziel-/Characterkontext.
- Buttonauswahl fuehrt ueber Eventfunktion/ID zur naechsten Serveraktion oder lokalen Folgeaktion.

## NPCTrade

### AgpmEventNPCTrade

Konstruktor: `FUN_005762d0`

- Modulname: `AgpmEventNPCTrade`
- Das Server-/Datenmodul selbst registriert in diesem Konstruktor keine eigene `FUN_004e4540`-ID.
- Es wird in `ApmEventManager` als Eventfunktion `9` registriert:

```text
FUN_0055cb30(9, FUN_00576500, FUN_00576390, 0, LAB_00576400, LAB_00576460, context)
```

Initialisierte Daten:

- `0x3c8` Byte Eventdatenblock
- `0x24` Byte Grid-/Tradeobjekt
- drei `0x140` Byte Bereiche fuer Layer/Listen
- Grid wird mit Status `6` initialisiert

### AgcmEventNPCTrade

Konstruktor: `FUN_006dd030`

- Modulname: `AgcmEventNPCTrade`
- Modul-ID: `FUN_004e4540(0x32)` -> `0x32`
- Hauptlayout `+3000`
- Nested-Itemlayout `+0x134cc`

Layouts:

```text
+0x2ee:
  0xc,1 1,1 5,1 5,1 0xc,1 5,1 5,1 1,1 1,1 1,1 0xff,0

+0x4d33:
  5,1 5,1 5,1 3,1 3,1 3,1 3,1 5,1 5,1 0xff,0
```

Client-Sends:

| Funktion | Modul | Bedeutung |
|---|---:|---|
| `FUN_006dd580` | `0x32` | NPCTrade Item bewegen/kaufen/verkaufen mit Item-, Grid- und drei optionalen Byteflags |
| `FUN_006dd710` | `0x32` | NPCTrade Itemaktion mit Itemstatus und Gridposition |
| `FUN_006dd870` | `0x32` | NPCTrade oeffnen/initialisieren/abfragen |

`FUN_006dd960` ist der Event-Einstieg fuer Funktion `9`. Es speichert Eventdaten in `AgcmEventNPCTrade +0x25de0/+0x25de4` und sendet danach `FUN_006dd870(localCID)`.

Server-Receive/Callback:

`FUN_006dd9e0` parst Hauptlayout `+3000`:

- Status `0`: Itemdaten werden ueber `FUN_006dd2b0` ins NPCTrade-Grid eingebaut.
- Status `1`: Callback `3`.
- Status `2`: Fehler-/Statusmapping ueber `FUN_006dd200`.
- Status `3`: unterscheidet Untercode `0` -> Callback `6`, Untercode `1` -> Callback `9`.
- Danach oft Callback `1`.

`FUN_006dd200` mappt Statuscodes:

| Code | Callback |
|---:|---:|
| `2` | `7` |
| `3` | `8` |
| `4` | `5` |
| `10` | `10` |
| `0x0b` | `0x0b` |

UI-Funde:

- `NPCT_OpenUI`
- `NPCT_CloseUI`
- `NPCT_InitLayer`
- `NPCT_MoveItem`
- `NPCT_UIOpen`
- `NPCT_UIClose`
- `NPCT_MoveNextLayer`
- `NPCT_MovePrevLayer`
- `NPCT_BuyStackCountOK`
- `NPCT_BuyStackCountCancel`
- `NPCT_BuyItemDirect`
- `NPCTMSG_InvenFull`
- `NPCTMSG_ConfirmBuy`
- `NPCTMSG_ConfirmBuyStackCount`
- `NPCTMSG_ConfirmSell`
- `NPCTMSG_NotEnoughGhelld`
- `NPCTMSG_NotEnoughCharisma`
- `NPCTMSG_NotEnoughShrineCoin`
- `NPCTMSG_NotEnoughSpaceToGetGhelld`
- `NPCTMSG_TradeSuccess`
- `NPCTradeGrid`

Interpretation:

- NPCTrade deckt Kauf, Verkauf, Stackkauf, Layer/Shopseiten und Sonderwaehrungen ab.
- Neben Ghelld gibt es Charisma-Preis und Shrine-Coin-Preis.

## Teleport

### AgpmEventTeleport

Konstruktor: `FUN_00559f70`

- Modulname: `AgpmEventTeleport`
- Modul-ID: `FUN_004e4540(0x31)` -> `0x31`
- Hauptlayout `+0xde4`
- Event-/Nestedlayout `+0x10f4` aus `ApmEventManager::FUN_0055ca00`

Layout `+0xde4`:

```text
1,1
0xc,1
5,1
0,0x21
10,1
0xd,1
0xff,0
```

### AgcmEventTeleport

`FUN_006dde70` konstruiert `AgcmEventTeleport`.

`FUN_006de0e0` registriert:

- `AgcmEventManager` Eventfunktion `8`
- Callback `FUN_006dded0`
- Eventhook `FUN_006ddfc0`
- Zusatzcallback `LAB_006de010`

Client-Sends in `AgpmEventTeleport`:

| Funktion | Subop | Bedeutung |
|---|---:|---|
| `FUN_0055a5f0` | `1` | Teleport-Aktion mit Ziel/Eventdaten |
| `FUN_0055a670` | `2` | zweite Teleport-Aktion/Cancel/Select |
| `FUN_0055a6f0` | `4` | Teleport mit Nested-Eventpaket und Ziel |
| `FUN_0055a550` | `7` | Teleport mit Eventpaket oder leerem Query |
| `FUN_0055a7a0` | `8` | Teleport mit einfachem Zielparameter |
| `FUN_0055a4b0` | variabel | generischer Teleport-Send; packt optional Eventdaten |

`FUN_006dded0` ist der Event-Einstieg:

- speichert Eventobjekt und Parameter bei `AgcmEventTeleport +0xbb0/+0xbb4`.
- prueft, ob das Event zum lokalen Character gehoert.
- wenn der Character nicht busy/dead ist und ein bestimmtes Eventflag gesetzt ist, Callback `1`.
- sonst ruft es `FUN_0055a6f0(event, params)` und sendet damit eine Teleport-Anfrage.

`FUN_006de040(name)` sendet Teleport mit Text-/Zielparameter ueber `FUN_0055a4b0`.

`FUN_006de080()` sendet Teleportauswahl/Default ueber `FUN_0055a550`.

## Warum das fuer den Server wichtig ist

Der Client zeigt, dass Serverinteraktionen aus mehreren Schichten bestehen:

1. Objekt/NPC/Item/Character ist Ziel der Interaktion.
2. `ApmEventManager` liefert Eventfunktion und Event-ID.
3. Conditions pruefen Itemanforderungen und Area-Anforderungen.
4. Das spezialisierte Modul verarbeitet die Aktion: Dialog, Shop, Teleport, Quest, Bank, Repair usw.
5. Ergebnis wird als Modulantwort und UI-Callback zurueckgesendet.

Serverseitig kann daraus nicht einfach eine Tabelle `npc_id -> action` reichen. Es braucht mindestens Eventdefinitionen, Zielbindungen und Conditions.

## Server-Datenbank-Inferenz

### Eventdefinitionen

`event_objects`

- `event_object_id`
- `world_object_id` oder `npc_id`
- `map_id`
- `object_type`
- `x`, `y`, `z`
- `enabled`

`event_functions`

- `event_object_id`
- `function_id`
- `event_id`
- `priority`
- `cooldown`
- `target_type`
- `payload_ref`

`event_conditions`

- `event_object_id`
- `function_id`
- `condition_type`
- `target_item_tid`
- `area_type`
- `sphere_radius`
- `fan_radius`
- `fan_angle`
- `box_min_x`, `box_min_y`, `box_min_z`
- `box_max_x`, `box_max_y`, `box_max_z`

### NPCDialog

`npc_dialogs`

- `dialog_id`
- `npc_id`
- `text_key`
- `script_file`

`npc_dialog_buttons`

- `dialog_id`
- `button_index`
- `text_key`
- `next_event_id`
- `required_condition_id`

### NPCTrade

`npc_shop_templates`

- `shop_id`
- `npc_id`
- `layer`
- `currency_type`: ghelld, charisma, shrine_coin

`npc_shop_items`

- `shop_id`
- `item_template_id`
- `quantity`
- `price`
- `charisma_price`
- `shrine_coin_price`
- `stock_limit`
- `trade_flags`

`npc_shop_transactions`

- `transaction_id`
- `character_id`
- `npc_id`
- `item_template_id`
- `count`
- `currency_type`
- `price_total`
- `created_at`

### Teleport

`teleport_groups`

- `group_id`
- `npc_id`
- `name`
- `required_level`
- `required_item_tid`
- `fee`

`teleport_points`

- `point_id`
- `group_id`
- `target_map_id`
- `target_x`
- `target_y`
- `target_z`
- `display_name`
- `fee`
- `condition_id`

`teleport_logs`

- `character_id`
- `source_map_id`
- `target_map_id`
- `fee`
- `used_item_tid`
- `created_at`

## Sicherheitsrelevante Punkte

- Eventfunktion und Event-ID duerfen nicht blind vom Client akzeptiert werden.
- Server muss Distanz/Area-Condition selbst pruefen.
- Required Item TID muss serverseitig im Inventar validiert und ggf. atomar verbraucht werden.
- NPCTrade muss Geld, Charisma, ShrineCoin, Inventory-Space und Itemlimits serverseitig pruefen.
- Teleport muss Zielpunkt, Kosten, Cooldown, Mapberechtigung und Busy/Combat-State pruefen.
- NPCDialog-Buttonauswahl muss gegen den aktuell gueltigen Dialogzustand des Characters validiert werden.

## Noch offene Detailarbeit

- `AgpmEventQuest` wird separat als Sequenz 12 behandelt.
- `AgpmEventBank`, `AgpmEventItemRepair`, `AgpmEventItemConvert`, `AgpmEventRefinery`, `AgpmEventSkillMaster` verdienen jeweils eigene Vertiefung oder einen kombinierten Service-NPC-Block.
- Die Label-Handler der UI (`NPCT_MoveItem`, `NPCDialog_SelectButton`, Teleport-UI-Auswahl) sollten noch mit Disassembly-Controlflow aufgeloest werden.
