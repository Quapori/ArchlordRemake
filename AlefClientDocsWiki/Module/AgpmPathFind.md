# AgpmPathFind (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmPathFind` (Wegsuche auf einem Blockfeld) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmPathFind/AgpmPathFind.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 3 von 13 Quellmethoden sind als eigene Funktion zugeordnet (`OnAddModule`, `initBlock`, `resetBlock`). `initSearchNode` ist in den Konstruktor eingebaut. Die eigentliche Wegsuche fehlt im Client-Binary: die drei Fassungen von `pathFind` haben in der Quelle nur Server-Aufrufer (`AgsmAI2`, `AgsmNPCAI2`); `lock`, `unlock`, `getPathToExternalList` und `resetBlock`-Aufruf gehören nur zu `pathFind`, `initStartPoint`, `initTargetPoint` und `reset` haben in der Quelle keinen Aufrufer.
- **Abweichungen:** keine festgestellt; Radius 50, Versuchszahl 100 und die Richtungstabellen stimmen mit der Quelle überein.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmPathFind.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `lock` | – | | nicht im Client-Binary: nur in `pathFind` (Server) benutzt |
| 1 | `unlock` | – | | nicht im Client-Binary: nur in `pathFind` (Server) benutzt |
| 2 | `OnAddModule` | `0x0057ADA0` | 30 | vtable/String |
| 3 | `initBlock` | `0x0057AF60` | 231 | von Hand geprüft |
| 4 | `resetBlock` | `0x0057ADC0` | 318 | von Hand geprüft |
| 5 | `initSearchNode` | – | | eingebaut im Konstruktor (Aufruf von `0x0057B1E0` mit 100) |
| 6 | `reset` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 7 | `getPathToExternalList` | – | | nicht im Client-Binary: nur von `pathFind` (Server) gerufen |
| 8 | `initStartPoint` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 9 | `initTargetPoint` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 10 | `pathFind` | – | | nicht im Client-Binary: Aufrufer in der Quelle nur im Server (`AgsmAI2`, `AgsmNPCAI2`) |
| 11 | `pathFind` | – | | nicht im Client-Binary: Aufrufer in der Quelle nur im Server (`AgsmAI2`, `AgsmNPCAI2`) |
| 12 | `pathFind` | – | | nicht im Client-Binary: Aufrufer in der Quelle nur im Server (`AgsmAI2`, `AgsmNPCAI2`) |

3 von 13 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmPathFind` (`0x0057B340`), `~AgpmPathFind_body` (`0x0057B540`), `scalar_deleting_dtor` (`0x0057B660`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xC20` | ``m_aArraryX[8]` (0, 1, 1, 1, 0, −1, −1, −1)` | Konstruktor |
| `this+0xC68 / 0xC64` | `Halbbreite / Breite (2·Halb+1)` | `initBlock` |
| `this+0xC70 / 0xC6C` | `Halbhöhe / Höhe (2·Halb+1)` | `initBlock` |
| `this+0xBFC` | `Zeiger auf das Feld der Spalten (`m_ppcPathFindBlock`)` | `initBlock` |
| `this+0xC60` | ``m_bFound`` | `initBlock` |
| `this+0xC74` | ``m_iRevision`` | `initBlock` |

## Aufbau

Vtable wie bei den anderen Modulen (Slot 0 Löschwrapper `0x0057B660`, Slot 1 `OnAddModule` `0x0057ADA0`). Konstruktor `0x0057B340` (498 Byte): trägt `AgpmPathFind` als Modulnamen ein, setzt den Modultyp 1 (öffentlich), richtet die Achtnachbar-Richtungstabellen ein (`m_aArraryX` = 0, 1, 1, 1, 0, −1, −1, −1 bei `this+0xC20`; `m_aArraryY` = −1, −1, 0, 1, 1, 1, 0, −1 danach), ruft `initBlock(50, 50)` (`0x0057AF60`; `AGPMPATHFIND_RADIUS` = 50) und `initSearchNode(100)` (`AGPMPATHFIND_TRY_COUNT` = 100; eingebaut: Aufruf der Listen-Zuweisung `0x0057B1E0` und `resetIndex`). Destruktorrumpf `0x0057B540` (279 Byte; gibt nach der Quelle die Blockfelder frei).
`OnAddModule` (`0x0057ADA0`, 30 Byte) holt [`ApmMap`](ApmMap.md) und liefert FALSE, wenn es fehlt.

## Wegsuchfeld

`initBlock` (`0x0057AF60`, 231 Byte) setzt Halbbreite und Halbhöhe (`this+0xC68`/`+0xC70`), berechnet Breite und Höhe als 2·Halb+1 (101 × 101 bei Radius 50), legt ein Feld von Spalten zu je Höhe Blöcken (0x24 Byte je `AgpdPathFindBlock`, Anfangsstatus 3) an und ruft `resetBlock` (`0x0057ADC0`, 318 Byte). `resetBlock` markiert den Rand des Feldes als gesperrt (Revision `0xFFFFFFFF`) und setzt das Innere auf „unbenutzt“ mit Revision 0.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind der Konstruktor und `initBlock`; `resetBlock` ist über die Aufrufbeziehung (nur von `initBlock` gerufen) und die Größe zugeordnet, nicht Zeile für Zeile verglichen.
- Dass `0x0057B1E0` die Listen-Zuweisung (`allocSwapBuffer`) ist, folgt aus ihren Aufrufern (Konstruktor, Konstruktor von `AgcmCharacter`) und der Größe; das Listen-Template wird mit anderen Modulen geteilt (`0x0057AF10`, `0x0057B050` u. a. haben Aufrufer in `AgcmCharacter`).
- Die Offsets stammen aus dem Konstruktor und `initBlock`; die Namen der Felder folgen der Quelle.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, nicht im Client: 4, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`ApmMap`](ApmMap.md)
