# AgcmTitle (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcmTitle` (Titelsystem: Titelliste, Aktivieren, Aufgeben, Quests, Oberfläche) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmTitle/AgcmTitle.cpp`. Das Paketformat steht im Bericht [AgpmTitle](AgpmTitle.md). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 95 von 130 Quellmethoden zugeordnet (neu: `_GetTitleByID`, `_GetLastActivateTime`, `_SaveTitleActivateLog`, `OnActivateTitle`/`OnDeActivateTitle` je zwei Überladungen, `OnClearTitleState`/`…All`, `OnUpdateTitleCounter`/`…TimeStamp`, `OnSetSelfCharacter`, `GetTitleFontColor`, `OnUpdateTitleTextBoard`, die zwei Höchstzahl-Prüfungen); die Rückrufe, die UI-Anmeldung, die 14 Voraussetzungsprüfungen, die Dialogsteuerung und die Auswahlfunktionen sind zugeordnet. Viele kleine Getter und `_Get…By…`-Suchfunktionen sind eingebaut.
- **OnInitialize:** gleiche Reihenfolge und Dateien wie die Quelle (`titledatatable.txt`, `titlestringtable.txt`, `TitleSetting.xml`), höchstens 20000 Titelvorlagen.
- **Anmeldungen:** 10 [`AgpmTitle`](AgpmTitle.md)-Rückrufe, 2 `AgcmCharacter`-Rückrufe, 4 Benutzerdaten, 4 Anzeigen und 15 Funktionen wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmTitle.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInitialize` | `0x0065C6D0` | 156 | Zeichenkette |
| 1 | `OnUnInitialize` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `OnClearTitleState` | `0x00659F00` | 400 | von Hand geprüft |
| 3 | `OnInitTitleSetting` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 4 | `OnLoadTitleSetting` | `0x00659580` | 743 | Zeichenkette |
| 5 | `OnOpenUI` | `0x00658B80` | 216 | von Hand geprüft |
| 6 | `OnUpateUI` | `0x00657FD0` | 164 | von Hand geprüft |
| 7 | `OnCloseUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 8 | `OnSendSetTargetTitle` | `0x00658C60` | 365 | Zeichenkette |
| 9 | `OnSendTitleActivate` | `0x00655900` | 278 | Zeichenkette |
| 10 | `OnSendSurrenderTitle` | `0x00655A20` | 248 | Zeichenkette |
| 11 | `OnSendRequestTitleList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `OnSendCompleteTitle` | `0x0065B640` | 546 | Zeichenkette |
| 13 | `OnChangeTitleState` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `OnUpdateTitleCounter` | `0x00659870` | 52 | von Hand geprüft |
| 15 | `OnUpdateTitleTimeStamp` | `0x00659DA0` | 53 | von Hand geprüft |
| 16 | `OnSelectCategory` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `OnSelectCategoryByID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `OnSelectCategoryByIndex` | `0x00658080` | 265 | von Hand geprüft |
| 19 | `OnSelectTitle` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 20 | `OnSelectTitleByID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `OnSelectTitleByIndex` | `0x00658190` | 137 | von Hand geprüft |
| 22 | `OnSelectTitleCurrentByIndex` | `0x006573A0` | 124 | von Hand geprüft |
| 23 | `OnSelectTitleMiniByIndex` | `0x00657420` | 62 | von Hand geprüft |
| 24 | `OnSetSelfCharacter` | `0x00658DD0` | 60 | von Hand geprüft |
| 25 | `OnActivateTitle` | `0x006598B0` | 411 | von Hand geprüft |
| 26 | `OnActivateTitle` | `0x00659A50` | 35 | von Hand geprüft |
| 27 | `OnDeActivateTitle` | `0x00658E10` | 102 | von Hand geprüft |
| 28 | `OnDeActivateTitle` | `0x00659A80` | 35 | von Hand geprüft |
| 29 | `_RegisterCallBack` | `0x0065BA20` | 1383 | Zeichenkette |
| 30 | `_GetDialogControls` | `0x00657460` | 398 | Zeichenkette |
| 31 | `_LoadAllTitleCategoryInfo` | `0x0065C370` | 852 | von Hand geprüft |
| 32 | `_GetCategoryByID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 33 | `_GetCategoryByName` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 34 | `_GetCategoryByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 35 | `_GetTitleByID` | `0x00658ED0` | 144 | von Hand geprüft |
| 36 | `_GetTitleByID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 37 | `_GetTitleByName` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 38 | `_GetTitleByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 39 | `_GetTitleCurrentByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 40 | `_ParseTimeStamp` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 41 | `_GetLastActivateTime` | `0x00658250` | 135 | von Hand geprüft |
| 42 | `_SaveTitleActivateLog` | `0x00659AB0` | 304 | von Hand geprüft |
| 43 | `_UpdateCategoryList` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 44 | `_UpdateTitleList` | `0x00657A40` | 117 | von Hand geprüft |
| 45 | `_UpdateTitleListPage` | `0x006575F0` | 415 | von Hand geprüft |
| 46 | `_AddRunningTitle` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 47 | `_GetRunningTitleByID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 48 | `_DeleteRunningTitle` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 49 | `OnClearTitleIDBoard` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 50 | `OnClearTitleStateAll` | `0x00659DE0` | 287 | von Hand geprüft |
| 51 | `OnClearTitleCategorySelection` | `0x00655B70` | 98 | von Hand geprüft |
| 52 | `OnClearTitleSelection` | `0x00655BE0` | 194 | von Hand geprüft |
| 53 | `OnClearTitleDescription` | `0x00655CB0` | 171 | von Hand geprüft |
| 54 | `_UpdateTitleInfo` | `0x00655D60` | 346 | von Hand geprüft |
| 55 | `_UpdateTitleEffect` | `0x00655EC0` | 105 | von Hand geprüft |
| 56 | `_UpdateDialogButtonState` | `0x00656C50` | 128 | von Hand geprüft |
| 57 | `_UpdateDialogButtonStateReady` | `0x00655F30` | 73 | von Hand geprüft |
| 58 | `_UpdateDialogButtonStateRunning` | `0x00655F80` | 25 | von Hand geprüft |
| 59 | `_UpdateDialogButtonStateComplete` | `0x00655FA0` | 73 | von Hand geprüft |
| 60 | `_UpdateDialogButtonStateEnable` | `0x00655FF0` | 134 | von Hand geprüft |
| 61 | `_UpdateDialogButtonStateActivate` | `0x00656080` | 151 | Zeichenkette |
| 62 | `OnUpdateTitleTextBoard` | `0x00656CF0` | 443 | von Hand geprüft |
| 63 | `_ReSetDialogButtonState` | `0x00656120` | 197 | Zeichenkette |
| 64 | `_CheckTitleExchangeTimeLimit` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 65 | `_CheckIsMaxRunningTitle` | `0x00658470` | 100 | Zeichenkette |
| 66 | `_CheckIsMaxEnableTitle` | `0x006584E0` | 116 | von Hand geprüft |
| 67 | `_CheckIsMaxEnableAndRunningTitle` | `0x00658560` | 132 | von Hand geprüft |
| 68 | `_CheckIsValidTitleRequirement` | `0x00656EB0` | 494 | Zeichenkette |
| 69 | `_CheckIsValidRequireLevel` | `0x006561F0` | 71 | von Hand geprüft |
| 70 | `_CheckIsValidRequireGuildMaster` | `0x00656240` | 76 | von Hand geprüft |
| 71 | `_CheckIsValidRequireArchlord` | `0x00656290` | 76 | von Hand geprüft |
| 72 | `_CheckIsValidRequireClassType` | `0x006562E0` | 336 | von Hand geprüft |
| 73 | `_CheckIsValidRequireCon` | `0x00656430` | 100 | von Hand geprüft |
| 74 | `_CheckIsValidRequireStr` | `0x006564A0` | 100 | von Hand geprüft |
| 75 | `_CheckIsValidRequireInt` | `0x00656510` | 100 | von Hand geprüft |
| 76 | `_CheckIsValidRequireDex` | `0x00656580` | 100 | von Hand geprüft |
| 77 | `_CheckIsValidRequireWis` | `0x006565F0` | 100 | von Hand geprüft |
| 78 | `_CheckIsValidRequireCharisma` | `0x00656660` | 100 | von Hand geprüft |
| 79 | `_CheckIsValidRequireGheld` | `0x006566D0` | 114 | von Hand geprüft |
| 80 | `_CheckIsValidRequireCash` | `0x00656750` | 84 | von Hand geprüft |
| 81 | `_CheckIsValidRequireItem` | `0x006567B0` | 122 | von Hand geprüft |
| 82 | `_CheckIsValidRequireTitle` | `0x00656830` | 91 | von Hand geprüft |
| 83 | `_ShowErrorMessageBoxOK` | `0x00656890` | 103 | von Hand geprüft |
| 84 | `GetCategoryNameByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 85 | `GetTitleNameByID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 86 | `GetTitleNameByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 87 | `GetTitleNameByIndexWithPage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 88 | `GetTitleStateByIndexWidthPage` | `0x00657AC0` | 52 | von Hand geprüft |
| 89 | `GetCurrTitleStateByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 90 | `GetCurrTitleNameByIndexWithPage` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 91 | `GetTitleCountByState` | `0x00657B00` | 205 | von Hand geprüft |
| 92 | `GetTitleCountCurrentCategory` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 93 | `SetTitlePageIndex` | `0x00657BD0` | 149 | von Hand geprüft |
| 94 | `GetCurrentActivateTitleID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 95 | `GetCurrentActivateTitleName` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 96 | `GetTitleFontColor` | `0x00658740` | 61 | von Hand geprüft |
| 97 | `IsOpenUI` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 98 | `CallBack_RecvTitleAdd` | `0x0065A510` | 574 | Zeichenkette |
| 99 | `CallBack_RecvTitleUse` | `0x0065A750` | 445 | Zeichenkette |
| 100 | `CallBack_RecvTitleList` | `0x0065A910` | 415 | von Hand geprüft |
| 101 | `CallBack_RecvTitleDelete` | `0x0065AAB0` | 395 | von Hand geprüft |
| 102 | `CallBack_RecvTitleQuestRequest` | `0x0065AC40` | 422 | von Hand geprüft |
| 103 | `CallBack_RecvTitleQuestCheck` | `0x0065ADF0` | 754 | von Hand geprüft |
| 104 | `CallBack_RecvTitleQuestComplete` | `0x0065B0F0` | 394 | von Hand geprüft |
| 105 | `CallBack_RecvTitleQuestList` | `0x0065B280` | 958 | von Hand geprüft |
| 106 | `CallBack_RecvTitleUseNear` | `0x00659BE0` | 101 | von Hand geprüft |
| 107 | `CallBack_RecvTitleOpenUI` | `0x00658F60` | 283 | von Hand geprüft |
| 108 | `CallBack_OnRecvSelfCharacter` | `0x00659080` | 49 | von Hand geprüft |
| 109 | `CallBack_AutoCloseByCharacterMove` | `0x00656970` | 126 | von Hand geprüft |
| 110 | `CallBack_OnOpenUIAll` | `0x006590C0` | 24 | UI-Registrierung |
| 111 | `CallBack_OnOpenUICurrent` | `0x006590E0` | 357 | UI-Registrierung |
| 112 | `CallBack_OnOpenUIMini` | `0x00659250` | 274 | UI-Registrierung |
| 113 | `CallBack_DisplayCategoryName` | `0x00657C70` | 77 | UI-Registrierung |
| 114 | `CallBack_DisplayTitleName` | `0x00658780` | 170 | UI-Registrierung |
| 115 | `CallBack_DisplayTitleNameCurrent` | `0x00658830` | 164 | von Hand geprüft |
| 116 | `CallBack_DisplayTitleNameMini` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 117 | `CallBack_OnClickCategoryItem` | `0x006588E0` | 94 | UI-Registrierung |
| 118 | `CallBack_OnClickTitleItem` | `0x00658940` | 43 | UI-Registrierung |
| 119 | `CallBack_OnClickTitleItemCurrent` | `0x00657790` | 43 | UI-Registrierung |
| 120 | `CallBack_OnClickTitleItemMini` | `0x006577C0` | 43 | UI-Registrierung |
| 121 | `CallBack_OnClickPagePrev` | `0x00657CC0` | 29 | UI-Registrierung |
| 122 | `CallBack_OnClickPageNext` | `0x00657CE0` | 29 | UI-Registrierung |
| 123 | `CallBack_OnClickPage` | `0x00657D00` | 95 | UI-Registrierung |
| 124 | `CallBack_OnClickSetTargetTitle` | `0x00659370` | 22 | UI-Registrierung |
| 125 | `CallBack_OnClickActivateTitle` | `0x006569F0` | 39 | UI-Registrierung |
| 126 | `CallBack_OnClickSurrenderTitleCurrent` | `0x00656A20` | 24 | UI-Registrierung |
| 127 | `CallBack_OnClickSurrenderTitleMini` | `0x00656A40` | 24 | UI-Registrierung |
| 128 | `CallBack_OnClickCompleteTitle` | `0x0065B870` | 22 | UI-Registrierung |
| 129 | `LoadXMLFileToDocument` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

95 von 130 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `CMap_GetByIndex_template` (`0x006577F0`), `ctor_or_dtor` (`0x0065C220`), `~AgcmTitle` (`0x0065C350`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+4` | `Merker „initialisiert“` | `OnInitialize` |

## Aufbau der Klasse

`AgcmTitle` ist kein vollwertiges Modul mit `OnAddModule`: Die Klasse hat im Binary nur den Destruktor (`0x0065C350`, ruft den Hauptdestruktor `0x0065C220`) in der Vtable. Sie wird von außen mit `OnInitialize` (`0x0065C6D0`) gestartet (Aufrufer: `OnPostRegisterModule`). Der Bereich liegt bei `0x00655900`–`0x0065C6D0`; zwischen den Methoden liegen viele Hilfsfunktionen für `std::vector`/`std::list`/`std::map`, die zu keiner Quellmethode gehören.

## OnInitialize (0x0065C6D0)

Läuft nur einmal (`this+4` als „initialisiert“-Merker). Holt `AgpmTitle`, setzt die Höchstzahl der Titelvorlagen auf **20000** (`SetMaxTitleTemplate`, `0x00568450`), liest `ini\titledatatable.txt` (`0x0087BCE0`) und `ini\titlestringtable.txt` (`0x0087ACB0`) ohne Entschlüsselung (Build mit `_BIN_EXEC_`), und ruft nacheinander `_RegisterCallBack` (`0x0065BA20`), `_GetDialogControls` (`0x00657460`), `_LoadAllTitleCategoryInfo` (`0x0065C370`) und `OnLoadTitleSetting("INI\TitleSetting.xml")` (`0x00659580`). Reihenfolge und Dateinamen entsprechen der Quelle.

## _RegisterCallBack (0x0065BA20)

Meldet bei `AgpmTitle` zehn Rückrufe an, in dieser Reihenfolge: Titel hinzugefügt (`0x0065A510`), benutzt (`0x0065A750`), Liste (`0x0065A910`), gelöscht (`0x0065AAB0`), Quest angefordert (`0x0065AC40`), Quest geprüft (`0x0065ADF0`), Quest abgeschlossen (`0x0065B0F0`), Quest-Liste (`0x0065B280`), Titel bei Nahen benutzt (`0x00659BE0`) und Oberfläche öffnen (`0x00658F60`). Bei `AgcmCharacter` kommen „eigener Charakter gesetzt“ (`0x00659080`) und „eigene Position geändert“ (`0x00656970`, schließt das Fenster `UI_TitleAll`) hinzu.
Danach legt es bei [`AgcmUIManager2`](AgcmUIManager2.md) vier Benutzerdaten an (`UserData_Title_CategoryIndex`, `…TitleIndex`, `…TitleIndexCurrent`, `…TitleIndexMini`), vier Anzeigen (`UiDialog_Title_DisplayCategoryName`, `…DisplayTitleName`, `…DisplayTitleNameCurrent`, `…DisplayTitleNameMini`) und 15 Funktionen (`UiDialog_Title_OnOpenUIAll/Current/Mini`, `OnClickCategory`, `OnClickTitle`, `…Current`, `…Mini`, `OnClickPagePrev/Next/Page`, `OnClickSetTargetTitle`, `OnClickActivateTitle`, `OnClickSurrenderTitleCurrent/Mini`, `OnClickCompleteTitle`). Alle Namen stimmen mit der Quelle überein.

## Voraussetzungen (_CheckIsValidRequire…)

`_CheckIsValidTitleRequirement` (`0x00656EB0`) prüft die Voraussetzungen eines Titels mit 14 Einzelprüfungen, die in Quellreihenfolge hintereinander liegen: Stufe (`0x006561F0`), Gildenmeister (`0x00656240`), Archlord (`0x00656290`), Klasse (`0x006562E0`), Kon/Stä/Int/Ges/Wei/Cha (`0x00656430`–`0x00656660`, je 100 Byte), Geld (`0x006566D0`), Cash (`0x00656750`), Gegenstand (`0x006567B0`) und Titel (`0x00656830`). Bei Fehlern zeigt `_ShowErrorMessageBoxOK` (`0x00656890`) die Meldung (Schlüssel `TitleErrorMsg_Require…`). Die Zuordnung der sechs gleichförmigen Attributprüfungen folgt der Quellreihenfolge, ihre Rümpfe sind bis auf die Attributnummer gleich.

## Dialog und Schaltflächen

`_UpdateDialogButtonState` (`0x00656C50`) ruft je nach Titelzustand `…Ready` (`0x00655F30`), `…Running` (`0x00655F80`), `…Complete` (`0x00655FA0`), `…Enable` (`0x00655FF0`) und `…Activate` (`0x00656080`) bzw. `_ReSetDialogButtonState` (`0x00656120`) auf. `OnOpenUI` (`0x00658B80`) holt die Dialogsteuerelemente und ruft `OnUpateUI` (`0x00657FD0`), das Kategorieliste, Titelliste, Beschreibung (`_UpdateTitleInfo` `0x00655D60`, Format `%s</n>(%d/%d)`) und Effekt (`0x00655EC0`) aktualisiert. Die Seitenanzeige (`_UpdateTitleListPage` `0x006575F0`, `%d / %d`) wird von `SetTitlePageIndex` (`0x00657BD0`) gesteuert.
Bestätigungen: `OnSendTitleActivate` (`0x00655900`), `OnSendSurrenderTitle` (`0x00655A20`), `OnSendSetTargetTitle` (`0x00658C60`) und `OnSendCompleteTitle` (`0x0065B640`) zeigen OK-/Abbrechen-Dialoge (`ConfirmDeActivateTitle`, `ConfirmSurrender`, `ConfirmDeleteTitle`); `OnSendSurrenderTitle` und `OnSendSetTargetTitle` rufen dabei `0x00597780` auf; `_CheckIsMaxRunningTitle` (`0x00658470`) begrenzt die laufenden Titel.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnInitialize`, `_RegisterCallBack`, UI-Namen).

## Grenzen

- Die Zuordnung der Auswahlfunktionen, Löschfunktionen und Dialogfunktionen stützt sich auf Aufrufer, Zeichenketten und die Quellreihenfolge, nicht auf einen Vergleich Zeile für Zeile.
- Die zehn `CallBack_RecvTitle…`-Funktionen sind über die Registrierungsreihenfolge in `_RegisterCallBack` zugeordnet; nur `…Add` und `…Use` waren bereits über Zeichenketten bestätigt.
- Die sechs Attributprüfungen (Kon, Stä, Int, Ges, Wei, Cha) haben bis auf eine Konstante identische Rümpfe; ihre Reihenfolge folgt der Quelle.
- `0x006577F0` (ein Karten-Zugriff „n-tes Element“) ist eine gemeinsame Schablonenfunktion für alle Karten der Klasse (Name jetzt `CMap_GetByIndex_template`) und war früher fälschlich als `GetCategoryNameByIndex` benannt; die übrigen Suchfunktionen (`_GetCategoryBy…`, `_GetTitleByIndex`, `_AddRunningTitle` u. a.) sind eingebaut, ebenso `OnClearTitleIDBoard`. `0x006585F0` ist eine zweite, ausgeschriebene Fassung der Titelsuche nach ID. `LoadXMLFileToDocument` wurde nicht gefunden.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 13, nicht im Client: 8, ohne Kandidat: 10, zugeordnet: 4.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `LoadXMLFileToDocument` | 49 | `0x00656A60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnChangeTitleState` | 73 | `0x0065A330` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsOpenUI` | 16 | `0x00656910` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_UpdateCategoryList` | 11 | `0x00655B20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmTitle`](AgpmTitle.md)
