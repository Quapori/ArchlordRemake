# AgcmRide (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmRide` (Reittiere: Aufsteigen, Absteigen, Arcadia-Reittier) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmRide/AgcmRide.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; alle acht Methoden sind zugeordnet (drei davon als gemeinsamer `return TRUE`-Rumpf).
- **Abweichungen:** keine festgestellt; die in der Quelle fest eingetragene Arcadia-TID 1295 steht auch im Binary (`0x50F`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmRide.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E7EF0` | 267 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `CBRideAck` | `0x006E7BA0` | 135 | Callback-Registrierung |
| 4 | `CBRideDismountAck` | `0x006E7C30` | 437 | Callback-Registrierung |
| 5 | `CBRideTimeOut` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 6 | `CBRideTID` | `0x006E7DF0` | 91 | Callback-Registrierung |
| 7 | `CBInitCharacter` | `0x006E7E50` | 99 | Callback-Registrierung |

8 von 8 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmRide` (`0x006E7B10`), `~AgcmRide` (`0x006E7EC0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Charakter+0x790` | `Reitbar-Merkmal (`m_bRidable`)` | `CBRideAck`, `CBRideDismountAck`, `CBInitCharacter` |
| `Charakter+0x794` | `Reiter-ID (`m_nRideCID`), beim Absteigen auf 0` | `CBRideDismountAck` |
| `Charakter+0x740` | `Sonderstatus-Bits (Bit `0x10000000` = Arcadia-Reittier)` | `CBInitCharacter` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmRide` (`0x006E7EC0`), 1 `OnAddModule` (`0x006E7EF0`), 2 `OnInit` (`0x0067AC90`), 3 bis 5 `0x0067FAB0`, 6 und 7 `0x0067AC90` (`OnDestroy` = `return TRUE`), 8 und 9 `0x004E3420`. Der Konstruktor (`0x006E7B10`) trägt den Modulnamen `AgcmRide` ein, schaltet `OnIdle` aus (`EnableIdle(FALSE)`) und setzt `m_pThis` (`DAT_00C23C2C`). `OnAddModule` holt [`AgpmItem`](AgpmItem.md), [`AgcmItem`](AgcmItem.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter` und [`AgpmRide`](AgpmRide.md), meldet die Rückrufe an und ruft `AgcmItem::SetAgcdRide`.

## Rückrufe

`CBRideAck` (`0x006E7BA0`): holt die Charakterdaten (`0x0059E810`), setzt das Reitbar-Merkmal des Charakters (Feld `+0x790`), holt das Item zur Gegenstands-ID und ruft `AttachRide` (`0x00706FB0`) mit dem Untertyp der Item-Vorlage (`+0x90`). `CBRideDismountAck` (`0x006E7C30`, 437 Byte): setzt das Merkmal und die Reiter-ID (`+0x794`) zurück, ruft `DetachRide` (`0x00706E00`), sendet die Inventarinfo des Reittier-Gegenstands (Ausrüstungsplatz `0xE`), legt den Lanzenplatz (`0xF`) ab, setzt die Ausrüstungs-Animationsart und legt die Waffen in beiden Händen (Plätze `10` und `9`) wieder an – in dieser Reihenfolge wie in der Quelle. `CBRideTID` (`0x006E7DF0`) ruft `AttachRide` mit der übergebenen Reit-TID. `CBInitCharacter` (`0x006E7E50`): für fremde Charaktere mit Sonderstatus-Bit `0x10000000` (`RIDE_ARCADIA`) wird das Reit-Merkmal gesetzt und `AttachRide` mit der fest eingetragenen TID `0x50F` (= 1295, Kommentar „Arcadia hardcode“ in der Quelle) gerufen. `CBRideTimeOut` ist in der Quelle leer und mit `return TRUE` (`0x0067AC90`) zusammengefaltet.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `CBRideDismountAck` ist über die Folge der Aufrufe (Ausrüstungsplätze `0xE`, `0xF`, `10`, `9`) mit der Quelle abgeglichen; die Bedeutung der Plätze (Reittier, Lanzer, rechte/linke Hand) folgt der Quelle, die Zahlenwerte der `AGPMITEM_PART_…`-Konstanten sind nicht gegen den Header geprüft.
- Die Feldnamen der Offsets stammen aus der Quelle (`m_bRidable`, `m_nRideCID`), nicht aus einer Layout-Rechnung.
- `CBRideTimeOut` ist nur deshalb dem Rumpf `0x0067AC90` zugeordnet, weil die Quelle einen leeren Rumpf hat.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmItem`](AgcmItem.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md), [`AgpmRide`](AgpmRide.md)
- **Erwähnt in:** [`AgcmItem`](AgcmItem.md)
