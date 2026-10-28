# AgcmUISearch (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUISearch` (Ergebnisliste der Charaktersuche) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUISearch/AgcmUISearch.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 18 Quellmethoden sind einer Adresse zugeordnet (`OnInit`, `OnIdle` und `CBSearchReultListSelect` als gemeinsame Rümpfe); neu ist `RefreshSearchResultList`. Sechs Methoden haben keinen Code im Binary.
- **Nur Anzeige:** `SendSearchCondition` ist im Binary nicht vorhanden; das Modul zeigt nur Ergebnisse an (Name, Stufe, Rasse, Klasse, Region).
- **UI:** 1 Funktion, 5 Anzeigen, 1 Benutzerdatum, 3 Ereignisse – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUISearch.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00693A10` | 163 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x00693450` | 87 | vtable/String |
| 3 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf (Vtable-Slot 3)` (vom Linker zusammengefaltet) |
| 4 | `AddEvent` | `0x00692D50` | 104 | Zeichenkette |
| 5 | `AddFunction` | `0x00692E10` | 41 | Zeichenkette |
| 6 | `AddUserData` | `0x00692E40` | 49 | Zeichenkette |
| 7 | `AddDisplay` | `0x00693370` | 161 | Zeichenkette |
| 8 | `RefreshSearchResultList` | `0x00692E80` | 63 | manual |
| 9 | `SendSearchCondition` | – | | wird nirgends aufgerufen, vom Linker entfernt |
| 10 | `FindClassName` | – | | wird nirgends aufgerufen, vom Linker entfernt |
| 11 | `CBSearchResult` | `0x00693970` | 145 | Callback-Registrierung |
| 12 | `CBSearchFail` | – | | nirgends angemeldet, vom Linker entfernt |
| 13 | `CBSearchResultList` | `0x00692F90` | 810 | UI-Registrierung |
| 14 | `CBSearchReultListSelect` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 15 | `AddSearchResultList` | – | | leer, ohne eigene Adresse |
| 16 | `OpenSearchResultUI` | – | | in CBSearchResult eingebaut |
| 17 | `CloseSearchResultUI` | – | | nirgends aufgerufen, entfernt |

12 von 18 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006936d0` (`0x006936D0`), `ctor_or_dtor_00693800` (`0x00693800`), `~AgcmUISearch` (`0x00693910`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBAC…0xBB4` | `Ereignis-IDs (Öffnen `+0xBAC`, Schließen, Suche fehlgeschlagen)` | `AddEvent`, `CBSearchResult` |
| `0xBA8` | `Benutzerdatum `SearchResultList_UD` (Anzahl bei `+0x4C`)` | `RefreshSearchResultList` |
| `0xBBC / 0xBC0` | `Ergebnisliste (Vektor: Anfang / Ende, Element 0x3C Byte)` | `CBSearchResult`, `CBSearchResultList` |
| `0xBC8…0xBD8` | `Klassentabelle ID → Name (`m_ClassNameMap`)` | `OnDestroy` |
| `0xBE0…0xBF0` | `Klassentabelle Name → ID (`m_RaceClassNameMap`)` | `OnDestroy` |

## Vtable

Vtable bei `0x008CDF5C`: Slot 0 Destruktor `0x00693910`, 1 `OnAddModule` (`0x00693A10`), 2/6 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (u. a. `OnIdle`), 7 `OnDestroy` (`0x00693450`).

## Registrierung (OnAddModule, 0x00693A10)

Holt `AgcmUISearch` (das Modul sucht sich selbst), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmSearch`](AgpmSearch.md) und [`ApmMap`](ApmMap.md); Pflicht sind `AgpmSearch`, `AgcmUISearch` und `ApmMap`. Meldet `CBSearchResult` (`0x00693970`) als Ergebnis-Callback bei `AgpmSearch` an und ruft `AddEvent` (`0x00692D50`), `AddFunction` (`0x00692E10`), `AddUserData` (`0x00692E40`) und `AddDisplay` (`0x00693370`).

| Art | Name | Handler |
|---|---|---|
| Ereignis | `SeachResultUI_Open` (Schreibweise der Quelle), `SearchResultUI_Close`, `SearchFailed_MsgBox` | – |
| Funktion | `SeachReultList_Selected` | `0x0067AC90` (gemeinsamer Rumpf, die Quelle gibt nur TRUE zurück) |
| Benutzerdatum | `SearchResultList_UD` (Liste mit dem Index 0…n, `AGPMSEARCH_MAX_COUNT` Einträge) | – |
| Anzeigen | `SearchResultList_Display_Name`, `_Level`, `_Race`, `_Class`, `_Region` (alle mit `CBSearchResultList`, Unterscheidung über die Nummer 0…4) | `0x00692F90` |

## Ergebnis (CBSearchResult, CBSearchResultList)

`CBSearchResult` (`0x00693970`) kopiert den Eintrag (Name, Klassen-ID, Mindest-/Höchststufe, Position; `AgpdSearch`, 0x3C Byte) an das Ende der Liste (Vektor ab `+0xBBC`), wirft das Ereignis „Ergebnisfenster öffnen“ (`OpenSearchResultUI` ist eingebaut) und aktualisiert das Benutzerdatum (`RefreshSearchResultList`, `0x00692E80`: Anzahl = Listenlänge).
`CBSearchResultList` (`0x00692F90`, 810 Byte) füllt je Zeile eine Spalte: Name (32 Zeichen), Stufe (`Lv%d`), Rasse aus der Klassen-ID (1, 96, 6 → Mensch; 4, 8, 3 → Ork; 460, 9 → Mondelf; Texte `UI_MESSAGE_ID_LG_RACE_*`), Klasse aus einer Tabelle ID → Name und Region aus der Position (`GetRegion`, lokalisierter Name über `RegionLocalName`). Das stimmt mit der Quelle überein.

## Nicht im Binary

`SendSearchCondition`, `FindClassName`, `CBSearchFail`, `AddSearchResultList` und die beiden Fensterfunktionen haben keine eigene Adresse: Die ersten drei werden nirgends aufgerufen, `CBSearchFail` und `AddSearchResultList` sind leer, `OpenSearchResultUI`/`CloseSearchResultUI` bestehen nur aus einem `ThrowEvent`. Damit sendet dieser Client **keine** Suchanfrage über dieses Modul; es zeigt nur Ergebnisse an, die `AgpmSearch` liefert. In der Quelle fügt `FindClassName` die ID 9 zweimal in die Klassentabelle ein (Elementalist und Swashbuckler); das zweite `insert` bleibt wirkungslos.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00692D50`, `0x00692E10`, `0x00692E40`, `0x00693370`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Ereignis** (3)

| Name | Id | Handler |
|---|---:|---|
| `SeachResultUI_Open` | 0 | – |
| `SearchResultUI_Close` | 0 | – |
| `SearchFailed_MsgBox` | 0 | – |

**Funktion** (1)

| Name | Id | Handler |
|---|---:|---|
| `SeachReultList_Selected` |  | `Element::GetSize` |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `SearchResultList_UD` |  | – |

**Anzeige** (5)

| Name | Id | Handler |
|---|---:|---|
| `SearchResultList_Display_Name` | 0 | `CBSearchResultList` |
| `SearchResultList_Display_Level` | 1 | `CBSearchResultList` |
| `SearchResultList_Display_Race` | 2 | `CBSearchResultList` |
| `SearchResultList_Display_Class` | 3 | `CBSearchResultList` |
| `SearchResultList_Display_Region` | 4 | `CBSearchResultList` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den vorhandenen Funktionen (Registrierung, `CBSearchResult`, Spaltenlogik von `CBSearchResultList`).

## Grenzen

- Dass `SendSearchCondition` und `FindClassName` entfernt wurden, folgt daraus, dass keine Funktion im Bereich sie aufruft und kein Treffer für die Klassen-Texte (`UI_MESSAGE_ID_LG_CLASS_*`) im Modulbereich vorhanden ist; das wurde nicht durch eine Suche im gesamten Binary bewiesen.
- Die Bedeutung der Region-Spalte (`GetRegion`, `RegionLocalName`) wurde nur über die Aufrufe gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, gemeinsamer Rumpf: 2, nicht im Client: 5.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmSearch`](AgpmSearch.md), [`ApmMap`](ApmMap.md)
