# AgcmCashMall (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmCashMall` (Cash-Shop: Liste, Kauf, Cash-Aktualisierung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, `OnDestroy`, `CBUpdateMallList`, zwei der vier Sendefunktionen und die Scheingegenstände (`CreateDummyItem`, `DestroyAllDummyItem`) zugeordnet. `SendPacketRefreshCash` und `SendPacketCheckListVersion` wurden nicht gefunden: zwischen `0x006E38CC` und `0x006E3970` hat der Export keine Funktion angelegt, dort liegen vermutlich genau diese beiden Methoden.
- **OnAddModule** (`0x006E3C40`): fünf Module in Quellreihenfolge ([`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmCashMall`](AgpmCashMall.md), `AgcmCharacter`, [`AgcmItem`](AgcmItem.md)) und der Rückruf `CBUpdateMallList` (`0x006E3B20`) bei `AgpmCashMall`.
- **Senden:** `SendPacketRequestMallList(lTab)` (`0x006E3810`, Paketbauer `0x0087C360`) und `SendPacketBuyProduct(lProductID, lType)` (`0x006E3870`, Bauer `0x0087C3B0`); beide prüfen `Länge > 0xC` (= `sizeof(PACKET_HEADER)`) und senden über `SendPacket`.
- **Scheingegenstände:** `CreateDummyItem` (`0x006E3970`) legt Gegenstände mit Gitter-Texturen an (`AgcmItem::SetGridItemAttachedTexture`), `DestroyAllDummyItem` (`0x006E3A70`) gibt sie über `ReleaseGridItemAttachedTexture` frei und wird von `OnDestroy` (`0x006E3B10`) und `CBUpdateMallList` gerufen.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmCashMall.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E3C40` | 155 | vtable/String |
| 1 | `OnDestroy` | `0x006E3B10` | 11 | vtable/String |
| 2 | `SendPacketRequestMallList` | `0x006E3810` | 87 | von Hand geprüft |
| 3 | `SendPacketBuyProduct` | `0x006E3870` | 92 | von Hand geprüft |
| 4 | `SendPacketRefreshCash` | – | | vermutlich im Lückenbereich `0x006E38CC`–`0x006E3970` (Export hat dort keine Funktion) |
| 5 | `SendPacketCheckListVersion` | – | | vermutlich im Lückenbereich `0x006E38CC`–`0x006E3970` (Export hat dort keine Funktion) |
| 6 | `CreateDummyItem` | `0x006E3970` | 244 | von Hand geprüft |
| 7 | `DestroyDummyItem` | – | | in `DestroyAllDummyItem` eingebaut |
| 8 | `DestroyAllDummyItem` | `0x006E3A70` | 119 | von Hand geprüft |
| 9 | `CBUpdateMallList` | `0x006E3B20` | 282 | Callback-Registrierung |

7 von 10 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006E37C0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA4` | `Zeiger auf `AgcmCharacter` (dessen Feld `+0x15964` ist die eigene Charakter-ID, wie bei den anderen Ereignismodulen)` | `SendPacketRequestMallList`, `SendPacketBuyProduct` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Deutung von `this+0xBA4` als `AgcmCharacter` folgt aus der Modulreihenfolge in `OnAddModule` (fünftes Modul `AgcmCharacter` an vierter Stelle nach `AgpmFactors`, `AgpmItem`, `AgpmCashMall`) und dem Feldzugriff `+0x15964` (eigene Charakter-ID, wie in [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md)); die Feldnamen der Quelle wurden nicht nachgeprüft.
- `CreateDummyItem` und `DestroyAllDummyItem` sind über die Aufrufe der Gitter-Textur-Funktionen von `AgcmItem` zugeordnet, nicht Zeile für Zeile verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 2, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md), [`AgcmItem`](AgcmItem.md), [`AgpmCashMall`](AgpmCashMall.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md)
- **Erwähnt in:** [`AgcmUICashMall`](AgcmUICashMall.md)
