# ApmEventManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `ApmEventManager` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`ApmEventManager` / `ApmEventManager.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0055D4D0` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Kein Operationsschalter:** In der Quelle bzw. im Binary wurde keine Verzweigung nach Operationen erkannt (`OnReceive` im Binary: 288 Byte).
- **Ereignisse:** `OnReceive` löst bis Tiefe 3 die Callback-IDs 1 aus (APMEVENT_CB_ADD_EVENT).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`0055cfe0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0055C040` | `ApmEventManager::ctor_or_dtor_0055c040` | merged |
| `0x0055C0F0` | `ApmEventManager::OnInit` | merged |
| `0x0055C3D0` | `ApmEventManager::~ApmEventManager` | merged |
| `0x0055C440` | `ApmEventManager::RegisterEvent` | merged |
| `0x0055CE20` | `ApmEventManager::CBStreamWrite` | stage1 |
| `0x0055CE50` | `ApmEventManager::CBStreamRead` | stage1 |
| `0x0055CFE0` | `ApmEventManager::ctor_or_dtor_0055cfe0` | merged |
| `0x0055D2E0` | `ApmEventManager::CBEventConstructorCharacter` | stage1 |
| `0x0055D310` | `ApmEventManager::CBEventConstructorCharacterTemplate` | stage1 |
| `0x0055D340` | `ApmEventManager::CBEventConstructorItem` | stage1 |
| `0x0055D370` | `ApmEventManager::CBEventConstructorItemTemplate` | stage1 |
| `0x0055D3A0` | `ApmEventManager::CBEventConstructorObject` | stage1 |
| `0x0055D3D0` | `ApmEventManager::CBEventConstructorObjectTemplate` | stage1 |
| `0x0055D400` | `ApmEventManager::CBEventDestructor` | stage1 |
| `0x0055D490` | `ApmEventManager::CBInitObject` | stage1 |
| `0x0055D4D0` | `ApmEventManager::OnReceive` | merged |
| `0x0055D5F0` | `ApmEventManager::OnAddModule` | merged |

17 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 4/4/4 | ja | ja |
| `m_csPacketEvent` | 1/1/1 | 2/2/2 | ja | ja |

**m_csPacket** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Source Type |
| 1 | `0x2` | INT32 | 1 | Source ID (Object/Item/Character) |
| 2 | `0x4` | INT32 | 1 | Effect ID |
| 3 | `0x8` | INT32 | 1 | Function ID |

**m_csPacketEvent** (2 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | PACKET | 1 | event base packet |
| 1 | `0x2` | PACKET | 1 | event custom data |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 7, gemeinsamer Rumpf: 4, nicht im Client: 5, ohne Kandidat: 16, zugeordnet: 10.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `RegisterPacketFunction` | 10 | `0x0055CFA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EventConstructor` | 2 | `0x0055C3F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckValidRange` | 9 | `0x0055C380` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamRead` | 118 | `0x0055CA90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetEventData` | 59 | `0x0055C5F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEvent` | 92 | `0x0055C4B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `EventDestructor` | 15 | `0x0055D290` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetEventFromBasePacket` | 26 | `0x0055D900` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InitObject` | 49 | `0x0055CE80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBase` | 27 | `0x0055C130` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetEvent` (`0x0055D8C0`), `GetBasePos` (`0x0055C2D0`), `GetBasePos` (`0x0055C2D0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmAuction`](AgcmAuction.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventManager`](AgcmEventManager.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmEventPointLight`](AgcmEventPointLight.md), [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgcmItem`](AgcmItem.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIEventGacha`](AgcmUIEventGacha.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUIStatus`](AgcmUIStatus.md), [`AgpmEventNPCTrade`](AgpmEventNPCTrade.md), [`AgpmEventPointLight`](AgpmEventPointLight.md)
