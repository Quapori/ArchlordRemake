# AgcaAnimation2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AgcaAnimation2` (Verwaltung der Laufzeit-Animationen, aus `AgcmAnimation/AgcaAnimation.cpp`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Die Klasse leitet von `ApAdmin` ab. Belege: Ghidra-Dekompilat, Funktionsübersicht (`fcalls.py`), Aufrufgraph, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build. Das Modul `AgcmAnimation` selbst (die `ApModule`-Klasse) ist im Binary nicht enthalten: weder der Modulname `AgcmAnimation` noch ein RTTI-Eintrag kommt vor.

## Kernbefund

- **Abdeckung:** 8 von 24 Quellmethoden zugeordnet. Zugeordnet sind Konstruktor, Destruktorrumpf, die Setzer für Pfad/Anzahl, `RemoveRtAnim` (beide), `RemoveAllRtAnim` und `ReadRtAnim` (beide).
- **Nicht eindeutig:** die übrigen Funktionen im Bereich (`0x007015B0`, `0x007017B0`, `0x00701880`, `0x007018F0`, `0x00701970`, `0x007019C0`, `0x00701A70`, `0x00701AB0`, `0x00701BA0`, `0x00701BE0`, `0x00701C70`, `0x00701D10` …) sind Anlegen/Entfernen/Kopieren der Animationsdaten und Verwaltung der angehängten Daten; ihre Reihenfolge im Binary entspricht nicht der Quelle und eine Zuordnung nach Größe allein wäre geraten.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcaAnimation2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetAnimationPathAndExtension` | `0x007014C0` | 164 | von Hand geprüft |
| 1 | `SetMaxRtAnim` | `0x00701570` | 26 | von Hand geprüft |
| 2 | `SetMaxFlags` | `0x00701590` | 29 | von Hand geprüft |
| 3 | `SetAttachedData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 4 | `RemoveRtAnim` | `0x00701690` | 233 | von Hand geprüft |
| 5 | `RemoveRtAnim` | `0x00701780` | 46 | von Hand geprüft |
| 6 | `ReadRtAnim` | `0x00702160` | 378 | von Hand geprüft |
| 7 | `ReadRtAnim` | `0x007022E0` | 68 | von Hand geprüft |
| 8 | `AddRtAnim` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 9 | `GetRtAnim` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 10 | `CreateAnimData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 11 | `AddAnimData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 12 | `AddAnimation` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 13 | `AddAnimation` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 14 | `CopyAnimation` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 15 | `DestroyAnimData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 16 | `RemoveAnimData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 17 | `RemoveAnimation` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 18 | `RemoveAllAnimation` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 19 | `RemoveAllRtAnim` | `0x00701B10` | 89 | von Hand geprüft |
| 20 | `GetAnimData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 21 | `GetAnimDataIndex` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 22 | `AddFlags` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |
| 23 | `GetAttachedData` | – | | nicht zugeordnet (Funktion im Bereich `0x007013C0`–`0x00702400` vorhanden, aber nicht eindeutig bestimmt); Verbleib offen |

8 von 24 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcaAnimation2` (`0x007013C0`), `RemoveRtAnim_animation` (`0x00701780`), `~AgcaAnimation2_body` (`0x00702080`), `ReadRtAnim_animation` (`0x007022E0`), `~AgcaAnimation2` (`0x00702360`).

## Funktionen

Vtable `AgcaAnimation2`: Löschwrapper `0x00702360` (Destruktorrumpf `0x00702080`: Vektor der angehängten Daten, `ApAdmin::RemoveObjectAll`, Aufrufliste `0x00701B10`). Der Konstruktor `0x007013C0` ruft `ApAdmin::ApAdmin` und legt Pfad/Erweiterung und Zähler an. `SetAnimationPathAndExtension` (`0x007014C0`) kopiert Pfad und Erweiterung in eigene Puffer; `SetMaxRtAnim` (`0x00701570`) und `SetMaxFlags` (`0x00701590`) rufen `ApAdmin::InitializeObject`.
`ReadRtAnim(AgcdAnimData2*)` (`0x00702160`, 378 Byte; Formate `%s%s` und `%s%s.%s`) baut Pfad, Name und Erweiterung zusammen und lädt die Animation über [`AgcmResourceLoader`](AgcmResourceLoader.md):LoadRtAnim`; die Fassung für `AgcdAnimation2*` (`0x007022E0`) ruft sie je Eintrag. `RemoveRtAnim` (`0x00701690`/`0x00701780`) entfernt den Eintrag aus der Verwaltung (`ApAdmin::RemoveObject`), `RemoveAllRtAnim` (`0x00701B10`) läuft über alle (`GetObjectSequence`) und leert dann (`RemoveObjectAll`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen ist nur der Aufrufgraph (`fcalls.py`) und der Kopf von `ReadRtAnim`; die Zuordnung der Setzer folgt aus der Form (Aufruf von `InitializeObject`), die der Entfernungsfunktionen aus den Aufrufen von `ApAdmin::RemoveObject`/`RemoveObjectAll`. `GetAttachedData` und `AddFlags` sowie die Anlege-/Kopierfunktionen sind nicht bestimmt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 5, eingebaut: 1, nicht im Client: 3, ohne Kandidat: 6, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `SetAttachedData` | 20 | `0x007015B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `AddAnimation` (`0x00701BE0`), `RemoveAllAnimation` (`0x00701BE0`), `GetAnimData` (`0x00701BE0`), `AddFlags` (`0x00701BE0`), `GetAttachedData` (`0x00702400`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmResourceLoader`](AgcmResourceLoader.md)
