# AgcmUIConsole (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse `AgcmUIConsole` (Skript-Konsole: Modul, Server-Befehle) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIConsole/AgcmUIConsole.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 7 von 7 Quellmethoden sind zugeordnet; neu sind `On`, `Off`, `sendToServerCommand`; `OnDestroy` steht als zusammengefalteter Rumpf. Die freien Funktionen der Datei wurden zusätzlich benannt (`AgcmUIConsole_static::print` usw.).
- **Server-Befehle:** Paket der Skript-Operation 0 mit Self-Character-ID.
- **Abweichungen:** keine festgestellt.
- **Hinweis:** Die Konsole ist ein Entwicklerwerkzeug; ob und wie sie im Spiel aufrufbar ist (Tastenbelegung), wurde nicht untersucht.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIConsole.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005C5600` | 101 | vtable/String |
| 1 | `OnInit` | `0x005C50F0` | 969 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `On` | `0x005C27E0` | 39 | ver |
| 4 | `Off` | `0x005C2810` | 48 | ver |
| 5 | `sendToServerCommand` | `0x005C2840` | 175 | ver |
| 6 | `CBRegisterServerKeyword` | `0x005C54C0` | 311 | Callback-Registrierung |

7 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_005c3e90` (`0x005C3E90`), `ctor_or_dtor_005c4240` (`0x005C4240`), `~AgcmUIConsole` (`0x005C4300`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1148` | `Zeiger auf `AgcmCharacter`` | `sendToServerCommand` |
| `0xBCC` | `Konsolenfenster `console_` (eingebettet)` | `On`, `Off` |
| `0x1140` | `Zeiger auf [`AgcmUIManager2`](AgcmUIManager2.md)` | `On`, `Off` |

## Umfang

`AgcmUIConsole.cpp` enthält zwei Klassen: das Modul `AgcmUIConsole` (dieser Bericht) und das Konsolenfenster `AgcConsole` (eigener Bericht [AgcConsole](AgcConsole.md)) sowie einige freie Funktionen für die Skriptsprache.

## Vtable

Vtable bei `0x008BBB54`: Slot 0 Destruktor `0x005C4300`, 1 `OnAddModule` (`0x005C5600`), 2 `OnInit` (`0x005C50F0`), 6/7 `return TRUE`-Rumpf `0x0067AC90` (u. a. die leere `OnDestroy`).

## Registrierung (OnAddModule, 0x005C5600)

Holt `AgcmUIManager2`, [`AgpmScript`](AgpmScript.md) und `AgcmCharacter` und meldet bei `AgpmScript` den Callback für Server-Schlüsselwörter an (`CBRegisterServerKeyword`, `0x005C54C0`): Die Wörter, getrennt durch `;`, werden in die Schlagwortliste der Konsole und in die Menge der Server-Schlüsselwörter eingetragen. Reihenfolge wie in der Quelle.

## Skriptfunktionen (OnInit, 0x005C50F0)

Die Funktion registriert beim Skript-Motor dieselben acht freien Funktionen wie die Quelle und, wo vorgesehen, ein Schlüsselwort in der Konsole. Danach `console_.init()` ([`AgcConsole`](AgcConsole.md):init`, `0x005C44A0`), `On()`, `moveCenter()` und `Off()`; `On` und `Off` sind in `OnInit` eingebaut, bestehen aber auch als eigene Funktionen (`0x005C27E0`, `0x005C2810`).

| Skript-Signatur | Adresse | Schlüsselwort |
|---|---|---|
| `void testFormatString()` | `0x005C2A00` | `testFormatString()` |
| `void exit()` | `0x005C29C0` | `exit()` |
| `void print(string &in)` | `0x005C1F40` | `print( )` |
| `void print(int)` | `0x005C1F70` | – |
| `void print(uint)` | `0x005C2040` | – |
| `void print(float)` | `0x005C2110` | – |
| `uint getRenderStateD3D(uint)` | `0x005C21E0` | `getRenderStateD3D( )` |
| `uint getTextureStageStateD3D(uint, uint)` | `0x005C2280` | `getTextureStageStateD3D( , )` |

## Server-Befehl senden (sendToServerCommand, 0x005C2840)

Baut mit `AgpmScript::MakeScriptPacket` (`0x00588100`) ein Skript-Paket (Operation 0 = Befehl) aus dem Befehlstext und der ID des Self-Characters und sendet es (`SendPacket`, `0x004E45A0`). Die Funktion hängt als Rückruf im Konsolenobjekt (im Konstruktor `0x005C4240` zusammen mit dem Modulzeiger gespeichert).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnInit`-Registrierungen, `On`/`Off`, `sendToServerCommand`).

## Grenzen

- `getRenderStateD3D` und `getTextureStageStateD3D` (Adressen `0x005C21E0`, `0x005C2280`) und `exitConsole` (`0x005C29C0`) fehlen in der Funktionsliste des Exports; die Adressen stammen aus den Registrierungen in `OnInit`.
- Die Funktion `print_ui_console` am Dateiende wurde nicht zugeordnet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcConsole`](AgcConsole.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmScript`](AgpmScript.md)
- **Erwähnt in:** [`AgcConsole`](AgcConsole.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmUIHelp`](AgcmUIHelp.md)
