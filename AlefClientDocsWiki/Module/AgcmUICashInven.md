# AgcmUICashInven (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmUICashInven` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmUICashInven` / `AgcmUICashInven.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x004E3420` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Kein Operationsschalter:** In der Quelle bzw. im Binary wurde keine Verzweigung nach Operationen erkannt (`OnReceive` im Binary: 8 Byte).
- **Ereignisse:** `OnReceive` löst bis Tiefe 3 keine `EnumCallback`-Aufrufe aus.
- **Paketlayout:** 0 Paketdefinition(en) in der Quelle, 0 davon im 2017er Konstruktor (`None`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x004E3420` | `AgcmUICashInven::OnReceive` | merged |
| `0x006CF530` | `AgcmUICashInven::OnInit` | merged |
| `0x006CF570` | `AgcmUICashInven::AddUserData` | strmatch |
| `0x006CF5D0` | `AgcmUICashInven::AddEvent` | strmatch |
| `0x006CF620` | `AgcmUICashInven::OnUpdateCashItemCount` | strmatch |
| `0x006CF700` | `AgcmUICashInven::CBDisplayCashInvenUseItemButtonText` | ui |
| `0x006CF870` | `AgcmUICashInven::CBDisplayCashInvenItemInfoName` | ui |
| `0x006CF900` | `AgcmUICashInven::CBDisplayCashInvenItemInfoCount` | ui |
| `0x006D00E0` | `AgcmUICashInven::CBDisplayCashInvenItemInfoTime` | ui |
| `0x006D01C0` | `AgcmUICashInven::CBDisplayCashInvenUsingItem` | ui |
| `0x006D02C0` | `AgcmUICashInven::CBDisplayCashInvenEnableTrade` | ui |
| `0x006D0370` | `AgcmUICashInven::CBCashInvenClickUseItem` | ui |
| `0x006D0550` | `AgcmUICashInven::CBUpdateItemCashInventory` | stage1 |
| `0x006D0660` | `AgcmUICashInven::CBSetSelfCharacter` | stage1 |
| `0x006D0690` | `AgcmUICashInven::CBReleaseSelfCharacter` | stage1 |
| `0x006D06F0` | `AgcmUICashInven::CBKeydownESC` | stage1 |
| `0x006D0710` | `AgcmUICashInven::CBGetItemTimeInfo` | stage1 |
| `0x006D0740` | `AgcmUICashInven::CBGetItemStaminaTime` | stage1 |
| `0x006D07B0` | `AgcmUICashInven::CBDisplayCashInvenStaminaCurrent` | ui |
| `0x006D0840` | `AgcmUICashInven::ctor_or_dtor` | merged |
| `0x006D0930` | `AgcmUICashInven::~AgcmUICashInven` | merged |
| `0x006D0960` | `AgcmUICashInven::OnDestroy` | merged |
| `0x006D09B0` | `AgcmUICashInven::CBCashInvenOpenUI` | ui |
| `0x006D0D40` | `AgcmUICashInven::AddFunction` | strmatch |
| `0x006D0DA0` | `AgcmUICashInven::CBAddCashItem` | stage1 |
| `0x006D0DC0` | `AgcmUICashInven::CBRemoveCashItem` | stage1 |
| `0x006D0DE0` | `AgcmUICashInven::CBDisplayCashInvenStaminaMax` | ui |
| `0x006D0ED0` | `AgcmUICashInven::AddDisplay` | strmatch |
| `0x006D0FE0` | `AgcmUICashInven::OnAddModule` | merged |

29 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, zugeordnet: 8.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `CashInvenOpenUI` | 27 | `0x006D05F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RefreshItemGrid` | 8 | `0x006D0500` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsSelfOperation` | 9 | `0x006D0770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetItemStaminaTime` | 48 | `0x006CFDE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckPetStateGrid` | 71 | `0x006D0B70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveCashItem` | 26 | `0x006D0A60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddCashItem` | 14 | `0x006D09C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetItemInfoTime` | 123 | `0x006CFA90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmUICashItemCabient`](AgcmUICashItemCabient.md)
