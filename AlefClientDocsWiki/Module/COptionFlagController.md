# COptionFlagController (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `COptionFlagController` (Ablehn-Optionen im Chat) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `COptionFlagController.cpp` (Datei `COptionFlagController.cpp`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 3 von 6 Quellmethoden sind zugeordnet.
- **Optionen:** sieben Meldungspaare, wie in der Quelle.
- **Nicht vorhanden:** `OnChangeOptionFlag` wird in der EP8-Quelle nirgends aufgerufen; `_CheckOptionFlag` und `_SendMsgChangeOptionFlag` werden nur von ihm benutzt. Im Binary sind keine Aufrufer gefunden, die Funktionen sind vermutlich entfernt.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`COptionFlagController.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInitOptionFlagController` | `0x0070C5C0` | 214 | Zeichenkette |
| 1 | `OnChangeOptionFlag` | – | | nicht zugeordnet (vermutlich vom Linker entfernt: ohne Aufrufer) |
| 2 | `OnRequestChangeOptionFlag` | `0x0070BDC0` | 135 | ver |
| 3 | `_AddOptionFlagMsg` | `0x0070C3B0` | 475 | ver |
| 4 | `_CheckOptionFlag` | – | | nicht zugeordnet (vermutlich vom Linker entfernt: ohne Aufrufer) |
| 5 | `_SendMsgChangeOptionFlag` | – | | nicht zugeordnet (vermutlich vom Linker entfernt: ohne Aufrufer) |

3 von 6 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0070c350` (`0x0070C350`), `ctor_or_dtor_0070c3a0` (`0x0070C3A0`), `~COptionFlagController` (`0x0070C590`).

## Umfang

`COptionFlagController` (`COptionFlagController.cpp`, 6 Methoden) meldet Änderungen der Ablehn-Optionen im Chat. Im Binary bei `0x0070C350`–`0x0070C5C0`, davor die Map-Hilfen für `m_mapOptionFlagMsg`.

## Meldungen je Option (OnInitOptionFlagController, 0x0070C5C0)

Sieben Aufrufe von `_AddOptionFlagMsg` (`0x0070C3B0`), jeweils mit UI-Text für „aus“/„an“ und den Farben `Negative_Text_Color`/`Positive_Text_Color`: Handel, Gruppe, Gilde, Gildenkampf, Kampf, Gildenbeziehung, Freunde. Reihenfolge und Zahl stimmen mit der Quelle überein (7 Aufrufe im Binary).

## Änderung anfordern

`OnRequestChangeOptionFlag` (`0x0070BDC0`) holt [`AgpmCharacter`](AgpmCharacter.md) und `AgcmCharacter`, setzt oder löscht das Bit am Self-Character (`SetOptionFlag` `0x00504C00` / `UnsetOptionFlag` `0x00504C20`) und sendet das Ergebnis (`SendPacketOptionFlag`, `0x005A2170`). Aufrufer sind die Chat-Befehle `RejectTradeOn/Off` usw. (`CChatCmd`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Das Entfernen der drei nicht zugeordneten Funktionen ist aus fehlenden Aufrufern geschlossen, nicht anders belegt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIChatting2`](AgcmUIChatting2.md), [`AgpmCharacter`](AgpmCharacter.md)
