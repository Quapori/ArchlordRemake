# Winsock-Sequenz 19: Automatischer Connect nach der Serverauswahl

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ursache

Das nach Klick auf einen Server und Connect erwartete automatische Ereignis ist
AGCMLOGIN_CB_CHARACTER_NAME_FINISH (Callback/Event 7) des Moduls AgcmLogin.
Der Callback ist im Client korrekt registriert. Er feuert nicht, weil der Server
die einzige ihn ausloesende Protokollnachricht nicht sendet:

    AgpmLogin / AgcmLogin Operation 5
    AGPMLOGIN_CHARACTER_NAME_FINISH

Der reale Trace endet nach Client-Op 3 (UNION_INFO) und der Serverantwort Op 3
(UNION_INFO). Er enthaelt weder Op-4-Namen noch die zwingende Abschlussmeldung
Op 5. Deshalb bleibt der Client im Server-Select-/Loading-Zustand stehen und
sendet keine Operation 6.

## Beweis im Client

Die originale Clientquelle registriert in AgcmUILogin::OnAddModule explizit:

    pcmLogin->SetCallbackCharacterNameFinish(
        CBGetMyCharacterNameFinish, this);

Der zentrale AgcmLogin::OnReceive-Switch loest den Callback nur in diesem Fall
aus:

    case AGPMLOGIN_CHARACTER_NAME_FINISH:
        EnumCallback(AGCMLOGIN_CB_CHARACTER_NAME_FINISH,
                     (PVOID) pszAccount, (PVOID) ulNID);
        break;

AgcmUILogin::CBGetMyCharacterNameFinish fuehrt anschliessend genau den
gewollten Connect-Fortschritt aus:

1. setzt AGCMLOGIN_MODE_WAIT_MY_CHARACTER;
2. schliesst die Serverauswahl;
3. zeigt den Loading-Screen;
4. ruft AgcmLogin::SendGetCharacters(world, account) auf.

Der letzte Aufruf erzeugt die im Serverlog fehlende Client-Anfrage
AGPMLOGIN_CHARACTER_INFO (Operation 6).

## Warum der Callback nicht manuell gefeuert werden darf

Ein Force-Fire von Event 7 umgeht die Protokollzustandsmaschine. Es kann zwar
den naechsten Request sichtbar machen, ist aber keine Loesung: Der Client hat
die accountweite Charakterlistenphase dann nie normal abgeschlossen und der
Zustand kann bei weiteren UI- oder Charakterlistenereignissen inkonsistent
werden. Das Event ist kein Timer und kein lokaler UI-Trigger, sondern der
Empfangsabschluss einer Serverantwort.

## Exakte serverseitige Loesung

Nach Verarbeitung von Client-Op 3 muss der Server in dieser Reihenfolge senden:

    1. Op 3  UNION_INFO
    2. Op 4  CHARACTER_NAME, einmal je vorhandenem accountweiten Eintrag
    3. Op 5  CHARACTER_NAME_FINISH, immer, auch bei null Eintraegen

Der originale Server macht exakt das in AgsmLoginDB::ProcessGetUnion:

    SendUnionInfo(...);
    for (jeder Datenbankeintrag)
        SendCharacterName(name, total, slot, client);
    SendCharacterNameFinish(account, client);

Die Op-5-Nutzlast ist minimal und eindeutig:

| Hauptfeld | Wert |
|---|---|
| Operation, Bit 0 | 5 |
| AccountID, Bit 2 | 49-Byte, NUL-gepaddeter Accountname |
| alle anderen Felder | nicht gesetzt |

Daraus folgt die Hauptmaske 0x0005 (Bits 0 und 2). Es gibt kein nested
CharDetailInfo, keine CID und keinen WorldName in dieser Abschlussmeldung.
Die Nachricht muss wie die vorangehenden Loginantworten auf derselben aktiven
TCP-Verbindung verschluesselt und im richtigen Wrapper/Sequenzkontext gesendet
werden.

Bei einem frischen Account ist Op 4 optional, Op 5 aber weiterhin Pflicht.
Der originale Ablauf sendet das Finish ausserhalb der Schleife und damit auch
bei null Datenbankzeilen.

## Abgrenzung

- Die Union-Antwort Op 3 allein aktiviert Event 5, nicht Event 7.
- Op 7 ist ein anderer Abschluss: CHARACTER_INFO_FINISH und triggert Event 8,
  nachdem der Client seine Op-6-Abfrage gestellt hat.
- Die spaetere 3D-Anzeige braucht zusaetzlich das separate AgpmCharacter-Add-
  Paket, wie in Sequenz 18 beschrieben. Das ist nicht die Ursache dafuer, dass
  Connect aktuell nicht weitergeht.

## Verifikation nach der Korrektur

Der erwartete neue Logabschnitt ist:

    Client -> Server: AgcmLogin Op 3 (UNION_INFO)
    Server -> Client: AgcmLogin Op 3 (UNION_INFO)
    Server -> Client: AgcmLogin Op 5 (CHARACTER_NAME_FINISH)
    Client -> Server: AgcmLogin Op 6 (CHARACTER_INFO)

Erscheint Op 6 direkt nach der Op-5-Antwort, feuert der Client-Callback wieder
nativ. Erst dann ist die naechste Analysephase die Antwort auf Op 6
(Character-Add-Daten und Op 7), nicht mehr die Serverauswahl.

## Quellen

- Referenzclient: EP8-c++-Source\Modules\AClient\AgcmLogin\AgcmLogin.cpp,
  Zeilen 160-175 und 902-943.
- UI-Callback: ...\AClient\AgcmUILogin\AgcmUILogin.cpp, Zeilen 2814-2849.
- Referenzserver: ...\AServer\AgsmLoginClient\AgsmLoginClient.cpp,
  Zeilen 1461-1495, und AgsmLoginDB.cpp, Zeilen 1801-1816.
- Live-Beleg: AlefLogin/server.log, Arbeitsphase 2026-09-08 18:29:01 UTC.
