# NPC-Handel und NPC-Dialog: AgpmEventNPCTrade, AgcmEventNPCTrade, AgpmEventNPCDialog (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und -Disassembly, EP8-Quelle (`Modules/APublic/AgpmEventNPCTrade`, `…/AgpmEventNPCDialog`, `Modules/AClient/AgcmEventNPCTrade`) und die 2013er Berichte (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **[`AgpmEventNPCTrade`](AgpmEventNPCTrade.md) hat kein eigenes Netzwerkpaket.** Sein vtable-Slot 9 ist der Standard-`ApModule::OnReceive` (`0x004E3420`). Das Modul verwaltet nur die Event-Daten (Konstruktor/Destruktor, Stream, `OnAddModule`). Der NPC-Handel läuft über das **Client-Modul `AgcmEventNPCTrade`** mit Paket-Typ `0x32`.
- **Protokoll unverändert (2017 = EP8 = 2013):** Die Pakete von `AgcmEventNPCTrade` (`m_csPacket` 10 Felder, `m_csDetailInfo` 9 Felder) und `AgpmEventNPCDialog` (`m_csPacket` 3 Felder, `m_csPacketEventData` 1 Feld, Typ `0x37`) stimmen in Feldtypen, Anzahlen und Flag-Längen überein. Die Operationen und die ausgelösten Callback-IDs stimmen ebenfalls überein.
- **Bestätigung Preisfeld-Befund:** [`AgpmItem`](AgpmItem.md):GetNPCPrice` (`0x0053B500`) liest den Preis im 2017er Binary per `*(float*)` direkt aus dem Faktor-Slot `PRICE`/`NPC_PRICE` (`0x0050B2C0(item+0x5C, 0x0C)`; Fallback `-1.0`). `SetNPCTradeGheld` (`0x0053B410`) schreibt den INT32 aus dem Paketfeld `Item Price` mit `SetValue(…, 0xC, 0)` in denselben Slot. Der Wert muss daher auf der Leitung die **f32-Bits** des Preises tragen, wie in deiner Notiz zum NPC-Trade-Preis-Bug.
- **`AgpmEventNPCDialog::OnOperationGrant` (`0x00574440`) liegt außerhalb des Modulblocks.** Die Funktion ist nur ein `EnumCallback(GRANT, Event, Zeichen)` und wurde vom Linker mit gleich aufgebauten Handlern anderer Module zusammengelegt (ICF); sie hat dort mehrere Aufrufer.
- **Adressen verschoben:** `AgpmEventNPCDialog::OnReceive` `0x00576A50` (2013: `0x00577030`), `AgcmEventNPCTrade::OnReceive` `0x006DD440` (2013: `0x006DD9E0`).

## AgpmEventNPCDialog (Paket-Typ `0x37`)

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00574440` | `AgpmEventNPCDialog::OnOperationGrant` | dispatch-struktur |
| `0x00576170` | `AgpmEventNPCDialog::ctor_or_dtor_00576170` | merged |
| `0x005762B0` | `AgpmEventNPCDialog::ctor_or_dtor_005762b0` | merged |
| `0x00576360` | `AgpmEventNPCDialog::CBEventConstructor` | stage1 |
| `0x00576380` | `AgpmEventNPCDialog::CBEventDestructor` | stage1 |
| `0x005763B0` | `AgpmEventNPCDialog::CBStreamWriteEvent` | stage1 |
| `0x00576410` | `AgpmEventNPCDialog::CBStreamReadEvent` | stage1 |
| `0x00576550` | `AgpmEventNPCDialog::CBMakePacketEventData` | stage1 |
| `0x00576580` | `AgpmEventNPCDialog::CBParsePacketEventData` | stage1 |
| `0x005765B0` | `AgpmEventNPCDialog::OnOperationRequest` | dispatch-struktur |
| `0x00576750` | `AgpmEventNPCDialog::CBActionNPCDialog` | stage1 |
| `0x005767D0` | `AgpmEventNPCDialog::OnOperationRequestEx` | dispatch-struktur |
| `0x00576810` | `AgpmEventNPCDialog::OnOperationGrantEx` | dispatch-struktur |
| `0x00576850` | `AgpmEventNPCDialog::~AgpmEventNPCDialog` | merged |
| `0x00576870` | `AgpmEventNPCDialog::OnAddModule` | merged |
| `0x00576950` | `AgpmEventNPCDialog::OnDestroy` | merged |
| `0x00576A50` | `AgpmEventNPCDialog::OnReceive` | merged |

`OnReceive` ist vtable-Slot 9. Das Dispatch ist eine Sprungtabelle (`jmp [op*4+0x576BEC]`, Ziele `0x576ABC`, `0x576B3A`, `0x576BBB`, `0x576BCF`), die Case-Blöcke liegen außerhalb des von Ghidra erfassten Funktionskörpers. Der Dispatch prüft `op ≤ 3`, sonst `return TRUE`.

### Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketEventData` | 1/1/1 | 1/1/1 | ja | ja |

**m_csPacket** (3 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | PACKET | 1 | event base packet |
| 2 | `0x4` | INT32 | 1 | CID |

**m_csPacketEventData** (1 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | NPCDialog TID; |

Die Ex-Pakete (`REQUEST_EX`/`GRANT_EX`) sind keine Feldmasken-Pakete, sondern rohe Strukturen mit `PACKET_HEADER`, `Flag1`, `pcOperation`, `CID`, `NID`, `lEvnetIndex`, `lStep` und dem Unterfeld `pcOperation2`; das Binary liest `pcOperation2` bei Paket-Offset `+0x20` (`1` = MESSAGEBOX, `2` = MENU).

### Opcodes

| Op | Name | 2017-Handler | Verhalten | Ereignis (ID) | Vergleich 2013 |
|---:|---|---|---|---|---|
| 0 | `REQUEST` | Case `0x576ABC` → `0x5765B0` `OnOperationRequest` | Event holen (`GetEventFromBasePacket`), `event.type == 0x15` (`NPCDIALOG`), Zeichen sperren, bei Client-Paketen `AllBlock` prüfen; in Reichweite 600 → `m_stNextAction` löschen, ggf. `StopCharacter`, Ereignis; sonst NextAction = `EVENT_NPC_DIALOG` (12) setzen und dem NPC folgen | `CB_REQUEST` (2) | = |
| 1 | `GRANT` | Case `0x576B3A` → `0x574440` `OnOperationGrant` | gleiche Prüfungen, dann nur Callback | `CB_GRANT` (3) | = |
| 2 | `REQUEST_EX` | Case `0x576BBB` → `0x5767D0` `OnOperationRequestEx` | `pcOperation2` 1 → MessageBox, 2 → Menü | `CB_REQUEST_MESSAGEBOX` (6) / `CB_REQUEST_MENU` (8) | = (`CB#6`, `CB#8`) |
| 3 | `GRANT_EX` | Case `0x576BCF` → `0x576810` `OnOperationGrantEx` | wie Op 2 | `CB_GRANT_MESSAGEBOX` (7) / `CB_GRANT_MENU` (9) | = (`CB#7`, `CB#9`) |

Die Konstante `AGPMEVENT_NPCDIALOG_MAX_USE_RANGE` = 600 und der Event-Funktionstyp `APDEVENT_FUNCTION_NPCDAILOG` = `0x15` stimmen mit der Quelle überein.

## AgcmEventNPCTrade (Paket-Typ `0x32`)

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0053B410` | `AgpmItem::SetNPCTradeGheld` | dispatch-struktur |
| `0x0053B460` | `AgpmItem::SetNPCTradeCharismaPoint` | dispatch-struktur |
| `0x0053B4B0` | `AgpmItem::SetNPCTradeShrineCoin` | dispatch-struktur |
| `0x0053B500` | `AgpmItem::GetNPCPrice` | dispatch-struktur |
| `0x006DCAB0` | `AgcmEventNPCTrade::ctor_or_dtor_006dcab0` | merged |
| `0x006DCBF0` | `AgcmEventNPCTrade::ctor_or_dtor_006dcbf0` | merged |
| `0x006DCC60` | `AgcmEventNPCTrade::ProcessBuyItem` | dispatch-struktur |
| `0x006DCCF0` | `AgcmEventNPCTrade::~AgcmEventNPCTrade` | merged |
| `0x006DCD10` | `AgcmEventNPCTrade::ProcessItemList` | dispatch-struktur |
| `0x006DD3C0` | `AgcmEventNPCTrade::CBRequestNPCItemList` | stage1 |
| `0x006DD440` | `AgcmEventNPCTrade::OnReceive` | merged |
| `0x006DD560` | `AgcmEventNPCTrade::OnAddModule` | merged |

`OnReceive` (`0x006DD440`, vtable-Slot 9) liest 10 Felder (`m_csPacket` bei `+0xBB8`) und verzweigt über die Operation (`nOperation`, Feld 1) in einer Vergleichskette.

### Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 2/2/2 | 10/10/10 | ja | ja |
| `m_csDetailInfo` | 2/2/2 | 9/9/9 | ja | ja |

**m_csPacket** (10 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | PACKET | 1 | Event Base |
| 1 | `0x2` | INT8 | 1 | nOperation	: °Å·¡ ¿¬»ê |
| 2 | `0x4` | INT32 | 1 | RequesterCID	: °Å·¡ ¿äÃ»ÀÚ ID |
| 3 | `0x8` | INT32 | 1 | lIID			: °Å·¡ ¾ÆÀÌÅÛ ID |
| 4 | `0x10` | PACKET | 1 | DetailInfo	: ¾ÆÀÌÅÛ ¼¼ºÎ Á¤º¸. |
| 5 | `0x20` | INT32 | 1 | lTimeStamp	; °¡°Ýº¯µ¿µî ÆÄ´Â ¹°°Ç¿¡ º¯È­°¡ ÀÖÀ»¶§ ÀÌ°ªÀÌ Áõ°¡µÈ´Ù. |
| 6 | `0x40` | INT32 | 1 | ÀÌ °ªÀ¸·Î ¾ÆÀÌÅÛ °¡°ÝÀ» »õ·Î ¹ÞÀ»Áö °áÁ¤ÇÑ´Ù. |
| 7 | `0x80` | INT8 | 1 | lResult		; °á°ú°ªÀ» º¸³½´Ù. |
| 8 | `0x100` | INT8 | 1 | Layer		; ÀÎº¥ÀÇ ¾î´À À§Ä¡¿¡ »ìÁö |
| 9 | `0x200` | INT8 | 1 | Row |

**m_csDetailInfo** (9 Felder, Flag-Länge 2):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Item TID		: TemplateID |
| 1 | `0x2` | INT32 | 1 | Item Price	: ¾ÆÀÌÅÛ °¡°Ý. |
| 2 | `0x4` | INT32 | 1 | Item Count	: ¾ÆÀÌÅÛ ¼ö·®. |
| 3 | `0x8` | INT16 | 1 | Item status	: item status |
| 4 | `0x10` | INT16 | 1 | Layer		: Layer |
| 5 | `0x20` | INT16 | 1 | Row			: Row |
| 6 | `0x40` | INT16 | 1 | Column		: Column |
| 7 | `0x80` | INT32 | 1 | Ä«¸®½º¸¶Æ÷ÀÎÆ® |
| 8 | `0x100` | INT32 | 1 | ½¬¶óÀÎÄÚÀÎ |

### Operationen

| Op | Name (`AGPDEVENTNPCTRADE_…`) | 2017-Verhalten | Ereignis (ID) | Vergleich 2013 |
|---:|---|---|---|---|
| 0 | `REQUESTITEMLIST` | `ProcessItemList` (`0x6DCD10`): Item per IID holen, DetailInfo lesen, ins NPC-Grid einfügen, Stapelzahl/Grid-Position setzen, `SetNPCTradeGheld/CharismaPoint/ShrineCoin` | `UPDATE_NPCTRADE_GRID` (0) | = |
| 1 | `SEND_ALL_ITEM_INFO` | direkt | `OPEN_UI_NPCTRADE` (3) | = |
| 2 | `BUYITEM` | `ProcessBuyItem` (`0x6DCC60`), danach `UPDATE_INVENTORY_GRID` (1); Ergebnis 2 → `MSG_BUY_ITEM` (7), 3 → `NOT_ENOUGH_GHELLD` (8), 4 → `INVEN_FULL` (5), 10 → `NOT_ENOUGH_CHARISMA` (10), 11 → `NOT_ENOUGH_SHRINECOIN` (11); Ergebnisse 5, 6, 7, 9 lösen nichts aus | siehe links | = |
| 3 | `SELLITEM` | `ProcessSellItem` (inline): Ergebnis 0 → `MSG_SELL_ITEM` (6), 1 → `NOT_ENOUGH_SPACE_TO_RETURN_GHELLD` (9), danach `UPDATE_INVENTORY_GRID` (1) | siehe links | = |

Hinweis: Die 2013er Doku führt für `AgcmEventNPCTrade` keine Binary-Ereignisse auf (`– / –`), weil dort die Hilfsfunktionen außerhalb des Suchradius lagen; die Zuordnung hier stammt aus der Auswertung der Case-Blöcke und der Quellkonstanten (Ergebnis- und Callback-IDs).

### Preisfeld im Detail

| Faktor | Index | Funktion 2017 |
|---|---:|---|
| `PRICE`-Block | `0x0C` (12) | Zugriff über `FUN_0050B220` (anlegen) / `FUN_0050B2C0` (holen) |
| `NPC_PRICE` (Ghelld-Preis) | 0 | `SetNPCTradeGheld` `0x53B410`; `GetNPCPrice` `0x53B500` liest `*(float*)` |
| `CHRISMA_PRICE` | 4 | `SetNPCTradeCharismaPoint` `0x53B460` |
| `SHRINE_COIN` | 5 | `SetNPCTradeShrineCoin` `0x53B4B0` |

Alle drei Setter schreiben den INT32 des Pakets unverändert per `SetValue`. Nur `GetNPCPrice` interpretiert den Slot als `float`. Die Funktion `0x53E4B0` liest den zweiten Slot (`+4`, `PC_PRICE`) ebenfalls als `float`.

## AgpmEventNPCTrade (Event-Daten, kein Paket)

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x00575CD0` | `AgpmEventNPCTrade::ctor_or_dtor_00575cd0` | merged |
| `0x00575D90` | `AgpmEventNPCTrade::CBEventDestructor` | stage1 |
| `0x00575E00` | `AgpmEventNPCTrade::CBStreamWriteEvent` | stage1 |
| `0x00575E60` | `AgpmEventNPCTrade::CBStreamReadEvent` | stage1 |
| `0x00575F00` | `AgpmEventNPCTrade::CBEventConstructor` | stage1 |
| `0x00575FD0` | `AgpmEventNPCTrade::OnAddModule` | merged |
| `0x00576070` | `AgpmEventNPCTrade::ctor_or_dtor_00576070` | merged |
| `0x00576150` | `AgpmEventNPCTrade::~AgpmEventNPCTrade` | merged |

Die Funktionen sind der Event-Konstruktor/-Destruktor (`0x575F00`, `0x575D90`), der Stream-Leser/-Schreiber für die Event-Daten (`0x575E60`, `0x575E00`) und `OnAddModule` (`0x575FD0`, registriert diese Callbacks im Event-Manager). Der Event hält laut Quelle ein Grid (`AgpdEventNPCTradeData.m_pcsGrid`), das `ProcessItemList` füllt.

## Grenzen

- Die Case-Blöcke von `AgpmEventNPCDialog::OnReceive` wurden an der Disassembly gelesen; die genaue Position der Bereichsprüfung (`CheckValidRange`, `FUN_0055C380`) und ihre Parameter sind nur für Op 0 geprüft.
- `ProcessItemList` wurde nicht Zeile für Zeile gegen die Quelle gelesen; das Feld-Mapping der `GetField`-Argumente im dekompilierten Stack-Code ist unübersichtlich. Die Setter-Aufrufe (Gheld, Charisma, Shrine-Münze) sind durch die Faktorindizes (0, 4, 5) belegt.
- Die Verschmelzung (ICF) von `OnOperationGrant` (`0x574440`) mit Handlern anderer Module ist aus Position und Aufbau abgeleitet, die anderen Aufrufer wurden nicht einzeln aufgelistet.
- Die Client-Seite der Dialog-UI ([`AgcmUIEventNPCDialog`](AgcmUIEventNPCDialog.md), Texte `CNpcText`) wurde nicht untersucht.

## Querverweise

- **Erwähnt Module:** [`AgcmUIEventNPCDialog`](AgcmUIEventNPCDialog.md), [`AgpmEventNPCTrade`](AgpmEventNPCTrade.md), [`AgpmItem`](AgpmItem.md)
