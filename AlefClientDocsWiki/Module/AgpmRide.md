# AgpmRide (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmRide` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmRide` / `AgpmRide.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0057A740` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMRIDE_OPERATION_*` kennt 7 Operationen, davon 6 mit eigenem Case im 2017er Binary; ohne Case: `NONE` (0).
- **Vergleich mit 2013:** Für 6 Operationen liegen 2013er Ereignisse vor; 6 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0057a5a0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0057A5A0` | `AgpmRide::ctor_or_dtor_0057a5a0` | merged |
| `0x0057A680` | `AgpmRide::ctor_or_dtor_0057a680` | merged |
| `0x0057A6E0` | `AgpmRide::OnAddModule` | merged |
| `0x0057A740` | `AgpmRide::OnReceive` | merged |
| `0x0057A860` | `AgpmRide::~AgpmRide` | merged |

5 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 4/4/4 | ja | ja |

**m_csPacket** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | Character ID |
| 2 | `0x4` | INT32 | 1 | Item ID (Ride Item) |
| 3 | `0x8` | INT32 | 1 | Remain Time (sec) |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `NONE` | – | – | kein Case (default) – wie 2013 |
| 1 | `RIDE_REQ` | inline | `RIDE_REQ` | = (2013 = 2017) |
| 2 | `RIDE_ACK` | inline | `RIDE_ACK` | = (2013 = 2017) |
| 3 | `DISMOUNT_REQ` | inline | `DISMOUNT_REQ` | = (2013 = 2017) |
| 4 | `DISMOUNT_ACK` | inline | `DISMOUNT_ACK` | = (2013 = 2017) |
| 5 | `TIMEOUT` | inline | `TIMEOUT` | = (2013 = 2017) |
| 6 | `RIDE_TID` | inline | `RIDE_TID` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 8, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmRide`](AgcmRide.md)
