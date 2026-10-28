# AcUIChattingEdit (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `AcUIChattingEdit` (Chat-Eingabefeld) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `AcUIChattingEdit.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 13 von 15 Quellmethoden sind zugeordnet; neu sind Vtable-Slots und die Ereignis-Verarbeitung (`UpdateEvent`, `_EventParse`, `_ProcessEvent`, `_KeyString`, `IsDoubleByteCode_Kr`, `UpdateCurrentStatus`, `SetCallbackRefresh`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AcUIChattingEdit.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnClose` | `0x007C6910` | 1 | gleiche Adresse wie `gemeinsamer leerer Rumpf` (vom Linker zusammengefaltet) |
| 1 | `OnIdle` | `0x0079C9C0` | 5 | vtable/String |
| 2 | `UpdateEvent` | `0x0079E1E0` | 145 | ver |
| 3 | `OnChar` | `0x0079E280` | 1786 | vtable/String |
| 4 | `OnKeyDown` | `0x0079E990` | 1571 | vtable/String |
| 5 | `OnWindowRender` | `0x0079CDD0` | 2639 | vtable/String |
| 6 | `SetCurrentInputType` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 7 | `UpdateCurrentStatus` | `0x0079D830` | 352 | ver |
| 8 | `RefreshCustomData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `OnEditActive` | `0x0079D990` | 43 | vtable/String |
| 10 | `IsDoubleByteCode_Kr` | `0x0079C9F0` | 252 | ver |
| 11 | `_EventParse` | `0x0079DF70` | 579 | ver |
| 12 | `_KeyString` | `0x0079CAF0` | 232 | ver |
| 13 | `_ProcessEvent` | `0x0079DAF0` | 732 | ver |
| 14 | `SetCallbackRefresh` | `0x0079CBE0` | 23 | ver |

13 von 15 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `stEventKey::ctor_or_dtor` (`0x0079D9C0`), `ctor_or_dtor_0079ddd0` (`0x0079DDD0`), `ctor_or_dtor_0079dea0` (`0x0079DEA0`), `~AcUIChattingEdit` (`0x0079E1C0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x3190` | `Funktionszeiger „ist Mehrbyte-Zeichen“` | `IsDoubleByteCode_Kr` |
| `0x31D0 / 0x31D4` | `Refresh-Callback und Klassenzeiger` | `SetCallbackRefresh` |
| `0x31D8` | `Liste der Ereigniseinträge` | `_ProcessEvent` |
| `0x1D04` | `Eingabetext (`m_szText`)` | `UpdateEvent` |

## Vtable

Die Vtable steht bei `0x008E5064`. Überschriebene Slots der Quelle:

| Slot | Adresse | Funktion |
|---:|---|---|
| 3 | `0x007C6910` | `OnClose` (leerer Rumpf, gemeinsam mit anderen leeren Funktionen) |
| 4 | `0x0079C9C0` | `OnIdle` (ruft nur die Basis `AcUIEdit::OnIdle`) |
| 8 | `0x0079CDD0` | `OnWindowRender` (2639 Byte) |
| 9 | `0x0079E990` | `OnKeyDown` (1571 Byte) |
| 28 | `0x0079E280` | `OnChar` (1786 Byte) |
| 36 | `0x0079D990` | `OnEditActive` |

## Ereignis-Schlüssel im Text

Der Text kann Ereignisse der Form `<Name:Wert>` enthalten. `_KeyString` (`0x0079CAF0`) sucht `<` und `>` und entfernt den Teil vor dem letzten `:` dazwischen; `_EventParse` (`0x0079DF70`) zerlegt den Text rekursiv, `_ProcessEvent` (`0x0079DAF0`, nur von `OnChar` aufgerufen) arbeitet die gesammelten Einträge ab. Die Einträge (`stEventKey`) kommen aus einem Pool für 20 Stück (`ApMemory<stEventKey,20>`).

## Mehrbyte-Zeichen

`IsDoubleByteCode_Kr` (`0x0079C9F0`) prüft ein Zeichen über einen Funktionszeiger der Klasse (`+0x3190`) und schließt `\ @ ^ ~ ` | _ [ ] { }` aus – wie in der Quelle.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `OnChar`, `OnKeyDown` und `OnWindowRender` wurden über die Vtable zugeordnet, ihr Inhalt (je rund 250–330 Quellzeilen) wurde nicht verglichen.
- `SetCurrentInputType` und `RefreshCustomData` (je 5–6 Zeilen) sind im Binary nicht als eigene Funktionen zu finden (eingebaut).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIChatting2`](AgcmUIChatting2.md)
- **Erwähnt in:** [`AgcmUIChatting2`](AgcmUIChatting2.md), [`CChattingInputController`](CChattingInputController.md)
