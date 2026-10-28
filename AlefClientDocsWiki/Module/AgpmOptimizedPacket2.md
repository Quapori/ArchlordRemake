# AgpmOptimizedPacket2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmOptimizedPacket2` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmOptimizedPacket2` / `AgpmOptimizedPacket2.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0057DA80` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGPMOPTIMIZEDVIEW_PACKET_*` kennt 1 Operationen, davon 0 mit eigenem Case im 2017er Binary; ohne Case: `AGSMGUILD_PACKET_TYPE` (0).
- **Vergleich mit 2013:** Die 2013er Berichte enthalten für dieses Modul keine Callback-Ereignisse je Operation; ein Abgleich ist nicht möglich.
- **Paketlayout:** 5 Paketdefinition(en) in der Quelle, 5 davon im 2017er Konstruktor (`0057c540`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0057C910` | `AgpmOptimizedPacket2::OnInit` | merged |
| `0x0057C940` | `AgpmOptimizedPacket2::OnAddModule` | merged |
| `0x0057D3E0` | `AgpmOptimizedPacket2::~AgpmOptimizedPacket2` | merged |
| `0x0057DA80` | `AgpmOptimizedPacket2::OnReceive` | merged |

4 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 14/14/14 | ja | ja |
| `m_csPacketCharView` | 4/4/4 | 25/25/25 | ja | ja |
| `m_csPacketItemView` | 4/4/4 | 20/20/20 | ja | ja |
| `m_csPacketCharMove` | 1/1/1 | 9/9/9 | ja | ja |
| `m_csPacketCharAction` | 2/2/2 | 9/9/9 | ja | ja |

**m_csPacket** (14 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | PACKET | 1 | character packet |
| 2 | `0x4` | PACKET | AGPMITEM_PART_NUM | item packet |
| 3 | `0x8` | MEMORY_BLOCK | 1 | buffed skill packet (structure memory copy) |
| 4 | `0x10` | MEMORY_BLOCK | 1 | event packet |
| 5 | `0x20` | CHAR | AGPMGUILD_MAX_GUILD_ID_LENGTH + 1 | Guild ID |
| 6 | `0x40` | MEMORY_BLOCK | 1 | character all item packet |
| 7 | `0x80` | MEMORY_BLOCK | 1 | character all item convert packet |
| 8 | `0x100` | MEMORY_BLOCK | 1 | character all skill packet |
| 9 | `0x200` | INT32 | 1 | character id |
| 10 | `0x400` | INT32 | 1 | GuildMarkTID//2005.10.24. By SungHoon |
| 11 | `0x800` | INT32 | 1 | GuildMarkColor//2005.10.24. By SungHoon |
| 12 | `0x1000` | INT32 | 1 | IsWinner |
| 13 | `0x2000` | MEMORY_BLOCK | 1 | title |

**m_csPacketCharView** (25 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | character id |
| 1 | `0x2` | INT32 | 1 | character tid |
| 2 | `0x4` | MEMORY_BLOCK | 1 | character name |
| 3 | `0x8` | INT8 | 1 | current action status |
| 4 | `0x10` | INT8 | 1 | IsNewCharacter |
| 5 | `0x20` | PACKET | 1 | factor packet |
| 6 | `0x40` | INT8 | 1 | move flag |
| 7 | `0x80` | INT8 | 1 | move direction |
| 8 | `0x100` | POS | 1 | character current pos |
| 9 | `0x200` | POS | 1 | destination pos |
| 10 | `0x400` | INT32 | 1 | follow target id |
| 11 | `0x800` | UINT16 | 1 | follow distance |
| 12 | `0x1000` | INT16 | 1 | turn x |
| 13 | `0x2000` | INT16 | 1 | turn y |
| 14 | `0x4000` | UINT64 | 1 | character special status |
| 15 | `0x8000` | INT8 | 1 | is transform status, is ridable |
| 16 | `0x10000` | INT8 | 1 | face index |
| 17 | `0x20000` | INT8 | 1 | hair index |
| 18 | `0x40000` | INT8 | 1 | view options |
| 19 | `0x80000` | UINT16 | 1 | bit flag option |
| 20 | `0x100000` | INT8 | 1 | character criminal status |
| 21 | `0x200000` | INT32 | 1 | wanted criminal flag |
| 22 | `0x400000` | CHAR | AGPACHARACTER_MAX_CHARACTER_NICKNAME | nick name |
| 23 | `0x800000` | INT32 | 1 | npc   . |
| 24 | `0x1000000` | INT32 | 1 | npc ,   .. |

**m_csPacketItemView** (20 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | item id |
| 1 | `0x2` | INT32 | 1 | item template id |
| 2 | `0x4` | INT16 | 1 | stack count |
| 3 | `0x8` | INT8 | 1 | convert packet |
| 4 | `0x10` | INT8 | 1 | # of physical convert |
| 5 | `0x20` | INT8 | 1 | # of socket |
| 6 | `0x40` | INT32 | 1 | # of converted socket |
| 7 | `0x80` | INT32 | 1 | converted socket item template id 1 |
| 8 | `0x100` | INT32 | 1 | converted socket item template id 2 |
| 9 | `0x200` | INT32 | 1 | converted socket item template id 3 |
| 10 | `0x400` | INT32 | 1 | converted socket item template id 4 |
| 11 | `0x800` | INT32 | 1 | converted socket item template id 5 |
| 12 | `0x1000` | INT32 | 1 | converted socket item template id 6 |
| 13 | `0x2000` | INT32 | 1 | converted socket item template id 7 |
| 14 | `0x4000` | INT32 | 1 | converted socket item template id 8 |
| 15 | `0x8000` | UINT16 | 1 | item status flag |
| 16 | `0x10000` | UINT16 | 1 | option tid 1 |
| 17 | `0x20000` | UINT16 | 1 | option tid 2 |
| 18 | `0x40000` | UINT16 | 1 | option tid 3 |
| 19 | `0x80000` | UINT16 | 1 | option tid 4 |

**m_csPacketCharMove** (9 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | character id |
| 1 | `0x2` | POS | 1 | AUTYPE_POS,1,// current position |
| 2 | `0x4` | POS | 1 | current position |
| 3 | `0x8` | INT32 | 1 | destination position |
| 4 | `0x10` | UINT16 | 1 | follow target |
| 5 | `0x20` | INT8 | 1 | follow distance |
| 6 | `0x40` | INT8 | 1 | move flag |
| 7 | `0x80` | INT8 | 1 | move direction |
| 8 | `0x100` | INT32 | 1 | next action type |

**m_csPacketCharAction** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | action character id |
| 1 | `0x2` | INT32 | 1 | target character id |
| 2 | `0x4` | INT8 | 1 | attack result |
| 3 | `0x8` | PACKET | 1 | factor packet |
| 4 | `0x10` | INT32 | 1 | target hp |
| 5 | `0x20` | INT8 | 1 | AUTYPE_POS,1,// action position |
| 6 | `0x40` | INT8 | 1 | combo info |
| 7 | `0x80` | UINT32 | 1 | force attack |
| 8 | `0x100` | UINT8 | 1 | Additional Effect |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `AGSMGUILD_PACKET_TYPE` | – | – | kein Case (default) – wie 2013 |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 4, nicht im Client: 9, ohne Kandidat: 14, zugeordnet: 7.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketCharMove` | 33 | `0x0057D2E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessItemPacket` | 111 | `0x0057D400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessCharacterPacket` | 131 | `0x0057CD80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnReceiveCharAction` | 74 | `0x0057D7A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnReceiveCharView` | 100 | `0x0057CBF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCharAction` | 23 | `0x0057D350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnReceiveCharMove` | 63 | `0x0057CA50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmSkill`](AgcmSkill.md)
