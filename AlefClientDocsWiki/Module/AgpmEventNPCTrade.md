# AgpmEventNPCTrade (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmEventNPCTrade` (Händler-Ereignis: Ereignisdaten, Stream, Gitter) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/APublic/AgpmEventNPCTrade/AgpmEventNPCTrade.cpp`. Alle Adressen gelten nur für den 2017er Build; die Dialog-Seite des Händlers steht im Bericht `NPC_Trade_Dialog`.

## Kernbefund

- **Abdeckung:** 6 von 9 Quellmethoden sind zugeordnet (`OnAddModule`, die vier Ereignis-Rückrufe und `SetCallbackDeleteGrid`). Nicht im Client-Binary sind `LoadNPCTradeRes` (Aufrufer nur im Server: `ServerEngine.cpp`), `IsItemInGrid` (Aufrufer nur im Server: `AgsmEventNPCTrade.cpp`) und `LoadNPCTradeTemplate` (in der Quelle ohne Aufrufer).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmEventNPCTrade.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00575FD0` | 153 | vtable/String |
| 1 | `CBEventConstructor` | `0x00575F00` | 207 | Callback-Registrierung |
| 2 | `CBEventDestructor` | `0x00575D90` | 98 | Callback-Registrierung |
| 3 | `CBStreamWriteEvent` | `0x00575E00` | 84 | Callback-Registrierung |
| 4 | `CBStreamReadEvent` | `0x00575E60` | 147 | Callback-Registrierung |
| 5 | `LoadNPCTradeTemplate` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 6 | `LoadNPCTradeRes` | – | | nicht im Client-Binary: einziger Aufrufer in der Quelle ist der Server (`ServerEngine.cpp`) |
| 7 | `IsItemInGrid` | – | | nicht im Client-Binary: einziger Aufrufer in der Quelle ist der Server (`AgsmEventNPCTrade.cpp`) |
| 8 | `SetCallbackDeleteGrid` | `0x006DA540` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf mit Kennung 0 (einziger Aufrufer [`AgcmUIItem`](AgcmUIItem.md):OnAddModule`)` (vom Linker zusammengefaltet) |

6 von 9 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmEventNPCTrade` (`0x00575CD0`), `~AgpmEventNPCTrade_body` (`0x00576070`), `scalar_deleting_dtor` (`0x00576150`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBCC` | `Zeiger [`ApmEventManager`](ApmEventManager.md)` | `OnAddModule` |
| `this+0xBD0` | `Zeiger [`AgpmGrid`](AgpmGrid.md)` | `OnAddModule`, `CBEventConstructor` |
| `Ereignis+0x08` | `Ereignisdaten (`AgpdEventNPCTradeData`, 0x3C8 Byte)` | alle Ereignis-Rückrufe |
| `Ereignisdaten+0x04` | `Zeiger `AgpdGrid`` | `CBEventConstructor`, `CBEventDestructor` |

## Vtable und Aufbau

Konstruktor `0x00575CD0` (180 Byte, trägt `AgpmEventNPCTrade` als Modulnamen ein und nullt die Modulzeiger), Destruktorrumpf `0x00576070` (212 Byte; gibt Vorlagen und Gegenstandsgruppen frei), Löschwrapper `0x00576150`. `OnAddModule` (`0x00575FD0`, 153 Byte) holt `ApmEventManager` (`this+0xBCC`) und `AgpmGrid` (`this+0xBD0`), meldet die Ereignisfunktion 9 (`APDEVENT_FUNCTION_NPCTRADE`) mit Konstruktor, Destruktor, Schreib- und Lese-Rückruf an und legt zwei `ApAdmin`-Tabellen für je 1000 Einträge an (`AGPMEVENT_NPCTRADE_MAX_NPC`: Vorlagen und Gegenstandsgruppen).

## Ereignisdaten

`CBEventConstructor` (`0x00575F00`, 207 Byte) legt den Ereignisblock (0x3C8 Byte) und ein `AgpdGrid` (0x24 Byte; danach Aufruf von `0x00587640` mit dem Wert 6) an und nullt drei Felder zu je 0x140 Byte (Anfangsdaten der Gitterfelder, Gegenstandskennungen, Gegenstandsdaten); `CBEventDestructor` (`0x00575D90`, 98 Byte) gibt Gitter und Block frei, wenn `AgpmGrid` vorhanden ist.
`CBStreamWriteEvent` (`0x00575E00`, 84 Byte) schreibt `NPCTradeStart`, die Zeile `Template` mit der Vorlagenkennung und `NPCTradeEnd`; `CBStreamReadEvent` (`0x00575E60`, 147 Byte) liest bis `NPCTradeEnd` und ruft bei `Template` den Leser der Vorlage auf.
`SetCallbackDeleteGrid` ist ein Einzeiler `SetCallback(AGPMEVENT_NPCTRADE_CB_ID_DELETE_GRID, …)` mit der Kennung 0 und liegt am gemeinsamen `SetCallback`-Rumpf `0x006DA540`; belegt ist das durch den einzigen Aufrufer `AgcmUIItem::OnAddModule` (`0x006D7490`: `push 0x789D00` = `CBNPCTradeDeleteGrid`, `call 0x006DA540`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `OnAddModule`, `CBEventConstructor`, `CBEventDestructor` und die beiden Stream-Rückrufe; die Struktur von `AgpdEventNPCTradeData` (Felder in den drei 0x140-Byte-Blöcken) wurde nicht vermessen.
- Der Rumpf `0x006DA540` ist über die gleiche Form (ein `SetCallback(0, …)`-Einzeiler) als gemeinsamer Rumpf belegt, nicht über einen Byte-Vergleich aller Klassen; weitere Klassen mit Kennung 0 teilen ihn.
- Die Gegenstandslisten des Händlers (`NPCTradeItemList.txt`) lädt nur der Server; wie der Client sie erhält (Paket), steht im Bericht zu `AgcmEventNPCTrade`/`NPC_Trade_Dialog`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht im Client: 4.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIItem`](AgcmUIItem.md), [`AgpmGrid`](AgpmGrid.md), [`ApmEventManager`](ApmEventManager.md)
- **Erwähnt in:** [`NPC_Trade_Dialog`](NPC_Trade_Dialog.md)
