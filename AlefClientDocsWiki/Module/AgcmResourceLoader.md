# AgcmResourceLoader (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmResourceLoader` (Hintergrund-Ladethread, Ladewarteschlange, Clumps/Atomics/Texturen/Animationen aus Zpack) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmResourceLoader/AgcmResourceLoader.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig; zugeordnet sind Aufbau, Thread, Lader-Verwaltung, Warteschlange, Zerstören, die Lade-Funktionen für Clump/Atomic/Animation/Spline/Textur und die Farbtabelle. Die übrigen Methoden sind im Binary nicht vorhanden, weil sie in der Quelle unreferenziert oder nur auskommentiert aufgerufen werden (Texturwörterbuch-Verwaltung, `Instance…`, `FindLoadEntry` u. a.), oder sie sind eingebaut bzw. mit gleichen Rümpfen anderer Klassen zusammengefaltet; jede ist in der Tabelle begründet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmResourceLoader.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00666130` | 64 | vtable/String |
| 1 | `OnInit` | `0x00663230` | 195 | vtable/String |
| 2 | `OnIdle` | `0x00662980` | 271 | vtable/String |
| 3 | `OnPreDestroy` | `0x00661AE0` | 61 | vtable/String |
| 4 | `OnDestroy` | `0x00663300` | 13 | vtable/String |
| 5 | `RegisterLoader` | `0x00661B20` | 89 | von Hand geprüft |
| 6 | `AddLoadEntry` | `0x00662780` | 274 | von Hand geprüft |
| 7 | `RemoveLoadEntry` | `0x00662A90` | 396 | von Hand geprüft |
| 8 | `RemoveAllEntry` | `0x00662C20` | 225 | von Hand geprüft |
| 9 | `IsEmptyEntry` | `0x006622D0` | 196 | von Hand geprüft |
| 10 | `AddDestroyClump` | `0x00661B80` | 148 | seqmatch |
| 11 | `AddDestroyAtomic` | `0x00661C20` | 148 | seqmatch |
| 12 | `AddDestroyHierarchy` | `0x00661CC0` | 50 | seqmatch |
| 13 | `RemoveResources` | `0x00662D10` | 356 | seqmatch |
| 14 | `ProcessLoader` | `0x00662E80` | 553 | von Hand geprüft |
| 15 | `SetTexDictPath` | `0x00661D00` | 31 | seqmatch |
| 16 | `SetCurrentTexDict` | – | | in der Quelle nur in auskommentierten Zeilen aufgerufen (`//SetCurrentTexDict(szTexDict);` in `LoadClump`, `LoadAtomic`, `LoadTexture`); im Binary nicht vorhanden |
| 17 | `AddTexDict` | – | | nur von `SetCurrentTexDict` gerufen, damit unreferenziert; im Binary nicht vorhanden |
| 18 | `GetTexDict` | – | | nur von `SetCurrentTexDict` und `RemoveTexDict` gerufen, damit unreferenziert; im Binary nicht vorhanden |
| 19 | `RemoveTexDict` | – | | in der Quelle nirgends aufgerufen; im Binary nicht vorhanden |
| 20 | `LoadClump` | `0x00664550` | 1418 | Zeichenkette |
| 21 | `LoadAtomic` | `0x00664AE0` | 1696 | seqmatch |
| 22 | `LoadRtAnim` | `0x00665190` | 687 | seqmatch |
| 23 | `LoadRpSpline` | `0x00665440` | 836 | seqmatch |
| 24 | `ReadTextureFromZpack` | `0x00665790` | 326 | von Hand geprüft |
| 25 | `LoadTexture` | `0x006658E0` | 759 | seqmatch |
| 26 | `CBGetTextureFromTexDict` | – | | in der Quelle nur im `_DEBUG`-Zweig von `LoadTextureFromTexDict` benutzt; im Release-Binary nicht vorhanden |
| 27 | `LoadTextureFromFile` | `0x00665BF0` | 721 | seqmatch |
| 28 | `LoadTextureFromTexDict` | `0x00661D20` | 206 | von Hand geprüft |
| 29 | `CBTextureRead` | `0x00665ED0` | 579 | Callback-Registrierung |
| 30 | `WriteAllTexDicts` | – | | in der Quelle nirgends aufgerufen; im Binary nicht vorhanden |
| 31 | `InstanceAtomic` | – | | wird nur von `CBInstanceAtomic` und `InstanceClump` gerufen, die ihrerseits nirgends aufgerufen werden (`AcuObject::InstanceClump` ist eine andere Klasse); im Binary nicht vorhanden |
| 32 | `CBInstanceAtomic` | – | | nur von `InstanceClump` benutzt, in der Quelle unreferenziert; im Binary nicht vorhanden |
| 33 | `InstanceClump` | – | | in der Quelle nirgends aufgerufen; im Binary nicht vorhanden |
| 34 | `SetCallbackLoadEntryEmpty` | – | | in der Quelle von keinem Modul aufgerufen; im Binary nicht vorhanden |
| 35 | `GetHierarchy` | – | | in `LoadClump` eingebaut (der Frame-Durchlauf mit `GetChildFrameHierarchy` steht dort direkt) |
| 36 | `SetTexturePath` | `0x00661DF0` | 28 | von Hand geprüft |
| 37 | `AddDefaultTexturePath` | `0x00661E10` | 83 | von Hand geprüft |
| 38 | `GetChildFrameHierarchy` | `0x00661E70` | 47 | seqmatch |
| 39 | `CBInitAtomic` | `0x006623A0` | 461 | von Hand geprüft |
| 40 | `CBFilterModeMaterial` | `0x0076ACF0` | 18 | gleiche Adresse wie `zusammengefaltet mit [`AgcDebugWindow`](AgcDebugWindow.md):CBMaterialFilter` (setzt den Filtermodus der Material-Textur)` (vom Linker zusammengefaltet) |
| 41 | `GetAtomicUsrDataArrayInt` | – | | in der Quelle nirgends aufgerufen (`CBInitAtomic` ruft `GetGeometryUsrDataArrayInt`); im Binary nicht vorhanden |
| 42 | `GetGeometryUsrDataArrayInt` | `0x00661EA0` | 169 | von Hand geprüft |
| 43 | `LoadTextureFromStream` | `0x00661F50` | 640 | seqmatch |
| 44 | `FindLoadEntry` | – | | in der Quelle nirgends aufgerufen; im Binary nicht vorhanden |
| 45 | `_LoadColor` | `0x00663580` | 573 | seqmatch |
| 46 | `_HexStringToDWORD` | `0x007A09D0` | 160 | gleiche Adresse wie `zusammengefaltet mit [`AgcChatMessage`](AgcChatMessage.md):_HexStringToDWORD`; `_LoadColor` ruft diese Adresse` (vom Linker zusammengefaltet) |
| 47 | `GetColor` | `0x00663310` | 143 | von Hand geprüft |

35 von 48 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmResourceLoader` (`0x00663440`), `AgcmResourceLoader` (`0x006637C0`), `ReadFromZpack` (`0x00663F20`), `ReadTextureFromZpack_global` (`0x00664140`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger [`AgcmGlyph`](AgcmGlyph.md) (für die Zielsperre beim Zerstören)` | `AddDestroyClump`, `AddDestroyAtomic` |
| `this+0xC50` | `Ende-Merkmal des Threads` | `ProcessLoader` |
| `this+0xC54` | `Thread-Handle` | Konstruktor, `OnPreDestroy` |
| `this+0xC5C` | `Anzahl registrierter Lader (höchstens 16), Einträge zu 0x34 Byte ab `+0xC60`` | `RegisterLoader` |
| `this+0x1010 / 0x1044` | `Listen „Warteschlange“ / „Fertig“` | `AddLoadEntry`, `RemoveLoadEntry` |
| `this+0x10AC` | `Pfad des Texturwörterbuchs` | `SetTexDictPath` |
| `this+0x1160 / 0x13E0` | `Standard-Texturpfade (5 × 128 Byte) / Anzahl` | `AddDefaultTexturePath` |
| `this+0x13F8` | `Farbtabelle (`std::map`)` | `GetColor` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmResourceLoader` (`0x00663A20`, Löschwrapper), 1 `OnAddModule` (`0x00666130`), 2 `OnInit` (`0x00663230`), 3 `OnIdle` (`0x00662980`), 4 und 5 `0x0067FAB0`, 6 `OnPreDestroy` (`0x00661AE0`), 7 `OnDestroy` (`0x00663300`), 8 `0x004E3420`. Der Konstruktor (`0x006637C0`, 603 Byte, trägt `AgcmResourceLoader`) startet den Hintergrund-Thread über `_beginthreadex` mit der Thread-Funktion `ProcessLoader` (`0x00662E80`); das Thread-Handle liegt bei `this+0xC54`. Der Destruktorrumpf ist `0x00663440` (ruft die Basisklasse und den Speicherpool-Destruktor `0x006633D0`).

## Lader und Warteschlange

Bis zu 16 Lader (`this+0xC5C` = Anzahl, Einträge zu `0x34` Byte ab `this+0xC60`): `RegisterLoader` (`0x00661B20`) trägt Klasse, Lade- und Fertig-Rückruf ein und gibt den Index zurück (-1 bei vollem Feld). `AddLoadEntry` (`0x00662780`) legt einen Auftrag aus dem Speicherpool in die Warteschlange (Liste bei `this+0x1010`, Sperre `this+0xFA0`; bei erzwungener Sofortausführung `this+0x13F4` wird nicht eingereiht). `RemoveLoadEntry` (`0x00662A90`) löscht passende Einträge aus Warteschlange und Fertig-Liste (`this+0x1044`, Sperre `this+0xFBC`) und löst bei leeren Listen den Rückruf 0 aus; `RemoveAllEntry` (`0x00662C20`) entfernt alle Einträge eines Laders; `IsEmptyEntry` (`0x006622D0`) prüft beide Listen. `ProcessLoader` (`0x00662E80`, 553 Byte) läuft bis das Ende-Merkmal (`this+0xC50`) gesetzt ist, nimmt den ersten Eintrag der Warteschlange, ruft den Lade-Rückruf des Laders und räumt Einträge ab; `RemoveResources` (`0x00662D10`) gibt die vorgemerkten Ressourcen frei.
`AddDestroyClump` (`0x00661B80`), `AddDestroyAtomic` (`0x00661C20`) und `AddDestroyHierarchy` (`0x00661CC0`) zerstören unter Sperre des Frame-Zugriffs (und, wenn `AgcmGlyph` vorhanden ist, unter dessen Zielsperre) das jeweilige RenderWare-Objekt sofort – wie der aktive Zweig der Quelle.

## Laden von Ressourcen

`ReadFromZpack` (`0x00663F20`, freie Funktion der Quelldatei) und `ReadTextureFromZpack_global` (`0x00664140`, 1026 Byte, enthält die Zeichenketten `texture` und `character`) lesen Dateien aus den Zpack-Archiven. Die Methoden: `LoadClump` (`0x00664550`), `LoadAtomic` (`0x00664AE0`), `LoadRtAnim` (`0x00665190`), `LoadRpSpline` (`0x00665440`), `ReadTextureFromZpack` (`0x00665790`, Schlüssel `asdfqwer`, Entschlüsselung bei Typ 3), `LoadTexture` (`0x006658E0`), `LoadTextureFromFile` (`0x00665BF0`, ebenfalls mit `asdfqwer`, Namen bis 256 Zeichen) und `LoadTextureFromStream` (`0x00661F50`, 640 Byte, wählt je Typ den RenderWare-Leser). `CBTextureRead` (`0x00665ED0`) war schon benannt.
`AddDefaultTexturePath` (`0x00661E10`) nimmt bis zu fünf Pfade zu je 128 Byte (`this+0x1160`, Zähler `this+0x13E0`), `SetTexDictPath` (`0x00661D00`) kopiert den Texturwörterbuch-Pfad nach `this+0x10AC` (einziger Aufrufer in der Quelle: `MyEngine.cpp`). `SetTexturePath` (`0x00661DF0`, 28 Byte, 21 Aufrufer) speichert den Zeiger in der Thread-lokalen Variablen `m_pszTexturePath` (TLS-Offset `+0x14`). `LoadTextureFromTexDict` (`0x00661D20`) liest ein Texturwörterbuch aus dem Stream (Chunk `0x16` oder `0x23`), holt die letzte Textur und zerstört das Wörterbuch; der Namensparameter wird im Release nicht benutzt. `CBInitAtomic` (`0x006623A0`, 461 Byte) wird von `LoadClump` per `RpClumpForAllAtomics` und von `LoadAtomic` gerufen und liest über `GetGeometryUsrDataArrayInt` das Feld `PartID`. `GetGeometryUsrDataArrayInt` (`0x00661EA0`) sucht in den Nutzerdaten der Geometrie das Feld mit dem Namen und liefert den ersten Ganzzahlwert. `GetChildFrameHierarchy` (`0x00661E70`) ist der Frame-Rückruf, der die erste Hierarchie in einem Kindframe findet.

## Farben

`_LoadColor` (`0x00663580`, 573 Byte) liest `INI\ArchlordColor.ini`; `GetColor` (`0x00663310`) sucht den Namen in der Farbtabelle (`std::map` bei `this+0x13F8`, Wert bei `+0x28`) und gibt 0 zurück, wenn er fehlt.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind `RegisterLoader`, `AddLoadEntry`, `RemoveLoadEntry`, `RemoveAllEntry`, `IsEmptyEntry` und die `AddDestroy…`-Funktionen; `LoadClump` war schon über Zeichenketten benannt.
- `LoadAtomic`, `LoadTexture`, `LoadTextureFromFile`, `LoadTextureFromStream`, `RemoveResources`, `_LoadColor` und `SetTexDictPath` sind über Quellreihenfolge, Größe und Aufrufbeziehungen zugeordnet, nicht Zeile für Zeile verglichen.
- `LoadRtAnim` (`0x00665190`) und `LoadRpSpline` (`0x00665440`) sind über die gelesene Chunk-Kennung belegt: die erste sucht Chunk `0x1B` (`rwID_ANIMANIMATION`) und liest mit `0x00429D20` (Kopfkennung `0x100`), die zweite sucht Chunk `0x0C` (`rwID_SPLINE`) und liest mit `0x0042C470`.
- `AddDestroyClump` (`0x00661B80`) und `AddDestroyAtomic` (`0x00661C20`) sind über die aufgerufene Zerstörfunktion belegt: `0x00434E70` ist `RpClumpDestroy` (Atomics, Lichter und Kameras des Clumps, Sperre des Clump-Objekts), `0x00434630` ist `RpAtomicDestroy` (Geometrie bei `+0x18`).
- `ReadFromZpack` und `ReadTextureFromZpack_global` sind freie Funktionen der Quelldatei; die Namen mit Präfix sind nur eine Ablagekonvention dieses Projekts.
- `ProcessLoader` (`0x00662E80`) ist über den `_beginthreadex`-Aufruf im Konstruktor zugeordnet und mit der Quelle abgeglichen: Schleife bis `m_bEnd`, F5-Pause (`GetAsyncKeyState(0x74)`) im Debug-Modus, Entnahme aus der Warteschlange, Lade-Rückruf, Fertig-Liste bzw. Freigabe samt Rückruf `LOADEND`, `RemoveResources(-1)` und `MsgWaitForMultipleObjects` (100 ms) bei leerer Warteschlange. Der Debug-Zweig mit Sleep 300 ms stimmt ebenfalls.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, gemeinsamer Rumpf: 1, nicht im Client: 5, ohne Kandidat: 6.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcChatMessage`](AgcChatMessage.md), [`AgcDebugWindow`](AgcDebugWindow.md), [`AgcmGlyph`](AgcmGlyph.md)
- **Erwähnt in:** [`AgcaAnimation2`](AgcaAnimation2.md), [`AgcmCustomizeRender`](AgcmCustomizeRender.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmGuild`](AgcmGuild.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmItem`](AgcmItem.md), [`AgcmMap`](AgcmMap.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmRender`](AgcmRender.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmSocialActon`](AgcmSocialActon.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUISocialAction`](AgcmUISocialAction.md), [`AgcmUITips`](AgcmUITips.md)
