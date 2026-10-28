# AgcmUIStatus (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIStatus` (Schnellleiste und Anzeigeoptionen mit Server-Speicherung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIStatus/AgcmUIStatus.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 14 von 14 Quellmethoden sind zugeordnet; neu sind `SendPacketUpdateQBeltItem` und `SendPacketUpdateViewHelmetOption`; `OnDestroy` steht als gemeinsamer Rumpf.
- **Pakete:** Typ `0x14`, Operation 1 (Schnellleiste) und 3 (Helm-Anzeige).
- **Verzögerung:** Schwellwert-Änderungen werden erst nach 20 s gesendet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIStatus.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00692220` | 361 | vtable/String |
| 1 | `OnInit` | `0x00691A00` | 30 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `OnIdle` | `0x00691C20` | 164 | vtable/String |
| 4 | `CBUpdateViewHelmetOption` | `0x00691A20` | 71 | Callback-Registrierung |
| 5 | `CBReceiveQuickBeltInfo` | `0x00691CD0` | 775 | Callback-Registrierung |
| 6 | `CBAddShortcut` | `0x00691FF0` | 279 | Callback-Registrierung |
| 7 | `CBRemoveShortcut` | `0x00692110` | 129 | Callback-Registrierung |
| 8 | `CBUpdateHPPotion` | `0x006921A0` | 60 | Callback-Registrierung |
| 9 | `CBUpdateMPPotion` | `0x006921E0` | 60 | Callback-Registrierung |
| 10 | `CBUpdateAutoUseHPGage` | `0x00691A70` | 42 | Callback-Registrierung |
| 11 | `CBUpdateAutoUseMPGage` | `0x00691AA0` | 42 | Callback-Registrierung |
| 12 | `SendPacketUpdateQBeltItem` | `0x00691AD0` | 154 | ver |
| 13 | `SendPacketUpdateViewHelmetOption` | `0x00691B70` | 118 | ver |

14 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x00691970`), `~AgcmUIStatus` (`0x00691BF0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBA4` | `Zeiger auf `AgcmCharacter`` | `OnIdle` |
| `0xBA8` | `Zeiger auf [`AgcmUIMain`](AgcmUIMain.md)` | `OnIdle` (Schwellwerte bei `+0x2A08` und `+0x2A0C`) |
| `0xBB0` | `Zeiger auf [`AgcmUIOption`](AgcmUIOption.md)` | `OnInit` |
| `0xBB4 / 0xBB8` | `Zeit der letzten HP- / MP-Schwellen-Änderung` | `OnIdle` |

## Vtable

Vtable bei `0x008CDCCC`: Slot 0 Destruktor `0x00691BF0`, 1 `OnAddModule` (`0x00692220`), 2 `OnInit` (`0x00691A00`, holt `AgcmUIOption`), 3 `OnIdle` (`0x00691C20`), 6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. die leere `OnDestroy`).

## Callbacks (OnAddModule, 0x00692220)

Sechs Module ([`ApmEventManager`](ApmEventManager.md), [`AgpmSkill`](AgpmSkill.md), [`AgpmUIStatus`](AgpmUIStatus.md), `AgcmCharacter`, `AgcmUIMain`, [`AgcmItem`](AgcmItem.md)). Danach acht Callbacks in der Reihenfolge der Quelle:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmUIStatus`: Schnellleisten-Info empfangen | `CBReceiveQuickBeltInfo` | `0x00691CD0` |
| `AgpmUIStatus`: Helm-Anzeige geändert | `CBUpdateViewHelmetOption` | `0x00691A20` |
| `AgcmUIMain`: Verknüpfung hinzugefügt | `CBAddShortcut` | `0x00691FF0` |
| `AgcmUIMain`: Verknüpfung entfernt | `CBRemoveShortcut` | `0x00692110` |
| `AgcmUIMain`: HP-Trank geändert | `CBUpdateHPPotion` | `0x006921A0` |
| `AgcmUIMain`: MP-Trank geändert | `CBUpdateMPPotion` | `0x006921E0` |
| `AgcmUIMain`: HP-Schwelle geändert | `CBUpdateAutoUseHPGage` | `0x00691A70` |
| `AgcmUIMain`: MP-Schwelle geändert | `CBUpdateAutoUseMPGage` | `0x00691AA0` |

## Pakete an den Server (Typ 0x14)

Die beiden Sender bauen Pakete des Typs `0x14` (20, `AGPMUISTATUS_PACKET_TYPE`) mit `MakePacket` (`0x004EA2D0`) und senden sie mit `SendPacket` (`0x004E45A0`):

| Sender | Adresse | Operation | Paketfunktion |
|---|---|---:|---|
| `SendPacketUpdateQBeltItem` | `0x00691AD0` | 1 (Schnellleiste aktualisieren) | `AgpmUIStatus::MakePacketUpdateQuickBeltItem` (`0x0057DC40`) |
| `SendPacketUpdateViewHelmetOption` | `0x00691B70` | 3 (Helm-Anzeige) | `MakePacketUpdateViewHelmetOption` (`0x0057DD80`) |

`SendPacketUpdateQBeltItem` lehnt Indizes außerhalb von −1…39 ab (40 Plätze = 4 Ebenen × 10 Spalten, `AGPMUISTATUS_MAX_QUICKBELT_LAYER`/`_COLUMN`). Das Feldformat steht im Bericht [AgpmUIStatus](AgpmUIStatus.md).

## Verzögertes Speichern (OnIdle, 0x00691C20)

Ändert der Spieler die HP- oder MP-Schwelle der automatischen Trankbenutzung, merkt sich das Modul die Zeit (`+0xBB4` für HP, `+0xBB8` für MP). `OnIdle` sendet erst **20 000 ms** nach der letzten Änderung ein Quickbelt-Update mit Index −1, ohne Gegenstand und nur mit dem neuen Schwellwert (HP bzw. MP, der jeweils andere Wert −1) und setzt die Zeit zurück. Das entspricht der Quelle.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnIdle`, beide Sender, Registrierungsreihenfolge).

## Grenzen

- `CBReceiveQuickBeltInfo` (119 Zeilen) und `CBAddShortcut` waren bereits zugeordnet und wurden hier nicht neu gelesen.
- Die Paket-Operationen 1 und 3 wurden aus den Sendern gelesen; die übrigen Operationen stehen im Bericht `AgpmUIStatus`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmItem`](AgcmItem.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIOption`](AgcmUIOption.md), [`AgpmSkill`](AgpmSkill.md), [`AgpmUIStatus`](AgpmUIStatus.md), [`ApmEventManager`](ApmEventManager.md)
