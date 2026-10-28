# AgcmUIHotkey (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIHotkey` (Einstellbare Tastenkürzel: Standard-/Benutzer-Hotkeys, Konfliktprüfung, Hotkey-Datei) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmUIHotkey/AgcmUIHotkey.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 22 von 32 Quellmethoden sind zugeordnet; die Registrierungen in `OnInit` und die Aufrufbeziehungen liefern die Zuordnung, mehrere Methoden (INI-Funktionen, Tastenabfrage) wurden zusätzlich gegen die Quelle gelesen.
- **Hotkey-Datei:** INI-Version 3, Aufbau wie in der Quelle.
- **Registrierungen:** unverändert gegenüber der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIHotkey.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006105C0` | 46 | vtable/String |
| 1 | `OnInit` | `0x006117B0` | 421 | vtable/String |
| 2 | `OnDestroy` | `0x006105F0` | 143 | vtable/String |
| 3 | `CBDisplayHotkeyDesc` | `0x00610680` | 84 | UI-Registrierung |
| 4 | `CBDisplayHotkeyCode` | `0x00611560` | 199 | UI-Registrierung |
| 5 | `CBFunctionHotkeyInputCode` | `0x00611630` | 106 | UI-Registrierung |
| 6 | `ReadDefaultHotkeyPack` | `0x00611960` | 698 | von Hand geprüft |
| 7 | `SetIniInfo` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 8 | `ReadCustomHotkeyIniFile` | `0x006106E0` | 512 | von Hand geprüft |
| 9 | `WriteCustomHotkeyIniFile` | `0x006108E0` | 373 | von Hand geprüft |
| 10 | `DoRegister` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 11 | `UpdateLastModified` | `0x00611250` | 173 | Aufrufgraph (geprüft) |
| 12 | `CBFunctionHotkeyOnOk` | `0x006116A0` | 104 | UI-Registrierung |
| 13 | `CBFunctionHotkeyOnDefault` | `0x00611300` | 149 | UI-Registrierung |
| 14 | `CBFunctionHotkeyOnCancle` | `0x006113A0` | 105 | UI-Registrierung |
| 15 | `CBEditControlHotkeyOverwriteCheck` | `0x00610A60` | 174 | von Hand geprüft |
| 16 | `CBFunctionHotkeyOnUIOpen` | `0x00611710` | 150 | UI-Registrierung |
| 17 | `ReMappingAllHotkeys` | `0x00611410` | 261 | Aufrufgraph (geprüft) |
| 18 | `ApplyHelpHotkeyContext` | `0x00610B10` | 1254 | Zeichenkette |
| 19 | `GetDefaultHotkey` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 20 | `GetDefaultHotkeyByIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 21 | `GetDefaultHotkeyIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 22 | `GetCurrentHotkey` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 23 | `GetCurrentHotkeyByIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 24 | `GetCurrentHotkeyIndex` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 25 | `ApplyPlayerMovementKeys` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 26 | `ScanCodeToVirtual` | `0x00611050` | 22 | von Hand geprüft |
| 27 | `FindCurrentHotkeyByDefault` | `0x00611000` | 65 | Aufrufgraph (geprüft) |
| 28 | `GetAsyncHotkeyState` | `0x00611520` | 57 | von Hand geprüft |
| 29 | `GetAsyncHotkeyState` | `0x006110B0` | 97 | von Hand geprüft |
| 30 | `RefreshUserData` | `0x00611120` | 243 | Aufrufgraph (geprüft) |
| 31 | `SortCompareFunc` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |

22 von 32 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006104E0`), `GetAsyncHotkeyState_006110b0` (`0x006110B0`), `~AgcmUIHotkey` (`0x00611220`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBB0` | `m_nHotkeyCount (≤ 256)` | `ReadCustomHotkeyIniFile`, `CBEditControlHotkeyOverwriteCheck` |
| `0xBB8 / 0xBBC` | `Ereignis-IDs „Überschreiben-Meldung“ / „UI öffnen“` | `OnInit` |
| `0xBC0` | `m_pIniFile (Pfad)` | `ReadCustomHotkeyIniFile` |
| `0xCC0` | `m_pDefaultPack[]` | `ReadDefaultHotkeyPack` |
| `0x14C0` | `m_pCurrentPack[]` | `GetCurrentHotkey…`, `CBEditControlHotkeyOverwriteCheck` |
| `0x1CC0` | `Indexliste für UserData` | `OnInit` |

## UI-Registrierung (OnInit 0x006117B0)

| Art | Name | Handler / Wert |
|---|---|---|
| UserData | `HotKey_ItemIndex` | 256 × 4 Byte (`+0x1CC0`, Indexliste 0–255) |
| Anzeige | `HotKey_DispItemDesc` | `CBDisplayHotkeyDesc` (`0x00610680`) |
| Anzeige | `HotKey_DispItemCode` | `CBDisplayHotkeyCode` (`0x00611560`) |
| Funktion | `HotKey_FuncInputCode` | `CBFunctionHotkeyInputCode` (`0x00611630`) |
| Funktion | `HotKey_FuncOnOk` | `CBFunctionHotkeyOnOk` (`0x006116A0`) |
| Funktion | `HotKey_FuncOnCancle` | `CBFunctionHotkeyOnCancle` (`0x006113A0`) |
| Funktion | `HotKey_FuncOnDefault` | `CBFunctionHotkeyOnDefault` (`0x00611300`) |
| Funktion | `HotKey_FuncOnUIOpen` | `CBFunctionHotkeyOnUIOpen` (`0x00611710`) |
| Ereignis | `Hotkey_EventOpenUI` | ID in `+0xBBC` |
| Ereignis | `Hotkey_EventDispOverwriteMsg` | ID in `+0xBB8` |

Namen und Anzahl stimmen mit der Quelle überein (1 UserData, 2 Anzeigen, 5 Funktionen, 2 Ereignisse).

## Hotkey-Datei (CustomHotkey)

`ReadCustomHotkeyIniFile` (`0x006106E0`) und `WriteCustomHotkeyIniFile` (`0x006108E0`) lesen/schreiben die benutzerdefinierten Hotkeys über den INI-Manager (Pfad `+0xBC0`): Abschnitt `CONFIG`, Schlüssel `VERSION` = **3** (`UI_HOTKEY_INI_VERSION`); je Hotkey ein Abschnitt `CustomHotkey<n>` mit `DefaultType`, `DefaultCode`, `CustomType` und `CustomCode`. Stimmt die Abschnittsanzahl nicht mit der Hotkey-Zahl + 1 oder die Version nicht überein, wird die Datei gelöscht (Lesefunktion). Hotkey-Zahl ≤ 256 (`+0xBB0`).
`ReadDefaultHotkeyPack` (`0x00611960`) baut die Standard-Hotkeys aus der Tabelle des [`AgcmUIManager2`](AgcmUIManager2.md) (Zeigerfeld `+0xCC0`, je 0x44 Byte).

## Tastenabfrage

`GetAsyncHotkeyState(type, vk)` (`0x006110B0`): Typ 1 = Shift, 2 = Strg, 3 = Alt; die Zustände kommen aus Engine-Variablen (`DAT_009A1D2C/30`, `…1D1C/20`, `…1D24/28`), danach `GetAsyncKeyState` (Bit 15). `ScanCodeToVirtual` (`0x00611050`) schlägt den Scancode in einer Tabelle mit 256 Einträgen bei `0x009522A8` nach; ungültige Scancodes ergeben 0. Beides entspricht der Quelle (die `MapVirtualKey`-Variante ist dort auskommentiert).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die kleinen Zugriffsfunktionen (`GetDefaultHotkey…`, `GetCurrentHotkey…`, `ApplyPlayerMovementKeys`, `SetIniInfo`, `DoRegister`, `SortCompareFunc`) sind im Binary eingefaltet oder haben keinen eindeutigen Anker.
- Die Standard-Hotkey-Tabelle selbst (Zuordnung Taste → Funktion) liegt in den UI-Daten, nicht im Code, und wurde nicht ausgewertet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 1, nicht im Client: 5, ohne Kandidat: 3.

Kandidaten ohne ausreichenden Beleg (nicht benannt): `DoRegister` (`0x00611C20`), `ApplyPlayerMovementKeys` (`0x00611C20`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIManager2`](AgcmUIManager2.md)
