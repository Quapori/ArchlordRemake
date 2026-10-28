# Winsock-Sequenz 30: Weltbeitritt-Meilenstein und Bewegungs-Recherche

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-13

## Meilenstein: kompletter Weltbeitritt live funktionsfaehig

Nach `LOADING_COMPLETE` sendet `alefgame-server` jetzt die volle
`EnterGameWorld`-Sequenz (`AgsmCharManager.cpp:1024-1121`, auf den fuer
dieses Projekt gewaehlten Umfang verengt):

1. Self-[`AgpmCharacter`](../Module/AgpmCharacter.md)-Add (Status `IN_GAME_WORLD`, da der Client sein
   lokales Charakterregister direkt vor `LOADING_COMPLETE` per
   `RemoveAllCharacters()` geleert hat).
2. Jedes ausgeruestete [`AgpmItem`](../Module/AgpmItem.md)-Add.
3. `SETTING_CHARACTER_OK`.

**Live verifiziert 2026-09-13**: der Charakter betritt die Welt tatsaechlich,
landet in der Startstadt (korrekter rassenabhaengiger Spawn-Anker statt
Kartenursprung), das 2D-UI zeigt Level/HP/Geld korrekt an (Level testweise
per direkter DB-Aenderung auf 50 gesetzt und korrekt im UI bestaetigt).

Dazu kam eine echte Sicherheitsluecke und ein Identitaetsfehler, beide
behoben:

- **Handoff-Sicherheit**: `alefgame-server` akzeptierte vorher jeden
  `REQUEST_CLIENT_CONNECT` allein nach Charaktername. Jetzt erzeugt
  `aleflogin-server`s `AGPMLOGIN_ENTER_GAME`-Handler einen kurzlebigen,
  einmaligen Handoff-Token (neue Tabelle `game_handoff_sessions`), den
  `alefgame-server` beim Connect pruefen und verbrauchen muss.
- **CID-Identitaet**: das aeussere "CID"-Feld im `ENTER_GAME`-Request ist
  tatsaechlich `memberBillingNum` (bestaetigt in `AgcmLogin.cpp:971-987`,
  ausserhalb `_AREA_KOREA_`-Builds fest `0`), keine echte Charakter-ID. Die
  echte CID wird jetzt serverseitig ueber Account+Welt+Name aufgeloest.

Siehe Commit `66cff07` fuer die vollstaendige Implementierung.

## Offen: Bewegung ("Zeitlupeneffekt")

Nach dem Weltbeitritt kann sich der Charakter nicht normal bewegen --
sichtbarer Zeitlupeneffekt. `alefgame-server` verarbeitet bislang gar keine
Bewegungspakete (Dispatcher reagierte nur auf Modul `0x03`).

### Fund: der Client nutzt ein drittes, bisher unbekanntes Wire-Format

Ein Blick in das laufende `alefgame-server`-Log (jedes empfangene Paket wird
bereits im Klartext geloggt) zeigt: waehrend der Bewegung sendet der Client
kontinuierlich Pakete mit **Opcode `0x40`**, nicht das erwartete `0x02`
(`AgpmCharacter`/`UPDATE`). Bestaetigt gegen die reale Quelle:

```
AGPMOPTIMIZEDCHARMOVE_PACKET_TYPE = 0x40   (Include/ApDefine.h:659)
```

Das ist [`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md):m_csPacketCharMove` -- ein DRITTES, separates
Feld-Layout auf derselben Klasse, die wir schon fuer die Charakterauswahl-
Ausruestung (`m_csPacket`, Opcode `0x42`) reverse-engineert hatten.
Feldliste (`AgpmOptimizedPacket2.cpp:109-122`, 1-Byte-Maske):

| Bit | Feld | Typ |
|---:|---|---|
| 0 | CharacterID | INT32 |
| 1 | CurrentPosition | POS (3xFLOAT) |
| 2 | DestinationPosition | POS (3xFLOAT) |
| 3 | FollowTarget | INT32 |
| 4 | FollowDistance | UINT16 |
| 5 | MoveFlag | INT8 |
| 6 | MoveDirection | INT8 |
| 7 | NextActionType | INT8 |
| 8?| NextActionSkillID | INT32 (9. Feld bei nur 1-Byte-Maske -- im Original selbst fragwuerdig, siehe unten) |

### Fund: dieses Modul nutzt `MakePacket(bIsPacket=TRUE)`, nicht unsere sonstige Konvention

Alle drei realen Sende-Stellen (`AgpmOptimizedPacket2.cpp:1166,1232,1254`)
rufen `m_csPacketCharMove.MakePacket(TRUE, ...)` -- im Unterschied zu JEDEM
anderen bisher in diesem Projekt dekodierten Paket (immer `bIsPacket=FALSE`
-> Maske-zuerst-Konvention). `bIsPacket=TRUE` erzeugt stattdessen einen
kompakten `PACKET_HEADER` (`AuPacket.cpp:286-296`, `AuPacket::SetCID`):

```c
struct PACKET_HEADER { UINT16 len; UINT8 type; INT32 lOwnerID; };  // 7 Bytes
```

`SetCID(pvPacket, nPacketLength, lCID)` schreibt die CID direkt in
`lOwnerID` -- vermutlich ein Transport-/Routing-Feld fuer die reale
Mehrprozess-Serverarchitektur, zusaetzlich zum eigenen Anwendungsfeld
"CharacterID" (Bit 0) in der Feldliste selbst (auch von `GetField`
ausgelesen, `AgpmOptimizedPacket2.cpp:333-343`).

**Das erklaert, warum unsere sonst zuverlaessige Annahme "9 Byte
Header, immer Null" fuer dieses Modul nicht passt** -- dieses Paket hat
gar keinen festen 9-Byte-Header, sondern diesen abweichenden
`PACKET_HEADER`-Aufbau.

### Noch nicht geloest: der exakte Byte-Versatz

Ein erster Versuch, das reale geloggte Paket

```
d6 2d 00 40 00 03 00 00 00 5e 72 00 00 67 03 00 00 00 00 85 e8 c8 60 46 ...
```

anhand von `[D6][len:u16][opcode][PACKET_HEADER: len:u16+type:u8+ownerID:i32][maske][felder]...[6B]`
zu dekodieren, ergab keine plausiblen Werte (die vermutete `ownerID` an
Byte-Position 3-6 des inneren Headers ergibt keine sinnvolle kleine CID).
Reine Quellenlektuere reicht hier nicht aus, um die exakte Verschachtelung
zweifelsfrei zu bestimmen -- das braucht entweder einen Live-Speicher-Hook
auf `AuPacket::SetCID` bzw. `AgpmOptimizedPacket2::MakePacketMove`-Aequivalente
im eigenen Client (gleiche Trampolin-Technik wie in
`WINSOCK_SEQUENCE_29`), oder eine sorgfaeltigere manuelle Nachverfolgung der
`MakePacket(TRUE, ...)`-Implementierung selbst (`AuPacket.cpp`, um die
19-Byte-Bytefolge um `PACKET_HEADER` herum exakt zu bestimmen).

### Offene naechste Schritte

1. Live-Hook auf `AuPacket::SetCID` (oder die Sendefunktion, die
   `m_csPacketCharMove.MakePacket(TRUE, ...)` aufruft) im eigenen Client,
   um den exakten Byte-Aufbau direkt zu beobachten -- gleiche Methode wie
   in `WINSOCK_SEQUENCE_29`.
2. Serverseitige Antwort klaeren: `OnReceiveCharMove`
   (`AgpmOptimizedPacket2.cpp:313-381`) ruft nur
   `AgpmCharacter::ProcessMovePacket(...)` lokal auf dem Serverobjekt auf --
   es ist noch nicht geklaert, ob/welche explizite Antwort an den
   sendenden Client selbst noetig ist, um den Zeitlupeneffekt zu beheben
   (moeglicherweise reicht ein reines Anwenden+kein Echo, moeglicherweise
   braucht der Client eine Bestaetigung; das haengt von der noch nicht
   gelesenen Fortsetzung von `ProcessMovePacket` ab).
3. Nicht bestaetigt: ob die frei erfundenen `BASE_MOVEMENT_SPEED`/
   `BASE_MOVEMENT_SPEED_FAST`-Werte (100/150) im `FactorPacket`
   (`build_factor_packet`) ebenfalls zur Ursache beitragen -- `GetMoveSpeed`
   (`AgpmCharacter.cpp:5787-5814`) deutet eher auf serverseitige
   Bewegungs-Buchhaltung (Anti-Cheat-Validierung, Follow-Distanz) als auf
   einen direkten Client-Rendergeschwindigkeits-Multiplikator hin, aber das
   ist nicht abschliessend geklaert.

## Ergebnis 2026-09-13: Bewegung vollstaendig geloest

Alle drei offenen Punkte oben sind geklaert, kein Live-Hook noetig:

1. **Byte-Layout durch Diff-Vergleich echter Pakete geklaert**, nicht durch
   `PACKET_HEADER`-Rechnung: mehrere reale `0x40`-Pakete aus dem laufenden
   `alefgame-server`-Log nebeneinandergelegt zeigten sofort, welche Bytes
   konstant (CID, Maske) und welche variabel (Position, Richtung) sind. Die
   Maske liegt an Offset 13 (`0x67` = Bits 0,1,2,5,6 = CharacterID+
   CurrentPos+DestPos+MoveFlag+MoveDirection), Felder ab Offset 14 -- der
   normalen `D6...6B`-Rahmenkonvention folgend, nur mit einem nicht-leeren
   9-Byte-Header statt des sonst ueberall beobachteten Null-Headers.
   `alefgame-server` beantwortet das Paket jetzt mit einem Echo derselben
   Werte und persistiert die Zielposition.
2. **Restliche "Zeitlupe" war die erfundene `BASE_MOVEMENT_SPEED`**: die
   erste Korrektur (`AGPMCHAR_DEFAULT_MOVE_SPEED=4000`) machte die Bewegung
   doppelt so schnell wie erwartet -- bestaetigt wurde die Vermutung "200%
   Speed". Die tatsaechlichen Werte liegen in `ini\characterdatatable.txt`
   (entschluesselt mit `tools\decode_archlord_data.ps1`, derselben Quelle
   wie die STR/DEX/etc-Werte aus Migration 0005): Spalten "Movement Walk"/
   "Movement Run", fuer alle 14 spielbaren Templates identisch `2000`/`6000`.
   `AGPMCHAR_DEFAULT_MOVE_SPEED` ist offenbar nur ein generischer Fallback
   fuer Objekte ohne Templatedaten (Monster/NPCs), nicht das, was
   Spielercharaktere tatsaechlich benutzen.
3. **Antwortverhalten**: ein einfaches Echo derselben Paketwerte reicht aus
   -- die volle `ProcessMovePacket`-Logik (Pfadfindung, Blocking, Follow)
   war fuer den akuten Zeitlupeneffekt nicht die Ursache.

**Live verifiziert**: Bewegungsgeschwindigkeit ist jetzt korrekt, UND die
Position wird bei jedem Bewegungspaket persistiert -- ein Neulogin spawnt
den Charakter an der zuletzt bewegten Position statt am rassenabhaengigen
Spawnanker (der nur noch fuer Charaktere ohne je gespeicherte Position
greift). Siehe Commit fuer die vollstaendige Implementierung.
