# Winsock-Sequenz 18: `AgpmCharacter` Add und 3D-Initialisierung

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ergebnis

Die Charakterauswahl braucht nach der Login-Operation `6` kein weiteres
[`AgcmLogin`](../Module/AgcmLogin.md)-Namenspaket fuer die 3D-Darstellung, sondern ein separates
[`AgpmCharacter`](../Module/AgpmCharacter.md)-Paket mit Operation `0` (`AGPMCHAR_PACKET_OPERATION_ADD`,
Modul-ID `0x02`). Der Client erzeugt daraus das `AgpdCharacter`-Objekt,
befuellt es und ruft anschliessend `UpdateInit` auf. Erst dieser letzte Schritt
aktiviert `AgcmCharacter`, den asynchronen Resource-Loader und schliesslich
`RpClumpClone` fuer das sichtbare RenderWare-Modell.

Ein direkter Aufruf von `AgpmCharacter::AddCharacter` bei `0x00507110` kann
zwar ein Objekt erzeugen, ersetzt den Add-Paketpfad aber nicht: Er setzt weder
die vom Paket gelieferten Felder noch `UpdateInit` in Gang.

Diese Datei beschreibt nur den Client- und Referenzserverbefund. Es wurden
keine Loginserver-, Datenbank- oder Konfigurationsdateien geaendert.

## Quellen und Versionsgrenze

- Zielbinary: `alefclient.pseudocode.c`, zentraler Receive-Switch
  `FUN_00509cb0` (`0x00509cb0`), Add-Handler `FUN_005072b0` und
  Objektanlage `FUN_00507110`.
- Lokale EP8-Referenzquelle:
  `EP8-c++-Source\Modules\APublic\AgpmCharacter\AgpmCharacter.cpp`
  (`OnOperationAdd`, Zeile 3827) und
  `...\AServer\AgsmCharacter\AgsmCharacterPacket.cpp`
  (`MakePacketAddCharacter`, Zeile 19).
- Die Referenzquelle entspricht nicht zwingend byteidentisch der analysierten
  Clientepisode. Feldreihenfolge, Datentypen und die clientseitige
  Kontrollflusskette stimmen jedoch mit dem Ghidra-Output ueberein und sind
  daher belastbar.

## Empfang und Initialisierungskette

```text
Server: AgpmCharacter Op 0
  -> AgpmCharacter::OnReceive / FUN_00509cb0
  -> OnOperationAdd / FUN_005072b0
  -> AddCharacter(CID, TID, Name) / FUN_00507110
  -> Felder aus Add-Paket uebernehmen
  -> UpdateInit(character)
  -> Callback AGPMCHAR_CB_ID_INIT
  -> AgcmCharacter::CBInitCharacter
  -> InitCharacter -> LoadCharacterData
  -> ResourceLoader (Background + Main Thread)
  -> LoadTemplateData
  -> RpClumpClone(template->m_pClump)
```

Im Pseudocode ist Operation `0` eindeutig: `FUN_00509cb0` deserialisiert das
Hauptlayout bei `AgpmCharacter + 0xde4`; sein Switch ruft fuer `case 0`
`FUN_005072b0` auf. Der Referenzhandler verlangt dabei zwingend `CID != 0`
und `TID != 0`; sonst wird der Add-Vorgang abgelehnt.

## Vollstaendige Reihenfolge des Referenz-Add-Pakets

`AgsmCharacter::MakePacketAddCharacter` baut ein `m_csPacket` mit folgender
Argumentreihenfolge. Nicht gesetzte optionale Felder werden mit `NULL`
uebergeben und erscheinen deshalb nicht in der Feldmaske.

| Nr. | Feld | Quelle / Bedeutung |
|---:|---|---|
| 0 | Operation | `AGPMCHAR_PACKET_OPERATION_ADD` = `0` |
| 1 | Character ID | persistente CID / `m_lID` |
| 2 | Character Template ID | TID / `m_lTID1`; bestimmt das lokale Template und DFF-Modell |
| 3 | Game ID | Charaktername, variabel mit `u16`-Laenge |
| 4 | Character Status | `m_unCurrentStatus` |
| 5 | Move Packet | nested: Quell-/Zielposition, Follow-Ziel/-Distanz, Turn X/Y, Move-Flags, Richtung |
| 6 | Action Packet | im Referenzpfad `NULL` |
| 7 | Factor Packet | nested Faktoren/Stats; vom Client via `ReflectFactorPacket` uebernommen |
| 8 | Money | `INT64` |
| 9 | Bank Money | `INT64` |
| 10 | Cash | `INT64` |
| 11 | Action Status | `INT8` |
| 12 | Criminal Status | `INT8` |
| 13 | Attacker ID | im Referenzpfad `NULL` |
| 14 | reserviert | im Referenzpfad `NULL` |
| 15 | Binding Region Index | `UINT8` |
| 16 | Social Action Index | im Referenzpfad `NULL` |
| 17 | Special Status | `UINT64` |
| 18 | Transform Flags | `INT8`: Transform, Ridable, Evolution |
| 19 | Skill Init | Skill-Initialisierungsstring |
| 20 | Face Index | `INT8` |
| 21 | Hair Index | `INT8` |
| 22 | Option Flag | im Referenzpfad `NULL` |
| 23 | Bank Size | `INT8` |
| 24 | Event Status Flag | `UINT16` |
| 25 | Remaining Criminal Time | `INT32` |
| 26 | Remaining Murderer Time | `INT32` |
| 27 | Nickname | String |
| 28 | GameGuard | im Referenzpfad `NULL` |
| 29 | Last Kill Time, Battle Square | `UINT32` |
| 30 | Last Escape Use Time | `UINT32` |

Der Move-Block ist im Referenzsender immer vorhanden. Fuer die reine
Login-Auswahl ist seine Position jedoch nicht bestimmend: Die Client-UI ersetzt
sie mit der lokal aus dem Slot berechneten Position. Der Move-Block bleibt
trotzdem ein Teil eines syntaktisch vollstaendigen Original-Add-Pakets.

## Was der Client tatsaechlich daraus benutzt

`AgpmCharacter::OnOperationAdd` uebernimmt insbesondere:

- CID, TID und Name bei der Anlage des lokalen Objekts;
- Status, Action-/Criminal-/Special-Status und Eventflags;
- Faktor-Nested-Paket, sofern vorhanden;
- Binding-Region, Transform-Flags, Face- und Hair-Index;
- Skill-Init und Nickname;
- Move-Position und Orientierung;
- Zeitstempel fuer Criminal-, Murderer-, Battle-Square- und Escape-Zustaende.

Danach folgt zwingend `UpdateInit`. Dieses feuert
`AGPMCHAR_CB_ID_INIT(character, characterTemplate)`. `AgcmCharacter` hat
diesen Callback registriert; `LoadCharacterData` reiht den Charakter in den
Resource-Loader ein. Der Hintergrundpfad laedt die Template-Daten, fordert
bei Bedarf die DFF-Ressource an und klont mit `RpClumpClone` den Template-Clump
in `AgcdCharacter::m_pClump`.

Damit ist die Ursache der frueheren unsichtbaren, per Injection erzeugten
Charaktere abgegrenzt: Das rohe Objekt existierte, aber die Renderpipeline
wurde nicht angestossen.

## Bedeutung fuer den aktuellen Login-Stand

Der unmittelbare Login-Stillstand aus Sequenz 17 tritt frueher auf und muss
zuerst auf Protokollebene bis zu Client-Op `6` untersucht werden. Danach ist
fuer einen vorhandenen Charakter folgende Trennung relevant:

1. Client-Op `3` bekommt Union sowie Op `4`/Op `5` fuer den accountweiten
   Vorlauf.
2. Client sendet Op `6` fuer die gewaehlte Welt.
3. Der originale Loginserver ruft pro Charakter `SendCharacterAllInfo` auf;
   diese Funktion ruft zuerst `SendPacketChar`, dessen Nutzlast das oben
   dokumentierte Add-Paket ist.
4. Erst danach schliesst der Login-Kanal die Phase mit Op `7` ab.

Ein Loginserver muss dafuer keine Verbindung zu einem Gameserver aufbauen: Die
Originalquelle baut das Auswahlobjekt aus der eigenen Login-DB und sendet es
direkt an den Client. Eine spaetere World-Session kann trotzdem einen eigenen
Handoff benoetigen.

## Offene Bytearbeit

- Die `AuPacket`-Feldtypen und Maskenbreite des Haupt-Add-Pakets muessen aus
  `AgpmCharacter`-Konstruktor und `m_csPacket.SetFieldType(...)` als exakte
  Wire-Spezifikation transkribiert werden.
- Anschliessend ist ein minimaler, maskenkorrekter Add-Paketfall fuer einen
  bereits persistierten Testcharakter gegen den Client zu validieren. Das ist
  eine separate Implementierungsaufgabe und Teil dieser Analyse nicht.
- Der Factor-Block muss separat auf die fuer die Auswahl zwingenden Felder
  reduziert werden. TID, Name und die echte Add-Dispatch-Kette sind fuer das
  Starten der Clump-Ladung nachweislich zentral; die restlichen optionalen
  Felder duerfen erst nach Bytevalidierung weggelassen werden.
