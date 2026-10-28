# AgcmGlyph (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmGlyph` (Bodenzeichen: Zielmarkierungen, Bewegungsziel, Gegnerziel) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmGlyph/AgcmGlyph.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; zugeordnet sind Modulaufbau, Rückrufe, Leerlauf mit den drei Aktualisierungen, die beiden Vertexfunktionen, `AddStaticGlyph`, `DeleteGlyph`, `StartEnemyTarget` (`0x006E55B0`, von [`AgcmTargeting`](AgcmTargeting.md) gerufen) und die Texturmatrix. Nicht zugeordnet sind `AddMovableGlyph`, `StartDestMoveTarget`, `CB_CUSTOM_RENDER` und die Kleinfunktionen.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmGlyph.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006E66F0` | 273 | vtable/String |
| 1 | `OnInit` | `0x006E72E0` | 1264 | vtable/String |
| 2 | `OnDestroy` | `0x006E5B60` | 169 | vtable/String |
| 3 | `OnIdle` | `0x006E7270` | 100 | vtable/String |
| 4 | `AddStaticGlyph` | `0x006E5C10` | 389 | von Hand geprüft |
| 5 | `AddMovableGlyph` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 6 | `UpdateGlyph` | `0x006E70B0` | 438 | von Hand geprüft |
| 7 | `DeleteGlyph` | `0x006E5DA0` | 197 | von Hand geprüft |
| 8 | `UpdatePosStaticGlyph` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `ResizeGlyph` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `AtomicsRenderProcess` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 11 | `AllMaterialRwTexturePointerSwap` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `AllMaterialRwTexturePointerRestore` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 13 | `CB_CUSTOM_RENDER` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 14 | `CB_POST_RENDER` | `0x006E5E70` | 1522 | Callback-Registrierung |
| 15 | `StartDestMoveTarget` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 16 | `StopDestMoveTarget` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 17 | `UpdateDestMoveTarget` | `0x006E41C0` | 2099 | von Hand geprüft |
| 18 | `SetMouseOnTargetClump` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 19 | `StartEnemyTarget` | `0x006E55B0` | 634 | von Hand geprüft |
| 20 | `StopEnemyTarget` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 21 | `CloseEnemyTargetSelectWindow` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 22 | `UpdateDestEnemyTarget` | `0x006E5830` | 807 | von Hand geprüft |
| 23 | `CB_SELF_CHARACTER_CAST_SKILL` | `0x006E4A40` | 162 | Callback-Registrierung |
| 24 | `SetVerts` | `0x006E4AF0` | 2094 | von Hand geprüft |
| 25 | `SetVertsCompact` | `0x006E6890` | 2067 | von Hand geprüft |
| 26 | `CB_CLEAR_CLUMPLIST` | `0x006E6470` | 46 | Callback-Registrierung |
| 27 | `AddRenderClumplist` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 28 | `UpdateProjectivelyTextureMatrix` | `0x006E5320` | 409 | von Hand geprüft |
| 29 | `IsGlyphedFrame` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 30 | `ShowDestMoveTarget` | `0x006E54F0` | 11 | as-register |
| 31 | `HideDestMoveTarget` | `0x006E5500` | 11 | as-register |

18 von 32 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_006e64a0` (`0x006E64A0`), `ctor_or_dtor_006e6660` (`0x006E6660`), `~AgcmGlyph` (`0x006E6870`).

## OnAddModule (0x006E66F0)

Holt elf Module in der Reihenfolge der Quelle: [`AgcmRender`](AgcmRender.md) (mit sofortiger Anmeldung von `CB_POST_RENDER` `0x006E5E70`), [`AgcmMap`](AgcmMap.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), `AgcmCharacter`, [`AgpmItem`](AgpmItem.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`AgpmFactors`](AgpmFactors.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmCamera2`](AgcmCamera2.md), [`ApmObject`](ApmObject.md), [`AgcmObject`](AgcmObject.md). Danach meldet es laut Quelle bei `AgcmSkill` den Rückruf „eigener Charakter beginnt zu wirken“ → `CB_SELF_CHARACTER_CAST_SKILL` (`0x006E4A40`) an und bei `AgcmMap` den Rückruf „Karte laden“ → `CB_CLEAR_CLUMPLIST` (`0x006E6470`); im Dekompilat ist die erste Anmeldung (`0x0058C480`) sichtbar, die zweite wurde nicht einzeln gelesen.

## OnInit (0x006E72E0)

Lädt die Zeichentexturen `Particles.tif`, `ET_Default.tif`, `ET_Magic.tif`, `ET_Water.tif`, `ET_Fire.tif`, `ET_Earth.tif`, `ET_Wind.tif`, `ET_Default_Deco.tif` (Zeichenketten im Binary) und meldet über AngelScript die Methoden `void ShowDestMoveTarget()` und `void HideDestMoveTarget()` an (Typname `AgcmGlyph`).

## OnIdle und Aktualisierung

`OnIdle` (`0x006E7270`) liest die Kameramatrix (Blickrichtung) und ruft in dieser Reihenfolge `UpdateGlyph` (`0x006E70B0`), `UpdateDestMoveTarget` (`0x006E41C0`) und `UpdateDestEnemyTarget` (`0x006E5830`). `UpdateGlyph` ruft für jedes sichtbare Glyph `SetVertsCompact` (`0x006E6890`, 2067 Byte); `UpdateDestEnemyTarget` ruft `SetVerts` (`0x006E4AF0`, 2094 Byte). `UpdateDestMoveTarget` (2099 Byte) enthält die Vertexberechnung offenbar eingebaut.

## Glyph-Verwaltung

`AddStaticGlyph` (`0x006E5C10`) leert die Clumpliste, legt ein `GlyphData` (92 Byte, `0x5C`) an, setzt Textur-Adressierung (`+0x51 = 0x33` im Textur-Objekt), Kugel und Größe. `DeleteGlyph` (`0x006E5DA0`) gibt die Puffer frei. `UpdateProjectivelyTextureMatrix` (`0x006E5320`) rechnet die Texturmatrix mit D3DX-Funktionen und wird von `CB_POST_RENDER` gerufen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung der drei Aktualisierungsfunktionen und der beiden Vertexfunktionen folgt der Aufrufreihenfolge in `OnIdle` und der Quelle (`SetVertsCompact` aus `UpdateGlyph`, `SetVerts` aus `UpdateDestEnemyTarget`); `UpdateDestMoveTarget` ist wegen der Größe von 2099 Byte nur indirekt belegt.
- `AddStaticGlyph` ist über den Anfang (Liste leeren, `GlyphData` anlegen) zugeordnet, `DeleteGlyph` über Aufrufer und Größe, beide nicht Zeile für Zeile.
- `CB_CLEAR_CLUMPLIST` (`0x006E6470`) war schon benannt (Aufruf der Methode `clear` auf der Clumpliste); die Anmeldung bei `AgcmMap` wurde nicht einzeln gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 6, nicht im Client: 3, ohne Kandidat: 2, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `IsGlyphedFrame` | 13 | `0x006E54C0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `UpdatePosStaticGlyph` | 8 | `0x006E3DC0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `AddRenderClumplist` | 15 | `0x006E6810` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmCamera2`](AgcmCamera2.md), [`AgcmMap`](AgcmMap.md), [`AgcmObject`](AgcmObject.md), [`AgcmRender`](AgcmRender.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgpmFactors`](AgpmFactors.md), [`AgpmItem`](AgpmItem.md), [`AgpmItemConvert`](AgpmItemConvert.md), [`ApmObject`](ApmObject.md)
- **Erwähnt in:** [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmTargeting`](AgcmTargeting.md)
