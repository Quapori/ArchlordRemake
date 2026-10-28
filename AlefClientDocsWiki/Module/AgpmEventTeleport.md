# AgpmEventTeleport (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventTeleport` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventTeleport` / `AgpmEventTeleport.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0055B540` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMEVENT_TELEPORT_OPERATION_*` kennt 9 Operationen, davon 9 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 9 Operationen liegen 2013er Ereignisse vor; 9 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`00559810`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0054C2B0` | `AgpmEventTeleport::StreamReadGroup` | merged |
| `0x0054C3D0` | `AgpmEventTeleport::StreamReadPoint` | merged |
| `0x0054C4F0` | `AgpmEventTeleport::GroupWriteCB` | stage1 |
| `0x0054C530` | `AgpmEventTeleport::GroupReadCB` | stage1 |
| `0x0054C5B0` | `AgpmEventTeleport::PointWriteCB` | merged |
| `0x0054C870` | `AgpmEventTeleport::PointReadCB` | stage1 |
| `0x0054CBE0` | `AgpmEventTeleport::CBStreamWriteEvent` | stage1 |
| `0x0054CC40` | `AgpmEventTeleport::CBStreamReadEvent` | stage1 |
| `0x0054CD00` | `AgpmEventTeleport::unk_0054cd00` | unbestimmt |
| `0x0054CD7E` | `AgpmEventTeleport::unk_0054cd7e` | unbestimmt |
| `0x00559810` | `AgpmEventTeleport::ctor_or_dtor_00559810` | merged |
| `0x00559950` | `AgpmEventTeleport::ctor_or_dtor_00559950` | merged |
| `0x005599E0` | `AgpmEventTeleport::OnInit` | merged |
| `0x0055A0D0` | `AgpmEventTeleport::CBEventConstructor` | stage1 |
| `0x0055A3B0` | `AgpmEventTeleport::~AgpmEventTeleport` | merged |
| `0x0055A7B0` | `AgpmEventTeleport::ConAgpdTeleportAttachToChar` | stage1 |
| `0x0055AC20` | `AgpmEventTeleport::CBEventDestructor` | stage1 |
| `0x0055AE20` | `AgpmEventTeleport::OnDestroy` | merged |
| `0x0055B540` | `AgpmEventTeleport::OnReceive` | merged |
| `0x0055BD30` | `AgpmEventTeleport::CBActionEventTeleport` | stage1 |
| `0x0055BEB0` | `AgpmEventTeleport::OnAddModule` | merged |
| `0x00559CB0` | `AgpmEventTeleport::GetTeleportPoint` | casemap:AgpmEventTeleport |
| `0x00559CF0` | `AgpmEventTeleport::GetEventFromBasePacket` | casemap:AgpmEventTeleport |
| `0x0055A640` | `AgpmEventTeleport::GetCharacterLock` | casemap:AgpmEventTeleport |

24 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 6/6/6 | ja | ja |

**m_csPacket** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation typef |
| 1 | `0x2` | PACKET | 1 | Event Base |
| 2 | `0x4` | INT32 | 1 | Character CID |
| 3 | `0x8` | CHAR | AGPD_TELEPORT_MAX_POINT_NAME + 1 | Target TeleportPoint nAME |
| 4 | `0x10` | POS | 1 | AUTYPE_INT32, 1,// Target Position Index (Local Attached Data) |
| 5 | `0x20` | MEMORY_BLOCK | 1 | Target Custom Position |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `TELEPORT_POINT` | `0x00559CB0` `GetTeleportPoint` | `ID_BATTLEGROUND_TELEPORT_LOG`, `ID_CALC_POS`, `ID_CHECK_USABLE_TELEPORT`, `ID_GET_BATTLEGROUND_STATE`, `ID_SET_TELEPORTBLOCK`, `ID_SYNC_TELEPORT_LOADING` … (7) | = (2013 = 2017) |
| 1 | `TELEPORT_START` | inline | `ID_RECEIVED_TELEPORT_START` | = (2013 = 2017) |
| 2 | `TELEPORT_CANCELED` | inline | `ID_RECEIVED_TELEPORT_CANCELED` | = (2013 = 2017) |
| 3 | `TELEPORT_CUSTOM_POS` | `0x0055A640` `GetCharacterLock` | `ID_BATTLEGROUND_TELEPORT_LOG`, `ID_CALC_POS`, `ID_GET_BATTLEGROUND_STATE`, `ID_SYNC_TELEPORT_LOADING`, `ID_TELEPORT_LOG` | = (2013 = 2017) |
| 4 | `REQUEST_TELEPORT` | `0x00559CF0` `GetEventFromBasePacket` | `ID_ARCHLORD_MESSAGE_ID` | = (2013 = 2017) |
| 5 | `REQUEST_TELEPORT_GRANTED` | inline | `ID_RECEIVED_REQUEST_RESULT` | = (2013 = 2017) |
| 6 | `REQUEST_TELEPORT_IGNOIRED` | inline | `ID_RECEIVED_REQUEST_RESULT` | = (2013 = 2017) |
| 7 | `TELEPORT_RETURN` | inline | `ID_RETURN_TOWN` | = (2013 = 2017) |
| 8 | `TELEPORT_LOADING` | inline | `ID_RECEIVE_TELEPORT_LOADING` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 12, gemeinsamer Rumpf: 14, nicht im Client: 12, ohne Kandidat: 10, zugeordnet: 14.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetTargetPointList` | 24 | `0x0055A490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSequenceTargetGroup` | 13 | `0x0055A450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadFee` | 44 | `0x0054CD00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsArchlordDungeonPoint` | 43 | `0x0055A210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsDisablePoint` | 29 | `0x0055B230` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendTeleportStart` | 20 | `0x00559F10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTargetPoint` | 65 | `0x0055B070` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveFee` | 17 | `0x00559A90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRequestTeleportGranted` | 69 | `0x0055B320` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetFee` | 24 | `0x0055A170` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTeleportLoading` | 24 | `0x0055A040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRequestTeleport` | 26 | `0x00559F90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTeleportReturn` | 30 | `0x00559DF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendTeleportInfo` | 22 | `0x00559D50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `RemoveTeleportPoint` (`0x0055A9C0`), `SendTeleportCanceled` (`0x00559E90`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgcmUIEventTeleport`](AgcmUIEventTeleport.md)
