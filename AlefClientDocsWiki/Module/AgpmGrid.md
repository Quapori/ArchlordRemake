# AgpmGrid (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmGrid` (Raster für Inventar, Bank, Handel u. a.) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`; die meisten Funktionen liegen in Export-Lücken), Aufrufgraph, Scan aller direkten Aufrufstellen (`call`/`jmp`) im Bereich, EP8-Quelle `Modules/APublic/AgpmGrid/AgpmGrid.cpp`/`AgpdGrid.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 32 von 49 Quellmethoden sind zugeordnet. Nicht gefunden sind u. a. `IsFullGrid`, `GetCountByTemplate`, `CheckEnoughItem`, `LockItem`/`ReleaseItem`/`IsLocked`, `Update` (beide Fassungen), `IsExistItemTemplate`, `GetQuestItemByTemplate`, `AttachGridItemTextureData`, `GetLayer`/`GetRow`/`GetColumn`: im ganzen Bereich ist keine Aufrufstelle für sie vorhanden. Ob sie eingebaut oder an anderer Stelle sind, ist offen.
- **Nicht im Client:** `InitGridMemoryPool` (nur Server), `IsMovalbeGrid` (in der Quelle ohne Aufrufer).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmGrid.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | `0x00587640` | 435 | von Hand geprüft |
| 1 | `Init` | `0x005864D0` | 191 | von Hand geprüft |
| 2 | `CreateByMemoryPool` | `0x00586590` | 216 | von Hand geprüft |
| 3 | `DeleteByMemoryPool` | `0x00586670` | 131 | von Hand geprüft |
| 4 | `InitGridMemoryPool` | – | | nicht im Client-Binary: Aufrufer nur im Server (`ServerEngine.cpp`) |
| 5 | `GetLayer` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 6 | `GetRow` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 7 | `GetColumn` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 8 | `GetLayerByIndex` | `0x00586700` | 39 | von Hand geprüft |
| 9 | `GetRowByIndex` | `0x00586730` | 64 | von Hand geprüft |
| 10 | `GetColumnByIndex` | `0x00586770` | 67 | von Hand geprüft |
| 11 | `GetItemCount` | `0x005867C0` | 10 | von Hand geprüft |
| 12 | `GetItem` | `0x00587830` | 155 | von Hand geprüft |
| 13 | `GetItem` | `0x005867D0` | 32 | von Hand geprüft |
| 14 | `Remove` | `0x005867F0` | 345 | von Hand geprüft |
| 15 | `IsExistItem` | `0x00586980` | 92 | von Hand geprüft |
| 16 | `IsExistItemTemplate` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 17 | `GetItemByTemplate` | `0x005869E0` | 65 | von Hand geprüft |
| 18 | `GetQuestItemByTemplate` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 19 | `GetItemByTemplate` | `0x00586A30` | 84 | von Hand geprüft |
| 20 | `AddItem` | `0x00586A90` | 16 | von Hand geprüft |
| 21 | `DeleteItem` | `0x00586AA0` | 16 | von Hand geprüft |
| 22 | `IsInGrid` | `0x00586AB0` | 128 | von Hand geprüft |
| 23 | `GetEmptyGrid` | `0x005878D0` | 44 | von Hand geprüft |
| 24 | `GetEmptyGridWithStartPos` | `0x00586B30` | 493 | von Hand geprüft |
| 25 | `IsEmptyGrid` | `0x00586D30` | 203 | von Hand geprüft |
| 26 | `GetEmpyGridCount` | `0x00586E00` | 13 | von Hand geprüft |
| 27 | `IsMovalbeGrid` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 28 | `Add` | `0x00586E10` | 231 | von Hand geprüft |
| 29 | `Add` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) (Fassung mit Startpunkt) |
| 30 | `Add` | `0x00586F00` | 330 | von Hand geprüft |
| 31 | `AddToLayer` | `0x00587050` | 201 | von Hand geprüft |
| 32 | `RemoveItem` | `0x00587900` | 121 | von Hand geprüft |
| 33 | `RemoveItemAndFillFirst` | `0x00587980` | 190 | von Hand geprüft |
| 34 | `Clear` | `0x00587120` | 239 | von Hand geprüft |
| 35 | `GetItemSequence` | `0x00587210` | 59 | von Hand geprüft |
| 36 | `Reset` | `0x00587250` | 78 | von Hand geprüft |
| 37 | `AttachGridItemTextureData` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 38 | `CreateGridItem` | `0x00587A40` | 126 | von Hand geprüft |
| 39 | `DeleteGridItem` | `0x005872A0` | 22 | von Hand geprüft |
| 40 | `IsLocked` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 41 | `LockItem` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 42 | `ReleaseItem` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 43 | `UpdateMaxRowExistItem` | `0x005872C0` | 103 | von Hand geprüft |
| 44 | `Update` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 45 | `Update` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 46 | `IsFullGrid` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 47 | `CheckEnoughItem` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |
| 48 | `GetCountByTemplate` | – | | kein direkter Aufruf im Bereich `0x00585FD0`–`0x00587A40` gefunden; Verbleib offen (vermutlich eingebaut) |

32 von 49 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmGrid` (`0x00585FD0`), `~AgpmGrid_body` (`0x005862E0`), `Init_size` (`0x005864D0`), `GetItem_index` (`0x005867D0`), `GetItemByTemplate_index` (`0x00586A30`), `Add_pos` (`0x00586F00`), `~AgpmGrid` (`0x00587620`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Raster+0x04` | `Anzahl Gegenstände (`m_lItemCount`)` | `AddItem`, `DeleteItem`, `GetItemCount`, `GetEmpyGridCount` |
| `Raster+0x08` | `Anzahl Felder (`m_lGridCount`)` | `GetItem`, `GetItemSequence` |
| `Raster+0x0C / 0x10` | `Feldtabelle / Sperrtabelle` | `Reset`, `Clear`, `RemoveItem` |
| `Raster+0x14 / 0x16 / 0x18` | `Ebenen / Zeilen / Spalten (je 16 Bit)` | `IsInGrid`, `GetItem`, Index-Funktionen |
| `Raster+0x1A` | `höchste belegte Zeile (`m_nMaxRowExistItem`)` | `Reset`, `UpdateMaxRowExistItem` |

## Vtable und Aufbau

`AgpmGrid` (Raster aus Ebenen, Zeilen und Spalten für Inventar, Bank, Handel, Ausrüstung, Quest u. a.) liegt im Binary bei `0x00585FD0`–`0x00587A40`. Vtable `0x008B95FC`: Slot 0 Löschwrapper (`0x00587620`, Rumpf `0x005862E0`), Slots 1 und 2 der gemeinsame Rumpf `0x0067AC90`. Der Konstruktor (`0x00585FD0`, 779 Byte) ruft den `ApModule`-Konstruktor, baut die Pool-Member der Rastertypen auf und legt den Datenblock für Rasterfelder an (`SetModuleData`).
Das Raster (`AgpdGrid`) hat im Binary diese Felder: Anzahl Gegenstände `+4`, Anzahl Felder `+8`, Feldtabelle `+0xC`, Sperrtabelle `+0x10`, Ebenen `+0x14`, Zeilen `+0x16`, Spalten `+0x18` (je 16 Bit), höchste belegte Zeile `+0x1A`. Der Feldindex ist `(Ebene · Zeilen + Zeile) · Spalten + Spalte`.

## Anlegen und Löschen

`Init(Typ)` (`0x00587640`, 435 Byte) wählt über den Rastertyp die Größen (Bank, Inventar, Ausrüstung, Handel, Verkauf, NPC-Handel, Quest, Cash-Inventar, Gildenlager, Zusatzinventar, Aufladeinventar) und ruft `CreateByMemoryPool` (`0x00586590`, fünf Aufrufstellen im Rumpf); `Remove` (`0x005867F0`, 345 Byte) räumt je nach Typ über `DeleteByMemoryPool` (`0x00586670`) auf. `Init(Ebene, Zeile, Spalte)` (`0x005864D0`, 191 Byte, 48 Aufrufstellen) legt ein Raster ohne Pool an. `InitGridMemoryPool` (die Pools füllen) ruft in der Quelle nur der Server auf (`ServerEngine.cpp`).

## Abfragen und Ändern

`IsInGrid` (`0x00586AB0`) prüft Grenzen einer Fläche; `GetItem` (`0x00587830`, mit Ebene, Zeile, Spalte) und `GetItem(Index)` (`0x005867D0`) liefern ein Feld; `GetLayerByIndex`/`GetRowByIndex`/`GetColumnByIndex` (`0x00586700`, `0x00586730`, `0x00586770`) rechnen den Index zurück; `GetItemSequence` (`0x00587210`) liefert den nächsten belegten Eintrag; `GetEmpyGridCount` (`0x00586E00`) ist `Felder − Gegenstände`. `IsExistItem` (`0x00586980`) und `GetItemByTemplate` (`0x005869E0`; Fassung mit Startindex `0x00586A30`) suchen nach Typ und Vorlagenkennung; `IsEmptyGrid` (`0x00586D30`, 203 Byte) prüft, ob eine Fläche frei ist.
`GetEmptyGridWithStartPos` (`0x00586B30`, 493 Byte) und `GetEmptyGrid` (`0x005878D0`, Aufruf mit Startpunkt 0) suchen den ersten freien Platz; `Add(Raster, Gegenstand, Höhe, Breite)` (`0x00586E10`) sucht einen Platz und trägt ein, `Add(…, Ebene, Zeile, Spalte, …)` (`0x00586F00`, 330 Byte) trägt an einer Position ein, `AddToLayer` (`0x00587050`) sucht in einer Ebene. `Clear` (`0x00587120`) leert eine Fläche, `RemoveItem` (`0x00587900`) und `RemoveItemAndFillFirst` (`0x00587980`) entfernen einen Gegenstand und rufen `UpdateMaxRowExistItem` (`0x005872C0`); `Reset` (`0x00587250`) leert das ganze Raster. `AddItem`/`DeleteItem` (`0x00586A90`/`0x00586AA0`) zählen den Gegenstandszähler hoch bzw. herunter.
`CreateGridItem` (`0x00587A40`, 126 Byte, 26 Aufrufstellen) legt ein `AgpdGridItem` über den Modul-Datenblock an und `DeleteGridItem` (`0x005872A0`) gibt es frei.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Disassembly oder Dekompilat) sind `IsInGrid`, `GetItem`, `GetItem(Index)`, `GetItemSequence`, `GetEmpyGridCount`, `AddItem`, `DeleteItem`, die drei Index-Funktionen, `IsExistItem`, beide `GetItemByTemplate`, `Clear`, `Reset`, `RemoveItem`, `UpdateMaxRowExistItem`, `CreateGridItem` und `Init(Ebene, Zeile, Spalte)`; `Init(Typ)`, `Remove`, `CreateByMemoryPool`, `DeleteByMemoryPool`, `GetEmptyGrid*`, `IsEmptyGrid`, `Add*` und `AddToLayer` sind über Aufrufbeziehungen, Argumentzahl und Größe zugeordnet, nicht Zeile für Zeile verglichen.
- Die 17 nicht gefundenen Methoden: Aufrufstellen wurden nur als direkte `call`/`jmp`-Befehle im Bereich gesucht; Aufrufe über Zeiger oder aus anderen Modulen, die dieselbe Funktion unter anderer Adresse eingebaut haben, würden so nicht erfasst. Bei `IsFullGrid`, `GetCountByTemplate` und `CheckEnoughItem` sind in der Quelle viele Aufrufer vorhanden; ihr Fehlen als eigene Funktion ist deshalb am ehesten Einbau.
- Die Rastertypen (`AGPDGRID_TYPE_…`) und ihre Größen wurden nicht einzeln gegen den Binary-Rumpf von `Init(Typ)` abgeglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 4, nicht im Client: 4, ohne Kandidat: 7, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetCountByTemplate` | 24 | `0x00587530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetItem` (`0x00587480`), `Add` (`0x005873E0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmBillInfo`](AgcmBillInfo.md), [`AgcmItem`](AgcmItem.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmSocialActon`](AgcmSocialActon.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUISocialAction`](AgcmUISocialAction.md), [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md), [`AgpmEventNPCTrade`](AgpmEventNPCTrade.md)
