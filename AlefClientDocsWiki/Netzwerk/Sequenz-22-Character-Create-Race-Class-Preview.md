# Winsock-Sequenz 22: Rassen- und Klassenvorschau bei der Charaktererstellung

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ursache

Die Rassen-/Klassenauswahl ist kein reines UI- oder Datenbankfeature. Der
Client erwartet nach dem Request AGPMLOGIN_RACE_BASE (Login Operation 10)
temporaere Basischaraktere auf dem AgpmCharacter-Kanal.

Der aktuelle Server antwortet auf Operation 10 nur mit einem leeren
AgcmLogin-Operation-10-Paket. Dadurch werden keine Basisobjekte fuer Human,
Orc und MoonElf in der lokalen AgpmCharacter-Registry angelegt. Sichtbar ist
nur der bereits anderweitig vorhandene DragonScion-Templatecharakter mit TID
1724.

Der Wert 1724 ist daher kein Auswahlwert, den der Server auf die anderen
Rassen ueberschreibt. Er ist das einzige lokal auffindbare, verwendbare
Vorschauobjekt.

## Clientbedingung fuer eine waehlbare Rasse/Klasse

AgcmUICharacterCreate::FindCreateCharacterModel durchsucht die lokale
AgpmCharacter-Registry. Ein Modell wird nur akzeptiert, wenn alle Bedingungen
zutreffen:

1. Das Character-Template hat die gewuenschte Rasse und Klasse.
2. Das Objekt hat einen geladenen Template-/Clump-Pfad.
3. Der Character-Status ist AGPDCHAR_STATUS_IN_GAME_WORLD.

Die Enums ergeben:

    AGPDCHAR_STATUS_LOGOUT        = 0
    AGPDCHAR_STATUS_IN_LOGIN_PROCESS = 1
    AGPDCHAR_STATUS_IN_GAME_WORLD = 2

Der aktuelle Add-Builder des Loginservers setzt das Hauptfeld Character Status
auf 0. Das reicht fuer die Charakterlistenansicht, aber nicht fuer
FindCreateCharacterModel. Vorschauobjekte muessen daher Status 2 erhalten.

## Originaler Ablauf

    Client: Op 10 + nested CharDetailInfo(RaceInfo = angeforderte Rasse)
    Server: AgpmCharacter Op 0 Add fuer die Basis-Templates
    Server: AgcmLogin Op 10 + CharDetailInfo(MaxRegisterChars, RaceInfo)
    Client: AGCMLOGIN_CB_RACE_BASE
    Client: Charaktererstellungsmodus, OnSelectRace und OnSelectClass

Der originale Loginserver verarbeitet den RaceInfo-Wert, sendet zuerst die
Basischaraktere per SendCharacterAllInfo und erst danach
SendBaseCharacterOfRace. Der finale Op-10-Reply enthaelt nested:

| CharDetailInfo-Feld | Wert |
|---|---|
| MaxRegisterChars, Bit 2 | 10 im EP8-Referenzserver |
| RaceInfo, Bit 5 | der RaceInfo-Wert aus dem Request |

Die leere Op-10-Antwort loest zwar den Callback aus, aber ohne die vorher
eingetroffenen Add-Pakete findet OnSelectRace kein Modell und kann keine
Rasse umschalten.

## Basis-Templates des Referenzservers

Der Referenzserver erzeugt zehn temporaere Basischaraktere. Die folgenden TIDs
sind sowohl in AgsmLoginClient.cpp als auch in der vorhandenen
character_templates-Migration belegt:

| TID | Rasse | Klasse / Vorschau |
|---:|---|---|
| 96 | Human | Knight/Warrior |
| 1 | Human | Archer/Ranger |
| 6 | Human | Mage/Elementalist |
| 4 | Orc | Berserker/Warrior |
| 8 | Orc | Hunter/Ranger |
| 3 | Orc | Sorcerer/Elementalist |
| 9 | MoonElf | Elementalist |
| 460 | MoonElf | Ranger |
| 377 | MoonElf | Swashbuckler/Warrior |
| 1724 | DragonScion | Scion |

Der Referenzpfad schickt diese Vorschauobjekte vor dem Op-10-Abschluss. Er
benutzt dafuer eigene, nicht persistierte Character IDs und Namen. Die IDs
muessen nicht die IDs aus der characters-Tabelle sein, aber pro Client-
Session eindeutig und ungleich 0 sein. Sie duerfen insbesondere nicht mit
einem gespeicherten Auswahlcharakter kollidieren.

## Erforderlicher Sendervertrag

Der kuenftige Op-10-Handler muss den RaceInfo-Wert aus dem nested
CharDetailInfo lesen. Danach:

1. Die zehn Basis-TIDs gegen die lokale Template-Tabelle validieren.
2. Fuer jedes Template ein temporaeres AgpmCharacter-Op-0-Add-Paket senden.
3. Jedes dieser Pakete braucht eine eindeutige nicht-null CID, Template-TID,
   Namen, einen syntaktisch validen Move-Block und Character Status 2.
4. Die Add-Pakete muessen vor dem abschliessenden Login-Op-10-Frame auf
   derselben verschluesselten Arbeitsphase gesendet werden.
5. Den finalen Op-10-Frame mit MaxRegisterChars = 10 und RaceInfo senden.

Das Factor-Paket ist fuer die Rassen-/Klassensuche nicht der unmittelbare
Blocker: FindCreateCharacterModel liest Rasse und Klasse aus dem bereits
lokal geladenen Character-Template. Es sollte trotzdem fuer einen
produktionsnahen Sender spaeter aus Templatewerten entstehen.

## Nachweis und Testkriterien

Nach dem Klick auf Charakter erstellen muss der Log in dieser Reihenfolge
zeigen:

1. Client-Request Login-Modul 0x0d, Operation 10, nested RaceInfo.
2. Zehn Serverframes Modul 0x02, Operation 0, mit den oben genannten TIDs
   und Status 2.
3. Einen Serverframe Modul 0x0d, Operation 10, mit nested
   MaxRegisterChars und RaceInfo.
4. Danach muessen Human, Orc, MoonElf und DragonScion lokale
   FindCreateCharacterModel-Treffer besitzen. Beim Klassentausch muss sich
   die an den Create-Request Op 11 uebergebene TID entsprechend aendern.

Fehlen die Op-0-Pakete, ist die leere Op-10-Antwort weiterhin die Ursache.
Sind die Pakete vorhanden, aber eine Rasse bleibt nicht waehlbar, sind als
naechstes Template-TID, Status 2, Template-Factor (Rasse/Klasse) und
CID-Kollisionen zu pruefen.

## Quellen

- Client: Modules/AClient/AgcmUILogin/AgcmUICharacterCreate.cpp,
  FindCreateCharacterModel, OnSelectRace, OnSelectClass und
  CB_OnGetBaseCharacterOfRace.
- Client: Modules/AClient/AgcmLogin/AgcmLogin.cpp,
  SendGetBaseCharacterOfRace.
- Referenzserver: Modules/AServer/AgsmLoginClient/AgsmLoginClient.cpp,
  ProcessBaseCharacterOfRace, SendBaseCharacterOfRace und
  CreateBaseCharacterOfRace.
- Statusenum: Include/AgpdCharacter.h.
- Aktueller Loginserver: AlefLogin/crates/aleflogin-server/src/main.rs,
  AGPMLOGIN_RACE_BASE und build_add_character_packet.
