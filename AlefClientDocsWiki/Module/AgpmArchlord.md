# AgpmArchlord (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmArchlord` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmArchlord` / `AgpmArchlord.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0057BAB0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMARCHLORD_OPERATION_*` kennt 10 Operationen, davon 10 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 8 Operationen liegen 2013er Ereignisse vor; 8 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0057b940`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0057B680` | `AgpmArchlord::ctor_or_dtor_0057b680` | merged |
| `0x0057B760` | `AgpmArchlord::CBEventAction` | stage1 |
| `0x0057B7D0` | `AgpmArchlord::~AgpmArchlord` | merged |
| `0x0057B900` | `AgpmArchlord::CBIsArchlord` | stage1 |
| `0x0057B940` | `AgpmArchlord::ctor_or_dtor_0057b940` | merged |
| `0x0057BA30` | `AgpmArchlord::OnAddModule` | merged |
| `0x0057BAB0` | `AgpmArchlord::OnReceive` | merged |
| `0x0057B840` | `AgpmArchlord::SetArchlord` | casemap:AgpmArchlord |
| `0x0057B8C0` | `AgpmArchlord::CancelArchlord` | casemap:AgpmArchlord |

9 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 8/8/8 | ja | ja |

**m_csPacket** (8 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | CHAR | AGPACHARACTER_MAX_CHARACTER_TITLE | archlord name |
| 2 | `0x4` | CHAR | AGPACHARACTER_MAX_CHARACTER_TITLE | guard name |
| 3 | `0x8` | INT8 | 1 | set guard result |
| 4 | `0x10` | INT32 | 1 | current step |
| 5 | `0x20` | INT32 | 1 | count of current guard |
| 6 | `0x40` | INT32 | 1 | count of max guard |
| 7 | `0x80` | INT32 | 1 | message id |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `SET_ARCHLORD` | `0x0057B840` `SetArchlord` | `OPERATION_SET_ARCHLORD`, `SET_ARCHLORD` | = (2013 = 2017) |
| 1 | `CANCEL_ARCHLORD` | `0x0057B8C0` `CancelArchlord` | `CANCEL_ARCHLORD`, `OPERATION_CANCEL_ARCHLORD` | = (2013 = 2017) |
| 2 | `SET_GUARD` | inline | `OPERATION_SET_GUARD` | = (2013 = 2017) |
| 3 | `CANCEL_GUARD` | inline | `OPERATION_CANCEL_GUARD` | = (2013 = 2017) |
| 4 | `GUARD_INFO` | inline | `OPERATION_GUARD_INFO` | = (2013 = 2017) |
| 5 | `STEP` | inline | `OPERATION_CURRENT_STEP` | = (2013 = 2017) |
| 6 | `MESSAGE_ID` | inline | `OPERATION_MESSAGE_ID` | = (2013 = 2017) |
| 7 | `EVENT_REQUEST` | inline | – | keine Callback-Ereignisse (beide) |
| 8 | `EVENT_GRANT` | inline | – | keine Callback-Ereignisse (beide) |
| 9 | `NOTICE_NEW_ARCHLORD` | inline | `NOTICE_NEW_ARCHLORD` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 2, gemeinsamer Rumpf: 15, nicht im Client: 9, ohne Kandidat: 2, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketEventRequest` | 25 | `0x0057B6F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `IsArchlord` (`0x0057B880`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmArchlord`](AgcmArchlord.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgcmUIArchlord`](AgcmUIArchlord.md), [`AgcmUITax`](AgcmUITax.md)
