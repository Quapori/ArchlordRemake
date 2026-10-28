# AgcmEventTeleport (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventTeleport` (Teleport-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, die drei Rückrufe und die beiden Teleport-Anfragen sind zugeordnet; `OnInit`/`OnDestroy` sind der gemeinsame `return TRUE`-Rumpf.
- **OnAddModule:** sechs Module ([`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`ApmEventManager`](ApmEventManager.md), [`AgcmEventManager`](AgcmEventManager.md), [`AgpmEventTeleport`](AgpmEventTeleport.md), [`AgpmArchlord`](AgpmArchlord.md)); Anmeldungen: Ereignis `8` → `CBExecuteEvent` (`0x006DD930`), `CBReceivedRequestResult` (`0x006DDA20`) und `CBReceiveTeleportLoading` (`0x006DDA70`).
- **Anfragen:** `RequestTeleport` (`0x006DDAA0`) ruft `AgpmEventTeleport::SendTeleportInfo` (`0x00559D50`) nach Prüfung von Ereignis, Erzeuger und Punktname; `RequestTeleportReturnOnly` (`0x006DDAE0`) ruft `SendTeleportReturn` (`0x00559DF0`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventTeleport.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DDB40` | 233 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `CBExecuteEvent` | `0x006DD930` | 230 | Callback-Registrierung |
| 4 | `CBReceivedRequestResult` | `0x006DDA20` | 69 | Callback-Registrierung |
| 5 | `CBReceiveTeleportLoading` | `0x006DDA70` | 36 | Callback-Registrierung |
| 6 | `RequestTeleport` | `0x006DDAA0` | 63 | von Hand geprüft |
| 7 | `RequestTeleportReturnOnly` | `0x006DDAE0` | 40 | von Hand geprüft |
| 8 | `SetCallbackSelectTeleportPoint` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 9 | `SetCallbackCannotUseForTransforming` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 10 | `SetCallbackCannotUseForCombatMode` | – | | Einzeiler (`SetCallback`), zusammengefaltet |

8 von 11 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DD8D0`), `~AgcmEventTeleport` (`0x006DDB10`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger auf `AgpmCharacter`` | `OnAddModule` |
| `this+0xB9C` | `Zeiger auf `AgcmCharacter`` | `OnAddModule` |
| `this+0xBA0` | `Zeiger auf `ApmEventManager`` | `OnAddModule` |
| `this+0xBA4` | `Zeiger auf `AgcmEventManager`` | `OnAddModule` |
| `this+0xBA8` | `Zeiger auf `AgpmEventTeleport`` | `OnAddModule` |
| `this+0xBAC` | `Zeiger auf `AgpmArchlord`` | `OnAddModule` |
| `this+0xBB0 / 0xBB4` | `aktuelles Ereignis / Erzeuger-Basis` | `RequestTeleport…` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-ID `8` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 5.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmArchlord`](AgpmArchlord.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventTeleport`](AgpmEventTeleport.md), [`ApmEventManager`](ApmEventManager.md)
- **Erwähnt in:** [`AgcmUIEventTeleport`](AgcmUIEventTeleport.md)
