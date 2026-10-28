# AgpmEventProduct (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventProduct` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventProduct` / `AgpmEventProduct.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00570370` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMEVENT_PRODUCT_PACKET_*` kennt 6 Operationen, davon 6 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 6 Operationen liegen 2013er Ereignisse vor; 6 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`0056f9e0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056F9E0` | `AgpmEventProduct::ctor_or_dtor_0056f9e0` | merged |
| `0x0056FAF0` | `AgpmEventProduct::ctor_or_dtor_0056faf0` | merged |
| `0x00570030` | `AgpmEventProduct::CBActionProduct` | stage1 |
| `0x005700B0` | `AgpmEventProduct::CBStreamWriteEvent` | stage1 |
| `0x00570110` | `AgpmEventProduct::CBStreamReadEvent` | stage1 |
| `0x00570230` | `AgpmEventProduct::CBEmbeddedPacketEncode` | stage1 |
| `0x00570260` | `AgpmEventProduct::CBEmbeddedPacketDecode` | stage1 |
| `0x00570290` | `AgpmEventProduct::~AgpmEventProduct` | merged |
| `0x005702B0` | `AgpmEventProduct::OnAddModule` | merged |
| `0x00570370` | `AgpmEventProduct::OnReceive` | merged |
| `0x0056FC70` | `AgpmEventProduct::OnOperationRequest` | casemap:AgpmEventProduct |
| `0x0056FD90` | `AgpmEventProduct::OnOperationBuyCompose` | casemap:AgpmEventProduct |
| `0x0056FE30` | `AgpmEventProduct::OnOperationLearnSkill` | casemap:AgpmEventProduct |
| `0x0056FE70` | `AgpmEventProduct::OnOperationLearnSkillResult` | casemap:AgpmEventProduct |

14 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csPacketEmb` | 1/1/1 | 1/1/1 | ja | ja |

**m_csPacket** (5 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | PACKET | 1 | Event Base Packet |
| 2 | `0x4` | INT32 | 1 | CID |
| 3 | `0x8` | INT32 | 1 | ID (SkillTID or ComposeID) |
| 4 | `0x10` | INT32 | 1 | Result |

**m_csPacketEmb** (1 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | product skill category |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `REQUEST` | `0x0056FC70` `OnOperationRequest` | `REQUEST` | = (2013 = 2017) |
| 1 | `GRANT` | `0x0056FD60` `OnOperationGrant` | `GRANT` | = (2013 = 2017) |
| 2 | `LEARN_SKILL` | `0x0056FE30` `OnOperationLearnSkill` | `LEARN_SKILL` | = (2013 = 2017) |
| 3 | `LEARN_SKILL_RESULT` | `0x0056FE70` `OnOperationLearnSkillResult` | `LEARN_SKILL_RESULT` | = (2013 = 2017) |
| 4 | `BUY_COMPOSE` | `0x0056FD90` `OnOperationBuyCompose` | `BUY_COMPOSE` | = (2013 = 2017) |
| 5 | `BUY_COMPOSE_RESULT` | `0x0056FDD0` `FUN_0056fdd0` | `BUY_COMPOSE_RESULT` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 5, gemeinsamer Rumpf: 6, nicht im Client: 3, ohne Kandidat: 4, zugeordnet: 7.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetBuyCost` | 5 | `0x0056FC30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidLearnSkill` | 36 | `0x00570570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketLearnSkill` | 19 | `0x00570830` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParsePacketEventData` | 13 | `0x005701E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventData` | 10 | `0x005701A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketBuyCompose` | 19 | `0x0056FF30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequest` | 20 | `0x0056FEB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventProduct`](AgcmEventProduct.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md)
