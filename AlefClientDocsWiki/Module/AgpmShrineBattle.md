# AgpmShrineBattle (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmShrineBattle` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmShrineBattle` / `AgpmShrineBattle.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0056AC90` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMSHRINEBATTLE_PACKET_SHRINEPOINT_*` kennt 13 Operationen, davon 13 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Die 2013er Berichte enthalten für dieses Modul keine Callback-Ereignisse je Operation; ein Abgleich ist nicht möglich.
- **Paketlayout:** 0 Paketdefinition(en) in der Quelle, 0 davon im 2017er Konstruktor (`None`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056A840` | `AgpmShrineBattle::OnInit` | merged |
| `0x0056AC90` | `AgpmShrineBattle::OnReceive` | merged |
| `0x0056AFB0` | `AgpmShrineBattle::ctor_or_dtor_0056afb0` | merged |
| `0x0056B040` | `AgpmShrineBattle::ctor_or_dtor_0056b040` | merged |
| `0x0056B110` | `AgpmShrineBattle::~AgpmShrineBattle` | merged |
| `0x0056A8A0` | `AgpmShrineBattle::OnProcessShrinePointInformation` | casemap:AgpmShrineBattle |
| `0x0056AA00` | `AgpmShrineBattle::OnProcessShrinePointInformationTotal` | casemap:AgpmShrineBattle |

7 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `INFORMATION_REQUEST` | inline | `0` | 2017 ⊃ 2013 |
| 1 | `INFORMATION` | `0x0056A8A0` `OnProcessShrinePointInformation` | `1` | 2017 ⊃ 2013 |
| 2 | `INFORMATION_TOTAL` | `0x0056AA00` `OnProcessShrinePointInformationTotal` | `2` | 2017 ⊃ 2013 |
| 3 | `TIMEBAR_STATE` | inline | `3` | 2017 ⊃ 2013 |
| 4 | `STATUS_UPDATE` | inline | `4` | 2017 ⊃ 2013 |
| 5 | `TRYIMPRINT` | inline | `5` | 2017 ⊃ 2013 |
| 6 | `IMPRINT_RESULT` | inline | `6` | 2017 ⊃ 2013 |
| 7 | `MESSAGE_CODE` | inline | `7` | 2017 ⊃ 2013 |
| 8 | `JOIN_REQUEST` | inline | – | keine Callback-Ereignisse (beide) |
| 9 | `JOIN_ANSWER` | inline | `8` | 2017 ⊃ 2013 |
| 10 | `READY_TO_START` | inline | `9` | 2017 ⊃ 2013 |
| 11 | `PVP_RECORD` | inline | `10` | 2017 ⊃ 2013 |
| 12 | `RACE_RECORD` | inline | `11` | 2017 ⊃ 2013 |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 20, gemeinsamer Rumpf: 2, nicht im Client: 9, ohne Kandidat: 8.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `IsInShrineRegionByIndex` (`0x0056A950`), `IsInShrineRegionByIndex` (`0x0056A950`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmShrine`](AgcmShrine.md)
