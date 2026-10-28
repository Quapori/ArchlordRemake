# AgpmWantedCriminal (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmWantedCriminal` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmWantedCriminal` / `AgpmWantedCriminal.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0056BB60` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGPMWANTEDCRIMINAL_OPERATION_*` kennt 9 Operationen, davon 1 mit eigenem Case im 2017er Binary; ohne Case: `EVENT_GRANT` (1), `ARRANGE` (2), `REQ_LIST` (3), `RES_LIST` (4), `MY_RANK` (5), `UPDATE_KILLER` (6), `UPDATE_FLAG` (7), `NOTIFY` (8).
- **Vergleich mit 2013:** Für 9 Operationen liegen 2013er Ereignisse vor; 0 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`0056b6e0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056B6E0` | `AgpmWantedCriminal::ctor_or_dtor_0056b6e0` | merged |
| `0x0056B810` | `AgpmWantedCriminal::ctor_or_dtor_0056b810` | merged |
| `0x0056B890` | `AgpmWantedCriminal::OnInit` | merged |
| `0x0056BA60` | `AgpmWantedCriminal::CBEventAction` | stage1 |
| `0x0056BAD0` | `AgpmWantedCriminal::~AgpmWantedCriminal` | merged |
| `0x0056BAF0` | `AgpmWantedCriminal::OnDestroy` | merged |
| `0x0056BB60` | `AgpmWantedCriminal::OnReceive` | merged |
| `0x0056BBB0` | `AgpmWantedCriminal::ConAgpdWantedCriminalCAD` | stage1 |
| `0x0056BC10` | `AgpmWantedCriminal::DesAgpdWantedCriminalCAD` | stage1 |
| `0x0056BC90` | `AgpmWantedCriminal::OnAddModule` | merged |

10 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 6/6/6 | ja | ja |
| `m_csPacketWC` | 2/2/2 | 5/5/5 | ja | ja |

**m_csPacket** (6 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | cid |
| 2 | `0x4` | INT32 | 1 | page |
| 3 | `0x8` | INT32 | 1 | rank |
| 4 | `0x10` | INT32 | 1 | result |
| 5 | `0x20` | PACKET | 1 | embedded packet(wanted criminal) |

**m_csPacketWC** (5 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPDCHARACTER_NAME_LENGTH + 1 | char id |
| 1 | `0x2` | INT64 | 1 | bounty |
| 2 | `0x4` | INT32 | 1 | level |
| 3 | `0x8` | INT32 | 1 | class |
| 4 | `0x10` | INT32 | 1 | on/offline |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `EVENT_REQUEST` | inline | – | keine Callback-Ereignisse (beide) |
| 1 | `EVENT_GRANT` | – | – | kein Case |
| 2 | `ARRANGE` | – | – | kein Case |
| 3 | `REQ_LIST` | – | – | kein Case |
| 4 | `RES_LIST` | – | – | kein Case |
| 5 | `MY_RANK` | – | – | kein Case |
| 6 | `UPDATE_KILLER` | – | – | kein Case |
| 7 | `UPDATE_FLAG` | – | – | kein Case |
| 8 | `NOTIFY` | – | – | kein Case |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 4, gemeinsamer Rumpf: 9, nicht im Client: 9, ohne Kandidat: 3, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SetFinalAttacker` | 4 | `0x0056B950` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketEventRequest` | 20 | `0x0056C1C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `IsEnoughBounty` (`0x0056BD20`), `GetFinalAttacker` (`0x0056BC70`), `GetBaseBounty` (`0x0056BD20`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md)
