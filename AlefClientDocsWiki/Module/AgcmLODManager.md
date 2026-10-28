# AgcmLODManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmLODManager` (Detailstufen von Modellen: Entfernungen, Laden und Speichern) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Modulaufbau, Entfernungsberechnung, Rahmenmatrix sichern/laden, Stream-Lesen/-Schreiben, Namenssuche und das Laden der Entfernungstabelle sind zugeordnet. Die Werkzeugmethoden `Initailize`, `MakeLODLevel`, `MakeLODLevel_Billboard`, `ReadDFF`, `SetLODCallback`, `LODCallback`, `SetAtomic`, `SearchAtomic…` sowie die Quelldatei `AgcmLODList.cpp` (außer Konstruktoren) wurden im Binary nicht gefunden (vermutlich Werkzeugcode, nicht aufgerufen).
- **OnAddModule** (`0x00617C40`) holt [`AgcmRender`](AgcmRender.md); **OnInit** (`0x00617C60`) fragt das Vertex-Shader-Flag ab und setzt für zwei Detailkurven Dreiecksgrenze und Entfernungsfaktor; **OnIdle** (`0x00617CA0`) schiebt die letzten drei Tickzahlen weiter.
- **Entfernungen:** `SetDistanceRate` (`0x00617CD0`) und `SetCharacterDistanceRate` (`0x00617D30`) berechnen `Standardentfernung / 100 × Verhältnis` und teilen sie linear auf die Stufen auf; die zweite setzt bei Verhältnis 0 den Wert 100 und nutzt eine zweite Standardentfernung.
- **Dateien:** `StreamRead` (`0x00617F10`) und `StreamWrite` (`0x00618220`) verwenden die Schlüssel `LOD_LEVEL`, `LOD_BILLBOARD_NUM` mit dem Format `%d:%d`; `SearchLODType` (`0x006183F0`) vergleicht den Namen ohne Groß-/Kleinschreibung mit `default`, `type1` … (zehn Vergleiche); `ReadLODDistanceData` (`0x00618500`) liest die Excel-Tabelle (Fehlermeldung `ReadLODDistanceData() Error`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmLODManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetDistanceTypeName` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 1 | `OnAddModule` | `0x00617C40` | 26 | vtable/String |
| 2 | `OnDestroy` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 3 | `OnInit` | `0x00617C60` | 55 | vtable/String |
| 4 | `OnIdle` | `0x00617CA0` | 42 | vtable/String |
| 5 | `SetDefaultDistance` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `SetDistanceRate` | `0x00617CD0` | 93 | von Hand geprüft |
| 7 | `SetCharacterDistanceRate` | `0x00617D30` | 97 | von Hand geprüft |
| 8 | `Initailize` | – | | Werkzeugcode, im Binary nicht gefunden |
| 9 | `SetAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `SearchAtomicCheckPartID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `SearchAtomicCB` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `MakeLODLevel` | – | | Werkzeugcode, im Binary nicht gefunden |
| 13 | `MakeLODLevel_Billboard` | – | | Werkzeugcode, im Binary nicht gefunden |
| 14 | `ReadDFF` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `GetGeometryUsrDataInt` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `SetLODCallback` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `FrameMatrixSave` | `0x00617DD0` | 77 | von Hand geprüft |
| 18 | `FrameMatrixLoad` | `0x00617E20` | 107 | von Hand geprüft |
| 19 | `LODCallback` | – | | im Binary nicht gefunden |
| 20 | `GetLODData` | `0x00617E90` | 125 | von Hand geprüft |
| 21 | `StreamRead` | `0x00617F10` | 783 | von Hand geprüft |
| 22 | `StreamWrite` | `0x00618220` | 461 | von Hand geprüft |
| 23 | `SearchLODType` | `0x006183F0` | 258 | von Hand geprüft |
| 24 | `ReadLODDistanceData` | `0x00618500` | 660 | vtable/String |
| 25 | `GetDistanceData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `IsSetLOD` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

12 von 27 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00617ad0` (`0x00617AD0`), `ctor_or_dtor_00617be0` (`0x00617BE0`), `~AgcmLODManager` (`0x006187A0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xC80` | `Standardentfernung für `SetDistanceRate`` | `SetDistanceRate` |
| `this+0xC84` | `Standardentfernung für Figuren` | `SetCharacterDistanceRate` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung stützt sich auf Zeichenketten, Feldzugriffe und die Quellreihenfolge, nicht auf einen Vergleich Zeile für Zeile; `SetDistanceRate` und `SetCharacterDistanceRate` sind nur über die Bedingung „Verhältnis 0 → FALSE“ bzw. „→ 100“ unterschieden.
- Die Offsets `0xC80`/`0xC84` stammen aus den beiden Funktionen; die Feldnamen in der Quelle wurden nicht nachgeprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht im Client: 3, ohne Kandidat: 8, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `LODCallback` | 238 | `0x006187C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetLODCallback` | 16 | `0x00618BD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmRender`](AgcmRender.md)
- **Erwähnt in:** [`AgcmItem`](AgcmItem.md), [`AgcmTuner`](AgcmTuner.md)
