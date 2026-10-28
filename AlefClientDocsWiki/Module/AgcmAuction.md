# AgcmAuction (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmAuction` (Auktionshaus, Client-Seite: Paketsendung und Rückrufe) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Operationsbytes in den Sendefunktionen, EP8-Quelle `Modules/AClient/AgcmAuction/AgcmAuction.cpp`. Das Paketformat steht im Bericht zu [`AgpmAuction`](AgpmAuction.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** Modulaufbau, die sieben Sendefunktionen (über die Operationsnummer eindeutig) und die Rückrufe sind zugeordnet; die fünf `SetCallback…`-Einzeiler sind zusammengefaltet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmAuction.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DFE70` | 431 | vtable/String |
| 1 | `SetCallbackSelect` | – | | Einzeiler (`SetCallback`), mit den anderen zu einem Rumpf zusammengefaltet |
| 2 | `SetCallbackAuctionUIOpen` | – | | Einzeiler, zusammengefaltet |
| 3 | `SetCallbackSalesBox2Add` | – | | Einzeiler, zusammengefaltet |
| 4 | `SetCallbackSalesBox2Remove` | – | | Einzeiler, zusammengefaltet |
| 5 | `SetCallbackSalesBox2Update` | – | | Einzeiler, zusammengefaltet |
| 6 | `CBRequestOpenAuction` | `0x006DFD30` | 85 | Callback-Registrierung |
| 7 | `CBSelect` | `0x006DFE00` | 98 | Callback-Registrierung |
| 8 | `CBAdd` | `0x006DF760` | 37 | Callback-Registrierung |
| 9 | `CBRemove` | `0x006DF790` | 37 | Callback-Registrierung |
| 10 | `CBUpdate` | `0x006DF7C0` | 37 | Callback-Registrierung |
| 11 | `CBAuctionOpen` | `0x006DF7F0` | 28 | Callback-Registrierung |
| 12 | `CBOpenAnywhere` | `0x006DF810` | 41 | Callback-Registrierung |
| 13 | `SendSelect` | `0x006DF840` | 187 | von Hand geprüft |
| 14 | `SendSell` | `0x006DF900` | 183 | von Hand geprüft |
| 15 | `SendCancel` | `0x006DF9C0` | 173 | von Hand geprüft |
| 16 | `SendConfirm` | `0x006DFA70` | 174 | von Hand geprüft |
| 17 | `SendBuy` | `0x006DFB20` | 186 | von Hand geprüft |
| 18 | `SendOpenAuction` | `0x006DFBE0` | 147 | von Hand geprüft |
| 19 | `SendOpenAnywhere` | `0x006DFC80` | 116 | von Hand geprüft |

15 von 20 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DF6E0`), `~AgcmAuction` (`0x006DFD00`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBAC` | `Zeiger auf `AgpmAuction`` | Sendefunktionen |
| `AgpmAuction+0xB9C` | `Paketbauer für Operationspakete` | Sendefunktionen |
| `AgpmAuction+0x386D8` | `Teilpaket (Verkaufsdaten)` | `SendSelect` |

## OnAddModule (0x006DFE70)

Holt neun Module in dieser Reihenfolge: [`ApmMap`](ApmMap.md), [`ApmEventManager`](ApmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), `AgpmAuction`, [`AgcmConnectManager`](AgcmConnectManager.md), [`AgcmEventManager`](AgcmEventManager.md), `AgcmCharacter` (Zeichenketten im Dekompilat, gleiche Reihenfolge wie die Quelle). Danach folgen die Rückrufe bei `AgpmAuction` (Add/Remove/Update-Sales, Select2, OpenAuction, OpenAnywhere → `0x006DF760`, `0x006DF790`, `0x006DF7C0`, `0x006DFE00`, `0x006DF7F0`, `0x006DF810`) und die Ereignisanmeldung `RegisterEventCallback(APDEVENT_FUNCTION_AUCTION)` mit `CBRequestOpenAuction` (`0x006DFD30`).

## Senden (Send…)

Die sieben Sendefunktionen liegen in Quellreihenfolge hintereinander und tragen die Operationsnummer im Paket: `SendSelect` `0x006DF840` (Operation 13 = `SELECT2`), `SendSell` `0x006DF900` (5), `SendCancel` `0x006DF9C0` (6), `SendConfirm` `0x006DFA70` (7), `SendBuy` `0x006DFB20` (8), `SendOpenAuction` `0x006DFBE0` (10 = `EVENT_REQUEST`), `SendOpenAnywhere` `0x006DFC80` (15). Alle Zahlen stimmen mit `AGPMAUCTION_OPERATION_…` in `AgpmAuction.h` überein. Select, Sell, Cancel, Confirm und Buy bauen zuerst ein Teilpaket (Verkaufsdaten) und danach das Operationspaket, `SendOpenAuction` und `SendOpenAnywhere` nur das Operationspaket; gesendet wird jeweils über `SendPacket`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Offsets `this+0xBAC` und `AgpmAuction+0xB9C/0x386D8` folgen aus den Zugriffen in den Sendefunktionen; die Paketfelder selbst wurden nicht Feld für Feld mit der Quelle verglichen.
- Die Rückrufe `CBAdd`, `CBRemove`, `CBUpdate`, `CBAuctionOpen`, `CBOpenAnywhere` und `CBSelect` waren schon über die Anmeldereihenfolge benannt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 5.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmConnectManager`](AgcmConnectManager.md), [`AgcmEventManager`](AgcmEventManager.md), [`AgpmAuction`](AgpmAuction.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmUIAuction`](AgcmUIAuction.md)
