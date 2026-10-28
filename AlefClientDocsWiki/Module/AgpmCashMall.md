# AgpmCashMall (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmCashMall` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmCashMall` / `AgpmCashMall.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x005576E0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMCASH_OPERATION_*` kennt 7 Operationen, davon 7 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 6 Operationen liegen 2013er Ereignisse vor; 6 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`005573c0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00556980` | `AgpmCashMall::OnAddModule` | merged |
| `0x00556CC0` | `AgpmCashMall::ctor_or_dtor_00556cc0` | merged |
| `0x00556D30` | `AgpmCashMall::~AgpmCashMall` | merged |
| `0x005573C0` | `AgpmCashMall::ctor_or_dtor_005573c0` | merged |
| `0x005576E0` | `AgpmCashMall::OnReceive` | merged |
| `0x00556A30` | `AgpmCashMall::OnOperationRequestMallProductList` | casemap:AgpmCashMall |
| `0x00556AA0` | `AgpmCashMall::OnOperationRequestBuyItem` | casemap:AgpmCashMall |
| `0x00556B30` | `AgpmCashMall::OnOperationResponseRefreshCash` | casemap:AgpmCashMall |
| `0x00557510` | `AgpmCashMall::OnOperationResponseMallList` | casemap:AgpmCashMall |
| `0x005575E0` | `AgpmCashMall::OnOperationResponseProductList` | casemap:AgpmCashMall |

10 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 9/9/9 | ja | ja |

**m_csPacket** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT8 | 1 | result |
| 2 | `0x4` | UINT8 | 1 | mall list version |
| 3 | `0x8` | INT32 | 1 | cid |
| 4 | `0x10` | INT32 | 1 | tab |
| 5 | `0x20` | INT32 | 1 | product id |
| 6 | `0x40` | MEMORY_BLOCK | 1 | mall tab list |
| 7 | `0x80` | MEMORY_BLOCK | 1 | item list |
| 8 | `0x100` | INT32 | 1 | type |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 1 | `REQUEST_MALL_PRODUCT_LIST` | `0x00556A30` `OnOperationRequestMallProductList` | `REQUEST_MALL_PRODUCT_LIST` | = (2013 = 2017) |
| 2 | `RESPONSE_MALL_LIST` | `0x00557510` `OnOperationResponseMallList` | – | keine Callback-Ereignisse (beide) |
| 3 | `RESPONSE_PRODUCT_LIST` | `0x005575E0` `OnOperationResponseProductList` | `UPDATE_MALL_LIST` | = (2013 = 2017) |
| 4 | `REQUEST_BUY_ITEM` | `0x00556AA0` `OnOperationRequestBuyItem` | `REQUEST_BUY_ITEM` | = (2013 = 2017) |
| 5 | `RESPONSE_BUY_RESULT` | inline | `RESPONSE_BUY_RESULT` | = (2013 = 2017) |
| 6 | `REFRESH_CASH` | `0x00556B30` `OnOperationResponseRefreshCash` | `REFRESH_CASH` | = (2013 = 2017) |
| 7 | `CHECK_LIST_VERSION` | `0x00556B70` `FUN_00556b70` | `CHECK_LIST_VERSION` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 9, nicht im Client: 5, ohne Kandidat: 10, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `DecodeProductList` | 58 | `0x00557120` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashItem` | 6 | `0x00556BF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmCashMall`](AgcmCashMall.md)
