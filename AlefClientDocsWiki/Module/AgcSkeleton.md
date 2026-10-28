# AgcSkeleton (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse von `AgcSkeleton` (Fensterschicht und Hauptschleife des Clients, das „Skelett“ der RenderWare-Beispielanwendung: `API_win.cpp`, `API_skeleton.cpp`, `API_camera.cpp`, `API_mouse.cpp`, `API_menu.cpp`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Die Quelle besteht aus 143 freien Funktionen (`ps…` für die Plattform, `Rs…` für die Ereignisschicht, `Camera…`, `Menu…`). Belege: Ghidra-Dekompilat, Windows-API-Aufrufe (`RegisterClassA`, `CreateWindowExA`, `PeekMessageA`, `DispatchMessageA`), Aufrufgraph, EP8-Quelle `Modules/AClient/AgcSkeleton`. Alle Adressen gelten nur für den 2017er Build. Die Klassen `CGameFramework`, `CRenderDevice`, `CRenderWindow` der Quelle kommen im Binary nicht vor (weder Name noch RTTI): der 2017er Client startet über die ältere Schicht.

## Kernbefund

- **Abdeckung:** 9 von 143 Funktionen zugeordnet. Zugeordnet ist die Startkette: `WinMain` (`0x00650D30`), `InitApplication` (`0x00650CA0`), `InitInstance` (`0x0064FB40`), `MainWndProc` (`0x0064FEA0`), `CommandLineToArgv` (`0x00650B50`), der Ereignisverteiler `RsEventHandler` (`0x0064D1E0`), `RsRwInitialize` (`0x0064D320`) und `RsIsDialogMessage` (`0x0064D170`).
- **Anderes Verhalten als die Quelle:** `MainWndProc` ist im Binary nur 363 Byte groß (Quelle: 554 Zeilen): der Client behandelt in ihr nur Fenster erstellen/schließen, Größe, Aktivierung und Zeitgeber (`WM_CREATE`, `WM_CLOSE`/`WM_DESTROY`, `WM_SIZE`, `WM_ACTIVATE`) und leitet Eingaben an die Engine-Module weiter. `InitApplication` initialisiert zusätzlich den Zeitgeber `AuTickCounter` (`0x004F4950`). In der Hauptschleife von `WinMain` werden pro Durchlauf zwei kleine Funktionen aus dem Adressbereich von `AuGameGuard` (`0x004EDFA0`, `0x004EDF40`) gerufen; liefert die zweite 0, fordert die Schleife das Beenden an (Ereignis `0x23`). Ob es der GameGuard-Wächter ist, ist aus der Lage geschlossen.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcSkeleton.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `psWindowSetText` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 1 | `psErrorMessage` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 2 | `psWarningMessage` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 3 | `psCameraShowRaster` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 4 | `psTimer` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 5 | `psGrabScreen` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 6 | `psMouseSetVisibility` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 7 | `psMouseSetPos` | `0x0064F8A0` | 82 | von Hand geprüft |
| 8 | `psPathnameCreate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 9 | `psPathnameDestroy` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 10 | `psPathGetSeparator` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 11 | `psGetMemoryFunctions` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 12 | `psInstallFileSystem` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 13 | `psNativeTextureSupport` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 14 | `psDebugMessageHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 15 | `winTranslateKey` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 16 | `ClipMouseToWindow` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 17 | `InitApplication` | `0x00650CA0` | 112 | von Hand geprüft |
| 18 | `InitInstance` | `0x0064FB40` | 124 | von Hand geprüft |
| 19 | `psInitialize` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 20 | `psTerminate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 21 | `psAlwaysOnTop` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 22 | `psMetricsRender` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 23 | `dialogAddModes` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 24 | `dialogInit` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 25 | `dialogDevSelect` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 26 | `DialogProc` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 27 | `MainWndProc` | `0x0064FEA0` | 363 | von Hand geprüft |
| 28 | `psSelectDevice` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 29 | `psDisplaySplashScreen` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 30 | `CommandLineToArgv` | `0x00650B50` | 321 | von Hand geprüft |
| 31 | `EnableWindowsShortcutKeys` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 32 | `DisableWindowsShortcutKeys` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 33 | `WinMain` | `0x00650D30` | 717 | von Hand geprüft |
| 34 | `RsGetWindowHandle` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 35 | `FreeDirectInput` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 36 | `InitDirectInputDevice` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 37 | `ReadImmediateDIData` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 38 | `ReadBufferedDIData` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 39 | `RsKeyFromScanCode` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 40 | `RsDisplaySplashScreen` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 41 | `RsTimer` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 42 | `RsWindowSetText` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 43 | `RsErrorMessage` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 44 | `RsWarningMessage` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 45 | `RsPathGetSeparator` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 46 | `RsCameraShowRaster` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 47 | `RsAlwaysOnTop` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 48 | `RsRegisterImageLoader` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 49 | `RsSetDebug` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 50 | `RsMouseSetVisibility` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 51 | `RsMouseSetPos` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 52 | `RsSelectDevice` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 53 | `RsInputDeviceAttach` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 54 | `rsCommandLine` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 55 | `rsPreInitCommandLine` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 56 | `RsKeyboardEventHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 57 | `RsMouseEventHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 58 | `RsPadEventHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 59 | `RsEventHandler` | `0x0064D1E0` | 225 | von Hand geprüft |
| 60 | `RsPathnameDestroy` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 61 | `RsPathnameCreate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 62 | `texDictDestroyCB` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 63 | `RsRwTerminate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 64 | `RsRwInitialize` | `0x0064D320` | 453 | von Hand geprüft |
| 65 | `RsTerminate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 66 | `RsInitialize` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 67 | `RsSetModelTexturePath` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 68 | `RsSetPresetView` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 69 | `RsSetNextPresetView` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 70 | `RsSetPreviousPresetView` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 71 | `RsDestroyPresetViews` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 72 | `CameraElAzPosFromLTM` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 73 | `RsGetPresetViewDescription` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 74 | `RsSavePresetView` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 75 | `RsGrabScreen` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 76 | `RsCharsetPrint` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 77 | `RsSetDialogMsgFunc` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 78 | `RsSetDialogMsgFuncClass` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 79 | `RsIsDialogMessage` | `0x0064D170` | 34 | von Hand geprüft |
| 80 | `CameraSize` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 81 | `CameraDestroy` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 82 | `CameraCreate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 83 | `CameraMove` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 84 | `CameraPan` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 85 | `CameraTilt` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 86 | `CameraRotate` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 87 | `CameraCreateCrossHair` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 88 | `rsMouseVisible` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 89 | `rsMouseAddDelta` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 90 | `rsMouseGetPos` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 91 | `rsMouseSetPos` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 92 | `rsMouseRender` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 93 | `rsMouseTerm` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 94 | `rsMouseInit` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 95 | `FreeHelpLines` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 96 | `HelpModeTrigger` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 97 | `MenuSetStatus` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 98 | `MenuGetStatus` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 99 | `MenuToggle` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 100 | `ResetActiveEntry` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 101 | `RemoveEntry` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 102 | `AddNewEntry` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 103 | `RgbToHsv` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 104 | `HsvToRgb` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 105 | `InterpolateColor` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 106 | `UpdateLongestEntryLength` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 107 | `FindByTarget` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 108 | `MenuRemoveEntry` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 109 | `MenuAddEntryBool` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 110 | `MenuAddEntryBoolTransient` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 111 | `ValidateEnumStrings` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 112 | `MenuAddEntryInt` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 113 | `MenuAddSeparator` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 114 | `MenuAddEntryReal` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 115 | `MenuAddEntryTrigger` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 116 | `MenuSelectEntry` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 117 | `MenuSetRangeReal` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 118 | `MenuSetRangeInt` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 119 | `MenuSelectNext` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 120 | `MenuSelectPrevious` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 121 | `MenuSelectNext` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 122 | `MenuSelectPrevious` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 123 | `MenuSelectionAddPercentage` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 124 | `MenuSelectionAddValue` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 125 | `CheckHelpFilesBottomLine` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 126 | `MenuMouseHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 127 | `AutoRepeatPrepare` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 128 | `AutoRepeat` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 129 | `HandlePadButtonDown` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 130 | `HandlePadButtonUp` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 131 | `HandlePadAnalogueLeft` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 132 | `MenuPadHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 133 | `MenuKeyboardShortcutHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 134 | `MenuHandleKeyDown` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 135 | `MenuHandleKeyUp` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 136 | `MenuKeyboardHandler` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 137 | `RenderMenuEntries` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 138 | `RenderMenuEntries` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 139 | `RenderHelpScreen` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 140 | `MenuRender` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 141 | `MenuClose` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |
| 142 | `MenuOpen` | – | | nicht zugeordnet (Verbleib offen: im Binary nicht eindeutig bestimmt oder gegen die Engine-Funktionen ersetzt) |

9 von 143 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Startkette

`WinMain` (`0x00650D30`, 717 Byte): ruft `RsEventHandler(0x15)` (Initialisieren), `InitApplication`, zerlegt die Befehlszeile (`GetCommandLineA`, `CommandLineToArgv` `0x00650B50`) und reicht die Argumente ab dem zweiten als Ereignis `0x2A` (Befehlszeile) weiter, erzeugt das Fenster (`InitInstance`), meldet `RsEventHandler(0x12)` (Engine initialisieren), richtet bei Vollbild das Fenster ohne Rahmen ein (`SetWindowLongA`, `SetWindowPos`), zentriert sonst das Fenster, zeigt es und läuft dann in der Schleife `PeekMessageA` / `RsIsDialogMessage` / `DispatchMessageA`; im Leerlauf (keine Nachricht) sendet es das Ereignis `0x17` und ruft danach `0x0075E320` (nicht untersucht). Am Ende folgen die Ereignisse `0x13` (Engine beenden) und `0x16` (beenden).
`InitApplication` (`0x00650CA0`) registriert die Fensterklasse (Stil `0x2008`, Fensterprozedur `0x0064FEA0`, Symbol 0x87, Pfeil-Cursor); `InitInstance` (`0x0064FB40`) erzeugt das Fenster (`CreateWindowExA`); `MainWndProc` (`0x0064FEA0`) behandelt `WM_CREATE` (Datei-Ziehen erlauben, Eingabemethode `0x00733550`/`0x00732600`), `WM_CLOSE`/`WM_DESTROY` (`ClipCursor(NULL)`, `PostQuitMessage`), `WM_SIZE` (Ereignis `0x2B`, Größe an die Engine `RsEventHandler(0, …)`), `WM_ACTIVATE` (Zeitgeber 1 mit 20 ms bei Inaktivität, Merker `0x00953994`) und leitet die übrigen Nachrichten weiter.

## Ereignisschicht

`RsEventHandler` (`0x0064D1E0`, 225 Byte) fragt zuerst die Module (Engine-Verteiler `0x005972C0`) und führt bei Antwort 2 (nicht behandelt) die Standardbehandlung aus: `0x11` Zeitgeber/Pause (`0x0064CF80`), `0x12` Engine einrichten (`RsRwInitialize` `0x0064D320`, Meldungen „Error initializing Engine.“, „Error attaching plugin.“, „Error attaching device.“), `0x13` Aufräumen (`0x0064D0C0`), `0x14` Gerät wählen (`0x0064CFE0`), `0x15` Anwendung initialisieren (`0x0064D0F0`, Fenstertitel „RenderWare Application“), `0x2A` Befehlszeile (Schalter `-vms` setzt `DAT_00953790` auf 0); Ereignis `0x23` setzt das Beenden-Flag `DAT_009E2ADC`. `RsIsDialogMessage` (`0x0064D170`) reicht eine Nachricht an die gesetzte Dialogfunktion weiter, falls es eine gibt.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen (Dekompilat) sind `WinMain`, `InitApplication`, `MainWndProc` (Anfang, bis `WM_ACTIVATE`) und `RsEventHandler`. Die Zuordnung von `InitInstance` (`0x0064FB40`) und `CommandLineToArgv` (`0x00650B50`) folgt aus ihrer Stellung in `WinMain` und den Windows-Funktionen (`CreateWindowExA` bzw. nur ein Aufruf nach `GetCommandLineA`), nicht aus gelesenem Code. `RsRwInitialize` ist über die drei Fehlermeldungen belegt. Die Ereigniscodes sind aus den Aufrufen von `RsEventHandler` gelesen und nicht gegen die Aufzählung `RsEventStatus` der RenderWare-Skeleton-Quelle verglichen.
- Die übrigen `ps…`-, `Rs…`-, `Camera…`-, `rsMouse…`- und `Menu…`-Funktionen sind nicht zugeordnet: viele sind in der Quelle Beispiel-Code (Menü, Kamerasteuerung, Mauszeiger), den der Client nicht benutzt; einige (z. B. `psTimer`, `psMouseSetVisibility`, `RsSetDialogMsgFunc`) sind kleine Funktionen, die im Bereich `0x0064CF00`–`0x0064FB40` nicht eindeutig ausmachen konnte (die Funktion `0x0064F8A0` mit `SetCursorPos` ist als `psMouseSetPos` benannt).

## Querverweise

- **Erwähnt in:** [`AuInputComposer`](AuInputComposer.md), [`CImmLib`](CImmLib.md)
