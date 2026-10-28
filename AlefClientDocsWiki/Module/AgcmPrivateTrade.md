# AgcmPrivateTrade (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmPrivateTrade` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmPrivateTrade` / `AgcmPrivateTrade.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x006E9880` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGPMPRIVATETRADE_PACKET_*` kennt 26 Operationen, davon 15 mit eigenem Case im 2017er Binary; ohne Case: `TRADE_REQUEST_TRADE` (1), `TRADE_CONFIRM` (4), `TRADE_EXECUTE` (7), `TRADE_END` (8), `ADD_TO_TRADE_GRID` (9), `REMOVE_FROM_TRADE_GRID` (10), `MOVE_TRADE_GRID` (11), `MOVE_INVEN_GRID` (12), `ADD_TO_TARGET_TRADE_GRID` (13), `REMOVE_FROM_TARGET_TRADE_GRID` (14), `MOVE_TARGET_TRADE_GRID` (15).
- **Vergleich mit 2013:** Für 14 Operationen liegen 2013er Ereignisse vor; 1 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 13 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 3 Paketdefinition(en) in der Quelle, 3 davon im 2017er Konstruktor (`006e8da0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x006E8DA0` | `AgcmPrivateTrade::ctor_or_dtor` | merged |
| `0x006E8F70` | `AgcmPrivateTrade::OnAddModule` | merged |
| `0x006E9880` | `AgcmPrivateTrade::OnReceive` | merged |

3 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 9/9/9 | ja | ja |
| `m_csOriginPos` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csGridPos` | 1/1/1 | 3/3/3 | ja | ja |

**m_csPacket** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation   |
| 1 | `0x2` | INT32 | 1 | lCID  |
| 2 | `0x4` | INT32 | 1 | lCTargetID  |
| 3 | `0x8` | INT32 | 1 | lIID       Item ID |
| 4 | `0x10` | INT32 | 1 | lITID      Item Type ID |
| 5 | `0x20` | INT32 | 1 | Money Count |
| 6 | `0x40` | PACKET | 1 | csOriginPos |
| 7 | `0x80` | PACKET | 1 | csGridPos |
| 8 | `0x100` | INT32 | 1 | lResult    Result |

**m_csOriginPos** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT16 | 1 | Layer |
| 1 | `0x2` | INT16 | 1 | Row |
| 2 | `0x4` | INT16 | 1 | Column |

**m_csGridPos** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT16 | 1 | Layer |
| 1 | `0x2` | INT16 | 1 | Row |
| 2 | `0x4` | INT16 | 1 | Column |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `TRADE_RESULT` | `0x006E9060` `FUN_006e9060` | `ID_TRADE_CLOSE_UI_PRIVATETRADE` | 2017 ⊂ 2013 |
| 1 | `TRADE_REQUEST_TRADE` | – | – | kein Case (default) – wie 2013 |
| 2 | `TRADE_WAIT_CONFIRM` | inline | – | keine Callback-Ereignisse (beide) |
| 3 | `TRADE_REQUEST_CONFIRM` | inline | – | 2017 ⊂ 2013 |
| 4 | `TRADE_CONFIRM` | – | – | kein Case (default) – wie 2013 |
| 5 | `TRADE_CANCEL` | `0x006E9790` `FUN_006e9790` | `ID_TRADE_CLOSE_UI_PRIVATETRADE`, `ID_TRADE_UI_MSG_TRADE_CANCEL` | = (2013 = 2017) |
| 6 | `TRADE_START` | inline | – | 2017 ⊂ 2013 |
| 7 | `TRADE_EXECUTE` | – | – | kein Case (default) – wie 2013 |
| 8 | `TRADE_END` | – | – | kein Case (default) – wie 2013 |
| 9 | `ADD_TO_TRADE_GRID` | – | – | kein Case (default) – wie 2013 |
| 10 | `REMOVE_FROM_TRADE_GRID` | – | – | kein Case (default) – wie 2013 |
| 11 | `MOVE_TRADE_GRID` | – | – | kein Case (default) – wie 2013 |
| 12 | `MOVE_INVEN_GRID` | – | – | kein Case (default) – wie 2013 |
| 13 | `ADD_TO_TARGET_TRADE_GRID` | – | – | kein Case (default) – wie 2013 |
| 14 | `REMOVE_FROM_TARGET_TRADE_GRID` | – | – | kein Case (default) – wie 2013 |
| 15 | `MOVE_TARGET_TRADE_GRID` | – | – | kein Case (default) – wie 2013 |
| 16 | `LOCK` | `0x006E9810` `FUN_006e9810` | `-1` | ≠ |
| 17 | `TARGET_LOCKED` | inline | – | 2017 ⊂ 2013 |
| 18 | `UNLOCK` | `0x006E9810` `FUN_006e9810` | `-1` | ≠ |
| 19 | `TARGET_UNLOCKED` | inline | – | 2017 ⊂ 2013 |
| 20 | `ACTIVE_READY_TO_EXCHANGE` | inline | – | 2017 ⊂ 2013 |
| 21 | `READY_TO_EXCHANGE` | inline | – | 2017 ⊂ 2013 |
| 22 | `TARGET_READY_TO_EXCHANGE` | inline | – | 2017 ⊂ 2013 |
| 23 | `UPDATE_MONEY` | inline | – | 2017 ⊂ 2013 |
| 24 | `TARGET_UPDATE_MONEY` | inline | – | 2017 ⊂ 2013 |
| 25 | `TRADE_REFUSE` | inline | – | 2017 ⊂ 2013 |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 0 | `TRADE_RESULT` | ITEM_CB_ID_TRADE_UI_MSG_TRADE_COMPELTE | – |
| 3 | `TRADE_REQUEST_CONFIRM` | ITEM_CB_ID_TRADE_OPEN_UI_PRIVATETRADE_YES_NO | – |
| 6 | `TRADE_START` | ITEM_CB_ID_TRADE_OPEN_UI_PRIVATETRADE | – |
| 16 | `LOCK` | ITEM_CB_ID_UPDATE_LOCK_BUTTON | -1 |
| 17 | `TARGET_LOCKED` | ITEM_CB_ID_TRADE_UI_UPDATE_TARGET_LOCK_BUTTON | – |
| 18 | `UNLOCK` | ITEM_CB_ID_UPDATE_LOCK_BUTTON | -1 |
| 19 | `TARGET_UNLOCKED` | ITEM_CB_ID_TRADE_UI_UPDATE_TARGET_LOCK_BUTTON | – |
| 20 | `ACTIVE_READY_TO_EXCHANGE` | ITEM_CB_ID_TRADE_UI_ACTIVE_READY_TO_EXCHANGE | – |
| 21 | `READY_TO_EXCHANGE` | ITEM_CB_ID_TRADE_UI_READY_TO_EXCHANGE | – |
| 22 | `TARGET_READY_TO_EXCHANGE` | ITEM_CB_ID_TRADE_UI_CLIENT_READY_TO_EXCHANGE | – |
| 23 | `UPDATE_MONEY` | ITEM_CB_ID_UPDATE_TRADE_MONEY | – |
| 24 | `TARGET_UPDATE_MONEY` | ITEM_CB_ID_UPDATE_TARGET_TRADE_MONEY | – |
| 25 | `TRADE_REFUSE` | ITEM_CB_ID_TRADE_REQUESE_REFUSE_USER | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 17, nicht als eigene Funktion: 9, nicht im Client: 6, zugeordnet: 11.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `ProcessCancel` | 29 | `0x006E9810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessLockButton` | 26 | `0x006E9790` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendReadyToExchange` | 39 | `0x006E96F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeUnlock` | 39 | `0x006E9650` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeLock` | 39 | `0x006E95B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeRemoveItemFromTradeGrid` | 60 | `0x006E9470` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeAddItemToTradeGrid` | 57 | `0x006E9350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeUpdateMoney` | 46 | `0x006E9280` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeCancel` | 39 | `0x006E91E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeRequestConfirm` | 29 | `0x006E9160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTradeRequest` | 47 | `0x006E9080` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIParty`](AgcmUIParty.md)
