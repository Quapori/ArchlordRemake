# Alefclient.exe Auslese-Roadmap

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Daten, Auslese und Werkzeuge](Index.md)*

Stand: 2026-09-06

## Aktualisierung 2026-09-09

Diese Roadmap enthaelt historische Zwischenstaende und beschreibt an mehreren
Stellen bereits ueberholte Blowfish-/Keyrichtungs-Hypothesen. Fuer den aktuellen
Live-Stand der Anmeldung ist [`WINSOCK_SEQUENCE_17_LOGIN_WORLD_CHARACTER_SELECTION.md`](../Netzwerk/Sequenz-17-Login-World-Character-Selection.md)
massgeblich: StartupEncryption, Sign-On, World-Listen und Union-Antwort laufen;
der aktuell belegte Stillstand entsteht danach durch die fehlende serverseitige
`AGPMLOGIN_CHARACTER_NAME_FINISH`-Meldung (Operation `5`) vor der erwarteten
Client-Anfrage Operation `6`. Diese Aktualisierung dokumentiert nur den Befund;
sie aendert keinen Loginserver-Code.

## Eingelesener Ist-Stand

- [`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](../Netzwerk/Transform-Cipher.md) dokumentiert die Netzwerkverschluesselung getrennt von der Dateiverschluesselung. Wichtig sind `AuCryptManager` bei `0x009AC12C`, Cipher-IDs `0..3` und der bisher in Ghidra fehlende Handler bei `0x00681970`, der Server-seitig gesetzte Encode-/Decode-Cipher-IDs uebernimmt.
- [`WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md`](../Netzwerk/Sequenz-01-Login-Handshake.md) ist inzwischen live gegen den echten Client verifiziert. Der StartupEncryption-Client-Request, der Field-Mask-Aufbau und die 2-Byte-Laengenpraefixe fuer Datenfelder sind bestaetigt.
- [`CLIENT_LAUNCH_AUTH_MECHANISM.md`](../Start-und-Login/Startmechanismus.md) beschreibt die Start-/Auth-Huerden: `NoExcuteAuth.arc` umgeht den Website-Token-Zwang; `NotCheckGameGuard.arc` waehlt den no-op `AuNPBase`-Pfad statt `AuNPGameLib`.
- `AlefLogin` ist weiter als seine README: Der Rust-Code implementiert bereits StartupEncryption-Antworten, Blowfish-LittleEndian-Wrapping, AgcmLogin Encrypt-Code- und Sign-On-Antworten. `cargo test` laeuft aktuell gruen.
- Die Netzwerkberichte decken aktuell Sequenzen `01` bis `16` ab, inklusive Login, ConnectManager, Charakter/World/Chat/Party/Guild/Trade/Auction/Wanted/GuildBattle/Item/Bank.
- Die Daten-/Weltberichte enthalten bereits RC4/MD5-Dateischluessel (`1111`, `asdfqwer`), World/MA1/MA2-Materialaufbau, Shader, Octree, Wasser, Gras und andere World-Konfigurationen.

## Live-Befund 2026-09-06 10:10

Der Client aus `C:\Spiele\Archlord\alefclient.exe` verbindet erfolgreich mit dem lokalen Server auf `127.0.0.1:11002`. Der Server-Log zeigt:

- TCP-Connect von `127.0.0.1`.
- Klartext-Frame [`AgpmStartupEncryption`](../Module/AgpmStartupEncryption.md) Operation `0`.
- Server sendet deterministic key setup: Operation `7` Blowfish/Blowfish, Operation `5` Encode-Key, Operation `6` Decode-Key, Operation `3` Activate.
- Client sendet danach einen Blowfish-gewrappten Frame mit Sequenz `2`.
- Entschluesselt ergibt sich [`AgcmLogin`](../Module/AgcmLogin.md) (`0x0d`) Operation `0`: Encrypt-Code-Anfrage.
- Server antwortet mit Encrypt-Code.
- Danach kam im gelesenen Log kein `AgcmLogin` Operation `1` Sign-On mehr.

Ursache/Fix:

- Die Serverantwort wurde bis dahin mit `ENCODE_KEY` verschluesselt.
- Das ist fuer Server-zu-Client wahrscheinlich falsch, weil der Client Operation `6` als Decode-Key fuer eingehende Serverpakete gesetzt bekommt.
- `AlefLogin/crates/aleflogin-server/src/main.rs` wurde deshalb geaendert: Login-Antworten werden jetzt mit `DECODE_KEY` verschluesselt.
- `cargo test` ist nach der Aenderung gruen.
- Wichtig: Danach musste zusaetzlich `cargo build -p aleflogin-server` laufen, weil `cargo test` nicht automatisch das gestartete `target/debug/aleflogin-server.exe` ersetzt.
- Der lokale Server wurde danach neu gestartet und hoert als PID `35992` auf `0.0.0.0:11002`.
- Das Logging wurde in den Server verlegt: `tracing_subscriber` schreibt jetzt direkt appendend in `AlefLogin/server.log`, unabhaengig von Shell-Redirection.

## Live-Befund 2026-09-06 10:17

Nach Neustart mit `DECODE_KEY` fuer Server-zu-Client blieb der Ablauf an derselben Stelle stehen:

- Client verbindet.
- StartupEncryption wird korrekt ausgehandelt.
- Client sendet verschluesseltes `AgcmLogin` Operation `0` mit Version-/Resource-Nested-Paket.
- Server entschluesselt das Paket korrekt.
- Server sendet `AgcmLogin` Operation `0` mit 32-Byte-Block.
- Danach bleibt die TCP-Verbindung offen, aber der Client sendet kein `AgcmLogin` Operation `1`.

Neue Schlussfolgerung:

- Die Keyrichtung allein war nicht die Ursache.
- Der Inhalt der op0-Antwort ist weiterhin plausibel, weil `FUN_0065e7f0` bei empfangener Server-op0 `local_28` als 8 DWORDs nach `AgcmLogin+0xbb4` kopiert.
- Der naechste wahrscheinlichere Fehler ist der Wrapper-Typ: Der Client sendet eigene transformierte Pakete sicher als `0xB1..0xBF`; fuer Server-zu-Client kann `0xA1..0xAF` noetig sein.
- `AlefLogin/crates/aleflogin-server/src/main.rs` wurde deshalb geaendert: Serverantworten werden jetzt als `FrameKind::WrapperA` gebaut.
- Server wurde neu gebaut und neu gestartet; aktueller Testserver hoert als PID `2924` auf `0.0.0.0:11002`.

## Offene Kernarbeit

1. **Master-Status aktualisieren**
   - `AlefLogin/README.md` ist veraltet und beschreibt noch den alten Beobachter-Stand.
   - Eine zentrale Statusdatei sollte festhalten, welche Client-Phase praktisch laeuft, welche nur statisch analysiert ist und welche live bestaetigt wurde.

2. **Server-zu-Client-Keyrichtung live verifizieren**
   - Im Code existieren `ENCODE_KEY = "AlefLoginEncKey!"` und `DECODE_KEY = "AlefLoginDecKey!"`.
   - Der Server verschluesselt Login-Antworten jetzt mit `DECODE_KEY`.
   - Naechster Live-Test: Client erneut verbinden/anmelden und pruefen, ob danach `AgcmLogin` Operation `1` beim Server ankommt.

3. **Login-Erfolg praktisch bis zur naechsten Client-Anfrage bringen**
   - Der lokale Server beantwortet bereits AgcmLogin op0 und op1.
   - Jetzt muss live geprueft werden, ob der Client diese Antworten akzeptiert oder ob Laenge, Field-Mask, Wrapper-Sequenz, Cipher-Key oder Antwortinhalt noch abweichen.
   - Jedes danach kommende entschluesselte Paket muss als neue Sequenz dokumentiert werden.

4. **AgcmLogin-Nachfolgeoperationen auslesen**
   - In `FUN_0065e7f0` sind weitere Login-Receive-Pfade bekannt.
   - Besonders wichtig sind op0 mit den 8 DWORDs bei `AgcmLogin+0xbb4`, op1 mit `+0xc44/+0xc48`, Event 2/Login-Erfolg und Event 4/Socket-ID.
   - Die Sendefunktionen um `FUN_0065d950`, `FUN_0065da30`, `FUN_0065dad0`, `FUN_0065db90`, `FUN_0065dcb0`, `FUN_0065dd80`, `FUN_0065de70` und `FUN_0065e1f0` muessen einzeln in Payload-Layouts uebersetzt werden.

5. **AgcmConnectManager-Handoff implementieren**
   - Nach erfolgreichem Login erwartet der Client vermutlich einen Server-/World-Handoff ueber Modul `0x1b`.
   - Zu klaeren ist, ob der Client eine neue TCP-Verbindung aufbaut oder auf derselben Verbindung in die World-Phase wechseln kann.
   - Ziel: minimalen Handoff senden, der den Client zur naechsten sichtbaren Phase bringt.

6. **Paketlayout-Generator bauen**
   - Viele Module verwenden wiederkehrend `FUN_004e9f30` fuer Field-Registration und `FUN_004ea280`/verwandte Funktionen fuer Serialisierung.
   - Ein Skript sollte aus Ghidra-Exports automatisch Modul-ID, Operationen, Field-Indizes, Typen, Offsets und String-/Data-Laengenregeln extrahieren.
   - Das reduziert Fehler beim manuellen Rekonstruieren der 100+ Netzwerkpakete.

7. **Live-Capture-Loop etablieren**
   - Vorgehen pro Schritt: Client verbinden, verschluesselten Wrapper loggen, entschluesseln, inneres Modul/opcode/Fields parsen, Antwort bauen, naechste Client-Reaktion erfassen.
   - `AlefLogin` sollte dafuer strukturiertes Logging fuer Rohdaten, entschluesselte Frames, Modulnamen, Operationen, Field-Masks und Sequenznummern bekommen.

8. **World-/Character-Bootstrap rekonstruieren**
   - Nach Login muessen mindestens Character-List, Character-Select, World-ID, Position, Entity-Spawn und Map-/Region-Daten verstanden werden.
   - Relevante Module aus den bisherigen Notizen: [`AgpmCharacter`](../Module/AgpmCharacter.md) (`0x02`), [`AgpmItem`](../Module/AgpmItem.md) (`0x04`), [`AgpmWorld`](../Module/AgpmWorld.md) (`0x18`) und Connect-/World-Manager-Pfade.

9. **Server-Datenbankschema ableiten**
   - Aus den Paketfeldern lassen sich Tabellen nur schrittweise ableiten.
   - Sicher zu erwartende Bereiche: Accounts/Sessions, Characters, Appearance/Customization, Inventory/Equipment/Bank, Skills, Quests, Guilds, Party, Trade, Auction, Wanted/GuildBattle und World-State.
   - Jedes erkannte Feld sollte mit Quelle markiert werden: live empfangen, statisch aus Sendefunktion, statisch aus Receivefunktion oder aus World-/Config-Datei abgeleitet.

10. **Noch offene Deep-Dives**
    - Vollstaendiger `AgpmItem`-Nested-Builder inklusive Subops `0..0x20`.
    - Guild/GuildMark/GuildBattle und Service-NPC-Jump-Tables.
    - Charaktererstellung und Charakteranpassung auf Paket- und Datenbankebene.
    - World-Dateien mit runtime IDs: Verknuepfung von MA1/MA2/DFF/TXD/Octree/Regionen zu Server-seitigen Spawn- und Navigationsdaten.

## Praktische naechste Reihenfolge

1. `AlefLogin`-README und Status-Doku auf den echten Code-Stand bringen.
2. Live-Test gegen Client laufen lassen und klaeren, ob Serverantworten mit `ENCODE_KEY` oder `DECODE_KEY` verschluesselt werden muessen.
3. Das erste vom Client nach Sign-On kommende Paket entschluesselt dokumentieren.
4. Den noetigen `AgcmLogin`-/[`AgcmConnectManager`](../Module/AgcmConnectManager.md)-Antwortpfad implementieren.
5. Danach iterativ Character-List, Character-Select und World-Enter entschluesseln.
