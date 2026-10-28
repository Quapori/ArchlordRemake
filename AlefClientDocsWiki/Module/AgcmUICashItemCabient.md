# AgcmUICashItemCabient (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Untersuchung des Quellverzeichnisses `AgcmUICashItemCabient` (Gutschein-Fenster: `AgcmUICouponBox`, `CouponTexture`, `CouponDisplayInfo`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Zeichenkettensuche im Binary, Vtable-Liste und Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmUICashItemCabient/`. Das Modul gehört nicht zum 2017er Build.

## Kernbefund

- **Abdeckung:** 0 von 46 Quellmethoden (38 in `AgcmUICouponBox`, 6 in `CouponTexture`, 2 in `CouponDisplayInfo`) haben Code im Binary.
- **Beleg:** Kein Klassen-, RTTI- oder UI-Name des Moduls ist als Zeichenkette im Binary vorhanden.
- **Grund:** Die Quelle baut das Modul nur für `_AREA_TAIWAN_`; der Client ist der Global-Build.
- **Abweichungen:** Keine im eigentlichen Sinn – das Modul fehlt vollständig.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUICashItemCabient.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 1 | `OnInit` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 2 | `OnDestroy` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 3 | `AddUserData` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 4 | `AddFunction` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 5 | `AddDisplay` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 6 | `AddEvent` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 7 | `AddBoolean` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 8 | `OnReceive` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 9 | `OnUpdateCashItemCount` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 10 | `CBDisplayCashInvenUseItemButtonText` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 11 | `CBDisplayCashInvenItemInfoName` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 12 | `CBDisplayCashInvenItemInfoCount` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 13 | `CBDisplayCashInvenUsingItem` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 14 | `CBDisplayCashInvenEnableTrade` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 15 | `CBCashInvenClickUseItem` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 16 | `RefreshItemGrid` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 17 | `CBCashInvenOpenUI` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 18 | `CBUpdateItemCashInventory` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 19 | `CBAddCoupon` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 20 | `AddCoupon` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 21 | `CBUseCoupon` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 22 | `CashInvenOpenUI` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 23 | `EraseCouponItem` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 24 | `EraseCouponItemAll` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 25 | `DestroyCouponItemAll` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 26 | `Open` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 27 | `Close` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 28 | `CBSetSelfCharacter` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 29 | `CBReleaseSelfCharacter` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 30 | `CBKeydownESC` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 31 | `CBGetItemTimeInfo` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 32 | `CBGetItemStaminaTime` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 33 | `RemoveCoupon` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 34 | `IsSelfOperation` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 35 | `CBDisplayCashInvenStaminaMax` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 36 | `CBDisplayCashInvenStaminaCurrent` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 37 | `CheckPetStateGrid` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 38 | `CouponTexture::OnSetFocus` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 39 | `CouponTexture::OnKillFocus` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 40 | `CouponTexture::OnWindowRender` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 41 | `CouponTexture::SetItemTID` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 42 | `CouponTexture::SetTexture` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 43 | `CouponTexture::SetTexture` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 44 | `CouponDisplayInfo::load` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |
| 45 | `CouponDisplayInfo::get` | – | | nicht im Binary (Modul nur für `_AREA_TAIWAN_` gebaut) |

0 von 46 Quellmethoden sind einer Binary-Adresse zugeordnet.

## Befund

Das Verzeichnis `AgcmUICashItemCabient` enthält in der Quelle die Klassen `AgcmUICouponBox` (Gutschein-Fenster), `CouponTexture` und `CouponDisplayInfo` (Dateien `AgcmUICouponBox.cpp`, `AgcmUICopon.cpp`). Eine Klasse `AgcmUICashItemCabient` gibt es nicht.
**Im 2017er Build ist nichts davon enthalten.** Weder die Klassennamen (`AgcmUICouponBox`, `CouponTexture`, `CouponDisplayInfo`, auch nicht als RTTI-Name `.?AV…`) noch eine der registrierten UI-Zeichenketten (`CouponBox_UIOpen`, `CouponBox_ClickUseItem`, `CouponBox_OpenUI`, `CouponBox_Grid_Item_List`, `CouponBox_Stamina`, `UI_CouponBox`) kommen im Binary vor; auch das Wort `Coupon` fehlt. Es gibt dazu keine Vtable.
**Ursache laut Quelle:** `AgcmUICashInven` schaltet die Gutschein-Box nur in `#ifdef _AREA_TAIWAN_` ein (`GetModule("AgcmUICouponBox")`, dann `Open`/`Close`). Der Global-Build (`_AREA_GLOBAL_`) enthält das Modul daher nicht; im Bericht [AgcmUICashInven](AgcmUICashInven.md) kommen diese Aufrufe folgerichtig nicht vor.
**Rest im Binary:** Nur die Paketseite ist vorhanden: [`AgpmCharacter`](AgpmCharacter.md):OnOperationRequestCouponInfo`, `…RequestCouponUse`, `…AnswerCouponUse` und `…RecieveCouponInfo` (`0x005037B0`–`0x00503810`) sind winzige Rümpfe, die ein Callback-Ereignis (`0x7B` usw.) auslösen; es gibt keinen Empfänger dafür in der Oberfläche. Das Paketformat steht im Bericht zu `AgpmCharacter`.

## Abweichungen von der EP8-Quelle

- Das gesamte Modul fehlt im Binary; die Quelle enthält es, schaltet es aber nur unter `_AREA_TAIWAN_` ein.

## Grenzen

- Die Aussage beruht auf der Abwesenheit aller Zeichenketten und Klassennamen im Binary sowie dem Fehlen einer passenden Vtable; ein hartes Muster einzelner Funktionen ohne Zeichenketten wurde nicht gesucht.
- Der Wert von `_AREA_TAIWAN_` bei der Übersetzung ergibt sich nur mittelbar aus dem Fehlen der Zeichenketten.

## Querverweise

- **Erwähnt Module:** [`AgcmUICashInven`](AgcmUICashInven.md), [`AgpmCharacter`](AgpmCharacter.md)
