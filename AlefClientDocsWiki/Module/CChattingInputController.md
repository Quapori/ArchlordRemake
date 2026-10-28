# CChattingInputController (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `CChattingInputController` (Chat-Eingabefeld und Eingabeart) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `CChattingInputController.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 23 von 25 Quellmethoden sind zugeordnet; neu sind elf Funktionen (Eingabefeld, Flüster-Antwort, Menü).
- **Flüster-Antwort:** Format `%s %s `, nur bei Eingabeart 1 oder 5.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CChattingInputController.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInitEditChatting` | `0x0070AFE0` | 53 | Zeichenkette |
| 1 | `OnDestroyEditChatting` | `0x0070B020` | 39 | ver |
| 2 | `OnAddCustomControl` | `0x0070B9E0` | 333 | Zeichenkette |
| 3 | `InitMenu` | `0x0070BB30` | 533 | ver |
| 4 | `OnSetChattingMessage` | `0x0070B050` | 73 | ver |
| 5 | `OnAddChattingMessage` | `0x0070B750` | 244 | ver |
| 6 | `ReCalcChatInputPosition` | `0x0070B0A0` | 68 | ver |
| 7 | `OnShowEditChatting` | `0x0070B560` | 25 | ver |
| 8 | `ActiveChatInput` | `0x0070B0F0` | 8 | ver |
| 9 | `OnReadyStatusEvent` | `0x0070B850` | 45 | ver |
| 10 | `OnReadyAutoReplyWhisper` | `0x0070B100` | 179 | ver |
| 11 | `OnReadyAutoReplyWhisper` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 12 | `OnReadyItemRegister` | `0x0070B880` | 116 | Zeichenkette |
| 13 | `OnReadyMapPosRegister` | `0x0070B900` | 125 | Zeichenkette |
| 14 | `CallBack_OnInputStart` | `0x0070B1C0` | 41 | UI-Registrierung |
| 15 | `CallBack_OnInputEnd` | `0x0070B1F0` | 317 | UI-Registrierung |
| 16 | `CallBack_OnInputEndPrivate` | `0x0070B350` | 300 | UI-Registrierung |
| 17 | `CallBack_OnAutoReplyWhisper` | `0x0070B580` | 40 | UI-Registrierung |
| 18 | `CallBack_OnInputStatusClick` | `0x0070B5B0` | 73 | UI-Registrierung |
| 19 | `Callback_DisplayStatus` | `0x0070B480` | 100 | UI-Registrierung |
| 20 | `CBMenuStatusChange` | `0x0070B980` | 53 | ver |
| 21 | `CallBack_StatusRefresh` | `0x0070B9C0` | 29 | ver |
| 22 | `ChangeInputStatus` | `0x0070B600` | 295 | Zeichenkette |
| 23 | `OpenInputStatusMenu` | `0x0070B4F0` | 73 | ver |
| 24 | `GetToID` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |

23 von 25 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0070aeb0` (`0x0070AEB0`), `ctor_or_dtor_0070af60` (`0x0070AF60`), `~CChattingInputController` (`0x0070B540`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x31CC` | `Textur der Eingabeinfo (`m_pInputInfoTex`)` | `OnDestroyEditChatting` |
| `0x31A4` | `aktuelle Eingabeart` | `OnReadyStatusEvent` |
| `0x31E8` | `Name des letzten Flüster-Ziels (`m_strAutoReplyTargetName`)` | `OnReadyStatusEvent`, `SetAutoReplyWhisperTarget` |

## Umfang

`CChattingInputController` verwaltet das Eingabefeld des Chats und die Eingabeart (`CChattingInputController.cpp`, 25 Methoden); im Binary bei `0x0070AEB0`–`0x0070BB30`. [`AgcmUIChatting2`](AgcmUIChatting2.md):OnInit` ruft `OnInitEditChatting` (`0x0070AFE0`) und `InitMenu` (`0x0070BB30`) auf, `OnDestroy` ruft `OnDestroyEditChatting` (`0x0070B020`).

## Eingabearten

Die Arten der Quelle sind 0 Normal, 1 Flüstern, 2 Gruppe, 3 Gilde, 4 Rufen, 5 Antwort. `OnReadyStatusEvent` (`0x0070B850`) wird nur bei 1 oder 5 aktiv und trägt dann das letzte Flüster-Ziel (Zeichenkette bei `+0x31E8`) ein. `OnReadyAutoReplyWhisper` (`0x0070B100`) setzt den Text `"<Flüsterbefehl> <Name> "` (UI-Text `0x21E`, Format `%s %s `); `OnSetChattingMessage` (`0x0070B050`) schreibt ihn ins Eingabefeld und aktualisiert die Ereignisse.

## Eingabefeld

`OnShowEditChatting` (`0x0070B560`) aktualisiert den Zustand ([`AcUIChattingEdit`](AcUIChattingEdit.md):UpdateCurrentStatus`) und aktiviert das Feld (`ActiveChatInput`, `0x0070B0F0`). `CBMenuStatusChange` (`0x0070B980`) leert den Text, wechselt die Eingabeart und aktiviert das Feld; `CallBack_StatusRefresh` (`0x0070B9C0`) wechselt nur die Art, ohne den Text zu leeren. `OpenInputStatusMenu` (`0x0070B4F0`) öffnet das Menü bei X mit fester Y-Lage 200 und Größe 100×200.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `SetAutoReplyWhisperTarget` (`0x005BE1F0`, 52 Byte) liegt im Binary im Bereich von `AgcmUIChatting2` und steht nicht in der Methodenliste der Quelle (Inline in der Headerdatei).
- Die größeren Handler `CallBack_OnInputEnd` und `CallBack_OnInputEndPrivate` waren bereits benannt und wurden hier nicht neu geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 1, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AcUIChattingEdit`](AcUIChattingEdit.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
