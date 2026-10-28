# Winsock Sequenz 03: World-Entry, AgpmWorld und AgpmCharacter

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei setzt nach Login, StartupEncryption und [`AgcmConnectManager`](../Module/AgcmConnectManager.md)-Handoff an. Ziel ist, die ersten World-/Character-Pakete zu dokumentieren: was der Client nach dem Wechsel auf den Spiel-/Worldsocket sendet, welche Module beteiligt sind und welche Serverdatenbank-Strukturen daraus ableitbar sind.

## Kurzfazit

- [`AgpmWorld`](../Module/AgpmWorld.md) ist Modul-ID `0x18`.
- [`AgpmCharacter`](../Module/AgpmCharacter.md) ist Modul-ID `0x02`.
- `AgcmCharacter` baut viele Client->Server Pakete ueber das `AgpmCharacter`-Layout.
- Der eigentliche Eintritt in die Spielwelt ist nicht ein einzelnes Paket, sondern eine Kette:
  1. Login-/Character-Auswahl liefert Charakter-/Server-Kontext.
  2. `AgcmConnectManager` schaltet auf Game-/Worldsocket.
  3. StartupEncryption kann auf dem neuen Socket erneut laufen.
  4. Client sendet ResourceInfo/Character-/World-Entry Pakete.
  5. Server sendet `AgpmCharacter` Operationen zum Anlegen/Aktualisieren von Charakteren und setzt den lokalen Spieler.

## AgpmWorld

### Konstruktor `FUN_0056dfc0` (`0x0056dfc0`)

Der Konstruktor initialisiert `AgpmWorld`:

```c
strncpy(moduleName, "AgpmWorld", 0x27);
FUN_004e4640(1);
FUN_004e4190(0x8c, 0);
FUN_004e4540(0x18);
FUN_004ea630(1);
FUN_004e9f30(param_1 + 0x2e1,
             1,1, 0,0x20, 3,1, 0xd,1, 0,0x20, 0xff,0);
```

Offset:

- `param_1 + 0x2e1 * 4 = +0xb84`: `AuPacket`-Layout fuer `AgpmWorld`.

Paketlayout:

| Reihenfolge | Layout-Code | Count/Size | Gesicherte/naheliegende Bedeutung |
|---|---:|---:|---|
| 1 | `1` | `1` | Operation Byte |
| 2 | `0` | `0x20` | String, max. 32 Bytes |
| 3 | `3` | `1` | kleiner Integer, vermutlich short/word |
| 4 | `0xd` | `1` | verschachteltes/variantes Feld |
| 5 | `0` | `0x20` | zweiter String, max. 32 Bytes |

Die World-Pakete sind damit im Vergleich zu Character klein. Wahrscheinlich werden hier Worldname, Instance/Region-Name, Mapname oder Transfer-Kontext ausgetauscht.

## AgcmWorld Sendefunktionen

### `FUN_006da9a0` (`0x006da9a0`)

Sendet `AgpmWorld` Modul `0x18`, Operation `0`.

```c
local_5 = 0;
packet = FUN_004ea280(AgpmWorld + 0xb84, 1, &packetLen, 0x18,
                      &local_5, packetLenOrArg, &local_4, 0);
FUN_004e45d0(packet, packetLen, 2, -1, socketId);
```

Beobachtungen:

- Route: `FUN_004e45d0(..., 2, -1, param_3)`
- Das Paket geht nicht zwingend ueber den Default-Socket, sondern ueber einen expliziten Socket/Routing-Wert.
- Enthalten sind Operation `0`, ein 32-bit/Pointer-Argument und ein lokaler Wert.

Interpretation:

- Sehr wahrscheinlich eine World-Entry- oder World-Request-Nachricht.
- Der Client sendet sie auf dem Game-/Worldsocket, nachdem der Socket durch ConnectManager/StartupEncryption bereit ist.

### `FUN_006daa30` (`0x006daa30`)

Sendet ebenfalls `AgpmWorld` Modul `0x18`; die Operation liegt in `local_1`, ist im Decompiler aber nicht initialisiert sichtbar.

```c
packet = FUN_004ea280(AgpmWorld + 0xb84, 1, &packetLen, 0x18,
                      &local_1, packetLenOrArg, 0, 0);
FUN_004e45d0(packet, packetLen, 2, -1, socketId);
```

Die nicht sichtbare Initialisierung ist ein Decompiler-Artefakt. Funktional ist sicher:

- Modul `0x18`
- expliziter Socket/Routing-Wert
- kurzer World-Request oder World-Ack

## ResourceInfo / Entry-Pakete mit Opcode `0x2f`

Vor oder waehrend des World-Entry tauchen Pakete mit Modul/Opcode `0x2f` auf. Sie werden aus ResourceInfo-/Return-Pfaden gebaut und anschliessend ueber `FUN_004e45d0` gesendet.

### `FUN_0057c450` (`0x0057c450`)

```c
op = 1;
packet = FUN_004ea280(this + 0xb88, 1, outLen, 0x2f,
                      &op, &param_2, 0,0,0,0);
```

Sicher:

- Modul `0x2f`
- Operation `1`
- ein 32-bit Wert `param_2`

Nutzung:

- `FUN_006da5b0` ruft diese Funktion mit `AgcmCharacter`-Daten auf.
- Das Ergebnis wird nur gesendet, wenn Paketlaenge groesser als `0x0c` ist.

Naheliegende Bedeutung:

- Resource-/Client-State fuer World-Entry
- Character-ID oder Clientobjekt-ID als erstes gebundenes Feld

### `FUN_0057c4a0` (`0x0057c4a0`)

```c
op = 6;
packet = FUN_004ea280(this + 0xb88, 1, outLen, 0x2f,
                      &op, 0, accountOrNameString, 0,0, &param_3);
```

Sicher:

- Modul `0x2f`
- Operation `6`
- String-Feld, aus `AgcmLogin + 0xc4c` bzw. Account-/Name-Kontext
- weiterer Wert `param_3`

Nutzung:

- `FUN_006da680` baut dieses Paket nach StartupEncryption/Return-to-login:

```c
packet = FUN_0057c4a0(AgcmLogin + 0xc4c, AgcmReturnToLogin + 0xbac, &len);
socketId = FUN_006f5740();
FUN_004e45d0(packet, len, 2, -1, socketId);
```

Interpretation:

- Wird ueber den ersten Socket vom ConnectManager-Typ `1` gesendet.
- Sehr wahrscheinlich eine Login-/Return-/Character-Session-Bestaetigung auf dem Game-/Worldsocket.
- Das String-Feld ist wahrscheinlich Accountname oder ein damit verwandter Login-Kontext.

## AgpmCharacter

### Konstruktor `FUN_0050aa40` (`0x0050aa40`)

Initialisiert `AgpmCharacter`:

```c
strncpy(moduleName, "AgpmCharacter", 0x27);
FUN_004e4600(1);
FUN_004e4620(1);
FUN_004e4190(0x818, 0);
FUN_004e4190(0x22c0, 1);
FUN_004e4540(2);
FUN_004ea630(4);
FUN_004e9f30(param_1 + 0x379, ...);
FUN_004ea630(1);
FUN_004e9f30(param_1 + 0x4dbe, ...);
FUN_004ea630(2);
FUN_004e9f30(param_1 + 0x9803, ...);
FUN_004ea630(2);
FUN_004e9f30(param_1 + 0xe248, ...);
```

Wichtige Layout-Offsets:

| Offset | Zweck |
|---:|---|
| `+0xde4` | Hauptlayout fuer `AgpmCharacter` Modul `0x02` |
| `+0x136f8` | verschachteltes Movement-/Position-/State-Layout |
| `+0x2600c` | weiteres verschachteltes Action-/State-Layout |
| `+0x38920` | 7-fach 32-bit Layout, vermutlich Faktor-/Statusblock |

Das Hauptlayout ist gross und enthaelt viele optionale Felder. Es beginnt mit:

```c
1,1, 5,1, 5,1, 0xd,1, 1,1,
0xc,1, 0xc,1, 0xc,1,
7,1, 7,1, 7,1,
...
0,0x20,
...
0,0x10,
0xd,1, 6,1, 6,1
```

Sicher ablesbare Feldgruppen:

- Operation Byte
- Character-ID / CID
- mehrere 32-bit IDs/Werte
- Name/String bis `0x20`
- mehrere Byte-Statusfelder
- mehrere 64-bit/Time-/Currency-artige Werte (`7`, `10`)
- verschachtelte Blobs (`0xd`)
- ein kurzer String bis `0x10`

## AgpmCharacter Empfang: `FUN_00509cb0`

`FUN_00509cb0` ist die zentrale `AgpmCharacter::OnReceive()`-Logik. Sie deserialisiert das Hauptlayout `+0xde4`:

```c
FUN_004e9fb0(param_1 + 0xde4, 1, packet, packetLen,
             &op, &cid, &local_120, &nameBlob,
             &nameLen, ... viele weitere Felder ...);
```

CID-Pruefung:

```c
if (op not in 0x1c..0x20 &&
    receivedFromServer == false &&
    ownerCID != 0 &&
    cid != ownerCID) {
    printf("Received Invalid CID Packet (AgpmCharacter)");
}
```

Das bestaetigt:

- Viele Character-Pakete sind an eine bestimmte Character-ID gebunden.
- Der Client kennt eine eigene/Owner-CID im Socket-/Dispatch-Kontext.
- Bestimmte globale Operationen `0x1c` bis `0x20` duerfen ohne CID-Bindung durch.

### Empfangsoperationen

| Op | Bedeutung aus Code | Serverseitige DB-/State-Relevanz |
|---:|---|---|
| `0x00` | Add Character; legt Charakter im Client-Pool an | Character Spawn, Sichtbarkeitsliste, Weltobjekt |
| `0x01` | Update Character; ruft `FUN_00509240`, Event `0x40` | Position/Status/Stats/Aussehen aktualisieren |
| `0x02` | Remove Character | Despawn, Logout, Zone verlassen |
| `0x03` | Character entfernen/zerstoeren ueber `FUN_00506d40` | Objektlebenszyklus |
| `0x05` | ruft `FUN_00505f20`, verarbeitet weiteres Objekt/Statusfeld | vermutlich attach/equip/entity-state |
| `0x06` | ruft `FUN_00505fb0` | Beziehung/Ziel/Objektbindung |
| `0x07` | `FUN_0058aa00`, zwei Werte | Erfahrungs-/Geld-/Zaehlwert-Update |
| `0x08` | Event `0x42` | globales Character-Event |
| `0x09` | Event `0x46` mit Flag `1` | Status-/Selection-/Visibility-Update |
| `0x0a` | CID-Gueltigkeits-/Ack-Fall, kein sichtbarer Statechange | Acknowledge/Keepalive-artig |
| `0x0b` | `FUN_00503cf0(cid, value)` | einzelnes Character-Feld setzen |
| `0x0c` | `FUN_00503d60(cid)` | Status loeschen/Reset |
| `0x0d` | `FUN_00506930(cid)` | serverbestaetigter Character-Zustand |
| `0x0e` | nur Gueltigkeits-/Ack-Pfad | offen |
| `0x0f` | server-only Gueltigkeitspfad | offen |
| `0x10` | `FUN_00503e90(cid, value)` | Status/Mode setzen |
| `0x11` | `FUN_00505d30`, Event `0x52` wenn Feld geaendert | wahrscheinlich HP/MP/Statuswert |
| `0x12` | `FUN_00505d30`, Event `0x5b` | aehnlich, aber anderer Eventkanal |
| `0x13` | Event `0x46` mit Flag `2` | Sichtbarkeit/Mode Variante |
| `0x14` | Event `0x46` mit Flag `3` | Sichtbarkeit/Mode Variante |
| `0x15` | `FUN_00503ef0(cid, a, b)` | Positions-/Richtungs-/Wertpaar |
| `0x16` | `FUN_00503f60(cid, value)` | einzelnes Feld |
| `0x17` | kopiert String nach `character + 0xa4`, Event/UI Update | Titel/Guild/Displayname-artiges Feld |
| `0x18` | `FUN_00503f80(cid, value, local_11c)` | zwei Werte |
| `0x19` | `FUN_00504010(cid, local_11c)` | ein Wert |
| `0x1a` | `FUN_00503db0(cid, local_120)` | Feld setzen |
| `0x1b` | `FUN_00503e20(cid, local_120)` | Feld setzen |
| `0x1c` | `FUN_00504040(packetPtr)` | globaler Character-Block |
| `0x1d` | Event `0x19` mit PacketPtr | globales Event |
| `0x1e` | `FUN_00504060(packetPtr)` | globaler Character-Block |
| `0x1f` | `FUN_005040c0(packetPtr)` | globaler Character-Block |
| `0x20` | `FUN_00504080(packetPtr)` | globaler Character-Block |
| `0x21` | `FUN_005040a0(packetPtr)` | globaler Character-Block |
| `0x22` | liest mehrere DWORDs ab `packet+0x14`, Event `0x7f` | groesserer Transform-/Stateblock |

## AgcmCharacter Client->Server Sends

Die folgenden Funktionen bauen `AgpmCharacter` Pakete mit Modul `0x02`.

### `FUN_005a02c0` (`0x005a02c0`)

```c
op = 0x0d;
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &op, &cid, 0,0,0,...);
FUN_004e45d0(packet, len, 0, 3, 0);
```

Sicher:

- Client sendet Operation `0x0d`.
- Enthalten ist eine Character-ID.
- Nur erlaubt, wenn kein lokaler Player gesetzt ist oder dessen ID zu `param_2` passt.

Interpretation:

- Wahrscheinlich Character-Select/Character-Ready/Request-State fuer einen bestimmten Charakter.

### `FUN_005a03c0` (`0x005a03c0`)

Baut ein verschachteltes Paket `AgpmCharacter + 0x136f8` und legt es in das Hauptpaket Operation `1`.

```c
flags = hasParam4 | hasParam5 << 1 | hasParam6 << 4;
nested = FUN_004ea280(AgpmCharacter + 0x136f8, 0, &len, 2,
                      fieldA, fieldB, 0,0,0,0, &flags, &param4);
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &op1, localPlayerCID, 0,0,0, nested, ...);
socketRoute = current character socket owner id;
FUN_004e45d0(packet, len, 0, -1, socketRoute);
```

Interpretation:

- Hauptoperation `1` ist ein Character-Update.
- Das Nested-Layout enthaelt Bewegung/Position/Action-Flags.
- Client sendet Positions- oder Bewegungszustand des lokalen Characters.

### `FUN_005a05b0` (`0x005a05b0`)

```c
nested flags: local_6 = 0x40, local_7 = 0;
main op = 1;
main cid = local player cid;
route = FUN_005a0200();
```

Interpretation:

- Spezielles Movement-/State-Paket mit Flag `0x40`.
- Wahrscheinlich Stop/Idle/State-Reset oder ein bestimmter Bewegungsmodus.

### `FUN_005a0700` (`0x005a0700`)

```c
nested position source = localPlayer + 0xd8;
nested flags: local_6 = 4, local_7 = 0;
main op = 1;
main cid = local player cid;
route = FUN_005a0200();
```

Interpretation:

- Sendet aktuelle lokale Position (`character + 0xd8`) mit Flag `4`.
- Sehr wahrscheinlich ein normaler Movement-/Position-Sync.

### `FUN_005a0860` (`0x005a0860`)

Baut nested Layout `AgpmCharacter + 0x2600c`, dann Hauptpaket Op `1`.

```c
nested = FUN_004ea280(AgpmCharacter + 0x2600c, 0, &len, 2,
                      &param_2, &param_3, &param_4, 0,0,0,
                      optional &param_5);
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &op1, localPlayerCID, 0,0,0,0,nested,...);
FUN_004e45d0(packet, len, ...);
```

Interpretation:

- Ebenfalls Character-Update, aber anderes Nested-Layout.
- Wahrscheinlich Action/Attack/Skill/Target-State, weil mehrere IDs/Werte und ein optionaler Parameter gesendet werden.

### `FUN_005a0a60` (`0x005a0a60`)

```c
op = 0x10;
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &op, localPlayer + 4, ... optional stack arg ...);
FUN_004e45d0(packet, len, 0, 3, 0);
```

Interpretation:

- Sendet Character Operation `0x10` fuer den lokalen Character.
- Bedingungen pruefen, dass der Character nicht in bestimmten gesperrten States ist.
- Moeglich: Interaktion/Cancel/Request-Status.

## Warum `AgpmCharacter` fuer World-Entry zentral ist

Der Client behandelt die Welt zuerst ueber Character-Objekte:

- Der lokale Spieler ist ein Character mit CID.
- Andere Spieler/NPCs/Mobs kommen als `Add Character`/`Update Character`/`Remove Character`.
- Positionen, Sichtbarkeit, Statuswerte und Appearance-Felder haengen an `AgpmCharacter`.
- `AgpmWorld` selbst scheint eher Metadaten/World-Auswahl/World-Transfer zu tragen.

## Wann wird was gesendet?

### Nach Login-Erfolg und vor Weltbeitritt

Wahrscheinlich:

- Loginmodul sendet Character-Auswahl oder Server-Auswahl.
- Server sendet Handoff-Daten.
- Client verbindet Game-/Worldsocket.
- StartupEncryption auf neuem Socket.
- Client sendet ResourceInfo `0x2f` Op `1` oder Op `6`, je nach Pfad.

### Beim eigentlichen Eintritt

Wahrscheinlich:

- Client sendet `AgpmWorld` Op `0`/weiteres World-Ack auf Modul `0x18`.
- Client sendet `AgpmCharacter` Op `0x0d` oder Op `1` fuer lokalen Character-Kontext.
- Server sendet `AgpmCharacter` Op `0` fuer Add Character und Op `1` fuer Update.
- Danach laufen Movement-/Action-Updates ueber `AgpmCharacter` Op `1`.

### Laufend im Spiel

Sicher sichtbare laufende Client-Sends:

- `AgpmCharacter` Op `1`: Movement/State/Action-Update mit nested Layout.
- `AgpmCharacter` Op `0x0d`: CID-bezogene Anfrage/Bestaetigung.
- `AgpmCharacter` Op `0x10`: lokaler Character-Status/Interaktion.

## Serverdatenbank: Ableitungen

### `worlds`

| Feld | Grund |
|---|---|
| `world_id` | World-/Mapauswahl und serverseitiger Zielkontext |
| `world_name` | `AgpmWorld` besitzt Stringfelder bis `0x20` |
| `server_group_id` | Login INI hat `ServerGroup` |
| `route_id` | ConnectManager Handoff zum Worldserver |

### `world_instances`

| Feld | Grund |
|---|---|
| `instance_id` | MMO-Zonen/Channels brauchen laufende Instanzen |
| `world_id` | Instanz gehoert zu Welt/Map |
| `channel_id` | Handoff kann auf Channelserver routen |
| `host` / `port` | ConnectManager sendet `host:port` |
| `population` | Loginserver muss Zielserver waehlen |
| `state` | online, full, locked, shutting_down |

### `characters`

| Feld | Grund |
|---|---|
| `character_id` / `cid` | in fast jedem `AgpmCharacter` Paket |
| `account_id` | Login/Characterbindung |
| `name` | Stringfeld bis `0x20`; UI zeigt CharName |
| `world_id` / `instance_id` | World-Entry |
| `x`, `y`, `z`, `rotation` | Movement-Pakete nutzen Position ab Character `+0xd8` |
| `state_flags` | Movement-/Action-Flags `0x04`, `0x40`, Bitmasken |
| `hp`, `mp`, `level`, `exp` | UI und Character-Update-Werte |
| `guild_id`, `title`, `display_name` | String/Statusfelder, UI/Guild-Strings |

### `character_visibility`

Server muss wissen, welche Characters an welchen Client gesendet werden:

| Feld | Grund |
|---|---|
| `viewer_character_id` | Client bekommt nur relevante Add/Update/Remove |
| `visible_character_id` | Server sendet Add/Remove fuer einzelne CIDs |
| `last_sent_state_hash` | viele optionale Felder sprechen fuer Delta-Updates |
| `distance_cell` / `region_cell` | World/Octree-Aufteilung passt zu Sichtbarkeitsmanagement |

### `movement_events`

| Feld | Grund |
|---|---|
| `character_id` | CID in Character Op `1` |
| `timestamp` | Movement muss zeitlich validiert werden |
| `position_x/y/z` | Position aus local character data |
| `heading` / `rotation` | Bewegungszustand |
| `flags` | `0x04`, `0x40`, weitere Bitflags |
| `socket_session_id` | Movement kommt ueber gebundenen Game-Socket |

### `entity_spawns`

Nicht zwingend persistent, aber serverseitig als Runtime-Struktur noetig:

| Feld | Grund |
|---|---|
| `entity_id` / `cid` | Add/Remove Character |
| `entity_type` | Spieler, NPC, Monster, Summon |
| `template_id` | Aussehen/Stats muessen aus Stammdaten kommen |
| `world_instance_id` | Spawn in bestimmter Zone |
| `position` | sichtbare Weltposition |
| `appearance_blob` | Character-Paket enthaelt viele optionale Appearance-/Statusfelder |

## Offene Punkte fuer weitere Sequenzen

- Die genaue Semantik jedes `AgpmCharacter`-Feldes im Hauptlayout muss ueber lokale Setter-Funktionen (`FUN_00503cf0`, `FUN_00503d60`, `FUN_00503e90`, usw.) weiter benannt werden.
- Movement muss separat zerlegt werden: `+0x136f8` und `+0x2600c` sind die entscheidenden Nested-Layouts.
- Danach sollten Item/Inventory, Skill/Combat, Chat und Party/Guild als eigene Sequenzen folgen.
- Fuer echte Paketnamen waere ein Abgleich mit Debugstrings und UI-Callbacks pro Operation sinnvoll.

## Relevante Funktionen

| Funktion | Adresse | Rolle |
|---|---:|---|
| `FUN_0056dfc0` | `0x0056dfc0` | `AgpmWorld` Konstruktor, Modul `0x18` |
| `FUN_006da9a0` | `0x006da9a0` | Client sendet `AgpmWorld` Op `0` |
| `FUN_006daa30` | `0x006daa30` | weiterer `AgpmWorld` Sendepfad |
| `FUN_0050aa40` | `0x0050aa40` | `AgpmCharacter` Konstruktor, Modul `0x02`, Layouts |
| `FUN_00509cb0` | `0x00509cb0` | `AgpmCharacter::OnReceive` |
| `FUN_005a02c0` | `0x005a02c0` | Client sendet Character Op `0x0d` |
| `FUN_005a03c0` | `0x005a03c0` | Client sendet Character Op `1` mit Movement/State Nested-Paket |
| `FUN_005a05b0` | `0x005a05b0` | Client sendet Character Op `1`, Flag `0x40` |
| `FUN_005a0700` | `0x005a0700` | Client sendet Character Op `1`, Position ab `+0xd8`, Flag `4` |
| `FUN_005a0860` | `0x005a0860` | Client sendet Character Op `1` mit zweitem Nested-Layout |
| `FUN_005a0a60` | `0x005a0a60` | Client sendet Character Op `0x10` |
| `FUN_0057c450` | `0x0057c450` | ResourceInfo/Entry Modul `0x2f`, Op `1` |
| `FUN_0057c4a0` | `0x0057c4a0` | ResourceInfo/Entry Modul `0x2f`, Op `6` |
