# AgpmReturnToLogin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmReturnToLogin` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmReturnToLogin` / `AgpmReturnToLogin.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0057BFD0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMRETURN_*` kennt 7 Operationen, davon 7 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 7 Operationen liegen 2013er Ereignisse vor; 7 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0057bcf0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056A820` | `AgpmReturnToLogin::OnAddModule` | merged |
| `0x0057BCF0` | `AgpmReturnToLogin::ctor_or_dtor_0057bcf0` | merged |
| `0x0057BDC0` | `AgpmReturnToLogin::ctor_or_dtor_0057bdc0` | merged |
| `0x0057BFB0` | `AgpmReturnToLogin::~AgpmReturnToLogin` | merged |
| `0x0057BFD0` | `AgpmReturnToLogin::OnReceive` | merged |
| `0x0057BE20` | `AgpmReturnToLogin::OnOperationRequest` | casemap:AgpmReturnToLogin |
| `0x0057BE60` | `AgpmReturnToLogin::OnOperationRequestKey` | casemap:AgpmReturnToLogin |
| `0x0057BE90` | `AgpmReturnToLogin::OnOperationReconnectLoginServer` | casemap:AgpmReturnToLogin |

8 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 6/6/6 | ja | ja |

**m_csPacket** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | character id |
| 2 | `0x4` | CHAR | AGPDCHARACTER_MAX_ID_LENGTH + 1 | account name |
| 3 | `0x8` | CHAR | 32 | server group name |
| 4 | `0x10` | CHAR | 25 | login server address |
| 5 | `0x20` | INT32 | 1 | encrypt code |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 1 | `OPERATION_REQUEST` | `0x0057BE20` `OnOperationRequest` | `REQUEST` | = (2013 = 2017) |
| 2 | `OPERATION_REQUEST_FAILED` | inline | `REQUEST_FAILED` | = (2013 = 2017) |
| 3 | `OPERATION_REQUEST_KEY` | `0x0057BE60` `OnOperationRequestKey` | `REQEUST_KEY` | = (2013 = 2017) |
| 4 | `OEPRATION_RESPONSE_KEY` | inline | `RESPONSE_KEY` | = (2013 = 2017) |
| 5 | `OPERATION_SEND_KEY_ADDR` | inline | `SEND_KEY_ADDR` | = (2013 = 2017) |
| 6 | `OPERATION_RECONNECT_LOGIN_SERVER` | `0x0057BE90` `OnOperationReconnectLoginServer` | `RECONNECT_LOGIN_SERVER` | = (2013 = 2017) |
| 7 | `OPERATION_END_PROCESS` | inline | `END_PROCESS` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 7, nicht im Client: 5, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketReconnectLoginServer` | 13 | `0x0057BF60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequest` | 13 | `0x0057BF10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmReturnToLogin`](AgcmReturnToLogin.md)
