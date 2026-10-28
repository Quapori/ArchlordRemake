# AgpmTax (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmTax` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmTax` / `AgpmTax.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x005789E0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMTAX_OPERATION_*` kennt 5 Operationen, davon 5 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 4 Operationen liegen 2013er Ereignisse vor; 0 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 4 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 3 Paketdefinition(en) in der Quelle, 3 davon im 2017er Konstruktor (`00578830`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00577BC0` | `AgpmTax::CBEventAction` | stage1 |
| `0x00578200` | `AgpmTax::CBGetTaxRatio` | stage1 |
| `0x00578290` | `AgpmTax::OnAddModule` | merged |
| `0x00578350` | `AgpmTax::ctor_or_dtor_00578350` | merged |
| `0x00578830` | `AgpmTax::ctor_or_dtor_00578830` | merged |
| `0x005789C0` | `AgpmTax::~AgpmTax` | merged |
| `0x005789E0` | `AgpmTax::OnReceive` | merged |
| `0x00577F10` | `AgpmTax::Reset` | casemap:AgpmTax |
| `0x005785D0` | `AgpmTax::Reset` | casemap:AgpmTax |

9 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 8/8/8 | ja | ja |
| `m_csPacketCastleTax` | 2/2/2 | 4/4/4 | ja | ja |
| `m_csPacketRegionTax` | 2/2/2 | 3/3/3 | ja | ja |

**m_csPacket** (8 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | cid |
| 2 | `0x4` | INT32 | 1 | result |
| 3 | `0x8` | PACKET | 1 | embedded packet, castle tax or event |
| 4 | `0x10` | PACKET | 1 | embedded packet, region tax 1 |
| 5 | `0x20` | PACKET | 1 | embedded packet, region tax 2 |
| 6 | `0x40` | PACKET | 1 | embedded packet, region tax 3 |
| 7 | `0x80` | PACKET | 1 | embedded packet, region tax 4 |

**m_csPacketCastleTax** (4 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | AGPMSIEGEWAR_MAX_CASTLE_NAME | castle |
| 1 | `0x2` | INT64 | 1 | total income |
| 2 | `0x4` | UINT32 | 1 | latest transfer date |
| 3 | `0x8` | UINT32 | 1 | latest modify date |

**m_csPacketRegionTax** (3 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | CHAR | 32 + 1 | region |
| 1 | `0x2` | INT64 | 1 | income |
| 2 | `0x4` | INT32 | 1 | ratio |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `EVENT_REQUEST` | inline | – | 2017 ⊂ 2013 |
| 1 | `EVENT_GRANT` | inline | – | 2017 ⊂ 2013 |
| 2 | `MODIFY_RATIO` | `0x00577F10` `Reset` | – | 2017 ⊂ 2013 |
| 3 | `INQUIRE_TAX` | `0x00577F10` `Reset` | – | 2017 ⊂ 2013 |
| 4 | `NOTIFY_RATIO` | `0x005785D0` `Reset` | – | keine Callback-Ereignisse (beide) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 0 | `EVENT_REQUEST` | AGPMTAX_CB_EVENT_REQUEST | – |
| 1 | `EVENT_GRANT` | AGPMTAX_CB_EVENT_GRANT | – |
| 2 | `MODIFY_RATIO` | AGPMTAX_CB_INQUIRE_TAX, AGPMTAX_CB_MODIFY_RATIO | – |
| 3 | `INQUIRE_TAX` | AGPMTAX_CB_INQUIRE_TAX, AGPMTAX_CB_MODIFY_RATIO | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 6, eingebaut: 1, gemeinsamer Rumpf: 4, nicht im Client: 4, ohne Kandidat: 5, zugeordnet: 5.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsCastleOwner` | 12 | `0x00577DF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCastle` | 9 | `0x00577DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetRegion` | 10 | `0x00577A00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketEventRequest` | 22 | `0x00578FC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOperationEventRequest` | 28 | `0x005778D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetTax` (`0x00578070`), `GetTax` (`0x00578070`), `GetTax` (`0x00578070`), `GetRegionTax` (`0x00578070`), `ParseCastleTax` (`0x00577AD0`), `ParseRegionTax` (`0x00577AD0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUITax`](AgcmUITax.md)
