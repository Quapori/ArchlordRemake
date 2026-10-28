# AgcmUISplitItem (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUISplitItem` (Mengen-Eingabefenster: Stapel teilen, Preis und Gebühr beim Verkauf) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUISplitItem/AgcmUISplitItem.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 26 von 26 Quellmethoden sind zugeordnet; neu sind `SetCondition` und `OpenSplitItemUI`; `OnInit` und `AddDisplay` stehen als gemeinsamer Rumpf.
- **Gebühr:** 3 % Registrierungsgebühr beim Verkauf, im Binary als `× 3 / 100` bestätigt.
- **UI:** 18 Funktionen, 1 Benutzerdatum, 4 Ereignisse – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUISplitItem.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006D9F40` | 172 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `AddDisplay` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 3 | `AddUserData` | `0x006D8F50` | 49 | Zeichenkette |
| 4 | `AddFunction` | `0x006D9C20` | 798 | Zeichenkette |
| 5 | `AddEvent` | `0x006D8F90` | 134 | Zeichenkette |
| 6 | `SetCondition` | `0x006D9020` | 95 | ver |
| 7 | `OpenSplitItemUI` | `0x006D9080` | 102 | ver |
| 8 | `CBButtonOK` | `0x006D90F0` | 465 | UI-Registrierung |
| 9 | `CBButtonCancel` | `0x006D92D0` | 25 | UI-Registrierung |
| 10 | `CBButtonUp` | `0x006D92F0` | 127 | UI-Registrierung |
| 11 | `CBButtonDown` | `0x006D9370` | 127 | UI-Registrierung |
| 12 | `CBButtonKey0` | `0x006D93F0` | 129 | UI-Registrierung |
| 13 | `CBButtonKey1` | `0x006D9480` | 131 | UI-Registrierung |
| 14 | `CBButtonKey2` | `0x006D9510` | 131 | UI-Registrierung |
| 15 | `CBButtonKey3` | `0x006D95A0` | 131 | UI-Registrierung |
| 16 | `CBButtonKey4` | `0x006D9630` | 131 | UI-Registrierung |
| 17 | `CBButtonKey5` | `0x006D96C0` | 131 | UI-Registrierung |
| 18 | `CBButtonKey6` | `0x006D9750` | 131 | UI-Registrierung |
| 19 | `CBButtonKey7` | `0x006D97E0` | 131 | UI-Registrierung |
| 20 | `CBButtonKey8` | `0x006D9870` | 131 | UI-Registrierung |
| 21 | `CBButtonKey9` | `0x006D9900` | 131 | UI-Registrierung |
| 22 | `CBButtonKeyClear` | `0x006D9990` | 114 | UI-Registrierung |
| 23 | `CBButtonKeyBack` | `0x006D9A10` | 145 | UI-Registrierung |
| 24 | `CBGetStackCountEditControl` | `0x006D9AB0` | 134 | UI-Registrierung |
| 25 | `CBChangeTitleEditControl` | `0x006D9B40` | 163 | UI-Registrierung |

26 von 26 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006D8E80`), `~AgcmUISplitItem` (`0x006D9BF0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBAC / 0xBB0 / 0xBB4` | `Mindest- / Höchst- / aktuelle Menge` | `CBButtonOK` |
| `0xBB8` | `Modal-Flag` | `SetCondition` |
| `0xBBC` | `Titel-Bedingung (`m_eTitleCondition`; 0 = Stapel teilen)` | `SetCondition`, `CBButtonOK` |
| `0xBC0` | `Status (Parameter an den Rückruf)` | `SetCondition` |
| `0xC48 / 0xC4C` | `Rückruf / Klassenzeiger` | `SetCondition`, `CBButtonOK` |
| `0xC54 / 0xC58 / 0xC5C / 0xC60` | `Benutzerdatum und Ereignisse (Titel, Mengenfeld, Öffnen, Schließen)` | `OpenSplitItemUI` |

## Vtable

Vtable bei `0x008D7E4C`: Slot 0 Destruktor `0x006D9BF0`, 1 `OnAddModule` (`0x006D9F40`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`; `AddDisplay` der Quelle gibt nur TRUE zurück).

## Bedingung setzen und öffnen

`SetCondition` (`0x006D9020`) speichert nur Rückruf, Klassenzeiger, Mindest-/Höchst-/Startmenge, Modal-Flag, Titel-Bedingung und Status (neun Werte, keine Aufrufe); `OpenSplitItemUI` (`0x006D9080`) aktualisiert die Benutzerdaten und wirft die drei Ereignisse „Titel ändern“, „Mengenfeld holen“ und „Fenster öffnen“. Beide werden von den Verschiebe-Callbacks von [`AgcmUIItem`](AgcmUIItem.md) (`CBInventoryMoveItem`, `CBSubInventoryMoveItem`, …) aufgerufen.

## Bestätigen (CBButtonOK, 0x006D90F0)

Liest die Menge aus dem Eingabefeld, begrenzt sie auf Mindest- und Höchstmenge und ruft den hinterlegten Rückruf. Ist die Titel-Bedingung nicht „Gegenstand teilen“ (also Verkauf in die Verkaufsbox), werden **3 %** Registrierungsgebühr berechnet (`menge × 3 / 100`; `AGPMITEM_REGISTER_FEE_RATIO` = 0,03), eine Bestätigungsfrage mit Menge und Gebühr gezeigt, und bei zu wenig Geld erscheint `NotEnoughCharge` und der Titel wechselt auf „zu wenig Geld“. Danach wird das Fenster geschlossen. Entspricht der Quelle.

## Tasten

Die Ziffernknöpfe `CBButtonKey0`…`CBButtonKey9` (je `0x006D93F0` + 0x90 Schritte), `CBButtonKeyClear`, `CBButtonKeyBack` (Menge durch 10, nicht unter Mindestmenge) sowie `CBButtonUp`/`CBButtonDown` (±1 im Bereich) ändern die Menge und das Eingabefeld. `CBChangeTitleEditControl` setzt den Titeltext je nach Bedingung (Teilen: `Item_Split_Stack_Count`, Verkauf: Preiseingabe, sonst „zu wenig Geld“).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006D9C20`, `0x006D8F50`, `0x006D8F90`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (18)

| Name | Id | Handler |
|---|---:|---|
| `SplitItem_ButtonOK` |  | `CBButtonOK` |
| `SplitItem_ButtonCancel` |  | `CBButtonCancel` |
| `SplitItem_ButtonUp` |  | `CBButtonUp` |
| `SplitItem_ButtonDown` |  | `CBButtonDown` |
| `SplitItem_ButtonKey0` |  | `CBButtonKey0` |
| `SplitItem_ButtonKey1` |  | `CBButtonKey1` |
| `SplitItem_ButtonKey2` |  | `CBButtonKey2` |
| `SplitItem_ButtonKey3` |  | `CBButtonKey3` |
| `SplitItem_ButtonKey4` |  | `CBButtonKey4` |
| `SplitItem_ButtonKey5` |  | `CBButtonKey5` |
| `SplitItem_ButtonKey6` |  | `CBButtonKey6` |
| `SplitItem_ButtonKey7` |  | `CBButtonKey7` |
| `SplitItem_ButtonKey8` |  | `CBButtonKey8` |
| `SplitItem_ButtonKey9` |  | `CBButtonKey9` |
| `SplitItem_ButtonKeyClear` |  | `CBButtonKeyClear` |
| `SplitItem_ButtonKeyBack` |  | `CBButtonKeyBack` |
| `SplitItem_GetStackCountEditControl` |  | `CBGetStackCountEditControl` |
| `SplitItem_ChangeTitleEditControl` |  | `CBChangeTitleEditControl` |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `SplitItemDummy` |  | – |

**Ereignis** (4)

| Name | Id | Handler |
|---|---:|---|
| `SplitItem_OpenUI` | 0 | – |
| `SplitItem_GetStackCountControl` | 0 | – |
| `SplitItem_ChangeTitle` | 0 | – |
| `SplitItem_CloseUI` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`CBButtonOK`, `SetCondition`, `OpenSplitItemUI`).

## Grenzen

- Die Zifferntasten sind 16 gleichgebaute Funktionen (je 23 Quellzeilen); ihre Zuordnung stützt sich auf die Registrierungsreihenfolge, nicht auf einzeln gelesene Inhalte.
- Die Offsets der Mengen- und Bedingungswerte stammen aus der Parameterreihenfolge von `SetCondition` und der Verwendung in `CBButtonOK`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIItem`](AgcmUIItem.md)
