# AgcmItemConvert (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmItemConvert` (Gegenstandsumwandlung: physisch, Sockel, Rune) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmItemConvert/AgcmItemConvert.cpp`. Das Paketformat steht im Bericht zu [`AgpmItemConvert`](AgpmItemConvert.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle 16 Quellmethoden zugeordnet: 13 mit eigener Adresse, die drei Ergebnis-Rückrufe über einen gemeinsamen Rumpf (Aliase).
- **Reihenfolge:** Die Funktionen liegen im Binary in Quellreihenfolge (`0x006EA910`–`0x006EAD20`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmItemConvert.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006EADF0` | 111 | vtable/String |
| 1 | `SendRequestPhysicalConvert` | `0x006EA910` | 115 | von Hand geprüft |
| 2 | `SendRequestSocketAdd` | `0x006EA990` | 110 | von Hand geprüft |
| 3 | `SendRequestRuneConvert` | `0x006EAA00` | 115 | von Hand geprüft |
| 4 | `SendCheckCashRuneConvert` | `0x006EAA80` | 115 | von Hand geprüft |
| 5 | `SendSocketInitialize` | `0x006EAB00` | 115 | von Hand geprüft |
| 6 | `IsPhysicalConvertable` | `0x006EAB80` | 71 | von Hand geprüft |
| 7 | `IsSocketConvertable` | `0x006EABD0` | 38 | von Hand geprüft |
| 8 | `IsRuneConvertable` | `0x006EAC00` | 114 | von Hand geprüft |
| 9 | `PhysicalConvert` | `0x006EAC80` | 79 | von Hand geprüft |
| 10 | `SocketConvert` | `0x006EACD0` | 69 | von Hand geprüft |
| 11 | `RuneConvert` | `0x006EAD20` | 85 | von Hand geprüft |
| 12 | `CBResultPhysicalConvert` | `0x006EAD80` | 23 | gleiche Adresse wie `gemeinsamer Rumpf (pClass && pCustData)` (vom Linker zusammengefaltet) |
| 13 | `CBResultSocketConvert` | `0x006EAD80` | 23 | gleiche Adresse wie `gemeinsamer Rumpf` (vom Linker zusammengefaltet) |
| 14 | `CBResultSpiritStoneConvert` | `0x006EADA0` | 30 | Callback-Registrierung |
| 15 | `CBResultRuneConvert` | `0x006EAD80` | 23 | gleiche Adresse wie `gemeinsamer Rumpf` (vom Linker zusammengefaltet) |

16 von 16 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006EA8C0`), `~AgcmItemConvert` (`0x006EADC0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger auf `AgpmItemConvert`` | `OnAddModule` |

## OnAddModule (0x006EADF0)

Holt `AgpmItemConvert` in `this+0xB98` und meldet vier Rückrufe an (Physical, Socket, Spirit-Stone-über-Socket-ID, Rune), wie in der Quelle. Drei davon (`CBResultPhysicalConvert`, `CBResultSocketConvert`, `CBResultRuneConvert`) zeigen auf denselben Rumpf `0x006EAD80` (prüft `pClass` und `pCustData`, liefert sonst `FALSE`); nur `CBResultSpiritStoneConvert` (`0x006EADA0`) hat einen eigenen Rumpf, weil er zusätzlich `pData` prüft.

## Senden

Die fünf Sendefunktionen (`0x006EA910`, `0x006EA990`, `0x006EAA00`, `0x006EAA80`, `0x006EAB00`) haben dieselbe Form: Paket über `AgpmItemConvert::MakePacket…` bauen (`0x00594390`, `0x005943F0`, `0x00594450`, `0x00594510`, `0x00594570`), bei Länge < 1 `FALSE`, sonst `SendPacket` und Paket freigeben. Reihenfolge und Paketbauer entsprechen der Quellreihenfolge Physical, SocketAdd, Rune, CheckCashRune, SocketInitialize.

## Prüfen und Konvertieren

`IsPhysicalConvertable` (`0x006EAB80`) prüft Gegenstand und Katalysator, `IsSocketConvertable` (`0x006EABD0`) nur den Gegenstand, `IsRuneConvertable` (`0x006EAC00`) vier Teilprüfungen. `PhysicalConvert`, `SocketConvert` und `RuneConvert` (`0x006EAC80`, `0x006EACD0`, `0x006EAD20`) rufen die zugehörige Prüfung und bei Erfolg die Sendefunktion.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die drei zusammengefalteten Rückrufe lassen sich nur über die Registrierungsreihenfolge in `OnAddModule` den Quellnamen zuordnen; ihr Rumpf ist identisch.
- Die Prüffunktionen sind über Aufrufer und Quellreihenfolge zugeordnet, die Teilprüfungen in `AgpmItemConvert` wurden nicht Zeile für Zeile verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmItemConvert`](AgpmItemConvert.md)
