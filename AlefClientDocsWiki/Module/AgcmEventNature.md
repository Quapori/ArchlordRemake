# AgcmEventNature (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventNature` (Himmel, Wolken, Sonne, Nebel, Wetter, Hintergrundmusik) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmEventNature/AgcmEventNature.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Zeit-/Wetterlogik, Himmelsteile, Ereignis-Objekte und die Texturverwaltung. Die Vertex-Erzeuger (`Create…Atomic`) und die Sternfunktionen sind nicht eindeutig zugeordnet.
- **Modulaufbau:** zwölf Module in Quellreihenfolge, Rückrufe wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventNature.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `__PreRenderCallback` | `0x005D2D00` | 15 | Callback-Registrierung |
| 1 | `IsMaptoolBuild` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 2 | `OnAddModule` | `0x005D6F30` | 621 | vtable/String |
| 3 | `OnInit` | `0x005D72C0` | 1156 | vtable/String |
| 4 | `OnDestroy` | `0x005D6000` | 107 | vtable/String |
| 5 | `OnLuaInitialize` | `0x005D7230` | 135 | vtable/String |
| 6 | `OnIdle` | `0x005D60A0` | 261 | vtable/String |
| 7 | `Init` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 8 | `ShowSky` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `LoadTextureScriptFile` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `SaveTextureScriptFile` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `CreateSkyAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `ModifySky` | `0x005D0F40` | 279 | von Hand geprüft |
| 13 | `CreateCloudAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `CreateCircumstanceAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 15 | `CreateSunAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `ChangeSunSize` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `GetDefaultSky` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 18 | `SetCharacterPosition` | `0x005D69B0` | 1092 | von Hand geprüft |
| 19 | `MoveSky` | `0x005D1240` | 704 | von Hand geprüft |
| 20 | `OnMyCharacterPositionChange` | `0x005D6E00` | 65 | Callback-Registrierung |
| 21 | `AddTexture` | `0x005D2D10` | 175 | von Hand geprüft |
| 22 | `GetTexture` | `0x005D2DC0` | 171 | Zeichenkette |
| 23 | `RemoveTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 24 | `GetTextureIndex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 25 | `RemoveAllTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 26 | `SetTime` | `0x005D4D40` | 3404 | Zeichenkette |
| 27 | `SetTimeForce` | `0x005D5A90` | 1034 | von Hand geprüft |
| 28 | `SetSkyRadius` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 29 | `SetSkyRadius` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `SetFog` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 31 | `SetCloud` | `0x005D3430` | 767 | von Hand geprüft |
| 32 | `SetSun` | `0x005D3730` | 451 | von Hand geprüft |
| 33 | `SetCircumstance` | `0x005D3900` | 427 | von Hand geprüft |
| 34 | `ModifyAtomic` | `0x005D2E70` | 155 | von Hand geprüft |
| 35 | `SetSkyHeight` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 36 | `EnableFog` | `0x005D0390` | 52 | von Hand geprüft |
| 37 | `SetFogSetting` | `0x005D03D0` | 95 | von Hand geprüft |
| 38 | `OnSkySetCreate` | `0x005D1500` | 77 | Callback-Registrierung |
| 39 | `OnSkySetDestroy` | `0x005D1550` | 34 | Callback-Registrierung |
| 40 | `SkySetStreamWriteCB` | `0x005D1580` | 1703 | Callback-Registrierung |
| 41 | `SkySetStreamReadCB` | `0x005D1C80` | 1872 | Callback-Registrierung |
| 42 | `GetSkySetClientData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 43 | `SetNextWeather` | `0x005D4000` | 923 | von Hand geprüft |
| 44 | `ResampleTexture` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 45 | `UpdateProjectionMatrix` | `0x005D0560` | 187 | von Hand geprüft |
| 46 | `RenderSky` | `0x005D2420` | 522 | von Hand geprüft |
| 47 | `ApplySkySetting` | `0x005D5EA0` | 108 | von Hand geprüft |
| 48 | `__SetTime` | `0x005D5F10` | 58 | von Hand geprüft |
| 49 | `__SetFog` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 50 | `CreateSkyAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 51 | `ModifyAtomic` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 52 | `__MoveSky` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 53 | `__SetSkyRadius` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 54 | `__SetSkyTemplateID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 55 | `CBOnAddObject` | `0x005D3AB0` | 618 | Callback-Registrierung |
| 56 | `CBOnRemoveObject` | `0x005D43A0` | 81 | Callback-Registrierung |
| 57 | `AddEventNatureObject` | `0x005D0620` | 1455 | von Hand geprüft |
| 58 | `CloudUVShift` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 59 | `SkyChange` | `0x005D3E20` | 97 | von Hand geprüft |
| 60 | `PlayBGM` | `0x005D2F10` | 340 | von Hand geprüft |
| 61 | `CBLoadSector` | `0x005D4400` | 112 | Callback-Registrierung |
| 62 | `UpdateSectorNatureObject` | `0x005D0BD0` | 141 | von Hand geprüft |
| 63 | `CBReceiveTime` | `0x005D5F50` | 40 | Callback-Registrierung |
| 64 | `CBNature` | `0x005D0C60` | 149 | Callback-Registrierung |
| 65 | `UpdateSectorNatureInfo` | `0x005D3E90` | 67 | von Hand geprüft |
| 66 | `SetSkyTemplateID` | `0x005D6540` | 64 | von Hand geprüft |
| 67 | `SetSkyTemplateID` | `0x005D61B0` | 896 | von Hand geprüft |
| 68 | `SetSkyCircleRadius` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 69 | `UpdateSunPosition` | `0x005D0D00` | 132 | von Hand geprüft |
| 70 | `GetSunPosition` | `0x005D0D90` | 38 | von Hand geprüft |
| 71 | `SetCloudZoomRate` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 72 | `CBOnSetSelfCharacter` | `0x005D6E50` | 74 | Callback-Registrierung |
| 73 | `RenderStar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 74 | `BlinkStar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 75 | `DestroyStar` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 76 | `GenerateStarVertex` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 77 | `LoadStarData` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 78 | `AddSkyObject` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 79 | `RemoveSkyObject` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 80 | `CBOnSetAutoLoadChange` | `0x005D5F80` | 87 | Callback-Registrierung |
| 81 | `NewD3D9ReleaseDeviceCB` | `0x005D2AE0` | 24 | Callback-Registrierung |
| 82 | `NewD3D9RestoreDeviceCB` | `0x005D2B00` | 38 | Callback-Registrierung |
| 83 | `OnLostDevice` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 84 | `OnResetDevice` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 85 | `SetNatureEffectSkyTemplateID` | `0x005D6580` | 870 | von Hand geprüft |
| 86 | `EndNatureEffectSky` | `0x005D6EA0` | 103 | von Hand geprüft |
| 87 | `CBOnNatureEffectStart` | `0x005D68F0` | 25 | Callback-Registrierung |
| 88 | `CBOnNatureEffectEnd` | `0x005D6F10` | 31 | Callback-Registrierung |
| 89 | `_ChangeEnvironmentSound` | `0x005D3070` | 307 | Zeichenkette |

52 von 90 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x005D4B00`), `~AgcmEventNature` (`0x005D5FE0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xD24` | `Kopf der Texturliste` | `AddTexture` |
| `this+0xD5C` | `Merker „Nebel an“` | `EnableFog` |
| `this+0x29B4` | `Merker „Nebel aktualisieren“` | `SetFogSetting` |
| `this+0x27D4…0x27DC` | `letzte Spielerposition` | `UpdateSunPosition` |
| `this+0x2A8C` | `Sonnenkreis-Radius` | `UpdateSunPosition` |
| `this+0x2A90…0x2A98` | `Sonnenposition` | `UpdateSunPosition`, `GetSunPosition` |

## OnAddModule (0x005D6F30)

Holt zwölf Module in dieser Reihenfolge: `AgcmCharacter`, [`AgcmEff2`](AgcmEff2.md), [`AgpmEventNature`](AgpmEventNature.md), [`AgcmRender`](AgcmRender.md), [`ApmMap`](ApmMap.md), [`AgcmMap`](AgcmMap.md), [`ApmEventManager`](ApmEventManager.md), [`ApmObject`](ApmObject.md), [`AgcmSound`](AgcmSound.md), [`AgpmTimer`](AgpmTimer.md), [`AgcmNatureEffect`](AgcmNatureEffect.md), [`AgcmResourceLoader`](AgcmResourceLoader.md) (Zeichenketten im Dekompilat, gleiche Reihenfolge wie die Quelle). Danach folgen die Rückrufe: bei `AgcmCharacter` „eigene Position geändert“ und „eigener Charakter gesetzt“ (`CBOnSetSelfCharacter` `0x005D6E50`), bei `AgpmEventNature` `CBNature` (`0x005D0C60`), bei `AgcmMap` Sektor laden (`CBLoadSector`, `0x005D4400`) und „Auto-Laden geändert“ (`CBOnSetAutoLoadChange`, `0x005D5F80`; die Funktion `0x005D71A0` wurde früher fälschlich als zweites `CBOnSetAutoLoadChange` geführt, sie passt nicht zur Quelle und ist unbenannt), bei `AgcmRender` der Vor-Render-Rückruf, bei `AgcmNatureEffect` Effekt-Start/-Ende (`0x005D68F0`, `0x005D6F10`), bei `ApmObject` Objekt hinzufügen/entfernen (`0x005D3AB0`, `0x005D43A0`) und bei `AgpmTimer` `CBReceiveTime` (`0x005D5F50`).

## OnInit und Lua

`OnInit` (`0x005D72C0`, 1156 Byte) ruft `Init`, schaltet den Himmel ein, setzt über `SetTime` die Spielzeit und ruft `SkyChange` sowie `MoveSky`. Danach meldet es über AngelScript (`AS_REGISTER_TYPE`) die Variablen `m_fNearValue`, `m_fNormalValue` und `m_bSkyFogDisable` an (Zeichenketten im Binary). `OnLuaInitialize` (`0x005D7230`) legt die vier Lua-Funktionen `EndSkySet`, `ApplySkySetting`, `SetNextWeather` und `SetSkyTemplateID` an, wie in der Quelle.

## Zeit, Wetter und Himmelswechsel

`SetTime` (`0x005D4D40`, 3404 Byte) ist die größte Funktion des Moduls; `SetTimeForce` (`0x005D5A90`) wird von `ApplySkySetting` (`0x005D5EA0`: Spielzeit, Stunde, Minute lesen, dann `SetTimeForce`) und von `__SetTime` (`0x005D5F10`) gerufen. `SetNextWeather` (`0x005D4000`) ruft `SkyChange` (`0x005D3E20`), und `SkyChange` ruft `_ChangeEnvironmentSound`. `PlayBGM` (`0x005D2F10`) bildet mit `%s\%s` den Musikpfad.

## Himmelsteile

`SetCloud` (`0x005D3430`, fünf `ModifyAtomic`-Aufrufe), `SetSun` (`0x005D3730`) und `SetCircumstance` (`0x005D3900`) liegen in dieser Reihenfolge hintereinander wie in der Quelle; `ModifyAtomic` (`0x005D2E70`) setzt Farbe und Sichtbarkeit (Alpha 0 → unsichtbar). `UpdateSunPosition` (`0x005D0D00`) rechnet `Sonne = letzte Position − Blickrichtung × Radius`, `GetSunPosition` (`0x005D0D90`) kopiert die drei Werte. `EnableFog` (`0x005D0390`) schreibt den Nebel-Zustand in die Engine, `SetFogSetting` (`0x005D03D0`) übernimmt bei gesetztem Merker die Nebelfarbe.

## Ereignis-Objekte

`AddEventNatureObject` (`0x005D0620`, 1455 Byte) verteilt die Himmel-Vorlagen auf die Sektorecken (16-Bit-Kennung im oberen, Gewicht im unteren Wort); `UpdateSectorNatureObject` (`0x005D0BD0`) holt die Vorlage des Ereignisses und ruft sie auf; `UpdateSectorNatureInfo` (`0x005D3E90`) durchläuft die Objektliste und entfernt ungültige Einträge.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`OnAddModule`, `OnLuaInitialize`, `OnInit`).

## Grenzen

- Die Zuordnung der Himmelsteile und Hilfsfunktionen stützt sich auf Aufrufbeziehungen, Größen und die Quellreihenfolge, nicht auf einen Vergleich Zeile für Zeile; am unsichersten sind `ModifySky` (`0x005D0F40`) und `SetNatureEffectSkyTemplateID` (`0x005D6580`).
- Die Funktionen `0x005CF670`–`0x005D0280` vor dem Modul gehören zu anderen Klassen (Himmel-Datenstrukturen) und sind nicht Teil dieser Zuordnung.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 2, eingebaut: 5, nicht im Client: 13, ohne Kandidat: 17, zugeordnet: 4.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `DestroyStar` | 21 | `0x005D1060` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `Init` | 59 | `0x005D10E0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GenerateStarVertex` | 92 | `0x005D2630` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `GetDefaultSky` | 51 | `0x005D0080` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SetFog` (`0x005D3D30`), `CloudUVShift` (`0x005D3D30`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEff2`](AgcmEff2.md), [`AgcmMap`](AgcmMap.md), [`AgcmNatureEffect`](AgcmNatureEffect.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmSound`](AgcmSound.md), [`AgpmEventNature`](AgpmEventNature.md), [`AgpmTimer`](AgpmTimer.md), [`ApmEventManager`](ApmEventManager.md), [`ApmMap`](ApmMap.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventPointLight`](AgcmEventPointLight.md), [`AgcmGrass`](AgcmGrass.md), [`AgcmLensFlare`](AgcmLensFlare.md), [`AgcmMap`](AgcmMap.md), [`CBGMTitleViewer`](CBGMTitleViewer.md)
