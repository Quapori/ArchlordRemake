# AgpmAdmin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmAdmin` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmAdmin` / `AgpmAdmin.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00556620` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMADMIN_PACKET_*` kennt 20 Operationen, davon 20 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Die 2013er Berichte enthalten für dieses Modul keine Callback-Ereignisse je Operation; ein Abgleich ist nicht möglich.
- **Paketlayout:** 14 Paketdefinition(en) in der Quelle, 14 davon im 2017er Konstruktor (`00555d20`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x005558E0` | `AgpmAdmin::ConAgpdAdminADChar` | stage1 |
| `0x00555930` | `AgpmAdmin::DesAgpdAdminADChar` | stage1 |
| `0x00555CA0` | `AgpmAdmin::CBRemoveAdmin` | stage1 |
| `0x00555D20` | `AgpmAdmin::ctor_or_dtor_00555d20` | merged |
| `0x00556190` | `AgpmAdmin::ctor_or_dtor_00556190` | merged |
| `0x00556350` | `AgpmAdmin::OnAddModule` | merged |
| `0x005564E0` | `AgpmAdmin::~AgpmAdmin` | merged |
| `0x00556620` | `AgpmAdmin::OnReceive` | merged |
| `0x005558A0` | `AgpmAdmin::OnOperationUserPosition` | casemap:AgpmAdmin |
| `0x005558C0` | `AgpmAdmin::OnOperationUserPositionStatistics` | casemap:AgpmAdmin |
| `0x00555A80` | `AgpmAdmin::OnOperationAdminClient` | casemap:AgpmAdmin |
| `0x00556500` | `AgpmAdmin::OnOperationLogin` | casemap:AgpmAdmin |

12 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 15/15/15 | ja | ja |
| `m_csLoginPacket` | 1/1/1 | 6/6/6 | ja | ja |
| `m_csSearchPacket` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csSearchResultPacket` | 2/2/2 | 12/12/12 | ja | ja |
| `m_csSearchCharDataPacket` | 2/2/2 | 6/6/6 | ja | ja |
| `m_csSearchCharItemPacket` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csSearchCharSkillPacket` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csSearchCustomPacket` | 1/1/1 | 2/2/2 | ja | ja |
| `m_csCharMovePacket` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csCharEditPacket` | 2/2/2 | 2/2/2 | ja | ja |
| `m_csBanPacket` | 2/2/2 | 10/10/10 | ja | ja |
| `m_csItemPacket` | 2/2/2 | 1/1/1 | ja | ja |
| `m_csServerInfoPacket` | 1/1/1 | 2/2/2 | ja | ja |
| `m_csTitlePacket` | 2/2/2 | 1/1/1 | ja | ja |

**m_csPacket** (15 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operator |
| 1 | `0x2` | INT32 | 1 | Admin ID |
| 2 | `0x4` | PACKET | 1 | Login |
| 3 | `0x8` | PACKET | 1 | Search |
| 4 | `0x10` | PACKET | 1 | Search - Character Data |
| 5 | `0x20` | PACKET | 1 | Edit - Character Data |
| 6 | `0x40` | PACKET | 1 | Search - Character Item |
| 7 | `0x80` | PACKET | 1 | Search - Character Skill |
| 8 | `0x100` | PACKET | 1 | Search - Character Party, Result   . |
| 9 | `0x200` | PACKET | 1 | Char Move |
| 10 | `0x400` | PACKET | 1 | Ban |
| 11 | `0x800` | PACKET | 1 | Help |
| 12 | `0x1000` | PACKET | 1 | Item |
| 13 | `0x2000` | PACKET | 1 | Server Info |
| 14 | `0x4000` | PACKET | 1 | Title |

**m_csLoginPacket** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | 1 : Login, 0 : Logout |
| 1 | `0x2` | INT32 | 1 | Admin ID |
| 2 | `0x4` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Game ID |
| 3 | `0x8` | INT16 | 1 | Admin Level |
| 4 | `0x10` | INT8 | 1 | Server ID |
| 5 | `0x20` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | AccName |

**m_csSearchPacket** (5 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Object Type |
| 1 | `0x2` | INT8 | 1 | Field |
| 2 | `0x4` | INT32 | 1 | Search (ID) |
| 3 | `0x8` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Game ID |
| 4 | `0x10` | PACKET | 1 | Search Result *   NULL   . |

**m_csSearchResultPacket** (12 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT16 | 1 | Total Result Num- 1 based |
| 1 | `0x2` | INT16 | 1 | Now Count - 1 based |
| 2 | `0x4` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Game ID |
| 3 | `0x8` | INT32 | 1 | CID |
| 4 | `0x10` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Acc Name |
| 5 | `0x20` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Guild ID |
| 6 | `0x40` | INT32 | 1 | TID |
| 7 | `0x80` | INT32 | 1 | Level |
| 8 | `0x100` | CHAR | AGPMADMIN_MAX_UT_STRING + 1 | UT |
| 9 | `0x200` | CHAR | AGPMADMIN_MAX_CREDATE_STRING + 1 | CreDate |
| 10 | `0x400` | CHAR | AGPMADMIN_MAX_IP_STRING + 1 | IP |
| 11 | `0x800` | INT32 | 1 | Status |

**m_csSearchCharDataPacket** (6 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | CID |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Char Name 2003.12.29. |
| 2 | `0x4` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Acc Name |
| 3 | `0x8` | UINT32 | 1 | Current Conntected TimeStamp |
| 4 | `0x10` | CHAR | AGPMADMIN_MAX_IP_STRING + 1 | IP |
| 5 | `0x20` | CHAR | AGPMADMIN_MAX_IP_STRING + 1 | Last IP |

**m_csSearchCharItemPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Char CID |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Char Name |
| 2 | `0x4` | INT8 | 1 | Position (Body, Bag, Board, Store...) |

**m_csSearchCharSkillPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Char CID |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Char Name |
| 2 | `0x4` | INT16 | 1 | Type (All, Mastery1, Mastery2, Mastery2... OR Skill Mastery Sub Type) |

**m_csSearchCustomPacket** (2 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Custom Type |
| 1 | `0x2` | MEMORY_BLOCK | 1 |     . |

**m_csCharMovePacket** (5 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Char Name |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Target Name ( NULL .     .) |
| 2 | `0x4` | FLOAT | 1 | x |
| 3 | `0x8` | FLOAT | 1 | y |
| 4 | `0x10` | FLOAT | 1 | z |

**m_csCharEditPacket** (2 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | MEMORY_BLOCK | 1 |  stAgpdAdminCharEdit  !!! |
| 1 | `0x2` | MEMORY_BLOCK | 1 | Skill 2006.05.04. |

**m_csBanPacket** (10 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Char Name |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | Acc Name |
| 2 | `0x4` | INT8 | 1 | Logout |
| 3 | `0x8` | INT8 | 1 | Ban Set Flag |
| 4 | `0x10` | INT32 | 1 | ChatBan Start Time |
| 5 | `0x20` | INT8 | 1 | ChatBan Keep Time |
| 6 | `0x40` | INT32 | 1 | CharBan Start Time |
| 7 | `0x80` | INT8 | 1 | CharBan Keep Time |
| 8 | `0x100` | INT32 | 1 | AccBan Start Time |
| 9 | `0x200` | INT8 | 1 | AccBan Keep Time |

**m_csItemPacket** (1 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | MEMORY_BLOCK | 1 |  stAgpdAdminItemOperation  !!! |

**m_csServerInfoPacket** (2 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPMADMIN_MAX_IP_STRING + 1 | Server IP |
| 1 | `0x2` | INT16 | 1 | Server Port |

**m_csTitlePacket** (1 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | MEMORY_BLOCK | 1 | stAgpdAdminTitleOperation |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `LOGIN` | `0x00556500` `OnOperationLogin` | `0`, `1` | 2017 ⊃ 2013 |
| 1 | `CONNECT` | inline | – | keine Callback-Ereignisse (beide) |
| 2 | `NUM_CURRENT_USER` | inline | – | keine Callback-Ereignisse (beide) |
| 3 | `SEARCH_CHARACTER` | inline | – | keine Callback-Ereignisse (beide) |
| 4 | `SEARCH_RESULT` | inline | – | keine Callback-Ereignisse (beide) |
| 5 | `SEARCH_CHARDATA` | inline | – | keine Callback-Ereignisse (beide) |
| 6 | `SEARCH_CHARITEM` | inline | – | keine Callback-Ereignisse (beide) |
| 7 | `SEARCH_CHARSKILL` | inline | – | keine Callback-Ereignisse (beide) |
| 8 | `SEARCH_CUSTOM` | inline | – | keine Callback-Ereignisse (beide) |
| 9 | `CHARMOVE` | inline | – | keine Callback-Ereignisse (beide) |
| 10 | `CHAREDIT` | inline | – | keine Callback-Ereignisse (beide) |
| 11 | `BAN` | inline | – | keine Callback-Ereignisse (beide) |
| 12 | `ITEM` | inline | – | keine Callback-Ereignisse (beide) |
| 13 | `SERVERINFO` | inline | – | keine Callback-Ereignisse (beide) |
| 14 | `GUILD` | inline | – | keine Callback-Ereignisse (beide) |
| 15 | `PING` | inline | – | keine Callback-Ereignisse (beide) |
| 16 | `USER_POSITION_ANSWER` | `0x005558C0` `OnOperationUserPositionStatistics` | `21` | 2017 ⊃ 2013 |
| 17 | `USER_POSITION_REQUEST` | `0x005558A0` `OnOperationUserPosition` | `20` | 2017 ⊃ 2013 |
| 18 | `ADMIN_CLIENT_LOGIN` | `0x00555A80` `OnOperationAdminClient` | `22` | 2017 ⊃ 2013 |
| 19 | `TITLE` | `0x00555B20` `FUN_00555b20` | `23` | 2017 ⊃ 2013 |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 9, gemeinsamer Rumpf: 27, nicht im Client: 34, ohne Kandidat: 19, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `OnOperationRemoveAdmin` | 36 | `0x00555BE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePingPacket` | 11 | `0x005559E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetAdminLevel` (`0x00555970`), `GetAdminLevel` (`0x00555970`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmAdmin`](AgcmAdmin.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md)
