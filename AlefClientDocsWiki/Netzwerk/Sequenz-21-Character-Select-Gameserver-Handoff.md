# Winsock-Sequenz 21: Charakterauswahl und Gameserver-Handoff

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ergebnis

Der sichtbare Charakter kann und muss vor einer Gameserver-Verbindung lokal
ausgewaehlt werden. Die Kausalitaet lautet nicht "erst mit Gameserver verbinden,
dann Charakter auswaehlen", sondern:

    lokale Charakterauswahl
      -> Client sendet AgcmLogin Operation 8
      -> Loginserver bestaetigt Operation 8 mit Zieladresse
      -> Client verbindet sich erst danach mit dem Gameserver

Der gegenwaertige Loginserver behandelt Operation 8 nicht. Sein Default-Zweig
protokolliert eine unbehandelte Operation und sendet keine Antwort. Selbst bei
korrekt ausgeloester Auswahl kann daher keine Gameserver-Verbindung entstehen.

## Aktueller Live-Stand

Im juengsten Serverlog endet der erfolgreiche Ablauf mit:

    Op 3 UNION_INFO
    Op 4 CHARACTER_NAME und Op 5 CHARACTER_NAME_FINISH
    Client Op 6 CHARACTER_INFO
    AgpmCharacter Op 0 Add
    Op 7 CHARACTER_INFO_FINISH

Nach Op 7 existiert in diesem Mitschnitt kein eingehender Login-Frame mit
Operation 8. Daher wurde entweder die eigentliche Enter-/Select-Schaltflaeche
noch nicht betaetigt oder die lokale Auswahl verwirft den Klick vor dem
Netzwerkversand. Der fehlende Gameserver ist zu diesem Zeitpunkt noch nicht
der unmittelbare Ausloeser, weil der Client dessen Adresse erst aus der
Op-8-Antwort erhalten wuerde.

## Verifizierter Client-Auswahlpfad

Der Ghidra-Output des vorliegenden alefclient.exe bestaetigt den Ablauf:

    FUN_0060e490  = LG_LoginMainSelectButtonClick
      -> FUN_0060d630
      -> FUN_0065e580
      -> AgcmLogin::SendEnterGame
      -> AgcmLogin Op 8

FUN_0060e490 prueft zuerst, ob AgcmUILogin + 0x1184 eine von Null verschiedene
ausgewaehlte CID enthaelt. FUN_0060d630 prueft zusaetzlich, ob
AgcmLogin + 0xc14 den Charakterauswahlmodus 7 hat. Nur dann ruft es den
Login-Sender auf und setzt den Modus auf 8 (Post-Login-Loading).

Daraus folgen zwei lokale Gates fuer einen nicht gesendeten Op-8-Request:

1. Die sichtbare Figur muss durch Slot-/Charakterklick tatsaechlich als
   Auswahl in AgcmUILogin + 0x1184 landen. Das sichtbare Modell allein reicht
   nicht.
2. Beim Klick auf die Enter-/Select-Schaltflaeche muss der Loginmodus noch 7
   sein. Ein vorzeitiger Wechsel des Modus verhindert den Aufruf.

Der Rueckgabewert von FUN_0060d630 ist kein Gameserver-Status. Er prueft nur
diese lokale Auswahl und ruft danach den Login-Paketsender auf.

## Operation 8: Client-Request

AGPMLOGIN_ENTER_GAME hat die numerische Operation 8. Der Client baut den
Request mit AgcmLogin::SendEnterGame wie folgt:

| Hauptfeld | Inhalt |
|---|---|
| Operation | 8 |
| AccountID | aktueller Account |
| WorldName | ausgewaehlte Welt, hier Brumhart |
| CID | Im Client-Request memberBillingNum, ausserhalb Korea 0 |
| CharDetailInfo | nested AuPacket: TID 0, CharName des ausgewaehlten Charakters |

Wichtig: Die echte Auswahlidentitaet im Client-Request ist der Charaktername
im nested CharDetailInfo, nicht das aeussere CID-Feld. Der originale
Loginserver liest in ProcessSelectCharacter den CharName und sucht damit den
persistierten Charakter. Ein neuer Handler darf den Request nicht wegen
aeusserem CID = 0 ablehnen.

## Operation 8: erforderliche Loginserver-Antwort

Die Antwort ist ebenfalls AgcmLogin Operation 8. Sie muss enthalten:

| Hauptfeld | Inhalt |
|---|---|
| Operation | 8 |
| CID | die echte persistente Charakter-CID, nicht 0 |
| CharDetailInfo | nested: echte TID und Charaktername |
| ServerInfo | nested: Gameserver-Adresse als fester 23-Byte-String, etwa IP:Port |

CharDetailInfo verwendet die bekannte zwei Byte breite Maske. ServerInfo
verwendet eine ein Byte breite Maske und genau ein AUTYPE_CHAR-Feld mit
AGPMLOGIN_IPADDRSIZE = 23.

Die Antwort darf erst erfolgen, wenn eine erreichbare Gameserver-Instanz fuer
die Welt feststeht. Der originale Server prueft die registrierte Weltzuordnung
und den Connected-Status des Gameservers, bereitet den Charakter fuer den
Handoff vor und schickt anschliessend SendEnterGameEnd.

## Wirkung der Antwort im Client

AgcmLogin::OnReceive verarbeitet die Antwortoperation 8 in dieser Reihenfolge:

    AGCMLOGIN_CB_ENTER_GAME
    -> OnEnterGame(CID, CharDetailInfo, ServerInfo)
    -> AgcmCharacter::SendEnterGameWorld(CharName, ServerAddress, CID)
    -> AgcmConnectManager::Connect(ServerAddress, GAMESERVER, ...)

OnEnterGame verlangt sowohl CharDetailInfo als auch ServerInfo. Fehlt eines
davon oder fehlen CharName bzw. Serveradresse, bricht der Pfad vor dem
Connect-Aufruf ab. SendEnterGameWorld speichert die Adresse, verbindet den
neuen Gameserver-Socket und setzt die Self-CID auf die CID aus der Op-8-
Antwort.

Ein beliebiger offener TCP-Port genuegt danach nicht: Nach dem Connect erwartet
der Client das Gameserver-Protokoll. Der Gameserver muss also mindestens den
anschliessenden Character-/World-Loginpfad bedienen. Der Loginserver muss
nicht schon fuer die lokale Auswahl mit ihm verbunden sein; fuer einen
realistischen Handoff braucht er aber ein zuverlaessiges Welt-zu-
Gameserver-Ziel.

## Konkrete naechste Messung

Beim naechsten Versuch genau einen Charakter-Slot anklicken und dann die
Enter-/Select-Schaltflaeche betaetigen. Der Serverlog muss unmittelbar danach
einen entschluesselten Frame mit Modul 0x0d und Operation 8 zeigen.

- Kein Op 8 im Log: Untersuchung bleibt lokal bei FUN_0060e490,
  FUN_0060d630, Auswahl-CID und Loginmodus 7.
- Op 8 im Log, danach "unhandled Operation": der aktuelle Loginserver-
  Handoff fehlt, wie der gelesene Handler bereits zeigt.
- Op-8-Antwort vorhanden, aber kein neuer TCP-Connect: ServerInfo-
  Verschachtelung, 23-Byte-Adresse und reale CID pruefen.
- Neuer Connect vorhanden, dann Abbruch: Beginn der separaten
  Gameserver-Protokollanalyse.

## Quellen

- Live-Protokoll: AlefLogin/server.log, Arbeitsphase ab 15:57:04 und
  Charakterdatenantwort um 15:59:59.
- Clientbinary: alefclient.pseudocode.c, FUN_0060e490, FUN_0060d630 und
  der Aufruf FUN_0065e580.
- EP8-Referenz: Modules/AClient/AgcmLogin/AgcmLogin.cpp
  (SelectCharacter, SendEnterGame, OnEnterGame) und
  Modules/AClient/AgcmCharacter/AgcmCharacter.cpp (SendEnterGameWorld).
- EP8-Referenzserver: Modules/AServer/AgsmLoginClient/AgsmLoginClient.cpp
  (ProcessSelectCharacter, SendEnterGameEnd).
