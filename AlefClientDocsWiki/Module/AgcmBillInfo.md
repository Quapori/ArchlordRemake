# AgcmBillInfo (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmBillInfo` (Abrechnungsinfo: PC-Raum-Symbol) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule`, `OnInit`, `CBUpdateBillInfo` und `AddSystemGridIcon_PCRoom` zugeordnet; `_AddSystemGridHangameS` und `_AddSystemGridHangameTPack` (Hangame-Symbole) wurden im Binary nicht gefunden (Regionscode des Global-Builds entfernt).
- **OnAddModule** (`0x006DDDE0`): holt [`AgpmBillInfo`](AgpmBillInfo.md) und meldet `CBUpdateBillInfo` (`0x006DDD90`) an. **OnInit** (`0x006DDC90`) holt [`AgcmUIControl`](AgcmUIControl.md), [`AgpmGrid`](AgpmGrid.md), [`AgcmUIMain`](AgcmUIMain.md) (wie die Quelle).
- **PC-Raum-Symbol:** `AddSystemGridIcon_PCRoom` (`0x006DDCD0`, Zeichenkette `PCRoom`) legt über `AgcmUIControl` das Gitter-Symbol an; `CBUpdateBillInfo` ruft es.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmBillInfo.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DDDE0` | 46 | vtable/String |
| 1 | `OnInit` | `0x006DDC90` | 62 | vtable/String |
| 2 | `CBUpdateBillInfo` | `0x006DDD90` | 76 | Callback-Registrierung |
| 3 | `AddSystemGridIcon_PCRoom` | `0x006DDCD0` | 136 | von Hand geprüft |
| 4 | `_AddSystemGridHangameS` | – | | Regionscode, im Binary nicht gefunden |
| 5 | `_AddSystemGridHangameTPack` | – | | Regionscode, im Binary nicht gefunden |

4 von 6 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmBillInfo` (`0x006DDC30`), `~AgcmBillInfo` (`0x006DDD60`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass die Hangame-Funktionen im Global-Build fehlen, ist aus dem Fehlen von Zeichenketten und Aufrufern geschlossen; ein Beweis aus der Quelle (Präprozessor) wurde nicht gesucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgpmBillInfo`](AgpmBillInfo.md), [`AgpmGrid`](AgpmGrid.md)
