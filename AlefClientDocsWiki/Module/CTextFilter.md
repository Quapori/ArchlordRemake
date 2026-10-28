# CTextFilter (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Klassenanalyse `CTextFilter` (Wortfilter für Chat-Eingaben) aus dem Quellverzeichnis `Modules/AClient/AgcmUIChatting2/` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und Aufrufer-Beziehungen, EP8-Quelle `CTextFilter.cpp` (Datei `CTextFilter.cpp`). Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 4 von 7 Quellmethoden sind zugeordnet; neu sind `OnFiltering`, `OnLoadFilterFile` und `_LoadCustomFilterFile`.
- **Flüstern:** der Filter überspringt `/w <Name> ` und prüft nur den Text, wie in der Quelle.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`CTextFilter.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnLoadFilterFile` | `0x00609B40` | 342 | ver |
| 1 | `OnAddFilter` | `0x006096E0` | 579 | Zeichenkette |
| 2 | `OnRemoveFilter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 3 | `OnClearFilter` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 4 | `OnSaveFilterFileCustom` | – | | nicht zugeordnet (klein, eingebaut oder ohne eindeutigen Anker) |
| 5 | `OnFiltering` | `0x00609070` | 900 | ver |
| 6 | `_LoadCustomFilterFile` | `0x00609980` | 304 | ver |

4 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00609650` (`0x00609650`), `ctor_or_dtor_00609ac0` (`0x00609AC0`), `~CTextFilter` (`0x00609B20`).

## Umfang

`CTextFilter` (`CTextFilter.cpp`, 7 Methoden) ersetzt Schimpfwörter in Chat-Eingaben. Im Binary bei `0x00609054`–`0x00609F30`, durchsetzt mit STL-Hilfen der beiden Filter-Maps.

## Filtern (OnFiltering, 0x00609070)

Wird vom Chat vor dem Senden aufgerufen ([`AgcmUIChatting2`](AgcmUIChatting2.md):OnSendMessage`, `CBClickSyncPosBtn`, `CBClickEscapeConfirmOk`). Ein führendes `/` wird übersprungen; beginnt der Befehl mit `w` oder `W` (Flüstern), werden zwei Leerzeichen übersprungen, damit nur der Text geprüft wird. Danach wird der Text in Kleinbuchstaben mit allen Filterwörtern verglichen; Treffer werden durch zufällige Zeichen aus einer Vier-Zeichen-Tabelle (`m_strBlindText`, in der Quelle `@`, `#`, …) ersetzt. Das entspricht der Quelle.

## Laden

`OnLoadFilterFile` (`0x00609B40`) liest verschlüsselte Excel-Textdateien (`AuExcelTxtLib`) und fügt jedes Wort über `OnAddFilter` (`0x006096E0`) ein; unverschlüsselte Dateien liest `_LoadCustomFilterFile` (`0x00609980`) zeilenweise (Puffer von 256 Byte je Wort).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Abschnitten (Kopf von `OnFiltering`).

## Grenzen

- Von `OnFiltering` wurde nur der Anfang (Behandlung von `/` und `w`) im Dekompilat mit der Quelle verglichen, nicht die Schleifen.
- `OnRemoveFilter`, `OnClearFilter` und `OnSaveFilterFileCustom` sind nicht zugeordnet. Für `OnRemoveFilter` und `OnSaveFilterFileCustom` gibt es keine Aufrufer im Binary; sie sind vermutlich vom Linker entfernt. `OnClearFilter` ist wahrscheinlich in den Destruktor eingebaut (`0x00609930` wird nur dort aufgerufen, ist aber nicht geprüft).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht im Client: 1, ohne Kandidat: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUIChatting2`](AgcmUIChatting2.md)
