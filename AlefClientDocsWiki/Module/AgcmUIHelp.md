# AgcmUIHelp (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIHelp` (Hilfe-Fenster mit Baumliste) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIHelp/AgcmUIHelp.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 10 von 10 Quellmethoden sind zugeordnet; neu sind `RefreshUI` und `ReleaseHelp`; die leere `OnDestroy` steht als zusammengefalteter Rumpf.
- **UI:** 1 Funktion, 1 Anzeige, 3 Benutzerdaten – wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIHelp.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0061D260` | 966 | vtable/String |
| 1 | `OnAddModule` | `0x0061D190` | 198 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `ReadHelp` | `0x0061C970` | 878 | Zeichenkette |
| 4 | `RefreshUI` | `0x0061CCF0` | 160 | ver |
| 5 | `ReleaseHelp` | `0x0061CD90` | 195 | ver |
| 6 | `WriteHelp` | `0x0061CE60` | 235 | as-register |
| 7 | `SetEditMode` | `0x0061CF60` | 83 | as-register |
| 8 | `CBDisplayContent` | `0x0061CFC0` | 149 | UI-Registrierung |
| 9 | `CBChangeItem` | `0x0061D060` | 247 | UI-Registrierung |

10 von 10 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x0061C8D0`), `~AgcmUIHelp` (`0x0061D160`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB9C` | `Anzahl Hilfeeinträge (`m_lNumHelp`)` | `ReleaseHelp`, `RefreshUI` |
| `0xBA0 / 0xBA4` | `Felder mit Titeln / Inhalten` | `ReleaseHelp` |
| `0xBB0 / 0xBB4 / 0xBB8` | `Benutzerdaten `Help_Item` / `Help_Depth` / `Help_CurrentItem`` | `OnAddModule`, `RefreshUI` |

## Vtable

Vtable bei `0x008C1444`: Slot 0 Destruktor `0x0061D160`, 1 `OnAddModule` (`0x0061D190`), 2 `OnInit` (`0x0061D260`), 6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. die leere `OnDestroy`).

## Registrierung (OnAddModule, 0x0061D190)

Holt [`AgcmUIManager2`](AgcmUIManager2.md) und legt an: Benutzerdaten `Help_Item`, `Help_Depth` und `Help_CurrentItem`, die Anzeige `Help_Content` (`CBDisplayContent`, `0x0061CFC0`) und die Funktion `Help_ChangeItem` (`CBChangeItem`, `0x0061D060`). Reihenfolge wie in der Quelle.

## Hilfetexte

`ReadHelp` (`0x0061C970`) liest die Hilfetexte in Felder (`m_pszHelpItem`, `m_pszHelpContent`, Tiefe `m_plHelpDepth`), `RefreshUI` (`0x0061CCF0`) legt Zeiger und Anzahl in die Benutzerdaten und aktualisiert sie (drei Einträge, wie in der Quelle), `ReleaseHelp` (`0x0061CD90`) gibt alle Felder frei, `WriteHelp` (`0x0061CE60`) schreibt sie zurück.

## Skript-Anbindung (OnInit, 0x0061D260)

Wenn [`AgcmUIConsole`](AgcmUIConsole.md) vorhanden ist, registriert `OnInit` den Skript-Typ `AgcmUIHelp` mit den Methoden `SetEditMode(bool)` und `WriteHelp(string)` – ein Bearbeitungswerkzeug für die Hilfetexte über die Konsole.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x0061D190`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**UserData** (3)

| Name | Id | Handler |
|---|---:|---|
| `Help_Item` | 0 | – |
| `Help_Depth` | 0 | – |
| `Help_CurrentItem` |  | – |

**Anzeige** (1)

| Name | Id | Handler |
|---|---:|---|
| `Help_Content` | 0 | – |

**Funktion** (1)

| Name | Id | Handler |
|---|---:|---|
| `Help_ChangeItem` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`RefreshUI`, `ReleaseHelp`, `OnAddModule`).

## Grenzen

- `ReadHelp` und `WriteHelp` waren bereits zugeordnet und wurden hier nicht neu gelesen.
- Die Hilfetexte selbst (Datei und Format) wurden nicht untersucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIConsole`](AgcmUIConsole.md), [`AgcmUIManager2`](AgcmUIManager2.md)
