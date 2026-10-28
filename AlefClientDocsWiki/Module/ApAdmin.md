# ApAdmin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der gemeinsamen Klasse `ApAdmin` (Objektverwaltung mit Hash-Tabellen über ganze Zahlen und Zeichenketten) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/APublic/ApAdmin/ApAdmin.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 17 von 35 Quellmethoden sind zugeordnet. Zugeordnet sind das Eintragen (alle drei `AddObject`), Entfernen (alle drei `RemoveObject`), Abfragen (beide `GetObject`, `GetObjectSequence`), Hash-Zugriffe über Zeichenketten, `InitializeObject`, `RemoveObjectAll` und `Reset`.
- **Nicht gefunden:** `IsObject` (beide), `RLock`/`WLock`/`Release`, `GlobalRLock`/`GlobalWLock`/`GlobalRelease`, `SetNotUseLockManager`, `SetCount`/`GetCount`/`GetObjectCount`, `UpdateKey`/`UpdateStringKey`, `ClearHashMap*`, `GetHashMapINT32`, `SetHashMap*` einzeln sowie `RemoveHashMapINT32` – die Quelle hat sie als sehr kleine Funktionen; sie sind in den Aufrufern eingebaut oder an STL-Hilfsfunktionen (`0x004EAAC0` u. a.) gebunden.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApAdmin.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `InitializeObject` | `0x004EBAE0` | 149 | von Hand geprüft |
| 1 | `GetHashMapINT32` | – | | nicht im Binary gefunden; Verbleib offen |
| 2 | `GetHashMapstring` | `0x004EB6A0` | 255 | von Hand geprüft |
| 3 | `SetHashMapINT32` | `0x004EC060` | 78 | von Hand geprüft |
| 4 | `SetHashMapstring` | `0x004EC230` | 224 | von Hand geprüft |
| 5 | `RemoveHashMapINT32` | – | | nicht im Binary gefunden; Verbleib offen |
| 6 | `RemoveHashMapstring` | `0x004EBB80` | 133 | von Hand geprüft |
| 7 | `ClearHashMapINT32` | – | | nicht im Binary gefunden; Verbleib offen |
| 8 | `ClearHashMapstring` | – | | nicht im Binary gefunden; Verbleib offen |
| 9 | `AddObject` | `0x004EC0B0` | 353 | von Hand geprüft |
| 10 | `AddObject` | `0x004EC310` | 342 | von Hand geprüft |
| 11 | `AddObject` | `0x004EC470` | 354 | von Hand geprüft |
| 12 | `AddStringKey` | `0x004EC5E0` | 291 | von Hand geprüft |
| 13 | `UpdateStringKey` | – | | nicht im Binary gefunden; Verbleib offen |
| 14 | `RemoveObject` | `0x004EB7A0` | 317 | von Hand geprüft |
| 15 | `RemoveObject` | `0x004EBC10` | 317 | von Hand geprüft |
| 16 | `RemoveObject` | `0x004EBD50` | 331 | von Hand geprüft |
| 17 | `GetObject` | `0x004EAD20` | 211 | von Hand geprüft |
| 18 | `GetObject` | `0x004EB8E0` | 217 | von Hand geprüft |
| 19 | `GetObjectSequence` | `0x004EABA0` | 131 | von Hand geprüft |
| 20 | `IsObject` | – | | nicht im Binary gefunden; Verbleib offen |
| 21 | `IsObject` | – | | nicht im Binary gefunden; Verbleib offen |
| 22 | `RLock` | – | | nicht im Binary gefunden; Verbleib offen |
| 23 | `WLock` | – | | nicht im Binary gefunden; Verbleib offen |
| 24 | `Release` | – | | nicht im Binary gefunden; Verbleib offen |
| 25 | `SetCount` | – | | nicht im Binary gefunden; Verbleib offen |
| 26 | `GetCount` | – | | nicht im Binary gefunden; Verbleib offen |
| 27 | `GetObjectCount` | – | | nicht im Binary gefunden; Verbleib offen |
| 28 | `Reset` | `0x004EC220` | 14 | von Hand geprüft |
| 29 | `RemoveObjectAll` | `0x004EBEA0` | 193 | von Hand geprüft |
| 30 | `UpdateKey` | – | | nicht im Binary gefunden; Verbleib offen |
| 31 | `GlobalRLock` | – | | nicht im Binary gefunden; Verbleib offen |
| 32 | `GlobalWLock` | – | | nicht im Binary gefunden; Verbleib offen |
| 33 | `GlobalRelease` | – | | nicht im Binary gefunden; Verbleib offen |
| 34 | `SetNotUseLockManager` | – | | nicht im Binary gefunden; Verbleib offen |

17 von 35 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `GetObjectByIndex` (`0x004EAB40`), `GetObject_key` (`0x004EAD20`), `RemoveObject_key` (`0x004EB7A0`), `GetObject_str` (`0x004EB8E0`), `~ApAdmin_body` (`0x004EBA50`), `RemoveObject_str` (`0x004EBC10`), `RemoveObject_both` (`0x004EBD50`), `ApAdmin` (`0x004EBF70`), `~ApAdmin` (`0x004EC040`), `AddObject_key` (`0x004EC0B0`), `AddObject_both` (`0x004EC470`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | `Zeiger auf den Objektpuffer` | Destruktor |
| `this+0x14` | `Anzahl Plätze` | `AddObject` |
| `this+0x18 / 0x1C` | `Elementgröße (Pool)` | `GetObject` |
| `this+0x20` | `belegte Plätze` | `AddObject`, `RemoveObjectAll` |
| `this+0x6C / 0x70` | `Tabelle der Zeichenkettenschlüssel` | `InitializeObject` |
| `this+0x84 / 0x88` | `Pool-Parameter` | `InitializeObject` |
| `this+0x8A` | `Objektanzahl (16 Bit)` | Konstruktor, `InitializeObject` |
| `this+0x8C` | `Zusatzzeiger` | `InitializeObject` |
| `this+0x90 / 0x94` | `Rückruf hinzugefügt / entfernt` | `AddObject`, `RemoveObject` |
| `this+0x98` | `kritische Sektion` | alle |
| `this+0xB0` | `Sperre benutzen (Schalter)` | alle |

## Vtable und Aufbau

`ApAdmin` (Objektverwaltung mit Zeiger-Pool, Hash-Tabelle über ganze Zahlen und über Zeichenketten, Sperre) liegt im Binary bei `0x004EAA00`–`0x004EC700`. Vtable: nur der Löschwrapper (`0x004EC040`, ruft den Destruktorrumpf `0x004EBA50`). Der Konstruktor `0x004EBF70` baut den Objektpool und die beiden Hash-Tabellen mit je 100 Plätzen auf und richtet die kritische Sektion bei `this+0x98` ein; `+0xB0` ist der Schalter „Sperre benutzen“. `this+0x88`/`+0x8A` halten Objektgröße und Anzahl, `+0x8C` den Zusatzzeiger und `+0x90`/`+0x94` die Rückrufe „Objekt hinzugefügt“ bzw. „Objekt entfernt“, `+0x14` und `+0x20` Pool-Größe bzw. Belegung.
`InitializeObject` (`0x004EBAE0`, sieben Argumente) richtet den Pool (`0x004E5420`) ein, leert die Tabellen und setzt die Rückrufe und den Zusatzzeiger.

## Eintragen

`AddObject` gibt es in drei Fassungen: mit ganzzahligem Schlüssel (`0x004EC0B0`), mit Zeichenkette (`0x004EC310`, bei vollem Pool meldet es „ApAdmin::AddObject() Adding Object Error(Buffer Full!!!)“ in `LOG\_ALEF_ERROR_.log`) und mit beiden Schlüsseln (`0x004EC470`). Alle holen einen freien Platz im Pool (`0x004E4D50`), tragen den Schlüssel in die Hash-Tabelle ein (`SetHashMapINT32` `0x004EC060`, `SetHashMapstring` `0x004EC230`), rufen den Rückruf „hinzugefügt“ und liefern den Objektzeiger. `AddStringKey` (`0x004EC5E0`) hängt einem vorhandenen Objekt einen Zeichenkettenschlüssel an (und lehnt ab, wenn dieser schon besteht).

## Abfragen und Entfernen

`GetObject` mit ganzzahligem Schlüssel (`0x004EAD20`) und mit Zeichenkette (`0x004EB8E0`) schlagen den Index in der Hash-Tabelle nach (`GetHashMapstring` `0x004EB6A0`; die Zeichenkette wird mit dem Hash `Σ(5·h + Zeichen)` `0x004EAA00` aufgelöst) und holen das Objekt aus dem Pool (`0x004EAB40`: Index − 1, mal Elementgröße `+0x18`). `GetObjectSequence` (`0x004EABA0`) läuft unter der Sperre über den Pool (`0x004E4E10`).
`RemoveObject` hat ebenfalls drei Fassungen (ganzzahlig `0x004EB7A0`, Zeichenkette `0x004EBC10`, beide `0x004EBD50`): Rückruf „entfernt“ mit dem Objekt, Schlüssel aus den Tabellen löschen (`RemoveHashMapstring` `0x004EBB80`), Platz im Pool freigeben (`0x004E4DA0`). `RemoveObjectAll` (`0x004EBEA0`) leert beide Tabellen und auf Wunsch den Pool; `Reset` (`0x004EC220`) ruft es mit TRUE.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Dekompilat) sind alle in der Karte genannten Funktionen; die Zuordnung der drei `AddObject`/`RemoveObject`-Fassungen folgt aus Argumentzahl und Schlüsselart. Die Hash-Tabellen sind STL-Container (STLport), ihre Hilfsfunktionen (`0x004EAAC0`, `0x004EAC90`, `0x004EAE30`, `0x004EB1D0` …) sind keine Quellmethoden und nicht benannt.
- Dass die kleinen Funktionen fehlen, beruht auf dem Fehlen einer eigenen Funktion im Bereich `0x004EAA00`–`0x004EC700`; ein Aufruf aus anderen Modulen ist nicht einzeln gesucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 12, nicht im Client: 2, ohne Kandidat: 2, zugeordnet: 2.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `GetObjectCount` | 6 | `0x004EA9C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCount` | 7 | `0x004EA9A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->
