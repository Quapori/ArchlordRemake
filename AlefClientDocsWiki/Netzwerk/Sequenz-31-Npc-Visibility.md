# Winsock-Sequenz 31: NPCs in der Startstadt sichtbar machen

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-13

## Ergebnis

`alefgame-server` sendet jetzt beim Weltbeitritt (`LOADING_COMPLETE`, nach
Self-Add und Items, vor `SETTING_CHARACTER_OK` -- passend zur echten
Reihenfolge in `AgsmCharManager.cpp:1104-1118`) alle NPCs in der Naehe der
Spawnposition als normale [`AgpmCharacter`](../Module/AgpmCharacter.md)-ADD-Pakete. **Live verifiziert**:
NPCs sind sichtbar (26 fuer den Human-Spawnpunkt). Dialoge/Handel fehlen
noch -- das ist ein eigenes, separates Interaktionsprotokoll
([`ApmEventManager`](../Module/ApmEventManager.md)/`NPCDialogStart`/`NPCTradeStart`), nicht Teil dieses
Schritts.

## Datenquelle: `ini\npc.ini`, nicht `obj*.ini`

Anders als die vier Charakter-Spawnanker (`WORLD_NEW_CHARACTER_BINDINGS_
FROM_CLIENT.md`, gefunden in `obj*.ini` via `ApmEventManager`/
`BindingType=2`) liegen NPCs in einer EIGENEN, zentralen Datei:
`C:\Spiele\Archlord\ini\npc.ini`, mit derselben RC4-Verschluesselung
(Schluessel `1111`) wie `characterdatatable.txt`. Eine Suche nach
`AgpmCharacter` in allen 171 `obj*.ini`-Dateien (147.997 Objektabschnitte)
ergab null Treffer -- diese Dateien enthalten nur Terrain-Dekoration und
die vier bekannten Spawn-Bindings, keine NPCs.

`npc.ini` enthaelt 623 Abschnitte der Form:

```ini
[3]
ModuleData1=AgpmCharacter
Name=<Merchant> Darryl
TID=584
Position=-473768.187500,4622.807617,-65465.996094
Degree=0.000000,13.000000
ModuleData2=ApmEventManager
Function=21
EventID=1073741841
NPCDialogStart=0
Template=1
NPCDialogEnd=0
...
```

`Name` ist der Anzeigename der konkreten NPC-Instanz; `TID` referenziert
eine wiederverwendbare Vorlage in `characterdatatable.txt` (dort meist ein
generischer Name wie "Human NPC Abella" -- das ist normal, kein
Datenfehler). Von 623 TIDs loesen 615 (98,7%) zu `Type=2`-Zeilen
("NPC-Charaktertemplate") in `characterdatatable.txt` auf; die restlichen
8 sind `TID=2207` ("Battle Square Gate", Arena-Tor-Requisiten, keine
echten NPCs) und wurden beim Import ausgeschlossen.

## Kein Regions-/Stadt-Schluessel in den Clientdaten

`npc.ini` hat kein Feld, das eine NPC einer Region/Stadt zuordnet (alle
Feldnamen der Datei wurden durchsucht: `Name`, `TID`, `Position`, `Degree`,
`Function`, `EventID`, `NPCDialogStart/End`, `QuestGroupID`,
`NPCTradeStart/End`, `Minimap`, `SkillRaceType` u.a. -- keine Region-ID
darunter). Der reale Server gruppiert NPCs serverseitig in
`m_mapTownToNPCList` (`AgsmCharacterPacket.cpp:544-557`), aber die
Zuordnung selbst muss aus einer anderen Quelle kommen (vermutlich
`BaseCharacterInfo.xml` oder aequivalente Serverdaten, die diesem Projekt
fehlen).

**Loesung**: Gruppierung nach raeumlicher Naehe zu den vier bekannten
Spawnankern, exakt wie bereits fuer die Charakterauswahl-Vorschau (die
zehn Rassen-/Klassen-Vorlagen) etabliert. Naehe-Auszaehlung ergab:

| Rasse (Spawnanker) | NPCs im Radius 10.000 | im Radius 20.000 |
|---|---:|---:|
| Human | 23 | 26 |
| Orc | 26 | 26 |
| MoonElf | 20 | 29 |
| DragonScion | 13 | 23 |

Implementiert als reine Datenbankabfrage (`db::list_npcs_near`), zentriert
auf die tatsaechlich aufgeloeste Spawnposition des Charakters (`resolve_
spawn_position`, dieselbe Funktion, die schon `CHARACTER_POSITION` und den
Self-Add speist) mit Radius 20.000 -- **nur in der XZ-Ebene**, Hoehe (Y)
bewusst ignoriert (ein NPC auf einer Bruecke/Plattform direkt ueber dem
Spieler soll nicht wegen der Hoehendifferenz ausgeschlossen werden).

## Umsetzung

1. Neue Tabelle `npcs` (Migration `0009_npcs.sql`), befuellt mit allen 615
   gueltigen NPCs (`id`=Originale `npc.ini`-Abschnittsnummer, `name`,
   `template_tid`, `position_x/y/z`) -- extrahiert per Python-Skript aus
   den entschluesselten `npc.ini`/`characterdatatable.txt`.
2. `alefgame-server::db::list_npcs_near(pool, x, z, radius)`.
3. `build_npc_add_packet`: ein bewusst schlankeres `AgpmCharacter`-ADD als
   der Self-Add -- nur Operation, CID, TID, GameID (Anzeigename), Status
   (`IN_GAME_WORLD`) und ein stehendes Move-Paket. Kein Money/Criminal-
   Status/Factor -- fuer NPCs nicht getrackt und (wie beim eigenen
   Charakter bereits mehrfach bestaetigt) vom Client null-safe behandelt,
   wenn abwesend.
4. NPC-CIDs liegen ab `2.000.000` (`NPC_CID_BASE`), getrennt von echten
   `characters.id`-Werten und von den Rassen-Vorschau-CIDs der
   Charakterauswahl (`1.000.000 + tid`).

## Offene naechste Schritte

- Dialoge/Handel/Quests (das `ApmEventManager`-Modul, das jede `npc.ini`-
  Sektion zusaetzlich traegt) -- eigenes, groesseres Protokoll.
- NPCs ausserhalb der vier Startstaedte (die anderen ~590 von 623 sind ueber
  die ganze Spielwelt verteilt) -- braucht echte Regionswechsel-Erkennung,
  aktuell sendet dieses Projekt NPCs nur einmalig bei `LOADING_COMPLETE`.
- Andere Spieler sichtbar machen -- separates Thema, siehe naechste
  Arbeitsphase.
