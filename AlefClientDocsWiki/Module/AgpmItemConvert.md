# AgpmItemConvert (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgpmItemConvert` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgpmItemConvert` / `AgpmItemConvert.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x00583C30` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPDITEMCONVERT_OPERATION_*` kennt 13 Operationen, davon 13 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 12 Operationen liegen 2013er Ereignisse vor; 2 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 8 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 2 Paketdefinition(en) in der Quelle, 2 davon im 2017er Konstruktor (`005838b0`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0052A290` | `AgpmItemConvert::unk_0052a290` | unbestimmt |
| `0x0052B510` | `AgpmItemConvert::unk_0052b510` | unbestimmt |
| `0x0052BB30` | `AgpmItemConvert::unk_0052bb30` | unbestimmt |
| `0x00582E60` | `AgpmItemConvert::ctor_or_dtor_00582e60` | merged |
| `0x00582F20` | `AgpmItemConvert::ConAgpdItemConvertADChar` | stage1 |
| `0x00582F60` | `AgpmItemConvert::CBEquipItem` | stage1 |
| `0x00582FE0` | `AgpmItemConvert::CBUnEquipItem` | stage1 |
| `0x00583060` | `AgpmItemConvert::CBInitItem` | stage1 |
| `0x00583120` | `AgpmItemConvert::CBRequestConvert` | stage1 |
| `0x00583190` | `AgpmItemConvert::~AgpmItemConvert` | merged |
| `0x005831B0` | `AgpmItemConvert::ConAgpdItemConvertADItem` | stage1 |
| `0x00583290` | `AgpmItemConvert::ConAgpdItemConvertADItemTemplate` | stage1 |
| `0x005838B0` | `AgpmItemConvert::ctor_or_dtor_005838b0` | merged |
| `0x00583AF0` | `AgpmItemConvert::OnAddModule` | merged |
| `0x00583C30` | `AgpmItemConvert::OnReceive` | merged |
| `0x00595EE0` | `AgpmItemConvert::ProcessRuneConvert` | strmatch |
| `0x00583320` | `AgpmItemConvert::OnOperationAdd` | casemap:AgpmItemConvert |

17 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 10/10/10 | ja | ja |
| `m_csPacketTID` | 1/1/1 | 8/8/8 | ja | ja |

**m_csPacket** (10 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | character id |
| 2 | `0x4` | INT32 | 1 | item id |
| 3 | `0x8` | INT32 | 1 | catalyst (rune, spiritstone) item id |
| 4 | `0x10` | INT8 | 1 | action result |
| 5 | `0x20` | INT8 | 1 | # of physical convert |
| 6 | `0x40` | INT8 | 1 | # of socket |
| 7 | `0x80` | INT8 | 1 | # of converted socket |
| 8 | `0x100` | INT32 | 1 | add convert item tid |
| 9 | `0x200` | PACKET | 1 | converted item tid list |

**m_csPacketTID** (8 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | converted item tid list |
| 1 | `0x2` | INT32 | 1 |  |
| 2 | `0x4` | INT32 | 1 |  |
| 3 | `0x8` | INT32 | 1 |  |
| 4 | `0x10` | INT32 | 1 |  |
| 5 | `0x20` | INT32 | 1 |  |
| 6 | `0x40` | INT32 | 1 |  |
| 7 | `0x80` | INT32 | 1 |  |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | `0x00583320` `OnOperationAdd` | `ADD` | = (2013 = 2017) |
| 1 | `REQUEST_PHYSICAL_CONVERT` | inline | – | keine Callback-Ereignisse (beide) |
| 2 | `REQUEST_ADD_SOCKET` | `0x0053A440` `FUN_0053a440` | – | keine Callback-Ereignisse (beide) |
| 3 | `REQUEST_RUNE_CONVERT` | inline | – | 2017 ⊂ 2013 |
| 4 | `REQUEST_SPIRITSTONE_CONVERT` | inline | – | 2017 ⊂ 2013 |
| 5 | `RESPONSE_PHYSICAL_CONVERT` | inline | – | 2017 ⊂ 2013 |
| 6 | `RESPONSE_ADD_SOCKET` | inline | – | 2017 ⊂ 2013 |
| 7 | `RESPONSE_SPIRITSTONE_CONVERT` | inline | – | 2017 ⊂ 2013 |
| 8 | `RESPONSE_RUNE_CONVERT` | inline | – | 2017 ⊂ 2013 |
| 9 | `RESPONSE_SPIRITSTONE_CHECK_RESULT` | inline | – | 2017 ⊂ 2013 |
| 10 | `RESPONSE_RUNE_CHECK_RESULT` | inline | – | 2017 ⊂ 2013 |
| 11 | `CHECK_CASH_RUNE_CONVERT` | inline | – | keine Callback-Ereignisse (beide) |
| 12 | `SOCKET_INITIALIZE` | inline | `PROCESS_SOCKET_INITIALIZE` | = (2013 = 2017) |

## Abweichungen zur 2013er Messung

| Op | Name | nur 2013 | nur 2017 |
|---:|---|---|---|
| 3 | `REQUEST_RUNE_CONVERT` | AGPDITEMCONVERT_CB_PROCESS_RUNE_CONVERT | – |
| 4 | `REQUEST_SPIRITSTONE_CONVERT` | AGPDITEMCONVERT_CB_PROCESS_SPIRITSTONE_CONVERT | – |
| 5 | `RESPONSE_PHYSICAL_CONVERT` | AGPDITEMCONVERT_CB_RESULT_PHYSICAL_CONVERT, AGPDITEMCONVERT_CB_UPDATE | – |
| 6 | `RESPONSE_ADD_SOCKET` | AGPDITEMCONVERT_CB_RESULT_SOCKET_CONVERT, AGPDITEMCONVERT_CB_UPDATE | – |
| 7 | `RESPONSE_SPIRITSTONE_CONVERT` | AGPDITEMCONVERT_CB_RESULT_SPIRITSTONE_CONVERT, AGPDITEMCONVERT_CB_UPDATE | – |
| 8 | `RESPONSE_RUNE_CONVERT` | AGPDITEMCONVERT_CB_RESULT_RUNE_CONVERT, AGPDITEMCONVERT_CB_UPDATE | – |
| 9 | `RESPONSE_SPIRITSTONE_CHECK_RESULT` | AGPDITEMCONVERT_CB_ASK_REALLY_SPIRITSTONE_CONVERT, AGPDITEMCONVERT_CB_RESULT_SPIRITSTONE_CONVERT | – |
| 10 | `RESPONSE_RUNE_CHECK_RESULT` | AGPDITEMCONVERT_CB_ASK_REALLY_RUNE_CONVERT, AGPDITEMCONVERT_CB_RESULT_RUNE_CONVERT | – |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 19, eingebaut: 9, gemeinsamer Rumpf: 18, nicht im Client: 10, ohne Kandidat: 46, zugeordnet: 25.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsSocketInitializable` | 23 | `0x00594B20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessSpiritStoneConvert` | 23 | `0x005942D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSpiritStoneConvertable` | 31 | `0x00593750` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBRequestSpiritStoneConvert` | 64 | `0x00593E40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SpiritStoneConvert` | 50 | `0x005939C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetNumSpiritStone` | 37 | `0x005938C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSocketConvertable` | 60 | `0x00594EA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidCatalyst` | 14 | `0x005960A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPhysicalConvertable` | 29 | `0x00596280` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalConvertPoint` | 12 | `0x00583F10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DecodeConvertHistory` | 90 | `0x00583490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsValidSpiritStone` | 16 | `0x00593800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsWeapon` | 11 | `0x00594A80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitializeSpiritStoneConvert` | 116 | `0x00596450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ApplyPhysicalConvert` | 58 | `0x00593F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitializePhysicalConvert` | 72 | `0x00593B00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBRequestRuneConvert` | 81 | `0x00595810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RuneConvert` | 116 | `0x005954D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsProperLevel` | 16 | `0x00595190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketSocketInitialize` | 20 | `0x00594570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketCheckCashRuneConvert` | 20 | `0x00594510` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestSpiritStoneConvert` | 20 | `0x005944B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestRuneConvert` | 20 | `0x00594450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestSocketAdd` | 19 | `0x005943F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestPhysicalConvert` | 20 | `0x00594390` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetTotalPhysicalConvertPoint` (`0x00583740`), `GetTotalRuneConvertPoint` (`0x00583740`), `CalcPhysicalConvertFactor` (`0x00596670`), `GetNumPhysicalConvert` (`0x00596120`), `GetPhysicalItemRank` (`0x005961E0`), `GetPhysicalItemRank` (`0x005961E0`), `IsRuneConvertable` (`0x00595430`), `IsValidRuneItem` (`0x00595430`), `IsProperPart` (`0x00595300`), `IsAntiNumber` (`0x00595430`), `IsConvertedAttribute` (`0x00595990`), `GetConvertedExtraType` (`0x00595990`), `GetNumSocket` (`0x00596120`), `GetNumConvertedSocket` (`0x00596120`), `IsArmour` (`0x00594AE0`), `IsEtc` (`0x00594AE0`), `AddSpiritStoneConvert` (`0x00596670`), `CalcSpiritStoneConvertFactor` (`0x00596670`), `IsEgoItem` (`0x00594AE0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventItemConvert`](AgcmEventItemConvert.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmItem`](AgcmItem.md), [`AgcmItemConvert`](AgcmItemConvert.md), [`AgpmCombat`](AgpmCombat.md), [`AgpmItem`](AgpmItem.md)
