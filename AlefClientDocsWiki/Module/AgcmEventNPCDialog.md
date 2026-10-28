# AgcmEventNPCDialog (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventNPCDialog` (NPC-Dialog-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle Methoden bis auf den zusammengefalteten Einzeiler `SetCallbackAriseNPCDialogEvent` zugeordnet. Die Quelle enthält weitere Dateien (`CExNPC`, `CExNPCDialog`, `CUiExNPCMsgBoxGrid`, `CUiGridItem`), die hier nicht abgeglichen wurden.
- **OnAddModule:** 2 Module in der Reihenfolge der Quelle ([`AgcmEventManager`](AgcmEventManager.md), `AgpmEventNPCDialog`); Anmeldungen: Ereignis `0x15` → `CBRequestNPCDialog` (`0x006DD720`), Grant → `CBReceiveGrant` (`0x006DD800`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventNPCDialog.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DD870` | 93 | vtable/String |
| 1 | `SetCallbackAriseNPCDialogEvent` | – | | Einzeiler (`SetCallback`), zusammengefaltet |
| 2 | `CBRequestNPCDialog` | `0x006DD720` | 210 | Callback-Registrierung |
| 3 | `CBReceiveGrant` | `0x006DD800` | 77 | Callback-Registrierung |

3 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006dd640` (`0x006DD640`), `ctor_or_dtor_006dd6c0` (`0x006DD6C0`), `~AgcmEventNPCDialog` (`0x006DD850`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Ereignis-ID `0x15` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md)
