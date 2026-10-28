# AgcmEventSiegeWarNPC (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventSiegeWarNPC` (Belagerungs-NPC-Ereignis) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten und Operationsbytes, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `OnAddModule` und `CBEventRequest` zugeordnet, `CBEventGrant` nicht angemeldet.
- **OnAddModule:** 4 Module in der Reihenfolge der Quelle ([`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventSiegeWarNPC`](AgpmEventSiegeWarNPC.md), [`AgcmEventManager`](AgcmEventManager.md), `AgpmCharacter (als `AgcmCharacter`-Zeiger gespeichert)`); Anmeldung: Ereignis `0x21` → `CBEventRequest` (`0x006DEB00`). `CBEventGrant` wird in der Quelle nicht angemeldet (leerer Rumpf) und fehlt im Binary.
- **Abweichungen:** Die Quelle holt den Zeiger `m_pcsAgcmCharacter` mit `GetModule("AgpmCharacter")` statt `"AgcmCharacter"`; das Binary enthält dieselbe Zeichenkette zweimal (`"AgpmCharacter"`) und stimmt damit mit der Quelle überein (Fehler schon in der Quelle).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventSiegeWarNPC.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DEBD0` | 130 | vtable/String |
| 1 | `CBEventRequest` | `0x006DEB00` | 151 | Callback-Registrierung |
| 2 | `CBEventGrant` | – | | in der Quelle nicht angemeldet (leerer Rumpf), im Binary keine Funktion |

2 von 3 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006DEAB0`), `~AgcmEventSiegeWarNPC` (`0x006DEBA0`).

## Abweichungen von der EP8-Quelle

- Die Quelle holt den Zeiger `m_pcsAgcmCharacter` mit `GetModule("AgpmCharacter")` statt `"AgcmCharacter"`; das Binary enthält dieselbe Zeichenkette zweimal (`"AgpmCharacter"`) und stimmt damit mit der Quelle überein (Fehler schon in der Quelle).

## Grenzen

- Die Ereignis-ID `0x21` ist die im Dekompilat sichtbare Zahl; sie wurde nicht gegen die Aufzählung in der Quelle nachgezählt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventSiegeWarNPC`](AgpmEventSiegeWarNPC.md)
- **Erwähnt in:** [`AgcmUISiegeWar`](AgcmUISiegeWar.md)
