# AgcmUITax (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUITax` (Steuerverwaltung der Burgherren: Steuersätze ändern und Einnahmen ansehen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUITax/AgcmUITax.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 55 von 58 Quellmethoden sind einer Adresse zugeordnet (die drei `Test…` gibt es nur im Debug-Build); neu sind `AddEvent`, `OpenSteward`, `OpenModifyRatio`, `OpenViewIncome`, `CloseAll`, `GetTax`, `GetRegionTax`, `UpdateTax`, `RequestIncome`, `SendRequestEvent`, `SendViewIncome`, `SendModifyRatio`, `GetMessageTxt` sowie die 29 UI-Funktionen und Anzeigen (über die Registrierungsreihenfolge).
- **Pakete:** Typ `0x53`, Operation 0 (Ereignis-Anfrage), 2 (Satz ändern) und 3 (Einnahmen abfragen).
- **UI:** 5 Funktionen, 24 Anzeigen, 1 Bool-Anzeige, 3 Benutzerdaten, 6 Ereignisse – Anzahl wie in der Quelle.
- **Hinweis:** `GetMessageTxt` übernimmt die Quellprüfung `> MAX` (Index 9 erlaubt); `CBReleaseCharacter` und `CBKeydownESC` sind ein gemeinsamer Rumpf.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUITax.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00697850` | 546 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf (die Skript-Anmeldung der Testfunktionen gibt es nur im Debug-Build)` (vom Linker zusammengefaltet) |
| 2 | `AddEvent` | `0x00695380` | 67 | manual |
| 3 | `AddFunction` | `0x00697450` | 201 | Zeichenkette |
| 4 | `AddDisplay` | `0x00697520` | 803 | Zeichenkette |
| 5 | `AddUserData` | `0x006953D0` | 116 | Zeichenkette |
| 6 | `OpenSteward` | `0x00695450` | 173 | manual |
| 7 | `OpenModifyRatio` | `0x00695500` | 78 | manual |
| 8 | `RequestIncome` | `0x00695CF0` | 78 | manual |
| 9 | `OpenViewIncome` | `0x00695550` | 78 | manual |
| 10 | `CloseAll` | `0x006955A0` | 77 | manual |
| 11 | `TestOpenSteward` | – | | nur im Debug-Build (`_DEBUG`) |
| 12 | `TestOpenModifyRatio` | – | | nur im Debug-Build (`_DEBUG`) |
| 13 | `TestRequestIncome` | – | | nur im Debug-Build (`_DEBUG`) |
| 14 | `GetTax` | `0x006955F0` | 67 | manual |
| 15 | `GetRegionTax` | `0x00695D50` | 89 | manual |
| 16 | `UpdateTax` | `0x00695DB0` | 186 | manual |
| 17 | `SendRequestEvent` | `0x00695640` | 124 | manual |
| 18 | `SendModifyRatio` | `0x00695E70` | 394 | manual |
| 19 | `SendViewIncome` | `0x006956C0` | 249 | manual |
| 20 | `CBResultModifyRatio` | `0x00696000` | 184 | Callback-Registrierung |
| 21 | `CBResultInquireTax` | `0x006960D0` | 104 | Callback-Registrierung |
| 22 | `CBReleaseCharacter` | `0x00698820` | 10 | gleiche Adresse wie `gemeinsamer Rumpf (return param != 0)` (vom Linker zusammengefaltet) |
| 23 | `CBRequestEvent` | `0x006957C0` | 125 | Callback-Registrierung |
| 24 | `CBGrant` | `0x00695840` | 41 | Callback-Registrierung |
| 25 | `CBSelfUpdatePosition` | `0x00695870` | 100 | Callback-Registrierung |
| 26 | `CBKeydownESC` | `0x00698820` | 10 | gleiche Adresse wie `gemeinsamer Rumpf (return param != 0)` (vom Linker zusammengefaltet) |
| 27 | `CBClickModifyRatio` | `0x00696140` | 26 | uireg |
| 28 | `CBClickViewIncome` | `0x00696160` | 26 | uireg |
| 29 | `CBClickReset` | `0x006958E0` | 379 | uireg |
| 30 | `CBClickConfirm` | `0x00696ED0` | 1112 | uireg |
| 31 | `CBClickBack` | `0x00695A60` | 16 | uireg |
| 32 | `CBDisplayStewardIntro` | `0x00696180` | 349 | uireg |
| 33 | `CBDisplayCaption` | `0x006962E0` | 113 | uireg |
| 34 | `CBDisplayRegion1` | `0x00696360` | 252 | uireg |
| 35 | `CBDisplayRegion2` | `0x00696460` | 252 | uireg |
| 36 | `CBDisplayRegion3` | `0x00696560` | 267 | uireg |
| 37 | `CBDisplayRegion4` | `0x00696670` | 267 | uireg |
| 38 | `CBDisplayRegion5` | `0x00697330` | 284 | uireg |
| 39 | `CBDisplayModifyRatio1` | `0x00696780` | 112 | uireg |
| 40 | `CBDisplayModifyRatio2` | `0x006967F0` | 112 | uireg |
| 41 | `CBDisplayModifyRatio3` | `0x00696860` | 112 | uireg |
| 42 | `CBDisplayModifyRatio4` | `0x006968D0` | 112 | uireg |
| 43 | `CBDisplayViewRatio1` | `0x00696940` | 114 | uireg |
| 44 | `CBDisplayViewRatio2` | `0x006969C0` | 114 | uireg |
| 45 | `CBDisplayViewRatio3` | `0x00696A40` | 123 | uireg |
| 46 | `CBDisplayViewRatio4` | `0x00696AC0` | 123 | uireg |
| 47 | `CBDisplayViewRatio5` | `0x00695A70` | 118 | uireg |
| 48 | `CBDisplayIncome1` | `0x00696B40` | 118 | uireg |
| 49 | `CBDisplayIncome2` | `0x00696BC0` | 123 | uireg |
| 50 | `CBDisplayIncome3` | `0x00696C40` | 127 | uireg |
| 51 | `CBDisplayIncome4` | `0x00696CC0` | 127 | uireg |
| 52 | `CBDisplayIncome5` | `0x00696D40` | 225 | uireg |
| 53 | `CBDisplayRecentIncome` | `0x00696E30` | 100 | uireg |
| 54 | `CBDisplayTotalIncome` | `0x00695AF0` | 105 | uireg |
| 55 | `CBDisplayLatestTransferDate` | `0x00695B60` | 183 | uireg |
| 56 | `CBIsCastleOwner` | `0x00695C20` | 42 | Callback-Registrierung |
| 57 | `GetMessageTxt` | `0x00695C50` | 43 | manual |

55 von 58 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUITax` (`0x00695320`), `~AgcmUITax` (`0x00695CC0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB84…0xBA8` | `Modulzeiger ([`AgpmCharacter`](AgpmCharacter.md) +0xB84, [`AgpmTax`](AgpmTax.md) +0xB88, [`AgpmSiegeWar`](AgpmSiegeWar.md) +0xB8C, [`AgpmArchlord`](AgpmArchlord.md) +0xB90, `AgcmCharacter` +0xB94, [`AgcmUIManager2`](AgcmUIManager2.md) +0xB98, [`AgcmUIControl`](AgcmUIControl.md) +0xB9C, [`AgcmUIMain`](AgcmUIMain.md) +0xBA0, [`AgcmEventManager`](AgcmEventManager.md) +0xBA4, [`AgcmUICharacter`](AgcmUICharacter.md) +0xBA8)` | `OnAddModule` |
| `0xBAC…` | `Ereignis-IDs `m_lEvent[6]`` | `AddEvent`, `OpenSteward` |
| `0xBC0 / 0xBC4 …` | `Benutzerdaten und Schaltflächen-IDs (Steward / Satz / Einnahmen)` | `OpenSteward`, `OpenModifyRatio`, `CloseAll` |
| `0xBDC` | `Merker „Satz-Fenster“ (`m_bModifyWindow`)` | `CBDisplayCaption`, `CBResultInquireTax` |
| `0xBE0` | `ID des Ereignis-NPCs (`m_lEventNPCID`)` | `CBRequestEvent`, `OpenSteward` |

## Vtable

Vtable bei `0x008CE218`: Slot 0 Destruktor `0x00695CC0`, 1 `OnAddModule` (`0x00697850`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`, `OnDestroy`), 3–5 gemeinsamer Rumpf `0x0067FAB0`.

## Registrierung (OnAddModule, 0x00697850)

Holt zehn Module (`AgpmCharacter`, `AgpmTax`, `AgpmSiegeWar`, `AgpmArchlord`, `AgcmCharacter`, `AgcmUIManager2`, `AgcmUIControl`, `AgcmUIMain`, `AgcmEventManager`, `AgcmUICharacter`); alle sind Pflicht. Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmTax`: Steuersatz ändern (Ergebnis) | `CBResultModifyRatio` | `0x00696000` |
| `AgpmTax`: Steuer abfragen (Ergebnis) | `CBResultInquireTax` | `0x006960D0` |
| `AgcmCharacter`: eigener Charakter freigegeben | `CBReleaseCharacter` | `0x00698820` (gemeinsamer Rumpf) |
| `AgcmEventManager`: Ereignisfunktion 0x22 (Steuer) | `CBRequestEvent` | `0x006957C0` |
| `AgpmTax`: Ereignis gewährt | `CBGrant` | `0x00695840` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x00695870` |
| `AgcmUIMain`: ESC | `CBKeydownESC` | `0x00698820` (derselbe Rumpf) |

Danach `AddEvent` (`0x00695380`), `AddFunction` (`0x00697450`), `AddDisplay` (`0x00697520`), `AddUserData` (`0x006953D0`) und die Bool-Anzeige `TAX_CASTLE_OWNER` (`CBIsCastleOwner`, `0x00695C20`).

## Fenster (OpenSteward, OpenModifyRatio, OpenViewIncome, CloseAll)

Das Modul steuert drei Fenster über sechs Ereignisse (`TAX_OPEN_STEWARD`/`_CLOSE_STEWARD`, `_RATIO`, `_INCOME`).
`OpenSteward` (`0x00695450`): nur für Burgherren (`AgpmTax::IsCastleOwner`, `0x00577DF0`); wählt den Verwalter-NPC als Ziel (`SelectTarget`), schließt die beiden anderen Fenster, öffnet das Verwalter-Fenster und aktualisiert das Ziel-Charakter-Benutzerdatum. `OpenModifyRatio` (`0x00695500`) und `OpenViewIncome` (`0x00695550`) schließen das Verwalter-Fenster und öffnen das jeweilige andere; `CloseAll` (`0x006955A0`) schließt alle drei.
`CBSelfUpdatePosition` ruft `CloseAll`, sobald der Charakter 150 Einheiten oder mehr vom Öffnungsort entfernt ist (Vergleich `≥ 0x96`). `CBReleaseCharacter` und `CBKeydownESC` sind in der Quelle leer (Prüfung auf den Klassenzeiger) und stehen im Binary als derselbe Rumpf `0x00698820` (`return param_2 != 0`).

## Pakete (Typ 0x53)

Alle drei Sender benutzen `AGPMTAX_PACKET_TYPE` (`0x53`) und `MakePacket` (`0x004EA2D0`):

| Sender | Adresse | Operation | Inhalt |
|---|---|---:|---|
| `SendRequestEvent` | `0x00695640` | 0 (Ereignis-Anfrage) | `AgpmTax::MakePacketEventRequest` (`0x00577B50`) mit Ereignis und Charakter-ID |
| `SendViewIncome` | `0x006956C0` | 3 (`INQUIRE_TAX`) | Charakter-ID und eingebettetes Burg-Paket mit dem Burgnamen |
| `SendModifyRatio` | `0x00695E70` | 2 (`MODIFY_RATIO`) | Charakter-ID, Burg-Paket und bis zu vier Region-Pakete (Regionsname und Satz) |

`CBRequestEvent` (`0x006957C0`) wirkt nur für den eigenen Charakter, lehnt bei Aktionssperre (`IsActionBlockCondition`) ab, merkt die ID des Ereignis-NPCs (`+0xBE0`) und sendet die Anfrage. `RequestIncome` (`0x00695CF0`) ermittelt die Burg des Charakters und sendet `SendViewIncome`.

## Steuerdaten (GetTax, GetRegionTax, UpdateTax)

`GetTax` (`0x006955F0`) liefert die Steuerdaten nur für Burgherren; `GetRegionTax` (`0x00695D50`) prüft den Index gegen die Zahl der Regionen (bis 4); `UpdateTax` (`0x00695DB0`) schreibt Burg- und Regionssteuern aus dem Serverergebnis in `AgpmTax` (`UpdateCastleTax` `0x00578420`, `UpdateRegionTax` `0x005785D0`). `CBResultModifyRatio` meldet Erfolg und die drei Fehlerfälle (nicht Besitzer, falsche Zeit, Wert außerhalb des Bereichs) in einem OK-Dialog; `CBResultInquireTax` öffnet bei Erfolg je nach Merker das Satz- oder das Einnahmen-Fenster.

## Bestätigen und Zurücksetzen (CBClickConfirm, CBClickReset)

`CBClickConfirm` (`0x00696ED0`, 1112 Byte) liest die vier Eingabefelder, prüft jeden Wert gegen `0…s_lBaseRatio[5]`, baut den Bestätigungstext aus Regionsname und Satz (`TAX_MODIFY_CON_REG`/`_QUE`), fragt per OK/Abbrechen-Dialog nach, kopiert die Steuerdaten in eine Arbeitskopie (der Speicher in `AgpmTax` bleibt bis zur Serverantwort unverändert) und sendet `SendModifyRatio`. `CBClickReset` (`0x006958E0`) setzt die Felder auf „0“ (bei fehlender Steuer auf leer).

## Anzeigefunktionen

24 Anzeigen (`TAX_INTRO`, `TAX_CAPTION`, fünf `TAX_REGIONn`, vier `TAX_MODIFY_RATIOn`, fünf `TAX_VIEW_RATIOn`, fünf `TAX_INCOMEn`, `TAX_REC_INCOME`, `TAX_TOT_INCOME`, `TAX_TR_DATE`) und 5 Funktionen (`TAX_MODIFY_RATIO`, `TAX_VIEW_INCOME`, `TAX_RESET`, `TAX_CONFIRM`, `TAX_BACK`). Die Zuordnung der Anzeigen zu den Adressen folgt der Registrierungsreihenfolge; gelesen wurden `CBDisplayStewardIntro` (Text `TAX_INTRO` mit Burgname, 100 Zeichen), `CBDisplayCaption` (Titel je nach Fenster), `CBDisplayTotalIncome` (`%I64d`) und `CBDisplayRecentIncome`. `GetMessageTxt` (`0x00695C50`) prüft den Index mit `< 10`: Die Quelle schreibt `eMessage > AGCMUITAX_MESSAGE_MAX` (statt `>=`), also ist auch Index 9 (hinter der Tabelle) erlaubt – das Binary übernimmt diese Prüfung unverändert.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00697450`, `0x00697520`, `0x006953D0`, `0x00695380`, `0x00697850`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (5)

| Name | Id | Handler |
|---|---:|---|
| `TAX_MODIFY_RATIO` |  | `FUN_00696140` |
| `TAX_VIEW_INCOME` |  | `FUN_00696160` |
| `TAX_RESET` |  | `FUN_006958e0` |
| `TAX_CONFIRM` |  | `FUN_00696ed0` |
| `TAX_BACK` |  | `FUN_00695a60` |

**Anzeige** (24)

| Name | Id | Handler |
|---|---:|---|
| `TAX_INTRO` | 0 | `FUN_00696180` |
| `TAX_CAPTION` | 0 | `FUN_006962e0` |
| `TAX_REGION1` | 0 | `FUN_00696360` |
| `TAX_REGION2` | 0 | `FUN_00696460` |
| `TAX_REGION3` | 0 | `FUN_00696560` |
| `TAX_REGION4` | 0 | `FUN_00696670` |
| `TAX_REGION5` | 0 | `FUN_00697330` |
| `TAX_MODIFY_RATIO1` | 0 | `FUN_00696780` |
| `TAX_MODIFY_RATIO2` | 0 | `FUN_006967f0` |
| `TAX_MODIFY_RATIO3` | 0 | `FUN_00696860` |
| `TAX_MODIFY_RATIO4` | 0 | `FUN_006968d0` |
| `TAX_VIEW_RATIO1` | 0 | `FUN_00696940` |
| `TAX_VIEW_RATIO2` | 0 | `FUN_006969c0` |
| `TAX_VIEW_RATIO3` | 0 | `FUN_00696a40` |
| `TAX_VIEW_RATIO4` | 0 | `FUN_00696ac0` |
| `TAX_VIEW_RATIO5` | 0 | `FUN_00695a70` |
| `TAX_INCOME1` | 0 | `FUN_00696b40` |
| `TAX_INCOME2` | 0 | `FUN_00696bc0` |
| `TAX_INCOME3` | 0 | `FUN_00696c40` |
| `TAX_INCOME4` | 0 | `FUN_00696cc0` |
| `TAX_INCOME5` | 0 | `FUN_00696d40` |
| `TAX_REC_INCOME` | 0 | `FUN_00696e30` |
| `TAX_TOT_INCOME` | 0 | `FUN_00695af0` |
| `TAX_TR_DATE` | 0 | `FUN_00695b60` |

**UserData** (3)

| Name | Id | Handler |
|---|---:|---|
| `TAX_UD_STEWARD` | 0 | – |
| `TAX_UD_MODIFY_RATIO` | 0 | – |
| `TAX_UD_VIEW_INCOME` | 0 | – |

**Boolean** (1)

| Name | Id | Handler |
|---|---:|---|
| `TAX_CASTLE_OWNER` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierungsreihenfolge, `OpenSteward`, `CloseAll`, `CBSelfUpdatePosition`, `CBRequestEvent`, die drei Sender, `GetMessageTxt`).

## Grenzen

- `CBClickConfirm` (1112 Byte) wurde nur über Größe, Aufrufe und Aufrufer geprüft, nicht Zeile für Zeile.
- Die 24 Anzeigefunktionen sind nach der Registrierungsreihenfolge zugeordnet; fünf davon (Steward-Intro, Caption, Gesamteinnahmen, letzte Einnahmen, Überweisungsdatum teilweise) wurden gelesen.
- Die kleine Hilfe `0x00695C80` (Summe über die Regionen, vermutlich eine Funktion von `AgpdTax`) und `0x00696EA0` (Konstruktor eines Zeichenpuffers) gehören zu keiner Quellmethode von `AgcmUITax`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, gemeinsamer Rumpf: 1, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmArchlord`](AgpmArchlord.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmSiegeWar`](AgpmSiegeWar.md), [`AgpmTax`](AgpmTax.md)
- **Erwähnt in:** [`AgcmUIRemission`](AgcmUIRemission.md)
