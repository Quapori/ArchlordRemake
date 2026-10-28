# AgpmStartupEncryption (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmStartupEncryption` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmStartupEncryption` / `AgpmStartupEncryption.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0056C9E0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMSTARTUPENCRYPTION_PACKET_*` kennt 7 Operationen, davon 7 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 7 Operationen liegen 2013er Ereignisse vor; 7 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0056c660`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056C660` | `AgpmStartupEncryption::ctor_or_dtor_0056c660` | merged |
| `0x0056C730` | `AgpmStartupEncryption::ctor_or_dtor_0056c730` | merged |
| `0x0056C9C0` | `AgpmStartupEncryption::~AgpmStartupEncryption` | merged |
| `0x0056C9E0` | `AgpmStartupEncryption::OnReceive` | merged |
| `0x0056C7E0` | `AgpmStartupEncryption::OnReceiveRequestPublic` | casemap:AgpmStartupEncryption |
| `0x0056C800` | `AgpmStartupEncryption::OnReceivePublic` | casemap:AgpmStartupEncryption |
| `0x0056C850` | `AgpmStartupEncryption::OnReceiveMakePrivate` | casemap:AgpmStartupEncryption |
| `0x0056C8A0` | `AgpmStartupEncryption::OnReceiveComplete` | casemap:AgpmStartupEncryption |
| `0x0056C8C0` | `AgpmStartupEncryption::OnReceiveDynCodePublic` | casemap:AgpmStartupEncryption |
| `0x0056C910` | `AgpmStartupEncryption::OnReceiveDynCodePrivate` | casemap:AgpmStartupEncryption |

10 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 2/2/2 | ja | ja |

**m_csPacket** (2 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | MEMORY_BLOCK | 1 | Data |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `REQUEST_PUBLIC` | `0x0056C7E0` `OnReceiveRequestPublic` | `REQUEST_PUBLIC` | = (2013 = 2017) |
| 1 | `PUBLIC` | `0x0056C800` `OnReceivePublic` | `PUBLIC` | = (2013 = 2017) |
| 2 | `MAKE_PRIVATE` | `0x0056C850` `OnReceiveMakePrivate` | `MAKE_PRIVATE` | = (2013 = 2017) |
| 3 | `COMPLETE` | `0x0056C8A0` `OnReceiveComplete` | `COMPLETE` | = (2013 = 2017) |
| 4 | `DYNCODE_PUBLIC` | `0x0056C8C0` `OnReceiveDynCodePublic` | `DYNCODE_PUBLIC` | = (2013 = 2017) |
| 5 | `DYNCODE_PRIVATE` | `0x0056C910` `OnReceiveDynCodePrivate` | `DYNCODE_PRIVATE` | = (2013 = 2017) |
| 6 | `ALGORITHM_TYPE` | `0x0056C790` `FUN_0056c790` | `ALGORITHM_TYPE` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 9, nicht als eigene Funktion: 1, nicht im Client: 1, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakeStartupPacket` | 9 | `0x0056C960` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmStartupEncryption`](AgcmStartupEncryption.md)
