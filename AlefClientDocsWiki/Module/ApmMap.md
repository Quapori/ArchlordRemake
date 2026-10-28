# ApmMap (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `ApmMap` (Weltkarte: Sektoren, Objekte in Sektoren, Bereiche, Weltkarte, Wegsuche) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Aufrufgraph, Vtable `0x008B1EFC`, Zeichenketten, Anker (`Init`, `DeleteSector`, `GetValidDestination`, `LoadRegionPerculiarity`), EP8-Quelle `Modules/APublic/ApmMap/ApmMap.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 67 von 143 Quellmethoden sind zugeordnet (dazu Konstruktor und Destruktorrumpf). Zugeordnet sind Sektorverwaltung (Anlegen, Laden, Entfernen), die Listen der Figuren, NPCs, Monster, Gegenstände und Objekte, die Entpack-Zwischenspeicher, die Bereichs- und Weltkartenfunktionen und die Sperrabfragen.
- **Nicht zugeordnet:** alle `Save*`-Funktionen (Editor), `LoadAll`/`LoadDivision`/`SaveAll`, die Bindungsfunktionen (`AddBindType`, `GetBindList` …), `LoadRegion`, `AddRegion`/`RemoveRegion`, die Dimensionsfunktionen, die Fassungen von `GetNPCList`/`GetMonsterList` mit Matrix, `GetObjectList`, `DeleteNPCs`/`DeleteMonsters`, `UpdateItem`/`UpdateObject`, `GetHeight` und weitere kleine Zugriffe. Ob sie eingebaut oder entfernt sind, ist offen.
- **Hinweis:** `0x00514430` war zuvor fälschlich als [`AgpmEventGacha`](AgpmEventGacha.md):StreamReadGachaTypeTable` benannt (Namens-Treffer über Schlüsselwörter); es ist `ApmMap::LoadTemplate`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApmMap.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetSkillDbgCB` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 1 | `Init` | `0x00510620` | 864 | Zeichenkette |
| 2 | `CheckBlockingInfo` | `0x00513DA0` | 174 | von Hand geprüft |
| 3 | `IsPassThis` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 4 | `GetSector` | `0x00511BE0` | 169 | von Hand geprüft |
| 5 | `GetSector` | `0x00510990` | 72 | von Hand geprüft |
| 6 | `GetSectorList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 7 | `GetSectorByArray` | `0x00510C40` | 61 | von Hand geprüft |
| 8 | `GetItemList` | `0x00511C90` | 744 | von Hand geprüft |
| 9 | `GetCharList` | `0x00513E50` | 334 | von Hand geprüft |
| 10 | `GetCharList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 11 | `GetCharList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 12 | `GetCharList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 13 | `GetCharList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 14 | `GetCharList` | `0x00511F80` | 904 | von Hand geprüft |
| 15 | `GetNPCList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 16 | `GetNPCList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 17 | `GetNPCList` | `0x00512310` | 904 | von Hand geprüft |
| 18 | `GetMonsterList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 19 | `GetMonsterList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 20 | `GetMonsterList` | `0x005126A0` | 1057 | von Hand geprüft |
| 21 | `GetObjectList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 22 | `SetupSector` | `0x00512AD0` | 282 | von Hand geprüft |
| 23 | `DeleteSector` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 24 | `DeleteSector` | `0x00513FA0` | 360 | von Hand geprüft |
| 25 | `DeleteSectorReal` | `0x00512BF0` | 115 | von Hand geprüft |
| 26 | `AddChar` | `0x00514110` | 183 | von Hand geprüft |
| 27 | `UpdateChar` | `0x005141D0` | 247 | von Hand geprüft |
| 28 | `DeleteChar` | `0x005142D0` | 153 | von Hand geprüft |
| 29 | `DeleteChars` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 30 | `MoveChar` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 31 | `AddChar` | `0x00512C70` | 264 | von Hand geprüft |
| 32 | `UpdateChar` | `0x00512D80` | 416 | von Hand geprüft |
| 33 | `DeleteChar` | `0x00512F50` | 172 | von Hand geprüft |
| 34 | `DeleteChars` | `0x00510C80` | 222 | von Hand geprüft |
| 35 | `MoveChar` | `0x00510D60` | 229 | von Hand geprüft |
| 36 | `AddNPC` | `0x00513000` | 264 | von Hand geprüft |
| 37 | `UpdateNPC` | `0x00513110` | 416 | von Hand geprüft |
| 38 | `DeleteNPC` | `0x005132E0` | 172 | von Hand geprüft |
| 39 | `DeleteNPCs` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 40 | `MoveNPC` | `0x00510E50` | 229 | von Hand geprüft |
| 41 | `AddMonster` | `0x00513390` | 264 | von Hand geprüft |
| 42 | `UpdateMonster` | `0x005134A0` | 416 | von Hand geprüft |
| 43 | `DeleteMonster` | `0x00513670` | 172 | von Hand geprüft |
| 44 | `DeleteMonsters` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 45 | `MoveMonster` | `0x00510F40` | 229 | von Hand geprüft |
| 46 | `AddItem` | `0x00513720` | 255 | von Hand geprüft |
| 47 | `UpdateItem` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 48 | `DeleteItem` | `0x00513820` | 174 | von Hand geprüft |
| 49 | `DeleteItems` | `0x00511030` | 103 | von Hand geprüft |
| 50 | `MoveItem` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 51 | `AddObject` | `0x005138D0` | 180 | von Hand geprüft |
| 52 | `UpdateObject` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 53 | `DeleteObject` | `0x00513990` | 147 | von Hand geprüft |
| 54 | `DeleteObjects` | `0x005110A0` | 83 | von Hand geprüft |
| 55 | `MoveObject` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 56 | `OnAddModule` | `0x00511100` | 12 | vtable/String |
| 57 | `OnInit` | `0x00511110` | 35 | vtable/String |
| 58 | `OnIdle` | `0x00514370` | 18 | vtable/String |
| 59 | `OnDestroy` | `0x005183D0` | 57 | vtable/String |
| 60 | `FlushDeleteSectors` | `0x00513A30` | 78 | von Hand geprüft |
| 61 | `ProcessRemove` | `0x00513A80` | 133 | von Hand geprüft |
| 62 | `AttachSectorData` | `0x00511140` | 30 | von Hand geprüft |
| 63 | `AttachSegmentData` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 64 | `GetSectorDataChar` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 65 | `GetSectorDataItem` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 66 | `GetSectorDataObject` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 67 | `GetSectorDataChar` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 68 | `GetSectorDataItem` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 69 | `GetSectorDataObject` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 70 | `SetCallbackAddChar` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 71 | `SetCallbackRemoveChar` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 72 | `SetCallbackMoveChar` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 73 | `SetCallbackAddItem` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 74 | `SetCallbackRemoveItem` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 75 | `SetCallbackLoadSector` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 76 | `SetCallbackClearSector` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 77 | `LoadDivision` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 78 | `LoadAll` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 79 | `SaveAll` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 80 | `DeleteAllSector` | `0x00514E60` | 117 | von Hand geprüft |
| 81 | `DeleteRealAllSector` | `0x00513B10` | 69 | von Hand geprüft |
| 82 | `ClearAllSector` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 83 | `ClearSector` | `0x00511160` | 43 | von Hand geprüft |
| 84 | `LoadSector` | `0x00511190` | 256 | von Hand geprüft |
| 85 | `AddObjectBlocking` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 86 | `ClearAllObjectBlocking` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 87 | `ClearAllHeightPool` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 88 | `GetHeight` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 89 | `GetType` | `0x00514390` | 66 | von Hand geprüft |
| 90 | `GetUnpackManagerDivisionCompact` | `0x00511290` | 377 | von Hand geprüft |
| 91 | `FlushUnpackManagerDivision` | `0x00511410` | 115 | von Hand geprüft |
| 92 | `GetUnpackManagerDivisionGeometry` | `0x00511490` | 391 | von Hand geprüft |
| 93 | `GetUnpackManagerDivisionMoonee` | `0x00511620` | 377 | von Hand geprüft |
| 94 | `CheckBlockingInfo` | `0x005117A0` | 175 | von Hand geprüft |
| 95 | `AddBindType` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 96 | `ClearAllBindData` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 97 | `GetBindList` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 98 | `AddBindElementRect` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 99 | `AddBindElementCircle` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 100 | `IsChangedBind` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 101 | `GetBindData` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 102 | `IsSameRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 103 | `IsSameRegionInvolveParent` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 104 | `GetLoadedDivisionInfo` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 105 | `EnumLoadedDivision` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 106 | `AddLoadedDivision` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 107 | `RemoveLoadedDivision` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 108 | `AddTemplate` | `0x005143E0` | 77 | von Hand geprüft |
| 109 | `RemoveTempate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 110 | `GetTemplate` | `0x00513B60` | 37 | von Hand geprüft |
| 111 | `GetTemplate` | `0x00513B90` | 101 | von Hand geprüft |
| 112 | `SaveTemplate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 113 | `LoadTemplate` | `0x00514430` | 1553 | von Hand geprüft |
| 114 | `AddRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 115 | `GetRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 116 | `RemoveRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 117 | `RemoveAllRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 118 | `SaveRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 119 | `LoadRegion` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 120 | `GetRegion` | `0x00514AC0` | 76 | von Hand geprüft |
| 121 | `CLS_AddSector` | `0x00511850` | 175 | von Hand geprüft |
| 122 | `CLS_RemoveSector` | `0x00511900` | 285 | von Hand geprüft |
| 123 | `LoadDimensionTemplate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 124 | `SaveDimensionTemplate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 125 | `AddDimensionTemplate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 126 | `RemoveDimensionTemplate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 127 | `GetDimensionTemplate` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 128 | `CreateDimension` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 129 | `DestroyDimension` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 130 | `LoadWorldMap` | `0x00515A50` | 1320 | von Hand geprüft |
| 131 | `ReloadWorldMap` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 132 | `SaveWorldMap` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 133 | `RemoveAllWorldMap` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 134 | `GetWorldMapInfo` | `0x00514B10` | 110 | von Hand geprüft |
| 135 | `GetWorldMapInfoByGroupName` | `0x00514B80` | 171 | von Hand geprüft |
| 136 | `GetMinHeight` | `0x00511A20` | 61 | von Hand geprüft |
| 137 | `GetValidDestination` | `0x005163F0` | 3834 | Zeichenkette |
| 138 | `GetValidDestination_LineBlock` | `0x00515F90` | 934 | von Hand geprüft |
| 139 | `LoadRegionPerculiarity` | `0x005172F0` | 2592 | Zeichenkette |
| 140 | `CheckRegionPerculiarity` | `0x00514FF0` | 345 | von Hand geprüft |
| 141 | `LoadRegioinPerculiaritySkulTid` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |
| 142 | `LoadRegioinPerculiaritySkulRestrictionTime` | – | | keine Funktion im Bereich `0x00510620`–`0x00518500` zugeordnet; Verbleib offen (in der Quelle zum Teil nur vom Editor oder vom Server gerufen, nicht einzeln belegt) |

67 von 143 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `GetSector_world` (`0x00510990`), `CheckBlockingInfo_xz` (`0x005117A0`), `GetCharList_range` (`0x00511F80`), `GetNPCList_range` (`0x00512310`), `GetMonsterList_range` (`0x005126A0`), `GetTemplate_name` (`0x00513B90`), `GetCharList_type` (`0x00513E50`), `AddChar_type` (`0x00514110`), `UpdateChar_type` (`0x005141D0`), `DeleteChar_type` (`0x005142D0`), `ApmMap` (`0x00517D80`), `~ApmMap_body` (`0x00518230`), `~ApmMap` (`0x00518470`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA0` | `Zeiger auf das Kartenverzeichnis (für die Entpacker)` | `GetUnpackManagerDivision*` |
| `this+0xB90` | `Flag/Zeiger, in `OnDestroy` auf 0 gesetzt (Bedeutung nicht belegt)` | `OnDestroy` |
| `this+0xBA4` | `Sektorfeld 800 × 800 Zeiger` | `GetSector`, `GetSectorByArray`, `GetItemList` |
| `this+0x271C64` | `Frist für das Entfernen (Takte)` | `ProcessRemove` |
| `this+0x271C6C` | `letzter Lauf von `ProcessRemove`` | `ProcessRemove` |
| `this+0x271C78` | `Liste der geladenen Sektoren (bis 65.535)` | `CLS_AddSector`, `CLS_RemoveSector` |
| `this+0x2B1C74` | `Anzahl geladener Sektoren` | `CLS_AddSector`, `CLS_RemoveSector` |
| `this+0x2B1CCC …` | `Entpack-Zwischenspeicher (3 × 9 Einträge)` | `GetUnpackManagerDivision*`, `FlushUnpackManagerDivision` |
| `this+0x2B1E08` | `Liste der Bereiche (Knoten `0x40` Byte)` | `OnDestroy` |
| `this+0x2B1E70` | `Liste der Bereichsvorlagen (`0xF0` Byte, Nachfolger `+0xF0`)` | `GetTemplate`, `AddTemplate` |
| `this+0x2B1EE4 / 0x2B1EE8` | `Vektor der Weltkarteneinträge (`0x52C` Byte je Eintrag)` | `GetWorldMapInfo`, `LoadWorldMap` |
| `Sektor+0x04` | `Flags: 2 geladen, 4 zum Entfernen vorgemerkt` | `GetSector`, `LoadSector` |
| `Sektor+0x9C / 0x9E` | `Index in der Liste / Zähler` | `CLS_AddSector`, `CLS_RemoveSector` |
| `Sektor+0xA0` | `Zeit der Vormerkung zum Entfernen` | `ProcessRemove` |

## Vtable und Aufbau

`ApmMap` (Weltkarte: Sektoren, Bereiche, Vorlagen, Weltkarten-Einträge) liegt im Binary bei `0x00510620`–`0x00518500`. Vtable `0x008B1EFC`: 0 Löschwrapper (`0x00518470`, ruft den Destruktorrumpf `0x00518230`), 1 `OnAddModule` (`0x00511100`), 2 `OnInit` (`0x00511110`, 35 Byte, ruft `0x004EBAE0`), `OnIdle` (`0x00514370`) springt auf `ProcessRemove` (`0x00513A80`), `OnDestroy` (`0x005183D0`) räumt zuerst alle Sektoren (`DeleteAllSector` `0x00514E60`), dann Bereichslisten, Entpack-Zwischenspeicher, Entfernungsliste und das Sektorfeld (`0x0051841B`). Der Konstruktor `0x00517D80` (1.197 Byte) trägt den Namen „ApmMap“ ein und baut die Listen auf. `Init` (`0x00510620`, 864 Byte) setzt die Verzeichnisse (`%s\Map`, `%s\Map\Data`, `%s\Map\Data\Geometry`) und meldet bei erneutem Aufruf „schon initialisiert“.
Die Sektoren stehen in einem Feld von 800 × 800 Zeigern bei `this+0xBA4` (Index = Spalte · 800 + Zeile); die Weltposition wird über `(Position + 0x271000) / 0x1900` umgerechnet (Sektorbreite 6.400, Versatz 400 Sektoren), bei `+0xBA0` steht der Zeiger auf den Verzeichnisnamen der Karte. Eine Liste aller geladenen Sektoren (bis 65.535 Zeiger) liegt bei `this+0x271C78`, ihre Anzahl bei `+0x2B1C74`; Zwischenspeicher für die Entpacker (je neun Einträge zu Zeiger, Division und Zeit) ab `+0x2B1CCC`; die Vorlagenliste der Bereiche bei `+0x2B1E70`, die Bereichsliste bei `+0x2B1E08` und der Vektor der Weltkarteneinträge bei `+0x2B1EE4`/`+0x2B1EE8` (je `0x52C` Byte).

## Sektoren

`GetSector(Position, …)` (`0x00511BE0`) rechnet die Position auf Sektorindizes um und liefert den Zeiger, wenn das Bit 4 (zum Entfernen vorgemerkt) nicht gesetzt ist; `GetSector(wx, wy, wz)` (`0x00510990`) macht dasselbe mit Weltindizes, `GetSectorByArray` (`0x00510C40`) verlangt das Bit 2 (geladen). `SetupSector` (`0x00512AD0`) legt einen Sektor über `CreateModuleData` an, trägt ihn ins Feld und in die Liste der geladenen Sektoren ein (`CLS_AddSector` `0x00511850`, mit Sperre); `DeleteSector(Sektor)` (`0x00513FA0`, anchor) merkt ihn zum Entfernen vor; `DeleteSectorReal` (`0x00512BF0`) zerstört ihn wirklich (`DestroyModuleData`, `CLS_RemoveSector` `0x00511900`); `FlushDeleteSectors` (`0x00513A30`), `DeleteAllSector` (`0x00514E60`) und `DeleteRealAllSector` (`0x00513B10`, 800 × 800 Schleife) räumen alles; `ProcessRemove` (`0x00513A80`) läuft höchstens einmal in 1.000 Takten und entfernt vorgemerkte Sektoren, deren Frist abgelaufen ist.
`LoadSector` (`0x00511190`) lädt einen Sektor (Bit 2) und löst Rückruf 5 aus; `ClearSector` (`0x00511160`) löst Rückruf 6 aus und leert den Sektor (`0x0051A580`). Die Entpacker laden Dateien aus dem Verzeichnis `this+0xBA0`: `GetUnpackManagerDivisionCompact` (`0x00511290`, `a%06dx.ma1`), `…Geometry` (`0x00511490`, `g%04d.mpf`) und `…Moonee` (`0x00511620`, `m%04d.mpf`); je Satz neun Einträge, der älteste wird verdrängt; `FlushUnpackManagerDivision` (`0x00511410`) gibt alle frei. `GetMinHeight` (`0x00511A20`) fragt Rückruf 11 ab und merkt sich den letzten Sektor.

## Objekte in Sektoren

Für Figuren, NPCs, Monster, Gegenstände und Objekte führt jeder Sektor eigene Listen (Sektordaten `+4`, `+8`, `+0xC`, `+0x10`, `+0x14`). `AddChar`/`UpdateChar`/`DeleteChar` (`0x00512C70`, `0x00512D80`, `0x00512F50`) tragen eine Figur ein, bewegen sie bei Sektorwechsel und tragen sie aus; ebenso `AddNPC`/`UpdateNPC`/`DeleteNPC` (`0x00513000`, `0x00513110`, `0x005132E0`) und `AddMonster`/`UpdateMonster`/`DeleteMonster` (`0x00513390`, `0x005134A0`, `0x00513670`); `AddItem`/`DeleteItem` (`0x00513720`, `0x00513820`), `AddObject` (`0x005138D0`; Aufrufer [`ApmObject`](ApmObject.md):AddObject`) und `DeleteObject` (`0x00513990`; Aufrufer `ApmObject::DeleteObject`). Die Fassungen mit Figurentyp (`0x00514110`, `0x005141D0`, `0x005142D0`) wählen nach dem Typ.
`MoveChar`/`MoveNPC`/`MoveMonster` (`0x00510D60`, `0x00510E50`, `0x00510F40`, je 229 Byte) tragen eine Figur von einem Sektor in einen anderen um und lösen Rückruf 2 aus; `DeleteChars` (`0x00510C80`), `DeleteItems` (`0x00511030`) und `DeleteObjects` (`0x005110A0`) leeren die Listen eines Sektors und rufen dabei die Rückrufe 1 bzw. 4. Abfragen im Umkreis: `GetItemList` (`0x00511C90`, 744 Byte) sowie `GetCharList`/`GetNPCList`/`GetMonsterList` mit Reichweite (`0x00511F80`, `0x00512310`, `0x005126A0`) und die Weiche nach Typ `0x00513E50`.

## Sperren, Bereiche und Weltkarte

`CheckBlockingInfo(x, z, Typ)` (`0x005117A0`) liest die Sperrbits des Segments (Typ 1 bis 3) und liefert 0, wenn der Sektor nicht geladen ist; `CheckBlockingInfo(Position, Typ)` (`0x00513DA0`) ruft die Fassung am Sektor. `GetValidDestination` (`0x005163F0`, 3.834 Byte, anchor) sucht das erreichbare Ziel entlang der Strecke; `GetValidDestination_LineBlock` (`0x00515F90`) sammelt die Sperrflächen der berührten Sektoren; die Hilfsfunktionen `0x00511A60`/`0x00511AD0` schneiden die Strecke mit einer Kante. `GetType` (`0x00514390`) liefert die Bodenart aus dem Segment.
`GetRegion(x, z)` (`0x00514AC0`) liefert den Bereichsindex (0xFFFF, wenn keiner); `GetTemplate` (`0x00513B60` nach Index, `0x00513B90` nach Name) durchsucht die verkettete Liste der Bereichsvorlagen (`0x00F0` Byte je Eintrag); `AddTemplate` (`0x005143E0`) fügt eine Vorlage hinzu, falls ihr Index noch fehlt; `LoadTemplate` (`0x00514430`, 1.553 Byte; Schlüssel `ParentIndex`, `ItemSection`, `Comment` u. a.) liest sie aus einer Datei; die frühere Zuordnung dieser Adresse zu `AgpmEventGacha::StreamReadGachaTypeTable` war ein Fehler (beide Berichte nachgezogen). `LoadWorldMap` (`0x00515A50`, 1.320 Byte; Schlüssel `Comment`, `XStart`, `ZStart`, `ItemID`, `GroupID`, `RegionTexture` u. a.) füllt den Vektor der Weltkarteneinträge; `GetWorldMapInfo` (`0x00514B10`) und `GetWorldMapInfoByGroupName` (`0x00514B80`) suchen darin.
`LoadRegionPerculiarity` (`0x005172F0`, anchor) liest `ini\RegionPerculiarity.xml` (`RegionRule`, `Index` …); `CheckRegionPerculiarity` (`0x00514FF0`, 345 Byte) prüft über eine Sprungtabelle mit Bits eines Eintrags (`+0x1C`: 1, 2, 0x20, 4, 8, 0x10) und eine Liste (Fall 7), ob eine Eigenschaft für den Bereich gilt; es wird u. a. von der Nachrichtenverarbeitung der Spielmodule gerufen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Dekompilat) sind `GetSector` (beide), `GetSectorByArray`, `LoadSector`, die drei Entpacker, `CheckBlockingInfo` (beide), `CLS_AddSector`/`CLS_RemoveSector`, `GetMinHeight`, `FlushDeleteSectors`, `ProcessRemove`, `DeleteRealAllSector`, die Move-Funktionen, `DeleteChars`/`DeleteItems`/`DeleteObjects`, `GetTemplate`/`AddTemplate`/`GetWorldMapInfo`, der Anfang von `GetItemList`, `LoadWorldMap` und `GetValidDestination_LineBlock` (Anfang), `CheckRegionPerculiarity` (Anfang). Die Figuren-, NPC- und Monsterfunktionen (`Add`/`Update`/`Delete`) sind über Größe, Gleichbau der Dreiergruppen und Aufrufbeziehungen zugeordnet, nicht gelesen; welcher der drei gleich gebauten Funktionen Figur, NPC oder Monster ist, folgt aus der Reihenfolge im Binary (Figur, NPC, Monster wie in der Quelle) und der Listenverschiebung im Sektor (nur für Figuren, Gegenstände und Objekte nachgewiesen).
- `GetCharList` mit Typweiche (`0x00513E50`) ist nur eine der drei Fassungen mit `lCharType`; welche, ist nicht geklärt (sie ist der ersten zugeordnet). `MoveChar`/`MoveNPC`/`MoveMonster` heißen so, weil sie Rückruf 2 (MoveChar) auslösen und je eine Liste umhängen; die kleinen 48-Byte-Umhüllungen davor (`0x00512F20`, `0x005132B0`, `0x00513640`) haben keinen Aufrufer und sind nicht benannt.
- `GetType` (`0x00514390`) und `ClearSector` (`0x00511160`) sind aus Größe, Aufruf eines Segment-Zugriffs bzw. dem Rückruf 6 und einer Bereinigungsfunktion geschlossen, nicht aus der Quelle verglichen. Die Hilfsfunktionen für STL-Listen und -Bäume (`0x00514C30`, `0x00515850` …) sind keine Quellmethoden und nicht benannt.
- Die Rückruf-Setzer `SetCallback…` liegen an den gemeinsamen Rümpfen (Kennung 0 bis 5: `0x006DA540`, `0x0053A200`, `0x0057BED0`, `0x005766B0`, `0x0057BEF0`, `0x00574590`); sie sind hier nicht einzeln den Namen zugeordnet.
- Die Aussage, dass die nicht zugeordneten Methoden fehlen, beruht darauf, dass alle Funktionen im Bereich bis auf STL-Hilfsfunktionen zugeordnet oder als nicht Quellmethode erkannt sind; Aufrufe aus anderen Modulen wurden nicht einzeln gesucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 5, gemeinsamer Rumpf: 7, nicht im Client: 30, ohne Kandidat: 26, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetSectorList` | 84 | `0x005109E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetHeight` (`0x00518800`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmEventGacha`](AgpmEventGacha.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcmAuction`](AgcmAuction.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmItem`](AgcmItem.md), [`AgcmLensFlare`](AgcmLensFlare.md), [`AgcmMap`](AgcmMap.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUISearch`](AgcmUISearch.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgpmEventGacha`](AgpmEventGacha.md), [`AgpmPathFind`](AgpmPathFind.md), [`ApmObject`](ApmObject.md), [`ApmOcTree`](ApmOcTree.md)
