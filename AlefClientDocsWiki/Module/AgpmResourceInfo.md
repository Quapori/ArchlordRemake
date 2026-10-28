# AgpmResourceInfo (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmResourceInfo` (Ressourcenversion, Erkennung des lokalen Servers) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/APublic/AgpmResourceInfo/AgpmResourceInfo.cpp`/`.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 4 von 5 Quellmethoden sind zugeordnet (`GetMajorVersion`, `GetMinorVersion`, `SetMajorVersion`, `SetMinorVersion`). `CheckValidVersion` ist nicht im Client-Binary: ihr einziger Aufrufer sitzt im Server (`AgsmLoginClient`).
- **Version im Client:** Der Konstruktor setzt Hauptversion 0 und Nebenversion 1 (Konstanten `AGPMRESOURCE_MAJOR_VERSION`/`…MINOR_VERSION` der Quelle); die Werte stimmen mit der Quelle überein.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmResourceInfo.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetMajorVersion` | `0x00568290` | 7 | von Hand geprüft |
| 1 | `GetMinorVersion` | `0x005682A0` | 7 | von Hand geprüft |
| 2 | `SetMajorVersion` | `0x005682B0` | 13 | von Hand geprüft |
| 3 | `SetMinorVersion` | `0x005682C0` | 13 | von Hand geprüft |
| 4 | `CheckValidVersion` | – | | nicht im Client-Binary: einziger Aufrufer in der Quelle ist der Server (`AgsmLoginClient.cpp`) |

4 von 5 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgpmResourceInfo` (`0x00568210`), `scalar_deleting_dtor` (`0x005682D0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB84` | ``m_lMajorVersion` (Konstruktor setzt 0)` | Konstruktor, `GetMajorVersion`, `SetMajorVersion` |
| `this+0xB88` | ``m_lMinorVersion` (Konstruktor setzt 1)` | Konstruktor, `GetMinorVersion`, `SetMinorVersion` |
| `0x0099F4F8` | `globales Flag `g_lLocalServer`` | Konstruktor |

## Aufbau

Vtable `0x008B821C`: Slot 0 Löschwrapper (`0x005682D0`), Slot 1 und 2 der gemeinsame Rumpf `0x0067AC90`. Konstruktor `0x00568210` (117 Byte): ruft den `ApModule`-Konstruktor (`0x004E4700`), trägt den Modulnamen `AgpmResourceInfo` ein (`strncpy` mit höchstens 39 Zeichen), setzt die Hauptversion `m_lMajorVersion` (`this+0xB84`) auf 0 und die Nebenversion `m_lMinorVersion` (`this+0xB88`) auf 1 und setzt das globale Flag für den lokalen Server (`0x0099F4F8`) auf 1, wenn die Datei `LocalServer.txt` vorhanden ist (`_access(…, 0) == 0`).

## Zugriffe

`GetMajorVersion` (`0x00568290`) und `GetMinorVersion` (`0x005682A0`) sind je 7 Byte und lesen `this+0xB84` bzw. `+0xB88`; beide werden von `0x0065D100` (269 Byte) gerufen: diese Funktion baut ein Teilpaket mit Haupt- und Nebenversion (nur wenn `this+0xBA8` gesetzt ist) und verpackt es in ein Paket vom Typ `0x0D` (`AGPMLOGIN_PACKET_TYPE`, Operation 0); Aufrufer sind `0x00681620` und `0x006817F0`. Ist das Feld bei `this+0xBA8` nicht gesetzt, bleiben beide Versionen 0. `SetMajorVersion` (`0x005682B0`) und `SetMinorVersion` (`0x005682C0`) sind je 13 Byte und schreiben die Felder; im Client hat keine der beiden einen Aufrufer.
`CheckValidVersion` (Vergleich mit der Client-Version, Meldung „Checked Client Version“) ist nur im Server aufgerufen (`AgsmLoginClient.cpp`, Zeile 425) und fehlt im Client-Binary.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass das Flag bei `0x0099F4F8` `g_lLocalServer` ist, folgt aus der Verwendung im Konstruktor (gesetzt, wenn `LocalServer.txt` vorhanden ist); die Auswertung des Flags im Client wurde nicht verfolgt.
- Die Funktion `0x0065D100` ist nicht benannt (vermutlich Teil des Login-Moduls); was `this+0xBA8` ist und wann es gesetzt wird, wurde nicht verfolgt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgpmLogin`](AgpmLogin.md)
