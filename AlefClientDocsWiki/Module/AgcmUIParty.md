# AgcmUIParty (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIParty` (Gruppen-Oberfläche: Mitglieder, Einladungen, Buffs, Rückruf) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIParty/AgcmUIParty.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 86 von 88 Quellmethoden sind einer Adresse zugeordnet (`CBChangeLeader`, `CBUseSkillForMember` und `CBUpdateExpType` als gemeinsame Rümpfe; `CBIsActiveDelegationLeader` teilt sich den Rumpf mit `CBIsActivePartyBanish`); die zwei `Refresh…Info` sind eingebaut. Neu sind 29 Funktionen, u. a. `SetMemberInfo`, `ThrowInitEvent`, `SetBuffedGrid`, `ThrowBonusEvent`, `CloseUserMenu`, `CheckMemberTransparent`, die acht Anzeigen und die UI-Funktionen.
- **Sperrzeit:** Die 10-s-Sperre gegen Mehrfach-Einladungen wird nur bei `g_eServiceArea == 1` (China) gestartet; im Binary ist der Startwert 4.
- **UI:** 13 Funktionen, 12 Anzeigen, 5 Bool-Anzeigen, 5 Benutzerdaten und 73 Ereignisse (laut Registrierungstabelle im Binary).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIParty.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006C4610` | 1334 | vtable/String |
| 1 | `OnInit` | `0x006C0A00` | 49 | vtable/String |
| 2 | `OnDestroy` | `0x006C0A40` | 43 | vtable/String |
| 3 | `AddUserData` | `0x006C0A70` | 206 | Zeichenkette |
| 4 | `AddFunction` | `0x006C3AA0` | 543 | Zeichenkette |
| 5 | `AddDisplay` | `0x006C3CC0` | 395 | Zeichenkette |
| 6 | `AddEvent` | `0x006C1FD0` | 2438 | Zeichenkette |
| 7 | `AddBoolean` | `0x006C3E50` | 151 | Zeichenkette |
| 8 | `CBReceiveInvite` | `0x006C0B40` | 222 | Callback-Registrierung |
| 9 | `CBReceiveReject` | `0x006C0C20` | 107 | Callback-Registrierung |
| 10 | `CBReceiveInviteAccept` | `0x006C0C90` | 107 | Callback-Registrierung |
| 11 | `CBReceiveLeave` | `0x006C0D00` | 97 | Callback-Registrierung |
| 12 | `CBReceiveBanish` | `0x006C0D70` | 97 | Callback-Registrierung |
| 13 | `CBReceiveInviteFailedAlreadyOtherMember` | `0x006C0DE0` | 107 | Callback-Registrierung |
| 14 | `CBReceiveInviteFailedAlreadyPartyMember` | `0x006C0E50` | 107 | Callback-Registrierung |
| 15 | `CBReceiveInviteFailedMemberIsFull` | `0x006C0EC0` | 107 | Callback-Registrierung |
| 16 | `CBReceiveInviteFailedNotLeader` | `0x006C0F30` | 107 | Callback-Registrierung |
| 17 | `CBReceiveInviteFailedMurdererSelf` | `0x006C2960` | 106 | Callback-Registrierung |
| 18 | `CBReceiveInviteFailedMurdererTarget` | `0x006C29D0` | 203 | Callback-Registrierung |
| 19 | `CBReceiveLeaveByMurderer` | `0x006C2AA0` | 96 | Callback-Registrierung |
| 20 | `CBReceiveOperationFailed` | `0x006C0FA0` | 117 | Callback-Registrierung |
| 21 | `CBRequestRecall` | `0x006C1020` | 101 | Callback-Registrierung |
| 22 | `CBAcceptRecall` | `0x006C1090` | 92 | von Hand geprüft |
| 23 | `CBRejectRecall` | `0x006C10F0` | 92 | von Hand geprüft |
| 24 | `CBAddParty` | `0x006C43A0` | 212 | Callback-Registrierung |
| 25 | `CBRemoveParty` | `0x006C1150` | 86 | Callback-Registrierung |
| 26 | `CBAddMember` | `0x006C4480` | 77 | Callback-Registrierung |
| 27 | `CBRemoveMember` | `0x006C44D0` | 172 | Callback-Registrierung |
| 28 | `CBChangeLeader` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 29 | `CBResetEffectArea` | `0x006C3EF0` | 488 | Callback-Registrierung |
| 30 | `CBUpdateExpType` | `0x00561430` | 23 | gleiche Adresse wie `gemeinsamer Rumpf (return pData && pClass)` (vom Linker zusammengefaltet) |
| 31 | `CBUpdateBonusStats` | `0x006C40E0` | 195 | Callback-Registrierung |
| 32 | `CBUpdateFactorParty` | `0x006C4580` | 135 | Callback-Registrierung |
| 33 | `CBSetSelfCharacter` | `0x006C11B0` | 66 | Callback-Registrierung |
| 34 | `CBDisplayMemberName` | `0x006C1200` | 81 | manual |
| 35 | `CBDisplayMemberHP` | `0x006C1260` | 44 | manual |
| 36 | `CBDisplayMemberMaxHP` | `0x006C1290` | 44 | manual |
| 37 | `CBDisplayMemberLevel` | `0x006C12C0` | 58 | manual |
| 38 | `CBDisplayBonusDamage` | `0x006C1300` | 47 | manual |
| 39 | `CBDisplayBonusDefense` | `0x006C1330` | 47 | manual |
| 40 | `CBDisplayBonusMaxHP` | `0x006C1360` | 47 | manual |
| 41 | `CBDisplayBonusMaxMP` | `0x006C1390` | 47 | manual |
| 42 | `CBDisplayLeaderName` | `0x006C2B00` | 76 | manual |
| 43 | `CBDisplayRecallTargetName` | `0x006C13C0` | 47 | UI-Registrierung |
| 44 | `CBDisplayRequestRecall` | `0x006C13F0` | 62 | UI-Registrierung |
| 45 | `CBDisplayInviter` | `0x006C1430` | 47 | UI-Registrierung |
| 46 | `CBInviteMember` | `0x006C1460` | 161 | manual |
| 47 | `CBBanishMember` | `0x006C2B50` | 114 | manual |
| 48 | `CBLeaveParty` | `0x006C1510` | 34 | manual |
| 49 | `CBInviteReject` | `0x006C1540` | 45 | manual |
| 50 | `CBInviteAccept` | `0x006C1570` | 45 | manual |
| 51 | `CBUseSkillForMember` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 52 | `CBSelfSelect` | `0x006C2BD0` | 112 | UI-Registrierung |
| 53 | `CBMemberSelect` | `0x006C2C40` | 238 | UI-Registrierung |
| 54 | `CBMoveCharacterMenu` | `0x006C15A0` | 126 | UI-Registrierung |
| 55 | `SetMemberInfo` | `0x006C41B0` | 487 | manual |
| 56 | `ThrowInitEvent` | `0x006C2D30` | 681 | manual |
| 57 | `SetBuffedGrid` | `0x006C2FE0` | 381 | manual |
| 58 | `RefreshUserDataMemberInfo` | – | | acht Zeilen, in SetMemberInfo eingebaut |
| 59 | `RefreshUserDataSelfInfo` | – | | acht Zeilen, in SetMemberInfo eingebaut |
| 60 | `RefreshUserDataBuffGrid` | `0x006C1620` | 71 | manual |
| 61 | `ThrowBonusEvent` | `0x006C3160` | 363 | manual |
| 62 | `CBEventReturnRecvInvite` | `0x006C1670` | 58 | manual |
| 63 | `CBEventReturnBanishMember` | `0x006C16B0` | 62 | manual |
| 64 | `CBEventReturnLeaveParty` | `0x006C16F0` | 54 | manual |
| 65 | `CBIsActivePartyMemu` | `0x006C32D0` | 177 | UI-Registrierung |
| 66 | `CBIsActivePartyBanish` | `0x006C3860` | 130 | manual |
| 67 | `CBIsActivePartyLeave` | `0x006C1730` | 38 | UI-Registrierung |
| 68 | `CBAddBuffedSkill` | `0x006C3390` | 301 | Callback-Registrierung |
| 69 | `CBRemoveBuffedSkill` | `0x006C34D0` | 243 | Callback-Registrierung |
| 70 | `CBUseItem` | `0x006C1760` | 113 | Callback-Registrierung |
| 71 | `CBUpdateActionStatus` | `0x006C35D0` | 656 | Callback-Registrierung |
| 72 | `CBDelegationLeader` | `0x006C17E0` | 72 | manual |
| 73 | `CBAcceptRecall` | `0x006C1830` | 84 | von Hand geprüft |
| 74 | `CBRejectRecall` | `0x006C1890` | 57 | von Hand geprüft |
| 75 | `CBGetRecallRequestEdit` | `0x006C18D0` | 139 | UI-Registrierung |
| 76 | `CBReceiveDelegationLeader` | `0x006C1960` | 147 | Callback-Registrierung |
| 77 | `CBReceiveDelegationLeaderFailed` | `0x006C1A00` | 60 | Callback-Registrierung |
| 78 | `CBIsActivePartyOptionUI` | `0x006C1A40` | 53 | UI-Registrierung |
| 79 | `CBIsActiveDelegationLeader` | `0x006C3860` | 130 | gleiche Adresse wie `mit CBIsActivePartyBanish zusammengefaltet (ICF)` (vom Linker zusammengefaltet) |
| 80 | `CBReceiveInvietFailedLevelDiff` | `0x006C1A80` | 60 | Callback-Registrierung |
| 81 | `CBReceiveOperationFailedRefuse` | `0x006C38F0` | 189 | Callback-Registrierung |
| 82 | `SetVisibleBuffIcon` | `0x006C39B0` | 61 | manual |
| 83 | `CBSelectTarget` | `0x006C39F0` | 24 | Callback-Registrierung |
| 84 | `CloseUserMenu` | `0x006C1AC0` | 71 | manual |
| 85 | `CheckMemberTransparent` | `0x006C3A10` | 134 | manual |
| 86 | `_GetUpdateClassIconEventSelf` | `0x006C1B10` | 303 | manual |
| 87 | `_GetUpdateClassIconEventMember` | `0x006C1C60` | 303 | manual |

86 von 88 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `CBAcceptRecall_006c1090` (`0x006C1090`), `CBRejectRecall_006c10f0` (`0x006C10F0`), `CBAcceptRecall_006c1830` (`0x006C1830`), `CBRejectRecall_006c1890` (`0x006C1890`), `ctor_or_dtor` (`0x006C1DB0`), `~AgcmUIParty` (`0x006C1FA0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBA4` | `Zeiger auf `AgcmCharacter`` | u. a. `CBInviteMember`, `SetMemberInfo` |
| `0xBCC…` | `Mitgliederliste (4 × 0x4C Byte), eigener Eintrag bei `+0xCFC`` | `SetMemberInfo` |
| `0xD48…` | `vier Buff-Gitter (je 0x24 Byte)` | `SetBuffedGrid`, `RefreshUserDataBuffGrid` |
| `0xDD8` | `aktuelle Gruppe (`m_pcsParty`)` | `SetMemberInfo`, `ThrowBonusEvent` |
| `0xDDC / 0xDE0 / 0xDE4` | `Einladender / Eingeladener / Ausgeschlossener (IDs)` | `CBReceiveInvite`, `CBEventReturn…` |
| `0xDEC…0xDF8` | `Bonus Schaden / Verteidigung / Max-HP / Max-MP` | `ThrowBonusEvent` |
| `0xED0 / 0xED4` | `gewähltes Mitglied / Flag „Buff-Symbole an“` | `CloseUserMenu`, `SetVisibleBuffIcon` |
| `0xF10` | `Name des Einladenden` | `CBReceiveInvite` |
| `0xF48 / 0xF4C` | `Zeit der letzten empfangenen / gesendeten Einladung` | `CBReceiveInvite`, `CBInviteMember` |

## Vtable

Vtable bei `0x008D4594`: Slot 0 Destruktor `0x006C1FA0`, 1 `OnAddModule` (`0x006C4610`), 2 `OnInit` (`0x006C0A00`), 3–5 gemeinsamer Rumpf `0x0067FAB0`, 6 `return TRUE`-Rumpf `0x0067AC90`, 7 `OnDestroy` (`0x006C0A40`).

## Registrierung (OnAddModule, 0x006C4610)

Holt 13 Module ([`ApmMap`](ApmMap.md) wird zweimal geholt; [`AgpmFactors`](AgpmFactors.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgpmParty`](AgpmParty.md), [`AgcmParty`](AgcmParty.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgpmSkill`](AgpmSkill.md), [`AgcmSkill`](AgcmSkill.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgcmPrivateTrade`](AgcmPrivateTrade.md)) und meldet dann 35 Callbacks in der Reihenfolge der Quelle an:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmFactors`: Gruppen-Faktoren | `CBUpdateFactorParty` | `0x006C4580` |
| `AgpmCharacter`: Aktionsstatus | `CBUpdateActionStatus` | `0x006C35D0` |
| `AgpmParty`: Gruppe angelegt | `CBAddParty` | `0x006C43A0` |
| `AgpmParty`: Gruppe aufgelöst | `CBRemoveParty` | `0x006C1150` |
| `AgpmParty`: Mitglied hinzugefügt | `CBAddMember` | `0x006C4480` |
| `AgpmParty`: Mitglied entfernt | `CBRemoveMember` | `0x006C44D0` |
| `AgpmParty`: Anführer gewechselt | `CBChangeLeader` | `0x0067AC90` (gemeinsamer Rumpf) |
| `AgpmParty`: Effektbereich neu | `CBResetEffectArea` | `0x006C3EF0` |
| `AgpmParty`: Erfahrungsart | `CBUpdateExpType` | `0x00561430` (gemeinsamer Rumpf) |
| `AgpmParty`: Bonuswerte | `CBUpdateBonusStats` | `0x006C40E0` |
| `AgcmParty`: Einladung empfangen | `CBReceiveInvite` | `0x006C0B40` |
| `AgcmParty`: abgelehnt | `CBReceiveReject` | `0x006C0C20` |
| `AgcmParty`: Einladung angenommen | `CBReceiveInviteAccept` | `0x006C0C90` |
| `AgcmParty`: Austritt | `CBReceiveLeave` | `0x006C0D00` |
| `AgcmParty`: Ausschluss | `CBReceiveBanish` | `0x006C0D70` |
| `AgcmParty`: Ziel in anderer Gruppe | `CBReceiveInviteFailedAlreadyOtherMember` | `0x006C0DE0` |
| `AgcmParty`: Ziel schon Mitglied | `CBReceiveInviteFailedAlreadyPartyMember` | `0x006C0E50` |
| `AgcmParty`: Gruppe voll | `CBReceiveInviteFailedMemberIsFull` | `0x006C0EC0` |
| `AgcmParty`: nicht Anführer | `CBReceiveInviteFailedNotLeader` | `0x006C0F30` |
| `AgcmParty`: Vorgang fehlgeschlagen | `CBReceiveOperationFailed` | `0x006C0FA0` |
| `AgcmParty`: Rückruf angefragt | `CBRequestRecall` | `0x006C1020` |
| `AgcmParty`: Rückruf angenommen | `CBAcceptRecall` | `0x006C1090` |
| `AgcmParty`: Rückruf abgelehnt | `CBRejectRecall` | `0x006C10F0` |
| `AgcmParty`: Anführer übertragen | `CBReceiveDelegationLeader` | `0x006C1960` |
| `AgcmParty`: Übertragung fehlgeschlagen | `CBReceiveDelegationLeaderFailed` | `0x006C1A00` |
| `AgcmParty`: Stufenunterschied | `CBReceiveInvietFailedLevelDiff` | `0x006C1A80` |
| `AgcmParty`: Einladung abgelehnt (Verweigerung) | `CBReceiveOperationFailedRefuse` | `0x006C38F0` |
| `AgcmCharacter`: eigener Charakter gesetzt | `CBSetSelfCharacter` | `0x006C11B0` |
| `AgcmCharacter`: Ziel gewählt | `CBSelectTarget` | `0x006C39F0` |
| `AgpmSkill`: Buff hinzugefügt | `CBAddBuffedSkill` | `0x006C3390` |
| `AgpmSkill`: Buff entfernt | `CBRemoveBuffedSkill` | `0x006C34D0` |
| `AgpmItem`: Gegenstand per TID benutzt | `CBUseItem` | `0x006C1760` |
| `AgcmParty`: Einladung scheitert (Mörder, selbst) | `CBReceiveInviteFailedMurdererSelf` | `0x006C2960` |
| `AgcmParty`: Einladung scheitert (Mörder, Ziel) | `CBReceiveInviteFailedMurdererTarget` | `0x006C29D0` |
| `AgcmParty`: Austritt wegen Mörder | `CBReceiveLeaveByMurderer` | `0x006C2AA0` |

Danach `AddEvent` (`0x006C1FD0`, 2438 Byte), `AddFunction` (`0x006C3AA0`), `AddDisplay` (`0x006C3CC0`), `AddUserData` (`0x006C0A70`) und `AddBoolean` (`0x006C3E50`).

## Einladung

`CBInviteMember` (`0x006C1460`, UI-Funktion `PartyInviteMember`) braucht ein Zielsteuerelement mit Zielcharakter und den eigenen Charakter und sendet `AgcmParty::SendPacketInvite`. `CBReceiveInvite` (`0x006C0B40`) wirkt nur, wenn der eigene Charakter Einladender oder Eingeladener ist, übernimmt beide IDs und den Namen, aktualisiert das Benutzerdatum `Inviter` und wirft `RecvInvite`. `CBInviteAccept` (`0x006C1570`) und `CBInviteReject` (`0x006C1540`) lösen `SendPacketAccept` (`0x006E8960`) bzw. `SendPacketReject` (`0x006E88C0`) aus und setzen die Sperrzeit zurück. Die Bestätigungsfenster rufen `CBEventReturnRecvInvite` (`0x006C1670`: 1 → annehmen, sonst ablehnen), `CBEventReturnBanishMember` (`0x006C16B0`, `SendPacketBanish`) und `CBEventReturnLeaveParty` (`0x006C16F0`, `SendPacketLeave`).
**Sperrzeit gegen Mehrfach-Einladungen:** Sowohl beim Senden als auch beim Empfangen werden Einladungen innerhalb von **10 000 ms** nach der vorigen abgewiesen – aber die Uhr wird nur gesetzt, wenn die Variable `g_eServiceArea` den Wert 1 (`AP_SERVICE_AREA_CHINA`) hat. Sie ist im Binary statisch mit 4 (Global) vorbelegt; bei diesem Wert wird die Sperrzeit also nie gestartet.

## Mitgliederliste (SetMemberInfo, 0x006C41B0)

`SetMemberInfo` merkt die Gruppe (`+0xDD8`), löscht die Mitgliedsliste (`0x130` Byte = vier Einträge zu je `0x4C` Byte ab `+0xBCC`) und füllt sie für jedes Mitglied aus Name, HP/Max-HP (Ergebnis-Faktoren), Stufe, Klasse, Effektbereich-Flag und Charakter-ID. Der eigene Charakter kommt in den eigenen Eintrag (`+0xCFC`), die anderen nacheinander in die Liste. Danach werden die Benutzerdaten aktualisiert (`RefreshUserDataMemberInfo`/`…SelfInfo` sind eingebaut), `SetBuffedGrid` (`0x006C2FE0`) und `ThrowInitEvent` (`0x006C2D30`) aufgerufen.
`SetBuffedGrid` leert vier Buff-Gitter (je `0x24` Byte ab `+0xD48`), geht über die Mitglieder außer dem eigenen und trägt deren sichtbare Buff-Fertigkeiten (bis `0x60` Einträge) ein; `RefreshUserDataBuffGrid` (`0x006C1620`) setzt das Benutzerdatum. `ThrowInitEvent` wirft je Mitglied die Ereignisse für die Klassen-Symbole (`_GetUpdateClassIconEventSelf` `0x006C1B10`, `…Member` `0x006C1C60`: Auswahl nach Rasse und Klasse aus 3 × 3-Tabellen ab `+0xF50` bzw. `+0xF84`) und schließt vorher das Benutzermenü (`CloseUserMenu`, `0x006C1AC0`: je vier Ereignisse, je nach Flag „Buff-Symbole“ `+0xED4`).
`CheckMemberTransparent` (`0x006C3A10`) macht unsichtbare Mitglieder sofort durchsichtig (`UpdateTransparent(…, TRUE, 2000)`); `SetVisibleBuffIcon` (`0x006C39B0`) schaltet die Buff-Symbole um.

## Bonus und Anführer

`ThrowBonusEvent` (`0x006C3160`) zeigt, wenn der eigene Charakter in der Gruppe ist, Systemmeldungen für Schaden-, Verteidigungs- und HP/MP-Bonus (Texte `Party_Add_Damage`, `Party_Add_Defense`, `Party_Add_HPMP`; Farbe aus `Party_Text_Color`, Standard `0xFF7BFFCD`). `CBIsActivePartyBanish` und `CBIsActiveDelegationLeader` sind im Binary dieselbe Funktion (`0x006C3860`): Ziel muss ein Spieler, nicht man selbst und in der eigenen Gruppe sein, und man selbst muss Anführer sein (Platz 0 der Mitgliederliste). `CBIsActivePartyLeave` (`0x006C1730`) prüft nur die Gruppenzugehörigkeit.

## Rückruf

Zwei Paare `CBAcceptRecall`/`CBRejectRecall` gibt es in der Quelle: die Modul-Callbacks von `AgcmParty` (`0x006C1090`, `0x006C10F0`) und die UI-Funktionen `PartyAcceptRecall`/`PartyRejectRecall` (`0x006C1830`, `0x006C1890`). Sie sind über ihre Größe und die Anmelder getrennt.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006C3AA0`, `0x006C3CC0`, `0x006C0A70`, `0x006C1FD0`, `0x006C3E50`, `0x006C4610`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (13)

| Name | Id | Handler |
|---|---:|---|
| `PartyInviteMember` |  | `FUN_006c1460` |
| `PartyBanishMember` |  | `FUN_006c2b50` |
| `PartyLeaveParty` |  | `FUN_006c1510` |
| `PartyInviteReject` |  | `FUN_006c1540` |
| `PartyInviteAccept` |  | `FUN_006c1570` |
| `PartyUseSkillForMember` |  | `Element::GetSize` |
| `PartySelfSelect` |  | `CBSelfSelect` |
| `PartyMemberSelect` |  | `CBMemberSelect` |
| `MoveCharacterMenu` |  | `CBMoveCharacterMenu` |
| `PartyDelegationLeader` |  | `FUN_006c17e0` |
| `PartyAcceptRecall` |  | `CBAcceptRecall` |
| `PartyRejectRecall` |  | `CBRejectRecall` |
| `PartyGetRecallRequestEdit` |  | `CBGetRecallRequestEdit` |

**Anzeige** (12)

| Name | Id | Handler |
|---|---:|---|
| `PartyMemberName` | 0 | `FUN_006c1200` |
| `PartyMemberHP` | 1 | `FUN_006c1260` |
| `PartyMemberMaxHP` | 2 | `FUN_006c1290` |
| `PartyMemberLevel` | 3 | `FUN_006c12c0` |
| `PartyBonusDamage` | 4 | `FUN_006c1300` |
| `PartyBonusDefense` | 5 | `FUN_006c1330` |
| `PartyBonusMaxHP` | 6 | `FUN_006c1360` |
| `PartyBonusMaxMP` | 7 | `FUN_006c1390` |
| `PartyLeaderName` | 8 | `FUN_006c2b00` |
| `PartyRecallTargetName` | 9 | `CBDisplayRecallTargetName` |
| `PartyRequestRecall` | 10 | `CBDisplayRequestRecall` |
| `PartyInviter` | 1 | `CBDisplayInviter` |

**UserData** (5)

| Name | Id | Handler |
|---|---:|---|
| `PartySelfInfo` |  | – |
| `PartyMemberInfo` |  | – |
| `PartyMemberBuffGrid` |  | – |
| `PartyRecallTargetName` |  | – |
| `PartyInviterName` |  | – |

**Ereignis** (73)

| Name | Id | Handler |
|---|---:|---|
| `PartyOpenUI` | 0 | – |
| `PartyCloseUI` | 0 | – |
| `PartyRecvInvite` |  | `FUN_006c1670` |
| `PartyRecvReject` | 0 | – |
| `PartyRecvInviteAccept` | 0 | – |
| `PartyRecvLeave` | 0 | – |
| `PartyRecvBanish` | 0 | – |
| `PartyRecvAlreadyOtherMember` | 0 | – |
| `PartyRecvAlreadyPartyMember` | 0 | – |
| `PartyRecvMemberFull` | 0 | – |
| `PartyRecvNotLeader` | 0 | – |
| `PartyRecvOperationFailed` | 0 | – |
| `PartyConformBanishMember` |  | `FUN_006c16b0` |
| `PartyConformLeaveParty` |  | `FUN_006c16f0` |
| `PartySelfActiveEffectAreaKnight` | 0 | – |
| `PartySelfActiveEffectAreaRanger` | 0 | – |
| `PartySelfActiveEffectAreaMage` | 0 | – |
| `PartySelfDisableEffectArea` | 0 | – |
| `PartySelfSetDead` | 0 | – |
| `PartySelfSetLeader` | 0 | – |
| `PartySelfSetMember` | 0 | – |
| `PartyActiveEffectAreaKnight` | 0 | – |
| `PartyActiveEffectAreaRanger` | 0 | – |
| `PartyActiveEffectAreaMage` | 0 | – |
| `PartyDisableEffectArea` | 0 | – |
| `PartySetDead` | 0 | – |
| `PartySetLeader` | 0 | – |
| `PartySetMember` | 0 | – |
| `PartyBonusDamage` | 0 | – |
| `PartyBonusDefense` | 0 | – |
| `PartyBonusMaxPoint` | 0 | – |
| `PartyChangeLeader` | 0 | – |
| `PartySelfUserMenuOn` | 0 | – |
| `PartySelfUserMenuOff` | 0 | – |
| `PartyMemberUserMenuOn` | 0 | – |
| `PartyMemberUserMenuOff` | 0 | – |
| `PartyOpenRequestRecallUI` | 0 | – |
| `Party_DelegationLeader` | 0 | – |
| `Party_DelegationLeaderFailed` | 0 | – |
| `Party_InviteMemeberLevelDiff` | 0 | – |
| `PartyMemberUserMenuOnBuffOff` | 0 | – |
| `PartyMemberUserMenuOffBuffOff` | 0 | – |
| `PartyAcceptRecall` | 0 | – |
| `PartyRejectRecall` | 0 | – |
| `PartyTargetAcceptRecall` | 0 | – |
| `PartyTargetRejectRecall` | 0 | – |
| `PartyUseRecallSuccess` | 0 | – |
| `PartyChageSelfClassHK` | 0 | – |
| `PartyChageSelfClassHA` | 0 | – |
| `PartyChageSelfClassHW` | 0 | – |
| `PartyChageSelfClassOK` | 0 | – |
| `PartyChageSelfClassOA` | 0 | – |
| `PartyChageSelfClassOW` | 0 | – |
| `PartyChageSelfClassMK` | 0 | – |
| `PartyChageSelfClassMA` | 0 | – |
| `PartyChageSelfClassMW` | 0 | – |
| `PartyChageSelfClassDS` | 0 | – |
| `PartyChageSelfClassDK` | 0 | – |
| `PartyChageSelfClassDA` | 0 | – |
| `PartyChageSelfClassDW` | 0 | – |
| `PartyChageMemberClassHK` | 0 | – |
| `PartyChageMemberClassHA` | 0 | – |
| `PartyChageMemberClassHW` | 0 | – |
| `PartyChageMemberClassOK` | 0 | – |
| `PartyChageMemberClassOA` | 0 | – |
| `PartyChageMemberClassOW` | 0 | – |
| `PartyChageMemberClassMK` | 0 | – |
| `PartyChageMemberClassMA` | 0 | – |
| `PartyChageMemberClassMW` | 0 | – |
| `PartyChageMemberClassDS` | 0 | – |
| `PartyChageMemberClassDK` | 0 | – |
| `PartyChageMemberClassDA` | 0 | – |
| `PartyChageMemberClassDW` | 0 | – |

**Boolean** (5)

| Name | Id | Handler |
|---|---:|---|
| `IsActivePartyMemu` |  | `CBIsActivePartyMemu` |
| `IsActivePartyBanish` |  | `FUN_006c3860` |
| `IsActivePartyLeave` |  | `CBIsActivePartyLeave` |
| `IsActivePartyOptionUI` |  | `CBIsActivePartyOptionUI` |
| `IsActivePartyDelegationLeader` |  | `FUN_006c3860` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierungsreihenfolge, Einladung mit 10-s-Sperre, `SetMemberInfo`, `SetBuffedGrid`, `ThrowBonusEvent`, `CloseUserMenu`, `CheckMemberTransparent`, `CBIsActive…`).

## Grenzen

- `ThrowInitEvent`, `AddEvent` (2438 Byte), `CBResetEffectArea`, `CBUpdateActionStatus` und `CBMoveCharacterMenu` wurden über Größe, Aufrufe und Aufrufer zugeordnet, nicht Zeile für Zeile verglichen.
- Die Gruppenobergrenze (Schleifen über vier plus den eigenen Charakter) stammt aus den Feldgrößen im Binary, nicht aus dem Wert der Konstante in `AgpmParty`.
- Die Anzeigefunktionen wurden über die Registrierungsreihenfolge zugeordnet.
- Der Wert von `g_eServiceArea` im Betrieb wurde nicht gemessen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, ohne Kandidat: 7.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmParty`](AgcmParty.md), [`AgcmPrivateTrade`](AgcmPrivateTrade.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmItem`](AgpmItem.md), [`AgpmParty`](AgpmParty.md), [`AgpmSkill`](AgpmSkill.md), [`ApmMap`](ApmMap.md)
- **Erwähnt in:** [`AgcmParty`](AgcmParty.md), [`AgpmParty`](AgpmParty.md)
