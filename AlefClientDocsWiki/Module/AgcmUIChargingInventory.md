# AgcmUIChargingInventory (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Teilbericht zu `AgcmUIChargingInventory.cpp` (Erweitertes Inventar A/B) der Klasse [`AgcmUIItem`](AgcmUIItem.md) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Offsets und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIItem/AgcmUIChargingInventory.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle 14 Methoden sind einer Adresse zugeordnet; vier davon (`BMoveItem`, `BMoveEndItem`, `DragDropB` und `AMoveEndItem`) liegen auf den Adressen ihrer identischen Gegenstücke.
- **Prüfung:** `OpenChargingInventory`, `CloseChargingInventory`, `Enable…`/`Disable…`, `CBChargingInventoryUIUpdate`, `CBChargingInventoryAOpenInvenLayer` und `CBDragDropItemToChargingInventoryA` wurden mit der Quelle verglichen; die Struktur des Verschiebens (elf Herkunftsstatus) ist bestätigt.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIChargingInventory.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `CBChargingInventoryAMoveItem` | `0x00788E20` | 1303 | von Hand geprüft |
| 1 | `CBChargingInventoryAMoveEndItem` | `0x00740320` | 121 | gleiche Adresse wie `CBSubInventoryMoveEndItem` (vom Linker zusammengefaltet) |
| 2 | `CBChargingInventoryUIUpdate` | `0x00789450` | 107 | von Hand geprüft |
| 3 | `CBChargingInventoryAOpenInvenLayer` | `0x00788B40` | 102 | von Hand geprüft |
| 4 | `CBDragDropItemToChargingInventoryA` | `0x00788CF0` | 139 | von Hand geprüft |
| 5 | `OpenChargingInventory` | `0x00789340` | 266 | von Hand geprüft |
| 6 | `CloseChargingInventory` | `0x00788BB0` | 78 | von Hand geprüft |
| 7 | `EnableChargingInventoryA` | `0x00788DD0` | 69 | von Hand geprüft |
| 8 | `DisableChargingInventory` | `0x00788C00` | 119 | von Hand geprüft |
| 9 | `CBChargingInventoryBMoveItem` | `0x00788E20` | 1303 | gleiche Adresse wie `CBChargingInventoryAMoveItem` (vom Linker zusammengefaltet) |
| 10 | `CBChargingInventoryBMoveEndItem` | `0x00740320` | 121 | gleiche Adresse wie `CBSubInventoryMoveEndItem` (vom Linker zusammengefaltet) |
| 11 | `CBChargingInventoryBOpenInvenLayer` | `0x00788C80` | 102 | von Hand geprüft |
| 12 | `CBDragDropItemToChargingInventoryB` | `0x00788CF0` | 139 | gleiche Adresse wie `CBDragDropItemToChargingInventoryA` (vom Linker zusammengefaltet) |
| 13 | `EnableChargingInventoryB` | `0x00788D80` | 69 | von Hand geprüft |

14 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x4F1C / 0x4F24` | `NPC-Handelsfenster offen / Schließ-Ereignis` | `CBChargingInventoryUIUpdate` |
| `0x4F5C` | `Beutel-Typ (1 = A, 2 = B)` | `OpenChargingInventory` |
| `0x4F60 / 0x4F64 / 0x4F68` | `A: Flag offen / Öffnen-Ereignis / Schließen-Ereignis` | `OpenChargingInventory`, `CloseChargingInventory` |
| `0x4F6C / 0x4F70 / 0x4F74` | `B: Flag offen / Öffnen-Ereignis / Schließen-Ereignis` | `OpenChargingInventory`, `CloseChargingInventory` |
| `0x11068 / 0x1106C` | `UI-Zeiger `UI_ExpandedInventoryA` / `B`` | `EnableChargingInventoryA/B`, `DisableChargingInventory` |

## Umfang

`AgcmUIChargingInventory.cpp` enthält 14 Methoden der Klasse `AgcmUIItem` (Erweitertes Inventar A und B). Sie sind auch im Bericht [AgcmUIItem](AgcmUIItem.md) enthalten; dieser Bericht prüft sie im Einzelnen. Eine eigene Klasse `AgcmUIChargingInventory` gibt es weder in der Quelle noch im Binary.

## Öffnen und Schließen (OpenChargingInventory, 0x00789340)

Ablauf wie in der Quelle: Self-Character holen; ist er tot (Status-Byte bei `+0x52A` gleich 2), passiert nichts; fehlt die Berechtigung ([`AgpmItem`](AgpmItem.md):IsEnableChargingInventory`, `0x0058D410`), erscheint der UI-Text `HaveToBuyChargingBag` in einem Meldungsdialog (`0x005979A0`) und das Ergebnis ist 0. Sonst wird nach dem Beutel-Typ (`+0x4F5C`) verzweigt:

| Typ | Ereignis öffnen | Flag „offen“ | Fenster aktivieren |
|---:|---|---|---|
| 1 (A) | `+0x4F64` | `+0x4F60` | `EnableChargingInventoryA` (`0x00788DD0`) |
| 2 (B) | `+0x4F70` | `+0x4F6C` | `EnableChargingInventoryB` (`0x00788D80`) |

`CloseChargingInventory` (`0x00788BB0`) wirft beide Schließ-Ereignisse (`+0x4F68`, `+0x4F74`) und löscht beide Flags.
`EnableChargingInventoryA/B` holen bei Bedarf die UIs `UI_ExpandedInventoryA/B` (`+0x11068`/`+0x1106C`), rufen `DisableChargingInventory` (`0x00788C00`, setzt beide Fenster inaktiv) und aktivieren dann das eigene Fenster (Aktiv-Flag bei Fensterzeiger `+0x1A0`).

## Umschalten (CBChargingInventoryUIUpdate, 0x00789450)

Ist eines der beiden Fenster offen, wird `CloseChargingInventory` aufgerufen, ein offenes NPC-Handelsfenster (Flag `+0x4F1C`, Schließ-Ereignis `+0x4F24`) geschlossen und [`AgcmItem`](AgcmItem.md):CancelCoolDown` (`0x006ECE00`) aufgerufen; sonst wird `OpenChargingInventory` aufgerufen. Das entspricht der Quelle.

## Gegenstand ziehen (CBDragDropItemToChargingInventoryA/B, 0x00788CF0)

Verlangt ein gezogenes Gitterobjekt vom Typ „Gegenstand“ und lehnt Gegenstände im Handelsgitter (Status 6) ab. Sonst wird `AgcmItem::SendChargingInventoryInfo` (`0x006EE2B0`) mit Gegenstands-ID, eigener Charakter-ID (`+0x15964` am Charaktermodul) und dem Ebenenindex des Steuerelements (`+0x130`) sowie zwei Mal −1 für Zeile und Spalte gesendet.

## Verschieben (CBChargingInventoryAMoveItem, 0x00788E20)

Die große Funktion (1303 Byte) verzweigt nach dem Herkunftsstatus des Gegenstands. Alle elf Status der Quelle kommen im Binary mit den erwarteten Zahlenwerten vor:

| Herkunft | Status-Wert |
|---|---:|
| Inventar | 2 |
| Ausrüstung | 3 |
| Handelsgitter | 6 |
| Verkaufsbox | 8 |
| NPC-Handel | 10 |
| Unterinventar | 13 (`0xD`) |
| Erweitertes Inventar | 15 (`0xF`) |
| Cash-Inventar | 51 (`0x33`) |
| Gilden-Lager | 53 (`0x35`) |
| Belagerungsobjekt | 90 (`0x5A`) |
| Bank | 100 |

Das Verschieben innerhalb des erweiterten Inventars verlangt Umschalt-Taste für das Teilen von Stapeln; bei Cash-Gegenständen werden Runen- und Sockel-Initialisierung unterschieden. Dies ist nach der Struktur der Verzweigungen geprüft, die einzelnen Zweige wurden nicht Zeile für Zeile verglichen.

## Zusammengefaltete A/B-Paare

Die Quelle enthält für B Kopien der A-Funktionen. Ein Textvergleich der Quellen zeigt: `CBChargingInventoryBMoveEndItem` und `CBDragDropItemToChargingInventoryB` sind bis auf den Namen identisch; `CBChargingInventoryBMoveItem` unterscheidet sich nur in Leerzeichen und Zeilenumbrüchen eines Aufrufs. Der Linker hat sie deshalb mit den A-Versionen (und `CBChargingInventoryAMoveEndItem` mit `CBSubInventoryMoveEndItem`, `0x00740320`) zusammengefaltet. Nur die Layer-Callbacks unterscheiden sich (A `0x00788B40`, B `0x00788C80`, anderes Gitter und anderer Ebenenindex).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zweige von `CBChargingInventoryAMoveItem` (194 Quellzeilen) wurden nur nach Verzweigungswerten und Aufrufzahl geprüft.
- Die Gleichheit der A/B-Kopien beruht auf dem Textvergleich der Quelle und dem gemeinsamen Binary-Rumpf, nicht auf einem Bytevergleich der beiden zusammengefalteten Aufrufstellen.

## Querverweise

- **Erwähnt Module:** [`AgcmItem`](AgcmItem.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgpmItem`](AgpmItem.md)
- **Erwähnt in:** [`AgcmUIBank`](AgcmUIBank.md), [`AgcmUIItem`](AgcmUIItem.md)
