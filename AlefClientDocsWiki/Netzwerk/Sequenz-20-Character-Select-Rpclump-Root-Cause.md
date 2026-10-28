# Winsock-Sequenz 20: Ursache der leeren 3D-Charakterauswahl

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Live-Befund

Der aktuelle, erfolgreiche Anmeldeversuch zeigt, dass Persistenz und Weltzuordnung
nicht mehr die Ursache sind:

    15:29:12.006  world_name="Brumhart" -> world_id=1
    15:29:12.014  AGPMLOGIN_UNION_INFO ... count=1
    15:29:12.059  AGPMLOGIN_CHARACTER_INFO ... count=1

Der Client sendet anschliessend AgcmLogin Operation 6
(AGPMLOGIN_CHARACTER_INFO). Der Loginserver antwortet danach nur mit zwei
Frames des Moduls AgcmLogin (0x0d):

1. Operation 4: CHARACTER_NAME, erneut mit dem Namen aus der Slotliste.
2. Operation 7: CHARACTER_INFO_FINISH.

Im gesamten Log dieses Versuchs ist kein ausgehender Frame mit Modul-ID 0x02
(AgpmCharacter) vorhanden. Das ist die direkte Ursache dafuer, dass ein
persistierter Charakter in der Auswahl keinen 3D-Charakter erhaelt.

## Abgrenzung

Die Datenbank liefert bereits einen Charakter. Ein erneut gesendeter
CHARACTER_NAME-Eintrag erstellt jedoch kein AgpdCharacter-Objekt im Client.
Er aktualisiert nur die Login-/Slotinformationen.

Der Client kann den RenderWare-Clump deshalb nicht laden, weil er den einzigen
Einstiegspunkt fuer diesen Ablauf nicht erreicht:

    fehlendes AgpmCharacter Op 0 Add
      -> kein AgpmCharacter::OnOperationAdd
      -> kein AddCharacter(CID, TID, Name)
      -> kein UpdateInit
      -> kein AGPMCHAR_CB_ID_INIT
      -> kein AgcmCharacter::CBInitCharacter
      -> kein ResourceLoader / LoadTemplateData
      -> kein RpClumpClone

Das ist kein Fehler innerhalb von RpClumpClone, in den DFF-Dateien oder im
Octree. Die Ladepipeline wird derzeit gar nicht angestossen.

## Korrekte Reihenfolge nach der Weltwahl

Der Referenzserver behandelt die vom Client gesendete Login-Operation 6 wie
folgt:

    Client: AgcmLogin Op 6 fuer Account + Welt
    Server: fuer jeden Charakter AgpmCharacter (Modul 0x02), Op 0 Add
    Server: AgcmLogin Op 7 CHARACTER_INFO_FINISH

Die Referenzfunktion AgsmCharacter::SendCharacterAllInfo ruft zuerst
SendPacketChar auf. Dieses baut mit MakePacketAddCharacter den Character-Add-
Frame und sendet danach weitere Charakterdaten. Erst dann folgt der
Login-Abschluss Op 7.

Die aktuelle Implementierung dokumentiert selbst, dass fuer Op 6 die
vollstaendigen Daten ueber SendCharacterAllInfo in einem separaten Modul
fehlen. Stattdessen wiederholt sie die Namensliste. Diese Diagnose beschreibt
ausschliesslich die erforderliche Aenderung; es wurde kein Servercode
veraendert.

## Sendervertrag fuer den ersten funktionierenden Add-Frame

Der Add-Frame muss auf derselben bereits verschluesselten Socket-Session
gesendet werden und den normalen Wrapper-/Sequenzzaehler verwenden. Seine
innere Modul-ID ist 0x02, die Add-Operation ist 0.

Das AgpmCharacter-Hauptpaket verwendet eine vier Byte breite Feldmaske. Die
vollstaendige Referenzreihenfolge ist in Sequenz 18 dokumentiert. Fuer den
ersten validen Auswahl-Charakter muessen mindestens diese Daten aus dem
persistierten Datensatz bzw. Template kommen:

| Add-Feld | Anforderung |
|---|---|
| Operation | 0 (Add) |
| CID | Persistente characters.id, nicht 0 |
| TID | race_tid / Character-Template-ID, nicht 0 und im lokalen Client-Template vorhanden |
| GameID | Charaktername als AUTYPE_MEMORY_BLOCK mit u16-Laenge |
| Status | gueltiger Character-Status |
| Move-Paket | Als syntaktisch vollstaendiges nested AuPacket; der Originalsender liefert es immer |
| Face/Hair | Persistierte face_index und hair_index |
| Region, Action-Status, Geld, Bankgroesse, Eventflags | Persistierte Werte bzw. definierte Standardwerte |
| Factor-Paket | Fuer UpdateInit nicht zwingend, aber fuer einen produktionsnahen Charakter aus Template/Level/Items erzeugen |

CID und TID werden im Client zwingend geprueft. Bei Null wird der Add-Vorgang
vor der Objektanlage verworfen. TID ist auch der Schluessel zum lokalen
Character-Template und damit zum zu klonenden DFF-/Clump-Template.

Das Move-Paket darf nicht durch einen beliebigen Byteblock ersetzt werden. Es
hat eine ein Byte breite Feldmaske und die Felder aktuelle Position,
Zielposition, Follow-Ziel, Follow-Distanz, Turn-X, Turn-Y, Move-Flags und
Richtung. Fuer die Auswahl wird die sichtbare Position anschliessend von der
UI auf den Slot gesetzt, aber ein originalgetreu aufgebauter Move-Block
vermeidet einen unvollstaendigen Bewegungszustand.

## Datenluecke im aktuellen Sender

Die vorhandene Datenbankabfrage liest bereits race_tid, hair_index und
face_index, aber nicht characters.id. Die Rust-Struktur Character und
list_characters in AlefLogin/crates/aleflogin-server/src/db.rs muessten fuer
einen spaeteren Add-Sender die persistente ID ebenfalls auswaehlen. Die
Erstellung liefert diese ID bereits mittels RETURNING id.

Die Namensliste kann fuer den UI-Vorlauf bestehen bleiben. Sie ersetzt weder
CID noch TID noch die AgpmCharacter-Dispatch-Kette und darf daher nicht als
Ersatz fuer den Add-Frame betrachtet werden.

## Verifikation nach einer Implementierung

1. Der Serverlog muss nach Client-Op 6 pro Charakter einen verschluesselten
   und im Debug entschluesselten AgpmCharacter-Frame (Modul 0x02, Operation 0)
   ausweisen, bevor Op 7 gesendet wird.
2. Der Client muss den Add-Handler erreichen und ein lokales Objekt mit
   nicht-null CID und TID anlegen.
3. Der Init-Callback muss den ResourceLoader erreichen; LoadTemplateData muss
   ein Template mit nicht-null pClump liefern.
4. Danach muss RpClumpClone fuer dieses Template laufen.
5. AgcmUILogin::CBAddCharacter muss nach Post-Add einen Charakter mit Clump
   und Frame erhalten und ihn in die Auswahlsteuerung aufnehmen.

Falls Schritt 3 fehlschlaegt, ist erst dann separat zu pruefen, ob race_tid
auf ein vorhandenes lokales Template und dessen Modellressource zeigt. Im
gegenwaertigen Test ist diese Pruefung verfrueht, weil kein Add-Paket den
Template-Ladepfad erreichen kann.

## Quellen

- Live-Protokoll: AlefLogin/server.log, Versuch ab 15:29:12.
- Gegenwart des Op-6-Handlers: AlefLogin/crates/aleflogin-server/src/main.rs,
  Bereich AGPMLOGIN_CHARACTER_INFO.
- Persistenzabfrage: AlefLogin/crates/aleflogin-server/src/db.rs,
  Character und list_characters.
- Client- und Referenzserverpfad: WINSOCK_SEQUENCE_18_CHARACTER_ADD_AND_3D_INIT.md.
