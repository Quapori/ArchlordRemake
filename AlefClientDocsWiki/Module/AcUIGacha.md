# AcUIGacha (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse `AcUIGacha` (Walzenfenster des Gachas) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIEventGacha/AcUIGacha.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 8 von 8 Quellmethoden sind zugeordnet; neu sind `StartRoll` und `SetSlotItems`; `OnPostInit` steht als gemeinsamer Rumpf.
- **Sperre:** Während der Drehung ist der Self-Character unbeweglich (Bit `0x400`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AcUIGacha.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x00769110` | 76 | vtable/String |
| 1 | `OnPostInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `SetSlotItems` | `0x00769E60` | 508 | ver |
| 3 | `OnIdle` | `0x007691C0` | 766 | vtable/String |
| 4 | `OnWindowRender` | `0x007694C0` | 796 | vtable/String |
| 5 | `StartRoll` | `0x007697E0` | 255 | ver |
| 6 | `LoadGachaSetting` | `0x0076A060` | 694 | Zeichenkette |
| 7 | `OnCloseUI` | `0x00769160` | 84 | vtable/String |

8 von 8 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00769d70` (`0x00769D70`), `ctor_or_dtor_00769de0` (`0x00769DE0`), `~AcUIGacha` (`0x00769E40`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1D04` | `Zeiger auf [`AgcmUIEventGacha`](AgcmUIEventGacha.md)` | `StartRoll` |
| `0x1D08 / 0x1D0C` | `Slot-Liste (Anfang / Ende, je 32 Byte)` | `StartRoll` |
| `0x1D18` | `Rollmodus (1 = rollt)` | `StartRoll` |
| `0x1D1C…0x1D34` | `Position, Maximum, Ergebnis, Zeiten, Ergebnis-TID` | `StartRoll` |

## Vtable

Vtable bei `0x008E09E4`: Slot 0 Destruktor `0x00769E40`, 1 `OnInit` (`0x00769110`), 2 `OnPostInit`-Rumpf `0x0067AC90` (leer in der Quelle), 4 `OnIdle` (`0x007691C0`), 8 `OnWindowRender` (`0x007694C0`).

## Walze starten (StartRoll, 0x007697E0)

Ist die Walze schon in Bewegung, wird abgelehnt. Sonst wird die Zielposition des Gegenstands in der Slot-Liste gesucht (Schrittweite 32 Byte je Eintrag, Zielposition = (Slotzahl × Umdrehungen + Index − 2) × 50); nicht gefunden → Rückruf `OnRollEnd` des Moduls. Beim Start wird der Modus auf „rollt“ gesetzt, Start- und Rollzeit mit `GetTickCount` gespeichert und beim Self-Character das Sonderstatus-Bit `0x400` (nicht bewegen) gesetzt; das Modul bekommt `SetGachaWindowOpen(TRUE)`. Das entspricht der Quelle.

## Slots (SetSlotItems, 0x00769E60)

Setzt Position und Modus zurück und legt für jeden Gegenstand der Liste Textur und Namen an (`GetItemTemplate`, Textur laden); der Name des mittleren Slots geht an das Modul, bei leerer Liste „----“.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`StartRoll`, `SetSlotItems`).

## Grenzen

- `OnIdle` (91 Zeilen) und `OnWindowRender` (117 Zeilen) waren bereits zugeordnet und wurden hier nicht gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIEventGacha`](AgcmUIEventGacha.md)
- **Erwähnt in:** [`AgcmUIEventGacha`](AgcmUIEventGacha.md)
