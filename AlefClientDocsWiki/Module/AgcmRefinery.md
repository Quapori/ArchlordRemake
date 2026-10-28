# AgcmRefinery (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmRefinery` (Veredelung von Gegenständen: Paket an den Server) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmRefinery/AgcmRefinery.cpp` und `AgpmRefinery.h`/`ApDefine.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: beide Quellmethoden (`OnAddModule`, `SendPacketRefineItem`) sind zugeordnet; das Modul hat keinen Empfangscode, die Antworten (`REFINE_ITEM_RESULT`) behandelt [`AgpmRefinery`](AgpmRefinery.md).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmRefinery.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E7870` | 30 | vtable/String |
| 1 | `SendPacketRefineItem` | `0x006E7890` | 149 | von Hand geprüft |

2 von 2 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006E77D0`), `~AgcmRefinery` (`0x006E7930`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger `AgpmRefinery`` | `OnAddModule`, `SendPacketRefineItem` |
| `AgpmRefinery+0xC4C` | `Paketobjekt `m_csPacket`` | `SendPacketRefineItem` |

## Vtable und Aufbau

Konstruktor `0x006E77D0` (Basis [`AgcModule`](AgcModule.md), trägt `AgcmRefinery` als Modulnamen ein, Modultyp 2 = Client, Idle aus, Zeiger `m_pAgpmRefinery` bei `this+0xB98` = 0), Destruktor `0x006E7930` (Löschwrapper). `OnAddModule` (`0x006E7870`, 30 Byte) holt `AgpmRefinery` und liefert FALSE, wenn es fehlt.

## Paket

`SendPacketRefineItem` (`0x006E7890`, 149 Byte, vorher unbenannt) baut mit dem Paketobjekt des `AgpmRefinery` (`m_pAgpmRefinery + 0xC4C` = `m_csPacket`) ein Paket vom Typ `0x4B` (`AGPMREFINERY_PACKET_TYPE`) mit Operation 2 (`AGPMREFINERY_PACKET_OPERATION_REFINE_ITEM`), Charakter-ID, Kennung und dem Zeiger auf die Quell-Gegenstände. Bei erfolgreichem Paket (Länge > 0) wird es gesendet (`0x004E45A0`) und freigegeben. Einziger Aufrufer im Binary ist `0x006A0BC0`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Feldfolge im Paket (Operation, Charakter-ID, Kennung, Quell-Gegenstände, dann zwei leere Felder) wurde nur aus den Aufrufargumenten gelesen, nicht gegen einen Mitschnitt geprüft.
- Dass der Aufrufer `0x006A0BC0` zur Veredelungs-Oberfläche gehört, ist nicht geprüft.

## Querverweise

- **Erwähnt Module:** [`AgcModule`](AgcModule.md), [`AgpmRefinery`](AgpmRefinery.md)
- **Erwähnt in:** [`AgcmUIRefinery`](AgcmUIRefinery.md)
