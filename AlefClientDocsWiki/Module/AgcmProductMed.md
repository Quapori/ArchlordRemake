# AgcmProductMed (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmProductMed` (Vermittler zwischen Fertigkeiten, Herstellung/Sammeln und Oberfläche) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmProductMed/AgcmProductMed.cpp` und `AgpmProduct.h`/`ApDefine.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle sieben Methoden sind zugeordnet, darunter die zwei vorher unbenannten `OnResult` und `SendPacketGather`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmProductMed.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006A24C0` | 321 | vtable/String |
| 1 | `CBPreProcessSkill` | `0x006A2210` | 438 | Callback-Registrierung |
| 2 | `CBActionSkillResult` | `0x006A23D0` | 127 | Callback-Registrierung |
| 3 | `CBAfterCooldown` | `0x006A2450` | 42 | Callback-Registrierung |
| 4 | `CBProductResult` | `0x006A2480` | 57 | Callback-Registrierung |
| 5 | `OnResult` | `0x006A2060` | 188 | von Hand geprüft |
| 6 | `SendPacketGather` | `0x006A2120` | 183 | von Hand geprüft |

7 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmProductMed` (`0x006A1F90`), `~AgcmProductMed` (`0x006A21E0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA0` | `Zeiger [`AgpmProduct`](AgpmProduct.md) (dessen `+0xD5C` ist das Paketobjekt)` | `SendPacketGather` |
| `this+0xBA4` | `Zeiger `AgcmCharacter` (dessen `+0x1596C` ist der eigene Charakter)` | `SendPacketGather` |
| `this+0xBB8` | `gemerkte Fertigkeit `m_pAgpdSkill`` | `OnResult` |
| `this+0xBBC` | `gemerktes Ziel `m_lTargetID`` | `OnResult` |

## Vtable und Aufbau

Konstruktor `0x006A1F90` (204 Byte; trägt `AgcmProductMed` als Modulnamen ein, Modultyp Client, Idle aus, nullt die Modulzeiger, `m_lCooldownID` und `m_lTargetID` auf die ungültigen Kennungen), Destruktor `0x006A21E0` (Löschwrapper). `OnAddModule` (`0x006A24C0`, 321 Byte) holt [`AgpmSkill`](AgpmSkill.md), [`AgcmSkill`](AgcmSkill.md), `AgpmProduct`, `AgcmCharacter`, [`AgcmProduct`](AgcmProduct.md), [`AgcmUIProduct`](AgcmUIProduct.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md) und [`AgcmUICooldown`](AgcmUICooldown.md), verlangt alle außer dem Abkühlmodul und meldet `CBActionSkillResult` (`0x006A23D0`, bei `AgpmSkill::ReceiveAction`), `CBPreProcessSkill` (`0x006A2210`, bei `AgcmSkill`) und `CBProductResult` (`0x006A2480`, bei `AgpmProduct`) an; ist `AgcmUICooldown` vorhanden, kommt `CBAfterCooldown` (`0x006A2450`) dazu und die Abkühlkennung wird angelegt.

## Sammeln und Ergebnis

`CBPreProcessSkill` (`0x006A2210`) prüft die Fertigkeit und gibt die Meldung „Fertigkeit benutzt“ im Systemchat aus; Fertigkeit und Ziel werden in `m_pAgpdSkill`/`m_lTargetID` gemerkt. `CBActionSkillResult` startet bei Aktionsart „Fertigkeit wirken“ die Abkühlanzeige oder, ohne Abkühlmodul, direkt `SendPacketGather`; `CBAfterCooldown` sendet nach Ablauf das Sammelpaket.
`SendPacketGather` (`0x006A2120`, 183 Byte, vorher unbenannt) baut mit dem Paketobjekt von `AgpmProduct` (`+0xD5C`) ein Paket vom Typ `0x17` (`AGPMPRODUCT_PACKET_TYPE`) mit Operation 2 (`GATHER`), eigener Charakter-ID, Fertigkeits-ID und Ziel-ID und sendet es, wenn eine Länge über 0 herauskommt; ohne eigenen Charakter liefert es FALSE. Aufrufer sind `CBActionSkillResult` und `CBAfterCooldown`.
`OnResult` (`0x006A2060`, 188 Byte, vorher unbenannt) setzt Fertigkeit und Ziel zurück (`this+0xBB8`, `+0xBBC`), holt die Fertigkeit und verzweigt: gehört sie zu einer Herstellungskategorie (`IsComposeSkill`, `0x0055F390`), geht das Ergebnis an `AgcmUIProduct::OnResult` (`0x006A3B80`), sonst an `AgcmUIProductSkill::OnResult` (`0x006A58C0`). Aufrufer sind `CBPreProcessSkill` (Sofortergebnis) und `CBProductResult`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der Modulzeiger zu `this+0xBA0`/`+0xBA4` folgt aus den Zugriffen in `SendPacketGather`; die Namen der übrigen Zeiger zwischen `0xB98` und `0xBB4` sind nicht einzeln geprüft.
- `CBPreProcessSkill`, `CBActionSkillResult`, `CBAfterCooldown` und `CBProductResult` waren schon über die Registrierung benannt und wurden hier nur über Aufrufbeziehungen geprüft, nicht Zeile für Zeile gelesen.
- Die Paketfelder nach der Ziel-ID (vier leere Felder) sind aus den Aufrufargumenten gelesen, nicht gegen einen Mitschnitt geprüft.

## Querverweise

- **Erwähnt Module:** [`AgcmProduct`](AgcmProduct.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIProduct`](AgcmUIProduct.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md), [`AgpmProduct`](AgpmProduct.md), [`AgpmSkill`](AgpmSkill.md)
- **Erwähnt in:** [`AgcmProduct`](AgcmProduct.md)
