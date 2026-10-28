# AgcmParty (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmParty` (Gruppeneinladungen, Paket-Typ `0x09`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und -Disassembly, EP8-Quelle (`Modules/AClient/AgcmParty`) und die 2013er Berichte (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Protokoll unverändert (2017 = EP8 = 2013):** Paket-Typ `0x09`, `m_csPacket` mit 4 Feldern (Operation INT8, Operator-ID INT32, Ziel-ID INT32, Zielname CHAR) und Flag-Länge 1. Alle 21 Operationen (0–20) sind im 2017er Binary vorhanden und lösen dieselben Callback-IDs aus wie in der Quelle und in der 2013er Messung.
- **Callback-ID = Operationsnummer** für alle Operationen: Op 0–14 und 18–20 feuern `EnumCallback(Op, …)`, Op 15–17 (Recall) rufen die Hilfsfunktionen `OnReceiveRequestRecall/AcceptRecall/RejectRecall`, die `EnumCallback(15/16/17)` auslösen. Keine ID-Verschiebung.
- **Dispatch:** `OnReceive` (`0x006E84C0`, vtable-Slot 9) liest 4 Felder und springt über eine Tabelle bei `0x006E87CC` (21 Einträge, Basis 0); Operationen `≥ 21` geben `TRUE` zurück. Die Case-Blöcke liegen bei `0x006E8538`–`0x006E87C8` außerhalb des von Ghidra erfassten Funktionskörpers.
- **Client → Server:** `SendPacketInvite` (Op 0), `SendPacketReject` (Op 1), `SendPacketAccept` (Op 2), `SendPacketLeave` (Op 3), `SendPacketBanish` (Op 4) und `SendPacketInviteByCharID` (Op 0 mit Zielname, Ziel-ID 0) senden dasselbe Paket mit der jeweiligen Operation. Die Fehlermeldung bei Sendefehlern lautet wie in der Quelle `AgsmParty::SendPacket…() failed` (Kopierfehler der Quelle).
- **Adressen verschoben:** `OnReceive` bei `0x006E84C0` (2013: `0x006E8AB0`, Tabelle `0x006E8DBC` → 2017: `0x006E87CC`).

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00566890` | [`AgpmParty`](AgpmParty.md):GetADCharacter` | dispatch-struktur |
| `0x006E8000` | `AgcmParty::ctor_or_dtor_006e8000` | merged |
| `0x006E80C0` | `AgcmParty::ctor_or_dtor_006e80c0` | merged |
| `0x006E8120` | `AgcmParty::OnReceiveRequestRecall` | dispatch-struktur |
| `0x006E8190` | `AgcmParty::OnReceiveAcceptRecall` | dispatch-struktur |
| `0x006E81D0` | `AgcmParty::OnReceiveRejectRecall` | dispatch-struktur |
| `0x006E8310` | `AgcmParty::CBCheckRemoveChar` | stage1 |
| `0x006E8370` | `AgcmParty::CBCheckDestroyParty` | stage1 |
| `0x006E83F0` | `AgcmParty::~AgcmParty` | merged |
| `0x006E8410` | `AgcmParty::OnAddModule` | merged |
| `0x006E84C0` | `AgcmParty::OnReceive` | merged |
| `0x006E8820` | `AgcmParty::SendPacketInvite` | strmatch |
| `0x006E88C0` | `AgcmParty::SendPacketReject` | strmatch |
| `0x006E8960` | `AgcmParty::SendPacketAccept` | strmatch |
| `0x006E8A00` | `AgcmParty::SendPacketLeave` | strmatch |
| `0x006E8A90` | `AgcmParty::SendPacketBanish` | strmatch |
| `0x006E8B30` | `AgcmParty::SendPacketInviteByCharID` | strmatch |

`AgcmParty` hat 17 vtable-Einträge (gleich wie die Quelle), der Konstruktor liegt bei `0x006E8000`, `m_csPacket` bei `+0xBA8`, die Referenz auf `AgcmCharacter` bei `+0xBA0`. `CBCheckRemoveChar` und `CBCheckDestroyParty` sind Handler, die `AgcmParty` bei `AgpmParty` registriert.

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 4/4/4 | ja | ja |

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | operator id |
| 2 | `0x4` | INT32 | 1 | target id |
| 3 | `0x8` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 |  |

## Opcodes (Server → Client)

Spalte „Block“ = Sprungtabellen-Ziel im 2017er Binary. Alle Blöcke setzen den Aufruf ab (`EnumCallback` bei `0x004E4040` bzw. Recall-Handler) und enden mit `return TRUE`.

| Op | Name (`AGCMPARTY_PACKET_OPERATION_…`) | Block | Aktion 2017 | Callback (ID) | Vergleich 2013 |
|---:|---|---|---|---|---|
| 0 | `INVITE` | `0x6E8538` | direkt `EnumCallback` | `RECEIVE_INVITE` (0) | = |
| 1 | `REJECT` | `0x6E8567` | direkt `EnumCallback` | `RECEIVE_REJECT` (1) | = |
| 2 | `INVITE_ACCEPT` | `0x6E8586` | direkt `EnumCallback` | `RECEIVE_INVITE_ACCEPT` (2) | = |
| 3 | `LEAVE` | `0x6E85A5` | direkt `EnumCallback` | `RECEIVE_LEAVE` (3) | = |
| 4 | `BANISH` | `0x6E85C4` | direkt `EnumCallback` | `RECEIVE_BANISH` (4) | = |
| 5 | `INVITE_FAILED_ALREADY_OTHER_PARTY_MEMBER` | `0x6E85E3` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_ALREADY_OTHER_PARTY_MEMBER` (5) | = |
| 6 | `INVITE_FAILED_ALREADY_PARTY_MEMBER` | `0x6E8602` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_ALREADY_PARTY_MEMBER` (6) | = |
| 7 | `INVITE_FAILED_PARTY_MEMBER_IS_FULL` | `0x6E8621` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_PARTY_MEMBER_IS_FULL` (7) | = |
| 8 | `INVITE_FAILED_NOT_LEADER` | `0x6E8640` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_NOT_LEADER` (8) | = |
| 9 | `FAILED` | `0x6E865F` | direkt `EnumCallback` | `RECEIVE_OPERATION_FAILED` (9) | = |
| 10 | `INVITE_FAILED_NO_LOGIN_MEMBER` | `0x6E867E` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_NO_LOGIN_MEMBER` (10) | = |
| 11 | `DELEGATION_LEADER` | `0x6E869D` | direkt `EnumCallback` | `RECEIVE_DELEGATION_LEADER` (11) | = |
| 12 | `DELEGATION_LEADER_FAILED` | `0x6E86BC` | direkt `EnumCallback` | `RECEIVE_DELEGATION_LEADER_FAILED` (12) | = |
| 13 | `INVITE_FAILED_LEVEL_DIFF` | `0x6E86DB` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_LEVEL_DIFF` (13) | = |
| 14 | `INVITE_FAILED_REFUSE` | `0x6E86FA` | direkt `EnumCallback` | `RECEIVE_INVITE_FAILED_REFUSE` (14) | = |
| 15 | `REQUEST_RECALL` | `0x6E8719` | `0x6E8120` `OnReceiveRequestRecall`: Zeichen und eigenes Zeichen vorhanden, beide in derselben Gruppe (`GetADCharacter(…)->lPID`) | `REQUEST_RECALL` (15) | = |
| 16 | `ACCEPT_RECALL` | `0x6E8731` | `0x6E8190` `OnReceiveAcceptRecall`: Zeichen und eigenes Zeichen vorhanden | `ACCEPT_RECALL` (16) | = |
| 17 | `REJECT_RECALL` | `0x6E874E` | `0x6E81D0` `OnReceiveRejectRecall`: Zeichen und eigenes Zeichen vorhanden | `REJECT_RECALL` (17) | = |
| 18 | `INVITE_FAILED_MURDERER_OPERATOR` | `0x6E876B` | direkt `EnumCallback` | `INVITE_FAILED_MURDERER_OPERATOR` (18) | = |
| 19 | `INVITE_FAILED_MURDERER_TARGET` | `0x6E8787` | direkt `EnumCallback` | `INVITE_FAILED_MURDERER_TARGET` (19) | = |
| 20 | `LEAVE_BY_MURDERER` | `0x6E87A6` | direkt `EnumCallback` | `LEAVE_BY_MURDERER` (20) | = |

Argumente der Callbacks (Quelle; im Binary als Zeiger übergeben): Op 0 `(&Operator-ID, {Ziel-ID, Zielname})`; Op 1–9, 11–13 `(&Operator-ID, &Ziel-ID)`; Op 10, 14 und 19 `(&Operator-ID, Zielname)`; Op 18 und 20 `(&Operator-ID, NULL)`. Im Binary entsprechen Op 18 und 20 genau dem Muster „zweites Argument 0“.

## Client → Server

| Funktion | Adresse | Operation |
|---|---|---:|
| `AgcmParty::SendPacketInvite` | `0x6E8820` | 0 |
| `AgcmParty::SendPacketReject` | `0x6E88C0` | 1 |
| `AgcmParty::SendPacketAccept` | `0x6E8960` | 2 |
| `AgcmParty::SendPacketLeave` | `0x6E8A00` | 3 |
| `AgcmParty::SendPacketBanish` | `0x6E8A90` | 4 |
| `AgcmParty::SendPacketInviteByCharID` | `0x6E8B30` | 0 |

Alle sechs rufen `MakePacket` (`FUN_004EA2D0`, Paket-Typ 9, 4 Felder) und `SendPacket` (`FUN_004E45A0`) und geben das Paket anschließend frei. Die Funktionen `SendPacketFailed`, `SendPacketUpdateExpType`, `SendPacketUpdateItemDivision`, `SendPacketDelegationLeader`, `SendPacketAcceptRecall` und `SendPacketRejectRecall` aus der Quelle liegen im 2017er Binary nicht im untersuchten Fenster (vermutlich inline in der UI-Schicht) und sind nicht belegt.

## Grenzen

- Die Zuordnung der Case-Blöcke zu den Operationen folgt der Reihenfolge der Sprungtabelle; die Argumente der Callbacks wurden nur an den Registern (Operator/Ziel/Name) nachvollzogen, nicht gegen die Quellstruktur Feld für Feld geprüft.
- Die Reaktion des Clients auf die Callbacks ([`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPartyOption`](AgcmUIPartyOption.md), Chat-Meldungen, Ablehnungsfenster) wurde nicht analysiert.
- Das Server-seitige Gegenstück (`AgsmParty`) liegt nicht im Client.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 24, nicht im Client: 1, ohne Kandidat: 15, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SendPacketDelegationLeader` | 12 | `0x006E8BC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPartyOption`](AgcmUIPartyOption.md), [`AgpmParty`](AgpmParty.md)
- **Erwähnt in:** [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgpmParty`](AgpmParty.md)
