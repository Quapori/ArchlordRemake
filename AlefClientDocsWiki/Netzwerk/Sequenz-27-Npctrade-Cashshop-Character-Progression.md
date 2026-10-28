# Sequenz 27: NPC-Handel-Abschluss, Chantra-Shop und Charakter-Progression

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-13

Diese Sequenz dokumentiert eine lange Session voller live getesteter Fixes und neuer Features, aufbauend auf Sequenz 24-26 (Welteintritt). Schwerpunkte: den NPC-Handel fertigstellen (Verkaufen, Löschen, Charisma/Shrine-Coin-Währungen), den Chantra-/Cash-Shop ([`AgpmCashMall`](../Module/AgpmCashMall.md)) neu implementieren, und die Charakter-Progression (Level/EXP, Basis-Attribute, Angriff/Verteidigung) korrekt an den Client senden.

## 1. Der NPC-Handel-Preis-Bug: `GetNPCPrice` bit-castet Int als Float

**Symptom:** Kaufbestätigungsdialog zeigte immer 0 Gold, unabhängig vom tatsächlichen Preis.

**Ursache** (`AgpmItem.cpp:6657-6674`, aktive Implementierung von [`AgpmItem`](../Module/AgpmItem.md):GetNPCPrice`):

```cpp
float AgpmItem::GetNPCPrice(AgpdItem *pcsItem)
{
    PVOID pvItemPrice = m_pagpmFactors->GetFactor(&pcsItem->m_csFactor, AGPD_FACTORS_TYPE_PRICE);
    if (pvItemPrice) fItemPrice = *((float *) pvItemPrice);   // roher Bit-Cast!
    return fItemPrice;
}
```

Das liest die ersten 4 Bytes des Preis-Faktor-Blocks direkt als IEEE-754-Float, nicht als Integer konvertiert. `AGPD_FACTORS_PRICE_TYPE_NPC_PRICE = 0` (`AgpdFactors.h:175`) liegt exakt an Offset 0 — der Slot, den `AgcmEventNPCTrade::ProcessItemList` (`AgcmEventNPCTrade.cpp:204`, `SetNPCTradeGheld`) aus unserem `DetailInfo.Price`-Feld befüllt. Ein gesendeter Plain-Integer (z.B. 19800) wird clientseitig als Bitmuster eines Float interpretiert — eine denormalisierte Zahl nahe 0.

**Fix:** Preis als LE-Bytes des eigenen f32-Bitmusters senden (`(price as f32).to_bits().to_le_bytes()`), nicht als Integer.

**Zweiter Bug, direkt danach gefunden:** `GetPriceNPCTradeItem` (`AgcmUINPCTrade.cpp:748`) multipliziert selbst noch `GetNPCPrice(item) * item.m_nCount`. Das Wire-Feld muss also der **Stückpreis** sein, nicht der in unserer DB gespeicherte Gesamtpreis für die jeweilige Stack-Größe — sonst wird der Preis quadratisch falsch (z.B. `19800 * 99 = 1.960.200`).

Beide Fixes live bestätigt: korrekte Anzeige (19.800 Gold für 99er Medium-Mana-Potion-Stack).

## 2. NPC-Handel: Verkaufen und Item-Zerstörung

- **SELLITEM** ([`AgpmEventNPCTrade`](../Module/AgpmEventNPCTrade.md), Operation `3`): Maske `0x1f` (EventBase+Operation+CID+IID+DetailInfo), DetailInfo-Maske `0x7c` (StackCount+Status+Layer+Row+Column). Preis kommt aus `item_templates.pc_price` (migration `0018`, `itemdatatable.txt`'s "PC Price"-Spalte), nicht aus Client-Daten. Live bestätigt beim ersten Versuch.
- **REQUEST_DESTROY_ITEM** (`AgpmItem`, Operation `21`): Maske `0x15` (Operation+ItemID+OwnerCID), 1:1 aus `AgpmItem::MakePacketRequestDestroyItem` (`AgpmItem.cpp:5813-5839`) übernommen. Kein Bestätigungspaket nötig — nur ein normales `REMOVE`.
- **USE_ITEM** (`AgpmItem`, Operation `3`): gleiche Feldform wie DESTROY_ITEM (Maske `0x15`). Tränke heilen HP/MP/SP anhand echter Werte aus `itemdatatable.txt`'s "HP"/"SP"/"MP"-Spalten (migration `0023`, 71 echte Items), gedeckelt aufs reale Maximum. Stack wird reduziert/entfernt. Ermöglicht die automatische Tränke-Nutzung der Inventar-Quickslots (rein clientseitige Schwellenwert-Logik, die einfach dieselbe Anfrage sendet).

## 3. Charisma-Punkte und Shrine Coins

Zwei reale Datenfehler in der ursprünglichen `npctradeitemlist.txt`-Importlogik gefunden und behoben (migration `0019`):

1. **Bruchzahlige Stückpreise** (z.B. Pfeil/Bolzen bei 0,1 Gold/Stück): Die ursprüngliche Importlogik castete den Stückpreis *vor* der Multiplikation mit der Stückzahl auf `int` (`int(float("0.1"))` = 0), wodurch der Gesamtpreis immer 0 wurde. Fix: erst multiplizieren, dann runden.
2. **Fehlende Charisma-/Shrine-Coin-Preise**: `itemdatatable.txt`'s "NPC Charisma Price"/"NPC Shrine Coin"-Spalten wurden nie importiert. Betraf u.a. Noctorn/Ashi (reine Shrine-Ausrüstungshändler, NPC-Price=0) — ihr komplettes Sortiment wurde vom `price > 0`-Filter rausgefiltert.

**Charisma Points** sind ein Charakter-Stat (`characters.charisma_points`, migration `0020`), analog zu Gold — [`AgpmCharacter`](../Module/AgpmCharacter.md):GetCharismaPoint` in echt. **Shrine Coins** sind dagegen ein normales Inventar-Item (`AGPMITEM_SHRINECOIN_TID = 53000`), gezählt über `GetItemTotalCountFromGrid` — kein Charakter-Stat. Käufe mit Shrine-Rang-Items (`AgsmEventNPCTrade::BuyShrineItem`, `AgsmEventNPCTrade.cpp:757-855`) prüfen/verbrauchen beide Währungen; unser Server bildet das über `handle_npc_trade_buy_shrine_item`/`handle_npc_trade_buy_normal_item` als getrennte Pfade nach.

## 4. Chantra-/Cash-Shop (`AgpmCashMall`)

Reales Protokoll komplett rekonstruiert (kein NPC-gebunden — eigenständiger Kanal, Opcode `0x2E`, `Include/ApDefine.h:647`):

- Ein Paket-Typ für alle 7 Operationen (`Include/AgpmCashMall.h:45-53`, ab `= 1` gezählt), 2-Byte-Maske: Operation, Result, MallListVersion, CID, Tab, ProductID, MallTabList (`AUTYPE_MEMORY_BLOCK`), ItemList (`AUTYPE_MEMORY_BLOCK`), Type.
- `AUTYPE_MEMORY_BLOCK` ist simpler als `AUTYPE_PACKET`: nur `[u16 Länge][Rohbytes]`, keine eigene Maske (`AuPacket.cpp:217-224,359-366,524-535`).
- Tab-/Produktlisten sind **textkodierte Strings** (kein Bitmuster-Risiko wie bei Preisen): `"<Name>;<ProduktID>,<ProduktID>,...,:"` für Tabs, `"<ProduktID>,<ItemTID>,<Menge>,<Preis>,<Flag>,<Beschreibung>:"` pro Produkt (`AgpmCashMall.cpp:365-527`).
- Käufe landen im **Chantra-Sack** = eigenes Grid, 1×200×1 Slots (`Include/AgpdItem.h:91-93`, `AGPMITEM_CASH_INVENTORY_*`), Status `AGPDITEM_STATUS_CASH_INVENTORY = 51` — dieselbe Item-Maschinerie wie normales Inventar, nur andere Grid-Zuordnung.
- Katalog: 15 handverlesene, aber echte Cash-Items (`itemdatatable.txt`'s "Cash"-Spalte, 569 echte Treffer) mit **synthetischen** WCoin-Preisen (keine echte Preistabelle in den verfügbaren Daten gefunden) — migration `0021`.

**Offen/pausiert:** Die WCoin-Guthabenanzeige im Shop bleibt bei 0, unabhängig von `characters.cash`. Realer Client (bestätigt `_AREA_GLOBAL_`-Build, die echte europäische Webzen-Version) liest die Anzeige auf `AgcmUICashMall.cpp:900-911` exklusiv über `AgpmBillInfo::GetCashGlobal()`, nicht über `AgpmCharacter::GetCash()`. Das zugehörige Netzwerkpaket (`AGPMBILL_OPERATION_CASHINFO`, Opcode `0x4E`) wird im verfügbaren Quellcode von **keiner** Stelle je gebaut/gesendet — der reale Fluss läuft vermutlich über ein externes Webzen-Billing-Gateway außerhalb des Spielsockets. Zwei Versuche (Paket selbst nachgebaut, Feldreihenfolge exakt nach Quellcode) ohne sichtbaren Effekt. Status: pausiert.

## 5. EXP/Level-System

- **Level-Kurve**: `level_up_exp.ini` (Drittanbieter-Emulator-Datei, wie schon bei den Monster-Spawns gegengecheckt), 121 Zeilen, **kumulative** Gesamt-EXP pro Level (migration `0022`, Tabelle `level_exp_requirements`). Das Delta pro Level (`exp_required(level) = kumulativ[level] - kumulativ[level-1]`) ist das, was der Client als `CharPointMax`-Anforderung erwartet.
- **`characters.exp`** ist als "Fortschritt innerhalb des aktuellen Levels" definiert (reset bei Level-Up), nicht als Lifetime-Total — das entspricht, wie der Client seine EXP-Leiste tatsächlich berechnet (reine Current/Max-Ratio, keine Basiswert-Subtraktion).
- **`normalize_level_and_exp`**: bei jedem Login (`LOADING_COMPLETE`) wird geprüft, ob `exp >= exp_required(level)`; falls ja, wird wiederholt hochgelevelt (und `exp` entsprechend reduziert) und das Ergebnis in die DB zurückgeschrieben — unabhängig davon, ob die Diskrepanz durch manuellen DB-Edit oder künftigen In-Game-EXP-Gewinn entstand.
- **EXP_LOW/EXP_HIGH-Bug**: Das Charakter-Info-Fenster (`AgcmUICharacter.cpp:1333-1415`) liest EXP **nicht** direkt aus `CharPoint.EXP_LOW`, sondern über `AgpmFactors::GetExp()`/`GetMaxExp()` (`AgpmFactors.cpp:4044-4076`), die einen 64-Bit-Wert **vertauscht** zusammensetzen: `llExp = EXP_HIGH + (EXP_LOW << 32)`. Ein kleiner echter Wert im (falschen) `EXP_LOW`-Feld ergibt astronomische Zahlen; die Aktionsleiste (reine Prozent-Anzeige) blieb davon unberührt, da sich der gemeinsame Skalierungsfaktor in einem Verhältnis herauskürzt — das verschleierte den Bug zunächst. Fix: echten Wert in `EXP_HIGH` senden, `EXP_LOW = 0`.
- **Charakterauswahl-Bildschirm zeigt bewusst kein EXP%**: [`AgpmFactors`](../Module/AgpmFactors.md):MakePacketFactorsCharView` (`AgpmFactors.cpp:1167-1207`) sendet nachweislich nur HP/Level/Movement — Exp ist im echten Server für dieses Paket absichtlich ausgeschlossen. Nicht unser Bug.

## 6. Basis-Attribute (CON/STR/INT/DEX/CHA/WIS)

Quelle: `grow_up_factor.ini` (Drittanbieter-Emulator), pro Charakter-Template-TID (`characters.race_tid`) und Level (migrationen `0022`/`0024`, Tabelle `character_level_stats`). Kein LUK-Wert in dieser Datei gefunden — bleibt 0.

**Fixpunkt-Skalierung**: `AgpdFactorCharStatusType`-Indizes 0-6 (CON..WIS) sind laut `g_bFactorUseFloat[CHAR_STATUS]` alle mit Faktor 100 skaliert (`AgpmFactors.cpp`'s generische `SetValue(INT32)`/`GetValue(FLOAT*)`: `raw = value * 100` / `value = raw / 100.0`). Ohne diese Skalierung wurden reale Werte wie 131 als "1" angezeigt (131/100, abgeschnitten). Level (bit7) und Movement (bit8/9) sind NICHT skaliert.

## 7. Angriff/Verteidigung

- **Range/Attack Speed**: `AgpdFactorAttackType` (`AgpdFactors.h:143-154`), 1-Byte-Maske, unskalierte Ints. Werte kommen vom **ausgerüsteten Item** (`itemdatatable.txt`'s "ATK Range"/"ATK Speed", migration `0025`), nicht vom Charakter-Template — mangels echtem Slot-System nimmt dieses Projekt heuristisch das Maximum über alle ausgerüsteten Items.
- **Verteidigung**: `AGPD_FACTORS_TYPE_DEFENSE -> DefensePoint -> Physical`, doppelt verschachtelt (Defense-Gruppe 1-Byte-Maske → Attribute-Array 2-Byte-Maske, ×100 skaliert wie CON/STR). **Nicht** identisch mit `CharPointMax.DR`/`AgpmCombat::GetDR()` (Formel `(Level+DEX+20)*0.4 + DR-Bonus`) — beide Wege implementiert, beide ohne sichtbaren Effekt auf den beobachteten "-5"-Rest. Keine echte Datenquelle für einen Charakter-eigenen Basis-Verteidigungswert gefunden (`characterdatatable.txt`'s AR/DR/AC sind 0 bei LVL=1; `grow_up_factor.ini` hat keine Verteidigungs-Spalten). Status: pausiert, kosmetischer Rest.

## Offene Punkte

1. **WCoin-Anzeige im Chantra-Shop** (Abschnitt 4) — vermutlich externes Billing-Gateway, keine reine Protokolllücke.
2. **"Defense -5"-Rest** (Abschnitt 7) — fehlende Datenquelle für Charakter-Basiswert.
3. ~~**Ausrüsten/Ablegen** (Equip/Unequip)~~ — erledigt, siehe [Sequenz 28](Sequenz-28-Equip-Unequip.md).

## Neue Migrationen (chronologisch)

| # | Zweck |
|---|---|
| 0018 | `item_templates.pc_price` (Verkaufspreis an NPC) |
| 0019 | Bruchzahl-Preis-Fix + Charisma-/Shrine-Coin-Preise |
| 0020 | `characters.charisma_points` |
| 0021 | Cash-Shop-Katalog (`cash_shop_products`) |
| 0022 | EXP-Kurve (`level_exp_requirements`) + Max-HP/MP/SP pro Level/Template |
| 0023 | Item-Heilwerte (`item_templates.hp_restore`/`sp_restore`/`mp_restore`) |
| 0024 | Basis-Attribute pro Level/Template (CON/STR/INT/DEX/CHA/WIS) |
| 0025 | Item-Kampfwerte (`atk_range`/`atk_speed`/`defense_point`) |
