# AgcmWarInfo (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmWarInfo` (Kriegsinformation: Zustand, Zeit, Zähler, Anmeldungen bei [`AgpmWarInfo`](AgpmWarInfo.md)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmWarInfo/AgcmWarInfo.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; alle Methoden bis auf das eingebaute `UpdatePvPInfo` sind zugeordnet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmWarInfo.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 1 | `OnAddModule` | `0x0068B250` | 175 | vtable/String |
| 2 | `OnIdle` | `0x0068A860` | 79 | vtable/String |
| 3 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 4 | `CBOperationUpdateWarState` | `0x0068B0E0` | 223 | Callback-Registrierung |
| 5 | `CBOperationUpdateTimeStep` | `0x0068A8B0` | 91 | Callback-Registrierung |
| 6 | `CBOperationUpdateAddInfo` | `0x0068B1C0` | 140 | Callback-Registrierung |
| 7 | `CBOperationUpdateCharacterPvPInfo` | `0x0068AA20` | 108 | Callback-Registrierung |
| 8 | `CBOperationUpdateRacePvPInfo` | `0x0068AA90` | 104 | Callback-Registrierung |
| 9 | `CBOperationEndWar` | `0x0068AB00` | 56 | Callback-Registrierung |
| 10 | `CBOperationUpdateFactor` | `0x0068A910` | 72 | Callback-Registrierung |
| 11 | `EndWar` | `0x0068A960` | 116 | von Hand geprüft |
| 12 | `StartWar` | `0x0068A9E0` | 62 | von Hand geprüft |
| 13 | `UpdatePvPInfo` | – | | in die Rückrufe eingebaut (Aufruf von `SetPvPInfo`) |

13 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmWarInfo` (`0x0068AE50`), `AgcmWarInfo` (`0x0068AFB0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xC60…0xC64` | `Kriegstyp, Schritt, Meldungsschritt, Zusatzflag, Restzeit (je 1 Byte)` | `StartWar`, `EndWar` |
| `this+0xC68` | `Endzeit` | `EndWar` |
| `this+0xC6C` | `Kriegsende-Merker` | `StartWar`, `EndWar` |
| `this+0xC70…0xC7C` | `Siege/Niederlagen Charakter, Siege/Niederlagen Rasse` | `CBOperationUpdateCharacterPvPInfo` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmWarInfo` (`0x0068B0C0`, Löschwrapper), 1 `OnAddModule` (`0x0068B250`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`), 3 `OnIdle` (`0x0068A860`), 4 und 5 `0x0067FAB0`, 6 und 7 `0x0067AC90` (`OnDestroy` = `return TRUE`). Der Konstruktor (`0x0068AFB0`) legt zwei Felder zu je vier `std::map`-Einträgen an (`this+0xBA0…`, je 24 Byte; das sind `m_mapWarInfoData` und `m_mapWarAddMessageData`), trägt `AgcmWarInfo` als Modulnamen ein und nullt die Zustandsfelder. Der Destruktorrumpf (`0x0068AE50`) zerstört beide Felder rückwärts.

## Zustand und Kriegsende

Die Zustandsfelder liegen bei `this+0xC60…0xC7C`: `+0xC60` Kriegstyp, `+0xC61` Schritt, `+0xC62` Meldungsschritt, `+0xC63` Zusatzflag, `+0xC64` Restzeit, `+0xC68` Endzeit, `+0xC6C` Kriegsende-Merker, `+0xC70/0xC74` Siege/Niederlagen des Charakters, `+0xC78/0xC7C` der Rasse (Reihenfolge wie `SetPvPInfo` sie liest). `StartWar` (`0x0068A9E0`, 62 Byte) setzt Restzeit, Schritt, Meldungsschritt, Zusatzflag, Kriegsende-Merker und die vier Zähler auf 0 (nicht den Kriegstyp, wie in der Quelle). `EndWar` (`0x0068A960`) kehrt bei gesetztem Merker sofort zurück, setzt den Merker, nullt alle Felder, merkt sich die aktuelle Zeit (`0x00877C10`) und ruft `AgcmUIWarInfo::UpdateTimeStep(0)` (`0x0068B970`). `CBOperationEndWar` (`0x0068AB00`) ruft `EndWar`; beide Funktionen werden außerdem von einem fremden Modul bei `0x0067FC70` gerufen. `UpdatePvPInfo` ist in die Rückrufe eingebaut (sie rufen `SetPvPInfo` direkt, `0x0068B740`).

## Rückrufe

`OnAddModule` (`0x0068B250`) holt `AgpmWarInfo` und [`AgcmUIWarInfo`](AgcmUIWarInfo.md) und meldet sieben Rückrufe an: `CBOperationUpdateWarState` (`0x0068B0E0`), `…UpdateTimeStep` (`0x0068A8B0`), `…UpdateAddInfo` (`0x0068B1C0`), `…UpdateCharacterPvPInfo` (`0x0068AA20`), `…UpdateRacePvPInfo` (`0x0068AA90`), `…EndWar` (`0x0068AB00`), `…UpdateFactor` (`0x0068A910`). `CBOperationUpdateCharacterPvPInfo` ist gegen die Quelle gelesen: Prüfung auf Null, Auslassen bei offenem Fenster, wenn der letzte Kriegstyp den Wert 2 und der Paketkriegstyp den Wert 1 hat (laut Quelle `ShrineBattle` bzw. `BattleGround`; die Enum-Werte sind nicht gegen die Header geprüft), dann Siege/Niederlagen übernehmen und `SetPvPInfo` rufen.

## Karten-Hilfsfunktionen

`0x0068AB40` (rekursives Löschen der Knoten, Knotengröße `0x74`, zerstört drei Zeichenketten pro Knoten), `0x0068AE20` (`clear` der Karte), `0x0068ABD0` (Einfügen mit Hinweis in den Rot-Schwarz-Baum) und `0x0068AED0` (Suchen oder Einfügen, `operator[]`) sind STL-Vorlagenfunktionen der Mitglieder `m_mapWarInfoData` und `m_mapWarAddMessageData`; sie haben keine Quellmethode.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Feldnamen und die Bedeutung der einzelnen Bytes ab `this+0xC60` sind aus der Konstruktor-/`StartWar`-Reihenfolge der Quelle gefolgert, nicht aus einem Klassenlayout belegt.
- `StartWar` und `EndWar` sind über die Feldzuweisungen (Quelle ↔ Dekompilat), den Aufruf von `UpdateTimeStep(0)` und den Aufrufer `CBOperationEndWar` zugeordnet.
- Die sechs übrigen Rückrufe waren bereits über die Callback-Registrierung benannt; nur `CBOperationUpdateCharacterPvPInfo` wurde hier zusätzlich gegen die Quelle gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 2, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIWarInfo`](AgcmUIWarInfo.md), [`AgpmWarInfo`](AgpmWarInfo.md)
- **Erwähnt in:** [`AgcmUIWarInfo`](AgcmUIWarInfo.md)
