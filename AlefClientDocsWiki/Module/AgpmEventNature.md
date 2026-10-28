# AgpmEventNature (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmEventNature` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmEventNature` / `AgpmEventNature.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0051E550` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Kein Operationsschalter:** In der Quelle bzw. im Binary wurde keine Verzweigung nach Operationen erkannt (`OnReceive` im Binary: 170 Byte).
- **Ereignisse:** `OnReceive` löst bis Tiefe 3 die Callback-IDs -1 aus (-1).
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`0051ec40`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0051E550` | `AgpmEventNature::OnReceive` | merged |
| `0x0051E600` | `AgpmEventNature::SkySetWriteCB` | stage1 |
| `0x0051E640` | `AgpmEventNature::SkySetReadCB` | stage1 |
| `0x0051E700` | `AgpmEventNature::CBEventNatureConstructor` | stage1 |
| `0x0051E720` | `AgpmEventNature::CBEventNatureStreamWrite` | stage1 |
| `0x0051E770` | `AgpmEventNature::CBEventNatureStreamRead` | stage1 |
| `0x0051E8D0` | `AgpmEventNature::OnAddModule` | merged |
| `0x0051EAB0` | `AgpmEventNature::OnDestroy` | merged |
| `0x0051EDB0` | `AgpmEventNature::ctor_or_dtor` | merged |
| `0x0051EE40` | `AgpmEventNature::~AgpmEventNature` | merged |

10 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 3/3/3 | ja | ja |

**m_csPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Weather |
| 1 | `0x2` | INT64 | 1 | AUTYPE_INT8, 1,// Time Ratio |
| 2 | `0x4` | INT64 | 1 | AUTYPE_INT64, 1,// Time |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 13, gemeinsamer Rumpf: 5, nicht im Client: 18, ohne Kandidat: 5, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetSkySet` | 15 | `0x0051E960` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventNature`](AgcmEventNature.md)
