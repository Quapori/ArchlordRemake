# AgpmChannel (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmChannel` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmChannel` / `AgpmChannel.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00560A50` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMCHANNEL_OPERATION_*` kennt 12 Operationen, davon 11 mit eigenem Case im 2017er Binary; ohne Case: `NONE` (0).
- **Vergleich mit 2013:** Für 11 Operationen liegen 2013er Ereignisse vor; 9 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`005600b0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x005600B0` | `AgpmChannel::ctor_or_dtor_005600b0` | merged |
| `0x005601C0` | `AgpmChannel::ctor_or_dtor_005601c0` | merged |
| `0x00560770` | `AgpmChannel::~AgpmChannel` | merged |
| `0x00560980` | `AgpmChannel::AgpdJoinChannelConstructor` | stage1 |
| `0x005609D0` | `AgpmChannel::OnAddModule` | merged |
| `0x00560A50` | `AgpmChannel::OnReceive` | merged |

6 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 4/4/4 | 9/9/9 | ja | ja |

**m_csPacket** (9 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | CID |
| 2 | `0x4` | CHAR | ApStrChannelName::eBufferLength + 1 | Channel Name |
| 3 | `0x8` | CHAR | ApStrChannelPassword::eBufferLength + 1 | password |
| 4 | `0x10` | CHAR | ApStrCharacterName::eBufferLength + 1 | user name |
| 5 | `0x20` | INT32 | 1 | Channel Type |
| 6 | `0x40` | INT32 | 1 | Message code |
| 7 | `0x80` | CHAR | ApStrChannelChatMsg::eBufferLength + 1 | Chatting Message |
| 8 | `0x100` | MEMORY_BLOCK | 1 | user list |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `NONE` | – | – | kein Case (default) – wie 2013 |
| 1 | `CREATE` | inline | `CREATE` | = (2013 = 2017) |
| 2 | `DESTROY` | inline | `DESTROY` | = (2013 = 2017) |
| 3 | `JOIN` | inline | `JOIN` | = (2013 = 2017) |
| 4 | `LEAVE` | inline | `LEAVE` | = (2013 = 2017) |
| 5 | `ADD_USER` | inline | `ADD_USER` | 2017 ⊃ 2013 |
| 6 | `REMOVE_USER` | inline | `REMOVE_USER` | 2017 ⊃ 2013 |
| 7 | `INVITATION` | inline | `INVITATION` | = (2013 = 2017) |
| 8 | `PASSWORD` | inline | `PASSWORD` | = (2013 = 2017) |
| 9 | `CHATMSG` | inline | `CHATMSG` | = (2013 = 2017) |
| 10 | `FIND_USER` | inline | `FIND_USER` | = (2013 = 2017) |
| 11 | `MSG_CODE` | inline | `MSG_CODE` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 14, nicht im Client: 5, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `CreateChannelData` | 19 | `0x00560D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIChannel`](AgcmUIChannel.md)
