# Winsock Sequenz 28: Sendepfad der Ausruestung in der Charakterauswahl

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

Diese Datei dokumentiert den im EP8-Referenzserver belegten End-to-End-Pfad, durch den eine Charakterauswahl den Charakter mit seiner aktuellen Ausruestung anzeigt. Sie unterscheidet den Referenzpfad vom aktuellen Rust-Loginserver. Es wurden keine Rust-Dateien geaendert.

## Kurzfassung

Die Charakterauswahl bekommt die Ausruestung nicht als Feld im [`AgpmCharacter`](../Module/AgpmCharacter.md)-Paket. Der Referenzserver laedt die Iteminstanzen aus der Datenbank, setzt sie in das serverseitige Equipment-Grid und sendet nach dem Character-Add separate [`AgpmItem`](../Module/AgpmItem.md)-Pakete. Der Client erstellt daraus die Item-Clumps und bindet Waffen, Schild und Ruestung an den bereits vorhandenen Character-Clump.

## Referenzserver: Request bis Datenbank-Laden

1. Client sendet [`AgcmLogin`](../Module/AgcmLogin.md)/[`AgpmLogin`](../Module/AgpmLogin.md) Operation `6` (`AGPMLOGIN_CHARACTER_INFO`) fuer die ausgewaehlte Welt.
2. `AgsmLoginClient::OnReceive` ruft `ProcessGetCharacters(account, server, db, clientNid)` auf.
3. Die Anfrage wird als `AGSMLOGIN_OPERATION_GET_CHARACTERS` an `AgsmLoginDB` weitergereicht.
4. `AgsmLoginDB::ProcessGetCharacters` ruft fuer jeden gespeicherten Charakternamen `_SelectCharacterView(database, characterName, NULL, clientNid)` auf.
5. `_SelectCharacterView` laedt Character-Detaildaten und fuehrt `EQUIP_ITEM_SELECT` aus.
6. Jede geladene Itemzeile wird durch `AgsmItemManager::GetSelectResult5` zur serverseitigen Iteminstanz. Ihr Status wird zunaechst auf `NOTSETTING` gesetzt; anschliessend versucht `AgpmItem::EquipItem(..., TRUE, TRUE)`, sie anhand ihrer Template-Definition in das passende Equipment-Grid zu setzen. Bei Fehlschlag wird sie ins Inventar gelegt, bei weiterem Fehlschlag entfernt.
7. Gibt es keine gespeicherten Equipmentzeilen und ist der Charakter zur Reinitialisierung markiert, erzeugt der Referenzserver die Defaultitems und persistiert sie mit `_InsertItem`.

Damit ist vor jedem Send bereits die reale, persistierte Ausruestung in der Serverstruktur vorhanden. Die Auswahl erratet keine TIDs aus Rasse oder Klasse.

## Referenzserver: Sendekette pro Charakter

Nach `_SelectCharacterView` ruft `ProcessGetCharacters` auf:

```cpp
AgsmCharacter::SendCharacterAllInfo(character, clientNid);
```

Die daraus folgende Kette ist:

```text
AgsmLoginDB::ProcessGetCharacters
  -> AgsmCharacter::SendCharacterAllInfo
       -> SendPacketChar
          -> AgpmCharacter ADD an Client
       -> EnumCallback(SEND_CHARACTER_ALL_INFO)
          -> AgsmItem::CallbackSendCharacterAllInfo
             -> SendPacketItemADCharacter
             -> SendPacketItemAll
                -> pro Item: SendPacketItem
                   -> AgpmItem::MakePacketItem
                      -> AgpmItem ADD an Client
```

`AgsmItem` registriert diesen Callback beim Start ueber `SetCallbackSendCharacterAllInfo(CallbackSendCharacterAllInfo, this)`. Der Itempfad ist deshalb ein Callback des allgemeinen Character-AllInfo-Sends, nicht ein separater Login-Opcode.

## Tatsaechliche Reihenfolge auf dem Socket

Fuer jeden Charakter folgt auf dem Auswahlsocket:

1. `AgpmCharacter` Operation `ADD`: erzeugt den Basischarakter/`RpClump`.
2. `AgpmItem`-Attached-Character-Paket aus `SendPacketItemADCharacter`: Item-Charakter-Zusatzdaten; der genaue AuPacket-Builder `MakePacketItemADCharacter` ist noch separat zu zerlegen.
3. Ein `AgpmItem`-Operation-`ADD`-Paket pro Item aus `SendPacketItemAll`.
4. Nach allen Charakteren: `AGPMLOGIN_CHARACTER_INFO_FINISH` (Login Operation `7`).

`SendPacketItemAll` iteriert im Referenzserver zuerst alle Equipment-Parts und danach Inventory, Bank, Quest, SalesBox, Cash, SubInventory und ChargingInventory. Damit sendet der Originalpfad mehr als nur die fuer die Vorschau sichtbaren Items. Fuer die sichtbare Ruestung sind jedoch ausschliesslich Eintraege mit Status `EQUIP` entscheidend.

## Aufbau eines sichtbaren Equipment-Item-Adds

`AgpmItem::MakePacketItem` baut fuer jede Iteminstanz:

```text
Operation       = AGPMITEM_PACKET_OPERATION_ADD
Status          = AGPDITEM_STATUS_EQUIP
ItemID          = persistente Instanz-ID
ItemTemplateID  = statische TID
ItemOwnerID     = CID des Charakter-Adds
ItemCount       = normalerweise 1
Equip subpacket = vorhanden bei Status EQUIP
Factors         = Differenz zu lokalem Template, wenn vorhanden
Options/Extras  = Optionen, SkillPlus, Bindung, Timer usw., wenn vorhanden
```

Bei Status `EQUIP` gibt es kein Inventory-Grid-Tripel. Die serverseitige `EquipItem`-Logik und die lokale Itemtemplate bestimmen den Part. Das Template liefert etwa rechte Hand (`10`), linke Hand (`9`) oder einen Ruestungspart.

## Client: vom Item-Add zum sichtbaren Modell

Nach dem `AgpmItem`-Receive wird die Iteminstanz dem Besitzer-CID zugeordnet. Die Client-Schicht [`AgcmItem`](../Module/AgcmItem.md):CBSetItem` behandelt `AGPDITEM_STATUS_EQUIP` explizit mit:

```cpp
AgcmItem::EquipItem(item->m_pcsCharacter, item);
```

Der sichtbare Pfad ist anschliessend:

```text
AgcmItem::EquipItem
  -> MakeItemClump
  -> AttachItem
     -> _AttachItemArmor / _AttachItemWeapon / _AttachItemShield
  -> Attachment an den vorhandenen Character-RpClump
```

Der Client entscheidet anhand der lokalen TID-Template-Daten, ob ein Item als Ruestung, Waffe oder Schild behandelt wird. Ohne Item-Add fehlt sowohl die TID als auch die Instanzzuordnung; der Basis-Character-Add kann diese Attachments nicht erzeugen.

## Ist-Zustand des Rust-Loginservers

Der aktuelle Rust-Pfad endet derzeit hier:

```text
AGPMLOGIN_CHARACTER_INFO (6)
  -> send_add_character_list_and_finish
     -> build_add_character_packet pro Character
     -> AGPMLOGIN_CHARACTER_INFO_FINISH (7)
```

Die notwendige Mitte fehlt vollstaendig:

- `db::list_character_items(character_id)` existiert, hat aber keinen Aufrufer.
- Es gibt keinen `OPCODE_AGPM_ITEM = 0x04`-Sender im Loginserver.
- Es gibt keinen Builder fuer `SendPacketItemADCharacter`.
- Es gibt keinen Builder fuer `AgpmItem::MakePacketItem`/Operation `ADD`.
- Deshalb wird kein `CharacterItem` mit `status = 'equipped'` auf den Auswahlsocket geschrieben.

Die korrekte Einhaengestelle ist direkt nach dem erfolgreich geschriebenen `build_add_character_packet` eines Charakters und vor dem naechsten Character-Add beziehungsweise vor Op `7`. Fuer Referenztreue gehoert davor das Item-ADCharacter-Paket und danach die vollstaendige Itemliste; fuer die reine Vorschau wuerde eine nachgewiesen kompatible Minimalvariante mindestens alle `equipped`-Items benoetigen. Ob das ADCharacter-Paket fuer eine Minimalvariante entbehrlich ist, ist noch nicht bewiesen und darf nicht geraten werden.

## Noch zu zerlegen

1. `AgpmItem::MakePacketItemADCharacter`: exakte Feldmaske und ob das Client-Receive ohne dieses Paket die Equip-Grids ausreichend initialisiert.
2. Die exakte AuPacket-Maske des Item-Add-Builders fuer den vorliegenden Clientbuild; die semantische Feldreihenfolge ist belegt, die Bitmaske muss fuer einen robusten Rust-Sender aus dem Konstruktor/Builder nachgezogen werden.
3. Vollstaendige Startausruestungs-TIDs inklusive Ruestung und Schild pro Rasse/Klasse. Die aktuellen Rust-Seeds enthalten nur unvollstaendige Waffen-/Verbrauchsitemdaten.
