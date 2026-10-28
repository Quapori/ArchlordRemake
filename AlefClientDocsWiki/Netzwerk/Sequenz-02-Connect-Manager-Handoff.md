# Winsock Sequenz 02: AgcmConnectManager, Server-Handoff und Socket-Routing

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei dokumentiert den zweiten Netzwerkabschnitt nach der Login-/StartupEncryption-Sequenz. Schwerpunkt ist [`AgcmConnectManager`](../Module/AgcmConnectManager.md): Der Server kann den Client anweisen, weitere TCP-Verbindungen zu `host:port`-Zielen zu öffnen, diese Verbindungen zu bestaetigen und spaeter als aktiven/default Socket fuer Spielpakete zu markieren.

## Kurzfazit

- Modulname: `AgcmConnectManager`
- Modul-ID / Paket-Opcode: `0x1b`
- Zentrale Empfangsfunktion: `FUN_006f5780` bei `0x006f5780`
- Zentrale Verbindungsfunktion: `FUN_006f5530` bei `0x006f5530`
- Client-seitige Antworten:
  - `FUN_006f5630`: sendet `AgcmConnectManager` Operation `2`
  - `FUN_006f56b0`: sendet `AgcmConnectManager` Operation `3`
- Interne Slot-Tabelle:
  - Basis: `AgcmConnectManager + 0x134ac`
  - Slot-Groesse: `0x20`
  - Anzahl laut Suchschleife: `800`
  - Adresse je Slot: `+0x134ac + slot * 0x20`
  - Metadaten je Slot: `+0x134c4 + slot * 0x20`
  - Slot-Typ/Flag je Slot: `+0x134c8 + slot * 0x20`
  - Aktiver/default Socket: `AgcmConnectManager + 0x198ac`

## Konstruktor und Paketlayout

### `FUN_006f53f0` (`0x006f53f0`)

Der Konstruktor initialisiert das Modul:

```c
strncpy(moduleName, "AgcmConnectManager", 0x27);
FUN_004e4540(0x1b);
FUN_004ea630(1);
FUN_004e9f30(param_1 + 0x2e6, 1,1, 5,1, 1,1, 0,0x17, 5,1, 0xc,1, 0xff,0);
memset(param_1 + 0x4d2b, 0, 0x6400);
*(undefined2 *)(param_1 + 0x662b) = 0xffff;
```

Auf Byte-Offsets umgerechnet:

- `param_1 + 0x2e6 * 4 = +0xb98`: `AuPacket`-Layout fuer ConnectManager.
- `param_1 + 0x4d2b * 4 = +0x134ac`: Beginn der Socket-/Server-Slot-Tabelle.
- `param_1 + 0x662b * 4 = +0x198ac`: aktiver/default Socket, initial `0xffff` (`-1`).

Das Layout wird mit Maskenbreite `1` registriert. Die Feldliste lautet:

| Reihenfolge | Layout-Code | Count/Size | Wahrscheinliche Bedeutung |
|---|---:|---:|---|
| 1 | `1` | `1` | Operation/Command Byte |
| 2 | `5` | `1` | 32-bit Wert, in Empfang als `local_c` genutzt |
| 3 | `1` | `1` | weiteres Byte/kleines Feld, in Empfang als `local_4` |
| 4 | `0` | `0x17` | String, wahrscheinlich `host:port`, max. 23 Zeichen |
| 5 | `5` | `1` | 32-bit Wert, in Empfang als `local_8` genutzt |
| 6 | `0xc` | `1` | weiterer Datentyp; bei Sendeseite teils decompiler-unsauber |

Die genaue Semantik der Feldtypen stammt aus dem lokalen `AuPacket`-Layoutsystem. Sicher ist: Feld 1 ist die Operation, Feld 4 ist ein String-Pointer, und mehrere Felder sind 32-bit Werte, die fuer Socket-/Session-Bindung verwendet werden.

## Interne Slot-Struktur

`FUN_006f5530` und `FUN_006f55d0` zeigen die Slot-Struktur:

```c
iVar4 = socketId * 0x20 + param_1;
strncpy((char *)(iVar4 + 0x134ac), hostPort, 0x17);
*(undefined2 *)(iVar4 + 0x134c8) = param_7;
```

`FUN_006f55d0` loescht fuer einen Slot acht DWORDs:

```c
puVar1 = (undefined4 *)(socketId * 0x20 + 0x134ac + param_1);
puVar1[0..7] = 0;
```

Damit ist die Slot-Laenge `0x20` sicher. Die ersten `0x18` Bytes enthalten offenbar den kopierten Zielstring, weil `strncpy(..., 0x17)` plus Nullterminierung in einen 24-Byte-Bereich passt. Danach folgen mindestens:

| Offset im Slot | Absoluter Offset | Beobachtung | Bedeutung |
|---:|---:|---|---|
| `+0x00` | `+0x134ac` | `strncpy(hostPort, 0x17)` | Zieladresse `host:port` |
| `+0x18` | `+0x134c4` | bei Server-Op `3` aus `local_8` gesetzt | Session-/Route-Metadatum |
| `+0x1c` | `+0x134c8` | von `param_7` gesetzt; Suche nach Wert `1` | Verbindungstyp/Gruppe |

`FUN_006f5740` durchsucht 800 Slots nach `slot.type == 1`:

```c
psVar2 = (short *)(param_1 + 0x134c8);
for (i = 0; i < 800; i++, psVar2 += 0x10) {
    if (*psVar2 == 1) return i;
}
return -1;
```

Das ist der wichtigste Hinweis auf zwei Socket-Gruppen:

- Typ `0`: vermutlich normale Login-/Handoff-Verbindung oder vom ConnectManager geoeffnete Verbindungen ohne Game-Routing-Flag.
- Typ `1`: Game-/World-Verbindung. Diese wird spaeter gezielt gesucht, z.B. fuer Return-to-login und Spielwelt-Kommunikation.

## Zentrale Verbindung: `FUN_006f5530`

Signatur laut Decompiler:

```c
short __thiscall FUN_006f5530(
    int this,
    char *hostPort,
    undefined4 owner,
    undefined4 onConnect,
    undefined4 onClose,
    undefined4 onError,
    undefined2 typeFlag)
```

Ablauf:

1. `hostPort` muss nicht-null und nicht leer sein.
2. `FUN_004e45f0()` liefert den globalen SocketManager.
3. `FUN_00597ba0(hostPort, owner, onConnect, onClose, onError)` oeffnet die eigentliche TCP-Verbindung ueber `AcSocketManager`.
4. Bei Erfolg wird die Adresse in den ConnectManager-Slot kopiert.
5. Wenn noch kein default Socket gesetzt ist, wird `+0x198ac` auf diese Socket-ID gesetzt.
6. `slot.typeFlag` wird auf `param_7` gesetzt.

Damit ist `AgcmConnectManager` nicht selbst der Winsock-Wrapper, sondern eine hoehere Routing-/Session-Schicht ueber `AcSocketManager`.

## Server -> Client: Operation `1`, neue Verbindung anfordern

Empfang in `FUN_006f5780`:

```c
FUN_004e9fb0(layout, 1, packet, packetLen,
             &op, &local_c, &local_4, &local_10, &local_8, &param_4);

if ((char)op == 1) {
    if (local_10 != NULL && local_10[0] != 0) {
        socketId = FUN_006f5530(local_10, 0, 0, 0, 0, 0);
        if (socketId >= 0) {
            strncpy(slot.address, local_10, 0x17);
            FUN_006f5630(local_c, socketId);
            return 1;
        }
    }
}
```

### Bedeutung

Der Server sendet eine ConnectManager-Nachricht mit:

- Operation `1`
- `local_10`: Zieladresse als String, Format sehr wahrscheinlich `IP:PORT` oder `HOST:PORT`
- `local_c`: ein 32-bit Wert, der vom Client in der Antwort wieder zurueckgesendet wird
- weitere Felder `local_4`, `local_8`, `param_4`, hier fuer Op `1` nicht sichtbar genutzt

Der Client oeffnet daraufhin eine neue TCP-Verbindung zu `local_10`.

### Client-Antwort: Operation `2`

`FUN_006f5630(local_c, socketId)` baut:

```c
local_5 = 2;
packet = FUN_004ea280(layout, 1, &packetLen, 0x1b,
                      &local_5, &local_c, 0, 0, 0, 0);
FUN_004e45d0(packet, packetLen, 1, -1, socketIdOrTarget);
```

Die sichtbare Argumentuebergabe ist decompiler-verkuerzt: In `FUN_006f5780` wird `FUN_006f5630(local_c, sVar3)` angezeigt, obwohl die Funktion ein `thiscall` ist. Inhaltlich sendet die Funktion:

- Modul `0x1b`
- Operation `2`
- den vom Server gelieferten Wert `local_c`
- die neu erzeugte Socket-ID `sVar3`

Routing-Parameter bei `FUN_004e45d0`: `param_4 = -1`, letzter Parameter ist der Socket-Kontext. Der dritte Parameter ist `1`, was in der SocketManager-Sendelogik nicht dem normalen Default-Weg entspricht. Wahrscheinlich wird die Antwort ueber den frisch geoeffneten bzw. betreffenden Socket geschickt.

### Interpretation

Dies ist ein klassischer Handoff:

1. Client ist auf Login-/Gateway-Verbindung.
2. Server sagt: "Verbinde dich zu diesem Game-/Channel-Server."
3. Client baut TCP-Verbindung auf.
4. Client meldet per Op `2`: "Neue Verbindung steht, meine Socket-ID ist X, hier ist dein Token/ID-Wert zurueck."

`local_c` ist daher sehr wahrscheinlich ein Server-seitiger Handoff-Identifier, z.B.:

- Session-ID
- Login-Token
- Account-Session-Handle
- Character-/World-Transfer-ID
- Challenge-/Nonce-ID fuer die neue Verbindung

## Server -> Client: Operation `3`, Slot-Metadaten setzen und bestaetigen

Empfang in `FUN_006f5780`:

```c
if ((char)op == 3) {
    *(undefined4 *)(param_5 * 0x20 + 0x134c4 + this) = local_8;
    FUN_006f56b0(local_c, local_4, 0, local_8);
    return 1;
}
```

`param_5` ist im Dispatch sehr wahrscheinlich die aktuelle Socket-ID, weil viele Modul-Handler den Socket als letztes Kontextargument bekommen. Diese Operation setzt fuer den aktuell empfangenden Socket ein 32-bit Metadatum im Slot.

### Client-Antwort: Operation `3`

`FUN_006f56b0(local_c, local_4, 0, local_8)` baut:

```c
local_5 = 3;
packet = FUN_004ea280(layout, 1, &packetLen, 0x1b,
                      &local_5, &local_c, &local_4, 0, &stackArg, 0);
FUN_004e45d0(packet, packetLen, 0, -1, local_8);
```

Sicher sichtbar:

- Modul `0x1b`
- Operation `3`
- Rueckgabe von `local_c`
- Rueckgabe von `local_4`
- Routing ueber einen durch `local_8` bestimmten Socket-/Routenwert

Der Decompiler zeigt in `FUN_006f56b0` noch `&stack0x00000010`; das ist ein Hinweis, dass ein weiteres Feld aus Stackargumenten oder der Calling-Convention nicht sauber rekonstruiert wurde. Die relevante Netzwerkbedeutung bleibt: Op `3` bestaetigt oder bindet die Verbindung mit Serverwerten.

### Interpretation

Operation `3` wirkt wie der zweite Schritt nach dem physischen Connect:

1. Server erkennt die neue Verbindung.
2. Server sendet Op `3` mit Bindungsdaten.
3. Client schreibt `local_8` in `slot.meta`.
4. Client bestaetigt Op `3`.

Moegliche Bedeutung von `slot.meta`:

- GameServer-Session-ID
- Channel-ID
- Character-Transfer-ID
- World-Instance-ID
- eine Routing-ID, die spaeter an `FUN_004e45d0` uebergeben wird

## Server -> Client: Operation `5`, aktiven/default Socket setzen

Empfang in `FUN_006f5780`:

```c
if ((char)op == 5) {
    *(undefined2 *)(this + 0x198ac) = (undefined2)param_5;
    return 1;
}
```

Der Server markiert damit den Socket, auf dem die Op `5` empfangen wurde, als aktiven/default Socket. Danach koennen Sendepfade ohne explizite Socket-ID ueber diesen Socket laufen.

### Bedeutung fuer "wann wird wohin gesendet?"

Vor Op `5` ist der Client in einer Uebergangsphase: mehrere Sockets koennen existieren, aber nicht alle Spielmodule muessen bereits auf den neuen Socket routen. Nach Op `5` zeigt `+0x198ac` auf den aktiven Socket. `AcSocketManager::Send` kann dann Pakete ohne explizites Ziel an diesen Socket senden.

## Zusammenhang mit SocketManager-Sendelogik

`AcSocketManager::Send` (`FUN_006fd8c0`) entscheidet anhand von Parametern, wohin ein Paket geht:

- Wenn kein explizites Ziel angegeben ist, wird der active/default Socket genutzt.
- Wenn ein Socket-Index angegeben ist, wird direkt an diesen Socket gesendet.
- Wenn Verbindungstyp `1` gesucht wird, kann `FUN_006f5740` den ersten passenden Game-/World-Socket liefern.
- Broadcast-artige Wege senden an Sockets mit bestimmtem Verbindungstyp.

Damit entsteht folgende Netzwerkschichtung:

| Schicht | Aufgabe |
|---|---|
| `AcClientSocket` | TCP-Socket, async Winsock, Send-/Recv-Puffer, optional Transform/Encryption |
| `AcSocketManager` | Socket-Pool, `host:port`-Parsing, Connect, Send-Routing |
| `AgcmConnectManager` | servergesteuerter Handoff, Slot-Metadaten, aktiver Socket |
| Spielmodule | Login, Character, World, Item, Combat usw.; senden ueber `FUN_004e45d0` |

## Externe Einstiegspunkte in den ConnectManager

### Normaler Login-Connect

`FUN_0065ebc0`:

```c
FUN_006f5530(AgcmLogin + 0xbd4, 1, AgcmLogin,
             LAB_0065e3f0, LAB_0065e430, FUN_0065e450);
```

`AgcmLogin + 0xbd4` enthaelt die Loginserver-Adresse aus `archlord.ini` bzw. Fallback-Konfiguration. Dieser Connect ist Typ `1`.

### Servergesteuerter Handoff

`FUN_006f5780`, Op `1`:

```c
FUN_006f5530(local_10, 0, 0, 0, 0, 0);
```

Dieser Connect verwendet keine Modul-Callbacks und Typ `0`. Die anschliessende Bindung erfolgt durch ConnectManager-Pakete selbst.

### Return-to-login / Rueckkehrpfad

`FUN_006da720`:

```c
if (hostPort missing) hostPort = AgcmLogin + 0xbd4;
FUN_006f5530(hostPort, 1, AgcmReturnToLogin, LAB_006da660, 0, 0);
```

Dieser Pfad speichert vorher `param_2` in `AgcmReturnToLogin + 0xbac` und nutzt spaeter `FUN_006da680`, um ein Return/Login-Paket ueber den ersten Slot vom Typ `1` zu senden:

```c
socketId = FUN_006f5740();
FUN_004e45d0(packet, len, 2, -1, socketId);
```

Das bestaetigt, dass Typ `1` fuer einen wichtigen Login/Game-Uebergangssocket steht.

### Weiterer Connect-Pfad

`FUN_005a3d50` ruft:

```c
FUN_006f5530(param_3, 0, param_1, LAB_005a1a80, LAB_005a1ab0, LAB_005a1ad0);
```

Dieser Pfad wird aus Login-Hilfsfunktionen erreicht, unter anderem nachdem verschachtelte Login-Daten ausgewertet wurden. Sehr wahrscheinlich ist das ein weiterer Game-/Zone-/Character-Server-Connect.

## Zeitlicher Ablauf

Der wahrscheinliche Ablauf nach erfolgreichem Login:

1. Client verbindet zu Loginserver aus `archlord.ini`.
2. StartupEncryption laeuft auf diesem Socket.
3. Client sendet Login-/Version-/ResourceInfo-Daten.
4. Loginserver authentifiziert Account/Passwort und liefert Session-/Charakter-/Serverdaten.
5. Server sendet ueber `AgcmConnectManager` Op `1` mit Ziel `host:port`.
6. Client verbindet zu diesem Ziel.
7. Client sendet ConnectManager Op `2` als "neuer Socket erstellt"-Bestaetigung.
8. Server sendet ConnectManager Op `3` mit Bindungs-/Routenmetadaten.
9. Client schreibt diese Metadaten in den Socket-Slot und antwortet ebenfalls mit Op `3`.
10. Server sendet ggf. ConnectManager Op `5`.
11. Client setzt den empfangenden Socket als active/default Socket.
12. Spielmodule senden danach World-, Character-, Inventory-, Movement- und weitere Pakete ueber den neuen Socket.

## Was wird an welchen Server gesendet?

### Loginserver

Quelle der Zieladresse:

- `archlord.ini`, entschluesselt mit Key `1111`
- dokumentierter Inhalt:
  - `211.43.159.147:11002`
  - `211.43.159.146:11002`

Typische Sendungen:

- StartupEncryption Op `0`
- StartupEncryption Op `2` mit transformierter Zufallsantwort
- Login Op `0`/ResourceInfo oder Version
- Login Op `1` mit Account/Passwort
- weitere Login-Operationen fuer Serverliste, Charakterliste, Character-Auswahl, Rename/Promotion usw.

### Game-/Channel-/Worldserver

Quelle der Zieladresse:

- nicht aus lokaler INI, sondern vom Server per ConnectManager Op `1`
- Feld `local_10`, String max. `0x17` Bytes

Typische Sendungen:

- ConnectManager Op `2`: Handoff-/Socket-Bestaetigung
- ConnectManager Op `3`: Bindungs-/Metadaten-Bestaetigung
- StartupEncryption kann auch auf neuer Verbindung laufen, falls Transform global aktiv ist
- Danach Spielmodule wie [`AgpmCharacter`](../Module/AgpmCharacter.md), [`AgpmWorld`](../Module/AgpmWorld.md), [`AgpmItem`](../Module/AgpmItem.md), [`AgpmSkill`](../Module/AgpmSkill.md), Movement, Chat usw.

## Server-Datenbank: belastbare Ableitungen

Aus dem Handoff lassen sich mehrere serverseitige Tabellen/Strukturen ableiten. Das sind keine gefundenen SQL-Schemas, sondern aus Clientverhalten begruendete Strukturen.

### `accounts`

Muss existieren, weil der Client Accountname und Passwort an Login Op `1` sendet.

Wahrscheinliche Felder:

| Feld | Grund |
|---|---|
| `account_id` | Account-Identitaet fuer Session/Characters |
| `login_name` | Client sendet Account-String, lowercased gespeichert |
| `password_hash` | Server prueft Passwort; Client sendet Klartext/verschleiert im Paket, DB sollte Hash halten |
| `status` / `blocked_until` | UI-Strings: `LoginAccountBlocked` |
| `last_login_at` | Sessionverwaltung |

### `login_sessions`

Noetig fuer den Uebergang Loginserver -> Game-/Worldserver.

Wahrscheinliche Felder:

| Feld | Grund |
|---|---|
| `session_id` | Kandidat fuer `local_c` |
| `account_id` | Bindung an Account |
| `login_socket_id` | Serverinterner Socket-Kontext |
| `created_at` / `expires_at` | Handoff muss zeitlich begrenzt sein |
| `client_seed_state` | StartupEncryption/Transform-Zustand |

### `server_routes` / `game_server_routes`

Noetig, weil der Server dem Client dynamisch `host:port` schickt.

Wahrscheinliche Felder:

| Feld | Grund |
|---|---|
| `route_id` | Kandidat fuer `local_8` oder `local_c` |
| `host` | Teil von `local_10` |
| `port` | Teil von `local_10` |
| `server_group` | INI enthaelt `GroupName Europe` |
| `channel_id` | MMO-typischer Channel/Shard |
| `world_id` | Ziel-Welt oder Zone |
| `is_active` | Loginserver muss nur gueltige Ziele senden |

### `handoff_tokens`

Sehr wahrscheinlich, weil der Loginserver einen neuen Socket auf einem anderen Server autorisieren muss.

Wahrscheinliche Felder:

| Feld | Grund |
|---|---|
| `token_id` | Kandidat fuer `local_c` |
| `account_id` | Token gehoert zu Account |
| `character_id` | falls Handoff nach Charakterwahl erfolgt |
| `target_server_id` | passt zu gesendeter `host:port` |
| `issued_at` / `expires_at` | verhindert Wiederverwendung |
| `consumed_at` | GameServer markiert Token als benutzt |

### `socket_session_map`

Serverintern noetig, um Op `3`/Op `5` und spaetere Spielmodule einem Account/Character zuzuordnen.

Wahrscheinliche Felder:

| Feld | Grund |
|---|---|
| `server_socket_id` | eigener Socket-Kontext |
| `client_socket_index` | Client meldet Socket-ID in Op `2` |
| `account_id` | Authentifizierter Account |
| `character_id` | nach Charakterauswahl |
| `route_meta` | Kandidat fuer `local_8` |
| `state` | pending, encrypted, bound, active, closed |

### `characters`

Aus Login-Sequenz und UI-Strings ableitbar.

Wahrscheinliche Felder:

| Feld | Grund |
|---|---|
| `character_id` | Charakterlisten/Selection brauchen stabile ID |
| `account_id` | Charakter gehoert Account |
| `name` | UI-Slots zeigen CharName; Rename-Pfade existieren |
| `level` | UI-Slot `Level` |
| `exp` | UI-Slot `Exp` |
| `guild_id` | UI-Slot `Guild`; Delete-Master-Fehler |
| `villain_points` | UI-Slot `Villian` |
| `last_world_id` / `position` | Eintritt in Welt/Return |
| `delete_pending_until` | UI-String `LoginCantDelete1Day` |

## Unsicherheiten und naechste Pruefpunkte

- `local_c`, `local_4` und `local_8` brauchen weitere Rueckverfolgung ueber Serverantworten und Call-Kontexte. Aktuell ist nur die Nutzung sicher, nicht der originale Feldname.
- `FUN_006f5630` und `FUN_006f56b0` sind wegen `thiscall` im Decompiler verkuerzt dargestellt. Die Paketoperationen sind sicher, aber einzelne sichtbare Argumentnamen koennen verschoben sein.
- Es muss noch geprueft werden, welche Module direkt nach ConnectManager Op `5` senden. Das klaert, ob der aktive Socket sofort World-/Character-Daten bekommt.
- Runtime-Mitschnitt waere fuer echte Zielserver heute wahrscheinlich nicht moeglich oder nicht sinnvoll, aber eine lokale Serveremulation koennte die Client-Paketfolge bestaetigen.

## Relevante Funktionen

| Funktion | Adresse | Rolle |
|---|---:|---|
| `FUN_006f53f0` | `0x006f53f0` | Konstruktor, Modul-ID `0x1b`, Layout, Slot-Tabelle |
| `FUN_006f5530` | `0x006f5530` | zentrale Connect-Funktion ueber `AcSocketManager` |
| `FUN_006f55d0` | `0x006f55d0` | Slot loeschen und Socket schliessen |
| `FUN_006f5630` | `0x006f5630` | Client sendet ConnectManager Op `2` |
| `FUN_006f56b0` | `0x006f56b0` | Client sendet ConnectManager Op `3` |
| `FUN_006f5740` | `0x006f5740` | ersten Slot mit Typ `1` suchen |
| `FUN_006f5780` | `0x006f5780` | Serverpakete Op `1`, `3`, `5` verarbeiten |
| `FUN_0065ebc0` | `0x0065ebc0` | Loginserver-Verbindung starten |
| `FUN_006da720` | `0x006da720` | Return-to-login-Verbindung |
| `FUN_005a3d50` | `0x005a3d50` | weiterer Connect-Pfad aus Login-Kontext |
