# AgpmEventItemRepair (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventItemRepair` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventItemRepair` / `AgpmEventItemRepair.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00575AC0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMEVENT_ITEMREPAIR_OPERATION_*` kennt 5 Operationen, davon 5 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 5 Operationen liegen 2013er Ereignisse vor; 5 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`00575470`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00575470` | `AgpmEventItemRepair::ctor_or_dtor_00575470` | merged |
| `0x00575570` | `AgpmEventItemRepair::ctor_or_dtor_00575570` | merged |
| `0x00575890` | `AgpmEventItemRepair::CBActionItemRepair` | stage1 |
| `0x00575990` | `AgpmEventItemRepair::~AgpmEventItemRepair` | merged |
| `0x005759B0` | `AgpmEventItemRepair::CBEmbeddedMakeEventPacket` | stage1 |
| `0x00575A10` | `AgpmEventItemRepair::OnAddModule` | merged |
| `0x00575AC0` | `AgpmEventItemRepair::OnReceive` | merged |
| `0x005757A0` | `AgpmEventItemRepair::OnOperationEventReq` | casemap:AgpmEventItemRepair |

8 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 6/6/6 | ja | ja |
| `m_csPacketEventData` | 1/1/1 | 1/1/1 | ja | ja |

**m_csPacket** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | PACKET | 1 | Event Base Packet |
| 2 | `0x4` | INT32 | 1 | Character id |
| 3 | `0x8` | INT32 | ITEM_REPAIR_GRID_MAX | repair item IDs |
| 4 | `0x10` | INT64 | 1 | repair cost |
| 5 | `0x20` | INT32 | 1 | Result Code |

**m_csPacketEventData** (1 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Quest Group ID |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `REPAIR_REQ` | inline | `REPAIR_REQ` | = (2013 = 2017) |
| 1 | `REPAIR_ACK` | inline | `REPAIR_ACK` | = (2013 = 2017) |
| 2 | `REPAIR_RESULT` | inline | `REPAIR_RESULT` | = (2013 = 2017) |
| 3 | `EVENT_REQ` | `0x005757A0` `OnOperationEventReq` | `EVENT_REQ` | = (2013 = 2017) |
| 4 | `GRANT` | inline | `GRANT` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 7, nicht im Client: 1, ohne Kandidat: 2, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketEventRequest` | 21 | `0x00575190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketItemRepair` | 23 | `0x005755E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetItemRepairPrice` | 41 | `0x00575670` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventItemRepair`](AgcmEventItemRepair.md), [`AgcmUIEventItemRepair`](AgcmUIEventItemRepair.md)
