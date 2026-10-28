# AgcmGuild (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmGuild` (Gildenpakete senden, Abfragen auf die eigene Gilde, Gilden-Marken) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmGuild/AgcmGuild.cpp`. Das Paketformat steht im Bericht [AgpmGuild](AgpmGuild.md), die Oberfläche in [AgcmUIGuild](AgcmUIGuild.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 68 von 71 Quellmethoden zugeordnet; offen sind `SendHostileLeaveReject` (nicht im Binary), `IsGuildBattle` (vermutlich eingebaut) und `CBCheckGuildAttackable` (Registrierung in der Quelle auskommentiert).
- **Pakete:** 39 Sendefunktionen sind zugeordnet (Gründung, Beitritt, Austritt, Hinauswurf, Auflösung, Ankündigung, Gildenschlacht, Liste, Umbenennung, Marke kaufen, Bündnis, Feindschaft, Weltmeisterschaft, Ernennung, Nachfolge); `SendHostileLeaveReject` (Operation 42) fehlt im Binary.
- **OnAddModule:** gleiche Module und gleiche acht Rückrufe wie in der Quelle; der auskommentierte Rückruf `CBCheckGuildAttackable` fehlt auch im Binary.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmGuild.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00668EE0` | 435 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE` (vom Linker zusammengefaltet) |
| 3 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `OnIdle-Rumpf` (vom Linker zusammengefaltet) |
| 4 | `GetSelfGuildID` | `0x00666470` | 30 | von Hand geprüft |
| 5 | `GetSelfGuildLock` | `0x00666490` | 57 | von Hand geprüft |
| 6 | `IsSelfGuildOperation` | `0x006664D0` | 110 | von Hand geprüft |
| 7 | `GetSelfCharLevel` | `0x00666540` | 62 | von Hand geprüft |
| 8 | `GetMemberList` | `0x006693D0` | 609 | von Hand geprüft |
| 9 | `SearchGuildMember` | `0x00666580` | 240 | von Hand geprüft |
| 10 | `SendCreateGuild` | `0x00666680` | 230 | von Hand geprüft |
| 11 | `SendJoinRequest` | `0x00666770` | 182 | von Hand geprüft |
| 12 | `SendJoinReject` | `0x00666830` | 205 | von Hand geprüft |
| 13 | `SendJoin` | `0x00666900` | 167 | von Hand geprüft |
| 14 | `SendLeave` | `0x006669B0` | 133 | von Hand geprüft |
| 15 | `SendForcedLeave` | `0x00666A40` | 222 | von Hand geprüft |
| 16 | `SendDestroy` | `0x00666B20` | 225 | von Hand geprüft |
| 17 | `SendNotice` | `0x00666C10` | 310 | von Hand geprüft |
| 18 | `SendBattlePerson` | `0x00666D50` | 275 | von Hand geprüft |
| 19 | `SendBattleRequest` | `0x00666E70` | 291 | von Hand geprüft |
| 20 | `SendBattleAccept` | `0x00666FA0` | 297 | von Hand geprüft |
| 21 | `SendBattleReject` | `0x006670D0` | 276 | von Hand geprüft |
| 22 | `SendBattleCancelRequest` | `0x006671F0` | 276 | von Hand geprüft |
| 23 | `SendBattleCancelAccept` | `0x00667310` | 276 | von Hand geprüft |
| 24 | `SendBattleCancelReject` | `0x00667430` | 276 | von Hand geprüft |
| 25 | `SendBattleWithdraw` | `0x00667550` | 276 | von Hand geprüft |
| 26 | `CBInitCharacter` | `0x00667670` | 136 | Callback-Registrierung |
| 27 | `SendGuildListRequest` | `0x00667700` | 131 | von Hand geprüft |
| 28 | `SendGuildListRequestFind` | `0x00667790` | 130 | von Hand geprüft |
| 29 | `CBGuildUpdateMaxMemberCount` | `0x00667820` | 63 | Callback-Registrierung |
| 30 | `SendMaxMemberCount` | `0x00667860` | 120 | von Hand geprüft |
| 31 | `SendSelfJoin` | `0x006678E0` | 211 | von Hand geprüft |
| 32 | `SendJoinAllow` | `0x006679C0` | 289 | von Hand geprüft |
| 33 | `SendLeaveAllow` | `0x00667AF0` | 246 | von Hand geprüft |
| 34 | `SendGuildRenameGuildID` | `0x00667BF0` | 115 | von Hand geprüft |
| 35 | `CBGuildRenameGuildID` | `0x006689C0` | 46 | Callback-Registrierung |
| 36 | `RenameGuild` | `0x00667C70` | 281 | von Hand geprüft |
| 37 | `IsSelfGuildMaster` | `0x00667D90` | 62 | von Hand geprüft |
| 38 | `IsGuildBattle` | – | | kein eigener Rumpf gefunden, vermutlich in `IsGuildBattleMember` und Aufrufer eingebaut |
| 39 | `IsGuildBattleMember` | `0x00667DD0` | 360 | von Hand geprüft |
| 40 | `CBGuildRenameCharID` | `0x006689F0` | 138 | Callback-Registrierung |
| 41 | `RenameCharID` | `0x00667F40` | 106 | von Hand geprüft |
| 42 | `SetGridGuildAttachedTexture` | `0x00668A80` | 174 | von Hand geprüft |
| 43 | `SetGridGuildAttachedSmallTexture` | `0x00668B30` | 175 | von Hand geprüft |
| 44 | `ConAgcdGuildMarkTemplate` | `0x00668BE0` | 80 | Callback-Registrierung |
| 45 | `DesAgcdGuildMarkTemplate` | `0x00668C30` | 64 | Callback-Registrierung |
| 46 | `CBCheckGuildAttackable` | – | | Registrierung in der Quelle auskommentiert, im Binary keine Funktion |
| 47 | `CB_OnResultWorldChampionShipRequest` | `0x00667FB0` | 49 | Callback-Registrierung |
| 48 | `GetAttachDataGuildMarkTemplate` | `0x00667FF0` | 38 | von Hand geprüft |
| 49 | `SetTexturePath` | `0x00668020` | 36 | von Hand geprüft |
| 50 | `CBGuildMarktemplateLoad` | `0x00668C70` | 527 | Callback-Registrierung |
| 51 | `ReleaseAgcdGuildMarkTemplate` | `0x00668050` | 99 | von Hand geprüft |
| 52 | `CBGetGuildMarkTexture` | `0x006680C0` | 79 | Callback-Registrierung |
| 53 | `CBGetGuildMarkSmallTexture` | `0x00668110` | 79 | Callback-Registrierung |
| 54 | `SendGuildBuyGuildMark` | `0x00668160` | 173 | von Hand geprüft |
| 55 | `SendJointRequest` | `0x00668210` | 157 | von Hand geprüft |
| 56 | `SendJointReject` | `0x006682B0` | 135 | von Hand geprüft |
| 57 | `SendJoint` | `0x00668340` | 139 | von Hand geprüft |
| 58 | `SendJointLeave` | `0x006683D0` | 183 | von Hand geprüft |
| 59 | `SendHostileRequest` | `0x00668490` | 157 | von Hand geprüft |
| 60 | `SendHostileReject` | `0x00668530` | 135 | von Hand geprüft |
| 61 | `SendHostile` | `0x006685C0` | 137 | von Hand geprüft |
| 62 | `SendHostileLeaveRequest` | `0x00668650` | 157 | von Hand geprüft |
| 63 | `SendHostileLeaveReject` | – | | keine Funktion im Binary, die Operation 42 sendet (vom Linker entfernt) |
| 64 | `SendHostileLeave` | `0x006686F0` | 148 | von Hand geprüft |
| 65 | `SendWorldChampionshipRequest` | `0x00668790` | 94 | von Hand geprüft |
| 66 | `SendWorldChampionshipEnter` | `0x006687F0` | 94 | von Hand geprüft |
| 67 | `SendAppointRequest` | `0x00668850` | 72 | von Hand geprüft |
| 68 | `SendAppointAnswer` | `0x006688A0` | 89 | von Hand geprüft |
| 69 | `SendSuccessionRequest` | `0x00668900` | 64 | von Hand geprüft |
| 70 | `SendSuccessionAnswer` | `0x00668940` | 72 | von Hand geprüft |

68 von 71 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmGuild` (`0x006663C0`), `~AgcmGuild` (`0x00668990`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98 / 0xB9C / 0xBA0 / 0xBA4` | `Zeiger auf [`AgpmFactors`](AgpmFactors.md), [`AgpmGuild`](AgpmGuild.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`` | `OnAddModule` |
| `0xBA8 / 0xBAC / 0xBB0` | `Zeiger auf [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmResourceLoader`](AgcmResourceLoader.md)` | `OnAddModule` |
| `0xBB4` | `Index der Markenvorlagen-Zusatzdaten` | `OnAddModule`, `GetAttachDataGuildMarkTemplate` |
| `0xBB8` | `Texturpfad (Puffer)` | `SetTexturePath` |

## Vtable

Vtable bei `0x008C9EEC`: Slot 0 Destruktor `0x00668990`, 1 `OnAddModule` (`0x00668EE0`), 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`, `return TRUE`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (`OnIdle`), 6 und 7 `0x0067AC90` (`OnDestroy`).

## OnAddModule (0x00668EE0)

Holt in dieser Reihenfolge `AgpmGuild` (`this+0xB9C`), `AgpmFactors` (`0xB98`), `AgpmCharacter` (`0xBA0`), `AgcmCharacter` (`0xBA4`), `AgcmUIControl` (`0xBAC`), `AgcmResourceLoader` (`0xBB0`) und `AgcmTextBoardMng` (`0xBA8`); alle sieben sind Pflicht. Danach hängt es Zusatzdaten an die Gilden-Markenvorlage (`AttachGuildMarkTemplateData`, 0x10 Byte, Konstruktor `0x00668BE0`, Destruktor `0x00668C30`; der Index liegt in `0xBB4`) und meldet acht Rückrufe an: Charakter initialisiert → `CBInitCharacter` (`0x00667670`), Höchstmitgliederzahl → `0x00667820`, Gilden-ID umbenannt → `0x006689C0`, Zeichen-ID umbenannt → `0x006689F0`, Markenvorlage geladen → `0x00668C70`, Marken-Textur (groß/klein) → `0x006680C0`/`0x00668110` und das Ergebnis der Weltmeisterschaft (Rückruf-ID `0x44`) → `0x00667FB0`. Der in der Quelle auskommentierte Rückruf `CBCheckGuildAttackable` wird auch im Binary nicht angemeldet.

## Abfragen auf die eigene Gilde

`GetSelfGuildID` (`0x00666470`) liefert die Gilden-ID des eigenen Charakters (`AgpmGuild::GetGuildID`, `0x0054D230`), `GetSelfGuildLock` (`0x00666490`) die gesperrte Gilde (`GetGuildLock`, `0x0054D940`; die Sperre muss der Aufrufer wieder lösen), `IsSelfGuildOperation` (`0x006664D0`) vergleicht die eigene Gilden-ID mit einem Argument, `GetSelfCharLevel` (`0x00666540`) holt die Stufe über `AgpmFactors` und `IsSelfGuildMaster` (`0x00667D90`) prüft mit `IsMaster` (`0x00551550`), ob der eigene Charakter Gildenmeister ist. `SearchGuildMember` (`0x00666580`) gibt 0 für den Meister, sonst den 1-basierten Index in der Mitgliederliste und −1, wenn der Name fehlt.
`GetMemberList` (`0x006693D0`, 609 Byte) sperrt die Gilde, legt den Meister (nur bei Index 0) an die Spitze, kopiert alle übrigen Mitglieder in eine `std::list`, sortiert sie (`list::sort`, `0x00669190`) und füllt dann ab dem gewünschten Index höchstens `lMaxCount` Einträge ohne den Meister in die Ausgabeliste. `IsGuildBattleMember` (`0x00667DD0`) prüft über [`AgcmUIGuild`](AgcmUIGuild.md) (Modulabfrage), ob zwei Charaktere in einer Gildenschlacht Gegner sind.

## Pakete senden (Send…)

Alle Sendefunktionen bauen das Paket in `AgpmGuild` (`MakeGuild…Packet`, `0x0054E270`–`0x0054F780`) und schicken es mit `SendPacket` (`0x004E45A0`). Die Zuordnung ist durch die Quellreihenfolge und die Operationsnummern der Pakete gestützt (1 = Beitritt anfragen, 2 = ablehnen, 3 = Beitritt, 4 = Austritt, 5 = Hinauswurf, 14 = Schlacht-Teilnehmer, 28 = Gildenliste, 34 ff. = Bündnis/Feindschaft):

| Funktion | Adresse | `MakeGuild…Packet` |
|---|---|---|
| `SendCreateGuild` | `0x00666680` | `0x0054E270` |
| `SendJoinRequest` | `0x00666770` | `0x0054E300` (Op 1) |
| `SendJoinReject` | `0x00666830` | `0x0054E3B0` (Op 2) |
| `SendJoin` | `0x00666900` | `0x0054E460` (Op 3) |
| `SendLeave` | `0x006669B0` | `0x0054E5D0` (Op 4) |
| `SendForcedLeave` | `0x00666A40` | `0x0054E680` (Op 5) |
| `SendDestroy` | `0x00666B20` | `0x0054E730` |
| `SendNotice` | `0x00666C10` | `0x0054E800` |
| `SendBattlePerson` | `0x00666D50` | `0x0054E970` (Op 14) |
| `SendBattleRequest` / `Accept` / `Reject` | `0x00666E70` / `0x00666FA0` / `0x006670D0` | `0x0054EA20` / `0x0054EA80` / `0x0054EB00` |
| `SendBattleCancelRequest` / `CancelAccept` / `CancelReject` | `0x006671F0` / `0x00667310` / `0x00667430` | `0x0054EB40` / `0x0054EB90` / `0x0054EBE0` |
| `SendBattleWithdraw` | `0x00667550` | `0x0054EC30` |
| `SendGuildListRequest` / `…RequestFind` | `0x00667700` / `0x00667790` | `0x0054F660` (Op 28) / `0x0054F720` |
| `SendMaxMemberCount` | `0x00667860` | `0x0054E7A0` |
| `SendSelfJoin` / `SendJoinAllow` / `SendLeaveAllow` | `0x006678E0` / `0x006679C0` / `0x00667AF0` | alle `0x0054E520` (`MakeGuildMemberPacket`, wie in der Quelle) |
| `SendGuildRenameGuildID` | `0x00667BF0` | `0x0054F780` |
| `SendGuildBuyGuildMark` | `0x00668160` | `0x0054EC70` / `0x0054ECE0` (normal/erzwungen) |
| `SendJointRequest` / `Reject` / `Joint` / `JointLeave` | `0x00668210` / `0x006682B0` / `0x00668340` / `0x006683D0` | `0x0054ED50` … `0x0054EFD0` (Op 34–37) |
| `SendHostileRequest` / `Reject` / `Hostile` | `0x00668490` / `0x00668530` / `0x006685C0` | `0x0054F090` / `0x0054F160` / `0x0054F230` (Op 38–40) |
| `SendHostileLeaveRequest` / `SendHostileLeave` | `0x00668650` / `0x006686F0` | `0x0054F310` (Op 41) / `0x0054F3E0` (Op 43) |

`SendHostileLeaveReject` (Operation 42) hat im Binary keine Funktion; die Operation wird vom Client nicht gesendet. `SendCreateGuild` verlangt Namen bis 32 und Passwort bis 12 Zeichen (`AGPMGUILD_MAX_GUILD_ID_LENGTH`/`…PASSWORD_LENGTH`); `SendNotice` prüft, dass die eigene Gilde existiert, der Name höchstens 32 Zeichen hat und der Sender Gildenmeister ist.

**Weltmeisterschaft, Ernennung, Nachfolge:** Diese vier Funktionen senden kein Gilden-Paket, sondern ein Paket über `0x00597780`: `SendWorldChampionshipRequest` (`0x00668790`) und `…Enter` (`0x006687F0`) füllen eine Struktur mit festen Kennungen (`0x15`, `0x18`, `0x2F`) und der Unterart 1 bzw. 2 und der Charakter-ID; `SendAppointRequest` (`0x00668850`), `SendAppointAnswer` (`0x006688A0`), `SendSuccessionRequest` (`0x00668900`) und `SendSuccessionAnswer` (`0x00668940`) rufen die Hilfsfunktionen `0x006661B0`, `0x00666230`, `0x006662C0`, `0x00666340` auf, die das Paket füllen, und senden es ebenfalls mit `0x00597780`.

## Umbenennung

`SendGuildRenameGuildID` (`0x00667BF0`) sendet die Umbenennung. Der Rückruf `CBGuildRenameGuildID` (`0x006689C0`) ruft `RenameGuild` (`0x00667C70`), das die Gilden-ID im Charakter und im Textbrett (`AgcmTextBoardMng`) ersetzt; `CBGuildRenameCharID` (`0x006689F0`) ruft `RenameCharID` (`0x00667F40`), das die Zeichen-ID in der Mitgliederliste tauscht.

## Gilden-Markenvorlage

`ConAgcdGuildMarkTemplate` (`0x00668BE0`) und `DesAgcdGuildMarkTemplate` (`0x00668C30`) legen die Zusatzdaten an bzw. rufen `ReleaseAgcdGuildMarkTemplate` (`0x00668050`), das beide Texturen freigibt (`0x004BF000`) und beide Puffer löscht. `CBGuildMarktemplateLoad` (`0x00668C70`) lädt die Textur über den `AgcmResourceLoader`; `SetTexturePath` (`0x00668020`) kopiert den Pfad (höchstens 0x104 Zeichen) nach `this+0xBB8`. `SetGridGuildAttachedTexture`/`…SmallTexture` (`0x00668A80`/`0x00668B30`) laden bei Bedarf die Textur und setzen die Gitterfelder (Markierung `0x33`); `CBGetGuildMarkTexture`/`…SmallTexture` (`0x006680C0`/`0x00668110`) liefern die Textur zurück.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, `SendCreateGuild`-Grenzen, `SendNotice`-Prüfungen, `SearchGuildMember`).

## Grenzen

- Die Sendefunktionen zwischen `SendDestroy` und `SendBattleWithdraw` sind über die Quellreihenfolge und die Operationsnummern 1–5 und 14 als Anker zugeordnet; die Einzelzuordnung der Schlachtpakete (Request/Accept/Reject/Cancel…) beruht auf dieser Reihenfolge, nicht auf einem Vergleich der Operationsnummern jeder Funktion.
- `GetMemberList` ist über Aufrufe (Sperre, Sortierung, Mitgliederliste) und Länge zugeordnet, nicht Zeile für Zeile verglichen.
- Die Hilfsfunktionen für Ernennung und Nachfolge (`0x006661B0`…`0x00666340`) wurden nicht im Einzelnen gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 3, nicht im Client: 2, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIGuild`](AgcmUIGuild.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmGuild`](AgpmGuild.md)
