# Winsock Sequenz 01: Login, StartupEncryption und Server-Handoff

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Ziel dieser Datei: den ersten Netzwerkabschnitt des Clients so konkret wie moeglich festhalten: was wird wann, warum und wohin gesendet. Alle Angaben stammen aus statischer Analyse von `alefclient.pseudocode.c`, `imports.txt` und der dekodierten `archlord.ini`.

## Beteiligte Server

Aus `C:\Spiele\Archlord\archlord.ini`, entschluesselt mit Key `1111`:

| Zweck | Adresse |
|---|---|
| Loginserver Europe 1 | `211.43.159.147:11002` |
| Loginserver Europe 2 | `211.43.159.146:11002` |
| Patchserver | `patch.archlord.webzen.net:11000` |

Die Loginserver werden als XML gelesen:

```xml
<ArchlordInfo>
  <ServerGroup>
    <GroupName>Europe</GroupName>
    <IP>211.43.159.147:11002</IP>
    <IP>211.43.159.146:11002</IP>
  </ServerGroup>
</ArchlordInfo>
```

Der Parser liegt bei `FUN_007b3620` (`0x007b3620`) und sucht `ArchlordInfo`, `ServerGroup`, `GroupName`, `IP` sowie `PatchServerInfo`.

## Sequenzuebersicht

| Schritt | Ausloeser | Richtung | Funktion(en) | Was passiert |
|---:|---|---|---|---|
| 1 | Clientstart/Login-UI | Datei -> Client | `FUN_007b3620` | `archlord.ini` wird geparst, Servergruppe/Server-IP-Liste wird aufgebaut |
| 2 | User klickt Login oder Autologin | UI/Config -> Client | `FUN_0065d7e0` | Account wird lower-case gespeichert, Passwort wird gespeichert |
| 3 | Serverauswahl/Login startet | Client intern | `FUN_00743210`, `FUN_00743160`, `FUN_0065ebc0` | Zielserver wird bestimmt, UI geht auf `LOGIN_WAITING` |
| 4 | TCP-Connect | Client -> Loginserver | `FUN_006f5530`, `FUN_006fd760`, `FUN_00707160`, `FUN_00706bd0` | TCP-Socket wird erstellt und `connect()` auf `host:port` ausgefuehrt |
| 5 | Socket connected | OS -> Client | `FUN_00706a70` | Socket-State wird `3`, Connect-Callback startet Folgefluss |
| 6 | Optionaler Encryption-Start | Client -> Loginserver | `FUN_00681800`, `FUN_0056cf80` | [`AgpmStartupEncryption`](../Module/AgpmStartupEncryption.md), Opcode `0x48`, Operation `0` |
| 7 | Server sendet Key/Seed | Loginserver -> Client | `FUN_006819c0` | Datenblock wird in lokalen Transformkontext eingearbeitet |
| 8 | Client sendet Antwortblock | Client -> Loginserver | `FUN_006819c0`, `FUN_006818b0` | `AgpmStartupEncryption`, Opcode `0x48`, Operation `2`, transformierte Zufallsdaten |
| 9 | Transform aktiv | Client intern | `FUN_00681b30` | `socket + 0xc807c = 2`; weitere Pakete werden mit `0xB1..0xBF` gewrappt |
| 10 | Login-Credentials | Client -> Loginserver | `FUN_0065ec80` | Opcode `0x0d`, Operation `1`, Account, Passwort |
| 11 | Loginantwort | Loginserver -> Client | `FUN_0065e7f0` | Status, Sessiondaten, Charakter-/Serverdaten oder Fehler |
| 12 | Handoff falls notwendig | Loginserver -> Client -> Gameserver | `FUN_006f5780` | Server kann neues `host:port` senden; Client verbindet weiteren Socket |

## Schritt 1: Serverliste aus Archlord.ini

`FUN_007b3620` liest eine XML-Struktur. Relevante Tags:

- `ArchlordInfo`
- `ServerGroup`
- `GroupName`
- `IP`
- `PatchServerInfo`

Jede Servergruppe bekommt einen Namen und mehrere IP-Strings. Die IP-Strings sind bereits im Format `host:port`, passend fuer `AcSocketManager::Connect`.

Wenn keine `Archlord.ini`/`Archlordtest.ini` gefunden wird, benutzt `FUN_0065eaf0` die Configwerte:

- `LoginServerIP`
- `LoginServerPort`

und schreibt `"%s:%d"` nach `AgcmLogin + 0xbd4`.

## Schritt 2: Account und Passwort werden vorbereitet

`FUN_0065d7e0`:

```text
memset(AgcmLogin + 0xc4c, 0, 0x40)
memset(AgcmLogin + 0xc8c, 0, 0x40)
account = lower(account)
copy account -> AgcmLogin + 0xc4c
copy password -> AgcmLogin + 0xc8c
```

Quellen:

- Manuelles Login: `LG_IdPasswordOK` ist an `FUN_00749a20` gebunden und bekommt `ID_EDIT` sowie `PASSWORD_EDIT`.
- Autologin-Pfade lesen `member_id`, `autopwd` oder `autologin` und rufen ebenfalls `FUN_0065d7e0`.

Wichtig: Die Zugangsdaten werden nicht sofort bei Eingabe gesendet. Sie werden zuerst in [`AgcmLogin`](../Module/AgcmLogin.md) gepuffert.

## Schritt 3: Serverauswahl und Connect

`FUN_00743210` entscheidet:

- keine Serverliste: direkt `AgcmLogin::Connect` (`FUN_0065ebc0`);
- genau ein Server: `FUN_00743160`;
- mehrere Server: Serverauswahl-UI oeffnen.

`FUN_00743160`:

1. holt die Servergruppe;
2. waehlt zufaellig einen IP-Eintrag aus der Gruppe;
3. ruft `FUN_0065ec40(serverString)`;
4. setzt UI auf `LOGIN_WAITING`.

`FUN_0065ec40`:

```text
AgcmLogin + 0xbd4 = serverString
FUN_0065ebc0()
```

`FUN_0065ebc0`:

- falls bereits verbunden (`+0xc18 != 0`), wird nur Event `2` ausgeloest und der gespeicherte Socket `+0xc3c` zurueckgegeben;
- sonst:
  - `FUN_0065eaf0` stellt sicher, dass Zielserver vorhanden ist;
  - `+0xda8` bekommt Timestamp;
  - `+0xdac = 1` aktiviert Timeout/Waiting;
  - `FUN_006f5530(AgcmLogin + 0xbd4, 1, AgcmLogin, onConnect, onClose, onError)` verbindet.

## Schritt 4: TCP-Socket-Aufbau

`FUN_006fd760` ist `AcSocketManager::Connect`:

```text
finde freien socket slot
splitte "host:port"
atoi(port)
AcClientSocket::Reset()
AcClientSocket::CreateSocket()
AcClientSocket::SetCallbacks(context,onConnect,onClose,onError)
AcClientSocket::Connect(host,port)
speichere Zielstring
speichere Verbindungstyp
```

`FUN_00707160`:

```c
socket(AF_INET, SOCK_STREAM, 0);
WSAAsyncSelect(socket, hwnd, 0x600, 0x3b);
state = 1;
```

`FUN_00706bd0`:

```c
sockaddr.sa_family = AF_INET;
addr = inet_addr(host);
if invalid: addr = inet_addr(gethostbyname(host));
port = htons(port);
connect(socket, sockaddr, 0x10);
```

`WSAEWOULDBLOCK` (`0x2733`) wird als normaler Async-Zustand akzeptiert. Andere Fehler werden nach `LOG\_ALEF_ERROR_.log` geschrieben.

## Schritt 5: Connected-Callback

`FUN_00706a70`:

```text
socket state = 3
if onConnect != null:
    onConnect(socket, context, 0)
```

Beim Loginconnect wurde als Context `AgcmLogin` uebergeben. Die konkreten Callback-Labels sind im Pseudocode teilweise nur als `LAB_0065e3f0`/`LAB_0065e430` sichtbar. Die Folgefunktionen zeigen aber, was passiert:

- wenn StartupEncryption aktiv ist: `FUN_00681800(socketId)` sendet Encryption-Start;
- wenn nicht aktiv: direkt `FUN_0065d840()` als erster Login-Folge-Request.

## Schritt 6-9: StartupEncryption

### Modul

`AgpmStartupEncryption`:

- Modul-ID/Opcode: `0x48`
- Layout:

```text
mask=1:
1,1,      // Operation
0xd,1     // length-prefixed Datenblock
```

### Client -> Server: Operation 0

`FUN_00681800(socketId)`:

1. holt Socket ueber `FUN_006fda40(socketId)`;
2. baut `AgpmStartupEncryption`-Paket mit `FUN_0056cf80(&len, op=0, data=0, dataLen=0)`;
3. sendet ueber `FUN_004e45d0(packet, len, socketConnectionType, -1, socketId)`.

Paket vor optionalem Wrapper:

```text
Clearframe:
  marker: 0xD6 ... 0x6B
  opcode: 0x48
  operation: 0
  kein Datenblock
```

Warum: Startet den Schluessel-/Transform-Handshake.

### Server -> Client: Seed/Keydaten

`FUN_006819c0(param_1, param_2, param_3)`:

- `param_3[0]` ist Socket-ID;
- `param_1[0]` und `*(short*)param_1[1]` liefern Datenpointer und Datenlaenge;
- der Socket wird geholt;
- der Transformkontext `socket + 0xc8078` wird mit dem Serverdatenblock initialisiert.

Kern:

```text
socket = FUN_006fda40(socketId)
ctx = socket + 0xc8078
FUN_004f96b0(ctx, serverData, serverLen, flag)
```

Warum: Server liefert Material, mit dem der Client seinen pro-Socket Transform-/Cryptozustand aufbaut.

### Client -> Server: Operation 2 mit Antwortdaten

Im selben Handler erzeugt der Client Zufallsdaten:

```text
len = globalTransformContext + 0x24
random[len] = FUN_007e3340(0xff)
FUN_004f9720(ctx, random, len, flag)
out = FUN_004f9790(ctx, random, len)
FUN_006818b0(out, outLen, socketId)
```

`FUN_006818b0` baut:

```text
opcode 0x48
operation 2
length-prefixed Datenblock
```

Warum: Client antwortet auf die Server-Challenge bzw. bestaetigt den Transformzustand.

### Live-verifiziert (2026-09-05, gegen echten Client via `AlefLogin`)

Erstmals wurde dieser Ablauf gegen den echten Client getestet (eigener Loginserver-Nachbau
in `AlefLogin/`, siehe dort). Ergebnis: **Schritte 6-8 sind jetzt empirisch bestaetigt**,
nicht mehr nur statische Inferenz.

**Reale Kommandozeilenfelder fuer `AgpmStartupEncryption` (Opcode `0x48`), aus
`FUN_004ea280` (dem generischen Feld-Serialisierer, den sich alle `Agpm*`/`Agcm*`-Module
teilen) direkt gelesen statt geraten:**

- Die Maske ist eine echte Bitmaske, ein Bit pro deklariertem Feldslot in Modulreihenfolge:
  Slot 0 (`Operation`, Typ `1`) = Bit `0x01`, Slot 1 (Datenblock, Typ `0xd`) = Bit `0x02`.
  Eine Nachricht mit nur `Operation` hat also Maske `0x01`; mit `Operation` + Datenblock
  Maske `0x03`.
- Ein `0xd`-Feld (laengenpraefigierter Datenblock) hat einen **2-Byte**-Laengenpraefix
  (Little Endian), nicht 1 Byte.
- Die tatsaechlichen Operationsnummern der StartupEncryption-Handler wurden ueber
  `FUN_004e41d0(N, handler, module)` in den fuenf Registrierungs-Wrapperfunktionen
  gefunden (nicht die vorher angenommene Registrierungsreihenfolge 0..4!):

  | Handler | Bedeutung | Registrierungswrapper | Operationsnummer `N` |
  |---|---|---|---:|
  | `FUN_006819c0` | Seed-Austausch (dieser Abschnitt) | `FUN_006dd1e0` | **1** |
  | `FUN_00681b30` | Transform aktivieren | `FUN_005781f0` | **3** |
  | `FUN_00681be0` | toter Code (Encode-Key direkt) | `FUN_0058ee20` | **5** |
  | `FUN_00681970` | Cipher-ID setzen (siehe [`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](Transform-Cipher.md)) | `FUN_0065e490` | **7** |

  (`FUN_00681c70`, der zweite tote Handler, wurde noch nicht auf seine Nummer geprueft,
  vermutlich `9` nach dem erkennbaren Muster ungerader Zahlen ab 1.)

**Getesteter Ablauf:**

1. Client verbindet, sendet automatisch (nicht optional!) sein `AgpmStartupEncryption`
   Operation `0` - bestaetigt bytegenau:

   ```text
   d6 10 00 48 00 00 00 00 00 00 00 00 00 01 00 6b
   ```

   (Marker, Laenge=16, Opcode `0x48`, 9-Byte-Header noch unbekannter Bedeutung (hier `0`),
   Maske `0x01`, Operation `0`, Ende-Marker.)

2. Server antwortet mit Operation `1` (Seed-Austausch-Trigger) und einem **frei erfundenen**
   16-Byte-"Seed" (`AlefLoginSeed001`, keine echten kryptographischen Daten):

   ```text
   d6 22 00 48 [9x00] 03 01 10 00 41 6c 65 66 4c 6f 67 69 6e 53 65 65 64 30 30 31 6b
   ```

   Maske `0x03` (Operation + Datenblock), Operation `1`, 2-Byte-Laenge `0x0010`=16, dann die
   16 Byte, dann Ende-Marker.

3. **Client akzeptiert das und antwortet** mit Operation `2` und einem 32-Byte
   verschluesselten Datenblock - exakt das in diesem Abschnitt dokumentierte Verhalten:

   ```text
   d6 32 00 48 [9x00] 03 02 20 00 [32 Byte Chiffretext] 6b
   ```

   Bemerkenswert: 32 Byte Antwort auf 16 Byte Seed - der Zusammenhang zwischen
   Seed-/Eingabelaenge und der vom Client generierten Zufallsdaten-Laenge (ueber
   `FUN_004f97d0(2,...)`, siehe [`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](Transform-Cipher.md)) ist noch nicht
   erklaert; haengt vermutlich vom aktuell aktiven Cipher ab, dessen ID wir in diesem Test
   nie explizit gesetzt haben (kein Operation-`7`-Paket gesendet), der Client nutzt also
   einen client-seitigen Default.

**Was das beweist:** Der komplette in diesem Abschnitt beschriebene Ablauf (Client startet
automatisch, Server liefert "Seed" beliebigen Inhalts, Client antwortet mit verschluesseltem
Zufallsblock) funktioniert tatsaechlich so gegen den echten Client - unabhaengig davon, dass
der gesendete "Seed" komplett unecht war. Das bestaetigt sowohl das Rahmenformat
(`0xD6...0x6B`, Laengenfeld = Gesamtlaenge, 9-Byte-Header, Bitmaske, 2-Byte-Laengenpraefixe)
als auch die Wahl der Operationsnummern.

**Noch offen:** ob/wie der Client reagiert, wenn der Server als naechstes Operation `3`
(Transform aktivieren) sendet, und ob danach echte Zugangsdaten (Opcode `0x0d`) folgen -
wird im laufenden `AlefLogin`-Experiment weiterverfolgt.

### Transform aktivieren

`FUN_00681b30`:

```text
socket = FUN_006fda40(socketId)
socket + 0xc807c = 2
```

Danach verpackt `AcClientSocket::Send` ausgehende Pakete in den Wrapper:

```text
0xB1 | uint16 wrapperLen | uint32 sequence | transformedPayload | 0xBF
```

Eingehend akzeptiert der Parser beide Wrapperarten:

```text
0xA1 ... 0xAF
0xB1 ... 0xBF
```

## Schritt 10: Credential-Loginpacket

Der eigentliche Login mit Account/Passwort wird in `FUN_0065ec80` gebaut.

Ausloeser:

- `FUN_0060b680` ruft:

```text
FUN_0065ec80(AgcmLogin + 0xc4c,
             AgcmLogin + 0xc8c,
             *(ushort *)(AgcmLogin + 0xc3c))
```

Gesendete Daten:

| Feld | Quelle | Max/Buffer | Bemerkung |
|---|---|---:|---|
| Operation | lokal | 1 Byte | Wert `1` |
| Account | `AgcmLogin + 0xc4c` | `0x31` Bytes | vorher lower-case |
| Account-Length | berechnet | 1 Byte | Laenge des Accountstrings |
| Passwort | `AgcmLogin + 0xc8c` | `0x21` Bytes | Klartext im Clientpuffer vor Pakettransform |
| Passwort-Length | berechnet | 1 Byte | Laenge des Passwortstrings |

Paket:

```text
opcode: 0x0d
operation: 1
route: socket id aus AgcmLogin + 0xc3c
```

Wenn `socket + 0xc807c == 2`, wird dieser Clearframe vor `send()` transformiert und als `0xB1..0xBF` gesendet. Ohne StartupEncryption geht er als `0xD6..0x6B` raus.

Wichtig: In der Funktion werden `autologin` und `gamestring` gelesen. Im sichtbaren dekompilierten `FUN_004ea280`-Call werden sie aber nicht eindeutig als Feld uebergeben. Das ist wahrscheinlich ein Decompiler-/Branch-Artefakt oder ein optionaler Pfad, der noch dynamisch geprueft werden muss.

## Schritt 11: Loginserver-Antworten auf Opcode 0x0d

`FUN_0065e7f0` ist der zentrale `AgcmLogin`-Receivehandler. Er deserialisiert das Paket und schaltet auf `local_35`, also das erste Operationsbyte.

| Server-Op | Clientreaktion | Bedeutung/Inferenz |
|---:|---|---|
| `0` | kopiert 8 DWORDs nach `AgcmLogin + 0xbb4`; Event `2` | Login-Erfolg / Sessiondaten |
| `1` | speichert zwei DWORDs nach `+0xc44/+0xc48`; Event `4` mit Socket-ID | Server-/Charakterlistenstatus oder Wechsel in naechste Loginphase |
| `2` | Event `0x0f` mit `local_1c` | Fehler-/Statuscode |
| `3` | `FUN_0065d4e0(local_34)` | nested Daten werden deserialisiert; Event `5` |
| `4` | `FUN_0065d550(local_34, 0)` | nested Daten; speichert `+0xc40`; Event `6` |
| `5` | Event `7` mit `local_30` und Socket-ID | wahrscheinlich Char-/Serverlisten-Aktion |
| `7` | Event `8`, setzt `+0xda4 = 0` | beendet laufenden Counter/Request; gibt zwei Werte weiter |
| `8` | Event `9`, danach `FUN_0065d610(local_2c, local_34, local_18)` | liest zwei Nested-Pakete und kann neuen Connect via `FUN_005a3d50` starten |
| `10` | Event `10` | Status/Phase |
| `0x0b` | `FUN_0065d550(local_34, 1)` | wie Op 4, aber Event `0x0b` |
| `0x0c` | Event `0x0c` | Status/Fehler |
| `0x0d` | `FUN_0065d6d0(local_34)` | nested Daten, Event `0x0d`, fuegt/aktiviert Characterdaten |
| `0x0f` | `FUN_0065d770(local_34, local_14, socketId)` | nested Daten, Event `0x0e` |
| `0x11` | `FUN_0065e6e0(local_30, local_34)` | liest mehrere Strings/Bloecke aus Nested-Paket; Event `0x10` |
| `0x20` | Event `3` | Disconnect/Return/Fehlerphase |

## Login-Folgepakete Client -> Server

Diese Funktionen senden weitere Opcode-`0x0d`-Pakete nach Login/Charakterauswahl. Viele werden durch UI-Events oder Serverantworten getriggert.

| Funktion | Operation | Sendet | Ausloeser/Hinweis |
|---|---:|---|---|
| `FUN_0065d840` | `0` | Nested-Paket aus zwei ResourceInfo-Werten (`FUN_00568930`, `FUN_00568940`) | direkt nach Connect/StartupEncryption; wahrscheinlich Clientversion/Resource-Handshake |
| `FUN_0065ec80` | `1` | Account + Passwort | Loginbutton/Autologin |
| `FUN_0065d950` | `2` | kurzer String `< 0x11` | wahrscheinlich Charakter-/Serverauswahl oder Rename-Token |
| `FUN_0065da30` | unklar/dekompiliert | ein Wert plus Datenblock aus `+0xc1c`/Parameter | von ReturnToLogin und UI-Fluss benutzt |
| `FUN_0065dad0` | unklar/dekompiliert | aehnlich `FUN_0065da30` | UI-Fluss bei Charakter-/Serverstatus |
| `FUN_0065db90` | unklar/dekompiliert | Account + nested Datenpaket (`+0x25dac`) | `FUN_0065e580`; vermutlich Charakterauswahl mit Name |
| `FUN_0065dcb0` | `9` | Datenpointer/String | UI-State `c14=3`; vermutlich Delete/Back/Slot-Aktion |
| `FUN_0065dd80` | `10` | nested Datenpaket | UI-State 6/7; bei `param_1 + 0x1180 == 1/2` mit Wert 1 oder 2 |
| `FUN_0065de70` | `0x0b` | komplexes Nested-Paket | weitere Login-/Charakteraktion |
| `FUN_0065dfa0` | `0x15` | komplexes Nested-Paket, nutzt gespeicherte Daten `+0xd14/+0xd18/+0xd1c/+0xd20` | `JumpingPromotion`/Bestaetigungsfluss |
| `FUN_0065e0d0` | unklar/dekompiliert | nested Daten + Nutzdatenargumente | Login-Unteraktion |
| `FUN_0065e1f0` | unklar/dekompiliert | nested Daten + mehrere Parameter | wird von `FUN_0065e650` bei gueltigem Charakter/String benutzt |
| `FUN_0065e2f0` | `0x12` oder `0x13` | nested Daten | Operation abhaengig von `param_5 == 0` |

## UI-Zustaende, die mit Loginantworten zusammenhaengen

`AgcmLogin + 0xc14` ist ein Login-UI-/State-Wert. Sichtbare Zustandswechsel:

| State | Sichtbare Verwendung |
|---:|---|
| `3` | Charakter-/Loginansicht wird aufgebaut, Guilddaten reset, `FUN_0065dcb0` kann gesendet werden |
| `4` | Ruecksprung/Charakterauswahl, Map/Camera/Nature werden vorbereitet |
| `5` | Waiting/Transition nach Auswahl oder Promotion |
| `6` | Eintrittsvorbereitung; kann `FUN_0065dd80(..., 1)` senden |
| `7` | Charakterauswahl/Detailansicht; kann `FUN_0065dd80(..., 2)` senden |
| `9` | Resource-/PointLight-/World-Ladephase |
| `10` | Spezialphase; `FUN_0060ee30` setzt danach Loginstatus zurueck |

UI-Strings bestaetigen folgende fachliche Loginbereiche:

- `Login01SlotCharName`, `Login01SlotCharLevel`, `Login01SlotCharExp`, `Login01SlotCharGuild`, `Login01SlotCharVillian`
- entsprechende Slots `02` und `03`
- `LoginGameServerName`
- `LoginAccountBlocked`
- `LoginCantDelete1Day`
- `GuildBattleMember_NotEraseMaster`
- `LoginRename`
- `ConnRename`
- `JumpingPromotion`
- `DisconnectedByServer`

## Schritt 12: Server-Handoff

Wenn der Loginserver oder ein bereits verbundener Server ein [`AgcmConnectManager`](../Module/AgcmConnectManager.md)-Paket sendet:

Opcode `0x1b`, Operation `1`:

```text
Server -> Client:
  op = 1
  local_c = vermutlich Verbindungs-/Session-ID
  local_10 = host:port

Client:
  FUN_006f5530(local_10, connectionType=0, callbacks=0)
  speichert local_10 im neuen Socket-Slot
  sendet FUN_006f5630(local_c, newSocketId)
```

Das Rueckpaket `FUN_006f5630`:

```text
opcode 0x1b
operation 2
payload: local_c, newSocketId
route: connectionType 1 / socket routing -1
```

Opcode `0x1b`, Operation `3`:

```text
Client speichert local_8 in socketSlot-Metadaten
Client sendet operation 3 zurueck
```

Opcode `0x1b`, Operation `5`:

```text
AgcmConnectManager + 0x198ac = aktueller Socket
```

Inferenz: Der Loginserver teilt einen Gameserver-/Channel-Endpunkt mit. Der Client verbindet einen zweiten Socket und bestaetigt dem Server die neue Socket-ID/Session.

## Datenbank-Inferenzen aus Sequenz 01

Diese Tabellen/Entitaeten sind aus dem ersten Ablauf ableitbar:

| Serverentitaet | Warum plausibel |
|---|---|
| `accounts` | Loginpacket sendet Account + Passwort; Server antwortet mit Block-/Fehlerstatus |
| `login_sessions` | Server liefert 8 DWORDs bei Op `0`; StartupEncryption/ConnectManager brauchen pro-Socket/session Zustand |
| `server_groups` | `ArchlordInfo` enthaelt Gruppenname und mehrere IPs |
| `game_servers` / `channels` | `AgcmConnectManager` kann `host:port` fuer weiteren Socket senden |
| `character_slots` | UI hat 3 Slots mit Name/Level/EXP/Guild/Villain |
| `characters` | Folgepakete behandeln Auswahl, Delete, Rename, Eintritt |
| `character_login_state` | Serverantworten treiben Loginstates `3..10` und Eintritts-/Wartephasen |
| `account_entitlements` | `JumpingPromotion`, BetaKey-/Blockmeldungen, Billing/Cash-Module im Client |

Nicht sicher bestimmbar:

- echte SQL-Tabellennamen;
- Passwort-Hashing;
- genaue Spaltennamen;
- ob Login- und Gameserver dieselbe Datenbank nutzen;
- ob die 8 DWORDs Sessionkey, Account-ID, User-ID, Billingflags oder Mix daraus sind.

## Transform-Cipher-Suite (Schritte 6-9)

Der in Schritt 6-9 nur als Blackbox beschriebene Transform-/Verschluesselungsmechanismus
ist mittlerweile per RTTI-Analyse aufgeschluesselt: eine austauschbare Cipher-Suite
(Blowfish/MD5Mac/Rijndael/SEED) hinter einem Singleton `AuCryptManager`. Details, Adressen
und offene Punkte dazu in [WINSOCK_TRANSFORM_CIPHER_SUITE.md](Transform-Cipher.md).

## Naechste konkrete Sequenz

Nach dieser Datei sollte als Sequenz 02 `AgcmConnectManager` + Gameserver-Handoff tiefer zerlegt werden:

- alle `0x1b` Sender/Receiver;
- genaue Feldbelegung des Layouts;
- welche Sockettypen `0` und `1` fachlich bedeuten;
- wann welcher Socket zum Default wird;
- welcher Request direkt nach Gameserver-Connect folgt.
