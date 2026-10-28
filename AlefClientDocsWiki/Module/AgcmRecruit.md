# AgcmRecruit (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmRecruit` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmRecruit` / `AgcmRecruit.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x006EA460` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGPMRECRUIT_*` kennt 9 Operationen, davon 7 mit eigenem Case im 2017er Binary; ohne Case: `ADD_TO_RECRUIT` (0), `UPDATE_LFP` (7).
- **Vergleich mit 2013:** Die 2013er Berichte enthalten für dieses Modul keine Callback-Ereignisse je Operation; ein Abgleich ist nicht möglich.
- **Paketlayout:** 4 Paketdefinition(en) in der Quelle, 4 davon im 2017er Konstruktor (`006ea6c0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x006E9BE0` | `AgcmRecruit::ctor_or_dtor` | merged |
| `0x006E9C90` | `AgcmRecruit::OnAddModule` | merged |
| `0x006EA460` | `AgcmRecruit::OnReceive` | merged |
| `0x006EA520` | `AgcmRecruit::OnInit` | merged |
| `0x006EA6C0` | `AgcmRecruit::AgcmRecruit` | strmatch |
| `0x006EA8A0` | `AgcmRecruit::~AgcmRecruit` | merged |

6 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 7/7/7 | ja | ja |
| `m_csLFPInfo` | 1/1/1 | 6/6/6 | ja | ja |
| `m_csLFMInfo` | 2/2/2 | 10/10/10 | ja | ja |
| `m_csSearchInfo` | 1/1/1 | 4/4/4 | ja | ja |

**m_csPacket** (7 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation  |
| 1 | `0x2` | INT32 | 1 | lControlServerID |
| 2 | `0x4` | INT32 | 1 | lPlayerID |
| 3 | `0x8` | PACKET | 1 | LFPInfo <-   . |
| 4 | `0x10` | PACKET | 1 | LFMInfo <-    . |
| 5 | `0x20` | PACKET | 1 | SearchInfo |
| 6 | `0x40` | INT32 | 1 | lResult    Result |

**m_csLFPInfo** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | lTotalCount |
| 1 | `0x2` | INT32 | 1 | lIndex |
| 2 | `0x4` | INT32 | 1 | LV |
| 3 | `0x8` | INT32 | 1 | Class |
| 4 | `0x10` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | pstrPlayerID; |
| 5 | `0x20` | INT32 | 1 | lPlayerID |

**m_csLFMInfo** (10 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | lTotalCount |
| 1 | `0x2` | INT32 | 1 | lIndex |
| 2 | `0x4` | CHAR | 20 | Purpose |
| 3 | `0x8` | INT32 | 1 | lRequire Member |
| 4 | `0x10` | INT32 | 1 | Min LV |
| 5 | `0x20` | INT32 | 1 | Max LV |
| 6 | `0x40` | INT32 | 1 | LV |
| 7 | `0x80` | INT32 | 1 | Class |
| 8 | `0x100` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 | pstrLeaderID; |
| 9 | `0x200` | INT32 | 1 | lLeaderID |

**m_csSearchInfo** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 |    ? |
| 1 | `0x2` | INT32 | 1 | Level? |
| 2 | `0x4` | INT32 | 1 |   ? |
| 3 | `0x8` | INT32 | 1 | Class Bit Flag |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD_TO_RECRUIT` | – | – | kein Case (default) – wie 2013 |
| 1 | `REGISTER_LFP` | inline | – | keine Callback-Ereignisse (beide) |
| 2 | `CANCEL_LFP` | inline | – | keine Callback-Ereignisse (beide) |
| 3 | `SEARCH_LFP_BY_PAGE` | `0x006EA1C0` `FUN_006ea1c0` | – | keine Callback-Ereignisse (beide) |
| 4 | `REGISTER_LFM` | inline | – | keine Callback-Ereignisse (beide) |
| 5 | `CANCEL_LFM` | inline | – | keine Callback-Ereignisse (beide) |
| 6 | `SEARCH_LFM_BY_PAGE` | `0x006EA320` `FUN_006ea320` | – | keine Callback-Ereignisse (beide) |
| 7 | `UPDATE_LFP` | – | – | kein Case (default) – wie 2013 |
| 8 | `RESULT` | inline | – | keine Callback-Ereignisse (beide) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 5, nicht im Client: 13, ohne Kandidat: 2, zugeordnet: 5.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SendCancelFromLFP` | 47 | `0x006EA060` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendRegisterToLFM` | 51 | `0x006E9F00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendRegisterToLFP` | 47 | `0x006E9E20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessSearchLFPResult` | 62 | `0x006EA1C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ProcessSearchLFMResult` | 70 | `0x006EA320` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SendCancelFromLFM` (`0x006E9D30`), `SendSearchLFPByPage` (`0x006E9D30`), `SendSearchLFMByPage` (`0x006E9D30`).

<!-- LUECKENREGISTER-NACHTRAG-END -->
