# AgpmAuctionCategory (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Moduls `AgpmAuctionCategory` (Kategoriebaum des Auktionshauses aus einer Excel-Tabelle) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmAuctionCategory/AgpmAuctionCategory.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle fünf Methoden (`OnAddModule`, `GetCategory1`, `GetCategory2`, `LoadCategoryInfo`, `BuildCategoryTree`) sind zugeordnet; dazu Konstruktor und Destruktor.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmAuctionCategory.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0054BA90` | 30 | vtable/String |
| 1 | `GetCategory1` | `0x0054BAB0` | 7 | von Hand geprüft |
| 2 | `GetCategory2` | `0x0054BAC0` | 7 | von Hand geprüft |
| 3 | `LoadCategoryInfo` | `0x0054BEB0` | 1014 | Zeichenkette |
| 4 | `BuildCategoryTree` | `0x0054BC00` | 671 | von Hand geprüft |

5 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmAuctionCategory` (`0x0054B9B0`), `~AgpmAuctionCategory_body` (`0x0054BAD0`), `scalar_deleting_dtor` (`0x0054BBE0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB84` | ``m_cAdminCategory1` (`ApAdmin` für Kategorien erster Stufe)` | `GetCategory1` |
| `this+0xC38` | ``m_cAdminCategory2` (`ApAdmin` für Kategorien zweiter Stufe)` | `GetCategory2` |

## Vtable und Aufbau

Vtable `0x008B755C`: Slot 0 Löschwrapper (`0x0054BBE0`), Slot 1 `OnAddModule` (`0x0054BA90`), übrige Slots die gemeinsamen Rümpfe (`0x0067AC90`, `0x0067FAB0`, `0x004E3420`). Konstruktor `0x0054B9B0` (221 Byte, legt zwei `ApAdmin`-Tabellen für je 10.000 Einträge an, `AGPA_AUCTION_CATEGORYCOUNT`, und setzt die aktuellen Kategorien auf 1), Destruktorrumpf `0x0054BAD0` (gibt alle Kategorie-Objekte frei). `OnAddModule` (30 Byte) holt [`AgpmItem`](AgpmItem.md) und liefert FALSE, wenn es fehlt.
`GetCategory1` (`0x0054BAB0`) und `GetCategory2` (`0x0054BAC0`) sind je 7 Byte: sie geben die Adresse der Tabellen im Modul zurück (`this+0xB84` bzw. `this+0xC38`); Aufrufer sind die Auktions-Oberflächenmodule (`0x00613EC0`, `0x00615900`, `0x006178D0`, `0x006264C0`, `0x0062A280`).

## Laden und Baum

`LoadCategoryInfo` (`0x0054BEB0`, 1.014 Byte; Aufrufer `0x0040DB10`) liest die Excel-Tabelle (Spaltenköpfe `TID`, `ItemName`, `Stack`, `FirstCategory`, `FirstCategoryName`, `SecondCategory`, `SecondCategoryName`) über `LoadExcelFile` und legt für jede Zeile mit stimmendem Gegenstandsnamen die Kategorien erster und zweiter Stufe an; am Schluss ruft sie `BuildCategoryTree`.
`BuildCategoryTree` (`0x0054BC00`, 671 Byte) zählt die Kinder jeder Kategorie, legt die Kindlisten an und füllt sie: Unterkategorien unter ihrer Oberkategorie, Gegenstände unter ihrer Unterkategorie (`m_lSecondCategory` der Gegenstandsvorlage, Durchlauf der Vorlagen-Tabelle von `AgpmItem`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `LoadCategoryInfo` und `BuildCategoryTree` wurden über Zeichenketten, Aufrufbeziehung und Größe zugeordnet, nicht Zeile für Zeile verglichen.
- Dass die Aufrufer von `GetCategory1`/`GetCategory2` zu den Auktions-Oberflächenmodulen gehören, folgt nur aus ihrer Adresslage.
- Welche Datei `LoadCategoryInfo` im Spiel lädt, wurde nicht verfolgt (der Aufrufer `0x0040DB10` liest Moduldaten).

## Querverweise

- **Erwähnt Module:** [`AgpmItem`](AgpmItem.md)
- **Erwähnt in:** [`AgcmUIAuction`](AgcmUIAuction.md)
