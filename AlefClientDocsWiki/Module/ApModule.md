# ApModule (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Basisklasse `ApModule` (gemeinsame Verwaltung von Moduldaten, angehängten Daten, Rückrufen, Strom-Funktionen und Idle-Ereignissen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Disassembly (`x86dis.py`; die Funktionen liegen fast alle in Export-Lücken), Vtable `0x008AC94C`, Feldoffsets gegen die Reihenfolge der Mitglieder in `ApModule.h`, Aufrufgraph, Scan über das ganze `.text`, EP8-Quelle `Modules/APublic/ApModule/ApModule.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 37 von 56 Quellmethoden sind zugeordnet: 33 als eigene Funktion, `OnPreDestroy`/`OnDestroy` am gemeinsamen Rumpf `0x0067AC90` und `ReleaseCallBackDataList`/`ReleaseStreamDataList` eingebaut im Destruktor. Dazu kommen Konstruktor, Destruktorrumpf und `AddIdleEvent` (steht nur in der Kopfdatei).
- **Nicht im Binary:** `Idle3`, `RemoveIdleEvent`/`2`/`3`, `GetIdleEvent3`, `SetMaxIdleEvent`/`2`/`3`, `GetMaxIdleEvent`/`2`/`3`, `EnableIdle3`, `AddPreReceiveModule`, `GetPacketType`, `Receive` und die beiden statischen Hilfsfunktionen `m_fConstructorCB`/`m_fDestructorCB`. Das Feldscan-Ergebnis spricht dafür, dass der Linker sie als ungenutzt entfernt hat, bewiesen ist das nur für die Idle-Gruppe 3.
- **Abweichung (Hinweis):** `ApModuleManager` ist hier nicht Teil des Berichts; ihre Funktionen `GetModule`, `EnableModuleIdle`/`2` und `GetPrevClockCount` sind nur als Gegenstellen benannt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApModule.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `ReleaseCallBackDataList` | – | | eingebaut in den Destruktorrumpf `0x004E4960` |
| 1 | `ReleaseStreamDataList` | – | | eingebaut in den Destruktorrumpf `0x004E4960` |
| 2 | `AddModule` | `0x004E4B40` | 79 | Zeichenkette |
| 3 | `OnPreDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 4 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 5 | `GetModuleName` | `0x004E4030` | 4 | von Hand geprüft |
| 6 | `EnumCallback` | `0x004E4040` | 97 | von Hand geprüft |
| 7 | `SetAttachedModuleData` | `0x004E4B90` | 324 | von Hand geprüft |
| 8 | `GetAttachedModuleData` | `0x004E40B0` | 42 | von Hand geprüft |
| 9 | `GetParentModuleData` | `0x004E40E0` | 36 | von Hand geprüft |
| 10 | `GetDataSize` | `0x004E4110` | 26 | von Hand geprüft |
| 11 | `AddDataSize` | `0x004E4130` | 34 | von Hand geprüft |
| 12 | `SetModuleData` | `0x004E4160` | 60 | von Hand geprüft |
| 13 | `SetCallback` | `0x004E41A0` | 109 | von Hand geprüft |
| 14 | `AddStreamCallback` | `0x004E4210` | 113 | von Hand geprüft |
| 15 | `GetModule` | `0x004E4290` | 8 | von Hand geprüft |
| 16 | `Idle` | `0x004E50C0` | 227 | von Hand geprüft |
| 17 | `Idle2` | `0x004E51B0` | 227 | von Hand geprüft |
| 18 | `Idle3` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 19 | `RemoveIdleEvent` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 20 | `RemoveIdleEvent2` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 21 | `RemoveIdleEvent3` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 22 | `GetIdleEvent` | `0x004E4F40` | 131 | von Hand geprüft |
| 23 | `GetIdleEvent2` | `0x004E4FD0` | 131 | von Hand geprüft |
| 24 | `GetIdleEvent3` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 25 | `SetMaxIdleEvent` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 26 | `SetMaxIdleEvent2` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 27 | `SetMaxIdleEvent3` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 28 | `GetMaxIdleEvent` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 29 | `GetMaxIdleEvent2` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 30 | `GetMaxIdleEvent3` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 31 | `m_fConstructorCB` | – | | nicht gefunden (statische Hilfsfunktion, vermutlich entfernt) |
| 32 | `m_fDestructorCB` | – | | nicht gefunden (statische Hilfsfunktion, vermutlich entfernt) |
| 33 | `EnumConstructor` | `0x004E42A0` | 76 | von Hand geprüft |
| 34 | `EnumDestructor` | `0x004E42F0` | 76 | von Hand geprüft |
| 35 | `InitMemoryPool` | `0x004E4340` | 65 | von Hand geprüft |
| 36 | `ExistCallback` | `0x004E4390` | 36 | von Hand geprüft |
| 37 | `CreateModuleData` | `0x004E43C0` | 193 | von Hand geprüft |
| 38 | `DestroyModuleData` | `0x004E4490` | 115 | von Hand geprüft |
| 39 | `SetPacketType` | `0x004E4510` | 48 | von Hand geprüft |
| 40 | `GetPacketType` | – | | nicht gefunden (in der Quelle gibt sie `m_ulPacketType` als Zeiger zurück; keine eigene Funktion mit `lea eax,[ecx+0x948]`) |
| 41 | `AddPreReceiveModule` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 42 | `EnumPreRecieveModule` | `0x004E4540` | 90 | von Hand geprüft |
| 43 | `SendPacket` | `0x004E45A0` | 21 | von Hand geprüft |
| 44 | `GetModuleManager` | `0x004E45C0` | 4 | von Hand geprüft |
| 45 | `EnableIdle` | `0x004E45D0` | 17 | von Hand geprüft |
| 46 | `EnableIdle2` | `0x004E45F0` | 17 | von Hand geprüft |
| 47 | `EnableIdle3` | – | | nicht im Binary gefunden: im ganzen Binary keine Funktion, die die zugehörigen Felder benutzt (vermutlich vom Linker entfernt, weil nie gerufen) |
| 48 | `SetModuleType` | `0x004E4610` | 16 | von Hand geprüft |
| 49 | `GetModuleType` | `0x004E4620` | 5 | von Hand geprüft |
| 50 | `SetSelfCID` | `0x004E4630` | 21 | von Hand geprüft |
| 51 | `GetPrevClockCount` | `0x004E4650` | 8 | von Hand geprüft |
| 52 | `GetClockCount` | `0x004E4660` | 8 | von Hand geprüft |
| 53 | `Receive` | – | | nicht gefunden (in der Quelle ein Aufruf von `OnReceive`; keine Funktion mit dem Sprung über Vtable-Eintrag 9) |
| 54 | `Report` | `0x004E4670` | 26 | vtable/String |
| 55 | `Report_Head` | `0x004E4690` | 30 | vtable/String |

37 von 56 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `ApModule` (`0x004E4700`), `~ApModule_body` (`0x004E4960`), `~ApModule` (`0x004E4D30`), `AddIdleEvent` (`0x004E4E90`), `GetModuleManager_thunk` (`0x007025B0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x04` | `Modultyp `m_nModuleType`` | `SetModuleType`, `GetModuleType` |
| `this+0x08` | `Modulname (40 Byte)` | `GetModuleName` |
| `this+0x30` | `Zeiger auf die Modulverwaltung` | `GetModuleManager`, `GetModule`, `SendPacket` |
| `this+0x34 / 0x38` | `Anzahl und Feld der angehängten Daten (16 Byte je Eintrag)` | `SetAttachedModuleData`, `GetAttachedModuleData` |
| `this+0x3C` | `Datengrößen (120 × 4)` | `GetDataSize`, `AddDataSize`, `SetModuleData` |
| `this+0x21C / 0x3FC` | `Konstruktor- / Destruktorlisten (je 120)` | `EnumConstructor`, `EnumDestructor` |
| `this+0x5DC` | `Rückruflisten (130)` | `SetCallback`, `EnumCallback`, `ExistCallback` |
| `this+0x7E4` | `Liste der Vorab-Empfänger` | `EnumPreRecieveModule` |
| `this+0x7E8 / 0x810` | `Sperre / Ereignisfeld der Idle-Gruppe 1` | `AddIdleEvent`, `GetIdleEvent`, `Idle` |
| `this+0x85C / 0x884` | `Sperre / Ereignisfeld der Idle-Gruppe 2` | `GetIdleEvent2`, `Idle2` |
| `this+0x8D0 / 0x8F8` | `Sperre / Ereignisfeld der Idle-Gruppe 3` | nur Konstruktor, Destruktor |
| `this+0x944` | `Modulstatus `m_eModuleStatus`` | `ApModuleManager` (nicht einzeln belegt) |
| `this+0x948` | `Paketkennungen (10)` | `SetPacketType` |
| `this+0x970 / 0x974` | `Idle-Schalter 1 und 2` | `EnableModuleIdle`/`2` |
| `this+0x97C` | `Strom-Listen (120)` | `AddStreamCallback` |
| `this+0xB5C / 0xB7C` | `Speicherpool / Typindex` | `InitMemoryPool`, `CreateModuleData` |
| `this+0xB80` | `Flag „dynamisch angelegt“` | `AddModule` |

## Vtable und Aufbau

`ApModule` (Basisklasse aller Module) hat die Vtable `0x008AC94C` mit 13 Einträgen: 0 Löschwrapper (`0x004E4D30`), 1 `OnAddModule` und 2 `OnInit` (gemeinsamer Rumpf `0x0067AC90`, return TRUE), 3 bis 5 `OnIdle`/`OnIdle2`/`OnIdle3` (`0x0067FAB0`, return TRUE mit einem Argument), 6 `OnPreDestroy` und 7 `OnDestroy` (`0x0067AC90`), 8 `OnPreReceive` und 9 `OnReceive` (`0x004E3420`, gemeinsamer Rumpf mit fünf Argumenten), 10 `OnValid` (`0x007AA0A0`), 11 `Report` (`0x004E4670`), 12 `Report_Head` (`0x004E4690`). Der Konstruktor (`0x004E4700`) setzt die Vtable und baut zuerst die sechs Sperr- und Listenobjekte der drei Idle-Ereignislisten auf.
Die Instanz ist 0xB84 Byte groß (aus den Feldern der Quelle und den Offsets der Funktionen): Modultyp `+4`, Name `+8` (40 Byte), Modulverwaltung `+0x30`, Anzahl angehängter Daten `+0x34`, Feld der angehängten Daten `+0x38` (120 Einträge zu 16 Byte), Datengrößen `+0x3C` (120 × 4), Konstruktorlisten `+0x21C`, Destruktorlisten `+0x3FC`, Rückruflisten `+0x5DC` (130 Einträge), Liste der Vorab-Empfänger `+0x7E4`, drei Idle-Ereignisgruppen ab `+0x7E8`, `+0x85C` und `+0x8D0` (Sperre, danach das Feld der Ereignisse bei `+0x28`), Paketkennungen `+0x948` (10 Einträge), Idle-Schalter `+0x970`/`+0x974`/`+0x978`, Strom-Listen `+0x97C` (120 Einträge), Speicherpool `+0xB5C` (Typindex bei `+0xB7C`) und das Flag „dynamisch angelegt“ bei `+0xB80`.

## Moduldaten und angehängte Daten

`GetDataSize` (`0x004E4110`), `AddDataSize` (`0x004E4130`) und `SetModuleData` (`0x004E4160`, rundet die Größe auf ein Vielfaches von 4) lesen und schreiben `m_nDataSize[Index]` (Index höchstens 119; sonst 0 bzw. FALSE). `SetAttachedModuleData` (`0x004E4B90`, 324 Byte, fünf Argumente) rundet die Größe auf 4, trägt Größe, Versatz und Elternindex in einen Eintrag von `+0x38` ein, erhöht die Größe des Elternmoduls und legt je einen Eintrag in der Konstruktor- und der Destruktorliste an; `GetAttachedModuleData` (`0x004E40B0`) rechnet vom Elterndatenblock auf den angehängten (Zeiger + Versatz) und `GetParentModuleData` (`0x004E40E0`) zurück (Zeiger − Versatz), beide mit Prüfung des Index gegen 0x77.
`CreateModuleData` (`0x004E43C0`, 169 Byte, Argumente Index und Anzahl) legt den Datenblock an: bei Index 0 und vorhandenem Pool aus dem Pool (Zuteilung `0x004E3F80`), sonst mit `new[]` (Anzahl · Größe Byte); danach Nullen und je Element `EnumConstructor`. `DestroyModuleData` (`0x004E4490`) ruft `EnumDestructor` und gibt den Block an den Pool (`0x0040FEC0`) bzw. mit `delete` zurück. `EnumConstructor` (`0x004E42A0`) und `EnumDestructor` (`0x004E42F0`) laufen über die verketteten Listen bei `+0x21C` bzw. `+0x3FC` und rufen die Zeiger (Zeiger auf Block, Klasse, Index). `InitMemoryPool` (`0x004E4340`) richtet den Pool ein (Größe 0 bedeutet Größe des Blocks 0) und liefert, ob der Typindex gültig ist.

## Rückrufe und Strom

`SetCallback` (`0x004E41A0`) hängt einen Eintrag (12 Byte: Klasse, Funktion, Nachfolger) ans Ende der Liste `+0x5DC + ID·4` (ID höchstens 129); `EnumCallback` (`0x004E4040`) ruft alle Einträge mit Daten und Zusatzdaten und bricht beim ersten FALSE ab (nur bei gesetztem Funktionszeiger, ein Zeiger wird über `IsBadCodePtr` geprüft); `ExistCallback` (`0x004E4390`) prüft, ob die Liste nicht leer ist. `AddStreamCallback` (`0x004E4210`, 16-Byte-Einträge: Lesefunktion, Schreibfunktion, Modul, Nachfolger) arbeitet entsprechend mit der Liste `+0x97C + Index·4` (Index höchstens 119).

## Idle-Ereignisse

Im Binary gibt es nur die Kette für die erste und zweite Ereignisliste: `AddIdleEvent` (`0x004E4E90`, fünf Argumente, in der Quelle nur in der Kopfdatei), `GetIdleEvent` (`0x004E4F40`) und `GetIdleEvent2` (`0x004E4FD0`) suchen das erste fällige Ereignis (Zeit ≤ jetzt); `Idle` (`0x004E50C0`) und `Idle2` (`0x004E51B0`) arbeiten die fälligen Ereignisse unter der Sperre (`0x004E7CF0`/`0x004E7C70`) ab; `Idle` holt das Ereignis über `GetIdleEvent` und ruft die Funktion aus dem Ereignis (Aufruf über Zeiger, Zeit, Klasse und Daten stehen in den Feldern `+4` bis `+0xC`). Alle Funktionen der dritten Gruppe und die Funktionen zum Entfernen und zur Größe der Listen (`RemoveIdleEvent*`, `SetMaxIdleEvent*`, `GetMaxIdleEvent*`) und `AddIdleEvent2/3` fehlen: im ganzen Binary verweist keine Funktion außer Konstruktor und Destruktor auf die Felder der dritten Gruppe (Scan über alle `lea`-Befehle mit `+0x7E8`, `+0x85C`, `+0x8D0`).
`EnableIdle` (`0x004E45D0`) und `EnableIdle2` (`0x004E45F0`) geben `this` und den Schalter an `ApModuleManager::EnableModuleIdle` (`0x004E3760`) bzw. `…2` (`0x004E3820`) weiter; die dritte Fassung fehlt.

## Weiterleitung an die Verwaltung

`GetModuleManager` (`0x004E45C0`, Thunk `0x007025B0`) liefert `this+0x30`. `GetModule` (`0x004E4290`) ruft mit der Verwaltung `ApModuleManager::GetModule` (`0x004E3540`), `SendPacket` (`0x004E45A0`) ruft nach Prüfung auf eine vorhandene Verwaltung deren virtuelle Funktion (Vtable-Eintrag 2) mit den fünf Argumenten, `SetSelfCID` (`0x004E4630`) deren Eintrag 3. `GetPrevClockCount` (`0x004E4650`) springt zu `0x004E3910` (liest `Verwaltung+0x40`) und `GetClockCount` (`0x004E4660`) zu `0x004E3920` (springt zur Zeitfunktion `0x004F4990`).
`AddModule` (`0x004E4B40`, 79 Byte) trägt die Verwaltung bei `this+0x30` ein, meldet ein Modul ohne Namen mit der Zeichenkette „ApModyle::AddModule Name Error“ (so geschrieben) und ruft `ApModuleManager::AddModule` (`0x004E3AD0`); das Flag „dynamisch“ steht bei `+0xB80`. `SetModuleType` (`0x004E4610`) und `GetModuleType` (`0x004E4620`, 16-Bit-Rückgabe) schreiben und lesen `+4`.

## Vorab-Empfänger und Paketkennungen

`SetPacketType` (`0x004E4510`) trägt eine Kennung in das erste freie Feld der zehn Einträge bei `+0x948` ein (sonst FALSE). `EnumPreRecieveModule` (`0x004E4540`) ruft für jedes eingetragene Modul die virtuelle Funktion `OnPreReceive` (Vtable-Eintrag 8, Versatz `0x20`) und bricht beim ersten FALSE ab. Die Liste bei `+0x7E4` wird im Binary nur hier und im Destruktor benutzt; `AddPreReceiveModule` fehlt.

## Löschen und Bericht

Der Destruktorrumpf (`0x004E4960`, 468 Byte) gibt das Feld der angehängten Daten frei, räumt je Index die Konstruktor-, Destruktor- und Strom-Listen und je Rückruf-ID die Rückruflisten ab (`ReleaseCallBackDataList`/`ReleaseStreamDataList` sind dabei eingebaut) und löscht die Liste der Vorab-Empfänger; danach folgen die Destruktoren der drei Ereignisgruppen. Der Löschwrapper `0x004E4D30` (Vtable-Eintrag 0) ruft ihn und gibt den Speicher frei. `Report` (`0x004E4670`) schreibt „None“ in die Datei, `Report_Head` (`0x004E4690`) den Kopf mit dem Modulnamen; beide sind in der Quelle virtuell.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Konstanten: 120 Module, 130 Rückrufe, 10 Paketkennungen, 40 Zeichen Modulname stimmen). Eine Abweichung in der Quelle selbst: `GetPacketType` gibt dort `m_ulPacketType` (ein Feld) als `UINT32` zurück.

## Grenzen

- Gelesen (Disassembly) sind `GetModuleName`, `EnumCallback` (Anfang), `Get/ParentModuleData`, `GetDataSize`, `AddDataSize`, `SetModuleData`, `SetCallback`, `AddStreamCallback` (Anfang), `EnumConstructor`/`Destructor`, `InitMemoryPool`, `ExistCallback`, `CreateModuleData`/`DestroyModuleData` (Anfang), `SetPacketType`, `EnumPreRecieveModule`, `SendPacket`, `EnableIdle`/`2`, `SetModuleType`, `GetModuleType`, `SetSelfCID`, `GetClockCount`, `GetPrevClockCount`, der Anfang von `SetAttachedModuleData` und des Konstruktors sowie `AddIdleEvent` (Anfang); `Idle`/`Idle2`/`GetIdleEvent`/`GetIdleEvent2` sind über Offsets, Argumentzahl und Aufrufbeziehung zugeordnet, nicht Zeile für Zeile verglichen. Der Ablauf der Schleife in `Idle` nach dem Aufruf (Austragen, Weiterzählen) wurde nicht gelesen.
- Der Scan nach den Idle-Gruppen sucht nur `lea`-Befehle mit den Offsets; Zugriffe über andere Befehle (z. B. `mov eax,[ecx+0x8F8]`) wurden nicht gesucht. Dass die fehlenden Funktionen vom Linker entfernt wurden, ist nur eine Folgerung aus dem Fehlen von Verweisen, keine Beobachtung.
- Die Namen der Gegenstellen in `ApModuleManager` (`GetModule` `0x004E3540`, `EnableModuleIdle`/`2` `0x004E3760`/`0x004E3820`, `GetPrevClockCount` `0x004E3910`) sind nur aus ihrer Form und dem Aufruf von `ApModule` abgeleitet; die übrigen Funktionen der Verwaltung wurden nicht untersucht.
- Die Zuordnung `Idle` zu Gruppe 1 und `Idle2` zu Gruppe 2 folgt aus den Offsets `+0x7E8/+0x810` bzw. `+0x85C/+0x884`; die Größe der Instanz (0xB84) ist aus den Offsets geschlossen, nicht aus einem `new`-Aufruf gelesen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, gemeinsamer Rumpf: 2, nicht im Client: 15, ohne Kandidat: 3.

<!-- LUECKENREGISTER-NACHTRAG-END -->
