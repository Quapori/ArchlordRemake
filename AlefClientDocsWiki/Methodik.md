# Methodik: Binary ↔ EP8-Quelle

*Navigation: [Wiki-Start](README.md) · [Glossar](Glossar.md) · [Funktionskarte](Uebersichten/Funktionskarte.md)*

Der 2017er Build hat keine PDB; alle Funktionen heißen zunächst `FUN_xxxxxxxx`. Die Namen in den Berichten stammen aus dem Abgleich mit der EP8-C++-Quelle. Dieser Abgleich ist mehrstufig, jede Zuordnung trägt in den Berichten ihren **Beleg**.

## Werkzeuge und Daten

- **Ghidra 12.1.x (Headless)** liefert Dekompilat, Funktionsgrößen, Aufrufgraph, Zeichenketten, Vtables und RTTI.
- **Skripte** (nicht Teil dieses Wikis): Exportskripte (Java für Ghidra), Abgleichskripte (Python) und Berichtsgeneratoren. Sie werden unten nur beim Namen genannt, damit die Arbeitsschritte nachvollziehbar sind.
- **Rohdaten** in `rea_export/` (nicht Teil dieses Wikis): `all_named.c` (benanntes Dekompilat), `fncalls.json` (Aufrufgraph; Schlüssel = Adresse ohne führende Nullen, `c` = Callees), `functions.tsv`, `vtables.tsv`, `names_allN.tsv` (jeweils neuester Namensstand), `tu_<Modul>.json` (Quellmethoden gegen Adressbereich), `gm_<Modul>.tsv` (Namensvorschläge je Modul), `extras_<Modul>.json` (Handtext je Bericht).

## Zuordnungsmethoden (nach Stärke des Belegs)

1. **Fehlerzeichenketten**: Strings wie `AgpmCharacter::OnReceive() Error (33)` nennen Klasse und Methode. Nur wenige Funktionen, weil der Release-Build Funktionsnamen entfernt.
2. **RTTI/Vtables**: Ghidra erkennt die Vtables; aus den EP8-Headern wird die Slot-Reihenfolge berechnet (Basisklasse zuerst, Überschreibungen am selben Slot, neue virtuelle Methoden angehängt) und je Slot zugeordnet. Bei vielen Modulen: Slot 2 = `OnInit`, 3 = `OnIdle`, 7 = `OnDestroy`.
3. **Callback- und UI-Registrierungen**: `SetCallback…(CBxxx, this)` und `AddFunction/AddDisplay/AddUserData(this, "Name", CB…)` haben in Quelle und Binary dieselbe Reihenfolge und denselben Namen als Zeichenkette → eindeutig.
4. **Zeichenketten und Konstanten** (`strmatch.py`, `scorematch.py`): ein Literal, das in genau einer Quellmethode und einer Binary-Funktion vorkommt, bindet beide; Konstanten (z. B. 0x66 = 0,4 × 255) ebenso.
5. **Operationsbytes** in `Make…`/`Send…`-Funktionen (Paketaufbau) und `OnReceive`-Switches (`casemap.py`).
6. **Aufrufgraph** (`graphmatch.py`): bekannte Namen als Anker; eindeutige Aufruf-/Aufrufer-Beziehungen und gegenseitige Aufrufe (z. B. `OnLButtonDblClk` → `OnLButtonDown`).
7. **Quellreihenfolge und Größenverhältnis** (`tuscan.py`, `tualign.py`): innerhalb einer Übersetzungseinheit liegen Funktionen oft in Quellreihenfolge; Quellzeilen ↔ Bytes liefert eine grobe Plausibilität. Das ist der schwächste Beleg und wird in den Berichten ausdrücklich als „nicht Zeile für Zeile verglichen“ geführt.
8. **Von Hand geprüft**: Dekompilat und Quelle werden gelesen und verglichen; so gekennzeichnete Namen („von Hand geprüft“) sind die belastbarsten.

Ein Bericht nennt immer: was zugeordnet ist, den Beleg je Funktion, **Abweichungen** zwischen Quelle und Binary und die **Grenzen** (was nur über Struktur/Größe zugeordnet ist).

## Typische Stolpersteine

- **Identical COMDAT Folding (ICF)**: gleiche Funktionsrümpfe verschiedener Klassen sind zu einer Adresse verschmolzen (z. B. `0x0067AC90` = `return TRUE`, `0x0067FAB0` = gemeinsamer `OnIdle`-Rumpf, `0x005BDCF0` = leerer Rumpf). `SetCallback…`-Einzeiler und leere Rückrufe sind deshalb nicht einzeln zuordenbar; Aufrufer solcher Funktionen werden nicht benannt.
- **Callee-Listen sind nach Adresse sortiert**, nicht nach Aufrufreihenfolge; die Reihenfolge muss im Dekompilat nachgelesen werden.
- **Ghidra-Lücken**: Codeadressen, die Ghidra nicht als Funktion angelegt hat (Zeiger-Ziele, `&LAB_…`), wurden nachträglich angelegt; einzelne Bereiche fehlen trotzdem im Export (z. B. in `AgcmCashMall` bei `0x006E38CC–0x006E3970`).
- **Falsche Altnamen** (`ctor_or_dtor`, `CCSLog::…`) immer am Aufrufkontext gegenprüfen; mehrfach waren sie falsch.
- **Eingebaute (inline) Funktionen** und vom Linker entfernte Editor-/Debug-/Regionscode-Funktionen fehlen im Binary; Berichte führen sie mit Begründung („nicht im Binary“, „Werkzeugcode“, „Regionscode“, „eingebaut“).
- **Modul-Zeiger**: Aus `GetModule("Name")`-Zuweisungen in `OnAddModule` ergeben sich Member-Offsets (siehe [Member-Offsets](Uebersichten/Member-Offsets.md)).

## Ablauf je Modul

1. Quellmethoden und Binary-Adressbereich ermitteln (`tuscan.py <Modul>` → `tu_<Modul>.json`).
2. Funktionen lesen (`showfn.py <Adresse>`), Anker und Belege sammeln.
3. Namen in `gm_<Modul>.tsv` eintragen und mit `applygm.py` in die nächste `names_allN.tsv` übernehmen.
4. Handtext in `extras_<Modul>.py` schreiben → `rea_export/extras_<Modul>.json`.
5. Bericht erzeugen (`mkreport_ui.py <Modul> <extras.json>` bzw. die Paket-Berichtsgeneratoren).
6. [Funktionskarte](Uebersichten/Funktionskarte.md) ergänzen und die Modul-Übersicht neu erzeugen (`mkinventory.py`).
