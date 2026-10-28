# Prüfung des Wikis auf Richtigkeit

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Prüfung des Wikis `AlefClientDocsWiki/` (337 Dateien, davon 255 Modulseiten) gegen die Exporte `rea_export/` (`fnindex.json`, `names_all*.tsv`, `vtables.tsv`, `all_named.c`), die EP8-Quelle und die Handentscheidungen `rea_export/gapwork/decisions.tsv`. Build: 2017er `AlefClient.exe`, SHA-256 `20009faa…e067b`. Geprüft wurde maschinell und, wo eine Abweichung auftrat, von Hand gegen Quelle und Dekompilat. **Nicht geprüft** ist der Fließtext der Seiten (Verhalten, Offsets, Paketfelder) gegen das Dekompilat; das sind mehrere tausend Einzelaussagen, hier wurden nur Zuordnungen, Zahlen und Verweise geprüft.

## Ergebnis in Kürze

| Prüfung | Ergebnis | Maßnahme |
|---|---|---|
| Links zwischen Seiten | 4.768 geprüft, 0 kaputt | keine |
| Abdeckungszahlen („X von Y Quellmethoden“) in 114 Modulseiten gegen die Tabellen | 0 Abweichungen | keine |
| Handentscheidungen (625 Zeilen `decisions.tsv`) gegen Namenstabelle | 0 Abweichungen (eine Adresse doppelt, [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md):_CheckConditionC` `0x005726D0`, gleicher Name) | keine |
| Adresse und Name in 6.136 Tabellenzeilen der Modulseiten gegen die Namenstabelle | 273 Abweichungen auf 155 Adressen, danach 239 | siehe unten |
| Lückenregister gegen Namenstabelle | 72 Zuordnungen im Register ohne Deckung in der Namenstabelle | Register neu erzeugt |
| Vtable-Zugehörigkeit (RTTI) gegen Klassenname | 22 falsche Klassennamen | umbenannt (`names_all308.tsv`) |
| Namen mit mehreren Adressen, obwohl die Quelle weniger Definitionen hat | 5 Namen | 1 Fehler behoben, 4 offen |
| Gesamtzahlen in Übersichten | 3 veraltete Angaben | aktualisiert |

## 1. Zuordnungen im Register ohne Deckung (behoben)

Die Lückenregister führten 72 Methoden als „zugeordnet“ mit dem Beleg „eindeutiger Treffer (erster Lauf)“, obwohl die Namenstabelle an dieser Adresse inzwischen einen anderen Namen oder keinen Namen trug. Ursache: `gapclose.py register` übernahm die Treffer des ersten Laufs (`gm_Luecken_PHASE*.tsv`) ungeprüft in jedes neue Register, auch wenn die Handprüfung sie verworfen oder umbenannt hatte. Die Modulseiten übernahmen diese Zeilen über den Nachtrag.

Beispiele für falsche Zeilen, die dadurch auf den Seiten standen:

| Seite | Zeile | Befund |
|---|---|---|
| [`AgcmUIItem`](../Module/AgcmUIItem.md) | `_SetItemToolTipDetailRequireClass` `0x00627B20`, `_SetItemToolTipDetailRequireRace` `0x006271A0` | Die Funktionen sind `SetItemToolTipAmuletInfo` (713 Byte, „+%d %%“ Verteidigung) und `SetItemToolTipSpiritStoneInfo` (1.710 Byte); die Namen aus dem ersten Lauf waren falsch |
| `AgcmUIItem` | `OnSendBuyNPCTradeItem` `0x00748459` | Adresse liegt mitten in einer anderen Funktion (Exportartefakt, Dekompilat beginnt mit `in_ZF`) |
| `AgcmUIItem` | `SetItemToolTipSpiritStoneInfo`, `_SetItemToolTipDetailHeroicDamage`, `_SetItemToolTipDetailWeaponDamage` | dieselben zwei Adressen (`0x00629F20`, `0x00629CB0`) waren mehreren Methoden gleichzeitig zugeordnet |
| [`AgcmRender`](../Module/AgcmRender.md) | `UpdateOBufferAndDrawNotTest` `0x005B9EF0` | Das Binary setzt die Höhe auf `Kamerahöhe * 2` und gehört damit zu `UpdateOBufferAndDrawTest`; dieselbe Adresse stand für beide Methoden |
| [`AgcmUIManager2`](../Module/AgcmUIManager2.md) | `GetEventMap` `0x005E2950` | Die Funktion hat keine Bereichsprüfung gegen `m_lMaxUIEvents`, passt also zu `AgcaUIManager2::GetUI`, nicht zu `GetEventMap` |
| `AgcmCharacter` | `DetachRide` `0x00609D60` | 268 Byte, holt Module per Namen ([`AgcmCamera2`](../Module/AgcmCamera2.md), [`AgcmEventNature`](../Module/AgcmEventNature.md), …), steht in der Vtable von [`AgcmUILogin`](../Module/AgcmUILogin.md) an Slot 2 (`OnInit`); `DetachRide` hat 83 Zeilen mit anderem Inhalt |

Korrektur: `gapclose.py` übernimmt Treffer des ersten Laufs nur noch, wenn die aktuelle Namenstabelle den Namen an der Adresse trägt. Die Register wurden neu erzeugt. Folge:

| Register | zugeordnet vorher | nachher |
|---|---:|---:|
| Phase 1 | 725 | 709 |
| Phase 4 | 429 | 372 |

Der Beleg der verbleibenden Treffer des ersten Laufs heißt jetzt „automatischer Treffer (erster Lauf), nicht von Hand geprüft“.

## 2. Falsche Klassennamen nach Vtable (behoben)

Abgleich: Ein Funktionsname `B::m` ist verdächtig, wenn die Funktion in keiner Vtable von `B` steht, wohl aber in der Vtable einer anderen Klasse (`rea_export/vtables.tsv`). Gefunden wurden 26 Fälle, 22 davon korrigiert (`gm_Korrektur_Wiki.tsv`; `names_all308.tsv`), dazu ein Fund aus der Doppelnamen-Prüfung (`gm_Korrektur_Wiki2.tsv`; `names_all309.tsv`):

- **15 Funktionen von `MyEngine`, genannt `AgcEngine::…`.** Die Vtable von `MyEngine` (`0x00899954`) überschreibt 18 Slots der Vtable von `AgcEngine` (`0x008998AC`). Die Vtable-Namensvergabe hatte die Basisklasse genannt. Betroffen unter anderem `OnPostRegisterModule` (`0x00410EB0`, 19.614 Byte), `OnRender` (`0x004106B0`), `OnCameraStateChange` (`0x00415BA0`), `OnPreRegisterModule` (`0x00410DC0`). Die Größen passen nicht zu den EP8-Basismethoden (z. B. hat `AgcEngine::OnRender` in der Quelle 151 Zeilen, das Binary an dieser Adresse 36 Byte).
- **`AgcmUILogin::OnInit`** (`0x00609D60`) statt des falschen `AgcmCharacter::DetachRide`.
- **6 Destruktoren** (`AcUIScrollButton`, [`AgcmCashMall`](../Module/AgcmCashMall.md), [`AgcmPrivateTrade`](../Module/AgcmPrivateTrade.md), `AcUIGridItem`, `AcUIRecruitWrite`, `AgcdEffAnim_Camera`), die mit dem Namen der Basisklasse und Adresssuffix geführt wurden.
- **`0x005D71A0`** war als zweites `AgcmEventNature::CBOnSetAutoLoadChange` geführt. Es passt nicht zur Quelle (kein `switch` über die Kartenansicht), ist jetzt wieder unbenannt; die Beschreibung im Bericht `AgcmEventNature` wurde korrigiert.

Nicht geändert (vier weitere Funde): `TiXmlNode::ToUnknown`, `TiXmlBase::Parse`, `TiXmlBase::~TiXmlBase_00873180` und `CCSLog::ctor_or_dtor_007221F0` gehören gemeinsam zu mehreren Klassen, die Vtable-Lage allein entscheidet dort nicht.

## 3. Abweichungen zwischen Seite und Namenstabelle, die keine Fehler sind

Die verbleibenden 239 Abweichungen zwischen dem Namen auf der Seite und dem Namen in der Tabelle fallen in diese Gruppen. Sie sind erklärbar und stehen auf den Seiten als „gleiche Adresse wie …“; geändert wurde nichts.

| Gruppe | Anzahl Adressen | Erklärung |
|---|---:|---|
| Überladung mit Namenszusatz (`_key`, `_ptr`, `_both` …) | 77 | die Tabelle muss Überladungen unterscheiden, die Seite führt den Quellnamen |
| Sammeladresse (Stub, vom Linker zusammengefaltet) | 13 | z. B. `0x0067AC90` (leere Funktion), auf die 86 Methoden verschiedener Klassen zeigen; dort ist der Name Konvention, keine Eindeutigkeit |
| Zwilling mit identischem Quelltext | 18 | z. B. `CBChargingInventoryAMoveItem` und `…BMoveItem` (192 Zeilen, wortgleich); das Binary kann nicht unterscheiden, welcher Name gilt |
| Name nur im Bericht, in der Tabelle noch `FUN_…` | 6 | Bericht ist weiter als die Tabelle |
| Wrapper-Stubs mit anderem Klassennamen (`AgcWindow::OnIdle` u. a.) | 4 | Stub-Rümpfe, die mehreren Klassen dienen |

## 4. Gesamtzahlen (behoben)

- [`ALEFCLIENT_2017_FUNKTIONSKARTE.md`](Funktionskarte.md): Die Zeile „Stand: 4.817 benannte Funktionen … von 20.910“ stammte vom Arbeitsbeginn. Sie ist jetzt als historisch gekennzeichnet; ein Absatz „Aktueller Stand“ nennt 8.657 Namenseinträge (7.807 mit Klassenname), 25.691 Funktionen im Export und die Herkunft der Namen nach Quelle.
- [`ALEFCLIENT_2017_LUECKENPLAN.md`](Lueckenplan.md): Der Kopf nannte „zur Freigabe, es wird nichts ausgeführt“ und den Stand `names_all264`; der Plan ist ausgeführt. Außerdem standen dort zwei Aussagen, die dem späteren Befund widersprachen („Backtest 0 Fehler“, „217 verbleibende Kandidaten“). Beides ist angeglichen.
- [`ALEFCLIENT_2017_MODULUEBERSICHT.md`](Modul-Uebersicht.md): Der Kopf nannte `names_all13.tsv` als Quelle der Spalte „benannt“, tatsächlich ist es die jeweils letzte Tabelle; die Spalte war außerdem nicht aktuell und wurde neu erzeugt.

## 5. Offene Punkte (nicht behoben)

1. **Automatische Namen (`gapclose`).** Alle 496 Namen mit der Quelle `gapclose` wurden anschließend gegen Quelle und Dekompilat gelesen (Abschnitt 6). Von Hand geprüft sind damit auch die Namen, die vorher nur „automatisch, nicht von Hand geprüft“ hießen; die Kennzeichnung in den Registern bleibt als Herkunftsangabe stehen.
2. **Namen mit mehreren Adressen ohne Quelldefinition:** [`AgpmAuction`](../Module/AgpmAuction.md):GetField` (`0x0055E200`, `0x0055E2D0`), [`AgpmTax`](../Module/AgpmTax.md):Reset` (`0x00577F10`, 47 Byte; `0x005785D0`, 597 Byte), [`AgpmBillInfo`](../Module/AgpmBillInfo.md):GetCharacterLock` (`0x00587C30`, `0x00587CF0`) und `StackWalker::ShowCallstack` (`0x004F5100`, `0x004F6120`). Die Namen stammen aus der Case-Zuordnung bzw. einer Fremdbibliothek; welche Adresse zu welcher Überladung gehört, ist nicht belegt.
3. **Funktionsgrenzen im Export.** `SetOcLineCheck` (`0x005B2840`), `GetOcLineCheck` (`0x005B2870`) und `SetCharacterLightEffect` (`0x005B28B0`) im Bericht `AgcmRender` liegen laut `fnindex.json` innerhalb der Funktion `0x005B2850` (542 Byte). Entweder fehlen dem Export Funktionsgrenzen oder die Adressen sind Einsprünge; ungeprüft.
4. **Zwillings-Paare** (Abschnitt 3) bleiben mehrdeutig, weil die Quelltexte gleich sind. Die Seiten nennen die gemeinsame Adresse; eine Entscheidung ist ohne Laufzeitbeobachtung nicht möglich.
5. **Seiten zum 2013er Build und Netzwerkfolgen** (`Netzwerk/`, `Start-und-Login/`, `Welt-und-Engine/`, `Daten-und-Werkzeuge/`): Hier wurden nur Links geprüft. Adressen in diesen Seiten gelten für den 2013er Build und lassen sich mit den 2017er Exporten nicht prüfen (86 Adressen fallen dort in die Mitte 2017er Funktionen, was erwartbar ist).
6. **Fließtext der Modulseiten** (Feldoffsets, Paketaufbau, Ablaufbeschreibungen) ist nicht systematisch gegen das Dekompilat gelesen worden.

## Werkzeuge der Prüfung

`wikicheck_1.py` bis `wikicheck_4.py` (Reihenfolge 1, 2; 3 und 4 unabhängig): (1) Tabellenzeilen der Modulseiten parsen (Spalte Methode, Spalte Adresse) und gegen die letzte `names_all*.tsv` vergleichen; (2) Abweichungen nach Namenszusatz, Zwilling (Quelltexte nach Ersetzen des Namens gleich), Sammeladresse und echtem Widerspruch einteilen; (3) gleiche Adresse mit verschiedenen Namen auf einer Seite und Adressen mitten in Funktionen; (4) Abdeckungszahlen („X von Y“) gegen die Tabellen. Die Vtable-Prüfung (Abschnitt 2), der Registervergleich (Abschnitt 1) und die Doppelnamen-Prüfung wurden als einmalige Auswertungen ausgeführt; dauerhaft eingebaut ist nur die Registerkorrektur in `gapclose.py` (Bedingung `nm_all.get(a.zfill(8)) == n`).

## 6. Einzelprüfung der automatischen Namen

Geprüft wurden alle 496 Namen der Namenstabelle mit der Quelle `gapclose` (nach `names_all309.tsv`). Vorgehen: Quelltext der Methode und Dekompilat der Adresse nebeneinander gelesen; zusätzlich maschinell geprüft: Adresse auf 16 Byte ausgerichtet, Klasse in der Vtable der Adresse, Größe gegen Zeilenzahl, Zeichenketten und Aufrufe von Quelle und Binary. Gelesen wurden die 205 am schwächsten belegten (keine Zeichenkette und weniger als zwei passende Aufrufe, oder eine maschinelle Auffälligkeit), dazu 192 der 291 stärker belegten; die übrigen rund 100 stützen sich auf übereinstimmende Zeichenketten oder mindestens vier passende Aufrufe und wurden nicht einzeln gelesen.

**Ergebnis: 14 von 496 Namen waren falsch oder nicht belegbar** (rund 3 %, deutlich weniger als die 13 % des Prüfstands). Korrigiert in `gm_Korrektur_gapclose.tsv` (`names_all310.tsv`):

| Adresse | bisheriger Name | Befund | jetzt |
|---|---|---|---|
| `0x00717720` | [`AgcaEffectData2`](../Module/AgcaEffectData2.md):Delete` | Destruktor mit Ausnahmerahmen und Vtable-Zuweisung, passt nicht zu einer 4-Zeilen-Methode | `AgcmEventEffectData::ctor_or_dtor_00717720` |
| `0x005E20F0`, `0x005E2350`, `0x005E2430`, `0x005E24C0` | `AgcmUIManager2::GetFunction`, `GetDisplay` (zweimal), `GetBoolean` | 28-Byte-Rümpfe ohne die Bereichsprüfung der Quelle (`lIndex >= m_lMax…`); es sind Getter des darunterliegenden Verwalters, nicht die Methoden von `AgcmUIManager2` | unbenannt |
| `0x00551bd0` | `AgpaGuild::GetGuild` | Binary holt die Gilde über Zeichenkette und angehängte Daten, die Quelle kleinschreibt und prüft die Länge | unbenannt |
| `0x0058CDC0`, `0x0058CEB0` | `AgpaComposeTemplate::Get` (zweimal) | 22-Byte-Getter, gleiche Form wie `AgpaQuestTemplate::Get`, `AgpaRefineItem::Get` und weitere; Klasse nicht belegbar | unbenannt |
| `0x0058D650` | [`AgpmItem`](../Module/AgpmItem.md):RemoveItemFromCashInventory` | eine von drei Adressen für eine Quelldefinition, passt nicht zur Überladung `(lCID, pcsItem)` | unbenannt |
| `0x0058D880` | `AgpmItem::GetChargingInventory` | 338 Byte mit denselben Aufrufen wie `AddItemToChargingInventoryResult`, die Quelle ist ein 3-Zeilen-Rumpf | unbenannt |
| `0x005205E0` | [`AgpmSiegeWar`](../Module/AgpmSiegeWar.md):GetSiegeWarInfo` | Paketleser (`GetField`), nicht der Feldzugriff der Quelle | unbenannt |
| `0x006FD7FD`, `0x00748459` | `AcUIEdit::DrawCandidateWindow`, `AgcmUIAccountCheck::CB_OnDisConnect` | Adressen liegen mitten in Funktionen (nicht 16 Byte ausgerichtet, Dekompilat beginnt mit `in_ZF`) | unbenannt |
| `0x00572000` | [`AgpmEventProduct`](../Module/AgpmEventProduct.md):GetBuyCost` | ist der Aufgerufene: ruft `GetSkillTemplate` und dann die zweite Überladung; der Aufrufer mit Nullprüfung ist `0x0056FC30` | `AgpmEventSkillMaster::GetBuyCost_2` |

Beim Lesen aufgefallen, aber nicht entscheidbar: viele gleich gebaute Kleinstfunktionen (Getter mit `GetObject`, `GetADCharacter`, Paketerzeuger mit nur `MakePacket`-Aufruf) unterscheiden sich nur durch Offsets oder Konstanten. Für sie gilt die Adressreihenfolge der Quelle; falsch zugeordnete Vertauschungen innerhalb einer solchen Familie (z. B. `IsSafePvPMode` / `IsFreePvPMode` / `IsCombatPvPMode`, `SendTradeLock` / `SendTradeUnlock` / `SendReadyToExchange`) sind damit nicht ausgeschlossen.
