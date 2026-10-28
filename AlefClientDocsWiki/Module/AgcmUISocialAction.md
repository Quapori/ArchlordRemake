# AgcmUISocialAction (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUISocialAction` (Fenster der sozialen Aktionen (Emotes)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUISocialAction/AgcmUISocialAction.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 15 von 18 Quellmethoden sind einer Adresse zugeordnet (`DragDrop` und `OnIdle` als gemeinsame Rümpfe, `DLClick`/`RClick` als ein zusammengefalteter Rumpf); `OnSocialUIOpen`, `OnSocialUIClose` und `ActionStart` sind in ihre Aufrufer eingebaut und haben keine eigene Adresse.
- **Paket:** Das Auslösen sendet ein Charakter-Paket mit Operation 16 (soziale Animation) und der Gitter-ID als Animationsnummer.
- **UI:** 9 Funktionen, 2 Ereignisse, 1 Benutzerdatum – wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUISocialAction.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00680FB0` | 530 | vtable/String |
| 1 | `OnInit` | `0x00680CB0` | 123 | vtable/String |
| 2 | `OnDestroy` | `0x00680D30` | 17 | vtable/String |
| 3 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf (Vtable-Slot 3)` (vom Linker zusammengefaltet) |
| 4 | `OnSocialUIOpen` | – | | in die drei Fenster-Callbacks eingebaut |
| 5 | `OnSocialUIClose` | – | | in die drei Fenster-Callbacks eingebaut |
| 6 | `CBSocialActionOpenUI` | `0x00680D50` | 66 | UI-Registrierung |
| 7 | `CBSocialActionCloseUI` | `0x00680DA0` | 44 | UI-Registrierung |
| 8 | `CBSocialActionToggleUI` | `0x00680DD0` | 116 | UI-Registrierung |
| 9 | `CBSocialActionDragDrop` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 10 | `CBSocialActionDragEnd` | `0x00680E50` | 50 | UI-Registrierung |
| 11 | `CBSocialActionDLClick` | `0x00680F70` | 49 | manual |
| 12 | `CBSocialActionRClick` | `0x00680F70` | 49 | gleiche Adresse wie `mit CBSocialActionDLClick zusammengefaltet (ICF)` (vom Linker zusammengefaltet) |
| 13 | `CBSocialActionFocus` | `0x00680E90` | 52 | UI-Registrierung |
| 14 | `CBSocialActionNotFocus` | `0x00680ED0` | 21 | UI-Registrierung |
| 15 | `CBOpenQuickBeltToolTip` | `0x00680EF0` | 52 | Callback-Registrierung |
| 16 | `CBCloseQuickBeltToolTip` | `0x00680F30` | 21 | Callback-Registrierung |
| 17 | `ActionStart` | – | | in CBSocialActionDLClick eingebaut (ruft SendSocialAnimation) |

15 von 18 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUISocialAction` (`0x00680BD0`), `ctor_or_dtor` (`0x00680C50`), `~AgcmUISocialAction` (`0x00680F50`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB98` | `Beginn des Teilobjekts [`AgcmSocialActon`](AgcmSocialActon.md) (Datenklasse)` | `OnAddModule` (`SetModule`) |
| `0xBA8` | `Gitter `m_cGrid` (Teilobjekt +0x10; Benutzerdatum `SocialActionGrid`)` | `OnAddModule`, `Create` |
| `0x2938 / 0x293C` | `Zeiger auf `AgcmCharacter` / [`AgcmUIMain`](AgcmUIMain.md)` | `OnAddModule` |
| `0x2940` | `Flag „Fenster offen“ (`m_bIsOpen`)` | `CBSocialActionOpenUI`, `…CloseUI`, `…ToggleUI` |
| `0x2944 / 0x2948` | `Ereignis-ID Öffnen / Schließen` | `OnAddModule` |
| `0x294C` | `Benutzerdatum `SocialActionGrid`` | `OnAddModule` |

## Umfang

`AgcmUISocialAction.cpp` ist die UI-Seite (Fenster „Soziale Aktionen“), `AgcmSocialAction.cpp` die Datenklasse `AgcmSocialActon` (Schreibweise der Quelle; Klasse für Gitter, Symbole und Tooltip) mit der Hilfsklasse `SocialAction`. Die Datenklasse hat einen eigenen Bericht: [AgcmSocialActon](AgcmSocialActon.md). Das Modul erbt von `AgcModule` und `AgcmSocialActon`; das Teilobjekt `AgcmSocialActon` beginnt bei `+0xB98` (dort die vier Zeiger von `SetModule`, das Gitter bei `+0xBA8`, die Liste bei `+0xBCC`), die eigenen Zeiger des Moduls folgen ab `+0x2938`.

## Vtable

Vtable bei `0x008CB4F4`: Slot 0 Destruktor `0x00680F50`, 1 `OnAddModule` (`0x00680FB0`), 2 `OnInit` (`0x00680CB0`), 3 `OnIdle` (der gemeinsame Rumpf `0x0067FAB0`, wie die Slots 4 und 5), 6 `return TRUE`-Rumpf `0x0067AC90`, 7 `OnDestroy` (`0x00680D30`).

## Registrierung (OnAddModule, 0x00680FB0)

Holt [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgpmGrid`](AgpmGrid.md) (übergibt sie an `SetModule`), `AgcmCharacter` und `AgcmUIMain`, meldet bei `AgcmUIMain` die beiden Schnellleisten-Tooltips an (`CBOpenQuickBeltToolTip` `0x00680EF0`, `CBCloseQuickBeltToolTip` `0x00680F30`) und legt an:

| Art | Name | Handler |
|---|---|---|
| Funktion | `CBSocialActionOpenUI` | `0x00680D50` |
| Funktion | `CBSocialActionCloseUI` | `0x00680DA0` |
| Funktion | `CBSocialActionToggleUI` | `0x00680DD0` |
| Funktion | `CBSocialActionDragDrop` | `0x0067AC90` (gemeinsamer Rumpf) |
| Funktion | `CBSocialActionDragEnd` | `0x00680E50` |
| Funktion | `CBSocialActionDLClick` | `0x00680F70` |
| Funktion | `CBSocialActionRClick` | `0x00680F70` (derselbe Rumpf) |
| Funktion | `CBSocialActionFocus` | `0x00680E90` |
| Funktion | `CBSocialActionNotFocus` | `0x00680ED0` |
| Ereignis | `SocialActionOpenUI`, `SocialActionCloseUI` | – |
| Benutzerdatum | `SocialActionGrid` (Gitter, 0x24 Byte, ab `+0xBA8`) | – |

## Öffnen und Schließen

`CBSocialActionOpenUI` setzt das Flag „offen“ (`+0x2940`), aktualisiert das Gitter-Benutzerdatum und wirft `SocialActionOpenUI`. `CBSocialActionCloseUI` löscht das Flag und wirft `SocialActionCloseUI`. `CBSocialActionToggleUI` wählt je nach Flag den einen oder anderen Weg. `OnSocialUIOpen` und `OnSocialUIClose` sind in diese drei Funktionen eingebaut.

## Aktion auslösen (DLClick / RClick)

Doppelklick und Rechtsklick haben denselben Rumpf (`0x00680F70`; der Linker hat sie zusammengefaltet): Sie holen das angeklickte Gitterfeld (`GetGridItemClickInfo`, `0x0072B6F0`) und rufen `ActionStart(m_lItemID)`, das im Binary eingebaut ist und `AgcmCharacter::SendSocialAnimation` (`0x005A0720`) aufruft. Diese Funktion sendet nur, wenn der eigene Charakter existiert, nicht reitet (`+0x790` = 0), nicht verwandelt ist (außer als Archlord: `IsArchlord`, `0x0057B880`; Flag `+0x4C4`) und nicht tot ist (Aktionsstatus `+0x52A` ≠ 2); das entspricht den vier Prüfungen der Quelle. Das Paket ist ein Charakter-Paket (Typ 2) mit Operation 16 (`AGPMCHAR_PACKET_OPERATION_SOCIAL_ANIMATION`), Charakter-ID und der Animationsnummer (`UINT8`); es wird mit `MakePacket` (`0x004EA2D0`) und `SendPacket` (`0x004E45A0`) gesendet. Die Animationsnummer ist die Gitter-ID des Symbols (Zeile × 4 + Spalte).

## Tooltip

`CBSocialActionFocus` (`0x00680E90`) prüft, dass das Gitter ein Tooltip-Feld hat und dessen Typ `AGPDGRID_ITEM_TYPE_SOCIALACTION` (0x40) ist, und ruft `OpenTooltip(m_lItemID)`. `CBOpenQuickBeltToolTip` hat denselben Rumpf mit dem Gitter aus dem Parameter statt aus der Quelle des Steuerelements. `CBSocialActionNotFocus` und `CBCloseQuickBeltToolTip` rufen `CloseTooltip` und liefern 1.

## Laden (OnInit)

`OnInit` (`0x00680CB0`) löscht das Flag, baut den Dateinamen `Ini\%sSocialAction.txt` mit der Sprache aus dem Engine-Objekt (`+0x12CD8`) und ruft `Load(Name, TRUE)` (die Entschlüsselung ist im Binary fest `TRUE`, da `_BIN_EXEC_` nicht gesetzt ist). Bei Erfolg folgt wie in der Quelle ein zweiter `Create`-Aufruf (`return Create()`), nicht `return TRUE`. `OnDestroy` (`0x00680D30`) ruft `Destory` und liefert 1.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00680FB0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (9)

| Name | Id | Handler |
|---|---:|---|
| `CBSocialActionOpenUI` |  | – |
| `CBSocialActionCloseUI` |  | – |
| `CBSocialActionToggleUI` |  | – |
| `CBSocialActionDragDrop` |  | `Element::GetSize` |
| `CBSocialActionDragEnd` |  | – |
| `CBSocialActionDLClick` |  | `FUN_00680f70` |
| `CBSocialActionRClick` |  | `FUN_00680f70` |
| `CBSocialActionFocus` |  | – |
| `CBSocialActionNotFocus` |  | – |

**Ereignis** (2)

| Name | Id | Handler |
|---|---:|---|
| `SocialActionOpenUI` | 0 | – |
| `SocialActionCloseUI` | 0 | – |

**UserData** (1)

| Name | Id | Handler |
|---|---:|---|
| `SocialActionGrid` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierung, `OnInit`, Öffnen/Schließen, Klick-Rumpf, Tooltip).

## Grenzen

- `AgcmCharacter::SendSocialAnimation` wurde nur in den Grundzügen gelesen (Paketaufbau, Operation 16); die Bedingungen vor dem Senden (Zustandsfelder `+0x790`, `+0x52A`) sind nicht gegen die Quelle abgeglichen.
- Die Datei `Ini\<Sprache>SocialAction.txt` selbst wurde nicht ausgewertet; sie liegt im Client-Verzeichnis (verschlüsselt).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 5, gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcModule`](AgcModule.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmSocialActon`](AgcmSocialActon.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmGrid`](AgpmGrid.md)
- **Erwähnt in:** [`AgcmSocialActon`](AgcmSocialActon.md)
