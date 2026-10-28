# CBGMTitleViewer (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `CBGMTitleViewer` (Anzeige des Hintergrundmusik-Titels) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `CBGMTitleViewer.cpp` (Datei `CBGMTitleViewer.cpp`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 8 von 9 Quellmethoden sind zugeordnet; neu sind die Titelsuche, die Aktualisierung und beide Eintragsfunktionen.
- **Titelliste:** 29 feste Einträge, gleich wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CBGMTitleViewer.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnReadyBGMTitle` | `0x0070A9A0` | 1138 | Zeichenkette |
| 1 | `OnUpdateBGMTitle` | `0x0070A1A0` | 322 | ver |
| 2 | `GetBGMTitle` | `0x0070A000` | 211 | ver |
| 3 | `GetCurrentBGMTitle` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 4 | `_AddBGMTitle` | `0x0070A420` | 334 | ver |
| 5 | `_AddLoginBGMTitle` | `0x0070A570` | 334 | ver |
| 6 | `CallBack_DisplayBGMTitle` | `0x0070A0E0` | 185 | UI-Registrierung |
| 7 | `CallBack_UpdateBGMTitle` | `0x0070A2F0` | 49 | ver |
| 8 | `ReadXMLData` | `0x0070A6C0` | 311 | Zeichenkette |

8 von 9 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0070a880` (`0x0070A880`), `ctor_or_dtor_0070a930` (`0x0070A930`), `~CBGMTitleViewer` (`0x0070AE20`).

## Umfang

`CBGMTitleViewer` (`CBGMTitleViewer.cpp`, 9 Methoden) zeigt den Titel der laufenden Hintergrundmusik. Im Binary bei `0x0070A000`–`0x0070AE40`.

## Titelliste (OnReadyBGMTitle, 0x0070A9A0)

Die Funktion registriert den Benutzerdatensatz `Chat_BGMTitle`, den Anzeige-Callback und den BGM-Wechsel-Callback ([`AgcmEventNature`](AgcmEventNature.md):SetCallbackBGMUpdate`) und trägt **29** feste Titel ein (Aufrufe von `_AddBGMTitle`, `0x0070A420`), beginnend mit `MT_001.MP3`, `HTT_001.MP3`, `HTT_002.MP3`. Die Zahl entspricht der Quelle (29 Zeilen). `ReadXMLData` (`0x0070A6C0`) liest zusätzlich Titel der Anmeldemusik über `_AddLoginBGMTitle` (`0x0070A570`).

## Anzeige

`GetBGMTitle` (`0x0070A000`) sucht erst in der Spiel-, dann in der Anmelde-Map. `OnUpdateBGMTitle` (`0x0070A1A0`) bricht ab, wenn die Hintergrundmusik stummgeschaltet ist, merkt den Dateinamen und zeigt `BGM : <Titel>`; nur im Dienstgebiet Korea (0) steht ein anderes Präfix, wie in der Quelle. `CallBack_DisplayBGMTitle` (`0x0070A0E0`) setzt denselben Text in ein Eingabefeld. `CallBack_UpdateBGMTitle` (`0x0070A2F0`) ruft `OnUpdateBGMTitle`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `GetCurrentBGMTitle` (4 Zeilen) ist im Binary nicht als eigene Funktion zu finden (eingebaut).
- Die Dateinamen der Titelliste wurden nur gezählt, nicht einzeln verglichen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEventNature`](AgcmEventNature.md), [`AgcmUIChatting2`](AgcmUIChatting2.md)
