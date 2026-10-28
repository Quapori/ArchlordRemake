# Winsock-, Netzwerk- und Protokoll-Funde

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei sammelt die statischen Erkenntnisse aus `alefclient.pseudocode.c`, `imports.txt`, den installierten Konfigurationsdateien unter `C:\Spiele\Archlord` und den bisher entschluesselten Daten. Es wurde noch kein Live-Traffic mitgeschnitten; alle Aussagen zu Server-Datenbankstrukturen sind deshalb als Inferenz aus Client-Paketen, Modulnamen und lokalen Datentabellen markiert.

## Fortschritt / Detaildateien

- [`WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md`](Sequenz-01-Login-Handshake.md): Loginserver-Adresse, `AgcmLogin`, StartupEncryption, Credential-Paket, Login-Receive-Operationen.
- [`WINSOCK_SEQUENCE_02_CONNECT_MANAGER_HANDOFF.md`](Sequenz-02-Connect-Manager-Handoff.md): `AgcmConnectManager`, Server-Handoff, dynamische `host:port`-Ziele, Socket-Slots, aktiver/default Socket.
- [`WINSOCK_SEQUENCE_03_WORLD_ENTRY_CHARACTER_WORLD.md`](Sequenz-03-World-Entry-Character-World.md): World-Entry, `AgpmWorld`, `AgpmCharacter`, erste Character-/Movement-/State-Pakete, DB-Ableitungen.
- [`WINSOCK_SEQUENCE_04_CHARACTER_MOVEMENT_STATE.md`](Sequenz-04-Character-Movement-State.md): Movement-Tick, Positionssync, Action-/Target-Nested-Pakete, 64-bit Wertdeltas.
- [`WINSOCK_SEQUENCE_05_ITEM_INVENTORY_EQUIP.md`](Sequenz-05-Item-Inventory-Equip.md): Iteminstanzen, Inventory-/Equip-/Bank-Container, lokale Itemtemplates, Trade-Basis und DB-Ableitungen.
- [`WINSOCK_SEQUENCE_06_SKILL_COMBAT.md`](Sequenz-06-Skill-Combat.md): `AgpmSkill`, `AgcmSkill`, Skill-Cast-Pfad, Skill-Statuspakete, Cooldowns, Combat-Abhaengigkeiten und DB-Ableitungen.
- [`WINSOCK_SEQUENCE_07_CHATTING_CHANNELS.md`](Sequenz-07-Chatting-Channels.md): `AgpmChatting`, Normal-/Party-/Guild-/Whisper-/Area-Chat, Channelverwaltung, Textlimits und DB-Ableitungen.
- [`WINSOCK_SEQUENCE_08_PARTY_GUILD.md`](Sequenz-08-Party-Guild.md): `AgpmParty`, `AgcmParty`, `AgpmGuild`, UI-Aktionen, Party-Ops, Guild-Subsysteme und DB-Ableitungen.
- [`WINSOCK_SEQUENCE_09_PRIVATE_TRADE.md`](Sequenz-09-Private-Trade.md): `AgcmPrivateTrade`, Modul `0x07`, Request/Accept/Reject/MoveItem/UpdateMoney/Lock/Ready, Server-Ops und Trade-DB-Inferenz.
- [`WINSOCK_SEQUENCE_10_AUCTION.md`](Sequenz-10-Auction.md): `AgpmAuction`, `AgcmAuction`, Modul `0x0b`, Auction-Board, Kaufen/Verkaufen/Cancel/Claim, Server-Ops und DB-Inferenz.
- [`WINSOCK_SEQUENCE_11_EVENT_NPC_INTERACTIONS.md`](Sequenz-11-Event-Npc-Interactions.md): `ApmEventManager`, NPCDialog, NPCTrade, Teleport, Eventfunktionen, Conditions und DB-Inferenz.
- [`WINSOCK_SEQUENCE_12_QUEST.md`](Sequenz-12-Quest.md): `AgpmQuest`, `AgpmEventQuest`, `AgcmQuest`, Questflags, AutoStart/AutoEnd, Questmessages und DB-Inferenz.
- [`WINSOCK_SEQUENCE_13_SERVICE_NPCS.md`](Sequenz-13-Service-Npcs.md): Bank, Repair, Refinery, Product/Crafting, SkillMaster, ItemConvert, Event-Module, Kernmodule und DB-Inferenz.
- [`WINSOCK_SEQUENCE_14_SERVICE_NPC_RECEIVE_SWITCHES.md`](Sequenz-14-Service-Npc-Receive-Switches.md): Receive-/Parserseite fuer Service-NPCs und Kernmodule `0x16`, `0x17`, `0x3b`, `0x4b`.
- [`WINSOCK_SEQUENCE_15_BANK_TRANSACTIONS.md`](Sequenz-15-Bank-Transactions.md): Bank-Geldtransfers ueber Character-Modul `0x02`, Bank-Itembewegung und Slotkauf ueber Item-Modul `0x04`.
- [`WINSOCK_SEQUENCE_16_AGPMITEM_OPCODE_MAP.md`](Sequenz-16-Agpmitem-Opcode-Map.md): allgemeiner `AgpmItem`-Receive-Switch, Subops `0..0x20`, Itembuilder, Containerkennungen und Bank-Bezug.
- [`WINSOCK_SEQUENCE_17_LOGIN_WORLD_CHARACTER_SELECTION.md`](Sequenz-17-Login-World-Character-Selection.md): live abgeglichener Uebergang Weltwahl -> Union -> accountweite Charakterliste; belegt die fehlende Op-5-Abschlussmeldung vor Client-Op 6.
- [`WINSOCK_SEQUENCE_18_CHARACTER_ADD_AND_3D_INIT.md`](Sequenz-18-Character-Add-And-3D-Init.md): `AgpmCharacter` Op 0, vollstaendige Referenz-Feldreihenfolge und der verifizierte Pfad bis `RpClumpClone`.
- [`WINSOCK_SEQUENCE_19_AUTO_CONNECT_EVENT_7.md`](Sequenz-19-Auto-Connect-Event-7.md): exakte Ursache und Protokollloesung fuer den nicht automatisch ausgeloesten Connect-Callback nach der Serverauswahl.
- [`WINSOCK_SEQUENCE_20_CHARACTER_SELECT_RPCLUMP_ROOT_CAUSE.md`](Sequenz-20-Character-Select-Rpclump-Root-Cause.md): Live-Nachweis fuer den fehlenden `AgpmCharacter`-Add-Frame nach Login-Op 6; Sendervertrag und vollstaendiger Pfad bis `RpClumpClone`.
- [`WINSOCK_SEQUENCE_21_CHARACTER_SELECT_GAMESERVER_HANDOFF.md`](Sequenz-21-Character-Select-Gameserver-Handoff.md): lokale Auswahl-Gates, Login-Op 8 und der erforderliche Loginserver-zu-Gameserver-Handoff.
- [`WINSOCK_SEQUENCE_22_CHARACTER_CREATE_RACE_CLASS_PREVIEW.md`](Sequenz-22-Character-Create-Race-Class-Preview.md): Op-10-Basischaraktere, erforderlicher Status `IN_GAME_WORLD` und die zehn belegten Vorschau-Template-TIDs.
- [`WINSOCK_SEQUENCE_23_CHARACTER_REFRESH_DUPLICATE_ADD_ROOT_CAUSE.md`](Sequenz-23-Character-Refresh-Duplicate-Add-Root-Cause.md): Ursache fuer inkorrekte Charakteranzeige nach Delete -> Create: Op 5 loest clientseitig Op 6 aus, waehrend der Refresh bereits einen ersten Add-Zyklus gesendet hat.
- [`WINSOCK_SEQUENCE_24_GAMESERVER_BOOTSTRAP_WORLD_ENTRY.md`](Sequenz-24-Gameserver-Bootstrap-World-Entry.md): Gameserver-Socket nach Login-Op 8, Op 2 Sessionbindung, Startposition, clientseitiges Op 9 LoadingComplete und Mindestzustand vor dem Weltbeitritt.
- [`WINSOCK_SEQUENCE_25_FIRST_WORLD_ENTRY_REQUIRED_STATE.md`](Sequenz-25-First-World-Entry-Required-State.md): exakte Reihenfolge nach LoadingComplete: Selbstcharakter-Add/All-Info, Modulzustand, Stadt-NPCs, SettingOK und anschliessende AOI-Sichtbarkeit.
- [`WINSOCK_SEQUENCE_26_WORLD_ENTRY_COORDINATE_SOURCE.md`](Sequenz-26-World-Entry-Coordinate-Source.md): Herkunft, Speicherung, Fallback und Validierung der Startkoordinaten fuer Op 8 CHARACTER_POSITION.
- [`WORLD_NEW_CHARACTER_BINDINGS_FROM_CLIENT.md`](../Welt-und-Engine/Neue-Charakter-Spawnpunkte.md): die vier im installierten Client gefundenen `BindingType=2`-Spawnanker mit Koordinaten, Radius und Rasse.
- [`WINSOCK_SEQUENCE_27_NEW_CHARACTER_START_ITEMS_EQUIPMENT.md`](Sequenz-27-New-Character-Start-Items-Equipment.md): serverseitige Startausstattung, Equip-Slots, erforderliche Gameserver-Itemsynchronisierung und die Grenze der im Client auffindbaren Daten.
- [`WINSOCK_SEQUENCE_28_CHARACTER_SELECT_EQUIPMENT_SEND_PATH.md`](Sequenz-28-Character-Select-Equipment-Send-Path.md): Referenz-Sendepfad von Login Op 6 ueber DB-Itemload, Character-AllInfo-Callback und `AgpmItem`-Adds bis zum Client-Attachment.
- Naechste sinnvolle Sequenzen: exakte AuPacket-Masken fuer Character-Add, [`AgcmConnectManager`](../Module/AgcmConnectManager.md)-Handoff, Guild-Battle/GuildMark-Deep-Dive.

## Kurzfazit

- Der Client nutzt klassischen Winsock-TCP-Code mit `WSAStartup`, `socket(AF_INET, SOCK_STREAM)`, `connect`, `send`, `recv`, `closesocket`, DNS-Aufloesung und `WSAAsyncSelect`.
- Die installierte `C:\Spiele\Archlord\archlord.ini` ist mit dem bekannten Schluessel `1111` entschluesselbar. Sie enthaelt als Loginserver-Ziele:
  - `211.43.159.147:11002`
  - `211.43.159.146:11002`
  - Patchserver: `patch.archlord.webzen.net:11000`
- Die Netzwerkschicht heisst im Client `AcClientSocket` / `AcSocketManager`. Darueber liegen Modulprotokolle wie [`AgcmLogin`](../Module/AgcmLogin.md), `AgcmConnectManager`, [`AgpmCharacter`](../Module/AgpmCharacter.md), [`AgpmItem`](../Module/AgpmItem.md), [`AgpmGuild`](../Module/AgpmGuild.md), `AgpmQuest`, [`AgpmAuction`](../Module/AgpmAuction.md), [`AgpmWorld`](../Module/AgpmWorld.md) usw.
- Cleartext-Netzwerkframes beginnen mit `0xD6`, enthalten bei Offset `+1` eine 16-bit Laenge, bei `+3` die Modul-/Opcode-ID, ab `+0x0d` eine Feldmaske und enden mit `0x6B`.
- Optional werden Frames in einen zweiten Wrapper transformiert: `0xA1 ... 0xAF` oder `0xB1 ... 0xBF`. Darin liegt bei `+3` ein laufender Sequenzzaehler und ab `+7` das transformierte eigentliche Paket.
- Der Server kann dem Client neue Endpunkte mitteilen. `AgcmConnectManager` verarbeitet mindestens Operation `1` als "verbinde zu weiterer Adresse", Operation `3` als Metadaten/Handshake-Antwort und Operation `5` als Auswahl des aktiven Sockets.
- Neben der Haupt-TCP-Schicht gibt es eine separate UDP-Funktion, die ein intern gebautes Paket per `sendto` an Port `15000` sendet. Diese Stelle gehoert wahrscheinlich zu Schutz-/Launcher-/Diagnosecode und ist noch nicht dem Spielprotokoll zugeordnet.

## Zieladressen und Konfiguration

### archlord.ini

Die Datei `C:\Spiele\Archlord\archlord.ini` ist nicht Klartext, aber mit dem allgemeinen Datendatei-Schluessel `1111` lesbar. Dekodierter Inhalt:

```xml
<ArchlordInfo>
    <ServerGroup>
        <GroupName>Europe</GroupName>
        <IP>211.43.159.147:11002</IP>
        <IP>211.43.159.146:11002</IP>
    </ServerGroup>
</ArchlordInfo>

<PatchServerInfo>
    <IP>patch.archlord.webzen.net:11000</IP>
</PatchServerInfo>
```

Der XML-Parser fuer diese Datei liegt bei `FUN_007b3620` / Adresse `0x007b3620`. Er sucht die Tags `ArchlordInfo`, `ServerGroup`, `GroupName`, mehrere `IP`-Eintraege und `PatchServerInfo`. Die gefundenen Servergruppen werden in einer internen Liste gespeichert; Patchserver-IP(s) werden separat gesammelt.

### Fallback-Konfiguration

`FUN_0065eaf0` / `0x0065eaf0` oeffnet zuerst `.\\Archlord.ini`, danach `.\\Archlordtest.ini`. Falls beide Dateien nicht existieren, werden die Schluessel `LoginServerIP` und `LoginServerPort` ueber den internen Config-Reader gelesen und als String `"%s:%d"` in `AgcmLogin + 0xbd4` abgelegt.

Wichtig: Wenn eine lokale `Archlord.ini` vorhanden ist, kehrt diese Funktion nach `fclose` direkt zurueck. Die eigentliche XML-Verarbeitung passiert an anderer Stelle ueber `AcArchlordInfo`.

## Winsock-API-Funde

Direkte Treffer in Pseudocode/Imports:

- `WSAStartup(0x101, &WSADATA)` in `FUN_00706840` fuer die Haupt-TCP-Schicht.
- `WSACleanup()` in `FUN_006fdb50`.
- `socket(2, 1, 0)` in `FUN_00707160`: `AF_INET`, `SOCK_STREAM`, Default-Protokoll, also TCP/IPv4.
- `connect(socket, sockaddr, 0x10)` in `FUN_00706bd0`.
- `send(socket, buffer, len, 0)` in `FUN_00706900` und `FUN_00706a10`.
- `recv(socket, recvbuf, remaining, 0)` in `FUN_00706e70`.
- `closesocket` in `FUN_00706880`, `FUN_006fdb50` und weiteren Cleanup-Pfaden.
- `WSAAsyncSelect(socket, hwnd, 0x600, 0x3b)` in `FUN_00707090`.
- `inet_addr`, `gethostbyname`, `gethostbyaddr`, `inet_ntoa`, `htons`.
- UDP-nahe Stelle: `WSAStartup(0x202)`, `socket(2,2,0)` und `htons(15000)` bei ca. `0x0080...` / Pseudocode um Zeile `807417`. Diese wirkt wie eine separate UDP/NAT/Diagnose- oder Hilfsfunktion und ist noch nicht in den Hauptprotokollfluss eingeordnet.
- `sendto` in `FUN_00803430`: sendet ein von `FUN_00807830` erzeugtes Paket an Port `15000`.
- Importtabelle nennt `WSASend`; im sichtbaren Pseudocode laeuft der Hauptpfad aber ueber `send`.

## AcClientSocket

`FUN_00706770` konstruiert `AcClientSocket`. Aus den Offsets ergibt sich ungefaehr:

| Offset | Bedeutung |
|---:|---|
| `+0x04` | Callback-Kontext |
| `+0x08` | onConnect-Callback |
| `+0x0c` | onClose-Callback |
| `+0x10` | onError-Callback |
| `+0x14` | `sockaddr`-Speicher |
| `+0x24` | Socket-State |
| `+0x28` | SOCKET-Handle, initial `-1` |
| `+0x2c` | hidden HWND fuer `WSAAsyncSelect` |
| `+0x30` | Socket-Slot/Index |
| `+0x34` | Anzahl Bytes im Receivebuffer |
| `+0x38` | Receivebuffer, `0x64000` Bytes |
| `+0x64038` | Anzahl gepufferte Sendebytes |
| `+0x6403c` | Sendebuffer, `0x64000` Bytes |
| `+0xc803c` | Connect gestartet/aktiv |
| `+0xc8040` | Receive gesehen |
| `+0xc8044` | Close/Disconnect-Flag |
| `+0xc8048` | Rueckzeiger auf `AcSocketManager` |
| `+0xc8078` | Transform-/Crypto-Kontext |
| `+0xc807c` | Transformmodus aktiv, Werte `1` oder `2` relevant |
| `+0xc8098` | ausgehender Sequenzzaehler |
| `+0xc809c` | eingehender Sequenzzaehler aus Wrapper |
| `+0xc80a0` | gespeicherter Zielstring, max. ca. 0x17 Zeichen |
| `+0xc80bc` | Verbindungstyp |

Der Objektabstand im Socketarray betraegt `0xc80c0`.

### Socket-States

Aus den Vergleichen ergibt sich:

- `0`: frei/geschlossen.
- `1`: Socket erstellt und Async-Window registriert, noch nicht verbunden.
- `2`: `connect` gestartet; `WSAEWOULDBLOCK` (`0x2733`) ist akzeptierter Async-Zustand.
- `3`: verbunden; nur in diesem Zustand wird gesendet.
- `4`: Fehler/Disconnect-Pfad.

## AcSocketManager

`FUN_006fd6a0` konstruiert den Manager, setzt aktive Indizes auf `-1` und ruft `WSAStartup`.

`FUN_006fda60` allokiert ein Array von `AcClientSocket`-Objekten. Jeder Slot bekommt seinen Index in `socket + 0x30`. Die Konstruktion zeigt, dass der Client fuer mehrere parallele Serververbindungen ausgelegt ist.

`FUN_006fd760` ist der zentrale Connect-Aufruf:

1. sucht freien Socket-State `0`;
2. erwartet Zielstring im Format `host:port`;
3. trennt Host und Port an `:`;
4. ruft Cleanup, TCP-Socket-Erstellung und Callback-Setup;
5. ruft `connect`;
6. speichert Zielstring und Verbindungstyp.

`FUN_006fd8c0` ist der zentrale Send-Router:

- Pakete groesser `0xa000` werden verworfen.
- In `packet + 5` wird ein Manager-/Owner-Kontext geschrieben.
- `param_4` ist der Socketindex bzw. eine Routingklasse.
- `param_5 == 0` nutzt den Default-/aktiven Socket.
- `param_5 < 0` erlaubt Spezialrouting:
  - Socket `0` oder `1` direkt.
  - `param_4 == 2`: Broadcast an alle Sockets mit Verbindungstyp `1`.
- Danach geht es in `AcClientSocket::Send` (`FUN_00706900`).

## Verbindungslifecycle

### Start

1. `AcSocketManager` ruft `WSAStartup(0x101)`.
2. `AgcmLogin` ermittelt Zielserver aus `Archlord.ini`/Serverliste oder aus `LoginServerIP`/`LoginServerPort`.
3. `AgcmLogin::Connect` (`FUN_0065ebc0`) speichert Timestamp/Status und ruft `AgcmConnectManager` / Socketmanager mit dem Zielstring auf.

### TCP-Aufbau

`AcClientSocket::CreateSocket` (`FUN_00707160`) ruft:

```c
socket(AF_INET, SOCK_STREAM, 0);
WSAAsyncSelect(socket, hwnd, 0x600, 0x3b);
```

`0x3b` entspricht `FD_READ | FD_WRITE | FD_ACCEPT | FD_CONNECT | FD_CLOSE`. `FD_ACCEPT` ist fuer einen Client ungewoehnlich, aber im Maskenwert enthalten.

Der eigentliche WindowProc-Body ist im Pseudocode nur als Label `LAB_00706f30` referenziert, nicht als sauber dekompilierte Funktion ausgegeben. Das bedeutet: Die genaue Zuordnung von Windows-Event zu `FUN_00706a70`/`FUN_00706a10`/`FUN_00706e70`/`FUN_00706a90` muss noch ueber Disassembly oder Ghidra-Labelanalyse vervollstaendigt werden. Die Ziel-Callbacks sind aber durch die Socketfunktionen eindeutig:

- `FD_CONNECT` fuehrt zu State `3` und onConnect (`FUN_00706a70`).
- `FD_READ` fuehrt zu `recv` und Frameparser (`FUN_00706e70` -> `FUN_00706cd0`).
- `FD_WRITE` spuelt den Sendebuffer (`FUN_00706a10`).
- `FD_CLOSE` fuehrt in den Close-/Errorpfad (`FUN_00706a90`/`FUN_00706ad0`).

`AcClientSocket::Connect` (`FUN_00706bd0`) baut `sockaddr_in`:

- `sin_family = AF_INET`
- `sin_addr = inet_addr(host)` oder DNS-aufgeloest ueber `gethostbyname`
- `sin_port = htons(port)`

`WSAEWOULDBLOCK` (`0x2733`) wird als normaler Async-Connect akzeptiert. Andere Connectfehler werden in `LOG\_ALEF_ERROR_.log` mit `AcClientSocket Connect -> 195 line : ErrorCode : %d` protokolliert.

### Verbunden

`FUN_00706a70` setzt State `3` und ruft den onConnect-Callback.

### Disconnect/Fehler

`FUN_00706a90` setzt State `4`, ruft onClose, loescht Flags und schliesst Socket/Window. `FUN_00706ad0` ist der Fehlerpfad und ruft onError, sofern kein Close-Flag gesetzt ist.

## Sendepfad

Der typische Sendepfad ist:

```text
Modulcode
  -> FUN_004ea280        // AuPacket serialisiert Felder in Netzwerkframe
  -> FUN_004e45d0        // ruft Owner/VTable-Send
  -> FUN_00597b30        // Wrapper
  -> FUN_006fd8c0        // AcSocketManager::Send/Routing
  -> FUN_00706900        // AcClientSocket::Send
  -> send()
```

Ein Sonderwrapper `FUN_00597ac0` nimmt ein bereits gebautes Paket, erhoeht die Laenge um 1, setzt Startmarker `0xD6`, Endmarker `0x6B`, schreibt Laenge und nullt ein Header-DWORD bei `+5`, bevor ueber App-VTable `+8` gesendet wird. Das wird offenbar benutzt, um interne/nested Pakete in einen echten Netzwerkframe zu heben.

`AcClientSocket::Send`:

1. erlaubt Senden nur bei State `3`;
2. inkrementiert `+0xc8098` als Sequenzzaehler, `0` wird auf `1` korrigiert;
3. falls `+0xc807c != 0`, wird `FUN_004ea6e0` aufgerufen und bei `wrapper + 3` der Sequenzzaehler geschrieben;
4. kopiert in den Sendebuffer;
5. ruft `send`.

Hinweis: Die dekompilierte Zeile `send(socket, param_2, queuedLen, 0)` ist wahrscheinlich durch Decompiler-Artefakte unsauber, weil unmittelbar davor in den internen Sendebuffer kopiert wird. `FUN_00706a10` sendet eindeutig aus `socket + 0x6403c`.

## Receivepfad

Der typische Receivepfad ist:

```text
Windows message 0x600 / FD_READ
  -> AcClientSocket::Recv (FUN_00706e70)
  -> recv()
  -> AcClientSocket::ParseReceiveBuffer (FUN_00706cd0)
  -> optional FUN_004ea800 decrypt/unpack
  -> Framecheck 0xD6 ... 0x6B
  -> FUN_00701b70 Queue
  -> Modul-Dispatch/OnReceive
```

`FUN_00706e70` ruft `recv(socket, recvbuf + recvLen, 0x64000 - recvLen, 0)`. Fehler ungleich `WSAEWOULDBLOCK` werden als `AcClientSocket Recv -> 288 line : ErrorCode : %d` nach `LOG\_ALEF_ERROR_.log` geschrieben.

`FUN_00706cd0` ist der Frameparser:

- haengt neu gelesene Bytes an den Receivebuffer an;
- liest ab Bufferoffset `+1` eine `uint16`-Laenge;
- verwirft Frame/Buffer bei Laenge `< 8` oder `> 0x63fff`;
- wartet, bis der komplette Frame im Buffer liegt;
- kopiert den Frame in eine neue Packet-Node mit:
  - `node[0] = packetPtr`
  - `node[1] = packetLen`
  - `node[2] = socketSlot`
- erkennt optionale Wrapper `0xA1..0xAF` und `0xB1..0xBF`;
- speichert eingehende Sequenz aus `packet + 3` in `socket + 0xc809c`;
- transformiert/decryptet mit `FUN_004ea800`;
- verlangt danach Clearframe `0xD6 ... 0x6B`;
- queued das Paket mit `FUN_00701b70`;
- verschiebt Restbytes nach vorne.

## Frameformate

### Cleartext-Netzwerkframe

Von `FUN_004ea280(param_2 != 0)` gebaut:

| Offset | Groesse | Bedeutung |
|---:|---:|---|
| `+0x00` | 1 | Startmarker `0xD6` |
| `+0x01` | 2 | Frame-Laenge, `uint16`, inklusive Header und Endmarker |
| `+0x03` | 1 | Modul-/Opcode-ID, z.B. `0x0d` Login, `0x1b` ConnectManager |
| `+0x04` | 1 | Flags; Bit 0 wird beim Bauen geloescht |
| `+0x05` | 4 | vom Serializer auf `0` gesetzt; vermutlich Session-/Owner-/Reserved-Feld |
| `+0x09` | 4 | noch ungeklaert/reserviert; Maske beginnt fest bei `+0x0d` |
| `+0x0d` | 1/2/4 | Feld-Bitmaske, Breite kommt aus dem jeweiligen `AuPacket`-Layout |
| danach | variabel | serialisierte Felder |
| `+len-1` | 1 | Endmarker `0x6B` |

### Nested/Subpacket

Von `FUN_004ea280(param_2 == 0)` gebaut:

| Offset | Bedeutung |
|---:|---|
| `+0x00` | Laenge minus 2 |
| `+0x02` | Feldmaske, Breite 1/2/4 |
| danach | Felder |

Nested-Pakete werden in mehreren Modulen als variable Felder in aeussere Netzwerkpakete eingebettet, z.B. bei Item/Guild/Auction/OptimizedPacket2.

### Transformierter Wrapper

Von `FUN_004ea6e0` gebaut und von `FUN_004ea800` gelesen:

| Offset | Groesse | Bedeutung |
|---:|---:|---|
| `+0x00` | 1 | `0xA1` bei Modus 1 oder `0xB1` bei Modus 2 |
| `+0x01` | 2 | Wrapper-Laenge |
| `+0x03` | 4 | Sequenzzaehler, im Sendepfad gesetzt |
| `+0x07` | variabel | transformiertes Cleartext-Paket |
| `+len-1` | 1 | `0xAF` bei Modus 1 oder `0xBF` bei Modus 2 |

Die eigentliche Transformation liegt in der `AuPacket`/`AuMiniLZO`-Region:

- `FUN_004f97d0`: berechnet transformierte Laenge.
- `FUN_004f9870`: outbound transform/compress/encrypt.
- `FUN_004f98f0`: inbound inverse transform.
- `FUN_004f9540`: entscheidet, ob in-place oder in neuen Buffer entpackt wird.
- `FUN_004ea680`: globaler Transform-Kontext `DAT_009ac12c`.

Der Name `AuMiniLZO::vftable` taucht in diesem Block auf; die Transformation ist also sehr wahrscheinlich Kompression plus optionales Verschleiern/Verschluesseln, nicht nur reine RC4-Dateiverschluesselung.

## AuPacket-Feldlayout

`AuPacket` ist die zentrale Serialisierungsschicht:

- `FUN_004e9ec0`: initialisiert Layoutobjekt.
- `FUN_004ea630`: setzt Maskenbreite auf `1`, `2` oder `4` Bytes.
- `FUN_004e9f30`: registriert eine Feldliste `(type, count)` bis Sentinel `0xff, 0`.
- `FUN_004ea280`: serialisiert ein Paket.
- `FUN_004e9fb0`: deserialisiert ein Paket.

Die Feldmaske kodiert, welche Felder tatsaechlich vorhanden sind. Null-Pointer beim Serialisieren fuehren dazu, dass das entsprechende Maskenbit nicht gesetzt wird.

Sichtbare Feldtypen:

| Typ | Bedeutung aus Code |
|---:|---|
| `0` | fester Byteblock, Groesse `count * typeSize[0]`, wird als Pointer in den Paketbuffer behandelt |
| `1..10` | feste primitive Typen/Arrays, Groesse aus `DAT_008b7698[type] * count`; exakte Typnamen noch offen |
| `0xc` | length-prefixed String/Blob; bei `count >= 2` Liste mehrerer length-prefixed Werte |
| `0xd` | length-prefixed Datenfeld mit separatem Laengenargument |
| `0xff` | Layout-Sentinel |

Die Type-Size-Tabelle `DAT_008b7698` wird im Pseudocode referenziert, aber ihre Werte sind im aktuellen Export nicht direkt ausgeschrieben. Naechster sinnvoller Schritt: Tabelle aus der Binary bei VA `0x008b7698` ueber Ghidra oder PE-Offset extrahieren.

## Bekannte Modul-/Opcode-IDs

Diese IDs kommen aus Konstruktoren mit `FUN_004e4540(id)` und Modulnamen. Sie beschreiben die erste Routing-Ebene bei `frame + 3`.

| ID | Modul |
|---:|---|
| `0x01` | [`AgpmConfig`](../Module/AgpmConfig.md) |
| `0x02` | `AgpmCharacter` |
| `0x03` | `AgcmCharacter` |
| `0x04` | `AgpmItem` |
| `0x05` | [`AgpmSkill`](../Module/AgpmSkill.md) |
| `0x07` | [`AgcmPrivateTrade`](../Module/AgcmPrivateTrade.md) |
| `0x08` | [`AgpmParty`](../Module/AgpmParty.md) |
| `0x09` | [`AgcmParty`](../Module/AgcmParty.md) |
| `0x0a` | [`AgcmRecruit`](../Module/AgcmRecruit.md) |
| `0x0b` | `AgpmAuction` |
| `0x0d` | `AgcmLogin` / Loginpacket nutzt `AgpmCharacter`-Layout bei `+0xb84` |
| `0x0e` | [`AgcmObject`](../Module/AgcmObject.md) |
| `0x0f` | [`AgpmChatting`](../Module/AgpmChatting.md) |
| `0x11` | [`AgpmTimer`](../Module/AgpmTimer.md) |
| `0x12` | [`AgpmAdmin`](../Module/AgpmAdmin.md) |
| `0x13` | `AgpmQuest` |
| `0x14` | [`AgpmUIStatus`](../Module/AgpmUIStatus.md) |
| `0x15` | `AgpmGuild` |
| `0x16` | [`AgpmItemConvert`](../Module/AgpmItemConvert.md) |
| `0x17` | [`AgpmProduct`](../Module/AgpmProduct.md) |
| `0x18` | `AgpmWorld` |
| `0x19` | [`AgpmCasper`](../Module/AgpmCasper.md) |
| `0x1b` | `AgcmConnectManager` |
| `0x2a` | [`AgpmRemission`](../Module/AgpmRemission.md) |
| `0x2b` | [`AgpmBuddy`](../Module/AgpmBuddy.md) |
| `0x2c` | [`AgpmChannel`](../Module/AgpmChannel.md) |
| `0x2d` | [`AgpmMailBox`](../Module/AgpmMailBox.md) |
| `0x2e` | [`AgpmCashMall`](../Module/AgpmCashMall.md) |
| `0x2f` | [`AgpmReturnToLogin`](../Module/AgpmReturnToLogin.md) |
| `0x30` | [`AgpmEventNature`](../Module/AgpmEventNature.md) |
| `0x31` | [`AgpmEventTeleport`](../Module/AgpmEventTeleport.md) |
| `0x32` | `AgcmEventNPCTrade` |
| `0x34` | [`AgpmEventItemRepair`](../Module/AgpmEventItemRepair.md) |
| `0x36` | [`AgpmEventBank`](../Module/AgpmEventBank.md) |
| `0x37` | `AgpmEventNPCDialog` |
| `0x38` | [`AgpmEventItemConvert`](../Module/AgpmEventItemConvert.md) |
| `0x39` | [`AgpmEventGuild`](../Module/AgpmEventGuild.md) |
| `0x3a` | [`AgpmEventProduct`](../Module/AgpmEventProduct.md) |
| `0x3b` | [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md) |
| `0x3c` | [`ApmEventManager`](../Module/ApmEventManager.md) |
| `0x3e` | `AgpmEventQuest` |
| `0x3f` | [`AgpmEventRefinery`](../Module/AgpmEventRefinery.md) |
| `0x40` | [`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md) |
| `0x41` | `AgpmOptimizedPacket2` |
| `0x42` | `AgpmOptimizedPacket2` |
| `0x43` | [`AgpmEventCharCustomize`](../Module/AgpmEventCharCustomize.md) |
| `0x44` | [`AgpmSystemMessage`](../Module/AgpmSystemMessage.md) |
| `0x45` | [`AgpmScript`](../Module/AgpmScript.md) |
| `0x46` | [`AgpmWantedCriminal`](../Module/AgpmWantedCriminal.md) |
| `0x47` | [`AgpmNatureEffect`](../Module/AgpmNatureEffect.md) |
| `0x48` | [`AgpmStartupEncryption`](../Module/AgpmStartupEncryption.md) |
| `0x49` | [`AgpmSiegeWar`](../Module/AgpmSiegeWar.md) |
| `0x4a` | [`AgpmPvP`](../Module/AgpmPvP.md) |
| `0x4b` | [`AgpmRefinery`](../Module/AgpmRefinery.md) |
| `0x4c` | [`AgpmAreaChatting`](../Module/AgpmAreaChatting.md) |
| `0x4d` | [`AgpmRide`](../Module/AgpmRide.md) |
| `0x4e` | [`AgpmBillInfo`](../Module/AgpmBillInfo.md) |
| `0x4f` | [`AgpmSummons`](../Module/AgpmSummons.md) |
| `0x50` | [`AgpmEventSiegeWarNPC`](../Module/AgpmEventSiegeWarNPC.md) |
| `0x52` | [`AgpmSearch`](../Module/AgpmSearch.md) |
| `0x53` | [`AgpmTax`](../Module/AgpmTax.md) |
| `0x54` | [`AgpmGuildWarehouse`](../Module/AgpmGuildWarehouse.md) |
| `0x55` | [`AgpmArchlord`](../Module/AgpmArchlord.md) |
| `0x57` | [`AgpmEventGacha`](../Module/AgpmEventGacha.md) |
| `0x58` | [`AgcmBattleGround`](../Module/AgcmBattleGround.md) |
| `0x60` | [`AgpmTitle`](../Module/AgpmTitle.md) |
| `0x61` | [`AgpmWarInfo`](../Module/AgpmWarInfo.md) |
| `0x62` | [`AgpmShrineBattle`](../Module/AgpmShrineBattle.md) |

## Login: was wird wann gesendet?

### Sequenz 1: Clientstart bis Loginserver

Das ist der erste sauber rekonstruierte Ablauf. Er beschreibt, was der Client vor dem eigentlichen Spielbeitritt an den Server sendet.

| Schritt | Wann/Warum | Funktion | Richtung | Inhalt |
|---:|---|---|---|---|
| 1 | Client liest Serverliste | `FUN_007b3620` | Datei -> Client | entschluesselte `Archlord.ini`, `ArchlordInfo/ServerGroup/IP` |
| 2 | User/Autologin liefert Zugangsdaten | `FUN_0065d7e0` | UI/Config -> Client | schreibt Account nach `AgcmLogin + 0xc4c`, Passwort nach `AgcmLogin + 0xc8c` |
| 3 | Serverauswahl startet Verbindung | `FUN_00743160` oder `FUN_00743210` | Client intern | waehlt `host:port`, setzt UI auf `LOGIN_WAITING` |
| 4 | TCP-Verbindung zum Loginserver | `FUN_0065ebc0` -> `FUN_006f5530` -> `FUN_006fd760` -> `FUN_00706bd0` | Client -> Server | `connect()` zu z.B. `211.43.159.147:11002` |
| 5 | Socket ist verbunden | `FUN_00706a70` / Connect-Callback | Server/OS -> Client | State wird `3`, Callback wird ausgeloest |
| 6 | StartupEncryption falls aktiv | `FUN_00681d00` / `FUN_00681d50` / `FUN_00681da0` -> `FUN_00681800` | Client -> Server | `AgpmStartupEncryption`, Opcode `0x48`, Operation `0` |
| 7 | Server liefert Seed/Keymaterial | `FUN_006819c0` | Server -> Client | `AgpmStartupEncryption`, Operation + Datenblock |
| 8 | Client antwortet mit transformiertem Zufallsblock | `FUN_006819c0` -> `FUN_006818b0` | Client -> Server | `AgpmStartupEncryption`, Opcode `0x48`, Operation `2`, Datenblock |
| 9 | Socket-Transformation aktiv | `FUN_00681b30` | Client intern | setzt `socket + 0xc807c = 2`, danach `0xB1..0xBF` Wrapper fuer Sendepakete |
| 10 | Login-Credentials werden gesendet | `FUN_0065ec80` | Client -> Loginserver | Opcode `0x0d`, Operation `1`, Account, Passwort |
| 11 | Loginserver antwortet | `FUN_0065e7f0` | Server -> Client | Loginstatus, Sessiondaten, Charakter-/Serverlisten-Status |
| 12 | Handoff zu weiterem Server moeglich | `FUN_006f5780` Op `1` | Server -> Client -> neuer Server | Server sendet neues `host:port`; Client verbindet weiteren Socket |

Wichtig: Schritt 6 bis 9 haengen an einem globalen Transform-Flag in `AuPacket` (`FUN_004ea680()->+4`). Wenn dieses Flag nicht aktiv ist, springen die Handler direkt zu den Folgeaktionen:

- Login-Verbindung: direkt `FUN_0065d840()`;
- anderer Verbindungstyp `0`: direkt `FUN_005a24f0(socketId)`;
- Verbindungstyp `1`: direkt `FUN_006da680()`.

### Serverauswahl/Connect

Die UI liest Servergruppen aus `Archlord.ini`. `FUN_00743160` waehlt einen Serverstring aus der Liste und ruft `AgcmLogin::ConnectTo(serverString)` (`FUN_0065ec40`). Danach wird UI-Status `LOGIN_WAITING` gesetzt.

Falls keine Serverliste vorhanden ist, wird `AgcmLogin::Connect` (`FUN_0065ebc0`) mit dem Fallback aus `LoginServerIP`/`LoginServerPort` benutzt.

### Loginpacket

`FUN_0065ec80` baut das Loginpacket:

- Modul-/Opcode-ID: `0x0d`.
- Ziel: ueber `FUN_004e45d0` an den Socketmanager.
- Operation/Statusbyte: `1`.
- Account/Loginname: Buffer bis `0x31` Bytes.
- Passwort: Buffer bis `0x21` Bytes.
- Ein `gamestring`/`autologin`-Pfad wird gelesen, aber im sichtbaren dekompilierten Call nicht eindeutig an `FUN_004ea280` uebergeben. Das ist noch ungeklaert und sollte dynamisch geprueft werden.

Die Puffer werden vorher von `FUN_0065d7e0` gefuellt:

- Account/Member-ID wird lower-case gemacht (`_mbslwr`) und nach `AgcmLogin + 0xc4c` geschrieben.
- Passwort wird nach `AgcmLogin + 0xc8c` geschrieben.
- Manuelle UI: `LG_IdPasswordOK` (`FUN_00749a20`) liest `ID_EDIT` und `PASSWORD_EDIT` und ruft danach `FUN_0065d7e0`.
- Autologin-Pfade lesen `member_id`, `autopwd` bzw. `autologin` und rufen ebenfalls `FUN_0065d7e0`.
- Der eigentliche Sendetrigger ist `FUN_0060b680`: `FUN_0065ec80(iVar2 + 0xc4c, iVar2 + 0xc8c, socketId)`.

Der relevante Serializer-Call:

```text
FUN_004ea280(*(AgpmCharacter) + 0xb84,
             outerFrame=1,
             outLen,
             opcode=0x0d,
             opByte,
             0,
             accountBuffer, accountLen,
             passwordBuffer, passwordLen,
             ...)
```

Das Layout, das hier wahrscheinlich benutzt wird, ist das erste [`AgpmLogin`](../Module/AgpmLogin.md)-Layout mit Maskenbreite `2`:

```text
1,1,
0,0x20,
0,0x31,
1,1,
0,0x21,
1,1,
5,1,
0,0x20,
0xc,1,
0xc,1,
5,1,
0xc,1,
0,0x801,
0,5,
5,1,
5,1
```

Feldnamen sind noch nicht vollstaendig rekonstruiert. Aus dem Login-Call sind aber Account und Passwort sicher erkennbar.

### Login-Folgepakete mit Opcode `0x0d`

Rund um `FUN_0065d840` bis `FUN_0065e2f0` liegen weitere Client->Server-Sender auf demselben Opcode `0x0d`. Sie benutzen meist Routing `socketType=2`, `param_5=-1`, Ziel `AgcmLogin + 0xc3c`.

| Funktion | Op/Statusbyte | Zweck aus Code/Inferenz |
|---|---:|---|
| `FUN_0065d840` | `0` | erstes Login-Folgepaket nach erfolgreichem StartupEncryption oder wenn Encryption deaktiviert; bettet ein Nested-Paket aus zwei Werten ein |
| `FUN_0065d950` | `2` | sendet kurzen String `< 0x11`; wahrscheinlich Server-/Character-Auswahl- oder Rename-Token |
| `FUN_0065da30` | nicht konstant sichtbar | sendet `param_3` plus Daten aus `+0xc1c`; wird u.a. von ReturnToLogin benutzt |
| `FUN_0065dad0` | nicht konstant sichtbar | aehnlich `FUN_0065da30`, mit Fehlercallback bei Sendefehler |
| `FUN_0065db90` | nicht konstant sichtbar | baut Nested-Datenpaket bei `+0x25dac` und sendet es im Loginframe |
| `FUN_0065dcb0` | `9` | sendet einen Pointer/Datenblock; genaue UI-Aktion noch offen |
| `FUN_0065dd80` | `10` | sendet Login-Operation `10` mit Nested-Paket |
| `FUN_0065de70` | `0x0b` | sendet komplexeres Nested-Paket; wahrscheinlich Charakter-/Serveraktion |
| `FUN_0065dfa0` | `0x15` | sendet weiteres komplexes Nested-Paket |
| `FUN_0065e0d0` | nicht konstant sichtbar | sendet verschachtelte Daten mit zwei Nutzdatenargumenten |
| `FUN_0065e1f0` | nicht konstant sichtbar | sendet Nested-Datenblock mit mehreren Parametern |
| `FUN_0065e2f0` | `0x12` oder `0x13` | Operation haengt davon ab, ob `param_5 == 0`; vermutlich alternativer Login-/Charakterstatus |

Diese Tabelle ist der naechste Ansatzpunkt, um die Login- und Charakterauswahlphase vollstaendig in einzelne Requests aufzuteilen.

### Login-Antworten

`AgcmLogin::OnReceive` (`FUN_0065e7f0`, um Pseudocode-Zeile `486420`) deserialisiert das Loginmodul und schaltet auf ein Operationsbyte:

| Op | Wirkung im Client |
|---:|---|
| `0` | kopiert 8 DWORDs nach `AgcmLogin + 0xbb4`; danach Event `2`; sehr wahrscheinlich Login-Erfolg / Sessiondaten |
| `1` | speichert zwei Integers nach `+0xc44/+0xc48`; Event `4`; wahrscheinlich Server-/Charakterlisten-Status |
| `2` | Event `0x0f` mit Fehler-/Statuswert |
| `3` | ruft `FUN_0065d4e0(local_34)` |
| `4` | ruft `FUN_0065d550(local_34, 0)` |
| `5` | Event `7` mit Wert und Socket-ID |
| `7` | Event `8`, setzt `+0xda4` zurueck |
| `8` | Event `9`, danach `FUN_0065d610(...)` |
| `10` | Event `10` |
| `0x0b` | ruft `FUN_0065d550(local_34, 1)` |
| `0x0c` | Event `0x0c` |
| `0x0d` | ruft `FUN_0065d6d0(local_34)` |
| `0x0f` | ruft `FUN_0065d770(local_34, local_14, socketId)` |
| `0x11` | ruft `FUN_0065e6e0(local_30, local_34)` |
| `0x20` | Event `3` |

UI-Strings wie `Login01SlotCharName`, `Login01SlotCharLevel`, `Login01SlotCharExp`, `Login01SlotCharGuild`, `Login01SlotCharVillian`, `LoginGameServerName`, `ConnRename` und `DisconnectedByServer` bestaetigen, dass die Loginantworten Charakter-Slots, Serverlisten/Servernamen, Rename-/Block-/Disconnect-Zustaende und Statuscodes enthalten.

## ConnectManager: Server-Handoff

`AgcmConnectManager` hat ID `0x1b` und Layout:

```text
mask=1:
1,1,
5,1,
1,1,
0,0x17,
5,1,
0xc,1
```

`FUN_006f5780` verarbeitet eingehende Operationen:

- Op `1`: Falls ein Zielstring vorhanden ist, verbindet der Client zu dieser Adresse (`host:port`) als neuer Socket, speichert die Adresse im Slot und sendet danach Op `2` mit dem neuen Socketindex zurueck.
- Op `3`: speichert einen Wert in `socketSlot * 0x20 + 0x134c4`, sendet Op `3` zurueck und uebergibt einen Wert als Routing/Handshake-Kontext.
- Op `5`: setzt `AgcmConnectManager + 0x198ac` auf den aktuellen Socket als aktiven/default Socket.

Interpretation: Loginserver und Gameserver sind wahrscheinlich getrennte Dienste. Der Loginserver kann dem Client eine Gameserver-/Channel-Adresse schicken. Danach authentifiziert/registriert der Client den neuen Socket beim Server.

## StartupEncryption

`AgpmStartupEncryption` hat ID `0x48`, Layout:

```text
mask=1:
1,1,
0xd,1
```

Das passt zu einem fruehen Handshake mit einem Operationsbyte und einem length-prefixed Datenblock. Es ist wahrscheinlich fuer das Aktivieren/Fuellen von `AcClientSocket + 0xc8078/+0xc807c` verantwortlich. Der genaue Ablauf ist noch nicht fertig rekonstruiert.

### Genauere StartupEncryption-Kette

`AgpmStartupEncryption` wird bei `FUN_0056cc80` konstruiert:

- Modulname: `AgpmStartupEncryption`
- Modul-ID: `0x48`
- Maskenbreite: `1`
- Layout: Operationsbyte plus optionaler length-prefixed Datenblock (`type 0xd`).

Wichtige Sender:

- `FUN_0056cf80`: baut ein Paket mit ID `0x48`. Falls `param_4` und `param_5` gesetzt sind, wird der variable Datenblock mit Laenge gesendet; sonst nur die Operation.
- `FUN_00681800`: sendet Operation `0` ueber den Sockettyp des ausgewaehlten Sockets.
- `FUN_006818b0`: sendet Operation `2` mit Datenblock und Laenge.

[`AgcmStartupEncryption`](../Module/AgcmStartupEncryption.md):OnReceive`/Handler bei `FUN_006819c0` verarbeitet eingehende Seed-/Keydaten:

1. liest Socket-ID aus `param_3`;
2. holt den Socket ueber `AcSocketManager::GetSocket` (`FUN_006fda40`);
3. schreibt/initialisiert den Transform-Kontext bei `socket + 0xc8078`;
4. erzeugt Zufallsdaten mit `FUN_007e3340(0xff)`;
5. transformiert diese Daten;
6. sendet sie per `FUN_006818b0(..., socketId)` zurueck.

`FUN_00681b30` schaltet danach den Socket auf Transformmodus `2`:

```text
*(socket + 0xc807c) = 2
```

Danach entscheidet der Verbindungstyp:

- Typ `0`: ruft `FUN_005a24f0(socketId)` auf.
- Typ `1`: prueft `AgcmCharacter`/Loginzustand und ruft je nach Zustand `FUN_0065d840()` oder `FUN_006da680()`.

Interpretation: Der erste Login-/Connect-Handshake laeuft wahrscheinlich noch im klaren `0xD6..0x6B`-Frameformat. Nach `AgpmStartupEncryption` wird fuer diesen Socket der `0xB1..0xBF` Wrapper aktiviert.

## Weitere Connect-Callsites

Neben dem Loginpfad gibt es mindestens diese Connect-Einstiege:

| Callsite | Ziel/Verwendung |
|---|---|
| `FUN_0065ebc0` | normaler Login-Connect zu `AgcmLogin + 0xbd4`; Verbindungstyp `1`; Callbacks `LAB_0065e3f0`, `LAB_0065e430`, `FUN_0065e450` |
| `FUN_0065ec40` | ueberschreibt `AgcmLogin + 0xbd4` mit einem Serverstring aus UI/Serverliste und ruft danach Login-Connect |
| `FUN_006f5780` Op `1` | servergesteuerter Handoff zu einem neuen `host:port`-Ziel; Verbindungstyp `0`; danach Rueckmeldung Op `2` |
| `FUN_006da7...` um Zeile `563177` | verbindet mit uebergebenem Ziel oder fallback `AgcmLogin + 0xbd4`; haengt an `AgcmConnectManager`/`AgcmLogin`/`AgcmCharacter` |
| `FUN_005a3d50` | weiterer Connect mit Callbackgruppe `LAB_005a1a80`, `LAB_005a1ab0`, `LAB_005a1ad0`; speichert einen Namen/String bei `+0x15978`; Modulkontext noch unbenannt |

Diese Callsites zeigen, dass der Client nicht nur "einmal Loginserver" macht, sondern mehrere Sessions/Sockets fuer Login, Gameserver/World und Sonderfluesse verwalten kann.

## UDP-Port 15000

`FUN_00803430(char *host)` ist ein separater UDP-Sender:

```text
WSAStartup(0x202)
socket(AF_INET, SOCK_DGRAM, 0)
sockaddr.port = htons(15000)
sockaddr.addr = inet_addr(host) oder gethostbyname(host)
buf = FUN_00807830()
sendto(socket, buf, *(uint32*)buf + 4, 0, sockaddr, 0x10)
closesocket(socket)
```

Das Paket ist length-prefixed: `*(uint32*)buf + 4` wird als Sendelaenge benutzt. Da diese Funktion nicht den `AcClientSocket`-/`AuPacket`-Framepfad nutzt, ist sie wahrscheinlich kein normales Spielprotokollpaket. Moegliche Funktionen: Launcher/GameGuard/Diagnose/Ping/Serverstatus. Das muss durch Rueckverfolgung von `FUN_00803430` und `FUN_00807830` noch bestaetigt werden.

## Charakter-, Item- und Weltpakete

### AgpmCharacter (`0x02`)

`AgpmCharacter` besitzt mehrere grosse Layouts. Das erste mit Maskenbreite `4` ist sehr wahrscheinlich ein voller Charakterzustand:

```text
1,1, 5,1, 5,1, 0xd,1, 1,1,
0xc,1, 0xc,1, 0xc,1,
7,1, 7,1, 7,1,
1,1, 1,1, 5,1, 1,1,
2,1, 2,1, 8,1, 1,1,
0,0x20,
1,1, 1,1, 5,1, 1,1,
4,1, 5,1, 5,1,
0,0x10,
0xd,1, 6,1, 6,1
```

Inferenz: Das enthaelt Charakteroperation, IDs, Name/Strings, Position/Orientierung, Statuswerte, Faktoren/Stats, feste Bytebloecke und variable Zusatzdaten. Die vielen `AgpmCharacter::OnReceive`-Events bestaetigen Add/Remove/Update/Idle/ImportData/Filter- und Statusfluesse.

### AgpmItem (`0x04`)

`AgpmItem` hat 12 Layouts. Das grosse Layout mit Maskenbreite `2` ist wahrscheinlich Iteminstanz/Inventory-Update:

```text
1,1, 5,1, 1,1, 9,1,
1,10, 5,10, 1,10, 1,10,
0xc,10, 0xc,10,
1,1, 5,1, 1,1, 1,1,
0xc,1, 0xc,1
```

Inferenz: Mehrfachfelder mit Count `10` passen zu Itemoptionen/Sockeln/Enchant-/Durability-/Grid- oder Statlisten. Weitere Layouts enthalten feste Bytebloecke `0x40`, mehrere Typ-3/Typ-4-Tripel und kleine Statusupdates.

### AgpmWorld (`0x18`)

Layout:

```text
mask=1:
1,1,
0,0x20,
3,1,
0xd,1,
0,0x20
```

Bekannte Sendestellen bei Pseudocode um Zeile `563256`/`563284` bauen World-Pakete mit Routing `param_4 = 2` und Spezialrouting `param_5 = -1`. Das passt zu World-/Zone- oder Channel-Verbindungen, nicht zum Login-Socket.

Inferenz: Datenbankseitig entspricht das vermutlich Welt-/Region-/Instanzzustand, Spawn-/Positions- oder Kartenwechseldaten. Exakte Felder sind noch offen.

### AgpmEventCharCustomize (`0x43`)

Layout:

```text
mask=1:
1,1,
0xc,1,
5,1,
1,1,
1,1
```

Inferenz: Operation, Name/String oder Presetdaten, Character-ID/Template-ID und zwei kleine Auswahlwerte. Zusammen mit den bisherigen Character-Customize-Funden deutet das auf Serverpersistenz fuer Aussehen/Charakteranpassung.

## Moegliche Server-Datenbankstrukturen

Die folgenden Strukturen lassen sich nicht als echte SQL-Tabellen beweisen. Sie sind aber stark aus Modulnamen, Packetfeldern, UI-Strings und lokalen `ini`-Tabellen ableitbar.

### Sicher ableitbare Server-Domaenen

- Account/Login: Accountname, Passwort/Authdaten, Loginstatus, Blockstatus, Session-/Handshake-Daten, Autologin/GameString.
- Serverliste/Channels: Servergruppen, Gameserver-IP:Port, aktive Socket-/Channel-ID, Routingtyp.
- Character: Character-ID, Accountbezug, Name, Level, EXP, Guild, Villain/Wanted-Criminal-Status, Position/Welt, Klasse/Rasse, sichtbare Ausruestung, Faktoren/Stats.
- Character customization: Aussehenswerte wie Head/Hair/Face/Body oder Preset-/Template-Auswahl.
- Inventory/Item: Iteminstanz-ID, Template-ID, Owner-Character-ID, Slot/Grid, Stackcount, Durability, Optionen/Sockel/Enchant/Convert/Refinery.
- Skill: erlernte Skills, Skilllevel, Cooldowns/Timers, Skillmaster/Eventdaten.
- Quest: Queststatus, Questflags, EventQuest-Fortschritt.
- Guild: Guild-ID, Name, Member, Ranks, Guildmark, Guildwarehouse, Siege-/Tax-Bezug.
- Chat/Channel/Party/Buddy/Mail: soziale Relationen und Nachrichten-/Mailboxdaten.
- Auction/CashMall/BillInfo: Markt-/Kaufdaten, Waehrung/Kontostand/Transaktionsstatus.
- World/Event/Nature: Weltzustand, Teleport-/NPC-/Bank-/Repair-/Product-/Refinery-Events, NatureEffects.

### Plausible Tabellen/Entitaeten

| Entitaet | Begruendung |
|---|---|
| `accounts` | Loginpacket enthaelt Account/Passwort; UI kennt AccountBlocked |
| `sessions` / `login_tokens` | Login-Erfolg kopiert 8 DWORDs; StartupEncryption/ConnectManager deuten auf Sessionhandoff |
| `server_groups` / `game_servers` | `ArchlordInfo` mit Gruppe und mehreren IPs; ConnectManager verbindet zu weiteren Servern |
| `characters` | Character-Slots, Name, Level, EXP, Guild, Villain im Login-UI; `AgpmCharacter` grosses State-Layout |
| `character_appearance` | `AgpmEventCharCustomize` und Charakteranpassungsdaten |
| `character_factors` | eigenes Modul [`AgpmFactors`](../Module/AgpmFactors.md) mit vielen Statlayouts |
| `items` / `item_instances` | `AgpmItem` grosse Instanzlayouts und lokale Itemtemplates |
| `inventory_slots` / `grids` | viele Verweise auf [`AgpmGrid`](../Module/AgpmGrid.md), Add/RemoveItemFromGrid |
| `skills` / `skill_cooldowns` | `AgpmSkill`, `AgpmTimer`, Skillmaster-Events |
| `guilds`, `guild_members`, `guild_warehouse` | `AgpmGuild`, `AgpmGuildWarehouse`, Guildmark-Templates |
| `quests`, `quest_progress` | `AgpmQuest`, `AgpmEventQuest` |
| `mail`, `mail_attachments` | `AgpmMailBox`, Item-Abhaengigkeit |
| `auction_listings` | `AgpmAuction`, Item-Abhaengigkeit und mehrere Such-/Kauf-/Listenlayouts |
| `cash_transactions` / `billing` | `AgpmCashMall`, `AgpmBillInfo` |
| `world_state` / `character_position` | `AgpmWorld`, Positions-/World-Routing, Mapdaten |
| `events` / `npc_dialogs` / `teleports` | viele `AgpmEvent*` Module |

### Was aus dem Client nicht sicher bestimmbar ist

- echte Tabellennamen und Spaltennamen des Servers;
- Primaer-/Fremdschluessel;
- SQL-Datentypen;
- serverseitige Validierungslogik;
- Passwort-Hashing oder Account-Speicherform;
- ob Login- und Gameserver dieselbe Datenbank oder getrennte Dienste nutzen.

Der Client liefert aber genug, um ein logisches Datenmodell und ein Packet-Schema zu rekonstruieren.

## Offene Punkte / naechste Schritte

1. `DAT_008b7698` direkt aus der Binary extrahieren, um alle festen Feldtypen (`1..10`) sauber zu benennen.
2. Alle `FUN_004e9f30`-Layouts automatisch in eine TSV/CSV-Tabelle exportieren: Modul, ID, Layoutoffset, Maskenbreite, Feldliste.
3. Alle `FUN_004ea280(... opcode=...)` Call-Sites gruppieren, um konkrete Client->Server Operationen pro Modul zu kartieren.
4. `LAB_00706f30` im Disassembly/Ghidra sauber als WindowProc benennen und Eventzweige dokumentieren.
5. `FUN_00803430`/`FUN_00807830` rueckverfolgen, um den UDP-Port-15000-Zweck zu bestimmen.
6. Runtime-Hook fuer `send`/`recv` oder `FUN_00706900`/`FUN_00706cd0` bauen, um echte Frames mit Timestamp, Socketindex, Ziel, Opcode, Laenge und Rohbytes zu loggen.
7. `archlordgb.ini` mit weiteren Schluesselkandidaten pruefen; `1111` und `asdfqwer` ergeben dort keinen lesbaren XML-/INI-Text.
8. Loginantworten dynamisch aufnehmen, um die 8 DWORDs bei Op `0` und die Serverhandoff-Felder sicher zu benennen.
