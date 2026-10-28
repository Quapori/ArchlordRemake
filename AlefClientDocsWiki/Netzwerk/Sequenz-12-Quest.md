# Winsock-Sequenz 12: Quest und EventQuest

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei dokumentiert den Quest-Bereich des `alefclient.exe`. Quellen sind `alefclient.pseudocode.c`, besonders `AgpmQuest`, [`AgcmQuest`](../Module/AgcmQuest.md), `AgcmQuestJournal`, `AgpmEventQuest` und [`AgcmEventQuest`](../Module/AgcmEventQuest.md). Es wurde kein Live-Traffic mitgeschnitten; Serverdatenbank-Strukturen sind Inferenz.

## Kurzfazit

- Das Kern-Questmodul heisst `AgpmQuest` und registriert Modul-ID `0x13`.
- Quest-Events laufen zusaetzlich ueber `AgpmEventQuest` mit Modul-ID `0x3e`.
- `AgcmQuest` ist der Clientwrapper, der `AgpmQuest`-Pakete baut und ueber `FUN_004e45d0` sendet.
- `AgcmEventQuest` registriert sich beim [`AgcmEventManager`](../Module/AgcmEventManager.md) fuer Eventfunktion `0x1b`.
- Lokale Questflags werden in einem Bitfeld mit drei `0x100`-Byte-Bloecken verwaltet.
- Die UI kennt AutoStart/AutoEnd, QuestStart/Complete/Full und getrennte Meldungen fuer Main-Inventar voll und Quest-Inventar voll.

## AgpmQuest

Konstruktor: `FUN_005590c0`

Wichtige Punkte:

- Modulname: `AgpmQuest`
- Modul-ID: `FUN_004e4540(0x13)` -> `0x13`
- Objektgroessen:
  - `FUN_004e4190(0x1f68, 0)`
  - `FUN_004e4190(0x7c, 1)`
- Hauptlayout `+0x344`
- Nested-/Hilfslayout `+0x4d89`

Hauptlayout:

```text
+0x344:
  1,1
  5,1
  0xc,1
  0xc,1
  5,1
  5,1
  5,1
  5,1
  0xd,1
  0xd,1
  0xd,1
  0xff,0
```

Hilfslayout:

```text
+0x4d89:
  5,1
  5,1
  5,1
  5,1
  5,1
  0,0x31
  0xff,0
```

Interpretation:

- Erstes Feld ist Quest-Subopcode.
- Danach folgen Character-/Quest-IDs, Status-/Counterfelder, 64-bit-nahe Werte und optional Nested-Eventdaten.
- Typcode `0,0x31` im Hilfslayout deutet auf einen laengeren variablen Block oder String-/Blobfeld.

## Questflags

`AgpdQuestFlag` wird in `FUN_005910c0` konstruiert:

```text
memset(block1, 2, 0x100)
memset(block2, 2, 0x100)
memset(block3, 2, 0x100)
```

`FUN_00591020(flagStore, questId, value)` setzt/loescht ein Bit fuer Quest-IDs `1..0x17ff`.

Aufteilung:

- Quest-ID wird in drei Bereiche zu je `0x800` IDs zerlegt.
- Innerhalb des Bereichs wird per Byte/Bit indexiert.
- `param_3 == 0` loescht das Bit.
- sonst wird das Bit gesetzt.

Server-Inferenz:

- Der Server muss pro Charakter Questzustand/Flags fuer mindestens ca. `0x1800` Quest-IDs speichern koennen.
- Das Clientbitfeld ist wahrscheinlich ein kompakter Sync fuer bekannt/aktiv/abgeschlossen oder Teilflags.

## Client -> Server: AgcmQuest Wrapper

`AgcmQuest` wird in `FUN_00613da0` konstruiert und heisst `AgcmQuest`.

`FUN_00613ad0` bindet `AgpmQuest`.

Die folgenden Wrapper bauen jeweils ein `AgpmQuest`-Paket und senden es ueber `FUN_004e45d0`:

| Wrapper | Kernfunktion | Harte Subop | Bedeutung |
|---|---|---:|---|
| `FUN_00613af0` | `FUN_00591170` | Lowbyte aus Param, meist `0`/maskiert | Quest-Aktion mit Event-Nested-Paket |
| `FUN_00613b70` | `FUN_005911f0` | `2` | Quest annehmen/Start/Antwort mit Eventdaten |
| `FUN_00613bf0` | `FUN_00591270` | `6` | kurze Questaktion, wahrscheinlich Abbruch/Statusrequest |
| `FUN_00613c60` | `FUN_005912c0` | `0x0b` | Questaktion mit Zusatzparameter und Eventdaten |
| `FUN_00613ce0` | `FUN_00591330` | `0x0e` | Questaktion mit Nested-Block `+0x13624` |

### `FUN_00591170`

```text
FUN_0055ca00(eventData)
FUN_004ea280(AgpmQuest + 0xd10, 1, ..., module 0x13, subop, ..., nestedEvent, ...)
```

Der Subopcode kommt aus dem Lowbyte eines Parameters, nachdem `param_2 & 0xffffff00` gebildet wird. Das ist im Decompiler nicht als klare Konstante sichtbar.

### `FUN_005911f0`

Setzt:

```text
subop = 2
```

und packt ebenfalls ein Nested-Eventpaket aus [`ApmEventManager`](../Module/ApmEventManager.md):FUN_0055ca00`.

### `FUN_00591270`

Setzt:

```text
subop = 6
```

und sendet ein kurzes Questpaket mit wenigen Feldern.

### `FUN_005912c0`

Setzt:

```text
subop = 0x0b
```

und sendet Quest-ID/Zusatzparameter plus Nested-Eventpaket.

### `FUN_00591330`

Setzt:

```text
subop = 0x0e
```

und baut vorher einen Nested-Block bei `+0x13624`.

## AgpmEventQuest

Konstruktor: `FUN_0056f3a0`

- Modulname: `AgpmEventQuest`
- Modul-ID: `FUN_004e4540(0x3e)` -> `0x3e`
- Hauptlayout `+0x2e4`
- Hilfslayout `+0x4d29`

Hauptlayout:

```text
+0x2e4:
  1,1
  0xc,1
  5,1
  5,1
  0xff,0
```

Hilfslayout:

```text
+0x4d29:
  5,1
  0xff,0
```

Sendefunktion: `FUN_0056f630`

- baut ein Nested-Eventpaket ueber `FUN_0055ca00`.
- sendet Modul `0x3e`.
- packt Character-/Quest-/Eventparameter.

Receive-/Eventseite:

- `FUN_0056f510` versucht Eventdaten aus `ApmEventManager` zu lesen.
- Bei Erfolg setzt es Quest-/Eventstatus am Character zurueck und ruft Callback `0`.
- Bei Misserfolg setzt es Felder um `character + 0x6e0..0x6ec` und ggf. Objekt-/Mapdaten.
- `FUN_0056f6b0` prueft Characterzustand und loest einen Quest-Callback aus.

## AgcmEventQuest

Konstruktor: `FUN_006de3b0`

- Modulname: `AgcmEventQuest`
- keine eigene sichtbare Modul-ID im Konstruktor; es ist Clientkleber fuer `AgpmEventQuest`.

`FUN_006de560` bindet:

- [`AgpmCharacter`](../Module/AgpmCharacter.md)
- `AgpmEventQuest`
- `AgcmCharacter`
- `AgcmEventManager`
- [`AgcmObject`](../Module/AgcmObject.md)

und registriert:

```text
FUN_006e0860(0x1b, LAB_006de420, AgcmEventQuest)
FUN_006dd1e0(LAB_006de4e0, AgcmEventQuest)
```

Interpretation:

- Eventfunktion `0x1b` ist der Client-Einstieg fuer Quest-Events.
- Questdialog/Questannahme wird ueber das generische Eventsystem angestossen und dann ueber `AgpmQuest` oder `AgpmEventQuest` bestaetigt.

## QuestJournal und UI

`AgcmQuestJournal` wird als eigenes Clientmodul gebaut. Es bindet `AgpmQuest` und `AgcmQuest`.

UI-/Eventnamen:

```text
QuestStart_Message
QuestInventoryMainFull_Message
QuestInventoryQuestFull_Message
QuestComplete_Message
QuestFull_Message
QuestStart_Sound
QuestFail_Sound
QuestCount
Quest_AutoStart
Quest_AutoEnd
QuestCount_UserData2
QuestCount_Display2
```

Config-/Datendatei-Funde:

```text
ini\\Quest_Aid_Data.txt
Quest_TransItemTid
Quest_TransItemName
Quest_TransItemCount
Gift_NextQuest_TID
Gift_NextQuest_Name
```

Interpretation:

- Quests koennen Transferitems verlangen/geben.
- Questabschluss kann Folgequest-ID und Folgequestname enthalten.
- AutoStart/AutoEnd sind explizit im Client vorhanden.

## Vermuteter Ablauf

### Quest-NPC anklicken

1. Spieler interagiert mit NPC/Eventobjekt.
2. `ApmEventManager` liefert Eventfunktion `0x1b` oder Quest-nahen Eventeintrag.
3. `AgcmEventQuest` prueft lokalen Character und Eventobjekt.
4. Client zeigt Questdialog/Journal oder sendet direkt einen `AgpmEventQuest`-/`AgpmQuest`-Request.

### Quest annehmen

1. UI/Questdialog ruft `AgcmQuest`-Wrapper.
2. `AgpmQuest` sendet Modul `0x13`, wahrscheinlich Subop `2` fuer Annahme/Start.
3. Eventdaten werden als Nested-Paket beigelegt.
4. Server prueft Requirements, Questlimit und Inventarplatz.
5. Client zeigt `QuestStart_Message` und ggf. `QuestStart_Sound`.

### Questfortschritt

1. Server aktualisiert Questflags und Counter.
2. Client setzt Bitflags ueber `AgpdQuestFlag`.
3. QuestCount-/Journal-UI wird aktualisiert.
4. Bei Zielerfuellung wird Quest als abgabebereit markiert.

### Questabschluss

1. UI/Questdialog sendet Abschlussaktion, wahrscheinlich ueber Subop `0x0b` oder `0x0e`.
2. Server prueft Ziele, Items, Inventarplatz und Rewards.
3. Transferitems werden entnommen/gegeben.
4. Server setzt Queststatus abgeschlossen und ggf. Folgequest.
5. Client zeigt `QuestComplete_Message` oder Inventar-/QuestFull-Fehler.

## Server-Datenbank-Inferenz

### Questdefinitionen

`quests`

- `quest_id`
- `name_key`
- `level_min`
- `level_max`
- `repeat_type`
- `category`
- `start_event_id`
- `end_event_id`
- `auto_start`
- `auto_end`
- `next_quest_id`

`quest_objectives`

- `quest_id`
- `objective_index`
- `objective_type`: kill, collect, talk, visit, use_item, escort, timed
- `target_id`
- `required_count`
- `area_condition_id`

`quest_rewards`

- `quest_id`
- `reward_type`: item, money, exp, skill, faction, charisma
- `item_template_id`
- `count`
- `value`
- `choice_group`

`quest_required_items`

- `quest_id`
- `item_template_id`
- `count`
- `consume_on_complete`

### Characterzustand

`character_quests`

- `character_id`
- `quest_id`
- `state`: unavailable, available, active, complete_ready, completed, failed
- `started_at`
- `completed_at`
- `repeat_reset_at`

`character_quest_objectives`

- `character_id`
- `quest_id`
- `objective_index`
- `current_count`
- `completed`

`character_quest_flags`

- `character_id`
- `flag_index`
- `flag_value`
- alternativ kompakte Blobspalten fuer die drei `0x100`-Byte-Bloecke

`quest_transaction_log`

- `character_id`
- `quest_id`
- `action`: start, progress, complete, fail, abandon
- `server_time`
- `payload`

## Sicherheitsrelevante Punkte

- Quest-Subops duerfen nicht ohne serverseitigen Zustand akzeptiert werden.
- EventID und QuestID muessen zum NPC/Eventobjekt und zur Position des Characters passen.
- AutoStart/AutoEnd duerfen serverseitig nur ausgelöst werden, wenn Requirements wirklich erfuellt sind.
- Transferitems muessen atomar entfernt/gegeben werden.
- Rewards muessen gegen Inventarplatz, Stacklimits und Queststatus validiert werden.
- Questflags sollten nur vom Server gesetzt werden; Clientflags sind Anzeige-/Syncdaten.

## Noch offene Detailarbeit

- Die exakten Bedeutungen der Quest-Subops `0`, `2`, `6`, `0x0b`, `0x0e` brauchen eine Label-/UI-Controlflow-Aufloesung.
- Der Server-Receive-Switch fuer `AgpmQuest` sollte noch tiefer anhand der `FUN_004e9fb0(param_1 + 0x344, ...)`-Aufrufer gemappt werden.
- `AgcmQuestJournal` sollte separat untersucht werden, um sichtbare Questlisten, Sortierung und Statusfarben mit Serverfeldern zu verbinden.
