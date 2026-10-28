# Sequenz 32: Modularisierung beider Server + Equip-Slot-Konfliktbehandlung

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-14

Zwei Themen in einer Session: (1) beide Rust-Crates (`alefgame-server`, `aleflogin-server`) von je einer ~2500-4000-Zeilen-`main.rs` in fachliche Module aufgeteilt, inklusive Unit-Tests; (2) beim anschließenden Live-Verifizieren ein echter, vorher unentdeckter Bug gefunden und behoben: gleichzeitig ausgerüstete, kollidierende Waffen/Schilde.

## 1. Modularisierung

Reiner Code-Umzug, keine Verhaltensänderung. Methodik: Python-Skript extrahiert zusammenhängende Codeblöcke (Konstanten/Structs/Funktionen inkl. ihrer Doc-Kommentare, per Lookback bis zur letzten Nicht-Kommentar-Zeile) aus der alten `main.rs` in neue Modul-Dateien, macht alle verschobenen Symbole `pub(crate)` (inkl. Struct-Felder), und jedes neue Modul importiert alle Geschwister-Module via `use crate::x::*;`. Anschließend `cargo build` iterativ zum Auflösen fehlender/doppelter Imports, `cargo fix`/gezieltes Script zum Entfernen ungenutzter Glob-Imports, `cargo fmt`.

**`alefgame-server`** (4033 → 11 Dateien):
`net` (Verbindungsverwaltung, Handshake, `send_reply`, Account-Kick-Listener), `dispatch` (der eine Opcode-Router), `session` (`REQUEST_CLIENT_CONNECT`/`LOADING_COMPLETE`), `character` (Factors/Stats/HP/EXP/Angriff/Verteidigung), `items` ([`AgpmItem`](../Module/AgpmItem.md): Inventar/Equip/Use/Destroy), `movement` ([`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md) CharMove), `npc` (Sichtbarkeit, Dialog-/Handelsbindung), `npc_trade` (Kauf/Verkauf), `monsters` (Spawn-Sichtbarkeit), `cash_mall` (Chantra-Shop + [`AgpmBillInfo`](../Module/AgpmBillInfo.md)), `return_to_login`.

**`aleflogin-server`** (2454 → 9 Dateien):
`net`, `dispatch` (hier bleibt der Login-Flow größtenteils inline im Router, da real ein einziger großer State-Machine-artiger Ablauf), `login` ([`AgpmLogin`](../Module/AgpmLogin.md)-Paketbau/-Parsing), `character` ([`AgpmCharacter`](../Module/AgpmCharacter.md) ADD/REMOVE + Factor-Packet für die Charakterauswahl), `items`/`optimized_view` (Ausrüstungs-Anzeige in der Charakterauswahl), `world` ([`AgpmWorld`](../Module/AgpmWorld.md)), `return_to_login`.

**Tests** (neu, 11 Stück, alle pinnen echte, in früheren Sessions gefundene Bugs als Regressionsschutz):
- `alefgame-server::items`: Equip/Unequip-Pakete round-triplen durch ihre eigenen Request-Parser; `peek_item_update_status` unterscheidet beide Richtungen korrekt.
- `alefgame-server::npc_trade`: Preis wird als f32-Bitmuster kodiert, nicht als Plain-Int (der allererste Bug dieses Projekts).
- `alefgame-server::character`: CON/STR/etc. ×100-Skalierung; EXP steht in EXP_HIGH, nicht EXP_LOW.
- `alefgame-server::movement`: CharMove round-tript durch Build/Parse.
- `aleflogin-server::character`: `race == -1` lässt das CharType-Unterpaket weg; reale Bewegungsgeschwindigkeit (2000/6000) korrekt gesetzt.
- `aleflogin-server::net`: `seed_key_setup_payload` liefert 32 Bytes (Schlüssel + Nullen), nicht nur 16.

`cargo test --workspace`: 28/28 grün (7 + 8 + 9 + 4, letztere zwei aus den bereits vorher existierenden `aleflogin-crypto`/`aleflogin-proto`-Testsuiten).

## 2. Live-Verifikation deckt echten Bug auf: Waffen-/Schild-Slot-Konflikt

Beim Durchtesten des frisch modularisierten Codes (Equip/Unequip, dann Charakterauswahl-Anzeige geprüft): Rüstungsteile wurden korrekt angezeigt, aber die Waffe nicht. Ursache lag NICHT am Umbau (reiner Code-Motion), sondern an einer vorbestehenden Lücke: der Test-Charakter hatte gleichzeitig zwei Einhandschwerter (Kurzschwert TID 11 + Scimitar TID 31) UND zwei Schilde (Holzschild TID 8 + Turmschild TID 23) auf `status = 'equipped'` stehen.

**Root Cause** (verifiziert im EP8-Quellcode):
- Der reale Client sendet beim Ausrüsten ([`AgcmItem`](../Module/AgcmItem.md):SendEquipInfo`, `AgcmItem.cpp:1385-1428`) NUR das neue Item, ohne vorher ein Unequip für das alte zu senden — Slot-Konfliktbehandlung ist keine Client-Aufgabe.
- Der reale Server (`AgpmItem::EquipItem`, `AgpmItemEquip.cpp:206-354`) löst `lEquipPart = pcsAgpdItemTemplate->m_nPart` auf, sucht das aktuell in diesem Part sitzende Item (`GetEquipItem`), und räumt es per `AddItemToInventory` zurück ins Inventar, BEVOR das neue Item eingefügt wird.
- Kollision wird über `AgpdItemTemplateEquip::m_nPart` bestimmt (Enum `AgpmItemPart`, u.a. `HAND_LEFT=9`, `HAND_RIGHT=10`) — ein autoriertes Feld pro Item-Template, nicht aus generischen Type/SubType-Spalten ableitbar (`AgpmItemStream.cpp:243-263,452-462`).
- Dieses Projekt hatte diese Eviction-Logik nie implementiert — der Server erlaubte beliebig viele gleichzeitig "equipped" markierte Items im selben konzeptionellen Slot.

**Fix:**
- Migration `0026_item_equip_slot.sql`: neue Spalte `item_templates.equip_slot` (`'weapon'`/`'shield'`/`NULL`), befüllt aus `itemdatatable.txt`'s FirstCategoryName (`*Weapon*` → `weapon`) / SecondCategoryName (`Shield` → `shield`) — die real verfügbare Annäherung an `m_nPart`, da dieses Projekt kein dekodiertes `m_nPart`/`m_nKind` besitzt. 848 Items klassifiziert.
- `handle_item_equip_request` (`alefgame-server/src/items.rs`): vor dem Ausrüsten wird geprüft, ob bereits ein anderes Item mit demselben `equip_slot` ausgerüstet ist (`db::find_equipped_item_in_slot`); falls ja, wird es automatisch in den ersten freien Inventarplatz verschoben (`db::first_free_inventory_slot` + `set_item_unequipped`), inklusive Unequip-Paket an den Client und Broadcast an andere Spieler — bevor das neue Item ausgerüstet wird.

**Bewusst nicht abgedeckt:** Zweihandwaffen, die eigentlich zusätzlich den Schild-Slot blockieren müssten (und umgekehrt) — aus den verfügbaren Kategoriedaten nicht zuverlässig ableitbar (Bogen/Armbrust/Stab sind trotz faktischer Zweihändigkeit nicht als "Two-Handed" benannt). Kein aktuell gemeldeter Bug dazu.

**Live bestätigt 2026-09-14** (Log-Auszug):
```
AgpmItem: equip UPDATE evicted a same-slot item back to inventory ... evicted_item_id=91 (Scimitar) equip_slot="weapon"
AgpmItem: equip UPDATE succeeded ... item_id=1 (Kurzschwert)
```
Gleiches Muster unmittelbar danach auch für die beiden Schilde. DB-Stand nach dem Test bestätigt exakt das erwartete Ergebnis (Kurzschwert + Holzschild `equipped`, Scimitar + Turmschild `inventory`).

## Migrationen

| # | Zweck |
|---|---|
| 0026 | `item_templates.equip_slot` (Waffe/Schild-Klassifikation für Slot-Konfliktauflösung) |
