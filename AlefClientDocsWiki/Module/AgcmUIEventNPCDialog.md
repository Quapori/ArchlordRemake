# AgcmUIEventNPCDialog (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIEventNPCDialog` (NPC-Dialog-Oberfläche: Schaltflächen je NPC-Funktion, NPC-Stimmen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIEventNPCDialog/AgcmUIEventNPCDialog.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 13 von 13 Quellmethoden sind zugeordnet; neu sind `OnAddModule`, `CBAriseNPCDialogUI`, `CBSelfUpdatePosition` und `CloseNPCDialog` (über Vtable, Registrierungsreihenfolge und Dekompilat).
- **Schließdistanz:** 150, wie in der Quelle.
- **NPC-Stimme:** nicht in China und Japan; Dateimuster `NP<TemplateID><Typ>.wav`.
- **UI:** zwei Funktionen, eine Anzeige (`NPCDialog_Button`), ein Benutzerdatum, zwei Ereignisse.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIEventNPCDialog.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006BE390` | 327 | ver |
| 1 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `AddEvent` | `0x006BD9D0` | 74 | Zeichenkette |
| 3 | `AddFunction` | `0x006BDE70` | 85 | Zeichenkette |
| 4 | `AddDisplay` | `0x006BDED0` | 33 | Zeichenkette |
| 5 | `AddUserData` | `0x006BDA20` | 45 | Zeichenkette |
| 6 | `CBAriseNPCDialogUI` | `0x006BDF00` | 846 | ver |
| 7 | `PlayNPCSound` | `0x006BDA50` | 368 | Zeichenkette |
| 8 | `CBNPCDialogDisplayDialog` | `0x006BDBC0` | 117 | UI-Registrierung |
| 9 | `CBDisplayNPCDialog` | `0x006BDC40` | 57 | UI-Registrierung |
| 10 | `CBNPCDailogSelectButton` | `0x006BDC80` | 186 | UI-Registrierung |
| 11 | `CBSelfUpdatePosition` | `0x006BDD40` | 136 | ver |
| 12 | `CloseNPCDialog` | `0x006BDDD0` | 42 | ver |

13 von 13 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006bd950` (`0x006BD950`), `~AgcmUIEventNPCDialog` (`0x006BDE00`), `ctor_or_dtor_006be250` (`0x006BE250`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBDC` | `ID des aktuell geöffneten Dialog-NPC` | `CBAriseNPCDialogUI`, `CloseNPCDialog` |
| `0xF84` | `Ereignis-ID `NPCDialog_CloseUI`` | `CBSelfUpdatePosition` |
| `0xF94` | `Flag „Dialogfenster offen“` | `CBSelfUpdatePosition`, `CloseNPCDialog` |
| `0xF9C` | `ID des zuletzt geöffneten Dialog-NPC (Abschiedston)` | `PlayNPCSound` |

## Umfang

Analysiert ist die Klasse `AgcmUIEventNPCDialog` (`AgcmUIEventNPCDialog.cpp`, 490 Zeilen, 13 Methoden). Die Hilfsklassen `CNpcText`, `CNpcTextManager` und `CRandomText` im selben Verzeichnis liegen im Binary davor (`0x006BD000`–`0x006BD950`) und wurden nicht abgeglichen.

## Vtable

Die Vtable steht bei `0x008D3D64`: Slot 1 ist `OnAddModule` (`0x006BE390`); Slot 2 und 6 zeigen auf den gemeinsamen `return TRUE`-Rumpf `0x0067AC90`. Die `OnDestroy` der Quelle (ruft `OnClearNpcDialogText`) ist im Binary offenbar zusammengefaltet oder eingebaut.

## Dialog öffnen (CBAriseNPCDialogUI, 0x006BDF00)

Wird über `SetCallbackAriseNPCDialogEvent` (`0x006DA540`) aufgerufen. Für jedes Ereignis des NPC mit Funktionsnummer 1 bis 0x29, außer 0x15 (`APDEVENT_FUNCTION_NPCDAILOG`), wird eine Schaltfläche mit einem UI-Text angelegt (Text-IDs `0x143`–`0x150`, `0x0E`, `0x211`, `0x261` u. a. je nach Funktion). Danach werden die Benutzerdaten aktualisiert und das Ereignis `NPCDialog_OpenUI` geworfen.

## Schließen bei Entfernung

`CBSelfUpdatePosition` (`0x006BDD40`) schließt das Dialogfenster (`NPCDialog_CloseUI`), sobald der XZ-Abstand zur Ereignisposition **≥ 150** wird (`> 0x95` im Binary; `AGCMUIEVENTNPCDIALOG_CLOSE_UI_DISTANCE` = 150 in der Quelle). `CloseNPCDialog` (`0x006BDDD0`) spielt den Abschied (`PlayNPCSound(1)`) und setzt das Offen-Flag zurück.

## NPC-Stimme (PlayNPCSound, 0x006BDA50)

Wie in der Quelle: nicht in China (1) und Japan (3). Dateiname `Sound\Effect\NP%03d%d.wav` (Template-ID < 1000) bzw. `NP%s%d.wav`; eine Sperre verhindert, dass derselbe NPC mit demselben Typ erneut spielt, solange der vorige Ton läuft.

## Callback-Registrierung in OnAddModule (0x006BE390)

Zuerst `SetCallbackAriseNPCDialogEvent`, danach `SetCallbackSelfUpdatePosition`, dann `AddEvent`, `AddFunction`, `AddDisplay`, `AddUserData` in dieser Reihenfolge (wie in der Quelle).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006BDE70`, `0x006BDED0`, `0x006BDA20`, `0x006BD9D0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (2)

| Name | Id | Handler |
|---|---:|---|
| `NPCDialog_DisplayDialog` |  | `CBNPCDialogDisplayDialog` |
| `NPCDialog_SelectButton` |  | `CBNPCDailogSelectButton` |

**Anzeige** (1)

| Name | Id | Handler |
|---|---:|---|
| `NPCDialog_Button` | 0 | `CBDisplayNPCDialog` |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `NPCDialog_Buttons` |  | – |

**Ereignis** (2)

| Name | Id | Handler |
|---|---:|---|
| `NPCDialog_OpenUI` | 0 | – |
| `NPCDialog_CloseUI` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`CBSelfUpdatePosition`, `CloseNPCDialog`, `PlayNPCSound`, `CBAriseNPCDialogUI` in Grundzügen).

## Grenzen

- `CBAriseNPCDialogUI` wurde nur in der Struktur und der Text-ID-Tabelle gelesen, nicht jede Funktion einzeln gegen die Quelle.
- Die Hilfsklassen `CNpcText`, `CNpcTextManager`, `CRandomText` sind nicht abgeglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`NPC_Trade_Dialog`](NPC_Trade_Dialog.md)
