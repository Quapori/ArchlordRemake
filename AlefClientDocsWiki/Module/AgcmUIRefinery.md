# AgcmUIRefinery (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIRefinery` (Veredelungs-Fenster (Gegenstände zu neuen Gegenständen verarbeiten)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIRefinery/AgcmUIRefinery.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 36 von 44 Quellmethoden sind einer Adresse zugeordnet; neu sind `GetMessageTxt`, `InitializeGrid`, `RefreshSourceGrid`, `Reset`, `AddItemToResultGrid`, `OnSuccess`, `OnMoveItem`, `OnResult`, `CBRefine` und `AddEvent`. Die übrigen acht sind in ihre Aufrufer eingebaut.
- **Ablauf:** zehn Quellplätze (1 × 2 × 5), ein Ergebnisplatz; Veredeln fragt nach dem Preis, zieht ihn ab, wartet 5000 ms und sendet dann `SendPacketRefineItem`.
- **UI:** 8 Funktionen, 4 Anzeigen, 8 Benutzerdaten, 7 Ereignisse (Ereignisnamen in Schleife registriert) – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIRefinery.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x006A09F0` | 49 | vtable/String |
| 1 | `OnDestroy` | `0x006A1190` | 85 | vtable/String |
| 2 | `OnAddModule` | `0x006A1CE0` | 686 | vtable/String |
| 3 | `Open` | – | | in CBGrant eingebaut |
| 4 | `OnResult` | `0x006A18A0` | 204 | manual |
| 5 | `OnSuccess` | `0x006A11F0` | 342 | manual |
| 6 | `OnMoveItem` | `0x006A1350` | 470 | manual |
| 7 | `CBOpenWindow` | `0x006A0510` | 125 | UI-Registrierung |
| 8 | `CBCloseWindow` | `0x006A1530` | 79 | UI-Registrierung |
| 9 | `CBClickRefineButton` | `0x006A1990` | 138 | UI-Registrierung |
| 10 | `CBRefine` | `0x006A1A20` | 230 | manual |
| 11 | `CBClickResetButton` | `0x006A1580` | 40 | UI-Registrierung |
| 12 | `CBMoveItem` | `0x006A15B0` | 164 | UI-Registrierung |
| 13 | `CBMoveEndItem` | `0x006A1660` | 268 | UI-Registrierung |
| 14 | `CBOpenTooltip` | `0x006A0590` | 93 | UI-Registrierung |
| 15 | `CBCloseTooltip` | `0x006A05F0` | 33 | UI-Registrierung |
| 16 | `CBDisplayMainEdit` | `0x006A0A30` | 111 | UI-Registrierung |
| 17 | `CBDisplaySubTitle` | `0x006A0AA0` | 71 | UI-Registrierung |
| 18 | `CBDisplaySubNotify` | `0x006A0AF0` | 194 | UI-Registrierung |
| 19 | `CBDisplayPrice` | `0x006A0620` | 107 | UI-Registrierung |
| 20 | `CBAfterCooldown` | `0x006A0BC0` | 110 | Callback-Registrierung |
| 21 | `CBRefineResult` | `0x006A1B10` | 32 | Callback-Registrierung |
| 22 | `CBGrant` | `0x006A1780` | 96 | Callback-Registrierung |
| 23 | `CBSelfUpdatePosition` | `0x006A17E0` | 149 | Callback-Registrierung |
| 24 | `CBKeydownESC` | `0x006A1880` | 24 | Callback-Registrierung |
| 25 | `CBCloseAllUIToolTip` | `0x006A0690` | 26 | Callback-Registrierung |
| 26 | `Reset` | `0x006A0C30` | 334 | manual |
| 27 | `GetMessageTxt` | `0x006A06B0` | 213 | manual |
| 28 | `AddEvent` | `0x006A1B30` | 95 | manual |
| 29 | `AddFunction` | `0x006A1B90` | 327 | Zeichenkette |
| 30 | `AddDisplay` | `0x006A0D80` | 131 | Zeichenkette |
| 31 | `AddUserData` | `0x006A0790` | 318 | Zeichenkette |
| 32 | `InitializeGrid` | `0x006A08D0` | 99 | manual |
| 33 | `DestroyGrid` | – | | in OnDestroy eingebaut |
| 34 | `AddItemToSourceGrid` | – | | sechs Zeilen, in OnMoveItem eingebaut |
| 35 | `RemoveItemFromSourceGrid` | – | | fünf Zeilen, eingebaut |
| 36 | `AddItemToResultGrid` | `0x006A0E10` | 182 | manual |
| 37 | `RefreshSourceGrid` | `0x006A0940` | 45 | manual |
| 38 | `RefreshResultGrid` | – | | eingebaut (OnSuccess, Reset) |
| 39 | `SetGridItemAttachedTexture` | – | | in AddItemToResultGrid eingebaut |
| 40 | `ClearSourceGrid` | – | | in Reset eingebaut |
| 41 | `ClearResultGrid` | – | | in Reset eingebaut |
| 42 | `CBRemoveItemFromInventory` | `0x006A0970` | 93 | Callback-Registrierung |
| 43 | `CBCheckUseItem` | `0x006A0ED0` | 68 | Callback-Registrierung |

36 von 44 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006A04B0`), `~AgcmUIRefinery` (`0x006A09D0`), `AgcmUIRefinery` (`0x006A0F20`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x2930 / 0x2954` | `Quellgitter / Ergebnisgitter (`AgpdGrid`)` | `InitializeGrid`, `Reset` |
| `0x2978` | `Gitterfeld des Ergebnisses` | `InitializeGrid`, `AddItemToResultGrid`, `OnDestroy` |
| `0x297C…` | `Ereignis-IDs (`REFINE_EVENT_OPEN` … `_END`), `MONEYMSGBOX` bei `+0x2994`` | `AddEvent` |
| `0x29C0` | `Kategorie (100 Stein / 200 Skelett / 400 Gegenstand)` | `GetMessageTxt` |
| `0x29C4…0x29E8` | `Liste der zehn Quellgegenstände (`m_pSources`)` | `OnMoveItem`, `CBCheckUseItem`, `CBAfterCooldown` |
| `0x29F0 / 0x29F4` | `Ergebniscode / Meldungsnummer (`m_eNotifyMsg`)` | `OnResult`, `OnMoveItem` |
| `0x29FC` | `Haltesperre (`m_bHold`)` | `CBRefine`, `CBClickRefineButton` |
| `0x2A00` | `Flag „Fenster offen“` | `CBSelfUpdatePosition` |
| `0x2A04…0x2A0C` | `Öffnungsposition (`m_stOpenPos`)` | `CBGrant` |
| `0x2A10` | `Abklingzeit-ID` | `CBRefine` |

## Vtable

Vtable bei `0x008CF38C`: Slot 0 Destruktor `0x006A09D0`, 1 `OnAddModule` (`0x006A1CE0`), 2 `OnInit` (`0x006A09F0`), 3–5 gemeinsamer Rumpf `0x0067FAB0` (u. a. `OnIdle`), 6 `return TRUE`-Rumpf `0x0067AC90`, 7 `OnDestroy` (`0x006A1190`).

## Registrierung (OnAddModule, 0x006A1CE0)

Holt 14 Module (u. a. [`AgpmRefinery`](AgpmRefinery.md), [`AgcmRefinery`](AgcmRefinery.md), [`AgcmEventRefinery`](AgcmEventRefinery.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUICooldown`](AgcmUICooldown.md)); Pflicht sind elf davon, optional sind [`AgcmUIMain`](AgcmUIMain.md), `AgcmUIItem` und `AgcmUICooldown`. Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgcmEventRefinery`: Ereignis gewährt | `CBGrant` | `0x006A1780` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x006A17E0` |
| `AgpmRefinery`: Ergebnis | `CBRefineResult` | `0x006A1B10` |
| `AgcmUIMain`: ESC | `CBKeydownESC` | `0x006A1880` |
| `AgcmUIMain`: alle Tooltips schließen | `CBCloseAllUIToolTip` | `0x006A0690` |
| [`AgpmItem`](AgpmItem.md): aus Inventar entfernt | `CBRemoveItemFromInventory` | `0x006A0970` |
| `AgpmItem`: aus Cash-Inventar entfernt | `CBRemoveItemFromInventory` | `0x006A0970` |
| [`AgcmItem`](AgcmItem.md): Gegenstand-Benutzung prüfen | `CBCheckUseItem` | `0x006A0ED0` |
| `AgcmUICooldown`: Abklingzeit beendet | `CBAfterCooldown` | `0x006A0BC0` |

Danach `AddEvent` (`0x006A1B30`), `AddFunction` (`0x006A1B90`), `AddDisplay` (`0x006A0D80`) und `AddUserData` (`0x006A0790`).

## Initialisierung (OnInit, InitializeGrid)

`OnInit` (`0x006A09F0`) setzt den Tooltip auf „immer oben“, hängt ihn an [`AgcmUIManager2`](AgcmUIManager2.md) und blendet ihn aus; danach `InitializeGrid` (`0x006A08D0`): Quellgitter 1 × 2 × 5 (zehn Plätze, `AGPMREFINERY_MAX_GRID`), Ergebnisgitter 1 × 1 × 1, beide mit Typ „Gegenstand“, plus ein Gitterfeld für das Ergebnis (`+0x2978`). `OnDestroy` (`0x006A1190`) ruft `Reset(FALSE)`, löscht das Ergebnisfeld und entfernt beide Gitter; `DestroyGrid` ist dort eingebaut.

## Meldungen (GetMessageTxt, 0x006A06B0)

Der Haupttext (`REFINE_MAIN_EDIT`) kommt aus der Stringtabelle (`STI_REFINERY_INTRO`, UI-Text `0x1C1`); alle anderen Meldungen werden aus dem Schlüssel plus Kategorie-Endung gebildet: 100 → `_STONE`, 200 → `_SKEL`, 400 → `_ITEM`, sonst leer (15 Meldungsnamen von `REFINE_SUB_TITLE` bis `REFINE_UNNEXT`). Das stimmt mit der Quelle überein.

## Veredeln (CBClickRefineButton → CBRefine → CBAfterCooldown)

`CBClickRefineButton` (`0x006A1990`) tut nichts, solange gehalten wird (`+0x29FC`). Ist noch kein Ergebnis gesetzt, prüft es `AgpmRefinery::IsValidStatusRefine` (`0x005293A0`) mit den bis zu zehn Quellgegenständen: bei Erfolg wird das Ereignis `REFINE_EVENT_MONEYMSGBOX` geworfen, sonst `OnResult(Fehlercode, 0)`; danach folgt in beiden Fehlerfällen `Reset`.
`CBRefine` (`0x006A1A20`, als Rückruf des Ereignisses angemeldet) wird nach der Geldfrage mit „Ja“ aufgerufen: Es setzt „gehalten“, zieht den Preis (`m_pAgpdResultItem->m_lPrice`, Ergebnis-Gegenstand) ab, bei Geldmangel erscheint die Meldung 6 (`REFINE_INSMONEY`). Sonst startet es eine Abklingzeit von **5000 ms** mit dem UI-Text `0x1C2` (`STI_REFINERYING`).
Nach der Abklingzeit sendet `CBAfterCooldown` (`0x006A0BC0`) `AgcmRefinery::SendPacketRefineItem` mit Charakter-ID, Vorlagen-ID 0 und den zehn Gegenstands-IDs (0 für leere Plätze). Das Ergebnis kommt über `CBRefineResult` → `OnResult`.

## Ergebnis (OnResult, OnSuccess)

`OnResult` (`0x006A18A0`) speichert den Code, hebt die Haltesperre auf und verzweigt über die sechs Codes: 0 Erfolg (→ `OnSuccess`), 1–5 Fehler (Meldungen „zu wenig Gegenstände“, „anderer Gegenstand“, „zu wenig Geld“, „Inventar voll“); jede Fehlermeldung geht als Systemnachricht in den Chat. `OnSuccess` (`0x006A11F0`) sucht die Ergebnisvorlage, setzt das Fenster zurück, trägt den Gegenstand (Anzahl 1) ins Ergebnisgitter ein, setzt die Meldung „Erfolg“ (Name des Gegenstands eingesetzt, Systemnachricht) und wirft `REFINE_EVENT_SUCCESS`.

## Gegenstände ablegen (OnMoveItem, 0x006A1350)

Wie in der Quelle: bei vorhandenem Ergebnis zuerst `Reset`; nur Gegenstände aus Inventar (Status 2) oder Cash-Inventar (Status 0x33) sind erlaubt; ein bereits abgelegter Gegenstand wird abgewiesen (Schleife über die zehn Plätze); ist das Gitter voll, erscheint die Meldung 7 („kann nicht geladen werden“); der Platz muss frei sein. Danach wird der Gegenstand ins Quellgitter eingetragen und in die Liste auf Platz `Zeile × 5 + Spalte` gelegt.

## Weitere Funktionen

`CBSelfUpdatePosition` schließt das Fenster ab 150 Einheiten Abstand (nur wenn offen); `CBGrant` merkt die Position (`+0x2A04…`), setzt zurück und wirft `REFINE_EVENT_OPEN` (`Open` ist eingebaut). `CBCheckUseItem` verbietet das Benutzen eines Gegenstands, der gerade im Quellgitter liegt. `CBRemoveItemFromInventory` entfernt das Gitterfeld aus dem Quellgitter und aktualisiert es.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006A1B90`, `0x006A0D80`, `0x006A0790`, `0x006A1B30`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (8)

| Name | Id | Handler |
|---|---:|---|
| `REFINE_OPEN` |  | `CBOpenWindow` |
| `REFINE_CLOSE` |  | `CBCloseWindow` |
| `REFINE_TOOLTIP_OPEN` |  | `CBOpenTooltip` |
| `REFINE_TOOLTIP_CLOSE` |  | `CBCloseTooltip` |
| `REFINE_MOVE_ITEM` |  | `CBMoveItem` |
| `REFINE_MOVEEND_ITEM` |  | `CBMoveEndItem` |
| `REFINE_REFINEBTN_CLICK` |  | `CBClickRefineButton` |
| `REFINE_RESETBTN_CLICK` |  | `CBClickResetButton` |

**Anzeige** (4)

| Name | Id | Handler |
|---|---:|---|
| `REFINE_DISP_MAIN_EDIT` | 0 | `CBDisplayMainEdit` |
| `REFINE_DISP_SUB_TITLE` | 0 | `CBDisplaySubTitle` |
| `REFINE_DISP_SUB_NOTIFY` | 0 | `CBDisplaySubNotify` |
| `REFINE_DISP_PRICE` | 0 | `CBDisplayPrice` |

**UserData** (8)

| Name | Id | Handler |
|---|---:|---|
| `REFINE_ACTIVE_TAB` |  | – |
| `REFINE_UD_MAIN_EDIT` | 0 | – |
| `REFINE_UD_SUB_TITLE` | 0 | – |
| `REFINE_UD_SUB_NOTIFY` | 0 | – |
| `REFINE_UD_PRICE` | 0 | – |
| `REFINE_UD_SOURCE_GRID` |  | – |
| `REFINE_UD_RESULT_GRID` |  | – |
| `REFINE_UD_REFINE_BTN` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`GetMessageTxt`, `InitializeGrid`, `OnResult`, `OnSuccess`, `OnMoveItem`, `CBRefine`, `CBClickRefineButton`, `CBSelfUpdatePosition`, Registrierungsreihenfolge).

## Grenzen

- `Open` (11 Zeilen) und die kleinen Gitterfunktionen sind eingebaut und haben keine eigene Adresse.
- `CBRefine` wurde über die Aufrufe (Abzug, Abklingzeit 5000 ms, Text `0x1C2`) und das Ereignis zugeordnet; der Geld-Abzug erfolgt im Binary über `0x0058A300` mit den Rückgabewerten der Quelle, die Verzweigung bei Geldmangel ist dort teilweise in `OnResult` eingebaut.
- `AddUserData` (`0x006A0790`, 318 Byte) wurde nur über die Registrierungstabelle geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, nicht als eigene Funktion: 3, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventRefinery`](AgcmEventRefinery.md), [`AgcmItem`](AgcmItem.md), [`AgcmRefinery`](AgcmRefinery.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmItem`](AgpmItem.md), [`AgpmRefinery`](AgpmRefinery.md)
