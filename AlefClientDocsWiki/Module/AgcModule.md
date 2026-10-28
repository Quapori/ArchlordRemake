# AgcModule (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Basisklasse `AgcModule` (Zugriff auf Welt, Kamera, Lichter der Engine; Verzögerungstakt; Sperren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcModule/AgcModule.cpp`/`.h` und `AgcEngine.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 5 von 9 Quellmethoden sind zugeordnet (`GetWorld`, `GetCamera`, `GetAmbientLight`, `GetDirectionalLight`, `CheckDelay`). `LockRender`, `UnlockRender`, `LockFrame` und `UnlockFrame` sind wegen leerer Engine-Methoden eingebaut und auf den Aufruf von `GetModuleManager` zusammengeschrumpft.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcModule.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `LockRender` | – | | eingebaut: Engine-Methode leer, nur `GetModuleManager`-Aufruf bleibt |
| 1 | `UnlockRender` | – | | eingebaut: Engine-Methode leer, nur `GetModuleManager`-Aufruf bleibt |
| 2 | `LockFrame` | – | | eingebaut: Engine-Methode leer, nur `GetModuleManager`-Aufruf bleibt |
| 3 | `UnlockFrame` | – | | eingebaut: Engine-Methode leer, nur `GetModuleManager`-Aufruf bleibt |
| 4 | `GetWorld` | `0x007025C0` | 24 | von Hand geprüft |
| 5 | `GetCamera` | `0x007025E0` | 24 | von Hand geprüft |
| 6 | `GetAmbientLight` | `0x00702600` | 24 | von Hand geprüft |
| 7 | `GetDirectionalLight` | `0x00702620` | 24 | von Hand geprüft |
| 8 | `CheckDelay` | `0x00702640` | 39 | von Hand geprüft |

5 von 9 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `UserInputMessageProc` (`0x004FA120`), `~AgcModule_006e3af0` (`0x006E3AF0`), `~AgcModule_006e97f0` (`0x006E97F0`), `AgcModule` (`0x00702530`), `~AgcModule_body` (`0x007025A0`), `scalar_deleting_dtor` (`0x00702670`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x30` | `Zeiger auf den Modulmanager (`ApModule`)` | `GetModuleManager` |
| `this+0xB84` | ``m_uType`` | Konstruktor |
| `this+0xB88` | ``m_uPriority`` | Konstruktor |
| `this+0xB8C` | ``m_bRegistered`` | Konstruktor |
| `this+0xB90 / 0xB94` | ``m_uDelayTick` / `m_uLastTick`` | `CheckDelay` |
| `g_pEngine+0x12C20 / 0x12C24 / 0x12C34 / 0x12C38` | `Welt / Kamera / Umgebungslicht / gerichtetes Licht` | `GetWorld`, `GetCamera`, `GetAmbientLight`, `GetDirectionalLight` |

## Vtable und Aufbau

`AgcModule` ist die Basisklasse aller Client-Module (von `ApModule` abgeleitet). Konstruktor `0x00702530` (ruft den `ApModule`-Konstruktor `0x004E4700`, trägt die Vtable `0x008DAC3C` ein, nullt `m_uType`/`m_uPriority`/`m_bRegistered` bei `this+0xB84/0xB88/0xB8C`, setzt den Modultyp 2 = Client über `SetModuleType` `0x004E4610` und nullt `m_uDelayTick`/`m_uLastTick` bei `+0xB90/0xB94`). Destruktorrumpf `0x007025A0`, Löschwrapper (Vtable-Slot 0) `0x00702670`.
Die vier eigenen Virtuellen (Vtable-Slots 13 bis 16) sind in der Quelle leer und zeigen auf gemeinsame Leer-Rümpfe: `OnCameraStateChange` und `OnLuaInitialize` auf `0x005BDCF0` (`ret 4`), `OnTerminate` auf `0x007C6910` (`ret`), `UserInputMessageProc` auf `0x004FA120` (`ret 8`). Der Name `AgcModule::UserInputMessageProc` für `0x004FA120` stammt aus dem Vtable-Abgleich; der Rumpf gehört allen Funktionen dieser Form.

## Zugriff auf die Engine

`GetWorld` (`0x007025C0`), `GetCamera` (`0x007025E0`), `GetAmbientLight` (`0x00702600`) und `GetDirectionalLight` (`0x00702620`) sind je 24 Byte: sie rufen `GetModuleManager` (`0x004E45C0`, liefert `this+0x30`) und lesen bei vorhandenem Manager aus der globalen Engine (`g_pEngine`, `0x009A1D18`) das Feld bei `+0x12C20` (Welt), `+0x12C24` (Kamera), `+0x12C34` (Umgebungslicht) bzw. `+0x12C38` (gerichtetes Licht); sonst 0. Die Offsets passen zur Feldfolge in `AgcEngine.h` (Welt, Kamera, Nah-/Fernebene, Nebel, dann beide Lichter).
`CheckDelay` (`0x00702640`) vergleicht den Takt mit `m_uLastTick + m_uDelayTick` (`this+0xB94`/`+0xB90`), setzt bei Erreichen `m_uLastTick` und liefert 1; einziger Aufrufer ist `0x00605490`.

## Sperren (LockRender/LockFrame)

`LockRender`, `UnlockRender`, `LockFrame` und `UnlockFrame` sind im Binary keine eigenen Funktionen. In der Quelle ruft jede `GetModuleManager()` und dann `g_pEngine->LockRender()` bzw. `…LockFrame()`; diese Engine-Methoden sind in `AgcEngine.h` leere Inline-Funktionen (Zeilen 281 und 285). Übrig bleibt der Aufruf von `GetModuleManager`, den der Compiler als Sprungverteiler `0x007025B0` (`jmp 0x004E45C0`) einbaut: 96 Funktionen rufen ihn (z. B. [`AgcmShadow`](AgcmShadow.md):Render` mehrfach, ohne Auswertung des Ergebnisses). Das erklärt die vielen „thunk“-Aufrufe in den Dekompilaten.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass die Lock-Methoden eingebaut sind, folgt aus dem Quelltext (leere Engine-Methoden) und dem Muster der Aufrufe von `0x007025B0` ohne weiteren Engine-Aufruf; ein vollständiger Abgleich aller 96 Aufrufer wurde nicht gemacht.
- Die Zuordnung der Licht-Getter beruht auf den Feldoffsets in `AgcEngine.h` (Umgebungslicht vor gerichtetem Licht), nicht auf der Aufrufreihenfolge in anderen Modulen.
- Die Bedeutung von `m_uType`-Werten und `m_uPriority` wurde nicht verfolgt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmShadow`](AgcmShadow.md)
- **Erwähnt in:** [`AgcmRefinery`](AgcmRefinery.md), [`AgcmTuner`](AgcmTuner.md), [`AgcmUISocialAction`](AgcmUISocialAction.md)
