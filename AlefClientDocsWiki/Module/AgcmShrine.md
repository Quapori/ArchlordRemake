# AgcmShrine (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmShrine` (Schrein-Kampf: Symbole, Listen, Statusfenster, Meldungen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmShrine/AgcmShrine.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, alle UI-Anmeldungen samt Rückrufen, die Listen-Suchfunktionen, `ClickShrine`, `SetTapControl`, `_ChangeShrineIcon`, die Fensterprüfung und `IsOtherRace`. Nicht zugeordnet sind `_SortShrineInfo`, `_CopyShrinInfo`, `_ShowTimeBar`, `_ChangeShrineObject`, `_ChangeTapUI`, `MakeShrineMessageByMessageCode`, die `_MessagePrintChecker…`- und `…PrintMessage…`-Familie, `_GetColorFromXml`, `_GetMsg…`, `EnterGameMode` und `CBDPMaxLefttime`/`CBDPMiniLefttime`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmShrine.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0068A6A0` | 434 | vtable/String |
| 1 | `OnInit` | `0x00684C10` | 172 | vtable/String |
| 2 | `OnDestroy` | `0x00687530` | 367 | vtable/String |
| 3 | `_LoadShrineMessage` | `0x006880F0` | 1241 | Zeichenkette |
| 4 | `_GetColorFromXml` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 5 | `AddFunction` | `0x00686D00` | 316 | vtable/String |
| 6 | `AddDisplay` | `0x006876A0` | 556 | vtable/String |
| 7 | `AddUserData` | `0x00684D80` | 510 | vtable/String |
| 8 | `AddEvent` | `0x00684F80` | 166 | vtable/String |
| 9 | `OnIdle` | `0x006889A0` | 1918 | vtable/String |
| 10 | `ClickShrine` | `0x006868C0` | 358 | Zeichenkette |
| 11 | `SetTapControl` | `0x00689120` | 446 | Zeichenkette |
| 12 | `EnterGameMode` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 13 | `_GetMsgRaceInfo` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `_GetMsgMessge` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `_CopyShrinInfo` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `_SortShrineInfo` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `_IsJoinShrine` | `0x006850D0` | 83 | von Hand geprüft |
| 18 | `_GetShrineInfo` | `0x00685130` | 57 | von Hand geprüft |
| 19 | `_GetShrineInfoIndex` | `0x00685170` | 40 | von Hand geprüft |
| 20 | `_GetShrineInfoIndex` | `0x006851A0` | 143 | von Hand geprüft |
| 21 | `_GetShrineOccupateCount` | `0x00685230` | 121 | von Hand geprüft |
| 22 | `_ChangeShrineIcon` | `0x00686AA0` | 358 | Zeichenkette |
| 23 | `_GetShrineStatus` | `0x006852B0` | 161 | von Hand geprüft |
| 24 | `_ShowTimeBar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 25 | `_ChangeShrineObject` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `_ChangeTapUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `_MessagePrintCheckerType` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `_MessagePrintCheckerTargetPlace` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `_MessagePrintCheckerTargetRace` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `CBShrineTimeToggleShow` | `0x006855C0` | 40 | Callback-Registrierung |
| 31 | `CBShrinePointStatusUpdate` | `0x00689520` | 107 | Callback-Registrierung |
| 32 | `CBShrinePointUpdateInfo` | `0x00689590` | 1007 | Callback-Registrierung |
| 33 | `CBAllShrinePointUpdateInfo` | `0x00689980` | 621 | Callback-Registrierung |
| 34 | `CBResultImprint` | `0x00689C00` | 642 | Callback-Registrierung |
| 35 | `CBReadyToStart` | `0x00689E90` | 313 | Callback-Registrierung |
| 36 | `CBShrineMessage` | `0x00689FD0` | 1681 | Callback-Registrierung |
| 37 | `CBShrinePvPRecord` | `0x006855F0` | 86 | Callback-Registrierung |
| 38 | `CBShrineRaceRecord` | `0x00685650` | 86 | Callback-Registrierung |
| 39 | `CBOpenShrineInfo` | `0x006856B0` | 292 | UI-Registrierung |
| 40 | `CBShrineIconClick` | `0x006857E0` | 315 | UI-Registrierung |
| 41 | `CBMaximizeShrineBattleInfo` | `0x00685920` | 184 | UI-Registrierung |
| 42 | `CBMinimizeShrineBattleInfo` | `0x006859E0` | 184 | UI-Registrierung |
| 43 | `CBShrineTapStatus` | `0x00686C10` | 75 | UI-Registrierung |
| 44 | `CBShrineTapScroe` | `0x0078B6A0` | 10 | Callback-Registrierung |
| 45 | `CBInfoListPrev` | `0x00685AA0` | 79 | UI-Registrierung |
| 46 | `CBInfoListNext` | `0x00685AF0` | 103 | UI-Registrierung |
| 47 | `CBShrineHPMAX` | `0x00685B60` | 84 | UI-Registrierung |
| 48 | `CBShrineHPCUR` | `0x00685BC0` | 65 | UI-Registrierung |
| 49 | `CBShrineHPDP` | `0x00687120` | 288 | UI-Registrierung |
| 50 | `CBShrineUpdate` | `0x00685C10` | 77 | UI-Registrierung |
| 51 | `CBShrineOccHCount` | `0x00685C60` | 51 | UI-Registrierung |
| 52 | `CBShrineOccOCount` | `0x00685CA0` | 51 | UI-Registrierung |
| 53 | `CBDPListStatus` | `0x00685CE0` | 207 | UI-Registrierung |
| 54 | `CBDPListName` | `0x00685DB0` | 91 | UI-Registrierung |
| 55 | `CBDPListShrineStatusBarCur` | `0x00685E10` | 129 | UI-Registrierung |
| 56 | `CBDPListShrineStatusBarMax` | `0x00685EA0` | 313 | UI-Registrierung |
| 57 | `CBDPListShrineStatusText` | `0x00685FF0` | 224 | UI-Registrierung |
| 58 | `CBDPListOccupyRace` | `0x006860F0` | 237 | UI-Registrierung |
| 59 | `CBDPListOccupyPCName` | `0x006861F0` | 125 | UI-Registrierung |
| 60 | `CBDPListRemainTime` | `0x00686270` | 212 | UI-Registrierung |
| 61 | `CBDPListPage` | `0x00686350` | 69 | UI-Registrierung |
| 62 | `CBDPMaxLefttime` | – | | gemeinsamer Anzeigerückruf `0x006863A0` (`LeftTimeMax_Time_DISP`) |
| 63 | `CBDPMiniLefttime` | – | | gemeinsamer Anzeigerückruf `0x006863A0` (`LeftTime_Mini_DISP`) |
| 64 | `CBDPMaxMyWin` | `0x006863E0` | 41 | UI-Registrierung |
| 65 | `CBDPMaxMyLose` | `0x00686410` | 41 | UI-Registrierung |
| 66 | `CBDPMaxRaceWin` | `0x00686440` | 41 | UI-Registrierung |
| 67 | `CBDPMaxRaceLose` | `0x00686470` | 41 | UI-Registrierung |
| 68 | `CloseAllBattleWindow` | `0x006864A0` | 134 | von Hand geprüft |
| 69 | `CheckBattleWindow` | `0x00686530` | 126 | von Hand geprüft |
| 70 | `CBShrineBattleInfoOpenUI` | `0x006865B0` | 143 | UI-Registrierung |
| 71 | `MakeShrineMessageByMessageCode` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 72 | `_SelfPrintShrineMessageChat` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 73 | `_SelfPrintShrineMessageCenter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 74 | `SelfPrintMessageChat` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 75 | `SelfPrintMessageCenter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 76 | `_ReservePrintMessage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 77 | `IsOtherRace` | `0x00686730` | 94 | von Hand geprüft |

58 von 78 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcmShrine` (`0x00688980`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBBC` | `Schrein-Punkte-Feld (10 Elemente zu `0xA0` Byte; Kennung am Anfang)` | `_GetShrineInfo`, `_GetShrineInfoIndex` |
| `this+0x3240` | `Zahl der aktiven Schreine (`m_iShrineEnableCount`)` | `_IsJoinShrine` |

## Vtable

Vtable-Slots: 0 `~AgcmShrine` (`0x00688980`), 1 `OnAddModule` (`0x0068A6A0`), 2 `OnInit` (`0x00684C10`), 3 `OnIdle` (`0x006889A0`), 4 und 5 `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x00687530`).

## OnAddModule und OnInit

`OnAddModule` (`0x0068A6A0`) holt [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmShrineBattle`](AgpmShrineBattle.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter` und [`AgcmEventEffect`](AgcmEventEffect.md) (Zeichenketten im Dekompilat, wie in der Quelle) und legt den Renderer `ShrineRender` an. `OnInit` (`0x00684C10`) holt [`AgcmFont`](AgcmFont.md) und lädt die zehn Schrein-Symbole: `Shrine_Icon_Battle.png`, `…_Disable.png`, `…_Enable_a.png` bis `…_Enable_d.png`, `…_Human.png`, `…_Orc.png`, `…_Moon.png`, `…_Dra.png`.

## UI-Anmeldungen

`AddFunction` (`0x00686D00`): neun Funktionen `Func_OpenShrineInfo`, `Func_ShrineIconClick`, `Func_ShrineInfoTapStatus`, `Func_ShrineInfoTapScroe` (so geschrieben), `Func_ShrineInfoListPrev`, `…ListNext`, `Func_ShrineBattleInfo_Maximize`, `…_Minimize`, `…_Open`. `AddDisplay` (`0x006876A0`): 21 Anzeigen – `DP_ShrineHPMax/Cur/DP`, `DP_Shrine_Name`, `DP_Shrine_Occ_H_Count`/`…O_Count`, die zehn `DP_Shrine_List_…`, `LeftTimeMax_Time_DISP`, `LeftTime_Mini_DISP` (beide mit demselben Rückruf `0x006863A0`), `MyWin_DISP`, `MyLose_DISP`, `RaceWin_DISP`, `RaceLose_DISP`. `AddUserData` (`0x00684D80`): 14 Benutzerdaten (`UDShrineHP`, `UD_Shrine_Update`, `UD_Shrine_List_Page`, `UD_Shrine_Info_List`, vier `UD_Occupate_*_Count`, `LeftTimeMax_Time_UD`, `MyWin_UD`, `MyLose_UD`, `RaceWin_UD`, `RaceLose_UD`, `LeftTime_Mini_UD`). `AddEvent` (`0x00684F80`): sechs Ereignisse (`Event_Shrine_HP_Show`, `…_Hide`, `ShrineBattleInfoOpen`, `Event_Shrine_Update`, `ShrineOpenSound`, `ShrineCloseSound`). Alle Namen stimmen mit der Quelle überein; die Rückrufe waren schon über diese Anmeldungen benannt.

## Schrein-Listen

Die kleinen Suchfunktionen liegen als Gruppe bei `0x006850D0`–`0x006852B0`: `_IsJoinShrine` (`0x006850D0`), `_GetShrineInfo` (`0x00685130`, liefert Zeiger auf Element der Größe `0xA0`), `_GetShrineInfoIndex(ID)` (`0x00685170`), `_GetShrineInfoIndex(Format, Name)` (`0x006851A0`, mit `sprintf`), `_GetShrineOccupateCount` (`0x00685230`, zählt die besetzten Schreine einer Rasse; der Zähler ist über zehn Plätze ausgerollt), `_GetShrineStatus` (`0x006852B0`). Es gibt höchstens zehn Schreine (Schleife bis 10).

## Kampf-Fenster und Rasse

`CloseAllBattleWindow` (`0x006864A0`) und `CheckBattleWindow` (`0x00686530`) holen die beiden Fenster `UI_ShrineBattle_Info_Maximum`/`…_Minimum`, schließen sie bzw. lesen deren Zustand. `IsOtherRace` (`0x00686730`) prüft Region, „ist Spieler“ und „gleiche Rasse wie ich“.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Suchfunktionen (`0x006850D0`–`0x006852B0`) sind über Feldabstände (`0xA0`), Schleifengrenze 10 und die Quellreihenfolge zugeordnet, nicht Zeile für Zeile verglichen; `_GetShrineStatus` ist nur über den Funktionskopf (Zeiger mit Kennung → Index) zugeordnet.
- `CloseAllBattleWindow` und `CheckBattleWindow` sind über die beiden Fenstername-Zeichenketten und die Anzahl der Fenster-Aufrufe zugeordnet; die Reihenfolge folgt der Quelle.
- Die Offsets stammen aus den genannten Funktionen; die Feldnamen der Quelle wurden nicht nachgeprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 3, eingebaut: 6, nicht im Client: 2, ohne Kandidat: 6, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `_ReservePrintMessage` | 30 | `0x006879B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_ChangeShrineObject` | 45 | `0x00685480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_ShowTimeBar` | 36 | `0x00685380` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `_CopyShrinInfo` (`0x006892F0`), `_SortShrineInfo` (`0x006892F0`), `MakeShrineMessageByMessageCode` (`0x006885D0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmFont`](AgcmFont.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmShrineBattle`](AgpmShrineBattle.md)
- **Erwähnt in:** [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIEventBank`](AgcmUIEventBank.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIRemission`](AgcmUIRemission.md)
