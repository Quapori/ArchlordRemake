# ApmObject (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `ApmObject` (Weltobjekte: Verwaltung, Vorlagen, Laden aus `Obj%05d.ini`, Entfernen) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/APublic/ApmObject/ApmObject.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 34 von 54 Quellmethoden sind zugeordnet. Nicht gefunden sind `AddObject(OID, TID)` und `CreateObject`, die Löschvarianten für Box, OID und alle Objekte, `CreateTemplate`/`DestroyTemplate`/`DestroyAllTemplate`, `AddObjectTemplate`/`DeleteObjectTemplate`, alle Schreibfunktionen (`StreamWriteTemplate`, `StreamWrite` ×3, `StreamRead(Datei)`), die `StreamReadAllDivision`-Funktionen, `UpdateInit` und `SetCallbackLoadSector`.
- **Hinweis:** `SetCallbackLoadSector` und `SetCallbackLoadError` teilen sich Rümpfe mit [`ApmMap`](ApmMap.md); für `LoadError` ist der Aufrufer `MainWindow` der Quelle nicht im Binary gesucht worden.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`ApmObject.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0051E300` | 78 | vtable/String |
| 1 | `OnInit` | `0x0051C6F0` | 119 | vtable/String |
| 2 | `OnDestroy` | `0x0051DBD0` | 271 | vtable/String |
| 3 | `OnIdle` | `0x0051D150` | 5 | vtable/String |
| 4 | `GetObjectSequence` | `0x0051C770` | 30 | von Hand geprüft |
| 5 | `AttachObjectData` | `0x00511140` | 30 | gleiche Adresse wie `gemeinsamer `SetAttachedModuleData`-Einzeiler mit Kennung 0` (vom Linker zusammengefaltet) |
| 6 | `SetMaxObject` | `0x0051C790` | 11 | von Hand geprüft |
| 7 | `CreateObject` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 8 | `DestroyObject` | `0x0051C7A0` | 69 | von Hand geprüft |
| 9 | `GetObject` | `0x0051C7F0` | 30 | von Hand geprüft |
| 10 | `AddObject` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 11 | `AddObject` | `0x0051C810` | 148 | von Hand geprüft |
| 12 | `DeleteObject` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 13 | `DeleteObject` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 14 | `DeleteObject` | `0x0051DCE0` | 222 | von Hand geprüft |
| 15 | `DeleteObject` | `0x0051D160` | 146 | von Hand geprüft |
| 16 | `DeleteAllObject` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 17 | `GetObjectTemplateSequence` | `0x0051C8B0` | 30 | von Hand geprüft |
| 18 | `AttachObjectTemplateData` | `0x0053A4F0` | 30 | gleiche Adresse wie `gemeinsamer `SetAttachedModuleData`-Einzeiler mit Kennung 1` (vom Linker zusammengefaltet) |
| 19 | `SetMaxObjectTemplate` | `0x0051C8D0` | 11 | von Hand geprüft |
| 20 | `CreateTemplate` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 21 | `DestroyTemplate` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 22 | `DestroyAllTemplate` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 23 | `GetObjectTemplate` | `0x0051C8E0` | 30 | von Hand geprüft |
| 24 | `AddObjectTemplate` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 25 | `DeleteObjectTemplate` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 26 | `StreamReadTemplate` | `0x0051C900` | 393 | von Hand geprüft |
| 27 | `StreamWriteTemplate` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 28 | `StreamRead` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 29 | `StreamWrite` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 30 | `StreamWrite` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 31 | `ObjectTemplateReadCB` | `0x0051D200` | 840 | Callback-Registrierung |
| 32 | `ObjectTemplateWriteCB` | `0x0051CA90` | 65 | Callback-Registrierung |
| 33 | `ObjectReadCB` | `0x0051DDC0` | 1341 | Callback-Registrierung |
| 34 | `ObjectWriteCB` | `0x0051CAE0` | 430 | Callback-Registrierung |
| 35 | `StreamWrite` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 36 | `StreamRead` | `0x0051D550` | 991 | von Hand geprüft |
| 37 | `StreamRead` | `0x0051DA60` | 311 | von Hand geprüft |
| 38 | `UpdateStatus` | `0x0051CC90` | 203 | von Hand geprüft |
| 39 | `StreamReadAllDivision` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 40 | `StreamReadAllDivision` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 41 | `StreamReadAllDivisionVersion2` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 42 | `SetMaxObjectRemove` | `0x0051CD60` | 11 | von Hand geprüft |
| 43 | `ProcessRemove` | `0x0051CD70` | 221 | von Hand geprüft |
| 44 | `AddRemoveObject` | `0x0051CE50` | 120 | von Hand geprüft |
| 45 | `UpdateInit` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 46 | `SetCallbackInitObject` | `0x006DA540` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf, Kennung 0` (vom Linker zusammengefaltet) |
| 47 | `SetCallbackRemoveObject` | `0x0053A200` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf, Kennung 1` (vom Linker zusammengefaltet) |
| 48 | `SetCallbackUpdateStatus` | `0x0057BED0` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf, Kennung 2` (vom Linker zusammengefaltet) |
| 49 | `SetCallbackAddObject` | `0x005766B0` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf, Kennung 3` (vom Linker zusammengefaltet) |
| 50 | `SetCallbackLoadSector` | – | | kein direkter Aufruf im Bereich `0x0051C6F0`–`0x0051E530` gefunden; Verbleib offen (vermutlich eingebaut oder nur im Editor/Server benutzt) |
| 51 | `SetCallbackLoadError` | `0x00574590` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf, Kennung 5 (auch `ApmMap::SetCallbackLoadSector`)` (vom Linker zusammengefaltet) |
| 52 | `ParsePOS` | `0x0051CED0` | 40 | von Hand geprüft |
| 53 | `GetEmptyIndex` | `0x0051CF00` | 92 | von Hand geprüft |

34 von 54 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `StreamRead_sector` (`0x0051DA60`), `DeleteObject_sector` (`0x0051DCE0`), `ApmObject` (`0x0051E350`), `~ApmObject_body` (`0x0051E470`), `scalar_deleting_dtor` (`0x0051E530`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB90` | `Zeiger `ApmMap`` | `OnAddModule`, `AddObject` |
| `this+0xB94` | ``ApAdmin` der Objekte (`m_clObjects`)` | `GetObject`, `GetObjectSequence`, `AddObject` |
| `this+0xC48` | ``ApAdmin` der Vorlagen` | `GetObjectTemplate`, `GetObjectTemplateSequence` |
| `this+0xDB0` | `Verzeichnisname der Objektdateien (`wsprintf "%s%s"`)` | `StreamRead(Sektor)` |
| `this+0xEB0` | `Entfernungstakt / -liste` | `ProcessRemove` |
| `Objekt+0x04` | `Objekt-ID` | `AddObject`, `AddRemoveObject` |
| `Objekt+0x1F0` | `Status` | `UpdateStatus` |
| `Objekt+0x1FC` | `Liste der angehängten Objekte (Kindverknüpfung)` | `DestroyObject`, `ProcessRemove` |
| `Objekt+0x200` | `Takt des Entfernens` | `AddRemoveObject`, `ProcessRemove` |
| `Objekt+0x204` | ``m_bAddedToWorld`` | `AddObject`, `DeleteObject` |

## Vtable und Aufbau

`ApmObject` (Weltobjekte und ihre Vorlagen) hat die Vtable `0x008B2410`: Slot 0 Löschwrapper (`0x0051E530`), Slot 1 `OnAddModule` (`0x0051E300`), Slot 2 `OnInit` (`0x0051C6F0`). Konstruktor `0x0051E350` (280 Byte, baut die Verwaltungen auf), Destruktorrumpf `0x0051E470`. `OnAddModule` meldet bei der Datenverwaltung die Strom-Rückrufe der Vorlagen (`ObjectTemplateReadCB` `0x0051D200`, `ObjectTemplateWriteCB` `0x0051CA90`) und der Objekte (`ObjectReadCB` `0x0051DDC0`, `ObjectWriteCB` `0x0051CAE0`) an und holt `ApmMap` (`this+0xB90`). `OnInit` richtet drei `ApAdmin`-Verwaltungen ein (Objekte, Vorlagen, Entfernen). `OnIdle` (`0x0051D150`) ist ein Sprung auf `ProcessRemove` (`0x0051CD70`).
Die Objekte stehen in einer `ApAdmin` bei `this+0xB94`, die Vorlagen in einer bei `this+0xC48` (belegt durch die Zugriffsfunktionen `GetObject`/`GetObjectTemplate` und die beiden `…Sequence`-Funktionen), die Entfernungsliste und der Entfernungstakt bei `this+0xEB0`.

## Objekte und Vorlagen

`GetObject(OID)` (`0x0051C7F0`) und `GetObjectTemplate(TID)` (`0x0051C8E0`) sind 30-Byte-Einzeiler um `ApAdmin::GetObject`; `GetObjectSequence` (`0x0051C770`) und `GetObjectTemplateSequence` (`0x0051C8B0`) um `GetObjectSequence`. `SetMaxObject` (`0x0051C790`), `SetMaxObjectTemplate` (`0x0051C8D0`) und `SetMaxObjectRemove` (`0x0051CD60`) sind 11-Byte-Einzeiler (Aufrufer: Modulregistrierung `0x00410EB0`). `AttachObjectData` und `AttachObjectTemplateData` sind die modulübergreifend geteilten `SetAttachedModuleData`-Einzeiler mit Kennung 0 (`0x00511140`) bzw. 1 (`0x0053A4F0`); [`AgcmObject`](AgcmObject.md):OnAddModule` ruft beide.
`AddObject(Objekt)` (`0x0051C810`, 148 Byte) trägt das Objekt ein, übergibt es der Karte (`ApmMap::AddObject` `0x005138D0`; setzt `m_bAddedToWorld`) und löst den Rückruf `ON_ADD_OBJECT` (Kennung 3) aus. `DestroyObject` (`0x0051C7A0`) gibt ein Objekt frei; `DeleteObject(Objekt, bForce, bImmediate)` (`0x0051D160`) meldet es bei der Karte ab (`0x00513990`) und gibt es entweder sofort frei oder trägt es (über `AddRemoveObject` `0x0051CE50`) in die Entfernungsliste ein; `DeleteObject(Sektor, …)` (`0x0051DCE0`) tut das für alle Objekte eines Sektors; `ProcessRemove` (`0x0051CD70`) räumt die Entfernungsliste nach 3.000 bzw. 5.000 Takten. `UpdateStatus` (`0x0051CC90`) setzt den Status (`+0x1F0`) und löst Rückruf 2 aus.

## Laden und Strom

`StreamReadTemplate` (`0x0051C900`, 393 Byte) liest die Vorlagendatei über `ApModuleStream`, legt je Abschnitt eine Vorlage an und trägt sie in die Vorlagenverwaltung ein. `StreamRead(Box, Teil, Datei)` (`0x0051D550`, 991 Byte) liest eine Objektdatei; `StreamRead(Sektor)` (`0x0051DA60`, 311 Byte) bildet daraus den Dateinamen `Obj%05d.ini` mit der Divisionsnummer `(ArrayX/16)·100 + ArrayZ/16` (die Argumentfolge im Binary ist Z zuerst, dann X) und ruft die vorige Fassung. `ObjectReadCB` (`0x0051DDC0`) liest Position, Skalierung, Drehwinkel und Octree-Kennungen eines Objekts (`ParsePOS` `0x0051CED0`: Format `%f,%f,%f`; `GetEmptyIndex` `0x0051CF00` sucht eine freie Objektnummer je Division).

## Rückrufe

Die Setzfunktionen der Rückrufe sind gemeinsame `SetCallback`-Einzeiler: `SetCallbackInitObject` (Kennung 0) `0x006DA540`, `SetCallbackRemoveObject` (1) `0x0053A200`, `SetCallbackUpdateStatus` (2) `0x0057BED0`, `SetCallbackAddObject` (3) `0x005766B0`, `SetCallbackLoadSector` (4) `0x0057BEF0` und `SetCallbackLoadError` (5) `0x00574590`. Belegt sind sie durch die Aufrufer `AgcmObject::OnAddModule` (0, 1), [`AgpmEventPointLight`](AgpmEventPointLight.md):OnAddModule` (3, 1) und [`ApmOcTree`](ApmOcTree.md):OnInit` (der Rumpf für Kennung 5 ist dort `ApmMap::SetCallbackLoadSector`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gelesen sind `OnAddModule`, `OnInit`, `AddObject(Objekt)`, `ProcessRemove` (Kopf), `AddRemoveObject`, `UpdateStatus`, `ParsePOS`, `GetEmptyIndex`, `DeleteObject(Objekt)` und der Aufbau von `StreamRead(Sektor)`; `StreamReadTemplate`, `StreamRead(Box, Teil, Datei)`, `ObjectReadCB`/`ObjectWriteCB` und die Vorlagen-Rückrufe sind über Zeichenketten (z. B. `Position`, `Scale`, `DegreeX`, `OcTreeIDNum`, `ObjectType`), Aufrufbeziehungen und Größe zugeordnet, nicht Zeile für Zeile verglichen.
- Die Aussage, dass die nicht gefundenen 20 Methoden keinen direkten Aufruf im Bereich haben, beruht auf einem Scan der `call`/`jmp`-Ziele; Einbau in andere Funktionen (z. B. `DeleteAllObject` in `OnDestroy`) ist möglich und nicht ausgeschlossen.
- Die Rümpfe der `SetCallback`- und `SetAttachedModuleData`-Einzeiler sind über die gleiche Form und je einen Aufrufer belegt, nicht über einen Byte-Vergleich aller Klassen.
- Dass `0x0051C770` und `0x0051C7F0` zur Objekt-Verwaltung (`+0xB94`) und `0x0051C8B0`/`0x0051C8E0` zur Vorlagen-Verwaltung (`+0xC48`) gehören, folgt aus den Offsets in ihren Rümpfen; die Zuordnung der Vorlagen-Verwaltung zu `+0xC48` bestätigt auch `OnInit` nicht einzeln.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 5, gemeinsamer Rumpf: 6, nicht im Client: 3, ohne Kandidat: 13.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmObject`](AgcmObject.md), [`AgpmEventPointLight`](AgpmEventPointLight.md), [`ApmMap`](ApmMap.md), [`ApmOcTree`](ApmOcTree.md)
- **Erwähnt in:** [`AgcmAmbOcclMap`](AgcmAmbOcclMap.md), [`AgcmCamera2`](AgcmCamera2.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmUIDebugInfo`](AgcmUIDebugInfo.md), [`AgpmEventPointLight`](AgpmEventPointLight.md), [`ApmMap`](ApmMap.md)
