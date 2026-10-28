# AgpmItem (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Paketmoduls `AgpmItem` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, EP8-Quelle (`Modules/APublic/AgpmItem`), Vergleich mit den Berichten zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Protokoll unverändert:** Paket-Typ `0x04`, alle 13 Pakete (Hauptpaket `PACKET_ITEM` mit 25 Feldern, 12 Teilpakete) und alle Feldtypen, Anzahlen und Flag-Längen stimmen im 2017er Binary mit der EP8-Quelle und mit der 2013er Doku überein.
- **Opcodes unverändert:** 31 der 33 Operationen haben im 2017er Binary einen Case. `13` (`EGO_ITEM`) und `24` (`UNUSE_ITEM_FAILED`) haben weder in der Quelle noch im 2013er noch im 2017er Binary einen Case und enden im `default`-Zweig, der den Kopierfehler-Text `AgpmCharacter::OnReceive() Error (19)` ausgibt (steht so auch in der Quelle).
- **Echter Versionsunterschied (nur intern, nicht im Netzwerkprotokoll):** Die Callback-Nummerierung des Moduls ist im 2017er Build ab EP8-ID 40 um **6 kleiner**. Es fehlen die sechs Konvertierungs-Callbacks `ASK_REALLY_CONVERT_ITEM`, `CONVERT_ITEM`, `ADD_CONVERT_HISTORY`, `REMOVE_CONVERT_HISTORY`, `UPDATE_CONVERT_HISTORY`, `SEND_CONVERT_HISTORY` (EP8-IDs 34–39). Belege: IDs ≤ 33 sind identisch (z. B. `USE_ITEM_BY_TID` 28), alle 12 geprüften IDs ≥ 36 liegen genau 6 unter dem EP8-/2013-Wert (z. B. `PICKUP_ITEM_RESULT` 36 statt 42, `UPDATE_COOLDOWN` 90 statt 96, `ITEM_INFORMATION` 103 statt 109). Das Paket `m_csPacketConvert` (16 Felder) und das Modul [`AgpmItemConvert`](AgpmItemConvert.md) sind weiterhin vorhanden.
- **Ereignisse:** Mit dieser ID-Korrektur stimmen alle einzeln vergleichbaren Opcodes mit der 2013er Messung überein. Ausnahmen: Op 11 (`PICKUP_ITEM`) und 17 (`SPLIT_ITEM`) lösen im 2017er Aufrufbaum zusätzlich `UPDATE_ITEM_STATUS_FLAG` aus (vermutlich Tiefe 3 gegenüber dem kleineren 2013er Suchradius, nicht gegen die Quelle geprüft).
- **Adressen verschoben:** `OnReceive` liegt bei `0x00543EB0` (2013: `0x00544620`).

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0053A7F0` | `AgpmItem::OnOperationUseItemFailedByTID` | case-map |
| `0x0053A870` | `AgpmItem::OnOperationUpdateReturnScrollStatus` | case-map |
| `0x0053A8C0` | `AgpmItem::OnOperationCancelReturnScroll` | case-map |
| `0x0053A900` | `AgpmItem::OnOperationUseReturnScroll` | case-map |
| `0x0053A950` | `AgpmItem::OnOperationUseReturnScrollResultFailed` | case-map |
| `0x0053A970` | `AgpmItem::OnOperationStackItem` | case-map |
| `0x0053AB10` | `AgpmItem::OnOperationUseItemSuccess` | case-map |
| `0x0053AB50` | `AgpmItem::UpdateReverseOrbReuseTime` | case-map |
| `0x0053ABC0` | `AgpmItem::UpdateTransformReuseTime` | case-map |
| `0x0053AC30` | `AgpmItem::InitTransformReuseTime` | case-map |
| `0x0053BD00` | `AgpmItem::RemoveStatus` | strmatch |
| `0x0053BFD0` | `AgpmItem::OnOperationUpdateItemUseTime` | case-map |
| `0x0053C060` | `AgpmItem::OnOperationUpdateStaminaRemainTime` | case-map |
| `0x0053C0E0` | `AgpmItem::OnOperationChangeAutoPickUpItem` | case-map |
| `0x0053D150` | `AgpmItem::OnIdle2` | merged |
| `0x0053D440` | `AgpmItem::unk_0053d440` | unbestimmt |
| `0x0053D540` | `AgpmItem::unk_0053d540` | unbestimmt |
| `0x0053E1C0` | `AgpmItem::OnOperationUseItem` | case-map |
| `0x0053E310` | `AgpmItem::OnOperationRequestDestroyItem` | case-map |
| `0x0053E730` | `AgpmItem::SubItemStackCount` | strmatch |
| `0x0053E830` | `AgpmItem::CBCheckActionRequirement` | stage1 |
| `0x0053E960` | `AgpmItem::CBPayActionCost` | stage1 |
| `0x0053EF00` | `AgpmItem::OnOperationUnuseItem` | case-map |
| `0x0053EF40` | `AgpmItem::OnOperationPauseItem` | case-map |
| `0x0053F140` | `AgpmItem::OnOperationRemove` | case-map |
| `0x0053F6D0` | `AgpmItem::CBPickupItem` | stage1 |
| `0x0053FB00` | `AgpmItem::Report` | merged |
| `0x0053FD30` | `AgpmItem::OnOperationPickupItem` | case-map |
| `0x0053FEB0` | `AgpmItem::OnOperationSplitItem` | case-map |
| `0x00540210` | `AgpmItem::ConAgpdItemADChar` | stage1 |
| `0x00540440` | `AgpmItem::OnOperationUpdate_pItem` | strmatch+overload |
| `0x005410F0` | `AgpmItem::OnOperationPickupItemResult` | case-map |
| `0x00541320` | `AgpmItem::OnOperationItemInformation` | case-map |
| `0x00541630` | `AgpmItem::AddItem` | merged |
| `0x00541780` | `AgpmItem::OnOperationAdd` | strmatch |
| `0x00542250` | `AgpmItem::OnOperationUpdate` | case-map |
| `0x00542510` | `AgpmItem::OnOperationItemInformationResult` | case-map |
| `0x00542C70` | `AgpmItem::OnInit` | merged |
| `0x00542ED0` | `AgpmItem::AddItemTemplate` | merged |
| `0x00542F50` | `AgpmItem::AddItemOptionTemplate` | merged |
| `0x005431B0` | `AgpmItem::OnDestroy` | merged |
| `0x00543420` | `AgpmItem::DesAgpdItemADChar` | stage1 |
| `0x00543570` | `AgpmItem::ConAgpdItemADCharTemplate` | stage1 |
| `0x00543820` | `AgpmItem::OnAddModule` | merged |
| `0x00543BA0` | `AgpmItem::OnOperationUpdateCooldown` | case-map |
| `0x00543CB0` | `AgpmItem::OnOperationUseItemByTID` | case-map |
| `0x00543EB0` | `AgpmItem::OnReceive` | merged |
| `0x005449A0` | `AgpmItem::ctor_or_dtor_005449a0` | merged |
| `0x00544C10` | `AgpmItem::ctor_or_dtor_00544c10` | merged |
| `0x00545330` | `AgpmItem::~AgpmItem` | merged |
| `0x00546E10` | `AgpmItem::TemplateWriteCB` | stage1 |
| `0x00547120` | `AgpmItem::TemplateReadCB` | stage1 |
| `0x00547920` | `AgpmItem::CharTemplateWriteCB` | stage1 |
| `0x0054A980` | `AgpmItem::StreamReadTemplate` | strmatch |
| `0x0054AE10` | `AgpmItem::CBInitTemplateDefaultValue` | stage1 |
| `0x0054AFC0` | `AgpmItem::StreamReadTemplates` | strmatch |
| `0x0054B340` | `AgpmItem::CharTemplateReadCB` | stage1 |
| `0x0054B3F0` | `AgpmItem::CharacterImportDataReadCB` | stage1 |
| `0x0058C600` | `AgpmItem::unk_0058c600` | unbestimmt |
| `0x0058D050` | `AgpmItem::AddItemToCashInventory` | merged |
| `0x0058D6E0` | `AgpmItem::RemoveItemFromCashInventory` | merged |
| `0x0058D9E0` | `AgpmItem::unk_0058d9e0` | unbestimmt |
| `0x0058E000` | `AgpmItem::unk_0058e000` | unbestimmt |
| `0x0058E580` | `AgpmItem::RemoveItemFromBank` | merged |
| `0x0058E910` | `AgpmItem::OnOperationRequestBuyBankSlot` | case-map |
| `0x0058EAB0` | `AgpmItem::RemoveItemFromSalesBox` | merged |
| `0x0058EBC0` | `AgpmItem::CBGetItemLancer` | stage1 |
| `0x0058EC00` | `AgpmItem::unk_0058ec00` | unbestimmt |
| `0x0058F200` | `AgpmItem::UnEquipItem` | merged |
| `0x0058FB20` | `AgpmItem::unk_0058fb20` | unbestimmt |
| `0x0058FC30` | `AgpmItem::RemoveItemFromClientTradeGrid` | merged |
| `0x0058FD70` | `AgpmItem::RemoveItemFromTradeGrid` | merged |
| `0x005971C0` | `AgpmItem::RemoveItemFromGrid` | merged |

`OnReceive` = vtable-Slot 9 (`0x00543EB0`). Der Modulkonstruktor liegt bei `0x00544C10` und legt 12 Teilpakete an. Das Hauptpaket `PACKET_ITEM` wird in einer eigenen Klasse (`AgppItem.h`) bei `0x00539F80` aufgebaut (`AgpmItem+0xEC4`). `OnOperationUpdate` existiert in der Quelle in zwei Überladungen: `0x00542250` (Variante mit `lIID`, 276 Byte, schlägt das Item nach) und `0x00540440` (Variante mit `AgpdItem*`, 3 KB, eigentliche Verarbeitung).

## Paketlayout

Typcodes wie bei [`AgpmCharacter`](AgpmCharacter.md). Verglichen wurden Quelle (`SetFieldType`), 2017er Konstruktoren (`FUN_004E9F80`) und die 2013er Tabellen.

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacketField` | 1/1/1 | 1/1/1 | ja | ja |
| `m_csPacketInventory` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketBank` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketQuest` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketEquip` | 1/1/1 | 0/0/0 | ja | ja |
| `m_csPacketConvert` | 2/2/2 | 16/16/16 | ja | ja |
| `m_csPacketEgo` | 1/1/1 | 4/4/4 | ja | ja |
| `m_csPacketOption` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csPacketSkillPlus` | 1/1/1 | 3/3/3 | ja | ja |
| `m_csPacketCashInformaion` | 1/1/1 | 5/5/5 | ja | ja |
| `m_csPacketAutoPickItem` | 1/1/1 | 1/1/1 | ja | ja |
| `m_csPacketExtra` | 1/1/1 | 1/1/1 | ja | ja |
| `PACKET_ITEM (m_csPacket)` | 4/4/4 | 25/25/25 | ja | ja |

**PACKET_ITEM (m_csPacket)** (25 Felder, Flag-Länge 4):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | Operation |
| 1 | `0x2` | INT8 | 1 | Status |
| 2 | `0x4` | INT32 | 1 | Item ID |
| 3 | `0x8` | INT32 | 1 | Item Template ID |
| 4 | `0x10` | INT32 | 1 | Item Owner CID |
| 5 | `0x20` | INT32 | 1 | Item Count |
| 6 | `0x40` | PACKET | 1 | Field |
| 7 | `0x80` | PACKET | 1 | Inventory |
| 8 | `0x100` | PACKET | 1 | Bank |
| 9 | `0x200` | PACKET | 1 | Equip |
| 10 | `0x400` | PACKET | 1 | Factors |
| 11 | `0x800` | PACKET | 1 | Percent Factors |
| 12 | `0x1000` | INT32 | 1 | target character id (case usable (scroll) item) |
| 13 | `0x2000` | PACKET | 1 | Convert packet |
| 14 | `0x4000` | PACKET | 1 | restrict factor packet |
| 15 | `0x8000` | PACKET | 1 | Ego Item packet |
| 16 | `0x10000` | PACKET | 1 | Quest Item packet |
| 17 | `0x20000` | INT32 | 1 | skill template id |
| 18 | `0x40000` | UINT32 | 1 | reuse time for reverse orb |
| 19 | `0x80000` | INT32 | 1 | status flag |
| 20 | `0x100000` | PACKET | 1 | option packet |
| 21 | `0x200000` | PACKET | 1 | skill plus packet |
| 22 | `0x400000` | UINT32 | 1 | reuse time for transform |
| 23 | `0x800000` | PACKET | 1 | CashItem adding information |
| 24 | `0x1000000` | PACKET | 1 | Extra information |

## Opcode-Tabelle

Handler im 2017er Binary; Ereignisse = Menge der `EnumCallback`-IDs (Tiefe 3 im Modul), ID ≥ 34 um +6 auf EP8-Namen umgerechnet. Op 13 und 24 haben keinen Case.

| Op | Name | 2017-Handler | Ereignisse 2017 (auf EP8-IDs umgerechnet) | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ADD` | `0x00541780` `OnOperationAdd` | `ID_ADD`, `ID_ADD_ITEM_EXTRADATA`, `ID_ADD_ITEM_TO_BANK`, `ID_ADD_ITEM_TO_GUILD_WAREHOUSE`, `ID_CHANGE_AUTOPICK_ITEM`, `ID_CHANGE_ITEM_OWNER` … (52) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 1 | `REMOVE` | `0x0053F140` `OnOperationRemove` | `ID_ADD`, `ID_ADD_ITEM_EXTRADATA`, `ID_ADD_ITEM_TO_BANK`, `ID_ADD_ITEM_TO_GUILD_WAREHOUSE`, `ID_CHANGE_AUTOPICK_ITEM`, `ID_CHARGING_INVENTORY_REMOVE` … (48) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 2 | `UPDATE` | `0x00542250` `OnOperationUpdate` | `ID_ADD`, `ID_ADD_ITEM_EXTRADATA`, `ID_ADD_ITEM_TO_BANK`, `ID_ADD_ITEM_TO_GUILD_WAREHOUSE`, `ID_CHANGE_AUTOPICK_ITEM`, `ID_CHANGE_ITEM_OWNER` … (52) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 3 | `USE_ITEM` | `0x0053E1C0` `OnOperationUseItem` | `ID_ADD`, `ID_ADD_ITEM_EXTRADATA`, `ID_ADD_ITEM_TO_BANK`, `ID_ADD_ITEM_TO_GUILD_WAREHOUSE`, `ID_CHANGE_AUTOPICK_ITEM`, `ID_CHARGING_INVENTORY_REMOVE` … (48) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 4 | `USE_ITEM_BY_TID` | `0x00543CB0` `OnOperationUseItemByTID` | `ID_UPDATE_COOLDOWN`, `ID_USE_ITEM_BY_TID` | = (2013 = 2017) |
| 5 | `USE_ITEM_FAILED_BY_TID` | `0x0053A7F0` `OnOperationUseItemFailedByTID` | `ID_USE_ITEM_FAILED_BY_TID` | = (2013 = 2017) |
| 6 | `USE_RETURN_SCROLL` | `0x0053A900` `OnOperationUseReturnScroll` | `ID_USE_RETURN_SCROLL` | = (2013 = 2017) |
| 7 | `USE_RETURN_SCROLL_FAILED` | `0x0053A950` `OnOperationUseReturnScrollResultFailed` | `ID_USE_RETURN_SCROLL_RESULT_FAILED` | = (2013 = 2017) |
| 8 | `CANCEL_RETURN_SCROLL` | `0x0053A8C0` `OnOperationCancelReturnScroll` | – | = (2013 = 2017) |
| 9 | `ENABLE_RETURN_SCROLL` | `0x0053A870` `OnOperationUpdateReturnScrollStatus` | `ID_UPDATE_RETURN_TELEPORT_STATUS` | = (2013 = 2017) |
| 10 | `DISABLE_RETURN_SCROLL` | `0x0053A870` `OnOperationUpdateReturnScrollStatus` | `ID_UPDATE_RETURN_TELEPORT_STATUS` | = (2013 = 2017) |
| 11 | `PICKUP_ITEM` | `0x0053FD30` `OnOperationPickupItem` | `ID_CHECK_CAN_PICKUP_ITEM`, `ID_PICKUP_ITEM_RESULT`, `ID_UPDATE_ITEM_STATUS_FLAG` | 2017 ⊃ 2013 |
| 12 | `PICKUP_ITEM_RESULT` | `0x005410F0` `OnOperationPickupItemResult` | `ID_PICKUP_ITEM_RESULT` | = (2013 = 2017) |
| 13 | `EGO_ITEM` | – (default) | – | kein Case (default) – wie 2013 |
| 14 | `STACK_ITEM` | `0x0053A970` `OnOperationStackItem` | – | = (2013 = 2017) |
| 15 | `DROP_MONEY` | inline: `return TRUE` (kein Handler) | – | = (2013 = 2017) |
| 16 | `USE_ITEM_SUCCESS` | `0x0053AB10` `OnOperationUseItemSuccess` | `ID_USE_ITEM_SUCCESS` | = (2013 = 2017) |
| 17 | `SPLIT_ITEM` | `0x0053FEB0` `OnOperationSplitItem` | `ID_SPLIT_ITEM`, `ID_UPDATE_ITEM_STATUS_FLAG` | 2017 ⊃ 2013 |
| 18 | `UPDATE_REUSE_TIME_FOR_REVERSE_ORB` | `0x0053AB50` `UpdateReverseOrbReuseTime` | `ID_UPDATE_REUSETIME_FOR_REVERSE_ORB` | = (2013 = 2017) |
| 19 | `UPDATE_REUSE_TIME_FOR_TRANSFORM` | `0x0053ABC0` `UpdateTransformReuseTime` | `ID_UPDATE_REUSETIME_FOR_TRANSFORM` | = (2013 = 2017) |
| 20 | `INIT_TIME_FOR_TRANSFORM` | `0x0053AC30` `InitTransformReuseTime` | `ID_INIT_REUSETIME_FOR_TRANSFORM` | = (2013 = 2017) |
| 21 | `REQUEST_DESTROY_ITEM` | `0x0053E310` `OnOperationRequestDestroyItem` | `ID_CHARGING_INVENTORY_REMOVE`, `ID_CHAR_CHECK_BANK`, `ID_CHAR_REMOVE_BANK`, `ID_CHAR_REMOVE_INVENTORY`, `ID_DELETE`, `ID_REMOVE` … (10) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 22 | `REQUEST_BUY_BANK_SLOT` | `0x0058E910` `OnOperationRequestBuyBankSlot` | – | = (2013 = 2017) |
| 23 | `UNUSE_ITEM` | `0x0053EF00` `OnOperationUnuseItem` | `ID_ADD`, `ID_ADD_ITEM_EXTRADATA`, `ID_ADD_ITEM_TO_BANK`, `ID_ADD_ITEM_TO_GUILD_WAREHOUSE`, `ID_CHANGE_AUTOPICK_ITEM`, `ID_CHARGING_INVENTORY_REMOVE` … (48) | Aufrufbaum (Tiefe 3), nicht vergleichbar |
| 24 | `UNUSE_ITEM_FAILED` | – (default) | – | kein Case (default) – wie 2013 |
| 25 | `PAUSE_ITEM` | `0x0053EF40` `OnOperationPauseItem` | `ID_CHAR_PAUSE_CASH_ITEM` | = (2013 = 2017) |
| 26 | `UPDATE_ITEM_USE_TIME` | `0x0053BFD0` `OnOperationUpdateItemUseTime` | `ID_UI_UPDATE_CASH_INVENTORY` | = (2013 = 2017) |
| 27 | `USE_ITEM_RESULT` | inline: `EnumCallback(USE_ITEM_RESULT)` | `ID_USE_ITEM_RESULT` | = (2013 = 2017) |
| 28 | `UPDATE_COOLDOWN` | `0x00543BA0` `OnOperationUpdateCooldown` | `ID_UPDATE_COOLDOWN` | = (2013 = 2017) |
| 29 | `UPDATE_STAMINA_REMAIN_TIME` | `0x0053C060` `OnOperationUpdateStaminaRemainTime` | `ID_UI_UPDATE_CASH_INVENTORY` | = (2013 = 2017) |
| 30 | `CHANGE_AUTOPICK_ITEM` | `0x0053C0E0` `OnOperationChangeAutoPickUpItem` | `ID_CHANGE_AUTOPICK_ITEM` | = (2013 = 2017) |
| 31 | `ITEMINFORMATION` | `0x00541320` `OnOperationItemInformation` | `ITEM_INFORMATION` | = (2013 = 2017) |
| 32 | `ITEMINFORMATION_RESULT` | `0x00542510` `OnOperationItemInformationResult` | `ID_ADD`, `ID_ADD_ITEM_EXTRADATA`, `ID_ADD_ITEM_TO_BANK`, `ID_ADD_ITEM_TO_GUILD_WAREHOUSE`, `ID_CHANGE_AUTOPICK_ITEM`, `ID_CHARGING_INVENTORY_REMOVE` … (48) | Aufrufbaum (Tiefe 3), nicht vergleichbar |

## Abgleich mit EP8-Quelle und Besonderheiten

- `OnReceive`: 25 Felder via `GetField` (Operation, Status, IID, TID, CID, Anzahl, Field/Inventory/Bank/Equip/Factor/FactorPercent, TargetID, Convert, RestrictFactor, Ego, Quest, SkillTID, ReuseTime Reverse Orb, StatusFlag, Option, SkillPlus, ReuseTime Transform, CashInformation, ExtraInformation), identisch zur Quelle.
- Vorprüfungen wie in der Quelle: bei Paketen vom Client muss die CID zum Socket-Besitzer passen; bei Paketen vom Client wird zusätzlich `IsAllBlockStatus` des Charakters geprüft (`FUN_00505A70`).
- `ADD` und `REMOVE` werden nur vom Server akzeptiert; `UPDATE` ruft nach `OnOperationUpdate` direkt `EnumCallback(RECEIVE_ITEM_DATA)` (Binary: ID 0x38 = 56 = EP8 62).
- Op 27 (`USE_ITEM_RESULT`) löst nur bei Serverpaketen aus (`EnumCallback` mit Result-Byte), Op 15 (`DROP_MONEY`) gibt sofort `TRUE` zurück.
- Vor der Weitergabe an die `OnOperation…`-Handler hält der Dispatch den Charakter-Mutex (`GetCharacterLock`) und gibt ihn am Ende frei (`FUN_004E7C70`).

## Grenzen

- Aufrufbäume der Operationen 0, 1, 2, 3, 21, 23 und 32 sind zu groß für einen Mengenvergleich; dort liefert die Tiefe-3-Suche viele zusätzliche Ereignisse über Inventar-/Bank-/Grid-Hilfsfunktionen.
- Die ID-Verschiebung ist aus 12 Opcodes und der Reihenfolge abgeleitet. Nicht geprüft ist, ob die sechs Konvertierungs-Callbacks im 2017er Build an anderer Stelle (z. B. in `AgpmItemConvert`) neu existieren.
- `OnOperationAdd`/`OnOperationUpdate_pItem` (je mehrere KB) wurden nicht Zeile für Zeile gegen die Quelle gelesen.
- Weitere `AgpmItem`-Dateien (`AgpmItemBank`, `…Inventory`, `…Equip`, `…CashInventory`, `…Grid`) liegen teils bei `0x0058….` und sind nur teilweise benannt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 52, eingebaut: 45, gemeinsamer Rumpf: 98, nicht im Client: 112, ohne Kandidat: 95, zugeordnet: 100.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `StreamReadTransformData` | 101 | `0x005454C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetItemDurabilityPercent` | 24 | `0x0053B730` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitTradeBlockItems` | 78 | `0x005429B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetEquipWeapon` | 30 | `0x0058F3E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ChangeItemOwner` | 2 | `0x0053F4A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitItem` | 12 | `0x0053A3E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInventory` | 18 | `0x0053D400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckBuyBankSlotCost` | 15 | `0x0058E8C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsBuyBankSlot` | 8 | `0x0058E620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUsableType` | 4 | `0x0058D210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalBoltCountInInventory` | 11 | `0x0053E460` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTotalArrowCountInInventory` | 11 | `0x0053E410` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAvatarItem` | 17 | `0x0053CC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsUsingStamina` | 8 | `0x0053C330` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsQuestItem` | 5 | `0x0053BBD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetBoundType` | 12 | `0x0053BAC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ResetTradeStats` | 9 | `0x0058FC70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetInventoryItemByTID` | 29 | `0x0058C6A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemOption` | 5 | `0x00596870` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AutoInsertStackMerge` | 89 | `0x00596F90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemFromField` | 13 | `0x0058FE70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsEquipWeapon` | 19 | `0x0058FA60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EquipItem` | 5 | `0x0058EC00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadItemTemplateEntryINI` | 50 | `0x0054A6D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadImportData` | 1694 | `0x00545820` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadOneTemplate` | 61 | `0x0054ABA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseQuestPacket` | 13 | `0x0058E9A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseInventoryPacket` | 13 | `0x0058C760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetShrineCoinPrice` | 6 | `0x0053B570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCharismaPrice` | 6 | `0x0053B540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetItemPrice` | 16 | `0x0053B390` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetPCPrice` | 13 | `0x0053E4B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetBuyBankSlotCost` | 22 | `0x0058E650` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToBank` | 2 | `0x0058C4A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemFromInventory` | 16 | `0x0058C600` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToChargingInventory` | 2 | `0x0058E0B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToInventory` | 2 | `0x0058C880` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SplitItem_field` | 0 | `0x0053FA20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SplitItem` | 101 | `0x0053F750` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessRemove` | 26 | `0x0053B960` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckUseItem` | 89 | `0x0053E4F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakePacketItemInforMation` | 33 | `0x0053AC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItem` | 59 | `0x0053D440` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyTemplate` | 37 | `0x005628E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateTemplate` | 51 | `0x00542CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CreateItem` | 65 | `0x0053D180` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddItemToChargingInventoryResult` | 54 | `0x0058DEA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsEnableEquipItemInMyRegion` | 17 | `0x0053CCC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddRemoveItem` | 12 | `0x0053B9F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBoltItemFromInventory` | 29 | `0x0053B8D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetArrowItemFromInventory` | 29 | `0x0053B840` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashItemByTID` | 6 | `0x0058D0D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetEquipSlotItem` | 15 | `0x0058FAC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `EquipItem` | 5 | `0x0058E430` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToClientTradeGrid` | 2 | `0x0058E160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemFromCashInventory` | 12 | `0x0058D7A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharShrineCoinCount` | 33 | `0x0053CF40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemStackCount` | 39 | `0x0053B670` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetItemStackCount` | 39 | `0x0053B5A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetItemPrice` | 14 | `0x0053B340` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketChangeAutoPickItem` | 40 | `0x0053B040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestBuyBankSlot` | 34 | `0x0053AF60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketRequestDestroyItem` | 35 | `0x0053AEE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketDropMoneyToField` | 35 | `0x0053AD70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToSalesBox` | 2 | `0x0058FB80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToChargingInventory` | 2 | `0x0058DB30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInBank` | 2 | `0x0058CB90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToBank` | 2 | `0x0058C9B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InsertStackMerge` | 51 | `0x00596D70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Insert` | 39 | `0x00596C10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetEquipItem` | 15 | `0x0058EB10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInChargingInventory` | 2 | `0x0058E250` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToChargingInventory` | 2 | `0x0058DBD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamReadAvatarSet` | 64 | `0x00544610` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckUpdateStatus` | 40 | `0x0053EE10` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GefEffectedSkillPlusLevel` | 40 | `0x0053EC90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToTradeGrid` | 2 | `0x0058FCB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToSalesBox` | 2 | `0x0058E9F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInInventory` | 2 | `0x0058E6E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemFromClientTradeGrid` | 16 | `0x0058E000` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetChargingInvectoryColumn` | 26 | `0x0058DB00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetChargingInvectoryRow` | 26 | `0x0058DAC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetChargingInvectoryLayer` | 26 | `0x0058DA90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemFromChargingInventory` | 2 | `0x0058D9E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUsingCashPetItemInvolveSubInventory` | 33 | `0x0058D320` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetUsingCashItemBySkillTID` | 25 | `0x0058D250` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashItemUsableByType` | 23 | `0x0058D160` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AutoInsert` | 23 | `0x00596EB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ParseFieldPacket` | 15 | `0x0058FEE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemToField` | 22 | `0x0058FDD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `UpdateItemInChargingInventory` | 2 | `0x0058DCC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCashInventoryItemByTID` | 29 | `0x0058D570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetExistReverseOrb` | 165 | `0x0053C6A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetExistCatalyst` | 100 | `0x0053C360` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakePacketItemUse` | 33 | `0x0053ACF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetItemSequence` | 9 | `0x0053A510` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacterTemplate` | 5 | `0x0053A4B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetADCharacter` | 5 | `0x0053A480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateOptionTemplate` | 14 | `0x0053A190` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DestroyItem` | 26 | `0x0053A100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `GetEquipIndexFromTable` (`0x0058EB80`), `DestroyOptionTemplate` (`0x00541580`), `GetInventory` (`0x005403E0`), `GetCashInventoryGrid` (`0x005403E0`), `GetCashInventoryGrid` (`0x005403E0`), `AddItem` (`0x005873E0`), `RemoveItem` (`0x0053D510`), `GetItem` (`0x0053BA30`), `GetItemLock` (`0x0053F550`), `GetItemTemplate` (`0x0058EB80`), `ProcessRefreshUI` (`0x0053A530`), `ProcessRefreshCount` (`0x0053E0E0`), `ProcessRefreshCount` (`0x0053A530`), `OnOperationUpdate` (`0x0058FB20`), `CheckUseItem` (`0x0057C190`), `PickupItem` (`0x0053F550`), `GetBoundType` (`0x0053EAD0`), `IsBoundOnOwner` (`0x0058D410`), `SetBoundOnOwner` (`0x0053EAD0`), `IsProperPart` (`0x00595300`), `AddItemOption` (`0x00582EE0`), `RemoveStatus` (`0x00591FF0`), `GetWeaponType` (`0x0058EB80`), `UpdateItemInBank` (`0x0053D510`), `AddItemToCashInventory` (`0x0053D2C0`), `GetCashItemByTID` (`0x0053BA30`), `RemoveItemFromCashInventory` (`0x0053BA30`), `ArrangeCashItemGridPos` (`0x0053BA30`), `GetCashSkillRollbackScroll` (`0x00564630`), `GetEquipItem` (`0x0053BA30`), `EquipItem` (`0x0058FB20`), `EquipItem` (`0x0053A440`), `UnEquipItem` (`0x0053A440`), `IsEquipBow` (`0x0058F900`), `IsEquipCrossBow` (`0x0058F900`), `IsEquipKatariya` (`0x0058F900`), `AddItemToInventory` (`0x0053D510`), `AddItemToInventory` (`0x0053D510`), `AddItemToInventoryResult` (`0x0058D880`), `UpdateItemInInventory` (`0x0053D510`), `RemoveItemFromInventory` (`0x0053B200`), `GetSkillRollbackScroll` (`0x00564630`), `SetDefaultEquipments` (`0x0054B260`), `SetDefaultEquipments` (`0x0054B260`), `SetDefaultInventoryItems` (`0x0054B260`), `SetDefaultInventoryItems` (`0x0054B260`), `StreamReadOptionData` (`0x00547A40`), `StreamReadBankSlotPrice` (`0x00546C70`), `AddItemTemplateEntry` (`0x0054A590`), `GetItemTemplateName` (`0x0054A590`), `AddItemToSubInventoryResult` (`0x0058D880`), `AddItemToUnseenInventoryResult` (`0x0058D880`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmCharacter`](AgpmCharacter.md), [`AgpmItemConvert`](AgpmItemConvert.md)
- **Erwähnt in:** [`AgcUIQuestText`](AgcUIQuestText.md), [`AgcmAuction`](AgcmAuction.md), [`AgcmCashMall`](AgcmCashMall.md), [`AgcmCharacter_Angriff`](AgcmCharacter_Angriff.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmItem`](AgcmItem.md), [`AgcmRide`](AgcmRide.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIChargingInventory`](AgcmUIChargingInventory.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgcmUIEventBank`](AgcmUIEventBank.md), [`AgcmUIEventItemRepair`](AgcmUIEventItemRepair.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgcmUIQuest2`](AgcmUIQuest2.md), [`AgcmUIRefinery`](AgcmUIRefinery.md), [`AgcmUIShrineShop`](AgcmUIShrineShop.md), [`AgcmUISiegeWar`](AgcmUISiegeWar.md), [`AgpmAuctionCategory`](AgpmAuctionCategory.md), [`AgpmCombat`](AgpmCombat.md), [`AgpmSkill`](AgpmSkill.md), [`NPC_Trade_Dialog`](NPC_Trade_Dialog.md)
