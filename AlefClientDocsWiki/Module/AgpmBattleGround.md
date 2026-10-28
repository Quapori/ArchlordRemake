# AgpmBattleGround (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmBattleGround` (Schlachtfeld-Regionen und Angreifbarkeit) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmBattleGround/AgpmBattleGround.cpp`, Konstanten aus `AgpmBattleGround.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 4 von 5 Quellmethoden sind zugeordnet. `SetCallbackSystemMessage` fehlt im Binary: sie ist in der Quelle ein leerer Rumpf (`return TRUE`) ohne Aufrufer.
- **Abweichungen:** keine festgestellt; die zehn Regionsnummern der Quelle stimmen mit den Fallwerten im Binary überein.
- **Hinweis:** `0x00569480` und `0x00569550` liegen im Bereich des Moduls, gehören aber zu [`AgpmEventGacha`](AgpmEventGacha.md) (Paketsender vom Typ `0x57`, Aufrufer [`AgcmEventGacha`](AgcmEventGacha.md):CBEventRequest` und [`AgcmUIEventGacha`](AgcmUIEventGacha.md):CBGachaRoll`).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmBattleGround.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x00569330` | 26 | vtable/String |
| 1 | `SetCallbackSystemMessage` | – | | nicht im Binary: leerer Rumpf in der Quelle, ohne Aufrufer |
| 2 | `IsInBattleGround` | `0x00569400` | 27 | von Hand geprüft |
| 3 | `IsBattleGround` | `0x00569350` | 40 | von Hand geprüft |
| 4 | `IsAttackable` | `0x00569420` | 83 | von Hand geprüft |

4 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmBattleGround` (`0x005692E0`), `scalar_deleting_dtor` (`0x005693D0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Charakter+0x718` | ``m_nBindingRegionIndex` (16 Bit)` | `IsInBattleGround`, `IsAttackable` |

## Vtable und Aufbau

Vtable `0x008B82E8`: Slot 0 Löschwrapper (`0x005693D0`), Slot 1 gemeinsamer Rumpf `0x0067AC90`, Slot 2 `OnInit` (`0x00569330`, 26 Byte; holt [`AgpmCharacter`](AgpmCharacter.md) und liefert TRUE). Konstruktor `0x005692E0` (75 Byte, trägt `AgpmBattleGround` als Modulnamen ein, nullt den Zeiger auf `AgpmCharacter`).

## Abfragen

`IsBattleGround` (`0x00569350`, 40 Byte) liefert TRUE für zehn Regionen: `110` (Zentrum des Chaos), `111`, `112` und `113` (Lager Mensch, Ork, Mondelf), `114` (Schlachtfeld), `123`, `124`, `125` (Felder Ork, Mensch, Mondelf) sowie `175` und `176` (Feld und Lager der Drachenkinder) – genau die Werte `REGIONINDEX_BATTLEGROUND_…` der Quelle. `IsInBattleGround` (`0x00569400`, 27 Byte) prüft, ob der Charakter (`m_nBindingRegionIndex`, `+0x718`) in einer solchen Region ist; Aufrufer sind u. a. [`AgcmIDBoard`](AgcmIDBoard.md):_DrawTitleName`, `_DrawNameEx` und `_DrawGuildCompetition` sowie Oberflächenmodule.
`IsAttackable` (`0x00569420`, 83 Byte) liefert TRUE, wenn beide Charaktere in einem Schlachtfeld sind und nicht dieselbe Rasse haben (`AgpmCharacter::IsSameRace`, `0x005051D0`); einziger Aufrufer ist `0x005808D0`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Namen der Regionen stammen aus `AgpmBattleGround.h`; die Zuordnung der Zahlen zu den Namen wurde mit der Headerdatei abgeglichen, nicht mit der Regionsdatei des Spiels.
- `IsAttackable` wurde über die Aufrufe von `IsSameRace` und `IsBattleGround` zugeordnet.
- `SetCallbackSystemMessage` gilt als nicht im Binary, weil die Quelle sie nirgends aufruft; ein vollständiger Abgleich aller Module nach einem gemeinsamen `return TRUE`-Rumpf mit zwei Parametern wurde nicht gemacht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventGacha`](AgcmEventGacha.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmUIEventGacha`](AgcmUIEventGacha.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventGacha`](AgpmEventGacha.md)
- **Erwähnt in:** [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmMinimap`](AgcmMinimap.md)
