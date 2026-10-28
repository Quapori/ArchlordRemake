# AgcmEff2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEff2` (Effektsystem: Effektsätze erzeugen, verwenden, entfernen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmEff2/AgcmEff2.cpp`. Die zahlreichen Hilfsklassen im selben Quellordner (`AgcdEff…`, `AgcuEff…`) sind nicht abgeglichen. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Behälteraufbau, Erzeugen/Verwenden von Effektsätzen, Pool, globale Zeiger und der Rückruf beim Entfernen von Figuren. Nicht zugeordnet sind die `DBG_…`-Methoden (nur über AngelScript erreichbar), `ToneDown`, `EffOn`/`EffOff`, `SetCallbackRemoveEffect` und `CBLoadEffBase`-Hilfen.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEff2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0065F990` | 288 | vtable/String |
| 1 | `DBG_ShowWire` | – | | Debug-Methode (nur über AngelScript), im Binary nicht einzeln gefunden |
| 2 | `DBG_ShowSphere` | – | | Debug-Methode, nicht einzeln gefunden |
| 3 | `DBG_ShowEffFrm` | – | | Debug-Methode, nicht einzeln gefunden |
| 4 | `DBG_ShowEffMemoryLog` | – | | Debug-Methode, nicht einzeln gefunden |
| 5 | `DBG_ShowEffInfo` | `0x0065EB80` | 275 | Zeichenkette |
| 6 | `DBG_ClearDbgAxis` | – | | Debug-Methode, nicht einzeln gefunden |
| 7 | `OnInit` | `0x0065FAB0` | 1996 | vtable/String |
| 8 | `OnDestroy` | `0x0065ECA0` | 73 | vtable/String |
| 9 | `OnIdle` | `0x0065ECF0` | 129 | vtable/String |
| 10 | `RemoveAllLoadingEffsetList` | `0x0065ED80` | 17 | von Hand geprüft |
| 11 | `RemoveEffSet` | `0x0065EDA0` | 43 | von Hand geprüft |
| 12 | `PushToEffSetPool` | `0x0065EDD0` | 11 | von Hand geprüft |
| 13 | `PopFromEffSetPool` | `0x0065EDE0` | 11 | von Hand geprüft |
| 14 | `_BuildEffSetContainer` | `0x0065F080` | 232 | von Hand geprüft |
| 15 | `CreateEffSet` | `0x0065F170` | 903 | von Hand geprüft |
| 16 | `UseEffSet` | `0x0065F590` | 300 | von Hand geprüft |
| 17 | `GetSoundLength` | `0x0065F500` | 75 | von Hand geprüft |
| 18 | `SetGlobalVariable` | `0x0065EDF0` | 56 | von Hand geprüft |
| 19 | `SetMainCharacterFrame` | `0x0065EE30` | 32 | von Hand geprüft |
| 20 | `ToneDown` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `EffOn` | – | | Einzeiler an `AgcdEffGlobal`, eingebaut |
| 22 | `EffOff` | – | | Einzeiler an `AgcdEffGlobal`, eingebaut |
| 23 | `SetCallbackRemoveEffect` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 24 | `CBLoadEffBase` | `0x0065F6C0` | 710 | Zeichenkette |
| 25 | `CBRemovecharacter` | `0x0065EE50` | 57 | von Hand geprüft |
| 26 | `GetEffectSet` | `0x0065EE90` | 11 | von Hand geprüft |

18 von 27 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0065e960` (`0x0065E960`), `ctor_or_dtor_0065ea20` (`0x0065EA20`), `~AgcmEff2` (`0x0065F060`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `AgcdEffGlobal+0x30` | `Rahmen der Hauptfigur` | `SetGlobalVariable`, `SetMainCharacterFrame` |
| `AgcdEffGlobal+0x34` | `Clump der Hauptfigur` | `SetGlobalVariable`, `SetMainCharacterFrame` |
| `AgcdEffGlobal+0x38 / 0x3C` | `Welt / Kamera` | `SetGlobalVariable` |

## OnAddModule (0x0065F990)

Holt elf Module und trägt sie in `AgcdEffGlobal` ein: [`AgcmRender`](AgcmRender.md), [`AgcmSound`](AgcmSound.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`ApmOcTree`](ApmOcTree.md), [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmPostFX`](AgcmPostFX.md), [`AgcmUVAnimation`](AgcmUVAnimation.md), `AgcmEff2`, `AgcmCharacter` (Zeichenketten im Dekompilat, gleiche Reihenfolge wie in der Quelle). Der Zugriff auf die Singleton-Instanz `AgcdEffGlobal::bGetInst` läuft über `0x00709B40`. Bei `AgcmCharacter` wird der Rückruf `CBRemovecharacter` (`0x0065EE50`) angemeldet.

## OnInit (0x0065FAB0)

1996 Byte. Holt [`AgcmEventEffect`](AgcmEventEffect.md), setzt Texturpfad und Vertexpuffer, baut über `_BuildEffSetContainer` (`0x0065F080`) den Effekt-Behälter und meldet über AngelScript die Debug-Methoden `DBG_ShowWire`, `DBG_ShowSphere`, `DBG_ShowEffFrm`, `DBG_ShowEffMemoryLog`, `DBG_ShowEffInfo(uint)` sowie die Variablen `m_chkEffSetID`, `m_skipEffSetID`, `m_axisDbgType`, `m_dbgBaseIndex` und `DBG_ClearDbgAxis` an (Zeichenketten im Binary).

## Effekte erzeugen und verwenden

`CreateEffSet` (`0x0065F170`, 903 Byte) ist die größte Methode; `UseEffSet` (`0x0065F590`) ruft sie. `GetSoundLength` (`0x0065F500`) sucht den Effektsatz (`FindEffSet` `0x0075FF00`), erhöht die Referenz, liest die Tonlänge und gibt frei. `GetEffectSet` (`0x0065EE90`) ist ein Aufruf von `FindEffSet`. `RemoveAllLoadingEffsetList` (`0x0065ED80`), `RemoveEffSet` (`0x0065EDA0`), `PushToEffSetPool` (`0x0065EDD0`) und `PopFromEffSetPool` (`0x0065EDE0`) sind Einzeiler an `AgcdEffCtrlMng`/`AgcdEffSetMng` und liegen in dieser Reihenfolge hintereinander wie in der Quelle.

## Globale Zeiger

`SetGlobalVariable` (`0x0065EDF0`) schreibt vier Zeiger (Clump, Rahmen, Welt, Kamera) in `AgcdEffGlobal` (`+0x34`, `+0x30`, `+0x38`, `+0x3C`), `SetMainCharacterFrame` (`0x0065EE30`) zwei davon (`+0x30` Rahmen, `+0x34` Clump).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Einzeiler-Zuordnung (`RemoveAllLoadingEffsetList` bis `PopFromEffSetPool`, `SetGlobalVariable`, `SetMainCharacterFrame`, `GetEffectSet`) stützt sich auf Aufrufziele, Anzahl der Schreibzugriffe und die Quellreihenfolge.
- `CreateEffSet` und `UseEffSet` sind über Größe und Aufrufbeziehung (Verwenden ruft Erzeugen) zugeordnet, nicht Zeile für Zeile verglichen.
- Die Offsets in `AgcdEffGlobal` stammen aus den beiden Schreibfunktionen; die Feldnamen der Quelle wurden nicht nachgeprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 5, gemeinsamer Rumpf: 1, nicht im Client: 2, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmPostFX`](AgcmPostFX.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmSound`](AgcmSound.md), [`AgcmUVAnimation`](AgcmUVAnimation.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmSound`](AgcmSound.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md)
