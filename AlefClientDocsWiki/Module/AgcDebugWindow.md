# AgcDebugWindow (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AgcDebugWindow` (Debug-Fenster, erbt von `AgcWindow`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Vtable, EP8-Quelle `Modules/AClient/AgcmUIDebugInfo/AgcDebugWindow.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 9 von 11 Quellmethoden sind zugeordnet (`OnInit` und `OnKeyUp` als gemeinsame Rümpfe); `RenderProfile` und `FindMaxItem` sind nur mit `_PROFILE_` übersetzt und fehlen.
- **Modi:** Speicher, Objekte, Grafik, Netzwerk; Profiler und Ton sind leer.
- **Hinweis:** Die Textur-Zähler in `RenderGraphic` zeigen in Quelle und Binary immer 0.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcDebugWindow.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 1 | `OnWindowRender` | `0x0076BB80` | 82 | vtable/String |
| 2 | `OnKeyDown` | `0x0076BC40` | 155 | vtable/String |
| 3 | `OnKeyUp` | `0x007AA0B0` | 5 | gleiche Adresse wie `gemeinsamer Rumpf (liefert 0)` (vom Linker zusammengefaltet) |
| 4 | `RenderProfile` | – | | nur mit `_PROFILE_` übersetzt, im Binary nicht vorhanden |
| 5 | `RenderMemory` | `0x0076AB70` | 217 | Zeichenkette |
| 6 | `RenderObject` | `0x0076B050` | 2355 | Zeichenkette |
| 7 | `RenderGraphic` | `0x0076AD90` | 696 | Zeichenkette |
| 8 | `RenderNetwork` | `0x0076AC80` | 107 | Zeichenkette |
| 9 | `FindMaxItem` | – | | nur mit `_PROFILE_` übersetzt, im Binary nicht vorhanden |
| 10 | `ChangeTextureFilterMode` | `0x0076B990` | 474 | manual |

9 von 11 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0076ab30` (`0x0076AB30`), `ctor_or_dtor_0076ab60` (`0x0076AB60`), `CBTextureCount` (`0x0076AC60`), `CBTextureRefCount` (`0x0076AC70`), `CBMaterialFilter` (`0x0076ACF0`), `CBGeometryFilter` (`0x0076AD10`), `CBAtomicFilter` (`0x0076AD30`), `~AgcDebugWindow` (`0x0076AD60`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xE8` | `Zeiger auf [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md)` | Konstruktor, alle `Render…` |
| `0xEC` | `Zeit des letzten Profiler-Wechsels (`m_ulPrevClockCount`)` | Konstruktor |
| `0x100` | `Textur-Filtermodus (`m_lFilterMode`)` | `ChangeTextureFilterMode` |

## Vtable

Vtable bei `0x008E0B2C` (Basis `AgcWindow`): Slot 0 Destruktor `0x0076AD60`, 1/2 `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`), 8 `OnWindowRender` (`0x0076BB80`), 9 `OnKeyDown` (`0x0076BC40`), 10 `OnKeyUp` (der Rumpf `0x007AA0B0`, liefert 0). Konstruktor `0x0076AB30` (Parameter: Zeiger auf `AgcmUIDebugInfo`).

## Darstellung (OnWindowRender)

Zeichnet nur, wenn das Modul und [`AgcmFont`](AgcmFont.md) vorhanden sind: Schrift beginnen, dann nach Modus: 1 Speicher (`RenderMemory`, `0x0076AB70`), 2 Objekte (`RenderObject`, `0x0076B050`, 2355 Byte), 3 Grafik (`RenderGraphic`, `0x0076AD90`), 5 Netzwerk (`RenderNetwork`, `0x0076AC80`), danach Schrift beenden. Modus 0 (Profiler) und 4 (Ton) zeichnen nichts: `RenderProfile` und `FindMaxItem` sind nur mit `_PROFILE_` übersetzt und fehlen im Binary.

## Tasten (OnKeyDown, 0x0076BC40)

Taste `-` (`0x2D`): Mit gedrückter linker Alt-Taste wird das Fenster ausgeblendet (`EnableDebugInfo(FALSE)`), ohne Umschalttasten wechselt es den Modus (`(Modus + 1) % 6`). Taste `=` (`0x3D`) ruft `ChangeTextureFilterMode` (`0x0076B990`): Es setzt den Textur-Filtermodus aller Charakter-, Gegenstands- und Objektvorlagen (über die Filter-Callbacks `CBAtomicFilter` `0x0076AD30`, `CBGeometryFilter` `0x0076AD10`, `CBMaterialFilter` `0x0076ACF0`) und schaltet die Stufe weiter (0…`rwFILTERLINEARMIPLINEAR`). Die Profiler-Tasten (`1`…`0`, Bild-auf/ab usw.) gibt es nur mit `_PROFILE_`.

## Anzeigen

`RenderMemory`: je Speicherpool eine Zeile „MemoryPool(%02d) : Size(%d) belegt/Größe [Spitze] - Typname“ (die `_CPPRTTI`-Fassung). `RenderNetwork`: „Receive Queue : %d“ (Zähler der Empfangswarteschlange). `RenderGraphic`: Position des eigenen Charakters mit Schattenpuffer-Flag, Gras- und Effektzähler sowie „Texture Count“ und „Texture Ref Count“; beide Textur-Zähler zeigen immer 0, weil die Quelle die Zähler nach den Schleifen (`CBTextureCount` `0x0076AC60`, `CBTextureRefCount` `0x0076AC70`) wieder auf 0 setzt – das Binary tut dasselbe. `RenderObject`: Zähler und geladene Vorlagen von Karte, Objekten, Charakteren und Gegenständen sowie die Warteschlangen des Ressourcenladers.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnWindowRender`, `OnKeyDown`, `RenderGraphic`, Filter-Callbacks).

## Grenzen

- `RenderObject` (2355 Byte) und `ChangeTextureFilterMode` (474 Byte) wurden über Zeichenketten, Aufrufe und Größe zugeordnet, nicht Zeile für Zeile verglichen.
- Die Filter-Callbacks `CBMaterialFilter`, `CBGeometryFilter` und `CBAtomicFilter` sind freie Funktionen der Quelle; sie stehen hier unter dem Namen der Klasse, in deren Datei sie liegen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht als eigene Funktion: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmFont`](AgcmFont.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md)
- **Erwähnt in:** [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md)
