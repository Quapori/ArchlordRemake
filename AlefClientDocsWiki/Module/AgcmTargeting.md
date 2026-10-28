# AgcmTargeting (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmTargeting` (Maus, Zielwahl, Bewegungsklick, Flächenziel) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmTargeting/AgcmTargeting.cpp`. Die Klasse `AgcSenderWindow` aus derselben Quelle ist nicht abgeglichen. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Maus-Behandlung, Zielwahl, Flächenziel und die Rückrufe. Nicht zugeordnet sind `TargetLast`, `ClearTarget`, `SetTargetBase`, `GetCharacterClump`, `SetRwCamera`, `StreamWriteTemplate`, die Debug-Funktionen und `OnRButtonDown` (Einzeiler).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmTargeting.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006385D0` | 811 | vtable/String |
| 1 | `OnInit` | `0x006379D0` | 1810 | vtable/String |
| 2 | `OnLuaInitialize` | `0x006361B0` | 87 | vtable/String |
| 3 | `OnDestroy` | `0x00636210` | 176 | vtable/String |
| 4 | `OnIdle` | `0x006342A0` | 552 | vtable/String |
| 5 | `OnLButtonDblClk` | `0x00637550` | 173 | von Hand geprüft |
| 6 | `OnRButtonDblClk` | `0x00635E20` | 197 | von Hand geprüft |
| 7 | `OnRButtonDown` | – | | Rumpf in der Quelle leer, gemeinsamer Stub |
| 8 | `OnLButtonDown` | `0x00636DF0` | 1700 | von Hand geprüft |
| 9 | `TargetCID` | `0x006344D0` | 437 | von Hand geprüft |
| 10 | `MoveSelfCharacter` | `0x00634690` | 679 | von Hand geprüft |
| 11 | `OnLButtonUp` | `0x006362C0` | 20 | von Hand geprüft |
| 12 | `OnMouseMove` | `0x00636660` | 1808 | von Hand geprüft |
| 13 | `CBIntersectAtomic` | `0x006362E0` | 645 | von Hand geprüft |
| 14 | `CBDetailCollision` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `AddPickedObject` | `0x006349A0` | 168 | von Hand geprüft |
| 16 | `ClearPickList` | `0x00634A50` | 47 | von Hand geprüft |
| 17 | `CBLoginProcessEnd` | `0x00634A80` | 78 | Callback-Registrierung |
| 18 | `CBEncryptCodeSuccess` | `0x00634AD0` | 117 | Callback-Registrierung |
| 19 | `CBRemoveCharacter` | `0x00634B50` | 133 | Callback-Registrierung |
| 20 | `CB_UnlockTarget` | `0x00634BE0` | 65 | Callback-Registrierung |
| 21 | `CB_LockTarget` | `0x00634C30` | 103 | Callback-Registrierung |
| 22 | `CBRButtonSkill` | `0x00634CA0` | 369 | Callback-Registrierung |
| 23 | `SetRwCamera` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `StreamReadTemplate` | `0x00634E50` | 1876 | Zeichenkette |
| 25 | `StreamWriteTemplate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `SetShowCursor` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 27 | `SetCallbackLButtonDownPickSomething` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `SetCallbackLButtonDownPickNothing` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `GetCharacterClump` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `CB_UpdateActionStatus` | `0x006355C0` | 26 | Callback-Registrierung |
| 31 | `SetTargetBase` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 32 | `ShowTarget` | `0x00635700` | 335 | Zeichenkette |
| 33 | `CBReturnToLoginEndProcess` | `0x00635850` | 25 | Callback-Registrierung |
| 34 | `CBSetTargetMode` | `0x00635870` | 25 | Callback-Registrierung |
| 35 | `TargetNear` | `0x006380F0` | 1071 | von Hand geprüft |
| 36 | `TargetLast` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 37 | `ClearTarget` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 38 | `TargetNearestDebug` | – | | Debug-Funktion, im Binary nicht gefunden |
| 39 | `TargetNextDebug` | – | | Debug-Funktion, im Binary nicht gefunden |
| 40 | `CBAutoTargetingForward` | `0x00638530` | 79 | UI-Registrierung |
| 41 | `CBAutoTargetingBackward` | `0x00638580` | 72 | UI-Registrierung |
| 42 | `StartAreaTargeting` | `0x006358B0` | 517 | von Hand geprüft |
| 43 | `StopAreaTargeting` | `0x00635AC0` | 66 | von Hand geprüft |
| 44 | `OnAreaTargetingDestPosDetected` | `0x00635B10` | 171 | von Hand geprüft |
| 45 | `CBStartGroundTarget` | `0x00635BC0` | 45 | Callback-Registrierung |
| 46 | `UpdateAreaTargeting` | `0x00635BF0` | 81 | von Hand geprüft |
| 47 | `CBKeydownESC` | `0x00635C50` | 69 | Callback-Registrierung |

35 von 48 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00634230` (`0x00634230`), `ctor_or_dtor_00635ef0` (`0x00635EF0`), `~AgcmTargeting` (`0x00636190`).

## Vtable

Vtable-Slots: 0 `~AgcmTargeting` (`0x00636190`), 1 `OnAddModule` (`0x006385D0`), 2 `OnInit` (`0x006379D0`), 3 `OnIdle` (`0x006342A0`), 4 und 5 `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x00636210`).

## OnAddModule (0x006385D0)

Holt 27 Module in dieser Reihenfolge (Zeichenketten im Dekompilat, gleiche Reihenfolge wie die Quelle): [`AgpmCharacter`](AgpmCharacter.md), [`AgcmGlyph`](AgcmGlyph.md), `AgcmCharacter`, [`AgcmEventManager`](AgcmEventManager.md), [`AgcmMap`](AgcmMap.md), [`AgcmSkill`](AgcmSkill.md), [`AgpmItem`](AgpmItem.md), [`AgcmItem`](AgcmItem.md), [`AgcmPrivateTrade`](AgcmPrivateTrade.md), [`ApmEventManager`](ApmEventManager.md), [`AgcmRender`](AgcmRender.md), [`AgcmParty`](AgcmParty.md), [`AgpmFactors`](AgpmFactors.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`ApmMap`](ApmMap.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgpmSiegeWar`](AgpmSiegeWar.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmLogin`](AgcmLogin.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmOcTree`](AgcmOcTree.md), [`ApmOcTree`](ApmOcTree.md), [`AgcmUIMain`](AgcmUIMain.md). Außerdem werden die UI-Funktionen `Targeting_FuncAutoTargetingF` und `Targeting_FuncAutoTargetingB` (Vorwärts- und Rückwärts-Zielwechsel) angelegt; ihre Rückrufe sind `CBAutoTargetingForward` (`0x00638530`) und `CBAutoTargetingBackward` (`0x00638580`), beide rufen `TargetNear` (`0x006380F0`).

## OnInit und Lua

`OnInit` (`0x006379D0`, 1810 Byte) meldet über AngelScript `ShowTarget()` und die Variablen `m_lTargetType`, `m_lTargetID`, `m_lTargetTID` an (Zeichenketten im Binary). `OnLuaInitialize` (`0x006361B0`) legt die Lua-Funktion `SendMoveSelfCharacter` an.

## Mausbedienung

`OnLButtonDown` (`0x00636DF0`, 1700 Byte) ist die große Klick-Behandlung (Charakter, Gegenstand, Schrein, Belagerungsobjekt); `OnLButtonDblClk` (`0x00637550`) ruft sie, wie in der Quelle. `OnMouseMove` (`0x00636660`, 1808 Byte) ändert Cursor und aktualisiert die Zielbasis. `OnLButtonUp` (`0x006362C0`, 20 Byte) ruft `OnAreaTargetingDestPosDetected` (`0x00635B10`), das `CastGroundTargetSkill` auslöst und `StopAreaTargeting` (`0x00635AC0`) ruft. `OnRButtonDblClk` (`0x00635E20`) ruft `MoveSelfCharacter` (`0x00634690`, 679 Byte), das ein Bodenzeichen (`AgcmGlyph::AddStaticGlyph`) setzt.

## Zielwahl

`TargetCID` (`0x006344D0`) löscht das alte Ziel (`DeleteGlyph`), startet `StartEnemyTarget` von `AgcmGlyph` (`0x006E55B0`) und wird von `TargetNear` gerufen. `CBIntersectAtomic` (`0x006362E0`) sammelt per `AddPickedObject` (`0x006349A0`) die getroffenen Objekte; `ClearPickList` (`0x00634A50`) gibt die Liste frei. `StartAreaTargeting` (`0x006358B0`) und `UpdateAreaTargeting` (`0x00635BF0`) steuern das Flächenziel mit einem Bodenzeichen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der Maus-Funktionen folgt den Aufrufbeziehungen untereinander (`OnLButtonDblClk` → `OnLButtonDown`, `OnLButtonUp` → `OnAreaTargetingDestPosDetected`, `OnRButtonDblClk` → `MoveSelfCharacter`), den Bodenzeichen-Aufrufen und der Größe; `OnLButtonDown` und `OnMouseMove` (`0x00636DF0` und `0x00636660`) sind nur über diese Struktur und die Aufrufmengen getrennt.
- `TargetCID`, `CBIntersectAtomic`, `AddPickedObject` und `ClearPickList` sind über Aufrufbeziehungen und Größen zugeordnet, nicht Zeile für Zeile verglichen.
- `StartEnemyTarget` (`0x006E55B0`) gehört zu `AgcmGlyph`; der Name wurde dort ergänzt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, gemeinsamer Rumpf: 2, nicht im Client: 4, ohne Kandidat: 4.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmItem`](AgcmItem.md), [`AgcmLogin`](AgcmLogin.md), [`AgcmMap`](AgcmMap.md), [`AgcmOcTree`](AgcmOcTree.md), [`AgcmParty`](AgcmParty.md), [`AgcmPrivateTrade`](AgcmPrivateTrade.md), [`AgcmRender`](AgcmRender.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmShadow`](AgcmShadow.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmSiegeWar`](AgcmSiegeWar.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUICharacter`](AgcmUICharacter.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmSiegeWar`](AgpmSiegeWar.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmGlyph`](AgcmGlyph.md), [`AgcmMap`](AgcmMap.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md)
