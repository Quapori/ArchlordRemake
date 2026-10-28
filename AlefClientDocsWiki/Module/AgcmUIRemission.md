# AgcmUIRemission (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIRemission` (Vergebung (Ablass) für Mörderpunkte) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIRemission/AgcmUIRemission.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 26 von 28 Quellmethoden sind einer Adresse zugeordnet; neu sind `AddEvent`, `Open`, `OnTest`, `OnResult`, `SendRemit`, `SendRequestEvent`, `CBIsActiveIndulButton` sowie die UI-Funktionen und Anzeigen; `Close` und `GetMessageTxt` sind eingebaut.
- **Ablauf:** Testanfrage (Typ 1) beim Öffnen; Ablass (Typ 4) mit Bestätigung, 3000 ms Abklingzeit und Anfrage; Pakettyp `0x2A`, Operation 2.
- **Konstanten:** 2 Punkte pro Ablass, 10 Ablässe; Mörderstufen bei 0, 40 und 60 Punkten.
- **UI:** 3 Funktionen, 5 Anzeigen, 1 Bool-Anzeige, 2 Benutzerdaten, 3 Ereignisse – Anzahl wie in der Quelle.
- **Hinweis:** `GetMessageTxt` hat in der Quelle denselben Fehler wie [`AgcmUITax`](AgcmUITax.md) (`> MAX` statt `>=`).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIRemission.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006A02F0` | 443 | vtable/String |
| 1 | `AddEvent` | `0x0069F800` | 67 | manual |
| 2 | `AddFunction` | `0x006A01C0` | 125 | Zeichenkette |
| 3 | `AddDisplay` | `0x006A0240` | 161 | Zeichenkette |
| 4 | `AddUserData` | `0x0069F850` | 85 | Zeichenkette |
| 5 | `AddBoolean` | `0x0069FB90` | 31 | Zeichenkette |
| 6 | `Open` | `0x0069F8B0` | 82 | manual |
| 7 | `Close` | – | | in CBSelfUpdatePosition eingebaut (wirft REMIT_EVENT_CLOSE) |
| 8 | `OnTest` | `0x0069FBB0` | 65 | manual |
| 9 | `OnResult` | `0x0069FC00` | 186 | manual |
| 10 | `CBRequestEvent` | `0x0069FCC0` | 109 | Callback-Registrierung |
| 11 | `CBGrant` | `0x0069FD30` | 47 | Callback-Registrierung |
| 12 | `CBSelfUpdatePosition` | `0x0069F910` | 117 | Callback-Registrierung |
| 13 | `CBRemit` | `0x0069FD60` | 83 | Callback-Registrierung |
| 14 | `CBKeydownESC` | `0x00698820` | 10 | gleiche Adresse wie `gemeinsamer Rumpf (return param != 0)` (vom Linker zusammengefaltet) |
| 15 | `CBOpenWindow` | `0x0069F990` | 52 | uireg |
| 16 | `CBCloseWindow` | `0x0078B6A0` | 10 | gleiche Adresse wie `gemeinsamer Rumpf (return param != 0)` (vom Linker zusammengefaltet) |
| 17 | `CBClickButtonIndul` | `0x0069FDC0` | 263 | uireg |
| 18 | `CBAfterCooldown` | `0x0069FED0` | 50 | Callback-Registrierung |
| 19 | `CBDisplayDescription` | `0x0069FF10` | 119 | uireg |
| 20 | `CBDisplayCurrentPoint` | `0x0069FF90` | 101 | uireg |
| 21 | `CBDisplayRemitablePoint` | `0x006A0000` | 61 | uireg |
| 22 | `CBDisplayIndulCount` | `0x006A0040` | 122 | uireg |
| 23 | `CBDisplayNeedIndulCount` | `0x006A00C0` | 247 | uireg |
| 24 | `CBIsActiveIndulButton` | `0x0069F9D0` | 44 | manual |
| 25 | `SendRemit` | `0x0069FA00` | 210 | manual |
| 26 | `SendRequestEvent` | `0x0069FAE0` | 118 | manual |
| 27 | `GetMessageTxt` | – | | in die Aufrufer eingebaut (Index als Konstante) |

26 von 28 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIRemission` (`0x0069F760`), `~AgcmUIRemission` (`0x0069FB60`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB94…0xBB0` | `Modulzeiger (`AgcmCharacter` +0xBA0, [`AgcmUICooldown`](AgcmUICooldown.md) +0xBB0)` | `OnAddModule` |
| `0xBBC…0xBC4` | `Öffnungsposition (`m_stOpenPos`)` | `Open` |
| `0xBC8…` | `Ereignis-IDs (Öffnen +0xBC8, Schließen +0xBCC, Erfolg +0xBD0)` | `AddEvent`, `CBSelfUpdatePosition` |
| `0xBD4 / 0xBD8` | `Benutzerdaten Dummy / Ablass-Schalter` | `CBOpenWindow`, `OnResult` |
| `0xBB8 (3000)` | `gemerkter Typ der Vergebung (`m_cType`)` | `CBClickButtonIndul`, `CBAfterCooldown` |
| `0xBE0 / 0xBE4` | `Abklingzeit-ID / Mörderstufe vor dem Ablass` | `CBClickButtonIndul`, `OnResult` |

## Vtable

Vtable bei `0x008CF23C`: Slot 0 Destruktor `0x0069FB60`, 1 `OnAddModule` (`0x006A02F0`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`, `OnDestroy`), 3–5 gemeinsamer Rumpf `0x0067FAB0`.

## Registrierung (OnAddModule, 0x006A02F0)

Holt acht Module ([`AgpmRemission`](AgpmRemission.md), [`AgpmCharacter`](AgpmCharacter.md), `AgcmCharacter`, [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), `AgcmUICooldown`, [`AgcmEventManager`](AgcmEventManager.md)); `AgcmUICooldown` ist optional. Danach:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmRemission`: Vergebung (Ergebnis) | `CBRemit` | `0x0069FD60` |
| `AgcmEventManager`: Ereignisfunktion 0x1F | `CBRequestEvent` | `0x0069FCC0` |
| `AgpmRemission`: Ereignis gewährt | `CBGrant` | `0x0069FD30` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x0069F910` |
| `AgcmUIMain`: ESC | `CBKeydownESC` | `0x00698820` (gemeinsamer Rumpf) |
| `AgcmUICooldown`: Abklingzeit beendet | `CBAfterCooldown` | `0x0069FED0` |

Danach `AddEvent` (`0x0069F800`), `AddFunction` (`0x006A01C0`), `AddDisplay` (`0x006A0240`), `AddUserData` (`0x0069F850`) und `AddBoolean` (`0x0069FB90`, Bool-Anzeige `REMIT_ACTIVE_INDUL_BTN`, Handler `CBIsActiveIndulButton` `0x0069F9D0`).

## Ablauf

`CBGrant` (`0x0069FD30`) sendet zunächst eine **Testanfrage** (Typ 1, `AGPMREMISSION_TYPE_TEST`) mit `SendRemit` (`0x0069FA00`). Die Antwort läuft über `CBRemit`: Typ 1 → `OnTest` (`0x0069FBB0`), Typ 4 (Ablass) → `OnResult` (`0x0069FC00`).
`OnTest` öffnet bei Ergebnis „vergebbar“ (2) das Fenster (`Open`, `0x0069F8B0`: merkt die Position und wirft `REMIT_EVENT_OPEN`), sonst erscheint ein OK-Dialog `REMIT_MSG_NOT_TP`.
`CBClickButtonIndul` (`0x0069FDC0`) fragt mit `REMIT_MSG_CNF_IND` nach: Bei Dienstgebiet „Global“ (Wert 4 in der Variablen `g_eServiceArea`, im Binary mit 4 vorbelegt) lauten die Zahlen **2 Punkte** und **10 Ablässe**, sonst in umgekehrter Reihenfolge (`AGPMREMISSION_REMIT_POINT_PER_TIME` 2, `AGPMREMISSION_PAY_INDULGENCE_QTY` 10). Bei „OK“ wird der Typ 4 gemerkt, die Mörderstufe gespeichert (`+0xBE4`) und eine Abklingzeit von **3000 ms** gestartet; danach sendet `CBAfterCooldown` (`0x0069FED0`) die Anfrage für Typ 1…4.
`OnResult` (bei Erfolg, Ergebnis 1) wirft `REMIT_EVENT_SUCCESS`, vergleicht die alte mit der neuen Mörderstufe und zeigt bei einer Senkung die Meldung `FreeMurdererLv1/2/3` (Stufen mit 0, 40 und 60 Mörderpunkten); danach werden beide Benutzerdaten aktualisiert.

## Pakete (Typ 0x2A)

`SendRemit` (`0x0069FA00`) baut ein eingebettetes Paket mit dem Typ und ein Hauptpaket `AGPMREMISSION_PACKET_TYPE` (`0x2A`) mit Operation 2 (`REMIT`) und der Charakter-ID. `SendRequestEvent` (`0x0069FAE0`) nutzt `AgpmRemission::MakePacketEventRequest` (`0x0056C1C0`). `CBRequestEvent` wirkt nur für den eigenen Charakter und lehnt bei Aktionssperre ab.

## Anzeigen

Fünf Anzeigen: Beschreibung (Text `REMIT_MSG_DESC` im Eingabefeld), aktuelle Punkte (`GetMurdererPoint`), vergebbare Punkte (2), Zahl der Ablassgegenstände (Gegenstandsprüfung `IsValidItem` mit Typ „Sonstiges/Vergebung“ und Menge 10) und der Hinweis „benötigte Ablässe“ (die Zahl 10 in Gelb eingebettet, `<C16776960>10<C16777215>`). Drei Benutzerdaten-Funktionen: `CBOpenWindow` (`0x0069F990`) aktualisiert beide Benutzerdaten; `CBCloseWindow` ist in der Quelle leer und im Binary ein gemeinsamer Rumpf (`0x0078B6A0`).

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x006A01C0`, `0x006A0240`, `0x0069F850`, `0x0069F800`, `0x0069FB90`, `0x006A02F0`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (3)

| Name | Id | Handler |
|---|---:|---|
| `REMIT_OPEN` |  | `FUN_0069f990` |
| `REMIT_CLOSE` |  | [`AgcmShrine`](AgcmShrine.md):CBShrineTapScroe` |
| `REMIT_INDUL_BTN_CLICK` |  | `FUN_0069fdc0` |

**Anzeige** (5)

| Name | Id | Handler |
|---|---:|---|
| `REMIT_DESC` | 0 | `FUN_0069ff10` |
| `REMIT_CURR_POINT` | 0 | `FUN_0069ff90` |
| `REMIT_ABLE_POINT` | 0 | `FUN_006a0000` |
| `REMIT_INDUL_COUNT` | 0 | `FUN_006a0040` |
| `REMIT_NEED_INDUL` | 0 | `FUN_006a00c0` |

**UserData** (2)

| Name | Id | Handler |
|---|---:|---|
| `REMIT_UD_DUMMY` | 0 | – |
| `REMIT_UD_INDUL_ENABLE` |  | – |

**Boolean** (1)

| Name | Id | Handler |
|---|---:|---|
| `REMIT_ACTIVE_INDUL_BTN` |  | `FUN_0069f9d0` |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierung, `CBGrant`, `CBRemit`, `OnTest`, `OnResult`, `CBClickButtonIndul`, `CBAfterCooldown`, `CBSelfUpdatePosition`).

## Grenzen

- Die Offsets `+0xBB8` (Typ) und `+0xBE0` (Abklingzeit-ID) stammen aus `CBClickButtonIndul` und `CBAfterCooldown`; der Typ liegt bei Dezimal 3000 = `0xBB8`.
- Die Anzeigefunktionen (`CBDisplay…`) wurden nur über die Registrierungsreihenfolge zugeordnet, nicht einzeln gelesen.
- Welchen Wert `g_eServiceArea` im Betrieb hat, wurde nicht gemessen; das Binary belegt nur den statischen Anfangswert 4.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht als eigene Funktion: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgcmShrine`](AgcmShrine.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUICooldown`](AgcmUICooldown.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUITax`](AgcmUITax.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmRemission`](AgpmRemission.md)
