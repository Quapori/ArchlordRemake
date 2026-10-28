# AgcmUIGuideMessage (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIGuideMessage` (Hilfe-Fenster: Stufenhinweise und Objekt-Hinweise) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIGuideMessage/AgcmUIGuideMessage.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 29 von 35 Quellmethoden sind zugeordnet; neu sind `LoadFile`, `CloseUI`, `CheckObjectRange`, `GetSelfCharacterLevel`, `NextMessage`, `PrevMessage`, `UpdateMessage`; `AddEvents` steht als zusammengefalteter Rumpf.
- **Objekt-Hinweis:** Ereignisnummer 0x28, Abstandsgrenze 1600.
- **Nicht im Binary:** `ShowLevelUpGuideUI`, `CallBack_Hide` und `HideGuideButton` haben im Binary keine Aufrufer; in der Quelle ist der einzige Aufruf von `ShowLevelUpGuideUI` auskommentiert. Sie sind vermutlich entfernt.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIGuideMessage.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `LoadFile` | `0x00678130` | 650 | ver |
| 1 | `LoadLevelUpGuideMessage` | `0x0067A3B0` | 853 | Zeichenkette |
| 2 | `LoadObjectGuideMessage` | `0x00678F30` | 966 | Zeichenkette |
| 3 | `GetRace` | `0x00677B90` | 113 | Zeichenkette |
| 4 | `GetClass` | `0x00677C10` | 113 | Zeichenkette |
| 5 | `OnInit` | `0x0067A710` | 26 | vtable/String |
| 6 | `OnAddModule` | `0x0067AAD0` | 245 | vtable/String |
| 7 | `InitMessage` | `0x0067A730` | 470 | Zeichenkette |
| 8 | `UpdateMessage` | `0x0067A910` | 363 | ver |
| 9 | `SelectMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `PrevMessage` | `0x00678680` | 98 | ver |
| 11 | `NextMessage` | `0x006786F0` | 90 | ver |
| 12 | `OpenLevelUpGuideUI` | `0x00677F40` | 225 | Zeichenkette |
| 13 | `OpenObjectGuideUI` | `0x00678B60` | 250 | Zeichenkette |
| 14 | `ShowLevelUpGuideUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `CloseUI` | `0x00677C90` | 47 | ver |
| 16 | `CallBack_Hide` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `GetSelfCharacterLevel` | `0x00677CC0` | 96 | ver |
| 18 | `GetSelfRace` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `GetSelfClass` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `CallBack_SelectCharacter` | `0x0067AA80` | 22 | Callback-Registrierung |
| 21 | `CallBack_CharacterLevelup` | `0x0067AAA0` | 48 | Callback-Registrierung |
| 22 | `CallBack_CharacterMove` | `0x00678030` | 73 | Callback-Registrierung |
| 23 | `CallBack_Close` | `0x00677D20` | 59 | UI-Registrierung |
| 24 | `CallBack_NextMsg` | `0x00678750` | 31 | UI-Registrierung |
| 25 | `CallBack_PrevMsg` | `0x00678770` | 31 | UI-Registrierung |
| 26 | `CallBack_Open` | `0x00678080` | 75 | UI-Registrierung |
| 27 | `CallBack_RequestObjectGuide` | `0x00678C60` | 57 | Callback-Registrierung |
| 28 | `CheckObjectRange` | `0x00677D60` | 187 | ver |
| 29 | `AddFunctions` | `0x00678790` | 167 | Zeichenkette |
| 30 | `AddEvents` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 31 | `AddUserDatas` | `0x00677E20` | 44 | Zeichenkette |
| 32 | `AddDisplay` | `0x00678CA0` | 33 | Zeichenkette |
| 33 | `CBDisplayGuideMainText` | `0x00678840` | 136 | UI-Registrierung |
| 34 | `HideGuideButton` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

29 von 35 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0067a070` (`0x0067A070`), `ctor_or_dtor_0067a260` (`0x0067A260`), `~AgcmUIGuideMessage` (`0x0067A390`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBC8` | `Baum der geschlossenen Nachrichten (`closedMessages_`)` | `NextMessage`, `PrevMessage` |
| `0xC08` | `gewählte Nachricht (`selMsg_`)` | `NextMessage`, `PrevMessage` |
| `0xC10` | `gewähltes Objekt (`selObject_`)` | `CloseUI`, `CheckObjectRange` |
| `0xBE4` | `Zeiger auf `AgcmCharacter`` | `CheckObjectRange`, `GetSelfCharacterLevel` |

## Vtable

Vtable bei `0x008CA87C`: Slot 0 Destruktor `0x0067A390`, 1 `OnAddModule` (`0x0067AAD0`), 2 `OnInit` (`0x0067A710`, lädt beide Nachrichtendateien), 6 und 7 der `return TRUE`-Rumpf `0x0067AC90` (u. a. `AddEvents`, `OnDestroy`).

## Registrierungen in OnAddModule (0x0067AAD0)

Module `AgcmCharacter`, [`AgpmCharacter`](AgpmCharacter.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmFactors`](AgpmFactors.md), [`AgcmEventManager`](AgcmEventManager.md). Callbacks: Self-Character gesetzt (`CallBack_SelectCharacter` → `InitMessage`), Level-Änderung (`CallBack_CharacterLevelup` → `UpdateMessage`), Positionsänderung (`CallBack_CharacterMove`) und das NPC-Ereignis mit der Funktionsnummer **0x28** (`APDEVENT_FUNCTION_GUIDE`, `CallBack_RequestObjectGuide`). Danach `AddFunctions` (`Open_GuideMessage`, `Close_GuideMessage`, `NextGuideMessage`, `PrevGuideMessage`), `AddDisplay` und `AddUserDatas`. Reihenfolge wie in der Quelle.

## Nachrichtendateien

`LoadLevelUpGuideMessage` (`0x0067A3B0`) liest `ini/LevelUpGuideMessage.txt` (je Rasse und Klasse über `GetRace`/`GetClass`), `LoadObjectGuideMessage` (`0x00678F30`) liest `ini/ObjectGuideMessage.txt`. Beide benutzen `LoadFile` (`0x00678130`, 650 Byte; optional verschlüsselt).

## Abstand zum Objekt

`CheckObjectRange` (`0x00677D60`) vergleicht den Abstand zwischen Self-Character und angewähltem Objekt mit **1600.0** (Konstante bei `0x008C3E78`, gelesen) und schließt das Fenster über `CloseUI` (`0x00677C90`), wenn der Abstand zu groß wird (`CallBack_CharacterMove`). Der Wert entspricht `_guide_max_use_length` der Quelle.

## Blättern

`NextMessage` (`0x006786F0`) und `PrevMessage` (`0x00678680`) bewegen die Auswahl in der Nachrichtenmenge und aktualisieren den Benutzerdatensatz; beide Callbacks tun nichts, solange ein Objekt gewählt ist (`selObject_`).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00678790`, `0x00678CA0`, `0x00677E20`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (4)

| Name | Id | Handler |
|---|---:|---|
| `Open_GuideMessage` |  | `CallBack_Open` |
| `Close_GuideMessage` |  | `CallBack_Close` |
| `NextGuideMessage` |  | `CallBack_NextMsg` |
| `PrevGuideMessage` |  | `CallBack_PrevMsg` |

**Anzeige** (1)

| Name | Id | Handler |
|---|---:|---|
| `GuideMessage_Display` | 0 | `CBDisplayGuideMainText` |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `GuideMessage_Data` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `SelectMessage` (Rumpf in der Quelle auskommentiert), `GetSelfRace`, `GetSelfClass` und `UpdateMessage`-Hilfen sind im Binary eingebaut oder nicht als eigene Funktionen zu finden.
- `UpdateMessage`, `LoadLevelUpGuideMessage` und `LoadObjectGuideMessage` wurden nur nach Aufrufern und Aufgerufenen zugeordnet, nicht Zeile für Zeile verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, nicht im Client: 2, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md)
