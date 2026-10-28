# AgpmEventGacha (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventGacha` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventGacha` / `AgpmEventGacha.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00569B30` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `OP_*` kennt 4 Operationen, davon 4 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 4 Operationen liegen 2013er Ereignisse vor; 3 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 1 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 0 Paketdefinition(en) in der Quelle, 0 davon im 2017er Konstruktor (`0056a070`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| – | `AgpmEventGacha::StreamReadGachaTypeTable` | nicht gefunden (die frühere Zuordnung zu `0x00514430` war falsch: dort liegt [`ApmMap`](ApmMap.md):LoadTemplate`, siehe ApmMap-Bericht) |
| `0x00569620` | `AgpmEventGacha::CBStreamWriteEvent` | stage1 |
| `0x005697C0` | `AgpmEventGacha::CBStreamReadEvent` | stage1 |
| `0x00569960` | `AgpmEventGacha::CBAction` | stage1 |
| `0x00569A60` | `AgpmEventGacha::OnAddModule` | merged |
| `0x00569B30` | `AgpmEventGacha::OnReceive` | merged |
| `0x00569FE0` | `AgpmEventGacha::ctor_or_dtor_00569fe0` | merged |
| `0x0056A070` | `AgpmEventGacha::ctor_or_dtor_0056a070` | merged |
| `0x0056A1A0` | `AgpmEventGacha::~AgpmEventGacha` | merged |

9 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `REQUEST` | `0x0055C380` `FUN_0055c380` | – | 2017 ⊂ 2013 |
| 1 | `REQUESTGRANTED` | inline | `REQUESTGRANTED` | = (2013 = 2017) |
| 2 | `GACHA` | inline | `GACHA` | = (2013 = 2017) |
| 3 | `RESULT` | inline | `RESULT` | = (2013 = 2017) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 0 | `REQUEST` | CB_EV_REQUEST | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 7, ohne Kandidat: 1, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketEventGacha` | 34 | `0x00569550` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketEventRequest` | 33 | `0x00569480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmEventGacha`](AgcmEventGacha.md), [`AgpmBattleGround`](AgpmBattleGround.md), [`ApmMap`](ApmMap.md)
