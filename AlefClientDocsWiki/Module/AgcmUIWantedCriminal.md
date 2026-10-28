# AgcmUIWantedCriminal (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIWantedCriminal` (Steckbriefe: Kopfgeld aussetzen und Rangliste der gesuchten Verbrecher) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIWantedCriminal/AgcmUIWantedCriminal.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 57 von 60 Quellmethoden sind einer Adresse zugeordnet (die zwei `Test…` gibt es nur im Debug-Build, `GetMessageTxt` ist eingebaut); neu sind `AddEvent`, `OpenBoard`, `OpenArrange`, `OnClickPage`, `ResetBoard`, `SendRequestEvent`, `SendArrange`, `SendRequstList`, `SendRequestMyRank` sowie 30 UI-Funktionen und Anzeigen (über die Registrierungsreihenfolge).
- **Pakete:** Typ `0x46`, Operationen 0, 2 (Aufgeben), 3 (Liste), 5 (eigener Rang).
- **Idle:** alle 30 s Rang-Anfrage, nur für gesuchte Charaktere; `EnableIdle(TRUE)` im Konstruktor.
- **UI:** 19 Funktionen, 11 Anzeigen, 1 Bool-Anzeige, 3 Benutzerdaten, 17 Ereignisse – Anzahl wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIWantedCriminal.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0069A780` | 599 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf (die Testfunktionen gibt es nur im Debug-Build)` (vom Linker zusammengefaltet) |
| 2 | `OnIdle` | `0x00698BC0` | 65 | vtable/String |
| 3 | `AddEvent` | `0x006982C0` | 67 | manual |
| 4 | `AddFunction` | `0x0069A460` | 789 | Zeichenkette |
| 5 | `AddDisplay` | `0x0069A120` | 361 | Zeichenkette |
| 6 | `AddUserData` | `0x00698310` | 126 | Zeichenkette |
| 7 | `OpenBoard` | `0x0069A290` | 222 | manual |
| 8 | `OpenArrange` | `0x00698390` | 105 | manual |
| 9 | `OnClickPage` | `0x00698C10` | 129 | manual |
| 10 | `TestOpenBoard` | – | | nur im Debug-Build (`_DEBUG`) |
| 11 | `TestOpenArrange` | – | | nur im Debug-Build (`_DEBUG`) |
| 12 | `SendRequestEvent` | `0x00698400` | 124 | manual |
| 13 | `SendArrange` | `0x00698480` | 241 | manual |
| 14 | `SendRequstList` | `0x00698580` | 151 | manual |
| 15 | `SendRequestMyRank` | `0x00698620` | 148 | manual |
| 16 | `CBResultArrange` | `0x00698CA0` | 431 | Callback-Registrierung |
| 17 | `CBResultList` | `0x00698E60` | 301 | Callback-Registrierung |
| 18 | `CBResultMyRank` | `0x00698F90` | 249 | Callback-Registrierung |
| 19 | `CBUpdateKiller` | `0x006986C0` | 69 | Callback-Registrierung |
| 20 | `CBUpdateFlag` | `0x00698710` | 258 | Callback-Registrierung |
| 21 | `CBNotify` | `0x00699090` | 247 | Callback-Registrierung |
| 22 | `CBReleaseCharacter` | `0x00698820` | 10 | gleiche Adresse wie `gemeinsamer Rumpf (return param != 0)` (vom Linker zusammengefaltet) |
| 23 | `CBRequestEvent` | `0x00698830` | 109 | Callback-Registrierung |
| 24 | `CBGrant` | `0x0069A370` | 41 | Callback-Registrierung |
| 25 | `CBSelfUpdatePosition` | `0x0069A3A0` | 124 | Callback-Registrierung |
| 26 | `CBKeydownESC` | `0x0069A420` | 22 | Callback-Registrierung |
| 27 | `CBClickArrangeOnMenu` | `0x006988A0` | 16 | uireg |
| 28 | `CBClickArrange1OK` | `0x00699190` | 238 | uireg |
| 29 | `CBClickArrange2OK` | `0x00699280` | 407 | uireg |
| 30 | `CBClickArrange3OK` | `0x006988B0` | 194 | uireg |
| 31 | `CBClickArrangeCancel` | `0x00699420` | 72 | uireg |
| 32 | `CBClickBoardLeft` | `0x00699470` | 139 | uireg |
| 33 | `CBClickBoardRight` | `0x00699500` | 142 | uireg |
| 34 | `CBClickBoardPage01` | `0x00699590` | 118 | uireg |
| 35 | `CBClickBoardPage02` | `0x00699610` | 121 | uireg |
| 36 | `CBClickBoardPage03` | `0x00699690` | 121 | uireg |
| 37 | `CBClickBoardPage04` | `0x00699710` | 121 | uireg |
| 38 | `CBClickBoardPage05` | `0x00699790` | 121 | uireg |
| 39 | `CBClickBoardPage06` | `0x00699810` | 121 | uireg |
| 40 | `CBClickBoardPage07` | `0x00699890` | 121 | uireg |
| 41 | `CBClickBoardPage08` | `0x00699910` | 121 | uireg |
| 42 | `CBClickBoardPage09` | `0x00699990` | 121 | uireg |
| 43 | `CBClickBoardPage10` | `0x00699A10` | 121 | uireg |
| 44 | `CBClickBoardRefresh` | `0x00699A90` | 26 | uireg |
| 45 | `CBClickBoardClose` | `0x0069A440` | 22 | uireg |
| 46 | `CBDisplayArrangeDesc` | `0x00699AB0` | 192 | uireg |
| 47 | `CBDisplayArrangeDesc2` | `0x00699B70` | 192 | uireg |
| 48 | `CBDisplayArrangeDesc3` | `0x00699C30` | 192 | uireg |
| 49 | `CBDisplayArrangeCharID` | `0x00698980` | 63 | uireg |
| 50 | `CBDisplayArrangeTotalGheld` | `0x006989D0` | 76 | uireg |
| 51 | `CBDisplayArrangeBounty` | `0x00698A20` | 121 | uireg |
| 52 | `CBDisplayBoardRank` | `0x00698AA0` | 81 | uireg |
| 53 | `CBDisplayBoardWanted` | `0x00699CF0` | 85 | uireg |
| 54 | `CBDisplayBoardBounty` | `0x00699D50` | 92 | uireg |
| 55 | `CBDisplayBoardLevel` | `0x00699DB0` | 88 | uireg |
| 56 | `CBDisplayBoardClass` | `0x00699E10` | 205 | uireg |
| 57 | `CBIsActiveArrange` | `0x00698B00` | 67 | Callback-Registrierung |
| 58 | `GetMessageTxt` | – | | acht Zeilen, in die Aufrufer eingebaut |
| 59 | `ResetBoard` | `0x00699F10` | 98 | manual |

57 von 60 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x00698B60`), `AgcmUIWantedCriminal` (`0x00699F80`), `~AgcmUIWantedCriminal` (`0x0069A100`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB84…0xBA0` | `Modulzeiger (u. a. `AgcmCharacter` +0xB90, [`AgpmWantedCriminal`](AgpmWantedCriminal.md) +0xB8C)` | `OnAddModule` |
| `0xBA4…` | `Ereignis-IDs `m_lEvent[17]` (Seiten-Ereignisse ab `+0xBC0`)` | `AddEvent`, `CBResultList` |
| `0xBEC` | `Benutzerdatum `WC_UD_BOARD` (Anzahl bei `+0x4C`)` | `CBResultList`, `OpenBoard` |
| `0xC28…0xC30` | `Öffnungsposition (`m_stOpenPos`)` | `OpenBoard` |
| `0xC38…` | `zehn Einträge `m_WantedCriminals` zu je 0x58 Byte (mit Mutex)` | `CBResultList`, `ResetBoard` |
| `0xFA8 / 0xFAC` | `aktuelle Seite (−1 = keine) / Zähler der gelesenen Einträge` | `OnClickPage`, `CBResultList` |
| `0xFC0` | `Zeit der letzten Rang-Anfrage` | `OnIdle` |

## Vtable

Vtable bei `0x008CE554`: Slot 0 Destruktor `0x0069A100`, 1 `OnAddModule` (`0x0069A780`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`, `OnDestroy`), 3 `OnIdle` (`0x00698BC0`), 4/5 gemeinsamer Rumpf `0x0067FAB0`.

## Registrierung (OnAddModule, 0x0069A780)

Holt acht Module ([`AgpmGrid`](AgpmGrid.md), [`AgpmCharacter`](AgpmCharacter.md), `AgpmWantedCriminal`, `AgcmCharacter`, [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmEventManager`](AgcmEventManager.md)); Pflicht sind sieben davon (`AgpmGrid` ist optional). Danach in dieser Reihenfolge:

| Anmeldung | Handler | Adresse |
|---|---|---|
| `AgpmWantedCriminal`: Steckbrief-Ergebnis | `CBResultArrange` | `0x00698CA0` |
| `AgpmWantedCriminal`: Listenantwort | `CBResultList` | `0x00698E60` |
| `AgpmWantedCriminal`: eigener Rang | `CBResultMyRank` | `0x00698F90` |
| `AgpmWantedCriminal`: letzter Angreifer | `CBUpdateKiller` | `0x006986C0` |
| `AgpmWantedCriminal`: Flag „gesucht“ | `CBUpdateFlag` | `0x00698710` |
| `AgpmWantedCriminal`: Benachrichtigung | `CBNotify` | `0x00699090` |
| `AgcmCharacter`: eigener Charakter freigegeben | `CBReleaseCharacter` | `0x00698820` (gemeinsamer Rumpf) |
| `AgcmEventManager`: Ereignisfunktion 0x20 | `CBRequestEvent` | `0x00698830` |
| `AgpmWantedCriminal`: Ereignis gewährt | `CBGrant` | `0x0069A370` |
| `AgcmCharacter`: eigene Position geändert | `CBSelfUpdatePosition` | `0x0069A3A0` |
| `AgcmUIMain`: ESC | `CBKeydownESC` | `0x0069A420` |

Danach `AddEvent` (`0x006982C0`), `AddFunction` (`0x0069A460`), `AddDisplay` (`0x0069A120`), `AddUserData` (`0x00698310`) und die Bool-Anzeige `WC_ACTIVE_ARRANGE` (`CBIsActiveArrange`, `0x00698B00`). Zuletzt legt das Modul ein Gitterfeld für das Alarm-Symbol an, wenn `AgpmGrid` vorhanden ist.

## Steckbrief aufgeben (drei Schritte)

Das Aufgeben läuft über drei Fenster, die über `WC_OPEN_ARRANGE1`…`3` geöffnet werden:

| Schritt | Funktion | Adresse | Ablauf |
|---|---|---|---|
| Menü | `CBClickArrangeOnMenu` | `0x006988A0` | ruft `OpenArrange` (`0x00698390`): braucht einen letzten Angreifer (`AgpmWantedCriminal::GetFinalAttacker`, `0x0056B910`), wirft Ereignis 1 und aktualisiert das Dummy-Datum |
| 1 | `CBClickArrange1OK` | `0x00699190` | prüft das Mindest-Kopfgeld (`IsEnoughBaseBounty`); sonst Systemmeldung `WC_NOT_ENOUGH_BASE`; merkt das Basis-Kopfgeld und öffnet Fenster 2 |
| 2 | `CBClickArrange2OK` | `0x00699280` | liest den Betrag aus dem Eingabefeld, prüft Mindestbetrag (`WC_UNDERBASE`) und Guthaben (`WC_NOT_ENOUGH_MONEY`), öffnet Fenster 3 |
| 3 | `CBClickArrange3OK` | `0x006988B0` | prüft nochmals alles und sendet `SendArrange` |
| Abbruch | `CBClickArrangeCancel` | `0x00699420` | Systemmeldung `WC_CANCELED`, Kopfgeld auf 0 |

`CBResultArrange` (`0x00698CA0`) zeigt je nach Ergebnis die Meldung „erfolgreich“ (Name und Kopfgeld; in der China-Variante vertauscht), „zu wenig Basis-Kopfgeld“, „zu wenig Geld“ oder „schon ausgeschrieben“ und löscht bei Erfolg den letzten Angreifer.

## Ranglisten-Tafel (OpenBoard, OnClickPage, CBResultList)

Die Tafel zeigt 10 Seiten zu je 10 Einträgen (`AGPMWANTEDCRIMINAL_MAX_PAGE`, `…_PER_PAGE`; Eintragsgröße im Binary `0x58` Byte). `OpenBoard` (`0x0069A290`) lädt Seite 0, merkt die Öffnungsposition (`+0xC28…`), wirft `WC_OPEN_BOARD` und aktualisiert die Liste. `OnClickPage` (`0x00698C10`) lehnt Seiten außerhalb 0…9 und eine unveränderte Seite ab (außer beim Aktualisieren), leert die Einträge und fragt die Seite an. `CBClickBoardLeft`/`Right` begrenzen auf 0…9; `CBClickBoardPage01`…`10` (`0x00699590`…`0x00699A10`, je 118/121 Byte) rufen `OnClickPage(0…9)`; `CBClickBoardRefresh` (`0x00699A90`) lädt die aktuelle Seite neu; `CBClickBoardClose` (`0x0069A440`) ruft `ResetBoard` (`0x00699F10`).
`CBResultList` (`0x00698E60`): Das Seitenende wird mit dem Wert −100 (`AGPMWANTEDCRIMINAL_END_OF_LIST`) gemeldet; dann wird die Eintragszahl gesetzt, das Seitenereignis (`WC_PAGE_01` + Seite) geworfen und je Eintrag `WC_CHAR_ONLINE` oder `WC_CHAR_OFFLINE` ausgelöst. Sonst wird der Eintrag am Platz `Rang − Seite × 10 − 1` unter einem Mutex abgelegt.

## Rang-Abfrage und Pakete (Typ 0x46)

Alle Sender benutzen `AGPMWANTEDCRIMINAL_PACKET_TYPE` (`0x46`) mit `MakePacket` (`0x004EA2D0`):

| Sender | Adresse | Operation | Inhalt |
|---|---|---:|---|
| `SendRequestEvent` | `0x00698400` | 0 (Ereignis-Anfrage) | `AgpmWantedCriminal::MakePacketEventRequest` (`0x0056B9F0`) |
| `SendArrange` | `0x00698480` | 2 (`ARRANGE`) | Charakter-ID und eingebettetes Paket mit Name und Kopfgeld (64 Bit) |
| `SendRequstList` | `0x00698580` | 3 (`REQ_LIST`) | Charakter-ID und Seitennummer |
| `SendRequestMyRank` | `0x00698620` | 5 (`MY_RANK`) | Charakter-ID |

`OnIdle` (`0x00698BC0`) sendet alle **30 000 ms** (`AGCMUIWANTEDCRIMINAL_UPDATE_RANK_INTERVAL`) die Rang-Anfrage, aber nur wenn der eigene Charakter als gesucht markiert ist (Flag `+0x7AC` am Charakter). Anders als bei [`AgcmUIPvP`](AgcmUIPvP.md) ist `OnIdle` hier aktiv: Der Konstruktor ruft `EnableIdle(TRUE)`.
`CBResultMyRank` (`0x00698F90`) setzt den Tooltip des Alarm-Symbols („Rang %d“ und „Kopfgeld %I64d“); `CBUpdateFlag` (`0x00698710`) zeigt oder entfernt das Alarm-Symbol (Textur `WantedAlarm`) als Systemmeldungs-Symbol; `CBNotify` (`0x00699090`) meldet „Gesuchten getötet“ bzw. „vom Gesuchten getötet“ mit Name und Kopfgeld.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x0069A460`, `0x0069A120`, `0x00698310`, `0x006982C0`, `0x0069A780`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Funktion** (19)

| Name | Id | Handler |
|---|---:|---|
| `WC_ARRANGE_MENU` |  | `FUN_006988a0` |
| `WC_ARRANGE1_OK` |  | `FUN_00699190` |
| `WC_ARRANGE2_OK` |  | `FUN_00699280` |
| `WC_ARRANGE3_OK` |  | `FUN_006988b0` |
| `WC_ARRANGE_CANCEL` |  | `FUN_00699420` |
| `WC_BOARD_LEFT` |  | `FUN_00699470` |
| `WC_BOARD_RIGHT` |  | `FUN_00699500` |
| `WC_BOARD_PAGE01` |  | `FUN_00699590` |
| `WC_BOARD_PAGE02` |  | `FUN_00699610` |
| `WC_BOARD_PAGE03` |  | `FUN_00699690` |
| `WC_BOARD_PAGE04` |  | `FUN_00699710` |
| `WC_BOARD_PAGE05` |  | `FUN_00699790` |
| `WC_BOARD_PAGE06` |  | `FUN_00699810` |
| `WC_BOARD_PAGE07` |  | `FUN_00699890` |
| `WC_BOARD_PAGE08` |  | `FUN_00699910` |
| `WC_BOARD_PAGE09` |  | `FUN_00699990` |
| `WC_BOARD_PAGE10` |  | `FUN_00699a10` |
| `WC_BOARD_REFRESH` |  | `FUN_00699a90` |
| `WC_BOARD_CLOSE` |  | `FUN_0069a440` |

**Anzeige** (11)

| Name | Id | Handler |
|---|---:|---|
| `WC_ARRANGE_DESC` | 0 | `FUN_00699ab0` |
| `WC_ARRANGE_DESC2` | 0 | `FUN_00699b70` |
| `WC_ARRANGE_DESC3` | 0 | `FUN_00699c30` |
| `WC_ARRANGE_CHARID` | 0 | `FUN_00698980` |
| `WC_ARRANGE_TGHELD` | 0 | `FUN_006989d0` |
| `WC_ARRANGE_BOUNTY` | 0 | `FUN_00698a20` |
| `WC_BOARD_RANK` | 0 | `FUN_00698aa0` |
| `WC_BOARD_WANTED` | 0 | `FUN_00699cf0` |
| `WC_BOARD_BOUNTY` | 0 | `FUN_00699d50` |
| `WC_BOARD_LEVEL` | 0 | `FUN_00699db0` |
| `WC_BOARD_CLASS` | 0 | `FUN_00699e10` |

**UserData** (3)

| Name | Id | Handler |
|---|---:|---|
| `WC_UD_DUMMY` | 0 | – |
| `WC_UD_BOARD` |  | – |
| `WC_UD_ARR_ENABLE` |  | – |

**Boolean** (1)

| Name | Id | Handler |
|---|---:|---|
| `WC_ACTIVE_ARRANGE` |  | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Registrierungsreihenfolge, `OpenBoard`, `OpenArrange`, `OnClickPage`, `CBResultList`, `OnIdle`, die vier Sender).

## Grenzen

- `CBResultArrange`, `CBResultMyRank`, `CBUpdateFlag`, `CBNotify` und die drei Arrange-OK-Funktionen wurden über Größe, Aufrufe und die Registrierungsreihenfolge zugeordnet; ihre Texte und Verzweigungen sind nicht Zeile für Zeile verglichen.
- Die 30 UI-Funktionen und Anzeigen folgen der Registrierungsreihenfolge; die zehn Seitenfunktionen unterscheiden sich im Binary nur durch die Seitenzahl.
- Die kleine Hilfe `0x00698B50` (Vektor-Destruktor für zehn Einträge zu je 0x58 Byte) gehört zu keiner Quellmethode.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, gemeinsamer Rumpf: 1, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventManager`](AgcmEventManager.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmGrid`](AgpmGrid.md), [`AgpmWantedCriminal`](AgpmWantedCriminal.md)
