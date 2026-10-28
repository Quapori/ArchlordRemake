# AuIniManagerA (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuIniManagerA` (INI-Dateien lesen, Abschnitte und Schlüssel abfragen; Modul `AuIniManager`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionstabelle (`ftable.py`), Aufrufer in den UI-Modulen (z. B. [`AgcmUIControl`](AgcmUIControl.md):_LoadTextureFromINI`), EP8-Quelle `Modules/AUtility/AuIniManager/AuIniManager.cpp`. Alle Adressen gelten nur für den 2017er Build. Die Klasse hat keine eigene Vtable (keine RTTI).

## Kernbefund

- **Abdeckung:** 14 von 41 Quellmethoden zugeordnet (Lesepfad: `SetPath`, `ReadFile`, `FromFile`, `FromMemory`, `ClearAllSectionKey`, `GetKeyIndex`, `GetSectionName`, `GetNumKeys`, `GetKeyName`, beide `GetValue`, `GetValueI`, `GetValueF`, `FindKey` (Abschnittsnummer), dazu Konstruktor und Destruktorrumpf).
- **Nicht gefunden:** alle Schreib- und Änderungsfunktionen (`SetValue*`, `AddSection`, `AddKey`, `WriteFile`, `EncryptSave`, `WritePartIndices`) – sie gehören in der Quelle zum Editor –, außerdem `Initialize`, `GetPackName`, `ParseMemory`, `StringMid`, `GetStringValue`, `GetValueI64`, `FindSection`, `FindKey(Name)`, `SetMode`/`SetType`, `ReadPartIndices`, `GetKeyNameTable`, `GetStartIndex`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuIniManagerA.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetKeyNameTable` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 1 | `GetKeyIndex` | `0x004F16B0` | 174 | von Hand geprüft |
| 2 | `Initialize` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 3 | `SetPath` | `0x004EFDE0` | 42 | von Hand geprüft |
| 4 | `ReadFile` | `0x004F3FC0` | 79 | von Hand geprüft |
| 5 | `GetPackName` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 6 | `FromMemory` | `0x004F2AC0` | 2550 | von Hand geprüft |
| 7 | `ParseMemory` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 8 | `FromFile` | `0x004F34D0` | 2154 | von Hand geprüft |
| 9 | `StringMid` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 10 | `GetSectionName` | `0x004EFE90` | 30 | von Hand geprüft |
| 11 | `GetNumKeys` | `0x004F0480` | 90 | von Hand geprüft |
| 12 | `GetKeyName` | `0x004F0960` | 80 | von Hand geprüft |
| 13 | `GetValue` | `0x004F04E0` | 84 | von Hand geprüft |
| 14 | `GetValue` | `0x004F1F60` | 260 | von Hand geprüft |
| 15 | `GetStringValue` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 16 | `GetStringValue` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 17 | `GetValueI` | `0x004F2070` | 46 | von Hand geprüft |
| 18 | `GetValueI64` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 19 | `GetValueF` | `0x004F20A0` | 46 | von Hand geprüft |
| 20 | `FindSection` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 21 | `FindKey` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 22 | `FindKey` | `0x004F20D0` | 259 | von Hand geprüft |
| 23 | `SetValue` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 24 | `SetValue` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 25 | `SetValueI` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 26 | `SetValue` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 27 | `SetValueI64` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 28 | `SetValueF` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 29 | `AddSection` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 30 | `AddKey` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 31 | `AddKey` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 32 | `WriteFile` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 33 | `ClearAllSectionKey` | `0x004F27F0` | 175 | von Hand geprüft |
| 34 | `SetMode` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 35 | `SetType` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 36 | `ReadPartIndices` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 37 | `ReadPartIndices` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 38 | `WritePartIndices` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 39 | `GetStartIndex` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |
| 40 | `EncryptSave` | – | | nicht zugeordnet (im Binary nicht eindeutig bestimmt; die Schreib- und Änderungsfunktionen gehören zum Editor); Verbleib offen |

14 von 41 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `GetValue_name` (`0x004F1F60`), `~AuIniManagerA_body` (`0x004F25E0`), `AuIniManagerA` (`0x004F3F10`).

## Aufbau

Objektlayout aus den Zugriffen: Modus/Typ-Flags `+0x00` (Bit 0 = Speicherung nach Abschnitten, Bit 1 = in Vektoren), Pfad `+4` (STL-Zeichenkette), Anzahl der Abschnitte `+0x1C`, Feld der Abschnitte `+0x28` (je `0x108` Byte: Name, `+0x100` Anzahl Schlüssel, `+0x104` Zeiger auf die Schlüssel, je `0x108` Byte: Namenshash `+0`, Wert ab `+4`), Zeichenpuffer `+0x44` (`0x400` Byte) und Typ-Flags `+0x3C`. Der Konstruktor (`0x004F3F10`, 171 Byte) setzt die Felder, legt den Puffer an und ruft `ClearAllSectionKey`.

## Lesen

`SetPath` (`0x004EFDE0`) setzt den Dateinamen; `ReadFile` (`0x004F3FC0`, 79 Byte) leert die Daten (`ClearAllSectionKey` `0x004F27F0`) und liest je nach Typ-Flag per `FromFile` (`0x004F34D0`, 692 Byte) oder `FromMemory` (`0x004F2AC0`, 2.576 Byte; beide gleichen in Größe den 341 bzw. 437 Zeilen der Quelle). `GetNumKeys` (`0x004F0480`) liefert die Schlüsselzahl eines Abschnitts, `GetKeyName` (`0x004F0960`) den Namen, `GetValue(Abschnitt, Schlüssel, Standard)` (`0x004F04E0`, 58 Aufrufer) den Wert; `GetKeyIndex` (`0x004F16B0`) bildet den Hash eines Schlüsselnamens; `FindKey` (`0x004F20D0`) sucht den Schlüssel in einem Abschnitt; `GetValue(Name, Name, Standard)` (`0x004F1F60`) holt den Wert über Abschnitts- und Schlüsselnamen, `GetValueI` (`0x004F2070`, `atoi`) und `GetValueF` (`0x004F20A0`, `atof`) wandeln ihn.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Dekompilat) sind `SetPath`, `GetSectionName`, `GetNumKeys`, `GetValue` (beide), `GetKeyName` (Anfang), `FindKey`, `GetValueI`/`GetValueF`, `ClearAllSectionKey` und der Konstruktor. `FromFile` und `FromMemory` sind nur nach Größe und Aufrufstruktur (`ReadFile` ruft beide je nach Flag) zugeordnet; `GetKeyIndex` nach seinem Einsatz als Hash in `FindKey`/`GetValue`. Die Zuordnung von `GetValue(Name, Name)` zu `0x004F1F60` folgt aus dem Abschnittsvergleich über `0x108`-Byte-Einträge.
- Das Schlüsselwort „Initialize“ der Quelle (10 Zeilen) fehlt; die Abschnittsliste wird im Binary vom Konstruktor und von `ReadFile` über `ClearAllSectionKey` gesetzt. Der Unterschied zwischen Typ-Flag Bit 0 und Bit 1 ist aus den Zugriffen auf `+0x2C` (Vektoren) und `+0x28` (Feld) geschlossen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 4, eingebaut: 10, nicht im Client: 2, ohne Kandidat: 5, zugeordnet: 8.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `AddSection` | 46 | `0x004F3D50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetValue_3` | 0 | `0x004F4140` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetValue_2` | 0 | `0x004F4010` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetValue` | 38 | `0x004F07D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseMemory` | 315 | `0x004F1760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddKey` | 58 | `0x004F21E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetKeyNameTable` | 4 | `0x004F0910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `WriteFile` | 128 | `0x004F09B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetPackName` (`0x004F2930`), `StringMid` (`0x004F2930`), `ReadPartIndices` (`0x004F0080`), `ReadPartIndices` (`0x004F0080`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIControl`](AgcmUIControl.md)
