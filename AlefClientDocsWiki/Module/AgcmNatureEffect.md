# AgcmNatureEffect (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmNatureEffect` (Wetter- und Naturpartikel: Regen, Schnee, Wind) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Modulaufbau, Wetter-Steuerung, Wurzelgitter, Aktualisierung und Laden sind zugeordnet; `SaveNatureEffectInfoToINI` fehlt im Binary, `SetWind`, `EndNatureEffect` und `StopNatureEffect` sind eingebaut oder nicht einzeln gefunden.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmNatureEffect.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00639ED0` | 106 | vtable/String |
| 1 | `OnInit` | `0x0063AED0` | 681 | vtable/String |
| 2 | `OnLuaInitialize` | `0x0063A020` | 87 | vtable/String |
| 3 | `SetNatureEffect` | `0x0063A080` | 352 | as-register |
| 4 | `SetWind` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 5 | `OnDestroy` | `0x006391B0` | 108 | vtable/String |
| 6 | `OnIdle` | `0x00639890` | 46 | vtable/String |
| 7 | `WindIdleProcess` | `0x006389B0` | 205 | von Hand geprüft |
| 8 | `ReleaseNatureEffectAll` | `0x00638A80` | 108 | von Hand geprüft |
| 9 | `StopNatureEffect` | – | | in `CBNatureEffectChanged` und `SetNatureEffect` eingebaut |
| 10 | `StartNatureEffect` | `0x006398C0` | 1295 | von Hand geprüft |
| 11 | `EndNatureEffect` | – | | keine eigene Funktion gefunden |
| 12 | `InitRoots` | `0x00638B70` | 399 | von Hand geprüft |
| 13 | `RefreshRoots` | `0x00638D00` | 739 | von Hand geprüft |
| 14 | `UpdateNatureEffects` | `0x00639220` | 967 | von Hand geprüft |
| 15 | `CB_NATUREEFFECT_POSTRENDER` | `0x006395F0` | 469 | Callback-Registrierung |
| 16 | `LoadNatureEffectInfoFromINI` | `0x0063A6D0` | 2041 | von Hand geprüft |
| 17 | `SaveNatureEffectInfoToINI` | – | | keine Funktion im Binary (nicht aufgerufen, vom Linker entfernt) |
| 18 | `CBNatureEffectChanged` | `0x00639E10` | 186 | Callback-Registrierung |

15 von 19 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0063a4c0` (`0x0063A4C0`), `ctor_or_dtor_0063a600` (`0x0063A600`), `~AgcmNatureEffect` (`0x0063A6B0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA4 / 0xBA8` | `Merker „Stopp läuft“ / Tickzahl bei Start` | `CBNatureEffectChanged` |
| `this+0xBD8` | `Wurzelliste (`m_listRoot`)` | `CBNatureEffectChanged` |

## OnAddModule und OnInit

`OnAddModule` (`0x00639ED0`) holt [`AgcmRender`](AgcmRender.md), [`AgcmMap`](AgcmMap.md) und [`AgpmNatureEffect`](AgpmNatureEffect.md) (Zeichenketten im Dekompilat, gleiche Reihenfolge wie die Quelle), meldet bei `AgcmRender` den Nach-Render-Rückruf `CB_NATUREEFFECT_POSTRENDER` (`0x006395F0`) und bei `AgpmNatureEffect` `CBNatureEffectChanged` (`0x00639E10`) an. `OnInit` (`0x0063AED0`) meldet über AngelScript die Methode `void SetNatureEffect(int)` an (Zeichenkette im Binary). `OnLuaInitialize` (`0x0063A020`) legt `SetNatureEffect` als Lua-Funktion an.

## Wetter starten und beenden

`CBNatureEffectChanged` und `SetNatureEffect` (`0x0063A080`) rufen je nach Wert `-1` die weiche oder die harte Beendigung (`StopNatureEffect`, in beiden Aufrufern eingebaut: `ReleaseNatureEffectAll` `0x00638A80` bzw. Rückruf `AGCMNATUREEFFECT_END` über `EnumCallback`) und danach `StartNatureEffect` (`0x006398C0`, 1295 Byte). Der Name `NatureEffect::ctor_or_dtor` für `0x006398C0` war falsch.

## Wurzelgitter und Aktualisierung

`InitRoots` (`0x00638B70`) legt um die Kameraposition ein 5×5-Gitter von Wurzeln an (Mittelpunkt, Radius, Bereichsgrenzen), `RefreshRoots` (`0x00638D00`, 739 Byte) verschiebt es bei Bewegung. `UpdateNatureEffects` (`0x00639220`, 967 Byte) wird von `OnIdle` (`0x00639890`) gerufen; direkt danach `WindIdleProcess` (`0x006389B0`), erkennbar an den Sinus-/Kosinus-Aufrufen (`sin·sin·cos·sin` wie in der Quelle).

## Laden

`LoadNatureEffectInfoFromINI` (`0x0063A6D0`, 2041 Byte) liest die Datei über `ApModuleStream` mit den Schlüsseln `TEXTURE_NAME`, `NEFFECT_ID` und dem Format `%d:%s` (Zeichenketten im Binary). `SaveNatureEffectInfoToINI` ist im Binary nicht vorhanden.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `InitRoots`/`RefreshRoots`/`UpdateNatureEffects` sind über Aufrufbeziehungen, Größen und die Quellreihenfolge zugeordnet, nicht Zeile für Zeile verglichen.
- Die Offsets `0xBA4`, `0xBA8`, `0xBD8` stammen aus `CBNatureEffectChanged`; ihre Namen in der Quelle wurden nicht nachgeprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 3, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `StopNatureEffect` | 28 | `0x00638AF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmMap`](AgcmMap.md), [`AgcmRender`](AgcmRender.md), [`AgpmNatureEffect`](AgpmNatureEffect.md)
- **Erwähnt in:** [`AgcmEventNature`](AgcmEventNature.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md)
