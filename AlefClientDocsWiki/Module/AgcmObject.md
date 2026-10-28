# AgcmObject (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmObject` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmObject` / `AgcmObject.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00671D00` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGCMOBJECT_OPERATION_*` kennt 1 Operationen, davon 1 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Die 2013er Berichte enthalten für dieses Modul keine Callback-Ereignisse je Operation; ein Abgleich ist nicht möglich.
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`00675270`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00670D30` | `AgcmObject::OnDestroy` | merged |
| `0x00670E60` | `AgcmObject::OnObjectCreate` | stage1 |
| `0x00670E90` | `AgcmObject::OnObjectDestroy` | stage1 |
| `0x00670EC0` | `AgcmObject::OnObjectTemplateCreate` | stage1 |
| `0x00671360` | `AgcmObject::ObjectTemplateStreamReadCB` | stage1 |
| `0x00671D00` | `AgcmObject::OnReceive` | merged |
| `0x006722A0` | `AgcmObject::CBOnGetHeight` | stage1 |
| `0x00672400` | `AgcmObject::ShowPickingInfo` | as-register |
| `0x006724F0` | `AgcmObject::HidePickingInfo` | as-register |
| `0x00672900` | `AgcmObject::ObjectTemplateStreamWriteCB` | merged |
| `0x00672CD0` | `AgcmObject::ObjectStreamWriteCB` | stage1 |
| `0x00673740` | `AgcmObject::CBLoaderTemplate` | stage1 |
| `0x006737A0` | `AgcmObject::RidableOverlapping::ctor_or_dtor_006737a0` | merged |
| `0x00673900` | `AgcmObject::OnObjectTemplateDestroy` | stage1 |
| `0x00673BA0` | `AgcmObject::RidableOverlapping::ctor_or_dtor_00673ba0` | merged |
| `0x00673BF0` | `AgcmObject::CBOcTreeIDSet` | stage1 |
| `0x00673E20` | `AgcmObject::CBRemoveObject` | stage1 |
| `0x006749D0` | `AgcmObject::CBLoaderInit` | stage1 |
| `0x00674BD0` | `AgcmObject::InitObject` | merged |
| `0x00674D10` | `AgcmObject::OnIdle` | merged |
| `0x00674DB0` | `AgcmObject::CBLoadMap` | stage1 |
| `0x00674E80` | `AgcmObject::ObjectStreamReadCB` | stage1 |
| `0x00674FB0` | `AgcmObject::SetupObjectClump` | merged |
| `0x00674FF0` | `AgcmObject::CBInitObject` | stage1 |
| `0x00675500` | `AgcmObject::ctor_or_dtor` | merged |
| `0x00675720` | `AgcmObject::~AgcmObject` | merged |
| `0x00675740` | `AgcmObject::OnInit` | merged |
| `0x00675D50` | `AgcmObject::CBUnLoadMap` | stage1 |
| `0x00675D90` | `AgcmObject::OnAddModule` | merged |

29 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 3/3/3 | ja | ja |

**m_csPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation type |
| 1 | `0x2` | INT32 | 1 | object id |
| 2 | `0x4` | INT8 | 1 | object status |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `UPDATE` | inline | – | keine Callback-Ereignisse (beide) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 9, gemeinsamer Rumpf: 6, nicht im Client: 25, ohne Kandidat: 15, zugeordnet: 18.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `RemoveObjectTemplateGroup` | 12 | `0x006737F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SectorRidableObjectIndexUpdate` | 20 | `0x00673EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetAllOcTreeIDs` | 45 | `0x00673A70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBOnAddObject` | 223 | `0x00673F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SectorObjectIndexUpdate` | 22 | `0x006736E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `WaitForQueueFlush` | 28 | `0x00674D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ObjectTemplateGroupStreamWrite` | 72 | `0x006719B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ObjectTemplateGroupStreamRead` | 109 | `0x00670F30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetupObjectClump2` | 135 | `0x00674550` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetupObjectClump` | 9 | `0x00674B60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GroupDelete` | 38 | `0x006739A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetupObjectClump1` | 375 | `0x00672D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseObjectTemplateData` | 54 | `0x00671FC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadAtomic` | 14 | `0x00671D80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadClump` | 19 | `0x00670DE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ObjectDeleteIdleProcess` | 45 | `0x006747C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ReleaseObjectData` | 155 | `0x006734B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadTemplateData` | 61 | `0x00671E90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetObjectData` (`0x00670D70`), `IsInValidOctreeData` (`0x00672730`), `ReCalulateOctreeData` (`0x00672730`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmAmbOcclMap`](AgcmAmbOcclMap.md), [`AgcmCamera2`](AgcmCamera2.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventManager`](AgcmEventManager.md), [`AgcmEventQuest`](AgcmEventQuest.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmMap`](AgcmMap.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`ApmObject`](ApmObject.md)
