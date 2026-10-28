# AgpmMailBox (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmMailBox` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmMailBox` / `AgpmMailBox.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x005585E0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMMAILBOX_OPERATION_*` kennt 6 Operationen, davon 6 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 5 Operationen liegen 2013er Ereignisse vor; 4 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 1 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`005579c0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00528920` | `AgpmMailBox::OnInit` | merged |
| `0x005579C0` | `AgpmMailBox::ctor_or_dtor_005579c0` | merged |
| `0x00557B20` | `AgpmMailBox::ctor_or_dtor_00557b20` | merged |
| `0x00557BA0` | `AgpmMailBox::OnDestroy` | merged |
| `0x00557FE0` | `AgpmMailBox::~AgpmMailBox` | merged |
| `0x00558000` | `AgpmMailBox::ConAgpdMailCAD` | stage1 |
| `0x00558070` | `AgpmMailBox::DesAgpdMailCAD` | stage1 |
| `0x00558530` | `AgpmMailBox::OnAddModule` | merged |
| `0x005585E0` | `AgpmMailBox::OnReceive` | merged |
| `0x00557900` | `AgpmMailBox::ParsePacketMail` | casemap:AgpmMailBox |
| `0x00557C00` | `AgpmMailBox::CreateMail` | casemap:AgpmMailBox |
| `0x00558210` | `AgpmMailBox::RemoveAllMail` | casemap:AgpmMailBox |

12 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 5/5/5 | ja | ja |
| `m_csPacketMail` | 2/2/2 | 9/9/9 | ja | ja |

**m_csPacket** (5 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | cid |
| 2 | `0x4` | PACKET | 1 | embedded packet(Mail) |
| 3 | `0x8` | INT32 | 1 | item id(write only) |
| 4 | `0x10` | INT32 | 1 | result |

**m_csPacketMail** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | mail id |
| 1 | `0x2` | CHAR | AGPDCHARACTER_NAME_LENGTH + 1 | from charid |
| 2 | `0x4` | CHAR | AGPDCHARACTER_NAME_LENGTH + 1 | to charid |
| 3 | `0x8` | CHAR | AGPMMAILBOX_MAX_SUBJECT_LENGTH + 1 | subject |
| 4 | `0x10` | INT32 | 1 | date(time_t) |
| 5 | `0x20` | INT32 | 1 | flag |
| 6 | `0x40` | INT32 | 1 | item tid |
| 7 | `0x80` | INT16 | 1 | item qty |
| 8 | `0x100` | MEMORY_BLOCK | 1 | content |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD_MAIL` | `0x00557C00` `CreateMail` | – | 2017 ⊂ 2013 |
| 1 | `REMOVE_MAIL` | `0x00557900` `ParsePacketMail` | `REMOVE_MAIL` | = (2013 = 2017) |
| 2 | `READ_MAIL` | `0x00557900` `ParsePacketMail` | `READ_MAIL` | = (2013 = 2017) |
| 3 | `WRITE_MAIL` | `0x00557900` `ParsePacketMail` | `WRITE_MAIL` | = (2013 = 2017) |
| 4 | `ITEM_SAVE` | `0x00557900` `ParsePacketMail` | `ITEM_SAVE` | = (2013 = 2017) |
| 5 | `REMOVE_ALL_MAIL` | `0x00558210` `RemoveAllMail` | – | keine Callback-Ereignisse (beide) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 0 | `ADD_MAIL` | AGPMMAILBOX_CB_ADD_MAIL | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, gemeinsamer Rumpf: 5, nicht im Client: 5, ohne Kandidat: 2, zugeordnet: 5.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsValidAttachItem` | 54 | `0x00558380` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketMail` | 39 | `0x00557D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketMailOnlyID` | 18 | `0x00557E40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetLetterCount` | 32 | `0x00557C80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCAD` | 5 | `0x00557C50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIMailBox`](AgcmUIMailBox.md)
