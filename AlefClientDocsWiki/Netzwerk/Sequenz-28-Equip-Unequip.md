# Sequenz 28: Ausrüsten/Ablegen (Equip/Unequip)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-13

Kurze Folge-Session auf Sequenz 27: das Character-Info-Fenster zeigte zwar Stats/Slots an, aber Items ließen sich weder ablegen noch tauschen. Diese Sequenz implementiert und bestätigt live das Ausrüsten und Ablegen von Items.

## Protokoll

Beide Richtungen laufen über [`AgpmItem`](../Module/AgpmItem.md), Operation `AGPMITEM_PACKET_OPERATION_UPDATE = 2` (`Include/AgpmItem.h:141`) — es gibt keine eigenen Equip/Unequip-Opcodes. Die Felder danach unterscheiden sich je nach Ziel-Status:

- **Ausrüsten** — realer Client-Request [`AgcmItem`](../Module/AgcmItem.md):SendEquipInfo` (`AgcmItem.cpp:1385-1439`): Operation+Status(`EQUIP=3`)+ItemID+OwnerCID+ein **leeres** verschachteltes Equip-Feld, Maske `0x217`.
- **Ablegen** — realer Client-Request `AgcmItem::SendInventoryInfo` (`AgcmItem.cpp:1178-1243`): Operation+Status(`INVENTORY=2`)+ItemID+OwnerCID+ein verschachteltes Inventory-Feld mit Tab/Row/Column (1-Byte-Maske, Bit0=Tab, Bit1=Row, Bit2=Column, je INT16), Maske `0x97`.

**Wichtiger Fund:** Das Equip-Feld trägt nie einen Körperslot. Der Client leitet den Slot rein clientseitig aus dem Item-Template selbst ab (`AGPMITEM_EQUIP_KIND_*` in `AgcmItemEquip.cpp`, z.B. ARMOUR/WEAPON/SHIELD/RING/NECKLACE). Der Server muss also gar keine Slot-Zuordnung führen oder Konflikte auflösen (anders als in Sequenz 27 noch vermutet) — er muss dem Client nur bestätigen, dass Status jetzt `EQUIP` ist, und der Client zeichnet den Rest selbst.

Da beide Request-Formen inhaltlich bereits die volle Antwort sind, ist die Serverantwort einfach: dieselbe Paketform mit Operation `UPDATE` unverändert zurückschicken, sobald die DB-Änderung durchgeführt wurde. Genau wie bei Bewegung ([`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md)) wird dieselbe Nachricht zusätzlich an alle anderen Online-Spieler gebroadcastet, da Ausrüsten das sichtbare Aussehen des Charakters ändert.

## Implementierung

- `handle_item_equip_request`: prüft, dass das Item dem anfragenden Charakter gehört und aktuell `status = 'inventory'` ist, setzt `status = 'equipped'` (Gridposition wird genullt), schickt `build_item_equip_update_packet` zurück, broadcastet an alle anderen Spieler, und schickt zusätzlich ein [`AgpmCharacter`](../Module/AgpmCharacter.md)-Factor-Update (Angriff/Verteidigung ändern sich ja mit der Ausrüstung).
- `handle_item_unequip_request`: prüft `status = 'equipped'`, verwendet die vom Client mitgeschickte Ziel-Row/Column oder — falls der Client keine sendet (`nInvIdx == -1`) — den ersten freien Inventarslot (`db::first_free_inventory_slot`, dieselbe Logik wie beim Kauf), setzt `status = 'inventory'` mit dieser Gridposition, schickt `build_item_unequip_update_packet` zurück, broadcastet, aktualisiert Factors.
- Beide Handler validieren die Item-Eigentümerschaft strikt aus der DB (nicht aus den vom Client mitgeschickten Feldern), gleiches Muster wie überall sonst in diesem Projekt.
- `character_items.slot_index` (Körperslot) bleibt unbenutzt — siehe oben, wird nicht gebraucht.

**Live bestätigt 2026-09-13**: Ausrüsten und Ablegen funktionieren.

## Offene Punkte (unverändert aus Sequenz 27)

1. WCoin-Anzeige im Chantra-Shop (vermutlich externes Billing-Gateway).
2. "Defense -5"-Rest im Character-Info-Fenster (fehlende Datenquelle für Charakter-Basiswert).
