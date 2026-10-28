# Neue Character-Spawnpunkte aus den Clientdaten

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Welt, Engine und Rendering](Index.md)*

Stand: 2026-09-09

## Ergebnis

Die benoetigten `NEW_CHARACTER`-Binding-Daten sind im installierten Client vorhanden. Sie liegen als Klartext in den sektorbezogenen Objektdateien unter `C:\Spiele\Archlord\ini\objNNNNN.ini`; sie sind weder in einer Serverdatenbank noch in den verschluesselten `Data.Dat`-Containern verborgen.

Eine vollstaendige Suche ueber alle `*.ini` in diesem Verzeichnis ergab genau vier Eintraege mit `BindingType=2` (`AGPDBINDING_TYPE_NEW_CHARACTER`), je einen fuer die Rassenwerte 1 bis 4.

## Extrahierte Spawnanker

| Rassewert | Rasse | Position `x, y, z` | Radius | Quelldatei | Objektabschnitt | Objekt-TID | Class-Wert |
|---:|---|---|---:|---|---:|---:|---:|
| 1 | Human | `-476200.000000, 4622.807617, -71800.000000` | 800 | `obj02024.ini` | `132646585` | 782 | 1 |
| 2 | Orc | `134600.000000, 9348.077148, 525800.000000` | 800 | `obj02630.ini` | `172360028` | 782 | 2 |
| 3 | MoonElf | `516200.000000, 19082.449219, 29200.000000` | 1000 | `obj03025.ini` | `198246809` | 782 | 1 |
| 4 | DragonScion | `-594420.187500, 22971.833984, 329053.531250` | 0 | `obj01928.ini` | `126354973` | 467 | 4 |

Die Zuordnung 1..4 zu Human, Orc, MoonElf und DragonScion folgt den belegten `AURACE_TYPE_*`-Verwendungen im Referenzcode und der bereits dokumentierten Charaktererstellungs-Tabelle.

## Dateiformat und Bindung an die Position

Jeder Eintrag ist ein Objektabschnitt wie dieser reale Human-Spawnanker:

```ini
[132646585]
ModuleData1=ApmObject
TID=782
Position=-476200.000000,4622.807617,-71800.000000
...
ModuleData5=ApmEventManager
Function=19
EventID=1073745403
BindingName=...
TownName=...
Radius=800
BindingType=2
CharRaceType=1
CharClassType=1
BindingEnd=0
```

Damit ist der Zusammenhang technisch vollstaendig:

```text
Objektabschnitt.Position
  + ApmEventManager / BindingType=2
  + CharRaceType
  + Radius
  -> NEW_CHARACTER-Spawnanker
```

Der Binding-Loader uebernimmt die Objektposition als `BasePos`. Der originale Spawnalgorithmus sucht ab dieser Basis einen begehbaren, nicht blockierten Zufallspunkt innerhalb des Radius. Bei Radius 0 oder fehlender freier Position wird die Basisposition direkt verwendet.

## Relevanz fuer den Gameserver

Ein minimaler Gameserver kann diese vier Werte direkt als serverseitige Spawnkonfiguration verwenden:

1. Bei neuem Character oder leerer persistierter Position die Rasse des Templates bestimmen.
2. Den zugehoerigen Anker aus der Tabelle waehlen.
3. Fuer den ersten funktionierenden Weltbeitritt exakt die angegebene Basisposition verwenden.
4. Dieselbe Position sowohl in `CHARACTER_POSITION` (Op 8) als auch im nach `LOADING_COMPLETE` gesendeten Self-[`AgpmCharacter`](../Module/AgpmCharacter.md)-Add verwenden.

Eine zufaellige Position im Radius erfordert zusaetzlich serverseitige Hoehen-/Kollisions- und Blocking-Pruefungen. Sie ist fuer den ersten korrekten Client-World-Entry nicht erforderlich. Der DragonScion-Anker hat ohnehin Radius 0.

## Abgrenzung der Clientdaten

- `C:\Spiele\Archlord\ini\obj*.ini`: Klartext, enthaelt Weltobjekte, Positionen und Event-Module einschliesslich Binding-Events.
- `C:\Spiele\Archlord\world\*.ma1`/`*.ma2`: MagPack-Container fuer Terrain, Renderdaten und Details; nicht die Quelle dieser vier Binding-Definitionen.
- `C:\Spiele\Archlord\world\{grass,octree,water}\Data.Dat`: gepackte Ressourcen fuer Rendering/Weltaufteilung; fuer den Character-Spawn hier nicht erforderlich.
- Sprach- und Character-Tabellen unter `ini\`: liefern Namen, Templates und UI-Daten, nicht die konkreten Weltpositionen.

## Quellen und Verifikation

- Vollstaendiger Scan aller `C:\Spiele\Archlord\ini\*.ini` auf `BindingType=2`: exakt vier Treffer.
- Rohdaten: `C:\Spiele\Archlord\ini\obj02024.ini`, `obj02630.ini`, `obj03025.ini`, `obj01928.ini`.
- Referenzcode: `AgpmEventBinding::GetBindingPositionForNewCharacter` und `AgpmEventBinding::CBStreamReadEvent`.
- Protokollfolge: [`WINSOCK_SEQUENCE_26_WORLD_ENTRY_COORDINATE_SOURCE.md`](../Netzwerk/Sequenz-26-World-Entry-Coordinate-Source.md).
