# Monsterbelohnungen und Bodenitems (27.09.2026)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

## Beobachteter Clientlauf

Der Testcharakter `Ritter` (CID 3, Level 50) griff einen Eber (TID 11,
Level 5) mit normalen Angriffen an. Das Serverlog zeigt drei Angriffe
außerhalb der Reichweite (766, 512 und 258 Einheiten) ohne Schaden. Beim
vierten Angriff lag die serverseitige Distanz bei 87 Einheiten und der
erste Treffer wurde gewertet. Der Eber schlug mehrfach zurück und starb
nach weiteren Treffern.

Für diesen Eber beträgt die EXP-Belohnung bei einem Level-50-Spieler nach
der aus dem EP8-Server abgeleiteten Dämpfung null. Die neue Chatmeldung
für `0 EXP` wurde erst nach diesem Lauf gebaut und ist clientseitig noch
nicht bestätigt.

Der Server erzeugte für den Tod 16 Gold als Bodenitem (Item-TID 268,
Ground-ID 1). Die Clientanfrage zum Aufheben traf sieben Sekunden später
ein:

```text
AgpmItem (Opcode 0x04), Maske 0x15,
Operation 11, ItemID 1500000001, OwnerCID 3
```

Erst danach schrieb der Server Gold gut und sendete das REMOVE-Paket.
Damit sind Bodenerzeugung, Client-Aufhebeanfrage und spätere Gutschrift
für Gold im Live-Lauf belegt.

Ein zweiter Live-Test am selben Tag fügte vorübergehend einen garantierten
Drop für TID 11 in die Datenbank ein. Zwei Eber ließen je Gold und einen
`Short Bow` (Item-TID 1) fallen. Der Client hob den zweiten Bogen mit
Operation 11 auf; die Datenbank enthält ihn danach als Inventaritem
`id=97, count=1, tab=0, x=2, y=0`. Die Testregel `id=7455` wurde danach
wieder gelöscht. Der normale Zufallsalgorithmus bleibt aktiv.

Bei weiteren Aufhebevorgängen zeigte sich, dass der vorhandene
Inventar-Grant auch nicht stapelbare Waffen zusammenführte. Der Grant liest
jetzt die importierte Spalte `item_templates.stack` und stapelt nur Items
mit einem Maximum über 1. Der bereits entstandene Zweier-Stapel des
Testbogens wurde in zwei Inventareinträge aufgeteilt.

## Umsetzung

- [`AgpmItem`](../Module/AgpmItem.md) FIELD-ADD: Status 1, ItemID in einem separaten Wire-ID-Bereich,
  Item-TID, Anzahl und verschachtelte X/Y/Z-Position.
- Bodenitems werden in `ground_items` gespeichert, bei Login und beim
  Monstertod versendet, nach 120 Sekunden entfernt.
- Aufheben akzeptiert nur Operation 11 mit Maske `0x15`, einen
  autorisierten Charakter, höchstens 200 Einheiten Abstand und die
  Eigentümer-Priorität der ersten 30 Sekunden. Das DB-DELETE ist atomar.
- Gold (TID 268) wird erst beim Aufheben dem Geldkonto zugeschrieben.
  Andere Gegenstände werden dann dem Inventar hinzugefügt.
- Monsterspezifische Drops folgen weiterhin dem dokumentierten
  `monster_drop_table`-Algorithmus. Wenn kein solcher Drop entsteht,
  addiert der Server die `drop_rate`-Werte der levelpassenden allgemeinen
  Items auf einer 100000er-Skala und wählt bei Erfolg ein Item gewichtet
  nach dessen Rate. Für den Level-5-Eber ergeben die aktuellen Daten
  38200/100000, also rund 38 Prozent. Die importierten Gruppen- und
  Rangraten sind Platzhalter; diese allgemeine Wahrscheinlichkeit ist
  daher weiterhin eine Näherung.
- Positive EXP bleiben per DB und Factor-Update verbucht; zusätzlich
  wird ein [`AgpmChatting`](../Module/AgpmChatting.md)-Systempaket geschickt. Auch Null-EXP wird als
  Erklärung im Chat gesendet. Nach jedem erfolgreichen Aufheben folgt
  eine Nachricht mit Goldmenge beziehungsweise Itemname und Anzahl.

## Level-1-Berserker und Chatformat

Der Berserker (CID 4) startete mit Level 1 und 0 EXP. Am 27.09.2026
erhielt er bei zwei Kills von TID 14 jeweils 27 EXP; nach dem zweiten
Kill stand er in der Datenbank auf Level 2 und 6 Rest-EXP. Ein weiteres
Monster (TID 648) gab 56 EXP. Gold erschien jeweils am Boden und wurde
erst durch eine Client-Aufhebeanfrage gutgeschrieben. Monster schlugen
nach Angriffen zurück.

Der Spieler sah keine EXP-Meldungen im Spielchat. Ein echter ausgehender
Client-Chattext lieferte das klare Gegenbeispiel zum bisherigen Builder:

```text
d6 24 00 0f 00 04 00 00 00 c8 83 04 00 4f 00 04
00 00 00 00 01 00 00 00 09 00 74 65 73 74 20 63 ...
```

Nach der Maske `0x4f` liegen Operation (1 Byte), CID (4), Chattyp (1),
**Sendertyp (4)** und erst dann Textlänge (2) und Text. Der erste
EXP-Builder schrieb den Sendertyp nur als ein Byte; der Client konnte
damit den Text nicht lesen. Der Builder ist jetzt auf vier Bytes korrigiert.
Die Anzeige mit der neuen Serverversion muss noch live bestätigt werden.

Um 07:04 UTC fiel beim Berserker zusätzlich zum Gold ein natürlicher
Gegenstand: TID 2727 (`Training Kataria`). Der Client hob Gold und Item
getrennt auf; der Gegenstand steht danach als Inventareintrag `id=99,
count=1`. Damit ist auch der allgemeine zufällige Itemdrop samt
manuellem Aufheben ohne Testregel belegt.

Der abschließende Datenbankstand nach dem Spieltest lautet: Berserker
Level 3, 34 Rest-EXP, 72 Gold; `Training Kataria` liegt als einzelner
Gegenstand im Inventar. Die EXP-Werte sind bei den jeweiligen Kills
persistiert und Factor-Updates wurden an den Client gesendet.

Der korrigierte Chatbuilder und die Aufhebe-Meldungen bestehen alle 23
`alefgame-server`-Unit-Tests. Nach dem Schließen des Clients wurde der
Release-Build erfolgreich erstellt und der Gameserver um 07:11 UTC mit
`RUST_LOG=info` neu gestartet. Port 11008 lauscht wieder. Dieser neue
Build wurde noch nicht mit einem angemeldeten Client auf sichtbare
Chatmeldungen getestet.

## Offene Liveprüfung

1. Nach Neustart der neuen Serverversion eine EXP- und eine
   Aufhebe-Meldung im Client prüfen.
2. Die automatische Annäherung anhand der sichtbaren Clientposition erneut
   abgleichen. Der Server begrenzt sie derzeit auf 300 Einheiten pro Sekunde,
   da der Client in diesem Pfad kein `CharMove` sendet.
