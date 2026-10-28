# AgcmUIMain (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIMain` (Hauptoberfläche: Quickbelt, Trank-Slots, Alarmleiste, Systemmeldungs-Grid) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIMain`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 108 von 134 Quellmethoden sind Binary-Adressen zugeordnet, 36 davon in diesem Durchgang neu über den Aufrufgraphen (und gegen das Dekompilat gelesen). Die übrigen sind überwiegend kleine Hüllen, die der Compiler eingefaltet hat (siehe unten).
- **Build-Variante:** Das Binary entspricht der Quelle mit `_AREA_GLOBAL_` und ohne `_AREA_KOREA_`: `OnIdle` ruft `UpdateMediaRateWindow` nicht auf, Systemmeldungs-Einträge tragen eine Ablaufzeit (`nExpireTime`, Knotengröße 0x18).
- **UI-Schnittstelle unverändert:** 46 Funktionen, 9 Userdaten, 7 Anzeigen und 4 Boolean-Registrierungen wie in der Quelle; bei den Ereignissen fehlt im Binary nur `Test_Event` (16 statt 17).
- **Callbacks unverändert:** Alle 13 `AGCMUI_MAIN_CB_*`-IDs stimmen mit der Quelle überein; `RBUTTON_SKILL_CAST` (4) wird weder im Binary noch (auskommentiert) in der Quelle ausgelöst.
- **Verhalten:** `ProcessSkill`, `UseGridItem`, `UseRideItemInQuickBelt`, `RefreshItemCount`, `OnInitQuickBeltGrid`, `UpdateAlarmGrid`, `AddItemToAlarmGrid`, die System-Grid-Funktionen und `OnIdle` folgen der Quelle.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIMain.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006071D0` | 4256 | vtable/String |
| 1 | `OnDestroy` | `0x006014E0` | 546 | vtable/String |
| 2 | `OnInit` | `0x00605460` | 46 | vtable/String |
| 3 | `OnInitQuickBeltGrid` | `0x00603E30` | 183 | Aufrufgraph (geprüft) |
| 4 | `OnIdle` | `0x00605490` | 957 | vtable/String |
| 5 | `AddShortcut` | `0x00603EF0` | 944 | Aufrufgraph (geprüft) |
| 6 | `RemoveGridLayer` | `0x00601710` | 172 | von Hand geprüft |
| 7 | `RemoveShortcut` | `0x006042A0` | 490 | Aufrufgraph (geprüft) |
| 8 | `AddHPPotion` | `0x006017D0` | 851 | Aufrufgraph (geprüft) |
| 9 | `RemoveHPPotion` | `0x00601B30` | 157 | von Hand geprüft |
| 10 | `AddMPPotion` | `0x00601BD0` | 835 | Aufrufgraph (geprüft) |
| 11 | `RemoveMPPotion` | `0x00601F20` | 157 | von Hand geprüft |
| 12 | `LoadSystemMessageGridToolTip` | – | | inline/eingefaltet (ruft `m_SystemGridTooltip.Initialize`) |
| 13 | `AddSystemMessageGridItem` | – | | Hülle um `OnAddSystemGridControl`, eingefaltet/inline |
| 14 | `AddSystemMessageGridItem` | – | | Hülle um `OnAddSystemGridControl`, eingefaltet/inline |
| 15 | `RemoveSystemMessageGridItem` | – | | Hülle um `OnDeleteSystemGridControl`, inline |
| 16 | `ClearSystemMessageGridItem` | – | | inline (`m_ListSystemGridControl.clear()`) |
| 17 | `GetGridItemExpireTime` | `0x00605850` | 67 | Aufrufgraph (geprüft) |
| 18 | `SetArrow` | `0x00606E90` | 307 | Zeichenkette |
| 19 | `ResetArrow` | – | | inline in `CBUnEquipItem` |
| 20 | `SetBolt` | `0x00606FD0` | 307 | Aufrufgraph (geprüft) |
| 21 | `ResetBolt` | – | | inline in `CBUnEquipItem` |
| 22 | `SetOnlineTimeAddictStatus` | `0x00601FE0` | 639 | von Hand geprüft |
| 23 | `CBAddShortcut` | `0x00604490` | 353 | UI-Registrierung |
| 24 | `CBRemoveShortcut` | `0x00604600` | 377 | UI-Registrierung |
| 25 | `CBAddHPPotion` | `0x00602260` | 136 | UI-Registrierung |
| 26 | `CBAddMPPotion` | `0x006022F0` | 136 | UI-Registrierung |
| 27 | `CBRemovePotion` | `0x00602380` | 225 | UI-Registrierung |
| 28 | `CBDisplayExp` | `0x00602470` | 483 | Callback-Registrierung |
| 29 | `CBGetOnlineTimeEditControl` | `0x00602670` | 64 | UI-Registrierung |
| 30 | `CBGetAddictStatusEditControl` | `0x006026B0` | 64 | UI-Registrierung |
| 31 | `CBDisplayDefault` | `0x006026F0` | 249 | Callback-Registrierung |
| 32 | `CBDisplayInt32` | `0x006027F0` | 62 | UI-Registrierung |
| 33 | `CBDisplayCurrentLayer` | `0x00602830` | 44 | UI-Registrierung |
| 34 | `CBButtonControlDisable` | `0x00602860` | 39 | UI-Registrierung |
| 35 | `CBButtonControlEnable` | `0x00602890` | 39 | UI-Registrierung |
| 36 | `CBEditControlInit` | `0x006028C0` | 37 | UI-Registrierung |
| 37 | `CBSelectListItem` | – | | nicht gefunden |
| 38 | `CBEditControlActive` | `0x006028F0` | 37 | UI-Registrierung |
| 39 | `CBLClickDown` | `0x00604780` | 209 | UI-Registrierung |
| 40 | `CBRClickDown` | `0x00602920` | 33 | UI-Registrierung |
| 41 | `CBRClickUp` | `0x00604860` | 345 | UI-Registrierung |
| 42 | `CBPotionGridRClickUp` | `0x00602950` | 293 | UI-Registrierung |
| 43 | `CBClickSystemGridNoAction` | – | | Rumpf identisch mit `Element::GetSTRING` (ICF): im Binary ist die Registrierung auf diese Funktion gefaltet |
| 44 | `CBClickSystemGrid` | `0x006065D0` | 49 | UI-Registrierung |
| 45 | `CBQuickBeltUse_1` | `0x006058A0` | 229 | Callback-Registrierung |
| 46 | `CBQuickBeltUse_2` | `0x00605990` | 229 | Callback-Registrierung |
| 47 | `CBQuickBeltUse_3` | `0x00605A80` | 229 | Callback-Registrierung |
| 48 | `CBQuickBeltUse_4` | `0x00605B70` | 229 | Callback-Registrierung |
| 49 | `CBQuickBeltUse_5` | `0x00605C60` | 229 | Callback-Registrierung |
| 50 | `UseBelt` | – | | Rumpf ist in der Quelle auskommentiert (`return TRUE`), nicht eindeutig |
| 51 | `CBQuickBeltUse_6` | `0x00605D50` | 233 | Callback-Registrierung |
| 52 | `CBQuickBeltUse_7` | `0x00605E40` | 233 | Callback-Registrierung |
| 53 | `CBQuickBeltUse_8` | `0x00605F30` | 233 | Callback-Registrierung |
| 54 | `CBQuickBeltUse_9` | `0x00606020` | 233 | Callback-Registrierung |
| 55 | `CBQuickBeltUse_10` | `0x00606110` | 233 | Callback-Registrierung |
| 56 | `CBQuickBeltUseHPPotion` | `0x00602A80` | 165 | Callback-Registrierung |
| 57 | `CBQuickBeltUseMPPotion` | `0x00602B30` | 165 | Callback-Registrierung |
| 58 | `CBQuickBeltLayerUp` | `0x006049C0` | 695 | Callback-Registrierung |
| 59 | `CBQuickBeltLayerDown` | `0x00604C80` | 637 | Callback-Registrierung |
| 60 | `CBCloseUIWindow` | `0x00602BE0` | 170 | UI-Registrierung |
| 61 | `RemoveGridItemFromQuickBelt` | `0x00602C90` | 90 | von Hand geprüft |
| 62 | `CheckQuickBeltItem` | `0x00602CF0` | 155 | von Hand geprüft |
| 63 | `SetCallbackOpenTooltip` | – | | identische Setter, vom Linker mit anderen Modulen zusammengefaltet (ICF) |
| 64 | `SetCallbackCloseTooltip` | – | | nicht gefunden |
| 65 | `SetCallbackCloseAllUITooltip` | – | | nicht gefunden |
| 66 | `SetCallbackUpdateAlarmGrid` | – | | nicht gefunden |
| 67 | `SetCallbackRButtonSkillCast` | – | | nicht gefunden |
| 68 | `SetCallbackKeydownCloseAllUIExceptMain` | – | | nicht gefunden |
| 69 | `SetCallbackKeydownESC` | – | | nicht gefunden |
| 70 | `SetCallbackAddShortcut` | – | | nicht gefunden |
| 71 | `SetCallbackRemoveShortcut` | – | | nicht gefunden |
| 72 | `SetCallbackUpdateHPPotion` | – | | nicht gefunden |
| 73 | `SetCallbackUpdateMPPotion` | – | | nicht gefunden |
| 74 | `SetCallbackUpdateHPPointGage` | – | | nicht gefunden |
| 75 | `SetCallbackUpdateMPPointGage` | – | | nicht gefunden |
| 76 | `CBOpenToolTip` | `0x00602DD0` | 39 | UI-Registrierung |
| 77 | `CBCloseToolTip` | `0x00602E00` | 39 | UI-Registrierung |
| 78 | `CBOpenSystemGridToolTip` | `0x00606610` | 40 | UI-Registrierung |
| 79 | `CBCloseSystemGridToolTip` | `0x00604F00` | 40 | UI-Registrierung |
| 80 | `CBCloseAllUIToolTip` | `0x00602E30` | 23 | UI-Registrierung |
| 81 | `RefreshQuickBeltGrid` | `0x00602E50` | 77 | Aufrufgraph (geprüft) |
| 82 | `UpdateAlarmGrid` | `0x00604F30` | 87 | von Hand geprüft |
| 83 | `AddItemToAlarmGrid` | `0x00602EA0` | 165 | von Hand geprüft |
| 84 | `ClearAlarmGrid` | – | | nicht gefunden |
| 85 | `UpdateMediaRateWindow` | – | | nur unter `_AREA_KOREA_`, im Binary nicht vorhanden |
| 86 | `CBUIReturnAppQuit` | `0x00602F50` | 59 | UI-Registrierung |
| 87 | `CBApplicationQuitEventCall` | `0x00602F90` | 102 | UI-Registrierung |
| 88 | `CBQuickBeltAdjustPos` | `0x00603000` | 128 | UI-Registrierung |
| 89 | `CBQuickBeltVAdjustPos` | `0x00603080` | 140 | UI-Registrierung |
| 90 | `CBDefaultBoolean` | `0x00603110` | 20 | Callback-Registrierung |
| 91 | `CBSelfCharacterDead` | `0x00603130` | 42 | UI-Registrierung |
| 92 | `CBIsSelected` | `0x00603160` | 43 | UI-Registrierung |
| 93 | `CBSetFocusMovableItem` | `0x00603190` | 318 | UI-Registrierung |
| 94 | `CBKillFocusMovableItem` | `0x006032D0` | 78 | UI-Registrierung |
| 95 | `SetHPPointScrollBarValue` | `0x00603320` | 71 | von Hand geprüft |
| 96 | `SetMPPointScrollBarValue` | `0x00603370` | 71 | von Hand geprüft |
| 97 | `CBChangeHPPointScollBarValue` | `0x006033C0` | 73 | UI-Registrierung |
| 98 | `CBChangeMPPointScollBarValue` | `0x00603410` | 73 | UI-Registrierung |
| 99 | `CBGetPotionScollBarControl` | `0x00604F90` | 63 | UI-Registrierung |
| 100 | `CBMainUIAllClose` | `0x00603460` | 34 | UI-Registrierung |
| 101 | `ProcessSkill` | `0x00603490` | 288 | Aufrufgraph (geprüft) |
| 102 | `RefreshItemCount` | `0x00606200` | 105 | von Hand geprüft |
| 103 | `RefreshItemCount` | `0x00604FD0` | 165 | von Hand geprüft |
| 104 | `GetItemTotalCount` | `0x006035B0` | 77 | von Hand geprüft |
| 105 | `CBAddItemToInventory` | `0x00606270` | 37 | Callback-Registrierung |
| 106 | `CBRemoveItemFromInventory` | `0x006062A0` | 31 | Callback-Registrierung |
| 107 | `CBUpdateStackCount` | `0x006062C0` | 50 | Callback-Registrierung |
| 108 | `CBGetRegisteredMPPotionTID` | `0x00603600` | 40 | Callback-Registrierung |
| 109 | `CBEquipItem` | `0x00607110` | 84 | Callback-Registrierung |
| 110 | `CBUnEquipItem` | `0x00606740` | 100 | Callback-Registrierung |
| 111 | `CBSetSelfCharacter` | `0x00607170` | 92 | Callback-Registrierung |
| 112 | `CBReleaseSelfCharacter` | `0x00603630` | 173 | Callback-Registrierung |
| 113 | `UseGridItem` | `0x00605080` | 159 | Aufrufgraph (geprüft) |
| 114 | `RefreshQBeltGridItemStackCount` | `0x006036E0` | 621 | von Hand geprüft |
| 115 | `CBChangeCharacterBindingRegion` | `0x00605120` | 710 | Callback-Registrierung |
| 116 | `CBIDPasswordOK` | `0x00603960` | 83 | Callback-Registrierung |
| 117 | `CBBooleanIsKorea` | `0x006039C0` | 12 | UI-Registrierung |
| 118 | `CBUpdateOnlineTime` | `0x006039D0` | 393 | Callback-Registrierung |
| 119 | `IsCurrentUI` | `0x00603B60` | 59 | Aufrufgraph (geprüft) |
| 120 | `OnAddSystemGridControl` | `0x00606D80` | 209 | von Hand geprüft |
| 121 | `OnAddSystemGridControl` | – | | nicht gefunden |
| 122 | `OnDeleteSystemGridControl` | `0x00606640` | 114 | von Hand geprüft |
| 123 | `OnClickSystemGridControl` | `0x00606300` | 98 | Aufrufgraph (geprüft) |
| 124 | `OnClearSystemGrid` | `0x006066C0` | 109 | von Hand geprüft |
| 125 | `OnRefreshSystemGrid` | `0x00606370` | 232 | von Hand geprüft |
| 126 | `_OpenSystemGridTooltip` | `0x00606460` | 245 | Aufrufgraph (geprüft) |
| 127 | `_CloseSystemGridTooltip` | `0x00603BA0` | 54 | Aufrufgraph (geprüft) |
| 128 | `UseRideItemInQuickBelt` | `0x00603BE0` | 163 | Aufrufgraph (geprüft) |
| 129 | `OnAdjustHPMPBarPosition` | `0x00603C90` | 152 | Zeichenkette |
| 130 | `GetKeyCode` | `0x00603D30` | 75 | Aufrufgraph (geprüft) |
| 131 | `GetCenterXPosOfUI` | `0x00603D80` | 115 | von Hand geprüft |
| 132 | `GetYPosOfBelt` | `0x00603E00` | 44 | von Hand geprüft |
| 133 | `CBChangedUseNewSlot` | `0x006053F0` | 99 | Callback-Registrierung |

108 von 134 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `RefreshItemCount_00604fd0` (`0x00604FD0`), `RefreshItemCount_00606200` (`0x00606200`), `ctor_or_dtor_006067b0` (`0x006067B0`), `ctor_or_dtor_00606cd0` (`0x00606CD0`), `~AgcmUIMain` (`0x00606E60`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98` | `m_pcsAgcmUIManager2` | `OnAddModule`: `GetModule("AgcmUIManager2")`; `IsCurrentUI` prüft den Zeiger |
| `0xB9C / 0xBA0 / 0xBA4` | `m_pcsAgpmGrid / m_pcsAgpmFactors / m_pcsAgpmCharacter` | Reihenfolge der `GetModule`-Aufrufe in `OnAddModule` |
| `0xBA8` | `m_pcsAgpmItem` | `CheckQuickBeltItem`: Prüfung auf 0 am Anfang |
| `0xBB0` | `m_pcsAgcmCharacter` | `+0x1596C` ist dessen Self-Character-Zeiger (`ProcessSkill`, `RefreshItemCount`) |
| `0xBB4` | `m_pcsAgcmSkill` | `ProcessSkill`: Prüfung am Anfang |
| `0xBC4 / 0xBC8` | `AgcmLogin / m_pcsAgcmUIOption (Vermutung für 0xBC4)` | `SetOnlineTimeAddictStatus` liest `+0xBC4`; `RefreshQBeltGridItemStackCount` und `OnIdle` lesen `[+0xBC8]+0xE30` (= `m_bUseNewSlot`) |
| `0xBCC` | `m_apstQuickBelt[8]` | `RemoveGridItemFromQuickBelt`/`OnInitQuickBeltGrid`: Zeigerfeld mit 8 Einträgen, Stride 4 |
| `0xBF4` | `m_pstSystemMessageGrid` | `OnRefreshSystemGrid`/`OnClearSystemGrid`: `SetUserDataRefresh` |
| `0xBF8 / 0xBFC` | `m_apstQBLayer[2]` | `OnInitQuickBeltGrid`: beide am Ende aktualisiert |
| `0x2960` | `m_csAlarmGrid (AgpdGrid)` | `UpdateAlarmGrid`; Zeilen bei `+0x16`, Spalten bei `+0x18` (`RemoveGridLayer`, `AddItemToAlarmGrid`) |
| `0x2984` | `m_pstAlarmGrid` | `UpdateAlarmGrid`/`AddItemToAlarmGrid`: `SetUserDataRefresh` |
| `0x2990 / 0x2994 / 0x299C / 0x29A0` | `Suchtstatus-Zustand (Online-Zeit)` | `SetOnlineTimeAddictStatus`: Controls, Taktzähler und Startzeit |
| `0x29DC` | `m_ulPrevProcessClockCount` | `OnIdle`: 500-ms-Takt für `UpdateAlarmGrid` |
| `0x29F0` | `m_pcsHPPointScrollBarControl` | `SetHPPointScrollBarValue`: `[+0xF4]` ist `m_pcsBase` |
| `0x2A08 / 0x2A0C` | `m_lHPPointScrollBarValue / m_lMPPointScrollBarValue` | `OnIdle`: Schwellwerte für automatische Tränke |
| `0x2A10` | `m_astQuickBeltGrid[8] (AgpdGrid, Stride 0x24)` | `RemoveGridItemFromQuickBelt` |
| `0x2B30` | `m_nNumOfActiveQuickbelt` | `RefreshQuickBeltGrid`, `OnInitQuickBeltGrid`; `AddUserData("QB_Layer(L)")` zeigt darauf |
| `0x2B34 / 0x2B38 / 0x2B3C` | `m_bQuickBeltSwitchButton[2] / m_nSavedCurrentQuickBeltLayer` | `OnIdle`: Umschalttaste und gemerkte Ebene |
| `0x2B40 / 0x2B64 / 0x2B88` | `m_stHPPotionGrid / m_stMPPotionGrid / m_stSystemMessageGrid` | `OnAddModule`: `AddUserData`-Zeiger und [`AgpmGrid`](AgpmGrid.md):Init` |
| `0x2BAC / 0x2BB0 / 0x2BB4 / 0x2BB8` | `m_lTotalHPPotionCount / MP / Arrow / Bolt` | `RefreshItemCount`, `SetBolt` |
| `0x2BBC / 0x2BC0 / 0x2BC4 / 0x2BC8` | `m_pcsHPPotionItem / MPPotionItem / ArrowItem / BoltItem` | `RefreshItemCount`, `OnIdle`, `SetBolt` |
| `0x4A40` | `m_ListSystemGridControl (STL-Liste)` | Listenkopf; Knoten (0x18 Byte): `+8` Grid-Item, `+0xC` Callback, `+0x10` Klasse, `+0x14` Ablaufzeit (`OnAddSystemGridControl`, `GetGridItemExpireTime`) |

## UI-Funktionen (AddFunction)

Aus `AgcmUIMain::OnAddModule` (`0x006071D0`); Spalte „Handler“ ist die Funktion, die das UI-Skript aufruft. Zahl der Registrierungen im Binary und in der Quelle: AddFunction 46/46, AddUserData 9/9, AddDisplay 7/7, AddBoolean 4/4, AddEvent 16/17 (`Test_Event` fehlt im Binary).

| UI-Funktion | Handler | Adresse | Steuerelemente | Typ |
|---|---|---|---:|---|
| `QB_Add` | `CBAddShortcut` | `0x00604490` | 1 | Self Grid Control |
| `QB_Remove` | `CBRemoveShortcut` | `0x00604600` | 1 | Self Grid Control |
| `HPPotion_Add` | `CBAddHPPotion` | `0x00602260` | 1 | Self Grid Control |
| `MPPotion_Add` | `CBAddMPPotion` | `0x006022F0` | 1 | Self Grid Control |
| `QB_Potion_Remove` | `CBRemovePotion` | `0x00602380` | 0 | – |
| `QuickBeltUse_1` | `CBQuickBeltUse_1` | `0x006058A0` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_2` | `CBQuickBeltUse_2` | `0x00605990` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_3` | `CBQuickBeltUse_3` | `0x00605A80` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_4` | `CBQuickBeltUse_4` | `0x00605B70` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_5` | `CBQuickBeltUse_5` | `0x00605C60` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_6` | `CBQuickBeltUse_6` | `0x00605D50` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_7` | `CBQuickBeltUse_7` | `0x00605E40` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_8` | `CBQuickBeltUse_8` | `0x00605F30` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_9` | `CBQuickBeltUse_9` | `0x00606020` | 1 | QuickBelt Grid Control |
| `QuickBeltUse_10` | `CBQuickBeltUse_10` | `0x00606110` | 1 | QuickBelt Grid Control |
| `QuickBeltUseHPPotion` | `CBQuickBeltUseHPPotion` | `0x00602A80` | 1 | QuickBelt Grid Control |
| `QuickBeltUseMPPotion` | `CBQuickBeltUseMPPotion` | `0x00602B30` | 1 | QuickBelt Grid Control |
| `QuickBeltLayerUp` | `CBQuickBeltLayerUp` | `0x006049C0` | 2 | QBelt(L) Grid |
| `QuickBeltLayerDown` | `CBQuickBeltLayerDown` | `0x00604C80` | 2 | QBelt(L) Grid |
| `Close UI Window` | `CBCloseUIWindow` | `0x00602BE0` | 0 | – |
| `Control Edit Init` | `CBEditControlInit` | `0x006028C0` | 1 | Edit Contol |
| `Control Edit Active` | `CBEditControlActive` | `0x006028F0` | 1 | Edit Active |
| `QB Left Click Down` | `CBLClickDown` | `0x00604780` | 0 | – |
| `QB Right Click Down` | `CBRClickDown` | `0x00602920` | 0 | – |
| `QB_Right_Click_Up` | `CBRClickUp` | `0x00604860` | 1 | QBSkill Grid Control |
| `QB PotionGrid RightClickUp` | `CBPotionGridRClickUp` | `0x00602950` | 0 | – |
| `QB Click System Grid NoAction` | `Element::GetSTRING` | – | 0 | – |
| `QB Click System Grid` | `CBClickSystemGrid` | `0x006065D0` | 0 | – |
| `QB Open System Grid Tooltip` | `CBOpenSystemGridToolTip` | `0x00606610` | 0 | – |
| `QB Close System Grid Tooltip` | `CBCloseSystemGridToolTip` | `0x00604F00` | 0 | – |
| `Control Button Disable` | `CBButtonControlDisable` | `0x00602860` | 1 | Button Contol Disable |
| `Control Button Enable` | `CBButtonControlEnable` | `0x00602890` | 1 | Button Contol Enable |
| `Open QuickBelt ToolTip` | `CBOpenToolTip` | `0x00602DD0` | 0 | – |
| `Close QuickBelt ToolTip` | `CBCloseToolTip` | `0x00602E00` | 0 | – |
| `Close All Opened UI ToolTip` | `CBCloseAllUIToolTip` | `0x00602E30` | 0 | – |
| `Quit Event Call` | `CBApplicationQuitEventCall` | `0x00602F90` | 0 | – |
| `QuickBelt Position Adjust` | `CBQuickBeltAdjustPos` | `0x00603000` | 0 | – |
| `QuickBeltV Position Adfjust` | `CBQuickBeltVAdjustPos` | `0x00603080` | 0 | – |
| `SetFocusMovableItem` | `CBSetFocusMovableItem` | `0x00603190` | 0 | – |
| `KillFocusMovableItem` | `CBKillFocusMovableItem` | `0x006032D0` | 0 | – |
| `ChangeHPPointScrollBarValue` | `CBChangeHPPointScollBarValue` | `0x006033C0` | 0 | – |
| `ChangeMPPointScrollBarValue` | `CBChangeMPPointScollBarValue` | `0x00603410` | 0 | – |
| `GetPotionScrollBarControl` | `CBGetPotionScollBarControl` | `0x00604F90` | 2 | AutoUseHPGageControl |
| `MainUIAllClose_KillFocus` | `CBMainUIAllClose` | `0x00603460` | 0 | – |
| `GetOnlineTimeEditControl` | `CBGetOnlineTimeEditControl` | `0x00602670` | 1 | OnlineTime Edit Control |
| `GetAddictStatusEditControl` | `CBGetAddictStatusEditControl` | `0x006026B0` | 1 | AddictStatus Edit Control |

## UI-Ereignisse (AddEvent)

| Ereignis | Handler |
|---|---|
| `QB_Add_Invalid_Item` | – |
| `MainUI_Quit_Question` | `CBUIReturnAppQuit` |
| `QB_Remove_Item_Sound` | – |
| `MainUI_AllClose` | – |
| `MainUI_GetPotionScrollBarControl` | – |
| `MainUI_OpenMediaRate` | – |
| `MainUI_OpenMediaRate18` | – |
| `MainUI_CloseMediaRate` | – |
| `MainUI_GetOnlineTimeEdit` | – |
| `MainUI_GetAddictStatusEdit` | – |
| `Event_ShowAdditionalQuickBelt1` | – |
| `Event_HideAdditionalQuickBelt1` | – |
| `Event_ShowAdditionalQuickBelt2` | – |
| `Event_HideAdditionalQuickBelt2` | – |
| `Event_ShowAdditionalQuickBelt3` | – |
| `Event_HideAdditionalQuickBelt3` | – |

## Anzeigen, Boolean, Userdata

**AddDisplay**

| Name | Id | Handler |
|---|---:|---|
| `&DAT_008bf540` | 0 | `CBDisplayExp` |
| `&DAT_008bf52c` | 1 | `CBDisplayExp` |
| `&DAT_008bf518` | 2 | `CBDisplayExp` |
| `&DAT_008bf504` | 3 | `CBDisplayExp` |
| `_Default` | 4 | `CBDisplayDefault` |
| `Main_INT32` | 4 | `CBDisplayInt32` |
| `QBelt Layer` | 5 | `CBDisplayCurrentLayer` |

**AddBoolean**

| Name | Handler |
|---|---|
| `_Default` | `CBDefaultBoolean` |
| `IsCharacterDead` | `CBSelfCharacterDead` |
| `IsSelected` | `CBIsSelected` |
| `IsAreaKorea` | `CBBooleanIsKorea` |

**AddUserData**

| Name | Zeiger | Größe | Anzahl |
|---|---|---:|---:|
| `local_40` | `iVar2` | 0x24 | 1 |
| `local_40 + 0x20` | `iVar2 + 0x24` | 0x24 | 1 |
| `QB_Layer(L)` | `param_1 + 0x2b30` | 4 | 1 |
| `QB_Layer(R)` | `param_1 + 0x2b30` | 4 | 1 |
| `Alarm_Grid` | `param_1 + 0x2960` | 0x24 | 1 |
| `HPPotion_Grid` | `param_1 + 0x2b40` | 0x24 | 1 |
| `MPPotion_Grid` | `param_1 + 0x2b64` | 0x24 | 1 |
| `SystemMessage_Grid` | `param_1 + 0x2b88` | 0x24 | 1 |
| `EnableExceptJapan` | `param_1 + 0x298c` | 4 | 1 |

## Callbacks (EnumCallback-IDs)

Das Modul feuert die dreizehn Callbacks `AGCMUI_MAIN_CB_*` (IDs 0–12 unverändert gegenüber der Quelle). Im Binary nachgewiesene Auslöser (letztes `push` vor `EnumCallback`, `0x004E4040`):

| ID | Name (Quelle) | Auslöser im Binary |
|---:|---|---|
| 0 | `OPEN_TOOLTIP` | `CBOpenToolTip` (`0x00602DD0`) |
| 1 | `CLOSE_TOOLTIP` | `CBCloseToolTip` (`0x00602E00`) |
| 2 | `CLOSE_ALL_UI_TOOLTIP` | `CBCloseAllUIToolTip` (`0x00602E30`) |
| 3 | `UPDATE_ALARM_GRID` | `UpdateAlarmGrid` (`0x00604F30`) |
| 4 | `RBUTTON_SKILL_CAST` | kein Auslöser (in der Quelle ebenfalls auskommentiert) |
| 5 | `KEYDOWN_CLOSE_ALL_UI_EXCEPT_MAIN` | `CBCloseUIWindow` (`0x00602BE0`) |
| 6 | `ADD_SHORTCUT_ITEM` | `AddShortcut` (`0x00603EF0`) |
| 7 | `REMOVE_SHORTCUT_ITEM` | `RemoveShortcut` (`0x006042A0`) |
| 8 | `UPDATE_HP_POTION` | `CBAddHPPotion` (`0x00602260`), `CBRemovePotion` (`0x00602380`) |
| 9 | `UPDATE_MP_POTION` | `CBAddMPPotion` (`0x006022F0`), `CBRemovePotion` |
| 10 | `KEYDOWN_ESC` | `CBCloseUIWindow` |
| 11 | `UPDATE_HPPOINT_GAGE` | `CBChangeHPPointScollBarValue` (`0x006033C0`) |
| 12 | `UPDATE_MPPOINT_GAGE` | `CBChangeMPPointScollBarValue` (`0x00603410`) |

## Abweichungen von der EP8-Quelle

- `OnIdle` ohne `UpdateMediaRateWindow` (Quelle: nur unter `_AREA_KOREA_`); der Medienbewertungs-Dialog (Alterskennzeichen) wird in diesem Build nie geöffnet.
- `GetKeyCode` liest die Modifikatortasten aus Engine-Zuständen (Shift → 1, Strg → 2, Alt → 3), wie `IsShiftDown/IsCtrlDown/IsAltDown` der Quelle.
- `RefreshQBeltGridItemStackCount` (`0x006036E0`): Die Bedingung für Cash-Skill-Rollen mit Restzeit prüft `+0x30C/+0x308/+0x310` des Items; sie entspricht weder der `_AREA_GLOBAL_`- noch der Standardvariante der Quelle genau (Mischform).
- `OnAddSystemGridControl`: nur die Variante mit `nExpireTime` ist im Binary vorhanden (die Quelle hat beide Varianten per `#ifdef`).
- Das Ereignis `Test_Event` fehlt im Binary; der Modullookup [`AgcmUIOption`](AgcmUIOption.md) steht dort nicht in `OnAddModule` (Zeiger `+0xBC8` wird anderswo gesetzt).

## Grenzen

- Die Zuordnung der 36 neu hinzugekommenen Methoden beruht auf dem Aufrufgraphen und wurde gegen Dekompilat und Quelle gelesen; die `SetCallback*`-Setter sind vom Linker mit gleichartigen Funktionen anderer Module zusammengefaltet und lassen sich nicht einzeln adressieren.
- Nicht untersucht sind die UI-Skripte (`.ui`-Daten), die diese Funktionen aufrufen, sowie `AgcmUIMainSystemGridTooltip` (eigene Klasse).
- Member-Namen der Offset-Tabelle ergeben sich aus der Lesereihenfolge von `OnAddModule` und den Verwendungsstellen; bei Zeigern mit unklarer Reihenfolge ist der Name eine Vermutung.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 6, gemeinsamer Rumpf: 13, nicht im Client: 4, ohne Kandidat: 4.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmLogin`](AgcmLogin.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIOption`](AgcmUIOption.md), [`AgpmGrid`](AgpmGrid.md)
- **Erwähnt in:** [`AgcmBillInfo`](AgcmBillInfo.md), [`AgcmItem`](AgcmItem.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUICustomizing`](AgcmUICustomizing.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIRefinery`](AgcmUIRefinery.md), [`AgcmUIRemission`](AgcmUIRemission.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md), [`AgcmUISocialAction`](AgcmUISocialAction.md), [`AgcmUIStatus`](AgcmUIStatus.md), [`AgcmUITax`](AgcmUITax.md), [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md)
