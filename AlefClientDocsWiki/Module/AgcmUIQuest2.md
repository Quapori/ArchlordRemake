# AgcmUIQuest2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIQuest2` (Quest-Annahme, Quest-Tagebuch, Checkpoint-Quests, Meldungen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIQuest2/AgcmUIQuest2.cpp`. Alle Adressen gelten nur für den 2017er Build. Das Paketformat der Quests steht im Bericht [Quest](Quest.md).

## Kernbefund

- **Abdeckung:** 80 von 88 Quellmethoden sind einer Adresse zugeordnet; neu sind u. a. die Registrierungshelfer, alle `Compose…`, `MakeAcceptList…`, `CheckPointQuest`, `StartAnimation`, `SetCharacterEffect`, `Notice…`, die vier `…QuestResult` und `UpdateQuestMainTree`. Die acht übrigen sind eingebaut oder Kartenoperationen.
- **Checkpoint-Quest:** 5000 ms Abklingzeit mit Quest-Ton, dann `SendPacketCheckPoint`; die Animation benutzt die Fertigkeit „연금술“ (Alchemie).
- **UI:** 9 Funktionen, 10 Anzeigen, 11 Benutzerdaten und 15 Ereignisse laut Registrierungstabellen im Binary; die Namen enthalten die Tippfehler der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIQuest2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006B5AD0` | 1034 | vtable/String |
| 1 | `OnInit` | `0x006AFE00` | 270 | vtable/String |
| 2 | `OnDestroy` | `0x006AFF10` | 66 | vtable/String |
| 3 | `OnIdle` | `0x006AFF60` | 83 | vtable/String |
| 4 | `AddEvent` | `0x006AFFC0` | 466 | manual |
| 5 | `AddFunction` | `0x006B56C0` | 369 | manual |
| 6 | `AddUserData` | `0x006B0B80` | 435 | manual |
| 7 | `AddDisplay` | `0x006B4300` | 366 | manual |
| 8 | `RefreshAcceptList` | `0x006B01A0` | 36 | manual |
| 9 | `OpenWorldMap` | `0x006B01D0` | 24 | manual |
| 10 | `RefreshAcceptListAutoStart` | `0x006B3B20` | 239 | Zeichenkette |
| 11 | `RefreshQuestUI` | `0x006B5840` | 75 | manual |
| 12 | `CBClickAutoStartQuest` | `0x006B2700` | 120 | manual |
| 13 | `UpdateQuestMainTree` | `0x006B45E0` | 1208 | manual |
| 14 | `CBDisplayQuestAcceptList` | `0x006B0D40` | 362 | manual |
| 15 | `CBButtonQuestAcceptListClick` | `0x006B0EC0` | 118 | manual |
| 16 | `RefreshAcceptText` | `0x006B0210` | 33 | manual |
| 17 | `RefreshMainText` | `0x006B01F0` | 21 | manual |
| 18 | `RefreshMainTree` | – | | fünf Zeilen, in UpdateQuestMainTree-Aufrufer eingebaut |
| 19 | `RefreshMainCount` | – | | vier Zeilen, eingebaut |
| 20 | `RefreshAcceptLeftButton` | – | | vier Zeilen, eingebaut |
| 21 | `RefreshAcceptLeftButtonEnable` | – | | fünf Zeilen, eingebaut |
| 22 | `CBDisplayQuestAcceptText` | `0x006B3C10` | 212 | manual |
| 23 | `CBDisplayQuestMainText` | `0x006B3CF0` | 107 | manual |
| 24 | `CBDisplayQuestMainCancel` | `0x006B0240` | 88 | manual |
| 25 | `CBDisplayQuestStart` | `0x006B02A0` | 88 | manual |
| 26 | `CBDisplayQuestComplete` | `0x006B0300` | 88 | manual |
| 27 | `CBDisplayQuestAcceptLeftButton` | `0x006B0F50` | 183 | manual |
| 28 | `CBDisplayQuestMainTreeCheck` | `0x006B1010` | 279 | manual |
| 29 | `CBDisplayQuestMainTree` | `0x006B1130` | 547 | manual |
| 30 | `CBButtonAcceptLeftClick` | `0x006B1370` | 657 | Zeichenkette |
| 31 | `ComposeAcceptText` | `0x006B2780` | 138 | manual |
| 32 | `ComposeAcceptTextNew` | `0x006B1610` | 695 | manual |
| 33 | `ComposeAcceptTextIncomplete` | `0x006B0360` | 80 | manual |
| 34 | `ComposeAcceptTextComplete` | `0x006B18D0` | 626 | manual |
| 35 | `ComposeAcceptItem` | `0x006B03B0` | 59 | manual |
| 36 | `ComposeMainText` | `0x006B2860` | 636 | manual |
| 37 | `ComposeMainSummaryText` | `0x006B1B50` | 1025 | manual |
| 38 | `ComposeCheckPointText` | `0x006B03F0` | 173 | manual |
| 39 | `ComposeAcceptSummaryText` | `0x006B04A0` | 91 | manual |
| 40 | `CBReturnCancelQuest` | `0x006B1F90` | 69 | manual |
| 41 | `CBCancelDialogOpen` | `0x006B1FE0` | 105 | manual |
| 42 | `CBMainUIHotKeyOpen` | `0x006B4AD0` | 101 | manual |
| 43 | `CBCheckJournal` | `0x006B4B40` | 331 | manual |
| 44 | `CBClickJournalClose` | `0x006B4C90` | 64 | manual |
| 45 | `CBClickMapOpen` | `0x006B0500` | 28 | manual |
| 46 | `CBClickQuestDel` | `0x006B2050` | 218 | Zeichenkette |
| 47 | `CBButtonQuestMainListClick` | `0x006B0520` | 60 | manual |
| 48 | `MakeAcceptList` | `0x006B2AE0` | 699 | manual |
| 49 | `MakeAcceptListAutoStart` | `0x006B2130` | 661 | manual |
| 50 | `CheckPointQuest` | `0x006B2DA0` | 742 | manual |
| 51 | `StartAnimation` | `0x006B0560` | 393 | manual |
| 52 | `CBQuestGrant` | `0x006B3D60` | 239 | Callback-Registrierung |
| 53 | `CBQuestAddEvent` | `0x006B3E50` | 35 | Callback-Registrierung |
| 54 | `SetCharacterEffect` | `0x006B3090` | 863 | manual |
| 55 | `CBInitBase` | `0x006B33F0` | 45 | Callback-Registrierung |
| 56 | `CBSelfUpdatePosition` | `0x006B06F0` | 134 | Callback-Registrierung |
| 57 | `CBRequireQuestResult` | `0x006B5890` | 113 | Callback-Registrierung |
| 58 | `RequireQuestResult` | `0x006B4CD0` | 569 | manual |
| 59 | `RefreshBaseEffect` | `0x006B3420` | 176 | manual |
| 60 | `CBCompleteQuestResult` | `0x006B5910` | 36 | Callback-Registrierung |
| 61 | `CompleteQuestResult` | `0x006B4F10` | 593 | manual |
| 62 | `AddMessageResult` | `0x006B0780` | 320 | von Hand geprüft |
| 63 | `AddMessageResult` | `0x006B08C0` | 101 | von Hand geprüft |
| 64 | `CBCancelQuestResult` | `0x006B5940` | 123 | Callback-Registrierung |
| 65 | `CancelQuestResult` | `0x006B5170` | 468 | manual |
| 66 | `CBInventoryFull` | `0x006B23D0` | 98 | Callback-Registrierung |
| 67 | `CBQuestInventoryFull` | `0x006B2440` | 238 | Callback-Registrierung |
| 68 | `CBUpdateQuest` | `0x006B3E80` | 454 | Callback-Registrierung |
| 69 | `CBRefreshAll` | `0x006B5350` | 204 | Callback-Registrierung |
| 70 | `NoticeQuestItem` | `0x006B34D0` | 439 | manual |
| 71 | `Notice` | `0x006B0930` | 133 | manual |
| 72 | `CBDispalyQuestCount` | `0x006B2530` | 126 | manual |
| 73 | `CBAfterCooldown` | `0x006B09C0` | 80 | Callback-Registrierung |
| 74 | `CBAddItemInventory` | `0x006B5AA0` | 44 | Callback-Registrierung |
| 75 | `CBQuestItemNotice` | `0x006B59C0` | 119 | Callback-Registrierung |
| 76 | `GetQuestTIDByItem` | `0x006B25B0` | 229 | manual |
| 77 | `NoticeNormalItem` | `0x006B5420` | 336 | manual |
| 78 | `AddQuestPositionInfo` | – | | nur `std::map`-Zugriff, als Vorlagenfunktion nicht als eigene Methode erkennbar |
| 79 | `DelQuestPositionInfo` | – | | nur `std::map`-Zugriff, nicht als eigene Methode erkennbar |
| 80 | `GetQuestPosName` | – | | vier Zeilen, `std::map`-Zugriff, eingebaut |
| 81 | `ClearQuestPositionInfo` | `0x006B4470` | 176 | manual |
| 82 | `_RefreshTextList` | `0x006B3690` | 219 | manual |
| 83 | `_CheckQuest` | `0x006B26A0` | 96 | manual |
| 84 | `_GetTopQuestTID` | – | | rekursive Hilfsmethode ohne Aufrufer im Modul, nicht gefunden |
| 85 | `SetScrollButton` | `0x006B0A10` | 127 | manual |
| 86 | `CBRemoveItemInventory` | `0x006B0A90` | 62 | Callback-Registrierung |
| 87 | `OpenMainQuest` | `0x006B0AD0` | 25 | manual |

80 von 88 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AddMessageResult_006b08c0` (`0x006B08C0`), `ctor_or_dtor_006b6440` (`0x006B6440`), `ctor_or_dtor_006b65f0` (`0x006B65F0`), `~AgcmUIQuest2` (`0x006B6870`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xC04 / 0xC08` | `Zeiger auf [`AgcmUICooldown`](AgcmUICooldown.md) / [`AgcmUIMain`](AgcmUIMain.md)` | `OnAddModule` |
| `0x31F8` | `Abklingzeit-ID (`m_lCooldownID`)` | `OnAddModule`, `CheckPointQuest` |

## Vtable

Vtable bei `0x008D15DC`: Slot 0 Destruktor `0x006B6870`, 1 `OnAddModule` (`0x006B5AD0`), 2 `OnInit` (`0x006AFE00`), 3 `OnIdle` (`0x006AFF60`), 4/5 gemeinsamer Rumpf `0x0067FAB0`, 6 `return TRUE`-Rumpf `0x0067AC90`, 7 `OnDestroy` (`0x006AFF10`).

## Registrierung (OnAddModule, 0x006B5AD0)

Holt 21 Module (u. a. `AgpmQuest`, [`AgcmQuest`](AgcmQuest.md), [`AgcmEventQuest`](AgcmEventQuest.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmObject`](AgcmObject.md), `AgcmUICooldown`, [`AgpmSkill`](AgpmSkill.md), [`AgcmSkill`](AgcmSkill.md), `AgcmUIMain`); mehrere sind Pflicht, `AgcmUICooldown` und `AgcmObject` optional. Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgcmUICooldown`: Abklingzeit beendet | `CBAfterCooldown` | `0x006B09C0` |
| `AgcmEventQuest`: Ereignis gewährt | `CBQuestGrant` | `0x006B3D60` |
| [`ApmEventManager`](ApmEventManager.md): Ereignis hinzugefügt | `CBQuestAddEvent` | `0x006B3E50` |
| `AgcmObject`: Objekt initialisiert (falls vorhanden) | `CBInitBase` | `0x006B33F0` |
| `AgcmCharacter`: Charakter initialisiert | `CBInitBase` | `0x006B33F0` |
| `AgcmCharacter`: eigene Position | `CBSelfUpdatePosition` | `0x006B06F0` |
| [`AgpmCharacter`](AgpmCharacter.md): Stufe geändert | `CBRefreshAll` | `0x006B5350` |
| `AgcmCharacter`: eigener Charakter gesetzt | `CBRefreshAll` | `0x006B5350` |
| `AgpmQuest`: Quest verlangt (Ergebnis) | `CBRequireQuestResult` | `0x006B5890` |
| `AgpmQuest`: Quest abgeschlossen (Ergebnis) | `CBCompleteQuestResult` | `0x006B5910` |
| `AgpmQuest`: Quest abgebrochen (Ergebnis) | `CBCancelQuestResult` | `0x006B5940` |
| `AgpmQuest`: Inventar voll | `CBInventoryFull` | `0x006B23D0` |
| `AgpmQuest`: Quest-Inventar voll | `CBQuestInventoryFull` | `0x006B2440` |
| `AgpmQuest`: Quest aktualisiert | `CBUpdateQuest` | `0x006B3E80` |
| `AgpmItem`: Gegenstand ins Inventar | `CBAddItemInventory` | `0x006B5AA0` |
| `AgpmItem`: Gegenstand aus Inventar entfernt | `CBRemoveItemInventory` | `0x006B0A90` |
| `AgpmItem`: Stapelzahl geändert | `CBQuestItemNotice` | `0x006B59C0` |

Dann `AddEvent` (`0x006AFFC0`), `AddFunction` (`0x006B56C0`), `AddUserData` (`0x006B0B80`) und `AddDisplay` (`0x006B4300`); zuletzt legt das Modul ein Gitterfeld für das Auto-Start-Symbol an.

## UI-Funktionen und Anzeigen

**Funktionen (9):** `QuestAcceptList_Click2` → `CBButtonQuestAcceptListClick` (`0x006B0EC0`), `QuestCancel_Button2` → `CBCancelDialogOpen` (`0x006B1FE0`), `QuestAcceptLeftButton_CLick2` → `CBButtonAcceptLeftClick`, `QuestMainLit_Cick2` → `CBButtonQuestMainListClick` (`0x006B0520`), `QuestMainHoeKey_Open2` → `CBMainUIHotKeyOpen` (`0x006B4AD0`), `QuestMain_CheckJournal` → `CBCheckJournal`, `QuestMain_Journal_Close` → `CBClickJournalClose`, `QuestMain_Del` → `CBClickQuestDel`, `QuestMain_MapOpen` → `CBClickMapOpen` (`0x006B0500`). Die Namen mit Tippfehlern („Lit“, „Cick“, „Hoe“) stehen so im Binary.
**Anzeigen (10):** Annahmeliste (Zeichenketten-Typ, `0x40`), Annahmetext, linker Annahme-Knopf, Haupttext, Abbrechen, Baum, Baum-Haken, Start, Abschluss und Anzahl (`CBDispalyQuestCount`, Schreibweise der Quelle). Dazu das Ereignis `QuestCancelDlg_Open` mit dem Rückruf `CBReturnCancelQuest` (`0x006B1F90`) für den Abbrechen-Dialog.

## Annahme-Fenster und Quest-Tagebuch

`CBQuestGrant` (`0x006B3D60`) baut bei einer Ereignis-Gewährung die Annahmeliste auf (`MakeAcceptList` `0x006B2AE0`, `MakeAcceptListAutoStart` `0x006B2130`), zeigt Symbol und Text und wirft das Öffnen-Ereignis. `RefreshAcceptListAutoStart` (`0x006B3B20`) fügt das Auto-Start-Symbol als Systemmeldungs-Symbol („Self Quest“) hinzu oder entfernt es; ein Klick darauf (`CBClickAutoStartQuest`, `0x006B2700`) öffnet die Annahmeliste der selbststartenden Quests. Das Tagebuch aktualisiert `RefreshQuestUI` (`0x006B5840`: Baum, Haupttext, `AgcmUIQuestJournal::RefreshJournalInfo` und `…Position`); der Quest-Baum wird in `UpdateQuestMainTree` (`0x006B45E0`, 1208 Byte) gefüllt.

## Texte (Compose…)

Die Texte werden als Zeichenketten mit Auszeichnungen zusammengesetzt: `</n>` ist der Zeilenumbruch, `<Hxxxxxxxx>` eine Farbe (Quest-Titel `FFB6FF38` grün, Bedingung/Standard/erfüllt/offen über die Farbkonstanten der Quelle) und `<ITEM::Anzahl::TID::Sockel::Aufwertung::Bindung::…>` ein Gegenstandssymbol. `ComposeAcceptText` (`0x006B2780`) setzt Titel und Gebiet und verzweigt je nach Annahme-Status auf `ComposeAcceptTextNew` (`0x006B1610`: Inhalt, Annahmetext, Abschlussbedingung, Belohnung mit Geld, Erfahrung, vier Gegenständen, wählbaren Gegenständen und Produktions-Fertigkeit), `…Incomplete` (`0x006B0360`: Inhalt und Text „unvollständig“) oder `…Complete` (`0x006B18D0`). `ComposeMainText` (`0x006B2860`) baut den Text für das Tagebuch, `ComposeMainSummaryText` (`0x006B1B50`, 1025 Byte) die Bedingungszeilen nach Faktor (Stufe, Geld, Gegenstandszahl, Monster 1/2, normaler Gegenstand, fünf Checkpoints, ohne Faktor) jeweils grün (erfüllt) oder rot (offen) mit „(aktuell/Ziel)“; `ComposeCheckPointText` (`0x006B03F0`) liefert die Checkpoint-Zeilen und `ComposeAcceptSummaryText` (`0x006B04A0`) die einfache Liste „`%s`</n>“.

## Checkpoint-Quests (CheckPointQuest, StartAnimation)

`CheckPointQuest` (`0x006B2DA0`) lehnt ab, solange gehalten wird (`m_bHold`), und mit einer Meldung (`STI_CANT_WITH_HORSE`), wenn der Charakter reitet. Es geht die Checkpoints der Quest-Gruppe durch, sucht den, dessen Quest der Charakter hat, prüft, ob der benötigte Gegenstand in Inventar, Bank, Cash-, Unter- oder Lade-Inventar vorhanden ist (sonst Meldung `STI_NO_MORE_ITEM`), und startet eine **Abklingzeit von 5000 ms** (mit Text `STI_QUEST` und Quest-Ton). Gelingt das, merkt es Quest und Index, stoppt den Charakter, ruft `StartAnimation` und setzt das Halte-Flag. Nach der Abklingzeit sendet `CBAfterCooldown` (`0x006B09C0`) `AgcmQuest::SendPacketCheckPoint`.
`StartAnimation` (`0x006B0560`) benutzt dafür die Fertigkeit „연금술“ (Alchemie; Zeichenkette bei `0x008D10C0`): Es setzt sie als aktuelle Fertigkeit, dreht den Charakter zum Ereignis und spielt die Animation (Skill-Animation je nach Zustand oder Standard); die Dauer sperrt Aktionen (`SetActionBlockTime`, Typ Fertigkeit).

## Ergebnisse und Meldungen

`RequireQuestResult` (`0x006B4CD0`), `CompleteQuestResult` (`0x006B4F10`) und `CancelQuestResult` (`0x006B5170`) bauen Annahmeliste, Basis-Effekt (`RefreshBaseEffect` `0x006B3420` → `SetCharacterEffect` `0x006B3090`, die Symbole über dem Kopf) und Tagebuch neu und geben mit `AddMessageResult` (`0x006B0780`, `0x006B08C0`; zwei Überladungen) eine Chat-/Systemmeldung aus. `Notice` (`0x006B0930`) ruft [`AgcmUINotice`](AgcmUINotice.md):AddMessage` und [`AgcChatManager`](AgcChatManager.md):OnAddQuestMessage`. `NoticeQuestItem` (`0x006B34D0`) und `NoticeNormalItem` (`0x006B5420`) melden „Name (Anzahl/Ziel)“ beim Einsammeln eines Quest- bzw. normalen Gegenstands; `GetQuestTIDByItem` (`0x006B25B0`) sucht die Quest dazu.

## Positionsliste

`ClearQuestPositionInfo` (`0x006B4470`) entfernt die Karten-Markierungen ([`AgcmMinimap`](AgcmMinimap.md):DestroyMapPosition`) einer Quest; `AddQuestPositionInfo`, `DelQuestPositionInfo` und `GetQuestPosName` arbeiten nur auf einer `std::map`; im Binary liegen dort Vorlagenfunktionen der Standardbibliothek (z. B. `0x006B3880`–`0x006B4520`, `0x006B5EE0`–`0x006B61C0`), aber keine eigenen Methoden.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006B56C0`, `0x006B4300`, `0x006B0B80`, `0x006AFFC0`, `0x006B5AD0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (9)

| Name | Id | Handler |
|---|---:|---|
| `QuestAcceptList_Click2` |  | `FUN_006b0ec0` |
| `QuestCancel_Button2` |  | `FUN_006b1fe0` |
| `QuestAcceptLeftButton_CLick2` |  | `FUN_006b1370` |
| `QuestMainLit_Cick2` |  | `FUN_006b0520` |
| `QuestMainHoeKey_Open2` |  | `FUN_006b4ad0` |
| `QuestMain_CheckJournal` |  | `FUN_006b4b40` |
| `QuestMain_Journal_Close` |  | `FUN_006b4c90` |
| `QuestMain_Del` |  | `FUN_006b2050` |
| `QuestMain_MapOpen` |  | `FUN_006b0500` |

**Anzeige** (10)

| Name | Id | Handler |
|---|---:|---|
| `QuestAccept_Display2` | 0 | `FUN_006b0d40` |
| `QuestAcceptText_Display2` | 0 | `FUN_006b3c10` |
| `QusetAcceptLeftButton_Display2` | 0 | `FUN_006b0f50` |
| `QuestMainText_Display2` | 0 | `FUN_006b3cf0` |
| `QuestMainCancel_Display2` | 0 | `FUN_006b0240` |
| `QuestMainTree_Display2` | 0 | `FUN_006b1130` |
| `QuestMainTreeCheck_Display2` | 0 | `FUN_006b1010` |
| `QuestStart_Display2` | 0 | `FUN_006b02a0` |
| `QuestComplete_Display2` | 0 | `FUN_006b0300` |
| `QuestCount_Display2` | 0 | `FUN_006b2530` |

**Ereignis** (15)

| Name | Id | Handler |
|---|---:|---|
| `QuestCancelDlg_Open` |  | `FUN_006b1f90` |
| `QuestAccept_Open2` | 0 | – |
| `QuestMain_Open2` | 0 | – |
| `QuestAccept_Close2` | 0 | – |
| `QuestDontHave_Message` | 0 | – |
| `QuestStart_Message` | 0 | – |
| `QuestInventoryMainFull_Message` | 0 | – |
| `QuestInventoryQuestFull_Message` | 0 | – |
| `QuestComplete_Message` | 0 | – |
| `QuestFull_Message` | 0 | – |
| `QuestStart_Sound` | 0 | – |
| `QuestFail_Sound` | 0 | – |
| `QuestCount` | 0 | – |
| `Quest_AutoStart` | 0 | – |
| `Quest_AutoEnd` | 0 | – |

**UserData** (11)

| Name | Id | Handler |
|---|---:|---|
| `QuestAcceptList_UserData2` |  | – |
| `QuestAcceptText_UserData2` | 0 | – |
| `QuestAcceptLeftButton_UserData2` | 0 | – |
| `QuestAcceptLeftButtonEnable_UserData2` |  | – |
| `QuestMainText_UserData2` | 0 | – |
| `QuestMainCancel_UserData2` | 0 | – |
| `QuestMainTree_UserData2` |  | – |
| `QuestMainTreeDepth_UserData2` |  | – |
| `QuestStart_UserData2` | 0 | – |
| `QuestComplete_UserData2` | 0 | – |
| `QuestCount_UserData2` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierungsreihenfolge, `CheckPointQuest` mit 5000 ms, `StartAnimation`, Zeichenketten der `Compose…`-Funktionen, `Notice`).

## Grenzen

- `UpdateQuestMainTree` (1208 Byte), `ComposeMainSummaryText` (1025 Byte), `SetCharacterEffect` (863 Byte), `MakeAcceptList` und die vier `…QuestResult` wurden über Größe, Zeichenketten, Aufrufer und Aufgerufene zugeordnet, nicht Zeile für Zeile verglichen.
- Die Unterscheidung von `ComposeAcceptTextNew` und `…Complete` stützt sich auf die Zahl der Abschnittsüberschriften in den Zeichenketten (vier gegen drei).
- Die Zuordnung `ClearQuestPositionInfo` ergibt sich aus Aufrufern (Abschluss und Abbruch einer Quest) und dem Aufruf von `DestroyMapPosition`; `AddMessageResult` (zwei Überladungen) über Größe und Zeichenketten.
- Mehrere Funktionen im Bereich (z. B. `0x006B3770`, `0x006B4090`, `0x006B6060`) sind Bibliotheksfunktionen von `std::map`/`vector` und gehören zu keiner Quellmethode.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 5, nicht im Client: 2, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcChatManager`](AgcChatManager.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventQuest`](AgcmEventQuest.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmObject`](AgcmObject.md), [`AgcmQuest`](AgcmQuest.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUINotice`](AgcmUINotice.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgpmSkill`](AgpmSkill.md), [`ApmEventManager`](ApmEventManager.md)
- **Erwähnt in:** [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmQuest`](AgcmQuest.md), [`Quest`](Quest.md)
