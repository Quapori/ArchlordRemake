# AgcmCamera2 (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmCamera2` (Kamera: Verfolgung, Zoom, Drehung, Pfade, Dämpfung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmCamera2/AgcmCamera2.cpp`. Die Hilfsklassen `AgcuCamMode`, `AgcuCamDampingForce`, `AgcuCamSpringForce`, `AgcuCamConstrain` und `AgcuCamPathWork` aus derselben Quelle sind nicht abgeglichen. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Vtable, Rückrufe, Leerlauf-Typen, Drehen/Zoomen, Matrixaufbau und Durchsichtigkeit. Die kleinen Zugriffsfunktionen (`bGetPtr…`, Flag- und Maskenfunktionen) sind eingebaut; `OptionFromFile` (Datei `cam2opt.txt`) und `vShowInfo` wurden im Binary nicht gefunden.
- **Modulaufbau:** sechs Module, fünf Rückrufanmeldungen, zehn Lua-Funktionen, sechs AngelScript-Einträge (zwei Methoden, vier Variablen) wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmCamera2.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `bGetPtrCX` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 1 | `bGetPtrCY` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `bGetPtrCZ` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 3 | `bGetPtrEye` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 4 | `bGetPtrLookat` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 5 | `bRotWY` | `0x006F1270` | 134 | von Hand geprüft |
| 6 | `bRotCX` | `0x006F1F50` | 146 | von Hand geprüft |
| 7 | `bZoom` | `0x006F1FF0` | 125 | von Hand geprüft |
| 8 | `bMove` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `bTurnWY_180` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `bSetTargetFrame` | `0x006F1340` | 94 | von Hand geprüft |
| 11 | `bSetIdleType` | `0x006F2E90` | 143 | von Hand geprüft |
| 12 | `CBOnTargetMove` | `0x006F13A0` | 50 | Callback-Registrierung |
| 13 | `CBOnTargetStop` | `0x006F0880` | 22 | Callback-Registrierung |
| 14 | `CBOnTargetSet` | `0x006F2F20` | 216 | Callback-Registrierung |
| 15 | `CBIsCameraMoving` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `CBTurnCamera` | `0x006F13E0` | 79 | Callback-Registrierung |
| 17 | `bOnMoveTarget` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `bSetCamFrm` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `bSetCamFrm` | `0x006F08A0` | 659 | von Hand geprüft |
| 20 | `bSetCamFrm` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `bSetViewWindow` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `bGetViewWindow` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 23 | `vOnIdle_default` | `0x006F2070` | 1994 | von Hand geprüft |
| 24 | `vOnIdle_Login` | `0x005BDCF0` | 3 | gleiche Adresse wie `leerer gemeinsamer Rumpf` (vom Linker zusammengefaltet) |
| 25 | `vOnIdle_modechage` | `0x006F1590` | 122 | von Hand geprüft |
| 26 | `vUpdateMatrix` | `0x006F1610` | 370 | von Hand geprüft |
| 27 | `vForcedZoom` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `vForcedRotCX` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `vAdjLookAt` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `vAdjAlpha` | `0x006F18B0` | 320 | von Hand geprüft |
| 31 | `bTransparentMainCharac` | `0x006F19F0` | 193 | von Hand geprüft |
| 32 | `OnAddModule` | `0x006F3000` | 284 | vtable/String |
| 33 | `OnInit` | `0x006F41E0` | 1895 | von Hand geprüft |
| 34 | `Info` | `0x006F0C10` | 628 | Zeichenkette |
| 35 | `ChangeHeight` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 36 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 37 | `OnIdle` | `0x006F1AC0` | 202 | vtable/String |
| 38 | `bLockAct` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 39 | `bUnlockAct` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 40 | `vLockFlagChk` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 41 | `bOptFlagOn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 42 | `bOptFlagOff` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `vOptFlagChk` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 44 | `vUdtMaskOn` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 45 | `vUdtMaskOff` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 46 | `vUdtMaskChk` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 47 | `vAvailablePitch` | `0x006F1B90` | 257 | von Hand geprüft |
| 48 | `vAvailableZoom` | `0x006F1CA0` | 163 | von Hand geprüft |
| 49 | `vShowInfo` | – | | im Binary nicht gefunden (Ausgabe über die Konsole) |
| 50 | `OnLuaInitialize` | `0x006F4C90` | 231 | vtable/String |
| 51 | `CBRegionChange` | `0x006F2CE0` | 198 | von Hand geprüft |
| 52 | `OptionFromFile` | – | | Zeichenkette `cam2opt.txt` fehlt im Binary |
| 53 | `RenderFrustum` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

25 von 54 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006f3ae0` (`0x006F3AE0`), `ctor_or_dtor_006f3b50` (`0x006F3B50`), `~AgcmCamera2` (`0x006F3E20`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Optionsflags (Bit 0 Federkraft, Bit 1 Dämpfung, Bit 4 Neigungsgrenze, Bit 5 Zoomgrenze)` | `bRotWY`, `vAvailablePitch`, `vAvailableZoom` |
| `this+0xC04` | `Aktualisierungsmaske (Bit 0 Gieren, Bit 8 180°-Drehung, Bit 9 Moduswechsel)` | `bRotWY`, `vOnIdle_modechage` |
| `this+0xC64 / 0xC68` | `Leerlauf-Typ / Zeiger auf den Leerlauf-Rückruf` | `bSetIdleType` |
| `this+0xC54 / 0xC58` | `kleinste / größte Entfernung (`m_fMinLen` / `m_fMaxLen`)` | `vAvailableZoom`, `CBRegionChange` |

## Vtable

Vtable bei `0x008D9914`: Slot 0 Destruktor `0x006F3E20`, 1 `OnAddModule` (`0x006F3000`), 2 `OnInit` (`0x006F41E0`, früher fälschlich als `vShowInfo` benannt), 3 `OnIdle` (`0x006F1AC0`), 4 und 5 gemeinsamer Rumpf `0x0067FAB0`, 6 und 7 gemeinsamer Rumpf `0x0067AC90` (`OnDestroy` = `return TRUE`), 14 `OnLuaInitialize` (`0x006F4C90`).

## OnAddModule (0x006F3000)

Holt sechs Module in der Reihenfolge der Quelle: [`AgcmMap`](AgcmMap.md), [`ApmObject`](ApmObject.md), [`AgcmObject`](AgcmObject.md), [`AgcmRender`](AgcmRender.md), `AgcmCharacter`, [`AgpmCharacter`](AgpmCharacter.md). Danach folgen die Rückrufe: bei `AgpmCharacter` „Position aktualisiert“ → `CBOnTargetMove` (`0x006F13A0`), bei `AgcmCharacter` „eigener Charakter stoppt“ und „eigener Charakter freigegeben“ beide → `CBOnTargetStop` (`0x006F0880`), „eigener Charakter gesetzt“ → `CBOnTargetSet` (`0x006F2F20`) und „Kamera drehen“ → `CBTurnCamera` (`0x006F13E0`). Zuletzt setzt `bSetCamFrm` die Startlage.

## OnInit und Lua

`OnInit` (`0x006F41E0`, 1895 Byte) meldet über AngelScript (`AS_REGISTER_TYPE`) die Methoden `Info` und `ChangeHeight(float,float)` sowie die Variablen `m_fMinLen`, `m_fMaxLen`, `m_fMinPitch`, `m_fMaxPitch` an (Zeichenketten im Binary) und meldet `CBRegionChange` (`0x006F2CE0`) bei `AgpmCharacter` an. `OnLuaInitialize` (`0x006F4C90`) legt zehn Lua-Funktionen an: `ClearCameraState`, `PushCameraState`, `PopCameraState`, `SetPathWorkDuration`, `PlaySpline`, `StopSpline`, `SaveSpline`, `LoadSpline`, `PushCameraPosition`, `PopCameraPosition`; die Namen stimmen mit der Quelle überein.

## Leerlauf und Steuerung

`bSetIdleType` (`0x006F2E90`) wählt den Leerlauf-Rückruf: Typ 0 → `vOnIdle_default` (`0x006F2070`, 1994 Byte), Typ 1 → `vOnIdle_Login` (leerer gemeinsamer Rumpf `0x005BDCF0`), Typ 2 → `vOnIdle_modechage` (`0x006F1590`). `vUpdateMatrix` (`0x006F1610`) baut aus `m_v3dEyeSubAt` die Kamerarotation (zweimal `atan2f`). `bRotWY` (`0x006F1270`), `bRotCX` (`0x006F1F50`) und `bZoom` (`0x006F1FF0`) geben bei gesetztem Dämpfungs-Flag den Wert an `AgcuCamDampingForce` weiter, sonst addieren sie direkt; Betragsgrenze 0,0001 wie in der Quelle. `vAvailablePitch` (`0x006F1B90`) und `vAvailableZoom` (`0x006F1CA0`) begrenzen mit `m_fMinLen`/`m_fMaxLen` bzw. den Pitch-Grenzen.

## Durchsichtigkeit

`vAdjAlpha` (`0x006F18B0`) und `bTransparentMainCharac` (`0x006F19F0`) schalten die Figur über [`AgcmShadowmap`](AgcmShadowmap.md) (Clump an-/abmelden) und `AgcmRender` (`StartTransparentClump`/`EndTransparentClump`) durchsichtig; der Aufruf mit `m_fMinLen + 1` und die Zeichenkette `AgcmShadowmap` bestätigen die Zuordnung.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der Dreh-, Zoom- und Matrixfunktionen stützt sich auf Aufrufbeziehungen zu den `AgcuCam…`-Klassen, Konstanten und Größen, nicht auf einen Vergleich Zeile für Zeile; am unsichersten sind `bRotCX`/`bZoom` (Unterscheidung nach Aufruf von `bAddOmegaX`/`bAddZoomSpeed`) und `vAdjAlpha`.
- Die Offsets stammen aus den Zugriffen in den genannten Funktionen; die Bedeutung einzelner Bits der Masken wurde nicht vollständig mit den Aufzählungen der Quelle abgeglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 15, gemeinsamer Rumpf: 1, nicht im Client: 6, ohne Kandidat: 8, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `bGetPtrEye` | 10 | `0x006F0830` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmMap`](AgcmMap.md), [`AgcmObject`](AgcmObject.md), [`AgcmRender`](AgcmRender.md), [`AgcmShadowmap`](AgcmShadowmap.md), [`AgpmCharacter`](AgpmCharacter.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcmGlyph`](AgcmGlyph.md)
