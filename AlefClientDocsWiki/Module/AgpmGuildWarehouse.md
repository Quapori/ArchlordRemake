# AgpmGuildWarehouse (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmGuildWarehouse` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmGuildWarehouse` / `AgpmGuildWarehouse.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00577180` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMGUILDWAREHOUSE_OPERATION_*` kennt 9 Operationen, davon 8 mit eigenem Case im 2017er Binary; ohne Case: `EXPAND` (8).
- **Vergleich mit 2013:** Für 8 Operationen liegen 2013er Ereignisse vor; 8 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Callback-ID-Verschiebung:** Der beste Abgleich mit der 2013er Messung ergibt sich bei einer Verschiebung der Quell-IDs um `1` (ab ID 0).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`00576db0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00576DB0` | `AgpmGuildWarehouse::ctor_or_dtor_00576db0` | merged |
| `0x00576E90` | `AgpmGuildWarehouse::ctor_or_dtor_00576e90` | merged |
| `0x00577160` | `AgpmGuildWarehouse::~AgpmGuildWarehouse` | merged |
| `0x00577180` | `AgpmGuildWarehouse::OnReceive` | merged |
| `0x00577670` | `AgpmGuildWarehouse::ConAgpdGuildWarehouse` | stage1 |
| `0x00577720` | `AgpmGuildWarehouse::DesAgpdGuildWarehouse` | stage1 |
| `0x005777D0` | `AgpmGuildWarehouse::OnAddModule` | merged |

7 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 9/9/9 | ja | ja |

**m_csPacket** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | cid |
| 2 | `0x4` | INT64 | 1 | money |
| 3 | `0x8` | INT32 | 1 | slot |
| 4 | `0x10` | INT32 | 1 | item id |
| 5 | `0x20` | INT32 | 1 | layer |
| 6 | `0x40` | INT32 | 1 | row |
| 7 | `0x80` | INT32 | 1 | column |
| 8 | `0x100` | INT32 | 1 | result |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `NONE` | `0x00576EF0` `FUN_00576ef0` | `BASE_INFO` | = (2013 = 2017) |
| 1 | `BASE_INFO` | inline | `OPEN` | = (2013 = 2017) |
| 2 | `OPEN` | inline | `CLOSE` | = (2013 = 2017) |
| 3 | `CLOSE` | inline | `MONEY_IN` | = (2013 = 2017) |
| 4 | `MONEY_IN` | inline | `MONEY_OUT` | = (2013 = 2017) |
| 5 | `MONEY_OUT` | inline | `ITEM_IN` | = (2013 = 2017) |
| 6 | `ITEM_IN` | inline | `ITEM_OUT` | = (2013 = 2017) |
| 7 | `ITEM_OUT` | inline | `EXPAND` | = (2013 = 2017) |
| 8 | `EXPAND` | – | – | kein Case (default) – wie 2013 |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 9, gemeinsamer Rumpf: 11, ohne Kandidat: 6, zugeordnet: 4.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `CheckPreviledge` | 21 | `0x005770D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItem` | 44 | `0x00577550` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItem` | 49 | `0x005773F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetGuildWarehouse` | 5 | `0x00576EF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIGuildWarehouse`](AgcmUIGuildWarehouse.md)
