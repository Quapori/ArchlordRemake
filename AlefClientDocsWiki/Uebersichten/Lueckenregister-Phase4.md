# Phase 4

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Erzeugt mit `gapclose.py register`. Jede Quellmethode ohne Binary-Adresse bekommt einen Status mit Beleg. **zugeordnet** = eindeutiger Treffer (mindestens zwei unabhängige Belege, Reihenfolge der Quelle passt zur Adressreihenfolge); **gemeinsamer Rumpf** = `SetCallback`-Einzeiler; **nicht im Client** = in der Quelle ruft sie kein Client-Modul (nur Server oder niemand); **eingebaut** = kleine Funktion mit Aufrufer im Client, ohne eigene Adresse; **Kandidat unbestätigt** = Aufrufer im Client und ein Kandidat mit nur einem Beleg oder mehrdeutig (nicht benannt); **ohne Kandidat** / **nicht als eigene Funktion** = Aufrufer im Client, aber keine unbenannte Funktion mit Beleg (bei „nicht als eigene Funktion“ ist im Klassenbereich gar keine unbenannte Funktion mehr übrig); in beiden Fällen ist die Methode vermutlich eingebaut oder entfernt.

Zahlen: Kandidat unbestätigt 264, eingebaut 738, gemeinsamer Rumpf 94, nicht als eigene Funktion 267, nicht im Client 537, ohne Kandidat 853, zugeordnet 362

## AcArchlordInfo (eingebaut 1, nicht im Client 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Destroy` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmItem::ItemDestructorCB, AgcmObject::ReleaseObjectData; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetGroup` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUILoginSelect::_LoginSelectWindowInit, AgcmUILoginSelect::GetLoginGroup, AgcmUILoginSelect::ConnectLoginServer |
| `GetPatchServer` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AcMapLoader (eingebaut 2, ohne Kandidat 4, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetUnpackManager` | 95 | zugeordnet | `0x00734500` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnIdleLoad` | 36 | zugeordnet | `0x00734990` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveQueue` | 70 | zugeordnet | `0x00734820` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsEmpty` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AcMapLoader::OnIdleLoad, CBmp::LoadBitmap, CBmp::Draw |
| `LoadDWSector` | 52 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::OnLoadRough, AgcmMap::OnLoadDetail, AgcmMap::LoadAll; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `AddLoadSectorInfo` | 25 | ohne Kandidat |  | Aufrufer im Client: AcMapLoader::LoadDWSector; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `DoExistSectorInfo` | 25 | ohne Kandidat |  | Aufrufer im Client: AcMapLoader::LoadDWSector, AcMapLoader::AddLoadSectorInfo; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `EmptyQueue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmMap::DeleteMyCharacterCheck |
| `FlushUnpackManager` | 12 | ohne Kandidat |  | Aufrufer im Client: AcMapLoader::~AcMapLoader; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |

## AcTextureList (nicht als eigene Funktion 10, nicht im Client 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `LoadScript` | 90 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmMap::InitMapToolData; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `GetTexture` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::ModifyAtomic, AgcmItem::GetTexture, AgcmItem::LoadTemplateTexture; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `DeleteAll` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AgcaEffectData2::CopyDataSet, AgcmEventEffect::AttachedDataUseEffectSetDestructCB, AgcmGrass::OnDestroy; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `Delete` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcaEffectData2::Delete, AgcaEffectData2::Delete, AgcaEffectData2::DeleteAll; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `LoadTexture` | 171 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::GetTexture, AgcmItem::GetTexture, AcTextureList::GetTexture; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `GetTextureInfo` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AcTextureList::GetTexture, AcTextureList::DeleteTexture, AcTextureList::LoadRaster; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `DeleteTexture` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddTexture` | 38 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::LoadTextureScriptFile, AgcmUIWorldmap::OnInit, AgcmShrine::OnInit; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `SaveScript` | 87 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeTempBitmap` | 228 | nicht als eigene Funktion |  | Aufrufer im Client: AcTextureList::AddTexture, AcTextureList::InitialTempFiles; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `InitialTempFiles` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ExportTile` | 80 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetExportFileName` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AcTextureList::LoadTexture, AcTextureList::ExportTile; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `LoadRaster` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadImage` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmMap::CreateImAtomic, CBmp::LoadBitmap; im Adressbereich der Klasse (0x007343C0–0x007343C0) ist keine unbenannte Funktion mehr übrig |
| `CleanUpUnusedTile` | 112 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AcUIBar (eingebaut 2, nicht im Client 1, ohne Kandidat 11)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `InitBar` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPointInfo` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RefreshControl; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_CalculateNextRate` | 56 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::SetPointInfo; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_GetBodyTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBar::OnWindowRender |
| `_GetEdgeTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBar::OnWindowRender |
| `_IsValidTexture` | 16 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawTexture` | 29 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::_DrawBodyNoAnim, AcUIBar::_DrawBodySmoothShadow, AcUIBar::_DrawBodySmoothBody; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawTexture` | 12 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::_DrawBodyNoAnim, AcUIBar::_DrawBodySmoothShadow, AcUIBar::_DrawBodySmoothBody; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawBody` | 20 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawBodyNoAnim` | 63 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::_DrawBody; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawBodySmooth` | 83 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::_DrawBody; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawBodySmoothShadow` | 62 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::_DrawBodySmooth; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawBodySmoothBody` | 57 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::_DrawBodySmooth; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_DrawEdge` | 37 | ohne Kandidat |  | Aufrufer im Client: AcUIBar::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |

## AcUIBase (Kandidat unbestätigt 10, eingebaut 18, nicht im Client 8, ohne Kandidat 11, zugeordnet 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetAlpha` | 17 | zugeordnet | `0x007272E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StartAnimation` | 9 | zugeordnet | `0x00727190` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetDragDropMessage` | 8 | zugeordnet | `0x007270C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetStatus` | 34 | zugeordnet | `0x00728B30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetStaticString` | 87 | zugeordnet | `0x00728870` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetStaticStringExt` | 19 | zugeordnet | `0x00728EC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddImage` | 23 | zugeordnet | `0x00727F80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_RenderText` | 40 | zugeordnet | `0x007278C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `MakeStringFit` | 57 | zugeordnet | `0x00726AA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `PlayUISound` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIButton::OnLButtonUp |
| `DestroyImage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIShrineShop::CBItemImage |
| `AddOnlyThisImage` | 18 | Kandidat unbestätigt | `0x00726850` | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap, AgcUIEffect::SetEffectImage, AgcUIEffect::SetEffectBG; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnLButtonDblClkForHandler` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBase::OnLButtonDblClk |
| `OnAddImage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBase::AddImage, AcUIBase::AddOnlyThisImage, AcUIButton::AddButtonImage |
| `DrawOutline` | 12 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `SetRenderColor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamReadCB |
| `SetRenderAlpha` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamReadCB |
| `SetRednerTexture` | 12 | Kandidat unbestätigt | `0x00728840` | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap, AgcmMinimap::ToggleMinimapSize, AcUIBase::SetStatus; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetRenderScale` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcUIEffect::OnIdle, AgcUIEffect::SetEffectText, AgcUIEffect::SetEffectImage |
| `SetDefaultRenderTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBase::OnInit, AcUIEditOKDialog::EditControlImage, AgcmUIManager2::StreamReadCB |
| `GetRenderColor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamWriteBase |
| `GetRenderAlpha` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamWriteBase |
| `GetRenderTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcTipWindow::OnWindowRender |
| `GetDefaultRenderTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamWriteBase |
| `EnableHandler` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetHandler` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIChatting::OnInit, AgcmUIManager2::StreamReadCB; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `SetShrinkMode` | 39 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MoveChildByShrink` | 59 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::SetShrinkMode; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `CheckInHandlerArea` | 11 | Kandidat unbestätigt | `0x00726C90` | Aufrufer im Client: AcUIBase::OnLButtonDown, AcUIBase::OnLButtonUp, AcUIBase::OnLButtonDblClk; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetStatusInfo` | 50 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamReadCB; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `GetStatusInfo_ID` | 11 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::SetStatus; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `GetStatusInfo_Index` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamWriteBase |
| `DeleteStatusInfo_ID` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteStatusInfo_Index` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteAllStatusInfo` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetUserData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIManager2::SetControlDisplayMap |
| `GetUserData` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RemoveAllUserData, AgcmUIManager2::CountUserData, AgcmUIManager2::ParseMessage; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `SetShrinkModeRenderInfo` | 24 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::AddImage, AcUIBase::SetRednerTexture, AcUIBase::SetShrinkMode; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `AddAnimation` | 25 | Kandidat unbestätigt | `0x00729F60` | Aufrufer im Client: AgcaAnimation2::AddAnimation, AgcaAnimation2::CopyAnimation, AgcmCharacter::AnimationStreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveAllAnimation` | 16 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcmCharacter::DeleteTemplateAnimation, AgcmObject::LoadTemplateData, AgcmObject::RemoveObjectTemplateGroupData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveAnimation` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StopAnimation` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StopAnimation, AgcmCharacter::StopAnimation, AgcmUIGuideMessage::CallBack_Open |
| `SetTooltip` | 15 | Kandidat unbestätigt | `0x00606E80` | Aufrufer im Client: AgcmBillInfo::AddSystemGridIcon_PCRoom, AgcmBillInfo::_AddSystemGridHangameS, AgcmBillInfo::_AddSystemGridHangameTPack; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `CloseUI` | 11 | Kandidat unbestätigt | `0x005E5F50` | Aufrufer im Client: CExNPCDialog::OnHideNPCDialog, AgcmUIWorldmap::CBWorldMapToggle, AgcmUIWorldmap::S_Close; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `GetColor` | 14 | Kandidat unbestätigt | `0x0063E4F0` | Aufrufer im Client: AgcmDmgBoard::_DrawDamage, AgcmDmgBoard::_DrawCriticalDamage, AgcmHPBar::SetData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `_RenderRGBARender` | 12 | Kandidat unbestätigt | `0x007274B0` | Aufrufer im Client: AcUIBase::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_RenderSmoothRGBARender` | 28 | Kandidat unbestätigt | `0x007274B0` | Aufrufer im Client: AcUIBase::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_RenderBaseTexture` | 21 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `_UpdateAnimation` | 40 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `_DrawOutLine` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AcUIBase::DrawOutline |
| `SetDefaultRenderType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatManager::CBDisplayColor, AgcUIChatMessage::Initialize |
| `SetRenderRGBAColor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatManager::CreateUIChatMessage, AgcChatManager::_DockingPreEventStart, AgcChatManager::_DockingPreEventEnd |
| `SetRenderSmoothTime` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRenderSmoothStartTime` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetBlink` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacter::CharacterStatusCB; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |
| `_CheckMouseReSizeArea` | 89 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 1749 unbenannten Funktionen im Klassenbereich |

## AcUIBbs (Kandidat unbestätigt 2, eingebaut 9, nicht im Client 2, ohne Kandidat 14, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_DrawPageManager` | 24 | zugeordnet | `0x00790A30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InitInfoInput` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIRecruit::ChildControlInit |
| `Destroy` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmItem::ItemDestructorCB, AgcmObject::ReleaseObjectData |
| `_CreateCellContentMemory` | 14 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::InitInfoInput; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_DestroyCellContentMemory` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::Destroy, AcUIBbs::_CreateCellContentMemory; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `SetColumnInfo` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIRecruit::ChildControlInit |
| `SetColumnInfo` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIRecruit::ChildControlInit; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_DrawBbsContent` | 38 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `OnPostRender` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::OnRender, AgcWindow::WindowControlMessageProc |
| `PageManagerSetting` | 29 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::InitInfoInput, AcUIBbs::SetPageInfo; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `SetPageInfo` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmRecruit::ProcessSearchLFPResult, AgcmRecruit::ProcessSearchLFMResult |
| `SetCellText` | 9 | Kandidat unbestätigt | `0x00791100` | Aufrufer im Client: AgcmRecruit::SendSearchLFPByPage, AgcmRecruit::SendSearchLFMByPage, AgcmRecruit::ProcessSearchLFPResult; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_IsValidArrayIndex` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIBbs::_GetCell |
| `_IsValidRowIndex` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIBbs::ClearCellText_ByRow |
| `_IsValidColumnIndex` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_IsValidPageIndex` | 11 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::_DrawPageManager, AcUIBbs::PageManagerSetting; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_IsValidCallBackIndex` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_IsInAreaPageManager` | 11 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_IsInAreaCell` | 11 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_GetCell` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIBbs::OnLButtonDown, AcUIBbs::SetCellText, AcUIBbs::ClearCellText |
| `_GetCell` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::OnLButtonDown, AcUIBbs::SetCellText, AcUIBbs::ClearCellText; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_SendChangePage` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_SendClickCell` | 10 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_DrawColumnName` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIBbs::_DrawBbsContent |
| `_DrawCell` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::_DrawBbsContent; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `ClearCellText_ByRow` | 7 | Kandidat unbestätigt | `0x00791100` | Aufrufer im Client: AgcmRecruit::ProcessSearchLFPResult, AgcmRecruit::ProcessSearchLFMResult; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ClearCellText` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::ClearCellText_ByRow, AcUIBbs::ClearAllCellText; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `ClearAllCellText` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIBbs::_CreateCellContentMemory; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |

## AcUIBbsContent (eingebaut 3, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnPostRender` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::OnRender, AgcWindow::WindowControlMessageProc |
| `SetContentText` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DrawContentText` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIBbsContent::OnWindowRender |
| `SetDrawRect` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseContentTextMemory` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AcUIBbsContent::OnClose |

## AcUIButton (Kandidat unbestätigt 2, eingebaut 5, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetButtonEnable` | 9 | zugeordnet | `0x007259F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddButtonImage` | 11 | zugeordnet | `0x00725690` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetButtonImage` | 8 | zugeordnet | `0x00725720` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetButtonSelectImage` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcUIQuestText::InsertQuestControl |
| `GetButtonImage` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamWriteButton; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `ClearImage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIToolTip::_InitExitButton |
| `OnPostRender` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcEngine::OnRender, AgcWindow::WindowControlMessageProc |
| `GetDragDropGridItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIEventBank::CBBankDragDropItem, AgcmUIItem::CBDragDropItemToChargingInventoryA, AgcmUIItem::CBDragDropItemToChargingInventoryB |
| `SetButtonMode` | 62 | Kandidat unbestätigt | `0x007252B0` | Aufrufer im Client: AcUIRecruit::SetBbsMode, AcUIRecruit::ChildControlInit, AcUIRecruitWrite::SetWriteWindowInit; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetButtonMode` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIRecruit::GetClassSelectInfo, AcUIRecruitWrite::OnClickWriteButton, AgcmUIBuddy::CBBtnBlockWhisperClick |
| `_DrawSelectImage` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIButton::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `_DrawBgColor` | 7 | Kandidat unbestätigt | `0x007254F0` | Aufrufer im Client: AcUIButton::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |

## AcUIChattingEdit (eingebaut 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnClose` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::Close, AcUIBbs::OnClose, AcUIBbsContent::OnClose |
| `SetCurrentInputType` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: CChattingInputController::ChangeInputStatus |
| `RefreshCustomData` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIChattingEdit::UpdateCurrentStatus |

## AcUICheckBox (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnPostRender` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcEngine::OnRender, AgcWindow::WindowControlMessageProc |
| `OnMouseMove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIRaider::OnMouseMove, AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc |

## AcUIClock (eingebaut 3, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetAlphaImageID` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamReadCB |
| `SetPointInfo` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIManager2::RefreshControl; im Adressbereich der Klasse (0x0072AA60–0x0072ADE0) ist keine unbenannte Funktion mehr übrig |
| `_GetAlphaTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIClock::OnWindowRender |
| `_IsVaildTexture` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIClock::OnWindowRender |

## AcUICombo (Kandidat unbestätigt 3, eingebaut 7, gemeinsamer Rumpf 1, nicht im Client 2, ohne Kandidat 15, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_DrawComboText` | 5 | zugeordnet | `0x00724940` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddString` | 47 | zugeordnet | `0x00723B30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_DrawSelectedItemText` | 18 | zugeordnet | `0x007249B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInit` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `ClearAllString` | 20 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::~AcUICombo, AcUICombo::AddString, AcUICombo::OnClose; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `OpenComboControl` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::OnCommand; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `CloseComboControl` | 10 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::OnCommand, AcUICombo::OnLButtonDown; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `GetComboItem` | 23 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::GetItemData, AcUICombo::GetItemData, AcUICombo::SetItemData; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `GetComboItem` | 17 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::GetItemData, AcUICombo::GetItemData, AcUICombo::SetItemData; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `GetItemData` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmAIDialog::OnAIFactorAdd, AgcmAIDialog::OnAIActionAddUpdate, AgcmAIDialog::OnItemchangedAIFactors; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `GetItemData` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmAIDialog::OnAIFactorAdd, AgcmAIDialog::OnAIActionAddUpdate, AgcmAIDialog::OnItemchangedAIFactors; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `DeleteString` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmAIScreamEditDlg::OnAiHelpScreamCharRemoveButton; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `DeleteString` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcmAIScreamEditDlg::OnAiHelpScreamCharRemoveButton; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `SetItemData` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmAIDialog::InitDataFactor, AgcmAIDialog::OnInitDialog, AgcmAITemplateDialog::OnInitDialog; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `SetItemData` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmAIDialog::InitDataFactor, AgcmAIDialog::OnInitDialog, AgcmAITemplateDialog::OnInitDialog; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `GetSelectedString` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIPartyOption::CBPartyOptionAply |
| `GetSelectedIndex` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcUIWindow::OnCommand, AgcmUISiegeWar::GetComboTime |
| `SelectString` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SelectIndex` | 21 | Kandidat unbestätigt | `0x007252B0` | Aufrufer im Client: AcUICombo::OnLButtonDown, AgcmUIManager2::RefreshControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `EnableString` | 9 | Kandidat unbestätigt | `0x00724760` | Aufrufer im Client: AgcmUIOption::CBWater, AgcmUIOption::CBBloom, AgcmUIOption::CBAutoExposure; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `EnableString` | 9 | Kandidat unbestätigt | `0x00724760` | Aufrufer im Client: AgcmUIOption::CBWater, AgcmUIOption::CBBloom, AgcmUIOption::CBAutoExposure; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetComboButton` | 12 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::OnCommand, AgcmUIManager2::StreamReadCB; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `SetDropDownTexture` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamReadCB |
| `_GetTextureNormal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUICombo::_DrawComboItemList |
| `_GetTextureOn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUICombo::_DrawComboItemList |
| `_GetTextureBottom` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUICombo::_DrawComboItemList |
| `_GetTextureWidth` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_GetTextureHeight` | 7 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::_DrawComboItemList; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `_DrawComboTexture` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUICombo::_DrawComboItemList |
| `_DrawComboItemList` | 42 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `_CalcItemWidth` | 17 | ohne Kandidat |  | Aufrufer im Client: AcUICombo::_DrawComboItemList; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |

## AcUIEdit (Kandidat unbestätigt 10, eingebaut 11, nicht im Client 3, ohne Kandidat 18, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_UpdateScrollBarVert` | 7 | zugeordnet | `0x006FEAE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_DrawCaretComposer` | 45 | zugeordnet | `0x006FDE00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTextMaxLength` | 19 | zugeordnet | `0x006FF450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetMeActiveEdit` | 6 | zugeordnet | `0x006FFBB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckSOL` | 7 | zugeordnet | `0x006FE060` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetHotkey` | 35 | zugeordnet | `0x006FFCB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetHotkey` | 35 | zugeordnet | `0x006FFBD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DrawReadingWindow` | 12 | zugeordnet | `0x006FD730` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnAddImage` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AcUIBase::AddImage, AcUIBase::AddOnlyThisImage, AcUIButton::AddButtonImage |
| `OnPostRender` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcEngine::OnRender, AgcWindow::WindowControlMessageProc |
| `DrawCandidateWindow` | 58 | Kandidat unbestätigt | `0x006FD7FD` | Aufrufer im Client: AcUIChattingEdit::OnWindowRender, AcUIEdit::_DrawCaretComposer; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `OnScrollTop` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnScrollBottom` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckEOL` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIChattingEdit::OnKeyDown, AcUIEdit::_ProcessKeyRight |
| `SetText` | 122 | Kandidat unbestätigt | `0x006FF920` | Aufrufer im Client: CExNPCDialog::OnSetDialogTitle, CExNPCDialog::OnSetDialogMessage, AcUIRecruitWrite::SetWriteWindowInit; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_ParseLine` | 54 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::SetText; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ParseTag` | 56 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::_ParseLine; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `AddStringItem` | 167 | ohne Kandidat |  | Aufrufer im Client: CChattingInputController::OnAddChattingMessage, AcUIEdit::_ParseLine; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `ClearStringInfo` | 28 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::~AcUIEdit, AcUIEdit::SetText, AcUIEdit::ClearText; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `ClearText` | 24 | Kandidat unbestätigt | `0x006FF920` | Aufrufer im Client: CExNPC::_ShowMsgBox, AgcEngine::EditMessageDialog2, AcUIRecruitWrite::SetWriteWindowInit; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetTextStartLine` | 8 | Kandidat unbestätigt | `0x006FF920` | Aufrufer im Client: AgcmUICashMall::CBDisplayProductName, AgcmUICashMall::CBDisplayProductDesc; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetLookLine` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIWarInfo::SetStepMessage, AgcmUIWarInfo::UpdateCenterMessage |
| `ReleaseMeActiveEdit` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcEngine::MouseHandler, AcUIChattingEdit::OnChar, AgcmUIConsole::Off |
| `SetLineDelimiter` | 7 | Kandidat unbestätigt | `0x006FF2C0` | Aufrufer im Client: CExNPCDialog::_MakeExNPCDIalogTextBox, AgcmTitle::_UpdateTitleInfo, AgcmTitle::_UpdateTitleEffect; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetVScroll` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::AddControl; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `GetHotkey` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIHotkey::ReadDefaultHotkeyPack, AgcmUIHotkey::UpdateLastModified, AgcmUIManager2::SetupActions; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `InitFuncPtr` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::AgcmFont, AcUIEdit::AcUIEdit, AgpmCharacter::AgpmCharacter; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `IsDBC_kr` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIEdit::InitFuncPtr |
| `IsDBC_cn` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIEdit::InitFuncPtr |
| `IsDBC_jp` | 7 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `IsDBC_en` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_GetStringWidth` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIEdit::OnWindowRender, AcUIEdit::_DrawStringAlignCenter, AcUIEdit::_DrawStringAlignRight |
| `_GetStringHeight` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIEdit::AddStringItem, AcUIEdit::OnMouseWheel, AcUIEdit::_DrawStringAlignCenter |
| `_GetStringStartPosY` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIEdit::AddStringItem, AcUIEdit::SetLookLine, AcUIEdit::OnMouseWheel |
| `_DrawStringAlignCenter` | 47 | Kandidat unbestätigt | `0x006FE590` | Aufrufer im Client: AcUIEdit::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_DrawStringAlignRight` | 41 | Kandidat unbestätigt | `0x006FE590` | Aufrufer im Client: AcUIEdit::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_DrawStringAlignLeft` | 49 | Kandidat unbestätigt | `0x006FE590` | Aufrufer im Client: AcUIEdit::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_ProcessKeyEnter` | 28 | Kandidat unbestätigt | `0x006FFE50` | Aufrufer im Client: AcUIEdit::OnChar; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_ProcessKeyESC` | 18 | Kandidat unbestätigt | `0x006FFE50` | Aufrufer im Client: AcUIEdit::OnChar; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_ProcessKeyBackSpace` | 37 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnChar; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyTab` | 18 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnChar; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyText` | 61 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnChar; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyLeft` | 61 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyRight` | 51 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyUp` | 69 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyDown` | 70 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_ProcessKeyDelete` | 38 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_UpdateCursorPosition` | 103 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::SetText; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `_CurrentStringParse` | 7 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnLButtonDblClk; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `SetLookEndLine` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIWarInfo::UpdateCenterMessage |

## AcUIEditOKCancelDialog (nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCancelButtonName` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AcUIEditOKDialog (eingebaut 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetButtonName` | 9 | ohne Kandidat |  | Aufrufer im Client: CExNPC::SetMsgBoxButtonName, AgcmUIManager2::StreamReadUIMessage; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `EditControlImage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIControl::_LoadTextureFromINI |

## AcUIEventButton (Kandidat unbestätigt 2, eingebaut 3, gemeinsamer Rumpf 4, nicht im Client 1, ohne Kandidat 1, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DestroyButtonMenu` | 13 | zugeordnet | `0x007673D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddMenuEvent` | 15 | zugeordnet | `0x00767660` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetRButtonClickMenu` | 23 | zugeordnet | `0x00767430` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetCallbackClickEvent` | 3 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDragEvent` | 3 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetFocusEvent` | 3 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackKillFocusEvent` | 3 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `_DrawCustomOnMouse` | 11 | Kandidat unbestätigt | `0x00767360` | Aufrufer im Client: AcUIEventButton::OnWindowRender, AcUIEventButton::_DrawCustomOnClick; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_DrawCustomOnClick` | 9 | Kandidat unbestätigt | `0x00767360` | Aufrufer im Client: AcUIEventButton::OnWindowRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `EditMenuEventName` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ClearMenuEvent` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcUIChatMessage::RefreshTabButton |
| `SetLastClickButton` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::SetLastButton; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `SetFocus` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: CExNPCDialog::OnShowNPCDialog, AgcWindow::UserInputMessageProc, AgcWindow::WindowListUpdate |
| `KillFocus` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcWindow::Close, AgcWindow::AllDeleteChild, AgcWindow::DeleteChild |

## AcUIGacha (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnPostInit` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::WindowControlMessageProc |

## AcUIGrid (Kandidat unbestätigt 5, eingebaut 10, nicht im Client 1, ohne Kandidat 7, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetGridItemClickInfo` | 8 | zugeordnet | `0x0072B6F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetAgpdGridPointer` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::SetControlGrid; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `SetGridItemDrawInfo` | 10 | Kandidat unbestätigt | `0x0072B860` | Aufrufer im Client: AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `UpdateUIGrid` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIGrid::SetAgpdGridPointer, AcUIGrid::SetNowLayer, AcUIGrid::OnCommand |
| `DeleteAllChild` | 24 | ohne Kandidat |  | Aufrufer im Client: AcUIGrid::~AcUIGrid, AcUIGrid::SetAgpdGridPointer, AcUIGrid::OnClose; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `SetGridItemMemory` | 20 | ohne Kandidat |  | Aufrufer im Client: AcUIGrid::SetAgpdGridPointer; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `AddGridItemWindow` | 20 | ohne Kandidat |  | Aufrufer im Client: AcUIGrid::SetAgpdGridPointer; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `GetIndex` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcdCamConstrain_Terrain::bPreChkTerrain, AgcmCharacter::CBSocketOnConnect, AgcmEventNature::SetCharacterPosition; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `GetGridItemWindow` | 10 | Kandidat unbestätigt | `0x0072B5B0` | Aufrufer im Client: AcUIGrid::OnLButtonDown, AcUIGrid::OnRButtonUp; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGridItemWindowByPos` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetGridItemTextureAndInfo` | 34 | ohne Kandidat |  | Aufrufer im Client: AcUIGrid::UpdateUIGrid; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `SetNowLayer` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIEventBank::CBBankUpdateLayer, AgcmUIGuild::CBGuildupdateGuildMarkLayer, AgcmUIGuildWarehouse::CBClickLayer |
| `GetGridRowColumn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIGrid::OnDragDrop, AcUIGrid::OnLButtonDown, AcUIGrid::OnRButtonUp |
| `GetGridRowColumn` | 29 | Kandidat unbestätigt | `0x0072B5B0` | Aufrufer im Client: AcUIGrid::OnDragDrop, AcUIGrid::OnLButtonDown, AcUIGrid::OnRButtonUp; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetGridRowColumn` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIGrid::OnDragDrop, AcUIGrid::OnLButtonDown, AcUIGrid::OnRButtonUp |
| `GetDragDropMessageInfo` | 8 | Kandidat unbestätigt | `0x0072B6D0` | Aufrufer im Client: AgcmUIEventBank::CBBankMoveItem, AgcmUIEventItemConvert::CBAddConvertGridItem, AgcmUIEventItemConvert::CBAddConvertGridItemSocket; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetCopyGridItem` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIGrid::OnCommand; kein unbenannter Kandidat mit Beleg unter 15 unbenannten Funktionen im Klassenbereich |
| `ReleaseCopyGridItem` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIGrid::OnCommand |
| `OnRButtonDown` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AgcSenderWindow::OnRButtonDown |
| `SetClickInfoTargetWindow` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIGridItem::OnLButtonUp |
| `SetReusableDisplayImage` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamReadCB |
| `GetReusableDisplayImage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIGridItem::OnWindowRender, AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamWriteGrid |
| `SetScroll` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIGrid::OnCommand, AgcmUIManager2::AddControl |
| `SetGridItemMovable` | 9 | Kandidat unbestätigt | `0x0072B860` | Aufrufer im Client: AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AcUIGridItem (zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DrawCoolTime` | 97 | zugeordnet | `0x0072BBC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

## AcUIJournal (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetReadImage` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIQuestJournal::OnInit; im Adressbereich der Klasse (0x007677D0–0x007679C0) ist keine unbenannte Funktion mehr übrig |
| `ClearImage` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AcUIToolTip::_InitExitButton; im Adressbereich der Klasse (0x007677D0–0x007679C0) ist keine unbenannte Funktion mehr übrig |

## AcUIList (Kandidat unbestätigt 3, eingebaut 1, gemeinsamer Rumpf 3, nicht im Client 6, ohne Kandidat 7, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetListItemPointer_Index` | 17 | zugeordnet | `0x00729030` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetListItemWindowStartRow` | 24 | zugeordnet | `0x00728FB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetListItemWindowTotalNum` | 20 | zugeordnet | `0x00728F50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetListItemWindowVisibleRow` | 11 | Kandidat unbestätigt | `0x0072B860` | Aufrufer im Client: AgcUIChatMessage::SetListItemMaxCount, AcUIList::SetListItemColumn, AgcmUIManager2::CopyBaseProperty; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetListItemWindowMoveInfo` | 10 | Kandidat unbestätigt | `0x0072B860` | Aufrufer im Client: AgcUIChatMessage::Initialize, AgcUIChatMessage::SetListItemMaxCount, AgcmUIManager2::CopyBaseProperty; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetCallbackConstructor` | 4 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackDestructor` | 4 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRefresh` | 4 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetMemoryppListItem` | 16 | ohne Kandidat |  | Aufrufer im Client: AcUIList::SetListItemWindowVisibleRow; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `NewListItemWidnow` | 35 | ohne Kandidat |  | Aufrufer im Client: AcUIList::RefreshList; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `RefreshListItemWindow` | 32 | ohne Kandidat |  | Aufrufer im Client: AcUIList::RefreshList; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `DeleteListItemWindow` | 11 | ohne Kandidat |  | Aufrufer im Client: AcUIList::DeleteAllListItemInfo; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `SetListInfo_String` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteListInfo_String` | 43 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetListItemInfoString` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteAllListItemInfo` | 28 | ohne Kandidat |  | Aufrufer im Client: AcUIList::~AcUIList, AcUIList::SetListItemWindowVisibleRow, AcUIList::OnClose; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `MoveListItemWindow` | 24 | ohne Kandidat |  | Aufrufer im Client: AcUIList::RefreshList, AcUIList::SetListItemWindowMoveInfo; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GoNextListPage` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GoPreListPage` | 37 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetListItemColumn` | 10 | Kandidat unbestätigt | `0x0072B860` | Aufrufer im Client: AgcUIChatMessage::SetListItemMaxCount, AgcmUIManager2::CopyBaseProperty, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `OnMouseMove` | 27 | ohne Kandidat |  | Aufrufer im Client: AcUIRaider::OnMouseMove, AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `SetSelectedTexture` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SelectItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection, AgcmTitle::CallBack_OnClickCategoryItem |

## AcUIListItem (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_GetTextureByID` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIListItem::OnWindowRender |

## AcUIMenu (eingebaut 2, nicht im Client 7, ohne Kandidat 9, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_RenderMenuBackground` | 139 | zugeordnet | `0x0079C200` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetCurrentEventIndex` | 31 | zugeordnet | `0x0079BD00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetChildMenu` | 6 | zugeordnet | `0x0079BCD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddMenuEvent` | 8 | zugeordnet | `0x0079BFA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_RenderMenuText` | 38 | zugeordnet | `0x0079BA90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Clear` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CharacterConstructor, AgcmCharacter::SetTemplateClumpRenderType, AgcdEffCtrl_Set::~AgcdEffCtrl_Set; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `ClearEvent` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcUIChatMessage::_InitMenuEvent, AcUIEventButton::ClearMenuEvent |
| `TextureClear` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMenuEvent` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIMenu::AddMenuEvent, AcUIMenu::DelMenuEvent, AcUIMenu::DelMenuEvent; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetMenuEvent` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIMenu::AddMenuEvent, AcUIMenu::DelMenuEvent, AcUIMenu::DelMenuEvent; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `DelMenuEvent` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DelMenuEvent` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateChildMenu` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::Initialize; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `DeleteChildMenu` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteChildMenu` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnLButtonDblClk` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AgcSenderWindow::OnLButtonDblClk |
| `_ProcessEvent` | 14 | ohne Kandidat |  | Aufrufer im Client: AcUIChattingEdit::OnChar, AcUIMenu::OnLButtonUp; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `_DrawTextureCorner` | 22 | ohne Kandidat |  | Aufrufer im Client: AcUIMenu::_RenderMenuBackground; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `_DrawTextureBody` | 33 | ohne Kandidat |  | Aufrufer im Client: AcUIMenu::_RenderMenuBackground; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `_DrawTextureSelect` | 20 | ohne Kandidat |  | Aufrufer im Client: AcUIMenu::_RenderMenuBackground; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `EnableEvent` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EnableEvent` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_SetBackImage` | 14 | ohne Kandidat |  | Aufrufer im Client: AcUIMenu::Initialize; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |

## AcUIMessageDialog (ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnCommand` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::WindowControlMessageProc, AcUICombo::OnCommand, AcUIEdit::OnCommand; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `SetButtonName` | 9 | ohne Kandidat |  | Aufrufer im Client: CExNPC::SetMsgBoxButtonName, AgcmUIManager2::StreamReadUIMessage; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |

## AcUIMinimap (eingebaut 4, ohne Kandidat 6, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RenderCursor` | 111 | zugeordnet | `0x0078C7A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderRegisterPos` | 73 | zugeordnet | `0x0078DCD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DestroyMapPosition` | 68 | zugeordnet | `0x0078DA90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderMinimap` | 96 | zugeordnet | `0x0078D350` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderDisplayPopup` | 83 | zugeordnet | `0x0078DF50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RenderDisplayRegisterPopup` | 86 | zugeordnet | `0x0078D730` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RenderETC` | 112 | zugeordnet | `0x0078D4B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RenderPartyMember` | 65 | zugeordnet | `0x0078CFD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnClose` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcWindow::Close, AcUIBbs::OnClose, AcUIBbsContent::OnClose |
| `RenderDivision` | 70 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::RenderMinimap; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `PositionUpdate` | 7 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::MapEnlargement, AcUIMinimap::MapReduction, AgcmMinimap::CBSelfCharacterPositionCallback; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `_RenderCameraClear` | 23 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::_RenderCameraCreate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `_RenderCameraCreate` | 34 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::OnInit, AcUIMinimap::MapEnlargement, AcUIMinimap::MapReduction; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MapEnlargement` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::CBClickPlusButton; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `MapReduction` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::CBClickMinusButton; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `GetTextureSize` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIMinimap::RenderMinimap, AcUIMinimap::RenderDivision, AcUIMinimap::_RenderCameraCreate |
| `GetMMPos` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIMinimap::RenderDivision, AcUIMinimap::PositionUpdate, AcUIMinimap::DestroyMapPosition |
| `GetMMPosINV` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIMinimap::OnLButtonDown, AcUIMinimap::OnRButtonUp, AcUIMinimap::OnRButtonDblClk |

## AcUIModalImage (eingebaut 4, nicht im Client 1, ohne Kandidat 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddImage` | 21 | zugeordnet | `0x0074FF90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddOnlyThisImage` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap, AcUIBase::AddOnlyThisImage, AgcUIEffect::SetEffectImage; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `GetImage` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnPostRender` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcEngine::OnRender, AgcWindow::WindowControlMessageProc |
| `OnLButtonDown` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CExNPCDialogButton::OnLButtonDown, AcUIRaider::OnLButtonDown, AgcWindow::UserInputMessageProc |
| `OnMouseMove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIRaider::OnMouseMove, AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc |
| `DestroyTextureList` | 12 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::~AcUIBase, AcUIBase::DestroyImage, AcUIBase::OnClose; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `OnAddImage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBase::AddImage, AcUIBase::AddOnlyThisImage, AcUIButton::AddButtonImage |

## AcUIOKCancelDialog (ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnKeyDown` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `SetButtonName` | 18 | ohne Kandidat |  | Aufrufer im Client: CExNPC::SetMsgBoxButtonName, AgcmUIManager2::StreamReadUIMessage; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |

## AcUIRaider (eingebaut 1, gemeinsamer Rumpf 1, nicht im Client 2, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_TargetRenderTexture` | 75 | zugeordnet | `0x0078CB30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_RenderCharacter` | 52 | zugeordnet | `0x0078C580` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_CharacterType` | 39 | zugeordnet | `0x0078C410` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnRButtonUp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage |
| `RaiderPositionUpdate` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::CBSelfCharacterPositionCallback; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `OnIdle` | 17 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `_RenderCameraCreate` | 33 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::OnInit, AcUIMinimap::MapEnlargement, AcUIMinimap::MapReduction; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_RenderRaider` | 83 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_RenderMap` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AcUIRecruit (nicht als eigene Funktion 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ChildControlInit` | 80 | zugeordnet | `0x0078FC90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetBbsMode` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AcUIRecruit::OnCommand; im Adressbereich der Klasse (0x0078FC90–0x0078FF50) ist keine unbenannte Funktion mehr übrig |
| `GetClassSelectInfo` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AcUIRecruit::OnCommand; im Adressbereich der Klasse (0x0078FC90–0x0078FF50) ist keine unbenannte Funktion mehr übrig |

## AcUIRecruitWrite (eingebaut 3, nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetWriteWindowInit` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetWriteWindowClose` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnLButtonDown` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CExNPCDialogButton::OnLButtonDown, AcUIRaider::OnLButtonDown, AgcWindow::UserInputMessageProc |
| `SetNextEdit` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIRecruitWrite::OnCommand |
| `SetModulePointer` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRecruit::OnAddModule |
| `OnClickWriteButton` | 36 | ohne Kandidat |  | Aufrufer im Client: AcUIRecruitWrite::OnCommand; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AcUIScroll (Kandidat unbestätigt 2, eingebaut 3, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CalcScrollValue` | 30 | zugeordnet | `0x007261D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetScrollValue` | 32 | zugeordnet | `0x00725DB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetRefreshCallback` | 6 | zugeordnet | `0x00726040` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetScrollButtonInfo` | 16 | Kandidat unbestätigt | `0x007270E0` | Aufrufer im Client: AgcUIChatMessage::Initialize, AgcUIChatMessage::RefreshScroll, AcUIList::UpdateScroll; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetScrollButton` | 19 | Kandidat unbestätigt | `0x007270E0` | Aufrufer im Client: AgcUIChatMessage::Initialize, AcUIScroll::OnCommand, AgcmUIManager2::CopyBaseProperty; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetScrollUpButton` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcUIChatMessage::Initialize, AcUIScroll::OnCommand, AgcmUIManager2::CopyBaseProperty |
| `SetScrollDownButton` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcUIChatMessage::Initialize, AcUIScroll::OnCommand, AgcmUIManager2::CopyBaseProperty |
| `GetScrollValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChatting::CBScrollMove, AgcUIChatMessage::RefreshList, AgcUIChatMessage::RefreshScroll |

## AcUISkillTree (eingebaut 2, nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetSkillBackImage` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::StreamReadCB |
| `GetSkillBackImage` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUISkillTree::_MoveGridSkill, AcUISkillTree::_MoveGridSkillOneLineMode, AgcmUIManager2::StreamWriteSkillTree |
| `_MoveGridSkill` | 40 | nicht als eigene Funktion |  | Aufrufer im Client: AcUISkillTree::MoveGridItemWindow; im Adressbereich der Klasse (0x00732030–0x00732060) ist keine unbenannte Funktion mehr übrig |
| `_MoveGridSkillOneLineMode` | 48 | nicht als eigene Funktion |  | Aufrufer im Client: AcUISkillTree::MoveGridItemWindow; im Adressbereich der Klasse (0x00732030–0x00732060) ist keine unbenannte Funktion mehr übrig |
| `_UpdateSkillTreeSize` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AcUISkillTree::MoveGridItemWindow; im Adressbereich der Klasse (0x00732030–0x00732060) ist keine unbenannte Funktion mehr übrig |

## AcUITexture (eingebaut 3, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetTexture` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCustomizeRender::DrawQuad, AgcmEventNature::CreateSkyAtomic, AgcmEventNature::CreateCloudAtomic |
| `SetAlphaValue` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetColorValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIGridItem::OnWindowRender, AgcmUIGuild::SetPreviewGuildMark, AgcmUIGuild::GuildMarkDraw |
| `GetTexturePointer` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIGrid::OnWindowRender, AcUIGrid::SetCopyGridItem |

## AcUIToolTip (Kandidat unbestätigt 4, eingebaut 2, ohne Kandidat 11, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_InitExitButton` | 18 | zugeordnet | `0x007239B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawToolTipBox` | 49 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `SetBoxIm2D` | 7 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::_DrawToolTipBoxBody, AcUIToolTip::_DrawToolTipBoxCorner, AcUIToolTip::_DrawToolTipBoxEdge; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `SetBoxIm2D2` | 7 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::_DrawToolTipBoxEdge; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `AddString` | 46 | Kandidat unbestätigt | `0x00724220` | Aufrufer im Client: AgcmAICharItemDialog::OnInitDialog, AgcmAIDialog::OnInitDialog, AgcmAIScreamEditDlg::OnInitDialog; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddToolTipTexture` | 23 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::SetItemConvertIcon; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `AddNewLine` | 10 | Kandidat unbestätigt | `0x00724220` | Aufrufer im Client: AgcmUIItem::_SetItemToolTipDetailType, AgcmUIItem::_SetItemToolTipDetailRank, AgcmUIItem::_SetItemToolTipDetailRequireLevel; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DeleteAllStringInfo` | 23 | Kandidat unbestätigt | `0x00724220` | Aufrufer im Client: AcUIToolTip::OnClose, AgcmUIItem::CBCloseAllUIToolTip, AgcmUIItem::OpenToolTip; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_GetRasterVoidPtr` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIToolTip::_DrawToolTipBoxBody, AcUIToolTip::_DrawToolTipBoxCorner, AcUIToolTip::_DrawToolTipBoxEdge |
| `_DrawToolTipBoxBody` | 29 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::DrawToolTipBox; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `_DrawToolTipBoxCorner` | 22 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::DrawToolTipBox; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `_DrawToolTipBoxEdge` | 34 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::DrawToolTipBox; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `SetMoveWindow` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIItem::AddTooltipRegisterItem |
| `EnableExitButton` | 18 | Kandidat unbestätigt | `0x00723DA0` | Aufrufer im Client: AgcmUIItem::AddTooltipRegisterItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_UpdateExitButtonPosition` | 14 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `CBTooltipExit` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::_InitExitButton; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `_DrawLine` | 10 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::DrawToolTipBox; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `GetRenderPos` | 70 | ohne Kandidat |  | Aufrufer im Client: AcUIToolTip::DrawToolTipBox, AcUIToolTip::DrawItemInfo, AgcmUIItem::OpenToolTip; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |

## AcUITree (eingebaut 1, ohne Kandidat 1, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OpenItem` | 21 | zugeordnet | `0x007308E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateStartRow` | 32 | zugeordnet | `0x00730780` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemDepth` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RefreshControl; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetTreeItemInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUITree::OnNewListItem, AcUITree::OnChangeTotalNum, AcUITree::IsValidListItem |

## AcUITreeItem (Kandidat unbestätigt 2, eingebaut 1, nicht im Client 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RefreshItem` | 22 | zugeordnet | `0x00730410` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTreeInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUITree::OnChangeTotalNum, AcUITree::IsValidListItem, AcUITreeItem::AcUITreeItem |
| `SetTreeButton` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTreeButtonClose` | 19 | Kandidat unbestätigt | `0x00730390` | Aufrufer im Client: AcUITreeItem::SetTreeButton, AgcmUIManager2::CBListItemConstructor, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetTreeButtonOpen` | 19 | Kandidat unbestätigt | `0x00730390` | Aufrufer im Client: AcUITreeItem::SetTreeButton, AgcmUIManager2::CBListItemConstructor, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AcuBlur (nicht als eigene Funktion 7, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CreateTextureCamera` | 56 | nicht als eigene Funktion |  | Aufrufer im Client: AcuBlur::PShaderOpen; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `PShaderOpen` | 63 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmGlare::OnInit; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `BoxFilterSetup` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AcuBlur::Blur; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `VBoxFilterSetup` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AcuBlur::Blur; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `HBoxFilterSetup` | 24 | nicht als eigene Funktion |  | Aufrufer im Client: AcuBlur::Blur; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `Blur` | 91 | nicht als eigene Funktion |  | Aufrufer im Client: AcuBlur::MakeBlur; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `PShaderClose` | 50 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmGlare::OnDestroy; im Adressbereich der Klasse (0x0076C0A0–0x0076C0A0) ist keine unbenannte Funktion mehr übrig |
| `MakeBlur` | 43 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AcuTextureList (Kandidat unbestätigt 3, eingebaut 2, nicht im Client 5, ohne Kandidat 7, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddOnlyThisImage` | 25 | zugeordnet | `0x0072DF20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ApplyRatio` | 22 | zugeordnet | `0x0072D490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddImage` | 38 | zugeordnet | `0x0072D760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddTexture` | 11 | zugeordnet | `0x0072DB50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DeleteImage_ID` | 27 | zugeordnet | `0x0072DD60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetImage_ID` | 19 | Kandidat unbestätigt | `0x0072DD00` | Aufrufer im Client: AcUIBar::_GetBodyTexture, AcUIBar::_GetEdgeTexture, AcUIBase::AddImage; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetImageName_ID` | 18 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::RenderTexture; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `GetImage_Index` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetImage_Index` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetImageName_Index` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetImage_ID` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetImageID_Name` | 34 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamReadCB; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `DestroyTextureList` | 17 | Kandidat unbestätigt | `0x0072DD00` | Aufrufer im Client: AcUIBase::~AcUIBase, AcUIBase::DestroyImage, AcUIBase::OnClose; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcmEventNature::LoadTextureScriptFile, CUiExNPCMsgBoxGrid::OnWindowRender |
| `GetHeadTextureListInfo` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIBbs::OnWindowRender, AcUIBbsContent::OnWindowRender, AcUICheckBox::OnWindowRender |
| `DeleteImage_Index` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetImageName_Index` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamWriteBase; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `LoadTextures` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::SetGrouping, AgcmUIManager2::OpenUI; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `LoadTexture` | 41 | Kandidat unbestätigt | `0x0072D640` | Aufrufer im Client: AgcmEventNature::GetTexture, AgcmItem::GetTexture, AcTextureList::GetTexture; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `UnloadTextures` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::CloseUI; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `_SafeReleaseTexture` | 12 | ohne Kandidat |  | Aufrufer im Client: AcuTextureList::SetImage_Index, AcuTextureList::SetImage_ID, AcuTextureList::SetImageID_Name; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |
| `_ParseTextureFileName` | 31 | ohne Kandidat |  | Aufrufer im Client: AcuTextureList::LoadTexture; kein unbenannter Kandidat mit Beleg unter 20 unbenannten Funktionen im Klassenbereich |

## AgcAuth (eingebaut 2, nicht im Client 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `init` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIQuestJournal::OnInit, AgcmUIConsole::OnInit, AgpmCharacter::CreateCharacter |
| `init` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIQuestJournal::OnInit, AgcmUIConsole::OnInit, AgpmCharacter::CreateCharacter |
| `final_process` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `setProperty_impl` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `setProperty_impl` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `setProperty_impl` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcChatManager (Kandidat unbestätigt 3, eingebaut 1, nicht im Client 3, ohne Kandidat 11, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_ItemEvent` | 20 | zugeordnet | `0x0070C7B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ParseMessageText` | 22 | zugeordnet | `0x0070C920` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_AddOptionTab` | 13 | zugeordnet | `0x0070CE90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `HideChatUI` | 16 | zugeordnet | `0x0070E220` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadBaseFile` | 93 | zugeordnet | `0x0070ECF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ShowChatUI` | 19 | zugeordnet | `0x0070CC30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_WhisperEvent` | 27 | zugeordnet | `0x0070C9C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_MapPosEvent` | 16 | zugeordnet | `0x0070C820` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddUIChatMessage` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::_LoadChatSetting, AgcChatManager::_DefaultChatSetting, AgcChatManager::CBDragCallback; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `DestroyUIChatMessage` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::ChatIdle, AgcChatManager::_LoadChatSetting, AgcChatManager::_DefaultChatSetting; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `SaveChatFile` | 81 | Kandidat unbestätigt | `0x0070D8E0` | Aufrufer im Client: AgcChatManager::ChatIdle; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 13, Belegarten 3) |
| `OnCollectControls` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::OnAddMessage, AgcmUIChatting2::CBSetSelfCharacter; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `_LoadChatSetting` | 44 | Kandidat unbestätigt | `0x0070F210` | Aufrufer im Client: AgcChatManager::LoadChatFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_DefaultChatSetting` | 57 | Kandidat unbestätigt | `0x0070F210` | Aufrufer im Client: AgcChatManager::LoadChatFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `GetChatMessage` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::InitMessageInstance; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `GetUIChatMessage` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::_LoadChatSetting, AgcChatManager::_DefaultChatSetting; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `AllForceDetailShow` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AllForceDetailHide` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AllShowChatUI` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBEnterGameEnd; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `AllHideChatUI` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBReturnLoginCharacterSelectMode; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `AllClearChatUI` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::LoadChatFile; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `AllClearMessage` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILogin::CBReturnLoginCharacterSelectMode |
| `SetEmptyUIData` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::ChatIdle; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `GetEmptyUIData` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::SetEmptyUIData; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `_EditOptionTab` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::CBOptionOK; kein unbenannter Kandidat mit Beleg unter 1301 unbenannten Funktionen im Klassenbereich |
| `OnAddNoticeMessage` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcChatMessage (Kandidat unbestätigt 1, eingebaut 6, ohne Kandidat 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SliceLineByWord` | 22 | zugeordnet | `0x007A0100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Initialize` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit |
| `Clear` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CharacterConstructor, AgcmCharacter::SetTemplateClumpRenderType, AgcdEffCtrl_Set::~AgcdEffCtrl_Set |
| `GetMessage` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcChatMessage::PopNewMessage, AgcUIChatMessage::_RefreshMessage, SplashWindow::run; kein unbenannter Kandidat mit Beleg unter 39 unbenannten Funktionen im Klassenbereich |
| `GetMessageCount` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcUIChatMessage::_RefreshMessage |
| `ClearMessage` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcChatMessage::Clear |
| `GetTextFormat` | 10 | Kandidat unbestätigt | `0x007A1550` | Aufrufer im Client: AgcChatMessage::AddMessage, AgcChatMessage::RefreshMessageEntry; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `PushNewMessage` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcChatMessage::_PushAndParseString |
| `PopNewMessage` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::AddMessage; kein unbenannter Kandidat mit Beleg unter 39 unbenannten Funktionen im Klassenbereich |
| `ClearOriginalMessage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatManager::AllClearMessage, AgcChatMessage::ClearMessage |

## AgcConsole (eingebaut 4, gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnKeyUp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage |
| `isVisibleLine` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcConsole::render |
| `registerServerKeyword` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIConsole::CBRegisterServerKeyword |
| `setCallbackPtr` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIConsole::AgcmUIConsole |

## AgcDebugWindow (eingebaut 1, gemeinsamer Rumpf 1, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 6 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnKeyUp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage |
| `RenderProfile` | 197 | nicht als eigene Funktion |  | Aufrufer im Client: AgcDebugWindow::OnWindowRender; im Adressbereich der Klasse (0x0076AB70–0x0076BC40) ist keine unbenannte Funktion mehr übrig |
| `FindMaxItem` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcDebugWindow::RenderProfile; im Adressbereich der Klasse (0x0076AB70–0x0076BC40) ist keine unbenannte Funktion mehr übrig |

## AgcEngine (Kandidat unbestätigt 7, eingebaut 11, gemeinsamer Rumpf 1, nicht im Client 10, ohne Kandidat 26, zugeordnet 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Draw2DPanel` | 89 | zugeordnet | `0x00597F70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetWideScreen` | 6 | zugeordnet | `0x00599A70` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MouseHandler` | 82 | zugeordnet | `0x00599FD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawIm2DPixelRaster` | 65 | zugeordnet | `0x00599240` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetProjection` | 45 | zugeordnet | `0x005988E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawRwTexture` | 35 | zugeordnet | `0x00597E40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReleaseMeActiveEdit` | 29 | zugeordnet | `0x00597C90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetMeActiveEdit` | 26 | zugeordnet | `0x00597BE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ProcessIdleLuaCommand` | 42 | zugeordnet | `0x0059A7A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RegisterModule` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnInitialize` | 15 | Kandidat unbestätigt | `0x004DEDB0` | Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIAccountCheck::AgcmUIAccountCheck, AgcmUIAccountCheck::~AgcmUIAccountCheck; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `OnInitialize3D` | 110 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnMessageSink; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OnTerminate` | 36 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIAccountCheck::CB_OnConnect; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OnRender` | 151 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnIdle, AgcWindow::WindowControlMessageProc, AgcmUILogin::CBLoginMainCreateButtonClick; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OnAttachInputDevices` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcEngine::OnMessageSink |
| `OnCameraResize` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnMessageSink; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OnDestroyCamera` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnTerminate; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `CreateCamera` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmCustomizeRender::Start, AgcEngine::OnCreateCamera; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `CreateWorld` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcEngine::OnCreateWorld |
| `CreateLights` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnCreateLight; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `DestroyLights` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnDestroyLight; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `KeyboardHandler` | 153 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnAttachInputDevices; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `AddChild` | 16 | Kandidat unbestätigt | `0x004EFB80` | Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogTitleBar, CExNPCDialog::_MakeExNPCDIalogTextBox, CExNPCDialog::_MakeExNPCDIalogBtnClose; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CloseWindowUIModule` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetFullUIModule` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnInitialize3D; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `SetTickCount` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcEngine::OnIdle, AgcEngine::OnMessageSink |
| `OnCreateWorld` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::OnInitialize3D |
| `OnCreateCamera` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::OnInitialize3D |
| `OnDestroyLight` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::OnTerminate |
| `SetActivate` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnMessageSink; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `GetActivate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::KeyboardIdleProcess, AgcmUIMain::OnIdle, AgcUIManager::UpdateCameraViewProcess |
| `EditMessageDialog2` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::ActionMessageEditOKDialog2; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OkCancelDialog` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::ActionMessageOKCancelDialog; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OkCancelDialog2` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::ActionMessageOKCancelDialog2; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `ThreeBtnDialog` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::ActionMessageThreeBtnDialog; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `SetSoundAlertMSGFile` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetWorldCameraFarClipPlane` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::SetSkyRadius, AgcmEventNature::SetSkyRadius; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `SetWorldCameraNearClipPlane` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::SetSkyRadius, AgcmEventNature::SetSkyRadius; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `SetWorldCameraViewWindow` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindTextureDirectory` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnCameraStateChange` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnInitialize3D, AgcEngine::OnCameraResize, AgcEngine::SetActivate; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `DrawIm2D` | 92 | Kandidat unbestätigt | `0x00598980` | Aufrufer im Client: CUiGridSlot::OnWindowRender, AgcmUIWorldmap::RenderButton, AGUIDrawMark::Render; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DrawIm2DRotate` | 40 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::RenderCursor, AGUIDrawMark::Render; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `GetWorldPosToScreenPos` | 12 | Kandidat unbestätigt | `0x004C9CA0` | Aufrufer im Client: AgcmGlare::CBPostRender, AgcmGrass::CB_GRASS_RENDER, AgcmLensFlare::OnIdle; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DrawIm2DInWorld` | 8 | Kandidat unbestätigt | `0x00598700` | Aufrufer im Client: AgcmIDBoard::_DrawGoMark, AgcmIDBoard::_DrawFlag, AgcmIDBoard::_DrawGuildCompetition; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DrawIm2DInWorld` | 51 | Kandidat unbestätigt | `0x00598700` | Aufrufer im Client: AgcmIDBoard::_DrawGoMark, AgcmIDBoard::_DrawFlag, AgcmIDBoard::_DrawGuildCompetition; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DrawIm2DInWorld2` | 53 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackSetCursorMousePosition` | 3 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `DrawIm2DPixel` | 175 | Kandidat unbestätigt | `0x00598980` | Aufrufer im Client: AcUIRaider::_RenderCharacter, AcUIRaider::_RenderMap, AcUIBar::_DrawTexture; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DrawIm2DPixelMask` | 142 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::OnWindowRender; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `OnSelectDevice` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIOption::Update3DProvider, AgcmUIOption::LoadFromINI |
| `ScreenShotSave` | 134 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveToBmp` | 222 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::ScreenShotSave; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `ProcessDeleteWindow` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnTerminate, AgcEngine::OnIdle; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `Lua_RunScript` | 55 | ohne Kandidat |  | Aufrufer im Client: CChatCmd::CallBack_OnScriptLua; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `Lua_IsRunning` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Lua_EnQueue` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcEngine::Lua_RunScript |
| `Lua_PushWait` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Lua_Flush_Queue` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcEngine::KeyboardHandler, AgcEngine::Lua_RunScript, AgcEngine::ProcessIdleLuaCommand |
| `LuaErrorHandler` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcEngine::LuaInitialize |
| `Debug_Idle` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnIdle; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `Debug_Idle2` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnIdle; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |
| `GetVideoMemoryState` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `InitRatio` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnInitialize3D; kein unbenannter Kandidat mit Beleg unter 3881 unbenannten Funktionen im Klassenbereich |

## AgcGPAuth (nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `init` | 72 | ohne Kandidat |  | Aufrufer im Client: AgcAuth::init, AgcmUIQuestJournal::OnInit, AgcmUIConsole::OnInit; kein unbenannter Kandidat mit Beleg unter 1819 unbenannten Funktionen im Klassenbereich |
| `error_handling` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `final_process` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcModalWindow (ohne Kandidat 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `EndDialog` | 18 | zugeordnet | `0x005FDC20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DoModal` | 60 | ohne Kandidat |  | Aufrufer im Client: AgcmAIDialog::OnAIEditCondition, AgcmAIDialog::OnAiUseitem, AgcmAIDialog::OnAiScream; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |

## AgcModule (eingebaut 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `LockRender` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::OnReceive, AgcmResourceLoader::InstanceAtomic, AgcmShadow2::ShadowTextureRender |
| `UnlockRender` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::OnReceive, AgcmResourceLoader::InstanceAtomic, AgcmShadow2::ShadowTextureRender |
| `LockFrame` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCamera2::bGetPtrCX, AgcmCamera2::bGetPtrCY, AgcmCamera2::bGetPtrCZ |
| `UnlockFrame` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCamera2::bGetPtrCX, AgcmCamera2::bGetPtrCY, AgcmCamera2::bGetPtrCZ |

## AgcSenderWindow (eingebaut 1, gemeinsamer Rumpf 1, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnRButtonDown` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage |
| `OnKeyDown` | 45 | nicht als eigene Funktion |  | Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage; im Adressbereich der Klasse (0x00751B10–0x00751C00) ist keine unbenannte Funktion mehr übrig |

## AgcTipWindow (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcUIChatMessage (eingebaut 7, nicht im Client 10, ohne Kandidat 3, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_RefreshMessage` | 34 | zugeordnet | `0x00739830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTab` | 14 | zugeordnet | `0x00735660` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTabCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatManager::SaveChatFile, AgcChatManager::_CombineDockingUI, AgcChatManager::CBOptionOK |
| `IsUseMessageType` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMessageInstance` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMessageInstanceCount` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyMessageInstance` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyMessageInstance` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AllDestroyMessageInstance` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ForceDetailShow` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcChatManager::AllForceDetailShow |
| `ForceDetailHide` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcChatManager::AllForceDetailHide |
| `_InitUIList` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_InitUIScroll` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_InitUITab` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_GetUsingMessage` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::RefreshList; kein unbenannter Kandidat mit Beleg unter 52 unbenannten Funktionen im Klassenbereich |
| `CBMenuEventDocking` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBMenuEventTabEnable` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::_InitMenuEvent; kein unbenannter Kandidat mit Beleg unter 52 unbenannten Funktionen im Klassenbereich |
| `SetLastButton` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcChatManager::CBDragCallback |
| `SetScrollValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChannel::CBDisplayChatList, AgcChatManager::ShowChatUI, AgcUIChatMessage::RefreshScroll |
| `GetScrollValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChatting::CBScrollMove, AgcUIChatMessage::RefreshList, AgcUIChatMessage::RefreshScroll |
| `IsUsableType` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcChatManager::OnAddMessage |
| `GetChatMessage` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcUIChatMessage::InitMessageInstance; kein unbenannter Kandidat mit Beleg unter 52 unbenannten Funktionen im Klassenbereich |

## AgcUIEffect (Kandidat unbestätigt 5, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetEffectFade` | 12 | zugeordnet | `0x00731900` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetEffectImage` | 27 | zugeordnet | `0x00731820` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetEffectText` | 14 | Kandidat unbestätigt | `0x00731970` | Aufrufer im Client: AgcmBattleGround::_BattleGroundEffectText, AgcmBattleGround::_EpicZoneEffectText, AgcmShrine::CBReadyToStart; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `SetEffectSubText` | 11 | Kandidat unbestätigt | `0x00731970` | Aufrufer im Client: AgcmUIArchlord::SetTextEffect, CBGMTitleViewer::OnUpdateBGMTitle, AgcmUIGuild::DrawBattleInfoInit; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetEffectSubText` | 22 | Kandidat unbestätigt | `0x00731970` | Aufrufer im Client: AgcmUIArchlord::SetTextEffect, CBGMTitleViewer::OnUpdateBGMTitle, AgcmUIGuild::DrawBattleInfoInit; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `SetEffectAboveText` | 11 | Kandidat unbestätigt | `0x00731970` | Aufrufer im Client: AgcmUIArchlord::SetTextEffect, AgcmUIGuild::DrawBattleInfoInit, AgcmUIGuild::DrawBattleInfoResult; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetEffectBG` | 16 | Kandidat unbestätigt | `0x00731A40` | Aufrufer im Client: AgcmUIArchlord::SetTextEffect; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |

## AgcUIManager (eingebaut 5, ohne Kandidat 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `UpdateCameraViewProcess` | 93 | zugeordnet | `0x0072E910` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnKeyDown` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `OnKeyUp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AcUIBase::PreTranslateInputMessage |
| `OnLButtonUp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIRaider::OnLButtonUp, AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc |
| `OnMButtonUp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcWindow::UserInputMessageProc |
| `SetAgcmCameraModule` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::OnAddModule |
| `SetAgcmCharacterModule` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIManager2::OnAddModule |
| `OnLButtonDblClk` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AgcSenderWindow::OnLButtonDblClk; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetCameraViewProcessHotkeys` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::SetUIMgrProcessHotkeys, AgcUIManager::UpdateCameraViewProcess; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcUIQuestText (eingebaut 3, nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DelQuestItemInfo` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetQuestItemInfo` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcUIQuestText::CBOpenQuestItemTooltip |
| `ClearQuestItemInfo` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `HexStringToDWORD` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcUIQuestText::MakeTextList; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CloseQuestItemTooltip` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcUIQuestText::CBCloseQuestItemTooltip |
| `ClearClickSelectButton` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcUIQuestText::ClearTextList |

## AgcUIWindow (eingebaut 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnLButtonDblClk` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::UserInputMessageProc, AgcWindow::WindowControlMessageProc, AgcSenderWindow::OnLButtonDblClk; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetUIDepth` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcUIWindow::OnMoveWindow |
| `GetUIDepthRecurse` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcUIWindow::GetUIDepth; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcWindow (Kandidat unbestätigt 11, eingebaut 10, nicht im Client 6, ohne Kandidat 9, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `MovableOn` | 13 | zugeordnet | `0x005FC640` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Close` | 18 | Kandidat unbestätigt | `0x0074C820` | Aufrufer im Client: AgcmCharacter::CBSocketOnError, AgcmLogin::CBSocketError, AgcWindow::WindowControlMessageProc; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `MessagePush` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcWindow::PostMessage |
| `MessageUpdate` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::MessageQueueProcessing; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `ClientToScreen` | 10 | Kandidat unbestätigt | `0x0072DA50` | Aufrufer im Client: CUiExNPCMsgBoxGrid::OnWindowRender, AcUIMinimap::OnWindowRender, AcUIMinimap::RenderCursor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ClientToScreen` | 15 | Kandidat unbestätigt | `0x0072D8F0` | Aufrufer im Client: CUiExNPCMsgBoxGrid::OnWindowRender, AcUIMinimap::OnWindowRender, AcUIMinimap::RenderCursor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ScreenToClient` | 10 | Kandidat unbestätigt | `0x005FC510` | Aufrufer im Client: AgcWindow::UserInputMessageProc, AcUIBase::PreTranslateInputMessage, AcUIBase::OnDragDrop; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ScreenToClient` | 10 | Kandidat unbestätigt | `0x005FC510` | Aufrufer im Client: AgcWindow::UserInputMessageProc, AcUIBase::PreTranslateInputMessage, AcUIBase::OnDragDrop; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddChild` | 55 | Kandidat unbestätigt | `0x00766ED0` | Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogTitleBar, CExNPCDialog::_MakeExNPCDIalogTextBox, CExNPCDialog::_MakeExNPCDIalogBtnClose; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ReculsiveWindowControlMessageProc` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::AddChild; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `WindowListUnlink` | 48 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::WindowListUpdate; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `WindowListLinkTail` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::AddChild, AgcWindow::WindowListUpdate, AgcWindow::SetFocus; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `WindowListLinkBefore` | 36 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::WindowListUpdate; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `AllDeleteChild` | 50 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcUIChatMessage::ClearUI, AgcUIChatMessage::AllDeleteListItem, AgcmUINotice::_ClearChildWindow; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DeleteChild` | 54 | Kandidat unbestätigt | `0x00725CD0` | Aufrufer im Client: CExNPCDialog::_DeleteExNPCDialogButton, AgcModalWindow::EndDialog, AgcmTargeting::OnDestroy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `DeleteChild` | 55 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: CExNPCDialog::_DeleteExNPCDialogButton, AgcModalWindow::EndDialog, AgcmTargeting::OnDestroy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetDepth` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AuRwImage::CreateSubImage, AgcmHPBar::SetData, AgcmHPBar::_HPBarUpdate |
| `GetDepthRecurse` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::GetDepth; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `MoveWindow` | 14 | Kandidat unbestätigt | `0x00766ED0` | Aufrufer im Client: CExNPC::OnInitNPCMsgBox, CExNPCDialog::_MakeExNPCDialogBase, CExNPCDialog::_MakeExNPCDialogTitleBar; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `WindowListUpdate` | 172 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcEngine::OnTerminate, AgcEngine::OnIdle, AgcmTargeting::OnDestroy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `MessageQueueProcessing` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MousePositionToUVCoordinate` | 37 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PostMessage` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcWindow::KillFocus, AuInputComposer::OnNotify |
| `SendMessage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChatting::CBScrollUp, AgcmUIChatting::CBScrollDown, AgcmUIChatting::CBScrollHome |
| `HasChild` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsFocused` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AcUIEditOKDialog::OnKeyDown |
| `KillFocus` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::Close, AgcWindow::AllDeleteChild, AgcWindow::DeleteChild; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `GetFocusedWindow` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `WindowFromPoint` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcEngine::OnIdle, AcUIGridItem::OnLButtonUp; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |
| `SetModal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatManager::CBDragCallback, AgcUIChatMessage::SetLastButton, AcUICombo::OpenComboControl |
| `ReleaseModal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatManager::CBDragCallback, AcUICombo::CloseComboControl, AcUIEventButton::OnLButtonUp |
| `MovableOff` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AcUIBase::OnLButtonUp, AcUIBase::OnLButtonUpForHandler, AcUIGridItem::OnLButtonUp |
| `BeInWindowRect` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetDockingCallback` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcChatManager::CreateUIChatMessage, AgcUIChatMessage::Initialize, AgcUIChatMessage::RefreshTabButton |
| `SetDockingPreCallback` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcChatManager::CreateUIChatMessage |
| `UpdateClippingRectParent` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateClippingRect` | 47 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::WindowRender, AgcWindow::UpdateClippingRectParent; kein unbenannter Kandidat mit Beleg unter 3584 unbenannten Funktionen im Klassenbereich |

## AgcaAnimation2 (Kandidat unbestätigt 5, eingebaut 1, nicht im Client 3, ohne Kandidat 6, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetAttachedData` | 20 | zugeordnet | `0x007015B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRtAnim` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcaAnimation2::GetRtAnim; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `GetRtAnim` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcaAnimation2::ReadRtAnim; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `CreateAnimData` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcaAnimation2::AddAnimData, AgcaAnimation2::AddAnimation; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `AddAnimData` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CopyAnimAttachedData, AgcmCharacter::AnimationStreamReadCB; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `AddAnimation` | 22 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcaAnimation2::CopyAnimation, AgcmCharacter::AnimationStreamReadCB, AgcmObject::ObjectTemplateGroupStreamRead; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddAnimation` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcaAnimation2::CopyAnimation, AgcmCharacter::AnimationStreamReadCB, AgcmObject::ObjectTemplateGroupStreamRead |
| `CopyAnimation` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyAnimData` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcaAnimation2::RemoveAnimData, AgcaAnimation2::RemoveAnimation, AgcaAnimation2::RemoveAllAnimation; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `RemoveAnimData` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::DeleteTemplateAnimation, AgcmCharacter::CopyAnimAttachedData; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `RemoveAnimation` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveAllAnimation` | 23 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcmCharacter::DeleteTemplateAnimation, AgcmObject::LoadTemplateData, AgcmObject::RemoveObjectTemplateGroupData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAnimData` | 17 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcmCharacter::GetAnimDuration, AgcmCharacter::AnimationStreamReadCB, AgcmEventEffect::StreamReadCharacterAnimationAttachedData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAnimDataIndex` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddFlags` | 7 | Kandidat unbestätigt | `0x00701BE0` | Aufrufer im Client: AgcmCharacter::AnimationStreamReadCB, AgcmSkill::AttachedTemplateReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAttachedData` | 19 | Kandidat unbestätigt | `0x00702400` | Aufrufer im Client: AgcmCharacter::DeleteTemplateAnimation, AgcmCharacter::SetNextAnimData, AgcmCharacter::LoadTemplateAnimation; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AgcaEffectData2 (Kandidat unbestätigt 1, nicht als eigene Funktion 1, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Delete` | 22 | Kandidat unbestätigt | `0x00717720` | Aufrufer im Client: AgcaEffectData2::DeleteAll, AgcmEventEffectData::~AgcmEventEffectData, AcTextureList::DeleteAll; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `CopyData` | 72 | nicht als eigene Funktion |  | Aufrufer im Client: AgcaEffectData2::CopyDataSet; im Adressbereich der Klasse (0x00717DF0–0x00717FE0) ist keine unbenannte Funktion mehr übrig |
| `CopyDataSet` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcaEventEffectSound (eingebaut 4, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Initialize` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit |
| `AddSound` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcaEventEffectSound::GetSound |
| `GetSound` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmEventEffectData::ReadMovingSoundData |
| `RemoveSound` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveAll` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffectData::~AgcmEventEffectData, AgcmGrass::OnDestroy, AcMapLoader::EmptyQueue |

## AgcaItemClump (eingebaut 1, nicht als eigene Funktion 1, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RemoveAllItemClump` | 19 | zugeordnet | `0x00791800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemClump` | 28 | zugeordnet | `0x00791880` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItemClump` | 24 | zugeordnet | `0x007916F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetItemClump` | 21 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmItem::GetClumpAdminData; im Adressbereich der Klasse (0x007916F0–0x00791880) ist keine unbenannte Funktion mehr übrig |
| `Initialize` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit |

## AgcaUIManager2 (eingebaut 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetUI` | 4 | zugeordnet | `0x005E2950` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddUI` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CExNPCDialog::OnShowNPCDialog, AgcmUIQuestJournal::OnInit, AgcmUIChannel::CBCloneUI |
| `GetUI` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIWorldmap::SetGrouping, AgcmMinimap::ToggleMinimapSize, AgcmUIQuestJournal::RefreshJournalInfo |
| `RemoveUI` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CExNPCDialog::~CExNPCDialog, CExNPCDialog::OnHideNPCDialog, AgcmUIChannel::~AgcmUIChannel |

## AgcdCamConstrain_Obj (eingebaut 1, nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bInit` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdAnimationTime::AddTime, AgcuCamConstrain::bConstrainDistance, AgcuEffVBMng::InitVB |
| `vCheckedObj` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdCamConstrain_Obj::bIntsct; im Adressbereich der Klasse (0x00796530–0x00796530) ist keine unbenannte Funktion mehr übrig |
| `bIntsct` | 39 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuCamConstrain::bConstrainDistance, AgcdEffGlobal::bGetInst; im Adressbereich der Klasse (0x00796530–0x00796530) ist keine unbenannte Funktion mehr übrig |
| `CBIntersectObj` | 39 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdCamConstrain_Obj::bIntsct; im Adressbereich der Klasse (0x00796530–0x00796530) ist keine unbenannte Funktion mehr übrig |
| `CBCmpDist` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdCamConstrain_Obj::CBIntersectObj; im Adressbereich der Klasse (0x00796530–0x00796530) ist keine unbenannte Funktion mehr übrig |

## AgcdCamConstrain_Terrain (nicht als eigene Funktion 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bPreChkTerrain` | 119 | zugeordnet | `0x00795DB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bChkTerrain` | 99 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuCamConstrain::bConstrainDistance; im Adressbereich der Klasse (0x00795D90–0x00795DB0) ist keine unbenannte Funktion mehr übrig |

## AgcdClumpRenderTypeData (eingebaut 1, nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Alloc` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::allocAtomicData, AgcmCharacter::CustomizeStreamReadCB, AgcmMap::CreateCompactDataFromDetailInfo |
| `MemsetRenderType` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::CustomizeStreamReadCB, AgcmRenderType::NewClumpRenderType, AgcmRenderType::SearchClumpRenderType; im Adressbereich der Klasse (0x00709170–0x00709170) ist keine unbenannte Funktion mehr übrig |
| `MemsetCustData` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::CustomizeStreamReadCB, AgcmRenderType::NewClumpRenderType, AgcmRenderType::SearchClumpRenderType; im Adressbereich der Klasse (0x00709170–0x00709170) ist keine unbenannte Funktion mehr übrig |
| `Clear` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::CharacterConstructor, AgcmCharacter::SetTemplateClumpRenderType, AgcdEffCtrl_Set::~AgcdEffCtrl_Set; im Adressbereich der Klasse (0x00709170–0x00709170) ist keine unbenannte Funktion mehr übrig |

## AgcdEffAnim (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `tToFile` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Missile::bToFile |
| `tFromFile` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Missile::bFromFile |

## AgcdEffAnim_Colr (eingebaut 3, nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal, AgcdEffAnim_Rev::bUpdateVal; im Adressbereich der Klasse (0x007AD220–0x007AD220) ist keine unbenannte Funktion mehr übrig |
| `bSetTVal` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Rev::bSetTVal, AgcdEffAnim_Rot::bSetTVal, AgcdEffBase::bEditEffAnim; im Adressbereich der Klasse (0x007AD220–0x007AD220) ist keine unbenannte Funktion mehr übrig |
| `bInsTVal` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Rev::bInsTVal, AgcdEffAnim_Rot::bInsTVal, AgcdEffBase::bInsEffAnimVal; im Adressbereich der Klasse (0x007AD220–0x007AD220) ist keine unbenannte Funktion mehr übrig |
| `bDelTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffBase::bDelEffAnimVal |
| `bUpdateVal` | 44 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal, AgcdEffCtrl_Base::PostUpdateFrm; im Adressbereich der Klasse (0x007AD220–0x007AD220) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile, AgcdEffAnim_Rev::bToFile |
| `bFromFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile, AgcdEffAnim_Rev::bFromFile |

## AgcdEffAnim_Linear (eingebaut 5, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal |
| `bSetTVal` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bSetTVal, AgcdEffAnim_Rev::bSetTVal, AgcdEffAnim_Rot::bSetTVal |
| `bInsTVal` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bInsTVal, AgcdEffAnim_Rev::bInsTVal, AgcdEffAnim_Rot::bInsTVal; im Adressbereich der Klasse (0x007AD340–0x007AD340) ist keine unbenannte Funktion mehr übrig |
| `bDelTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffBase::bDelEffAnimVal |
| `bUpdateVal` | 34 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal; im Adressbereich der Klasse (0x007AD340–0x007AD340) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Rev::bToFile |
| `bFromFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Rev::bFromFile |

## AgcdEffAnim_Missile (eingebaut 2, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Rev::bGetTVal, AgcdEffAnim_Rev::bUpdateVal; im Adressbereich der Klasse (0x007AA130–0x007AA130) ist keine unbenannte Funktion mehr übrig |
| `bUpdateVal` | 407 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal; im Adressbereich der Klasse (0x007AA130–0x007AA130) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile |

## AgcdEffAnim_Rev (eingebaut 1, nicht als eigene Funktion 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 24 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bUpdateVal; im Adressbereich der Klasse (0x007AD3C0–0x007AD3C0) ist keine unbenannte Funktion mehr übrig |
| `bSetTVal` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bSetTVal, AgcdEffAnim_Rot::bSetTVal, AgcdEffBase::bEditEffAnim; im Adressbereich der Klasse (0x007AD3C0–0x007AD3C0) ist keine unbenannte Funktion mehr übrig |
| `bInsTVal` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bInsTVal, AgcdEffAnim_Rot::bInsTVal, AgcdEffBase::bInsEffAnimVal; im Adressbereich der Klasse (0x007AD3C0–0x007AD3C0) ist keine unbenannte Funktion mehr übrig |
| `bDelTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffBase::bDelEffAnimVal |
| `bUpdateVal` | 52 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal, AgcdEffCtrl_Base::PostUpdateFrm; im Adressbereich der Klasse (0x007AD3C0–0x007AD3C0) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; im Adressbereich der Klasse (0x007AD3C0–0x007AD3C0) ist keine unbenannte Funktion mehr übrig |
| `bFromFile` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007AD3C0–0x007AD3C0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffAnim_Rot (eingebaut 3, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bSetTVal` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bSetTVal, AgcdEffAnim_Rev::bSetTVal, AgcdEffBase::bEditEffAnim; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bInsTVal` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bInsTVal, AgcdEffAnim_Rev::bInsTVal, AgcdEffBase::bInsEffAnimVal; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bDelTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffBase::bDelEffAnimVal |
| `bToFile` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile |

## AgcdEffAnim_RpSpline (eingebaut 1, nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bSetSplineFName` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_RpSpline::bFromFile, AgcuEffAnimCreater::vCreate_RpSpline; im Adressbereich der Klasse (0x007AA370–0x007AA370) ist keine unbenannte Funktion mehr übrig |
| `bGetTVal` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal; im Adressbereich der Klasse (0x007AA370–0x007AA370) ist keine unbenannte Funktion mehr übrig |
| `bUpdateVal` | 45 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal; im Adressbereich der Klasse (0x007AA370–0x007AA370) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007AA370–0x007AA370) ist keine unbenannte Funktion mehr übrig |

## AgcdEffAnim_RtAnim (eingebaut 2, nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bSetAnimFName` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_RtAnim::bFromFile, AgcuEffAnimCreater::vCreate_RtAnim; im Adressbereich der Klasse (0x007AA660–0x007AA660) ist keine unbenannte Funktion mehr übrig |
| `bGetTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal |
| `bUpdateVal` | 35 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal; im Adressbereich der Klasse (0x007AA660–0x007AA660) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 10 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007AA660–0x007AA660) ist keine unbenannte Funktion mehr übrig |

## AgcdEffAnim_Scale (eingebaut 5, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal |
| `bSetTVal` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bSetTVal, AgcdEffAnim_Rev::bSetTVal, AgcdEffAnim_Rot::bSetTVal |
| `bInsTVal` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bInsTVal, AgcdEffAnim_Rev::bInsTVal, AgcdEffAnim_Rot::bInsTVal; im Adressbereich der Klasse (0x007AD4D0–0x007AD4D0) ist keine unbenannte Funktion mehr übrig |
| `bDelTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffBase::bDelEffAnimVal |
| `bUpdateVal` | 26 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal; im Adressbereich der Klasse (0x007AD4D0–0x007AD4D0) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile |

## AgcdEffAnim_TuTv (eingebaut 5, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetTVal` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bGetTVal, AgcdEffAnim_Missile::bGetTVal, AgcdEffAnim_Rev::bGetTVal |
| `bSetTVal` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bSetTVal, AgcdEffAnim_Rev::bSetTVal, AgcdEffAnim_Rot::bSetTVal |
| `bInsTVal` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bInsTVal, AgcdEffAnim_Rev::bInsTVal, AgcdEffAnim_Rot::bInsTVal; im Adressbereich der Klasse (0x007AD2C0–0x007AD2C0) ist keine unbenannte Funktion mehr übrig |
| `bDelTVal` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffBase::bDelEffAnimVal |
| `bUpdateVal` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Rev::bUpdateVal, AgcdEffAnim_Rot::bUpdateVal; im Adressbereich der Klasse (0x007AD2C0–0x007AD2C0) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_Linear::bToFile, AgcdEffAnim_Rev::bToFile |
| `bFromFile` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_Linear::bFromFile, AgcdEffAnim_Rev::bFromFile |

## AgcdEffBase (Kandidat unbestätigt 2, eingebaut 4, nicht im Client 4, ohne Kandidat 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `vEffAnimClear` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffBase::~AgcdEffBase |
| `bSetTitle` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt, AgcuEffIniMng::_Read_EffBase_txt |
| `bSetVarSizeInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt, AgcuEffIniMng::_Read_EffBase_txt |
| `bInsEffAnim` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBase::bForTool_InsAnim, AgcuEffIniMng::_Read_EffAnim_Colr_txt, AgcuEffIniMng::_Read_EffAnim_TuTv_txt; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bDelEffAnim` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBase::bForTool_DelAnim; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bInsEffAnimVal` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bDelEffAnimVal` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bEditEffAnim` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Colr_txt, AgcuEffIniMng::_Read_EffAnim_TuTv_txt, AgcuEffIniMng::_Read_EffAnim_PostFX_txt; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bForTool_InsAnim` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBase::bForTool_Clone; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bForTool_FindAnimIndex` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_DelAnim` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_Clone` | 159 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `tToFile` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Missile::bToFile; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `tFromFile` | 16 | Kandidat unbestätigt | `0x007A7F10` | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Missile::bFromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `tToFileVariableData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffBoard::bToFile, AgcdEffBoard::bFromFile, AgcdEffLight::bToFile |
| `tFromFileVariableData` | 26 | Kandidat unbestätigt | `0x007A7F10` | Aufrufer im Client: AgcdEffBoard::bFromFile, AgcdEffLight::bFromFile, AgcdEffMFrm::bFromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AgcdEffBoard (eingebaut 1, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bToFile` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 10 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007B8FA0–0x007B8FA0) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone, AgcdEffObj::bForTool_Clone; im Adressbereich der Klasse (0x007B8FA0–0x007B8FA0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffCamera (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bToFile` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile |

## AgcdEffCtrlMng (eingebaut 1, nicht im Client 2, ohne Kandidat 7, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ValidParentClump` | 46 | zugeordnet | `0x0075EE80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllEffectByClump` | 22 | zugeordnet | `0x0075FBC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `TimeUpdate` | 27 | zugeordnet | `0x0075FB10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateLoadedEffCtrlList` | 42 | zugeordnet | `0x0075F530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ClearCtrlSet` | 25 | zugeordnet | `0x0075F400` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveEffSet` | 25 | zugeordnet | `0x0075F9C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `InsertCtrlSet` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::CreateEffSet; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `RemoveCtrl` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::RemoveEffSet; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `InsertPreEff` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::UseEffSet; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `ToneDown` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::ToneDown, AgcmEff2::ToneDown; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `ToneRestore` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::ToneRestore, AgcmEff2::ToneDown; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `ForTool_DeleteEff` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindEffectSet` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::CB_Update, AgcdEffCtrl_Set::CB_Render; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `IsVaildCtrlSet` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffCtrlMng::ToneDown, AgcdEffCtrlMng::ToneRestore, AgcdEffCtrlMng::ForTool_DeleteEff |
| `ClearPreSet` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::RemoveAllLoadingEffsetList; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `DeletePreSet` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcdEffCtrl_Base (eingebaut 4, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `tBeginUpdate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Base::Update, AgcdEffCtrl_TerrainBoard::Update, AgcdEffCtrl_ParticleSyst_SBH::Update |
| `tPreUpdateFrm` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::Update, AgcdEffCtrl_ParticleSyst_SBH::Update, AgcdEffParticleSystem::vEmiterFrmUpdate; kein unbenannter Kandidat mit Beleg unter 57 unbenannten Funktionen im Klassenbereich |
| `tLifeCheck` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::Update, AgcdEffCtrl_TerrainBoard::Update, AgcdEffCtrl_ParticleSysTem::Update; kein unbenannter Kandidat mit Beleg unter 57 unbenannten Funktionen im Klassenbereich |
| `GetBlendType` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal |
| `GetBaseType` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffAnim_Missile::bUpdateVal, AgcdEffAnim_Linear::bUpdateVal |
| `ApplyRGBScale` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffCtrl_ParticleSysTem::_ParticleUpdate, AgcdEffCtrl_ParticleSyst_SBH::_ParticleUpdate |
| `ApplyRGBScale` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bUpdateVal, AgcdEffCtrl_ParticleSysTem::_ParticleUpdate, AgcdEffCtrl_ParticleSyst_SBH::_ParticleUpdate; kein unbenannter Kandidat mit Beleg unter 57 unbenannten Funktionen im Klassenbereich |

## AgcdEffCtrl_Board (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Update` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x0071C9E0–0x0071C9E0) ist keine unbenannte Funktion mehr übrig |
| `Render` | 51 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Render, AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky; im Adressbereich der Klasse (0x0071C9E0–0x0071C9E0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffCtrl_Camera (eingebaut 1, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetState` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; im Adressbereich der Klasse (0x0071DE90–0x0071DE90) ist keine unbenannte Funktion mehr übrig |
| `Update` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update |

## AgcdEffCtrl_Light (nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetLightRadius` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Scale::bUpdateVal; im Adressbereich der Klasse (0x0071D8A0–0x0071D8A0) ist keine unbenannte Funktion mehr übrig |
| `SetState` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; im Adressbereich der Klasse (0x0071D8A0–0x0071D8A0) ist keine unbenannte Funktion mehr übrig |
| `Update` | 35 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x0071D8A0–0x0071D8A0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffCtrl_MFrm (nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetTargetFrm` | 29 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetMFrmTarget; im Adressbereich der Klasse (0x0071D960–0x0071D960) ist keine unbenannte Funktion mehr übrig |
| `ReleaseTargetFrm` | 28 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_MFrm::~AgcdEffCtrl_MFrm; im Adressbereich der Klasse (0x0071D960–0x0071D960) ist keine unbenannte Funktion mehr übrig |
| `Update` | 85 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x0071D960–0x0071D960) ist keine unbenannte Funktion mehr übrig |

## AgcdEffCtrl_Obj (Kandidat unbestätigt 1, eingebaut 2, nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_ExpandForMissileChild` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Obj::Update; im Adressbereich der Klasse (0x00721440–0x00721440) ist keine unbenannte Funktion mehr übrig |
| `Update` | 53 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x00721440–0x00721440) ist keine unbenannte Funktion mehr übrig |
| `Render` | 26 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Render, AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky; im Adressbereich der Klasse (0x00721440–0x00721440) ist keine unbenannte Funktion mehr übrig |
| `SetState` | 46 | Kandidat unbestätigt | `0x00721450` | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `AddPreRemoveFrm` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::InitEffBaseDpnd; im Adressbereich der Klasse (0x00721440–0x00721440) ist keine unbenannte Funktion mehr übrig |
| `ToneDown` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::ToneDown, AgcdEffCtrlMng::ToneDown, AgcmEff2::ToneDown |
| `ToneRestore` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::ToneRestore, AgcdEffCtrlMng::ToneRestore, AgcmEff2::ToneDown |

## AgcdEffCtrl_ParticleSysTem (eingebaut 1, nicht im Client 1, ohne Kandidat 6, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_RenderFP` | 210 | zugeordnet | `0x0071F5E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ClearPaticle` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::~AgcdEffCtrl_ParticleSysTem, AgcdEffCtrl_ParticleSyst_SBH::~AgcdEffCtrl_ParticleSyst_SBH; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_PushBack_Particle` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::vShootGroup, AgcdEffParticleSys_SimpleBlackHole::bShootPaticle; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_ParticleUpdate` | 116 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::_RenderVS, AgcdEffCtrl_ParticleSysTem::_RenderFP, AgcdEffCtrl_ParticleSyst_SBH::Render; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `Update` | 133 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `PostUpdateFrm` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::Update, AgcdEffCtrl_ParticleSyst_SBH::Update, AgcdEffParticleSystem::vEmiterFrmUpdate; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `_RenderVS` | 234 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Render` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::Render, AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky |
| `SetState` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |

## AgcdEffCtrl_ParticleSyst_SBH (ohne Kandidat 6, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Render` | 100 | zugeordnet | `0x0071FE40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ClearPaticle` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::~AgcdEffCtrl_ParticleSysTem, AgcdEffCtrl_ParticleSyst_SBH::~AgcdEffCtrl_ParticleSyst_SBH; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `_PushBack_Particle` | 23 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::vShootGroup, AgcdEffParticleSys_SimpleBlackHole::bShootPaticle; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `_ParticleUpdate` | 102 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::_RenderVS, AgcdEffCtrl_ParticleSysTem::_RenderFP, AgcdEffCtrl_ParticleSyst_SBH::Render; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `Update` | 87 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `PostUpdateFrm` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::Update, AgcdEffCtrl_ParticleSyst_SBH::Update, AgcdEffParticleSystem::vEmiterFrmUpdate; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `SetState` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |

## AgcdEffCtrl_PostFX (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetState` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; im Adressbereich der Klasse (0x0071DCF0–0x0071DCF0) ist keine unbenannte Funktion mehr übrig |
| `Update` | 73 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x0071DCF0–0x0071DCF0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffCtrl_Set (Kandidat unbestätigt 3, eingebaut 8, nicht als eigene Funktion 22, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Init_Set` | 76 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEff2::CreateEffSet; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `UpdateRwSphere` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `UpdateBBoxHeight` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::SetState |
| `UpdateSphereCenter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::Update |
| `SetState` | 260 | Kandidat unbestätigt | `0x007221F0` | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `End` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffCtrlMng::RemoveEffSet, AgcdEffCtrlMng::ForTool_DeleteEff, AgcmEventNature::OnDestroy |
| `SetPtrClumpEmiter` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmEff2::CreateEffSet |
| `SetPtrAtomicEmiter` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmEff2::CreateEffSet |
| `SetID` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffCtrlMng::InsertCtrlSet |
| `SetInfo` | 20 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEff2::CreateEffSet, AgcmUIGuild::CBReceiveBattleAccept, AgcmUIGuild::CBReceiveBattleStart; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `SetMissileInfo` | 36 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcmEff2::CreateEffSet; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `SetMFrmTarget` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEff2::CreateEffSet; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `SetSoundType3DToSample` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEff2::CreateEffSet; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `SetLife` | 14 | Kandidat unbestätigt | `0x00722A50` | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrlMng::RemoveEffSet, AgcmEff2::CreateEffSet; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetScale` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetDirAndOffset` | 136 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Async, AgcmEff2::CreateEffSet; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `SetAsyncData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmEff2::CreateEffSet |
| `Async` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::SetState |
| `InitEffBaseCtrl` | 109 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Init; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `InitEffBaseDpnd` | 241 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Init; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `Init` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAIDlg::OpenTemplates, AgcmAIDlg::OpenTemplate, AgcmCustomizeRender::AgcmCustomizeRender; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `Clear` | 30 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::CharacterConstructor, AgcmCharacter::SetTemplateClumpRenderType, AgcdEffCtrl_Set::~AgcdEffCtrl_Set; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `TimeUpdate` | 71 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrlMng::TimeUpdate, AgcmEff2::OnIdle; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `Update` | 27 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::CB_Update; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `Render` | 162 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky, AgcmGlyph::CB_POST_RENDER; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `RemFromRenderOrOctree` | 36 | Kandidat unbestätigt | `0x00722AE0` | Aufrufer im Client: AgcdEffCtrl_Set::Clear, AgcdEffCtrlMng::RemoveEffSet; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 12, Belegarten 3) |
| `CB_Update` | 28 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `CB_Render` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `Get1stSound` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::SetTime; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `AddPreRemoveFrm` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::InitEffBaseDpnd; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `DelPreRemoveFrm` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Board::~AgcdEffCtrl_Board, AgcdEffCtrl_TerrainBoard::~AgcdEffCtrl_TerrainBoard, AgcdEffCtrl_ParticleSysTem::~AgcdEffCtrl_ParticleSysTem; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `PreRemoveFrm` | 26 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Obj::~AgcdEffCtrl_Obj; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `ToneDown` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrlMng::ToneDown, AgcmEff2::ToneDown; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `ToneRestore` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrlMng::ToneRestore, AgcmEff2::ToneDown; im Adressbereich der Klasse (0x00721960–0x00721960) ist keine unbenannte Funktion mehr übrig |
| `CB_EFFECT_DISTCORRECT` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcdEffCtrl_Sound (Kandidat unbestätigt 1, nicht als eigene Funktion 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `StopSound` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PlaySound` | 58 | Kandidat unbestätigt | `0x0071DB20` | Aufrufer im Client: AgcdEffCtrl_Sound::Update, AgcdEffCtrl_Sound::Update3DSoundPos, AgcmEventEffect::StartEventEffect; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `Update` | 27 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x0071DC00–0x0071DC00) ist keine unbenannte Funktion mehr übrig |
| `Update3DSoundPos` | 31 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::TimeUpdate; im Adressbereich der Klasse (0x0071DC00–0x0071DC00) ist keine unbenannte Funktion mehr übrig |

## AgcdEffCtrl_Tail (eingebaut 1, nicht im Client 1, ohne Kandidat 6, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_CurrPointUpdate` | 62 | zugeordnet | `0x00720A40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetTargetInfo` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::InitEffBaseCtrl, AgcdEffCtrl_Set::InitEffBaseDpnd; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetTargetInfo` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::InitEffBaseCtrl, AgcdEffCtrl_Set::InitEffBaseDpnd; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetTargetInfo` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::InitEffBaseCtrl, AgcdEffCtrl_Set::InitEffBaseDpnd |
| `_FirstPointUpdate` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_TailUpdate` | 72 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Tail::Update; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `Update` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `Render` | 173 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::Render, AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetState` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcdEffCtrl_TerrainBoard (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Update` | 74 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update; im Adressbereich der Klasse (0x0071CC30–0x0071CC30) ist keine unbenannte Funktion mehr übrig |
| `Render` | 43 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Render, AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky; im Adressbereich der Klasse (0x0071CC30–0x0071CC30) ist keine unbenannte Funktion mehr übrig |

## AgcdEffGlobal (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetInst` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `bGetInst` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |

## AgcdEffLight (nicht als eigene Funktion 3, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bSetPos` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bSetAngle` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bToFile` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; im Adressbereich der Klasse (0x007B93D0–0x007B93D0) ist keine unbenannte Funktion mehr übrig |
| `bFromFile` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007B93D0–0x007B93D0) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffMFrm::bForTool_Clone, AgcdEffObj::bForTool_Clone; im Adressbereich der Klasse (0x007B93D0–0x007B93D0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffMFrm (nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bShakeFrm` | 54 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_MFrm::Update; im Adressbereich der Klasse (0x007B1660–0x007B1660) ist keine unbenannte Funktion mehr übrig |
| `bToFile` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; im Adressbereich der Klasse (0x007B1660–0x007B1660) ist keine unbenannte Funktion mehr übrig |
| `bFromFile` | 21 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007B1660–0x007B1660) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffObj::bForTool_Clone; im Adressbereich der Klasse (0x007B1660–0x007B1660) ist keine unbenannte Funktion mehr übrig |

## AgcdEffObj (nicht im Client 1, ohne Kandidat 3, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bFromFile` | 31 | zugeordnet | `0x00763FC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bSetClumpName` | 43 | zugeordnet | `0x00763F20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `vLoadClump` | 21 | zugeordnet | `0x00763BE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `bLoadClump` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bFindNodeIndex` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::InitEffBaseDpnd; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `bToFile` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `bForTool_Clone` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |

## AgcdEffParticleSys_SimpleBlackHole (Kandidat unbestätigt 2, nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `vCircleEmiter` | 20 | Kandidat unbestätigt | `0x007B1030` | Aufrufer im Client: AgcdEffParticleSys_SimpleBlackHole::bShootPaticle; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `bShootPaticle` | 165 | Kandidat unbestätigt | `0x007B1030` | Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::Update, AgcdEffCtrl_ParticleSyst_SBH::Update, AgcdEffParticleSystem::vShootGroup; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `bToFile` | 20 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; im Adressbereich der Klasse (0x007B00D0–0x007B00D0) ist keine unbenannte Funktion mehr übrig |
| `bFromFile` | 31 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007B00D0–0x007B00D0) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 24 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; im Adressbereich der Klasse (0x007B00D0–0x007B00D0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffParticleSystem (eingebaut 1, ohne Kandidat 8, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `vShootGroup` | 128 | zugeordnet | `0x007B0460` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `vShakeEmiter_forOldPSyst` | 17 | zugeordnet | `0x007AFE00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bShootPaticle` | 142 | zugeordnet | `0x007B09C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `vEmiterFrmUpdate` | 80 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::bShootPaticle; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `vEmiterGetDir` | 84 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::bShootPaticle; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `vCalcOffset_Point` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffParticleSystem::vShootGroup |
| `vCalcOffset_Box` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::vShootGroup; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `vCalcOffset_Cylinder` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::vShootGroup; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `vCalcOffset_Sphere` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcdEffParticleSystem::vShootGroup; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `bToFile` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `bFromFile` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `bForTool_Clone` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |

## AgcdEffPostFX (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bForTool_Clone` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone |

## AgcdEffRenderBase (eingebaut 1, nicht als eigene Funktion 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bSetInitPos` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffRenderBase::tFromFile, AgcuEffIniMng::_Read_EffRenderBase_txt |
| `bSetInitAngle` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffRenderBase::tFromFile, AgcuEffIniMng::_Read_EffRenderBase_txt; im Adressbereich der Klasse (0x00763B90–0x00763BC0) ist keine unbenannte Funktion mehr übrig |
| `bSet_Renderstate` | 114 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Board::Render, AgcdEffCtrl_TerrainBoard::Render, AgcdEffCtrl_ParticleSysTem::_RenderVS; im Adressbereich der Klasse (0x00763B90–0x00763BC0) ist keine unbenannte Funktion mehr übrig |
| `bRestore_Renderstate` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Board::Render, AgcdEffCtrl_TerrainBoard::Render, AgcdEffCtrl_ParticleSysTem::_RenderVS; im Adressbereich der Klasse (0x00763B90–0x00763BC0) ist keine unbenannte Funktion mehr übrig |
| `tToFile` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Missile::bToFile; im Adressbereich der Klasse (0x00763B90–0x00763BC0) ist keine unbenannte Funktion mehr übrig |
| `tFromFile` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Missile::bFromFile; im Adressbereich der Klasse (0x00763B90–0x00763BC0) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; im Adressbereich der Klasse (0x00763B90–0x00763BC0) ist keine unbenannte Funktion mehr übrig |

## AgcdEffSet (Kandidat unbestätigt 1, eingebaut 4, nicht im Client 16, ohne Kandidat 6, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `vClear` | 10 | zugeordnet | `0x007634D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bRelease` | 14 | zugeordnet | `0x007635D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bAddRef` | 42 | zugeordnet | `0x00763A50` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `bGetSoundLendth` | 26 | zugeordnet | `0x00762AF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `bInsEffTex` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffSet::bForTool_InsEffEffTex, AgcuEffIniMng::_Read_EffSet_txt |
| `bInsEffBase` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffSet::bForTool_InsEffBase, AgcuEffIniMng::_Read_EffSet_txt |
| `bInsDependancy` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcdEffSet::bForTool_InsDependancy, AgcuEffIniMng::_Read_EffSet_txt |
| `bSetEffTexName` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bSetDependancy` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bFromFile` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `bToFile` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `bToFileVariableData` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSetMng::MakeEffFile; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `bFromFileVariableData` | 70 | Kandidat unbestätigt | `0x00763770` | Aufrufer im Client: AgcdEffSet::bAddRef; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `vAllocMem` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffSet::bAddRef |
| `bForTool_IsTexUsed` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSet::bForTool_IsAllTexUsed, AgcdEffSet::bForTool_DelAllEffTexNotUsed; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `bForTool_IsAllTexUsed` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_FindEffTex` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSet::bForTool_InsEffEffTex; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `bForTool_InsEffEffTex` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_InsEffBase` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_InsEffBase` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_InsDependancy` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_DelEffTex` | 55 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSet::bForTool_DelAllEffTexNotUsed, AgcdEffSet::bForTool_ChangeBaseTexIndex; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `bForTool_DelAllEffTexNotUsed` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_ChkDependancy` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_DelDependancyAll` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_FindBaseIndex` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_DelEffBase` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_DelDependancy` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_ChangeBaseTexIndex` | 36 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_FindDependancy` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bForTool_FlagChk` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcdEffSetMng (Kandidat unbestätigt 1, nicht im Client 3, ohne Kandidat 5, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `PopFromEffSetPool` | 31 | zugeordnet | `0x0075FEA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LoadEffFile` | 33 | zugeordnet | `0x007603F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `PushToEffSetPool` | 34 | zugeordnet | `0x00760120` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ClearEffSet` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSetMng::~AgcdEffSetMng, AgcdEffSetMng::LoadAll, AgcdEffSetMng::LoadEffFile; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_InsertEffSet` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSetMng::_LoadEffSet, AgcdEffSetMng::LoadEffFile; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_DeleteEffSet` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_DeleteEffSet` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindEffSet` | 8 | Kandidat unbestätigt | `0x0075FF00` | Aufrufer im Client: AgcdEffSetMng::_InsertEffSet, AgcmEff2::DBG_ShowEffInfo, AgcmEff2::UseEffSet; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_LoadEffSet` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcdEffSetMng::LoadAll; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `LoadAll` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::_BuildEffSetContainer, AgcmMap::LoadAll, AgcmMap::LoadAll; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `MakeEffFile` | 101 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ShowState` | 54 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::OnDestroy; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |

## AgcdEffSound (eingebaut 2, ohne Kandidat 4, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bPlaySound` | 72 | zugeordnet | `0x007A80D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bStopSound` | 29 | zugeordnet | `0x007A8040` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bSetSoundName` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffSound_txt; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bSetMonoFName` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffSound_txt; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bPosUpdateFor3DSound` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrl_Sound::PlaySound, AgcdEffCtrl_Sound::Update3DSoundPos |
| `bToFile` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `bForTool_Clone` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |

## AgcdEffTail (nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bToFile` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile; im Adressbereich der Klasse (0x007B9140–0x007B9140) ist keine unbenannte Funktion mehr übrig |
| `bFromFile` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007B9140–0x007B9140) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 20 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; im Adressbereich der Klasse (0x007B9140–0x007B9140) ist keine unbenannte Funktion mehr übrig |

## AgcdEffTerrainBoard (eingebaut 1, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bToFile` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile; im Adressbereich der Klasse (0x007B9500–0x007B9500) ist keine unbenannte Funktion mehr übrig |
| `bForTool_Clone` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffBoard::bForTool_Clone, AgcdEffLight::bForTool_Clone, AgcdEffMFrm::bForTool_Clone; im Adressbereich der Klasse (0x007B9500–0x007B9500) ist keine unbenannte Funktion mehr übrig |

## AgcdEffTex (Kandidat unbestätigt 1, eingebaut 3, nicht als eigene Funktion 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bAddRef` | 18 | Kandidat unbestätigt | `0x0075FF00` | Aufrufer im Client: AgcdEffSet::bAddRef, AgcdEffSetMng::MakeEffFile, AgcdEffSetMng::PushToEffSetPool; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `bRelease` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Clear, AgcdEffSet::bForTool_ChangeBaseTexIndex, AgcdEffSetMng::MakeEffFile; im Adressbereich der Klasse (0x0075E8F0–0x0075E8F0) ist keine unbenannte Funktion mehr übrig |
| `bLoadTex` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffTex::bSetTexName, AgcdEffTex::bSetMaskName, AgcdEffTex::bSetTexMaskName; im Adressbereich der Klasse (0x0075E8F0–0x0075E8F0) ist keine unbenannte Funktion mehr übrig |
| `bSetTexName` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffSet::bSetEffTexName; im Adressbereich der Klasse (0x0075E8F0–0x0075E8F0) ist keine unbenannte Funktion mehr übrig |
| `bSetMaskName` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffSet::bSetEffTexName; im Adressbereich der Klasse (0x0075E8F0–0x0075E8F0) ist keine unbenannte Funktion mehr übrig |
| `bSetTexMaskName` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffTex::AgcdEffTex; im Adressbereich der Klasse (0x0075E8F0–0x0075E8F0) ist keine unbenannte Funktion mehr übrig |
| `bCmpFileName` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffSet::bForTool_FindEffTex |
| `bToFile` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bToFile, AgcdEffAnim_TuTv::bToFile, AgcdEffAnim_Linear::bToFile |
| `bFromFile` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffAnim_Colr::bFromFile, AgcdEffAnim_TuTv::bFromFile, AgcdEffAnim_Linear::bFromFile |

## AgcdEffTexInfo (nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bSetPtrEffTex` | 10 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffSet::bForTool_ChangeBaseTexIndex, AgcmEff2::CBLoadEffBase, AgcuEffIniMng::_Read_EffSet_txt; im Adressbereich der Klasse (0x0075E8D0–0x0075E8D0) ist keine unbenannte Funktion mehr übrig |

## AgcmAmbOcclMap (eingebaut 1, gemeinsamer Rumpf 1, nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `getObjectData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::objectStreamWriteCB, AgcmAmbOcclMap::objectStreamReadCB, AgcmAmbOcclMap::objectDestructor |
| `searchAtomicById` | 52 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAmbOcclMap::initObjectCB; im Adressbereich der Klasse (0x006F5260–0x006F56B0) ist keine unbenannte Funktion mehr übrig |
| `allocAtomicData` | 10 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB; im Adressbereich der Klasse (0x006F5260–0x006F56B0) ist keine unbenannte Funktion mehr übrig |
| `freeAtomicData` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAmbOcclMap::objectDestructor; im Adressbereich der Klasse (0x006F5260–0x006F56B0) ist keine unbenannte Funktion mehr übrig |

## AgcmBaseBoard (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetScreenPos` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmBaseBoard::AgcmBaseBoard, AgcmHPBar::SetData |

## AgcmCamera2 (eingebaut 15, gemeinsamer Rumpf 1, nicht im Client 6, ohne Kandidat 8, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetPtrEye` | 10 | zugeordnet | `0x006F0830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `bGetPtrCX` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default, AgcmCamera2::vForcedRotCX; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bGetPtrCY` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bGetPtrCZ` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default, AgcmCamera2::vForcedZoom, AgcmCamera2::vAvailablePitch; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bGetPtrLookat` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::vOnIdle_default, AgcuCamConstrain::bConstrainDistance |
| `bMove` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bOnMoveTarget, AgcmObject::SetupObjectClump1, AgcmRender::OnDestroy |
| `bTurnWY_180` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcUIManager::OnMButtonDown; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `CBIsCameraMoving` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::OnAddModule; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bOnMoveTarget` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bSetCamFrm` | 56 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::bSetTargetFrame, AgcmCamera2::OnAddModule, AgcmCamera2::OnIdle; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `bSetCamFrm` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCamera2::bSetTargetFrame, AgcmCamera2::OnAddModule, AgcmCamera2::OnIdle |
| `bSetViewWindow` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::OptionFromFile |
| `bGetViewWindow` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `vOnIdle_Login` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bSetIdleType |
| `vForcedZoom` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default, AgcuCamSpringForce::bOnReleaseLinearSpring; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `vForcedRotCX` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `vAdjLookAt` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default; kein unbenannter Kandidat mit Beleg unter 45 unbenannten Funktionen im Klassenbereich |
| `ChangeHeight` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::OnInit |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `bLockAct` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcuCamMode::bChageMode |
| `bUnlockAct` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcuCamMode::bChageMode |
| `vLockFlagChk` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `bOptFlagOn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::OptionFromFile, AgcuCamMode::bChageMode |
| `bOptFlagOff` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::OptionFromFile, AgcuCamMode::bChageMode |
| `vOptFlagChk` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `vUdtMaskOn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `vUdtMaskOff` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bOnMoveTarget, AgcmCamera2::vOnIdle_default, AgcmCamera2::vForcedZoom |
| `vUdtMaskChk` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bTurnWY_180, AgcmCamera2::vOnIdle_default |
| `vShowInfo` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OptionFromFile` | 142 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RenderFrustum` | 34 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmCustomizeRender (eingebaut 7, gemeinsamer Rumpf 1, nicht im Client 14, ohne Kandidat 4, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `End` | 15 | zugeordnet | `0x00660D30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderAtomicCB` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmCustomizeRender::Render; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `RemoveCustomizeAtomicCB` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmCustomizeRender::ClumpClone; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SetState` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Base::AgcdEffCtrl_Base, AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update |
| `GetState` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Base::tLifeCheck, AgcdEffCtrl_Base::Update, AgcdEffCtrl_Set::TimeUpdate |
| `SetWidth` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetHeight` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmCharacter::DetachRide, AgcmHPBar::SetData |
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnLostDevice` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::NewD3D9ReleaseDeviceCB, AgcmPostFX::OnLostDevice, AgcmPostFX::OnCameraStateChange; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `OnResetDevice` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEventNature::NewD3D9RestoreDeviceCB, AgcmPostFX::OnResetDevice, AgcmPostFX::OnCameraStateChange |
| `Start` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmLogin::ConnectLoginServer, AgcmResourceLoader::SetCurrentTexDict, AgcmResourceLoader::InstanceAtomic; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SetWorld` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmItem::OnAddModule |
| `DrawQuad` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCameraPosY` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCameraPosZ` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTargetPosY` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPreviewFar` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPreviewNear` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetZoom` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AtUpOn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AtDownOn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AtUpOff` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AtDownOff` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsAtUpOn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsAtDownOn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetHairNum` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::LoadTemplateDefaultHair, AgcmCharacter::TemplateHairStreamWrite, AgcmExportResource::ExportCharacterClump |
| `GetFaceNum` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::LoadTemplateDefaultFace, AgcmCharacter::TemplateFaceStreamWrite, AgcmExportResource::ExportCharacterClump |

## AgcmDynamicLightmap (nicht im Client 3, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `turnOnLight` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `turnOffLight` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `customUpdateCB` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmDynamicLightmap::addLight; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `customRenderCB` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmDynamicLightmap::addLight; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `Im2DRenderQuad` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcmDynamicLightmap::previewLightmap, AgcmShadow::ShadowRasterBlur, AgcmShadowmap::previewShadowmap; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `previewLightmap` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmEff2 (eingebaut 5, gemeinsamer Rumpf 1, nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DBG_ShowWire` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEff2::OnInit |
| `DBG_ShowSphere` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEff2::OnInit |
| `DBG_ShowEffFrm` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEff2::OnInit |
| `DBG_ShowEffMemoryLog` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEff2::OnInit |
| `DBG_ClearDbgAxis` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEff2::OnInit |
| `ToneDown` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::ToneDown, AgcdEffCtrlMng::ToneDown; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `EffOn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EffOff` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackRemoveEffect` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmEventEffect (Kandidat unbestätigt 1, eingebaut 10, nicht im Client 20, ohne Kandidat 12, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetWeaponType` | 9 | zugeordnet | `0x005C7510` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetBaseEquipItemEventEffect` | 34 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::EventCharAnimWaitCB, AgcmEventEffect::EventCharAnimRunCB, AgcmEventEffect::EventCharAnimAttackCB; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `CBCheckSkipSkillEffect` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::SetBaseSkillEventEffect; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `GetSpiritStoneInfo` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::GetSpiritStoneHitEffect, AgcmEventEffect::SetSpiritStoneHitEffect; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `GetSpiritStoneHitEffect` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventCharCreate` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventCharUpdateMovemenntCB` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::OnAddModule |
| `EventCharDamageCB` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSoundDataNum` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadMovingSoundData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadConvertedItemGradeEffectData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadConvertedArmourAttrEffectData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSpiritStoneHitEffectData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSpiritStoneAttrEffectData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadCommonCharEffectData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSocialAnimationData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate |
| `SetSpiritStoneHitEffect` | 47 | Kandidat unbestätigt | `0x005C5860` | Aufrufer im Client: AgcmEventEffect::SetTargetStruckEffect; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `SetConvertedArmourEffectData` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::SetConvertedArmourAttrEffectCB; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `StartConvertedArmourAttrEventEffect` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::SetConvertedItemEffect |
| `NoticeEffectSetTargetStruckAnimCB` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::CheckCustomData; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `GetSkySetFlagData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::StartEventEffect, AgcmEventEffect::SetOnlySoundSkill, AgcmEventEffect::UpdateNatureStatus |
| `NoticeEffectHitEffectCB` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PlayAnimLoopSound` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCustDataIndex` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::StartEffect, AgcmEventEffect::StartEventEffect, AgcmEventEffect::SetCheckTimeDataList; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `EventSkillChargeThirdAttackCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventSkillConsumeThirdAttackCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventSkillEvationCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventSkillDamageReflectionCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventSkillChangeVelocityCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EventSkillAbsorbDamageCB` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCheckTimeDataList` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::SetCheckTimeDataList; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `RemoveAllCheckTimeData` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::RemoveCheckTimeDataList; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `ReleaseCheckTimeDataList` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::RemoveCommonObjectCB |
| `RemoveCheckTimeDataList` | 38 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddCheckTimeData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::SetCheckTimeDataList |
| `SetStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmShrine::CBDPListStatus, AgcmShrine::CBDPListOccupyRace, AgcmUIBuddy::CBDisplayFriendSelect |
| `AttachShieldAndWeapons` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEventEffect::EventCharEndSocialAnimCB, AgcmEventEffect::CBAttachShieldAndWeapons |
| `CopyCharAnimAttachedData` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveCurrentEffectEvolution` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEventEffect::RemoveCommonCharacterEffect |
| `StreamReadTemplate` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::StreamReadTemplate, AgcmCharacter::StreamReadTemplateAnimation, AgcmCharacter::StreamReadTemplateCustomize; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `StreamWriteTemplate` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `CheckExclusiveEffect` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::Update; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `IsExclusiveEffect` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::Render; kein unbenannter Kandidat mit Beleg unter 345 unbenannten Funktionen im Klassenbereich |
| `ClearExclusiveEffectInfoPerFrame` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::ClearLists |

## AgcmEventEffectData (Kandidat unbestätigt 5, eingebaut 8, nicht im Client 12, ohne Kandidat 14, zugeordnet 7)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SearchSpiritStoneIndex` | 23 | zugeordnet | `0x007149B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReadCommonEffectData` | 154 | zugeordnet | `0x007159E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetSocialAnim` | 12 | zugeordnet | `0x00717190` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `InitializeAnimation` | 8 | zugeordnet | `0x00716110` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SearchCommonCharEffectDataByID` | 16 | zugeordnet | `0x00715850` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetConvertedArmourFX` | 37 | zugeordnet | `0x00714CE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ReadCommonCharEffectData` | 33 | zugeordnet | `0x00716610` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetMaxSoundData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::SetSoundDataNum |
| `SearchMaterialIndex` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffectData::ReadMovingSoundData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SearchCommonCharTypeIndex` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SearchSpiritStoneIndex` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::GetMaxSpiritStoneType, AgcmEventEffectData::ReadConvertedArmourEffectData, AgcmEventEffectData::ReadSpiritStoneEffectData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `_CreateCharEffectMemory` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffectData::ReadCommonCharEffectData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `_DestroyCharEffectMemory` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffectData::~AgcmEventEffectData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `ReadConvertedItemGradeEffectData` | 100 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmEventEffect::ReadConvertedItemGradeEffectData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ReadMovingSoundData` | 86 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmEventEffect::ReadMovingSoundData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `SearchEmptyCommonCharEffectData` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffectData::ReadCommonCharEffectData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SearchCommonCharEffectDataByEID` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::CBCharUseEffect; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SearchEmptySpiritStoneAttrEffectData` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffectData::ReadSpiritStoneAttrEffectData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `SearchEmptySpiritStoneHitEffectData` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffectData::ReadSpiritStoneHitEffectData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `ReadCommonFXData` | 88 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSpiritStoneEffectData` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadSpiritStoneAttrEffectData` | 44 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmEventEffect::ReadSpiritStoneAttrEffectData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ForXport_GetAllSocialAnim` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterSocialAnimation; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `ReadSocialAnimationData` | 103 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmEventEffect::ReadSocialAnimationData, AgcmExportResource::ExportCharacterTemplate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ReadSpiritStoneHitEffectData` | 49 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmEventEffect::ReadSpiritStoneHitEffectData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetAttackSound` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::PlayAttackSound; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetHitSound` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetMovingSound` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::PlayCharacterMovingSound |
| `SetAttackSound` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetHitSound` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMovingSound` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmEventEffectData::ReadMovingSoundData |
| `SetNumHitSound` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetConvertedWeaponGradeEffectData` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::StartConvertedWeaponGradeEventEffect; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetCommonCharEffectData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::RemoveCommonCharacterEffect, AgcmEventEffect::SetCommonCharEffect |
| `GetSpiritStoneAttrEffectData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::EventItemSpiritStoneAttrCB |
| `GetSpiritStoneAttrPointData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::EventItemSpiritStoneAttrCB |
| `GetSpiritStoneHitEffectData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventEffect::GetSpiritStoneHitEffect, AgcmEventEffect::SetAttrDamageEffect, AgcmEventEffect::SetAttrDamageEffect |
| `GetSpiritStoneHitEffectData` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::GetSpiritStoneHitEffect, AgcmEventEffect::SetAttrDamageEffect, AgcmEventEffect::SetAttrDamageEffect; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `GetSocialTypeIndex` | 82 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRaceIndex` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetClassIndex` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetGenderIndex` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSocialSound` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::PlaySocialSound; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |
| `RemoveLoginSocial` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveAllSocialAnimation` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmEventEffectData::~AgcmEventEffectData, AgcmExportResource::ExportCharacterTemplate |
| `GetMovingSoundSet` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::PlayCharacterMovingSound, AgcmEventEffectData::ReadMovingSoundData; kein unbenannter Kandidat mit Beleg unter 37 unbenannten Funktionen im Klassenbereich |

## AgcmEventNature (Kandidat unbestätigt 2, eingebaut 5, nicht im Client 13, ohne Kandidat 17, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DestroyStar` | 21 | zugeordnet | `0x005D1060` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Init` | 59 | zugeordnet | `0x005D10E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GenerateStarVertex` | 92 | zugeordnet | `0x005D2630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetDefaultSky` | 51 | zugeordnet | `0x005D0080` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsMaptoolBuild` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ShowSky` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmEventNature::OnInit, AgcmEventNature::CleanAllData |
| `LoadTextureScriptFile` | 48 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveTextureScriptFile` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CreateSkyAtomic` | 98 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `CreateSkyAtomic` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `CreateCloudAtomic` | 62 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init, AgcmEventNature::SetCloudZoomRate; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `CreateCircumstanceAtomic` | 57 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `CreateSunAtomic` | 60 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `ChangeSunSize` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CreateHalfSphere` | 128 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::CreateSkyAtomic; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `CleanAllData` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::OnDestroy; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `RemoveTexture` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetTextureIndex` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::ModifyAtomic; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `RemoveAllTexture` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::CleanAllData; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `SetSkyRadius` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init, AgcmEventNature::__SetSkyRadius; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `SetSkyRadius` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::Init, AgcmEventNature::__SetSkyRadius; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `SetFog` | 34 | Kandidat unbestätigt | `0x005D3D30` | Aufrufer im Client: AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce, AgcmEventNature::__SetFog; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `FlowCloud` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::SetTime; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `ModifyAtomic` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::SetCloud, AgcmEventNature::SetSun, AgcmEventNature::SetCircumstance; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `SetSkyHeight` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSkySetClientData` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::OnSkySetCreate, AgcmEventNature::OnSkySetDestroy |
| `ResampleTexture` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `__SetFog` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `__MoveSky` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `__SetSkyRadius` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `__SetSkyTemplateID` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CloudUVShift` | 52 | Kandidat unbestätigt | `0x005D3D30` | Aufrufer im Client: AgcmEventNature::SetTime, AgcmEventNature::SetTimeForce; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `SetSkyCircleRadius` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmEventNature::Init |
| `SetCloudZoomRate` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RenderStar` | 90 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::RenderSky; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `BlinkStar` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::SetTime; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `LoadStarData` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddSkyObject` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::CBOnAddObject; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `RemoveSkyObject` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::CBOnRemoveObject; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `OnLostDevice` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::NewD3D9ReleaseDeviceCB, AgcmPostFX::OnLostDevice, AgcmPostFX::OnCameraStateChange |
| `OnResetDevice` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEventNature::NewD3D9RestoreDeviceCB, AgcmPostFX::OnResetDevice, AgcmPostFX::OnCameraStateChange |

## AgcmEventPointLight (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetPointLightClientData` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmEventPointLight::OnPointLightCreate, AgcmEventPointLight::OnPointLightDestroy, AgcmEventPointLight::PointLightStreamWriteCB |

## AgcmFont (eingebaut 9, nicht im Client 7, ohne Kandidat 7)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `InitFuncPtr` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::AgcmFont, AcUIEdit::AcUIEdit, AgpmCharacter::AgpmCharacter; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `DrawTextIMMode2DWorldScale` | 49 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CharToWchar` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::PrepareIMMode2D, AgcmFont::RenderIMMode2DSCALE, AgcmFont::RenderIMMode2DWORLD; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `SetWorldCamera` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmFont::OnAddModule, AgcmTextBoardMng::OnAddModule |
| `GetHashKey` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmFont::PrepareIMMode2D, AgcmFont::RenderIMMode2DSCALE, AgcmFont::RenderIMMode2DWORLD |
| `GetSequenceFont` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSequenceImageFont` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DrawTextMapTool` | 27 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RenderMapTool` | 344 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::DrawTextMapTool; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetMaxTexSize` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmFont::OnInit |
| `SetJapaneseTable` | 465 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::AgcmFont; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `SJIS_TO_UNICODE` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmFont::OnInit |
| `GetTextExtentKr` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetTextExtentCn` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetTextExtentJp` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::InitFuncPtr; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetTextExtentEn` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCharacterWidthKr` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmFont::InitFuncPtr |
| `GetCharacterWidthCn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmFont::InitFuncPtr |
| `GetCharacterWidthJp` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmFont::InitFuncPtr |
| `GetCharacterWidthEn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsLeadByteKr` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmFont::InitFuncPtr |
| `IsLeadByteEn` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsLeadByteCn` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmFont::InitFuncPtr |

## AgcmGlyph (eingebaut 6, nicht im Client 3, ohne Kandidat 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsGlyphedFrame` | 13 | zugeordnet | `0x006E54C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdatePosStaticGlyph` | 8 | zugeordnet | `0x006E3DC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRenderClumplist` | 15 | zugeordnet | `0x006E6810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddMovableGlyph` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ResizeGlyph` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AtomicsRenderProcess` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmGlyph::CB_POST_RENDER; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `AllMaterialRwTexturePointerSwap` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmGlyph::AtomicsRenderProcess |
| `AllMaterialRwTexturePointerRestore` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmGlyph::AtomicsRenderProcess |
| `CB_CUSTOM_RENDER` | 69 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StartDestMoveTarget` | 52 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::MoveSelfCharacter; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `StopDestMoveTarget` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTargeting::OnLButtonDown, AgcmTargeting::TargetCID, AgcmTargeting::CB_LockTarget |
| `SetMouseOnTargetClump` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTargeting::OnMouseMove, AgcmTargeting::CBRemoveCharacter |
| `StopEnemyTarget` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmResourceLoader::AddDestroyClump, AgcmResourceLoader::AddDestroyAtomic, AgcmResourceLoader::RemoveResources |
| `CloseEnemyTargetSelectWindow` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTargeting::CBRemoveCharacter |

## AgcmGrass (nicht im Client 8, ohne Kandidat 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SaveGrassInfoToINI` | 92 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeGrassVerts` | 145 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::LoadGrassInfoFromINI; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `InitGrass` | 64 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::LoadGrass, AgcmGrass::AddGrass; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `GrassMatrixSet` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::CB_GRASS_RENDER; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `AddGrass` | 87 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveGrass` | 84 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateGrassHeight` | 28 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateGrassHeight` | 31 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetGrassMinHeight` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::CB_GET_MIN_HEIGHT; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `CB_GET_MIN_HEIGHT` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::OnAddModule; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `CheckGrassList` | 59 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OptimaizeGrassList` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UnityForSave` | 102 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::SaveToFiles; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `SaveToFiles` | 172 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SaveAllOctrees; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `SetDirectoryPath` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetGrassRoot` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::AddGrass, AgcmGrass::SaveToFiles; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |
| `CB_GRASS_DISTCORRECT` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmGrass::OnIdle; kein unbenannter Kandidat mit Beleg unter 25 unbenannten Funktionen im Klassenbereich |

## AgcmIDBoard (nicht als eigene Funktion 5, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_DrawName` | 100 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmIDBoard::_Draw_Normal, AgcmIDBoard::_Draw_InGuildStadium; im Adressbereich der Klasse (0x00753610–0x007552A0) ist keine unbenannte Funktion mehr übrig |
| `_DrawTitleName` | 30 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmIDBoard::_Draw_Normal; im Adressbereich der Klasse (0x00753610–0x007552A0) ist keine unbenannte Funktion mehr übrig |
| `_DrawNameEx` | 36 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmIDBoard::_Draw_Normal; im Adressbereich der Klasse (0x00753610–0x007552A0) ist keine unbenannte Funktion mehr übrig |
| `_DrawGuild` | 92 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmIDBoard::_Draw_Normal, AgcmIDBoard::_Draw_InGuildStadium; im Adressbereich der Klasse (0x00753610–0x007552A0) ist keine unbenannte Funktion mehr übrig |
| `_IsPlayerInBattleGround` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_IsCheckDrawByPVP` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmIDBoard::_DrawName; im Adressbereich der Klasse (0x00753610–0x007552A0) ist keine unbenannte Funktion mehr übrig |

## AgcmLODList (nicht als eigene Funktion 1, nicht im Client 1, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetLODData` | 15 | zugeordnet | `0x00709620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAllLODData` | 21 | zugeordnet | `0x007095E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddLODData` | 20 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmLODManager::GetLODData; im Adressbereich der Klasse (0x007095E0–0x00709640) ist keine unbenannte Funktion mehr übrig |
| `RemoveLODData` | 67 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmLODManager (eingebaut 1, gemeinsamer Rumpf 1, nicht im Client 3, ohne Kandidat 8, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `LODCallback` | 238 | zugeordnet | `0x006187C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetLODCallback` | 16 | zugeordnet | `0x00618BD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetDistanceTypeName` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnDestroy` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetDefaultDistance` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Initailize` | 80 | ohne Kandidat |  | Aufrufer im Client: AgcmPreLODManager::SetLOD; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SetAtomic` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SearchAtomicCheckPartID` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmLODManager::MakeLODLevel; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SearchAtomicCB` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmLODManager::Initailize, AgcmLODManager::MakeLODLevel, AgcmLODManager::MakeLODLevel_Billboard; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `MakeLODLevel` | 158 | ohne Kandidat |  | Aufrufer im Client: AgcmPreLODManager::SetLOD; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `MakeLODLevel_Billboard` | 96 | ohne Kandidat |  | Aufrufer im Client: AgcmPreLODManager::SetLOD; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `ReadDFF` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmLODManager::MakeLODLevel, AgcmLODManager::MakeLODLevel_Billboard; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetGeometryUsrDataInt` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmLODManager::SearchAtomicCheckPartID, AgcmLODManager::MakeLODLevel; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetDistanceData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmLODManager::LODCallback |
| `IsSetLOD` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmPreLODManager::ItemLoadClumpCB; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcmLensFlare (eingebaut 1, nicht im Client 1, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBLightRayIntersect` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMyWorldCamera` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmLensFlare::OnAddModule |
| `StreamWriteTemplate` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportCharacterTemplate, AgcmExportResource::ExportItemTemplates, AgcmExportResource::ExportObjectTemplate; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBSkyChange` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::OnInit, AgcmEventPointLight::OnAddModule, AgcmLensFlare::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `checkAndUpdateOcclusionQuery` | 86 | ohne Kandidat |  | Aufrufer im Client: AgcmLensFlare::RenderLensFlare; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgcmMinimap (eingebaut 1, gemeinsamer Rumpf 1, nicht im Client 4, ohne Kandidat 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `InitMinimapTextureBuffer` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmMinimap::AgcmMinimap |
| `GetMinimapDummyTexture` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::GetMinimapTexture; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetWorldMapTexture` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetPcPosTexture` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBToggleWorldMapUI` | 51 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::OnAddModule; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetPoint` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUseMapItem` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::OnAddModule; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `SetCallbackRegisterMapPos` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `DestroyMapPosition` | 19 | ohne Kandidat |  | Aufrufer im Client: AcUIMinimap::OnRButtonDblClk, AcUIMinimap::DestroyMapPosition, AgcmUIQuestJournal::CBJournalPositionLinkEvent; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `GetMapPosition` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::AddMapPosition; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |
| `ClearMapPosition` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ToggleCameraView` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmMinimap::CBClickCameraView; kein unbenannter Kandidat mit Beleg unter 12 unbenannten Funktionen im Klassenbereich |

## AgcmNatureEffect (nicht im Client 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `StopNatureEffect` | 28 | zugeordnet | `0x00638AF0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetWind` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EndNatureEffect` | 44 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveNatureEffectInfoToINI` | 116 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmPostFX (eingebaut 4, nicht im Client 2, ohne Kandidat 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnResetDevice` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::NewD3D9RestoreDeviceCB, AgcmPostFX::OnCameraStateChange; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetInstance` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmPostFX::CreateFX, AgcmPostFX::DeleteFX, AgcmPostFX::SetRadius; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `CreateFX` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_PostFX::Update, AgcmPostFX::OnInit, AgcmTextBoardMng::CB_DisplayActionResult; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `AllDeleteFX` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `changeRenderTarget` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRadius` | 7 | ohne Kandidat |  | Aufrufer im Client: Technique::Technique, AgcmPostFX::OnIdle, AgcuUIControlPostFX::OnUpdate; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `SetRadius` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: Technique::Technique, AgcmPostFX::OnIdle, AgcuUIControlPostFX::OnUpdate |
| `SetCenter` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmTextBoardMng::CB_DisplayActionResult, AgcmTextBoardMng::CB_KillCharacter |
| `SetCenter` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTextBoardMng::CB_DisplayActionResult, AgcmTextBoardMng::CB_KillCharacter |
| `saveImmediateFrame` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderInvisibleAtomics, AgcuUIControlPostFX::OnStartPostFX; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcmEventNature::LoadTextureScriptFile, CUiExNPCMsgBoxGrid::OnWindowRender |

## AgcmRender (Kandidat unbestätigt 10, eingebaut 29, gemeinsamer Rumpf 11, nicht im Client 27, ohne Kandidat 79, zugeordnet 17)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsExcept` | 64 | zugeordnet | `0x005B05F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveAtomicFromSector` | 39 | zugeordnet | `0x005B3940` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddAtomicToSector` | 30 | zugeordnet | `0x005B4AF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateOBufferAndDrawTest` | 113 | zugeordnet | `0x005B9EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AtomicPreRender` | 67 | zugeordnet | `0x005B9C40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddTerrainToSector` | 10 | zugeordnet | `0x005B02A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddCustomToBlendRenderList` | 19 | zugeordnet | `0x005B9560` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MyWorldAddAtomic` | 96 | zugeordnet | `0x005B5F00` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `LightValueUpdate` | 18 | zugeordnet | `0x005B1370` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetWorldPosToScreenPos` | 29 | zugeordnet | `0x005B0530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveUpdateInfoFromClump` | 24 | zugeordnet | `0x005B3B50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CullModeWorldRender` | 126 | zugeordnet | `0x005B9640` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveCustomRenderFromSector` | 14 | zugeordnet | `0x005B3A60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CustomizeLighting` | 4 | zugeordnet | `0x005B01F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderWorldForAllIntersections` | 44 | zugeordnet | `0x005AFF50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddAtomicToWorld` | 30 | zugeordnet | `0x005BC6F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddLightToRenderWorld` | 93 | zugeordnet | `0x005B58A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetDrawCollisionTerrain` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetDrawCollisionObject` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsMaptoolBuild` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetPreRenderAtomicCallback` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMainFrame` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::SetSelfCharacter, AgcmCharacter::ReleaseSelfCharacter |
| `SetWorldCamera` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmFont::OnAddModule, AgcmTextBoardMng::OnAddModule; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SetLight` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MyWorldAddClump` | 78 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `MyWorldRemoveClump` | 65 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RemoveClumpFromWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AddClumpToRenderWorld` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MyWorldAddClump; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RemoveClumpFromRenderWorld` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MyWorldRemoveClump; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AddAtomicToRenderWorld` | 48 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MyWorldAddAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RemoveAtomicFromRenderWorld` | 57 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MyWorldRemoveAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `UpdateBoundingSphere` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::InitCharacterCB; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `GetLightByAtomic` | 70 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::MyWorldGetAtomicLocalLightsCallBack; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CB_LIGHT_UPDATE` | 60 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddLightToRenderWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CB_LIGHT_RENDER` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmRender::AddLightToRenderWorld |
| `MyWorldGetAtomicLocalLightsCallBack` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::OnInit, AgcmRender::Render |
| `MyWorldGetAtomicLocalLightsDummyCallBack` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::Render |
| `SetAtomicListCB` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmRender::AddClumpToRenderWorld |
| `InitAtomicSetRenderCallBack` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::LoadZoneRoughBuffer, AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AddClumpToWorld` | 46 | Kandidat unbestätigt | `0x005BC5E0` | Aufrufer im Client: AgcmCharacter::InitCharacterMainThread, AgcmItem::SetFieldItem, AgcmItem::AddClumpToWorld; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddAlphaBModeClumpToWorld` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddBillAtomicToWorld` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddAlphaBModeAtomicToWorld` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AtomicSetInfoBlendAlpha` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddAlphaBModeClumpToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `InitAtomicDatas` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld, AgcmRender::AddBillAtomicToWorld |
| `InitAtomicDatas` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld, AgcmRender::AddBillAtomicToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `InitAtomicDatasCB` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmRender::InitAtomicDatas |
| `AddClumpFromUDA` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRenderCBFromUDACB` | 51 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAtomicToWorld, AgcmRender::AddClumpFromUDA; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RemoveClumpFromWorld` | 31 | Kandidat unbestätigt | `0x005BC5E0` | Aufrufer im Client: AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB, AgcmItem::RemoveClumpFromWorld; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ReturnDefOriginalRenderCB` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RemoveClumpFromWorld, AgcmRender::RemoveAtomicFromWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CheckAlphaAtomicFromClump` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddClumpToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CheckAlphaAtomic` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddBillAtomicToWorld, AgcmRender::AddAtomicToWorld, AgcmRender::AddAlphaBModeAtomicToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AtomicSetAlpha` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SetRenderCBFromUDACB, AgcmRender::CheckAlphaAtomicFromClump, AgcmRender::CheckAlphaAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AtomicSetNonAlpha` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SetRenderCBFromUDACB, AgcmRender::CheckAlphaAtomicFromClump, AgcmRender::CheckAlphaAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AtomicSetAmbient` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SetRenderCBFromUDACB, AgcmRender::CheckAlphaAtomicFromClump, AgcmRender::CheckAlphaAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AtomicSetAlphaFunc` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SetRenderCBFromUDACB, AgcmRender::CheckAlphaAtomicFromClump, AgcmRender::CheckAlphaAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AtomicSetLastZWrite` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmRender::CheckAlphaAtomicFromClump, AgcmRender::CheckAlphaAtomic |
| `GetCameraDistance` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DefaultAtomicListTestRender` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render, AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ImmediateAtomicListTestRender` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DefaultAtomicRender` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::Render |
| `ImmediateAtomicRender` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DefaultTerrainRender` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ImmediateTerrainRender` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RenderWorldAtomics` | 46 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render, AgcmRender::RenderMyCamera, AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderMyCamera` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmWater::UpdateReflectionMap; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ProcessBillboardDraw` | 88 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderAtomic; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderSortedBlendAtomics` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render, AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderSkinPipeAlphaAtomics` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderLastZWriteAtomics` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render, AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `TerrainDataSet` | 70 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render, AgcmRender::ImmediateTerrainRender, AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForAmbientAtomic` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAmbient; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForAlphaFuncAtomic` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlphaFunc; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForBlendAtomicNotSort` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForAlphaAtomic` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForBlendAtomic` | 31 | Kandidat unbestätigt | `0x005BB920` | Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `RenderCallbackForNonAlphaAtomic` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::LoadZoneRoughBuffer, AgcmRender::AtomicSetNonAlpha, AgcmWater::ChangeStatus; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForSkinPipe` | 70 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetNonAlpha, AgcmRender::AtomicSetAmbient; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForSkinPipeBlend` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB |
| `RenderCallbackForSkinPipeAlpha` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForUVAnim` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderCallbackForSpecialRendering; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForUVAnimSkin` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderCallbackForSpecialRendering; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForLastZWrite` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetLastZWrite; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForNone` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RenderCallbackForAmbientAtomicBill` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAmbient; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForAlphaFuncAtomicBill` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlphaFunc; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForAlphaAtomicBill` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForBlendAtomicNotSortBill` | 47 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForNonAlphaAtomicBill` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetNonAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForBlendAtomicBill` | 27 | Kandidat unbestätigt | `0x005BB920` | Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `SetCallbackCustomRender` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPreRender` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPostRender` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPostRender2` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackPostRenderOcTreeClear` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveAtomic` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveClump` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOctreeUDASet` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackOctreeIDSet` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddAtomic` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddClump` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CBWorldIntersection` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::OnAddModule |
| `GeometryMaterialFlagOff` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GeometryMaterialFlagOn` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OriginalAtomicRender` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCustomizeRender::RenderAtomicCB, AgcmGlyph::AtomicsRenderProcess, AgcmRender::RenderClumpOriginalDefaultRender |
| `OriginalClumpRender` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Obj::Render, AgcmShadow2::ShadowTextureRender, AgcmShadowmap::renderShadowmap |
| `SetUVAnimRenderCB` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::SetConvertedArmourEffectData; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ReturnUVAnimRenderCB` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmEventEffect::ReleaseConvertedArmourAttrEffectCB; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderClumpOriginalDefaultRender` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmRender::OriginalClumpRender |
| `UpdateDistanceForTool` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetDistance` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderCallbackForAlphaAtomicBill, AgcmRender::UpdateDistanceForTool, AgcmRender::CullModeWorldRender; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ResetLighting` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBUpdatePosition, AgcmEventEffect::RemoveCommonCharacterEffect, AgcmTargeting::OnMouseMove |
| `SetSectorDistanceC` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld |
| `SetSectorDistanceA` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmRender::AddBillAtomicToWorld, AgcmRender::AddAtomicToWorld, AgcmRender::AddAlphaBModeAtomicToWorld |
| `CalcBoundingSphere` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddClumpToSector` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::MyWorldAddClump |
| `CallBackForEnumAtomicAddSector` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmRender::AddClumpToSector |
| `RemoveClumpFromSector` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmRender::MyWorldRemoveClump |
| `AddCustomRenderToSector` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmDynamicLightmap::addLight, AgcmGrass::OnIdle, AgcmGrass::AddGrass |
| `CallBackForEnumAtomicRemoveSector` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmRender::RemoveClumpFromSector |
| `RenderCustomObjects` | 14 | Kandidat unbestätigt | `0x005BA120` | Aufrufer im Client: AgcmRender::Render, AgcmRender::RenderGeometryOnly; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `CBInitSector` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmRender::OnAddModule |
| `CBRemoveSector` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::OnAddModule; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CBInitSectorData` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::OnAddModule; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CBRemoveSectorData` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::OnAddModule; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderGeometryOnly` | 206 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `WorldToAtomicRender` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::CullModeWorldRender, AgcmRender::CullModeWorldRenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `WorldToAtomicFrustumRender` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::CullModeWorldRender; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CullModeWorldRenderGeometryOnly` | 89 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CalcWorldBoundingSphere` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmMap::SectorForAllAtomicsIntersection, AgcmMap::LoadingSectorsForAllAtomicsIntersection, AgcmMap::LoadingSectorsForAllAtomicsIntersection2 |
| `SetBoundingSphereFromUDA` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld, AgcmRender::AddBillAtomicToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SetBoundingSphereFromUDA` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld, AgcmRender::AddBillAtomicToWorld; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `CallBackForEnumAtomicforSetBSFromUDA` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SetBoundingSphereFromUDA; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AddUpdateInfotoClump` | 51 | Kandidat unbestätigt | `0x005BC5E0` | Aufrufer im Client: AgcmCharacter::InitCharacterMainThread, AgcdEffCtrl_Set::SetState, AgcmObject::SetupObjectClump_TransformOnly; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddUpdateInfotoAtomic` | 44 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveUpdateInfoFromAtomic` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveUpdateInfoFromClump2` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmShadowmap::unregisterClump; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RemoveUpdateInfoFromAtomic2` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveUpdateInfoFromClump3` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcdEffCtrl_Set::RemFromRenderOrOctree; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RemoveUpdateinfoFromAtomic3` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamReadClumpRenderType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamReadCB, AgcmItem::ItemTemplateStreamReadCB, AgcmObject::ObjectTemplateGroupStreamRead |
| `StreamWriteClumpRenderType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateGroupStreamWrite |
| `GetRenderTypeName` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetRenderBlendModeName` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRenderTypeCB` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmCustomizeRender::ClumpClone, AgcmRender::ClumpSetRenderType; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ClumpSetRenderType` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::InitCharacterMainThread, AgcmItem::MakeItemClump, AgcmObject::LoadTemplateData |
| `SetRenderTypeCheckCustDataCB` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::ClumpSetRenderTypeCheckCustData; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ClumpSetRenderTypeCheckCustData` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::SetTemplateClumpRenderType, AgcmItem::LoadTemplateClump |
| `MakeOctrees` | 69 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SaveAllOctrees; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SaveAllOctrees` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddCustomRenderObject` | 15 | Kandidat unbestätigt | `0x005B4C20` | Aufrufer im Client: AgcmDynamicLightmap::addLight, AgcdEffCtrl_Set::SetState, AgcmRender::AddLightToRenderWorld; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RenderCallbackForAlphaAtomic2` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForBlendAtomic2` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForLastBlendAtomic` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RenderCallbackForAlphaAtomicBill2` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AtomicSetAlpha; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForBlendAtomicBill2` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AddAlphaBModeAtomicToWorld, AgcmRender::AtomicSetInfoBlendAlpha, AgcmRender::SetRenderCBFromUDACB; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `_GetSortFactor` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderCallbackForAlphaAtomic, AgcmRender::RenderCallbackForAlphaAtomicBill, AgcmRender::RenderCallbackForAlphaAtomic2; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `InsertPreListOcTree` | 307 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::OcTreeChildRender; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `InsertPreListWorld` | 92 | Kandidat unbestätigt | `0x005B6780` | Aufrufer im Client: AgcmRender::OcTreeModeRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `InsertPreListCustom` | 78 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::OcTreeChildRender; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `UpdateOBufferAndDrawNotTest` | 72 | Kandidat unbestätigt | `0x005BA120` | Aufrufer im Client: AgcmRender::Render; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SetTerrainOccluderBoxs` | 52 | Kandidat unbestätigt | `0x005B6780` | Aufrufer im Client: AgcmRender::OcTreeModeRender; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OcTreeChildRender` | 144 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::OcTreeModeRender; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SetMaxHeightTable` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::SetOccluderLine; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SetOccluderLine` | 481 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::UpdateOBufferAndDrawTest, AgcmRender::UpdateOBufferAndDrawNotTest; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForVSFadeAtomic` | 96 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::RenderCallbackForSpecialRendering; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `RenderCallbackForSpecialRendering` | 38 | ohne Kandidat |  | Aufrufer im Client: CRenderFadeInOut::StartFadeInOut, CRenderFadeInOut::StartFadeIn, CRenderFadeInOut::StartFadeOut; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SetDirectionalLightAdjust` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AgcmRender, AgcmRender::OnInit; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `SetAmbientLightAdjust` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::AgcmRender, AgcmRender::OnInit; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `GetCameraDistanceOnXZ` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::InsertPreListOcTree, AgcmRender::InsertPreListWorld, AgcmRender::InsertPreListCustom; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `AtomicAmbOcclMVLRenderCallBack` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::InitAtomicDatas; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `ComputeLightColors` | 80 | ohne Kandidat |  | Aufrufer im Client: AgcmRender::Render, AgcmRender::RenderGeometryOnly; kein unbenannter Kandidat mit Beleg unter 180 unbenannten Funktionen im Klassenbereich |
| `_RestoreRenderStateForBlendAtomic` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmRender::RenderSortedBlendAtomics |

## AgcmRenderType (eingebaut 1, nicht als eigene Funktion 3, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `NewClumpRenderType` | 56 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmRenderType::StreamReadClumpRenderType; im Adressbereich der Klasse (0x00708F90–0x00708F90) ist keine unbenannte Funktion mehr übrig |
| `SearchClumpRenderType` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SearchClumpRenderType` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteClumpRenderType` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::TemplateDestructor, AgcmItem::ItemTemplateDestructorCB, AgcmRenderType::NewClumpRenderType |
| `StreamReadClumpRenderType` | 28 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::TemplateStreamReadCB, AgcmItem::ItemTemplateStreamReadCB, AgcmObject::ObjectTemplateGroupStreamRead; im Adressbereich der Klasse (0x00708F90–0x00708F90) ist keine unbenannte Funktion mehr übrig |
| `StreamWriteClumpRenderType` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateGroupStreamWrite; im Adressbereich der Klasse (0x00708F90–0x00708F90) ist keine unbenannte Funktion mehr übrig |

## AgcmShadow (nicht als eigene Funktion 1, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ShadowRasterBlur` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Im2DRenderQuad` | 33 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmDynamicLightmap::previewLightmap, AgcmShadow::ShadowRasterBlur, AgcmShadowmap::previewShadowmap; im Adressbereich der Klasse (0x005BC7A0–0x005BE1D0) ist keine unbenannte Funktion mehr übrig |

## AgcmShadow2 (eingebaut 1, gemeinsamer Rumpf 1, nicht als eigene Funktion 1, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetSectorData` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmMap::SectorForAllAtomicsIntersection, AgcmMap::LoadingSectorsForAllAtomicsIntersection, AgcmMap::LoadingSectorsForAllAtomicsIntersection2 |
| `CB_POST_RENDER` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmGlyph::OnAddModule, AgcmGlyph::CB_POST_RENDER, AgcmLensFlare::OnAddModule; im Adressbereich der Klasse (0x00651ED0–0x006530B0) ist keine unbenannte Funktion mehr übrig |
| `SetCallbackTextureUpdate` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `BrightenShadow` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBBlitter` | 36 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmShadowmap (gemeinsamer Rumpf 1, nicht im Client 2, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `releaseClumpCB` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmShadowmap::registerClump, AgcmShadowmap::unregisterClump; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `Im2DRenderQuad` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcmDynamicLightmap::previewLightmap, AgcmShadow::ShadowRasterBlur, AgcmShadowmap::previewShadowmap; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `previewShadowmap` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `createSubTexelPrecisionMap` | 21 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmShrine (Kandidat unbestätigt 3, eingebaut 6, nicht im Client 2, ohne Kandidat 6, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_ReservePrintMessage` | 30 | zugeordnet | `0x006879B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_ChangeShrineObject` | 45 | zugeordnet | `0x00685480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_ShowTimeBar` | 36 | zugeordnet | `0x00685380` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_GetColorFromXml` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::_LoadShrineMessage; kein unbenannter Kandidat mit Beleg unter 1727 unbenannten Funktionen im Klassenbereich |
| `EnterGameMode` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_GetMsgRaceInfo` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::CBShrinePointUpdateInfo, AgcmShrine::CBShrineMessage, AgcmShrine::MakeShrineMessageByMessageCode; kein unbenannter Kandidat mit Beleg unter 1727 unbenannten Funktionen im Klassenbereich |
| `_GetMsgMessge` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::CBShrineMessage, AgcmShrine::MakeShrineMessageByMessageCode; kein unbenannter Kandidat mit Beleg unter 1727 unbenannten Funktionen im Klassenbereich |
| `_CopyShrinInfo` | 18 | Kandidat unbestätigt | `0x006892F0` | Aufrufer im Client: AgcmShrine::CBShrinePointStatusUpdate, AgcmShrine::CBShrinePointUpdateInfo, AgcmShrine::CBAllShrinePointUpdateInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_SortShrineInfo` | 39 | Kandidat unbestätigt | `0x006892F0` | Aufrufer im Client: AgcmShrine::CBShrinePointStatusUpdate, AgcmShrine::CBAllShrinePointUpdateInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_ChangeTapUI` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::CBShrineTapStatus; kein unbenannter Kandidat mit Beleg unter 1727 unbenannten Funktionen im Klassenbereich |
| `_MessagePrintCheckerType` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmShrine::_ReservePrintMessage |
| `_MessagePrintCheckerTargetPlace` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_MessagePrintCheckerTargetRace` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmShrine::_ReservePrintMessage |
| `CBDPMaxLefttime` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::AddDisplay; kein unbenannter Kandidat mit Beleg unter 1727 unbenannten Funktionen im Klassenbereich |
| `CBDPMiniLefttime` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmShrine::AddDisplay; kein unbenannter Kandidat mit Beleg unter 1727 unbenannten Funktionen im Klassenbereich |
| `MakeShrineMessageByMessageCode` | 52 | Kandidat unbestätigt | `0x006885D0` | Aufrufer im Client: AgcmShrine::OnIdle, AgcmShrine::CBResultImprint, AgcmShrine::CBReadyToStart; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_SelfPrintShrineMessageChat` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmShrine::_ReservePrintMessage, AgcmUISiegeWar::CBStatusInfo |
| `_SelfPrintShrineMessageCenter` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmShrine::_ReservePrintMessage |
| `SelfPrintMessageChat` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmShrine::OnIdle |
| `SelfPrintMessageCenter` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmShrine::OnIdle |

## AgcmSound (eingebaut 6, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetDeviceInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmSound::OnSelectDevice, AgcmSound::OnSelectDevice, AgcmSound::GetCurrentDeviceName |
| `PreStop3DSound` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcdEffCtrl_Set::SetState, AgcmEventEffect::PreStop3DSound |
| `StopStream` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Stop3DSound` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcdEffSound::bStopSound |
| `JobQueueAdd` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcmGrass::CB_LOAD_MAP, AgcmGrass::CB_UNLOAD_MAP, AgcmGrass::SetGrassDetail |
| `JobQueueRemove` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcmGrass::CB_LOAD_MAP, AgcmGrass::CB_UNLOAD_MAP, AgcmGrass::SetGrassDetail |
| `_GetPreset` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmSound::SetRoom |

## AgcmTextBoardMng (Kandidat unbestätigt 4, eingebaut 4, nicht im Client 5, ohne Kandidat 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CreateBoard` | 26 | Kandidat unbestätigt | `0x006586A0` | Aufrufer im Client: AgcmTextBoardMng::DisplayUpdateFactor, AgcmTextBoardMng::CB_SetSelfCharacter, AgcmTextBoardMng::CB_AddChar; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CreateBoard` | 7 | Kandidat unbestätigt | `0x006586A0` | Aufrufer im Client: AgcmTextBoardMng::DisplayUpdateFactor, AgcmTextBoardMng::CB_SetSelfCharacter, AgcmTextBoardMng::CB_AddChar; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetBoard` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTextBoardMng::_CreateImoticon, AgcmTextBoardMng::_CreateIDBoard, AgcmTextBoardMng::EnableHPBar |
| `_CreateIDBoard` | 159 | ohne Kandidat |  | Aufrufer im Client: AgcmTextBoardMng::CreateBoard; kein unbenannter Kandidat mit Beleg unter 1871 unbenannten Funktionen im Klassenbereich |
| `DisableHPBar` | 20 | Kandidat unbestätigt | `0x006E4A00` | Aufrufer im Client: AgcmTargeting::OnLButtonDown, AgcmTargeting::TargetCID, AgcmTargeting::OnMouseMove; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `DisableHPBar` | 57 | Kandidat unbestätigt | `0x006E4A00` | Aufrufer im Client: AgcmTargeting::OnLButtonDown, AgcmTargeting::TargetCID, AgcmTargeting::OnMouseMove; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `_CreateHPBar` | 46 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CreateItemID` | 63 | ohne Kandidat |  | Aufrufer im Client: AgcmTextBoardMng::CreateBoard; kein unbenannter Kandidat mit Beleg unter 1871 unbenannten Funktionen im Klassenbereich |
| `GetGuildIDColor` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::CBInitCharacter, AgcmTextBoardMng::_CreateIDBoard, AgcmTextBoardMng::ChangeIDColor; kein unbenannter Kandidat mit Beleg unter 1871 unbenannten Funktionen im Klassenbereich |
| `GetGuildIDColor` | 38 | ohne Kandidat |  | Aufrufer im Client: AgcmGuild::CBInitCharacter, AgcmTextBoardMng::_CreateIDBoard, AgcmTextBoardMng::ChangeIDColor; kein unbenannter Kandidat mit Beleg unter 1871 unbenannten Funktionen im Klassenbereich |
| `DestroyBoard` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmTextBoardMng::DestroyMainBoard, AgcmTextBoardMng::CB_SetSelfCharacter |
| `DestroyBoard` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRideClump, AgcmTextBoardMng::DestroyMainBoard, AgcmTextBoardMng::CB_SetSelfCharacter |
| `PvPRefreshSiege` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::CBReceiveAttackGuildList, AgcmUISiegeWar::CBReceiveDefenseGuildList; kein unbenannter Kandidat mit Beleg unter 1871 unbenannten Funktionen im Klassenbereich |
| `SetWorldCamera` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmFont::OnAddModule, AgcmTextBoardMng::OnAddModule |
| `RenderText` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckPeculiarity` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmIDBoard::_DrawGuild, AgcmIDBoard::_DrawGuild, AgcmIDBoard::_Draw_Normal; kein unbenannter Kandidat mit Beleg unter 1871 unbenannten Funktionen im Klassenbereich |
| `CB_UpdateFactor` | 23 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CB_MissAttack` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CB_RegionChange` | 49 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmTitle (eingebaut 13, nicht im Client 8, ohne Kandidat 10, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `LoadXMLFileToDocument` | 49 | zugeordnet | `0x00656A60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnChangeTitleState` | 73 | zugeordnet | `0x0065A330` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsOpenUI` | 16 | zugeordnet | `0x00656910` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_UpdateCategoryList` | 11 | zugeordnet | `0x00655B20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnUnInitialize` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnInitTitleSetting` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTitle::OnLoadTitleSetting |
| `OnCloseUI` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::CallBack_AutoCloseByCharacterMove, AcUIBase::CloseUI, AgcmUISkillDragonScion::OpenSkillUI; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `OnSendRequestTitleList` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSelectCategory` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSelectCategoryByID` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSelectTitle` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSelectTitleByID` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_GetCategoryByID` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::OnSelectCategoryByID |
| `_GetCategoryByName` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnSelectCategory; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `_GetCategoryByIndex` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmTitle::OnSelectCategoryByIndex, AgcmTitle::GetCategoryNameByIndex |
| `_GetTitleByID` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmTitle::OnChangeTitleState, AgcmTitle::OnUpdateTitleCounter, AgcmTitle::OnUpdateTitleTimeStamp |
| `_GetTitleByName` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnSelectTitle; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `_GetTitleByIndex` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmTitle::OnSelectTitleByIndex, AgcmTitle::GetTitleNameByIndex, AgcmTitle::GetTitleNameByIndexWithPage |
| `_GetTitleCurrentByIndex` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTitle::OnSelectTitleCurrentByIndex, AgcmTitle::OnSelectTitleMiniByIndex, AgcmTitle::GetCurrTitleStateByIndex |
| `_ParseTimeStamp` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::CallBack_RecvTitleUse; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `_AddRunningTitle` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnChangeTitleState; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `_GetRunningTitleByID` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::_AddRunningTitle; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `_DeleteRunningTitle` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnChangeTitleState; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `OnClearTitleIDBoard` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::OnClearTitleState; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `_CheckTitleExchangeTimeLimit` | 51 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCategoryNameByIndex` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTitle::CallBack_DisplayCategoryName |
| `GetTitleNameByID` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::GetCurrentActivateTitleName, AgcmTitle::CallBack_RecvTitleAdd; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |
| `GetTitleNameByIndex` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetTitleNameByIndexWithPage` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmTitle::CallBack_DisplayTitleName |
| `GetCurrTitleStateByIndex` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTitle::CallBack_DisplayTitleNameCurrent, AgcmTitle::CallBack_DisplayTitleNameMini |
| `GetCurrTitleNameByIndexWithPage` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmTitle::CallBack_DisplayTitleNameCurrent, AgcmTitle::CallBack_DisplayTitleNameMini |
| `GetTitleCountCurrentCategory` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmTitle::SetTitlePageIndex |
| `GetCurrentActivateTitleID` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIProduct::OnMake |
| `GetCurrentActivateTitleName` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmTextBoardMng::CB_SetSelfCharacter, AgcmTextBoardMng::CB_AddChar |
| `CallBack_DisplayTitleNameMini` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::_RegisterCallBack; kein unbenannter Kandidat mit Beleg unter 43 unbenannten Funktionen im Klassenbereich |

## AgcmUIAccountCheck (Kandidat unbestätigt 1, eingebaut 2, ohne Kandidat 4, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CB_OnLoginOK` | 31 | zugeordnet | `0x00748AC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInitialize` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIAccountCheck::AgcmUIAccountCheck, AgcmUIAccountCheck::~AgcmUIAccountCheck |
| `OnAddCallBack` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::OnAddModule; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `OnAddLoginRetryCount` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::OnLoginResult; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `CB_OnCancel` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIAccountCheck::OnAddFunction |
| `CB_OnConnect` | 43 | ohne Kandidat |  | Aufrufer im Client: AgcmUIAccountCheck::OnAddCallBack; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `CB_OnDisConnect` | 27 | Kandidat unbestätigt | `0x00748459` | Aufrufer im Client: AgcmUIAccountCheck::OnAddCallBack; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `CB_OnActiveKey` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUIAccountCheck::OnAddCallBack; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |

## AgcmUIAuction (gemeinsamer Rumpf 2, nicht im Client 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetItemInstanceOnBoard` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIAuction::CBSetFocusOnACBoard, AgcmUIAuction::CBKillFocusOnACBoard; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `SetCallbackSetFocus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackKillFocus` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `CBAfterCooldown` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::OnAddModule, AgcmProductMed::OnAddModule, AgcmUIAuction::OnAddModule; kein unbenannter Kandidat mit Beleg unter 6 unbenannten Funktionen im Klassenbereich |
| `_GetAuctionQuantity` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIBuddy (Kandidat unbestätigt 1, eingebaut 1, gemeinsamer Rumpf 2, nicht im Client 3, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CBCheckBlockTrade` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBCheckBlockInvitation` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `BuddyListUpdate` | 8 | Kandidat unbestätigt | `0x006AD500` | Aufrufer im Client: AgcmUIBuddy::OperationAddBuddy, AgcmUIBuddy::OperationRemoveBuddy, AgcmUIBuddy::OperationOnlineBuddy; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RefreshBuddyDetailInfo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIBuddy::CBBuddyListMemberClear, AgcmUIBuddy::CBBuddyUIKeydownESC, AgcmUIBuddy::OperationRegionInfo |
| `CBBanAddDlgSetFocus` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIBuddy::AddFunction; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `OperationMentorUIClose` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUICashMall (eingebaut 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBSetSelfCharacter` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::OnAddModule, AgcmMinimap::OnAddModule, AgcmQuestJournal::OnInit; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBIsShowChargeButton` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICashMall::AddBoolean |
| `CBReturnRefresh` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUICashMall::AddEvent; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgcmUIChannel (eingebaut 3, gemeinsamer Rumpf 2, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `RefreshAllChatRoom` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RefreshChatRoomUserList` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChannel::OperationAddUser, AgcmUIChannel::OperationRemoveUser |
| `RefreshWhisperBtnStatus` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChannel::OperationFindUser |
| `CBDestroyChannel` | 2 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OperationFindUser` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIChannel::CBFindUserResult |

## AgcmUICharacter (eingebaut 4, gemeinsamer Rumpf 2, ohne Kandidat 6, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnShowUIResurrection` | 5 | zugeordnet | `0x006214B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowBlindEquipSlot` | 14 | zugeordnet | `0x006213C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowBtnRestoreEvolution` | 31 | zugeordnet | `0x006212F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnHideBtnRestoreTransform` | 15 | zugeordnet | `0x006212A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowBtnRestoreTransform` | 31 | zugeordnet | `0x006211D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetBaseMinimapInfo` | 5 | zugeordnet | `0x00620F30` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnDestroy` | 15 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 20 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CBConstBase` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacter::OnAddModule; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `CBDestBase` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacter::OnAddModule; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `CBDesCharTemplate` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacter::OnAddModule; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `AddDisplay` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddDisplay, AgcmMinimap::OnAddModule; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `AddDisplay` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddDisplay, AgcmMinimap::OnAddModule; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `AddUserData` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddUserData, AgcmMinimap::OnAddModule; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `ChangeBaseMinimapType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICharacter::CharacterStatusCB |
| `OnToggleBtnRestoreTransform` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnPolyMorph, AgcmUICharacter::CharacterStatusCB, AgcmUILogin::CharacterDoubleClick |
| `OnToggleBtnRestoreEvolution` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StartCharEvolutionByTID, AgcmUICharacter::CharacterStatusCB, AgcmUILogin::CharacterDoubleClick |
| `OnHideBtnRestoreEvolution` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUICharacter::CharacterStatusCB, AgcmUICharacter::OnToggleBtnRestoreEvolution |

## AgcmUICharacterCreate (Kandidat unbestätigt 3, eingebaut 17, ohne Kandidat 7, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_UpdateDescription` | 34 | zugeordnet | `0x007462F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CB_OnGetBaseCharacterOfRace` | 7 | zugeordnet | `0x007471E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetCreatableClass` | 5 | zugeordnet | `0x007469E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnSelectHead` | 20 | zugeordnet | `0x00746B60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnSelectClass` | 28 | zugeordnet | `0x00746E30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnSelectRace` | 36 | zugeordnet | `0x00747000` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnInitialize` | 26 | Kandidat unbestätigt | `0x00748459` | Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIAccountCheck::AgcmUIAccountCheck, AgcmUIAccountCheck::~AgcmUIAccountCheck; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnGetBtnControls` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBLoginMainCreateButtonClick; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `OnAddEvent` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::AddEvent, AgcmUISkill2::AddEvent, AgcmUISkillDragonScion::OnAddEvent; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `OnAddCallBack` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::OnAddModule; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `OnClear` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: CUiExNPCMsgBoxGrid::OnClearGridItem, AgcmUICharacterCreate::~AgcmUICharacterCreate, AgcmUICharacterCreate::OnInitialize |
| `OnCheckNickName` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnCheckNickName |
| `OnSelectPrevHead` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnSelectHeadPrev |
| `OnSelectNextHead` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnSelectHeadNext |
| `OnSelectFace` | 20 | Kandidat unbestätigt | `0x00746C20` | Aufrufer im Client: AgcmUICharacterCreate::OnSelectRace, AgcmUICharacterCreate::OnSelectClass, AgcmUICharacterCreate::OnSelectPrevFace; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `OnSelectPrevFace` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnSelectFacePrev |
| `OnSelectNextFace` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnSelectFaceNext |
| `OnToggleZoom` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnToggleZoom |
| `_LoadSelectableRace` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacterCreate::OnInitialize; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `_ChangeBtnSetSelectClass` | 69 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacterCreate::OnSelectRace; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `_GetSelectRace` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::OnSelectClass, AgcmUICharacterCreate::_GetSelectClass, AgcmUICharacterCreate::_GetSelectClassType |
| `_GetSelectClass` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::OnSelectHead, AgcmUICharacterCreate::OnSelectPrevHead, AgcmUICharacterCreate::OnSelectNextHead |
| `_GetSelectRaceType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::OnSelectHead, AgcmUICharacterCreate::OnSelectFace, AgcmUICharacterCreate::_UpdateDescription |
| `_GetSelectClassType` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::OnSelectHead, AgcmUICharacterCreate::OnSelectFace, AgcmUICharacterCreate::_UpdateDescription |
| `_GetCreatableRace` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::_GetCreatableClass |
| `_UpdateCharacterCreateUI` | 21 | Kandidat unbestätigt | `0x00746C20` | Aufrufer im Client: AgcmUICharacterCreate::OnSelectRace, AgcmUICharacterCreate::OnSelectClass, AgcmUICharacterCreate::OnSelectHead; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_UpdateHead` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacterCreate::_UpdateCharacterCreateUI; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `_UpdateFace` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacterCreate::_UpdateCharacterCreateUI; kein unbenannter Kandidat mit Beleg unter 47 unbenannten Funktionen im Klassenbereich |
| `_IsCurrentRaceType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::OnSelectRace |
| `_IsCurrentClassType` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::OnSelectRace |
| `GetSelectHair` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnCharacterCreateOK |
| `GetSelectFace` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnCharacterCreateOK |
| `GetBtnToggleZoomText` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnDisplayBtnToggleZoom |

## AgcmUIChatting2 (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsEnableSendAreaChatting` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CChatCmd::CallBack_OnSendMsgShout |
| `UpdateTimeLastSendAreaMsg` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CChatCmd::CallBack_OnSendMsgShout |

## AgcmUIConsole (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUIControl (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnClose` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcWindow::Close, AcUIBbs::OnClose, AcUIBbsContent::OnClose |
| `GetGridItemTexture` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIGrid::SetGridItemTextureAndInfo, AcUIGridItem::OnWindowRender |

## AgcmUICooldown (gemeinsamer Rumpf 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUICustomizing (gemeinsamer Rumpf 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CBInitialize` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUICustomizing::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcmUIDebugInfo (gemeinsamer Rumpf 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 6 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUIEventBank (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBRemoveItemFromBank` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIEventBank::OnAddModule; im Adressbereich der Klasse (0x006BE4E0–0x006BF440) ist keine unbenannte Funktion mehr übrig |
| `CBCancelBankSlot` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIEventBank::AddFunction; im Adressbereich der Klasse (0x006BE4E0–0x006BF440) ist keine unbenannte Funktion mehr übrig |

## AgcmUIEventGacha (eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `UpdateControlNotice` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIEventGacha::CBOpenGachaUI |
| `UpdateControlItem` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcUIGacha::OnIdle, AgcmUIEventGacha::CBOpenGachaUI |

## AgcmUIEventItemConvert (eingebaut 1, nicht im Client 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBConvertCancel` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIEventItemConvert::AddFunction |
| `CBDisplayConvertPhysicalResult` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RefreshUserDataConvertType` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RefreshUserDataConvertResult` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIEventItemRepair (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RefreshInventoryMoney` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIEventItemRepair::CBUpdateMoney, AgcmUIEventItemRepair::CBItemRepairUIOpen |

## AgcmUIEventNPCDialog (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUIEventTeleport (gemeinsamer Rumpf 2, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CBMapLoadEnd` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIEventTeleport::OnAddModule; im Adressbereich der Klasse (0x006C4C20–0x006C5A70) ist keine unbenannte Funktion mehr übrig |

## AgcmUIGuideMessage (eingebaut 4, nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SelectMessage` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::UpdateMessage, AgcmUIGuideMessage::PrevMessage, AgcmUIGuideMessage::NextMessage |
| `ShowLevelUpGuideUI` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallBack_Hide` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuideMessage::ShowLevelUpGuideUI; kein unbenannter Kandidat mit Beleg unter 33 unbenannten Funktionen im Klassenbereich |
| `GetSelfRace` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::InitMessage, AgcmUIGuideMessage::UpdateMessage, AgcmUIGuideMessage::OpenLevelUpGuideUI |
| `GetSelfClass` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuideMessage::InitMessage, AgcmUIGuideMessage::UpdateMessage |
| `AddEvents` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIEventItemRepair::OnAddModule, AgcmUIEventTeleport::OnAddModule, AgcmUIGuideMessage::OnAddModule |
| `HideGuideButton` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIGuild (eingebaut 5, nicht im Client 6, ohne Kandidat 9, zugeordnet 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DrawBattleInfoStart` | 19 | zugeordnet | `0x0074E530` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawBattleInfoAccept` | 23 | zugeordnet | `0x0074E460` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `MakeCommaNumber` | 22 | zugeordnet | `0x00633870` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenGuildMarkUI` | 7 | zugeordnet | `0x00632BC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawBattleInfoInit` | 12 | zugeordnet | `0x0074E2C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `DrawBattleInfoScore` | 73 | zugeordnet | `0x0074E930` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `DrawBattleInfoTime` | 71 | zugeordnet | `0x0074E5F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenBattleWithdrawConfirmUI` | 14 | zugeordnet | `0x0074E260` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenBattleRequestConfirmUI` | 22 | zugeordnet | `0x0074E050` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CBDisplayGuildText` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBJoinReject` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `CBForcedLeave` | 25 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CBProcessChatCommand` | 61 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LeaveByCommand` | 16 | ohne Kandidat |  | Aufrufer im Client: CChatCmd::CallBack_OnGuildLeaveOut, AgcmUIGuild::CBProcessChatCommand; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `OpenBattleCancelRequestConfirmUI` | 32 | ohne Kandidat |  | Aufrufer im Client: CChatCmd::CallBack_OnGuildBattleCancel, AgcmUIGuild::CBProcessChatCommand; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `OpenBattleCancelAcceptConfirmUI` | 25 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateBattleTime` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuild::CBReceiveBattleAccept, AgcmUIGuild::CBReceiveBattleStart, AgcmUIGuild::CBReceiveBattleUpdateTime |
| `DrawBattleRount` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBReceiveBattleReject` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `CBReceiveBattleCancelReject` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIGuild::OnAddModule |
| `CBGuildBattleTimeToggle` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CloseGuildMarkUI` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIGuild::CBGuildGuildMarkUIClose, AgcmUIGuild::CBGuildBuyGuildMark |
| `MakeCommaNumber` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuild::CBDisplayGuildMarkInfo, AgcmUIGuild::CBMaxMemberIncreaseUIToggle |
| `CBGuildMaxMemberIncreaseOK` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIGuild::AddFunction |
| `CBEventReturnGuildMaxMemberIncreaseOK` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::AddEvent; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `InitMemberUIData` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmReturnToLogin::CBReceiveAuthKey; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `CBMemberSelectDClick` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::AddFunction; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `CBDisplayMemberSelect` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::AddDisplay; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |
| `CBGetJointColor` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2198 unbenannten Funktionen im Klassenbereich |

## AgcmUIGuildBattleMember (eingebaut 3, nicht im Client 1, ohne Kandidat 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Open` | 25 | zugeordnet | `0x0077EF70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetRandomGuildMember` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleMember::CBBattleListRandomSelect; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `CBBattleListRandomSelect` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBBattleListDelete` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleMember::AddModule; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `CBBattleListDeleteAll` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleMember::AddModule; kein unbenannter Kandidat mit Beleg unter 9 unbenannten Funktionen im Klassenbereich |
| `PushList` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIGuild::CBMemberSelectDClick |
| `RefreshList` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcUIChatMessage::Refresh, AgcUIChatMessage::AddMessage, AgcUIChatMessage::_InitUIList |
| `GetSelectMember` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuildBattleMember::CBBattleListDelete |

## AgcmUIGuildBattleOffer (Kandidat unbestätigt 3, eingebaut 7, nicht im Client 2, ohne Kandidat 1, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ComboClear` | 10 | zugeordnet | `0x0074C2C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Clear` | 7 | zugeordnet | `0x0074C6F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Open` | 13 | zugeordnet | `0x0074CAA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Update` | 1 | eingebaut |  | kleine Funktion (1 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::SetState, AgcdEffCtrl_Set::TimeUpdate, AgcdEffCtrl_Set::Update |
| `BattleStringClear` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIGuild::CBSystemMessage |
| `SetBattleType` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIGuild::CBReceiveBattleAccept, AgcmUIGuild::CBReceiveBattleInfo, AgcmUIGuildBattleOffer::Open |
| `SetBattleTime` | 15 | Kandidat unbestätigt | `0x0074C530` | Aufrufer im Client: AgcmUIGuild::CBReceiveBattleAccept, AgcmUIGuild::CBReceiveBattleInfo, AgcmUIGuildBattleOffer::Open; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetBattlePersonSize` | 14 | Kandidat unbestätigt | `0x0074C820` | Aufrufer im Client: AgcmUIGuildBattleMember::CBBattleListDone, AgcmUIGuildBattleMember::CBDisplayGuildBattleMemberMax, AgcmUIGuildBattleOffer::CBBattleRequest; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetBattlePerson` | 20 | Kandidat unbestätigt | `0x0074C530` | Aufrufer im Client: AgcmUIGuild::CBReceiveBattleAccept, AgcmUIGuild::CBReceiveBattleInfo, AgcmUIGuildBattleOffer::Open; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CBIsBattlePerson` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsGuildBattle` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsPossiblePerson` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuild::OpenBattleRequestConfirmUI; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `SendRequest` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIGuildBattleMember::CBBattleListDone, AgcmUIGuildBattleOffer::CBBattleRequest |
| `SendAccept` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIGuild::CBEventReturnBattleAccept, AgcmUIGuildBattleMember::CBBattleListDone |
| `SendReject` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuild::CBEventReturnBattleRequest, AgcmUIGuild::CBEventReturnBattleAccept, AgcmUIGuildBattleMember::CBBattleListCancel |
| `SendCancelRequest` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuild::CBEventReturnBattleCancelRequest, AgcmUIGuildBattleOffer::CBMessageBattleRequestEnd |

## AgcmUIGuildBattleResult (eingebaut 1, nicht im Client 3, ohne Kandidat 6, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RefreshUserData` | 9 | zugeordnet | `0x005D8020` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenResult` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBDisplayGuildResultNameLeft` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleResult::AddModule; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `CBDisplayGuildResultNameRight` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleResult::AddModule; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `CBDisplayGuildBattleWinDetail1` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleResult::AddModule; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `CBDisplayGuildBattleWinDetail2` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleResult::AddModule; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `CBDisplayGuildBattleLoseDetail1` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleResult::AddModule; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `CBDisplayGuildBattleLoseDetail2` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildBattleResult::AddModule; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `GetGPPoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIGuildBattleResult::CBDisplayGuildBattleWin, AgcmUIGuildBattleResult::CBDisplayGuildBattleLose |
| `GetResultPointString` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetTimePointString` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIGuildWarehouse (eingebaut 1, gemeinsamer Rumpf 1, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 8 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `TestOpen` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIGuildWarehouse::OnInit; im Adressbereich der Klasse (0x00693AC0–0x00695030) ist keine unbenannte Funktion mehr übrig |
| `GetMessageTxt` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBClickExpansion, AgcmUIGuildWarehouse::CBDisplayCaption |

## AgcmUIHelp (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUIHotkey (Kandidat unbestätigt 2, eingebaut 1, nicht im Client 5, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetIniInfo` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DoRegister` | 10 | Kandidat unbestätigt | `0x00611C20` | Aufrufer im Client: AgcmUIHotkey::SetIniInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `GetDefaultHotkey` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetDefaultHotkeyByIndex` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetDefaultHotkeyIndex` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIHotkey::FindCurrentHotkeyByDefault; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetCurrentHotkey` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCurrentHotkeyByIndex` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIHotkey::FindCurrentHotkeyByDefault |
| `GetCurrentHotkeyIndex` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ApplyPlayerMovementKeys` | 10 | Kandidat unbestätigt | `0x00611C20` | Aufrufer im Client: AgcmUIHotkey::SetIniInfo, AgcmUIHotkey::CBFunctionHotkeyOnOk, AgcmUIHotkey::CBFunctionHotkeyOnUIOpen; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetAsyncHotkeyState` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcUIManager::UpdateCameraViewProcess; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `SortCompareFunc` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIHotkey::RefreshUserData; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcmUIItem (Kandidat unbestätigt 14, eingebaut 10, gemeinsamer Rumpf 5, nicht im Client 13, ohne Kandidat 27, zugeordnet 26)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SendChatRegisterItemRequest` | 7 | zugeordnet | `0x006D4620` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetTooltipRegisterItem` | 9 | zugeordnet | `0x006D6760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsAlertItemDurationUnder20` | 6 | zugeordnet | `0x00708070` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemToolTipAmuletInfo` | 79 | zugeordnet | `0x00627B20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemToolTipSpiritStoneInfo` | 144 | zugeordnet | `0x006271A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipUsable` | 29 | zugeordnet | `0x0062B8A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipEquip` | 79 | zugeordnet | `0x0062B7A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsItemPartDurable` | 33 | zugeordnet | `0x006D2EF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnCheckUseEnable` | 22 | zugeordnet | `0x0067D740` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipDetailEnableEquipClass` | 6 | zugeordnet | `0x006288F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipDetailEnableEquipRace` | 6 | zugeordnet | `0x006288A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemToolTipInfo` | 29 | zugeordnet | `0x0062BA80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenChattingItemTooltip` | 17 | zugeordnet | `0x006D6C90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckItemLevel` | 8 | zugeordnet | `0x006D2DC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsPetItem` | 5 | zugeordnet | `0x007404A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBSetPrice4SalesBox` | 30 | zugeordnet | `0x0078B6E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetItemConvertIcon` | 102 | zugeordnet | `0x00629600` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_SetItemToolTipDetailHeroicDefense` | 47 | zugeordnet | `0x00626D40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenToolTip` | 2 | zugeordnet | `0x0062BAD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ClearTooltipRegisterItem` | 14 | zugeordnet | `0x006D6990` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddTooltipRegisterItem` | 30 | zugeordnet | `0x006D6CF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsItemDurable` | 33 | zugeordnet | `0x006D2E20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdateEquipSlotEnable` | 18 | zugeordnet | `0x00708110` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveItemDurabilityUnder5PercentList` | 33 | zugeordnet | `0x006D32E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveItemDurabilityZeroList` | 33 | zugeordnet | `0x006D3200` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CheckItemDurability` | 20 | zugeordnet | `0x006D2FD0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CBChargingInventoryAMoveEndItem` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBChargingInventoryBMoveItem` | 192 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBChargingInventoryBMoveEndItem` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBDragDropItemToChargingInventoryB` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBOpenDuplicateInven` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `UpdateEquipSlotEnable` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::OnChagneEquipItemByEvolution, AgcmUIItem::UpdateEquipSlot; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `IsUsableItem` | 38 | Kandidat unbestätigt | `0x0073AF00` | Aufrufer im Client: AgcmCharacter::OnChagneEquipItemByEvolution, AgcmItem::AttachItem, AgcmItem::_EquipItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `GetEquipSlotMaskEvent` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::UpdateEquipSlotEnable; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBDisplayInventoryMoney` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventItemRepair::AddDisplay, AgcmUIItem::AddDisplay; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBUIInventoryFull` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUIInventoryNotEnoughSpaceToGetGhelld` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUIInventoryDropItem` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUIInventoryDropGhelld` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddEvent; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBUIInventoryDropGhelld` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::AddEvent |
| `CBDropMoneyToField` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIItem::AddFunction |
| `CBReturnConfirmCancelItemFromAuction` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddEvent; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBSplitItemInventory` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBChargingInventoryAMoveItem, AgcmUIItem::CBChargingInventoryBMoveItem, AgcmUIItem::CBInventoryMoveItem; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBInventoryQuestAdd` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBInventoryQuestUpdate` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBInventoryQuestRemove` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBUIUpdateInventoryQuest` | 23 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CheckItemDurability` | 31 | Kandidat unbestätigt | `0x006D5680` | Aufrufer im Client: AgcmUIItem::CBEquipItem, AgcmUIItem::CBUnEquipItem, AgcmUIItem::OnIdle; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetADItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmEventEffect::GetMaxSpiritStoneType, AgcmGlyph::StartEnemyTarget, AgcmUIAuction::CBBoardSelect |
| `AddItemDurabilityZeroList` | 37 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddItemDurabilityUnder5PercentList` | 36 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUpdateAlarmGrid` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBChangeOwner` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBUseReturnScroll` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction, AgcmUIItem::CBUpdateReturnScrollStatus; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBCancelReturnScroll` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBUseReturnScrollResultFailed` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::OnAddModule |
| `SetCallbackSetTooltip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackMovedFromGuildWarehouse` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveSiegeWarGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetItemTimeInfo` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackGetItemStaminaTime` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `GetTooltipRegisterItemByTID` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetTooltipRegisterItemIndex` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OpenChattingItemTooltip; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `StreamReadTooltipData` | 95 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmUIItem::StreamReadTooltipDescData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `StreamReadTooltipDescData` | 35 | Kandidat unbestätigt | `0x00717B93` | Aufrufer im Client: AgcmUILogin::LoadTemplates; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetTooltipList` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::StreamReadTooltipData; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `OpenToolTip` | 188 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::CBTooltipRegisterItem, AgcmUIItem::OpenChattingItemTooltip, AgcmUIItem::CBOpenGridItemToolTip; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `_SetItemToolTipDetailName` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail |
| `_SetItemToolTipDetailPrice` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail |
| `_SetItemToolTipDetailRequireRace` | 56 | Kandidat unbestätigt | `0x00629F20` | Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 11, Belegarten 3) |
| `_SetItemToolTipDetailRequireClass` | 79 | Kandidat unbestätigt | `0x00629F20` | Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 11, Belegarten 3) |
| `_SetItemToolTipDetailWeaponDamage` | 28 | Kandidat unbestätigt | `0x00626760` | Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 11, Belegarten 4) |
| `_SetItemToolTipDetailHeroicDamage` | 58 | Kandidat unbestätigt | `0x00626760` | Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 3) |
| `SetItemToolTipTimeInfo` | 37 | Kandidat unbestätigt | `0x00629F20` | Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_GetItemSecondCategoryName` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CollectClassNames` | 116 | Kandidat unbestätigt | `0x00629F20` | Aufrufer im Client: AgcmUIItem::_SetItemToolTipDetailRequireClass; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_IsEnableRace` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIItem::IsUsableItem, AgcmUIItem::_SetItemToolTipDetailRequireRace, AgcmUIItem::_SetItemToolTipDetailEnableEquipRace |
| `_IsEnableClass` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIItem::IsUsableItem, AgcmUIItem::_SetItemToolTipDetailRequireClass, AgcmUIItem::_SetItemToolTipDetailEnableEquipClass |
| `GetToolTipColor` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::SetItemToolTipDetail; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CalcTooltipPos` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OpenChattingItemTooltip; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBNPCTradeUIOpen` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule, AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBNPCTradeUIOpen` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule, AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBUINPCTradeMSGConfirmBuy` | 35 | Kandidat unbestätigt | `0x0072B6D0` | Aufrufer im Client: AgcmUIItem::CBChargingInventoryAMoveItem, AgcmUIItem::CBChargingInventoryBMoveItem, AgcmUIItem::CBInventoryMoveItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `CBUINPCTradeMSGConfirmBuyStackCountCancel` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIItem::AddFunction |
| `CBUINPCTradeMSGConfirmSell` | 59 | Kandidat unbestätigt | `0x0073AF00` | Aufrufer im Client: AgcmUIItem::AddEvent; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `CBSplitItemNPCTrade` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnOpenMsgBoxConfirmBuyNPCTradeItem` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnSendBuyNPCTradeItem` | 10 | Kandidat unbestätigt | `0x00748459` | Aufrufer im Client: AgcmUIItem::OnOpenMsgBoxConfirmBuyNPCTradeItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnCheckUseEnable` | 13 | Kandidat unbestätigt | `0x00748459` | Aufrufer im Client: AgcmItem::UseItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `CBUIClosePrivateTradeYesNo` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSalesBox2Add` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule, AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBSalesBox2Remove` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule, AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBSalesBox2Update` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIItem::OnAddModule, AgcmUIItem::AddFunction; kein unbenannter Kandidat mit Beleg unter 2280 unbenannten Funktionen im Klassenbereich |
| `CBSetQuantity4SalesBox` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CloseSubInventory` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUICashInven::CBUpdateItemCashInventory, AgcmUICouponBox::CBUpdateItemCashInventory |

## AgcmUILogin (eingebaut 8, nicht im Client 4, ohne Kandidat 9, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBResultDisconnectByAnotherUser` | 8 | zugeordnet | `0x0060B5D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddMyCharacterInfo` | 19 | zugeordnet | `0x0060A1A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddEvent` | 45 | zugeordnet | `0x0060FCE0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBAddCharacter` | 86 | zugeordnet | `0x0060B2B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CBMapSectorChangePreCallback` | 30 | zugeordnet | `0x0060B0D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CreateCharacter` | 22 | zugeordnet | `0x0060A090` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `LoadTemplates` | 95 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLoginMode` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIAccountCheck::CB_OnConnect, AgcmUICharacterSelect::OnBtnSlot, AgcmUICharacterSelect::OnBtnCompensation |
| `OpenMoveToHangame` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveMyCharacterInfo` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBRemoveCharacter; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `GetMyCharacterCount` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBLoginMainCreateButtonClick, AgcmUILogin::CBGetMyCharacterNameFinish; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `GetMyCharacterInfoIndex` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::RemoveMyCharacterInfo, AgcmUILogin::CBAddCharacter; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `GetMyCharacterInfoIndex` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::RemoveMyCharacterInfo, AgcmUILogin::CBAddCharacter; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `CBOpenHangameWeb` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILogin::AddEvent |
| `CBCancelDeleteConfirm` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILogin::AddFunction |
| `CBOpenExitWindow` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUILogin::AddFunction |
| `CBLoginReturnRemoveDuplicateAccount` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUILogin::AddEvent |
| `CBReturnNotTester` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUILogin::AddEvent |
| `CBResultNotApplied` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::AddEvent; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `CBIDFailed` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUILogin::AddEvent |
| `CBPasswordFailed` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::AddEvent; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `CBMapSectorChangeCallback` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::OnAddModule; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `CBGetCharCount` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILogin::OnAddModule, AgcmWorld::OnAddModule |
| `CBKeydownCloseAllUI` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::OnAddModule; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |
| `ParsePatchCodeString` | 78 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ParseChannelingCodeString` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReConnectLoginServer` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIAccountCheck::CB_OnConnect; kein unbenannter Kandidat mit Beleg unter 19 unbenannten Funktionen im Klassenbereich |

## AgcmUILoginSelect (eingebaut 1, ohne Kandidat 5, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ConnectLoginServer` | 16 | zugeordnet | `0x007424C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Initialize` | 19 | zugeordnet | `0x007428E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBSelectLoginServer` | 53 | zugeordnet | `0x00743030` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenLoginSelect` | 33 | zugeordnet | `0x00742570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CloseLoginSelect` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUILoginSelect::CBSelectLoginServer |
| `GetLoginGroup` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUILoginSelect::CBSelectLoginServer, AgcmUILoginSelect::IsRetryLoginServer, AgcmUILoginSelect::ReConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `CBSelectExit` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUILoginSelect::_LoginSelectWindowInit; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `CBMouseOnLoginServer` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUILoginSelect::_LoginSelectWindowInit; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `IsRetryLoginServer` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::ReConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |
| `ReConnectLoginServer` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUIAccountCheck::CB_OnConnect, AgcmUILogin::ReConnectLoginServer; kein unbenannter Kandidat mit Beleg unter 11 unbenannten Funktionen im Klassenbereich |

## AgcmUILoginSetting (Kandidat unbestätigt 3, eingebaut 2, ohne Kandidat 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `LoadSettingFromFile` | 54 | zugeordnet | `0x0074BDF0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ClearData` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUILoginSetting::LoadSettingFromFile; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `_ParseHeaderDataType` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUILoginSetting::LoadSettingFromFile; kein unbenannter Kandidat mit Beleg unter 26 unbenannten Funktionen im Klassenbereich |
| `_ParseRaceName` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILoginSetting::_AddCharacterSelectMoveOffset, AgcmUILoginSetting::_AddCharacterCreatePosition, AgcmUILoginSetting::_AddCameraCharacterCreateTM |
| `_ParseClassName` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILoginSetting::_AddCharacterSelectMoveOffset, AgcmUILoginSetting::_AddCameraCharacterZoomTM |
| `_AddCameraLoginTM` | 28 | Kandidat unbestätigt | `0x0074AAE0` | Aufrufer im Client: AgcmUILoginSetting::LoadSettingFromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |
| `_AddCameraCharacterSelectTM` | 28 | Kandidat unbestätigt | `0x0074AAE0` | Aufrufer im Client: AgcmUILoginSetting::LoadSettingFromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |
| `_AddCameraCharacterCreateTM` | 34 | Kandidat unbestätigt | `0x0074AAE0` | Aufrufer im Client: AgcmUILoginSetting::LoadSettingFromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |

## AgcmUIMailBox (eingebaut 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `TestOpenWriteWindow` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMailBox::OnInit |
| `TestOpenList` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMailBox::OnInit |
| `GetMessageTxt` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBClickExpansion, AgcmUIGuildWarehouse::CBDisplayCaption |

## AgcmUIMain (eingebaut 6, gemeinsamer Rumpf 13, nicht im Client 4, ohne Kandidat 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `LoadSystemMessageGridToolTip` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddSystemMessageGridItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBillInfo::AddSystemGridIcon_PCRoom, AgcmBillInfo::_AddSystemGridHangameS, AgcmBillInfo::_AddSystemGridHangameTPack |
| `AddSystemMessageGridItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBillInfo::AddSystemGridIcon_PCRoom, AgcmBillInfo::_AddSystemGridHangameS, AgcmBillInfo::_AddSystemGridHangameTPack |
| `RemoveSystemMessageGridItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmBillInfo::CBUpdateBillInfo, AgcmUICashInven::CheckPetStateGrid, AgcmUICouponBox::CheckPetStateGrid |
| `ClearSystemMessageGridItem` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ResetArrow` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMain::CBUnEquipItem |
| `ResetBolt` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMain::CBUnEquipItem |
| `CBSelectListItem` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBClickSystemGridNoAction` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIMain::OnAddModule |
| `UseBelt` | 56 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCallbackOpenTooltip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCloseTooltip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCloseAllUITooltip` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateAlarmGrid` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRButtonSkillCast` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackKeydownCloseAllUIExceptMain` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackKeydownESC` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackAddShortcut` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackRemoveShortcut` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateHPPotion` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMPPotion` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateHPPointGage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackUpdateMPPointGage` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `ClearAlarmGrid` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMain::UpdateAlarmGrid; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `UpdateMediaRateWindow` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMain::OnIdle; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `RefreshItemCount` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMain::CBAddItemToInventory, AgcmUIMain::CBRemoveItemFromInventory, AgcmUIMain::CBUpdateStackCount; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `RefreshItemCount` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMain::CBAddItemToInventory, AgcmUIMain::CBRemoveItemFromInventory, AgcmUIMain::CBUpdateStackCount; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |

## AgcmUIMainSystemGridTooltip (eingebaut 1, nicht im Client 2, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Initialize` | 75 | ohne Kandidat |  | Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `Destroy` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmItem::ItemDestructorCB, AgcmObject::ReleaseObjectData; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CloseSystemGridTooltip` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIMain::_CloseSystemGridTooltip |
| `_GetString` | 17 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_LineColor` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMainSystemGridTooltip::LoadSystemGridTooltipXML; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `_MakeExpireTimeString` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIManager2 (Kandidat unbestätigt 37, eingebaut 29, gemeinsamer Rumpf 4, nicht im Client 23, ohne Kandidat 33, zugeordnet 37)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBListItemConstructor` | 45 | zugeordnet | `0x005E8CD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ResetControlDisplayMap` | 13 | zugeordnet | `0x005E2640` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenTooltip` | 43 | zugeordnet | `0x005E3210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetControlDisplayFont` | 13 | zugeordnet | `0x005E28D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetControlDisplayMap_2` | 0 | zugeordnet | `0x005E2770` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetControlDisplayMap` | 26 | zugeordnet | `0x005E26A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyControl` | 106 | zugeordnet | `0x005E8910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyBaseProperty` | 151 | zugeordnet | `0x005E1A80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddUI` | 13 | zugeordnet | `0x005E19A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetMouseOnUI` | 10 | zugeordnet | `0x005E34D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveWindow` | 12 | zugeordnet | `0x005E2E30` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyHotkey` | 24 | zugeordnet | `0x005E6560` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetHotkey` | 4 | zugeordnet | `0x005E2980` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddHotkey` | 13 | zugeordnet | `0x005E6C90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RefreshUserData` | 9 | zugeordnet | `0x005E43E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemoveControl` | 111 | zugeordnet | `0x005E74B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddControl` | 153 | zugeordnet | `0x005E8250` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetUIData` | 7 | zugeordnet | `0x005E1A20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CopyUI` | 108 | zugeordnet | `0x005E9210` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CloseAllEventUI` | 13 | zugeordnet | `0x005E59A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CloseAllUI` | 11 | zugeordnet | `0x005E5890` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `StreamReadAction` | 198 | zugeordnet | `0x0062FDB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteClock` | 16 | zugeordnet | `0x0062F790` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteCombo` | 15 | zugeordnet | `0x0062F720` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteScroll` | 19 | zugeordnet | `0x0062F660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteEdit` | 19 | zugeordnet | `0x0062F5D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteTree` | 12 | zugeordnet | `0x0062F570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteList` | 14 | zugeordnet | `0x0062F500` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteBar` | 18 | zugeordnet | `0x0062F450` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteGrid` | 20 | zugeordnet | `0x0062F350` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `StreamWriteBase` | 99 | zugeordnet | `0x0062EE80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `IsOpenModalWindow` | 56 | zugeordnet | `0x005E35B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Notice` | 33 | zugeordnet | `0x005E33C0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ActionMessageEditOKCancelDialog` | 5 | zugeordnet | `0x005E3040` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ActionMessageThreeBtnDialog` | 8 | zugeordnet | `0x005E2FB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `ActionMessageOKDialog2` | 5 | zugeordnet | `0x005E2F20` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `CameraStatusChange` | 43 | zugeordnet | `0x005E2CE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AttachUIData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AttachControlData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxUI` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMaxUIMessage` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetMainWindow` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ResizeManagerWindow` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::CameraStatusChange; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetMaxMaps` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeValidName` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::AddUI; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `GetUI` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWorldmap::SetGrouping, AgcmMinimap::ToggleMinimapSize, AgcmUIQuestJournal::RefreshJournalInfo |
| `GetUI` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWorldmap::SetGrouping, AgcmMinimap::ToggleMinimapSize, AgcmUIQuestJournal::RefreshJournalInfo |
| `RemoveAllUI` | 10 | Kandidat unbestätigt | `0x005E8DF0` | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `ChangeUIName` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetSequenceUI` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::DestroyUI, AgcmUIManager2::RemoveAllUI, AgcmUIManager2::OpenMainUI |
| `OpenUI` | 225 | Kandidat unbestätigt | `0x005E5F50` | Aufrufer im Client: CExNPCDialog::OnShowNPCDialog, AgcmUIWorldmap::OpenWorldMap, AgcmUIWorldmap::CBRoadMapToggle; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 13, Belegarten 2) |
| `AttachTooltip` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DetachTooltip` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OpenMainUI` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBEnterGameEnd; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetUIData` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIChannel::CBCloneUI |
| `SetControlAlpha` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::AddControl; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `GetControl` | 15 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmTitle::_GetDialogControls, AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetControl` | 15 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmTitle::_GetDialogControls, AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetControl` | 15 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmTitle::_GetDialogControls, AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetControl` | 15 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmTitle::_GetDialogControls, AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetControl` | 15 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmTitle::_GetDialogControls, AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetControl` | 15 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmTitle::_GetDialogControls, AgcmTitle::OnClearTitleCategorySelection, AgcmTitle::OnClearTitleSelection; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveControl` | 7 | Kandidat unbestätigt | `0x005FD740` | Aufrufer im Client: AgcmUIManager2::DestroyUI, AgcmUIManager2::CBListItemDestructor; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSequenceControl` | 34 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIWorldmap::SetGrouping, AgcmShrine::SetTapControl, AgcmShrine::CBAllShrinePointUpdateInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetSequenceControl` | 31 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIWorldmap::SetGrouping, AgcmShrine::SetTapControl, AgcmShrine::CBAllShrinePointUpdateInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddFunction` | 7 | Kandidat unbestätigt | `0x0062D600` | Aufrufer im Client: AgcmCamera2::OnLuaInitialize, AgcmCharacter::OnLuaInitialize, AgcmEventNature::OnLuaInitialize; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddUserData` | 7 | Kandidat unbestätigt | `0x0062D600` | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddUserData, AgcmMinimap::OnAddModule; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddDisplay` | 18 | Kandidat unbestätigt | `0x005E1EF0` | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddDisplay, AgcmMinimap::OnAddModule; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddDisplay` | 7 | Kandidat unbestätigt | `0x0062D600` | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddDisplay, AgcmMinimap::OnAddModule; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddBoolean` | 7 | Kandidat unbestätigt | `0x00602DB0` | Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIBuddy::OnAddModule, AgcmUICashInven::OnAddModule; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `AddCustomControl` | 18 | Kandidat unbestätigt | `0x005E1EF0` | Aufrufer im Client: AgcmUIWorldmap::OnInit, AgcmMinimap::OnAddModule, AgcmShrine::OnAddModule; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CreateFunction` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::AddFunction |
| `DestroyFunction` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::AddFunction, AgcmUIManager2::RemoveAllFunction |
| `GetFunction` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllFunction, AgcmUIManager2::StreamReadCB, AgcmUIManager2::StreamReadAction |
| `GetFunction` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllFunction, AgcmUIManager2::StreamReadCB, AgcmUIManager2::StreamReadAction |
| `RemoveAllFunction` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `CreateUserData` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUICharacter::AddUserData, AgcmUIManager2::AddUserData; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `DestroyUserData` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::AddUserData, AgcmUIManager2::RemoveAllUserData, AgcmHeroicSkill::Destroy |
| `GetUserData` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllUserData, AgcmUIManager2::CountUserData, AgcmUIManager2::ParseMessage |
| `GetUserData` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllUserData, AgcmUIManager2::CountUserData, AgcmUIManager2::ParseMessage |
| `RemoveAllUserData` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `GetControlUserData` | 9 | Kandidat unbestätigt | `0x005E4C50` | Aufrufer im Client: AgcmUIChatting2::CBSendWhisper, AgcmUIEventBank::CBBankUpdateLayer, AgcmUIEventTeleport::CBRequestTeleport; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CountUserData` | 30 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIChannel::CBCloneUI, AgcmUIManager2::RemoveControl, AgcmUIManager2::CopyControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CountUserData` | 61 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIChannel::CBCloneUI, AgcmUIManager2::RemoveControl, AgcmUIManager2::CopyControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CountUserData` | 71 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIChannel::CBCloneUI, AgcmUIManager2::RemoveControl, AgcmUIManager2::CopyControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetUserDataRefresh` | 40 | Kandidat unbestätigt | `0x005E4C50` | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap, AgcmMinimap::CBSelfCharacterPositionCallback, AgcmMinimap::CBBindingRegionChange; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `CreateDisplay` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUICharacter::AddDisplay, AgcmUICharacter::AddDisplay, AgcmUIManager2::AddDisplay |
| `DestroyDisplay` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::AddDisplay, AgcmUIManager2::AddDisplay, AgcmUIManager2::RemoveAllDisplay |
| `GetDisplay` | 7 | Kandidat unbestätigt | `0x005E24C0` | Aufrufer im Client: AgcmUIManager2::RemoveAllDisplay, AgcmUIManager2::ParseMessage, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetDisplay` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllDisplay, AgcmUIManager2::ParseMessage, AgcmUIManager2::StreamReadCB |
| `RemoveAllDisplay` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `CreateBoolean` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::AddBoolean |
| `DestroyBoolean` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::AddBoolean, AgcmUIManager2::RemoveAllBoolean |
| `GetBoolean` | 7 | Kandidat unbestätigt | `0x005E24C0` | Aufrufer im Client: AgcmUIManager2::RemoveAllBoolean, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetBoolean` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllBoolean, AgcmUIManager2::StreamReadCB |
| `RemoveAllBoolean` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `GetCControl` | 7 | Kandidat unbestätigt | `0x005E24C0` | Aufrufer im Client: AgcmUIManager2::RemoveAllCControl, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `GetCControl` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIManager2::RemoveAllCControl, AgcmUIManager2::StreamReadCB |
| `RemoveAllCControl` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `EnumDisplayCallback` | 42 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RefreshControl, AgcmUIManager2::SetControlDisplayMap, AgcmUIManager2::ParseMessage; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetControlDisplayMap` | 55 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIManager2::CopyControl, AgcmUIManager2::RefreshControl, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetEventMap` | 7 | Kandidat unbestätigt | `0x005E77A0` | Aufrufer im Client: AgcChatManager::_WhisperEvent, AgcmUILogin::OnIdle, AgcmUIManager2::ThrowEvent; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetEventMap` | 7 | Kandidat unbestätigt | `0x005E77A0` | Aufrufer im Client: AgcChatManager::_WhisperEvent, AgcmUILogin::OnIdle, AgcmUIManager2::ThrowEvent; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ThrowEvent` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::ItemUseByTIDCB, AcUIMinimap::RenderMinimap, AgcmUIWorldmap::OpenWorldMap |
| `ThrowEvent` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::ItemUseByTIDCB, AcUIMinimap::RenderMinimap, AgcmUIWorldmap::OpenWorldMap |
| `RemoveAllEvent` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `RemoveAllEventActions` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RemoveAllEvent; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `RemoveHotkey` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUIHotkey::OnDestroy, AgcmUIHotkey::ReMappingAllHotkeys; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `RemoveHotkey` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIHotkey::OnDestroy, AgcmUIHotkey::ReMappingAllHotkeys; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `RemoveAllHotkey` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::~AgcmUIManager2; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetHotkeyDescription` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamRead; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `ResetControlGrid` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetControlGrid` | 44 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIManager2::CopyControl, AgcmUIManager2::RefreshControl, AgcmUIManager2::StreamReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetControlGrid` | 15 | Kandidat unbestätigt | `0x005E7750` | Aufrufer im Client: AgcmUIEventBank::CBBankMoveItem, AgcmUIEventItemRepair::CBMoveEndItem, AgcmUIItem::CBChargingInventoryAMoveItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ParseMessage` | 48 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::ProcessAction; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetupActions` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamRead; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetupActions` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamRead; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `SetupAction` | 104 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::SetupActions, AgcmUIManager2::SetupActions; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `RemoveFromActions` | 37 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIManager2::DestroyUI, AgcmUIManager2::RemoveControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveFromActions` | 35 | Kandidat unbestätigt | `0x005FD850` | Aufrufer im Client: AgcmUIManager2::DestroyUI, AgcmUIManager2::RemoveControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RemoveFromAction` | 61 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RemoveFromActions, AgcmUIManager2::RemoveFromActions; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `CBListItemDestructor` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::AddControl, AgcmUIManager2::CBListItemRefresh; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `CBListItemRefresh` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::AddControl; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `CB_POST_RENDER` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmGlyph::OnAddModule, AgcmGlyph::CB_POST_RENDER, AgcmLensFlare::OnAddModule |
| `SetCamera` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmTextBoardMng::SetWorldCamera, AgcmUIManager2::OnAddModule |
| `AddWindow` | 8 | Kandidat unbestätigt | `0x005FC1F0` | Aufrufer im Client: CExNPC::_ShowMsgBox, AgcEngine::EditMessageDialog2, AgcEngine::OkCancelDialog2; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `RefreshWindow` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AcUIEventButton::DestroyButtonMenu |
| `SetCallbackOpenMainUI` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackCloseAllUI` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackSetMainWindow` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackActionMessageChat` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `IsMainWindow` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIItem::CBChargingInventoryAMoveEndItem, AgcmUIItem::CBChargingInventoryBMoveEndItem, AgcmUIItem::CBInventoryMoveEndItem |
| `ActionMessageOKCancelDialog2` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ActionMessageEditOKDialog` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ActionMessageEditOKDialog2` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SortPopupUI` | 61 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSoundPath` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetTexturePath` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmEff2::OnInit, CExNPC::OnMakeResource, AgcmExportResource::ExportDDSPath |
| `SetUIMode` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLineDelimiter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIChannel::CBEnterChatMessage, AgcmUIEventItemConvert::UpdatePhysicalConvertConfirm, AgcmUIEventItemConvert::UpdateRuneConvertConfirm |
| `GetSeparateLine` | 34 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CloseTooltip` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::CloseUI, AgcUIWindow::OnCommand, AgcmUISocialAction::CBSocialActionNotFocus; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `CloseTooltip` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIManager2::CloseUI, AgcUIWindow::OnCommand, AgcmUISocialAction::CBSocialActionNotFocus |
| `SetControlTooltip` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::StreamReadCB; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `UIClose` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIManager2::OnInit |
| `SetUIMgrProcessHotkeys` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIHotkey::CBFunctionHotkeyOnOk |
| `GetModeWidth` | 17 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::RenderTexture; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `GetModeHeight` | 17 | ohne Kandidat |  | Aufrufer im Client: AcUIBase::RenderTexture; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `RunFade` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnRender` | 26 | Kandidat unbestätigt | `0x005E7750` | Aufrufer im Client: AgcEngine::OnRender, AgcEngine::OnIdle, AgcWindow::WindowControlMessageProc; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `RenderFade` | 67 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::OnRender; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `_RunFade` | 40 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RenderFade; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `_DelayFade` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::RenderFade; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `_EventFadeFinsh` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIManager2::_RunFade; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `_CalcPosition` | 55 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CalcSize` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcRelativeToAbsolute` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcAbsoluteToRelative` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWriteUI` | 24 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamWrite` | 68 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::TemplateStreamWriteCB, AgcmItem::ItemTemplateStreamWriteCB, AgcmObject::ObjectTemplateStreamWriteCB; kein unbenannter Kandidat mit Beleg unter 362 unbenannten Funktionen im Klassenbereich |
| `StreamWriteAction` | 150 | Kandidat unbestätigt | `0x0062FAB0` | Aufrufer im Client: AgcmUIManager2::StreamWrite, AgcmUIManager2::StreamWriteControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |
| `StreamWriteButton` | 28 | Kandidat unbestätigt | `0x0062FAB0` | Aufrufer im Client: AgcmUIManager2::StreamWriteControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |
| `StreamWriteSkillTree` | 14 | Kandidat unbestätigt | `0x0062FAB0` | Aufrufer im Client: AgcmUIManager2::StreamWriteControl; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 2) |

## AgcmUINotice (gemeinsamer Rumpf 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `_HexStringToDWORD` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::_LoadColor, AgcChatMessage::_PushAndParseString, AgcmUINotice::_ParseMessage; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgcmUIOption (eingebaut 1, gemeinsamer Rumpf 2, ohne Kandidat 32, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Update3DProvider` | 13 | zugeordnet | `0x005DC630` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `AddOptionUserData` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::OnAddModule; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateAutoTuning` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBAutoTuning; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateDisableOtherPlayerSkillEffect` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBDisableOtherPlayerSkillEffect; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateWideView` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBWideView; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateLensFlare` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateNature, AgcmUIOption::CBLensFlare; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateFog` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateNature, AgcmUIOption::CBFog; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateSky` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateNature, AgcmUIOption::CBSky; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateShadowSelf` | 21 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateShadow, AgcmUIOption::CBShadowSelf; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateEffectField` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateEffect, AgcmUIOption::CBEffectField; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateCriminal` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::CBCriminal; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateWanted` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::CBWanted; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateMurderer` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::CBMurderer; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateEffectCombat` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateEffect, AgcmUIOption::CBEffectCombat; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateEffectUI` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateEffect, AgcmUIOption::CBEffectUI; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateUseEAX` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBUseEAX; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateSpeakerType` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBSpeakerType; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewNameMine` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewNameMine; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewNameMonster` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewNameMonster; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewNameGuild` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewNameGuild; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewNameParty` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewNameParty; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewNameOthers` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewNameOthers; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewHelpBaloonTip` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewHelpBaloonTip; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewHelpBaloonChat` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewHelpBaloonChat; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewHelpUclie` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewHelpUclie; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewSelfBars` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBViewSelfBars; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdatePartyBuffIcon` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBVisiblePartyBuffIcon; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewHelmet` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBVisibleViewHelmet; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `UpdateViewItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBVisibleViewItem |
| `UpdateUseNewSlot` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::UpdateGameOption, AgcmUIOption::CBUseNewSlot; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `CB3DProvider` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::OnAddModule; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SendOptionFlag` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::CBRefuseTrade, AgcmUIOption::CBRefusePartyIn, AgcmUIOption::CBRefuseGuildIn; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `CBDisplay3DProvider` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::OnAddModule; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `RefreshRefuseControl` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIOption::CBSettingCharacterOK, AgcmUIOption::CBUpdateOptionFlag, AgcmUIOption::CBSystemMessage; kein unbenannter Kandidat mit Beleg unter 3 unbenannten Funktionen im Klassenbereich |
| `SetCallbackChangeOptionUseNewSlot` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |

## AgcmUIParty (eingebaut 3, ohne Kandidat 7)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CBAcceptRecall` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::OnAddModule, AgcmUIParty::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBAcceptRecall` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::OnAddModule, AgcmUIParty::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBRejectRecall` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::OnAddModule, AgcmUIParty::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBRejectRecall` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::OnAddModule, AgcmUIParty::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBChangeLeader` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIParty::OnAddModule |
| `CBUpdateExpType` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::OnAddModule; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBUseSkillForMember` | 22 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `RefreshUserDataMemberInfo` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIParty::SetMemberInfo |
| `RefreshUserDataSelfInfo` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIParty::SetMemberInfo |
| `CBIsActiveDelegationLeader` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmUIParty::AddBoolean; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcmUIProduct (eingebaut 1, ohne Kandidat 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetGridItemAttachedTexture` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmCashMall::CreateDummyItem, AgcmItem::ItemInitCB, AgcmItem::CBLoadTemplate; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `RefreshSourceItemGrid` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProduct::DisplaySourceItem, AgcmUIProduct::ClearGrid, AgcmUIProduct::CBMoveItem; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBMoveItem` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventItemRepair::AddFunctions, AgcmUIGuildWarehouse::AddFunction, AgcmUIRefinery::AddFunction; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetComposeByIndex` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIProduct::CBOpenTooltip, AgcmUIProduct::CBClickListItem, AgcmUIProduct::CBDisplaySelectList |
| `GetMessageTxt` | 60 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBClickExpansion, AgcmUIGuildWarehouse::CBDisplayCaption; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetMessageTxt` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBClickExpansion, AgcmUIGuildWarehouse::CBDisplayCaption; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcmUIProductSkill (eingebaut 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsActiveBuyItem` | 26 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProductSkill::SetStatusBuyItem, AgcmUIProductSkill::CBBuyBuy, AgcmUIProductSkill::CBDisplayBuyPrice; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBDisplayName` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::OnRegisterCallBack, AgcmUIProductSkill::AddDisplay; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `Open` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StreamReadTemplate, AgcmCharacter::StreamReadTemplateAnimation, AgcmCharacter::StreamReadTemplateCustomize |

## AgcmUIQuest2 (eingebaut 5, nicht im Client 2, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RefreshMainTree` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIQuestJournal::CBClickJournalButton3, AgcmUIQuest2::RefreshQuestUI, AgcmUIQuest2::CBMainUIHotKeyOpen |
| `RefreshMainCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIQuest2::CBMainUIHotKeyOpen, AgcmUIQuest2::RequireQuestResult, AgcmUIQuest2::CompleteQuestResult |
| `RefreshAcceptLeftButton` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIQuest2::CBButtonQuestAcceptListClick |
| `RefreshAcceptLeftButtonEnable` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIQuest2::CBButtonQuestAcceptListClick, AgcmUIQuest2::RequireQuestResult, AgcmUIQuest2::CompleteQuestResult |
| `AddMessageResult` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIQuest2::CompleteQuestResult; kein unbenannter Kandidat mit Beleg unter 23 unbenannten Funktionen im Klassenbereich |
| `AddQuestPositionInfo` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcUIQuestText::MakeTextList; kein unbenannter Kandidat mit Beleg unter 23 unbenannten Funktionen im Klassenbereich |
| `DelQuestPositionInfo` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetQuestPosName` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcUIQuestText::CBPositionLinkEvent |
| `_GetTopQuestTID` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIQuestJournal (eingebaut 3, gemeinsamer Rumpf 2, nicht im Client 1, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RefreshJournalPosition` | 26 | zugeordnet | `0x0067B050` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_RefreshTempText` | 20 | zugeordnet | `0x0067ADB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_RefreshText` | 21 | zugeordnet | `0x0067ACA0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OpenJournalUI` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUILogin::OnIdle |
| `RefreshTempJournalAlpha` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIQuestJournal::OnIdle |
| `OnAddModule` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `_ClearTempText` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIQuestJournal::RefreshJournalInfo |
| `CBJournalPositionLinkEvent` | 45 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIRefinery (eingebaut 4, nicht als eigene Funktion 3, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Open` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::StreamReadTemplate, AgcmCharacter::StreamReadTemplateAnimation, AgcmCharacter::StreamReadTemplateCustomize; im Adressbereich der Klasse (0x006A0510–0x006A1CE0) ist keine unbenannte Funktion mehr übrig |
| `DestroyGrid` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIRefinery::OnDestroy; im Adressbereich der Klasse (0x006A0510–0x006A1CE0) ist keine unbenannte Funktion mehr übrig |
| `AddItemToSourceGrid` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIRefinery::OnMoveItem |
| `RemoveItemFromSourceGrid` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RefreshResultGrid` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIRefinery::OnSuccess, AgcmUIRefinery::ClearResultGrid |
| `SetGridItemAttachedTexture` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCashMall::CreateDummyItem, AgcmItem::ItemInitCB, AgcmItem::CBLoadTemplate; im Adressbereich der Klasse (0x006A0510–0x006A1CE0) ist keine unbenannte Funktion mehr übrig |
| `ClearSourceGrid` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIRefinery::Reset |
| `ClearResultGrid` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIRefinery::Reset |

## AgcmUIRemission (eingebaut 2, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Close` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBSocketOnError, AgcmLogin::CBSocketError, AgcWindow::Close |
| `CBKeydownESC` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmTargeting::OnAddModule, AgcmUICashInven::OnAddModule, AgcmUICouponBox::OnAddModule; im Adressbereich der Klasse (0x0069F760–0x006A02F0) ist keine unbenannte Funktion mehr übrig |
| `CBCloseWindow` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIProduct::AddFunction, AgcmUIRefinery::AddFunction, AgcmUIRemission::AddFunction; im Adressbereich der Klasse (0x0069F760–0x006A02F0) ist keine unbenannte Funktion mehr übrig |
| `GetMessageTxt` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBClickExpansion, AgcmUIGuildWarehouse::CBDisplayCaption |

## AgcmUISearch (eingebaut 2, gemeinsamer Rumpf 2, nicht im Client 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 4 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SendSearchCondition` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindClassName` | 107 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSearchFail` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSearchReultListSelect` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISearch::AddFunction |
| `AddSearchResultList` | 1 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OpenSearchResultUI` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISearch::CBSearchResult |
| `CloseSearchResultUI` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUIServerSelect (Kandidat unbestätigt 11, eingebaut 7, nicht im Client 1, ohne Kandidat 3, zugeordnet 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetUIMessage` | 8 | zugeordnet | `0x00743250` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnLoadServerList` | 117 | zugeordnet | `0x007444C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnServerClose` | 22 | zugeordnet | `0x007431B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnUpdateServerInfo` | 17 | zugeordnet | `0x00742FB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnRefresh` | 13 | zugeordnet | `0x00742F70` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInitialize` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIAccountCheck::AgcmUIAccountCheck, AgcmUIAccountCheck::~AgcmUIAccountCheck |
| `OnClear` | 14 | ohne Kandidat |  | Aufrufer im Client: CUiExNPCMsgBoxGrid::OnClearGridItem, AgcmUICharacterCreate::~AgcmUICharacterCreate, AgcmUICharacterCreate::OnInitialize; kein unbenannter Kandidat mit Beleg unter 28 unbenannten Funktionen im Klassenbereich |
| `OnSelectServer` | 10 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnClickListGroup` | 12 | Kandidat unbestätigt | `0x00744950` | Aufrufer im Client: AgcmUIServerSelect::CB_OnSelectServer, AgcmUIServerSelect::CB_OnClickList, AgcmUIServerSelect::CB_OnClickTree; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 14, Belegarten 3) |
| `OnClickListServer` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnChangeTreeState` | 17 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnChangeServerState` | 27 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnChangeServerCharacter` | 17 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnChangeServerAgeRate` | 27 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnChangeServerOpen` | 26 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `OnEnterCharacterSelect` | 54 | Kandidat unbestätigt | `0x00744950` | Aufrufer im Client: AgcmUIServerSelect::CB_OnSelectServer, AgcmUIServerSelect::CB_OnClickList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 11, Belegarten 3) |
| `GetCurrentApgdWorld` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUILogin::CBLoginMainCreateButtonClick, AgcmUILogin::CBLoginMainDeleteButtonClick |
| `GetServerAgpdWorld` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIServerSelect::GetCurrentApgdWorld, AgcmUIServerSelect::CB_OnSelectServer, AgcmUIServerSelect::CB_OnClickList |
| `GetGroupIndexByListIndex` | 15 | Kandidat unbestätigt | `0x00744950` | Aufrufer im Client: AgcmUIServerSelect::CB_OnSelectServer, AgcmUIServerSelect::CB_OnClickList, AgcmUIServerSelect::CB_OnClickTree; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetCurrentSelectIndex` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIServerSelect::CB_OnClickList |
| `GetServerGroupName` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIServerSelect::CB_OnDisplayServerName |
| `_DisableServerGroupFlag` | 10 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_ClearServerList` | 14 | Kandidat unbestätigt | `0x00743C10` | Aufrufer im Client: AgcmUIServerSelect::OnLoadServerList; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_GetServerGroup` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIServerSelect::OnChangeTreeState |
| `_GetServer` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUIServerSelect::OnChangeServerState, AgcmUIServerSelect::OnChangeServerCharacter, AgcmUIServerSelect::OnChangeServerAgeRate; kein unbenannter Kandidat mit Beleg unter 28 unbenannten Funktionen im Klassenbereich |
| `CB_IsActiveBtnBack` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIServerSelect::OnAddBoolean; kein unbenannter Kandidat mit Beleg unter 28 unbenannten Funktionen im Klassenbereich |
| `CB_IsClickedBtnTree` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIServerSelect::OnAddBoolean |

## AgcmUISiegeWar (eingebaut 2, gemeinsamer Rumpf 3, nicht im Client 14, ohne Kandidat 12)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `CBReceiveAttackGuildList` | 57 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBReceiveDefenseGuildList` | 61 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBIsFriendGuild` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CBIsEnemyGuild` | 18 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `CBChangeCharacterBindingRegion` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIMain::OnAddModule, AgcmUISiegeWar::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBInputSiegeWarMessage` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSiegeWarInfoEdit` | 32 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::CBInputSiegeWarMessage; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBDisplayDefenseGuildName` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddDisplay; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBDisplayDefenseGuildMasterName` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddDisplay; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBDisplayDefenseGuildPoint` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddDisplay; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBDisplayComboHour` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddDisplay; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBRepairAtkResTower` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddFunction; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBActiveAtkResTower` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddFunction; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBAtkResTowerDragDrop` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::AddFunction; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBGetSiegeWarInfoEditControl` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBGetRemainTimeEditControl` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSiegeWarInfoScrollUp` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBSiegeWarInfoScrollDown` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsInAttackGuild` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::CBIsFriendGuild, AgcmUISiegeWar::CBIsEnemyGuild; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `IsInDefenseGuild` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::CBIsFriendGuild, AgcmUISiegeWar::CBIsEnemyGuild; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `SetCallbackReceiveAttackGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `SetCallbackReceiveEnemyGuildList` | 2 | gemeinsamer Rumpf |  | SetCallback-Einzeiler; identische Rümpfe werden vom Linker zusammengefaltet |
| `OpenSiegeWarInfo` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CloseSiegeWarInfo` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRemainTime` | 16 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetInfoEdit` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISiegeWar::OnIdle |
| `SetUseCharName` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `UpdateSiegeWarInfoUI` | 26 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_SetMessageText` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUISiegeWar::SetInfoEdit; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `_SetMsgTextToEditBox` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUISiegeWar::CBSiegeWarInfoScrollUp, AgcmUISiegeWar::CBSiegeWarInfoScrollDown |

## AgcmUISkill2 (Kandidat unbestätigt 3, eingebaut 4, nicht im Client 2, ohne Kandidat 10, zugeordnet 10)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetSkillToolTipInfo` | 25 | zugeordnet | `0x00776F10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCostWithTax` | 11 | zugeordnet | `0x00772DC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillBookTooltip` | 108 | zugeordnet | `0x00772920` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipEADamageAttribute` | 129 | zugeordnet | `0x007723A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipFactorPercent` | 624 | zugeordnet | `0x00770900` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipDamageAttribute` | 503 | zugeordnet | `0x0076D750` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetSkillToolTipName` | 81 | zugeordnet | `0x0076C180` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveHeroicSkill` | 15 | zugeordnet | `0x006CEBC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RemoveArchlordSkill` | 10 | zugeordnet | `0x006CEB60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMasteryArchlord` | 69 | zugeordnet | `0x006CCE90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SetMasteryHeroic` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkill2::SetMastery |
| `CBOpenSkillUpgradeUI` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::AddFunction; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `AddHeroicSkill` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBAddSkill; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `GetUpdateFactor` | 60 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetRecastSkillTimeToGridItem` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProductSkill::CBReceiveSkillAction, AgcmUISkill2::CBReceiveSkillAction; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `CBBuySkillResult` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::OnAddModule; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `IsActiveBuyItem` | 64 | ohne Kandidat |  | Aufrufer im Client: AgcmUIProductSkill::IsActiveBuyItem, AgcmUIProductSkill::SetStatusBuyItem, AgcmUIProductSkill::CBBuyBuy; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `IsActiveUpgradeItem` | 44 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBIsActiveUpgradeButton, AgcmUISkill2::SetStatusActiveUpgradeItem, AgcmUISkillDragonScion::_LoadScionSkillBuy; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `OpenSkillUI` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBOpenSkillUI, AgcmUISkill2::CBToggleSkillUI, AgcmUISkillDragonScion::CallBackGetBaseControlScion; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `RefreshInitButton` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::_LoadScionSkillBuy, AgcmUISkillDragonScion::_LoadSlayerSkillBuy, AgcmUISkillDragonScion::_LoadObiterSkillBuy |
| `CloseSkillToolTip` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::CBCloseScionSkillToolTip, AgcmUISkillDragonScion::CBCloseUpgradeScionSkillToolTip, AgcmUISkillDragonScion::CBCloseBuyScionSkillToolTip |
| `SetSkillToolTipInfo` | 46 | Kandidat unbestätigt | `0x007767E0` | Aufrufer im Client: AgcmUISkill2::OpenSkillToolTip, AgcmUISkill2::SetSkillToolTipCurrentLevel, AgcmUISkill2::SetSkillToolTipNextLevel; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `SetSkillToolTipAttribute` | 19 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetSkillToolTipCurrentLevel` | 59 | Kandidat unbestätigt | `0x00776C10` | Aufrufer im Client: AgcmUISkill2::SetSkillToolTipInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `SetSkillToolTipNextLevel` | 74 | Kandidat unbestätigt | `0x00776C10` | Aufrufer im Client: AgcmUISkill2::SetSkillToolTipInfo, AgcmUISkill2::SetSkillTemplateToolTipInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 13, Belegarten 3) |
| `SetSkillScrollTooltip` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkill2::CBSetItemTooltip |
| `CBCloseSkillDescToolTip` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::AddFunction; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `_GetDurationTime` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |
| `_GetBuffedSkill` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBOpenSkillDescToolTip; kein unbenannter Kandidat mit Beleg unter 1518 unbenannten Funktionen im Klassenbereich |

## AgcmUISkillDragonScion (Kandidat unbestätigt 15, eingebaut 10, nicht im Client 1, ohne Kandidat 22, zugeordnet 15)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_GetCharacterTID` | 11 | zugeordnet | `0x00784EA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckRollbackSkill` | 28 | zugeordnet | `0x00784BD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `IsActiveUpgradeItem` | 73 | zugeordnet | `0x00786CB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetPassiveSkill` | 22 | zugeordnet | `0x00786440` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetSummernerSkill` | 22 | zugeordnet | `0x00786380` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetObiterSkill` | 22 | zugeordnet | `0x007862C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetSlayerSkill` | 22 | zugeordnet | `0x00786200` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetScionSkill` | 22 | zugeordnet | `0x00786140` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_LoadArchlordSkill` | 59 | zugeordnet | `0x00786EA0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OpenSkillUI` | 4 | zugeordnet | `0x00788220` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetSummernerSkillPoint` | 31 | zugeordnet | `0x00786BB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_GetPassiveSkillPoint` | 31 | zugeordnet | `0x00786AB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_GetSlayerSkillPoint` | 31 | zugeordnet | `0x007869B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_GetObiterSkillPoint` | 31 | zugeordnet | `0x007868B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_GetScionSkillPoint` | 31 | zugeordnet | `0x007867B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnAddBoolean` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUILogin::AddUserData |
| `OnOpenUI` | 30 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::CallBack_RecvTitleOpenUI, AgcmTitle::CallBack_OnOpenUIAll, AgcmTitle::CallBack_OnOpenUICurrent; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `UnSelectSkillUI` | 11 | Kandidat unbestätigt | `0x00786500` | Aufrufer im Client: AgcmUISkillDragonScion::CBSelectScionSkillGrid, AgcmUISkillDragonScion::CBSelectSlayerSkillGrid, AgcmUISkillDragonScion::CBSelectObiterSkillGrid; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `UnSelectUpgradeSkillUI` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::CBSelectBuyScionSkillGrid, AgcmUISkillDragonScion::CBSelectUpgradeScionSkillGrid, AgcmUISkillDragonScion::CBSelectBuySlayerSkillGrid; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `_UnSelectSkillScion` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::UnSelectSkillUI |
| `_UnSelectSkillSlayer` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::UnSelectSkillUI |
| `_UnSelectSkillObiter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::UnSelectSkillUI |
| `_UnSelectSkillSummerner` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::UnSelectSkillUI |
| `_UnSelectSkillPassive` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::UnSelectSkillUI |
| `_UnSelectSkillArchlord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISkillDragonScion::UnSelectSkillUI |
| `LoadSkill` | 12 | Kandidat unbestätigt | `0x00787E70` | Aufrufer im Client: AgcmUISkillDragonScion::OnOpenUI, AgcmUISkillDragonScion::CBBuyScionSkillResult, AgcmUISkillDragonScion::CBUpgradeScionSkillResult; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `LoadBuySkill` | 11 | Kandidat unbestätigt | `0x00787E70` | Aufrufer im Client: AgcmUISkillDragonScion::OnOpenUpUI, AgcmUISkillDragonScion::CBBuyScionSkillResult, AgcmUISkillDragonScion::CBUpgradeScionSkillResult; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `OnCloseUI` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmTitle::CallBack_AutoCloseByCharacterMove, AcUIBase::CloseUI, AgcmUISkillDragonScion::OpenSkillUI; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `OnOpenUpUI` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OpenSkillUpUI; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `OnCloseUpUI` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OpenSkillUpUI, AgcmUISkillDragonScion::CloseSkillUpUI; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `OpenSkillUpUI` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillBuyUI, AgcmUISkill2::CBOpenSkillHighLevelUI, AgcmUISkill2::CBOpenSkillHighLevelSkillUpgradeUI |
| `CloseSkillUI` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISkill2::CBOpenSkillUI, AgcmUISkill2::CBToggleSkillUI, AgcmUISkillDragonScion::OnDestroy |
| `CloseSkillUpUI` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUISkill2::CBSelfUpdatePosition, AgcmUISkillDragonScion::OnDestroy, AgcmUISkillDragonScion::CBCloseScionUPSkillUI |
| `_LoadScionSkill` | 70 | Kandidat unbestätigt | `0x00787090` | Aufrufer im Client: AgcmUISkillDragonScion::LoadSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadSlayerSkill` | 70 | Kandidat unbestätigt | `0x00785700` | Aufrufer im Client: AgcmUISkillDragonScion::LoadSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadObiterSkill` | 70 | Kandidat unbestätigt | `0x00787620` | Aufrufer im Client: AgcmUISkillDragonScion::LoadSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadSummernerSkill` | 70 | Kandidat unbestätigt | `0x007878E0` | Aufrufer im Client: AgcmUISkillDragonScion::LoadSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadPassiveSkill` | 70 | Kandidat unbestätigt | `0x00787BB0` | Aufrufer im Client: AgcmUISkillDragonScion::LoadSkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadScionSkillBuy` | 74 | Kandidat unbestätigt | `0x00787090` | Aufrufer im Client: AgcmUISkillDragonScion::LoadBuySkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadSlayerSkillBuy` | 82 | Kandidat unbestätigt | `0x00785700` | Aufrufer im Client: AgcmUISkillDragonScion::LoadBuySkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadObiterSkillBuy` | 77 | Kandidat unbestätigt | `0x00787620` | Aufrufer im Client: AgcmUISkillDragonScion::LoadBuySkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadSummernerSkillBuy` | 81 | Kandidat unbestätigt | `0x007878E0` | Aufrufer im Client: AgcmUISkillDragonScion::LoadBuySkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_LoadPassiveSkillBuy` | 75 | Kandidat unbestätigt | `0x00787BB0` | Aufrufer im Client: AgcmUISkillDragonScion::LoadBuySkill; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `_GetSkillIndex` | 24 | Kandidat unbestätigt | `0x00786500` | Aufrufer im Client: AgcmUISkillDragonScion::CBSelectScionSkillGrid, AgcmUISkillDragonScion::CBSelectBuyScionSkillGrid, AgcmUISkillDragonScion::CBSelectUpgradeScionSkillGrid; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_GetSkill` | 23 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::IsActiveUpgradeItem; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `IsCurScionWindowOpen` | 33 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkill2::CBOpenSkillUI; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `_MoveSkillWindow` | 12 | Kandidat unbestätigt | `0x00787FE0` | Aufrufer im Client: AgcmUISkill2::SetMastery, AgcmUISkill2::CBSetBuyMastery0, AgcmUISkill2::CBSetBuyMastery1; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_MoveSkillUpgradeWindow` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnOpenUpUI; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `_GetUI` | 31 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::_MoveSkillWindow, AgcmUISkillDragonScion::_MoveSkillUpgradeWindow; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectBuyScionSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectUpgradeScionSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectBuySlayerSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectUpgradeSlayerSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectBuyObiterSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectUpgradeObiterSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectBuyPassiveSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectUpgradePassiveSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectBuySummernerSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBSelectUpgradeSummernerSkillGrid` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBCloseScionSkillToolTip` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBCloseUpgradeScionSkillToolTip` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBCloseBuyScionSkillToolTip` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUISkillDragonScion::OnAddFunction; kein unbenannter Kandidat mit Beleg unter 628 unbenannten Funktionen im Klassenbereich |
| `CBUpdateScionCost` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmUISocialAction (eingebaut 5, gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnIdle` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnSocialUIOpen` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUISocialAction::CBSocialActionOpenUI, AgcmUISocialAction::CBSocialActionToggleUI |
| `OnSocialUIClose` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUISocialAction::CBSocialActionCloseUI, AgcmUISocialAction::CBSocialActionToggleUI |
| `CBSocialActionDragDrop` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISocialAction::OnAddModule |
| `CBSocialActionRClick` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUISocialAction::OnAddModule |
| `ActionStart` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUISocialAction::CBSocialActionDLClick, AgcmUISocialAction::CBSocialActionRClick |

## AgcmUISplitItem (eingebaut 1, gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `AddDisplay` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddDisplay, AgcmMinimap::OnAddModule |

## AgcmUIStatus (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUITax (eingebaut 3, gemeinsamer Rumpf 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 10 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `TestOpenSteward` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUITax::OnInit |
| `TestOpenModifyRatio` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUITax::OnInit |
| `TestRequestIncome` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUITax::OnInit |
| `CBReleaseCharacter` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUITax::OnAddModule, AgcmUIWantedCriminal::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `CBKeydownESC` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmTargeting::OnAddModule, AgcmUICashInven::OnAddModule, AgcmUICouponBox::OnAddModule; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgcmUITips (gemeinsamer Rumpf 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |

## AgcmUIWantedCriminal (eingebaut 2, gemeinsamer Rumpf 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 9 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `TestOpenBoard` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIWantedCriminal::OnInit |
| `TestOpenArrange` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWantedCriminal::OnInit; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `CBReleaseCharacter` | 11 | ohne Kandidat |  | Aufrufer im Client: AgcmUITax::OnAddModule, AgcmUIWantedCriminal::OnAddModule; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetMessageTxt` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIGuildWarehouse::CBExpandResult, AgcmUIGuildWarehouse::CBClickExpansion, AgcmUIGuildWarehouse::CBDisplayCaption |

## AgcmUIWarInfo (gemeinsamer Rumpf 3, ohne Kandidat 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `UpdateCenterMessage` | 33 | zugeordnet | `0x0068BB20` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnDestroy` | 2 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnInit` | 3 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `OnIdle` | 16 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `SetStepMessage` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmWarInfo::CBOperationUpdateWarState; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## AgcmUIWorldmap (eingebaut 4, ohne Kandidat 7, zugeordnet 12)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCastleInfomation` | 18 | zugeordnet | `0x0067C2D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnUpdateCastleInfo` | 56 | zugeordnet | `0x0067D8E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `S_Close` | 4 | zugeordnet | `0x0067C0A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_ChangeMap` | 23 | zugeordnet | `0x0067D270` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RemovePoint` | 5 | zugeordnet | `0x0067C040` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetGroupIndex` | 11 | zugeordnet | `0x0067C740` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetCastleOwnerGuildMarkSimbol` | 8 | zugeordnet | `0x0067D220` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCastleOwnerGuildMarkPattern` | 8 | zugeordnet | `0x0067D1D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCastleOwnerGuildMarkBG` | 8 | zugeordnet | `0x0067D180` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCastleOwnerGuild` | 11 | zugeordnet | `0x0067D110` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `S_ChangeMap` | 101 | zugeordnet | `0x0067CA80` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddPoint` | 29 | zugeordnet | `0x0067C9B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddBoolean` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIBuddy::OnAddModule, AgcmUICashInven::OnAddModule |
| `AllHideControl` | 14 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `ShowControl` | 27 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `RemovePoint` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmMinimap::RemovePoint, AgcmMinimap::RemovePointGroup, AgcmMinimap::DestroyMapPosition |
| `OpenWorldMap` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::CBWorldMapToggle, AgcmUIWorldmap::CBBindingRegionChange, AgcmUIQuestJournal::CBClickJournalButton2; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `CloseWorldMap` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::CBWorldMapToggle; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `OnGetControls` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::S_ChangeMap; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `OnUpdateGuildMarkTexture` | 74 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::OnUpdateCastleInfo; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `RenderButton` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmUIWorldmap::OnUpdateGuildMarkTexture; kein unbenannter Kandidat mit Beleg unter 30 unbenannten Funktionen im Klassenbereich |
| `GetCastleOwnerGuildName` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnUpdateCastleInfo, AgcmUIWorldmap::GetCastleOwnerGuild |
| `GetCastleOwnerGuildMasterName` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnUpdateCastleInfo |

## AgcmUVAnimation (nicht als eigene Funktion 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `IsVaildUVAnimation` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUVAnimation::UpdateUVAnimation; im Adressbereich der Klasse (0x006DC490–0x006DCA50) ist keine unbenannte Funktion mehr übrig |
| `CallBack_DeleteAtomic` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUVAnimation::CallBack_RemoveAtomic; im Adressbereich der Klasse (0x006DC490–0x006DCA50) ist keine unbenannte Funktion mehr übrig |
| `Callback_UVConstructor` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcmWater (eingebaut 3, nicht als eigene Funktion 11, nicht im Client 17)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `onLostDevice` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `onResetDevice` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CB_W1Update` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CB_W1Release` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CB_W2Release` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReleaseWave` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmWater::DeleteAll, AgcmWater::JobQueueRemoveAll, AgcmWater::JobQueueRemove |
| `AddWater` | 241 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeleteWater` | 47 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ChangeWater` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddWave` | 60 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::AutoMakeWave; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `AutoMakeWave` | 270 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::AddWater, AgcmWater::RemoveWaterRange; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `DeleteWave` | 49 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetWaterType` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetWaterStatus` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveToFiles` | 222 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmRender::SaveAllOctrees; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `RemoveWaterRange` | 160 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ChangeStatus` | 155 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SkinAtomicDraw` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::ImmediateHWaterAtomicListRender, AgcmWater::ImmediateHWaterAtomicRender; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `ImmediateHWaterAtomicListRender` | 79 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::UpdateReflectionMap; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `ImmediateHWaterAtomicRender` | 44 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::UpdateReflectionMap; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `ImmediateHWaterTerrainRender` | 32 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::UpdateReflectionMap; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `sgn` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmWater::ModifyD3DProjectionMatrix |
| `ModifyD3DProjectionMatrix` | 61 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::UpdateReflectionMap; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `RemoveHWaterFromRender` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::DeleteAll, AgcmWater::RemoveWaterRange, AgcmWater::ChangeHWaterMode; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `ReleaseHWater` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::DeleteAll, AgcmWater::RemoveWaterRange, AgcmWater::ChangeHWaterMode; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `CB_POST_RENDER` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmGlyph::OnAddModule, AgcmGlyph::CB_POST_RENDER, AgcmLensFlare::OnAddModule |
| `CB_HWRelease` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeHWaterFromWater` | 282 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmWater::OnIdle, AgcmWater::SetWaterDetail, AgcmWater::ChangeHWaterStatus; im Adressbereich der Klasse (0x00642D40–0x00649230) ist keine unbenannte Funktion mehr übrig |
| `ChangeHWaterStatus` | 70 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveStatusInfoT1ToINI` | 182 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SaveHWaterStatusToINI` | 142 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcuCamDampingForce (eingebaut 4, nicht als eigene Funktion 7, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetInst` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `bAddOmega` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `bAddOmegaX` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCamera2::bRotCX, AgcuCamDampingForce::bAddOmega; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |
| `bAddOmegaY` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCamera2::bRotWY, AgcuCamDampingForce::bAddOmega; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |
| `bAddZoomSpeed` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCamera2::bZoom; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |
| `bOnIdle` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default, AgcmCamera2::vOnIdle_modechage, AgcuCamMode::bOnIdle; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |
| `vUdtMaskOn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `vUdtMaskOff` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bOnMoveTarget, AgcmCamera2::vOnIdle_default, AgcmCamera2::vForcedZoom |
| `vUdtMaskChk` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bTurnWY_180, AgcmCamera2::vOnIdle_default |
| `vOnIdleOmegaX` | 23 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuCamDampingForce::bOnIdle; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |
| `vOnIdleOmegaY` | 21 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuCamDampingForce::bOnIdle; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |
| `vOnIdleZoom` | 24 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuCamDampingForce::bOnIdle; im Adressbereich der Klasse (0x00795AE0–0x00795AE0) ist keine unbenannte Funktion mehr übrig |

## AgcuCamMode (eingebaut 2, nicht im Client 2, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetCameraInfo` | 89 | zugeordnet | `0x0078E930` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `bOnIdle` | 17 | zugeordnet | `0x0078E850` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `bChageMode` | 62 | zugeordnet | `0x0078E590` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `bGetInst` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `bGetCurrModeData` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddCameraInfo` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReloadCamSetting` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CChatCmd::CallBack_OnReloadCamSetting |

## AgcuCamSpringForce (eingebaut 9, nicht als eigene Funktion 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bGetInst` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `bOnReleaseLinearSpring` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCamera2::vOnIdle_default |
| `bOnReleaseSpiralSpring` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCamera2::vOnIdle_default; im Adressbereich der Klasse (0x00795850–0x00795850) ist keine unbenannte Funktion mehr übrig |
| `bOnMoveCharac` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCamera2::bOnMoveTarget; im Adressbereich der Klasse (0x00795850–0x00795850) ist keine unbenannte Funktion mehr übrig |
| `bOnIdle` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::vOnIdle_default, AgcmCamera2::vOnIdle_modechage, AgcuCamDampingForce::bOnIdle |
| `vOnIdleExt` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuCamSpringForce::bOnIdle; im Adressbereich der Klasse (0x00795850–0x00795850) ist keine unbenannte Funktion mehr übrig |
| `bOptFlagOn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::OptionFromFile, AgcuCamMode::bChageMode |
| `bOptFlagOff` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::OptionFromFile, AgcuCamMode::bChageMode |
| `vOptFlagChk` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `vUdtMaskOn` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bRotCX, AgcmCamera2::bZoom |
| `vUdtMaskOff` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bOnMoveTarget, AgcmCamera2::vOnIdle_default, AgcmCamera2::vForcedZoom |
| `vUdtMaskChk` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::bRotWY, AgcmCamera2::bTurnWY_180, AgcmCamera2::vOnIdle_default |

## AgcuEffBaseCtrlCreater (eingebaut 1, nicht im Client 11)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_Create_Board` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_PSyst` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_PSystSBH` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_Tail` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_Object` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_Light` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_Sound` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_MFrm` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_TerrainB` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_PostFX` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Create_Camera` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DestroyCtrl` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Set::Clear, AgcdEffCtrl_Set::Render |

## AgcuEffIniMng (Kandidat unbestätigt 12, eingebaut 4, nicht im Client 2, ohne Kandidat 24, zugeordnet 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_Read_EffRenderBase_txt` | 38 | zugeordnet | `0x00798610` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_Read_EffBase_txt` | 55 | zugeordnet | `0x00798540` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Read_txt` | 18 | zugeordnet | `0x0079AC60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_Read_EffAnim_Colr_txt` | 61 | zugeordnet | `0x0079A660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_Read_EffLight_txt` | 99 | zugeordnet | `0x0079A2D0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_Read_EffObj_txt` | 76 | zugeordnet | `0x0079A170` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_Read_EffPSysSBH_txt` | 109 | zugeordnet | `0x00799F40` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_Read_EffPSys_txt` | 209 | zugeordnet | `0x00799B60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_Read_EffTail_txt` | 69 | zugeordnet | `0x007999F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `_FindSect` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_FindKey` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Read_EffSet_txt` | 345 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::Read_txt, AgcuEffIniMng::Read_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 2) |
| `_Read_EffBoard_txt` | 38 | Kandidat unbestätigt | `0x00799970` | Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `_Read_EffTerrainB_txt` | 38 | Kandidat unbestätigt | `0x00799970` | Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `_Read_EffPostFX_txt` | 114 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Read_EffSound_txt` | 31 | Kandidat unbestätigt | `0x0079A4D0` | Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `_Read_EffMFrm_txt` | 70 | Kandidat unbestätigt | `0x0079A4D0` | Aufrufer im Client: AgcuEffIniMng::_Read_EffSet_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `_Read_EffAnim_Base_txt` | 78 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::_Read_EffBoard_txt, AgcuEffIniMng::_Read_EffTerrainB_txt, AgcuEffIniMng::_Read_EffTail_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 14, Belegarten 3) |
| `_Read_EffAnim_TuTv_txt` | 60 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `_Read_EffAnim_PostFX_txt` | 59 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_Read_EffAnim_Missile_txt` | 39 | Kandidat unbestätigt | `0x0079A4D0` | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `_Read_EffAnim_Linear_txt` | 60 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `_Read_EffAnim_Rev_txt` | 74 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `_Read_EffAnim_Rot_txt` | 71 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `_Read_EffAnim_RpSpline_txt` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Read_EffAnim_RtAnim_txt` | 24 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Read_EffAnim_Scale_txt` | 58 | Kandidat unbestätigt | `0x00799690` | Aufrufer im Client: AgcuEffIniMng::_Read_EffAnim_Base_txt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 8, Belegarten 2) |
| `Write_txt` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniExporter::bSaveFile; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffSet_txt` | 164 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::Write_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffBase_txt` | 50 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffSet_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffRenderBase_txt` | 20 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffBoard_txt` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt |
| `_Write_EffTerrainB_txt` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt |
| `_Write_EffPostFX_txt` | 73 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffTail_txt` | 49 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffPSys_txt` | 224 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffPSysSBH_txt` | 84 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffObj_txt` | 28 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffLight_txt` | 79 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffSound_txt` | 59 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffMFrm_txt` | 70 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_Base_txt` | 59 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_Colr_txt` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_TuTv_txt` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_Missile_txt` | 51 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_Linear_txt` | 36 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_Rev_txt` | 49 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_Rot_txt` | 47 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `_Write_EffAnim_RpSpline_txt` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt |
| `_Write_EffAnim_RtAnim_txt` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt |
| `_Write_EffAnim_Scale_txt` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcuEffIniMng::_Write_EffAnim_Base_txt; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |

## AgcuEffVBMng (eingebaut 7, ohne Kandidat 2, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RenderParticle` | 32 | zugeordnet | `0x00760DD0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenderTerrainBoard` | 138 | zugeordnet | `0x00760F90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Clear` | 19 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::CharacterConstructor, AgcmCharacter::SetTemplateClumpRenderType, AgcdEffCtrl_Set::~AgcdEffCtrl_Set; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `InitVB` | 141 | ohne Kandidat |  | Aufrufer im Client: AgcmEff2::OnInit; kein unbenannter Kandidat mit Beleg unter 14 unbenannten Funktionen im Klassenbereich |
| `RenderBoard` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrl_Board::Render |
| `RenderTail` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrl_Tail::Render |
| `LockVB_Board` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Board::Render, AgcuEffVBMng::InitVB |
| `LockVB_Particle` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::_RenderVS, AgcdEffCtrl_ParticleSysTem::_RenderFP, AgcdEffCtrl_ParticleSyst_SBH::Render |
| `LockVB_ParticleExtra` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_ParticleSysTem::_RenderVS |
| `LockVB_Tail` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_Tail::Render |
| `LockVB_TerrainBaord` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcdEffCtrl_TerrainBoard::Render |

## AgcuPathDoubleSpline (eingebaut 2, ohne Kandidat 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bInitSpline` | 51 | ohne Kandidat |  | Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `bInitSpline` | 17 | ohne Kandidat |  | Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `bSetActType` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting |
| `bSetAccel` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting |
| `vGetMatrix` | 94 | ohne Kandidat |  | Aufrufer im Client: AgcuPathDoubleSpline::bOnIdle; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `vGetEye` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcuPathDoubleSpline::vGetMatrix; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `vGetLookat` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcuPathDoubleSpline::vGetMatrix; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |

## AgcuPathSingleSpline (Kandidat unbestätigt 4, eingebaut 3, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bInitSpline` | 29 | ohne Kandidat |  | Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `bInitSpline` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `bSetFixedLookat` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcuPathWork::Load |
| `bSetActType` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting |
| `bSetAccel` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcuPathWork::Load, AcUIGacha::LoadGachaSetting |
| `vGetMatrix_flight` | 9 | Kandidat unbestätigt | `0x00796EE0` | Aufrufer im Client: AgcuPathSingleSpline::bOnIdle, AgcuPathSingleSpline::bOnIdleOffset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `vGetMatrix_sideParallelXzplane` | 21 | Kandidat unbestätigt | `0x00796EE0` | Aufrufer im Client: AgcuPathSingleSpline::bOnIdle, AgcuPathSingleSpline::bOnIdleOffset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `vGetMatrix_upWorldUp` | 33 | Kandidat unbestätigt | `0x00796EE0` | Aufrufer im Client: AgcuPathSingleSpline::bOnIdle, AgcuPathSingleSpline::bOnIdleOffset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `vGetMatrix_fixedLookat` | 60 | Kandidat unbestätigt | `0x00796EE0` | Aufrufer im Client: AgcuPathSingleSpline::bOnIdle, AgcuPathSingleSpline::bOnIdleOffset; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |

## AgcuPathWork (nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `bOnIdleSetKeyTime` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `Load` | 181 | ohne Kandidat |  | Aufrufer im Client: AgcuPathWork::CreateSplinePath, AgcuEffBaseCtrlCreater::CreateCtrl, AcMapLoader::OnIdleLoad; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `CreateSplinePath` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgcuUIControlCamera (eingebaut 1, nicht als eigene Funktion 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnUpdate` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OnIdle; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `OnChangeMode` | 41 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OnIdle, AgcmUILogin::SetLoginMode; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `OnChangeRace` | 31 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::CreateCharacter; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `OnClickBtnZoom` | 45 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnToggleZoom; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `SetCameraAndNature` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUILogin::OnInit, AgcmUILogin::CBReturnToLoginEndProcess |
| `_UpdateCharacterCreate` | 32 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCamera::OnUpdate; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `_UpdateCameraAndNature` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCamera::OnChangeMode, AgcuUIControlCamera::OnChangeRace; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `_UpdateCameraZoom` | 31 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCamera::_UpdateCharacterCreate; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |
| `_IsValidRaceAndClassType` | 20 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCamera::OnChangeRace; im Adressbereich der Klasse (0x00609CB0–0x00609CB0) ist keine unbenannte Funktion mehr übrig |

## AgcuUIControlCharacter (eingebaut 7, nicht als eigene Funktion 12, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnUpdate` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OnIdle; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `OnChangeMode` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OnIdle, AgcmUILogin::SetLoginMode; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `OnClearCharacter` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUILogin::DeleteAllMyCharacter |
| `OnAddCharacter` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUICharacterSelect::_MakeCharacter, AgcmUILogin::CBAddCharacter; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `OnDeleteCharacter` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUILogin::CBRemoveCharacter |
| `OnDeleteCharacter` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::CBRemoveCharacter; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `OnDoubleClickCharacter` | 22 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUICharacterSelect::OnBtnSlot, AgcmUILogin::CharacterClick, AgcmUILogin::CharacterDoubleClick; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `OnRotateStartLeft` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnRotateLeft |
| `OnRotateStartRight` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnRotateRight |
| `OnRotateEnd` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmUICharacterCreate::CB_OnBtnRotateEnd |
| `InitializeCreateCharacter` | 34 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::CreateCharacter; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `SetExternalClassPointers` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUILogin::OnInit, AgcmUILogin::CBReturnToLoginEndProcess |
| `GetCurrSelectCharacter` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCharacterController` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCharacter::CallBackSelectAnimationEnd; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `GetSelectAnimationType` | 54 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventEffect::StartSelectionAnimation; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `_UpdateModeCharacterCreate` | 31 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCharacter::OnUpdate; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `_SelectCharacter` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCharacter::OnDoubleClickCharacter; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `_UnSelectCharacter` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCharacter::OnDoubleClickCharacter, AgcuUIControlCharacter::UnSelectCharacter; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `CallBackSelectAnimationEnd` | 29 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuUIControlCharacter::_SelectCharacter, AgcuUIControlCharacter::_UnSelectCharacter; im Adressbereich der Klasse (0x0060F4F0–0x0060F4F0) ist keine unbenannte Funktion mehr übrig |
| `UnSelectCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUILogin::RemoveSelectedMyCharacter |

## AgcuUIControlPostFX (nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInitialzie` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OnAddModule; im Adressbereich der Klasse (0x00609CE0–0x00609CE0) ist keine unbenannte Funktion mehr übrig |
| `OnUpdate` | 32 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OnIdle; im Adressbereich der Klasse (0x00609CE0–0x00609CE0) ist keine unbenannte Funktion mehr übrig |
| `OnStartPostFX` | 27 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::SetLoginMode; im Adressbereich der Klasse (0x00609CE0–0x00609CE0) ist keine unbenannte Funktion mehr übrig |
| `OnStopPostFX` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUILogin::OpenLoadingWindow, AgcmUILogin::CBMapLoadSector; im Adressbereich der Klasse (0x00609CE0–0x00609CE0) ist keine unbenannte Funktion mehr übrig |

## AgcuUILoadingWindow (Kandidat unbestätigt 1, ohne Kandidat 1, zugeordnet 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnRefresh` | 13 | zugeordnet | `0x007490B0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnClose` | 22 | zugeordnet | `0x00749480` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnOpen` | 21 | zugeordnet | `0x007493E0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnInitialize` | 9 | Kandidat unbestätigt | `0x00748450` | Aufrufer im Client: AgcEngine::OnMessageSink, AgcmUIAccountCheck::AgcmUIAccountCheck, AgcmUIAccountCheck::~AgcmUIAccountCheck; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `OnUpdateAdd` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmUILogin::CBAddCharacter; kein unbenannter Kandidat mit Beleg unter 1958 unbenannten Funktionen im Klassenbereich |

## AgpaAuctionSales (eingebaut 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Remove` | 5 | zugeordnet | `0x00592360` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |

## AgpaChannel (eingebaut 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |

## AgpaCharacter (Kandidat unbestätigt 1, eingebaut 4, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCharacter` | 7 | zugeordnet | `0x00589FE0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetCharacter` | 7 | Kandidat unbestätigt | `0x0058A270` | Aufrufer im Client: AgcmCamera2::CBOnTargetSet, AgcmCharacter::ActionSelfCharacter, AgcmCharacter::LockTarget; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `AddCharacter` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::AttachRide, AgcmShrine::_ChangeShrineObject, stAutoPickUpSettings::AddCharacter |
| `RemoveCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::OnIdle, AgcmCharacter::CBInitCharacter, AgcmCharacter::CBRemoveCharacter |
| `IsCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::IsCharacter, AgpmCharacter::IsCharacter |
| `IsCharacter` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::IsCharacter, AgpmCharacter::IsCharacter |

## AgpaCharacterTemplate (eingebaut 2, nicht als eigene Funktion 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCharacterTemplate` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAIScreamEditDlg::OnInitDialog, AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcuCamMode::SetCameraInfo; im Adressbereich der Klasse (0x0058A090–0x0058A160) ist keine unbenannte Funktion mehr übrig |
| `GetCharacterTemplate` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAIScreamEditDlg::OnInitDialog, AgcmAIScreamEditDlg::OnAiScreamOkButton, AgcuCamMode::SetCameraInfo; im Adressbereich der Klasse (0x0058A090–0x0058A160) ist keine unbenannte Funktion mehr übrig |
| `RemoveCharacterTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::RemoveCharacterTemplate, AgpmCharacter::RemoveAllCharacterTemplate, AgpmCharacter::RemoveCharacterTemplate |
| `AddTemplateStringKey` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::TemplateReadCB, AgpmShrine::TemplateReadCB, AgpmSkill::TemplateReadCB |
| `LoadTemplateFromIni` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpaComposeTemplate (eingebaut 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |

## AgpaGuild (Kandidat unbestätigt 1, nicht als eigene Funktion 3, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddGuild` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmGuild::AddGuild, AgpmGuild::CreateGuild, AgpmGuild::DestroyGuild; im Adressbereich der Klasse (0x00552920–0x00552920) ist keine unbenannte Funktion mehr übrig |
| `RemoveGuild` | 22 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmGuild::RemoveGuild, AgpmGuild::DestroyGuild, AgpmGuild::DestroyGuildFromRemoveAdmin; im Adressbereich der Klasse (0x00552920–0x00552920) ist keine unbenannte Funktion mehr übrig |
| `GetGuild` | 17 | Kandidat unbestätigt | `0x00551BD0` | Aufrufer im Client: AgcmGuild::IsGuildBattle, AgcmGuild::IsGuildBattleMember, AgcmUIWorldmap::GetCastleOwnerGuild; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `SortGuildMemberDesc` | 64 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `IsGuildMasterVisitMaxTermOver` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgpaGuild::SortGuildMemberDesc, AgpmGuild::MakeGuildListPacket; im Adressbereich der Klasse (0x00552920–0x00552920) ist keine unbenannte Funktion mehr übrig |

## AgpaItem (eingebaut 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetItem` | 7 | zugeordnet | `0x0058D810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmItem::_GetDragonScionItemAgcdItem, AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBAddConvertGridItem |
| `RemoveItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIAuction::CBBoardSelect, AgcmUIEventItemConvert::CBRemoveItem, AgcmUIEventItemRepair::CBMoveEndItem |

## AgpaMailBox (eingebaut 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Remove` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |

## AgpaParty (eingebaut 2, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddParty` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmParty::AddParty, AgpmParty::CreateParty |
| `RemoveParty` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmParty::OnDestroy, AgpmParty::RemoveParty, AgpmParty::CreateParty |
| `GetParty` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmUIWorldmap::OnIdle, AgcmHPBar::SetData; im Adressbereich der Klasse (0x005922E0–0x005922E0) ist keine unbenannte Funktion mehr übrig |

## AgpaProductSkillFactor (eingebaut 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |

## AgpaQuestGroup (Kandidat unbestätigt 1, eingebaut 2, nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Get` | 7 | Kandidat unbestätigt | `0x00590C80` | Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `IsExistEstimate` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsExistGrant` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AgpaQuestTemplate (Kandidat unbestätigt 1, eingebaut 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Get` | 7 | Kandidat unbestätigt | `0x0058CEB0` | Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |

## AgpaRefineItem (eingebaut 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |

## AgpaSkill (eingebaut 2, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddSkill` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmSkill::CBLearnSkill, AgpmSkill::AddSkill, AgpmSkill::AddSkill |
| `GetSkill` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmProductMed::CBActionSkillResult, AgcmProductMed::OnResult, AgcmSkill::ProcessReceiveCastSkill; im Adressbereich der Klasse (0x005921A0–0x005921A0) ist keine unbenannte Funktion mehr übrig |
| `RemoveSkill` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmSkill::CBLearnSkill, AgcmSkill::CBForgetSkill, AgpmEventSkillMaster::CBRollbackSkill |

## AgpaSkillSpecializeTemplate (eingebaut 2, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddSkillSpecializeTemplate` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSkill::AddSpecialize |
| `GetSkillSpecializeTemplate` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmSkill::GetSpecialize; im Adressbereich der Klasse (0x00592200–0x00592200) ist keine unbenannte Funktion mehr übrig |
| `RemoveSkillSpecializeTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::RemoveSpecialize |

## AgpaSkillTemplate (Kandidat unbestätigt 1, eingebaut 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetSkillTemplate` | 7 | zugeordnet | `0x0058CF60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `AddSkillTemplate` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmGuild::AddGuildMarkTemplate, AgpmSkill::AddSkillTemplate, AgpmSkill::StreamReadTemplate |
| `GetSkillTemplate` | 7 | Kandidat unbestätigt | `0x0058D4E0` | Aufrufer im Client: AgcmAIUseSkillEdit::OnInitDialog, AgcmAIUseSkillEdit::OnAiUseSkillAddButton, AgcmCharacter::_GetCurrentEvolutionSkillTemplate; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `RemoveSkillTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::RemoveSkillTemplate, AgpmSkill::RemoveAllSkillTemplate |
| `AddTemplateStringKey` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmCharacter::TemplateReadCB, AgpmShrine::TemplateReadCB, AgpmSkill::TemplateReadCB |

## AgpaSkillTooltipTemplate (eingebaut 2, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddSkillTooltipTemplate` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgpmSkill::AddTooltipTemplate |
| `GetSkillTooltipTemplate` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmSkill::GetTooltipTemplate; im Adressbereich der Klasse (0x00592280–0x00592280) ist keine unbenannte Funktion mehr übrig |
| `RemoveSkillTooltipTemplate` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmSkill::RemoveTooltipTemplate |

## AgpaTitleTemplate (eingebaut 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Add` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu, AgcmEventNPCTrade::ProcessItemList, AgcmExportResource::ExportClump |
| `Remove` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::CBInitCharacter, AgcmCharacter::RemoveCharacter, AgcmItem::ItemRemoveCB |
| `Get` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCamera2::OnAddModule, CExNPCDialog::_GetNPCDialogBtn, CExNPCDialog::_SetButtonEventInfo |

## AgpaWorld (eingebaut 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddWorld` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmCharacter::InitCharacterMainThread, AgcmUIServerSelect::OnLoadServerList |
| `RemoveWorld` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmObject::ReleaseObjectData, AgpmWorld::OnDestroy |
| `GetWorld` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmDynamicLightmap::addLight, AgcmDynamicLightmap::removeLight |
| `GetWorld` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::OnAddModule, AgcmDynamicLightmap::addLight, AgcmDynamicLightmap::removeLight |

## AgpdQuestFlag (Kandidat unbestätigt 1, eingebaut 1, nicht als eigene Funktion 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `InitFlags` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgpdQuestFlag::AgpdQuestFlag; im Adressbereich der Klasse (0x00590E00–0x00590E00) ist keine unbenannte Funktion mehr übrig |
| `GetBlockIndex` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpdQuestFlag::GetValueByDBID, AgpdQuestFlag::SetValueByDBID |
| `MemoryCopy` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmQuest::OnReceive; im Adressbereich der Klasse (0x00590E00–0x00590E00) ist keine unbenannte Funktion mehr übrig |
| `IsValid` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AgpmGamble::IsValid, AgpdQuestFlag::GetValueByDBID, AgpdQuestFlag::SetValueByDBID; im Adressbereich der Klasse (0x00590E00–0x00590E00) ist keine unbenannte Funktion mehr übrig |
| `GetBlockMemory` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgpdQuestFlag::GetValueByDBID, AgpdQuestFlag::SetValueByDBID; im Adressbereich der Klasse (0x00590E00–0x00590E00) ist keine unbenannte Funktion mehr übrig |
| `GetValueByDBID` | 20 | Kandidat unbestätigt | `0x00590C80` | Aufrufer im Client: AgcmUIQuest2::MakeAcceptList, AgcmUIQuest2::MakeAcceptListAutoStart, AgpmQuest::EvaluationStartCondition; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `SetValueByDBID` | 31 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIQuest2::CompleteQuestResult; im Adressbereich der Klasse (0x00590E00–0x00590E00) ist keine unbenannte Funktion mehr übrig |

## ApModuleStream (Kandidat unbestätigt 5, eingebaut 6, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetValue` | 9 | Kandidat unbestätigt | `0x00871B30` | Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB, AgcmCharacter::CBReceiveAction, AgcmCharacter::InitCharacterBackThread; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetValue` | 8 | Kandidat unbestätigt | `0x00871B30` | Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB, AgcmCharacter::CBReceiveAction, AgcmCharacter::InitCharacterBackThread; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetValue` | 8 | Kandidat unbestätigt | `0x00871B30` | Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB, AgcmCharacter::CBReceiveAction, AgcmCharacter::InitCharacterBackThread; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetValue` | 8 | Kandidat unbestätigt | `0x00871B30` | Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB, AgcmCharacter::CBReceiveAction, AgcmCharacter::InitCharacterBackThread; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetValue` | 8 | Kandidat unbestätigt | `0x00871B30` | Aufrufer im Client: AgcmAmbOcclMap::objectStreamReadCB, AgcmCharacter::CBReceiveAction, AgcmCharacter::InitCharacterBackThread; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `WriteValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::objectStreamWriteCB, AgcmCharacter::TemplatePreDataStreamWrite, AgcmCharacter::TemplateAnimationAttachedDataStreamWrite |
| `WriteValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::objectStreamWriteCB, AgcmCharacter::TemplatePreDataStreamWrite, AgcmCharacter::TemplateAnimationAttachedDataStreamWrite |
| `WriteValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::objectStreamWriteCB, AgcmCharacter::TemplatePreDataStreamWrite, AgcmCharacter::TemplateAnimationAttachedDataStreamWrite |
| `WriteValue` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmAmbOcclMap::objectStreamWriteCB, AgcmCharacter::TemplatePreDataStreamWrite, AgcmCharacter::TemplateAnimationAttachedDataStreamWrite; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `Write` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::StreamWriteTemplate, AgcmCharacter::StreamWriteTemplateAnimation, AgcmCharacter::StreamWriteTemplateCustomize |
| `SetMode` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StreamReadTemplate, AgcmCharacter::StreamWriteTemplate, AgcmCharacter::StreamReadTemplateAnimation |
| `SetType` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::StreamWriteTemplate, AgcmCharacter::StreamWriteTemplateAnimation, AgcmCharacter::StreamWriteTemplateCustomize |

## ApaEvent (eingebaut 2, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddEvent` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmUIWorldmap::OnAddModule, AgcmUIWorldmap::AddEvent, AgcmMinimap::OnAddModule |
| `GetEvent` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::SetCharacterPosition, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBOnRemoveObject; im Adressbereich der Klasse (0x00592000–0x00592000) ist keine unbenannte Funktion mehr übrig |
| `RemoveEvent` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: ApmEventManager::EventDestructor, ApmEventManager::RemoveEvent, ApmEventManager::RemoveEvent |
| `GetSequence` | 7 | nicht als eigene Funktion |  | Aufrufer im Client: ApAdmin::GetObjectSequence, ApmEventManager::GetEventSquence, ApModule::RemoveIdleEvent; im Adressbereich der Klasse (0x00592000–0x00592000) ist keine unbenannte Funktion mehr übrig |

## AuAngelScriptEngine (eingebaut 1, nicht im Client 11, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `getReturnDWord` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `getReturnQWord` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `getReturnFloat` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `getReturnDouble` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `getReturnObject` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `registerGlobalVariable` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `registerGlobalFunctionCdecl` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmUIConsole::OnInit |
| `registerGlobalFunctionStdcall` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `registerObjectType` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `registerObjectVariable` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `registerObjectMethod` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `getVariableDeclarationByName` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcConsole::registerWatch; kein unbenannter Kandidat mit Beleg unter 10 unbenannten Funktionen im Klassenbereich |
| `getFunctionDeclarationByName` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuBlowFish (nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Blowfish_encipher` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: AuBlowFish::Initialize, AuBlowFish::Encrypt; im Adressbereich der Klasse (0x00500B30–0x00501020) ist keine unbenannte Funktion mehr übrig |
| `Blowfish_decipher` | 20 | nicht als eigene Funktion |  | Aufrufer im Client: AuBlowFish::Decrypt; im Adressbereich der Klasse (0x00500B30–0x00501020) ist keine unbenannte Funktion mehr übrig |

## AuCircularBuffer (Kandidat unbestätigt 1, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Destroy` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCharacter::DestroyCharacter, AgcmItem::ItemDestructorCB, AgcmObject::ReleaseObjectData; im Adressbereich der Klasse (0x004EF500–0x004EF7D0) ist keine unbenannte Funktion mehr übrig |
| `Free` | 9 | Kandidat unbestätigt | `0x004EF4E0` | Aufrufer im Client: AgcmAmbOcclMap::freeAtomicData, AgcmObjectList::RemoveAllObjectGroup, AgcmResourceLoader::OnIdle; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |

## AuConsole (eingebaut 3, ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `passKey` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcConsole::OnChar |
| `passBackspace` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcConsole::OnChar; kein unbenannter Kandidat mit Beleg unter 1557 unbenannten Funktionen im Klassenbereich |
| `passLeft` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcConsole::OnKeyDown |
| `passRight` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcConsole::OnKeyDown |
| `passUp` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcConsole::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 1557 unbenannten Funktionen im Klassenbereich |
| `passDown` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcConsole::OnKeyDown; kein unbenannter Kandidat mit Beleg unter 1557 unbenannten Funktionen im Klassenbereich |

## AuExcelBinaryLib (nicht im Client 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ReadExcelFile` | 74 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `WriteExcelFile` | 78 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportINIResource; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `WriteExcelFIleText` | 45 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuExcelTxtLib (Kandidat unbestätigt 1, nicht im Client 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetData` | 9 | Kandidat unbestätigt | `0x004EFB80` | Aufrufer im Client: AgcmAIDialog::OnInitDialog, AgcmCharacter::StreamReadPolyMorphTable, AgcmCharacter::CharacterImportDataReadCB; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `ResetRowData` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EncryptSave` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::_CopyFile, AuIniManagerA::WriteFile; kein unbenannter Kandidat mit Beleg unter 461 unbenannten Funktionen im Klassenbereich |

## AuFileFind (eingebaut 2, nicht im Client 13)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Initialize` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit |
| `Close` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::CBSocketOnError, AgcmLogin::CBSocketError, AgcWindow::Close |
| `IsNormal` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsArchive` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsCompressed` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsEncrypted` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsOffLine` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsReadOnly` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsReparsePoint` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsSparseFile` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsSystem` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsTemporary` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCreationTime` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLastAccessTime` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLastWriteTime` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuGameEnv (nicht als eigene Funktion 1, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `InitEnvironment` | 28 | zugeordnet | `0x008791F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CheckOption` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: AuGameEnv::InitEnvironment; im Adressbereich der Klasse (0x008791F0–0x008791F0) ist keine unbenannte Funktion mehr übrig |

## AuGenerateID (nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCurrentID` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuHistoryDlg (eingebaut 1, nicht als eigene Funktion 3, nicht im Client 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DoDataExchange` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcmAICharFactorDialog::DoDataExchange, AgcmAICharItemDialog::DoDataExchange, AgcmAICharStatusDialog::DoDataExchange |
| `OnInitDialog` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAICharItemDialog::OnInitDialog, AgcmAIDialog::OnInitDialog, AgcmAIScreamEditDlg::OnInitDialog; im Adressbereich der Klasse (0x00417B60–0x00417B60) ist keine unbenannte Funktion mehr übrig |
| `InitHistory` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: AuHistoryDlg::OnInitDialog; im Adressbereich der Klasse (0x00417B60–0x00417B60) ist keine unbenannte Funktion mehr übrig |
| `SetHistoryList` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddListItem` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: AuHistoryDlg::InitHistory, AuLoginDlg::InitConfig, AuRKMainDlg::ViewFileList; im Adressbereich der Klasse (0x00417B60–0x00417B60) ist keine unbenannte Funktion mehr übrig |
| `OnGetFile` | 22 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnClickHistory` | 10 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuIniManagerA (Kandidat unbestätigt 4, eingebaut 10, nicht im Client 2, ohne Kandidat 5, zugeordnet 8)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AddSection` | 46 | zugeordnet | `0x004F3D50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetValue_3` | 0 | zugeordnet | `0x004F4140` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetValue_2` | 0 | zugeordnet | `0x004F4010` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetValue` | 38 | zugeordnet | `0x004F07D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ParseMemory` | 315 | zugeordnet | `0x004F1760` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddKey` | 58 | zugeordnet | `0x004F21E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetKeyNameTable` | 4 | zugeordnet | `0x004F0910` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `WriteFile` | 128 | zugeordnet | `0x004F09B0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `Initialize` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit |
| `GetPackName` | 18 | Kandidat unbestätigt | `0x004F2930` | Aufrufer im Client: AuIniManagerA::FromMemory, AuIniManagerA::FromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `StringMid` | 31 | Kandidat unbestätigt | `0x004F2930` | Aufrufer im Client: AuIniManagerA::FromMemory, AuIniManagerA::ParseMemory, AuIniManagerA::FromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `GetStringValue` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmResourceLoader::_LoadColor |
| `GetStringValue` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmResourceLoader::_LoadColor |
| `GetValueI64` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `FindSection` | 51 | ohne Kandidat |  | Aufrufer im Client: AgcmEventNature::LoadTextureScriptFile, AuIniManagerA::FindKey, AuIniManagerA::SetValue; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `FindKey` | 44 | ohne Kandidat |  | Aufrufer im Client: AgpmEventGacha::StreamReadGachaTypeTable, ApmMap::LoadTemplate, ApmMap::LoadRegion; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `SetValue` | 39 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::SetHPZero, AgcuEffIniMng::_Write_EffSet_txt, AgcuEffIniMng::_Write_EffBase_txt; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `SetValue` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::SetHPZero, AgcuEffIniMng::_Write_EffSet_txt, AgcuEffIniMng::_Write_EffBase_txt |
| `SetValueI` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmUIHotkey::WriteCustomHotkeyIniFile, ApmMap::SaveTemplate, ApmMap::SaveRegion |
| `SetValueI64` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: ApModuleStream::WriteValue |
| `SetValueF` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: ApmMap::SaveTemplate, ApmMap::SaveWorldMap, ApModuleStream::WriteValue |
| `AddKey` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AuIniManagerA::SetValue |
| `SetMode` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::StreamReadTemplate, AgcmCharacter::StreamWriteTemplate, AgcmCharacter::StreamReadTemplateAnimation |
| `SetType` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: AgcmCharacter::StreamWriteTemplate, AgcmCharacter::StreamWriteTemplateAnimation, AgcmCharacter::StreamWriteTemplateCustomize |
| `ReadPartIndices` | 76 | Kandidat unbestätigt | `0x004F0080` | Aufrufer im Client: AuIniManagerA::FromFile, AuIniManagerA::WriteFile, AuINIPackingManager::FromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `ReadPartIndices` | 18 | Kandidat unbestätigt | `0x004F0080` | Aufrufer im Client: AuIniManagerA::FromFile, AuIniManagerA::WriteFile, AuINIPackingManager::FromFile; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `WritePartIndices` | 11 | ohne Kandidat |  | Aufrufer im Client: AuIniManagerA::WriteFile; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `GetStartIndex` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `EncryptSave` | 35 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::_CopyFile, AuIniManagerA::WriteFile; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |

## AuInputComposer (eingebaut 4, nicht im Client 5, ohne Kandidat 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnComposition` | 120 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnEndComposition` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnNotify` | 222 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |
| `OnChar` | 41 | ohne Kandidat |  | Aufrufer im Client: AgcWindow::UserInputMessageProc, AcUIBase::PreTranslateInputMessage; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetInput` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetComp` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetReading` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcUIEdit::DrawReadingWindow |
| `GetCandidate` | 46 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::DrawCandidateWindow; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetCandidateCount` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::DrawCandidateWindow; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetCandidateSelection` | 12 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::DrawCandidateWindow; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetCandidatePageSize` | 9 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::DrawCandidateWindow; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetCandidatePageStart` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::DrawCandidateWindow; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetNextChar` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgpmLogin::IsDuplicatedCharacterOfMigration |
| `GetPrivateReadingString` | 162 | ohne Kandidat |  | Aufrufer im Client: AuInputComposer::OnNotify; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `CheckToggleState` | 75 | ohne Kandidat |  | Aufrufer im Client: AuInputComposer::OnInputLanguageChange, AuInputComposer::OnNotify; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `GetCodePageFromLang` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AuInputComposer::OnInputLanguageChange |
| `ToAlphaNumeric` | 8 | ohne Kandidat |  | Aufrufer im Client: AcUIEdit::OnEditActive; kein unbenannter Kandidat mit Beleg unter 13 unbenannten Funktionen im Klassenbereich |
| `ToNative` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AcUIEdit::OnEditDeactive |

## AuLua (nicht als eigene Funktion 1, nicht im Client 11)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RunScript` | 28 | nicht als eigene Funktion |  | Aufrufer im Client: AgcEngine::LuaInitialize; im Adressbereich der Klasse (0x004E3120–0x004E3320) ist keine unbenannte Funktion mehr übrig |
| `GetErrorString` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PushString` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PushInteger` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `PushNumber64` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunction` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunction` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunction` | 13 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunction` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunctionInt` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunctionFloat` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CallLuaFunctionString` | 8 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuMD5Encrypt (eingebaut 1, nicht im Client 1, ohne Kandidat 2, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DecryptString` | 44 | zugeordnet | `0x004F9660` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CleanUp` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AgcdEffCtrlMng::DeletePreSet, AuCryptActor::AuCryptActor, AuMD5Encrypt::~AuMD5Encrypt |
| `GetMD5Hash` | 58 | ohne Kandidat |  | Aufrufer im Client: AgcTaiwanAuth::encrypt, AgcmLogin::SendAccount; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `EncryptString` | 45 | ohne Kandidat |  | Aufrufer im Client: AgcAuth::encrypt, AgcTaiwanAuth::encrypt, AuExcelTxtLib::EncryptSave; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |
| `GetRandomHashString` | 25 | nicht im Client |  | Aufrufer nur im Server (1); kein Treffer im Binary |

## AuMD5Mac (eingebaut 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Startup` | 8 | ohne Kandidat |  | Aufrufer im Client: AuMD5Mac::AuMD5Mac; kein unbenannter Kandidat mit Beleg unter 2 unbenannten Funktionen im Klassenbereich |
| `Cleanup` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgpmWorld::_DestroyWorldData, AuDynCode::~AuDynCode, AuDynCode::~AuDynCode |

## AuMiniLZO (nicht im Client 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Compress` | 30 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `DeCompress` | 27 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuNPWrapper (eingebaut 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Init` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmAIDlg::OpenTemplates, AgcmAIDlg::OpenTemplate, AgcmCustomizeRender::AgcmCustomizeRender |
| `GetMessage` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcChatMessage::PopNewMessage, AgcUIChatMessage::_RefreshMessage, SplashWindow::run |
| `NPGameMonCallback` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuPackingManager (Kandidat unbestätigt 2, eingebaut 1, nicht im Client 32, ohne Kandidat 11, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ReadReferenceFile` | 152 | zugeordnet | `0x004EE6C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Destroy` | 31 | zugeordnet | `0x004EEC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetFolderInfo` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetPatchList` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsCheckedBuildJZP` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsCheckedBuildDat` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsCheckedCopyRawFiles` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetBuildJZP` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetBuildDat` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `SetCopyRawFiles` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MakeInstance` | 15 | ohne Kandidat |  | Aufrufer im Client: AuExcelTxtLibHelper::GetSingletonPtr, AuPackingManager::GetSingletonPtr; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `DestroyInstance` | 11 | ohne Kandidat |  | Aufrufer im Client: ApMemoryTracker::GetInstance, AuPackingManager::MakeInstance; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetSingletonPtr` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmGrass::LoadGrass, AgcmResourceLoader::SetCurrentTexDict, AgcmResourceLoader::LoadClump |
| `LoadIgnoreFileInfo` | 101 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddIgnoreFileName` | 18 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::LoadIgnoreFileInfo; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `RemoveIgnoreFileName` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `IsIgnoreFileName` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetIgnoreFileInfo` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddCrackedFolderName` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `RemoveCrackedFolderName` | 20 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCrackedFolderInfo` | 2 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetLastVersion` | 24 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::LoadResFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetPatchInfo` | 15 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddFolder` | 31 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::LoadResFile, AuRKMainDlg::OnAddFolder, AuRKMainDlg::AddFolder; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `AddFile` | 46 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::LoadResFile, AuRKMainDlg::OnAddFile, AuRKSingleton::AddFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetFolder` | 16 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::OpenFile, AuPackingManager::ReadFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetFile` | 30 | ohne Kandidat |  | Aufrufer im Client: ApWorldSector::LoadDetailDataGeometry, ApWorldSector::LoadDetailDataTile, CMagUnpackManager::SetFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `AddPatch` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `BuildJZPFile` | 182 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadResFile` | 166 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MarkPacking` | 23 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `MarkPackingComplete` | 41 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `LoadReferenceFile` | 72 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CloseAllFileHandle` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `BuildDatFile` | 148 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFolderName` | 27 | ohne Kandidat |  | Aufrufer im Client: AuRKSingleton::CreateRepository; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CreateFolder` | 35 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::ReadyPacking, AuRKSingleton::CreateFolder, AuRKSingleton::FileDownLoad; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetJZPInfo` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileSize` | 41 | Kandidat unbestätigt | `0x004EF4E0` | Aufrufer im Client: AgcmResourceLoader::SetCurrentTexDict, AgcmResourceLoader::LoadClump, AgcmResourceLoader::LoadAtomic; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `Unlock` | 14 | Kandidat unbestätigt | `0x004EF4E0` | Aufrufer im Client: AgcmEventNature::OnIdle, AgcmEventNature::CBOnAddObject, AgcmEventNature::CBLoadSector; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 1) |
| `CreateEmptyFile` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadyPacking` | 76 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CompletePacking` | 343 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `BuildPackingFile` | 78 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadBakReference` | 264 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `AddEmptyPackingFileInfo` | 45 | ohne Kandidat |  | Aufrufer im Client: AuPackingManager::ReadBakReference; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `ResizeFileSize` | 56 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CompleteCurrentFolderProcess` | 176 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## AuRegionNameConvert (eingebaut 1, nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `parse_data` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: AuRegionNameConvert::Load; im Adressbereich der Klasse (0x00877B50–0x00877B50) ist keine unbenannte Funktion mehr übrig |
| `parse_data` | 29 | nicht als eigene Funktion |  | Aufrufer im Client: AuRegionNameConvert::Load; im Adressbereich der Klasse (0x00877B50–0x00877B50) ist keine unbenannte Funktion mehr übrig |
| `Load` | 50 | nicht als eigene Funktion |  | Aufrufer im Client: AgcuPathWork::CreateSplinePath, AgcuEffBaseCtrlCreater::CreateCtrl, AcMapLoader::OnIdleLoad; im Adressbereich der Klasse (0x00877B50–0x00877B50) ist keine unbenannte Funktion mehr übrig |
| `GetStr` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmBattleGround::StartBattleGround, AgcmBattleGround::EndBattleGround, AgcmBattleGround::StartEventBattleGround |
| `GetDecryptStr` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: AuRegionNameConvert::Load, AuStrTable::Load; im Adressbereich der Klasse (0x00877B50–0x00877B50) ist keine unbenannte Funktion mehr übrig |

## AuRijnDael (nicht als eigene Funktion 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `RijnDaelKeySetupEnc` | 22 | nicht als eigene Funktion |  | Aufrufer im Client: AuRijnDael::RijnDaelKeySetupDec, AuRijnDael::Initialize; im Adressbereich der Klasse (0x004FFDF0–0x004FFF90) ist keine unbenannte Funktion mehr übrig |
| `RijnDaelKeySetupDec` | 39 | nicht als eigene Funktion |  | Aufrufer im Client: AuRijnDael::Initialize; im Adressbereich der Klasse (0x004FFDF0–0x004FFF90) ist keine unbenannte Funktion mehr übrig |
| `RijnDaelEncrypt` | 150 | nicht als eigene Funktion |  | Aufrufer im Client: AuRijnDael::Encrypt; im Adressbereich der Klasse (0x004FFDF0–0x004FFF90) ist keine unbenannte Funktion mehr übrig |
| `RijnDaelDecrypt` | 150 | nicht als eigene Funktion |  | Aufrufer im Client: AuRijnDael::Decrypt; im Adressbereich der Klasse (0x004FFDF0–0x004FFF90) ist keine unbenannte Funktion mehr übrig |
| `Initialize` | 21 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit; im Adressbereich der Klasse (0x004FFDF0–0x004FFF90) ist keine unbenannte Funktion mehr übrig |

## AuSeed (Kandidat unbestätigt 5, eingebaut 2, ohne Kandidat 21, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `PaddSet` | 16 | zugeordnet | `0x004FDCC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Initialize` | 25 | ohne Kandidat |  | Aufrufer im Client: AgcmAmbOcclMap::OnInit, AgcmEventEffectData::SetMaxSoundData, CUiExNPCMsgBoxGrid::OnInit; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `SEED_SetAlgInfo` | 8 | ohne Kandidat |  | Aufrufer im Client: AuSeed::Initialize; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `SEED_KeySchedule` | 40 | ohne Kandidat |  | Aufrufer im Client: AuSeed::Initialize; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `SEED_EncInit` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AuSeed::Encrypt |
| `SEED_EncUpdate` | 12 | ohne Kandidat |  | Aufrufer im Client: AuSeed::Encrypt; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `SEED_EncFinal` | 8 | ohne Kandidat |  | Aufrufer im Client: AuSeed::Encrypt; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `SEED_Encrypt` | 36 | ohne Kandidat |  | Aufrufer im Client: AuSeed::ECB_EncUpdate, AuSeed::CBC_EncUpdate, AuSeed::OFB_EncUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ECB_EncUpdate` | 43 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CBC_EncUpdate` | 44 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `OFB_EncUpdate` | 44 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CFB_EncUpdate` | 46 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ECB_EncFinal` | 23 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CBC_EncFinal` | 24 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `OFB_EncFinal` | 19 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CFB_EncFinal` | 17 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_EncFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `SEED_DecInit` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: AuSeed::Decrypt |
| `SEED_DecUpdate` | 12 | Kandidat unbestätigt | `0x004FDF80` | Aufrufer im Client: AuSeed::Decrypt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SEED_DecFinal` | 8 | Kandidat unbestätigt | `0x004FDF80` | Aufrufer im Client: AuSeed::Decrypt; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 6, Belegarten 2) |
| `SEED_Decrypt` | 37 | ohne Kandidat |  | Aufrufer im Client: AuSeed::ECB_DecUpdate, AuSeed::CBC_DecUpdate, AuSeed::ECB_DecFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ECB_DecUpdate` | 44 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_DecUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CBC_DecUpdate` | 54 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_DecUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `OFB_DecUpdate` | 45 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_DecUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CFB_DecUpdate` | 47 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_DecUpdate; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `ECB_DecFinal` | 27 | Kandidat unbestätigt | `0x004FDFE0` | Aufrufer im Client: AuSeed::SEED_DecFinal; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CBC_DecFinal` | 29 | Kandidat unbestätigt | `0x004FDFE0` | Aufrufer im Client: AuSeed::SEED_DecFinal; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `OFB_DecFinal` | 16 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_DecFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `CFB_DecFinal` | 16 | ohne Kandidat |  | Aufrufer im Client: AuSeed::SEED_DecFinal; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `PaddCheck` | 19 | Kandidat unbestätigt | `0x004FDFE0` | Aufrufer im Client: AuSeed::ECB_DecFinal, AuSeed::CBC_DecFinal; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |

## AuTickCounter (nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetElapsedTime` | 9 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## CBGMTitleViewer (eingebaut 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetCurrentBGMTitle` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CBGMTitleViewer::CallBack_DisplayBGMTitle |

## CChatCmd (Kandidat unbestätigt 2, eingebaut 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_GetCmdCallBack` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: CChatCmd::_AddChatCmd |
| `CallBack_OnChangeSoundEffect` | 12 | Kandidat unbestätigt | `0x007115B0` | Aufrufer im Client: CChatCmd::OnRegisterCmdCallBack; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CallBack_OnTest3DSound` | 12 | Kandidat unbestätigt | `0x007115B0` | Aufrufer im Client: CChatCmd::OnRegisterCmdCallBack; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `CallBack_OnSendMsgShout` | 33 | ohne Kandidat |  | Aufrufer im Client: CChatCmd::OnRegisterCmdCallBack; kein unbenannter Kandidat mit Beleg unter 34 unbenannten Funktionen im Klassenbereich |

## CChattingInputController (nicht als eigene Funktion 1, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnReadyAutoReplyWhisper` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcChatManager::_WhisperEvent, AgcmUIChatting2::CBSendWhisper, CChattingInputController::OnReadyStatusEvent; im Adressbereich der Klasse (0x0070AFE0–0x0070BB30) ist keine unbenannte Funktion mehr übrig |
| `GetToID` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## CD3DFxMng (eingebaut 3, gemeinsamer Rumpf 1, nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInit` | 7 | gemeinsamer Rumpf |  | virtuelle Standardfunktion; der Vtable-Eintrag zeigt auf einen gemeinsamen Rumpf (return TRUE/leer) |
| `FxCheckMaterialCallBack` | 8 | nicht als eigene Funktion |  | Aufrufer im Client: CD3DFxMng::FxCheckGeometryCallBack; im Adressbereich der Klasse (0x005AE440–0x005AE440) ist keine unbenannte Funktion mehr übrig |
| `FxCheckGeometryCallBack` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CD3DFxMng::AtomicFxOn |
| `AtomicFxOn` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmLODManager::LODCallback, CD3DFxMng::AtomicFxCheck; im Adressbereich der Klasse (0x005AE440–0x005AE440) ist keine unbenannte Funktion mehr übrig |
| `AtomicFxCheck` | 11 | nicht als eigene Funktion |  | Aufrufer im Client: CD3DFxMng::FxAllCheckAtomicCallBack, CD3DFxMng::AllAtomicFxCheck, AgcmRender::InitAtomicDatas; im Adressbereich der Klasse (0x005AE440–0x005AE440) ist keine unbenannte Funktion mehr übrig |
| `FxAllCheckClumpCallBack` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CD3DFxMng::AllAtomicFxCheck |
| `FxAllCheckAtomicCallBack` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CD3DFxMng::FxAllCheckClumpCallBack |
| `AllAtomicFxCheck` | 79 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmUIOption::UpdateMatEffect; im Adressbereich der Klasse (0x005AE440–0x005AE440) ist keine unbenannte Funktion mehr übrig |

## CExNPC (Kandidat unbestätigt 2, eingebaut 4, ohne Kandidat 7, zugeordnet 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInitNPCMsgBox` | 31 | zugeordnet | `0x0072F490` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetMsgBoxButtonName` | 14 | zugeordnet | `0x0072F050` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddMsgBoxImage` | 19 | zugeordnet | `0x0072EF90` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnRegisterCallBack` | 14 | zugeordnet | `0x0072F720` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnShowNPCMsgBox` | 17 | ohne Kandidat |  | Aufrufer im Client: CExNPC::CBShowExNPCMsgBox; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `OnSendNPCMsgBox` | 20 | ohne Kandidat |  | Aufrufer im Client: CExNPC::CBShowExNPCMsgBox; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `OnSendNPCMsgBoxItem` | 18 | Kandidat unbestätigt | `0x0072F360` | Aufrufer im Client: CExNPC::CBMsgBoxGridReturnItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 5, Belegarten 1) |
| `OnHideNPCMsgBox` | 7 | ohne Kandidat |  | Aufrufer im Client: CExNPC::CBShowExNPCMsgBox, CExNPC::CBMsgBoxGridCancelItem, CExNPCDialog::CBAutoCloseByCharacterMove; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `CopyLastReceiveMsgBoxPacket` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: CExNPC::CBShowExNPCMsgBox |
| `IsOpenModalWindow` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcmCharacter::KeyboardIdleProcess, AgcmUIManager2::IsOpenModalWindow; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `IsOpenWaitingMsgBox` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmUIMain::CBCloseUIWindow |
| `_ShowMsgBox` | 46 | ohne Kandidat |  | Aufrufer im Client: CExNPC::OnShowNPCMsgBox; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `_HideMsgBox` | 25 | Kandidat unbestätigt | `0x0072F360` | Aufrufer im Client: CExNPC::OnHideNPCMsgBox; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 7, Belegarten 1) |
| `CBShowExNPCMsgBox` | 23 | ohne Kandidat |  | Aufrufer im Client: CExNPC::OnRegisterCallBack; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `CBShowExNPCDialog` | 20 | ohne Kandidat |  | Aufrufer im Client: CExNPC::OnRegisterCallBack; kein unbenannter Kandidat mit Beleg unter 8 unbenannten Funktionen im Klassenbereich |
| `CBMsgBoxGridReturnItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPC::OnInitNPCMsgBox |
| `CBMsgBoxGridCancelItem` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: CExNPC::OnInitNPCMsgBox |

## CExNPCDialog (Kandidat unbestätigt 2, eingebaut 2, nicht im Client 2, ohne Kandidat 12, zugeordnet 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnInitNPCDialog` | 17 | zugeordnet | `0x00740280` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnHideNPCDialog` | 16 | zugeordnet | `0x0073F4A0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnShowNPCDialog` | 22 | ohne Kandidat |  | Aufrufer im Client: CExNPC::CBShowExNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `OnSencNPCDialog` | 10 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::CBClickMenuButton; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `OnSetDialogButton` | 1 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnUpdateNPCDialog` | 16 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::OnShowNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `_MakeExNPCDialogTitleBar` | 16 | Kandidat unbestätigt | `0x0073F620` | Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBase; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_MakeExNPCDIalogTextBox` | 13 | Kandidat unbestätigt | `0x0073F620` | Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBase; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_ClearExNPCDialogButton` | 19 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::OnUpdateNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `_DeleteExNPCDialogButton` | 22 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::~CExNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `_UpdateNPCDialogBtn` | 11 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::OnUpdateNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `_GetNPCDialogBtn` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: CExNPCDialog::OnUpdateNPCDialog |
| `_SetButtonEventInfo` | 8 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::OnUpdateNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `_GetEventIDByButton` | 17 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::OnSencNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `_GetEventStepByButton` | 17 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::OnSencNPCDialog; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `GetModule` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcAuth::login, AgcmAdmin::OnAddModule, AgcmAdmin::GetUIMessageString; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `IsExNpcDialog` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CBClickMenuButton` | 8 | ohne Kandidat |  | Aufrufer im Client: CExNPCDialog::_MakeExNPCDialogBtnMenu; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |
| `CBClickCloseButton` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: CExNPCDialog::_MakeExNPCDIalogBtnClose |
| `CBAutoCloseByCharacterMove` | 13 | ohne Kandidat |  | Aufrufer im Client: CExNPC::OnRegisterCallBack; kein unbenannter Kandidat mit Beleg unter 17 unbenannten Funktionen im Klassenbereich |

## CFlagImoticon (eingebaut 1, nicht im Client 2, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `ReloadFlag` | 7 | ohne Kandidat |  | Aufrufer im Client: CChatCmd::CallBack_OnFlagImoticon; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetFlagTexture` | 12 | ohne Kandidat |  | Aufrufer im Client: AgcmIDBoard::_DrawFlag; kein unbenannter Kandidat mit Beleg unter 16 unbenannten Funktionen im Klassenbereich |
| `GetFlagOffsetX` | 7 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFlagOffsetX` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFlagOffsetY` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmIDBoard::_DrawFlag |

## CGetArg2 (eingebaut 4, nicht als eigene Funktion 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetParam` | 28 | nicht als eigene Funktion |  | Aufrufer im Client: AcTextureList::LoadScript, CGetArg2::CGetArg2, AuDatabase2::SetParam; im Adressbereich der Klasse (0x004E7B20–0x004E7B20) ist keine unbenannte Funktion mehr übrig |
| `GetParam` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AcTextureList::LoadScript, AgcmSkill::AttachedTemplateReadCB, AgcmUIGuild::CBProcessChatCommand |
| `GetParam` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcTextureList::LoadScript, AgcmSkill::AttachedTemplateReadCB, AgcmUIGuild::CBProcessChatCommand |
| `GetArgCount` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AcTextureList::LoadScript, AgcmSkill::AttachedTemplateReadCB, AgcmUIGuild::CBProcessChatCommand |
| `Clear` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCharacter::CharacterConstructor, AgcmCharacter::SetTemplateClumpRenderType, AgcdEffCtrl_Set::~AgcdEffCtrl_Set |

## CMagUnpackManager (Kandidat unbestätigt 2, eingebaut 2, nicht im Client 2, ohne Kandidat 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `AllocMemory` | 11 | ohne Kandidat |  | Aufrufer im Client: CMagUnpackManager::SetFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `FreeMemory` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: CMagUnpackManager::~CMagUnpackManager, CMagUnpackManager::AllocMemory |
| `SetFile` | 222 | Kandidat unbestätigt | `0x0058AD70` | Aufrufer im Client: AcMapLoader::GetUnpackManager, ApmMap::GetUnpackManagerDivisionCompact, ApmMap::GetUnpackManagerDivisionGeometry; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 11, Belegarten 3) |
| `GetAllFiles` | 29 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFile` | 100 | ohne Kandidat |  | Aufrufer im Client: ApWorldSector::LoadDetailDataGeometry, ApWorldSector::LoadDetailDataTile, CMagUnpackManager::SetFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetFile` | 29 | ohne Kandidat |  | Aufrufer im Client: ApWorldSector::LoadDetailDataGeometry, ApWorldSector::LoadDetailDataTile, CMagUnpackManager::SetFile; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetFileCount` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: ApmMap::GetUnpackManagerDivisionGeometry, ApWorldSector::LoadCompactData, ApWorldSector::LoadDetailDataGeometry |
| `GetFileBinary` | 37 | ohne Kandidat |  | Aufrufer im Client: AgcmMap::LoadDWSector, AgcmMap::LoadRoughAtomic, ApWorldSector::LoadCompactData; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `CloseFile` | 22 | Kandidat unbestätigt | `0x0058AD70` | Aufrufer im Client: AgcmCharacter::StreamReadPolyMorphTable, AgcmEventEffectData::ReadCommonCharEffectData, AgcmEventEffectData::ReadConvertedArmourEffectData; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 2) |
| `GetFileNum` | 32 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileSize` | 18 | ohne Kandidat |  | Aufrufer im Client: AgcmResourceLoader::SetCurrentTexDict, AgcmResourceLoader::LoadClump, AgcmResourceLoader::LoadAtomic; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |
| `GetFileName` | 15 | ohne Kandidat |  | Aufrufer im Client: AgcmExportResource::ExportINIResource, AgcmExportResource::ExportFXData, AgcmExportResource::ExportTexDictFolder; kein unbenannter Kandidat mit Beleg unter 4 unbenannten Funktionen im Klassenbereich |

## CMiniVersion (eingebaut 1, nicht als eigene Funktion 1, nicht im Client 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Release` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCustomizeRender::Render, AgcmEventEffect::CBRemoveAnimation, AgcmEventEffect::CopyCharAnimAttachedData |
| `GetFileVersion` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetProductVersion` | 4 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileFlags` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileOS` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileType` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileSubtype` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetCompanyName` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFileDescription` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetProductName` | 6 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `GetFixedInfo` | 17 | nicht als eigene Funktion |  | Aufrufer im Client: CMiniVersion::Init; im Adressbereich der Klasse (0x004F6A10–0x004F6AE0) ist keine unbenannte Funktion mehr übrig |

## CNpcText (eingebaut 1, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnTextAdd` | 43 | nicht als eigene Funktion |  | Aufrufer im Client: CNpcTextManager::OnAddNpcDialogText; im Adressbereich der Klasse (0x00758D50–0x00758D50) ist keine unbenannte Funktion mehr übrig |
| `OnTextClear` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: CNpcTextManager::OnClearNpcDialogText; im Adressbereich der Klasse (0x00758D50–0x00758D50) ist keine unbenannte Funktion mehr übrig |
| `GetNpcText` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: CNpcTextManager::GetNpcDialogText |

## CNpcTextManager (eingebaut 1, nicht im Client 1, ohne Kandidat 3, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `GetNpcDialogText` | 25 | zugeordnet | `0x00640E60` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnLoadNpcDialogText` | 77 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnAddNpc` | 39 | ohne Kandidat |  | Aufrufer im Client: CNpcTextManager::OnLoadNpcDialogText; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `OnAddNpcDialogText` | 7 | ohne Kandidat |  | Aufrufer im Client: CNpcTextManager::OnLoadNpcDialogText; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |
| `OnAddNpcDialogText` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: CNpcTextManager::OnLoadNpcDialogText |
| `OnClearNpcDialogText` | 16 | ohne Kandidat |  | Aufrufer im Client: AgcmUIEventNPCDialog::OnDestroy; kein unbenannter Kandidat mit Beleg unter 5 unbenannten Funktionen im Klassenbereich |

## COptionFlagController (eingebaut 2, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnChangeOptionFlag` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_CheckOptionFlag` | 5 | eingebaut |  | kleine Funktion (5 Zeilen); Aufrufer im Client: COptionFlagController::OnChangeOptionFlag |
| `_SendMsgChangeOptionFlag` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: COptionFlagController::_CheckOptionFlag |

## CRenderFadeInOut (eingebaut 8, nicht als eigene Funktion 9)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `StartFadeInOut` | 15 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmLODManager::LODCallback; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `StartFadeIn` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmLODManager::LODCallback, CRenderFadeInOut::CallBackSetFadeIn; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `StartFadeOut` | 14 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::CallBackSetFadeOut; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `StartFadeOutClump` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCharacter::CBCheckRemoveChar |
| `StartFadeInClump` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmCharacter::CBAlreadyExistChar, AgcmCharacter::ShowClumpForced, AgcmLODManager::LODCallback |
| `StartTransparentClump` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::vAdjAlpha, AgcmCamera2::bTransparentMainCharac |
| `EndTransparentClump` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::vAdjAlpha, AgcmCamera2::bTransparentMainCharac |
| `ChangeTransparentValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCamera2::vAdjAlpha |
| `InvisibleFxBegin` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmCharacter::ShowClumpForced, AgcmItem::_EquipItem |
| `InvisibleFxEnd` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmCharacter::UpdateTransparent, AgcmCharacter::ShowClumpForced |
| `CallBackSetFadeIn` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::StartFadeInClump, AgcmRender::AddClumpToWorld, AgcmRender::AddAlphaBModeClumpToWorld; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `CallBackSetFadeOut` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: CRenderFadeInOut::StartFadeOutClump |
| `CallBackSetStartTransparent` | 16 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::StartTransparentClump; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `CallBackSetEndTransparent` | 18 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::EndTransparentClump; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `CallBackChangeTransparent` | 9 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::ChangeTransparentValue; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `CallBackInvisibleFxBegin` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::InvisibleFxBegin; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |
| `CallBackInvisibleFxEnd` | 19 | nicht als eigene Funktion |  | Aufrufer im Client: CRenderFadeInOut::InvisibleFxEnd; im Adressbereich der Klasse (0x005AE220–0x005AE220) ist keine unbenannte Funktion mehr übrig |

## CSLogManager (nicht als eigene Funktion 1, nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Push` | 28 | nicht im Client |  | Aufrufer nur im Server (5); kein Treffer im Binary |
| `Pop` | 25 | nicht als eigene Funktion |  | Aufrufer im Client: AgcEngine::OnIdle; im Adressbereich der Klasse (0x004F4720–0x004F4720) ist keine unbenannte Funktion mehr übrig |

## CSmtpMessage (nicht als eigene Funktion 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CommitHeaders` | 84 | nicht als eigene Funktion |  | Aufrufer im Client: CSmtpMessage::Parse; im Adressbereich der Klasse (0x00485582–0x00485582) ist keine unbenannte Funktion mehr übrig |
| `EncodeQuotedPrintable` | 92 | nicht als eigene Funktion |  | Aufrufer im Client: CSmtpMessage::EncodeMessage; im Adressbereich der Klasse (0x00485582–0x00485582) ist keine unbenannte Funktion mehr übrig |
| `BreakMessage` | 61 | nicht als eigene Funktion |  | Aufrufer im Client: CSmtpMessage::EncodeMessage; im Adressbereich der Klasse (0x00485582–0x00485582) ist keine unbenannte Funktion mehr übrig |
| `Make7Bit` | 13 | nicht als eigene Funktion |  | Aufrufer im Client: CSmtpMessage::EncodeMessage; im Adressbereich der Klasse (0x00485582–0x00485582) ist keine unbenannte Funktion mehr übrig |
| `EncodeMessage` | 102 | nicht als eigene Funktion |  | Aufrufer im Client: CSmtpMessage::Parse; im Adressbereich der Klasse (0x00485582–0x00485582) ist keine unbenannte Funktion mehr übrig |
| `GuessEncoding` | 36 | nicht als eigene Funktion |  | Aufrufer im Client: CSmtpMessage::EncodeMessage; im Adressbereich der Klasse (0x00485582–0x00485582) ist keine unbenannte Funktion mehr übrig |

## CTextFilter (nicht im Client 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnRemoveFilter` | 18 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `OnClearFilter` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::~AgcChatManager; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |
| `OnSaveFilterFileCustom` | 22 | ohne Kandidat |  | Aufrufer im Client: CTextFilter::OnAddFilter; kein unbenannter Kandidat mit Beleg unter 7 unbenannten Funktionen im Klassenbereich |

## CUiCharacterProperty (Kandidat unbestätigt 4, nicht im Client 2, ohne Kandidat 4, zugeordnet 6)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `_GetFactorItemOptionValue` | 19 | zugeordnet | `0x005FF470` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_GetZeroBasePropertyByItem` | 57 | zugeordnet | `0x005FFA50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnSelectProperty` | 4 | zugeordnet | `0x00600100` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `OnChangeProperty` | 43 | zugeordnet | `0x00600020` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `_LoadProperty` | 108 | zugeordnet | `0x00600A90` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `OnUpdateProperty` | 36 | zugeordnet | `0x005FFC00` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `RegisterPropertyCallBack` | 19 | ohne Kandidat |  | Aufrufer im Client: CUiCharacterProperty::_InitPropertyCallBack; kein unbenannter Kandidat mit Beleg unter 23 unbenannten Funktionen im Klassenbereich |
| `CalcCurrentZeroBaseProperty` | 33 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `CalcCurrentItemProperty` | 3 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `_ChangeCurrentPropertyTabBtn` | 17 | ohne Kandidat |  | Aufrufer im Client: CUiCharacterProperty::OnChangeProperty; kein unbenannter Kandidat mit Beleg unter 23 unbenannten Funktionen im Klassenbereich |
| `_GetPropertyCallBack` | 7 | ohne Kandidat |  | Aufrufer im Client: CUiCharacterProperty::_LoadProperty; kein unbenannter Kandidat mit Beleg unter 23 unbenannten Funktionen im Klassenbereich |
| `_GetZeroBaseProperty` | 8 | ohne Kandidat |  | Aufrufer im Client: CUiCharacterProperty::CalcCurrentZeroBaseProperty; kein unbenannter Kandidat mit Beleg unter 23 unbenannten Funktionen im Klassenbereich |
| `_GetZeroBasePropertyByPassive` | 54 | Kandidat unbestätigt | `0x005FF0C0` | Aufrufer im Client: CUiCharacterProperty::CalcCurrentZeroBaseProperty; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_GetZeroBasePropertyByBuff` | 76 | Kandidat unbestätigt | `0x005FF0C0` | Aufrufer im Client: CUiCharacterProperty::CalcCurrentZeroBaseProperty; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 10, Belegarten 2) |
| `_GetItemOptionValuePoint` | 78 | Kandidat unbestätigt | `0x005FF0C0` | Aufrufer im Client: CUiCharacterProperty::_GetZeroBasePropertyByItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 3) |
| `_GetItemOptionValueSkill` | 118 | Kandidat unbestätigt | `0x005FF0C0` | Aufrufer im Client: CUiCharacterProperty::_GetZeroBasePropertyByItem; bester Kandidat nur mit Einzelbeleg oder mehrdeutig (Punkte 9, Belegarten 3) |

## CUiExNPCMsgBoxGrid (eingebaut 1, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnClearGridItem` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: CExNPC::OnSendNPCMsgBoxItem |
| `SetButtonName` | 9 | ohne Kandidat |  | Aufrufer im Client: CExNPC::SetMsgBoxButtonName, AgcmUIManager2::StreamReadUIMessage; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## CUiGridSlot (ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `OnClear` | 7 | ohne Kandidat |  | Aufrufer im Client: CUiExNPCMsgBoxGrid::OnClearGridItem, AgcmUICharacterCreate::~AgcmUICharacterCreate, AgcmUICharacterCreate::OnInitialize; kein unbenannter Kandidat mit Beleg unter 1 unbenannten Funktionen im Klassenbereich |

## CUsableRwFrameTable (nicht im Client 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `EnumRemoveRwFrameCallback` | 11 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## Element (ohne Kandidat 3)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `DetermineType` | 11 | ohne Kandidat |  | Aufrufer im Client: AuExcelBinaryLib::ReadExcelFile; kein unbenannter Kandidat mit Beleg unter 7776 unbenannten Funktionen im Klassenbereich |
| `GetMaxBlockSize` | 10 | ohne Kandidat |  | Aufrufer im Client: AuExcelBinaryLib::AuExcelBinaryLib, AuExcelBinaryLib::ReadExcelFile; kein unbenannter Kandidat mit Beleg unter 7776 unbenannten Funktionen im Klassenbereich |
| `ReadTypeFromString` | 33 | ohne Kandidat |  | Aufrufer im Client: AuExcelBinaryLib::AuExcelBinaryLib; kein unbenannter Kandidat mit Beleg unter 7776 unbenannten Funktionen im Klassenbereich |

## Image2D (eingebaut 1, nicht als eigene Funktion 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SetPos` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmGrass::LoadGrass, AgcmDmgBoard::_DrawDamage, AgcmDmgBoard::_DrawCriticalDamage; im Adressbereich der Klasse (0x007B3DE0–0x007B3F00) ist keine unbenannte Funktion mehr übrig |
| `SetUV` | 12 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmDmgBoard::_DrawDamage, AgcmDmgBoard::_DrawCriticalDamage, AgcmHPBar::_DrawHPBar; im Adressbereich der Klasse (0x007B3DE0–0x007B3F00) ist keine unbenannte Funktion mehr übrig |
| `SetColor` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmDmgBoard::_DrawDamage, AgcmDmgBoard::_DrawCriticalDamage, AgcmHPBar::SetData |

## MagImAtomic (nicht als eigene Funktion 4)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CreateAtomic` | 28 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::CreateSkyAtomic, AgcmEventNature::CreateCloudAtomic, AgcmEventNature::CreateCircumstanceAtomic; im Adressbereich der Klasse (0x007183E0–0x007183E0) ist keine unbenannte Funktion mehr übrig |
| `DestroyAtomic` | 34 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmEventNature::CreateCloudAtomic, AgcmEventNature::CleanAllData, MagImAtomic::~MagImAtomic; im Adressbereich der Klasse (0x007183E0–0x007183E0) ist keine unbenannte Funktion mehr übrig |
| `Render` | 44 | nicht als eigene Funktion |  | Aufrufer im Client: AgcdEffCtrl_Set::Render, AgcdEffCtrl_Set::CB_Render, AgcmEventNature::RenderSky; im Adressbereich der Klasse (0x007183E0–0x007183E0) ist keine unbenannte Funktion mehr übrig |
| `SetTexture` | 26 | nicht als eigene Funktion |  | Aufrufer im Client: AgcmCustomizeRender::DrawQuad, AgcmEventNature::CreateSkyAtomic, AgcmEventNature::CreateCloudAtomic; im Adressbereich der Klasse (0x007183E0–0x007183E0) ist keine unbenannte Funktion mehr übrig |

## TiXmlAttribute (eingebaut 6, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `Next` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmMap::MyCharacterPositionChange, AgcmTitle::_LoadAllTitleCategoryInfo, TiXmlBase::EncodeString |
| `Previous` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: AgcmExportResource::ReadCharacterTemplate, AgcmExportResource::ReadItemTemplate, AgcmExportResource::ReadObjectTemplate |
| `QueryIntValue` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString |
| `QueryDoubleValue` | 4 | eingebaut |  | kleine Funktion (4 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString |
| `SetIntValue` | 8 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 33 unbenannten Funktionen im Klassenbereich |
| `SetDoubleValue` | 8 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 33 unbenannten Funktionen im Klassenbereich |
| `IntValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString |
| `DoubleValue` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString |

## TiXmlBase (nicht im Client 3, ohne Kandidat 5, zugeordnet 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SkipWhiteSpace` | 47 | zugeordnet | `0x00874C50` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `EncodeString` | 886 | ohne Kandidat |  | Aufrufer im Client: TiXmlAttribute::Print, TiXmlText::Print, TiXmlPrinter::Visit; kein unbenannter Kandidat mit Beleg unter 72 unbenannten Funktionen im Klassenbereich |
| `ConvertUTF32ToUTF8` | 37 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::GetEntity; kein unbenannter Kandidat mit Beleg unter 72 unbenannten Funktionen im Klassenbereich |
| `IsAlpha` | 17 | ohne Kandidat |  | Aufrufer im Client: AgpmConfig::SetExpAdjustmentRatio, AgpmConfig::SetDropAdjustmentRatio, AgpmConfig::SetDrop2AdjustmentRatio; kein unbenannter Kandidat mit Beleg unter 72 unbenannten Funktionen im Klassenbereich |
| `IsAlphaNum` | 17 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::ReadName; kein unbenannter Kandidat mit Beleg unter 72 unbenannten Funktionen im Klassenbereich |
| `StreamWhiteSpace` | 12 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `StreamTo` | 14 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |
| `ReadName` | 34 | ohne Kandidat |  | Aufrufer im Client: TiXmlAttribute::Parse; kein unbenannter Kandidat mit Beleg unter 72 unbenannten Funktionen im Klassenbereich |
| `GetEntity` | 102 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## TiXmlComment (eingebaut 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CopyTo` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString, TiXmlDocument::CopyTo, TiXmlDocument::Clone |
| `Accept` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmQuest::ReadXMLData, TiXmlBase::EncodeString, TiXmlDocument::Accept |
| `Clone` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CreateArmourPartClumpCB, AgcmItem::AttachNodeIndex, TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 51 unbenannten Funktionen im Klassenbereich |

## TiXmlDeclaration (eingebaut 2, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CopyTo` | 6 | eingebaut |  | kleine Funktion (6 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString, TiXmlDocument::CopyTo, TiXmlDocument::Clone |
| `Accept` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmQuest::ReadXMLData, TiXmlBase::EncodeString, TiXmlDocument::Accept |
| `Clone` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CreateArmourPartClumpCB, AgcmItem::AttachNodeIndex, TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `StreamIn` | 19 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |

## TiXmlDocument (ohne Kandidat 5)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `SaveFile` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::SaveChatFile, stAutoPickUpSettings::SaveToFile, AgpmItem::_SaveXmlFile; kein unbenannter Kandidat mit Beleg unter 7371 unbenannten Funktionen im Klassenbereich |
| `SaveFile` | 13 | ohne Kandidat |  | Aufrufer im Client: AgcChatManager::SaveChatFile, stAutoPickUpSettings::SaveToFile, AgpmItem::_SaveXmlFile; kein unbenannter Kandidat mit Beleg unter 7371 unbenannten Funktionen im Klassenbereich |
| `CopyTo` | 15 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::EncodeString, TiXmlDocument::Clone, TiXmlComment::TiXmlComment; kein unbenannter Kandidat mit Beleg unter 7371 unbenannten Funktionen im Klassenbereich |
| `Clone` | 7 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CreateArmourPartClumpCB, AgcmItem::AttachNodeIndex, TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 7371 unbenannten Funktionen im Klassenbereich |
| `Accept` | 10 | ohne Kandidat |  | Aufrufer im Client: AgcmQuest::ReadXMLData, TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 7371 unbenannten Funktionen im Klassenbereich |

## TiXmlText (eingebaut 2, nicht im Client 1, ohne Kandidat 2)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CopyTo` | 3 | eingebaut |  | kleine Funktion (3 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString, TiXmlDocument::CopyTo, TiXmlDocument::Clone |
| `Accept` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmQuest::ReadXMLData, TiXmlBase::EncodeString, TiXmlDocument::Accept |
| `Clone` | 9 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CreateArmourPartClumpCB, AgcmItem::AttachNodeIndex, TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `StreamIn` | 27 | ohne Kandidat |  | Aufrufer im Client: TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 36 unbenannten Funktionen im Klassenbereich |
| `Blank` | 5 | nicht im Client |  | kein Aufrufer in der Quelle; kein Treffer im Binary |

## TiXmlUnknown (eingebaut 2, ohne Kandidat 1)

| Methode | Zeilen | Status | Adresse | Beleg |
|---|---:|---|---|---|
| `CopyTo` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: TiXmlBase::EncodeString, TiXmlDocument::CopyTo, TiXmlDocument::Clone |
| `Accept` | 2 | eingebaut |  | kleine Funktion (2 Zeilen); Aufrufer im Client: AgcmQuest::ReadXMLData, TiXmlBase::EncodeString, TiXmlDocument::Accept |
| `Clone` | 8 | ohne Kandidat |  | Aufrufer im Client: AgcmItem::CreateArmourPartClumpCB, AgcmItem::AttachNodeIndex, TiXmlBase::EncodeString; kein unbenannter Kandidat mit Beleg unter 48 unbenannten Funktionen im Klassenbereich |
