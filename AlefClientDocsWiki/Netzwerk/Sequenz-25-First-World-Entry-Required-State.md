# Sequenz 25: Erster notwendiger Weltzustand nach LoadingComplete

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ergebnis

Der erste zwingende Schritt, damit ein Character die Welt betreten kann, ist nicht Kampf, Monster, Quests oder ein allgemeines Weltpaket. Es ist der abgeschlossene Positions-Handshake und danach der Wiederaufbau des eigenen Characters in der lokalen Registry:

```text
Gameserver Op 8 CHARACTER_POSITION
  -> Client: LoadTargetPosition(x, z), RemoveAllCharacters(), Op 9 LOADING_COMPLETE
  -> Gameserver: SendCharacterAllInfo(Self)
  -> Gameserver: Title-Daten und lokale Stadt-NPCs als Character-View/Add
  -> Gameserver Op 7 SETTING_CHARACTER_OK(Self CID)
  -> Server: Runtime-Entity in die Welt/AOI aufnehmen
  -> Sichtbereich, Bewegung, Kampf, Quest- und Drop-Logik
```

Das Selbst-Add muss vor Op 7 eintreffen. Der Client sucht bei Op 7 bereits `AgpmCharacter::GetCharacter(CID)` und verweigert die SelfCharacter-Bindung, wenn der Eintrag fehlt.

## Tatsaechliche Serverreihenfolge

Der Op-9-Empfang ruft im Referenzserver direkt `AgsmCharManager::EnterGameWorld(character)` auf. Bei der normalen Validierungsvariante geschieht Folgendes in dieser Reihenfolge:

1. Der Server verlangt einen vom Loginserver vollstaendig uebergebenen Character (`m_bIsRecvAllDataFromLoginSvr`) und einen gebundenen Client-Socket/NID. Fehlt eines davon, wird der Weltbeitritt verworfen.
2. Er prueft bzw. korrigiert die Spawnposition, setzt bei neuen Characters die Binding-Position und aktualisiert die Region.
3. Er richtet Game-Daten ein und sendet `AgsmCharacter::SendCharacterAllInfo(character, NID)`.
4. Er sendet Titelliste und Titelquestliste.
5. Er sendet die NPCs der Binding-Region durch `SendRegionNPCToChar`; jeder NPC wird als `SendPacketCharView` uebertragen.
6. Er sendet `AgcmCharacter` Op 7 `SETTING_CHARACTER_OK` nur mit der CID.
7. Erst dann berechnet er Faktoren neu, fuegt die Runtime-Entity mit `AgsmCharacter::EnterGameWorld` in die Welt ein und beginnt die normalen Enter-World-Callbacks.

Die Reihenfolge belegt, dass Op 7 kein Ersatz fuer den Character-Add ist und dass NPC-/AOI-Sichtbarkeit nicht vor dem Selbstcharacter aufgebaut werden darf.

## Mindestdaten des Selbstcharacters

`SendCharacterAllInfo` beginnt zwingend mit `SendPacketChar`. Das ist ein vollstaendiges [`AgpmCharacter`](../Module/AgpmCharacter.md)-Add fuer den eigenen Character, nicht nur eine CID-Bestaetigung. Die Add-Daten enthalten mindestens:

| Datenbereich | Zweck beim ersten Weltbeitritt |
|---|---|
| CID | Schluessel fuer die lokale Character-Registry und Op 7 |
| Template-TID und GameID/Name | Templateauflosung, Modell und Namensanzeige |
| Character-Status | lokaler Lifecycle und Darstellungszustand |
| Move-Paket mit aktueller Position/Ziel/Richtung | Platzierung nach dem Sektorload |
| Factor-Paket | Level, EXP, HP/MP/SP und kampfrelevante Grundwerte |
| Action-, Criminal-, Special-, Transform-, Eventstatus | sichtbarer Zustand und Folgesysteme |
| Face/Hair/Nickname | Characterdarstellung |

Der normale `CharView`-Add fuer NPCs, Monster und andere Spieler verwendet ebenfalls `AgpmCharacter` Op 0. Er umfasst CID, TID, Name, Status, Move-Paket, Factor-Paket, Action- und Sichtbarkeitsstatus. Der Referenzserver hat alternativ einen OptimizedPacket2-Pfad; die semantische Voraussetzung bleibt ein vollstaendiger lokaler Character-Eintrag.

## All-Info ist ein Modul-Burst

Nach dem Basis-Add ruft `SendCharacterAllInfo` die Callback-Kette `AGSMCHARACTER_CB_SEND_CHARACTER_ALL_INFO` auf. Sie transportiert den persistenten Playerzustand der aktivierten Servermodule. In der Referenz sind mindestens folgende Empfaenger registriert:

| Modul | Bedeutung fuer den Einstieg |
|---|---|
| `AgsmItem` | Inventar-, Ausruestungs- und Item-Zustand |
| `AgsmSkill` | gelernte Skills und skillbezogener Status |
| `AgsmQuest` | Questdaten und vorhandener Fortschritt |
| `AgsmGuild` | Gildenzugehoerigkeit/Anzeige |
| `AgsmMailBox` | Mailbox-Status |
| `AgsmAuction` | Auktionsdaten |
| `AgsmBillInfo` | Abrechnungs-/Servicezustand |
| `AgsmPvP`, `AgsmSiegeWar` | PvP- und Belagerungszustand |
| `AgsmProduct` | Produktions-/Craftingzustand |

Fuer einen minimal sichtbaren Weltbeitritt sind nicht alle optionalen Module sofort erforderlich. Das Basis-Add mit Position und Factors ist jedoch nicht optional. Inventar und Skills sollten vor dem ersten nutzerinitiierten Angriff vorhanden sein; Questdaten vor NPC-Interaktion oder Questfortschritt.

## Stadt-NPCs und AOI sind getrennt

`SendRegionNPCToChar` nimmt die Binding-Region des Spielers und iteriert die dort konfigurierte Town-to-NPC-Liste. Es sendet jedes Ergebnis einzeln via `SendPacketCharView` an den neuen Socket. Das ist eine explizite Startsichtbarkeit fuer Stadt-NPCs, nicht die allgemeine Octree-/AOI-Abfrage.

Die allgemeine Sichtbarkeit startet erst, nachdem der Server die Runtime-Entity in `AgsmCharacter::EnterGameWorld` aufgenommen hat. Dabei erhaelt der Spieler ueber AOI-Zellen die View-Adds fuer nahe Characters; umgekehrt erhalten bereits nahe Spieler einen View-Add des neu beigetretenen Characters. Monster, Bodenitems und andere dynamische Objekte gehoeren in diese anschliessende AOI-Phase.

## Minimaler testbarer Vertrag

Ein Gameserver, der nur den ersten Weltbeitritt sichtbar machen soll, muss in dieser Reihenfolge mindestens leisten:

1. Die mit Login-Op 8 uebergebene Handoff-Session an Op 2 (Name, einmaliger AuthKey, Zielwelt, Socket) binden.
2. Op 8 `CHARACTER_POSITION(CID, x, y, z)` senden und genau auf Op 9 derselben gebundenen CID warten.
3. Nach Op 9 den SelfCharacter per `AgpmCharacter`-Add mit CID, TID, Name, Status, Position und Factors anlegen.
4. Erst nach erfolgreichem Self-Add Op 7 `SETTING_CHARACTER_OK(CID)` senden.
5. Danach lokale NPCs und allgemeine AOI-Entities als Add/View senden; keine View-/Update-Pakete fuer unbekannte CIDs voraussetzen.
6. Kampf, Skills, Inventarinteraktion und Quests erst freigeben, wenn die jeweilige Initialdatenkette gesendet wurde.

## Nicht als erster Schritt erforderlich

- Monster-Spawn, Aggro, Kampf- oder Schadenspakete.
- EXP, Level-Up, Loot oder Questfortschritt.
- Vollstaendige Welt-/Octree-Konfiguration im Netzwerk, sofern der Client die lokale Map bereits aus den Datendateien laden kann.
- Senden beliebiger `Update`-Frames vor dem ersten `Add` derselben CID.

Diese Systeme folgen auf den erfolgreichen World-Entry und bauen auf derselben CID-/Registry- und AOI-Grundlage auf.

## Quellen

- Client: `Modules/AClient/AgcmCharacter/AgcmCharacter.cpp`, Receive Op 7/8, `SendLoadingComplete`.
- Referenz-Gameserver: `Modules/AServer/AgsmCharManager/AgsmCharManager.cpp`, `OnReceive` Op 9 und `EnterGameWorld`.
- Referenz-Gameserver: `Modules/AServer/AgsmCharacter/AgsmCharacterPacket.cpp`, `SendCharacterAllInfo`, `SendPacketChar`, `SendPacketCharView`, `SendRegionNPCToChar`.
- Vorbedingung: [`WINSOCK_SEQUENCE_24_GAMESERVER_BOOTSTRAP_WORLD_ENTRY.md`](Sequenz-24-Gameserver-Bootstrap-World-Entry.md).
