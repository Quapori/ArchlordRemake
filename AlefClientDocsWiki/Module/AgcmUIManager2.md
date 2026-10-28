# AgcmUIManager2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIManager2` (UI-Verwaltung: UI- und Steuerelement-Tabellen, Registrierung von Funktionen/Ereignissen/Anzeigen, Aktionen, `.ui`-Streams) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmUIManager2` (`AgcmUIManager2.cpp`, `AgcmUIManager2Stream.cpp`). Der Code liegt in zwei Adressbereichen: `0x005E1500`–`0x005EAD20` (Hauptteil) und `0x00630210`–`0x00632C20` (Stream).

## Kernbefund

- **Abdeckung:** 37 von 194 Quellmethoden sind zugeordnet (siehe Tabelle). Die meisten Funktionen im Bereich sind klein, werden über Funktionszeiger aufgerufen und besitzen keine Zeichenketten; Aufrufgraph-Vorschläge ergaben sich nur für die sieben Verwaltungsfunktionen unten.
- **Registrierung:** Die fünf `Add*`-Funktionen, über die jedes UI-Modul seine Skriptschnittstelle anmeldet, sind adressiert und stimmen in Signatur und Objektlayout mit der Quelle überein (Details unten). Damit sind die Registrierungen von [`AgcmUIMain`](AgcmUIMain.md) (46 Funktionen) und weiteren UI-Modulen einem festen Satz Zieladressen zugeordnet.
- **UI-Lebenszyklus:** `AttachUI`, `DetachUI`, `RemoveUI`, `DestroyUI`, `RefreshUI` und `CloseAllUIExceptMainUI` entsprechen der Quelle; Status- und Offsetwerte der UI-Struktur sind in der Offset-Tabelle.
- **Stream:** Die Formatzeichenketten der `.ui`-Dateien stimmen, soweit lokalisiert, mit der Quelle überein; `StreamReadCB` ist im Binary größer als in der Quelle (1426 Dekompilat-Zeilen gegen ~940 Quellzeilen), was durch Inline-Ausdehnung erklärbar ist, aber nicht Zeile für Zeile geprüft wurde.
- **Abweichungen:** keine festgestellt; geprüft sind nur die oben genannten Funktionen.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIManager2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005E6960` | 463 | vtable/String |
| 1 | `CBUpdateActionState` | `0x005E5E50` | 138 | Callback-Registrierung |
| 2 | `OnInit` | `0x005E9910` | 3835 | vtable/String |
| 3 | `OnIdle` | `0x005E7D70` | 716 | vtable/String |
| 4 | `OnDestroy` | `0x005E7410` | 148 | vtable/String |
| 5 | `AttachUIData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 6 | `AttachControlData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 7 | `SetMaxUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 8 | `SetMaxUIMessage` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 9 | `SetMainWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 10 | `ResizeManagerWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 11 | `SetMaxMaps` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 12 | `MakeValidName` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 13 | `CreateUI` | `0x005E1840` | 347 | Aufrufgraph (geprüft) |
| 14 | `DestroyUI` | `0x005E8040` | 429 | Aufrufgraph (geprüft) |
| 15 | `AddUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 16 | `GetUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 17 | `GetUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 18 | `RemoveUI` | `0x005E5EE0` | 102 | Aufrufgraph (geprüft) |
| 19 | `RemoveAllUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 20 | `ChangeUIName` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 21 | `GetSequenceUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 22 | `OpenUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 23 | `CloseUI` | `0x005E54B0` | 829 | Zeichenkette |
| 24 | `AttachUI` | `0x005E5800` | 143 | Aufrufgraph (geprüft) |
| 25 | `DetachUI` | `0x005E51B0` | 56 | Aufrufgraph (geprüft) |
| 26 | `AttachTooltip` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 27 | `DetachTooltip` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 28 | `OpenMainUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 29 | `CloseAllUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 30 | `CloseAllUIExceptMainUI` | `0x005E5900` | 152 | Aufrufgraph (geprüft) |
| 31 | `CloseAllEventUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 32 | `CopyUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 33 | `SetUIData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 34 | `GetUIData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 35 | `AddControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 36 | `SetControlAlpha` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 37 | `GetControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 38 | `GetControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 39 | `GetControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 40 | `GetControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 41 | `GetControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 42 | `GetControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 43 | `RemoveControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 44 | `RemoveControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 45 | `GetSequenceControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 46 | `GetSequenceControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 47 | `CopyBaseProperty` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 48 | `CopyControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 49 | `RefreshUI` | `0x005E4AC0` | 135 | Aufrufgraph (geprüft) |
| 50 | `RefreshControl` | `0x005E3850` | 1825 | Aufrufgraph (geprüft) |
| 51 | `AddFunction` | `0x005E3FB0` | 123 | von Hand geprüft |
| 52 | `AddUserData` | `0x005E4030` | 130 | von Hand geprüft |
| 53 | `AddDisplay` | `0x005E40C0` | 118 | von Hand geprüft |
| 54 | `AddDisplay` | `0x005E4140` | 118 | von Hand geprüft |
| 55 | `AddBoolean` | `0x005E41C0` | 99 | von Hand geprüft |
| 56 | `AddCustomControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 57 | `CreateFunction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 58 | `DestroyFunction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 59 | `AddFunction` | `0x005E1F80` | 74 | von Hand geprüft |
| 60 | `GetFunction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 61 | `GetFunction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 62 | `RemoveAllFunction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 63 | `CreateUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 64 | `DestroyUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 65 | `AddUserData` | `0x005E20A0` | 74 | von Hand geprüft |
| 66 | `GetUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 67 | `GetUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 68 | `RemoveAllUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 69 | `GetControlUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 70 | `CountUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 71 | `CountUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 72 | `CountUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 73 | `SetUserDataRefresh` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 74 | `RefreshUserData` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 75 | `CreateDisplay` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 76 | `DestroyDisplay` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 77 | `AddDisplay` | `0x005E2300` | 74 | von Hand geprüft |
| 78 | `GetDisplay` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 79 | `GetDisplay` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 80 | `RemoveAllDisplay` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 81 | `CreateBoolean` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 82 | `DestroyBoolean` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 83 | `AddBoolean` | `0x005E23E0` | 74 | von Hand geprüft |
| 84 | `GetBoolean` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 85 | `GetBoolean` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 86 | `RemoveAllBoolean` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 87 | `GetCControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 88 | `GetCControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 89 | `RemoveAllCControl` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 90 | `EnumDisplayCallback` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 91 | `ResetControlDisplayMap` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 92 | `SetControlDisplayMap` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 93 | `SetControlDisplayMap` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 94 | `SetControlDisplayFont` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 95 | `AddEvent` | `0x005E6BA0` | 226 | von Hand geprüft |
| 96 | `GetEventMap` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 97 | `GetEventMap` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 98 | `ThrowEvent` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 99 | `ThrowEvent` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 100 | `RemoveAllEvent` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 101 | `RemoveAllEventActions` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 102 | `AddHotkey` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 103 | `GetHotkey` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 104 | `RemoveHotkey` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 105 | `RemoveHotkey` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 106 | `CopyHotkey` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 107 | `RemoveAllHotkey` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 108 | `SetHotkeyDescription` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 109 | `ResetControlGrid` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 110 | `SetControlGrid` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 111 | `GetControlGrid` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 112 | `ProcessAction` | `0x005E6E70` | 1324 | Zeichenkette |
| 113 | `ParseMessage` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 114 | `SetupActions` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 115 | `SetupActions` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 116 | `SetupAction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 117 | `RemoveFromActions` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 118 | `RemoveFromActions` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 119 | `RemoveFromAction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 120 | `CBListItemConstructor` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 121 | `CBListItemDestructor` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 122 | `CBListItemRefresh` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 123 | `CB_POST_RENDER` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 124 | `CBIsCameraMoving` | `0x005E2CB0` | 33 | Callback-Registrierung |
| 125 | `OnCameraStateChange` | `0x005E4430` | 8 | vtable/String |
| 126 | `CameraStatusChange` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 127 | `SetCamera` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 128 | `AddWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 129 | `RemoveWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 130 | `RefreshWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 131 | `SetCallbackOpenMainUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 132 | `SetCallbackCloseAllUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 133 | `SetCallbackSetMainWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 134 | `SetCallbackActionMessageChat` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 135 | `IsMainWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 136 | `CBSetCursorMousePosition` | `0x005E2EB0` | 36 | Callback-Registrierung |
| 137 | `ActionMessageOKDialog` | `0x005E2EE0` | 64 | von Hand geprüft |
| 138 | `ActionMessageOKDialog2` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 139 | `ActionMessageOKCancelDialog` | `0x005E2F70` | 64 | von Hand geprüft |
| 140 | `ActionMessageOKCancelDialog2` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 141 | `ActionMessageEditOKDialog` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 142 | `ActionMessageEditOKDialog2` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 143 | `ActionMessageThreeBtnDialog` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 144 | `ActionMessageEditOKCancelDialog` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 145 | `SortPopupUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 146 | `SetSoundPath` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 147 | `SetTexturePath` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 148 | `SetUIMode` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 149 | `GetLineDelimiter` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 150 | `GetUIMessage` | `0x005E6600` | 259 | Zeichenkette |
| 151 | `GetSeparateLine` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 152 | `CloseTooltip` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 153 | `CloseTooltip` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 154 | `OpenTooltip` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 155 | `SetControlTooltip` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 156 | `Notice` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 157 | `SetMouseOnUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 158 | `UIClose` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 159 | `ShowUIName` | `0x005E3520` | 128 | Zeichenkette |
| 160 | `SetUIMgrProcessHotkeys` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 161 | `IsOpenModalWindow` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 162 | `GetModeWidth` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 163 | `GetModeHeight` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 164 | `RunFade` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 165 | `OnRender` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 166 | `RenderFade` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 167 | `_RunFade` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 168 | `_DelayFade` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 169 | `_EventFadeFinsh` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 170 | `_CalcPosition` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 171 | `_CalcSize` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 172 | `CalcRelativeToAbsolute` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 173 | `CalcAbsoluteToRelative` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 174 | `StreamWriteUI` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 175 | `StreamWrite` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 176 | `StreamRead` | `0x00630210` | 866 | Zeichenkette |
| 177 | `StreamWriteCB` | `0x006325E0` | 612 | Callback-Registrierung |
| 178 | `StreamWriteControl` | `0x00630580` | 1078 | Zeichenketten/Konstanten (geprüft) |
| 179 | `StreamWriteBase` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 180 | `StreamWriteAction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 181 | `StreamWriteButton` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 182 | `StreamWriteSkillTree` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 183 | `StreamWriteGrid` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 184 | `StreamWriteBar` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 185 | `StreamWriteList` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 186 | `StreamWriteTree` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 187 | `StreamWriteEdit` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 188 | `StreamWriteScroll` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 189 | `StreamWriteCombo` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 190 | `StreamWriteClock` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 191 | `StreamReadCB` | `0x00630A00` | 7134 | Callback-Registrierung |
| 192 | `StreamReadAction` | – | | nicht zugeordnet (klein, Funktionszeiger-Aufruf oder ohne eindeutigen Anker) |
| 193 | `StreamReadUIMessage` | `0x00632850` | 868 | vtable/String |

37 von 194 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AddFunction_005e1f80` (`0x005E1F80`), `AddUserData_005e20a0` (`0x005E20A0`), `AddDisplay_005e2300` (`0x005E2300`), `AddBoolean_005e23e0` (`0x005E23E0`), `AddDisplay_005e4140` (`0x005E4140`), `~AgcmUIManager2` (`0x005E98F0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `AgcdUI +0x34` | `m_eStatus (0 NONE, 1 ADDED, 2 CLOSING, 4 OPENED)` | `AttachUI`, `RemoveUI` |
| `AgcdUI +0x58` | `m_szUIName` | `RemoveUI`; `AgcmUIMain::IsCurrentUI` vergleicht mit `"UI_CharInfo"` |
| `AgcdUI +0x98` | `m_pcsUIWindow` | `CloseAllUIExceptMainUI` (`[+0x98]+0xC` = m_bOpened), `AttachUI` |
| `AgcdUI +0xA0` | `Liste der Steuerelemente` | `RefreshUI`, `DestroyUI` |
| `AgcdUI +0x120 / +0x124` | `m_bMainUI / m_bAutoClose` | `CloseAllUIExceptMainUI` |
| `AgcdUI +0x13C / +0x140` | `m_pcsUIAttach / m_eAttachType` | `AttachUI`, `DetachUI` |
| `AgcdUIControl +0xF0 / +0xF4` | `m_lType / m_pcsBase` | `RefreshControl`; `AgcmUIMain::SetHPPointScrollBarValue` |
| `AgcdUIControl +0x150` | `m_pcsParentUI` | `AgcmUIMain::IsCurrentUI` |
| `AgcmUIManager2 +0xEF0 / +0xEF4` | `m_lMaxUIEvents / m_lMaxUIEventID` | `AddEvent` |
| `AgcmUIManager2 +0x2628` | `m_pcsMouseOnUI` | `AgcmUIMain::OnIdle` |
| `AgcmUIManager2 +0x262C` | `m_pcsMouseOnUIPrev` | `RemoveUI`, `DestroyUI` |
| `AgcmUIManager2 +0x2630` | `m_bBeingDestroyed` | `RemoveUI` gibt es an `CloseUI` weiter |
| `AgcmUIManager2 +0x4560 / +0x4564` | `m_lWindowWidth / m_lWindowHeight` | `ActionMessageOK(Cancel)Dialog` |

## Registrierungsschnittstelle (für UI-Module)

Alle UI-Module (`AgcmUIMain` u. a.) melden ihre Funktionen, Ereignisse, Anzeigen und Userdaten über diese Aufrufe an; die Signaturen stimmen mit der Quelle überein (Parameterreihenfolge und Feldzuweisung gegen das Dekompilat gelesen).

| Aufruf | Adresse | Neues Objekt | Felder im Objekt |
|---|---|---|---|
| `AddFunction(pvClass, name, callback, argNum, desc1..5)` | `0x005E3FB0` | `AgcdUIFunction`, 0x60 Byte | `+0x5C` Klasse, `+0x40` Callback, `+0x44` ArgAnzahl, `+0x48..0x58` Beschreibungen |
| `AddUserData(name, data, size, count, type)` | `0x005E4030` | `AgcdUIUserData`, 0x68 Byte | `+0x44` Daten, `+0x48` Größe, `+0x4C` Anzahl, `+0x40` Typ, `+0x50/0x54` = −1 |
| `AddDisplay(pvClass, name, id, callback, dataType)` | `0x005E40C0` | `AgcdUIDisplay`, 0x54 Byte | `+0x4C` Klasse, `+0x40` ID, `+0x44` Callback, `+0x48` alter Callback = 0, `+0x50` Datentyp |
| `AddDisplay(…, oldCallback, …)` | `0x005E4140` | wie oben | `+0x44` = 0, `+0x48` alter Callback |
| `AddBoolean(pvClass, name, callback, dataType)` | `0x005E41C0` | `AgcdUIBoolean`, 0x4C Byte | `+0x44` Klasse, `+0x40` Callback, `+0x48` Datentyp |
| `AddEvent(name, returnCallback, pClass)` | `0x005E6BA0` | Eintrag, 0x7C Byte (Speicherpool) | `+0x74` Callback, `+0x78` Klasse; Zähler `+0xEF4` gegen Maximum `+0xEF0`; gibt die neue Ereignis-ID oder −1 zurück |

Die Hilfsfunktionen für das Eintragen in die Tabellen (`AddFunction(AgcdUIFunction*)` `0x005E1F80`, `AddUserData(…)` `0x005E20A0`, `AddDisplay(…)` `0x005E2300`, `AddBoolean(…)` `0x005E23E0`) sind benannt; das Anlegen (`CreateFunction` usw.) ist in die Aufrufer eingefaltet.

## Meldungsdialoge

`ActionMessageOKDialog` (`0x005E2EE0`) und `ActionMessageOKCancelDialog` (`0x005E2F70`) setzen die Position des Meldungsfensters mittig (`Breite/2 − 206`, `Höhe/2 − 90`, also 412 × 180 Pixel) und rufen `MessageDialog` bzw. `OkCancelDialog` der Engine. Fenstergröße des Clients: `+0x4560` Breite, `+0x4564` Höhe.

## UI-Lebenszyklus

| Funktion | Adresse | Befund |
|---|---|---|
| `AttachUI` | `0x005E5800` | verweigert Status NONE/ADDED/CLOSING (`+0x34` = 0/1/2) bei beiden UIs; hängt an `+0x13C` (Ziel) und `+0x140` (Typ) |
| `DetachUI` | `0x005E51B0` | löscht `+0x13C`, entfernt aus der Anhängeliste |
| `CloseAllUIExceptMainUI` | `0x005E5900` | schließt alle UIs mit `+0x120` (m_bMainUI) = 0, `+0x124` (m_bAutoClose) ≠ 0 und geöffnetem Fenster |
| `RemoveUI` | `0x005E5EE0` | schließt geöffnete UIs (Status 4), entfernt aus der Tabelle, setzt Status 0 und räumt `+0x262C` (Maus-UI) |
| `DestroyUI` | `0x005E8040` | räumt Steuerelemente (Typen 10 und 0x11 zuerst), Verweise und Maus-UI auf |
| `RefreshUI` | `0x005E4AC0` | ruft `RefreshControl` (`0x005E3850`, 1825 Byte, Switch über den Steuerelementtyp `+0xF0`) für jedes Steuerelement |
| `CloseUI` | `0x005E54B0` | benannt (Zeichenkette) |

## Stream-Funktionen (.ui-Dateien)

| Funktion | Adresse | Größe |
|---|---|---:|
| `StreamRead` | `0x00630210` | 186 Dekompilat-Zeilen |
| `StreamWriteControl` | `0x00630580` | 188 Zeilen (Zeichenketten identisch mit der Quelle) |
| `StreamReadCB` | `0x00630A00` | 1426 Zeilen (Quelle: ~940) |
| `StreamWriteCB` | `0x006325E0` | 79 Zeilen |
| `StreamReadUIMessage` | `0x00632850` | 180 Zeilen |

Von den 31 Formatzeichenketten der Quelle (`"%d:%d:…"`, mit denen Aktionen und Steuerelement-Parameter gelesen werden) kommen 24 im Adressbereich der Stream-Funktionen vor, im Binary gibt es dort keine zusätzlichen. Die 7 fehlenden gehören vermutlich zu Schreibfunktionen, die nicht lokalisiert sind; ein Format, das nur im Binary vorkommt, wurde nicht gefunden.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`Add*`, Dialoge, `AttachUI`, `DetachUI`, `CloseAllUIExceptMainUI`, `RemoveUI`, `RefreshUI`).

## Grenzen

- Zugeordnet sind überwiegend Funktionen mit Zeichenketten oder eindeutiger Aufrufbeziehung; rund 150 Methoden (Steuerelement-Tabellen `GetControl`/`GetSequenceControl`, Hotkeys, Aktionen, Tooltips, `StreamWrite*`-Varianten) sind nicht einzeln adressiert.
- `RefreshControl` und `DestroyUI` wurden gegen die Quelle gelesen, aber nicht Zeile für Zeile verglichen (große Schalter über den Steuerelementtyp).
- Das Format der `.ui`-Dateien (Schlüssel und Reihenfolge) wurde nur über die Formatzeichenketten geprüft, nicht über die Schlüsselnamen, da diese als Konstanten übergeben werden.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 37, eingebaut: 29, gemeinsamer Rumpf: 4, nicht im Client: 23, ohne Kandidat: 33, zugeordnet: 37.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `CBListItemConstructor` | 45 | `0x005E8CD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ResetControlDisplayMap` | 13 | `0x005E2640` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenTooltip` | 43 | `0x005E3210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetControlDisplayFont` | 13 | `0x005E28D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetControlDisplayMap_2` | 0 | `0x005E2770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetControlDisplayMap` | 26 | `0x005E26A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyControl` | 106 | `0x005E8910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyBaseProperty` | 151 | `0x005E1A80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddUI` | 13 | `0x005E19A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetMouseOnUI` | 10 | `0x005E34D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveWindow` | 12 | `0x005E2E30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyHotkey` | 24 | `0x005E6560` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHotkey` | 4 | `0x005E2980` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddHotkey` | 13 | `0x005E6C90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RefreshUserData` | 9 | `0x005E43E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveControl` | 111 | `0x005E74B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddControl` | 153 | `0x005E8250` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUIData` | 7 | `0x005E1A20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyUI` | 108 | `0x005E9210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CloseAllEventUI` | 13 | `0x005E59A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CloseAllUI` | 11 | `0x005E5890` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadAction` | 198 | `0x0062FDB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteClock` | 16 | `0x0062F790` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteCombo` | 15 | `0x0062F720` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteScroll` | 19 | `0x0062F660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteEdit` | 19 | `0x0062F5D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteTree` | 12 | `0x0062F570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteList` | 14 | `0x0062F500` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteBar` | 18 | `0x0062F450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteGrid` | 20 | `0x0062F350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteBase` | 99 | `0x0062EE80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsOpenModalWindow` | 56 | `0x005E35B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Notice` | 33 | `0x005E33C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ActionMessageEditOKCancelDialog` | 5 | `0x005E3040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ActionMessageThreeBtnDialog` | 8 | `0x005E2FB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ActionMessageOKDialog2` | 5 | `0x005E2F20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CameraStatusChange` | 43 | `0x005E2CE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `RemoveAllUI` (`0x005E8DF0`), `OpenUI` (`0x005E5F50`), `GetControl` (`0x005FD850`), `GetControl` (`0x005FD850`), `GetControl` (`0x005FD850`), `GetControl` (`0x005FD850`), `GetControl` (`0x005FD850`), `GetControl` (`0x005FD850`), `RemoveControl` (`0x005FD740`), `GetSequenceControl` (`0x005FD850`), `GetSequenceControl` (`0x005FD850`), `AddFunction` (`0x0062D600`), `AddUserData` (`0x0062D600`), `AddDisplay` (`0x005E1EF0`), `AddDisplay` (`0x0062D600`), `AddBoolean` (`0x00602DB0`), `AddCustomControl` (`0x005E1EF0`), `GetControlUserData` (`0x005E4C50`), `CountUserData` (`0x005FD850`), `CountUserData` (`0x005FD850`), `CountUserData` (`0x005FD850`), `SetUserDataRefresh` (`0x005E4C50`), `GetDisplay` (`0x005E24C0`), `GetBoolean` (`0x005E24C0`), `GetCControl` (`0x005E24C0`), `SetControlDisplayMap` (`0x005FD850`), `GetEventMap` (`0x005E77A0`), `GetEventMap` (`0x005E77A0`), `SetControlGrid` (`0x005FD850`), `GetControlGrid` (`0x005E7750`), `RemoveFromActions` (`0x005FD850`), `RemoveFromActions` (`0x005FD850`), `AddWindow` (`0x005FC1F0`), `OnRender` (`0x005E7750`), `StreamWriteAction` (`0x0062FAB0`), `StreamWriteButton` (`0x0062FAB0`), `StreamWriteSkillTree` (`0x0062FAB0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIMain`](AgcmUIMain.md)
- **Erwähnt in:** [`AgcAuth`](AgcAuth.md), [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmMinimap`](AgcmMinimap.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmSocialActon`](AgcmSocialActon.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTitle`](AgcmTitle.md), [`AgcmUIArchlord`](AgcmUIArchlord.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIConsole`](AgcmUIConsole.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIEventBank`](AgcmUIEventBank.md), [`AgcmUIEventGacha`](AgcmUIEventGacha.md), [`AgcmUIGuideMessage`](AgcmUIGuideMessage.md), [`AgcmUIHelp`](AgcmUIHelp.md), [`AgcmUIHotkey`](AgcmUIHotkey.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIRefinery`](AgcmUIRefinery.md), [`AgcmUIRemission`](AgcmUIRemission.md), [`AgcmUISearch`](AgcmUISearch.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUISocialAction`](AgcmUISocialAction.md), [`AgcmUITax`](AgcmUITax.md), [`AgcmUITips`](AgcmUITips.md), [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md), [`AgcmUIWarInfo`](AgcmUIWarInfo.md)
