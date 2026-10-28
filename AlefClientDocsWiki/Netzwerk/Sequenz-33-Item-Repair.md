# Sequenz 33: Reparatur (Blacksmith-NPC)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-14

Erstes von mehreren geplanten NPC-Service-Features (Dialoge/Quests/Repair/Skills). Begonnen wurde mit Repair: kleinstes, in sich geschlossenes Feature aus [`AgpmEventItemRepair`](../Module/AgpmEventItemRepair.md) (Opcode `0x34`, `APDEVENT_FUNCTION_ITEM_REPAIR = 17`).

## Voraussetzung: Item-Haltbarkeit existierte noch gar nicht

`character_items.durability`/`max_durability` gab es zwar als Spalten seit Migration `0004`, wurden aber nie befüllt oder an den Client gesendet — ohne das ist Reparatur bedeutungslos (nichts zu reparieren, Anzeige immer 0/0). Nachgezogen:

- `item_templates.max_durability` (aus `itemdatatable.txt`'s "DUR"-Spalte) und `item_templates.npc_price` (Spalte "NPC Price", **nicht** dieselbe wie `pc_price`/"PC Price" — Reparaturkosten basieren auf [`AgpmItem`](../Module/AgpmItem.md):GetNPCPrice`, bestätigt in `AgpmEventItemRepair::GetItemRepairPrice`, `AgpmEventItemRepair.cpp:219`).
- Neue `character_items`-Zeilen (Käufe) bekommen jetzt echte `durability = max_durability` beim Anlegen.
- Alle bereits bestehenden Zeilen per Migration auf "frisch repariert" (durability = max_durability) zurückgesetzt — da dieses Projekt noch keinen Haltbarkeits-Verlust-Mechanismus hat, wären sie sonst dauerhaft auf 0/0 hängengeblieben.
- [`AgpmFactors`](../Module/AgpmFactors.md)' "Item"-Unterpaket (`AgpdFactors.h`, Envelope-Bit 10 der Factors-Hülle, **nicht** zu verwechseln mit `AgpmItem`s eigenem Bit10 "hier folgt ein Factors-Objekt") überträgt jetzt Durability(Bit0)/MaxDurability(Bit4), unskaliert (`g_bFactorUseFloat[AGPD_FACTORS_TYPE_ITEM]` ist komplett FALSE, kein ×100-Trick wie bei CON/STR). Eingebaut in `build_item_factors_field` (vormals nur PC_PRICE), jetzt sowohl für ausgerüstete als auch Inventar-Items gesendet.

## Welche NPCs reparieren wirklich

Statt (wie ursprünglich erwogen) anhand des Namens "Blacksmith" zu raten, direkt aus der bereits vorhandenen entschlüsselten `npc.ini` extrahiert: NPCs mit einem echten `Function=17`-Unterblock (gleiche Technik wie Migration `0016`s `Function=9`-Trade-Import). Ergebnis: **28 von 623 NPCs**, praktisch ausschließlich "Blacksmith"-benannte (plus ein überraschender Ausreißer: `<Animal Breeder> Fosteros`, id 322 — laut Rohdaten korrekt, nicht händisch korrigiert).

## Protokoll

Gemeinsame Paketform (`AgpmEventItemRepair::m_csPacket`, **1-Byte-Maske**, nicht wie `AgpmItem`s 4-Byte): Operation(Bit0), EventBasePacket(Bit1), CharacterID(Bit2), RepairItemIDs\[20\](Bit3), RepairCost(Bit4,INT64), ResultCode(Bit5).

1. **EVENT_REQ** (Klick auf NPC, Client → Server): Operation+EventBase+CID, Maske `0x07`.
2. **GRANT** (Server → Client): identische Form, echot NPC-CID + Spieler-CID zurück. Öffnet die Reparatur-UI — **kein Item-Vorschlag vom Server**: der Client scannt sein eigenes, bereits bekanntes Inventar selbst nach reparaturbedürftigen Items.
3. **REPAIR_REQ** (Client → Server, nach Auswahl im UI): alle 6 Felder gesetzt, Maske `0x3F` — inklusive einer vom Client selbst geschätzten Reparaturkosten-Summe, die der Server bewusst **ignoriert** (Server rechnet autoritativ neu, gleiches "Client-Daten nie vertrauen"-Muster wie überall sonst im Projekt).
4. **REPAIR_ACK** (Server → Client): nur Operation+CID+ResultCode, Maske `0x25`.

Kostenformel pro Item (`AgpmEventItemRepair::GetItemRepairPrice`, `AgpmEventItemRepair.cpp:201-243`): `(npc_price / max_durability) * (max_durability - durability) * 0.5`, keine Steuer (dieses Projekt modelliert nirgends eine Steuer). Bereits volle Items tragen 0 zu den Kosten bei, zählen aber trotzdem als "gefunden" — eine Anfrage mit ausschließlich bereits vollen Items schlägt laut echtem Quellcode **nicht** fehl (der `ALREADY_FULL`-Ergebniscode existiert im Enum, wird vom echten Server aber nie tatsächlich gesendet).

## Live bestätigt 2026-09-14

Scimitar (30/88 Haltbarkeit) bei Blacksmith Halo (NPC-CID 2000011) für 1977 Gold auf 88/88 repariert, Kontostand korrekt von 302455 auf 300478 reduziert — Log und DB-Stand stimmen exakt überein.

## Migrationen

| # | Zweck |
|---|---|
| 0027 | `item_templates.npc_price`/`max_durability`, `npcs.has_npc_repair` (28 echte NPCs), Backfill bestehender `character_items` auf volle Haltbarkeit |

## Offene Punkte für die restlichen NPC-Services

- Generischer NPC-Dialog (Menü-Inhalte, nicht nur die Bindung) — nächster sinnvoller Schritt laut ursprünglicher Anfrage.
- Quests (`AgpmQuest`/`AgpmEventQuest`) — umfangreichstes verbleibendes System.
- Skills ([`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md)) — braucht erst ein Skill-Datenmodell, existiert noch gar nicht.
- Bank, Refinery, ItemConvert, Product — je eigene Event-Module, noch nicht angefasst.
