# AgcmSocialActon (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AgcmSocialActon` (Datenklasse der sozialen Aktionen: Liste, Gitter, Tooltip) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmUISocialAction/AgcmSocialAction.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 6 von 6 Quellmethoden sind zugeordnet; dazu Konstruktor, Destruktor und `SocialAction`-Konstruktor.
- **Daten:** höchstens 17 Einträge (`reserve(17)`), Gitter 1 × 5 × 4 (20 Plätze), Spalte 1 = Symbol, 2 = Befehl und Tooltip-Titel, 3 = Tooltip-Text.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmSocialActon.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Create` | `0x0076A3E0` | 310 | Zeichenkette |
| 1 | `Destory` | `0x0076AAB0` | 116 | manual |
| 2 | `Load` | `0x0076A880` | 379 | manual |
| 3 | `SetModule` | `0x0076A3A0` | 30 | manual |
| 4 | `OpenTooltip` | `0x0076A520` | 161 | manual |
| 5 | `CloseTooltip` | `0x0076A3C0` | 23 | manual |

6 von 6 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmSocialActon` (`0x0076A7F0`), `~AgcmSocialActon` (`0x0076AA00`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x34 / 0x38 / 0x3C` | `Vektor `m_vecInfo` (Anfang / Ende / Kapazität)` | `Load`, `Destory` |
| `0x10` | `Gitter `m_cGrid`` | `Create`, `Destory` |
| `0x40 / 0xC0 / 0xC4` | `Tooltip-Fenster `m_cTooltip` / Flag „immer oben“ / Sichtbarkeit` | `Create`, `OpenTooltip`, `CloseTooltip` |
| `0x0 / 0x4 / 0x8 / 0xC` | `Zeiger [`AgpmGrid`](AgpmGrid.md) / [`AgcmResourceLoader`](AgcmResourceLoader.md) / [`AgcmUIControl`](AgcmUIControl.md) / [`AgcmUIManager2`](AgcmUIManager2.md)` | `SetModule` |

## Umfang

`AgcmSocialAction.cpp` enthält die Klasse `AgcmSocialActon` (Schreibweise der Quelle) mit Liste, Gitter und Tooltip der sozialen Aktionen sowie die Hilfsklasse `SocialAction` (ein Eintrag). Die UI-Seite ist [AgcmUISocialAction](AgcmUISocialAction.md).

## Funktionen

| Funktion | Adresse | Befund |
|---|---|---|
| `SocialAction::SocialAction` | `0x0076A320` | kopiert Symbol-, Befehls-, Tooltip-Titel und -Text in vier Puffer (`+0x0`, `+0x80`, `+0x100`, `+0x120`); `pGridItem` (`+0x320`) und `pTexture` (`+0x324`) = 0; Größe des Eintrags `0x328` Byte (Aufrufer: `Load`) |
| `AgcmSocialActon::AgcmSocialActon` | `0x0076A7F0` | Vektor `m_vecInfo` leer, `reserve(0x11)` = 17 (`SOCIALACTION_MAX`); die auskommentierten Einträge der Quelle sind nicht enthalten; initialisiert den Tooltip (`AcUIToolTip`) |
| `AgcmSocialActon::~AgcmSocialActon` | `0x0076AA00` | löscht jeden Eintrag, leert den Vektor, zerstört den Tooltip |
| `SetModule` | `0x0076A3A0` | speichert vier Zeiger (`AgpmGrid`, `AgcmResourceLoader`, `AgcmUIControl`, `AgcmUIManager2`) |
| `Load` | `0x0076A880` | öffnet die Tabelle (`AuExcelTxtLib::OpenExcelFile`), liest ab Zeile 1 je Zeile Symbol (Spalte 1), Befehl (Spalte 2), Tooltip-Titel (Spalte 2 + 1 Zeichen) und Tooltip-Text (Spalte 3), legt je einen `SocialAction` an und ruft am Ende `Create` |
| `Create` | `0x0076A3E0` | setzt den Texturpfad `Texture\UI\BASE\`, initialisiert das Gitter mit 1 × 5 × 4, legt je Eintrag ein Gitterfeld mit Textur an (Filtermodus 1 = `rwFILTERNEAREST`, Adressierung `0x33` = Clamp in beide Richtungen; die Textur wird per `RwTextureRead` geladen), Typ `AGPDGRID_ITEM_TYPE_SOCIALACTION` (0x40), verschiebbar, ID = Index, Zeile = Index / 4, Spalte = Index % 4; zuletzt der Tooltip (`+0xC0` = immer oben, an `AddWindow` übergeben, dann ausgeblendet); Gittertyp 10 (`+0x2C`) |
| `OpenTooltip` | `0x0076A520` | Index < 17 und Eintrag vorhanden; Tooltip 30 Pixel rechts und unter dem Mauszeiger, Titel Schrift 14, Text Schrift 12, beide weiß `0xFFFFFFFF` (`0xE`/`0xC` und `-1` im Aufruf); macht das Fenster sichtbar (Flag `+0xC4`, `ShowWindow` eingebaut) |
| `CloseTooltip` | `0x0076A3C0` | löscht die Tooltip-Texte und blendet das Fenster aus (`+0xC4` = 0) |
| `Destory` | `0x0076AAB0` | löscht Gitterfelder und Einträge, `Clear` und `Remove` des Gitters (1 × 5 × 4) |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Offsets der Zeiger in `SetModule` (`+0x0`…`+0xC`) sind relativ zum Teilobjekt `AgcmSocialActon` angegeben; im Modul [`AgcmUISocialAction`](AgcmUISocialAction.md) kommen `0xB98` dazu (Mehrfachvererbung).
- Die Gitter-Schriftgrößen und Farben wurden gegen die Konstanten im Dekompilat gelesen, die Texturfilter-Aufrufe von `Create` nur über die Aufrufliste (`RwTextureSetFilterMode`/`…Addressing`).

## Querverweise

- **Erwähnt Module:** [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUISocialAction`](AgcmUISocialAction.md), [`AgpmGrid`](AgpmGrid.md)
- **Erwähnt in:** [`AgcmUISocialAction`](AgcmUISocialAction.md)
