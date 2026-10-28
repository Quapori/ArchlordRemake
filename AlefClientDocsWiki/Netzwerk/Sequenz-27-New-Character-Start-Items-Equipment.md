# Winsock Sequenz 27: Startausstattung neuer Charaktere

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

Diese Analyse beantwortet, ob ein neu angelegter Charakter mit Waffen starten kann, wie die Ausruestungsplaetze bestimmt werden und welche Daten beim Weltbeitritt vom Gameserver kommen muessen. Quellen sind der Referenzserver `EP8-c++-Source`, die installierten Clienttabellen unter `C:\Spiele\Archlord\ini` und der bereits zerlegte Client.

## Ergebnis

- Ja: Der Referenzserver legt bei jeder normalen Charaktererstellung explizit eine Startausstattung an. Diese kann eine Waffe enthalten, wenn das serverseitige Startset fuer die gewaehlte Charaktertemplate eine Waffen-TID definiert.
- Es ist keine nur optische Clientfunktion. Jede Startwaffe wird als eigene serverautorisierte Iteminstanz erzeugt, dem Charakter zugeordnet und sofort ausgeruestet.
- Die Startset-Zuordnung liegt in der externen, serverseitig geladenen `BaseCharacterInfo.xml`. Diese Datei befindet sich nicht im untersuchten Clientbestand. Konkrete Startwaffen-TIDs sind deshalb aus dem installierten Client allein noch nicht belegbar.
- Der Client besitzt die statischen Itemtemplates, Clumps und Materialdaten. Er kann aus einer vom Server gesendeten Itemtemplate-ID das Modell und den vorgesehenen Equip-Part aufloesen, darf die Instanz, Besitzerschaft, Status oder Startausstattung aber nicht selbst erzeugen.

## Erzeugungszeitpunkt

`AgsmLoginClient::CreateCharacter` erzeugt zuerst den Charakter und ruft danach sowohl fuer normale als auch fuer Jumping-Charaktere auf:

```cpp
m_pAgsmItemManager->GiveDefaultItem(pAgpdCharacter, 1);
```

Der normale Pfad liegt bei `AgsmLoginClient.cpp:911`; der Jumping-Event-Pfad ruft die gleiche Funktion mit `bJumpingEvent=TRUE` auf (`:889`). Das Set `1` ist damit der Startausruestungs-Satz.

`AgsmItemManager::GiveDefaultItem` waehlt innerhalb der zum Charaktertemplate gehoerenden `EquipItemSetInfo` den Eintrag mit:

```cpp
m_nSetNumber == 1
m_bIsJumpingEventEquip == bJumpingEvent
```

Dann iteriert es ueber alle Equip-Parts. Fuer jede von Null verschiedene `m_lDefaultEquipITID[part]` passiert serverseitig:

```cpp
item = CreateItem(templateTid, character);
AgpmItem::EquipItem(character, item, TRUE, TRUE);
```

Der gleiche Aufruf legt anschliessend konfigurierte Verbrauchsitems/sonstige Startitems in das Inventory und nutzt dort Stackcount sowie Inventarplatzierung. Geld wird separat aus der Charakterbasis-Konfiguration gesetzt.

## Startset-Konfiguration und ihre Grenze

`AgsmCharacter::StreamReadBaseCharacterInfo` laedt die externe Datei `BaseCharacterInfo.xml`. Pro `Character`-Knoten werden folgende Werte eingelesen:

```xml
<TID Race="..." Class="..." Name="...">CHARACTER_TEMPLATE_TID</TID>
<Equip>
  <Set Index="1">
    <Item Part="10" TID="WEAPON_TEMPLATE_TID"/>
  </Set>
</Equip>
<Inventory>
  <Default TID="..." Count="..."/>
</Inventory>
<Gheld>...</Gheld>
```

Die XML-Struktur ist aus dem Reader belegt; die obigen konkreten Platzhalter-TIDs sind absichtlich keine Behauptung ueber den Inhalt. Die Datei wurde weder im Workspace noch unter `C:\Spiele\Archlord` gefunden. Sie ist daher Server-Content, nicht Client-Content.

Folgerung: Es ist belegt, dass neue Charaktere im Referenzserver Startitems erhalten. Ob ein bestimmtes Rassen-/Klassetemplate eine Waffe, Schild, Kleidung oder nur Inventaritems bekommt, ist ohne die passende `BaseCharacterInfo.xml` beziehungsweise einen Packet-Mitschnitt noch offen.

## Feste Ausruestungsplaetze

Die Enum `AgpmItemPart` definiert die fachlichen Slots. Fuer Waffen relevant:

| Part-ID | Bezeichnung | Verwendung |
|---:|---|---|
| `2` | `BODY` | Ruestung Koerper |
| `3` | `HEAD` | Kopf |
| `5` | `HANDS` | Handschuhe |
| `6` | `LEGS` | Beine |
| `7` | `FOOT` | Schuhe |
| `9` | `HAND_LEFT` | linke Hand, z. B. Schild, Zweithand oder linker Dolch |
| `10` | `HAND_RIGHT` | rechte Hand, primaere Waffe |
| `11`, `12` | `RING1`, `RING2` | Ringe |
| `13` | `NECKLACE` | Halskette |

Der Server verwendet den im Itemtemplate definierten `m_nPart`, nicht blind den `Part`-Index des Startsets. [`AgpmItem`](../Module/AgpmItem.md):EquipItem` liest die Template-TID der erzeugten Instanz, prueft Nutzungsvoraussetzungen und legt das Item im Equipment-Grid ab. Daraus folgen wichtige Regeln:

- Ein Template mit Part `10` wird zur rechten Hand.
- Ein Template mit Part `9` wird zur linken Hand.
- Zweihandwaffen reservieren beide Haende; vorhandene Gegenstaende der anderen Hand werden in das Inventar verschoben.
- Ein linker Einhand-Dolch ist nur zusammen mit einem rechten Rapier erlaubt; diese Laufzeitregel wird beim normalen Equippen geprueft.
- Ringe werden dynamisch auf Ring 1, dann Ring 2 verteilt.

Die Reihenfolge, in der `GiveDefaultItem` die TIDs aus dem Set abarbeitet, ist Part-Reihenfolge. Die finale Slotentscheidung bleibt dennoch die Template- und Equiplogik.

## Was der Gameserver senden muss

Beim ersten Weltbeitritt muessen bereits persistierte oder beim Create erzeugte Items als `AgpmItem` Modul `0x04` an den eingeloggten Client synchronisiert werden. Der Referenzserver baut dafuer mit `AgpmItem::MakePacketItem` einen Add-Frame (`AGPMITEM_PACKET_OPERATION_ADD`). Die Kernfelder sind:

| Feld | Quelle | Fuer eine Startwaffe erforderlich |
|---|---|---|
| Operation | immer `ADD` | ja |
| Status | `AGPDITEM_STATUS_EQUIP` | ja |
| Item-ID | eindeutige Instanz-ID | ja |
| Template-ID | Waffen-/Ruestungs-TID | ja |
| Owner-CID | Charakter-ID | ja |
| Count | typischerweise `1` | ja |
| Equip-Subpacket | bei Status `EQUIP` vorhanden | ja |
| Factor-Differenzen | dynamische Werte gegen lokales Template | bei Abweichungen |
| Options/SkillPlus/Extra | Instanz-Zusatzdaten | falls vorhanden |

Fuer Inventory-Startitems sendet der gleiche Add-Frame statt des Equip-Subpackets ein Inventory-Tripel `tab,row,column`. Fuer `EQUIP` wird kein separater Hand-Slot im Frame aufgebaut. Der Client bestimmt die sichtbare Hand anhand des lokalen Itemtemplates zur gesendeten Template-ID.

Die bereits dokumentierte Clientanalyse ([`WINSOCK_SEQUENCE_05_ITEM_INVENTORY_EQUIP.md`](Sequenz-05-Item-Inventory-Equip.md)) bestaetigt dazu: Die Itemtemplate-ID wird lokal gegen die Clienttabellen aufgeloest, waehrend Instanz-ID, Owner, Status, Stackcount, Bindung, Optionen, Timer und Containerzustand Serverdaten sind.

## Persistenzbedarf

Die Ausruestung darf nicht nur beim Create im Speicher existieren. Vor dem ersten Reload beziehungsweise erneuten Login muessen mindestens folgende Daten dauerhaft gespeichert werden:

| Datenwert | Grund |
|---|---|
| Iteminstanz-ID | eindeutige Referenz fuer Move, Equip, Drop und spaetere Pakete |
| Character-ID | Eigentum und Autorisierung |
| Itemtemplate-ID | Clientmodell, Stats und Equip-Part |
| Status `EQUIP` oder `INVENTORY` | bestimmt Zielcontainer beim Load |
| Equip-Part oder aequivalente Equipment-Gridposition | persistente Platzierung; aus Template ableitbar, aber fuer konsistente Wiederherstellung speichern |
| Inventory tab/row/column | fuer nicht ausgeruestete Startitems |
| Stackcount | Verbrauchsitems |
| optionale Instanzwerte | Haltbarkeit, Bindung, Optionen, Runen, Ablaufzeit, Statusflags |

Nach dem Gameserver-`LoadingComplete` ist die Reihenfolge aus Sequenz 25 relevant: erst den Selbstcharakter als vollstaendige [`AgpmCharacter`](../Module/AgpmCharacter.md)-Instanz anlegen, danach dessen Items ueber `AgpmItem` Add synchronisieren und erst anschliessend den Weltzustand freigeben. Damit koennen Item-Owner-CID und das 3D-Characterobjekt im Client aufgeloest werden.

## Charakterauswahl vor dem Weltbeitritt

Das Vorhandensein einer Startwaffe bedeutet nicht automatisch, dass sie bereits in der Charakterauswahl sichtbar sein muss. Der bisher belegte Auswahlfluss liefert `AgpmCharacter`-Add-Daten fuer das Erzeugen des Basis-`RpClump` sowie Name, Template und Appearance. Er enthaelt keine Iteminstanzen.

Der Referenzserver besitzt fuer eine vollstaendige Itemsynchronisierung die Routine `AgsmItem::SendPacketItemAll`. Sie sendet zuerst alle Equipment-Items und danach Inventory, Bank, Quest und weitere Container als einzelne `AgpmItem`-Add-Frames. Erst ein solcher Equip-Frame mit Template-TID und Status `EQUIP` kann den Client veranlassen, das Waffenmodell am bestehenden Character-Clump anzubringen.

Damit gelten zwei getrennte, korrekte Varianten:

1. Die Auswahl zeigt nur den Basischarakter. Das ist mit dem bisher beobachteten Login-/Auswahlprotokoll vereinbar; die Startwaffe wird erst nach Gameserver-Login sichtbar.
2. Die Auswahl soll die reale Ausruestung zeigen. Dann muss der Auswahlserver nach jedem Character-Add auch dessen Equipment-`AgpmItem`-Adds liefern, mindestens fuer alle Items mit Status `EQUIP`. Die Items muessen vor den Add-Frames bereits in der Datenhaltung vorhanden sein.

Die Auswahl darf die Waffe nicht allein anhand der Rasse/Klasse clientseitig erraten, weil Ausruestung nach dem ersten Spiel jederzeit wechselbar ist. Fuer einen neu erzeugten Charakter ist die TID zwar anfangs aus dem Startset ableitbar; dieselbe Regel waere fuer bestehende Charaktere jedoch falsch.

## Audit des aktuellen Rust-Loginservers (nur Befund)

Der aktuelle Server besitzt bereits eine `character_items`-Persistenz, deckt die Equipment-Vorschau aber nicht ab. Die Luecke ist konkret und reproduzierbar:

1. `db::create_character` legt aus `character_templates.weapon_item_tid` eine Itemzeile mit `status = 'equipped'` an. Inventar-Startitems werden ebenfalls angelegt.
2. `db::list_character_items` liest diese Zeilen korrekt, hat aber `#[allow(dead_code)]` und keinen Aufrufer.
3. `send_add_character_list_and_finish` sendet fuer die Auswahl ausschliesslich `AgpmCharacter`-Add-Frames und danach Login-Op `7`. Es gibt weder eine `AgpmItem`-Opcode-Konstante noch einen Item-Paketbuilder oder einen Send-Aufruf pro CharacterItem.

Die fehlende Vorschau ist daher kein Client-Asset-Problem: Der Client kennt die Ausruestung schlicht nicht, weil im Auswahlzyklus keine `AgpmItem`-Add-Frames eintreffen.

### Weitere Datenluecken im aktuellen Stand

| Befund | Auswirkung |
|---|---|
| Die beim Create angelegte Waffe wird mit `slot_index = 0` gespeichert. | `0` ist kein gueltiger `AGPMITEM_PART_*`-Equip-Part. Die Handplaetze sind `9` und `10`; die korrekte Seite muss aus dem Itemtemplate abgeleitet und gespeichert werden. |
| Das SQL-Schema besitzt Spalten fuer Head/Body/Arms/Hands/Legs/Foot/Mantle, aber die aktuelle Rust-`CharacterTemplate`-Struktur und deren SELECT lesen sie nicht. | Diese Ausruestung kann weder beim Create erzeugt noch fuer die Auswahl uebertragen werden. |
| Das Template-Seed nutzt in der Insertliste nur `weapon_item_tid` und Verbrauchsitems. | Selbst wenn Itemframes implementiert waeren, existiert fuer die meisten neuen Charaktere keine persistierte Start-Ruestung oder ein Schild. |
| Die DragonScion-Templates `1722`, `1723` und `1732` haben in den aktuellen Seedwerten keine Weapon-/Starter-TIDs. | Diese drei Klassen erhalten nach aktuellem Datenstand keine Startausstattung. |

### Erforderlicher Auswahlvertrag

Pro gespeicherten Charakter ist die belastbare Reihenfolge:

1. `AgpmCharacter` Operation `ADD`: erzeugt den Basis-`RpClump` fuer die Auswahl.
2. Das Item-Character-Zusatzpaket und danach `AgpmItem` Operation `ADD` fuer die persistierten Iteminstanzen desselben CIDs. Fuer sichtbare Teile muss der Status `EQUIP` mitsamt Item-ID, Template-ID, Owner-CID und Equip-Subpacket vorliegen.
3. Erst danach `AGPMLOGIN_CHARACTER_INFO_FINISH` (Login Op `7`).

Der Referenzserver sendet im Auswahlpfad ueber `SendPacketItemAll` auch Inventory, Bank, Quest und weitere Container. Fuer die Vorschau sichtbar sind davon nur `EQUIP`-Items. Details zum exakten Sendepfad stehen in [`WINSOCK_SEQUENCE_28_CHARACTER_SELECT_EQUIPMENT_SEND_PATH.md`](Sequenz-28-Character-Select-Equipment-Send-Path.md).

## Fundorte im Clientbestand

Statische Daten liegen im installierten Client unter:

| Pfad | Rolle |
|---|---|
| `C:\Spiele\Archlord\ini\itemtemplateentry.ini` | Einstieg/Index der Itemtemplate-Daten |
| `C:\Spiele\Archlord\ini\itemdatatable.txt` | statische Itemdaten, die der Client fuer Tooltip/Templateaufloesung verwendet |
| `C:\Spiele\Archlord\ini\itemtooltip.txt` und `itemtooltipdesc.txt` | Anzeige- und Beschreibungstexte |
| `C:\Spiele\Archlord\ini\charactertemplatepublic.ini` | statische Charaktertemplate-Daten |

Eine Suche in `charactertemplatepublic.ini`, `characterdatatable.txt` und `itemtemplateentry.ini` nach `DefaultItem`, `DefaultEquip`, `EquipSet` oder `StartItem` liefert keine Startset-Konfiguration. Das passt zum Referenzserver: Die TID-Auswahl ist eine Serverdatei `BaseCharacterInfo.xml`; der Client besitzt nur die Assets und Templates, um die vom Server gewaehlten Items darzustellen.

## Naechste belastbare Schritte

1. `BaseCharacterInfo.xml` aus einem passenden EP8-Serverpaket oder Backup beschaffen; daraus lassen sich alle Start-TIDs pro Rasse/Klasse direkt extrahieren.
2. Alternativ einen Create- und ersten Gameserver-Login gegen einen Referenzserver mitschneiden. Die ersten `AgpmItem` Add-Pakete nach dem Self-Character-Add enthalten die tatsaechlichen TIDs und den Status `EQUIP`.
3. Danach die betreffenden TIDs gegen die lokalen Itemtemplate-Dateien aufloesen und die Clump-/Attachment-Pfade fuer jede Startwaffe dokumentieren.
