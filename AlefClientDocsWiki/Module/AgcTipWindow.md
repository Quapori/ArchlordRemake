# AgcTipWindow (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AgcTipWindow` (Tipp-Fenster mit wechselndem Ladebild, erbt von `AcUIBase`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Vtable, EP8-Quelle `Modules/AClient/AgcmUITips/AgcTipWindow.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 3 von 3 Quellmethoden sind zugeordnet (`OnInit` als gemeinsamer Rumpf), dazu Konstruktor und Destruktor.
- **Wechsel:** neues Bild alle 60 s oder wenn die Textur fehlt; `GetRandomTipImage` kommt aus [`AgcmUITips`](AgcmUITips.md).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcTipWindow.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `gemeinsamer return-TRUE-Rumpf` (vom Linker zusammengefaltet) |
| 1 | `OnWindowRender` | `0x0074FEC0` | 130 | vtable/String |
| 2 | `OnClose` | `0x0074FF50` | 11 | vtable/String |

3 von 3 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ctor_or_dtor_0074fe80` (`0x0074FE80`), `ctor_or_dtor_0074feb0` (`0x0074FEB0`), `~AgcTipWindow` (`0x0074FF60`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0x1D04` | `Zeiger auf `AgcmUITips`` | Konstruktor |
| `0x1D08` | `aktuelle Tipp-Textur (`m_pstTipTexture`)` | `OnWindowRender` |
| `0x1D0C` | `Zeit des letzten Wechsels (`m_ulPrevClockCount`)` | `OnWindowRender`, `OnClose` |

## Vtable

Vtable bei `0x008DF1CC` (Basis `AcUIBase`): Slot 0 Destruktor `0x0074FF60`, 1/2 `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`), 3 `OnClose` (`0x0074FF50`), 8 `OnWindowRender` (`0x0074FEC0`). Konstruktor `0x0074FE80` (ein Parameter: Zeiger auf `AgcmUITips`), Aufräum-Konstruktor `0x0074FEB0`.

## Darstellung (OnWindowRender)

Bei jedem Zeichnen wird die Uhr geholt; ist die aktuelle Textur aus der Textur-Liste verschwunden, werden Textur und Zeit auf 0 gesetzt. Nach **60 000 ms** (`AGC_TIP_DURATION`; im Binary als Vergleich `> 59999`) wird die Texturliste geleert, über `AgcmUITips::GetRandomTipImage` (`0x0061DB20`) ein neues Bild geholt und als Zeichentextur eingetragen; erst danach zeichnet die Basisklasse. `OnClose` setzt die Zeit auf 0, sodass beim nächsten Öffnen sofort ein neues Bild gewählt wird.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle.

## Grenzen

- Die Hilfsaufrufe der Textur-Liste (`DestroyTextureList`, `AddTexture`, `SetRednerTexture` in der Schreibweise der Quelle) wurden nur über die Aufrufreihenfolge zugeordnet und hier nicht benannt.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): gemeinsamer Rumpf: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmUITips`](AgcmUITips.md)
- **Erwähnt in:** [`AgcmUITips`](AgcmUITips.md)
