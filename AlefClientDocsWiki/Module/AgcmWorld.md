# AgcmWorld (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmWorld` (Weltliste im Login: Zeichenanzahl je Welt, Weltgruppen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmWorld/AgcmWorld.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle elf Methoden sind zugeordnet. `DesAgcdWorld` liegt mit `ConAgcdWorld` an derselben Adresse (beide setzen nur die Zeichenanzahl des Datenblocks auf 0).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmWorld.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DAA00` | 107 | vtable/String |
| 1 | `ConAgcdWorld` | `0x006DA640` | 55 | von Hand geprüft |
| 2 | `DesAgcdWorld` | `0x006DA640` | 55 | gleiche Adresse wie `verschmolzen mit `ConAgcdWorld` (ICF)` (vom Linker zusammengefaltet) |
| 3 | `GetAD` | `0x006DA400` | 36 | von Hand geprüft |
| 4 | `SendPacketGetWorld` | `0x006DA430` | 132 | von Hand geprüft |
| 5 | `SendPacketGetCharCount` | `0x006DA4C0` | 120 | von Hand geprüft |
| 6 | `CBGetWorldAll` | `0x006DA680` | 65 | Callback-Registrierung |
| 7 | `CBGetCharCount` | `0x006DA6D0` | 84 | Callback-Registrierung |
| 8 | `SetCallbackGetCharCount` | `0x006DA540` | 20 | von Hand geprüft |
| 9 | `ResetWorldGroup` | `0x006DC2C0` | 464 | von Hand geprüft |
| 10 | `_DecodeWorldCharCount` | `0x006DA560` | 208 | von Hand geprüft |

11 von 11 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmWorld` (`0x006DC0C0`), `~AgcmWorld` (`0x006DC1A0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB9C` | `Zeiger [`AgpmWorld`](AgpmWorld.md)` | `OnAddModule` |
| `this+0xBA0` | `Index des angehängten Moduldatenblocks (16 Bit)` | `OnAddModule` |
| `this+0xBA2` | `Zeichenanzahl-Zeichenkette `m_szWorldCharCount` (2048 Byte)` | `CBGetCharCount` |
| `this+0x13A4` | ``m_bReceiveWorld`` | `CBGetWorldAll` |
| `this+0x13A8` | `Vektor `m_vecWorldGroup` (Element 44 Byte)` | `ResetWorldGroup` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmWorld` (`0x006DC2A0`, Löschwrapper), 1 `OnAddModule` (`0x006DAA00`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`), 3 bis 5 `0x0067FAB0`, 6 und 7 `0x0067AC90`. Der Konstruktor (`0x006DC0C0`) trägt den Modulnamen `AgcmWorld` ein, der Destruktorrumpf (`0x006DC1A0`) zerstört den Vektor `m_vecWorldGroup` (bei `this+0x13A8`).

## OnAddModule (0x006DAA00)

Holt `AgpmWorld` (Zeiger bei `this+0xB9C`), hängt über `SetAttachedModuleData` einen Datenblock von 4 Byte an (Index bei `this+0xBA0`, Konstruktor/Destruktor beide `0x006DA640`) und meldet `CBGetWorldAll` (`0x006DA680`) und `CBGetCharCount` (`0x006DA6D0`) an – Reihenfolge wie in der Quelle. `ConAgcdWorld` und `DesAgcdWorld` setzen beide die Zeichenanzahl des angehängten Blocks auf 0 und sind vom Linker zu `0x006DA640` verschmolzen (ICF); `GetAD` ist darin eingebaut (`0x004E40B0`).

## Weltliste und Zeichenanzahl

`CBGetWorldAll` setzt `m_bReceiveWorld` (`this+0x13A4`) und ruft `_DecodeWorldCharCount` (`0x006DA560`, 208 Byte), wenn die Zeichenanzahl-Zeichenkette (`this+0xBA2`, 2048 Byte) bereits angekommen ist. `CBGetCharCount` kopiert die empfangene Zeichenkette (höchstens `0x800` Byte) und decodiert sofort, wenn die Weltliste schon da ist. `_DecodeWorldCharCount` sucht je Eintrag die Welt (`0x0058CF60`), schreibt die Anzahl in den angehängten Block und löst am Ende den Rückruf 0 aus (`0x004E4040`); `SetCallbackGetCharCount` (`0x006DA540`) meldet ihn an (Rückruf-Kennung 0).
`ResetWorldGroup` (`0x006DC2C0`, 464 Byte) leert die Gruppen, läuft über 30 Welten (`0x1E` = `s_dwWorldMax`), ordnet jede ihrer Gruppe zu oder legt eine neue an und sortiert die Gruppen absteigend.

## Pakete senden

`SendPacketGetWorld` (`0x006DA430`, 132 Byte) baut mit dem Paketerzeuger von `AgpmWorld` (`this+0xB9C`, Paketobjekt bei `+0xB84`, Pakettyp `0x18`) ein Paket aus Operation (0), Weltname und Status (0) und sendet es mit Sendeart 2 (laut Quelle `ACDP_SEND_LOGINSERVER`) an die übergebene NID; `SendPacketGetCharCount` (`0x006DA4C0`, 120 Byte) baut dasselbe Paket mit dem Konto statt Weltname und ohne Status. Beide geben das Paket frei und liefern TRUE bei Erfolg. Aufrufer sind `AgcmUIAccountCheck`/`AgcmUIServerSelect` (z. B. `0x00742FB0`). `GetAD` (`0x006DA400`) liefert den angehängten Datenblock des übergebenen Objekts (`GetAttachedModuleData`, Index aus `this+0xBA0`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `ResetWorldGroup` ist über die Schleife bis 30, den Aufruf von `GetWorld(i)` (`0x0056D960`) und die Hilfsfunktionen der Gruppen-Vektoren (Suchen, Einfügen, Sortieren) zugeordnet; der Rumpf wurde nicht Zeile für Zeile verglichen.
- `SendPacketGetWorld` und `SendPacketGetCharCount` (und `GetAD`) liegen im Adressbereich vor `AgcmWorld::OnAddModule`, zwischen `SetCallbackGetCharCount` und der STL-Gruppe; sie waren zunächst fälschlich als „nicht im Binary“ geführt. Sie sind über die Paketfelder (Weltname mit Status gegenüber Konto ohne Status), die Reihenfolge der Quelle und die Aufrufer im Login-UI zugeordnet; die Welt-Fassung ist die mit dem zusätzlichen Status-Feld.
- Die Offsets stammen aus den genannten Funktionen; Feldnamen der Quelle sind aus der Verwendung gefolgert.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmWorld`](AgpmWorld.md)
- **Erwähnt in:** [`AgcmMap`](AgcmMap.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmWater`](AgcmWater.md)
