# AgcmUICooldown (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse `AgcmUICooldown` (Fortschrittsbalken für Wartezeiten (Items, Quests, Skills)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUICooldown/AgcmUICooldown.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 17 von 18 Quellmethoden sind zugeordnet; neu sind `AddEvent`, `RegisterCooldown`, `StartCooldown`, `CancelCooldown`, `OnEnd` und `ProcessCooldown`.
- **Grenzen:** höchstens 50 Zeitgeber, nur einer gleichzeitig; fünf UI-Ereignisse.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUICooldown.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 1 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnAddModule` | `0x006F0570` | 132 | vtable/String |
| 3 | `OnIdle` | `0x006F0600` | 18 | vtable/String |
| 4 | `AddEvent` | `0x006F0060` | 67 | ver |
| 5 | `AddFunction` | `0x006F0420` | 85 | Zeichenkette |
| 6 | `AddDisplay` | `0x006F00B0` | 101 | Zeichenkette |
| 7 | `AddUserData` | `0x006EFED0` | 44 | Zeichenkette |
| 8 | `RegisterCooldown` | `0x006EFF00` | 67 | ver |
| 9 | `StartCooldown` | `0x006F0120` | 220 | ver |
| 10 | `CancelCooldown` | `0x006F0200` | 74 | ver |
| 11 | `ProcessCooldown` | `0x006F0480` | 225 | ver |
| 12 | `OnEnd` | `0x006F0250` | 103 | ver |
| 13 | `CBOpen` | `0x006EFF50` | 30 | UI-Registrierung |
| 14 | `CBClose` | `0x006F02C0` | 48 | UI-Registrierung |
| 15 | `CBDisplayTitle` | `0x006EFF70` | 73 | UI-Registrierung |
| 16 | `CBDisplayProgress` | `0x006EFFC0` | 103 | UI-Registrierung |
| 17 | `CBKeydownESC` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

17 von 18 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmUICooldown` (`0x006F0030`), `ctor_or_dtor` (`0x006F02F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBBC` | `Anzahl registrierter Zeitgeber (`m_lCount`)` | `RegisterCooldown` |
| `0xBC0` | `ID des laufenden Zeitgebers (−1 = keiner)` | `StartCooldown` |
| `0xBA4…` | `Ereignis-IDs (5 × 4 Byte)` | `AddEvent` |
| `0x1E84` | `verstrichene Zeit (`m_ulElapsed`)` | `StartCooldown` |
| `Eintrag 0x60 Byte, ab 0xBC8` | `Zeitgeber-Tabelle (Rückruf, Klasse, Start, Dauer, UI-Flag, Titel)` | `RegisterCooldown`, `StartCooldown` |

## Vtable

Vtable bei `0x008D96E4`: Slot 0 Destruktor `0x006F0030`, 1 `OnAddModule` (`0x006F0570`), 3 `OnIdle` (`0x006F0600`), 2/6/7 der `return TRUE`-Rumpf `0x0067AC90` (u. a. die leeren `OnInit` und `OnDestroy` der Quelle).

## Ablauf

Bis zu **50** Zeitgeber (`AGCMUICOOLDOWN_MAX`; `RegisterCooldown`, `0x006EFF00`, liefert −1 ab dem 51.) mit je 0x60 Byte (Titel höchstens 64 Zeichen). Es läuft immer nur einer: `StartCooldown` (`0x006F0120`) lehnt ab, wenn bereits einer läuft (aktuelle ID `+0xBC0` ≠ −1), setzt Dauer, Titel und Benutzerdaten, wirft das Ereignis `UI_COOLDOWN_OPEN`, wenn die Oberfläche gebraucht wird, und bei Klangart > 1 das passende Ereignis.
`OnIdle` ruft `ProcessCooldown` (`0x006F0480`): Die Startzeit wird beim ersten Aufruf gesetzt; ist die Dauer erreicht, wird `OnEnd` (`0x006F0250`) gerufen, das das Schließ-Ereignis wirft, den Rückruf des Zeitgebers aufruft und die Startzeit zurücksetzt. `CancelCooldown` (`0x006F0200`) bricht nur den laufenden Zeitgeber mit passender ID ab.
Die Zuordnung dieser fünf Funktionen stützt sich auf Aufrufer und Aufgerufene (Ereignis-Würfe, `OnIdle` → `ProcessCooldown`); der Quelltext wurde nicht Zeile für Zeile verglichen.

## Ereignisse

`AddEvent` (`0x006F0060`) legt fünf Ereignisse an (Namenstabelle, 30 Byte pro Eintrag, ab `0x00957F48`): `UI_COOLDOWN_OPEN`, `UI_COOLDOWN_CLOSE`, `UI_COOLDOWN_ITEM`, `UI_COOLDOWN_QUEST`, `UI_COOLDOWN_SKILL`. Anzahl wie in der Quelle.

## Aufrufer

`StartCooldown` rufen u. a. [`AgcmUIAuction`](AgcmUIAuction.md):SetCooldown` und weitere Callbacks (`CBReceiveResult`, `CBStatusInfo`, `CBActionSkillResult`); `CancelCooldown` rufen u. a. `CBReceiveResult`, `CBUpdateStatus` und `CBStatusInfo`.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006F0420`, `0x006F00B0`, `0x006EFED0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (2)

| Name | Id | Handler |
|---|---:|---|
| `COOLDOWN_OPEN` |  | `CBOpen` |
| `COOLDOWN_CLOSE` |  | `CBClose` |

**Anzeige** (3)

| Name | Id | Handler |
|---|---:|---|
| `COOLDOWN_DISP_TITLE` | 0 | `CBDisplayTitle` |
| `COOLDOWN_DISP_BARCUR` | 1 | `CBDisplayProgress` |
| `COOLDOWN_DISP_BARMAX` | 2 | `CBDisplayProgress` |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `COOLDOWN_UD_DUMMY` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`RegisterCooldown`, Beginn von `StartCooldown`, `AddEvent`).

## Grenzen

- `CBKeydownESC` ist im Binary nicht zu finden; in `OnAddModule` gibt es keinen Aufruf, der ihn registriert (er ist in der Quelle vermutlich nirgends angemeldet).
- `ProcessCooldown`, `OnEnd` und `CancelCooldown` wurden nur nach Aufrufern und Aufgerufenen zugeordnet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIAuction`](AgcmUIAuction.md)
- **Erwähnt in:** [`AgcmItem`](AgcmItem.md), [`AgcmProductMed`](AgcmProductMed.md), [`AgcmUIAuction`](AgcmUIAuction.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIRefinery`](AgcmUIRefinery.md), [`AgcmUIRemission`](AgcmUIRemission.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md)
