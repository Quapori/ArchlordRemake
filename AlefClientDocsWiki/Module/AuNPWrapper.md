# AuNPWrapper (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Klasse `AuNPWrapper` (Hülle um den Spielschutz nProtect GameGuard, aus `AuGameGuard/AuNPGameLib.cpp`; Basisklasse `AuNPBase`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable `AuNPBase`, Aufrufer (`WinMain`, `AgcmCharacter::CBGameguardAuth`), EP8-Quelle. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 4 von 7 Quellmethoden zugeordnet (`Send`, `Check`, `SetWndHandle`, `Auth`), dazu Konstruktor, Destruktor und die Zugriffsfunktion `GetNProtect` (`0x004EDFA0`).
- **Befund:** Der eigentliche Spielschutz ist im 2017er Client nicht gelinkt: `AuNPGameLib` (die Klasse, die `CNPGameLib` benutzt) kommt weder als Name noch als RTTI vor; die Vtable `AuNPBase` besteht nur aus Standardrümpfen (`return TRUE` `0x0067AC90`, leer `0x005BDCF0`, `return 0` `0x007AA0B0`). Damit liefert `Check` immer TRUE und `Auth`/`Send` tun nichts.
- **Nicht gefunden:** `Init`, `GetMessage`, `NPGameMonCallback` (je 7 Zeilen, in den Aufrufern eingebaut).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AuNPWrapper.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `Init` | – | | nicht im Binary gefunden; Verbleib offen (7-Zeilen-Weiterleitung, vermutlich eingebaut) |
| 1 | `Send` | `0x004EDF30` | 10 | von Hand geprüft |
| 2 | `GetMessage` | – | | nicht im Binary gefunden; Verbleib offen (7-Zeilen-Weiterleitung, vermutlich eingebaut) |
| 3 | `NPGameMonCallback` | – | | nicht im Binary gefunden; Verbleib offen (7-Zeilen-Weiterleitung, vermutlich eingebaut) |
| 4 | `Check` | `0x004EDF40` | 10 | von Hand geprüft |
| 5 | `SetWndHandle` | `0x004EDF50` | 10 | von Hand geprüft |
| 6 | `Auth` | `0x004EDF60` | 10 | von Hand geprüft |

4 von 7 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AuNPWrapper` (`0x004EDEC0`), `~AuNPWrapper` (`0x004EDF70`), `GetNProtect` (`0x004EDFA0`).

## Funktionen

`AuNPWrapper` hält einen Zeiger auf ein `AuNPBase`-Objekt bei `this+4` und ein Flag „initialisiert“ bei `+8`. Der Konstruktor (`0x004EDEC0`, Zeichenkette `NotCheckGameGuard.arc`) legt das Objekt an; wenn die Datei `NotCheckGameGuard.arc` vorhanden ist, wird der Schutz übersprungen. `GetNProtect` (`0x004EDFA0`, 5 Aufrufer) liefert die einzige Hülle. Die vier Weiterleitungen rufen je einen Vtable-Eintrag des Basisobjekts: `SetWndHandle` (`0x004EDF50`, Eintrag 2), `Auth` (`0x004EDF60`, Eintrag 3; aufgerufen von `AgcmCharacter::CBGameguardAuth` `0x00410C90`), `Check` (`0x004EDF40`, Eintrag 4; `WinMain` prüft damit in jedem Schleifendurchlauf und fordert bei 0 das Beenden an) und `Send` (`0x004EDF30`, Eintrag 5). Die Reihenfolge der Einträge folgt der Kopfdatei (`Init`, `SetWndHandle`, `Auth`, `Check`, `Send`, `GetInfo`, `GetMessage`, `NPGameMonCallback`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind die vier Weiterleitungen im Disassembly (Vtable-Versätze `0x8`, `0xC`, `0x10`, `0x14`) und `GetNProtect` im Kopf. Dass der Schutz nicht gelinkt ist, folgt aus dem Fehlen von `AuNPGameLib` und `CNPGameLib` (Name und RTTI) und den Standardrümpfen in der Vtable; ob zur Laufzeit ein anderes Modul `AuNPBase` ersetzt, wurde nicht geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->
