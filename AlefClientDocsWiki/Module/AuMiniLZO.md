# AuMiniLZO (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuMiniLZO` (Kompression mit miniLZO) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Aufrufgraph, EP8-Quelle `Modules/AUtility/AuPacket/AuMiniLZO.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 0 von 2 Quellmethoden zugeordnet; nur Konstruktor und Destruktor sind belegt. **Nicht gefunden:** `Compress`, `DeCompress`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuMiniLZO.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Compress` | – | | nicht im Binary gefunden (nicht zugeordnet): keine Funktion mit Aufrufern, die ein `AuMiniLZO`-Objekt bearbeitet |
| 1 | `DeCompress` | – | | nicht im Binary gefunden (nicht zugeordnet): wie `Compress` |

0 von 2 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuMiniLZO` (`0x004F8A80`), `ctor_or_dtor_004f8ac0` (`0x004F8AC0`), `~AuMiniLZO` (`0x004F8AD0`).

## Funktionen

Vtable mit dem Löschwrapper `0x004F8AD0` (Konstruktorrumpf `0x004F8AC0` setzt nur die Vtable). Der Konstruktor `0x004F8A80` nullt zwei Arbeitspuffer (`0x10000` Byte ab `+4`, `0x2800` Byte ab `+0x10004`) und setzt die Größenangabe `+0x12804` auf `0x2800`. Die Zahl `0x4a01` Dwords entspricht dem Objektumfang bis `+0x12808`, wo `AuPacket` seine Beschreibung ablegt.
Die Kompressionsfunktionen aus `minilzo.c` (`lzo1x_1_compress`, `lzo1x_decompress`) sind im Bereich `0x004F8600`–`0x004F8A80` nur als viele kleine Sprungziele ohne Aufrufer (`ftable.py`) erkennbar und nicht benannt.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Dass `Compress`/`DeCompress` im Binary fehlen, ist nicht belegt: die Kompression wird im Client womöglich gar nicht aufgerufen (`AuPacket::EncryptPacket` ruft sie nicht), die Quellmethoden sind dann vom Linker entfernt. Ein Beweis (alle Aufrufer in Quelle und Binary) steht aus.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->
