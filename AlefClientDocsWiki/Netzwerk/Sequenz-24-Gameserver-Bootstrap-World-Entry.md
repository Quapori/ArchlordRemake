# Sequenz 24: Gameserver-Bootstrap nach Login-Op8

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ziel und Grenze

Diese Sequenz beginnt nach der bereits dokumentierten Login-Antwort Op 8. Sie beschreibt den ersten TCP-Dialog mit dem Gameserver bis zu dem Punkt, an dem die Welt fuer den Spieler betreten werden darf. Sie ist die notwendige Grundlage fuer NPC-Spawns, Bewegung, Kampf, EXP, Items und Quests.

Die Erkenntnisse sind sowohl gegen den Client als auch gegen den vorhandenen EP8-Referenz-Gameserver abgeglichen. Sie sind deshalb ein belastbarer Protokollvertrag, nicht nur eine UI-Inferenz.

## Gesamtfolge

```text
Loginserver Op 8: CID + CharacterName + Gameserver-Adresse
  -> Client baut neuen TCP-Socket zum Gameserver auf
  -> optional StartupEncryption auf diesem Socket
  -> Client -> Gameserver AgcmCharacter Op 2 REQUEST_CLIENT_CONNECT
  -> Gameserver prueft CharacterName, AuthKey, Welt und Socketbesitz
  -> Gameserver -> Client Konfiguration/EventEffect und AgcmCharacter Op 8 CHARACTER_POSITION
  -> Client laedt Mapsektoren an dieser Position und leert die lokale Registry
  -> Client -> Gameserver AgcmCharacter Op 9 LOADING_COMPLETE
  -> Gameserver -> Client Character-All-Info, regionsgebundene NPCs und Op 7 SETTING_CHARACTER_OK
  -> Gameserver gibt die Figur in die Welt und beginnt Sichtbereich/Gameplay zu senden
```

Der Gameserver darf sichtbare NPCs, andere Spieler oder kampfrelevante Pakete nicht als Ersatz fuer Op 8/Op 9 verwenden. Ohne die Startposition ruft der Client `LoadTargetPosition` nicht auf; ohne sein eigenes LoadingComplete ruft der Originalserver `EnterGameWorld` nicht auf.

## Paketmodul und Felder

Der Bootstrap verwendet das `AgcmCharacter`/`AgsmCharManager`-Paket mit sechs maskierten Feldern:

| Feld | Typ | Bedeutung |
|---:|---|---|
| 0 | INT8 | Operation |
| 1 | CHAR[12] | AccountName |
| 2 | INT32 | CharacterTemplateID |
| 3 | CHAR[AGPACHARACTER_MAX_ID_STRING + 1] | CharacterName |
| 4 | INT32 | CID |
| 5 | POS | Position |
| 6 | INT32 | AuthKey |

Die Maske hat in diesem Modul ein Byte. Nicht benoetigte Felder werden weggelassen.

## Client -> Gameserver

### Op 2: REQUEST_CLIENT_CONNECT

Direkt nach erfolgreichem TCP-Connect ruft [`AgcmStartupEncryption`](../Module/AgcmStartupEncryption.md):CBConnectGameServer` den Sender `AgcmCharacter::SendRequestClientConnection` auf. Wenn StartupEncryption aktiv ist, geschieht dies erst nach deren Public/Private-Handshake.

| Feld | Gesendeter Wert |
|---|---|
| Operation | 2 |
| CharacterName | der aus Login-Op 8 uebernommene Name |
| AuthKey | zuletzt empfangener AuthKey, anfangs ggf. 0 |

AccountName, TemplateID, CID und Position fehlen im Request.

Der Charaktername ist die primaere Identitaet am Gameserver. Der Originalserver sucht damit die vorab aus dem Loginserver uebergebene Charakterinstanz. Ein neuer Server darf den Clientnamen nicht als ausreichenden Besitznachweis behandeln: Er muss Name, Welt, Session und Socketbindung gegen seinen Handoff-Zustand pruefen.

### Op 9: LOADING_COMPLETE

Der Client sendet Op 9 erst als Reaktion auf die serverseitige Startposition:

| Feld | Gesendeter Wert |
|---|---|
| Operation | 9 |
| CID | persistente Character-CID aus Op 8/Startposition |

Dieser Frame ist der Freigabepunkt fuer das Weltbetreten. Nicht mit dem vorherigen Socket-Connect verwechseln.

## Gameserver -> Client

### Selbstcharakterdaten nach Op 9

Die Op-2-Behandlung sendet bewusst noch keine Character-All-Info. Erst der Empfang von Op 9 ruft im Referenzserver `AgsmCharManager::EnterGameWorld` auf. Diese Funktion sendet als erstes `AgsmCharacter::SendCharacterAllInfo`, danach Titeldaten, regionale NPCs und schliesslich Op 7.

Bevor `SETTING_CHARACTER_OK` sinnvoll verarbeitet werden kann, muss die lokale [`AgpmCharacter`](../Module/AgpmCharacter.md)-Registry den eigenen CID daher durch diesen nach-Op-9-Burst bereits kennen. `SendCharacterAllInfo` beginnt mit einem vollstaendigen `AgpmCharacter`-Add inklusive Factors und ruft anschliessend die registrierten Module fuer weitere Charakterdaten auf. Beim Empfang von Op 7 muss `AgpmCharacter::GetCharacter(CID)` erfolgreich sein; sonst bricht der Client ab.

Der genaue Character-All-Info-Burst wird als naechste Sequenz getrennt zerlegt. Mindestbedingung ist: Beim Empfang von Op 7 muss `AgpmCharacter::GetCharacter(CID)` erfolgreich sein. Sonst bricht der Client ab.

### Op 7: SETTING_CHARACTER_OK

| Feld | Gesendeter Wert |
|---|---|
| Operation | 7 |
| CID | persistente Character-CID |

Der Client setzt SelfCID, nimmt das bereits bekannte lokale Character-Objekt als SelfCharacter und verknuepft es mit dem Gameserver-Socket.

### Op 8: CHARACTER_POSITION

| Feld | Gesendeter Wert |
|---|---|
| Operation | 8 |
| CID | persistente Character-CID |
| Position | persistierte Weltposition `(x, y, z)` |

Die Wirkung im Client ist fest:

1. SelfCID wird erneut gesetzt.
2. `AgcmMap::LoadTargetPosition(x, z)` laedt die Welt um die Startposition.
3. Die lokale Character-Registry wird geleert.
4. Der Client sendet unmittelbar Op 9 `LOADING_COMPLETE`.

Die Reihenfolge ist absichtlich: Op 8 loest den sektorbezogenen Weltload aus und entfernt alle temporaeren lokalen Character-Objekte. Erst nach dem darauf folgenden Op 9 baut der Gameserver die Registry erneut auf: zuerst SelfCharacter/All-Info, dann NPCs und erst danach die SelfCharacter-Bindung durch Op 7.

### Op 11: AUTH_KEY

| Feld | Gesendeter Wert |
|---|---|
| Operation | 11 |
| CharacterName | CharacterName |
| AuthKey | serverseitig erzeugter Sessionwert |

Der Client speichert diesen Wert als `m_lReceivedAuthKey`. Beim naechsten Gameserver-Connect wird er in Op 2 zurueckgesendet. Der Referenzserver markiert AuthKeys nach erfolgreicher Verwendung ungueltig; sie muessen daher pro Handoff einmalig und kurzlebig sein.

## Serverseitige Validierung vor Weltbeitritt

Der Referenzserver validiert beim Op-2-Empfang mindestens:

1. StartupEncryption ist vollstaendig, falls aktiv.
2. CharacterName ist nicht leer und referenziert einen vom Loginserver vorbereiteten Charakter.
3. Character besitzt Serverdaten und gehoert zur Zielwelt oder einer erlaubten Subworld.
4. AuthKey ist gueltig, wenn der Handoff einen verwendet.
5. Socket wird an die Character-CID und den Account gebunden.

Erst danach aktiviert er den Sendepuffer, uebertraegt Konfiguration/EventEffect-Daten, sendet die Startposition und wartet auf Op 9.

## Persistenzbedarf fuer den Mindest-World-Entry

| Entitaet | Erforderliche Werte |
|---|---|
| Handoff-Session | AccountID, CID, CharacterName, Zielwelt, Ablaufzeit, einmaliger AuthKey, erlaubte Socketbindung |
| Character | CID, TemplateTID, Name, Level/EXP/Faktoren, HP/MP/SP, Position, Richtung, Status, Aussehen |
| World | WorldID/Name, erlaubte Subworlds, Spawn-/Fallback-Position, Map-/Sektorkonfiguration |
| Laufzeit-Entity | CID, Socket/NID, Sichtbereich, Ladezustand `await_loading_complete` oder `in_world` |

## Unmittelbare Folgearbeit

Nach Op 9 beginnt der echte Gameserver. Die Analyse wird in dieser Reihenfolge fortgesetzt:

1. Character-All-Info und Sichtbereich: SelfCharacter, NPCs, Monster und andere Spieler korrekt als Add-/View-Pakete senden.
2. Bewegung und Zielauswahl: clientseitige Requests, serverautoritatives Positionsupdate und Sichtbereichswechsel.
3. Normalangriff und Skills: Action-Pakete, Schaden, HP-/Factor-Updates, Tod.
4. Monster-Tod: Angreiferliste, EXP-Verteilung, Level-Up-Paket und Respawn.
5. Drops und Pickup: Bodenitem, Besitzer-/Sichtbarkeitsregeln, Inventartransaktion.
6. Quests: Annahme, Kill-/Item-/Checkpoint-Fortschritt, Abschluss, Belohnung.

## Quellen

- Client: `Modules/AClient/AgcmCharacter/AgcmCharacter.cpp` (`SendEnterGameWorld`, `SendRequestClientConnection`, `OnReceive`, `SendLoadingComplete`).
- Client: `Modules/AClient/AgcmStartupEncryption/AgcmStartupEncryption.cpp` (`CBConnectGameServer`).
- Referenz-Gameserver: `Modules/AServer/AgsmCharManager/AgsmCharManager.cpp` (Op-2-Validierung, `SendCharacterSettingOK`, `SendCharacterLoadingPosition`, `SendAuthKeyPacket`, Op-9-Verarbeitung).
- Vorbedingung: [`WINSOCK_SEQUENCE_21_CHARACTER_SELECT_GAMESERVER_HANDOFF.md`](Sequenz-21-Character-Select-Gameserver-Handoff.md).
