# AgpmSummons (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmSummons` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmSummons` / `AgpmSummons.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00585CF0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMSUMMONS_PACKET_*` kennt 5 Operationen, davon 5 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 5 Operationen liegen 2013er Ereignisse vor; 1 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 2 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`00583f90`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00583F90` | `AgpmSummons::ctor_or_dtor_00583f90` | merged |
| `0x00584090` | `AgpmSummons::ctor_or_dtor_00584090` | merged |
| `0x005840F0` | `AgpmSummons::OnInit` | merged |
| `0x00584560` | `AgpmSummons::~AgpmSummons` | merged |
| `0x00585610` | `AgpmSummons::ConAgpdSummonsADChar` | stage1 |
| `0x00585760` | `AgpmSummons::CBResetMonster` | stage1 |
| `0x00585860` | `AgpmSummons::DesAgpdSummonsADChar` | stage1 |
| `0x00585900` | `AgpmSummons::OnAddModule` | merged |
| `0x00585CF0` | `AgpmSummons::OnReceive` | merged |
| `0x00584580` | `AgpmSummons::OnReceiveSetMaxSummons` | casemap:AgpmSummons |
| `0x00584D80` | `AgpmSummons::OnReceiveSetPropensity` | casemap:AgpmSummons |
| `0x00585370` | `AgpmSummons::OnReceiveRemoveSummons` | casemap:AgpmSummons |
| `0x00585B90` | `AgpmSummons::OnReceiveNewSummons` | casemap:AgpmSummons |

13 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 9/9/9 | ja | ja |

**m_csPacket** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | Owner CID |
| 2 | `0x4` | INT32 | 1 | Summons CID |
| 3 | `0x8` | INT32 | 1 | Summons TID |
| 4 | `0x10` | INT8 | 1 | Summons Type |
| 5 | `0x20` | INT8 | 1 | Summons Propensity |
| 6 | `0x40` | UINT32 | 1 | Start Time |
| 7 | `0x80` | UINT32 | 1 | End Time |
| 8 | `0x100` | UINT8 | 1 | Force |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `NEW_SUMMONS` | `0x00585B90` `OnReceiveNewSummons` | `NEW_SUMMONS`, `SET_MAX_SUMMONS` | 2017 ⊃ 2013 |
| 1 | `REMOVE_SUMMONS` | `0x00585370` `OnReceiveRemoveSummons` | `REMOVE_SUMMONS`, `SET_MAX_SUMMONS` | 2017 ⊃ 2013 |
| 2 | `SET_PROPENSITY` | `0x00584D80` `OnReceiveSetPropensity` | `SET_PROPENSITY` | = (2013 = 2017) |
| 3 | `SET_MAX_SUMMONS` | `0x00584580` `OnReceiveSetMaxSummons` | `SET_MAX_SUMMONS` | 2017 ⊃ 2013 |
| 4 | `SET_MAX_TAME` | `0x005845E0` `FUN_005845e0` | `SET_MAX_TAME` | 2017 ⊃ 2013 |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 0 | `NEW_SUMMONS` | – | AGPMSUMMONS_CB_SET_MAX_SUMMONS |
| 1 | `REMOVE_SUMMONS` | – | AGPMSUMMONS_CB_SET_MAX_SUMMONS |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, gemeinsamer Rumpf: 8, nicht im Client: 18, ohne Kandidat: 16, zugeordnet: 6.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SetMaxSummonsCount` | 15 | `0x00584270` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsMySummons` | 18 | `0x00584C80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `NewFixed` | 57 | `0x00584AB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `NewTaming` | 58 | `0x005848E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `NewSummons` | 67 | `0x00585990` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetADCharacter` | 9 | `0x00584110` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SetOwnerAndLifeTime` (`0x00584470`), `GetOwnerCID` (`0x00584320`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUICharacter`](AgcmUICharacter.md)
