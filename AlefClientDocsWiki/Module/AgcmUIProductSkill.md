# AgcmUIProductSkill (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `AgcmUIProductSkill` (Rezepte lernen und Fertigkeitenliste der Herstellung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIProduct/AgcmUIProductSkill.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 49 von 50 Quellmethoden sind zugeordnet; neu in diesem Durchgang sind elf (`SetList`, beide `IsActiveBuyItem`, `SetRecastSkillTimeToGridItem`, `SetStatusBuyItem`, `SetTooltipText`, `SetBuyList`, `OnBuyComposeResult`, `OnLearnSkillResult`, `OnResult`) sowie `CBDisplayName` als gemeinsamer Rumpf.
- **UI:** 11 Funktionen, 8 Anzeigen (IDs 0–7), 5 Benutzerdaten, 1 Boolean, `PDSK_EVENT_BUY_CONFIRM` – wie in der Quelle.
- **Zusatz:** `AgcmUIProduct::OnResult` wurde dabei ebenfalls gefunden (`0x006A3B80`) und im Bericht [AgcmUIProduct](AgcmUIProduct.md) nachgetragen.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIProductSkill.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006A69C0` | 855 | vtable/String |
| 1 | `OnInit` | `0x006A4310` | 142 | vtable/String |
| 2 | `OnDestroy` | `0x006A43A0` | 61 | vtable/String |
| 3 | `AddFunction` | `0x006A6790` | 456 | Zeichenkette |
| 4 | `AddEvent` | `0x006A6060` | 99 | Zeichenkette |
| 5 | `AddUserData` | `0x006A43E0` | 207 | Zeichenkette |
| 6 | `AddDisplay` | `0x006A5460` | 262 | Zeichenkette |
| 7 | `AddBoolean` | `0x006A60D0` | 31 | Zeichenkette |
| 8 | `SetList` | `0x006A44B0` | 181 | ver |
| 9 | `SetBuyList` | `0x006A60F0` | 749 | ver |
| 10 | `IsActiveBuyItem` | `0x006A5570` | 46 | von Hand geprüft |
| 11 | `IsActiveBuyItem` | `0x006A4570` | 220 | von Hand geprüft |
| 12 | `SetStatusBuyItem` | `0x006A55A0` | 121 | ver |
| 13 | `SetRecastSkillTimeToGridItem` | `0x006A4650` | 78 | ver |
| 14 | `CBSetSelfCharacter` | `0x006A5640` | 193 | Callback-Registrierung |
| 15 | `CBReleaseSelfCharacter` | `0x006A46A0` | 25 | Callback-Registrierung |
| 16 | `CBUpdateInvenMoney` | `0x006A46C0` | 62 | Callback-Registrierung |
| 17 | `CBAddSkill` | `0x006A4700` | 147 | Callback-Registrierung |
| 18 | `CBUpdateSkillPoint` | `0x006A47A0` | 76 | Callback-Registrierung |
| 19 | `CBReceiveSkillAction` | `0x006A47F0` | 98 | Callback-Registrierung |
| 20 | `CBGrant` | `0x006A4860` | 118 | Callback-Registrierung |
| 21 | `CBSelfUpdatePosition` | `0x006A48E0` | 136 | Callback-Registrierung |
| 22 | `CBBuyComposeResult` | `0x006A6960` | 33 | Callback-Registrierung |
| 23 | `CBLearnSkillResult` | `0x006A6990` | 33 | Callback-Registrierung |
| 24 | `CBOpen` | `0x006A4970` | 70 | UI-Registrierung |
| 25 | `CBClose` | `0x006A49C0` | 49 | UI-Registrierung |
| 26 | `CBOpenTooltip` | `0x006A4A00` | 116 | UI-Registrierung |
| 27 | `CBCloseTooltip` | `0x006A4A80` | 48 | UI-Registrierung |
| 28 | `CBBuyOpen` | `0x006A63F0` | 16 | UI-Registrierung |
| 29 | `CBBuyClose` | `0x006A4AB0` | 49 | UI-Registrierung |
| 30 | `CBBuySelectGrid` | `0x006A4AF0` | 119 | UI-Registrierung |
| 31 | `CBBuyBuy` | `0x006A5710` | 74 | UI-Registrierung |
| 32 | `CBBuyUpdateListItem` | `0x006A5760` | 99 | UI-Registrierung |
| 33 | `CBBuyOpenTooltip` | `0x006A6400` | 303 | UI-Registrierung |
| 34 | `CBBuyCloseTooltip` | `0x006A4B70` | 148 | UI-Registrierung |
| 35 | `CBDisplayName` | `0x006C7FE0` | 144 | gleiche Adresse wie [`AgcmUISkill2`](AgcmUISkill2.md):CBDisplaySkillName` (vom Linker zusammengefaltet) |
| 36 | `CBDisplayLvExp` | `0x006A4C10` | 421 | UI-Registrierung |
| 37 | `CBDisplayExpBar` | `0x006A4DC0` | 241 | UI-Registrierung |
| 38 | `CBDisplayBuyName` | `0x006A4EC0` | 191 | UI-Registrierung |
| 39 | `CBDisplayBuyPrice` | `0x006A4F80` | 478 | UI-Registrierung |
| 40 | `CBDisplayBuyInvenMoney` | `0x006A5160` | 64 | UI-Registrierung |
| 41 | `CBDisplayTitle` | `0x006A51A0` | 148 | UI-Registrierung |
| 42 | `CBConfirmBuy` | `0x006A57D0` | 175 | UI-Registrierung |
| 43 | `CBIsActiveBuyButton` | `0x006A5880` | 58 | UI-Registrierung |
| 44 | `CBKeydownESC` | `0x006A5240` | 31 | Callback-Registrierung |
| 45 | `Open` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 46 | `OnResult` | `0x006A58C0` | 158 | ver |
| 47 | `OnBuyComposeResult` | `0x006A6530` | 302 | ver |
| 48 | `OnLearnSkillResult` | `0x006A6660` | 302 | ver |
| 49 | `SetTooltipText` | `0x006A5D60` | 759 | ver |

49 von 50 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006a42b0` (`0x006A42B0`), `ctor_or_dtor_006a5260` (`0x006A5260`), `~AgcmUIProductSkill` (`0x006A5440`), `IsActiveBuyItem_Wrapper` (`0x006A5570`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x2940` | `Benutzerdaten Kauf-Gitter (`m_pUDBuyGrid`)` | `IsActiveBuyItem`-Hülle |
| `0x2974 / 0x2978` | `Ereignis-IDs, die `OnBuyComposeResult` wirft` | `OnBuyComposeResult` |
| `0x3B64` | `Zeiger auf [`AgpmProduct`](AgpmProduct.md)` | `IsActiveBuyItem` |

## Umfang

`AgcmUIProductSkill` (Fertigkeiten-Fenster der Herstellung: Liste der gelernten Rezepte, Kauf neuer Rezepte) ist die zweite Klasse neben [AgcmUIProduct](AgcmUIProduct.md) im Verzeichnis `AgcmUIProduct` (`AgcmUIProductSkill.cpp`, 50 Methoden). Binary: `0x006A42B0`–`0x006A69C0`.

## Vtable

Vtable bei `0x008CF90C`: Slot 0 Destruktor `0x006A5440`, 1 `OnAddModule` (`0x006A69C0`), 2 `OnInit` (`0x006A4310`), 7 `OnDestroy` (`0x006A43A0`), 6 `return TRUE`-Rumpf `0x0067AC90`.

## Callbacks (OnAddModule, 0x006A69C0)

Siebzehn Module werden geholt (u. a. `AgpmProduct`, [`AgpmEventProduct`](AgpmEventProduct.md), [`AgcmProduct`](AgcmProduct.md), [`AgcmEventProduct`](AgcmEventProduct.md), `AgcmUISkill2`, [`AgcmUIItem`](AgcmUIItem.md)). Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgcmCharacter`: Self-Character gesetzt | `CBSetSelfCharacter` | `0x006A5640` |
| `AgcmCharacter`: Self-Character freigegeben | `CBReleaseSelfCharacter` | `0x006A46A0` |
| [`AgpmCharacter`](AgpmCharacter.md): Geld geändert | `CBUpdateInvenMoney` | `0x006A46C0` |
| [`AgpmSkill`](AgpmSkill.md): Fertigkeit initialisiert | `CBAddSkill` | `0x006A4700` |
| `AgpmSkill`: Fertigkeitspunkte geändert | `CBUpdateSkillPoint` | `0x006A47A0` |
| `AgpmSkill`: Fertigkeit aktualisiert | `CBUpdateSkillPoint` | `0x006A47A0` |
| `AgpmSkill`: Aktion empfangen | `CBReceiveSkillAction` | `0x006A47F0` |
| `AgpmEventProduct`: Rezeptkauf-Ergebnis | `CBBuyComposeResult` | `0x006A6960` |
| `AgpmEventProduct`: Fertigkeit-Lernen-Ergebnis | `CBLearnSkillResult` | `0x006A6990` |
| `AgcmEventProduct`: Ereignis gewährt | `CBGrant` | `0x006A4860` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x006A48E0` |
| [`AgcmUIMain`](AgcmUIMain.md): Esc-Taste (falls vorhanden) | `CBKeydownESC` | `0x006A5240` |

Danach `AddFunction`, `AddEvent`, `AddUserData`, `AddDisplay`, `AddBoolean`. Reihenfolge wie in der Quelle.

## Ergebnisse (OnBuyComposeResult / OnLearnSkillResult)

`OnBuyComposeResult` (`0x006A6530`) und `OnLearnSkillResult` (`0x006A6660`) setzen je nach Ergebniscode eine Systemmeldung (UI-Texte `0x1AB`, `0x1AD`, `0x1AE` u. a., bei Erfolg mit dem Rezeptnamen) ab und werfen das passende UI-Ereignis (Kauf erfolgreich, fehlgeschlagen u. a.); bei „zu wenig Geld“ eine eigene Meldung. Struktur und Texte entsprechen der Quelle.

## Kaufliste

`SetBuyList` (`0x006A60F0`, 749 Byte) baut die Liste kaufbarer Rezepte, `IsActiveBuyItem` (`0x006A4570`) bestimmt je Rezept den Status (bereits gelernt, aktiv, zu wenig Geld/Stufe/Voraussetzung), die Hülle `0x006A5570` prüft nur den Index. `SetStatusBuyItem` (`0x006A55A0`) wirft daraus das Ereignis „gelernt“, „aktiv“ oder „deaktiviert“. `SetTooltipText` (`0x006A5D60`, 759 Byte) baut die Tooltips; `SetList` (`0x006A44B0`) füllt die Liste der gelernten Rezepte.

## Gemeinsamer Anzeigerumpf

Die Anzeige `PDSKName` (Anzeige-ID 0) zeigt auf `0x006C7FE0`, dieselbe Funktion wie `AgcmUISkill2::CBDisplaySkillName`; `CBDisplayName` ist in beiden Klassen identisch (Fertigkeitsname aus dem Gitter) und wurde vom Linker zusammengefaltet.

## Gemeinsame Ergebnisverarbeitung

[`AgcmUIProduct`](AgcmUIProduct.md):OnResult` (`0x006A3B80`) und `AgcmUIProductSkill::OnResult` (`0x006A58C0`) haben dieselbe Struktur (großer Wechsel nach dem Ergebniscode mit Systemmeldungen); die Weiche `0x006A2060` ruft nach einer Prüfung (`0x0055F390`) eine der beiden auf; welche Bedingung genau gilt, wurde nicht ausgewertet.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006A6790`, `0x006A5460`, `0x006A43E0`, `0x006A60D0`, `0x006A6060`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (11)

| Name | Id | Handler |
|---|---:|---|
| `PDSkill_Open` |  | `CBOpen` |
| `PDSkill_Close` |  | `CBClose` |
| `PDSkill_OpenTooltip` |  | `CBOpenTooltip` |
| `PDSkill_CloseTooltip` |  | `CBCloseTooltip` |
| `PDSkill_BuyOpen` |  | `CBBuyOpen` |
| `PDSkill_BuySelectGrid` |  | `CBBuySelectGrid` |
| `PDSkill_BuyBuy` |  | `CBBuyBuy` |
| `PDSkill_BuyUpdateListItem` |  | `CBBuyUpdateListItem` |
| `PDSkill_BuyClose` |  | `CBBuyClose` |
| `PDSkill_BuyOpenTooltip` |  | `CBBuyOpenTooltip` |
| `PDSkill_BuyCloseTooltip` |  | `CBBuyCloseTooltip` |

**Anzeige** (8)

| Name | Id | Handler |
|---|---:|---|
| `PDSKName` | 0 | `FUN_006c7fe0` |
| `PDSKLvExp` | 1 | `CBDisplayLvExp` |
| `PDSKLvExpDegree` | 2 | `CBDisplayExpBar` |
| `PDSKLvExpDegreeMax` | 3 | `CBDisplayExpBar` |
| `PDSKBuyName` | 4 | `CBDisplayBuyName` |
| `PDSKBuyPrice` | 5 | `CBDisplayBuyPrice` |
| `PDSKBuyInvenMoney` | 6 | `CBDisplayBuyInvenMoney` |
| `PDSKBuyTitle` | 7 | `CBDisplayTitle` |

**UserData** (5)

| Name | Id | Handler |
|---|---:|---|
| `PDSK_LISTGRID` |  | – |
| `PDSK_BUYLISTGRID` |  | – |
| `PDSK_BUYINVENMONEY` |  | – |
| `PDSK_BUYACTIVEBUYBTN` |  | – |
| `PDSK_TITLE` | 0 | – |

**Boolean** (1)

| Name | Id | Handler |
|---|---:|---|
| `PDSKActiveBuyBtn` |  | `CBIsActiveBuyButton` |

**Ereignis** (1)

| Name | Id | Handler |
|---|---:|---|
| `PDSK_EVENT_BUY_CONFIRM` |  | `CBConfirmBuy` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `Open` (10 Zeilen, ein Ereignis-Wurf) ist in `CBOpen` eingebaut und nicht als eigene Funktion zu finden.
- Die großen Funktionen (`SetBuyList`, `SetTooltipText`, `OnResult`) wurden nur nach Aufrufer, Größe und Aufgerufenen zugeordnet, nicht verglichen.
- Die Ereignis-Tabelle (zehn Ereignisse über eine Schleife) wurde nicht ausgelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventProduct`](AgcmEventProduct.md), [`AgcmProduct`](AgcmProduct.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIProduct`](AgcmUIProduct.md), [`AgcmUISkill2`](AgcmUISkill2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventProduct`](AgpmEventProduct.md), [`AgpmProduct`](AgpmProduct.md), [`AgpmSkill`](AgpmSkill.md)
- **Erwähnt in:** [`AgcmProductMed`](AgcmProductMed.md), [`AgcmUIProduct`](AgcmUIProduct.md)
