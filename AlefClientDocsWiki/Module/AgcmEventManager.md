# AgcmEventManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventManager` (Verteiler für NPC- und Objektereignisse) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle Methoden außer den gemeinsamen Rümpfen `OnInit`/`OnDestroy` zugeordnet.
- **OnAddModule** (`0x006E0360`): holt [`AgcmObject`](AgcmObject.md), `AgcmCharacter` und [`ApmEventManager`](ApmEventManager.md) (bei fehlendem `ApmEventManager` `FALSE`) und meldet `CBInitEventObject` (`0x006E02F0`) an.
- **RegisterEventCallback** (`0x006E02C0`): prüft Rückruf, Klassenzeiger und `eFunction < 0x2A` (= `APDEVENT_MAX_FUNCTION`, 42 Ereignisarten) und ruft `SetCallback`; 22 Aufrufer, nämlich die `OnAddModule` der NPC-Ereignismodule.
- **CheckEvent:** die Fassung ohne Funktionsangabe (`0x006E03C0`, 224 Byte) bevorzugt das NPC-Dialog-Ereignis (Wert `0x15`) und prüft sonst alle Ereignisse des Objekts; die Fassung mit Funktionsangabe (`0x006E04A0`, 123 Byte) ruft nur die passende.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E0360` | 82 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `RegisterEventCallback` | `0x006E02C0` | 44 | von Hand geprüft |
| 4 | `CheckEvent` | `0x006E03C0` | 224 | von Hand geprüft |
| 5 | `CheckEvent` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `CBInitEventObject` | `0x006E02F0` | 50 | Callback-Registrierung |

6 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006E0270`), `~AgcmEventManager` (`0x006E0330`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Zeiger auf `AgcmObject`` | `OnAddModule` |
| `this+0xB9C` | `Zeiger auf `AgcmCharacter`` | `OnAddModule` |
| `this+0xBA0` | `Zeiger auf `ApmEventManager`` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der beiden `CheckEvent`-Fassungen stützt sich auf den NPC-Dialog-Wert `0x15`, die Größen und die Quellreihenfolge.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmObject`](AgcmObject.md), [`ApmEventManager`](ApmEventManager.md)
- **Erwähnt in:** [`AgcmArchlord`](AgcmArchlord.md), [`AgcmAuction`](AgcmAuction.md), [`AgcmEventBank`](AgcmEventBank.md), [`AgcmEventCharCustomize`](AgcmEventCharCustomize.md), [`AgcmEventGacha`](AgcmEventGacha.md), [`AgcmEventGuild`](AgcmEventGuild.md), [`AgcmEventItemConvert`](AgcmEventItemConvert.md), [`AgcmEventItemRepair`](AgcmEventItemRepair.md), [`AgcmEventNPCDialog`](AgcmEventNPCDialog.md), [`AgcmEventProduct`](AgcmEventProduct.md), [`AgcmEventQuest`](AgcmEventQuest.md), [`AgcmEventRefinery`](AgcmEventRefinery.md), [`AgcmEventSiegeWarNPC`](AgcmEventSiegeWarNPC.md), [`AgcmEventSkillMaster`](AgcmEventSkillMaster.md), [`AgcmEventTeleport`](AgcmEventTeleport.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIGuideMessage`](AgcmUIGuideMessage.md), [`AgcmUIRemission`](AgcmUIRemission.md), [`AgcmUITax`](AgcmUITax.md), [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md)
