# AgcmProduct (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmProduct` (Herstellen von Gegenständen: Paket an den Server) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmProduct/AgcmProduct.cpp` und `AgpmProduct.h`/`ApDefine.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle vier Methoden sind zugeordnet; `OnInit` und `OnDestroy` liegen am gemeinsamen Rumpf `0x0067AC90` (`return TRUE`). Die Antworten des Servers behandelt [`AgpmProduct`](AgpmProduct.md)/[`AgcmProductMed`](AgcmProductMed.md), nicht dieses Modul.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmProduct.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E7A00` | 60 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `SendPacketCompose` | `0x006E7A40` | 148 | von Hand geprüft |

4 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmProduct` (`0x006E7960`), `scalar_deleting_dtor` (`0x006E7AE0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger `AgpmProduct` (dessen `+0xD5C` ist das Paketobjekt)` | `OnAddModule`, `SendPacketCompose` |
| `this+0xB9C` | `Zeiger [`AgpmCharacter`](AgpmCharacter.md)` | `OnAddModule` |

## Vtable und Aufbau

Vtable `0x008D8EE4`: Slot 0 Löschwrapper (`0x006E7AE0`), 1 `OnAddModule` (`0x006E7A00`), 2 `OnInit` (`0x0067AC90`, `return TRUE`), 3 bis 5 `0x0067FAB0`, 6 und 7 `0x0067AC90` (Slot 7 ist `OnDestroy`), 8 `0x004E3420`. Der Konstruktor (`0x006E7960`) trägt `AgcmProduct` als Modulnamen ein, setzt Modultyp Client, schaltet Idle aus und nullt die beiden Modulzeiger.
`OnAddModule` (`0x006E7A00`, 60 Byte) holt `AgpmProduct` (`this+0xB98`) und `AgpmCharacter` (`this+0xB9C`) und liefert FALSE, wenn eines fehlt.

## Paket

`SendPacketCompose` (`0x006E7A40`, 148 Byte, vorher unbenannt) baut mit dem Paketobjekt von `AgpmProduct` (`+0xD5C`) ein Paket vom Typ `0x17` (`AGPMPRODUCT_PACKET_TYPE`) mit Operation 0 (`COMPOSE`), Charakter-ID, Fertigkeits-ID, Herstellungs-ID und Rezept-ID (vier Argumente auf dem Stapel, dahinter drei leere Felder) und sendet es, wenn die Länge über 0 liegt; das Paket wird danach freigegeben. Aufrufer im Binary sind `0x006A2940` und `0x006A33F0` (Bereich von [`AgcmUIProduct`](AgcmUIProduct.md)).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `OnInit` und `OnDestroy` sind über Vtable-Slot und Form zugeordnet, nicht über Aufrufer.
- Dass die beiden Aufrufer von `SendPacketCompose` zu `AgcmUIProduct` gehören, folgt nur aus ihrer Adresslage (`0x006A29xx`, `0x006A33xx`), nicht aus Namen.
- Die Paketfelder sind aus den Aufrufargumenten gelesen, nicht gegen einen Mitschnitt geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmProductMed`](AgcmProductMed.md), [`AgcmUIProduct`](AgcmUIProduct.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmProduct`](AgpmProduct.md)
- **Erwähnt in:** [`AgcmProductMed`](AgcmProductMed.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md)
