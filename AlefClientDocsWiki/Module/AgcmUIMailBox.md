# AgcmUIMailBox (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIMailBox` (Briefkasten: Liste, Lesen, Schreiben, Anhänge speichern) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIMailBox/AgcmUIMailBox.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 59 von 62 Quellmethoden sind zugeordnet; fast alle Handler ergeben sich aus der Reihenfolge der UI-Registrierungen (neues Werkzeug `uireg.py`).
- **Pakete:** Remove 1, Read 2, Write 3, ItemSave 4 über Paket-Typ `0x2D`, wie in der Quelle.
- **UI-Schnittstelle:** unverändert (12 Funktionen, 13 Anzeigen, 3 Boolean).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIMailBox.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0069D150` | 495 | vtable/String |
| 1 | `OnInit` | `0x0069A9E0` | 99 | vtable/String |
| 2 | `OnDestroy` | `0x0069AA50` | 78 | vtable/String |
| 3 | `OnIdle` | `0x0069B6E0` | 239 | vtable/String |
| 4 | `AddEvent` | `0x0069AAA0` | 67 | von Hand geprüft |
| 5 | `AddFunction` | `0x0069CD50` | 495 | Zeichenkette |
| 6 | `AddDisplay` | `0x0069CF40` | 429 | Zeichenkette |
| 7 | `AddUserData` | `0x0069AAF0` | 313 | Zeichenkette |
| 8 | `AddBoolean` | `0x0069D0F0` | 95 | Zeichenkette |
| 9 | `OpenWriteWindow` | `0x0069AC30` | 124 | Aufrufgraph (geprüft) |
| 10 | `CBSetSelfCharacter` | `0x0069ACB0` | 52 | Callback-Registrierung |
| 11 | `CBReleaseSelfCharacter` | `0x0069ACF0` | 41 | Callback-Registrierung |
| 12 | `CBAddMail` | `0x0069C430` | 238 | Callback-Registrierung |
| 13 | `CBWriteMail` | `0x0069B7D0` | 196 | Callback-Registrierung |
| 14 | `CBRemoveMail` | `0x0069C520` | 250 | Callback-Registrierung |
| 15 | `CBItemSave` | `0x0069C620` | 185 | Callback-Registrierung |
| 16 | `CBRemoveItem` | `0x0069B8A0` | 87 | Callback-Registrierung |
| 17 | `CBOpenWindowList` | `0x0069C6E0` | 98 | Zeichenkette |
| 18 | `CBClickButtonListRead` | `0x0069C750` | 235 | Aufrufgraph (geprüft) |
| 19 | `CBClickButtonListDelete` | `0x0069C840` | 65 | uireg:AgcmUIMailBox |
| 20 | `CBClickButtonListWrite` | `0x0069AD20` | 26 | uireg:AgcmUIMailBox |
| 21 | `CBClickButtonWriteSend` | `0x0069B900` | 660 | uireg:AgcmUIMailBox |
| 22 | `CBCloseWindowWrite` | `0x0069BBA0` | 137 | uireg:AgcmUIMailBox |
| 23 | `CBMoveItemWrite` | `0x0069BC30` | 249 | uireg:AgcmUIMailBox |
| 24 | `CBMoveEndItemWrite` | `0x0069BD30` | 100 | uireg:AgcmUIMailBox |
| 25 | `CBInputTabWrite` | `0x0069AD40` | 70 | uireg:AgcmUIMailBox |
| 26 | `CBCloseWindowRead` | `0x0069AD90` | 49 | uireg:AgcmUIMailBox |
| 27 | `CBClickButtonReadItemSave` | `0x0069C890` | 196 | Zeichenkette |
| 28 | `CBClickButtonReadReply` | `0x0069ADD0` | 32 | uireg:AgcmUIMailBox |
| 29 | `CBDisplayListSubject` | `0x0069C960` | 67 | uireg:AgcmUIMailBox |
| 30 | `CBDisplayListDate` | `0x0069C9B0` | 96 | uireg:AgcmUIMailBox |
| 31 | `CBDisplayAvailableLetter` | `0x0069BDA0` | 194 | uireg:AgcmUIMailBox |
| 32 | `CBDisplayReadToCharID` | `0x0069CA10` | 56 | uireg:AgcmUIMailBox |
| 33 | `CBDisplayReadSubject` | `0x0069CA50` | 56 | uireg:AgcmUIMailBox |
| 34 | `CBDisplayReadContent` | `0x0069CA90` | 79 | uireg:AgcmUIMailBox |
| 35 | `CBDisplayReadFromCharID` | `0x0069CAE0` | 56 | uireg:AgcmUIMailBox |
| 36 | `CBDisplayReadDesc` | `0x0069ADF0` | 33 | uireg:AgcmUIMailBox |
| 37 | `CBDisplayWriteFromCharID` | `0x0069AE20` | 48 | uireg:AgcmUIMailBox |
| 38 | `CBDisplayWriteDesc` | `0x0069BE70` | 228 | uireg:AgcmUIMailBox |
| 39 | `CBDisplayWriteToCharID` | `0x0069CB20` | 95 | uireg:AgcmUIMailBox |
| 40 | `CBDisplayWriteSubject` | `0x0069CB80` | 166 | uireg:AgcmUIMailBox |
| 41 | `CBDisplayWriteContent` | `0x0069CC30` | 69 | uireg:AgcmUIMailBox |
| 42 | `CBIsActiveDeleteButton` | `0x0069CC80` | 50 | uireg:AgcmUIMailBox |
| 43 | `CBIsActiveItemSaveButton` | `0x0069CCC0` | 135 | uireg:AgcmUIMailBox |
| 44 | `CBIsActiveWriteButton` | `0x0069AE50` | 71 | uireg:AgcmUIMailBox |
| 45 | `SendWriteMail` | `0x0069AEA0` | 238 | von Hand geprüft |
| 46 | `SendReadMail` | `0x0069AF90` | 209 | von Hand geprüft |
| 47 | `SendRemoveMail` | `0x0069B070` | 209 | Aufrufgraph (geprüft) |
| 48 | `SendItemSave` | `0x0069B150` | 271 | Aufrufgraph (geprüft) |
| 49 | `TestOpenWriteWindow` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 50 | `TestOpenList` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 51 | `GetMessageTxt` | – | | nicht zugeordnet (klein, eingefaltet oder ohne eindeutigen Anker) |
| 52 | `GetMailOfIndex` | `0x0069BF60` | 77 | Aufrufgraph (geprüft) |
| 53 | `RefreshList` | `0x0069BFB0` | 415 | Aufrufgraph (geprüft) |
| 54 | `AddItemToWriteGrid` | `0x0069B260` | 159 | Aufrufgraph (geprüft) |
| 55 | `AddItemToReadGrid` | `0x0069C150` | 274 | von Hand geprüft |
| 56 | `RemoveItemFromWriteGrid` | `0x0069B300` | 82 | Aufrufgraph (geprüft) |
| 57 | `RemoveItemFromReadGrid` | `0x0069B360` | 63 | von Hand geprüft |
| 58 | `SetGridItemAttachedTexture` | `0x0069B3A0` | 92 | von Hand geprüft |
| 59 | `IsOpenMailRead` | `0x0069B400` | 58 | Zeichenkette |
| 60 | `IsHaveNotReadMail` | `0x0069C270` | 350 | Zeichenketten/Konstanten (geprüft) |
| 61 | `CheckHaveNotReadMail` | `0x0069C3E0` | 79 | Aufrufgraph (geprüft) |

59 von 62 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor` (`0x0069B500`), `~AgcmUIMailBox` (`0x0069B6B0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xB88` | `m_pAgpmMailBox` | `[+0xC4C]` ist dessen Paketdefinition `m_csPacket` |
| `0xCB4` | `m_pAgpdCharacterSelf` | `CBIsActiveWriteButton` |
| `0xCB8` | `m_pAgpdMailCADSelf (Briefliste)` | `GetMailOfIndex`, `RefreshList` (Anzahl bei `[+0x30]`) |
| `0xCBC` | `m_lSelectedIndex` | `CBDisplayRead…` |
| `Brief +0x31 / +0x52` | `Empfänger (m_szToCharID) / Betreff (m_szSubject)` | `CBDisplayReadToCharID`, `CBDisplayListSubject` |

## Pakete an den Server (Typ 0x2D)

Die Sender bauen Pakete des Typs `0x2D` (45) mit `MakePacket` (`0x004EA2D0`): Operation (1 Byte), Charakter-ID, Mail-Paket ([`AgpmMailBox`](AgpmMailBox.md):MakePacketMail`, `0x00557D70` bzw. `0x00557E40`). Die Operationen entsprechen `eAGPMMAILBOX_OPERATION` der Quelle:

| Sender | Adresse | Operation |
|---|---|---|
| `SendRemoveMail` | `0x0069B070` | 1 REMOVE_MAIL |
| `SendReadMail` | `0x0069AF90` | 2 READ_MAIL |
| `SendWriteMail` | `0x0069AEA0` | 3 WRITE_MAIL (mit Gegenstand-ID) |
| `SendItemSave` | `0x0069B150` | 4 ITEM_SAVE |

Die Operationen 0 (ADD_MAIL) und 5 (REMOVE_ALL_MAIL) kommen vom Server. Die Schaltfläche „Schreiben“ ist nur aktiv, wenn die Zahl der normalen Briefe aus `AgpmMailBox::GetLetterCount` größer als 0 ist (`CBIsActiveWriteButton`).

## UI-Registrierung

Aus den Registrierungsfunktionen `AddFunction` (`0x0069CD50`), `AddDisplay` (`0x0069CF40`) und `AddBoolean` (`0x0069D0F0`); Zahl der Aufrufe: 12 Funktionen, 13 Anzeigen, 3 Boolean-Werte, in Quelle und Binary gleich (die Quelle enthält die Anzeigen und Booleans mehrfach, je Regionsvariante).

| Art | UI-Name | Handler | Adresse |
|---|---|---|---|
| Funktion | `MAIL_LIST_OPEN` | `CBOpenWindowList` | `0x0069C6E0` |
| Funktion | `MAIL_LIST_READ` | `CBClickButtonListRead` | `0x0069C750` |
| Funktion | `MAIL_LIST_DELETE` | `CBClickButtonListDelete` | `0x0069C840` |
| Funktion | `MAIL_LIST_WRITE` | `CBClickButtonListWrite` | `0x0069AD20` |
| Funktion | `MAIL_WRITE_SEND` | `CBClickButtonWriteSend` | `0x0069B900` |
| Funktion | `MAIL_WRITE_CLOSE` | `CBCloseWindowWrite` | `0x0069BBA0` |
| Funktion | `MAIL_WRITE_MOVE` | `CBMoveItemWrite` | `0x0069BC30` |
| Funktion | `MAIL_WRITE_MVEND` | `CBMoveEndItemWrite` | `0x0069BD30` |
| Funktion | `MAIL_WRITE_TAB` | `CBInputTabWrite` | `0x0069AD40` |
| Funktion | `MAIL_READ_SAVE` | `CBClickButtonReadItemSave` | `0x0069C890` |
| Funktion | `MAIL_READ_REPLY` | `CBClickButtonReadReply` | `0x0069ADD0` |
| Funktion | `MAIL_READ_CLOSE` | `CBCloseWindowRead` | `0x0069AD90` |
| Anzeige | `MAIL_LIST_SUBJECT` | `CBDisplayListSubject` | `0x0069C960` |
| Anzeige | `MAIL_LIST_DATE` | `CBDisplayListDate` | `0x0069C9B0` |
| Anzeige | `MAIL_LETTER_COUNT` | `CBDisplayAvailableLetter` | `0x0069BDA0` |
| Anzeige | `MAIL_READ_TOCHAR` | `CBDisplayReadToCharID` | `0x0069CA10` |
| Anzeige | `MAIL_READ_SUBJECT` | `CBDisplayReadSubject` | `0x0069CA50` |
| Anzeige | `MAIL_READ_CONTENT` | `CBDisplayReadContent` | `0x0069CA90` |
| Anzeige | `MAIL_READ_FROMCHAR` | `CBDisplayReadFromCharID` | `0x0069CAE0` |
| Anzeige | `MAIL_READ_DESC` | `CBDisplayReadDesc` | `0x0069ADF0` |
| Anzeige | `MAIL_WRITE_FROMCHAR` | `CBDisplayWriteFromCharID` | `0x0069AE20` |
| Anzeige | `MAIL_WRITE_DESC` | `CBDisplayWriteDesc` | `0x0069BE70` |
| Anzeige | `MAIL_WRITE_TOCHAR` | `CBDisplayWriteToCharID` | `0x0069CB20` |
| Anzeige | `MAIL_WRITE_SUBJECT` | `CBDisplayWriteSubject` | `0x0069CB80` |
| Anzeige | `MAIL_WRITE_CONTENT` | `CBDisplayWriteContent` | `0x0069CC30` |
| Boolean | `MAIL_ACTIVE_DEL_BTN` | `CBIsActiveDeleteButton` | `0x0069CC80` |
| Boolean | `MAIL_ACTIVE_SAV_BTN` | `CBIsActiveItemSaveButton` | `0x0069CCC0` |
| Boolean | `MAIL_ACTIVE_WRT_BTN` | `CBIsActiveWriteButton` | `0x0069AE50` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Drei Methoden sind nicht zugeordnet (`TestOpenWriteWindow`, `TestOpenList`, `GetMessageTxt`), sie sind klein oder nur für Tests.
- Der Inhalt der Anzeigefunktionen wurde nur stichprobenartig gelesen (zwei von 13).
- Die Mail-Paketfelder stehen im Bericht des Moduls `AgpmMailBox`.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmMailBox`](AgpmMailBox.md)
