# AuInputComposer (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuInputComposer` (IME-Eingabe: Zusammensetzung, Lesefenster, Kandidatenliste; abgeleitet von `CImmLib`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Funktionsübersicht (`fcalls.py`), Zeichenketten (`TINTLGNT.IME`, `CINTLGNT.IME`, `MSTCIPHA.IME`, `Keyboard Mapping`), Aufrufer `MainWndProc`, EP8-Quelle `AgcSkeleton/AuInputComposer.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 7 von 25 Quellmethoden zugeordnet (`GetInstance`, `InitInputComposer`, `OnInputLanguageChange`, `GetReadingWindowOrientation`, `GetImeId`, `GetCharsetFromLang`, `GetCodePageFromCharset`), dazu Konstruktor und Destruktor; `GetCodePageFromLang` (4 Zeilen) ist eingebaut.
- **Nicht gefunden:** `OnComposition`, `OnEndComposition`, `OnNotify`, `OnChar`, die `Get…`-Abfragen für Text und Kandidaten, `CheckToggleState`, `GetPrivateReadingString` (vermutlich `0x00732AE0`, 414 Byte, nicht gesichert) und die Umschalter `ToAlphaNumeric`/`ToNative`.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuInputComposer.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetInstance` | `0x00733550` | 90 | von Hand geprüft |
| 1 | `InitInputComposer` | `0x00732600` | 11 | von Hand geprüft |
| 2 | `OnInputLanguageChange` | `0x00732F50` | 116 | von Hand geprüft |
| 3 | `OnComposition` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 4 | `OnEndComposition` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 5 | `OnNotify` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 6 | `OnChar` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 7 | `GetInput` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 8 | `GetComp` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 9 | `GetReading` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 10 | `GetCandidate` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 11 | `GetCandidateCount` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 12 | `GetCandidateSelection` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 13 | `GetCandidatePageSize` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 14 | `GetCandidatePageStart` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 15 | `GetNextChar` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 16 | `GetReadingWindowOrientation` | `0x00732790` | 322 | Zeichenkette |
| 17 | `GetPrivateReadingString` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 18 | `GetImeId` | `0x007328E0` | 502 | von Hand geprüft |
| 19 | `CheckToggleState` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 20 | `GetCharsetFromLang` | `0x00732C80` | 149 | von Hand geprüft |
| 21 | `GetCodePageFromCharset` | `0x00732D80` | 122 | von Hand geprüft |
| 22 | `GetCodePageFromLang` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 23 | `ToAlphaNumeric` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |
| 24 | `ToNative` | – | | nicht im Binary eindeutig bestimmt; Verbleib offen (IME-Behandlung der Quelle, vermutlich eingebaut oder nicht zugeordnet) |

7 von 25 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_00733220` (`0x00733220`), `ctor_or_dtor_00733320` (`0x00733320`), `~AuInputComposer` (`0x00733530`).

## Funktionen

Vtable mit dem Löschwrapper `0x00733530`; Konstruktorrümpfe `0x00733220` (ruft den von `CImmLib`) und `0x00733320` (Destruktorrumpf). `GetInstance` (`0x00733550`, 15 Aufrufer) liefert die einzige Instanz. `InitInputComposer` (`0x00732600`) ruft `CImmLib::Init`; aufgerufen wird es von `MainWndProc` bei `WM_CREATE`, danach `OnInputLanguageChange` (`0x00732F50`) mit der Tastaturbelegung: es merkt Sprache und Zeichensatz (`GetCharsetFromLang` `0x00732C80`, `GetCodePageFromCharset` `0x00732D80`), setzt die IME-Kennung (`GetImeId` `0x007328E0`: vergleicht die Belegung mit den chinesischen und taiwanischen IME-Dateien `TINTLGNT.IME`, `CINTLGNT.IME`, `MSTCIPHA.IME`) und ruft `SetupImeApi`. `GetReadingWindowOrientation` (`0x00732790`, 322 Byte) liest aus der Registry (Schlüssel `Keyboard Mapping`, IME-Namen `MSTCIPH`, `TINTLGNT`), ob das Lesefenster senkrecht ist.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `OnInputLanguageChange` und der Kopf von `GetImeId`; die übrigen Zuordnungen folgen aus Zeichenketten und Aufrufbeziehungen (`GetCharsetFromLang`/`GetCodePageFromCharset` als Argumentkette in `OnInputLanguageChange`).

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 4, nicht im Client: 5, ohne Kandidat: 9.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcSkeleton`](AgcSkeleton.md)
