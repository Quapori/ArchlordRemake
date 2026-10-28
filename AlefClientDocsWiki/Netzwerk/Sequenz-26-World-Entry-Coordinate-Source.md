# Sequenz 26: Herkunft der Weltbeitritt-Koordinaten

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ergebnis

Die Koordinaten fuer die erste Platzierung des Characters kommen primaer aus dem persistenten Character-Datensatz, nicht aus dem Client und nicht aus dem Login-Op-8-Handoff.

```text
Character-Detaildatensatz: Position = "x,y,z"
  -> AgsmCharacter::DecodingPosition
  -> AgpdCharacter::m_stPos (float x/y/z)
  -> Gameserver Op 8 CHARACTER_POSITION(CID, m_stPos)
  -> Client AgcmMap::LoadTargetPosition(x, z)
```

Der Client uebernimmt diese Position nur zum Laden der passenden Mapsektoren. Er darf die Startposition nicht bestimmen; der Gameserver bleibt autoritativ.

## Persistente Quelle

Die Referenzfunktion `AgsmCharacter::GetDetailSelectResult5` liest im Character-Detailresultat die Spalte an Ergebnisindex 7 als Positionsstring. Wenn das Feld nicht leer ist, wird es mit `DecodingPosition` in `AgpdCharacter::m_stPos` uebernommen.

| Persistierter Wert | Laufzeitwert |
|---|---|
| `Position = "12345,678,90123"` | `m_stPos = { 12345.0f, 678.0f, 90123.0f }` |

Die Referenz speichert beim Detail-Update wieder genau dieses Format. `EncodingPosition` schneidet die float-Komponenten dabei auf `INT32` ab und formatiert `"%ld,%ld,%ld"`. Fuer die persistente Character-Tabelle ist die Position deshalb ein Stringfeld mit drei dezimalen Ganzzahlen, nicht drei Float-Spalten.

Beim normalen Logout bzw. Character-Detail-Update ist die Parametrierung belegt als:

```text
CharacterName, SkillInit, Position, CriminalStatus, MurdererPoint, ...
```

`Position` gehoert damit zum Character-Detailzustand zusammen mit HP/MP/SP, EXP, Level, Skillpunkten, Quickbelt, Binding-Region sowie Hair/Face; sie ist keine reine Welt-Konfiguration.

## Fallback fuer neue Characters

Fehlt der Positionsstring oder ist er leer, ruft der Referenzserver `AgpmEventBinding::GetBindingPositionForNewCharacter` auf.

1. Er sucht den ersten Binding-Eintrag vom Typ `AGPDBINDING_TYPE_NEW_CHARACTER`.
2. Die Auswahl erfolgt effektiv nach Rasse. Die fruehere Klassenpruefung ist im Referenzcode auskommentiert.
3. Der Binding-Eintrag liefert `BasePos`, `Radius`, Town und Character-Type-Factors.
4. `ApmEventManager::GetRandomPos(BasePos, radius, blocking=true)` erzeugt eine freie Zufallsposition innerhalb des Radius. Schlaegt das fehl, wird exakt `BasePos` verwendet.

Die Binding-Events sind Teil der Welt/Eventdaten, aber die Werte haben zwei getrennte Quellen:

| Binding-Wert | Konkrete Herkunft |
|---|---|
| Basisposition `BasePos` | Weltposition des Objekts, an das der Binding-Event angehaengt ist. Beim Laden ruft `CBStreamReadEvent` `ApmEventManager::GetBasePos(event->source)` auf. Fuer ein Weltobjekt ist dies direkt dessen `m_stPosition`. |
| Radius | serialisierter Binding-Event-Wert `Radius` |
| Binding-Type | serialisierter Binding-Event-Wert `BindingType`; `2` bedeutet `NEW_CHARACTER` |
| Rasse/Klasse | serialisierte `CharRaceType`/`CharClassType`-Factors; die aktive Auswahl prueft derzeit nur die Rasse |
| Town/Name | serialisierte `TownName`/`BindingName`-Werte |

Die Quelle ist somit weder eine Server-Datenbank noch ein an den Client gesendetes Spawnpaket: Es ist ein in der Welt platzierter Event-Anker mit Binding-Eventdaten. Fuer einen eigenen Gameserver reicht als belastbarer Fallback ein pro Rasse definierter Spawnpunkt; fuer das Originalverhalten wird zusaetzlich ein freier Punkt im Radius gesucht.

## Was in Op 8 landet

`AgsmCharManager::SendCharacterLoadingPosition` baut `CHARACTER_POSITION` direkt mit:

| Feld | Quelle |
|---|---|
| Operation | `CHARACTER_POSITION` / Op 8 |
| CID | `pcsCharacter->m_lID` |
| Position | `pcsCharacter->m_stPos` |

Damit ist die genaue, fuer den Client relevante Koordinate die aktuelle Laufzeitposition des auf dem Gameserver vorbereiteten Characters.

## Nachtraegliche Korrektur beim World-Entry

Nach dem clientseitigen `LOADING_COMPLETE` validiert der Referenzserver die Position erneut in `AgsmCharManager::EnterGameWorld`:

1. Sind `x == 0` und `z == 0`, wird der New-Character-Binding-Spawn verwendet.
2. Sonst werden moduleigene Login-Positionsregeln aufgerufen.
3. `AgsmCharacter::CheckLoginPosition` ersetzt die Position bei einer Regions-Resurrection-Position, Level-Restriktionen, gesperrten Login-Regionen, Event-Battlegrounds oder geschlossenen Shrine-Battle-Areas durch Resurrection- oder New-Character-Bindings.
4. Danach wird die Region aus der korrigierten Position aktualisiert und der SelfCharacter-Add gesendet.

## Wichtige Reihenfolge-Falle

Im Referenzcode wird Op 8 bereits beim Op-2-Connect gesendet. Die umfassende Login-Positionskorrektur geschieht dagegen erst nach Op 9 in `EnterGameWorld`.

Das bedeutet: Ein gesperrter oder inkonsistenter gespeicherter Ort kann dazu fuehren, dass der Client zuerst Mapsektoren um die alte Position laedt, waehrend der Server den Character anschliessend auf einen Binding-/Resurrection-Punkt korrigiert. Ein eigener Gameserver sollte das nicht nachbilden:

1. Persistierte Position laden.
2. Vor Op 8 gegen die aktive Welt, erreichbare Mapsektoren und Spawn-/Binding-Regeln validieren bzw. korrigieren.
3. Die bereits kanonisierte Position sowohl in Op 8 als auch im Self-[`AgpmCharacter`](../Module/AgpmCharacter.md)-Add verwenden.

Damit sind Client-Mapload, sichtbarer Character und serverseitige AOI-Zelle konsistent.

## Mindestdaten fuer den lokalen Gameserver

| Datenquelle | Benoetigte Werte |
|---|---|
| Character-Persistenz | `cid`, Welt/Server, `position_x/y/z` oder kompatibler `"x,y,z"`-Wert |
| Spawn-Fallback | Welt-ID, Rasse, Basisposition, optional Radius |
| Map-Validierung | gueltige Weltgrenzen, Region/Sektor und gesperrte Regionen |
| Handoff-Laufzeit | CID, Zielwelt und die kanonisierte Startposition |

Die bestehende Loginserver-Datenhaltung muss dafuer nur gelesen werden; die konkrete Implementierung wird hier bewusst nicht veraendert.

## Quellen

- Referenz-Gameserver: `Modules/AServer/AgsmCharacter/AgsmCharacter.cpp`, `GetDetailSelectResult5`, `EncodingPosition`, `DecodingPosition`, `CheckLoginPosition`.
- Referenz-Gameserver: `Modules/AServer/AgsmCharManager/AgsmCharManager.cpp`, `SendCharacterLoadingPosition`, `EnterGameWorld`, Character-Erstellung.
- Gemeinsames Modul: `Modules/APublic/AgpmEventBinding/AgpmEventBinding.cpp`, `GetBindingForNewCharacter`, `GetBindingPositionForNewCharacter`.
- Gemeinsame Event-Infrastruktur: `Modules/APublic/AgpmEventBinding/AgpmEventBindingStream.cpp` und `Modules/APublic/ApmEventManager/ApmEventManager.cpp`, Binding-Stream und Aufloesung der Weltposition des Event-Quellobjekts.
- Folge: [`WINSOCK_SEQUENCE_24_GAMESERVER_BOOTSTRAP_WORLD_ENTRY.md`](Sequenz-24-Gameserver-Bootstrap-World-Entry.md) und [`WINSOCK_SEQUENCE_25_FIRST_WORLD_ENTRY_REQUIRED_STATE.md`](Sequenz-25-First-World-Entry-Required-State.md).
