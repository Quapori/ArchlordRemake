# WINSOCK_SEQUENCE_37: Monster-Gegenangriff sendet Schaden, aber keine Animation

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

## Auflösung am 26.09.2026 (Code korrigiert, Neustart und Live-Retest ausstehend)

Der Gegenangriff erreicht `ActionCharacter`: Der Mitschnitt
`analysis/monster_attack_action_gates_20260926_combat.jsonl` zeigt für
Monster-CID `7_180_001` erfolgreiches `CheckEnableActionCharacter` und
`CheckActionStatus`, danach `ActionCharacter`-Rückgabe 0, ohne Ziel-Lookup
oder Callback 19. Die Binärdatei prüft unmittelbar davor `[Character+0x790]`
und ruft bei gesetztem Wert Callback 85 (`GET_ITEM_LANCER`) auf. Ein weiterer
lesender Mitschnitt (`analysis/monster_ridable_field_20260926.jsonl`) zeigt
das Flag für Monster-CID `7_180_002` tatsächlich als **1**, für den Spieler
hingegen als 0. Im Referenzquellcode ist dieses Feld `m_bRidable`; bei
fehlendem `IsTransform`-Feld dekodiert der Client zunächst `-1`, dessen
`RIDABLE`-Bit gesetzt ist. `build_monster_add_packet` sendet nun dieses
Feld ausdrücklich mit Wert 0. Damit sollte die Lancer-Prüfung entfallen und
die Monster-Angriffsanimation erreichbar sein. Die Wirkung muss nach
Serverneustart am Client bestätigt werden.

Gleichzeitig traten viele „Miss“ trotz sichtbar
automatischem Anlauf auf. Das Serverlog belegt, dass dies serverseitige
Reichweitenablehnungen sind, keine zufälligen Trefferwürfe: `CharAction`
für Boar-CID `7_180_002` traf bei gemessenem Serverabstand 2.870 bis
3.961 (Schwelle 100) ein. Der automatische Anlauf des Clients sendet in
diesem Build keine passenden `CharMove`-Updates; deshalb stimmt die
gespeicherte Serverposition nicht mit der sichtbaren Position überein.
`handle_char_action_request` gleicht bei einem vom Client lokal
reichweitengeprüften Angriff auf ein bereits bekanntes, lebendes Monster
die gespeicherte Position auf 75 Einheiten vor dem Ziel ab. Das ist eine
Annäherung anhand der letzten bekannten Anlaufrichtung, keine exakt
übertragene Clientposition; Multiplayer-Sichtbarkeit und Missbrauchsschutz
brauchen einen eigenen End-to-End-Test.

Die Vermutung zu den Spawnradien war ebenfalls richtig:
Migration `0037` gibt den getesteten Boar-Regeln `3180` und `3181` Radien
von 2.511,7 bzw. 2.883,8. Dieselben großen Werte wurden bisher sowohl
für die Verteilung der 5 Instanzen um das Camp als auch ein zweites Mal
als Leine **um jede einzelne Instanz** verwendet. Ein Boar konnte somit
mehrere Tausend Einheiten vom Camp wegwandern. Die Leine für zufälliges
Leerlaufwandern ist im Code nun auf höchstens 300 Einheiten um seine
Instanzposition begrenzt; die ursprüngliche Spawnverteilung bleibt erhalten.

Zusätzlich verwendet der EXP-Faktorupdate nach einem Kill nun den bereits
belohnten Charakterzustand, und der Respawntimer wird vor fehlbaren
Belohnungsschritten gesetzt. Ein Belohnungsfehler unterdrückt auch die
Trefferantwort an den Client nicht mehr. `cargo test -p alefgame-server --offline
--locked -q` besteht mit 21 Tests. Der laufende Release-Server verwendet
noch den alten Stand; Live-Wirkung für Animation, Angriff, EXP, Gold und
Drops bleibt bis zum Neustart ungeprüft.

## KORREKTUR (2026-09-26, nach Erstfassung dieses Dokuments)

**Die zentrale Schlussfolgerung unten ("`EnumCallback` feuert nie mit
Monster-CID") ist durch einen Messfehler nicht belegt und wird hiermit
zurückgezogen.** Der Fehler liegt hier: `observe_monster_attack_
callback.js`'s `isTrackedCid()` akzeptierte Monster-CIDs nur im Bereich
`4_000_000..4_999_999`. Echte Instanz-CIDs sind aber `MONSTER_CID_BASE
(4_000_000) + rule.id * 1000 + slot` (`monsters.rs`) -- bei größeren
`rule.id`-Werten liegt das WEIT über 5 Millionen. Der dokumentierte
Testgegner in Lauf 3 hatte laut Server-Log tatsächlich CID `7_123_00x`
(siehe unten), weitere reale Fälle erreichen `7_420_004`. Der alte Filter
hat JEDE Monster-CID aus allen drei Aufnahmen stillschweigend verworfen --
die "null Treffer"-Beobachtung ist deshalb ein Artefakt des Filters, kein
Beleg dafür, dass der Client die Callback-Kette tatsächlich nie erreicht.

Der Filter ist jetzt korrigiert (`id >= 4_000_000 && id < 100_000_000`).
Der Rest dieses Dokuments (ursprüngliche Fassung) bleibt unten stehen, weil
die Methode (Adress-Relokation, Tooling, offene Fragen) weiterhin gültig
ist -- nur die "Ergebnis"/"Schlussfolgerung"-Abschnitte sind mit dieser
Korrektur zu lesen, nicht als bestätigter Befund. Eine erste korrigierte
Kurzaufnahme erfasste in etwa 12 Sekunden 51.657 Callbacks und 145
verschiedene Monster-CIDs. Die große Rohdatei wurde nach Auswertung
entfernt. Die Aufnahme enthielt keinen im Serverlog bestätigten Gegenangriff;
die Ursache der fehlenden Angriffsanimation ist damit weiter offen.

Eine zweite Korrektur am Argument zur Callback-Kette: In der verfügbaren
Referenzquelle ruft [`AgpmCharacter`](../Module/AgpmCharacter.md):ProcessActionPacket` den ersten Callback
`AGPMCHAR_CB_ID_CHECK_NOW_UPDATE_ACTION_FACTOR` mit `pvBuffer` als `pClass`
auf, nicht mit dem Angreifer. Die frühere Aussage „in jedem EnumCallback ist
`pClass` der Angreifer“ ist somit ebenfalls falsch. Der spätere
`AGPMCHAR_CB_ID_RECEIVE_ACTION`-Aufruf verwendet den Angreifer. Im
Referenz-Header entsprechen `RECEIVE_ACTION` der ID 58 und
`ACTION_ATTACK` der ID 19; diese Zuordnung muss für den konkreten
2017er Client im echten Kampffenster überprüft werden.

### Korrigierter Mitschnitt mit echtem Gegenangriff

`analysis/monster_attack_callback_20260926_attack_long.jsonl` und das
gleichzeitige `AlefLogin/gameserver.log` belegen vier Gegenangriffe von
Monster-CID `7_234_000` um 19:37:35, :37, :39 und :41 UTC. Für diese CID
feuerte im Client jeweils Callback **58** (`RECEIVE_ACTION`, Rückgabe 1),
aber kein einziges Mal Callback **19** (`ACTION_ATTACK`). Beim Spieler
(CID 3) feuerte Callback 19 im selben 14-Sekunden-Fenster 27-mal. Der
Paketempfang und `ProcessActionPacket` funktionieren also für Monster;
der Abbruch liegt im anschließenden `ActionCharacter`-Pfad vor dem
Animations-Callback. Der aktuelle 2017er Binärcode ruft nach Callback 58
an `0x50580e` die Funktion `0x50f220` auf. Deren Angriffsfall prüft bei
`0x50f327` und `0x50f339` zwei Zustandsfunktionen, bevor die Zielprüfung
und Callback 19 folgen. Das Messwerkzeug kann diese drei Einstiege nun
mit `--action-gates` beobachten. Die genaue scheiternde Prüfung ist noch
zu messen; aus dem bisherigen Fenster allein ergibt sich keine sichere
Server-Paketkorrektur.

## Ursprüngliche Fassung (Befund unten ungültig, siehe Korrektur oben)

2026-09-26. Ausgangspunkt: Normalangriff (Spieler -> Monster) und Monster-Aggro/
Gegenangriff (Monster -> Spieler) sind live bestätigt funktionsfähig, was
Schaden und HP-Synchronisation angeht (siehe `combat.rs`'s `tick_monster_combat`
und `apply_damage`). Beobachtet: beim Gegenangriff sinkt die HP des Spielers
nachweislich, aber es spielt keine Angriffsanimation des Monsters.

## Ausgangsthese (aus echtem Quellcode)

`AgsmAI2::AttackEnemy` (Server, `Modules/AServer/AgsmAI2/AgsmAI2.cpp:3693`) löst
einen Monster-Angriff über exakt dieselbe Funktion aus wie einen Spieler-Angriff:
`AgpmCharacter::ActionCharacter`. Client-seitig (`AgpmOptimizedPacket2::
OnReceiveCharAction`, `AgpmOptimizedPacket2.cpp:383-458`) läuft ein eingehendes
`0x41`-CharAction-Paket durch dieselbe Kette, unabhängig davon, ob CID=Spieler
oder CID=Monster der Angreifer ist:

```
OnReceiveCharAction
  -> pcsCharacter = GetCharacterLock(lCID)      // lCID = ANGREIFER
     if (!pcsCharacter) return FALSE;           // <- einzige Vor-Bedingung
  -> ProcessActionPacket(pcsCharacter, pcsTargetChar=GetCharacter(lTargetID), ...)
     -> EnumCallback(AGPMCHAR_CB_ID_RECEIVE_ACTION, pcsCharacter, pvBuffer)
     -> ActionCharacter(AGPDCHAR_ACTION_TYPE_ATTACK, pcsCharacter, pcsTargetChar, ...)
        -> CheckEnableActionCharacter / CheckActionStatus(pcsCharacter, ...)
        -> pcsTargetCharacter = GetCharacterLock(pcsTargetBase->m_lID)  // TARGET, erneut
        -> AgpmFactors::IsInRange(...)
        -> EnumCallback(AGPMCHAR_CB_ID_ACTION_ATTACK, pcsCharacter, pvBuffer)  // <- Animation
```

In JEDEM dieser `EnumCallback`-Aufrufe ist das zweite Argument (`pClass`) der
ANGREIFER (`pcsCharacter`). Das ergibt eine direkt testbare Vorhersage: Wenn
der Monster-Gegenangriff dieselbe Kette durchläuft, muss `EnumCallback`
irgendwann mit `pClass` = Monster-CID aufgerufen werden.

## Methode

Wichtiger Fund VOR der eigentlichen Messung: `C:\Spiele\Archlord\AlefClient.exe`
hat sich seit der letzten Analyse (23.09., `WINSOCK_SEQUENCE_36`) geändert
(SHA256 `20009faa5db75de88ec09ae11324d479f85946b5ca37ad3c64ec4dcac29e067b`,
vorher `0336f7978c258c3121d115c0bdc14be410f85003ebc8dd8181c276cde13d4fbc`).
PE-Zeitstempel (`0x5992c8ec` = 2017-08-15) bestätigt weiterhin den richtigen
Build; nur die konkrete Kopie an diesem Pfad ist eine andere. Alle in
`observe_skill_gate.py` hart codierten Adressen sind damit für diese Datei
ungültig.

Die Funktion `EnumCallback` (generischer Dispatcher, jede `AgpmXXX`-Modul-Klasse
nutzt dieselbe Implementierung: `this[0x5dc + id*4]` als Kopf einer
Callback-Liste je ID -- exakt die Notiz in `combat.rs`'s Modul-Dokumentation)
wurde per 8-Byte-Prologsignatur aus der alten Messung (`skill_gate_
20260923_before.jsonl`, Probe `callbacks`) in der NEUEN Datei eindeutig
neu lokalisiert: ein einziger Treffer bei `0x4e4040` (alt: `0x4e4070`).
Neues Tool: `AlefLogin/tools/observe_monster_attack_callback.py`/`.js`.
Es hookt ausschließlich diese eine Funktion, liest `pClass` als `ApBase*`
(`m_eType`@0, `m_lID`@4 -- Layout aus `observe_skill_gate.js`'s `base()`
übernommen) und filtert auf die Spieler-CID sowie den Monster-CID-Bereich
(`4_000_000..5_000_000`).

## Ergebnis: drei Live-Aufnahmen (ungültig, siehe Korrektur oben -- Monster-CID-Filter war zu eng)

1. **Lauf 1** (60s, versehentlich ohne echten Kampf): 20.815 `EnumCallback`-
   Aufrufe, ausnahmslos mit `pClass.id == 3` (Spieler). Keine Monster-CID.
2. **Lauf 2** (60s, Spieler griff an + wurde zurückgeschlagen, bestätigt im
   Server-Log): dieselbe Beobachtung -- nur CID 3.
3. **Lauf 3** (60s, mit zusätzlichem `callerRva`-Feld; Server-Log zeigt im
   Fenster 19:11:32-37 UTC 5 Spieler-Treffer und 3 Monster-Gegenangriffe):
   1.675 `EnumCallback`-Aufrufe in diesem Fenster, wieder **ausschließlich**
   `pClass.id == 3`.

Lauf 3s Ausschnitt für exakt das Kampffenster (19:11:31-38 UTC) ist gesichert
in `analysis/monster_attack_callback_20260926_combat_window.jsonl` (die vollen
~6-10MB je Lauf wurden nicht committet, nur dieser fokussierte Ausschnitt).

**In keinem der drei Fenster ist `EnumCallback` jemals mit einer Monster-CID
als `pClass` aufgerufen worden** -- trotz bestätigter echter Gegenangriffe
mit Schaden/HP-Sync in Läufen 2 und 3. Für CID 3 feuert derselbe Dispatcher
dagegen tausendfach pro Minute (Bewegung, Animation, Statuswechsel), inklusive
mehrerer niedrigfrequenter IDs, die klar mit den geloggten Spieler-Treffern
korrelieren (z. B. `id=12`/`id=11` an eng benachbarten Aufruferadressen,
5 Treffer bei 5-6 gelandeten Spieler-Hits im Fenster -- diese Funktion liest/
schreibt `[Character+0x52a]`, dasselbe Feld, das `monsters.rs`'s
`MONSTER_ACTION_STATUS_ALIVE`-Kommentar bereits als vielfach gegateten
Status-Wert dokumentiert).

## Schlussfolgerung (ungültig, siehe Korrektur oben)

Da laut Quellcode **jeder** Schritt der Verarbeitungskette ab
`ProcessActionPacket` (inklusive des allerersten `EnumCallback`-Aufrufs,
`AGPMCHAR_CB_ID_RECEIVE_ACTION`) den Angreifer als `pClass` durchreicht, und
dieser Aufruf für Monster-als-Angreifer nachweislich NIE stattfindet, wird
diese gesamte Kette für das Monster-Gegenangriffspaket serverseitig korrekt
gesendet, aber client-seitig **nie erreicht**. Der einzige vorgeschaltete
Schritt in `OnReceiveCharAction` ist `GetCharacterLock(lCID)` (Angreifer-CID).
Das ist die engste belegbare Eingrenzung: entweder scheitert die Suche selbst
(unwahrscheinlich -- dieselbe CID wird über `GetCharacter` ohne Lock
zuverlässig für Rendering/HP-Anzeige gefunden) oder der zusätzliche Schritt,
den `GetCharacterLock` gegenüber `GetCharacter` hat: `pcsCharacter->m_Mutex.
WLock()`.

Wichtig: Dieser exakte Pfad -- eine Monster-Instanz als AKTEUR (nicht nur als
Ziel) einer `ActionCharacter`-Aktion -- wurde in diesem Projekt vor der
heutigen Aggro/Gegenangriff-Funktion nie durchlaufen (Monster waren bis dahin
ausschließlich passives Ziel, nie Angreifer). Es handelt sich also plausibel
um eine echte Client-Eigenheit bei genau dieser (bisher unbenutzten)
Kombination, nicht um einen Reichweiten- oder Timing-Fehler.

## Nicht abschließend bewiesen

`GetCharacterLock`s exakte Adresse in der aktuellen Datei wurde NICHT
gefunden. Mehrere indirekte Suchansätze (Aufrufer-Adressen bekannter
`EnumCallback`-IDs über `callerRva` zurückverfolgen, Byte-Signatur-Suche nach
Aufrufern einer als Status-Setter identifizierten Nachbarfunktion `0x501690`)
führten zu benachbarten, aber nicht eindeutig identifizierten Funktionen
(u. a. eine Kandidatenregion um `0x50e8a0`-`0x50ea40`, die strukturell zu
Angriffsintervall-Berechnung und Status-Übergängen passt, deren
`EnumCallback`-Aufrufe darin aber in keinem der drei Läufe je mit einer
verfolgten CID als `pClass` auftraten -- passt zu Aufrufen mit `pvBuffer`
statt Charakter-Pointer als zweitem Argument, wie es für
`AGPMCHAR_CB_ID_CHECK_NOW_UPDATE_ACTION_FACTOR` im echten Quellcode
dokumentiert ist, beweist aber nicht, dass diese Region tatsächlich
`ActionCharacter`/`ProcessActionPacket` ist).

Bekannt und für spätere Läufe wiederverwendbar:
- `EnumCallback`: `0x4e4040` (stabil, per Signatur bestätigt).
- `AgpmCharacter`-Modulinstanz zur Laufzeit (ein Beispiel-Lauf):
  `0x1536d9f8` (ändert sich pro Prozessstart, aber die Identifikationsmethode
  -- "welches Modul feuert die `+0x52a`-Statusfunktion" -- ist reproduzierbar).
- Funktion `0x501690`: liest/schreibt `[Character+0x52a]` (ActionStatus),
  ruft `EnumCallback` mit IDs 12 (davor) und 11 (danach) auf, ruft bedingt
  `0x67fab0` auf, wenn `ActionStatus == 2` UND ein übergebenes Word-Argument
  matcht -- plausibel `SetActionStatus`.
- Sechs Aufrufer von `0x501690`: `0x507b0d`, `0x508d55`, `0x50e8cb`,
  `0x50ebc0`, `0x50f06a`, `0x5acd7d`. Keiner davon ist bislang sicher als
  `ActionCharacter` identifiziert.

## Reproduzierbarkeit

```powershell
"C:\Program Files\Python313\python.exe" AlefLogin\tools\observe_monster_attack_callback.py `
  --pid <AlefClient-PID> --seconds 60 --output AlefLogin\analysis\monster_attack_callback_<ts>.jsonl
```

Vor jedem Angriff-Zyklus im Fenster wirklich angreifen lassen UND einen
Gegenangriff abwarten; danach `gameserver.log` auf `combat: monster
counter-attack landed` im selben Zeitfenster prüfen, um das Aufnahmefenster
zu validieren (Lauf 1 dieser Arbeitsphase war sonst ergebnislos, weil gar kein
Kampf stattfand).

## Nächste Schritte (nicht heute)

1. `GetCharacterLock` (oder direkt `OnReceiveCharAction`) präzise lokalisieren
   -- z. B. über eine Vtable-losen Pattern-Scan der Aufrufer von `GetCharacter`
   (der ungelockten Schwesterfunktion), oder über den Paket-Dispatch-Pfad von
   [`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md) für Modul-Subtyp `0x41`.
2. `WLock()`/`m_Mutex` direkt hooken, sobald das Objekt bekannt ist, um zu
   bestätigen, ob es für Monster-Instanzen als Angreifer tatsächlich
   fehlschlägt (und warum -- Kontention, fehlende Initialisierung, o. Ä.).
3. Erst danach eine serverseitige Gegenmaßnahme ableiten -- ohne bestätigte
   Ursache aktuell keine Code-Änderung an `combat.rs` vorgenommen.
