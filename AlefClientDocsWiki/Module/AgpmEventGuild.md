# AgpmEventGuild (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventGuild` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventGuild` / `AgpmEventGuild.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x005748F0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMEVENT_GUILD_PACKET_*` kennt 6 Operationen, davon 6 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 6 Operationen liegen 2013er Ereignisse vor; 5 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 1 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`00574130`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00574130` | `AgpmEventGuild::ctor_or_dtor_00574130` | merged |
| `0x00574200` | `AgpmEventGuild::ctor_or_dtor_00574200` | merged |
| `0x00574730` | `AgpmEventGuild::CBActionGuild` | stage1 |
| `0x005747B0` | `AgpmEventGuild::CBActionGuildWarehouse` | stage1 |
| `0x00574830` | `AgpmEventGuild::~AgpmEventGuild` | merged |
| `0x00574850` | `AgpmEventGuild::OnAddModule` | merged |
| `0x005748F0` | `AgpmEventGuild::OnReceive` | merged |
| `0x00574260` | `AgpmEventGuild::OnOperationRequest` | casemap:AgpmEventGuild |
| `0x00574350` | `AgpmEventGuild::OnOperationRequestWarehouse` | casemap:AgpmEventGuild |
| `0x00574470` | `AgpmEventGuild::OnOperationRequestWorldChampionship` | casemap:AgpmEventGuild |

10 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 3/3/3 | ja | ja |

**m_csPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | PACKET | 1 | Event Base Packet |
| 2 | `0x4` | INT32 | 1 | CID |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `REQUEST` | `0x00574260` `OnOperationRequest` | `REQUEST` | = (2013 = 2017) |
| 1 | `GRANT` | inline | – | 2017 ⊂ 2013 |
| 2 | `REQUEST_WAREHOUSE` | `0x00574350` `OnOperationRequestWarehouse` | `REQUEST_WAREHOUSE` | = (2013 = 2017) |
| 3 | `GRANT_WAREHOUSE` | `0x00574440` `OnOperationGrant` | `GRANT_WAREHOUSE` | = (2013 = 2017) |
| 4 | `REQUEST_WORLD_CHAMPIONSHIP` | `0x00574470` `OnOperationRequestWorldChampionship` | `REQUEST_WORLD_CHAMPIONSHIP` | = (2013 = 2017) |
| 5 | `GRANT_WORLD_CHAMPIONSHIP` | `0x00574560` `FUN_00574560` | `GRANT_WORLD_CHAMPIONSHIP` | = (2013 = 2017) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 1 | `GRANT` | AGPMEVENT_GUILD_CB_GRANT | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 6, nicht im Client: 3, ohne Kandidat: 3, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketEventRequestWorldChampionship` | 18 | `0x005746B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequestWarehouse` | 18 | `0x00574630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequest` | 18 | `0x005745B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventGuild`](AgcmEventGuild.md), [`AgcmUIGuild`](AgcmUIGuild.md)
