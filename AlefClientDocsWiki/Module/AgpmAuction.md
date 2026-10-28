# AgpmAuction (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmAuction` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmAuction` / `AgpmAuction.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0055E670` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMAUCTION_OPERATION_*` kennt 16 Operationen, davon 15 mit eigenem Case im 2017er Binary; ohne Case: `NONE` (0).
- **Vergleich mit 2013:** Für 14 Operationen liegen 2013er Ereignisse vor; 11 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 3 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 9 Paketdefinition(en) in der Quelle, 9 davon im 2017er Konstruktor (`0055d9a0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0055D9A0` | `AgpmAuction::ctor_or_dtor_0055d9a0` | merged |
| `0x0055DCF0` | `AgpmAuction::ctor_or_dtor_0055dcf0` | merged |
| `0x0055DE10` | `AgpmAuction::OnInit` | merged |
| `0x0055DE40` | `AgpmAuction::OnDestroy` | merged |
| `0x0055DF40` | `AgpmAuction::CBEventConstructor` | stage1 |
| `0x0055DF70` | `AgpmAuction::CBEventDestructor` | stage1 |
| `0x0055DFA0` | `AgpmAuction::CBStreamWriteEvent` | stage1 |
| `0x0055E000` | `AgpmAuction::CBStreamReadEvent` | stage1 |
| `0x0055E170` | `AgpmAuction::~AgpmAuction` | merged |
| `0x0055E590` | `AgpmAuction::OnAddModule` | merged |
| `0x0055E670` | `AgpmAuction::OnReceive` | merged |
| `0x0055DEA0` | `AgpmAuction::CreateSales` | casemap:AgpmAuction |
| `0x0055E200` | `AgpmAuction::GetField` | casemap:AgpmAuction |
| `0x0055E2D0` | `AgpmAuction::GetField` | casemap:AgpmAuction |

14 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 4/4/4 | ja | ja |
| `m_csPacketSales` | 2/2/2 | 9/9/9 | ja | ja |
| `m_csPacketSelect` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketSelect2` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csPacketSell` | 1/1/1 | 4/4/4 | ja | ja |
| `m_csPacketCancel` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketConfirm` | 1/1/1 | 4/4/4 | ja | ja |
| `m_csPacketBuy` | 1/1/1 | 4/4/4 | ja | ja |
| `m_csPacketRowset` | 2/2/2 | 8/8/8 | ja | ja |

**m_csPacket** (4 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | cid |
| 2 | `0x4` | PACKET | 1 | embedded packet |
| 3 | `0x8` | INT32 | 1 | result |

**m_csPacketSales** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | sales id |
| 1 | `0x2` | UINT64 | 1 | doc id. |
| 2 | `0x4` | UINT64 | 1 | item seq |
| 3 | `0x8` | INT32 | 1 | item id |
| 4 | `0x10` | INT32 | 1 | price |
| 5 | `0x20` | INT16 | 1 | quantity |
| 6 | `0x40` | INT16 | 1 | status |
| 7 | `0x80` | CHAR | 33 | reg date |
| 8 | `0x100` | INT32 | 1 | item tid |

**m_csPacketSelect** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | item tid |
| 1 | `0x2` | UINT32 | 1 | page |
| 2 | `0x4` | PACKET | 1 | item info.(rowset) |

**m_csPacketSelect2** (5 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | item tid |
| 1 | `0x2` | UINT64 | 1 | doc id.(max, min) |
| 2 | `0x4` | INT16 | 1 | flag(forward, backward) |
| 3 | `0x8` | INT32 | 1 | total no. of sales of Item TID |
| 4 | `0x10` | PACKET | 1 | item info.(rowset) |

**m_csPacketSell** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | item id |
| 1 | `0x2` | INT16 | 1 | quantity |
| 2 | `0x4` | INT32 | 1 | price |
| 3 | `0x8` | CHAR | 33 | date |

**m_csPacketCancel** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | sales id |
| 1 | `0x2` | INT32 | 1 | item tid |
| 2 | `0x4` | INT16 | 1 | quantity remained |

**m_csPacketConfirm** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | sales id |
| 1 | `0x2` | INT32 | 1 | item tid |
| 2 | `0x4` | INT16 | 1 | quantity selled |
| 3 | `0x8` | INT32 | 1 | income |

**m_csPacketBuy** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT64 | 1 | doc id |
| 1 | `0x2` | INT16 | 1 | quantity |
| 2 | `0x4` | INT32 | 1 | item tid |
| 3 | `0x8` | INT32 | 1 | price |

**m_csPacketRowset** (8 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | AUTYPE_INT16,1,// eAgsmRelay2Operation |
| 1 | `0x2` | MEMORY_BLOCK | 1 | Query Index |
| 2 | `0x4` | MEMORY_BLOCK | 1 | Query Text |
| 3 | `0x8` | UINT32 | 1 | Headers |
| 4 | `0x10` | UINT32 | 1 | No. of Rows |
| 5 | `0x20` | UINT32 | 1 | No. of Cols |
| 6 | `0x40` | MEMORY_BLOCK | 1 | Row Buffer Size |
| 7 | `0x80` | MEMORY_BLOCK | 1 | Buffer |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `NONE` | – | – | kein Case (default) – wie 2013 |
| 1 | `ADD_SALES` | `0x0055DEA0` `CreateSales` | – | 2017 ⊂ 2013 |
| 2 | `REMOVE_SALES` | `0x0055E2D0` `GetField` | `REMOVE_SALES` | = (2013 = 2017) |
| 3 | `UPDATE_SALES` | `0x0055E200` `GetField` | `UPDATE_SALES` | = (2013 = 2017) |
| 4 | `SELECT` | inline | `OPEN_AUCTION` | 2017 ⊃ 2013 |
| 5 | `SELL` | inline | `SELL` | = (2013 = 2017) |
| 6 | `CANCEL` | inline | `CANCEL` | = (2013 = 2017) |
| 7 | `CONFIRM` | inline | `CONFIRM` | = (2013 = 2017) |
| 8 | `BUY` | inline | `BUY` | = (2013 = 2017) |
| 9 | `NOTIFY` | inline | `NOTIFY` | = (2013 = 2017) |
| 10 | `EVENT_REQUEST` | inline | – | 2017 ⊂ 2013 |
| 11 | `EVENT_GRANT` | inline | – | 2017 ⊂ 2013 |
| 12 | `LOGIN` | inline | `LOGIN` | = (2013 = 2017) |
| 13 | `SELECT2` | inline | `SELECT2` | = (2013 = 2017) |
| 14 | `REQUEST_ALL_SALES` | inline | `REQUEST_ALL_SALES` | = (2013 = 2017) |
| 15 | `OPEN_ANYWHERE` | inline | `OPEN_ANYWHERE` | = (2013 = 2017) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 1 | `ADD_SALES` | AGPMAUCTION_CB_ADD_SALES | – |
| 10 | `EVENT_REQUEST` | AGPMAUCTION_CB_OPEN_AUCTION | – |
| 11 | `EVENT_GRANT` | AGPMAUCTION_CB_OPEN_AUCTION | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 6, gemeinsamer Rumpf: 14, nicht im Client: 4, ohne Kandidat: 5, zugeordnet: 4.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `RemoveAllSales` | 38 | `0x0055E330` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseRowsetPacket` | 42 | `0x0055E470` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DestroySales` | 6 | `0x0055DED0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCAD` | 5 | `0x0055DF00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmAuction`](AgcmAuction.md)
