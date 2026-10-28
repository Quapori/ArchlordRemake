# AgcmUIDebugInfo (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIDebugInfo` (Debug-Fenster für Speicher, Objekte, Grafik und Netzwerk) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable und Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmUIDebugInfo/AgcmUIDebugInfo.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 6 von 6 Quellmethoden sind zugeordnet (`OnInit` und `OnIdle` als gemeinsame Rümpfe); neu sind `EnableDebugInfo` und `SetDebugMode`.
- **Nicht erreichbar:** Nichts im Binary ruft `EnableDebugInfo(TRUE)` auf; das Fenster kann in diesem Client nicht geöffnet werden.
- **Profiler:** `OnIdle` ist leer (`_PROFILE_` ist nicht gesetzt).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIDebugInfo.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00683C00` | 296 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf (Vtable-Slot 3)` (vom Linker zusammengefaltet) |
| 3 | `OnDestroy` | `0x00683DF0` | 50 | vtable/String |
| 4 | `EnableDebugInfo` | `0x00683D30` | 140 | manual |
| 5 | `SetDebugMode` | `0x00683DC0` | 13 | manual |

6 von 6 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIDebugInfo` (`0x00683AF0`), `ctor_or_dtor` (`0x00683BA0`), `~AgcmUIDebugInfo` (`0x00683DD0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98` | `Zeiger auf [`AgcmUIManager2`](AgcmUIManager2.md)` | `EnableDebugInfo` |
| `0xB9C` | `eingebettetes Debug-Fenster ([`AgcDebugWindow`](AgcDebugWindow.md))` | `EnableDebugInfo` |
| `0xC84` | `Zeiger des Fensters auf das Modul (Fenster `+0xE8`)` | Konstruktor |
| `0xCA0 / 0xCA4` | `Flag „Debug-Info an“ / Modus (0…5)` | `EnableDebugInfo`, `SetDebugMode` |
| `0xCB4 / 0xCCC / 0xCD8` | `Zeiger auf `AgcmCharacter` / [`AgcmShadow2`](AgcmShadow2.md) / [`AgcmFont`](AgcmFont.md)` | `RenderGraphic`, `OnWindowRender` |

## Vtable

Vtable bei `0x008CBB9C`: Slot 0 Destruktor `0x00683DD0`, 1 `OnAddModule` (`0x00683C00`), 2/6 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (u. a. `OnIdle`), 7 `OnDestroy` (`0x00683DF0`). Der Konstruktor (`0x00683AF0`) baut das Debug-Fenster (`AgcDebugWindow`) ein, aktiviert `OnIdle` (`EnableIdle(TRUE)`) und gibt dem Fenster einen Zeiger auf das Modul.

## Registrierung (OnAddModule, 0x00683C00)

Holt 16 Module ohne Prüfung (`AgcmUIManager2`, [`ApmMap`](ApmMap.md), [`AgcmMap`](AgcmMap.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgpmItem`](AgpmItem.md), [`AgcmItem`](AgcmItem.md), [`ApmObject`](ApmObject.md), [`AgcmObject`](AgcmObject.md), [`AgcmGrass`](AgcmGrass.md), `AgcmShadow2`, [`AgcmRender`](AgcmRender.md), [`AgcmSound`](AgcmSound.md), `AgcmFont`, [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmEff2`](AgcmEff2.md)) und liefert immer TRUE. Es legt keine UI-Funktionen, Anzeigen oder Ereignisse an.

## Ein- und Ausschalten

`EnableDebugInfo` (`0x00683D30`) hängt das Fenster bei `AgcmUIManager2` ein und setzt es auf 1024 × 768 (`0x400` × `0x300`) in die Mitte des Elternfensters, oder entfernt es wieder. `SetDebugMode` (`0x00683DC0`) setzt nur die Modusnummer (`+0xCA4`). `OnDestroy` ruft `EnableDebugInfo(FALSE)`. **Aufrufer:** Im ganzen Binary ruft nur `AgcDebugWindow::OnKeyDown` (`0x0076BC40`) diese beiden Funktionen auf. `EnableDebugInfo(TRUE)` hat keinen Aufrufer, das Fenster lässt sich in diesem Client also nicht einblenden (die Umschaltung im Fenster wäre erst nach dem Einblenden erreichbar).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierung, `EnableDebugInfo`, `SetDebugMode`).

## Grenzen

- Dass `EnableDebugInfo(TRUE)` nirgends aufgerufen wird, beruht auf dem Aufrufgraphen; indirekte Aufrufe über Funktionszeiger oder Skripte wären darin nicht sichtbar.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcDebugWindow`](AgcDebugWindow.md), [`AgcmEff2`](AgcmEff2.md), [`AgcmFont`](AgcmFont.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmItem`](AgcmItem.md), [`AgcmMap`](AgcmMap.md), [`AgcmObject`](AgcmObject.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmShadow2`](AgcmShadow2.md), [`AgcmSound`](AgcmSound.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItem`](AgpmItem.md), [`ApmMap`](ApmMap.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcDebugWindow`](AgcDebugWindow.md)
