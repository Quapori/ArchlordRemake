# CFlagImoticon (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `CFlagImoticon` (Flaggen-Symbole und Versätze aus `FlagImoticon.xml`; Basisklasse von [`AgcmTextBoardMng`](AgcmTextBoardMng.md)) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Aufrufgraph, EP8-Quelle `Modules/AClient/AgcmTextBoard/CFlagImoticon.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 6 von 10 Quellmethoden sind zugeordnet. Nicht im Binary sind `ReloadFlag` (die Quelle ruft sie nur im Chat-Befehl `CChatCmd::CallBack_OnFlagImoticon` und dort nur unter `#ifdef _DEBUG`; im Release-Binary prüft `0x00711350` nur Argument und Modul `AgcmTextBoardMng`), `GetFlagTexture(char*)`, `GetFlagOffsetX(char*)` und `GetFlagOffsetX(bool, bool)` (in der Quelle ohne Aufrufer).
- **Abweichungen:** keine; das Fehlen von `ReloadFlag` erklärt sich durch die Debug-Bedingung der Quelle.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CFlagImoticon.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `LoadFlagFromFile` | `0x00756930` | 984 | von Hand geprüft |
| 1 | `ReloadFlag` | – | | nicht im Binary: einziger Aufrufer der Quelle liegt unter `#ifdef _DEBUG` (`CallBack_OnFlagImoticon`, im Binary `0x00711350` ohne Aufruf) |
| 2 | `ClearAllFlag` | `0x00756D10` | 172 | von Hand geprüft |
| 3 | `_LoadXmlFile` | `0x00755F00` | 383 | von Hand geprüft |
| 4 | `GetFlagTexture` | – | | nicht im Binary: Fassung mit Namen in der Quelle ohne Aufrufer |
| 5 | `GetFlagTexture` | `0x007563B0` | 131 | von Hand geprüft |
| 6 | `GetFlagOffsetX` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 7 | `GetFlagOffsetY` | `0x007566A0` | 135 | von Hand geprüft |
| 8 | `GetFlagOffsetX` | – | | nicht im Binary: in der Quelle ohne Aufrufer |
| 9 | `GetFlagOffsetY` | `0x00756730` | 73 | von Hand geprüft |

6 von 10 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `GetFlagOffsetY_byName` (`0x007566A0`), `~CFlagImoticon` (`0x00756EA0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `Eintrag+0x140 / 0x144` | `Textur / Ereigniscode eines Flaggeneintrags (`stFlagEntry`)` | `GetFlagTexture(int)` |
| `this+0x08 / 0x10` | `Tabelle und Anzahl der Flaggeneinträge (nach den Zugriffen in `GetFlagTexture(int)`)` | `GetFlagTexture(int)` |

## Aufbau

`CFlagImoticon` ist eine Basisklasse von `AgcmTextBoardMng` (Flaggen-Symbole neben dem Namen: Nationalflaggen nach Ereigniscode, Versätze nach Gilden-/Charisma-Zustand). Zwei Tabellen (`m_mapFlag`, `m_mapOffset`) halten Einträge nach Namen. `AgcmTextBoardMng::OnInit` lädt die Datei `INI\FlagImoticon.xml` mit `LoadFlagFromFile` (`0x00756930`, 984 Byte); `OnDestroy` ruft `ClearAllFlag` (`0x00756D10`), der Destruktor des Managers die Aufräumkette `0x00756EA0`.

## Laden

`_LoadXmlFile` (`0x00755F00`, 383 Byte) liest die Datei mit `CreateFile`/`ReadFile`, entschlüsselt sie bei verschlüsselten Dateien mit `AuMD5Encrypt` und dem Schlüssel „1111“ und parst sie mit TinyXML. `LoadFlagFromFile` erwartet die Wurzel `FlagImoticon` mit den Listen `FlagList` (Einträge `Name`, `FileName`, `EventCode`; die Textur wird mit `RwTextureRead` geladen) und `PositionList` (`Name`, `OffsetX`, `OffsetY`) und füllt beide Tabellen. `ClearAllFlag` zerstört die Texturen und leert beide Tabellen.

## Abfragen

`GetFlagTexture(int)` (`0x007563B0`, 131 Byte) sucht den Eintrag mit passendem Ereigniscode (Feld `+0x144`, Textur bei `+0x140`); es wird von [`AgcmIDBoard`](AgcmIDBoard.md):_DrawFlag` mit der Nationalflagge des Charakters gerufen. `GetFlagOffsetY(bool, bool)` (`0x00756730`, 73 Byte) wählt den Zustandsnamen („Normal“, „HaveGuild“, „HaveCharisma“, „HaveGuildAndCharisma“) und ruft die Namensfassung `0x007566A0` (135 Byte); Aufrufer ist ebenfalls `_DrawFlag`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Zuordnung von `LoadFlagFromFile` (`0x00756930`) und `_LoadXmlFile` (`0x00755F00`) beruht auf TinyXML-Aufrufen, der Aufrufbeziehung zu `OnInit` bzw. zueinander und der Größe; sie wurden nicht Zeile für Zeile verglichen.
- Die Offsets stammen nur aus `GetFlagTexture(int)`; die Struktur der Tabellen (`m_mapFlag`) ist nicht vermessen.
- Dass die Namensfassung `0x007566A0` zu `GetFlagOffsetY(char*)` gehört, folgt aus der Aufrufbeziehung (nur von `0x00756730` gerufen) und dem Tabellenzugriff.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht im Client: 2, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmIDBoard`](AgcmIDBoard.md), [`AgcmTextBoard`](AgcmTextBoard.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md)
