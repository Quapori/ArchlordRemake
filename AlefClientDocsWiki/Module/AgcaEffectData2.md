# AgcaEffectData2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AgcaEffectData2` (Verwaltung der Effektdaten je Effektsatz, aus `AgcmEffectDataAdmin/AgcaEffectData.cpp`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Die Klasse leitet von `ApAdmin` ab. Belege: Ghidra-Dekompilat, Funktionsübersicht (`fcalls.py`), EP8-Quelle. Alle Adressen gelten nur für den 2017er Build. Das Modul `AgcmEffectDataAdmin` selbst ist nur diese Klasse (der Vorgänger `AgcaEffectData` ist in der Quelle auskommentiert).

## Kernbefund

- **Abdeckung:** 5 von 8 Quellmethoden zugeordnet (`Create`, beide einfachen `Delete`, `DeleteAll`, `GetData`), dazu Konstruktor (`0x00717DC0`), Destruktorrumpf (`0x00717DE0`) und Löschwrapper (`0x00717FB0`).
- **Nicht gefunden:** `Delete(Satz, Daten)`, `CopyData`, `CopyDataSet`. In der Nähe liegen `0x00717A10` und `0x007172B0` (Kopieren/Zuweisen eines Datensatzes), sie sind aber ohne Zeilenvergleich nicht eindeutig `CopyData`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcaEffectData2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Create` | `0x00717DF0` | 60 | von Hand geprüft |
| 1 | `Delete` | `0x00717FE0` | 31 | von Hand geprüft |
| 2 | `Delete` | `0x00717E30` | 89 | von Hand geprüft |
| 3 | `Delete` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen |
| 4 | `DeleteAll` | `0x00717E90` | 125 | von Hand geprüft |
| 5 | `GetData` | `0x00717F10` | 152 | von Hand geprüft |
| 6 | `CopyData` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen |
| 7 | `CopyDataSet` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen |

5 von 8 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00717dc0` (`0x00717DC0`), `ctor_or_dtor_00717de0` (`0x00717DE0`), `~AgcaEffectData2` (`0x00717FB0`), `Delete_free` (`0x00717FE0`).

## Funktionen

`Create` (`0x00717DF0`) legt einen Datensatz an (`0x5C` Byte, `AgcdUseEffectSetData`), setzt den Index (`m_ulIndex`) und zählt `m_ulCount` (`this+0xB4`) hoch. `Delete(Daten)` (`0x00717E30`) gibt die vier Zeiger frei, die ein Datensatz besitzt (Drehung `+0x34`, Zusatzdaten `+0x38`, Klangname `+8`, Versatz `+0x14`); `Delete(Daten, bFree)` (`0x00717FE0`) ruft das und löscht den Datensatz bei Bedarf selbst. `DeleteAll` (`0x00717E90`) läuft über die verkettete Liste des Satzes (Zeiger `+0x5C`), gibt jeden Datensatz so frei und leert den Kopf. `GetData` (`0x00717F10`) sucht den Datensatz mit dem Index `ulFindIndex` in der Liste und hängt bei `bAdd` einen neuen an (`0x60` Byte je Listenknoten).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Alle fünf zugeordneten Funktionen sind im Dekompilat vollständig gelesen; die Namen folgen aus den freigegebenen Feldern und der Listenstruktur (Knoten `0x60` Byte, Nachfolger `+0x5C`).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, nicht als eigene Funktion: 1, nicht im Client: 1.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `Delete` (`0x00717720`).

<!-- LUECKENREGISTER-NACHTRAG-END -->
