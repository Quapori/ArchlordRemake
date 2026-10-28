# AgcmQuest (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmQuest` (Quest-Pakete senden, Namensfarben aus XML) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmQuest/AgcmQuest.cpp`. Das Paketformat steht im Bericht [Quest](Quest.md), die Oberfläche in [AgcmUIQuest2](AgcmUIQuest2.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 11 von 14 Quellmethoden zugeordnet (`OnInit`, `OnIdle`, `OnDestroy` über gemeinsame Rümpfe, `OnAddModule`, fünf `SendPacket…`, `ReadXMLData`, `GetJournalQuestNameColor`); drei Farbfunktionen sind eingebaut.
- **Sendefunktionen:** Die fünf Pakete (Quest verlangen, abschließen, abbrechen, Checkpoint, Tagebuch-Eintrag ändern) werden jeweils in `AgpmQuest` gebaut und über `SendPacket` verschickt; die Zuordnung ist über die Aufrufer in [`AgcmUIQuest2`](AgcmUIQuest2.md) eindeutig.
- **Farben:** `ReadXMLData` liest Annahme-, Tagebuch-, Haupt- und Sonderfarben als `R/G/B`-Attribute; Zeichenketten identisch zur Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmQuest.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 1 | `OnAddModule` | `0x00613360` | 30 | vtable/String |
| 2 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `OnIdle-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 4 | `SendPacketRequireQuest` | `0x00613380` | 115 | von Hand geprüft |
| 5 | `SendPacketCompleteQuest` | `0x00613400` | 120 | von Hand geprüft |
| 6 | `SendPacketQuestCancel` | `0x00613480` | 110 | von Hand geprüft |
| 7 | `SendPacketCheckPoint` | `0x006134F0` | 120 | von Hand geprüft |
| 8 | `SendPacketQuestJournalRegisterChange` | `0x00613570` | 115 | von Hand geprüft |
| 9 | `ReadXMLData` | `0x00613710` | 1460 | Zeichenkette |
| 10 | `GetAcceptQuestNameColor` | – | | in die Aufrufer eingebaut (`AgcmUIQuest2`) |
| 11 | `GetMainQuestNameColor` | – | | in die Aufrufer eingebaut |
| 12 | `GetJournalQuestNameColor` | `0x006135F0` | 58 | von Hand geprüft |
| 13 | `GetCustomColor` | – | | eine Zeile, eingebaut |

11 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmQuest` (`0x00613630`), `~AgcmQuest_body` (`0x00613690`), `~AgcmQuest` (`0x00613CD0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98` | `Zeiger auf `AgpmQuest` (`m_pcsAgpmQuest`)` | `OnAddModule` |
| `0xBA4` | `Annahmefarben (3 × DWORD)` | `ReadXMLData`, `GetJournalQuestNameColor`-Nachbarschaft |
| `0xBB0 / 0xBB4` | `Tagebuchfarben Mission / Epic` | `GetJournalQuestNameColor` |
| `0xBC4` | `Liste `m_listQuestNameMain`` | Konstruktor, Destruktor |

## Vtable

Vtable bei `0x008C06CC`: Slot 0 Destruktor `0x00613CD0`, 1 `OnAddModule` (`0x00613360`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`, `return TRUE`), 3–5 `OnIdle` u. a. (gemeinsamer Rumpf `0x0067FAB0`), 6 und 7 `0x0067AC90` (`OnDestroy` = `return TRUE`).

## OnAddModule und Konstruktor

`OnAddModule` (`0x00613360`, 30 Byte) holt über `GetModule("AgpmQuest")` das Paketmodul in `this+0xB98` und liefert `FALSE`, wenn es fehlt. Der Konstruktor (`0x00613630`) ruft den Basiskonstruktor, setzt die vtable, legt den Modulnamen `"AgcmQuest"` an (`strncpy`, 0x27 Byte) und initialisiert die Liste `m_listQuestNameMain` bei `this+0xBC4` (leerer Listenknoten). Ein zweiter Rumpf (`0x00613690`) gibt die Listenknoten frei (`__node_alloc::deallocate`, 0x10 Byte je Knoten) und ruft den Basisdestruktor; der Eintrag in Slot 0 (`0x00613CD0`) ist der zugehörige löschende Destruktor.

## Pakete senden (SendPacket…)

Alle fünf Funktionen haben dieselbe Form: Paket über `AgpmQuest::MakePacket…` bauen (`0x00590E60`, `0x00590EE0`, `0x00590F60`, `0x00590FB0`, `0x00591020`), bei fehlendem Paket oder Länge < 1 `FALSE`, sonst senden (`0x004E45A0`), danach `FreePacket` (in Ghidra mit dem Namen `AgcWindow::OnDragDrop` angezeigt, weil der Rumpf mit einer anderen Funktion zusammengefaltet ist). Die Zuordnung ist durch die Aufrufer eindeutig: `SendPacketRequireQuest` (`0x00613380`) und `…CompleteQuest` (`0x00613400`) werden nur von `AgcmUIQuest2::CBButtonQuestAcceptListClick` (`0x006B1370`) aufgerufen, `…QuestCancel` (`0x00613480`) von `CBReturnCancelQuest` (`0x006B1F90`) und dem Abbrechen-Dialog (`0x006B2050`), `…CheckPoint` (`0x006134F0`) von `CBAfterCooldown` (`0x006B09C0`) und `…QuestJournalRegisterChange` (`0x00613570`) vom Tagebuch (`AgcmQuestJournal`, `0x00612490`, `0x00612710`) und `AgcmUIQuest2` (`0x006B4B40`, `0x006B4CD0`). Die Argumentzahl (3/4/2/4/3) stimmt mit der Quelle überein.

## Farben (XML)

`ReadXMLData` (`0x00613710`, 1460 Byte) liest die XML-Datei mit `AuXmlParser` und füllt vier Farbtabellen: Knoten `Accept` (`NEW`, `ING`, `COMPLETE`), `Journal` (`Mission`, `Epic`), `Main` (mehrere `Color`-Knoten mit Attribut `Interval`) und die benutzerdefinierten Farben (`EPICSCENARIO`, `MISSIONSCENARIO`, `AREA`). Jede Farbe ergibt sich aus den Attributen `R`, `G`, `B` (`0xFF<<24 + R<<16 + G<<8 + B`). Alle Zeichenketten stimmen mit der Quelle überein. Die Annahmefarben liegen ab `this+0xBA4` (drei Einträge), die Tagebuchfarben ab `this+0xBB0`.
`GetJournalQuestNameColor` (`0x006135F0`, 58 Byte) liefert `this+0xBB0` (Mission), wenn die Kategorie der Quest-Vorlage (`+0xEC`) gleich 1 ist (Szenario), sonst `this+0xBB4` (Epic); der einzige Aufrufer ist `AgcmQuestJournal::MakeJournalText` (`0x00612580`).
`GetAcceptQuestNameColor`, `GetMainQuestNameColor` und `GetCustomColor` haben im Binary keine eigene Funktion; sie sind in die Aufrufer eingebaut (`ComposeAcceptText…`, `ComposeMainText` in `AgcmUIQuest2`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, Paketfunktionen, XML-Zeichenketten).

## Grenzen

- `ReadXMLData` wurde über die Zeichenketten und die Reihenfolge der Knotennamen zugeordnet, die Farbberechnung nicht Zeile für Zeile verglichen.
- Die Offsets der Farbtabellen ergeben sich aus dem Zugriff in `GetJournalQuestNameColor` und der Reihenfolge in der Quelle; `0xBA4` für die Annahmefarben ist daraus abgeleitet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 3, nicht im Client: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIQuest2`](AgcmUIQuest2.md)
- **Erwähnt in:** [`AgcmUIQuest2`](AgcmUIQuest2.md)
