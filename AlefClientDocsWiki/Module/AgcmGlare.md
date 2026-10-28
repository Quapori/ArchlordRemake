# AgcmGlare (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmGlare` (Blendeffekt nach dem Rendern, Unschärfe-Pixelshader) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph, Zeichenketten, EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** alle vier Methoden zugeordnet (`OnAddModule`, `OnInit`, `OnDestroy`, `CBPostRender`).
- **OnAddModule** (`0x00692D00`) holt [`AgcmRender`](AgcmRender.md), liest die Kamera und meldet `CBPostRender` (`0x006929E0`) an; **OnInit** (`0x00692930`) legt bei aktivem Blendeffekt zwei Kamera-Texturen in Bildschirmgröße an (`RwRasterCreate` × 2) und öffnet den Pixelshader (`AcuBlur::PShaderOpen`); **OnDestroy** (`0x00692990`) gibt beide Rasterbilder frei und schließt den Shader.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmGlare.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00692D00` | 69 | vtable/String |
| 1 | `OnInit` | `0x00692930` | 96 | vtable/String |
| 2 | `OnDestroy` | `0x00692990` | 68 | vtable/String |
| 3 | `CBPostRender` | `0x006929E0` | 756 | Callback-Registrierung |

4 von 4 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmGlare` (`0x00692830`), `ctor_or_dtor` (`0x006928D0`), `~AgcmGlare` (`0x00692CE0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98` | `Kamera` | `OnAddModule` |
| `this+0xB9C` | `Zeiger auf `AgcmRender`` | `OnAddModule` |

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `CBPostRender` (`0x006929E0`) war schon über die Anmeldung in `OnAddModule` benannt und wurde hier nicht Zeile für Zeile mit der Quelle verglichen.
- Die Klasse `AcuBlur` aus `AcuBlur.cpp` ist nicht abgeglichen.

## Querverweise

- **Erwähnt Module:** [`AgcmRender`](AgcmRender.md)
