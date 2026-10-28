# AgpmUIStatus (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmUIStatus` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmUIStatus` / `AgpmUIStatus.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0057E220` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMUISTATUS_PACKET_OPERATION_*` kennt 4 Operationen, davon 4 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 4 Operationen liegen 2013er Ereignisse vor; 4 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0057dad0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0057DAD0` | `AgpmUIStatus::ctor_or_dtor_0057dad0` | merged |
| `0x0057DBB0` | `AgpmUIStatus::ctor_or_dtor_0057dbb0` | merged |
| `0x0057DE90` | `AgpmUIStatus::~AgpmUIStatus` | merged |
| `0x0057DEB0` | `AgpmUIStatus::ConAgpdUIStatusADChar` | stage1 |
| `0x0057DF20` | `AgpmUIStatus::DesAgpdUIStatusADChar` | stage1 |
| `0x0057E180` | `AgpmUIStatus::OnAddModule` | merged |
| `0x0057E220` | `AgpmUIStatus::OnReceive` | merged |
| `0x0057DDE0` | `AgpmUIStatus::OnOperationEncodedString` | casemap:AgpmUIStatus |
| `0x0057DF90` | `AgpmUIStatus::OnOperationAdd` | casemap:AgpmUIStatus |
| `0x0057E060` | `AgpmUIStatus::OnOperationUpdate` | casemap:AgpmUIStatus |

10 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 12/12/12 | ja | ja |

**m_csPacket** (12 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | character id |
| 2 | `0x4` | PACKET | AGPMUISTATUS_MAX_QUICKBELT_LAYER * AGPMUISTATUS_MAX_QUICKBELT_COLUMN | whole QBelt Item Information |
| 3 | `0x8` | INT8 | 1 | Quick Belt Grid Base |
| 4 | `0x10` | PACKET | 1 | update QBelt Item |
| 5 | `0x20` | MEMORY_BLOCK | 1 | QBelt Index |
| 6 | `0x40` | INT32 | 1 | Updated Item Packet |
| 7 | `0x80` | INT32 | 1 | Encoded QBelt Information (Type String) |
| 8 | `0x100` | INT8 | 1 | HP Potion TID |
| 9 | `0x200` | INT8 | 1 | MP Potion TID |
| 10 | `0x400` | INT8 | 1 | view helmet option value |
| 11 | `0x800` | MEMORY_BLOCK | 1 | auto use hp gage |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | `0x0057DF90` `OnOperationAdd` | `ADD_QUICKBELT_INFORMATION` | = (2013 = 2017) |
| 1 | `UPDATE_ITEM` | `0x0057E060` `OnOperationUpdate` | `UPDATE_QUICKBELT_ITEM` | = (2013 = 2017) |
| 2 | `ENCODED_STRING` | `0x0057DDE0` `OnOperationEncodedString` | `RECEIVED_ENCODED_QUICKBELT_STRING` | = (2013 = 2017) |
| 3 | `UPDATE_VIEW_HELMET_OPTION` | `0x0057DE40` `FUN_0057de40` | `UPDATE_VIEW_HELMET_OPTION` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 6, nicht im Client: 4, ohne Kandidat: 1, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketUpdateViewHelmetOption` | 19 | `0x0057DD80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketUpdateQuickBeltItem` | 44 | `0x0057DC40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 5 | `0x0057DC10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIStatus`](AgcmUIStatus.md)
