# AuGenerateID (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Hilfsklasse `AuGenerateID` (Erzeugung eindeutiger Kennungen mit Server-Bits und Rückgabeliste) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat/Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable, Aufrufgraph, EP8-Quelle `Modules/AUtility/AuGenerateID/AuGenerateID.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 3 von 4 Quellmethoden zugeordnet (`Initialize`, `GetID`, `AddRemoveID`), dazu Konstruktor und Destruktorrumpf.
- **Nicht gefunden:** `GetCurrentID`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuGenerateID.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Initialize` | `0x00878810` | 279 | von Hand geprüft |
| 1 | `GetID` | `0x00878930` | 122 | von Hand geprüft |
| 2 | `GetCurrentID` | – | | nicht im Binary gefunden: kleine Funktion, vermutlich in die Aufrufer eingebaut oder vom Linker entfernt; Verbleib offen |
| 3 | `AddRemoveID` | `0x00878AA0` | 300 | von Hand geprüft |

3 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AuGenerateID_body` (`0x00878790`), `AuGenerateID` (`0x008789F0`), `~AuGenerateID` (`0x00878A80`).

## Funktionen

Der Konstruktor `0x008789F0` richtet die kritische Sektion (`this+0x10`, Flag `+0x28`) ein, nullt die Felder und baut zwei Puffer (je `0x14` Byte, ab `+0x50`) auf; danach ruft er `Initialize(1, 0, 0, 0, 0)`. Der Destruktorrumpf `0x00878790` gibt den Puffer (`+0x44`) und die Sektion frei.
`Initialize` (`0x00878810`, 279 Byte) bildet aus Anfangswert, Serverkennung und Anzahl der Bits den Wertebereich: Basis `Server << (31 − Bits)` (`+4`), aktueller Wert `+0xC` und Untergrenze `+0x2C` als Basis ODER Anfangswert, Obergrenze `+0x30` als `((Server + 1) << (31 − Bits)) − 1`; die Liste der zurückgegebenen Kennungen (`+0x4C`) wird geleert. `GetID` (`0x00878930`) holt unter der Sperre zuerst eine zurückgegebene Kennung (`0x00878690`), sonst zählt es `+0xC` hoch; `AddRemoveID` (`0x00878AA0`) nimmt eine Kennung zurück, wenn sie im gültigen Bereich liegt (Prüfung gegen `+0x2C`/`+0x30`), und legt sie in die Rückgabeliste (`0x008789B0`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `Initialize`, `GetID` und die Anfänge von `AddRemoveID` im Dekompilat; die Rückgabeliste (Hilfsfunktionen `0x00878700`/`0x00878760`/`0x008789B0`) ist aus der Form geschlossen, nicht mit der Quelle Zeile für Zeile verglichen. `GetCurrentID` (9 Zeilen) ist vermutlich eingebaut.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->
