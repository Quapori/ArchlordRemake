# AgcmUIControl (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIControl` (Verwaltung der UI-Steuerelement-Klassen: modale Dialoge, Tooltip-Texturen, Skin-INI, Grid-Item-Texturen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmUIControl/AgcmUIControl.cpp`. Die ~25 Steuerelement-Klassen im Ordner (`AcUIBase`, `AcUIEdit`, `AcUIGrid`, …) sind eigene Klassen und nicht Teil dieser Analyse. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 15 Quellmethoden sind zugeordnet; offen sind `OnClose` und die beiden `SetButtonName`-Überladungen.
- **Build-Variante:** Der Drei-Tasten-Dialog ist vorhanden, der Client ist also wie in [`AgcmUIMain`](AgcmUIMain.md) ein `_AREA_GLOBAL_`-Build.
- **Verhalten:** `OnAddModule`, `OnInit`, `SetMessageDialogPosition`, die Grid-Textur-Zugriffe, `GetCustomTexture`, `UIIniRead` und die beiden INI-Lader folgen der Quelle; Meldungsfenster 412 × 180 Pixel.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIControl.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0062D6A0` | 239 | vtable/String |
| 1 | `OnInit` | `0x0062D790` | 235 | vtable/String |
| 2 | `OnClose` | – | | drei Zeilen, vermutlich eingefaltet |
| 3 | `UIIniRead` | `0x0062ED90` | 236 | von Hand geprüft |
| 4 | `OnDestroy` | `0x0062D880` | 556 | vtable/String |
| 5 | `GetAttachGridItemTextureData` | `0x0062DAB0` | 34 | von Hand geprüft |
| 6 | `GetGridItemTexture` | `0x0062DAE0` | 42 | von Hand geprüft |
| 7 | `GetGridItemTexture` | `0x0062DB10` | 74 | von Hand geprüft |
| 8 | `GetGridItemPointer` | `0x0062DB60` | 11 | von Hand geprüft |
| 9 | `SetMessageDialogPosition` | `0x0062DB70` | 162 | von Hand geprüft |
| 10 | `SetButtonName` | – | | ruft die Dialog-Methoden; kein eindeutiger Anker (die Überladung mit drei Tasten ist in der Quelle leer) |
| 11 | `SetButtonName` | – | | ruft die Dialog-Methoden; kein eindeutiger Anker (die Überladung mit drei Tasten ist in der Quelle leer) |
| 12 | `GetCustomTexture` | `0x0062DD00` | 76 | von Hand geprüft |
| 13 | `_LoadTextureFromINI` | `0x0062E380` | 2558 | von Hand geprüft |
| 14 | `_LoadSoundFromINI` | `0x0062DC60` | 125 | von Hand geprüft |

12 von 15 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `GetGridItemTexture_0062db10` (`0x0062DB10`), `ctor_or_dtor_0062dfa0` (`0x0062DFA0`), `ctor_or_dtor_0062e180` (`0x0062E180`), `~AgcmUIControl` (`0x0062E310`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98` | `m_pcsAgpmGrid` | `OnAddModule` |
| `0xC38` | `m_lItemGridTextureADDataIndex` | `GetAttachGridItemTextureData`, `GetGridItemTexture` |
| `0x1CDB8 / 0x1CDBC` | `Anfang/Ende des Vektors `m_vCustomTexture`` | `GetCustomTexture` |

## Dialogfenster (OnInit 0x0062D790)

`OnInit` initialisiert sechs modale Dialoge, versteckt sie und meldet sie im Engine-Objekt (`DAT_009A1D18`) an. Die Reihenfolge entspricht der Quelle; die sechste (Drei-Tasten-Dialog) gibt es nur im `_AREA_GLOBAL_`-Build, d. h. der 2017er Client ist ein Global-Build:

| Dialog (Quelle) | Member im Modul | Engine-Slot |
|---|---|---|
| `m_clWaitingDialog` | `+0x0CBC` | `+0x12EAC` |
| `m_clMessageDialog` | `+0x32CC` | `+0x12EB0` |
| `m_clOkCancelDialog` | `+0x58D8` | `+0x12EB8` |
| `m_clEditOKDialog` | `+0x10014` | `+0x12EBC` |
| `m_clThreeBtnDialog` (nur Global) | `+0x9D48` | `+0x12EC4` |
| `m_clEditOKCancelDialog` | `+0x157B4` | `+0x12EC0` |

Die Zuordnung der Member zu den Namen folgt der Reihenfolge der Quelle; Offsets und Slots sind aus dem Dekompilat gelesen.
`SetMessageDialogPosition` (`0x0062DB70`) verschiebt alle sechs Dialoge auf (x, y) mit Größe `0x19C × 0xB4` = **412 × 180** Pixel (`AGCMUICONTROL_MESSAGE_WIDTH/HEIGHT`).

## Modulaufbau (OnAddModule 0x0062D6A0)

Holt [`AgcmSound`](AgcmSound.md), [`AgcmFont`](AgcmFont.md) und [`AgpmGrid`](AgpmGrid.md), hängt an jedes Grid-Item ein Textur-Zeiger-Feld an (`AttachGridItemTextureData`, 4 Byte; Index in `+0xC38`) und stellt neun Tooltip-Texturen auf lineare Filterung (`+0x50 = 2`), wie in der Quelle.

## Texturen und Skin (INI)

`UIIniRead` (`0x0062ED90`) liest über den INI-Packing-Manager die UI-Skin-Datei (verschlüsselt oder nicht) und ruft `_LoadTextureFromINI` (`0x0062E380`, 2558 Byte; Schlüssel wie `tt_back` für die Tooltip-Texturen) und `_LoadSoundFromINI` (`0x0062DC60`, setzt den Klickton der Schaltflächen). `GetCustomTexture` (`0x0062DD00`) sucht in einem Vektor aus 0x80-Byte-Einträgen (Name bei `+0`, Textur-Dateiname bei `+0x40`) ohne Beachtung der Groß-/Kleinschreibung.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die `AcUI*`-Steuerelement-Klassen sind nicht analysiert; ihre Quelldateien (`AcUIEdit`, `AcUIGrid`, …) haben fast keine Zeichenketten und wurden hier nicht abgeglichen.
- Die Zuordnung der Dialog-Member zu den Namen beruht auf der Reihenfolge in `OnInit`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmFont`](AgcmFont.md), [`AgcmSound`](AgcmSound.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgpmGrid`](AgpmGrid.md)
- **Erwähnt in:** [`AgcmBillInfo`](AgcmBillInfo.md), [`AgcmGuild`](AgcmGuild.md), [`AgcmItem`](AgcmItem.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmSocialActon`](AgcmSocialActon.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIRemission`](AgcmUIRemission.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgcmUISocialAction`](AgcmUISocialAction.md), [`AgcmUITax`](AgcmUITax.md), [`AgcmUIWantedCriminal`](AgcmUIWantedCriminal.md), [`AuIniManagerA`](AuIniManagerA.md)
