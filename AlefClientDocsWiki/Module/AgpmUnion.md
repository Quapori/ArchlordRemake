# AgpmUnion (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmUnion` (Union-Rang aus den Rangpunkten, Rangtabelle) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmUnion/AgpmUnion.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 4 von 10 Quellmethoden sind zugeordnet (`OnAddModule`, `OnInit`, `OnDestroy`, `GetUnionRank`). `GetUnionRankPoint` ist in `GetUnionRank` eingebaut. Nicht im Client-Binary sind `UpdateUnionRankPoint`, `SetUnionRankPoint`, `SetCallbackUpdateUnionRank` und `SetCallbackUpdateUnionRankPoint` (Aufrufer nur im Server: `AgsmUnion`, `AgsmEventUvUReward`) sowie `StreamReadUnionRankTable` (in der Quelle ohne Aufrufer).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmUnion.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00585ED0` | 48 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `SetCallbackUpdateUnionRank` | – | | nicht im Client-Binary: Aufrufer nur im Server (`AgsmUnion`) |
| 4 | `SetCallbackUpdateUnionRankPoint` | – | | nicht im Client-Binary: Aufrufer nur im Server (`AgsmUnion`) |
| 5 | `GetUnionRankPoint` | – | | eingebaut in `GetUnionRank` |
| 6 | `SetUnionRankPoint` | – | | nicht im Client-Binary: nur von `UpdateUnionRankPoint` (Server) gerufen |
| 7 | `GetUnionRank` | `0x00585F30` | 85 | von Hand geprüft |
| 8 | `UpdateUnionRankPoint` | – | | nicht im Client-Binary: Aufrufer nur im Server |
| 9 | `StreamReadUnionRankTable` | – | | nicht im Binary: in der Quelle ohne Aufrufer |

4 von 10 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmUnion` (`0x00585E70`), `scalar_deleting_dtor` (`0x00585F00`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Charakter+0x3F0` | `Faktorblock `m_csFactor` des Charakters (Aufrufargument von `GetValue`)` | `GetUnionRank` |
| `0x009A0C38` | `Rangtabelle (Einträge zu 0x50 Byte; Grenze der Rangpunkte am Eintragsanfang)` | `GetUnionRank` |

## Vtable und Aufbau

Vtable `0x008B95A4`: Slot 0 Löschwrapper (`0x00585F00`), Slot 1 `OnAddModule` (`0x00585ED0`, 48 Byte; holt [`AgpmFactors`](AgpmFactors.md) und [`AgpmCharacter`](AgpmCharacter.md), verlangt nur Letzteres), Slot 2 (`OnInit`) und Slot 7 (`OnDestroy`) am gemeinsamen Rumpf `0x0067AC90` (`return TRUE`), Slot 3 bis 5 `0x0067FAB0`. Konstruktor `0x00585E70` (89 Byte, trägt `AgpmUnion` als Modulnamen ein, nullt die Zeiger auf `AgpmFactors` und `AgpmCharacter`).

## Rang

`GetUnionRank` (`0x00585F30`, 85 Byte) liest den Rangpunkte-Faktor des Charakters (Ergebnis-Faktor, Charakterstatus, Union-Rang, über `AgpmFactors::GetValue` `0x0050BAD0`; `GetUnionRankPoint` ist darin eingebaut) und sucht in der globalen Rangtabelle ab `0x009A0C38` (Einträge zu je 0x50 Byte) den ersten Rang ab 1, dessen Punktegrenze größer als die Rangpunkte ist; höchstens Rang 8 (`AGPMUNION_MAX_UNION_RANK`). Aufrufer sind drei Funktionen im Charakter-Modul (`0x005673A0`, `0x00567630`, `0x00567800`).
Die globale Tabelle `g_csUnionRankTable` (8 Einträge zu 0x50 Byte = 0x280 Byte) wird vermutlich von `AgpdUnionRank::AgpdUnionRank` (`0x00585F90`, `memset` über 0x280 Byte) genullt; die einzige Füllfunktion der Quelle, `StreamReadUnionRankTable`, fehlt im Binary und hat in der Quelle keinen Aufrufer, die Tabelle wird im Client also nicht über sie gefüllt.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Lage der Rangpunkte-Grenze innerhalb eines Tabelleneintrags (hier „am Eintragsanfang“) folgt nur aus dem Vergleich in `GetUnionRank`; die übrigen Felder des 0x50-Byte-Eintrags (Titel, Bonus, Verluste) wurden nicht vermessen.
- `OnInit` und `OnDestroy` sind über Vtable-Slot und Form zugeordnet, nicht über Aufrufer.
- Dass `AgpdUnionRank::AgpdUnionRank` (`0x00585F90`, ohne Aufrufer) der Initialisierer der globalen Tabelle ist, folgt aus dem `memset` von 0x280 Byte; die statische Registrierung wurde nicht verfolgt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 4, nicht als eigene Funktion: 1, nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md)
