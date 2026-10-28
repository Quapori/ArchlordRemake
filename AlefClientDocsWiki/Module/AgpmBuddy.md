# AgpmBuddy (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmBuddy` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmBuddy` / `AgpmBuddy.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0056D1C0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMBUDDY_OPERATION_*` kennt 15 Operationen, davon 14 mit eigenem Case im 2017er Binary; ohne Case: `NONE` (0).
- **Vergleich mit 2013:** Für 11 Operationen liegen 2013er Ereignisse vor; 11 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0056cb40`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056CB40` | `AgpmBuddy::ctor_or_dtor_0056cb40` | merged |
| `0x0056CC40` | `AgpmBuddy::ctor_or_dtor_0056cc40` | merged |
| `0x0056CD20` | `AgpmBuddy::~AgpmBuddy` | merged |
| `0x0056CD40` | `AgpmBuddy::AgpdBuddyDestructor` | stage1 |
| `0x0056D1C0` | `AgpmBuddy::OnReceive` | merged |
| `0x0056D820` | `AgpmBuddy::AgpdBuddyConstructor` | stage1 |
| `0x0056D870` | `AgpmBuddy::OnAddModule` | merged |

7 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 4/4/4 | 7/7/7 | ja | ja |

**m_csPacket** (7 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | CID |
| 2 | `0x4` | CHAR | AGPDCHARACTER_NAME_LENGTH + 1 | Buddy Name |
| 3 | `0x8` | UINT32 | 1 | Options -> Online  . |
| 4 | `0x10` | INT32 | 1 | Region Index |
| 5 | `0x20` | INT32 | 1 | Mentor Status |
| 6 | `0x40` | INT32 | 1 | message code |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `NONE` | – | – | kein Case (default) – wie 2013 |
| 1 | `ADD` | inline | `ADD` | = (2013 = 2017) |
| 2 | `ADD_REQUEST` | inline | `ADD_REQUEST` | = (2013 = 2017) |
| 3 | `ADD_REJECT` | inline | `ADD_REJECT` | = (2013 = 2017) |
| 4 | `REMOVE` | inline | `REMOVE` | = (2013 = 2017) |
| 5 | `OPTIONS` | inline | `OPTIONS` | = (2013 = 2017) |
| 6 | `ONLINE` | inline | – | keine Callback-Ereignisse (beide) |
| 7 | `REGION` | inline | `REGION` | = (2013 = 2017) |
| 8 | `MSG_CODE` | inline | – | keine Callback-Ereignisse (beide) |
| 9 | `INIT_END` | inline | – | keine Callback-Ereignisse (beide) |
| 10 | `MENTOR_REQUEST` | inline | `MENTOR_REQUEST` | = (2013 = 2017) |
| 11 | `MENTOR_DELETE` | inline | `MENTOR_DELETE` | = (2013 = 2017) |
| 12 | `AGPMBUDDY_OPRRATION_MENTOR_REQUEST_ACCEPT` | inline | `MENTOR_REQUEST_ACCEPT` | = (2013 = 2017) |
| 13 | `AGPMBUDDY_OPRRATION_MENTOR_REQUEST_REJECT` | inline | `MENTOR_REQUEST_REJECT` | = (2013 = 2017) |
| 14 | `AGPMBUDDY_OPRRATION_MENTOR_UI_OPEN` | inline | `MENTOR_UI_OPEN` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 11, gemeinsamer Rumpf: 17, nicht im Client: 12, ohne Kandidat: 8, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsExistBuddy` | 26 | `0x0056D5D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MentorBuddy` | 18 | `0x0056D730` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetMentorStatus` (`0x0056CCA0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIBuddy`](AgcmUIBuddy.md)
