# AgcmUIEventGacha (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse `AgcmUIEventGacha` (Gacha-Fenster) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIEventGacha/AgcmUIEventGacha.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 14 Quellmethoden sind zugeordnet; neu sind `ShowErrorReport`, `CBReceiveResult`, `CBOpenGachaUI` und `OnRollEnd`. (`OnRollEnd` fehlte in der automatischen Methodenliste, weil ein Kommentar hinter der Signatur steht; die Liste wurde um den Eintrag ergänzt.)
- **Lua:** drei Befehle (`LoadGachaSetting`, `GachaTestRoll`, `GachaRollCount`) mit den Meldungstexten der Quelle.
- **Fehlercodes:** sechs, wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIEventGacha.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnLuaInitialize` | `0x006803E0` | 119 | vtable/String |
| 1 | `OnAddModule` | `0x00680920` | 128 | vtable/String |
| 2 | `AddEvent` | `0x00680760` | 441 | Zeichenkette |
| 3 | `ShowErrorReport` | `0x0067FD50` | 90 | ver |
| 4 | `CBOpenGachaUI` | `0x00680620` | 304 | ver |
| 5 | `CBReceiveResult` | `0x0067FDD0` | 46 | ver |
| 6 | `CBGachaClose` | `0x0067FE00` | 75 | UI-Registrierung |
| 7 | `CBGachaRoll` | `0x0067FE50` | 158 | UI-Registrierung |
| 8 | `UpdateControlNotice` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 9 | `UpdateControlItem` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 10 | `CBDisplayGachaMessage` | `0x0067FF20` | 445 | UI-Registrierung |
| 11 | `CBDisplayGachaItem` | `0x006800E0` | 66 | UI-Registrierung |
| 12 | `CBSelfCharacterUpdatePosition` | `0x006801E0` | 124 | Callback-Registrierung |
| 13 | `OnRollEnd` | `0x00680130` | 176 | ver |

12 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00680460` (`0x00680460`), `ctor_or_dtor_006804f0` (`0x006804F0`), `~AgcmUIEventGacha` (`0x00680600`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x28CC` | `Flag „Walze läuft“ (in `CBOpenGachaUI` abgefragt)` | `CBOpenGachaUI` |
| `0x2914…0x292C` | `Kopie der Gacha-Angaben (`m_stGachaInfo`)` | `CBOpenGachaUI` |
| `0x2944` | `Flag „Gacha-Fenster offen“` | `CBOpenGachaUI` |

## Umfang

`AgcmUIEventGacha.cpp` (14 Methoden, dieser Bericht) verwaltet das Gacha-Fenster; das Walzenfenster selbst ist die Klasse `AcUIGacha` (Datei `AcUIGacha.cpp`, eigener Bericht [AcUIGacha](AcUIGacha.md)).

## Vtable

Vtable bei `0x008CB35C`: Slot 0 Destruktor `0x00680600`, 1 `OnAddModule` (`0x00680920`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90`.

## Registrierung (OnAddModule, 0x00680920)

Holt [`ApmEventManager`](ApmEventManager.md), [`AgcmUIManager2`](AgcmUIManager2.md) und [`AgcmEventGacha`](AgcmEventGacha.md), legt über `AddEvent` (`0x00680760`) die Ereignisse `Gacha_OpenUI`, `Gacha_Error`, `Gacha_Roll`, `Gacha_CloseUI` an, meldet bei `AgcmEventGacha` die Callbacks `CBOpenGachaUI` und `CBReceiveResult` an und registriert das Fenster `GachaWindow` als eigenes Steuerelement. Außerdem meldet es bei `AgcmCharacter` `CBSelfCharacterUpdatePosition` an. Reihenfolge wie in der Quelle.

## Fenster öffnen und Ergebnis

`CBOpenGachaUI` (`0x00680620`) kopiert die Gacha-Angaben (sieben Werte) ins Modul, aktualisiert die Benutzerdaten für Hinweis und Gegenstand und unterscheidet das Ergebnis: bei den Codes 0–4 (kein Fehler, zu wenig Gegenstand, Geld, Charisma, Inventar) wird das Fenster geöffnet (`Gacha_OpenUI`, Walzen bekommen die Gegenstände über [`AcUIGacha`](AcUIGacha.md):SetSlotItems`); bei 5 und 6 wird nur eine Fehlermeldung gezeigt.
`ShowErrorReport` (`0x0067FD50`) zeigt zu den Fehlercodes 1–6 je einen Meldungstext (UI-Texte `0x2D9`–`0x2DD`, `0x2E3`) im OK-Dialog – das entspricht den sechs Fällen der Quelle. `CBReceiveResult` (`0x0067FDD0`) startet bei Erfolg die Walze (`AcUIGacha::StartRoll`), sonst `ShowErrorReport`.

## Lua-Befehle (OnLuaInitialize, 0x006803E0)

Registriert drei Lua-Funktionen, wie in der Quelle: `LoadGachaSetting` (`0x00680260`, liest die Rolltabelle, Standard `RollTable.txt`; Ausgabe „Gacha Rolling Table Load Succeeded/Failed“), `GachaTestRoll` (`0x00680330`, startet einen Testlauf mit zufälligem Treffer; „Gacha is not initialized“, wenn leer) und `GachaRollCount` (`0x006802D0`, ändert die Anzahl der Umdrehungen; „Gacha Roll Count Changed“).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00680760`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Ereignis** (4)

| Name | Id | Handler |
|---|---:|---|
| `Gacha_OpenUI` | 0 | – |
| `Gacha_Error` | 0 | – |
| `Gacha_Roll` | 0 | – |
| `Gacha_CloseUI` | 0 | – |

**Funktion** (2)

| Name | Id | Handler |
|---|---:|---|
| `Gacha_Roll` |  | `CBGachaRoll` |
| `Gacha_Close` |  | `CBGachaClose` |

**UserData** (2)

| Name | Id | Handler |
|---|---:|---|
| `Gacha_TextData` |  | – |
| `Gacha_ItemName` |  | – |

**Anzeige** (2)

| Name | Id | Handler |
|---|---:|---|
| `Gacha_Display_Notice` | 0 | `CBDisplayGachaMessage` |
| `Gacha_Display_Item` | 0 | `CBDisplayGachaItem` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (`ShowErrorReport`, `CBReceiveResult`, Lua-Namen).

## Grenzen

- `UpdateControlNotice` und `UpdateControlItem` (je 5 Zeilen) sind in `CBOpenGachaUI` eingebaut.
- `CBOpenGachaUI` wurde nur in den ersten Zeilen und der Verzweigung gelesen.
- `OnRollEnd` (`0x00680130`) löscht beim Self-Character das Bit `0x400` (Bewegung wieder frei), zeigt den Gewinn (UI-Text `0x2E0` mit dem Gegenstandsnamen) im OK-Dialog und setzt das Rollen-Flag zurück.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AcUIGacha`](AcUIGacha.md), [`AgcmEventGacha`](AgcmEventGacha.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`ApmEventManager`](ApmEventManager.md)
- **Erwähnt in:** [`AcUIGacha`](AcUIGacha.md), [`AgpmBattleGround`](AgpmBattleGround.md)
