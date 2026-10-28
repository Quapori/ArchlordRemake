# AgpmParty (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Paketmoduls `AgpmParty` (Gruppen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, EP8-Quelle (`Modules/APublic/AgpmParty`), Vergleich mit den Berichten zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Das Client-Modul [`AgcmParty`](AgcmParty.md) (Einladungen, Paket-Typ `0x09`) ist nicht Teil dieser Analyse.

## Kernbefund

- **Protokoll unverändert (2017 = EP8 = 2013):** Paket-Typ `0x08`; `m_csPacket` 11 Felder (Flag-Länge 2), `m_csPacketEffectArea` 5 Felder (Flag-Länge 1), `m_csPacketBonusStats` 4 Felder (Flag-Länge 1). Typen, Anzahlen und Flag-Längen stimmen mit der EP8-Quelle und der 2013er Doku überein.
- **Opcodes und Ereignisse unverändert:** Alle 7 Operationen (0–6) haben im 2017er Binary einen Case und lösen exakt dieselben Callback-IDs aus wie in der 2013er Messung. Die Callback-IDs sind gegenüber EP8 nicht verschoben (u. a. `ADD_PARTY` 6, `CHECK_DESTROY_PARTY` 9, `UPDATE_EXP_TYPE` 12, `UPDATE_ITEM_DIVISION` 15).
- **`OnReceive` entspricht der Quelle Zeile für Zeile:** 12 `GetField`-Argumente, Standardwerte `cCalcExpType` = 0 (`BY_DAMAGE`) und `cDivisionItem` = 2 (`DIVISION_ITEM_DAMAGE`), Mitgliederobergrenze 5 (`AGPMPARTY_MAX_PARTY_MEMBER`), Server-Pflicht für die Operationen 0–4 (`bReceivedFromServer`), keine Server-Pflicht für 5 und 6. Das `default` gibt wie in der Quelle `TRUE` zurück.
- **Adressen verschoben:** `OnReceive` bei `0x00567A90` (2013: `0x00568130`).

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x005665D0` | `AgpmParty::ctor_or_dtor_005665d0` | merged |
| `0x00566790` | `AgpmParty::ctor_or_dtor_00566790` | merged |
| `0x00566830` | `AgpmParty::OnInit` | merged |
| `0x005668F0` | `AgpmParty::GetPartyLock` | dispatch-struktur |
| `0x00566920` | `AgpmParty::OnOperationUpdateBonusStats` | dispatch-struktur |
| `0x005669C0` | `AgpmParty::CBCheckValidNormalAttack` | stage1 |
| `0x00566C50` | `AgpmParty::~AgpmParty` | merged |
| `0x00566C70` | `AgpmParty::OnIdle2` | merged |
| `0x00566C90` | `AgpmParty::ConAgpdPartyADChar` | stage1 |
| `0x00566CD0` | `AgpmParty::DesAgpdPartyADChar` | stage1 |
| `0x00566EB0` | `AgpmParty::GetLeaderCID` | dispatch-struktur |
| `0x00566F10` | `AgpmParty::DestroyParty` | dispatch-struktur |
| `0x00567130` | `AgpmParty::OnOperationUpdateEffectArea` | dispatch-struktur |
| `0x00567440` | `AgpmParty::OnDestroy` | merged |
| `0x00567510` | `AgpmParty::DestroyParty_ByID` | dispatch-struktur |
| `0x00567530` | `AgpmParty::CBCharLevelUp` | stage1 |
| `0x00567630` | `AgpmParty::AddMember` | dispatch-struktur |
| `0x00567740` | `AgpmParty::CreateParty` | dispatch-struktur |
| `0x00567800` | `AgpmParty::RemoveMember` | dispatch-struktur |
| `0x00567A90` | `AgpmParty::OnReceive` | merged |
| `0x005680D0` | `AgpmParty::CBRemoveChar` | stage1 |
| `0x00568160` | `AgpmParty::OnAddModule` | merged |

`OnReceive` = vtable-Slot 9; der Konstruktor liegt bei `0x005665D0`, `m_csPacket` bei `+0xD00`. Die Hilfsfunktionen (`GetPartyLock`, `CreateParty`, `AddMember`, `DestroyParty`, `RemoveMember`, `GetLeaderCID`, `OnOperationUpdateEffectArea`, `OnOperationUpdateBonusStats`) sind aus der Aufrufreihenfolge in `OnReceive` gegen die Quelle zugeordnet. Das Party-Objekt hat `m_nMaxMember` bei `+0x30`, `m_eCalcExpType` bei `+0x70` und `m_eDivisionItem` bei `+0x7C`.

## Paketlayout

Typcodes wie bei [`AgpmCharacter`](AgpmCharacter.md). Verglichen wurden Quelle (`SetFieldType`), 2017er Konstruktor (`FUN_004E9F80`) und die 2013er Tabellen.

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 11/11/11 | ja | ja |
| `m_csPacketEffectArea` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csPacketBonusStats` | 1/1/1 | 4/4/4 | ja | ja |

**m_csPacket** (11 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | Party ID |
| 2 | `0x4` | INT8 | 1 | # of MaxMember |
| 3 | `0x8` | INT8 | 1 | # of current member |
| 4 | `0x10` | INT32 | 1 | Add Remove member |
| 5 | `0x20` | MEMORY_BLOCK | 1 | party member list |
| 6 | `0x40` | PACKET | 1 | factor |
| 7 | `0x80` | PACKET | 1 | effect area |
| 8 | `0x100` | INT8 | 1 | AgpmPartyCalcExpType |
| 9 | `0x200` | PACKET | 1 | Bonus Stats |
| 10 | `0x400` | INT8 | 1 | ItemDivisionType |

**m_csPacketEffectArea** (5 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | member 1 |
| 1 | `0x2` | INT8 | 1 | member 2 |
| 2 | `0x4` | INT8 | 1 | member 3 |
| 3 | `0x8` | INT8 | 1 | member 4 |
| 4 | `0x10` | INT8 | 1 | member 5 |

**m_csPacketBonusStats** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | damage |
| 1 | `0x2` | INT8 | 1 | defense |
| 2 | `0x4` | INT16 | 1 | max hp |
| 3 | `0x8` | INT16 | 1 | max mp |

## Opcode-Tabelle

Alle Cases stehen inline in `OnReceive`; die Tabelle nennt die aufgerufenen Hilfsfunktionen im Verhalten. Ereignisse = Menge der `EnumCallback`-IDs (Tiefe 3).

| Op | Name | 2017-Handler | Ereignisse 2017 (auf EP8-IDs umgerechnet) | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | inline in `OnReceive` (`0x567A90`) | `ADD_MEMBER`, `ADD_PARTY`, `CREATE`, `REMOVE_ID`, `RESET_EFFECT_AREA` | = (2013 = 2017) |
| 1 | `REMOVE` | inline in `OnReceive` (`0x567A90`) | `REMOVE`, `REMOVE_ID` | = (2013 = 2017) |
| 2 | `UPDATE` | inline in `OnReceive` (`0x567A90`) | `RESET_EFFECT_AREA`, `UPDATE_BONUS_STATS` | = (2013 = 2017) |
| 3 | `ADD_MEMBER` | inline in `OnReceive` (`0x567A90`) | `ADD_MEMBER`, `RESET_EFFECT_AREA` | = (2013 = 2017) |
| 4 | `AGPMPARTY_PACKET_OPERATOIN_REMOVE_MEMBER` | inline in `OnReceive` (`0x567A90`) | `CHANGE_LEADER`, `CHECK_DESTROY_PARTY`, `REMOVE`, `REMOVE_ID`, `REMOVE_MEMBER`, `RESET_EFFECT_AREA` | = (2013 = 2017) |
| 5 | `UPDATE_EXP_TYPE` | inline in `OnReceive` (`0x567A90`) | `UPDATE_EXP_TYPE` | = (2013 = 2017) |
| 6 | `UPDATE_ITEM_DIVISION` | inline in `OnReceive` (`0x567A90`) | `UPDATE_ITEM_DIVISION` | = (2013 = 2017) |

## Abgleich mit EP8-Quelle und Besonderheiten

- **Op 0 `ADD`** (nur vom Server): `partyID != 0`, `maxMember != 0`, `currentMember ≥ 2`, Mitgliederliste vorhanden; Liste (1…5 Einträge) kopieren, die ersten beiden Zeichen sperren (`GetCharacterLock` für zwei IDs), `AllBlock` prüfen; `CreateParty(partyID, Anführer, zweites Mitglied, maxMember)`. Der Anführer ist das Zeichen, dessen CID `list[0]` entspricht. Danach `m_eCalcExpType` und `m_eDivisionItem` setzen, weitere Mitglieder (Index ≥ 2) per `AddMember(…, FALSE)` ergänzen, Effektbereich aktualisieren, `EnumCallback(ADD_PARTY, 6)`.
- **Op 1 `REMOVE`** (nur Server): Gruppe holen und `DestroyParty`.
- **Op 2 `UPDATE`** (nur Server): `m_nMaxMember` setzen (falls ≠ 0), Effektbereich und Bonus-Statistiken aktualisieren (Callbacks `RESET_EFFECT_AREA`, `UPDATE_BONUS_STATS`).
- **Op 3 `ADD_MEMBER`** (nur Server): Gruppe und Mitglied holen, `AddMember(…, FALSE)`, Effektbereich aktualisieren.
- **Op 4 `REMOVE_MEMBER`** (nur Server): zuerst `EnumCallback(CHECK_DESTROY_PARTY, 9)`; wird die Gruppe dadurch aufgelöst, `DestroyParty(partyID)`, sonst `RemoveMember(…)`.
- **Op 5 `UPDATE_EXP_TYPE` und Op 6 `UPDATE_ITEM_DIVISION`:** nur, wenn die Member-CID im Paket der Anführer-CID der Gruppe entspricht (`GetLeaderCID`); Änderung nur bei neuem Wert, dann `UPDATE_EXP_TYPE` (12) bzw. `UPDATE_ITEM_DIVISION` (15). Wie in der Quelle prüfen diese beiden Operationen nicht, ob sie vom Server kommen, und geben bei fremder Member-CID ohne Entsperren der Gruppe `FALSE` zurück.
- Der auskommentierte Faktor-Pfad (`pvPacketFactor` in `ADD`/`UPDATE`) ist auch im Binary nicht vorhanden; das Feld wird gelesen, aber nicht ausgewertet.

## Grenzen

- Die Helfer (`CreateParty`, `AddMember`, `RemoveMember`, `DestroyParty`) wurden nur an ihrer Aufrufstelle in `OnReceive` gegen die Quelle abgeglichen, nicht innerhalb ihrer Rümpfe; die ausgelösten Ereignisse (CREATE, ADD_MEMBER, REMOVE …) stammen aus der Tiefe-3-Suche.
- Die Reaktion des Clients auf die Party-Callbacks (`AgcmParty`, [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPartyOption`](AgcmUIPartyOption.md)) und die Einladungs-Operationen (Typ `0x09`) wurden nicht analysiert.
- `AGPMPARTY_CB_*`-Namen sind aus der Quelle übernommen; im Binary tragen die Ereignisse nur Nummern.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 4, eingebaut: 17, nicht im Client: 30, ohne Kandidat: 20, zugeordnet: 4.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `DestroyPartyData` | 4 | `0x005668B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveParty` | 30 | `0x00566DA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRemoveParty` | 23 | `0x00566BB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ArrangeHighestUnionRank` | 33 | `0x005673A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetParty` (`0x00566ED0`), `GetPartyLock` (`0x00566E50`), `GetLeaderCID` (`0x00566AC0`), `IsMember` (`0x00566ED0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmParty`](AgcmParty.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPartyOption`](AgcmUIPartyOption.md), [`AgpmCharacter`](AgpmCharacter.md)
- **Erwähnt in:** [`AgcmMinimap`](AgcmMinimap.md), [`AgcmParty`](AgcmParty.md), [`AgcmUIParty`](AgcmUIParty.md)
