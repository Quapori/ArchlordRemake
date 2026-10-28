# AgcmTextBoardMng (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmTextBoardMng` (Manager für Namens-, Lebensbalken-, Schadens-, Sprechblasen- und Emoticon-Bretter) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`) der Funktionen in Export-Lücken, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmTextBoard/AgcmTextBoardMng.cpp` und `AgcmTextBoardMngCallback.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten: alle über Registrierung, Aufrufgraph oder Aufrufmuster auffindbaren Methoden sind zugeordnet. Eingebaut sind u. a. `_CreateHPBar`, `GetBoard(UINT32)`, `DestroyBoard(AgcmBaseBoard*)`, `DestroyBoard(sBoardDataPtr)`, `CheckPeculiarity` und `SetWorldCamera`. Nicht im Binary sind `PvPRefreshSiege`, `RenderText`, `CB_UpdateFactor`, `CB_MissAttack` und `CB_RegionChange` (in der Quelle ohne Aufrufer bzw. ohne Anmeldung).
- **Besonderheit:** Mehrere Funktionen liegen in Lücken des Ghidra-Exports und wurden über Aufrufer und Disassembly gefunden (`0x0063B960`, `0x0063F0F6`/`0x0063F111`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmTextBoardMng.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `CreateBoard` | `0x00640040` | 55 | von Hand geprüft |
| 1 | `CreateBoard` | `0x0063FFE0` | 1196 | von Hand geprüft |
| 2 | `CreateBoard` | `0x00640550` | 55 | von Hand geprüft |
| 3 | `GetBoard` | `0x0063B290` | 71 | von Hand geprüft |
| 4 | `GetBoard` | – | | Fassung mit Spieler-ID eingebaut (holt den Charakter und ruft die andere Fassung) |
| 5 | `OnAddModule` | `0x0063CC90` | 1053 | vtable/String |
| 6 | `OnInit` | `0x00640590` | 2133 | vtable/String |
| 7 | `OnDestroy` | `0x00640080` | 697 | vtable/String |
| 8 | `OnIdle` | `0x0063E9B0` | 91 | vtable/String |
| 9 | `PostRender` | `0x0063D910` | 516 | von Hand geprüft |
| 10 | `Update` | `0x0063E750` | 185 | von Hand geprüft |
| 11 | `_Update` | `0x0063E510` | 356 | von Hand geprüft |
| 12 | `_CreateImoticon` | `0x0063EA10` | 590 | von Hand geprüft |
| 13 | `_CreateIDBoard` | `0x0063FFE0` | 1196 | gleiche Adresse wie `eingebaut in `CreateBoard(ApBase*)` (Konstruktor [`AgcmIDBoard`](AgcmIDBoard.md) und Endstück `0x0063F111`)` (vom Linker zusammengefaltet) |
| 14 | `GetTextureSize` | `0x0063C160` | 48 | von Hand geprüft |
| 15 | `EnableHPBar` | `0x0063DB20` | 428 | von Hand geprüft |
| 16 | `DisableHPBar` | `0x0063B300` | 177 | von Hand geprüft |
| 17 | `DisableHPBar` | `0x0063B3C0` | 294 | von Hand geprüft |
| 18 | `EnableGuild` | `0x0063D0B0` | 897 | von Hand geprüft |
| 19 | `DisableGuild` | `0x0063D440` | 363 | von Hand geprüft |
| 20 | `EnableParty` | `0x0063B4F0` | 167 | von Hand geprüft |
| 21 | `DisableParty` | `0x0063B5A0` | 127 | von Hand geprüft |
| 22 | `DisableAllParty` | `0x0063B620` | 124 | von Hand geprüft |
| 23 | `EnableIDFlag` | `0x0063B6A0` | 119 | von Hand geprüft |
| 24 | `DisableIDFlag` | `0x0063B720` | 105 | von Hand geprüft |
| 25 | `_CreateHPBar` | – | | eingebaut in `EnableHPBar` / `SetMainCharacter` (nicht als eigene Funktion gefunden) |
| 26 | `_CreateDmg` | `0x0063F180` | 721 | von Hand geprüft |
| 27 | `_CreateText` | `0x0063F460` | 949 | von Hand geprüft |
| 28 | `_CreateItemID` | – | | nicht einzeln gefunden; vermutlich in `CreateBoard(ApBase*)` eingebaut |
| 29 | `GetPointPercent` | `0x0063B790` | 225 | von Hand geprüft |
| 30 | `GetGuildIDColor` | `0x0063D5B0` | 174 | von Hand geprüft |
| 31 | `GetGuildIDColor` | `0x0063B880` | 187 | von Hand geprüft |
| 32 | `DrawGuildImage` | `0x0063D660` | 263 | von Hand geprüft |
| 33 | `CalculateJointGuildMarkPositionOffset` | `0x0063B960` | 107 | von Hand geprüft |
| 34 | `ChangeIDColor` | `0x0063D770` | 156 | von Hand geprüft |
| 35 | `GetTargetIDColor` | `0x0063B9D0` | 530 | von Hand geprüft |
| 36 | `SetTexture` | `0x0063F9F0` | 257 | von Hand geprüft |
| 37 | `UpdateNickName` | `0x0063DCD0` | 332 | von Hand geprüft |
| 38 | `ChangeGuildIDColor` | `0x0063DE20` | 873 | von Hand geprüft |
| 39 | `SetHeight` | `0x0063BBF0` | 201 | von Hand geprüft |
| 40 | `UpdateIDBoardHPBar` | `0x0063E1A0` | 427 | von Hand geprüft |
| 41 | `DisplayUpdateFactor` | `0x00640340` | 524 | von Hand geprüft |
| 42 | `GetFactorDamage` | `0x0063BCD0` | 81 | von Hand geprüft |
| 43 | `DestroyMainBoard` | `0x0063E4E0` | 16 | von Hand geprüft |
| 44 | `SetMainCharacter` | `0x0063E680` | 197 | von Hand geprüft |
| 45 | `DestroyBoard` | `0x0063E350` | 394 | von Hand geprüft |
| 46 | `DestroyBoard` | – | | dreizeilige Fassung, eingebaut |
| 47 | `DestroyBoard` | – | | dreizeilige Fassung, eingebaut |
| 48 | `StreamReadTemplate` | `0x0063FB20` | 336 | von Hand geprüft |
| 49 | `SetAllIDEnable` | `0x0063BD30` | 132 | von Hand geprüft |
| 50 | `SetAllGuildEnable` | `0x0063BDC0` | 120 | von Hand geprüft |
| 51 | `SetAllPartyEnable` | `0x0063BE50` | 120 | von Hand geprüft |
| 52 | `PvPRefreshSiege` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 53 | `SetWorldCamera` | – | | eingebaut in `OnAddModule` |
| 54 | `Trans3DTo2D` | `0x0063D810` | 135 | von Hand geprüft |
| 55 | `GetWorldPosToScreenPos` | `0x0063BEE0` | 127 | von Hand geprüft |
| 56 | `GetCastleTexture` | `0x0063BF60` | 190 | von Hand geprüft |
| 57 | `GetStateTexture` | `0x0063C020` | 177 | von Hand geprüft |
| 58 | `RenderTexture` | `0x0063C0E0` | 113 | von Hand geprüft |
| 59 | `RenderText` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 60 | `CheckPeculiarity` | – | | eingebaut (Aufruf von [`ApmMap`](ApmMap.md):CheckRegionPerculiarity`) |
| 61 | `IsRender` | `0x0063C190` | 106 | von Hand geprüft |
| 62 | `CB_POST_RENDER` | `0x00751CB0` | 22 | Callback-Registrierung |
| 63 | `CB_UpdateIDMurderIconFlag` | `0x00751CD0` | 201 | Callback-Registrierung |
| 64 | `CB_UpdateIDFirstAttackerIconFlag` | `0x00751DA0` | 63 | Callback-Registrierung |
| 65 | `CB_SetSelfCharacter` | `0x00752BB0` | 590 | Callback-Registrierung |
| 66 | `CB_ReleaseSelfCharacter` | `0x00752E00` | 119 | Callback-Registrierung |
| 67 | `CB_AddChar` | `0x007532A0` | 608 | Callback-Registrierung |
| 68 | `CB_RemoveChar` | `0x00751DE0` | 70 | Callback-Registrierung |
| 69 | `CB_UpdateFactor` | – | | nicht im Binary: in der Quelle nicht angemeldet |
| 70 | `CB_MissAttack` | – | | nicht im Binary: in der Quelle nicht angemeldet |
| 71 | `CB_MissCastSkill` | `0x00751E30` | 123 | Callback-Registrierung |
| 72 | `CB_BlockCastSkill` | `0x00751EB0` | 115 | Callback-Registrierung |
| 73 | `CB_DisplayActionResult` | `0x00751F30` | 1278 | Callback-Registrierung |
| 74 | `CB_ItemAdd` | `0x00752460` | 184 | Callback-Registrierung |
| 75 | `CB_ItemRemove` | `0x00752520` | 20 | Callback-Registrierung |
| 76 | `CB_UpdateActionStatus` | `0x00752E80` | 61 | Callback-Registrierung |
| 77 | `CB_RegionChange` | – | | nicht im Binary: in der Quelle nicht angemeldet |
| 78 | `CB_SkillAddHPBar` | `0x00752540` | 41 | Callback-Registrierung |
| 79 | `CB_HPUpdate` | `0x00752570` | 117 | Callback-Registrierung |
| 80 | `CB_MPUpdate` | `0x007525F0` | 84 | Callback-Registrierung |
| 81 | `CB_Guild` | `0x00753500` | 128 | Callback-Registrierung |
| 82 | `CB_PartyAdd` | `0x00752EC0` | 69 | Callback-Registrierung |
| 83 | `CB_PartyLeave` | `0x00752650` | 15 | Callback-Registrierung |
| 84 | `CB_PartyAddMember` | `0x00752660` | 20 | Callback-Registrierung |
| 85 | `CB_PartyLeaveMember` | `0x00752680` | 20 | Callback-Registrierung |
| 86 | `CB_UpdateIDBoard` | `0x007526A0` | 365 | von Hand geprüft |
| 87 | `CB_UpdateIDBoardHPBar` | `0x00752810` | 320 | von Hand geprüft |
| 88 | `CB_PvPRefreshChar` | `0x00752950` | 181 | Callback-Registrierung |
| 89 | `CB_PvPRefreshGuild` | `0x00752F10` | 910 | Callback-Registrierung |
| 90 | `CB_PvPInit` | `0x00753580` | 131 | Callback-Registrierung |
| 91 | `CB_DestroyBoard` | `0x00752A10` | 40 | Callback-Registrierung |
| 92 | `CB_KillCharacter` | `0x00752A40` | 329 | Callback-Registrierung |
| 93 | `CB_UpdateNickName` | `0x00752B90` | 22 | Callback-Registrierung |

82 von 94 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `DisableHPBar_ApBase` (`0x0063B300`), `DisableHPBar_Clump` (`0x0063B3C0`), `GetGuildIDColor_guild` (`0x0063B880`), `GetGuildIDColor_member` (`0x0063D5B0`), `~AgcmTextBoardMng_body` (`0x0063E8F0`), `CreateBoard_tail_0063f0f6` (`0x0063F0F6`), `CreateBoard_tail_0063f111` (`0x0063F111`), `AgcmTextBoardMng` (`0x0063FCA0`), `scalar_deleting_dtor` (`0x0063FFC0`), `CreateBoard_ID` (`0x00640040`), `CreateBoard_GameID` (`0x00640550`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xFEC / 0xFF4` | `Zeiger auf `AgcmCharacter` (zwei Kopien: `m_pcCmCharacter`, `m_pcsAgcmCharacter`; `+0x1596C` ist der eigene Charakter)` | `DisableHPBar`, `CreateBoard(UINT32)` |
| `this+0xFF0` | `Zeiger [`AgcmRender`](AgcmRender.md) (für `AddUpdateInfotoClump`)` | `CreateBoard` (Endstück) |
| `this+0x1008` | `Zeiger [`AgcmItem`](AgcmItem.md) (Gegenstandsdaten)` | `DisableHPBar` |
| `this+0x11B8 / 0x11BC / 0x11CC` | `Namensoptionen (eigener Charakter / Monster / andere)` | `DisableHPBar`, [`AgcmTextBoard`](AgcmTextBoard.md):Update` |
| `this+0x11C0 / 0x11C4` | `Gilden- / Gruppenanzeige` | `AgcmTextBoard::Update` |
| `this+0x11DC` | `Brettdaten des Hauptcharakters (`sBoardData*`, `+0xC` = [`AgcmHPBar`](AgcmHPBar.md))` | `DisableHPBar`, `AgcmTextBoard::Render` |

## Vtable und Aufbau

`AgcmTextBoardMng` verwaltet alle Bretter (Namen, Lebensbalken, Schaden, Sprechblasen, Emoticons) über Charakteren und Gegenständen. Konstruktor `0x0063FCA0` (786 Byte), Destruktorrumpf `0x0063E8F0`, Löschwrapper `0x0063FFC0`. Der Pool der Brettdaten ist `ApMemory<_sBoardData,1000>` (`0x0063E850`/`0x0063D8E0`/`0x0063FC80`). `OnAddModule` (`0x0063CC90`, 1.053 Byte) holt 23 Module und meldet die Rückrufe an (siehe unten), `OnInit` (`0x00640590`, 2.133 Byte) lädt Texturen, Farben und die Flaggen, `OnDestroy` (`0x00640080`) gibt alles frei, `OnIdle` (`0x0063E9B0`, 91 Byte) ruft `Update` (`0x0063E750`) mit der Kameramatrix.

## Rückrufe

`OnAddModule` meldet 29 Rückrufe an: `CB_POST_RENDER` (`0x00751CB0`) bei `AgcmRender`; `CB_AddChar` (`0x007532A0`), `CB_RemoveChar` (`0x00751DE0`), `CB_SetSelfCharacter` (`0x00752BB0`), `CB_ReleaseSelfCharacter` (`0x00752E00`), `CB_DisplayActionResult` (`0x00751F30`), `CB_HPUpdate` (`0x00752570`), `CB_MPUpdate` (`0x007525F0`), `CB_KillCharacter` (`0x00752A40`) und `CB_DestroyBoard` (`0x00752A10`) bei `AgcmCharacter`; `CB_ItemAdd`/`CB_ItemRemove` (`0x00752460`/`0x00752520`) bei `AgcmItem`; `CB_UpdateActionStatus` (`0x00752E80`), `CB_UpdateIDFirstAttackerIconFlag` (`0x00751DA0`) und `CB_UpdateNickName` (`0x00752B90`) bei [`AgpmCharacter`](AgpmCharacter.md); `CB_UpdateIDMurderIconFlag` (`0x00751CD0`) bei [`AgpmFactors`](AgpmFactors.md); `CB_MissCastSkill`, `CB_BlockCastSkill`, `CB_SkillAddHPBar` bei [`AgcmSkill`](AgcmSkill.md); `CB_Guild` (`0x00753500`), vier Gruppen-Rückrufe (`0x00752EC0`, `0x00752650`, `0x00752660`, `0x00752680`) und fünf PvP-Rückrufe (`CB_PvPRefreshChar` `0x00752950`, `CB_PvPRefreshGuild` `0x00752F10`, `CB_PvPInit` `0x00753580`).
Zwei weitere Rückrufe hängt der Manager an die Klumpen der Bretter: `CB_UpdateIDBoard` (`0x007526A0`, Position und Alpha des Namensbretts) und `CB_UpdateIDBoardHPBar` (`0x00752810`, ruft `UpdateIDBoardHPBar` `0x0063E1A0`); der erste wird im Endstück von `CreateBoard` (`0x0063F111`) angemeldet, der zweite in `CB_SetSelfCharacter` anstelle des ersten für den Hauptcharakter. `CB_UpdateFactor`, `CB_MissAttack` und `CB_RegionChange` sind in der Quelle nirgends angemeldet und nicht im Binary.

## Bretter erzeugen und zerstören

`CreateBoard(ApBase*, sBoardAttr*)` (`0x0063FFE0`, 1.196 Byte, mit Endstücken `0x0063F0F6`/`0x0063F111`) legt je nach Attribut ein Brett an: Namensbrett (der `AgcmIDBoard`-Konstruktor `0x00754010` und `_CreateIDBoard` sind hier eingebaut), Sprechblase `_CreateText` (`0x0063F460`), Schaden `_CreateDmg` (`0x0063F180`), Emoticon `_CreateImoticon` (`0x0063EA10`). Die Fassungen mit Spieler-ID (`0x00640040`) und Spielzeichenkette (`0x00640550`) holen den Charakter über `AgpmCharacter` und rufen sie. `EnableHPBar` (`0x0063DB20`, 428 Byte, Aufrufer [`AgcmTargeting`](AgcmTargeting.md)) legt das Lebensbalkenbrett an (`_CreateHPBar` ist darin eingebaut); `DisableHPBar` gibt es als Fassung für `ApBase*` (`0x0063B300`) und für `RpClump*` (`0x0063B3C0`).
`DestroyBoard(ApBase*)` (`0x0063E350`) löscht die Bretter eines Charakters oder Gegenstands; `DestroyMainBoard` (`0x0063E4E0`) das des Hauptcharakters; `SetMainCharacter` (`0x0063E680`) legt dafür ein neues `AgcmHPBar` an und kopiert die Daten (`AgcmHPBar::SetData`). `_Update` (`0x0063E510`) aktualisiert ein einzelnes Brett.

## Namen, Gilden, Gruppen

`EnableGuild` (`0x0063D0B0`, 897 Byte) setzt Gildenname, Farbe und Anzeigeflag und berechnet den Versatz neu (`AgcmIDBoard::ReCalulateOffsetX`); `DisableGuild` (`0x0063D440`) löscht sie wieder (beide aus `CB_Guild`). `EnableParty`/`DisableParty`/`DisableAllParty` (`0x0063B4F0`, `0x0063B5A0`, `0x0063B620`) steuern die Gruppenanzeige, `EnableIDFlag`/`DisableIDFlag` (`0x0063B6A0`, `0x0063B720`) die Flaggen am Namensbrett (Mörder- und Erstangreifer-Symbol), `SetAllIDEnable`/`SetAllGuildEnable`/`SetAllPartyEnable` (`0x0063BD30`, `0x0063BDC0`, `0x0063BE50`) die Optionen aus [`AgcmUIOption`](AgcmUIOption.md). `UpdateNickName` (`0x0063DCD0`) und `SetHeight` (`0x0063BBF0`) aktualisieren Spitzname bzw. Höhe.
Farben: `GetGuildIDColor` in zwei Fassungen (`0x0063D5B0` mit Spielerkennung, `0x0063B880` mit Gilde und Mitglied), `ChangeIDColor` (`0x0063D770`), `ChangeGuildIDColor` (`0x0063DE20`, 873 Byte, aus `CB_PvPRefreshGuild`) und `GetTargetIDColor` (`0x0063B9D0`, 530 Byte, aus `CB_PvPRefreshChar`: Gegner, Freund, Gildenkampf, Monster). `DrawGuildImage` (`0x0063D660`) zeichnet die Gildenmarken, `CalculateJointGuildMarkPositionOffset` (`0x0063B960`) die Lage für verbündete Gilden.

## Zeichnen und Hilfen

`PostRender` (`0x0063D910`, 516 Byte; gerufen von `CB_POST_RENDER`) rendert nacheinander alle Bretter; `Trans3DTo2D` (`0x0063D810`) und `GetWorldPosToScreenPos` (`0x0063BEE0`) rechnen Weltpunkte in Bildschirmkoordinaten (mit Kehrwert z) um. `RenderTexture` (`0x0063C0E0`), `GetTextureSize` (`0x0063C160`), `IsRender` (`0x0063C190`, Sichtbarkeit je Charakter), `GetStateTexture` (`0x0063C020`, Belagerungs-Symbole), `GetCastleTexture` (`0x0063BF60`), `GetPointPercent` (`0x0063B790`), `GetFactorDamage` (`0x0063BCD0`) und `DisplayUpdateFactor` (`0x00640340`) sind die Zeichen- und Anzeigehilfen. `SetTexture` (`0x0063F9F0`) und `StreamReadTemplate` (`0x0063FB20`, Zeichenkette `%d:%s`) laden die Texturen der Vorlagendatei.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen wurden die Rückrufe `CB_UpdateIDBoard`/`CB_UpdateIDBoardHPBar` (Zeile für Zeile verglichen), `OnAddModule` (Registrierung) und die Aufrufmuster der Erzeuger; die übrigen Zuordnungen beruhen auf Aufrufer-/Callee-Beziehungen, Größen und je einem Merkmal (z. B. [`AgcmSiegeWar`](AgcmSiegeWar.md)-Aufrufe für `GetStateTexture`, `AgcmIDBoard`-Konstruktor für `CreateBoard`) und wurden nicht Zeile für Zeile verglichen.
- Die Rückrufe der Gruppen- und PvP-Anmeldungen sind über die Reihenfolge der Anmeldungen in `OnAddModule` den schon früher benannten Adressen zugeordnet.
- `_CreateItemID` und `_CreateHPBar` sind nicht einzeln gefunden; dass sie eingebaut sind, ist aus der Größe der Aufrufer (`CreateBoard` 1.196 Byte, `EnableHPBar` 428 Byte) gefolgert, nicht bewiesen.
- Die Offsets des Managers stammen aus Zugriffen in anderen Funktionen; die Zuordnung der beiden `AgcmCharacter`-Zeiger zu `m_pcCmCharacter`/`m_pcsAgcmCharacter` ist nicht belegt.
- `0x0063B1E0` (112 Byte, Aufrufer u. a. [`AgcChatManager`](AgcChatManager.md):OnAddMessage`) gehört wahrscheinlich zur Attribut-Struktur `sBoardAttr` (Konstruktor), ist aber keine Quellmethode und nicht weiter geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 4, eingebaut: 4, nicht im Client: 5, ohne Kandidat: 6.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `CreateBoard` (`0x006586A0`), `CreateBoard` (`0x006586A0`), `DisableHPBar` (`0x006E4A00`), `DisableHPBar` (`0x006E4A00`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcChatManager`](AgcChatManager.md), [`AgcmBaseBoard`](AgcmBaseBoard.md), [`AgcmHPBar`](AgcmHPBar.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmItem`](AgcmItem.md), [`AgcmRender`](AgcmRender.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmUIOption`](AgcmUIOption.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmGuild`](AgcmGuild.md), [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmImoticonBoard`](AgcmImoticonBoard.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTuner`](AgcmTuner.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`CFlagImoticon`](CFlagImoticon.md)
