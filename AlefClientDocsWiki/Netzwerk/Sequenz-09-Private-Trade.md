# Winsock-Sequenz 09: Private Trade

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei dokumentiert den bisher statisch rekonstruierten Private-Trade-Teil des `alefclient.exe`. Quellen sind `alefclient.pseudocode.c`, besonders die Bereiche um [`AgcmPrivateTrade`](../Module/AgcmPrivateTrade.md), die UI-Registrierung `PT_*` und die Item-/Grid-Flows. Es wurde kein Live-Traffic mitgeschnitten; DB-Strukturen sind daher als Inferenz markiert.

## Kurzfazit

- Private Trade ist ein eigenes Netzwerkmodul: `AgcmPrivateTrade`, Modul-ID `0x07`.
- Der Client sendet Trade-Aktionen ueber `FUN_004ea280(..., module 7, ...)` und danach `FUN_004e45d0(...)`.
- Das System haengt direkt an Character, Item, Grid und UI:
  - [`AgpmCharacter`](../Module/AgpmCharacter.md)
  - `AgcmCharacter`
  - [`AgpmItem`](../Module/AgpmItem.md)
  - [`AgcmItem`](../Module/AgcmItem.md)
  - [`AgpmGrid`](../Module/AgpmGrid.md)
  - [`AgpmFactors`](../Module/AgpmFactors.md)
- Sichtbare Client-Aktionen: Request, RequestCancel, Accept, Reject, MoveItem, UpdateMoney, Lock, Unlock, ReadyToExchange, Cancel.
- Sichtbare UI-Daten: eigener Trade-Grid, Client-/Gegenpartner-Grid, eigener Name, Gegenpartnername, eigenes Geld/Ghelld, Gegenpartner-Ghelld.
- Server-seitig muss dieser Bereich sehr wahrscheinlich transaktional implementiert sein, weil Items und Geld reserviert, gelockt und am Ende atomar zwischen zwei Charakteren transferiert werden muessen.

## Modul und Paketlayouts

### Konstruktor / Modulregistrierung

`FUN_006e9390` konstruiert `AgcmPrivateTrade`.

Wichtige Punkte:

- Modulname: `AgcmPrivateTrade`
- Modul-ID: `FUN_004e4540(7)` -> `0x07`
- Hauptlayout liegt bei Objekt-Offset `+0xbb4`.
- Zwei Nested-Layouts liegen bei:
  - `+0x134c8`
  - `+0x25ddc`

Die drei Layouts werden fuer normale Private-Trade-Pakete und eingebettete Grid-/Item-Tripel benutzt.

### Hauptlayout `+0xbb4`

Initialisierung im Konstruktor:

```text
0xbb4:
  1,1
  5,1
  5,1
  5,1
  5,1
  5,1
  0xc,1
  0xc,1
  5,1
```

Interpretation:

- Erstes Feld ist die Trade-Operation bzw. der Subopcode.
- Danach folgen mehrere 32-bit/ID-Felder, Geld-/Wertfelder und optionale Nested-Pakete.
- Die exakte Feldtyp-Namensgebung muss noch mit `AuPacket`-Typcodes validiert werden. Die Nutzung zeigt aber klar:
  - Character-ID / Target-ID
  - ein zweites ID-/Statusfeld
  - Geldwert
  - zwei Nested-Grid-Pakete
  - Status/Container-Code

### Nested-Layouts `+0x134c8` und `+0x25ddc`

Beide Nested-Layouts werden identisch initialisiert:

```text
3,1
3,1
3,1
```

Diese Pakete werden in Itembewegungen eingebettet. Die drei Felder wirken wie Grid-/Slot-/Itempositionsdaten. In den Aufrufen werden sie aus Stackpositionen gebaut, die aus Item/Grid-Kontexten stammen:

- Item-template oder Item-instance Kontext
- Ursprungsgrid / Zielgrid
- X/Y- oder Slot-Koordinaten

## Abhaengigkeiten im Modul

`FUN_006e9560` verdrahtet `AgcmPrivateTrade` mit anderen Modulen:

| Offset | Bedeutung |
|---:|---|
| `+0xb98` | [`ApmMap`](../Module/ApmMap.md) |
| `+0xb9c` | `AgpmCharacter` |
| `+0xba0` | `AgcmCharacter` |
| `+0xba4` | `AgpmFactors` |
| `+0xba8` | `AgpmItem` |
| `+0xbac` | `AgcmItem` |
| `+0xbb0` | `AgpmGrid` |

Damit ist Private Trade nicht nur UI, sondern ein Clientmodul, das Character-Objekte, Iteminstanzen, Gridpositionen und Werte direkt prueft.

## UI-Registrierung und sichtbare Aktionen

Die Private-Trade-UI registriert unter anderem:

```text
PT_OpenRequest
PT_CloseRequest
PT_OpenConfirmEvent
PT_CloseConfirmEvent
PT_OpenUIEvent
PT_CloseUIEvent
PT_ClientLock
PT_ClientUnlock
PT_ActiveReadyToExchange
PT_ClientReadyToExchange
PTMSG_InvenFull
PTMSG_TradeComplete
PTMSG_TradeCancel
PTMSG_Error
PrivateTradeGrid
PrivateTradeGridEx
PrivateTradeClientGridEx
PrivateTradeClientGrid
PrivateTraderName
PT_Request
PrivateTradeSetName
PrivateTradeSetClientName
PrivateTradeGhelld
PrivateTradeClientGhelld
```

Die Button-/Command-Registrierung zeigt die wichtigsten Client-Aktionen:

| UI-Command | Handler | Bedeutung |
|---|---:|---|
| `PT_RequestCancel` | `FUN_0074e1e0` | Anfrage/Confirm-Fenster abbrechen bzw. ablehnen/wegschicken |
| `PT_Accept` | `LAB_0074e240` | Trade-Anfrage akzeptieren, Label nicht als eigene Funktion dekompiliert |
| `PT_Reject` | `FUN_0074e340` | Anfrage ablehnen |
| `PT_MoveItem` | `LAB_0074e810` | Item in/aus Trade-Grid bewegen, Label nicht als eigene Funktion dekompiliert |
| `PT_UpdateMoney` | `FUN_0074e390` | Geldbetrag aus UI lesen und senden |
| `PT_Lock` | `LAB_0074e410` | eigenes Angebot sperren |
| `PT_Unlock` | `LAB_0074e420` | eigenes Angebot entsperren |
| `PT_ReadyToExchange` | `FUN_0074e4c0` | finale Bereitschaft / Austausch bestaetigen |
| `PT_Cancel` | `LAB_0074e430` | laufenden Trade abbrechen |
| `PT_RequestTrade` | `LAB_006d4220` | Trade mit Zielcharakter anfragen |

Einige Adressen sind nur als Labels referenziert, weil Ghidra sie in einen groesseren UI-Dispatcher eingebettet hat. Die Registrierungen sind trotzdem wertvoll, weil die UI-Namen die Semantik liefern.

## Client -> Server: gesendete Private-Trade-Aktionen

Alle folgenden Sendepfade enden im normalen Winsock-Sendepfad:

```text
AgcmPrivateTrade
  -> FUN_004ea280(..., module 7, ...)
  -> FUN_004e45d0(...)
  -> AcSocketManager / AcClientSocket
  -> send()
```

### Trade Request an Zielcharakter

Funktion: `FUN_006e9690(param_1, targetCID)`

Pruefungen:

- `AgpmCharacter` muss vorhanden sein.
- `FUN_005035d0(targetCID)` muss den Zielcharakter finden.
- `FUN_00503150(target)` muss erfolgreich sein.
- Zielzustand bei `target + 0x52a` muss `0` oder `3` sein.

Payload:

- Modul `0x07`
- Hauptlayout `+0xbb4`
- enthaelt `targetCID`

Wahrscheinliche Bedeutung: Client fordert privaten Handel mit einem angeklickten/ausgewaehlten Charakter an.

### RequestCancel / Reject / Anfrageantwort

Funktionen:

- `FUN_006e9770`
- `FUN_006e97f0`
- UI-Handler `FUN_0074e1e0`
- UI-Handler `FUN_0074e340`
- weiterer UI-Helfer `FUN_0074e7d0`

`FUN_006e9770` setzt ein echtes lokales Byte:

```text
local_5 = 4
FUN_004ea280(... module 7, &local_5, ...)
```

`FUN_006e97f0` validiert eine Character-ID und sendet ein kurzes Modul-7-Paket ohne Ziel-ID im Payload. Diese Funktion wird mehrfach von RequestCancel/Reject/Confirm-nahen UI-Pfaden aufgerufen:

- `FUN_0074e1e0`: nutzt `param_1 + 0xbbc` und lokalen Character-Kontext.
- `FUN_0074e340`: nutzt lokalen Character `AgcmCharacter + 0x15964`.
- `FUN_0074e7d0`: holt `AgcmPrivateTrade` und `AgcmCharacter`, dann ebenfalls `FUN_006e97f0(localCID)`.

Wahrscheinliche Bedeutung: Antwort-/Abbruchpaket fuer offene Private-Trade-Anfrage. Die genaue Unterteilung Accept vs Reject vs Cancel braucht noch Label-Aufloesung fuer `LAB_0074e240`, `LAB_0074e410`, `LAB_0074e420`, `LAB_0074e430`.

### Geldbetrag setzen

UI-Handler: `FUN_0074e390`

Ablauf:

1. Erwartet UI-Control-Typ `2`.
2. Liest Textpointer aus `control + 0xf4 + 0x1d04`.
3. Verwift leere Strings.
4. Parst Betrag mit `atoi`.
5. Betrag muss `>= 1` sein.
6. Setzt einen lokalen UI-/Statewert via `FUN_00700170(&DAT_0091f56c,0,1)`.
7. Sendet `FUN_006e9890(localCID, amount)`.

Sendefunktion: `FUN_006e9890(param_1, amount)`

Pruefungen:

- `AgpmCharacter` vorhanden.
- `FUN_005035d0(...)` erfolgreich.
- `FUN_0058a5f0(character, &availableMoney)` liefert aktuelles Geld.
- Falls eingegebener Betrag groesser als verfuegbares Geld ist, wird er auf `availableMoney` gekappt.

Payload:

- Modul `0x07`
- Hauptlayout `+0xbb4`
- Geldbetrag im Geldfeld

Wichtig: Die Kappung im Client ist nur UI-/Komfortschutz. Der Server muss den Betrag erneut validieren.

### Itembewegung in Trade-Grids

Funktionen:

- `FUN_006e9960`
- `FUN_006e9a80`

`FUN_006e9960(param_1, param_2, param_3)`:

- validiert Character `param_3`.
- baut Nested-Paket `+0x134c8` aus drei Stackfeldern.
- baut Nested-Paket `+0x25ddc` aus drei weiteren Stackfeldern.
- baut aeusseres Modul-7-Paket mit beiden Nested-Paketen.

`FUN_006e9a80(param_1, param_2, ..., tradeMoveCode)`:

- erlaubt fuer `tradeMoveCode` nur:
  - `2`
  - `0x0d`
  - `0x0f`
- andere Werte werden auf `2` normalisiert.
- baut ebenfalls zwei Nested-Grid-Pakete.
- sendet danach ein aeusseres Modul-7-Paket.

Item-/Grid-Aufrufer bestaetigen die Rolle:

- Bei Itemstatus `6` wird `FUN_006e9a80(...)` aus mehreren Inventory-/Grid-Flows aufgerufen.
- Je nach Kontext wird der letzte Parameter `2`, `0x0d` oder `0x0f` gesetzt.
- Vor dem Move werden Item-/Grid-Koordinaten gelesen, unter anderem Offsets wie `item + 0x138`, `+0x13a`, `+0x13c` und Griddaten um `+0x1d10`.

Wahrscheinliche Bedeutung:

- Item in eigenes Trade-Angebot legen.
- Item aus Trade-Angebot zuruecknehmen.
- Item zwischen Client-/Trade-spezifischen Gridkontexten synchronisieren.

Server muss hier zwingend pruefen:

- Item gehoert wirklich dem Character.
- Item ist nicht already locked/reserved.
- Quelle und Ziel sind gueltige Container/Gridpositionen.
- Stacksize und Itemzustand stimmen.
- Item darf handelbar sein.

### Lock / Unlock / ReadyToExchange / Cancel

Funktionen:

- `FUN_006e9bc0`
- `FUN_006e9c60`
- `FUN_006e9d00`

Alle drei:

- holen lokale Character-ID aus `AgcmCharacter + 0x15964`;
- validieren den Character;
- senden ein kurzes Modul-7-Paket ueber Hauptlayout `+0xbb4`.

Gesicherte UI-Zuordnung:

- `PT_ReadyToExchange` -> `FUN_0074e4c0` -> `FUN_006e9d00`

Fuer `PT_Lock`, `PT_Unlock` und `PT_Cancel` sind die Label-Adressen nur in der UI-Registrierung sichtbar. Die drei Sendefunktionen liegen direkt nebeneinander und haben identische Struktur, unterscheiden sich aber wahrscheinlich durch ein Stack-Byte im ersten Payloadfeld, das Ghidra hier nicht sauber als Konstante dargestellt hat.

## Server -> Client: empfangene Private-Trade-Operationen

Receive-/Dispatchfunktion: `FUN_006e9e90`

Sie parst das Modul-7-Hauptlayout:

```text
FUN_004e9fb0(param_1 + 0xbb4, 1, packet, ..., 
  &op,
  &local_20,
  &local_1c,
  local_4,
  local_8,
  &local_18,
  local_c,
  local_10,
  &local_14)
```

Danach wird ueber `op` verzweigt.

| Server-Op | Client-Reaktion | Interpretation |
|---:|---|---|
| `0x00` | wenn `local_14 == 8`: Character validieren, Trade-Daten leeren, Callback `9`, dann Callback `0x0e` | spezieller Reset/Cancel/Close mit Status `8` |
| `0x02` | sofort `return 1` | Ack/No-op/valid packet |
| `0x03` | Callback `7` mit `local_1c` | Anfrage-/Statusantwort |
| `0x05` | `FUN_006e9da0(local_20)` | Trade fuer Character leeren, Callbacks `9` und `0x0f` |
| `0x06` | beide Character aufloesen, beide Trade-Daten leeren, `tradeData + 0x16c = local_1c`, Callback `8` | Trade-Session oeffnen/initialisieren oder Gegenpartner setzen |
| `0x10` | `FUN_006e9e20(local_20, 1)` | Lock-Flag fuer Character setzen |
| `0x11` | Callback `0x0a` mit Wert `1` | Ready-/Exchange-State aktiv |
| `0x12` | `FUN_006e9e20(local_20, 0)` | Lock-Flag fuer Character loeschen |
| `0x13` | Callback `0x0a` mit Wert `0` | Ready-/Exchange-State aus |
| `0x14` | Callback `0x0b` | Trade-UI Event, wahrscheinlich Complete/ClientLock-nah |
| `0x15` | Callback `0x0c` | Trade-UI Event, wahrscheinlich Cancel/Error-nah |
| `0x16` | Callback `0x0d` | Trade-UI Event, wahrscheinlich Error/InventoryFull-nah |
| `0x17` | Callback `2` mit `local_18` | Geldbetrag eigener/anderer Teilnehmer aktualisieren |
| `0x18` | Callback `3` mit `local_18` | zweiter Geldbetrag aktualisieren |
| `0x19` | Callback `0x10` mit `local_20` und `local_1c` | Status-/Fehlercode mit zwei IDs/Werten |

Die Callbacknummern gehen an `FUN_004e4070(...)`, also in das registrierte Modulcallback-/Eventsystem. Die UI-Events `PT_OpenRequest`, `PT_OpenUIEvent`, `PT_ClientLock`, `PT_ClientUnlock`, `PT_ActiveReadyToExchange`, `PT_ClientReadyToExchange`, `PTMSG_*` duerften dort angebunden sein.

## Lokale Trade-Daten am Character

Mehrere Funktionen holen aus einer Character-ID zunaechst das Characterobjekt und danach Private-/Itemdaten via `FUN_0053af60`.

Sichtbare Offsets:

| Offset | Nutzung | Interpretation |
|---:|---|---|
| `+0x16c` | bei Server-Op `0x06` auf `local_1c` gesetzt | Trade-Partner-ID, Session-ID oder Money/State-Feld |
| `+0x17c` | bei Op `0x10/0x12` auf `1/0` gesetzt | Lock-Flag fuer Private Trade |
| `+0x1d8` bis `+0x208` | Dreiergruppen werden geloescht/geprueft | eigene/andere Trade-Itemslots |

`FUN_0058ffa0(...)` loescht offenbar Trade-/Itemdaten eines Charakters. Es wird bei Cancel/Close/Session-Reset mehrfach gerufen.

## UI- und Item-Schutz

Es gibt einen String `CannotAuctionInPrivateTrade`. Der Client verhindert also mindestens UI-seitig, dass Auktion/PrivateTrade gleichzeitig oder unpassend genutzt werden.

Wichtig: Das ist kein ausreichender Schutz. Server-seitig muessen Auction, Mail, Bank, NPC-Shop, Inventory-Move und PrivateTrade dieselben Iteminstanzen gegen parallele Reservierung sperren.

## Vermuteter Ablauf

### 1. Trade anfordern

1. Spieler waehlt Zielcharakter.
2. UI `PT_RequestTrade` loest einen Modul-7-Send aus.
3. Client validiert Zielcharakter lokal.
4. Paket enthaelt Ziel-CID.
5. Server prueft Reichweite, Zustand, Blocklisten/Trade-Flags und ob beide Spieler frei sind.

### 2. Anfrage beim Ziel

1. Server sendet Modul-7-Op fuer Request/Popup.
2. Client zeigt `PT_OpenRequest` / `Diaplay_PT_Request`.
3. Ziel klickt Accept oder Reject.
4. Client sendet kurzes Modul-7-Antwortpaket.

### 3. Trade-Session oeffnen

1. Server sendet wahrscheinlich Op `0x06`.
2. Client loescht alte Trade-Daten beider Teilnehmer.
3. Client setzt ein Feld bei `+0x16c`.
4. UI-Callback `8` oeffnet/initialisiert die Trade-UI.

### 4. Items und Geld setzen

1. Drag/Drop von Items trifft normale Item-/Grid-Handler.
2. Bei Itemstatus `6` wird `FUN_006e9a80` benutzt.
3. Client sendet zwei Nested-Grid-Pakete mit Quell-/Zielpositionen.
4. Geldfeld wird aus UI-Text gelesen, per `atoi` in Integer gewandelt und gesendet.
5. Server aktualisiert die Trade-Session und broadcastet die neuen Item-/Geldwerte an beide Clients.
6. Empfangene Geldwerte kommen wahrscheinlich ueber Op `0x17` und `0x18`.

### 5. Lock / Unlock

1. Spieler sperrt sein Angebot.
2. Client sendet kurzes Modul-7-Paket.
3. Server prueft, dass alle angebotenen Items/Geldwerte noch gueltig sind.
4. Server sendet Op `0x10` oder `0x12`; Client setzt `tradeData + 0x17c` auf `1` oder `0`.
5. UI aktualisiert Lock/Unlock-Anzeige.

### 6. ReadyToExchange / Commit

1. Nach Lock bestaetigt Spieler final per `PT_ReadyToExchange`.
2. Handler `FUN_0074e4c0` sendet `FUN_006e9d00`.
3. Server wartet auf beide Ready-Zustaende.
4. Server fuehrt den Austausch atomar aus.
5. Server sendet Erfolg/Cancel/Error/InventoryFull-Events, wahrscheinlich ueber Ops `0x14`, `0x15`, `0x16` und UI-Messages `PTMSG_*`.

## Server-Datenbank-Inferenz

Private Trade erlaubt recht klare Rueckschluesse auf notwendige Serverdaten. Das sind keine Client-Strings, sondern technische Notwendigkeiten aus dem Protokoll.

### Permanente Tabellen

`characters`

- `character_id`
- `account_id`
- `name`
- `level`
- `current_map`
- `x`, `y`, `z`
- Trade-relevante Flags: online, busy, dead, in_private_trade, no_trade_mode

`item_instances`

- `item_instance_id`
- `owner_character_id`
- `template_id`
- `stack_count`
- `durability`
- `enhance/socket/option fields`
- `bind/tradeable flags`
- `container_type`
- `slot_x`, `slot_y` oder linearer Slot
- `locked/reserved_by_trade_session`

`character_money`

- `character_id`
- `money/ghelld`
- eventuell getrennte Ledger-/Auditfelder

### Transiente Serverstrukturen

`private_trade_sessions`

- `trade_session_id`
- `character_a_id`
- `character_b_id`
- `state`: requested, accepted, open, locked, ready, committed, cancelled, failed
- `requester_id`
- `created_at`
- `updated_at`
- `cancel_reason` / `error_code`
- `a_locked`, `b_locked`
- `a_ready`, `b_ready`
- `a_money`, `b_money`

`private_trade_items`

- `trade_session_id`
- `owner_character_id`
- `item_instance_id`
- `source_container`
- `source_slot`
- `trade_slot`
- `stack_count`
- `reserved_at`

`item_locks`

- `item_instance_id`
- `lock_type = private_trade`
- `owner_character_id`
- `trade_session_id`
- `created_at`
- `expires_at`

`money_reservations`

- `trade_session_id`
- `character_id`
- `amount`
- `created_at`

### Audit/Anti-Dupe

Ein echter Server braucht fuer Private Trade fast sicher ein Audit:

`trade_audit`

- `trade_session_id`
- `character_a_id`
- `character_b_id`
- `result`
- `started_at`
- `committed_at`
- `cancelled_at`
- `reason_code`

`trade_audit_items`

- `trade_session_id`
- `from_character_id`
- `to_character_id`
- `item_instance_id`
- `template_id`
- `stack_count`
- `before_container`
- `before_slot`
- `after_container`
- `after_slot`

`money_ledger`

- `ledger_id`
- `character_id`
- `delta`
- `reason = private_trade`
- `trade_session_id`
- `balance_before`
- `balance_after`
- `created_at`

## Sicherheitsrelevante Punkte

- Client validiert Trade-Ziel, Geldbetrag und teilweise Item/Grid-Kontext, aber der Server darf dem nicht vertrauen.
- `atoi` bedeutet: Eingabe ist lokal simpel numerisch, aber Server muss integer overflow, negative Werte und Formatfehler selbst abfangen.
- Geld wird lokal auf verfuegbares Geld gekappt; Server muss Saldo erneut pruefen.
- Itembewegungen enthalten Grid-/Slotinformationen; Server muss Besitz, Container, Stacksize, Tradeability und Lockstatus validieren.
- Lock/Ready muss serverseitig jede Angebotsaenderung invalidieren. Sonst koennen Race Conditions oder Dupe-Zustaende entstehen.
- Commit muss atomar laufen: entweder beide Item-/Geldtransfers gelingen komplett oder alles bleibt unveraendert.

## Noch offene Detailarbeit

- Die Label-Handler `LAB_0074e240`, `LAB_0074e410`, `LAB_0074e420`, `LAB_0074e430`, `LAB_0074e810`, `LAB_006d4220` sollten im Disassembly/Ghidra-Controlflow weiter aufgeloest werden.
- Die genauen Subopcode-Werte fuer `FUN_006e9690`, `FUN_006e97f0`, `FUN_006e9890`, `FUN_006e9960`, `FUN_006e9bc0`, `FUN_006e9c60`, `FUN_006e9d00` sind in der Pseudocode-Ausgabe teilweise durch Ghidra-Stacknamen verdeckt. Nur echte gesetzte Konstanten wie `local_5 = 4` und Server-Ops aus dem Switch sollten als harte Werte gelten.
- Die Callbacknummern `0x0b`, `0x0c`, `0x0d` sollten gegen die UI-Event-Registrierung gemappt werden, um `TradeComplete`, `TradeCancel`, `Error` und `InvenFull` exakt zu trennen.
