# AgcmUIProduct (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse `AgcmUIProduct` (Herstellungsfenster (Kochen, Alchemie)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIProduct/AgcmUIProduct.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 34 von 40 Quellmethoden sind zugeordnet; neu sind `AddEvent`, `Open`, `CastAnimation`, `ClearGrid`, `IsComposable`, `AddGridItem`, `DisplaySourceItem`, `RefreshAll`, `OnPostResult` und `OnResult` (`0x006A3B80`, über die Weiche `0x006A2060` zusammen mit der Schwesterfunktion von [`AgcmUIProductSkill`](AgcmUIProductSkill.md) gefunden).
- **Hinweis:** `AgcmUIEventProduct` existiert nicht; gemeint ist dieses Modul `AgcmUIProduct`.
- **UI:** 6 Funktionen, 6 Anzeigen, 1 Boolean – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIProduct.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x006A2670` | 82 | vtable/String |
| 1 | `OnDestroy` | `0x006A2E80` | 33 | vtable/String |
| 2 | `OnAddModule` | `0x006A4080` | 557 | vtable/String |
| 3 | `AddEvent` | `0x006A26D0` | 67 | ver |
| 4 | `AddFunction` | `0x006A3A80` | 243 | Zeichenkette |
| 5 | `AddDisplay` | `0x006A3690` | 191 | Zeichenkette |
| 6 | `AddUserData` | `0x006A2720` | 199 | Zeichenkette |
| 7 | `AddBoolean` | `0x006A2EB0` | 31 | Zeichenkette |
| 8 | `Open` | `0x006A27F0` | 126 | ver |
| 9 | `CBOpenWindow` | `0x006A3930` | 61 | UI-Registrierung |
| 10 | `CBOpenTooltip` | `0x006A2ED0` | 209 | UI-Registrierung |
| 11 | `CBCloseTooltip` | `0x006A2870` | 45 | UI-Registrierung |
| 12 | `CBClickListItem` | `0x006A3970` | 139 | UI-Registrierung |
| 13 | `CBClickOkButton` | `0x006A3750` | 23 | UI-Registrierung |
| 14 | `CBCloseWindow` | `0x006A28A0` | 67 | UI-Registrierung |
| 15 | `CBDisplayTitle` | `0x006A28F0` | 71 | UI-Registrierung |
| 16 | `CBDisplaySelectEdit` | `0x006A2FB0` | 256 | UI-Registrierung |
| 17 | `CBDisplayMakeOk` | `0x006A30B0` | 55 | UI-Registrierung |
| 18 | `CBDisplayMakeCancel` | `0x006A30F0` | 55 | UI-Registrierung |
| 19 | `CBDisplaySelectList` | `0x006A3130` | 147 | UI-Registrierung |
| 20 | `CBDisplayMakeEdit` | `0x006A31D0` | 538 | UI-Registrierung |
| 21 | `CBAfterCooldown` | `0x006A2940` | 82 | Callback-Registrierung |
| 22 | `OnMake` | `0x006A33F0` | 445 | Zeichenkette |
| 23 | `CastAnimation` | `0x006A29A0` | 291 | ver |
| 24 | `OnResult` | `0x006A3B80` | 158 | ver |
| 25 | `OnPostResult` | `0x006A3A00` | 117 | ver |
| 26 | `DisplaySourceItem` | `0x006A3770` | 337 | ver |
| 27 | `AddGridItem` | `0x006A35B0` | 211 | ver |
| 28 | `SetGridItemAttachedTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `RefreshSourceItemGrid` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `ClearGrid` | `0x006A2AD0` | 137 | ver |
| 31 | `CBMoveItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 32 | `CBIsActiveComposeButton` | `0x006A2B60` | 128 | UI-Registrierung |
| 33 | `CBKeydownESC` | `0x006A2BE0` | 31 | Callback-Registrierung |
| 34 | `CBCloseAllUIToolTip` | `0x006A2C00` | 26 | Callback-Registrierung |
| 35 | `RefreshAll` | `0x006A38D0` | 92 | ver |
| 36 | `IsComposable` | `0x006A2C20` | 70 | ver |
| 37 | `GetComposeByIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 38 | `GetMessageTxt` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 39 | `GetMessageTxt` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

34 von 40 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006a2610` (`0x006A2610`), `ctor_or_dtor_006a2c70` (`0x006A2C70`), `~AgcmUIProduct` (`0x006A2E60`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x29A8 / 0x29AC` | `Kategorie / Fertigkeits-ID` | `Open` |
| `0x29B0` | `Rezeptliste (100 × 4 Byte)` | `Open` |
| `0x2B40` | `Anzahl Rezepte` | `Open` |
| `0x2B50` | `Flag „Fenster offen“` | `Open` |
| `0x2978` | `Ereignis „Fenster öffnen“` | `Open` |

## Umfang

Das Modul `AgcmUIProduct` (Herstellen/Kochen/Alchemie) besteht in der Quelle aus zwei Dateien: `AgcmUIProduct.cpp` (40 Methoden, dieser Bericht) und `AgcmUIProductSkill.cpp` (Klasse `AgcmUIProductSkill`, nicht abgeglichen). Ein Modul `AgcmUIEventProduct` gibt es in der Quelle nicht. Die Produktions-Ereignisse liegen in [`AgcmEventProduct`](AgcmEventProduct.md).

## Vtable

Vtable bei `0x008CF694`: Slot 0 Destruktor `0x006A2E60`, 1 `OnAddModule` (`0x006A4080`), 2 `OnInit` (`0x006A2670`), 7 `OnDestroy` (`0x006A2E80`), 6 `return TRUE`-Rumpf `0x0067AC90`.

## Fenster öffnen (Open, 0x006A27F0)

`Open(Kategorie, Fertigkeits-ID)` merkt beide Werte, leert die Rezeptliste (100 Einträge = 400 Byte, `AGCMUIPRODUCT_MAX_LIST`), füllt sie über [`AgpmProduct`](AgpmProduct.md):GetComposeList` für den Self-Character und wirft das Ereignis „Fenster öffnen“, Flag „offen“ gesetzt. Entspricht der Quelle.

## Rezepte und Gitter

`IsComposable` (`0x006A2C20`) prüft über `AgpmProduct::IsValidStatus`, ob der Charakter das Rezept mit seiner Fertigkeit herstellen darf; `GetComposeByIndex` ist darin eingebaut. `DisplaySourceItem` (`0x006A3770`) leert das Gitter (`ClearGrid`, `0x006A2AD0`), füllt es mit den Zutaten (`AddGridItem`, `0x006A35B0`) und `RefreshAll` (`0x006A38D0`) aktualisiert alle Benutzerdaten und die Zutatenanzeige. `OnPostResult` (`0x006A3A00`) gibt die Sperre frei, setzt eine nicht mehr herstellbare Auswahl zurück und ruft `RefreshAll`.

## Herstellen (OnMake, 0x006A33F0)

Bricht ab, wenn gerade eine Herstellung läuft oder kein Self-Character vorhanden ist; prüft, ob der aktive Titel die Anforderung des Rezepts erfüllt – wenn nicht, erscheint der UI-Text `NotActivateRequireTitle` im OK-Dialog. `CastAnimation` (`0x006A29A0`) spielt die Fertigkeitsanimation und liefert ihre Dauer.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006A3A80`, `0x006A3690`, `0x006A2720`, `0x006A2EB0`, `0x006A26D0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (6)

| Name | Id | Handler |
|---|---:|---|
| `COMPOSE_OPEN` |  | `CBOpenWindow` |
| `COMPOSE_LIST_ITEM_CLICK` |  | `CBClickListItem` |
| `COMPOSE_TOOLTIP_OPEN` |  | `CBOpenTooltip` |
| `COMPOSE_TOOLTIP_CLOSE` |  | `CBCloseTooltip` |
| `COMPOSE_OKBUTTON_CLICK` |  | `CBClickOkButton` |
| `COMPOSE_CLOSE` |  | `CBCloseWindow` |

**Anzeige** (6)

| Name | Id | Handler |
|---|---:|---|
| `COMPOSE_DISP_TITLE` | 0 | `CBDisplayTitle` |
| `COMPOSE_DISP_SEL_EDIT` | 0 | `CBDisplaySelectEdit` |
| `COMPOSE_DISP_SEL_LIST` | 0 | `CBDisplaySelectList` |
| `COMPOSE_DISP_MAKE_EDIT` | 0 | `CBDisplayMakeEdit` |
| `COMPOSE_DISP_MAKE_OK` | 0 | `CBDisplayMakeOk` |
| `COMPOSE_DISP_MAKE_CANCEL` | 0 | `CBDisplayMakeCancel` |

**UserData** (5)

| Name | Id | Handler |
|---|---:|---|
| `COMPOSE_UD_DUMMY` | 0 | – |
| `COMPOSE_UD_SEL_LIST` |  | – |
| `COMPOSE_UD_MAKE_EDIT` | 0 | – |
| `COMPOSE_UD_MAKE_GRID` |  | – |
| `COMPOSE_UD_COMPOSE_BTN` |  | – |

**Boolean** (1)

| Name | Id | Handler |
|---|---:|---|
| `COMPOSE_ACTIVE_COMPOSE_BTN` |  | `CBIsActiveComposeButton` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`Open`).

## Grenzen

- `CBMoveItem`, `RefreshSourceItemGrid`, `SetGridItemAttachedTexture`, `GetComposeByIndex`, `RefreshAll`-Teile und die beiden `GetMessageTxt` konnten keiner eigenen Funktion zugeordnet werden (teils eingebaut, teils ohne Anker). `CBMoveItem` wird von den sechs angemeldeten UI-Funktionen nicht benutzt und ist vermutlich entfernt.
- Die Zuordnung der neun neuen Funktionen stützt sich auf Aufrufer und Aufgerufene; nur `Open` wurde Zeile für Zeile gelesen.
- Die Klasse `AgcmUIProductSkill` (1668 Zeilen) wurde nicht analysiert.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, ohne Kandidat: 5.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventProduct`](AgcmEventProduct.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md), [`AgpmProduct`](AgpmProduct.md)
- **Erwähnt in:** [`AgcmProduct`](AgcmProduct.md), [`AgcmProductMed`](AgcmProductMed.md), [`AgcmUIProductSkill`](AgcmUIProductSkill.md)
