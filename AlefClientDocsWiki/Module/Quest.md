# AgpmQuest und AgpmEventQuest (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, EP8-Quelle (`Modules/APublic/AgpmQuest`, `…/AgpmEventQuest`) und die 2013er Berichte (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Protokoll unverändert (2017 = EP8 = 2013):** `AgpmQuest` (Typ `0x13`): `m_csPacket` 11 Felder (Flag-Länge 2) und `m_csPacketQuest` 6 Felder (Flag-Länge 1). `AgpmEventQuest` (Typ `0x3E`): `m_csPacket` 4 Felder und `m_csPacketEventData` 1 Feld. Alle Typen, Anzahlen und Flag-Längen stimmen überein.
- **Der 2013er Bericht ließ `AgpmQuest` offen** (Vergleichsbaum mit Bereichssprüngen, nur Op 4 und 5 aufgeführt). Hier ist der Dispatch aufgelöst: `OnReceive` (`0x00559030`) behandelt Op 4 (`INIT_QUEST`) und Op 5 (`INIT_FLAGS`) selbst; **alle übrigen Operationen lösen `EnumCallback(Operation, &CBQuestParam)` aus, die Callback-ID ist also die Operationsnummer** (wie in der Quelle). Die Ereignisse sind daher die Callbacks, die andere Module für diese Operationen registrieren.
- **Client-Abonnenten im 2017er Binary** (aus der Registrierungsreihenfolge gegen die Quelle zugeordnet): [`AgcmUIQuest2`](AgcmUIQuest2.md):CBRequireQuestResult` (`0x006B5890`, Op 1), `CBCompleteQuestResult` (`0x006B5910`, Op 3), `CBCancelQuestResult` (`0x006B5940`, Op 7), `CBInventoryFull` (`0x006B23D0`, Op 8), `CBQuestInventoryFull` (`0x006B2440`, Op 9), `CBUpdateQuest` (`0x006B3E80`, Op 10) und `AgcmUIQuestJournal::CBRefreshJournalInfo` (`0x0067B590`, Op 10), dazu `AgcmQuestJournal::CBInitQuest` (`0x006130B0`, ID 16). Ein Server muss diese Operationen senden, damit die Quest-UI reagiert.
- **Zwei Quest-Schalter müssen an sein**, sonst verwirft der Client jedes Quest-Paket und löst `DISABLE_FORAWHILE` (ID 13) aus: der Wert in [`AgpmConfig`](AgpmConfig.md) (über `IsEnableQuest`, `0x00589B60`) und der eigene Schalter von `AgpmQuest` bei `+0xD0C`. Der Konstruktor setzt `+0xD0C` auf 1; die Quelle hat für beide den Standard `TRUE`.
- **Adressen verschoben:** `AgpmQuest::OnReceive` `0x00559030` (2013: `0x00559790`), `AgpmEventQuest::OnReceive` `0x0056F3A0` (2013: `0x0056F9E0`).

## AgpmQuest (Paket-Typ `0x13`)

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00537B60` | `AgpmQuest::StreamReadTemplate` | strmatch |
| `0x00558960` | `AgpmQuest::ctor_or_dtor_00558960` | merged |
| `0x00558B00` | `AgpmQuest::ctor_or_dtor_00558b00` | merged |
| `0x00558BA0` | `AgpmQuest::OnInit` | merged |
| `0x00558C10` | `AgpmQuest::GetAttachAgpdQuestData` | dispatch-struktur |
| `0x00558F80` | `AgpmQuest::~AgpmQuest` | merged |
| `0x00558FA0` | `AgpmQuest::AgpdQuestConstructor` | stage1 |
| `0x00559030` | `AgpmQuest::OnReceive` | merged |
| `0x00559550` | `AgpmQuest::OnDestroy` | merged |
| `0x00559670` | `AgpmQuest::AgpdQuestDestructor` | stage1 |
| `0x005596C0` | `AgpmQuest::OnAddModule` | merged |
| `0x00589B60` | `AgpmConfig::IsEnableQuest` | dispatch-struktur |

`OnReceive` ist vtable-Slot 9 (`0x559030`); der Konstruktor liegt bei `0x00558960`, `m_csPacket` bei `+0xD10`.

### Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 11/11/11 | ja | ja |
| `m_csPacketQuest` | 1/1/1 | 6/6/6 | ja | ja |

**m_csPacket** (11 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT32 | 1 | Character ID |
| 2 | `0x4` | PACKET | 1 | Äù½ºÆ®¸¦ ¹ß»ý½ÃÅ² ApdEvent ÆÐÅ¶ |
| 3 | `0x8` | PACKET | 1 | ÆÐÅ¶ »ó¼¼ µ¥ÀÌÅÍ |
| 4 | `0x10` | INT32 | 1 | Quest ID |
| 5 | `0x20` | INT32 | 1 | Check Point Index |
| 6 | `0x40` | INT32 | 1 | Result |
| 7 | `0x80` | INT32 | 1 | SelectItem Index |
| 8 | `0x100` | MEMORY_BLOCK | 1 | Flag Memory1 |
| 9 | `0x200` | MEMORY_BLOCK | 1 | Flag Memory2 |
| 10 | `0x400` | MEMORY_BLOCK | 1 | Flag Memory3 |

**m_csPacketQuest** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Quest ID |
| 1 | `0x2` | INT32 | 1 | Param 1 |
| 2 | `0x4` | INT32 | 1 | Param 2 |
| 3 | `0x8` | INT32 | 1 | Item TID |
| 4 | `0x10` | INT32 | 1 | bRegisterJournal |
| 5 | `0x20` | CHAR | AGPACHARACTER_MAX_ID_STRING + 1 |  |

### Ablauf von `OnReceive` (2017 = Quelle)

1. 14 Felder per `GetField` lesen (die drei Memory-Blöcke liefern je Zeiger und Länge): Operation, CID, Event-Basispaket, Quest-Teilpaket, Quest-TID, Checkpoint-Index, Ergebnis, Auswahl-Item-Index, Puffer 1–3.
2. Operation `> 14` → `return 0` (`AGPMQUEST_PACKET_OPERATION_MAX` = 15).
3. Event-Basispaket vorhanden → `GetEventFromBasePacket` (`0x55D900`); `NULL` → `return 0`.
4. Ist Quest per `AgpmConfig` oder per eigenem Schalter (`+0xD0C`) aus: Zeichen per CID holen und `EnumCallback(13 = DISABLE_FORAWHILE)`; `return 0`.
5. Zeichen sperren (`GetCharacterLock`); bei Client-Paketen und `AllBlock` abbrechen.
6. Parameterstruktur `CBQuestParam` füllen (Zeichen, Event, TID, Checkpoint, Ergebnis, Auswahl, Teilpaket, Puffer 1–3 mit Längen).
7. Op 4: eingebettetes Quest-Paket lesen (`FUN_00590E20`), `GetAttachAgpdQuestData` (`0x558C10`), neue Quest eintragen (`FUN_00590B60`), `EnumCallback(16 = INIT_QUEST, QuestID, RegisterJournal)`. Op 5: die Flag-Puffer 1–3 in die Flag-Verwaltung des Zeichens kopieren (`FUN_00590C10`, Index 0/1/2). Sonst `EnumCallback(Operation, &Param)`.

### Opcodes

| Op | Name (`AGPMQUEST_PACKET_OPERATION_…`) | Behandlung 2017 | Abonnent im Client |
|---:|---|---|---|
| 0 | REQUIRE_QUEST | Callback 0 | – |
| 1 | REQUIRE_QUEST_RESULT | Callback 1 | `AgcmUIQuest2::CBRequireQuestResult` |
| 2 | QUEST_COMPLETE | Callback 2 | – |
| 3 | QUEST_COMPLETE_RESULT | Callback 3 | `AgcmUIQuest2::CBCompleteQuestResult` |
| 4 | INIT_QUEST | direkt: Quest anlegen, Callback 16 | `AgcmQuestJournal::CBInitQuest` |
| 5 | INIT_FLAGS | direkt: Flag-Puffer kopieren | – |
| 6 | CANCEL | Callback 6 | – |
| 7 | CANCEL_RESULT | Callback 7 | `AgcmUIQuest2::CBCancelQuestResult` |
| 8 | INVENTORY_FULL | Callback 8 | `AgcmUIQuest2::CBInventoryFull` |
| 9 | QUEST_INVENTORY_FULL | Callback 9 | `AgcmUIQuest2::CBQuestInventoryFull` |
| 10 | UPDATE_QUEST | Callback 10 | `AgcmUIQuest2::CBUpdateQuest`, `AgcmUIQuestJournal::CBRefreshJournalInfo` |
| 11 | CHECKPOINT | Callback 11 | – |
| 12 | CHECKPOINT_RESULT | Callback 12 | – |
| 13 | DISABLE_FORAWHILE | intern bei deaktivierter Quest gefeuert; als Paket-Operation fiele sie in den Default-Zweig (Callback 13) | – |
| 14 | QUEST_REGISTER_JOURNAL_CHANGE | Callback 14 | – |

Die Spalte „Abonnent“ nennt nur die im 2017er Binary gefundenen Registrierungen der Client-Module; Server-Module (die Ops 0, 2, 6, 11, 12 verarbeiten) liegen nicht im Client. Vergleich mit 2013: dort waren nur Op 4/5 aufgeführt (ohne Binary-Ereignisse); Verhalten und IDs stimmen mit der Quelle überein.

## AgpmEventQuest (Paket-Typ `0x3E`)

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0056ED20` | `AgpmEventQuest::ctor_or_dtor_0056ed20` | merged |
| `0x0056EE20` | `AgpmEventQuest::ctor_or_dtor_0056ee20` | merged |
| `0x0056EE90` | `AgpmEventQuest::OnOperationRequest` | dispatch-struktur |
| `0x0056F030` | `AgpmEventQuest::CBActionQuest` | stage1 |
| `0x0056F0B0` | `AgpmEventQuest::CBStreamWriteEvent` | stage1 |
| `0x0056F110` | `AgpmEventQuest::CBStreamReadEvent` | stage1 |
| `0x0056F270` | `AgpmEventQuest::CBEmbeddedMakeEventPacket` | stage1 |
| `0x0056F2A0` | `AgpmEventQuest::CBEmbeddedReceiveEventPacket` | stage1 |
| `0x0056F2D0` | `AgpmEventQuest::~AgpmEventQuest` | merged |
| `0x0056F2F0` | `AgpmEventQuest::OnAddModule` | merged |
| `0x0056F3A0` | `AgpmEventQuest::OnReceive` | merged |
| `0x0056FD60` | `AgpmEventQuest::OnOperationGrant` | dispatch-struktur |

### Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 4/4/4 | ja | ja |
| `m_csPacketEventData` | 1/1/1 | 1/1/1 | ja | ja |

**m_csPacket** (4 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | PACKET | 1 | Event Base Packet |
| 2 | `0x4` | INT32 | 1 | CID |
| 3 | `0x8` | INT32 | 1 | Object Range |

**m_csPacketEventData** (1 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Quest Group ID |

### Opcodes

`OnReceive` (`0x0056F3A0`) liest 4 Felder (`m_csPacket` bei `+0xB90`), holt das Event (`event.type == 0x1B`, `APDEVENT_FUNCTION_QUEST`), das Zeichen (`GetCharacterLock`), prüft bei Client-Paketen `AllBlock` und dispatcht per Vergleich:

| Op | Name | 2017-Handler | Verhalten | Ereignis (ID) | Vergleich 2013 |
|---:|---|---|---|---|---|
| 0 | `AGPMEVENT_QUEST_PACKET_REQUEST` | `0x56EE90` `OnOperationRequest` | Reichweite `lRange` auf 1…1600 begrenzen (`≤ 0` oder `> 1599` → 1600); in Reichweite: NextAction löschen, ggf. `StopCharacter`, Ereignis; sonst NextAction = `EVENT_QUEST` (15) setzen und zum Objekt/Event laufen | `CB_REQUEST` (0) | = |
| 1 | `AGPMEVENT_QUEST_PACKET_GRANT` | `0x56FD60` `OnOperationGrant` | nur Callback | `CB_GRANT` (1) | = |

Die Konstante `AGPMEVENT_QUEST_MAX_USE_RANGE` = 1600 stimmt mit der Quelle überein.

## Grenzen

- Die Callback-Abonnenten stammen aus der Zuordnung der Registrierungsaufrufe gegen die Quelle (Sequenzabgleich); die Zuordnung zu den Operationsnummern folgt der Quelle, die registrierenden `SetCallback…`-Funktionen sind im Binary durch Linker-Faltung nicht eindeutig benannt.
- Die Quest-Datenstrukturen (`AgpdQuest`, Flag-Verwaltung `AgpdQuestFlag`, `AgpaQuestTemplate`) und die Stream-Dateien (`QuestTemplate`) wurden nicht untersucht, ebenso nicht die Server-Seite der Operationen 0, 2, 6, 11, 12.
- Die Bereichsprüfung `CheckValidRange` (`FUN_0055C380`) und die Folge-Bewegung wurden nur an der Struktur verglichen.

## Querverweise

- **Erwähnt Module:** [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgpmConfig`](AgpmConfig.md)
