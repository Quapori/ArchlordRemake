# AgpmEventSiegeWarNPC (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventSiegeWarNPC` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventSiegeWarNPC` / `AgpmEventSiegeWarNPC.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00579160` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGPMEVENTSIEGEWAR_EVENT_*` kennt 2 Operationen, davon 2 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 2 Operationen liegen 2013er Ereignisse vor; 2 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`00578d10`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00578D10` | `AgpmEventSiegeWarNPC::ctor_or_dtor_00578d10` | merged |
| `0x00578DE0` | `AgpmEventSiegeWarNPC::ctor_or_dtor_00578de0` | merged |
| `0x00578F60` | `AgpmEventSiegeWarNPC::CBActionSiegeWar` | stage1 |
| `0x005790B0` | `AgpmEventSiegeWarNPC::~AgpmEventSiegeWarNPC` | merged |
| `0x005790D0` | `AgpmEventSiegeWarNPC::OnAddModule` | merged |
| `0x00579160` | `AgpmEventSiegeWarNPC::OnReceive` | merged |
| `0x00578E50` | `AgpmEventSiegeWarNPC::OnOperationEventRequest` | casemap:AgpmEventSiegeWarNPC |
| `0x00578F40` | `AgpmEventSiegeWarNPC::OnOperationEventGrant` | casemap:AgpmEventSiegeWarNPC |

8 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 3/3/3 | ja | ja |

**m_csPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | PACKET | 1 | event base packet |
| 2 | `0x4` | INT32 | 1 | Character ID |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 1 | `REQUEST` | `0x00578E50` `OnOperationEventRequest` | `EVENT_GRANT` | = (2013 = 2017) |
| 2 | `GRANT` | `0x00578F40` `OnOperationEventGrant` | `EVENT_GRANT` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, nicht im Client: 1, ohne Kandidat: 1, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `MakePacketEventRequest` | 20 | `0x00577B50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventSiegeWarNPC`](AgcmEventSiegeWarNPC.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md)
