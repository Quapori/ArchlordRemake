# AgcmUITips (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUITips` (Spiel- und Ladetipps, Warnungen nach Spielzeit) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUITips/AgcmUITips.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 14 von 14 Quellmethoden sind einer Adresse zugeordnet (`OnInit` als gemeinsamer Rumpf); neu sind `GetRandomTipImage`, `DestroyTipImages`, `DestroyTipTexts`, `SetTexturePath`, `EnableTipText` und die Vergleichsfunktion `TipTextCompare`.
- **Zeiten:** Tipp alle 120 s für 10 s; Warnung je volle Stunde Spielzeit; Ladebild-Wechsel alle 60 s ([`AgcTipWindow`](AgcTipWindow.md)).
- **UI:** 2 Funktionen, 1 Anzeige, 2 Benutzerdaten, 3 Steuerelemente, 2 Ereignisse – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUITips.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 1 | `OnAddModule` | `0x0061DED0` | 411 | vtable/String |
| 2 | `OnIdle` | `0x0061D7F0` | 491 | vtable/String |
| 3 | `OnDestroy` | `0x0061E070` | 22 | vtable/String |
| 4 | `ReadTipImages` | `0x0061E090` | 530 | Zeichenkette |
| 5 | `ReadTipTexts` | `0x0061E2B0` | 768 | Zeichenkette |
| 6 | `DestroyTipImages` | `0x0061DA00` | 109 | manual |
| 7 | `DestroyTipTexts` | `0x0061DA80` | 153 | manual |
| 8 | `GetRandomTipImage` | `0x0061DB20` | 315 | manual |
| 9 | `SetTexturePath` | `0x0061DC70` | 31 | manual |
| 10 | `EnableTipText` | `0x0061DC90` | 76 | manual |
| 11 | `CBNextTip` | `0x0061DCE0` | 98 | UI-Registrierung |
| 12 | `CBPrevTip` | `0x0061DD50` | 95 | UI-Registrierung |
| 13 | `CBDisplayTip` | `0x0061DDB0` | 243 | UI-Registrierung |

14 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0061d630` (`0x0061D630`), `ctor_or_dtor_0061d760` (`0x0061D760`), `TipTextCompare` (`0x0061D9E0`), `~AgcmUITips` (`0x0061DEB0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB9C` | `Zeiger auf [`AgcmLogin`](AgcmLogin.md)` | `OnIdle` |
| `0xBA8 / 0xBAC` | `Tipps erlaubt (`m_bEnableTipText`) / gewählter Tipp (`m_lTipText`)` | `OnIdle`, `CBDisplayTip` |
| `0xBB0 / 0xBB4` | `Benutzerdaten `Tip_Text` / `Loading_Warning`` | `OnAddModule`, `GetRandomTipImage` |
| `0xBB8 / 0x28C8 / 0x45D8` | `Tipp-Fenster 1024 / 1280 / 1600 (je 0x1D10 Byte)` | `OnAddModule` |
| `0x62E8` | `Texturpfad (`m_szTexturePath`)` | `SetTexturePath` |
| `0x6368 / 0x636C` | `Zahl und Liste der Tipp-Bilder` | `DestroyTipImages`, `GetRandomTipImage` |
| `0x6370 / 0x6374 / 0x6378` | `Zahl normaler / Belagerungs- / Warn-Tipps` | `OnIdle`, `DestroyTipTexts` |
| `0x637C` | `Liste der Tipp-Texte (Element 0xC Byte: Typ, Stunden, Text)` | `OnIdle`, `DestroyTipTexts` |
| `0x6380…0x638C` | `Text sichtbar / letzte Warnstunde / Spielstartzeit / Öffnungszeit` | `OnIdle` |
| `0x6390 / 0x6394` | `Ereignis-ID Öffnen / Schließen` | `OnIdle`, `EnableTipText` |
| `0x6398 / 0x639C` | `Nummer der Lade-Warnung / Zeiger auf ihren Text` | `GetRandomTipImage` |

## Vtable

Vtable bei `0x008C15D4`: Slot 0 Destruktor `0x0061DEB0`, 1 `OnAddModule` (`0x0061DED0`), 2/6 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`), 3 `OnIdle` (`0x0061D7F0`), 7 `OnDestroy` (`0x0061E070`). Der Konstruktor (`0x0061D630`) legt die drei Tipp-Fenster ein und aktiviert `OnIdle` (`EnableIdle(TRUE)`).

## Registrierung (OnAddModule, 0x0061DED0)

Holt [`AgcmUIManager2`](AgcmUIManager2.md), `AgcmLogin` und [`AgcmResourceLoader`](AgcmResourceLoader.md) und legt an:

| Art | Name | Handler / Ziel |
|---|---|---|
| Benutzerdatum | `Tip_Text` (Zahl, `+0xBAC`) | – |
| Benutzerdatum | `Loading_Warning` (Zeichenkette, 64 Byte, `+0x639C`) | – |
| Funktion | `Tip_Next` | `CBNextTip` `0x0061DCE0` |
| Funktion | `Tip_Prev` | `CBPrevTip` `0x0061DD50` |
| Steuerelement | `Tip1024`, `Tip1280`, `Tip1600` (je ein `AgcTipWindow`, `+0xBB8`, `+0x28C8`, `+0x45D8`) | – |
| Anzeige | `Tip_Text` | `CBDisplayTip` `0x0061DDB0` |
| Ereignis | `Tip_OpenText`, `Tip_CloseText` | – |

## Ablauf (OnIdle, 0x0061D7F0)

Zwei Zeitgeber, beide wie in der Quelle:
- **Tipp-Text:** Nur im Spiel (Anmeldemodus 9, `AGCMLOGIN_MODE_POST_LOGIN` der Quelle) und wenn Texte vorhanden sind, wird beim ersten Aufruf die Spielstartzeit gemerkt. Alle **120 000 ms** (`AGCM_TIP_TEXT_DELAY`) wählt das Modul einen zufälligen Tipp (`randInt(Anzahl − 1)`), aktualisiert das Benutzerdatum und wirft `Tip_OpenText`; nach **10 000 ms** (`AGCM_TIP_TEXT_TIME`) wirft es `Tip_CloseText`.
- **Warntext:** Je volle Stunde (**3 600 000 ms**, `AGCM_TIP_TEXT_WARN_DELAY`) seit dem Spielstart wird aus den Warntexten (Einträge hinter den normalen Tipps und den Belagerungs-Tipps) der letzte gewählt, dessen Stundenwert erreicht ist; er wird sofort eingeblendet.

## Tipp-Dateien (ReadTipImages, ReadTipTexts)

`ReadTipImages` (`0x0061E090`) liest eine Tabelle mit der Spalte `Texture` (Zeilenzahl − 1 Bilder). `ReadTipTexts` (`0x0061E2B0`) liest die Spalten `Text`, `Hour` und `Type`: Ein von 0 verschiedener Stundenwert macht den Eintrag zum Warntext; je Typ werden Belagerungs-, Warn- und normale Tipps gezählt; danach sortiert `qsort` die Einträge (`TipTextCompare`, `0x0061D9E0`: bei gleichem Typ nach Stunden, sonst 0). Die Quelle ruft die Funktionen mit Dateinamen aus dem Anmelde-/Ladevorgang auf; die Aufrufer liegen außerhalb dieses Moduls.

## Ladebild-Tipp (GetRandomTipImage, 0x0061DB20)

Wählt das nächste Lade-Warnungs-Label `WARN_MESSAGE_%d` (beginnt bei 1, springt nach dem letzten wieder auf 1), setzt es als Benutzerdatum `Loading_Warning` und wählt dann aus der Bildliste bis zu **zehn** Mal zufällig ein Bild, das sich laden lässt (`AgcmResourceLoader::LoadTexture`); die Textur bekommt Clamp-Adressierung (Byte `+0x51` = `0x33`). Der Texturpfad kommt aus `SetTexturePath` (`0x0061DC70`, Kopie nach `+0x62E8`).

## Bedienung

`CBNextTip`/`CBPrevTip` blättern durch die normalen Tipps (mit Umlauf) und setzen die Öffnungszeit zurück, sodass `OnIdle` den Tipp nicht sofort schließt; beide tun nichts, solange ein Warntext angezeigt wird. `EnableTipText` (`0x0061DC90`) schaltet die Tipps ein und aus und wirft dabei `Tip_CloseText` bzw. `Tip_OpenText`. `CBDisplayTip` zeigt den gewählten Text (Warntexte mit der Stundenzahl als Formatwert); in der Quelle liefert sie für den Index 0 `FALSE` (`<= 0`), sodass der erste Tipp nie angezeigt wird.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x0061DED0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**UserData** (2)

| Name | Id | Handler |
|---|---:|---|
| `Tip_Text` |  | – |
| `Loading_Warning` |  | – |

**Funktion** (2)

| Name | Id | Handler |
|---|---:|---|
| `Tip_Next` |  | – |
| `Tip_Prev` |  | – |

**Anzeige** (1)

| Name | Id | Handler |
|---|---:|---|
| `Tip_Text` | 0 | – |

**Ereignis** (2)

| Name | Id | Handler |
|---|---:|---|
| `Tip_OpenText` | 0 | – |
| `Tip_CloseText` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Zeitkonstanten in `OnIdle`, `GetRandomTipImage`, `EnableTipText`, `TipTextCompare`, Registrierung).

## Grenzen

- `CBNextTip`, `CBPrevTip`, `CBDisplayTip`, `ReadTipImages` und `ReadTipTexts` wurden über Registrierung und Größe zugeordnet; ihre Verzweigungen wurden nicht Zeile für Zeile verglichen.
- Die Tipp-Dateien selbst (Tabellen mit `Text`, `Hour`, `Type`, `Texture`) liegen verschlüsselt im Client-Verzeichnis und wurden nicht ausgewertet.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcTipWindow`](AgcTipWindow.md), [`AgcmLogin`](AgcmLogin.md), [`AgcmResourceLoader`](AgcmResourceLoader.md), [`AgcmUIManager2`](AgcmUIManager2.md)
- **Erwähnt in:** [`AgcTipWindow`](AgcTipWindow.md)
