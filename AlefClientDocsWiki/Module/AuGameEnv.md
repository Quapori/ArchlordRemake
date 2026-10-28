# AuGameEnv (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuGameEnv` (Startparameter „alpha“, „debugtest“, „admin“) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Zeichenketten, EP8-Quelle `Modules/AUtility/AuGameEnv/AuGameEnv.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** `InitEnvironment` ist zugeordnet (`0x008791F0`, 711 Byte); `CheckOption` ist dort dreimal eingebaut (je ein Vergleich mit „alpha“, „debugtest“, „admin“ über `FUN_0040AA90`). Eine frühere Zuordnung dieser Adresse an `CheckOption` war falsch und ist korrigiert.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuGameEnv.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `InitEnvironment` | `0x008791F0` | 711 | von Hand geprüft |
| 1 | `CheckOption` | – | | nicht im Binary gefunden; Verbleib offen |

1 von 2 Quellmethoden sind einer Binary-Adresse zugeordnet.

## InitEnvironment

Die Funktion legt einen Puffer von 2048 Byte an, kopiert `GetCommandLineA()`, wandelt in Kleinbuchstaben (`_strlwr_s`), liest die Wörter über einen `stringstream` und prüft nacheinander das zweite, dritte und vierte Wort gegen „alpha“, „debugtest“ und „admin“ (das erste Wort, der Programmname, wird verworfen). Die Schalter sind Bytes im Objekt (`+0` alpha, `+1` debugtest, `+2` admin).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Lage der Schalter im Objekt ist aus dem Dekompilat gelesen, nicht gegen Zugriffe in anderen Modulen geprüft; die Singleton-Funktion `GetGameEnv` ist nicht gesucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): nicht als eigene Funktion: 1, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `InitEnvironment` | 28 | `0x008791F0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->
