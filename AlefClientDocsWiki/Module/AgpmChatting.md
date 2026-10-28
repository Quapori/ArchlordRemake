# AgpmChatting (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmChatting` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmChatting` / `AgpmChatting.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0056E980` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPDCHATTING_OPERATION_*` kennt 5 Operationen, davon 5 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 3 Operationen liegen 2013er Ereignisse vor; 3 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0056e290`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056E290` | `AgpmChatting::ctor_or_dtor_0056e290` | merged |
| `0x0056E380` | `AgpmChatting::ctor_or_dtor_0056e380` | merged |
| `0x0056E3F0` | `AgpmChatting::OnInit` | merged |
| `0x0056E590` | `AgpmChatting::~AgpmChatting` | merged |
| `0x0056E610` | `AgpmChatting::ConAgpdCharacter` | stage1 |
| `0x0056E650` | `AgpmChatting::OnAddModule` | merged |
| `0x0056E980` | `AgpmChatting::OnReceive` | merged |
| `0x0056E420` | `AgpmChatting::OnOperationReplyBlockWhisper` | casemap:AgpmChatting |
| `0x0056E5B0` | `AgpmChatting::OnOperationSetBlockWhisper` | casemap:AgpmChatting |
| `0x0056E5E0` | `AgpmChatting::OnOperationReleaseBlockWhisper` | casemap:AgpmChatting |
| `0x0056E6B0` | `AgpmChatting::OnOperationChat` | casemap:AgpmChatting |

11 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 7/7/7 | ja | ja |

**m_csPacket** (7 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | CID |
| 2 | `0x4` | INT8 | 1 | Chat Type |
| 3 | `0x8` | UINT32 | 1 | Character Type |
| 4 | `0x10` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Sender ID |
| 5 | `0x20` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Target ID |
| 6 | `0x40` | MEMORY_BLOCK | 1 | chatting message |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `CHAT` | `0x0056E6B0` `OnOperationChat` | `CHECK_BLOCK_WHISPER_MSG`, `CHECK_ENABLE`, `RECV_EMPHASIS_MSG`, `RECV_GUILD_JOINT_MSG`, `RECV_GUILD_MSG`, `RECV_NORMAL_MSG` … (12) | = (2013 = 2017) |
| 1 | `SET_BLOCK_WHISPER` | `0x0056E5B0` `OnOperationSetBlockWhisper` | – | keine Callback-Ereignisse (beide) |
| 2 | `RELEASE_BLOCK_WHISPER` | `0x0056E5E0` `OnOperationReleaseBlockWhisper` | – | keine Callback-Ereignisse (beide) |
| 3 | `REPLY_BLOCK_WHISPER` | `0x0056E420` `OnOperationReplyBlockWhisper` | `RECV_REPLY_BLOCK_WHISPER` | = (2013 = 2017) |
| 4 | `OFFLINE_WHISPER_TARGET` | `0x0056E450` `FUN_0056e450` | `RECV_OFFLINE_WHISPER_TARGET` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 17, nicht im Client: 9, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketChatting` | 38 | `0x0056E480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIChatting2`](AgcmUIChatting2.md)
