# AgcmSound (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmSound` (Ton: BGM, Stream, Samples, 3D-Sound, Geräte, Raumeffekte; benutzt den `SoundManager` mit FMOD) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Zeichenketten, EP8-Quelle `Modules/AClient/AgcmSound/AgcmSound.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: jede Quellmethode ist einer Adresse zugeordnet oder (zusammengefaltet, eingebaut, unreferenziert) begründet. Neu belegt: `OnUpdate3DSoundPosition` (`0x005F70E0`; sucht die Instanz und prüft, ob sie ein 3D-Sound ist – Typ 3 oder 4 –, sonst FALSE; Aufrufer ist eine [`AgcmEff2`](AgcmEff2.md)-Funktion `0x007A8220`), `GetDeviceInfo` (Namensfassung `0x005F8130`) und `LoadSound` (`0x005F83C0`).
- **Nicht als eigene Funktion im Binary:** `StopStream` (nur auskommentiert aufgerufen), `JobQueueAdd`/`JobQueueRemove` (leer und unreferenziert), die Fassung `PreStop3DSound(int)` (kein Aufrufer im Binary), `GetDeviceInfo(int)` und `_GetPreset` (eingebaut); `Stop3DSound` liegt mit `StopSampleSound` an derselben Adresse.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmSound.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005F90E0` | 7761 | vtable/String |
| 1 | `OnInit` | `0x005F8800` | 23 | vtable/String |
| 2 | `OnDestroy` | `0x005F70C0` | 18 | vtable/String |
| 3 | `OnIdle` | `0x005F7960` | 272 | vtable/String |
| 4 | `OnUpdate3DSoundPosition` | `0x005F70E0` | 63 | von Hand geprüft |
| 5 | `CloseAll3DSample` | `0x005F7120` | 12 | von Hand geprüft |
| 6 | `CloseAllSample` | `0x005F7130` | 12 | von Hand geprüft |
| 7 | `SetSpeaker` | `0x005F7140` | 108 | von Hand geprüft |
| 8 | `SetRoom` | `0x005F8360` | 85 | von Hand geprüft |
| 9 | `GetDeviceInfo` | – | | Indexfassung: in `OnSelectDevice` und `GetCurrentDeviceName` eingebaut; sie ruft die gemeinsame Karten-Funktion `GetByIndex` (`0x00740CB0`). Die Namensfassung ist `0x005F8130` |
| 10 | `GetDeviceInfo` | `0x005F8130` | 131 | von Hand geprüft |
| 11 | `OnSelectDevice` | `0x005F7E40` | 51 | von Hand geprüft |
| 12 | `OnSelectDevice` | `0x005F81C0` | 46 | von Hand geprüft |
| 13 | `GetCurrentDeviceName` | `0x005F7E80` | 27 | von Hand geprüft |
| 14 | `SetStreamVolume` | `0x005F71C0` | 41 | von Hand geprüft |
| 15 | `SetBGMVolume` | `0x005F71F0` | 63 | von Hand geprüft |
| 16 | `SetSampleVolume` | `0x005F7230` | 84 | von Hand geprüft |
| 17 | `Set3DSampleVolume` | `0x005F7290` | 84 | von Hand geprüft |
| 18 | `MuteSound` | `0x005F72F0` | 135 | von Hand geprüft |
| 19 | `UnMuteSound` | `0x005F7380` | 177 | von Hand geprüft |
| 20 | `PreStop3DSound` | `0x005F7440` | 41 | von Hand geprüft |
| 21 | `PreStop3DSound` | – | | Fassung mit Kanalindex: im Binary kein Aufrufer und keine eigene Funktion; die Quelle ruft sie nur in `AgcdEffCtrl.cpp:679` auf (die Fassung mit Clump ist `0x005F7440`) |
| 22 | `PlayBGM` | `0x005F7470` | 158 | von Hand geprüft |
| 23 | `StopBGM` | `0x005F7510` | 73 | von Hand geprüft |
| 24 | `PlayStream` | `0x005F7560` | 166 | von Hand geprüft |
| 25 | `StopStream` | – | | in der Quelle nur in einer auskommentierten Zeile von `AgcdEffSound.cpp` aufgerufen, damit unreferenziert; im Binary nicht vorhanden |
| 26 | `ClearStream` | `0x005F7610` | 18 | von Hand geprüft |
| 27 | `Play3DSound` | `0x005F7A70` | 210 | von Hand geprüft |
| 28 | `Stop3DSound` | `0x005F7690` | 25 | gleiche Adresse wie `Rumpf identisch mit `StopSampleSound` (ICF)` (vom Linker zusammengefaltet) |
| 29 | `PlaySampleSound` | `0x005F7630` | 85 | von Hand geprüft |
| 30 | `StopSampleSound` | `0x005F7690` | 25 | von Hand geprüft |
| 31 | `JobQueueAdd` | – | | leerer Rumpf, in der Quelle von keinem Modul aufgerufen; im Binary nicht vorhanden |
| 32 | `JobQueueRemove` | – | | leerer Rumpf, in der Quelle von keinem Modul aufgerufen; im Binary nicht vorhanden |
| 33 | `GetStreamSoundLength` | `0x005F76B0` | 114 | von Hand geprüft |
| 34 | `GetSampleSoundLength` | `0x005F7730` | 119 | von Hand geprüft |
| 35 | `GetCurrBGMFileName` | `0x005F77B0` | 31 | seqmatch |
| 36 | `IsIn3DSoundRange` | `0x005F77D0` | 145 | seqmatch |
| 37 | `IsSoundMuted` | `0x005F7870` | 51 | von Hand geprüft |
| 38 | `LoadSound` | `0x005F83C0` | 403 | Callback-Registrierung |
| 39 | `_LoadPackingFile` | `0x005F8820` | 973 | von Hand geprüft |
| 40 | `_LoadPackingSound` | `0x005F81F0` | 314 | seqmatch |
| 41 | `_GetDeviceInformation` | `0x005F8BF0` | 362 | von Hand geprüft |
| 42 | `_GetPreset` | – | | in `SetRoom` eingebaut |
| 43 | `_AddPreset` | `0x005F8610` | 62 | von Hand geprüft |

38 von 44 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmSound` (`0x005F8E70`), `~AgcmSound` (`0x005F9000`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA0 / 0xBA4` | `BGM-Lautstärke aktuell / vorher` | `SetBGMVolume` |
| `this+0xBA8` | `BGM stumm` | `PlayBGM`, `MuteSound`, `IsSoundMuted` |
| `this+0xBAC / 0xBB0` | `Stream-Lautstärke aktuell / vorher` | `SetStreamVolume` |
| `this+0xBB4` | `Stream stumm` | `PlayStream` |
| `this+0xBB8 / 0xBBC` | `Sample-Lautstärke aktuell / vorher` | `SetSampleVolume`, `PlaySampleSound` |
| `this+0xBC0` | `Sample stumm` | `PlaySampleSound` |
| `this+0xBC4 / 0xBC8` | `3D-Sample-Lautstärke aktuell / vorher` | `Set3DSampleVolume` |
| `this+0xBCC` | `3D-Sample stumm` | `Play3DSound` |
| `this+0xBD0` | `Raumtyp (`m_eSoundEffectType`)` | `SetRoom` |
| `this+0xC04` | `Index des gewählten Geräts` | `OnSelectDevice` |
| `this+0xC08` | `Nummer der laufenden BGM-Instanz` | `PlayBGM`, `SetBGMVolume` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmSound` (`0x005FAF40`, Löschwrapper), 1 `OnAddModule` (`0x005F90E0`, 7761 Byte), 2 `OnInit` (`0x005F8800`, 23 Byte), 3 `OnIdle` (`0x005F7960`), 4 und 5 `0x0067FAB0`, 6 `0x0067AC90`, 7 `OnDestroy` (`0x005F70C0`), 8 `0x004E3420`. Der Konstruktor (`0x005F8E70`) trägt den Modulnamen `AgcmSound` ein, der Destruktorrumpf ist `0x005F9000`. `OnAddModule` ist so groß, weil darin die Raum-Voreinstellungen (`_AddPreset`-Aufrufe) und die Geräteabfrage (`_GetDeviceInformation`, `0x005F8BF0`) eingebaut sind; es liest `Sound\SoundPak.info`.

## Lautstärke und Stummschaltung

Die Lautstärken liegen paarweise (aktuell / vorher) in `this`: BGM `+0xBA0/0xBA4`, Stream `+0xBAC/0xBB0`, Samples `+0xBB8/0xBBC`, 3D-Samples `+0xBC4/0xBC8`; die Stumm-Merker folgen als `+0xBA8` (BGM), `+0xBB4` (Stream), `+0xBC0` (Sample), `+0xBCC` (3D). Die vier Setter liegen in Quellreihenfolge hintereinander: `SetStreamVolume` (`0x005F71C0`, ruft `SetEnvSoundVolume`), `SetBGMVolume` (`0x005F71F0`, setzt die Lautstärke der laufenden BGM-Instanz `+0xC08`), `SetSampleVolume` (`0x005F7230`) und `Set3DSampleVolume` (`0x005F7290`). `MuteSound` (`0x005F72F0`) und `UnMuteSound` (`0x005F7380`) schalten je Typ (1 = BGM, 2 = Samples und 3D-Samples, 3 = Stream) die Lautstärke auf 0 bzw. den gemerkten Wert zurück; `IsSoundMuted` (`0x005F7870`) liefert den Merker je Typ (1 → `+0xBA8`, 2 → `+0xBCC`, 3 → `+0xBB4`).

## Abspielen

`PlayBGM` (`0x005F7470`) kehrt bei stummem BGM mit 0 zurück, wechselt über den `SoundManager` (`ChangeBGM`) die Musik (Überblendzeit nur bei `bUseFade`) und gleicht anschließend den Stumm-Zustand ab; `StopBGM` (`0x005F7510`) wechselt auf „keine Datei“. `PlayStream` (`0x005F7560`) prüft den Stumm-Merker, sucht zuerst `FindEnvironmentSound` und legt sonst `AddEnvironmentSound` an; `ClearStream` (`0x005F7610`) ruft `ClearEnvSound`. `PlaySampleSound` (`0x005F7630`) multipliziert die Sample-Lautstärke (`+0xBB8`) mit dem Parameter; `StopSampleSound` (`0x005F7690`) ruft `Stop`; `Stop3DSound` hat denselben Rumpf und ist damit zusammengefaltet. `Play3DSound` (`0x005F7A70`, 210 Byte) holt über [`AgcmRender`](AgcmRender.md) die Kamera (`+0xCA0`), prüft den 3D-Stumm-Merker und spielt über den `SoundManager`; `IsIn3DSoundRange` (`0x005F77D0`) vergleicht den Abstand zur Kameraposition mit der Konstante `_DAT_008BE1A8`. `PreStop3DSound` (`0x005F7440`) gibt den Szenenknoten eines Clumps frei.
`GetStreamSoundLength` (`0x005F76B0`) und `GetSampleSoundLength` (`0x005F7730`) suchen die Ressource und liefern ihre Länge in Millisekunden; `GetCurrBGMFileName` (`0x005F77B0`) liefert den Dateinamen der laufenden BGM-Instanz.

## Geräte, Raum, Lautsprecher

`SetSpeaker` (`0x005F7140`) wählt über `switch` den Lautsprechermodus (Werte 2 und 3 werden auf 4 bzw. 3 abgebildet). `SetRoom` (`0x005F8360`) setzt `m_eSoundEffectType` (`this+0xBD0`, nur bei aktivem `m_bUseRoom`), sucht die Voreinstellung in der Karte (`_GetPreset` ist eingebaut) und übergibt sie an den `SoundManager`; `_AddPreset` (`0x005F8610`) kopiert die Eigenschaften (32 Doppelwörter) in die Karte. `OnSelectDevice` gibt es in zwei Fassungen: nach Index (`0x005F7E40`, setzt `this+0xC04`) und nach Name (`0x005F81C0`, über die Namenssuche `0x005F8130`); `GetCurrentDeviceName` (`0x005F7E80`) liefert den Namen (Eintrag `+0x14`) des aktuellen Geräts.

## Laden

`LoadSound` (`0x005F83C0`, 403 Byte, static) holt über `AgcmSound` (Zeiger `DAT_009E2458`) das Modul, versucht zuerst `SoundManager::LoadFile` und dann `_LoadPackingSound`, danach den Weg über `AuPackingManager` (Datei öffnen, Größe, in einen Puffer lesen, `LoadBuffer`). `_LoadPackingSound` (`0x005F81F0`, 314 Byte) macht den Dateinamen klein (`tolower`), schneidet einen führenden `\` ab, sucht ihn in der Packkarte und lädt die Daten daraus. `_LoadPackingFile` (`0x005F8820`, 973 Byte) öffnet die Pack-Datei (`fopen` mit `rb`), baut die Pfade `%s\%s%s`, `%s\%s` und `%s%s\%s` und trägt jeden Eintrag über den Karten-Einfüger `0x005F8700` (Zeichenkette → Zeiger, nur wenn noch nicht vorhanden) in die Packkarte ein. Der Aufrufer von `_LoadPackingFile` ist `OnAddModule`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind `SetStreamVolume`, `SetBGMVolume`, `PlayBGM`, `StopBGM`, `PlayStream`, `ClearStream`, `PlaySampleSound`, `GetStreamSoundLength`, `IsIn3DSoundRange`, `OnUpdate3DSoundPosition`, `LoadSound`, `_LoadPackingSound` und die Geräte-/Raum-Funktionen; die Feldzuordnung der Lautstärkepaare folgt aus dem Zusammenspiel der Setter, der Stumm-Funktionen und von `IsSoundMuted`.
- Zuordnungen mit Aufrufer-Beleg: `PreStop3DSound(void*)` (`0x005F7440`) wird von `0x005AA280` und `0x005C7010` gerufen, den Entsprechungen von `AgcmCharacter.cpp:4209` und `AgcmEventEffect.cpp:3238`; `StopSampleSound` (`0x005F7690`) wird von der `AgcmEff2`-Funktion `0x007A8040` zweimal gerufen (Zweige „3D“ und „Sample“), das dritte Ziel dort ist `StopBGM`; `OnUpdate3DSoundPosition` von `0x007A8220`; `GetCurrentDeviceName` von `0x005D9970`.
- `MuteSound`/`UnMuteSound` sind über die Aufrufe der Setter und die Typzweige zugeordnet (1 = BGM, 2 = Samples und 3D-Samples, 3 = Stream); die Enum-Werte sind nicht gegen den Header geprüft.
- Dass `Stop3DSound` mit `StopSampleSound` zusammengefaltet ist, folgt aus den gleichen Quellrümpfen (beide rufen nur `Stop(nIndex)`) und daraus, dass `0x007A8040` dieselbe Adresse für beide Zweige ruft; ein Byte-Vergleich liegt nicht vor.
- Ob `PreStop3DSound(int)` wirklich entfernt wurde, ist aus dem Fehlen eines Aufrufers im Binary geschlossen: die Quelle ruft sie in `AgcdEffCtrl.cpp:679` auf, die umgebende Funktion ist nicht geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 6, nicht im Client: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmEff2`](AgcmEff2.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmRender`](AgcmRender.md)
- **Erwähnt in:** [`AgcmEff2`](AgcmEff2.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmUIControl`](AgcmUIControl.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`CChatCmd`](CChatCmd.md)
