# AgcmLogin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmLogin` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmLogin` / `AgcmLogin.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x0065E1D0` (vtable-Slot 9); Auswertung über Sprungtabelle (aus dem Binary ausgewertet).
- **Opcodes:** Quelle `AGPMLOGIN_*` kennt 23 Operationen, davon 23 mit eigenem Case im 2017er Binary; alle haben einen Case.
- **Vergleich mit 2013:** Für 15 Operationen liegen 2013er Ereignisse vor; 15 davon stimmen mit den im 2017er Binary gefundenen Callback-Ereignissen überein, 0 weichen ab. Abweichungen sind Messhinweise, keine bestätigten Protokolländerungen: die Auswertung folgt nur Funktionen im Adressbereich des Moduls, Ereignisse in weiter entfernten Hilfsfunktionen fehlen deshalb (`2017 ⊂ 2013`).
- **Paketlayout:** 0 Paketdefinition(en) in der Quelle, 0 davon im 2017er Konstruktor (`None`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x0065CA70` | `AgcmLogin::ctor_or_dtor_0065ca70` | merged |
| `0x0065CC20` | `AgcmLogin::ctor_or_dtor_0065cc20` | merged |
| `0x0065CC80` | `AgcmLogin::OnAddModule` | merged |
| `0x0065CD10` | `AgcmLogin::OnIdle` | merged |
| `0x0065DE20` | `AgcmLogin::~AgcmLogin` | merged |
| `0x0065E1D0` | `AgcmLogin::OnReceive` | merged |
| `0x0065E4D0` | `AgcmLogin::_IsExistLoginSelectFile` | strmatch |
| `0x0065CDA0` | `AgcmLogin::OnUnionInfo` | casemap:AgcmLogin |
| `0x0065CE10` | `AgcmLogin::OnCharacterName` | casemap:AgcmLogin |
| `0x0065CED0` | `AgcmLogin::OnEnterGame` | casemap:AgcmLogin |
| `0x0065CF90` | `AgcmLogin::OnRemoveCharacter` | casemap:AgcmLogin |
| `0x0065D030` | `AgcmLogin::OnLoginResult` | casemap:AgcmLogin |
| `0x0065DFA0` | `AgcmLogin::OnCompensationInfo` | casemap:AgcmLogin |

13 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 0 | `ENCRYPT_CODE` | inline | `ENCRYPT_CODE` | = (2013 = 2017) |
| 1 | `SIGN_ON` | inline | `SIGN_ON` | = (2013 = 2017) |
| 2 | `EKEY` | inline | `EKEY_ACTIVE` | = (2013 = 2017) |
| 3 | `UNION_INFO` | `0x0065CDA0` `OnUnionInfo` | `UNION_INFO` | = (2013 = 2017) |
| 4 | `CHARACTER_NAME` | `0x0065CE10` `OnCharacterName` | `CHARACTER_NAME`, `NEW_CHARACTER_NAME` | = (2013 = 2017) |
| 5 | `CHARACTER_NAME_FINISH` | inline | `CHARACTER_NAME_FINISH` | = (2013 = 2017) |
| 6 | `CHARACTER_INFO` | inline | – | keine Callback-Ereignisse (beide) |
| 7 | `CHARACTER_INFO_FINISH` | inline | `CHARACTER_INFO_FINISH` | = (2013 = 2017) |
| 8 | `ENTER_GAME` | `0x0065CED0` `OnEnterGame` | `ENTER_GAME` | = (2013 = 2017) |
| 9 | `RETURN_TO_SELECT_WORLD` | inline | – | keine Callback-Ereignisse (beide) |
| 10 | `RACE_BASE` | inline | `RACE_BASE` | = (2013 = 2017) |
| 11 | `NEW_CHARACTER_NAME` | `0x0065CE10` `OnCharacterName` | `CHARACTER_NAME`, `NEW_CHARACTER_NAME` | = (2013 = 2017) |
| 12 | `NEW_CHARACTER_INFO_FINISH` | inline | `NEW_CHARACTER_INFO_FINISH` | = (2013 = 2017) |
| 13 | `REMOVE_CHARACTER` | `0x0065CF90` `OnRemoveCharacter` | `REMOVE_CHARACTER` | = (2013 = 2017) |
| 14 | `RENAME_CHARACTER` | inline | – | keine Callback-Ereignisse (beide) |
| 15 | `LOGIN_RESULT` | `0x0065D030` `OnLoginResult` | `LOGIN_RESULT` | = (2013 = 2017) |
| 16 | `REMOVE_DUPLICATED_ACCOUNT` | inline | – | keine Callback-Ereignisse (beide) |
| 17 | `COMPENSATION_INFO` | `0x0065DFA0` `OnCompensationInfo` | `COMPENSATION_INFO` | = (2013 = 2017) |
| 18 | `COMPENSATION_CHARACTER_SELECT` | inline | – | keine Callback-Ereignisse (beide) |
| 19 | `COMPENSATION_CHARACTER_CANCEL` | inline | – | keine Callback-Ereignisse (beide) |
| 20 | `COUPON_INFO` | inline | – | keine Callback-Ereignisse (beide) |
| 21 | `CREATE_CHARACTER` | inline | – | keine Callback-Ereignisse (beide) |
| 32 | `INVALID_CLIENT_VERSION` | inline | `INVALID_CLIENT_VERSION` | = (2013 = 2017) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): Kandidat unbestätigt: 1, eingebaut: 1, gemeinsamer Rumpf: 17, nicht im Client: 2, ohne Kandidat: 5, zugeordnet: 17.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `DisconnectLoginServer` | 11 | `0x0065CD60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendRenameCharacter` | 53 | `0x0065DAB0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendEnterGame` | 66 | `0x0065D450` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `RenameCharacter` | 13 | `0x0065DF10` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SelectCharacter` | 31 | `0x0065DE40` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `ConnectLoginServer` | 16 | `0x0065E5A0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendAccount` | 82 | `0x0065E660` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendCharacter4Compensation` | 53 | `0x0065DBB0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendRemoveCharacter` | 61 | `0x0065D990` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendCreateCharacter` | 62 | `0x0065D860` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendCreateCharacter` | 62 | `0x0065D730` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetBaseCharacterOfRace` | 50 | `0x0065D640` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendReturnToSelectServer` | 39 | `0x0065D570` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetCharacters` | 40 | `0x0065D390` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetUnion` | 34 | `0x0065D2F0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendEKey` | 39 | `0x0065D210` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |
| `SendGetEncryptCode` | 56 | `0x0065D100` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

Kandidaten ohne ausreichenden Beleg (nicht benannt): `SetIDPassword` (`0x0065D0A0`).

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcAuth`](AgcAuth.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmStartupEncryption`](AgcmStartupEncryption.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUITips`](AgcmUITips.md)
