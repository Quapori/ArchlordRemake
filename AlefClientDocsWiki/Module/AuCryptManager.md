# AuCryptManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuCryptManager` (Verwaltung der Verschlüsselungsverfahren) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/AUtility/AuCrypt/AuCryptManager.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 10 von 31 Quellmethoden zugeordnet, die übrigen sind kleine Weiterleitungen oder Server-Teile. **Nicht gefunden:** `SetAlgorithm`, die Zeichenkettenfunktionen, `IsPublicCopy`/`IsPrivateCopy`, `MakeRandomKey`, `InitializeActor` (beide), `InitializeActorPublic`/`Private` mit Quelle, `Encrypt`/`Decrypt` mit Schlüssel, `DecryptByPublic`/`EncryptByPrivate`/`DecryptByPrivate`, `IsUseDynCode`, `InitServer`, `GetClientDynCode*`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuCryptManager.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `SetAlgorithm` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 1 | `GetPublicAlgorithmString` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 2 | `GetPrivateAlgorithmString` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 3 | `GetAlgorithmString` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 4 | `IsPublicClone` | `0x004F8D40` | 10 | von Hand geprüft |
| 5 | `IsPrivateClone` | `0x004F8D50` | 10 | von Hand geprüft |
| 6 | `IsPublicCopy` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 7 | `IsPrivateCopy` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 8 | `UseDecryptBuffer` | `0x004F8D60` | 39 | von Hand geprüft |
| 9 | `MakeRandomKey` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 10 | `InitializeActor` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 11 | `InitializeActorPublic` | `0x004F8ED0` | 105 | von Hand geprüft |
| 12 | `InitializeActorPrivate` | `0x004F8F40` | 105 | von Hand geprüft |
| 13 | `InitializeActor` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 14 | `InitializeActorPublic` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 15 | `InitializeActorPrivate` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 16 | `InitializeCTX` | `0x004F8D90` | 304 | von Hand geprüft |
| 17 | `Encrypt` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 18 | `Decrypt` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 19 | `Encrypt` | `0x004F9090` | 113 | von Hand geprüft |
| 20 | `Decrypt` | `0x004F9110` | 125 | von Hand geprüft |
| 21 | `EncryptByPublic` | `0x004F8FB0` | 63 | von Hand geprüft |
| 22 | `DecryptByPublic` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 23 | `EncryptByPrivate` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 24 | `DecryptByPrivate` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 25 | `GetOutputSize` | `0x004F8FF0` | 56 | von Hand geprüft |
| 26 | `IsUseDynCode` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 27 | `InitServer` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 28 | `GetClientDynCode` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 29 | `GetClientDynCodePublic` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |
| 30 | `GetClientDynCodePrivate` | – | | nicht im Binary gefunden; Verbleib offen (kleine Weiterleitung, Server-Teil oder eingebaut) |

10 von 31 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuCryptManager` (`0x004F9270`), `~AuCryptManager_body` (`0x004F9440`), `~AuCryptManager` (`0x004F94F0`).

## Funktionen

Vtable mit dem Löschwrapper `0x004F94F0`; Konstruktor `0x004F9270` (337 Byte, legt die Tabelle der Verfahren an, `this+0xC` ist der Vektor der Verfahrensobjekte, `+0x18` Nummer des öffentlichen und `+0x1C` des privaten Verfahrens), Destruktorrumpf `0x004F9440`. Die Verfahrensnummern: 1 = Klon, 3 = Kopie (`IsPublicClone` `0x004F8D40`, `IsPrivateClone` `0x004F8D50`, `UseDecryptBuffer` `0x004F8D60`).
`InitializeCTX` (`0x004F8D90`, 320 Byte) legt den Schlüsselkontext einer Zelle an; `InitializeActorPublic` (`0x004F8ED0`) und `InitializeActorPrivate` (`0x004F8F40`) rufen die Initialisierung des öffentlichen bzw. privaten Verfahrens (Vtable-Eintrag 2 des Verfahrens) mit dem Schlüssel; `EncryptByPublic` (`0x004F8FB0`) ruft Eintrag 3; `GetOutputSize` (`0x004F8FF0`) Eintrag 5; `Encrypt` (`0x004F9090`) und `Decrypt` (`0x004F9110`) mit Verfahrensart werden von `AuPacket::EncryptPacket`/`DecryptPacket` gerufen.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `IsPublicClone`/`IsPrivateClone`, `UseDecryptBuffer`, `InitializeActorPublic`/`Private`, `EncryptByPublic` (Form) und `GetOutputSize`; `Encrypt`/`Decrypt` sind über den Aufruf aus `AuPacket` zugeordnet. Die Zuordnung der Vtable-Einträge zu Verfahrensfunktionen ist aus der Form geschlossen. Das Verfahren selbst (`AuCryptAlgorithmBase`-Klassen: Blowfish, MD5MAC, Rijndael, Seed) wurde hier nicht untersucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 9, ohne Kandidat: 12.

<!-- LUECKENREGISTER-NACHTRAG-END -->
