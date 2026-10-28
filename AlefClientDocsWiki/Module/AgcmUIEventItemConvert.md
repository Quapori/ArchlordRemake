# AgcmUIEventItemConvert (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIEventItemConvert` (Item-Umwandlung: physisch, Sockel, Rune, Geisterstein) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIEventItemConvert/fünf Dateien`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 56 von 59 Quellmethoden sind zugeordnet; in diesem Durchgang kamen 23 hinzu (alle `Init/Check/ThrowEvent/Start/Update/Set…Result` der drei Arten, `RecalcConvertCost`, vier `RefreshUserData…`).
- **Arten:** die Zuordnung der drei Umwandlungsarten ist über die Aufrufe in `CBStartConvert`/`CBConvertOK` und die UI-Texte der Bestätigungen gesichert.
- **UI:** 13 Funktionen, 3 Anzeigen, 6 Benutzerdaten, 30 Ereignisse – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIEventItemConvert.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006BD650` | 598 | vtable/String |
| 1 | `OnInit` | `0x006BC0B0` | 116 | vtable/String |
| 2 | `OnDestroy` | `0x006BC130` | 46 | vtable/String |
| 3 | `OnIdle` | `0x006BC160` | 58 | vtable/String |
| 4 | `AddEvent` | `0x006BC1A0` | 1010 | Zeichenkette |
| 5 | `AddFunction` | `0x006BD420` | 555 | Zeichenkette |
| 6 | `AddDisplay` | `0x006BD000` | 107 | Zeichenkette |
| 7 | `AddUserData` | `0x006BC5A0` | 255 | Zeichenkette |
| 8 | `CBReceiveGrant` | `0x006BC6A0` | 200 | Callback-Registrierung |
| 9 | `CBSelfUpdatePosition` | `0x006BC770` | 136 | Callback-Registrierung |
| 10 | `CBAddConvertGridItem` | `0x006BD070` | 480 | UI-Registrierung |
| 11 | `CBAddConvertGridItemSocket` | `0x006BD250` | 312 | UI-Registrierung |
| 12 | `CBStartConvert` | `0x006BC800` | 80 | UI-Registrierung |
| 13 | `CBConvertOK` | `0x006BC850` | 128 | UI-Registrierung |
| 14 | `CBConvertCancel` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 15 | `CBUpdateConvertConfirm` | `0x006BC8D0` | 86 | UI-Registrierung |
| 16 | `CBSetNPCConv` | `0x006BC930` | 39 | UI-Registrierung |
| 17 | `CBRemoveItem` | `0x006BD390` | 139 | Callback-Registrierung |
| 18 | `CBDisplayConvertItemName` | `0x006BC960` | 313 | UI-Registrierung |
| 19 | `CBDisplayConvertCost` | `0x006BCAA0` | 88 | UI-Registrierung |
| 20 | `CBDisplayConvertCostPayResult` | `0x006BCB00` | 127 | UI-Registrierung |
| 21 | `CBDisplayConvertPhysicalResult` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `RefreshUserDataGrid` | `0x006BCB80` | 36 | ver |
| 23 | `RefreshUserDataGridSocket` | `0x006BCBB0` | 36 | ver |
| 24 | `RefreshUserDataConvertCost` | `0x006BCBE0` | 36 | ver |
| 25 | `RefreshUserDataConvertType` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `RefreshUserDataConvertItem` | `0x006BCC10` | 36 | ver |
| 27 | `RefreshUserDataConvertResult` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `PlayEffectSuccess` | `0x006BCC40` | 166 | Zeichenkette |
| 29 | `PlayEffectFailed` | `0x006BCCF0` | 166 | Zeichenkette |
| 30 | `CBGetPhysicalEditControl` | `0x006BCDA0` | 31 | UI-Registrierung |
| 31 | `CBGetRuneEditControl` | `0x006BCDC0` | 31 | UI-Registrierung |
| 32 | `CBGetSocketEditControl` | `0x006BCDE0` | 31 | UI-Registrierung |
| 33 | `CBSetPhysicalConvert` | `0x0077FE50` | 16 | UI-Registrierung |
| 34 | `InitPhysicalConvertUI` | `0x0077F990` | 307 | ver |
| 35 | `CheckPhysicalConvert` | `0x0077FAD0` | 403 | ver |
| 36 | `ThrowEventPhysicalConvertable` | `0x0077FC70` | 18 | ver |
| 37 | `StartPhysicalConvert` | `0x0077FC90` | 282 | ver |
| 38 | `UpdatePhysicalConvertConfirm` | `0x0077F4A0` | 485 | ver |
| 39 | `CBResultPhysicalConvert` | `0x0077FDB0` | 126 | Callback-Registrierung |
| 40 | `SetPhysicalResult` | `0x0077F690` | 730 | ver |
| 41 | `CBSetRuneConvert` | `0x00780F50` | 23 | UI-Registrierung |
| 42 | `InitRuneConvertUI` | `0x00780A60` | 268 | ver |
| 43 | `CheckRuneConvert` | `0x00780B70` | 327 | ver |
| 44 | `ThrowEventRuneConvertable` | `0x00780CC0` | 5 | ver |
| 45 | `StartRuneConvert` | `0x00780CD0` | 244 | ver |
| 46 | `UpdateRuneConvertConfirm` | `0x007805F0` | 341 | ver |
| 47 | `CBResultRuneConvert` | `0x00780DE0` | 310 | Callback-Registrierung |
| 48 | `SetRuneResult` | `0x00780750` | 729 | ver |
| 49 | `CBSetSocketConvert` | `0x007805D0` | 23 | UI-Registrierung |
| 50 | `InitSocketConvertUI` | `0x007802F0` | 244 | ver |
| 51 | `CheckSocketConvert` | `0x007803F0` | 189 | ver |
| 52 | `ThrowEventSocketConvertable` | `0x007804B0` | 5 | ver |
| 53 | `StartSocketConvert` | `0x007804C0` | 154 | ver |
| 54 | `UpdateSocketConvertConfirm` | `0x0077FE60` | 354 | ver |
| 55 | `CBResultSocketConvert` | `0x00780560` | 103 | Callback-Registrierung |
| 56 | `RecalcConvertCost` | `0x0077FFD0` | 178 | ver |
| 57 | `SetSocketResult` | `0x00780090` | 570 | ver |
| 58 | `CBResultSpiritStoneConvert` | `0x00780F70` | 190 | Callback-Registrierung |

56 von 59 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x006BC050`), `AgcmUIEventItemConvert` (`0x006BCE00`), `~AgcmUIEventItemConvert` (`0x006BCFE0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Klasse` | ``m_eConvertType`, `m_ulNextRequestConvertTime`, `m_bIsRequestConvert`` | `CBStartConvert`, `CBConvertOK` |

## Umfang

Die Klasse `AgcmUIEventItemConvert` verteilt sich in der Quelle auf fünf Dateien (`AgcmUIEventItemConvert.cpp`, `…PhysicalConvert.cpp`, `…RuneConvert.cpp`, `…SocketConvert.cpp`, `…SpiritStoneConvert.cpp`; zusammen 59 Methoden). Im Binary liegt der Hauptteil bei `0x006BC050`–`0x006BD650`, die Umwandlungsarten bei `0x0077F4A0`–`0x00780F70`.

## Vtable

Vtable bei `0x008D36E4`: Slot 0 Destruktor `0x006BCFE0`, 1 `OnAddModule` (`0x006BD650`), 2 `OnInit` (`0x006BC0B0`), 3 `OnIdle` (`0x006BC160`), 7 `OnDestroy` (`0x006BC130`).

## Umwandlungsarten

`CBStartConvert` (`0x006BC800`) und `CBConvertOK` (`0x006BC850`) verzweigen nach der Umwandlungsart (physisch, Sockel, Rune); `CBUpdateConvertConfirm` ebenso. Die Zuordnung der Zweige ergibt sich aus den Aufrufen:

| Funktion | Physisch | Sockel | Rune |
|---|---|---|---|
| `CBSet…Convert` | `0x0077FE50` | `0x007805D0` | `0x00780F50` |
| `Init…ConvertUI` | `0x0077F990` | `0x007802F0` | `0x00780A60` |
| `Check…Convert` (von `CBStartConvert`) | `0x0077FAD0` | `0x007803F0` | `0x00780B70` |
| `ThrowEvent…Convertable` | `0x0077FC70` | `0x007804B0` | `0x00780CC0` |
| `Start…Convert` (von `CBConvertOK`) | `0x0077FC90` | `0x007804C0` | `0x00780CD0` |
| `Update…ConvertConfirm` | `0x0077F4A0` | `0x0077FE60` | `0x007805F0` |
| `CBResult…Convert` | `0x0077FDB0` | `0x00780560` | `0x00780DE0` |
| `Set…Result` | `0x0077F690` | `0x00780090` | `0x00780750` |

Die Bestätigungsfunktionen sind über ihre UI-Texte unterschieden (`Convert_Physical_Confirm`, `Convert_Socket_Confirm`, `Convert_Rune_Confirm`). `ThrowEventSocketConvertable` und `ThrowEventRuneConvertable` sind nur 5-Byte-Sprünge auf `Set…Result` (wie in der Quelle, deren Rumpf nur `Set…Result` aufruft). `RecalcConvertCost` (`0x0077FFD0`) gehört zum Sockel.
`CBConvertOK` sperrt bei der physischen Umwandlung eine Folgeanfrage für 3000 ms (`m_ulNextRequestConvertTime`).

## Benutzerdaten-Aktualisierung

`RefreshUserDataGrid` (`0x006BCB80`), `…GridSocket` (`0x006BCBB0`), `…ConvertCost` (`0x006BCBE0`) und `…ConvertItem` (`0x006BCC10`) sind 36-Byte-Funktionen mit je einem `SetUserDataRefresh`. `…ConvertType` und `…ConvertResult` sind im Binary nicht als eigene Funktionen zu finden.

## Abbrechen und Anzeige

`Convert_Cancel` zeigt auf den gemeinsamen `return TRUE`-Rumpf `0x0067AC90` (`CBConvertCancel` der Quelle gibt nur TRUE zurück). `CBDisplayConvertPhysicalResult` ist in der Quelle `return TRUE` und wird nirgends als Anzeige angemeldet; im Binary gibt es keine Anmeldung dafür.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006BD420`, `0x006BD000`, `0x006BC5A0`, `0x006BC1A0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (13)

| Name | Id | Handler |
|---|---:|---|
| `Convert_SetPhysicalConvert` |  | `CBSetPhysicalConvert` |
| `Convert_SetSocketConvert` |  | `CBSetSocketConvert` |
| `Convert_SetRuneConvert` |  | `CBSetRuneConvert` |
| `Convert_AddItem` |  | `CBAddConvertGridItem` |
| `Convert_AddItemSocket` |  | `CBAddConvertGridItemSocket` |
| `Convert_Start` |  | `CBStartConvert` |
| `Convert_OK` |  | `CBConvertOK` |
| `Convert_Cancel` |  | `Element::GetSize` |
| `Convert_Update_ConvertConfirm` |  | `CBUpdateConvertConfirm` |
| `Convert_Set_NPCConv` |  | `CBSetNPCConv` |
| `Convert_GetPhysicalEditControl` |  | `CBGetPhysicalEditControl` |
| `Convert_GetRuneEditControl` |  | `CBGetRuneEditControl` |
| `Convert_GetSocketEditControl` |  | `CBGetSocketEditControl` |

**Anzeige** (3)

| Name | Id | Handler |
|---|---:|---|
| `Display_ConvertItemName` | 2 | `CBDisplayConvertItemName` |
| `Display_ConvertCost` | 0 | `CBDisplayConvertCost` |
| `Display_ConvertCostPayResult` | 1 | `CBDisplayConvertCostPayResult` |

**UserData** (6)

| Name | Id | Handler |
|---|---:|---|
| `Convert_Grid` |  | – |
| `Convert_Grid_Socket` |  | – |
| `Convert_Cost` |  | – |
| `Convert_Type` |  | – |
| `Convert_Item` |  | – |
| `Convert_Result` |  | – |

**Ereignis** (30)

| Name | Id | Handler |
|---|---:|---|
| `Convert_MainUI_Open` | 0 | – |
| `Convert_UI_Close` | 0 | – |
| `Convert_UI_Open` | 0 | – |
| `Convert_Confirm` | 0 | – |
| `Convert_SS_Result_Success` | 0 | – |
| `Convert_SS_Result_Fail` | 0 | – |
| `Convert_SS_Result_ImproperItem` | 0 | – |
| `Convert_SS_Result_AlreadyFull` | 0 | – |
| `Convert_Physical_Result_AlreadyFull` | 0 | – |
| `Convert_Physical_Result_ImproperItem` | 0 | – |
| `Convert_Socket_Result_ImproperItem` | 0 | – |
| `Convert_Socket_Result_NotEnoughMoney` | 0 | – |
| `Convert_Socket_Result_AlreadyFull` | 0 | – |
| `Convert_Socket_NotEnoughInvenMoney` | 0 | – |
| `Convert_Socket_EnoughInvenMoney` | 0 | – |
| `Convert_Rune_Result_NotEnoughSocket` | 0 | – |
| `Convert_Err_AlreadyFull` | 0 | – |
| `Convert_Err_NotExistItem` | 0 | – |
| `Convert_Err_InvalidCatalyst` | 0 | – |
| `Convert_Err_InvalidRune` | 0 | – |
| `Convert_Err_NotEnoughSocket` | 0 | – |
| `Convert_Err_LowCharLevel` | 0 | – |
| `Convert_Err_LowItemLevel` | 0 | – |
| `Convert_Err_ImproperPart` | 0 | – |
| `Convert_Err_NotEnoughMoney` | 0 | – |
| `Convert_Err_TryEquipItem` | 0 | – |
| `Convert_Err_AlreadyAntiConvert` | 0 | – |
| `Convert_Update_NPCConv` | 0 | – |
| `Convert_Update_ConvertInfo` | 0 | – |
| `Convert_Update_ConvertConfirm` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Verzweigung in `CBStartConvert`/`CBConvertOK`, Bestätigungstexte).

## Grenzen

- `RefreshUserDataConvertType` und `…ConvertResult` sind eingebaut oder zusammengefaltet.
- `CBDisplayConvertPhysicalResult` ist im Binary nicht zu finden.
- Die Zuordnung der `Check…`-, `Start…`- und `Set…Result`-Funktionen stützt sich auf Aufrufer, Größe und Aufgerufene; nur die drei `Update…ConvertConfirm` wurden über ihre UI-Texte einzeln geprüft (physisch nur über die Größe und den Text `Convert_Physical_Confirm`).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht im Client: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->
