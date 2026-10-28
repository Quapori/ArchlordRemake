# AgpmLogin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmLogin` (Paketformate der Anmeldung, Zeichenlängen-Behandlung je Dienstgebiet) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmLogin/AgpmLogin.cpp`, `Include/AgpmLogin.h`, `Include/AuType.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle sieben Methoden sind zugeordnet. `OnAddModule` liegt am gemeinsamen Rumpf `0x0067AC90`; `GetNextCharKr` und `GetNextCharCn` teilen sich `0x0057A990`.
- **Paketformate:** Das Hauptpaket der Anmeldung (16 Felder) und fünf Unterpakete sind im Konstruktor vollständig lesbar und stimmen mit der Quelle überein; die Typnummern und Größen sind im Abschnitt „Paketaufbau“ aufgelistet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmLogin.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 1 | `IsDuplicatedCharacterOfMigration` | `0x0057A930` | 77 | von Hand geprüft |
| 2 | `InitFuncPtr` | `0x0057AB00` | 102 | von Hand geprüft |
| 3 | `GetNextCharKr` | `0x0057A990` | 21 | von Hand geprüft |
| 4 | `GetNextCharEn` | `0x0057A980` | 10 | von Hand geprüft |
| 5 | `GetNextCharCn` | `0x0057A990` | 21 | gleiche Adresse wie `gleicher Rumpf wie `GetNextCharKr` (zusammengefaltet)` (vom Linker zusammengefaltet) |
| 6 | `GetNextCharJp` | `0x0057A9B0` | 30 | von Hand geprüft |

7 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgpmLogin_body` (`0x0057A880`), `scalar_deleting_dtor` (`0x0057AAE0`), `AgpmLogin` (`0x0057AB70`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB84` | `Hauptpaket `m_csPacket`` | Konstruktor, `0x0065D100` |
| `this+0x13498` | `Paket Serveradresse` | Konstruktor |
| `this+0x25DAC` | `Paket Charakterinfo` | Konstruktor |
| `this+0x386C0` | `Paket Serverinfo` | Konstruktor |
| `this+0x4AFD4` | `Paket Versionsinfo (Hauptversion, Nebenversion)` | Konstruktor, `0x0065D100` |
| `this+0x5D8E8` | `Paket Entschädigungsinfo` | Konstruktor |
| `this+0x701FC` | `Zeiger `GetNextCharPtr`` | `InitFuncPtr`, `IsDuplicatedCharacterOfMigration` |
| `0x008AD470` | `Dienstgebiet `g_eServiceArea`` | `InitFuncPtr` |

## Vtable und Aufbau

Vtable `0x008B91B0`: Slot 0 Löschwrapper (`0x0057AAE0`, Rumpf `0x0057A880`: sechs `AuMiniLZO`-Objekte und sechs Paketobjekte werden abgebaut), Slot 1 `OnAddModule` und Slot 2 am gemeinsamen Rumpf `0x0067AC90` (`return TRUE`), Slot 3 `0x0067FAB0`. Der Konstruktor (`0x0057AB70`, 554 Byte) trägt `AgpmLogin` als Modulnamen ein und richtet sechs Pakete mit ihren Feldlisten ein (siehe unten); zum Schluss ruft er `InitFuncPtr` (`0x0057AB00`).

## Paketaufbau (aus dem Konstruktor)

Die Feldlisten stehen im Konstruktor als Aufrufe von `SetFieldType` (`0x004E9F80`) mit den Typnummern von `eAUTYPE` (0 `CHAR`, 1 `INT8`, 5 `INT32`, 12 `PACKET`, 13 `MEMORY_BLOCK`, `0xFF` Ende). Die Pakete liegen als Unterobjekte im Modul: `m_csPacket` bei `this+0xB84`, Serveradresse bei `+0x13498`, Charakterinfo bei `+0x25DAC`, Serverinfo bei `+0x386C0`, Versionsinfo bei `+0x4AFD4`, Entschädigungsinfo bei `+0x5D8E8`.
Hauptpaket (Flag-Länge 2 Byte, 16 Felder): `INT8`; `CHAR[32]` (Verschlüsselungstext); `CHAR[49]` (Konto-ID, 48 Zeichen + 0); `INT8`; `CHAR[33]` (Passwort, 32 + 0); `INT8`; `INT32`; `CHAR[32]` (Servergruppenname); `PACKET`; `PACKET`; `INT32`; `PACKET`; `CHAR[2049]` (J-Authentifizierungstext, 2048 + 0); `CHAR[5]` (Challenge des Schlüsselaustauschs, `AGPMLOGIN_EKEY_CHALLENGE`); `INT32`; `INT32`. Das stimmt Feld für Feld mit der Liste der Quelle überein; die Bedeutung der Felder steht in den Kommentaren der Quelle, die im Binary fehlen.
Unterpakete (Flag-Länge 1 Byte, außer wo angegeben): Serveradresse = drei `CHAR[23]` (`AGPMLOGIN_IPADDRSIZE`); Charakterinfo (Flag-Länge 2) = `INT32`, `CHAR[49]`, sechs `INT32`, `CHAR[49]`, `INT32`; Serverinfo = ein `CHAR[23]`; Versionsinfo = zwei `INT32` (Hauptversion, Nebenversion; von [`AgpmResourceInfo`](AgpmResourceInfo.md) gefüllt, siehe dessen Bericht); Entschädigungsinfo = zwei `INT32`, `CHAR[49]`, `CHAR[100]`, ein `MEMORY_BLOCK`.

## Zeichenbehandlung

`InitFuncPtr` (`0x0057AB00`, 102 Byte) wählt nach dem Dienstgebiet (`g_eServiceArea`, `0x008AD470`) den Zeiger `GetNextCharPtr` (`this+0x701FC`): Korea, China und Taiwan zeigen auf `0x0057A990` (zwei Byte bei Zeichen über `0x80`, sonst eines), Japan auf `0x0057A9B0` (Doppelbytebereiche `0x81–0x9F` und `0xE0` aufwärts), Global auf `0x0057A980` (immer ein Byte). `GetNextCharKr` und `GetNextCharCn` sind im Binary derselbe Rumpf (`0x0057A990`, gleiche Anweisungen).
`IsDuplicatedCharacterOfMigration` (`0x0057A930`, 77 Byte) liefert TRUE, wenn der Name kürzer als vier Zeichen ist (`AGPMLOGIN_MIN_CHARID_SIZE`) oder ein `@` enthält; Aufrufer sind `0x0060BE50`, `0x0065DE40` und `0x0065DF10`. `AgpdLoginCompenItemList::Parse` (`0x0057A9D0`, 260 Byte; kein Teil der Methodenzählung) zerlegt Listen der Form `TID:Menge,TID:Menge` (Format `%d:%d`) für Entschädigungsgegenstände; Aufrufer ist `0x0060E810`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Feldlisten sind aus den Zahlenargumenten von `SetFieldType` gelesen und über die Typnummern von `eAUTYPE` und die Konstanten der Quelle (`AGPMLOGIN_…`) gedeutet; die Größen 49 und 33 (Konto-ID, Passwort) sind aus dem Binary, nicht aus einem Mitschnitt.
- Die Namen der Felder (welche `INT8` Operation, welche `INT32` Charakter-ID usw. ist) stehen in der Quelle nur in Kommentaren, die hier nicht ausgewertet wurden; ein Abgleich mit dem Login-Protokoll des Privatservers wurde nicht gemacht.
- Die Zuordnung der Dienstgebiete zu den drei Rümpfen folgt aus den Vergleichen in `InitFuncPtr` (Wert 0 bis 4); welches Gebiet der 2017er Build tatsächlich eingestellt hat, wurde nicht geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmResourceInfo`](AgpmResourceInfo.md)
