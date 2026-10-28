# AgcmUIGuild (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIGuild` (Gilden-Fenster: Gründung, Mitglieder, Liste, Gildenzeichen, Beziehungen, Gildenkampf) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIGuild` (14 Quelldateien). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Tabelle; Grundlage sind die Callback-Registrierungsreihenfolge (44 Handler), der Aufrufgraph und Zeichenketten. Rund 20 Zuordnungen wurden gegen Dekompilat und Quelle gelesen; keine war falsch, die übrigen sind über die Methode abgesichert.
- **Registrierung:** 47 statt 48 Callbacks erkennbar; Stub-Handler für `CBJoinReject` und zwei Kampf-Rejects.
- **Konstanten:** 19 Einträge je Listenseite, 10 Seiten in der Seitenleiste; Ränge 1/10/11 wie in der Quelle.
- **Abweichungen:** keine festgestellt; die Stub-Handler (Reject-Callbacks) sind eine Eigenheit der Registrierung, keine bestätigte Verhaltensänderung.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIGuild.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006BB9A0` | 1712 | vtable/String |
| 1 | `OnInit` | `0x006B7F80` | 46 | vtable/String |
| 2 | `OnIdle` | `0x006B6930` | 33 | vtable/String |
| 3 | `OnDestroy` | `0x006B6960` | 11 | vtable/String |
| 4 | `AddEvent` | `0x006B7FB0` | 2116 | Zeichenkette |
| 5 | `AddFunction` | `0x006B8800` | 2847 | Zeichenkette |
| 6 | `AddDisplay` | `0x006B9320` | 1143 | Zeichenkette |
| 7 | `AddUserData` | `0x006B6970` | 2653 | Zeichenkette |
| 8 | `AddBoolean` | `0x006B97A0` | 95 | Zeichenkette |
| 9 | `CBDisplayGuildText` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 10 | `CBDisplayInviteGuild` | `0x006B73D0` | 55 | UI-Registrierung |
| 11 | `CBIsActiveGuildInviteMemu` | `0x006B7410` | 133 | UI-Registrierung |
| 12 | `CBCreateComplete` | `0x006B74A0` | 187 | cbreg:AgcmUIGuild |
| 13 | `CBJoinRequest` | `0x006B7560` | 145 | cbreg:AgcmUIGuild |
| 14 | `CBJoinReject` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 15 | `CBJoin` | `0x006B7600` | 140 | cbreg:AgcmUIGuild |
| 16 | `CBLeave` | `0x006B7690` | 236 | cbreg:AgcmUIGuild |
| 17 | `CBForcedLeave` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 18 | `CBDestroy` | `0x006B9800` | 246 | cbreg:AgcmUIGuild |
| 19 | `CBCharData` | `0x006B9900` | 272 | cbreg:AgcmUIGuild |
| 20 | `CBUpdateMemberStatus` | `0x006BB500` | 682 | Aufrufgraph (geprüft) |
| 21 | `CBUpdateNotice` | `0x006B7780` | 527 | Zeichenketten/Konstanten (geprüft) |
| 22 | `CBSystemMessage` | `0x006B9A10` | 2304 | Aufrufgraph (geprüft) |
| 23 | `CBEventGrant` | `0x006B7990` | 100 | cbreg:AgcmUIGuild |
| 24 | `CBEventGrantWorldChampionship` | `0x006B7A00` | 55 | Callback-Registrierung |
| 25 | `CBSelfUpdatePosition` | `0x006B7A40` | 246 | cbreg:AgcmUIGuild |
| 26 | `CBSendJoinRequest` | `0x006B7B40` | 52 | UI-Registrierung |
| 27 | `CBEventReturnInviteConfirm` | `0x006B7B80` | 65 | UI-Registrierung |
| 28 | `CBEventReturnLeaveConfirm` | `0x006B7BD0` | 33 | UI-Registrierung |
| 29 | `CBEventReturnForcedLeaveConfirm` | `0x006B7C00` | 92 | UI-Registrierung |
| 30 | `CBProcessChatCommand` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 31 | `LeaveByCommand` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 32 | `CalcFirstPage` | `0x006B7CE0` | 44 | Aufrufgraph (geprüft) |
| 33 | `CBReceiveLeaveRequestSelf` | `0x006B7D10` | 225 | cbreg:AgcmUIGuild |
| 34 | `OpenGuildUI` | `0x006B7E00` | 100 | Aufrufgraph (geprüft) |
| 35 | `InitGuildUI` | `0x006B7E70` | 50 | Aufrufgraph (geprüft) |
| 36 | `CBGuildRenameCharID` | `0x006BA7C0` | 125 | cbreg:AgcmUIGuild |
| 37 | `RenameCharID` | `0x006BA680` | 311 | Aufrufgraph (geprüft) |
| 38 | `CBReleaseSelfCharacter` | `0x006BB7B0` | 449 | cbreg:AgcmUIGuild |
| 39 | `GetMemberRankText` | `0x006B7EB0` | 81 | Aufrufgraph (geprüft) |
| 40 | `OpenBattleRequestConfirmUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 41 | `OpenBattleCancelRequestConfirmUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 42 | `OpenBattleCancelAcceptConfirmUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 43 | `OpenBattleWithdrawConfirmUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 44 | `UpdateBattleTime` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 45 | `ProcessDrawBattleInfo` | `0x0074F400` | 110 | Aufrufgraph (geprüft) |
| 46 | `DrawBattleInfo` | `0x0074F470` | 215 | Aufrufgraph (geprüft) |
| 47 | `DrawBattleInfoInit` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 48 | `DrawBattleInfoAccept` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 49 | `DrawBattleInfoStart` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 50 | `DrawBattleInfoTime` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 51 | `DrawBattleInfoScore` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 52 | `DrawBattleInfoResult` | `0x0074EBD0` | 616 | Zeichenkette |
| 53 | `DrawBattleRount` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 54 | `CBEventReturnBattleRequest` | `0x0074EE50` | 33 | UI-Registrierung |
| 55 | `CBEventReturnBattleAccept` | `0x0074F560` | 192 | UI-Registrierung |
| 56 | `CBEventReturnBattleCancelRequest` | `0x0074EE80` | 67 | UI-Registrierung |
| 57 | `CBEventReturnBattleCancelAccept` | `0x0074F620` | 146 | UI-Registrierung |
| 58 | `CBEventReturnBattleWithdraw` | `0x0074EED0` | 74 | UI-Registrierung |
| 59 | `CBDisplayDialogEnemyGuildID` | `0x0074EF20` | 61 | UI-Registrierung |
| 60 | `CBDisplayDialogBattleType` | `0x0074EF60` | 61 | UI-Registrierung |
| 61 | `CBDisplayDialogDuration` | `0x0074EFA0` | 61 | UI-Registrierung |
| 62 | `CBDisplayDialogBattlePerson` | `0x0074EFE0` | 77 | UI-Registrierung |
| 63 | `CBReceiveBattleRequest` | `0x0074F030` | 162 | cbreg:AgcmUIGuild |
| 64 | `CBReceiveBattleAccept` | `0x0074FCF0` | 322 | cbreg:AgcmUIGuild |
| 65 | `CBReceiveBattleReject` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 66 | `CBReceiveBattleCancelRequest` | `0x0074F0E0` | 185 | cbreg:AgcmUIGuild |
| 67 | `CBReceiveBattleCancelAccept` | `0x0074F6C0` | 149 | cbreg:AgcmUIGuild |
| 68 | `CBReceiveBattleCancelReject` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 69 | `CBReceiveBattleStart` | `0x0074F760` | 233 | Zeichenkette |
| 70 | `CBReceiveBattleUpdateTime` | `0x0074F850` | 86 | cbreg:AgcmUIGuild |
| 71 | `CBReceiveBattleUpdateScore` | `0x0074F8B0` | 86 | cbreg:AgcmUIGuild |
| 72 | `CBReceiveBattleResult` | `0x0074F910` | 375 | cbreg:AgcmUIGuild |
| 73 | `CBReceiveBattleMember` | `0x0074F1A0` | 149 | cbreg:AgcmUIGuild |
| 74 | `CBReceiveBattleMemberList` | `0x0074F240` | 55 | cbreg:AgcmUIGuild |
| 75 | `CBReceiveBattleRound` | `0x0074F280` | 103 | cbreg:AgcmUIGuild |
| 76 | `CBReceiveBattleInfo` | `0x0074FAA0` | 301 | cbreg:AgcmUIGuild |
| 77 | `CBDisplayRecord` | `0x0074F2F0` | 272 | UI-Registrierung |
| 78 | `CBGuildBattleTimeOpenUIClick` | `0x0074FBD0` | 276 | UI-Registrierung |
| 79 | `CBGuildBattleTimeToggle` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 80 | `CBCreateToggle` | `0x0077DED0` | 86 | UI-Registrierung |
| 81 | `CBCreateOkClick` | `0x0077DF30` | 477 | UI-Registrierung |
| 82 | `CBCreateCompleteToggle` | `0x0077DAC0` | 229 | UI-Registrierung |
| 83 | `CBCreateConfirmToggle` | `0x0077DBB0` | 336 | UI-Registrierung |
| 84 | `CBCreateConfirmOkClick` | `0x0077DD00` | 128 | UI-Registrierung |
| 85 | `CBDestroyToggle` | `0x0077DD80` | 119 | UI-Registrierung |
| 86 | `CBDestroyOkClick` | `0x0077DE00` | 198 | UI-Registrierung |
| 87 | `CBDestroyCompleteToggle` | `0x0077D790` | 198 | UI-Registrierung |
| 88 | `CBDestroyConfirmToggle` | `0x0077D960` | 350 | UI-Registrierung |
| 89 | `CBDestroyConfirmOkClick` | `0x0077D860` | 152 | UI-Registrierung |
| 90 | `GuildDestroyConfirmGuildMarkDraw` | `0x0077D900` | 93 | Aufrufgraph (geprüft) |
| 91 | `CBGuildListToggle` | `0x0077C340` | 314 | UI-Registrierung |
| 92 | `CBGuildListTabClick` | `0x0077C480` | 210 | UI-Registrierung |
| 93 | `CBGuildListClose` | `0x0077B670` | 49 | UI-Registrierung |
| 94 | `CBGuildListClick` | `0x0077C560` | 54 | UI-Registrierung |
| 95 | `CBGuildListLeftClick` | `0x0077B6B0` | 49 | UI-Registrierung |
| 96 | `CBGuildListRightClick` | `0x0077B6F0` | 50 | UI-Registrierung |
| 97 | `CBDisplayGuildListDetailInfo` | `0x0077C5A0` | 339 | UI-Registrierung |
| 98 | `CBDisplayGuildName` | `0x0077B730` | 229 | UI-Registrierung |
| 99 | `CBDisplayGuildMemberCount` | `0x0077B820` | 92 | UI-Registrierung |
| 100 | `CBDisplayGuildWinPoint` | `0x0077B880` | 92 | UI-Registrierung |
| 101 | `RefreshGuildList` | `0x0077B8E0` | 166 | Aufrufgraph (geprüft) |
| 102 | `GuildListGuildMarkDraw` | `0x0077B990` | 93 | Aufrufgraph (geprüft) |
| 103 | `CBDisplayGuildSelected` | `0x0077B9F0` | 119 | UI-Registrierung |
| 104 | `InitGuildListUIData` | `0x0077BA70` | 74 | Aufrufgraph (geprüft) |
| 105 | `CBReceiveGuildListInfo` | `0x0077BAC0` | 891 | cbreg:AgcmUIGuild |
| 106 | `CBGuildUpdateMaxMemberCount` | `0x0077BE40` | 179 | cbreg:AgcmUIGuild |
| 107 | `CBGuildListSearch` | `0x0077BF00` | 188 | UI-Registrierung |
| 108 | `CBDisplayGuildListPage` | `0x0077BFC0` | 472 | UI-Registrierung |
| 109 | `CBDisplayGuildListMaxPage` | `0x0077C1A0` | 128 | UI-Registrierung |
| 110 | `CBDisplayGuildGuildBattleJoinRequest` | `0x0077C220` | 133 | UI-Registrierung |
| 111 | `CBEventReturnConfirmJoinRequest` | `0x0077C2B0` | 126 | UI-Registrierung |
| 112 | `CBMainOpenRequest` | `0x0077E110` | 188 | UI-Registrierung |
| 113 | `CBMainToggle` | `0x0077E1D0` | 765 | UI-Registrierung |
| 114 | `CBMainCreateRequest` | `0x0077E560` | 217 | UI-Registrierung |
| 115 | `CBMainDestroyRequest` | `0x0077E4D0` | 137 | UI-Registrierung |
| 116 | `OpenGuildMarkUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 117 | `CloseGuildMarkUI` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 118 | `CBGuildCreateGuildMark` | `0x00632C20` | 106 | UI-Registrierung |
| 119 | `CBGuildGuildMarkUIInit` | `0x006338C0` | 216 | UI-Registrierung |
| 120 | `SetGridItem` | `0x00632C90` | 433 | Zeichenketten/Konstanten (geprüft) |
| 121 | `InitGuildMarkGridItem` | `0x006339A0` | 694 | Aufrufgraph (geprüft) |
| 122 | `DestroyPreviewGuildMark` | `0x00632E50` | 359 | Aufrufgraph (geprüft) |
| 123 | `CBGuildGuildMarkUIClose` | `0x00632FC0` | 39 | UI-Registrierung |
| 124 | `CBIsGuildMarkSelected` | `0x00632FF0` | 43 | UI-Registrierung |
| 125 | `CBGuildupdateGuildMarkLayer` | `0x00633C70` | 109 | UI-Registrierung |
| 126 | `CBGuildMarkGridLClickDown` | `0x00633CE0` | 188 | UI-Registrierung |
| 127 | `CBGuildMarkColorGridLClickDown` | `0x00633DA0` | 145 | UI-Registrierung |
| 128 | `SetPreviewGuildMark` | `0x00633020` | 619 | Aufrufgraph (geprüft) |
| 129 | `CBDisplayGuildMarkInfo` | `0x00633E40` | 881 | UI-Registrierung |
| 130 | `CBGuildGuildMarkClickInitialize` | `0x00633290` | 39 | UI-Registrierung |
| 131 | `GuildMarkInitialize` | `0x006332C0` | 127 | Aufrufgraph (geprüft) |
| 132 | `CBGuildGuildMarkClickBuy` | `0x00633340` | 86 | UI-Registrierung |
| 133 | `CBGuildGuildMarkClickBuyOK` | `0x006333A0` | 42 | UI-Registrierung |
| 134 | `GetCurrentTabIndex` | `0x006333D0` | 28 | Aufrufgraph (geprüft) |
| 135 | `InitSeletedGridItem` | `0x006333F0` | 129 | Aufrufgraph (geprüft) |
| 136 | `CBGuildGuildMarkInitialize` | `0x00633480` | 58 | UI-Registrierung |
| 137 | `CBGuildGuildMarkDuplicate` | `0x006334C0` | 49 | UI-Registrierung |
| 138 | `CBGuildBuyGuildMark` | `0x00633500` | 389 | Aufrufgraph (geprüft) |
| 139 | `CBGuildGuildMarkBuyConfirmUIOpen` | `0x00634220` | 16 | UI-Registrierung |
| 140 | `GuildMarkBuyConfirmUIOpen` | `0x006341C0` | 95 | Aufrufgraph (geprüft) |
| 141 | `GuildMarkDraw` | `0x00633690` | 287 | Aufrufgraph (geprüft) |
| 142 | `MakeCommaNumber` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 143 | `MakeCommaNumber` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 144 | `CBMaxMemberIncreaseUIToggle` | `0x0077C700` | 715 | UI-Registrierung |
| 145 | `CBGuildMaxMemberIncreaseOK` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 146 | `CBGuildMaxMemberIncreaseOpenUI` | `0x0077CA00` | 220 | UI-Registrierung |
| 147 | `CBEventReturnGuildMaxMemberIncreaseOK` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 148 | `InitMemberUIData` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 149 | `SetCurrentPage` | `0x00778DB0` | 25 | Aufrufgraph (geprüft) |
| 150 | `RefreshMemberPageUI` | `0x007789C0` | 235 | Aufrufgraph (geprüft) |
| 151 | `GetMemberListPage` | `0x00777D70` | 74 | Aufrufgraph (geprüft) |
| 152 | `GetGuildMember` | `0x00777DC0` | 97 | Aufrufgraph (geprüft) |
| 153 | `CBMemberToggle` | `0x00778AB0` | 49 | UI-Registrierung |
| 154 | `CBMemberTabClick` | `0x007772C0` | 99 | UI-Registrierung |
| 155 | `CBMemberSelect` | `0x00778AF0` | 84 | Aufrufgraph (geprüft) |
| 156 | `SelectMember` | `0x00778900` | 123 | Aufrufgraph (geprüft) |
| 157 | `RefreshGuildMemberButton` | `0x00777E30` | 836 | Aufrufgraph (geprüft) |
| 158 | `CBMemberLeaveClick` | `0x00777AA0` | 320 | UI-Registrierung |
| 159 | `CBMemberLeftClick` | `0x00778B50` | 43 | UI-Registrierung |
| 160 | `CBMemberRightClick` | `0x00778B80` | 61 | UI-Registrierung |
| 161 | `CBMemberClose` | `0x00777330` | 49 | UI-Registrierung |
| 162 | `CBMemberSelectDClick` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 163 | `CBDisplayMemberStatus` | `0x00778180` | 100 | UI-Registrierung |
| 164 | `CBDisplayMemberName` | `0x007781F0` | 207 | UI-Registrierung |
| 165 | `CBDisplayMemberLevel` | `0x007782C0` | 168 | UI-Registrierung |
| 166 | `CBDisplayMemberClass` | `0x00778370` | 155 | UI-Registrierung |
| 167 | `CBDisplayMemberRace` | `0x00778410` | 126 | UI-Registrierung |
| 168 | `CBDisplayMemberSelect` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 169 | `CBDisplaySelectedMember` | `0x007773E0` | 61 | UI-Registrierung |
| 170 | `CBDisplayMemberDetailInfo` | `0x00778490` | 522 | UI-Registrierung |
| 171 | `CBGuildMemberSearch` | `0x00778BC0` | 493 | UI-Registrierung |
| 172 | `CBDisplayGuildMemberListPage` | `0x00777420` | 472 | UI-Registrierung |
| 173 | `CBDisplayGuildMemberListMaxPage` | `0x00777600` | 120 | UI-Registrierung |
| 174 | `CBGuildClickWhisperChat` | `0x00777680` | 34 | UI-Registrierung |
| 175 | `CBGuildClickInviteParty` | `0x007786A0` | 123 | UI-Registrierung |
| 176 | `CBGuildWhisperChat` | `0x007776B0` | 117 | UI-Registrierung |
| 177 | `CBGuildJoinAllowMember` | `0x00778720` | 59 | UI-Registrierung |
| 178 | `CBGuildLeaveAllowMember` | `0x00778760` | 59 | UI-Registrierung |
| 179 | `CBDisplayGuildAllowButton` | `0x007787A0` | 135 | UI-Registrierung |
| 180 | `CBGuildAllowClick` | `0x00778980` | 52 | UI-Registrierung |
| 181 | `AllowSelectMember` | `0x00778830` | 200 | Aufrufgraph (geprüft) |
| 182 | `CBGuildAppointClick` | `0x00777730` | 282 | UI-Registrierung |
| 183 | `CBGuildSuccessionClick` | `0x00777850` | 113 | UI-Registrierung |
| 184 | `CBGuildAppointAsk` | `0x007778D0` | 234 | cbreg:AgcmUIGuild |
| 185 | `CBGuildAppointSysMsg` | `0x00777BE0` | 43 | cbreg:AgcmUIGuild |
| 186 | `CBGuildSuccessionAsk` | `0x007779C0` | 123 | cbreg:AgcmUIGuild |
| 187 | `CBGuildMemberRankChange` | `0x00777C10` | 175 | Aufrufgraph (geprüft) |
| 188 | `CBDisplayAppointAndCancelBtnText` | `0x00777A40` | 49 | UI-Registrierung |
| 189 | `CBNoticeOpenRequest` | `0x0077CE00` | 119 | UI-Registrierung |
| 190 | `CBNoticeToggle` | `0x0077CE80` | 39 | UI-Registrierung |
| 191 | `CBNoticeUIInit` | `0x0077CEB0` | 789 | UI-Registrierung |
| 192 | `CBNoticeTabClick` | `0x0077D1D0` | 99 | UI-Registrierung |
| 193 | `CBNoticeClose` | `0x0077D240` | 49 | UI-Registrierung |
| 194 | `CBNoticeEditClick` | `0x0077D280` | 94 | UI-Registrierung |
| 195 | `CBNoticeSendClick` | `0x0077D2E0` | 163 | UI-Registrierung |
| 196 | `CBDisplayNotice` | `0x0077D390` | 275 | UI-Registrierung |
| 197 | `CBDisplayDetailInfo` | `0x0077D4B0` | 496 | UI-Registrierung |
| 198 | `CBGuildClickLeaveGuildNotice` | `0x0077D6A0` | 237 | UI-Registrierung |
| 199 | `CBJointRequest` | `0x00778DD0` | 219 | cbreg:AgcmUIGuild |
| 200 | `CBJoint` | `0x0077A8E0` | 282 | cbreg:AgcmUIGuild |
| 201 | `CBJointLeave` | `0x0077AD20` | 586 | cbreg:AgcmUIGuild |
| 202 | `CBHostileRequest` | `0x00778EB0` | 219 | cbreg:AgcmUIGuild |
| 203 | `CBHostile` | `0x00778F90` | 246 | cbreg:AgcmUIGuild |
| 204 | `CBHostileLeaveRequest` | `0x00779090` | 195 | cbreg:AgcmUIGuild |
| 205 | `CBHostileLeave` | `0x0077A1F0` | 344 | cbreg:AgcmUIGuild |
| 206 | `CBEventReturnJointRequest` | `0x00779160` | 347 | UI-Registrierung |
| 207 | `CBEventReturnJointAccept` | `0x007792C0` | 64 | UI-Registrierung |
| 208 | `CBEventReturnJointLeave` | `0x00779300` | 33 | UI-Registrierung |
| 209 | `CBEventReturnHostileRequest` | `0x00779330` | 347 | UI-Registrierung |
| 210 | `CBEventReturnHostileAccept` | `0x00779490` | 64 | UI-Registrierung |
| 211 | `CBEventReturnHostileLeaveRequest` | `0x007794D0` | 40 | UI-Registrierung |
| 212 | `CBEventReturnHostileLeaveAccept` | `0x00779500` | 64 | UI-Registrierung |
| 213 | `CBOpenJointList` | `0x00779EF0` | 34 | UI-Registrierung |
| 214 | `CBOpenHostileList` | `0x00779F20` | 34 | UI-Registrierung |
| 215 | `CBOnJointRequestBtnClick` | `0x00779540` | 369 | UI-Registrierung |
| 216 | `CBOnHostileRequestBtnClick` | `0x007796C0` | 207 | UI-Registrierung |
| 217 | `CBJointDetail` | `0x0077B3A0` | 705 | cbreg:AgcmUIGuild |
| 218 | `CBHostileDetail` | `0x0077AF70` | 705 | cbreg:AgcmUIGuild |
| 219 | `AddJointDetail` | `0x0077B240` | 347 | Aufrufgraph (geprüft) |
| 220 | `SortJointDetail` | `0x0077AA00` | 425 | Aufrufgraph (geprüft) |
| 221 | `AddHostileDetail` | `0x0077ABC0` | 340 | Aufrufgraph (geprüft) |
| 222 | `CBDisplayRelationGuildID` | `0x00779790` | 61 | UI-Registrierung |
| 223 | `CBDisplayRelationMasterID` | `0x007797D0` | 61 | UI-Registrierung |
| 224 | `CBDisplayJointRequestBtn` | `0x00779810` | 108 | UI-Registrierung |
| 225 | `CBDisplayHostileRequestBtn` | `0x00779880` | 104 | UI-Registrierung |
| 226 | `SetGuildListToJointList` | `0x00779BB0` | 173 | Aufrufgraph (geprüft) |
| 227 | `SetGuildListToHostileList` | `0x00779C70` | 173 | Aufrufgraph (geprüft) |
| 228 | `CBGetJointMark` | `0x00779FB0` | 85 | cbreg:AgcmUIGuild |
| 229 | `CBGetJointColor` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 230 | `CBGuildRenameUIOpen` | `0x0077CC30` | 86 | UI-Registrierung |
| 231 | `CBGuildRenameUIInit` | `0x0077CC90` | 122 | UI-Registrierung |
| 232 | `CBGuildRenameOKClick` | `0x0077CD10` | 91 | UI-Registrierung |
| 233 | `CBGuildRenameGuildID` | `0x0077CD70` | 144 | cbreg:AgcmUIGuild |
| 234 | `CBDisplayDialogWorldChampionship` | `0x0077CBB0` | 60 | UI-Registrierung |
| 235 | `CBOnWorldChampionshipRequestBtnClick` | `0x0077CBF0` | 26 | UI-Registrierung |
| 236 | `CBOnWorldChampionshipEnterBtnClick` | `0x0077CC10` | 26 | UI-Registrierung |

208 von 237 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006ba8a0` (`0x006BA8A0`), `ctor_or_dtor_006bb3c0` (`0x006BB3C0`), `~AgcmUIGuild` (`0x006BB980`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1C20` | `Zustand der eigenen Gilde (Felder werden in `CBReleaseSelfCharacter` geleert)` | `CBReleaseSelfCharacter`, `CBGuildUpdateMaxMemberCount`, `AddJointDetail` |
| `0x1C41` | `Zeichenkette der eigenen Gilde (Vergleich in `CBCreateComplete`, vermutlich der Name)` | `CBCreateComplete` |
| `0x1D38` | `Mitgliederliste (STL-Liste)` | `GetGuildMember` |
| `0x1E24` | `letzter Tab der Gildeninfo (0 Notiz, 1 Mitglieder)` | `InitGuildUI` |
| `0x1E28` | `aktuelle Seite der Mitgliederliste` | `SetCurrentPage` |
| `0x1E30` | `Anzahl der Gilden in der Liste` | `RefreshGuildList` |
| `0x2114` | `Userdata Ebenenindex des Gildenzeichens` | `GetCurrentTabIndex` |

## Adressbereiche

Die Klasse verteilt sich auf viele Quelldateien in vier Adressbereichen:

| Bereich | Inhalt (nach Quellnamen und Zeichenketten) |
|---|---|
| `0x00632C20`–`0x00634230` | `AgcmUIGuildMark.cpp` (Gildenzeichen) |
| `0x006B6930`–`0x006BBA00` | `AgcmUIGuild.cpp` (Hauptteil, `OnAddModule` bei `0x006BB9A0`) |
| `0x0074EBD0`–`0x0074FE80` | `AgcmUIGuildBattle.cpp` (Gildenkampf) |
| `0x007772C0`–`0x0077E700` | Mitglieder-, Listen-, Beziehungs-, Umbenennungs- u. a. Dateien |

## Callback-Registrierung in OnAddModule (0x006BB9A0)

Die Quelle meldet 48 Callbacks an, im Binary sind es 47 erkennbare Aufrufe in gleicher Reihenfolge. Fest verankert ist die Ausrichtung durch vier unabhängige Treffer (`CBUpdateMemberStatus`, `CBUpdateNotice`, `CBSystemMessage`, `CBGuildBuyGuildMark` stehen an den gleichen Positionen). `CBJoinReject`, `CBReceiveBattleReject` und `CBReceiveBattleCancelReject` zeigen im Binary auf Stub-Funktionen (`0x005759F0`, `Element::GetSize`); `CBGetJointMark` und `CBGetJointColor` haben denselben Rumpf und teilen sich `0x00779FB0`, ein Eintrag der Quelle ist im Binary nicht einzeln erkennbar.

| Position | Handler | Adresse |
|---:|---|---|
| 1 | `CBCreateComplete` | `0x006B74A0` |
| 2 | `CBJoinRequest` | `0x006B7560` |
| 3 | `CBJoin` | `0x006B7600` |
| 4 | `CBLeave` | `0x006B7690` |
| 5 | `CBDestroy` | `0x006B9800` |
| 6 | `CBCharData` | `0x006B9900` |
| 7 | `CBUpdateMemberStatus` | `0x006BB500` |
| 8 | `CBUpdateNotice` | `0x006B7780` |
| 9 | `CBSystemMessage` | `0x006B9A10` |
| 10 | `CBGuildUpdateMaxMemberCount` | `0x0077BE40` |
| 11 | `CBReceiveBattleInfo` | `0x0074FAA0` |
| 12 | `CBReceiveBattleRequest` | `0x0074F030` |
| 13 | `CBReceiveBattleAccept` | `0x0074FCF0` |
| 14 | `CBReceiveBattleCancelRequest` | `0x0074F0E0` |
| 15 | `CBReceiveBattleCancelAccept` | `0x0074F6C0` |
| 16 | `CBReceiveBattleStart` | `0x0074F760` |
| 17 | `CBReceiveBattleUpdateTime` | `0x0074F850` |
| 18 | `CBReceiveBattleUpdateScore` | `0x0074F8B0` |
| 19 | `CBReceiveBattleResult` | `0x0074F910` |
| 20 | `CBReceiveBattleMember` | `0x0074F1A0` |
| 21 | `CBReceiveBattleMemberList` | `0x0074F240` |
| 22 | `CBReceiveBattleRound` | `0x0074F280` |
| 23 | `CBEventGrant` | `0x006B7990` |
| 24 | `CBSelfUpdatePosition` | `0x006B7A40` |
| 25 | `CBReceiveGuildListInfo` | `0x0077BAC0` |
| 26 | `CBReceiveLeaveRequestSelf` | `0x006B7D10` |
| 27 | `CBGuildRenameGuildID` | `0x0077CD70` |
| 28 | `CBGuildRenameCharID` | `0x006BA7C0` |
| 29 | `CBGuildBuyGuildMark` | `0x00633500` |
| 30 | `CBJointRequest` | `0x00778DD0` |
| 31 | `CBJoint` | `0x0077A8E0` |
| 32 | `CBJointLeave` | `0x0077AD20` |
| 33 | `CBHostileRequest` | `0x00778EB0` |
| 34 | `CBHostile` | `0x00778F90` |
| 35 | `CBHostileLeaveRequest` | `0x00779090` |
| 36 | `CBHostileLeave` | `0x0077A1F0` |
| 37 | `CBJointDetail` | `0x0077B3A0` |
| 38 | `CBHostileDetail` | `0x0077AF70` |
| 39 | `CBGetJointMark` | `0x00779FB0` |
| 40 | `CBReleaseSelfCharacter` | `0x006BB7B0` |
| 41 | `CBGuildAppointAsk` | `0x007778D0` |
| 42 | `CBGuildSuccessionAsk` | `0x007779C0` |
| 43 | `CBGuildAppointSysMsg` | `0x00777BE0` |
| 44 | `CBGuildMemberRankChange` | `0x00777C10` |

## Konstanten

- **Seitenanzeige:** `CalcFirstPage` (`0x006B7CE0`): ab 10 Seiten (`AGCMUIGUILD_MAX_VIEW_PAGE`) zeigt die Leiste 10 Seiten, mit 5 (`HALF`) davor/danach um die aktuelle Seite.
- **Gildenliste:** 19 Einträge je Seite (`AGCMUIGUILD_MAX_VISIBLE_MEMBER_LIST`, `RefreshGuildList` `0x0077B8E0` rechnet `(Anzahl − 1) / 19`).
- **Rangtexte (`GetMemberRankText`, `0x006B7EB0`):** Rang 1 = normales Mitglied, 10 = Meister, 11 = Vize-Meister (wie `AgpmGuildMemberRank` der Quelle); andere Werte liefern keinen Text.
- **Gildenzeichen:** `GetCurrentTabIndex` (`0x006333D0`) bildet den ausgewählten Ebenen-Index (0–2) auf 1–3 ab, sonst 1.

## Abweichungen von der EP8-Quelle

- Keine bestätigte Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Rund ein Achtel der Methoden ist nicht zugeordnet, meist kleine Hilfsfunktionen und UI-Callbacks (`CBDisplay…`, Klick-Handler) ohne eindeutige Aufrufbeziehung.
- Die Adressbereiche der Quelldateien sind aus Zeichenketten und Nachbarklassen abgeleitet; die Dateizuordnung im Mitglieder-Bereich ist nicht Datei für Datei belegt.
- Die Texte der Gilden-Meldungen und die Server-Pakete ([`AgpmGuild`](AgpmGuild.md), [`AgpmEventGuild`](AgpmEventGuild.md)) wurden nicht erneut verglichen; sie stehen in den Berichten der Paketmodule.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 5, nicht im Client: 6, ohne Kandidat: 9, zugeordnet: 9.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `DrawBattleInfoStart` | 19 | `0x0074E530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawBattleInfoAccept` | 23 | `0x0074E460` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakeCommaNumber` | 22 | `0x00633870` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenGuildMarkUI` | 7 | `0x00632BC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawBattleInfoInit` | 12 | `0x0074E2C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawBattleInfoScore` | 73 | `0x0074E930` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DrawBattleInfoTime` | 71 | `0x0074E5F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenBattleWithdrawConfirmUI` | 14 | `0x0074E260` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenBattleRequestConfirmUI` | 22 | `0x0074E050` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmEventGuild`](AgpmEventGuild.md), [`AgpmGuild`](AgpmGuild.md)
- **Erwähnt in:** [`AgcmGuild`](AgcmGuild.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md)
