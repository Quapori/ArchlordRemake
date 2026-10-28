# AgcmAmbOcclMap (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmAmbOcclMap` (Umgebungsverdeckung pro Objekt) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle Methoden außer den Kleinfunktionen zugeordnet (schon über die Anmeldung benannt: `objectStreamWriteCB`, `objectStreamReadCB`, `objectConstructor`, `objectDestructor`, `initObjectCB`); `OnDestroy` ist der gemeinsame `return TRUE`-Rumpf (Vtable-Slot 7).
- **OnAddModule** (`0x006F56B0`): holt [`ApmObject`](ApmObject.md) und [`AgcmObject`](AgcmObject.md) in dieser Reihenfolge, meldet die Stream-Rückrufe für Objektdaten bei `ApmObject` an und `initObjectCB` (`0x006F5680`) bei `AgcmObject`; **OnInit** (`0x006F52F0`) richtet den Speicherpool (`AtomicData`, 10000 Einträge) ein.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmAmbOcclMap.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006F56B0` | 153 | vtable/String |
| 1 | `OnInit` | `0x006F52F0` | 26 | vtable/String |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 3 | `getObjectData` | – | | eine Zeile, eingebaut |
| 4 | `objectStreamWriteCB` | `0x006F5310` | 340 | Callback-Registrierung |
| 5 | `objectStreamReadCB` | `0x006F54F0` | 289 | Callback-Registrierung |
| 6 | `objectDestructor` | `0x006F5620` | 87 | Callback-Registrierung |
| 7 | `objectConstructor` | `0x006F5470` | 47 | Callback-Registrierung |
| 8 | `initObjectCB` | `0x006F5680` | 34 | Callback-Registrierung |
| 9 | `searchAtomicById` | – | | nicht einzeln gefunden |
| 10 | `allocAtomicData` | – | | in `objectConstructor` eingebaut |
| 11 | `freeAtomicData` | – | | in `objectDestructor` eingebaut |

8 von 12 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmAmbOcclMap` (`0x006F5260`), `~AgcmAmbOcclMap` (`0x006F54A0`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die fünf Objekt-Rückrufe waren schon vor diesem Bericht über ihre Anmeldereihenfolge benannt und wurden hier nicht Zeile für Zeile mit der Quelle verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, nicht als eigene Funktion: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmObject`](AgcmObject.md), [`ApmObject`](ApmObject.md)
