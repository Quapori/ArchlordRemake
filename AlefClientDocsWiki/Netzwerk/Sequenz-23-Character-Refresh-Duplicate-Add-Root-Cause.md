# Sequenz 23: Delete/Create-Refresh erzeugt doppelten 3D-Aufbau

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ergebnis

Die Datenbank, Slotvergabe und der eigentliche Delete/Create-Vorgang sind nicht die Ursache. Das Problem ist ein doppelter, ueberlappender Character-Add-Zyklus auf derselben Login-Verbindung.

Der bestehende Server-Refresh sendet nach einer Loeschung oder Erstellung:

1. Op 13 fuer alle noch vorhandenen Charaktere, um die lokale UI/Registry zu leeren.
2. Op 4 pro Name und Op 5 als Abschluss.
3. Unaufgefordert alle AgpmCharacter-Add-Pakete und Op 7.

Schritt 2 ist aber kein passiver Listenabschluss. Der Client verarbeitet Op 5 in [`AgcmUILogin`](../Module/AgcmUILogin.md):CBGetMyCharacterNameFinish`: Er setzt den Modus auf `WAIT_MY_CHARACTER`, setzt `m_lAddMyCharacterCount = 0` und sendet sofort [`AgcmLogin`](../Module/AgcmLogin.md):SendGetCharacters`, also Login-Op 6.

Dadurch trifft nach dem vom Server bereits gesendeten Aufbau ein echter Op-6-Request ein. Der aktuelle Op-6-Handler sendet erneut alle AddCharacter-Pakete und Op 7. Jede Figur durchlaeuft deshalb zwei Add-Zyklen, obwohl die Client-UI nur einen erwartet. Das erklaert fehlende oder doppelte Modelle, falsche Slots und eine inkonsistente Auswahl nach Delete -> Create. Beim Verlassen und Neuverbinden existiert nur der normale, eine Zyklus umfassende Weg und alles wird korrekt.

## Direkter Logbeweis

Beispiel: Erstellung von `Swashbuckler` im Slot 2 am 2026-09-09.

| Zeit | Serveraktion |
|---|---|
| 18:00:32.814 | Op 11 bestaetigt die Erstellung |
| 18:00:32.815 | Op 12 beendet den Create-Dialog |
| 18:00:32.816 | `refreshing full character roster ... count=3` |
| 18:00:32.819 bis 18:00:35.246 | der Refresh sendet bereits alle AddCharacter-Pakete, jeweils mit Wiederholung |
| 18:00:35.251 | der Client sendet danach Op 6; der Server protokolliert `AGPMLOGIN_CHARACTER_INFO request -> sending character list` |
| danach | ein zweiter kompletter Add-Zyklus wird erzeugt |

Das gleiche Muster ist im Delete-Fall vorhanden: Refresh um 17:53:13.130, anschliessender clientseitiger Op-6-Request um 17:53:14.767.

## Client-Vertrag

### Op 4 / Op 5 loesen den Add-Request aus

`AgcmUILogin::CBGetMyCharacterNameFinish`:

- setzt `AGCMLOGIN_MODE_WAIT_MY_CHARACTER`;
- oeffnet die Ladeansicht;
- setzt `m_lAddMyCharacterCount = 0`;
- ruft `AgcmLogin::SendGetCharacters(world, account)` auf.

Daraus folgt zwingend:

```text
Op 4 x N -> Op 5
  Client: Op 6
  Server: AgpmCharacter Add x N -> Op 7
```

Der Client erwartet genau diese Trennung zwischen Namen/Slots und 3D-Objekten.

### Lokale State-Maschine

- Op 4 ruft `AgcmUILogin::CBGetMyCharacterName` und damit `AddMyCharacterInfo(name, slot)` auf.
- Ein bereits belegter Slot wird dort nicht ueberschrieben. Der Client waehlt stattdessen den ersten freien Slot.
- Op 13 ruft `CBRemoveCharacter` auf, entfernt Name/Slot und das lokale [`AgpmCharacter`](../Module/AgpmCharacter.md)-Objekt.
- Op 7 erst schliesst den ersten Character-Add-Zyklus ab und wechselt den Loginmodus in die Character-Auswahl.

Die bisherige Idee, vor dem Refill fuer jeden ueberlebenden Charakter Op 13 zu senden, ist weiterhin richtig: Sie verhindert die Fallback-Umverteilung in `AddMyCharacterInfo`. Falsch ist nur der anschliessend serverinitiierte Add-Teil.

## Erforderliche Serverkorrektur

Nur als Befund; keine Aenderung durch diese Analyse.

`refresh_world_characters` darf nach den Op-13-Clears nur die Namensliste senden:

```text
Op 13 fuer jeden weiterhin existierenden Charakter
Op 4 fuer jeden Charakter
Op 5
warte auf den nativen Client-Request Op 6
Op-6-Handler sendet AddCharacter x N und Op 7 genau einmal
```

Der Aufruf von `send_add_character_list_and_finish` innerhalb von `refresh_world_characters` muss deshalb entfallen. Der bestehende `AGPMLOGIN_CHARACTER_INFO`-Handler ist bereits der korrekte alleinige Sender fuer AddCharacter und Op 7.

Fuer den Delete gilt zusaetzlich: Zuerst Op 13 fuer den geloeschten Namen, dann die Clears fuer die Ueberlebenden, dann Op 4/Op 5. Dadurch bleibt das lokale Drei-Slot-Array leer, bevor es erneut befuellt wird.

## Nebenbefund: Zaehler-Unterlauf

`CBRemoveCharacter` dekrementiert `m_lAddMyCharacterCount` bedingungslos. Nach Op 11 kennt die UI den neuen Namen bereits, sein 3D-Objekt wurde aber noch nicht hinzugefuegt. Ein unmittelbar danach gesendetes Op 13 fuer diesen Namen kann den Zaehler daher unter null bringen.

Der anschliessende Op-5-Callback setzt den Zaehler wieder auf 0. Das ist ein weiterer Grund, die vom Client initiierte Op-6-Grenze zu respektieren: Der Reset geschieht vor dem einzigen gueltigen Add-Zyklus.

## Verifikation nach der Korrektur

1. Drei Charaktere in Slots 0, 1 und 2 erstellen.
2. Slot 2 loeschen und einen neuen Charakter in Slot 2 erzeugen.
3. Im Serverlog muessen nach dem Refresh Op 4/Op 5 erscheinen.
4. Genau ein anschliessender Op-6-Request und genau ein Satz `AgpmCharacter Add`-Pakete plus genau ein Op 7 duerfen folgen.
5. Ohne Rueckkehr zur Serverauswahl muessen drei Modelle, Namen und selektierbare Slots korrekt sein.
