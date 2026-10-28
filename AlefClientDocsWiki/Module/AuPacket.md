# AuPacket (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuPacket` (Paketbeschreibung: Feldtypen, Erzeugen und Lesen von Paketen, Verschlüsselung) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/AUtility/AuPacket/AuPacket.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 10 von 14 Quellmethoden zugeordnet (`SetFieldType`, `GetField`, `SetCID`, `MakePacket`, `SetFlagLength`, `GetFlagLength`, `GetCryptManager`, `EncryptPacket`, `DecryptPacket`, `SetDummy`), dazu Konstruktor und Destruktor. Mit dieser Klasse legt jedes Netzwerkmodul seine Paketformate an.
- **Nicht gefunden:** `MakeStaticPacket`, `FreePacket`, `FreeStaticPacket`, `FreeEncryptBuffer`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuPacket.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetFieldType` | `0x004E9F80` | 105 | von Hand geprüft |
| 1 | `GetField` | `0x004EA000` | 664 | von Hand geprüft |
| 2 | `SetCID` | `0x004EA2A0` | 40 | von Hand geprüft |
| 3 | `MakePacket` | `0x004EA2D0` | 937 | von Hand geprüft |
| 4 | `MakeStaticPacket` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 5 | `FreePacket` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 6 | `FreeStaticPacket` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 7 | `SetFlagLength` | `0x004EA680` | 20 | von Hand geprüft |
| 8 | `GetFlagLength` | `0x004EA6A0` | 8 | von Hand geprüft |
| 9 | `GetCryptManager` | `0x004EA6D0` | 90 | von Hand geprüft |
| 10 | `EncryptPacket` | `0x004EA730` | 277 | von Hand geprüft |
| 11 | `DecryptPacket` | `0x004EA850` | 330 | von Hand geprüft |
| 12 | `FreeEncryptBuffer` | – | | nicht im Binary gefunden; Verbleib offen (kleine Funktion, vermutlich eingebaut) |
| 13 | `SetDummy` | `0x004EA6B0` | 19 | von Hand geprüft |

10 von 14 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuPacket` (`0x004E9F10`), `~AuPacket` (`0x004E9F70`).

## Aufbau

`AuPacket` hat keine eigene Vtable; sie erbt von `AuMiniLZO` (Kompression, siehe dort). Größe `0x12914` Byte: Kompressionspuffer, dann die Beschreibung ab `+0x12808` (Feldtypen, 64 Einträge zu 16 Bit), `+0x12888` (Feldanzahlen, 64 Einträge), `+0x12908` Zahl der Felder, `+0x1290C` „Beschreibung gesetzt“ und `+0x12910` die Länge des Flagfelds. Der Konstruktor `0x004E9F10` ruft den von `AuMiniLZO` und nullt diese Felder; `0x004E9F70` ist der Destruktor (setzt nur die Vtable von `AuMiniLZO`).
`SetFieldType` (`0x004E9F80`, 163 Aufrufer) nimmt eine Liste aus Paaren (Typ, Anzahl) bis zum Endwert `0xFF` und trägt sie ein; `SetFlagLength` (`0x004EA680`, 163 Aufrufer) und `GetFlagLength` (`0x004EA6A0`) setzen und lesen die Länge des Flagfelds (1 oder 2 Byte, wie in den Berichten der Netzwerkmodule benutzt).

## Paketbau, Lesen und Verschlüsselung

`MakePacket` (`0x004EA2D0`, 914 Byte, 301 Aufrufer) baut aus den übergebenen Werten ein Paket nach der Beschreibung; `GetField` (`0x004EA000`, 672 Byte, 181 Aufrufer) liest ein Paket in die übergebenen Zeiger zurück. `SetCID` (`0x004EA2A0`) schreibt eine Kennung in einen Paketkopf (mindestens 7 Byte). `SetDummy` (`0x004EA6B0`) legt einen Zeitwert (`GetTickCount`) ab Byte 9 ab.
`GetCryptManager` (`0x004EA6D0`, 22 Aufrufer) liefert den einzigen `AuCryptManager`. `EncryptPacket` (`0x004EA730`, 277 Byte) verschlüsselt ein Paket nur, wenn die Verschlüsselung eingeschaltet ist (`CryptManager+4`) und es nicht schon einen Rahmen trägt (Anfangsbyte `0xA1`/`0xB1` mit Endbyte `0xAF`/`0xBF`): Ausgabegröße über `AuCryptManager::GetOutputSize`, Puffer aus dem Ringpuffer (`AuCircularBuffer::Alloc`), dann `AuCryptManager::Encrypt`; vorn Rahmenbyte und Länge, hinten das Endbyte. `DecryptPacket` (`0x004EA850`, 330 Byte) ist die Umkehrung; bei fehlendem Pufferplatz schreibt es „AuPacket::DecryptPacket … Alloc fail“ in `LOG\\CircularBuffer.log`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind Konstruktor, `SetFieldType`, `SetFlagLength`, `GetFlagLength`, `SetCID` (Anfang), `EncryptPacket` und `DecryptPacket` (Köpfe); `MakePacket` und `GetField` sind über Größe, Aufrufzahl (301 bzw. 181) und die Verwendung in den Netzwerkmodulen zugeordnet, nicht Zeile für Zeile verglichen. Die Rahmenbytes sind aus den Vergleichswerten im Dekompilat gelesen (−0x5F = 0xA1, −0x51 = 0xAF, −0x4F = 0xB1, −0x41 = 0xBF).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht als eigene Funktion: 1, nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->
