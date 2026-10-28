# AgcmUICustomizing (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUICustomizing` (Charakter-Anpassung: Frisur und Gesicht wählen, bezahlen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUICustomizing/AgcmUICustomizing.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 37 von 37 Quellmethoden sind zugeordnet; neu sind `InitializeList`, `PriceWithTax`, `GetInvenMoney`, `IsEnoughCost`, `SetFaceDescription`, `SetHairDescription`, `SetSummaryDescription`, `CBInit` und `CBInitialize` (gleiche Adresse); `OnInit` ist ein zusammengefalteter Rumpf.
- **Preis:** Geld plus Steuersatz des Charakters; Totenkopf-Preise sind Gegenstände.
- **UI:** 14 Funktionen, 3 Anzeigen, 4 Benutzerdaten, 5 Ereignisse (Tabelle „UI-Namen“), jeweils in Anzahl und Namen gleich der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUICustomizing.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00683700` | 493 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnIdle` | `0x00681BE0` | 145 | vtable/String |
| 3 | `OnDestroy` | `0x00681C80` | 56 | vtable/String |
| 4 | `AddEvent` | `0x00681CC0` | 164 | Zeichenkette |
| 5 | `AddFunction` | `0x006834A0` | 594 | Zeichenkette |
| 6 | `AddUserData` | `0x00681D70` | 179 | Zeichenkette |
| 7 | `AddDisplay` | `0x00682490` | 101 | Zeichenkette |
| 8 | `CBGetEditControl` | `0x00681E30` | 80 | UI-Registrierung |
| 9 | `IsEnoughCost` | `0x00682500` | 358 | ver |
| 10 | `CBBuy` | `0x00682670` | 101 | UI-Registrierung |
| 11 | `CBInit` | `0x00683490` | 16 | ver |
| 12 | `CBConfirmOK` | `0x00681E80` | 181 | UI-Registrierung |
| 13 | `CBSelectFace` | `0x00682E00` | 147 | UI-Registrierung |
| 14 | `CBSelectHair` | `0x00682EA0` | 147 | UI-Registrierung |
| 15 | `CBDisplayFaceName` | `0x00681F40` | 65 | UI-Registrierung |
| 16 | `CBDisplayHairName` | `0x00681F90` | 65 | UI-Registrierung |
| 17 | `CBDisplayBuyPrice` | `0x00681FE0` | 53 | UI-Registrierung |
| 18 | `CBEventGrant` | `0x006833D0` | 178 | Callback-Registrierung |
| 19 | `CBKeydownESC` | `0x00682020` | 76 | Callback-Registrierung |
| 20 | `CBRotateLeft` | `0x00682070` | 26 | UI-Registrierung |
| 21 | `CBRotateRight` | `0x00682090` | 26 | UI-Registrierung |
| 22 | `CBRotateEnd` | `0x006820B0` | 42 | UI-Registrierung |
| 23 | `CBZoomIn` | `0x006820E0` | 26 | UI-Registrierung |
| 24 | `CBZoomOut` | `0x00682100` | 26 | UI-Registrierung |
| 25 | `CBZoomEnd` | `0x00682120` | 42 | UI-Registrierung |
| 26 | `CBInitialize` | `0x00683490` | 16 | gleiche Adresse wie `CBInit` (vom Linker zusammengefaltet) |
| 27 | `InitializeList` | `0x00682F40` | 1150 | ver |
| 28 | `SetFaceDescription` | `0x006826E0` | 539 | ver |
| 29 | `SetHairDescription` | `0x00682900` | 539 | ver |
| 30 | `SetSummaryDescription` | `0x00682B20` | 731 | ver |
| 31 | `CBCloseUI` | `0x00682150` | 76 | UI-Registrierung |
| 32 | `CBSelfUpdateCustomize` | `0x006821A0` | 355 | Callback-Registrierung |
| 33 | `CBSetSelfCharacter` | `0x00682310` | 49 | Callback-Registrierung |
| 34 | `CBSelfUpdatePosition` | `0x00682350` | 140 | Callback-Registrierung |
| 35 | `PriceWithTax` | `0x006823E0` | 65 | ver |
| 36 | `GetInvenMoney` | `0x00682430` | 51 | ver |

37 von 37 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUICustomizing` (`0x00681A50`), `ctor_or_dtor` (`0x00681B80`), `~AgcmUICustomizing` (`0x00682470`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x24E0 / 0x24E4` | `Benutzerdaten Gesichtsliste / Frisurenliste (`m_lSelectedIndex` bei `+0x50`)` | `IsEnoughCost`, `CBBuy` |
| `0x280FC / 0x28100` | `Gesamtpreis Geld / Totenkopf` | `IsEnoughCost` |
| `Eintrag 0x5C Byte` | `Listeneintrag (Preis, Level, Namen)` | `InitializeList`, `IsEnoughCost` |
| `0x41EC / 0x1616C` | `Gesichtsliste / Frisurenliste (je 0x11F80 Byte gelöscht)` | `InitializeList` |

## Vtable

Vtable bei `0x008CB71C`: Slot 0 Destruktor `0x00682470`, 1 `OnAddModule` (`0x00683700`), 2 `OnInit`-Rumpf `0x0067AC90` (leer in der Quelle), 3 `OnIdle` (`0x00681BE0`), 6 `return TRUE`-Rumpf `0x0067AC90`, 7 `OnDestroy` (`0x00681C80`).

## Callbacks (OnAddModule, 0x00683700)

Zehn Module werden geholt (u. a. [`AgpmEventCharCustomize`](AgpmEventCharCustomize.md), [`AgcmCustomizeRender`](AgcmCustomizeRender.md), [`AgcmEventCharCustomize`](AgcmEventCharCustomize.md), [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgcmUIMain`](AgcmUIMain.md)). Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| [`AgpmCharacter`](AgpmCharacter.md): Aussehen geändert | `CBSelfUpdateCustomize` | `0x006821A0` |
| `AgcmCharacter`: Self-Character gesetzt | `CBSetSelfCharacter` | `0x00682310` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x00682350` |
| `AgcmEventCharCustomize`: Ereignis gewährt | `CBEventGrant` | `0x006833D0` |
| `AgcmUIMain`: Esc-Taste | `CBKeydownESC` | `0x00682020` |

Danach `AddEvent`, `AddFunction`, `AddUserData` und `AddDisplay`, zuletzt die Vorschau-Steuerung `CustomizePreview`. Reihenfolge wie in der Quelle.

## Kosten (IsEnoughCost, 0x00682500)

Summiert die Kosten aus der gewählten Frisur und dem gewählten Gesicht: Kostet ein Eintrag nur Geld (Totenkopf-Preis 0), wird `PriceWithTax` (`0x006823E0`, Preis + Steuersatz in Prozent des Charakters) aufgerufen; sonst gilt der Eintrag als Gegenstandspreis (die „Totenkopf“-Zahl ist die Gegenstands-TID). Die Summe liegt bei `+0x280FC` (Geld) und `+0x28100` (Totenkopf/Gegenstand). `CBBuy` (`0x00682670`) wirft das Kaufbestätigungs-Ereignis, nur wenn mindestens eine Auswahl besteht und `IsEnoughCost` gelingt. `GetInvenMoney` (`0x00682430`) liest das Inventargeld.

## Beschreibungen

`CBSelectFace` und `CBSelectHair` rufen jeweils ihre Beschreibung (`SetFaceDescription` `0x006826E0`, `SetHairDescription` `0x00682900`) und die Zusammenfassung `SetSummaryDescription` (`0x00682B20`, 731 Byte); `InitializeList` (`0x00682F40`, 1150 Byte) füllt die Listen und ruft Beschreibung und Zusammenfassung. `CBInit` und `CBInitialize` haben denselben Rumpf (sie rufen nur `InitializeList`) und stehen auf `0x00683490`; die UI-Funktionen `CustomizeInit` und `CustomizeInitialize` zeigen beide darauf.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006834A0`, `0x00682490`, `0x00681D70`, `0x00681CC0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (14)

| Name | Id | Handler |
|---|---:|---|
| `CustomizeGetEdit` |  | `CBGetEditControl` |
| `CustomizeBuy` |  | `CBBuy` |
| `CustomizeInit` |  | `FUN_00683490` |
| `CustomizeConfirmOK` |  | `CBConfirmOK` |
| `CustomizeSelectFace` |  | `CBSelectFace` |
| `CustomizeSelectHair` |  | `CBSelectHair` |
| `CustomizeRotateLeft` |  | `CBRotateLeft` |
| `CustomizeRotateRight` |  | `CBRotateRight` |
| `CustomizeRotateEnd` |  | `CBRotateEnd` |
| `CustomizeZoomIn` |  | `CBZoomIn` |
| `CustomizeZoomOut` |  | `CBZoomOut` |
| `CustomizeZoomEnd` |  | `CBZoomEnd` |
| `CustomizeInitialize` |  | `FUN_00683490` |
| `CustomizeCloseUI` |  | `CBCloseUI` |

**Anzeige** (3)

| Name | Id | Handler |
|---|---:|---|
| `CustomizeFaceName` | 0 | `CBDisplayFaceName` |
| `CustomizeHairName` | 0 | `CBDisplayHairName` |
| `CustomizeBuyPrice` | 0 | `CBDisplayBuyPrice` |

**UserData** (4)

| Name | Id | Handler |
|---|---:|---|
| `CustomizeFaceList` |  | – |
| `CustomizeHairList` |  | – |
| `CustomizeBuyPrice` |  | – |
| `CustomizeIsActiveBuy` |  | – |

**Ereignis** (5)

| Name | Id | Handler |
|---|---:|---|
| `OpenCustomizeUI` | 0 | – |
| `CloseCustomizeUI` | 0 | – |
| `CustomizeBuyConfirm` | 0 | – |
| `CustomizeNeedDismountRide` | 0 | – |
| `CustomizeNeedRestoreTransform` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`IsEnoughCost`, `CBBuy`, Registrierungsreihenfolge).

## Grenzen

- `SetFaceDescription`, `SetHairDescription`, `SetSummaryDescription` und `InitializeList` wurden nur nach Aufrufern, Größe und aufgerufenen Hilfen (UI-Texte) zugeordnet, nicht Zeile für Zeile verglichen.
- Die Listengrößen (`AGCMUICUSTOMIZE_MAX_FACE` 50, `MAX_HAIR` 100) wurden nicht gegen die Speichergrößen im Binary abgeglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1, ohne Kandidat: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmCustomizeRender`](AgcmCustomizeRender.md), [`AgcmEventCharCustomize`](AgcmEventCharCustomize.md), [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventCharCustomize`](AgpmEventCharCustomize.md)
