# AgcmAdmin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmAdmin` (Admin-Werkzeug: lädt die Admin-DLL) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, `OnIdle`, `OnDestroy`, `CBIsDialogMessage`, `StartAdminClient` und `GetDLLFunction` zugeordnet, `OnInit` ist der gemeinsame `return TRUE`-Rumpf (Vtable-Slot 2). `SendAdminClientRequest` und `GetUIMessageString` wurden im Binary nicht gefunden (kein Aufrufer, vermutlich vom Linker entfernt).
- **StartAdminClient** (`0x005D7900`): lädt im Release-Build `AlefAdminDLL.dll` (die Debug-Fassung `AlefAdminDLLd.dll` steht nicht im Binary) und ruft die Funktion `ADMIN_Common_SetAdminModule` aus der DLL; `GetDLLFunction` (`0x005D77E0`) ist ein `GetProcAddress`-Aufruf.
- **OnDestroy** (`0x005D7860`) ruft `ADMIN_Common_DeleteInstance` und gibt die DLL frei; **OnAddModule** (`0x005D7950`) ruft zuerst `StartAdminClient`, holt dann [`AgpmAdmin`](AgpmAdmin.md) und `AgcmCharacter` (Zeiger `this+0xB9C`/`0xBA0`) und liefert `FALSE`, wenn eines fehlt. Die DLL liegt bei `this+0xB98`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmAdmin.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005D7950` | 67 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnIdle` | `0x005D7830` | 48 | vtable/String |
| 3 | `OnDestroy` | `0x005D7860` | 74 | vtable/String |
| 4 | `CBIsDialogMessage` | `0x005D78B0` | 66 | Zeichenkette |
| 5 | `SendAdminClientRequest` | – | | keine Funktion im Binary (nicht aufgerufen, vermutlich entfernt) |
| 6 | `StartAdminClient` | `0x005D7900` | 80 | Zeichenkette |
| 7 | `GetUIMessageString` | – | | keine Funktion im Binary (nicht aufgerufen, vermutlich entfernt) |
| 8 | `GetDLLFunction` | `0x005D77E0` | 28 | von Hand geprüft |

7 von 9 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmAdmin` (`0x005D7750`), `~AgcmAdmin` (`0x005D7800`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Handle der Admin-DLL` | `StartAdminClient`, `OnDestroy` |
| `this+0xB9C` | `Zeiger auf `AgpmAdmin`` | `OnAddModule` |
| `this+0xBA0` | `Zeiger auf `AgcmCharacter`` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass `SendAdminClientRequest` und `GetUIMessageString` entfernt wurden, ist aus dem Fehlen von Aufrufern und Zeichenketten geschlossen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmAdmin`](AgpmAdmin.md)
