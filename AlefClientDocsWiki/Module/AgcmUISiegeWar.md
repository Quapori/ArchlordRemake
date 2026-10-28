# AgcmUISiegeWar (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUISiegeWar` (Belagerungskrieg: Bewerbung, Kriegszeit, Katapult/Turm, Meldungen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUISiegeWar/AgcmUISiegeWar.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 98 von 120 Quellmethoden sind einer Adresse zugeordnet (16 davon als gemeinsame Rümpfe); neu sind 26 Funktionen, u. a. `OpenCatapultUI`, `OpenAtkResTowerUI`, `SetMainUIEdit`, `SetComboBoxData`, `GetComboTime`, `SetTextEffect`, `SetRemainTimeEdit` und `AddBoolean`. Die 22 fehlenden sind in der Quelle auskommentiert, ohne Aufrufer oder eingebaut.
- **UI:** 32 Funktionen, 14 Anzeigen, 5 Bool-Anzeigen, 16 Benutzerdaten und 64 Ereignisse (laut Registrierungstabellen im Binary).
- **Zeit:** Kriegsbeginn 20, 21 oder 22 Uhr an einem von zwei Tagen (Kombifelder).
- **Meldungen:** höchstens eine pro 2000 ms als Text-Effekt; `SetInfoEdit` fehlt im Binary.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUISiegeWar.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00691520` | 1096 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 2 | `OnDestroy` | `0x006906C0` | 17 | vtable/String |
| 3 | `OnIdle` | `0x006906E0` | 375 | vtable/String |
| 4 | `AddEvent` | `0x0068BD90` | 2166 | Zeichenkette |
| 5 | `AddFunction` | `0x00690160` | 1368 | Zeichenkette |
| 6 | `AddUserData` | `0x0068C610` | 697 | Zeichenkette |
| 7 | `AddDisplay` | `0x0068EC30` | 463 | Zeichenkette |
| 8 | `AddBoolean` | `0x0068EE00` | 166 | manual |
| 9 | `CBUpdateCastleInfo` | `0x0068FD20` | 48 | Callback-Registrierung |
| 10 | `CBReceiveResult` | `0x0068C8D0` | 738 | Callback-Registrierung |
| 11 | `CBReceiveAttackApplGuildList` | `0x0068CC00` | 397 | Callback-Registrierung |
| 12 | `CBReceiveDefenseApplGuildList` | `0x0068EEB0` | 347 | Callback-Registrierung |
| 13 | `CBReceiveAttackGuildList` | – | | Anmeldung in der Quelle auskommentiert, nicht im Binary |
| 14 | `CBReceiveDefenseGuildList` | – | | Anmeldung in der Quelle auskommentiert, nicht im Binary |
| 15 | `OpenCatapultUI` | `0x0068CD90` | 632 | manual |
| 16 | `OpenAtkResTowerUI` | `0x0068D010` | 632 | manual |
| 17 | `CBResponseUseAttackObject` | `0x0068D290` | 106 | Callback-Registrierung |
| 18 | `CBAddItemResult` | `0x0068D300` | 177 | Callback-Registrierung |
| 19 | `CBStatusInfo` | `0x00690C30` | 2131 | Callback-Registrierung |
| 20 | `CBSyncMessage` | `0x0068F010` | 1012 | Callback-Registrierung |
| 21 | `CBUpdateStatus` | `0x0068F410` | 296 | Callback-Registrierung |
| 22 | `CBIsFriendGuild` | – | | Anmeldung in der Quelle auskommentiert, nicht im Binary |
| 23 | `CBIsEnemyGuild` | – | | Anmeldung in der Quelle auskommentiert, nicht im Binary |
| 24 | `CBEventGrant` | `0x0068FD50` | 167 | Callback-Registrierung |
| 25 | `CBSetSelfCharacter` | `0x0068D3C0` | 480 | Callback-Registrierung |
| 26 | `CBSelfUpdatePosition` | `0x0068D5A0` | 196 | Callback-Registrierung |
| 27 | `CBRemoveSiegeWarGrid` | `0x0068F540` | 222 | Callback-Registrierung |
| 28 | `CBRemoveItem` | `0x0068F620` | 236 | Callback-Registrierung |
| 29 | `CBUpdateActionStatus` | `0x0068D670` | 300 | Callback-Registrierung |
| 30 | `CBChangeCharacterBindingRegion` | `0x00561430` | 23 | gleiche Adresse wie `gemeinsamer Rumpf (return pData && pClass)` (vom Linker zusammengefaltet) |
| 31 | `CBEndCooldown` | `0x0068D7A0` | 39 | Callback-Registrierung |
| 32 | `CBInputSiegeWarMessage` | – | | Anmeldung in der Quelle auskommentiert, nicht im Binary |
| 33 | `CBSetTargetCharacter` | `0x0068D7D0` | 152 | Callback-Registrierung |
| 34 | `CBResetTargetCharacter` | `0x0068D870` | 63 | Callback-Registrierung |
| 35 | `CBGetMainUIDescEdit` | `0x0068D8B0` | 46 | UI-Registrierung |
| 36 | `CBGetMainUISiegeWarTimeEdit` | `0x0068D8E0` | 46 | UI-Registrierung |
| 37 | `CBGetAttackHelpEdit` | `0x0068D910` | 46 | UI-Registrierung |
| 38 | `CBGetAttackSiegeWarTimeEdit` | `0x0068D940` | 46 | UI-Registrierung |
| 39 | `CBGetDefenseHelpEdit` | `0x0068D970` | 46 | UI-Registrierung |
| 40 | `CBGetDefenseGuildInfoEdit` | `0x0068D9A0` | 46 | UI-Registrierung |
| 41 | `CBGetDateCombo` | `0x0068D9D0` | 46 | UI-Registrierung |
| 42 | `CBGetHourCombo` | `0x0068DA00` | 46 | UI-Registrierung |
| 43 | `CBOpenSiegeWarTimeSetUI` | `0x0068F710` | 289 | UI-Registrierung |
| 44 | `CBOpenAttackApplicationUI` | `0x0068FE00` | 228 | UI-Registrierung |
| 45 | `CBOpenDefenseApplicationUI` | `0x0068F840` | 71 | UI-Registrierung |
| 46 | `SetSiegeWarTimeEdit` | `0x0068DA30` | 522 | Zeichenkette |
| 47 | `SetMainUIEdit` | `0x0068F890` | 349 | manual |
| 48 | `SetSiegeWarTimeUIEdit` | `0x0068DC40` | 472 | manual |
| 49 | `SetSiegeWarDefenseHelpEdit` | `0x0068DE20` | 78 | manual |
| 50 | `SetSiegeWarDefenseGuildInfoEdit` | `0x0068DE70` | 297 | manual |
| 51 | `SetSiegeWarInfoEdit` | – | | nur von auskommentierten Stellen benutzt, nicht im Binary |
| 52 | `SetRemainTimeEdit` | `0x0068F9F0` | 341 | manual |
| 53 | `SetComboBoxData` | `0x0068DFA0` | 400 | manual |
| 54 | `CBDisplayNPCName` | `0x0068E130` | 123 | UI-Registrierung |
| 55 | `CBDisplayAttackGuildName` | `0x0068E200` | 57 | gleiche Adresse wie `Rumpf gleich mit CBDisplayDefenseGuildName` (vom Linker zusammengefaltet) |
| 56 | `CBDisplayAttackGuildMasterName` | `0x0068E240` | 62 | gleiche Adresse wie `Rumpf gleich mit CBDisplayDefenseGuildMasterName` (vom Linker zusammengefaltet) |
| 57 | `CBDisplayAttackGuildPoint` | `0x0068E1B0` | 80 | gleiche Adresse wie `Rumpf gleich mit CBDisplayDefenseGuildPoint` (vom Linker zusammengefaltet) |
| 58 | `CBDisplayDefenseGuildName` | `0x0068E200` | 57 | gleiche Adresse wie `Rumpf gleich mit CBDisplayAttackGuildName` (vom Linker zusammengefaltet) |
| 59 | `CBDisplayDefenseGuildMasterName` | `0x0068E240` | 62 | gleiche Adresse wie `Rumpf gleich mit CBDisplayAttackGuildMasterName` (vom Linker zusammengefaltet) |
| 60 | `CBDisplayDefenseGuildPoint` | `0x0068E1B0` | 80 | gleiche Adresse wie `Rumpf gleich mit CBDisplayAttackGuildPoint` (vom Linker zusammengefaltet) |
| 61 | `CBDisplayAttackPageNumber` | `0x0068E280` | 113 | UI-Registrierung |
| 62 | `CBDisplayDefensePageNumber` | `0x0068E300` | 113 | UI-Registrierung |
| 63 | `CBDisplayComboDate` | `0x0068E380` | 50 | gleiche Adresse wie `Rumpf gleich mit CBDisplayComboHour` (vom Linker zusammengefaltet) |
| 64 | `CBDisplayComboHour` | `0x0068E380` | 50 | gleiche Adresse wie `Rumpf gleich mit CBDisplayComboDate` (vom Linker zusammengefaltet) |
| 65 | `CBDisplayUseCharacterName` | `0x0068E3C0` | 47 | UI-Registrierung |
| 66 | `CBDisplayRepairBarMax` | `0x0068E3F0` | 57 | UI-Registrierung |
| 67 | `CBDisplayRepairBarCurrent` | `0x0068E430` | 87 | UI-Registrierung |
| 68 | `CBIsActiveCatapultRepairButton` | `0x0068E490` | 11 | UI-Registrierung |
| 69 | `CBIsActiveCatapultActiveButton` | `0x0068E4A0` | 11 | UI-Registrierung |
| 70 | `CBIsActiveAtkResTowerRepairButton` | `0x0068E4B0` | 11 | UI-Registrierung |
| 71 | `CBIsActiveAtkResTowerActiveButton` | `0x0068E4C0` | 11 | UI-Registrierung |
| 72 | `CBIsActiveAttackApplButton` | `0x0068E4D0` | 11 | UI-Registrierung |
| 73 | `CBConfirmSiegeWarTime` | `0x0068FB50` | 94 | UI-Registrierung |
| 74 | `CBSelectDefenseGuild` | `0x0068FEF0` | 161 | UI-Registrierung |
| 75 | `CBApplicationDefense` | `0x0068E4E0` | 218 | UI-Registrierung |
| 76 | `CBCancelDefense` | `0x0068E5C0` | 114 | UI-Registrierung |
| 77 | `CBApplicationAttack` | `0x0068E640` | 194 | UI-Registrierung |
| 78 | `CBAttackPageLeft` | `0x0068FFA0` | 54 | UI-Registrierung |
| 79 | `CBAttackPageRight` | `0x0068FFE0` | 66 | UI-Registrierung |
| 80 | `CBAttackGoPage` | `0x00690030` | 80 | UI-Registrierung |
| 81 | `CBDefensePageLeft` | `0x00690080` | 54 | UI-Registrierung |
| 82 | `CBDefensePageRight` | `0x006900C0` | 66 | UI-Registrierung |
| 83 | `CBDefenseGoPage` | `0x00690110` | 80 | UI-Registrierung |
| 84 | `CBDefenseGuildListSelect` | `0x0068FBB0` | 106 | UI-Registrierung |
| 85 | `CBGetCatapultDescEdit` | `0x0068E710` | 46 | UI-Registrierung |
| 86 | `CBGetAtkResTowerDescEdit` | `0x0068E740` | 46 | UI-Registrierung |
| 87 | `CBRepairCatapult` | `0x0068E770` | 28 | gleiche Adresse wie `Rumpf gleich mit CBRepairAtkResTower` (vom Linker zusammengefaltet) |
| 88 | `CBRepairAtkResTower` | `0x0068E770` | 28 | gleiche Adresse wie `Rumpf gleich mit CBRepairCatapult` (vom Linker zusammengefaltet) |
| 89 | `CBActiveCatapult` | `0x0068E790` | 28 | gleiche Adresse wie `Rumpf gleich mit CBActiveAtkResTower` (vom Linker zusammengefaltet) |
| 90 | `CBActiveAtkResTower` | `0x0068E790` | 28 | gleiche Adresse wie `Rumpf gleich mit CBActiveCatapult` (vom Linker zusammengefaltet) |
| 91 | `CBCatapultDragDrop` | `0x0068E7B0` | 131 | gleiche Adresse wie `Rumpf gleich mit CBAtkResTowerDragDrop` (vom Linker zusammengefaltet) |
| 92 | `CBAtkResTowerDragDrop` | `0x0068E7B0` | 131 | gleiche Adresse wie `Rumpf gleich mit CBCatapultDragDrop` (vom Linker zusammengefaltet) |
| 93 | `CBGetSiegeWarInfoEditControl` | – | | Registrierung in der Quelle auskommentiert, nicht im Binary |
| 94 | `CBGetRemainTimeEditControl` | – | | Registrierung in der Quelle auskommentiert, nicht im Binary |
| 95 | `CBSiegeWarInfoScrollUp` | – | | Registrierung in der Quelle auskommentiert, nicht im Binary |
| 96 | `CBSiegeWarInfoScrollDown` | – | | Registrierung in der Quelle auskommentiert, nicht im Binary |
| 97 | `CBRegisterDefenseGuild` | `0x0068E840` | 73 | UI-Registrierung |
| 98 | `SetAttackGuildPage` | `0x0068FC20` | 118 | manual |
| 99 | `SetDefenseGuildPage` | `0x0068FCA0` | 118 | manual |
| 100 | `GetComboTime` | `0x0068E890` | 226 | manual |
| 101 | `SetAttackSelectPageSlot` | `0x0068E980` | 69 | manual |
| 102 | `SetDefenseSelectPageSlot` | `0x0068E9D0` | 69 | manual |
| 103 | `IsInAttackGuild` | – | | nur von den auskommentierten CBIsFriendGuild/CBIsEnemyGuild benutzt, nicht im Binary |
| 104 | `IsInDefenseGuild` | – | | nur von den auskommentierten CBIsFriendGuild/CBIsEnemyGuild benutzt, nicht im Binary |
| 105 | `SetCallbackReceiveAttackGuildList` | – | | nicht im Binary (kein Aufrufer) |
| 106 | `SetCallbackReceiveEnemyGuildList` | – | | nicht im Binary (kein Aufrufer) |
| 107 | `OpenSiegeWarInfo` | – | | nicht im Binary (kein Aufrufer) |
| 108 | `CloseSiegeWarInfo` | – | | nicht im Binary (kein Aufrufer) |
| 109 | `SetRemainTime` | – | | nicht im Binary (kein Aufrufer) |
| 110 | `SetInfoEdit` | – | | im Binary nicht erhalten (OnIdle ruft ihn nicht mehr) |
| 111 | `SetTextEffect` | `0x0068EA20` | 267 | manual |
| 112 | `SetSelectedDefenseGuild` | `0x0068EB30` | 123 | manual |
| 113 | `SetUseCharName` | – | | vermutlich in den Aufrufer eingebaut |
| 114 | `IsUsableItemForCatapult` | `0x0068EBB0` | 62 | manual |
| 115 | `IsUsableItemForAtkResTower` | `0x0068EBF0` | 62 | manual |
| 116 | `UpdateSiegeWarInfoUI` | – | | vermutlich eingebaut oder entfernt |
| 117 | `_SetMessageText` | – | | nicht im Binary (kein Aufrufer) |
| 118 | `_SetMsgTextToEditBox` | – | | nicht im Binary (kein Aufrufer) |
| 119 | `_SelfPrintShrineMessageChat` | `0x00690860` | 102 | manual |

98 von 120 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006908d0` (`0x006908D0`), `ctor_or_dtor_00690bd0` (`0x00690BD0`), `~AgcmUISiegeWar` (`0x00691500`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBCC` | `Zeiger auf [`AgcmUICharacter`](AgcmUICharacter.md) (Ziel des Charakters)` | `OnIdle` |
| `0xBA4` | `Zeiger auf [`AgpmSiegeWar`](AgpmSiegeWar.md)` | `IsUsableItemFor…` |
| `0xD28…0xD5C` | `Textfelder und Kombifelder (u. a. `+0xD38` Verteidigungs-Hilfe, `+0xD40` Katapult-Beschreibung, `+0xD5C` Burg)` | `Set…Edit`, `Open…UI` |
| `0x1998` | `Zeiger auf das Modul, das Reparieren, Aktivieren und Ablegen ausführt (Aufrufe `0x006E0A60`, `0x006E09E0`, `0x006E0B70`)` | `CBRepairCatapult`, `CBActiveCatapult`, `CBCatapultDragDrop` |
| `0x19E0` | `Flag „Fenster geöffnet“ (`m_bOpenUI`)` | `CBSelfUpdatePosition` |
| `0x2024…0x2038` | `Anfangs-/Ende-/Auswahlseite für Angriff und Verteidigung` | `SetAttackGuildPage`, `SetDefenseGuildPage` |
| `0x2040 / 0x2044 / 0x2048` | `Reparaturstart / -dauer / Flag „Leiste offen“` | `OnIdle` |
| `0x2450 / 0x2458` | `Meldungsliste (`std::list<string>`) / Zeitzähler` | `OnIdle`, `_SelfPrintShrineMessageChat` |

## Vtable

Vtable bei `0x008CD90C`: Slot 0 Destruktor `0x00691500`, 1 `OnAddModule` (`0x00691520`), 2/6 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`), 3 `OnIdle` (`0x006906E0`), 4/5 gemeinsamer Rumpf `0x0067FAB0`, 7 `OnDestroy` (`0x006906C0`).

## Registrierung (OnAddModule, 0x00691520)

Holt 18 Module ([`ApmMap`](ApmMap.md), [`ApmEventManager`](ApmEventManager.md), `AgpmSiegeWar`, [`AgpmEventSiegeWarNPC`](AgpmEventSiegeWarNPC.md), [`AgpmGuild`](AgpmGuild.md), [`AgpmAdmin`](AgpmAdmin.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmEventSiegeWarNPC`](AgcmEventSiegeWarNPC.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), `AgcmUICharacter`, [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIControl`](AgcmUIControl.md)), meldet dann in dieser Reihenfolge Callbacks an:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmSiegeWar`: Burginfo aktualisiert | `CBUpdateCastleInfo` | `0x0068FD20` |
| `AgpmSiegeWar`: Ergebnis | `CBReceiveResult` | `0x0068C8D0` |
| `AgpmSiegeWar`: Angriffs-Gildenliste (Bewerber) | `CBReceiveAttackApplGuildList` | `0x0068CC00` |
| `AgpmSiegeWar`: Verteidigungs-Gildenliste (Bewerber) | `CBReceiveDefenseApplGuildList` | `0x0068EEB0` |
| `AgpmSiegeWar`: Belagerungsobjekt benutzt | `CBResponseUseAttackObject` | `0x0068D290` |
| `AgpmSiegeWar`: Gegenstand eingesetzt | `CBAddItemResult` | `0x0068D300` |
| `AgpmSiegeWar`: Statusinformation | `CBStatusInfo` | `0x00690C30` |
| `AgpmSiegeWar`: Synchronisations-Meldung | `CBSyncMessage` | `0x0068F010` |
| `AgpmSiegeWar`: Burginfo aktualisiert (zweiter Handler) | `CBUpdateStatus` | `0x0068F410` |
| `AgpmEventSiegeWarNPC`: Ereignis gewährt | `CBEventGrant` | `0x0068FD50` |
| `AgcmCharacter`: eigener Charakter gesetzt | `CBSetSelfCharacter` | `0x0068D3C0` |
| `AgcmCharacter`: eigene Position | `CBSelfUpdatePosition` | `0x0068D5A0` |
| `AgcmUIItem`: Belagerungs-Gitter entfernt | `CBRemoveSiegeWarGrid` | `0x0068F540` |
| `AgpmItem`: Gegenstand entfernt | `CBRemoveItem` | `0x0068F620` |
| `AgpmCharacter`: Aktionsstatus | `CBUpdateActionStatus` | `0x0068D670` |
| `AgpmCharacter`: Sonderstatus | `CBUpdateActionStatus` | `0x0068D670` |
| `AgpmCharacter`: Bindungsregion gewechselt | `CBChangeCharacterBindingRegion` | `0x00561430` (gemeinsamer Rumpf) |
| `AgcmUICharacter`: Ziel gesetzt | `CBSetTargetCharacter` | `0x0068D7D0` |
| `AgcmUICharacter`: Ziel gelöscht | `CBResetTargetCharacter` | `0x0068D870` |

Danach `AddEvent` (`0x0068BD90`, 2166 Byte), `AddFunction` (`0x00690160`), `AddUserData` (`0x0068C610`), `AddDisplay` (`0x0068EC30`), `AddBoolean` (`0x0068EE00`) und zuletzt die Abklingzeit (`RegisterCooldown` mit `CBEndCooldown`, `0x0068D7A0`).
In der Quelle sind weitere Anmeldungen auskommentiert und deshalb nicht im Binary: `CBReceiveAttackGuildList`, `CBReceiveDefenseGuildList`, `CBIsFriendGuild`, `CBIsEnemyGuild` und `CBInputSiegeWarMessage`.

## UI-Funktionen (AddFunction, 0x00690160)

Das Binary registriert **32** Funktionen: 8 Textfeld-/Kombifeld-Übernahmen (`SiegeWarGet…Edit`, `…DateCombo`, `…HourCombo`, mit Beschreibungstext), 3 Fenster-Öffner (Zeit setzen, Angriffs- und Verteidigungsbewerbung), Bestätigen, Gilde wählen, Bewerben/Abbrechen (Verteidigung), Bewerben (Angriff), je 3 Seitenfunktionen (Links, Rechts, Gehe zu) für Angriff und Verteidigung, Gilde eintragen, Listenauswahl, zwei Beschreibungsfelder (Katapult, Angriffs-Wiederbelebungsturm) sowie je Katapult und Turm Reparieren, Aktivieren und Ziehen-und-Ablegen. Die sechs letzten sind paarweise dieselben Rümpfe (`0x0068E770` Reparieren, `0x0068E790` Aktivieren, `0x0068E7B0` Ziehen-und-Ablegen); die Quelle benutzt hier nur andere Tabellenindizes. Vier Registrierungen der Quelle fehlen: `SiegeWarGetInfoEditControl`, `SiegeWarGetRemainTimeEditControl`, `SiegeWarInfoScrollUp` und `…ScrollDown` sind dort auskommentiert; die beiden `GetInfoEditControl`/`GetRemainTimeEditControl` bleiben als Ereignisse erhalten.

## Anzeigen und Bool-Anzeigen

`AddDisplay` legt 14 Anzeigen an: NPC-Name, Angriffs- und Verteidigungs-Gilde je Name, Meister und Punkte (`0x0068E200`, `0x0068E240`, `0x0068E1B0`, je für beide Seiten derselbe Rumpf), beide Seitennummern, Datum/Stunde (derselbe Rumpf `0x0068E380`), Namen des Benutzers und die Reparaturleiste (Maximum/aktuell); `AddBoolean` fünf Schalter (Reparieren/Aktivieren für Katapult und Turm sowie Bewerben). Die fünf Schalter haben je einen 11-Byte-Rumpf (`0x0068E490`…`0x0068E4D0`).

## Zeit des Krieges und Bewerbung

`SetComboBoxData` (`0x0068DFA0`) füllt die Kombifelder: zwei Datumsangaben (der erste Kriegstag und der folgende) und drei Uhrzeiten ab 20 Uhr (`AGPMSIEGEWAR_START_WAR_TIME` 8 + 12 = PM 8, 9, 10). `GetComboTime` (`0x0068E890`) bildet daraus die Zeit: erste Kriegszeit der Burg (oder die nächste) plus gewählte Tage (`× 86 400 × 10 000 000` Zeiteinheiten) und Stunde `20 + Index`. `CBConfirmSiegeWarTime`, `CBApplicationDefense`/`…Attack`, `CBCancelDefense` und `CBSelectDefenseGuild` lösen die Anfragen an `AgpmSiegeWar` aus; die Seitenfunktionen (`SetAttackGuildPage`/`SetDefenseGuildPage`, `0x0068FC20`/`0x0068FCA0`) merken Anfangs- und Auswahlseite und markieren den Seiten-Knopf (`1…9`).

## Belagerungsobjekte (Katapult, Turm)

`OpenCatapultUI` (`0x0068CD90`) und `OpenAtkResTowerUI` (`0x0068D010`, je 632 Byte) füllen das Beschreibungsfeld mit Reparaturanzahl, Kosten und Dauer aus den Anhangsdaten des Objekts. `IsUsableItemForCatapult` (`0x0068EBB0`) und `IsUsableItemForAtkResTower` (`0x0068EBF0`) prüfen, ob die Vorlagen-ID des Gegenstands in einer der acht Aktivierungs-IDs des Objekts steht. `OnIdle` aktualisiert bei offener Reparaturleiste Dauer (Minuten × 60 000) und Startzeit aus den Anhangsdaten des Ziels.

## Meldungen (OnIdle, SetTextEffect)

`OnIdle` (`0x006906E0`) ruft jedes Mal `SetRemainTimeEdit` (`0x0068F9F0`: verbleibende Zeit bis zur nächsten Phase, im Format „%2d : %2d“, bei Global; sonst mit Einheiten `Time_Unit_Minute`/`_Second`) und gibt aus einer Warteschlange (`std::list` ab `+0x2450`) höchstens alle **2000 ms** (`AGCMUISIEGEWAR_PRINT_MESSAGE_TIME`) eine Meldung als Text-Effekt aus (`SetTextEffect`, `0x0068EA20`). Das Binary ruft hier **nicht** `SetInfoEdit` auf (die Meldung geht nur in den Effekt), anders als die Quelle; `SetInfoEdit` ist im Binary nicht erhalten. Meldungen kommen über `_SelfPrintShrineMessageChat` (`0x00690860`, hängt die Meldung an die Liste).

## Schließen beim Entfernen

`CBSelfUpdatePosition` (`0x0068D5A0`) schließt Hauptfenster, Katapult- und Turmfenster, wenn das Flag „geöffnet“ (`+0x19E0`) gesetzt ist und der Charakter 150 oder mehr Einheiten vom Öffnungsort entfernt ist (`> 0x95`).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00690160`, `0x0068EC30`, `0x0068C610`, `0x0068BD90`, `0x0068EE00`, `0x00691520`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (32)

| Name | Id | Handler |
|---|---:|---|
| `SiegeWarGetMainUIDescEdit` |  | `CBGetMainUIDescEdit` |
| `SiegeWarGetMainUIWarTimeEdit` |  | `CBGetMainUISiegeWarTimeEdit` |
| `SiegeWarGetAttackHelpEdit` |  | `CBGetAttackHelpEdit` |
| `SiegeWarGetAttackSiegeWarTimeEdit` |  | `CBGetAttackSiegeWarTimeEdit` |
| `SiegeWarGetDefenseHelpEdit` |  | `CBGetDefenseHelpEdit` |
| `SiegeWarGetDefenseGuildInfoEdit` |  | `CBGetDefenseGuildInfoEdit` |
| `SiegeWarGetDateCombo` |  | `CBGetDateCombo` |
| `SiegeWarGetHourCombo` |  | `CBGetHourCombo` |
| `SiegeWarOpenSiegeWarTimeSetUI` |  | `CBOpenSiegeWarTimeSetUI` |
| `SiegeWarOpenAttackApplicationUI` |  | `CBOpenAttackApplicationUI` |
| `SiegeWarOpenDefenseApplicationUI` |  | `CBOpenDefenseApplicationUI` |
| `SiegeWarConfirmSiegeWarTime` |  | `CBConfirmSiegeWarTime` |
| `SiegeWarSelectDefenseGuild` |  | `CBSelectDefenseGuild` |
| `SiegeWarApplicationDefense` |  | `CBApplicationDefense` |
| `SiegeWarCancelDefense` |  | `CBCancelDefense` |
| `SiegeWarApplicationAttack` |  | `CBApplicationAttack` |
| `SiegeWarAttackPageLeft` |  | `CBAttackPageLeft` |
| `SiegeWarAttackPageRight` |  | `CBAttackPageRight` |
| `SiegeWarAttackGoPage` |  | `CBAttackGoPage` |
| `SiegeWarDefensePageLeft` |  | `CBDefensePageLeft` |
| `SiegeWarDefensekPageRight` |  | `CBDefensePageRight` |
| `SiegeWarDefenseGoPage` |  | `CBDefenseGoPage` |
| `SiegeWarRegisterDefenseGuild` |  | `CBRegisterDefenseGuild` |
| `SiegeWarDefenseGuildListSelect` |  | `CBDefenseGuildListSelect` |
| `SiegeWarGetCatapultDescEdit` |  | `CBGetCatapultDescEdit` |
| `SiegeWarGetAtkResTowerDescEdit` |  | `CBGetAtkResTowerDescEdit` |
| `SiegeWarRepairCatapult` |  | `FUN_0068e770` |
| `SiegeWarRepairAtkResTower` |  | `FUN_0068e770` |
| `SiegeWarActiveCatapult` |  | `FUN_0068e790` |
| `SiegeWarActiveAtkResTower` |  | `FUN_0068e790` |
| `SiegeWarCatapultDragDrop` |  | `FUN_0068e7b0` |
| `SiegeWarAtkResTowerDragDrop` |  | `FUN_0068e7b0` |

**Anzeige** (14)

| Name | Id | Handler |
|---|---:|---|
| `SiegeWarNPCName` | 1 | `CBDisplayNPCName` |
| `SiegeWarAttackGuildName` | 1 | `FUN_0068e200` |
| `SiegeWarAttackGuildMasterName` | 1 | `FUN_0068e240` |
| `SiegeWarAttackGuildPoint` | 1 | `FUN_0068e1b0` |
| `SiegeWarDefenseGuildName` | 1 | `FUN_0068e200` |
| `SiegeWarDefenseGuildMasterName` | 1 | `FUN_0068e240` |
| `SiegeWarDefenseGuildPoint` | 1 | `FUN_0068e1b0` |
| `SiegeWarAttackPageNumber` | 0 | `CBDisplayAttackPageNumber` |
| `SiegeWarDefensePageNumber` | 0 | `CBDisplayDefensePageNumber` |
| `SiegeWarComboDate` | 0 | `FUN_0068e380` |
| `SiegeWarComboHour` | 0 | `FUN_0068e380` |
| `SiegeWarUseCharName` | 0 | `CBDisplayUseCharacterName` |
| `SiegeWarRepairBarMax` | 0 | `CBDisplayRepairBarMax` |
| `SiegeWarRepairBarCurrent` | 0 | `CBDisplayRepairBarCurrent` |

**UserData** (16)

| Name | Id | Handler |
|---|---:|---|
| `SiegeWarInfo` |  | – |
| `SiegeWarDateCombo` |  | – |
| `SiegeWarHourCombo` |  | – |
| `SiegeWarAttackGuildList` |  | – |
| `SiegeWarDefenseGuildList` |  | – |
| `SiegeWarAttackCurrentPage` |  | – |
| `SiegeWarDefenseCurrentPage` |  | – |
| `SiegeWarCatapultGrid` |  | – |
| `SiegeWarAtkResTowerGrid` |  | – |
| `SiegeWarActiveCatapultRepairButton` |  | – |
| `SiegeWarActiveAtkResTowerRepairButton` |  | – |
| `SiegeWarActiveCatapultActiveButton` |  | – |
| `SiegeWarActiveAtkResTowerActiveButton` |  | – |
| `SiegeWarActiveAttackApplButton` |  | – |
| `SiegeWarUseCharName` |  | – |
| `SiegeWarRepairBar` |  | – |

**Ereignis** (64)

| Name | Id | Handler |
|---|---:|---|
| `SiegeWarOpenMainUI` | 0 | – |
| `SiegeWarOpenSetTimeUI` | 0 | – |
| `SiegeWarOpenApplicationDefenseUI` | 0 | – |
| `SiegeWarOpenSelectDefenseGuildUI` | 0 | – |
| `SiegeWarOpenApplicationAttackUI` | 0 | – |
| `SiegeWarCloseUI` | 0 | – |
| `SiegeWarGetMainUIDescEdit` | 0 | – |
| `SiegeWarGetMainUISiegeWarTimeEdit` | 0 | – |
| `SiegeWarGetAttackHelpEdit` | 0 | – |
| `SiegeWarGetAttackSiegeWarTimeEdit` | 0 | – |
| `SiegeWarGetDefenseHelpEdit` | 0 | – |
| `SiegeWarGetDefenseGuidInfoEdit` | 0 | – |
| `SiegeWarGetDateCombo` | 0 | – |
| `SiegeWarGetHourCombo` | 0 | – |
| `SiegeWarRequireCastleMaster` | 0 | – |
| `SiegeWarRequireGuildMaster` | 0 | – |
| `SiegeWarRequireGuildCondition` | 0 | – |
| `SiegeWarAlreadyApplGuild` | 0 | – |
| `SiegeWarCannotSetSiegeWarTime` | 0 | – |
| `SiegeWarCannotApplSiegeWar` | 0 | – |
| `SiegeWarDefenseApplSuccess` | 0 | – |
| `SiegeWarAttackApplSuccess` | 0 | – |
| `SiegeWarDefenseGuildSuccess` | 0 | – |
| `SiegeWarNextSiegeWarTimeSuccess` | 0 | – |
| `SiegeWarNotEnoughMoney` | 0 | – |
| `SiegeWarNoMoreRepair` | 0 | – |
| `SiegeWarSelectAttackPage1` | 0 | – |
| `SiegeWarSelectAttackPage2` | 0 | – |
| `SiegeWarSelectAttackPage3` | 0 | – |
| `SiegeWarSelectAttackPage4` | 0 | – |
| `SiegeWarSelectAttackPage5` | 0 | – |
| `SiegeWarSelectAttackPage6` | 0 | – |
| `SiegeWarSelectAttackPage7` | 0 | – |
| `SiegeWarSelectAttackPage8` | 0 | – |
| `SiegeWarSelectAttackPage9` | 0 | – |
| `SiegeWarSelectDefensePage1` | 0 | – |
| `SiegeWarSelectDefensePage2` | 0 | – |
| `SiegeWarSelectDefensePage3` | 0 | – |
| `SiegeWarSelectDefensePage4` | 0 | – |
| `SiegeWarSelectDefensePage5` | 0 | – |
| `SiegeWarSelectDefensePage6` | 0 | – |
| `SiegeWarSelectDefensePage7` | 0 | – |
| `SiegeWarSelectDefensePage8` | 0 | – |
| `SiegeWarSelectDefensePage9` | 0 | – |
| `SiegeWarGetCatapultEdit` | 0 | – |
| `SiegeWarGetAtkResTowerEdit` | 0 | – |
| `SiegeWarOpenCatapultUI` | 0 | – |
| `SiegeWarOpenAtkResTowerUI` | 0 | – |
| `SiegeWarCloseCatapultUI` | 0 | – |
| `SiegeWarCloseAtkResTowerUI` | 0 | – |
| `SiegeWarSelectedDefenseGuild` | 0 | – |
| `SiegeWarDisableDefenseGuild` | 0 | – |
| `SiegeWarNormalDefenseGuild` | 0 | – |
| `SiegeWarOpenCarveMessageUI` | 0 | – |
| `SiegeWarCloseCarveMessageUI` | 0 | – |
| `SiegeWarGetInfoEditControl` | 0 | – |
| `SiegeWarGetRemainTimeEditControl` | 0 | – |
| `SiegeWarUseCharNameMessage` | 0 | – |
| `SiegeWarRepairCharNameMessage` | 0 | – |
| `SiegeWarOpenRepairBarUI` | 0 | – |
| `SiegeWarCloseRepairBarUI` | 0 | – |
| `SiegeWarConfirmApplGuildMessage` | 0 | – |
| `SiegeWar_Start` | 0 | – |
| `SiegeWar_Close` | 0 | – |

**Boolean** (5)

| Name | Id | Handler |
|---|---:|---|
| `SiegeWarActiveCatapultRepairButton` |  | `CBIsActiveCatapultRepairButton` |
| `SiegeWarActiveCatapultActiveButton` |  | `CBIsActiveCatapultActiveButton` |
| `SiegeWarActiveAtkResTowerRepairButton` |  | `CBIsActiveAtkResTowerRepairButton` |
| `SiegeWarActiveAtkResTowerActiveButton` |  | `CBIsActiveAtkResTowerActiveButton` |
| `SiegeWarActiveAttackApplButton` |  | `CBIsActiveAttackApplButton` |


## Abweichungen von der EP8-Quelle

- Ein Unterschied: `OnIdle` ruft `SetInfoEdit(Meldung)` in der Quelle auf; im Binary geht die Meldung nur an `SetTextEffect`, weil `SetInfoEdit` kein Binary-Gegenstück hat (die zugehörigen Textfelder sind in der Quelle auskommentiert). Sonst keine Abweichung in den gelesenen Funktionen.

## Grenzen

- `CBStatusInfo` (2131 Byte), `CBSyncMessage` (1012 Byte), `CBReceiveResult` (738 Byte), `AddEvent` (2166 Byte) und `AddUserData` wurden über Größe, Registrierung und Aufrufer zugeordnet, nicht Zeile für Zeile verglichen.
- Bei den gemeinsamen Rümpfen (Anzeigen- und Katapult/Turm-Paare) wurde nur geprüft, dass der Rumpf mit beiden Registrierungen identisch ist.
- `SetUseCharName` und `UpdateSiegeWarInfoUI` wurden nicht in einem Aufrufer nachgewiesen; die Angabe „eingebaut“ ist eine Vermutung aus der Größe.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, gemeinsamer Rumpf: 3, nicht im Client: 14, ohne Kandidat: 12.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventSiegeWarNPC`](AgcmEventSiegeWarNPC.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIItem`](AgcmUIItem.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmAdmin`](AgpmAdmin.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmEventSiegeWarNPC`](AgpmEventSiegeWarNPC.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmGuild`](AgpmGuild.md), [`AgpmItem`](AgpmItem.md), [`AgpmSiegeWar`](AgpmSiegeWar.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmSiegeWar`](AgcmSiegeWar.md)
