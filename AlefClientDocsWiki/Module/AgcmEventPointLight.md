# AgcmEventPointLight (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmEventPointLight` (Punktlichter an Objekten: Erzeugen, Ein-/Ausschalten, Stream) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmEventPointLight/AgcmEventPointLight.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; die Lichtverwaltung (Hinzufügen/Entfernen/Ein-/Ausschalten) und alle Rückrufe sind zugeordnet. Nicht als eigene Funktion vorhanden ist `GetPointLightClientData` (eingebaut).
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmEventPointLight.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `GetPointLightClientData` | – | | in die Aufrufer eingebaut |
| 1 | `OnAddModule` | `0x006849A0` | 249 | vtable/String |
| 2 | `TogglePointLight` | `0x006842B0` | 18 | as-register |
| 3 | `OnInit` | `0x00684680` | 681 | vtable/String |
| 4 | `OnPointLightCreate` | `0x00683E30` | 85 | Callback-Registrierung |
| 5 | `OnPointLightDestroy` | `0x00683E90` | 34 | Callback-Registrierung |
| 6 | `PointLightStreamWriteCB` | `0x00683EC0` | 129 | Callback-Registrierung |
| 7 | `PointLightStreamReadCB` | `0x00683F50` | 208 | Callback-Registrierung |
| 8 | `CBOnPointLightAddObject` | `0x00684930` | 105 | Callback-Registrierung |
| 9 | `CBOnPointLightRemoveObject` | `0x00684330` | 95 | Callback-Registrierung |
| 10 | `AddLightToArray` | `0x006845F0` | 130 | von Hand geprüft |
| 11 | `RemoveLightToArray` | `0x006842D0` | 92 | von Hand geprüft |
| 12 | `AddLight` | `0x00684020` | 247 | von Hand geprüft |
| 13 | `RemoveLight` | `0x00684120` | 116 | von Hand geprüft |
| 14 | `EnablePointLight` | `0x006841A0` | 120 | von Hand geprüft |
| 15 | `CBSkyChange` | `0x00684220` | 37 | Callback-Registrierung |

15 von 16 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmEventPointLight` (`0x006844D0`), `~AgcmEventPointLight` (`0x00684560`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA8` | `Index des angehängten Moduldatenblocks (16 Bit)` | `CBOnPointLightAddObject` |
| `this+0xBAC / 0xBB0 / 0xBB4` | `Anfang / Ende / Kapazität des Licht-Vektors (Element 8 Byte)` | `AddLightToArray`, `RemoveLightToArray` |
| `this+0xBB8` | `Punktlichter aktiv (`m_bEnablePointLight`)` | `EnablePointLight`, `CBOnPointLightAddObject` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmEventPointLight` (`0x006845D0`, Löschwrapper), 1 `OnAddModule` (`0x006849A0`), 2 `OnInit` (`0x00684680`), 3 bis 5 `0x0067FAB0`, 6 und 7 `0x0067AC90`, 8 `0x004E3420`. Der Konstruktor (`0x006844D0`) trägt `AgcmEventPointLight` ein, der Destruktorrumpf ist `0x00684560`. `OnAddModule` holt [`ApmEventManager`](ApmEventManager.md), [`AgpmEventPointLight`](AgpmEventPointLight.md), [`AgcmRender`](AgcmRender.md), [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md) (und [`AgcmEventNature`](AgcmEventNature.md), falls vorhanden), meldet `CBSkyChange` bei der Natur an, hängt über `SetAttachedModuleData` einen Datenblock von `0x40` Byte an Objekte (Erzeuger `OnPointLightCreate`, Zerstörer `OnPointLightDestroy`), registriert die Stream-Funktionen (`PointLightStreamReadCB`/`…WriteCB`) und die Rückrufe `CBOnPointLightAddObject` (Kennung 0) und `CBOnPointLightRemoveObject` (Kennung 1).

## Lichter

Die Lichter liegen in einem `std::vector` (Element: Zeiger auf Objekt und auf die Client-Daten, 8 Byte, Anfang `this+0xBAC`, Ende `+0xBB0`). `AddLightToArray` (`0x006845F0`) prüft auf Duplikate und hängt an (die Vektor-Erweiterung ist `0x00684390`), `RemoveLightToArray` (`0x006842D0`) sucht, schiebt nach und verkürzt. `AddLight` (`0x00684020`, 247 Byte) erzeugt bei fehlendem Licht ein Punktlicht, setzt Farbe (Byte-Werte durch 255), Radius und einen eigenen Frame an der Position; `RemoveLight` (`0x00684120`) löst Frame und Licht, meldet es bei `AgcmRender` (Flag `0x1000000`, Objekt) bzw. `AgcmDynamicLightmap` (Flag `0x2000000`, Geometrie) ab und zerstört es. `EnablePointLight` (`0x006841A0`) schaltet bei geändertem Zustand (`this+0xBB8`) alle Lichter des Vektors ein (`AddLight`) oder aus (`RemoveLight`). `CBOnPointLightAddObject` (`0x00684930`) holt das Punktlicht-Ereignis des Objekts (Funktion `0x1E`), trägt es ein und fügt das Licht hinzu, wenn Punktlichter aktiv sind.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen die Quelle gelesen sind `AddLightToArray`, `RemoveLightToArray`, `AddLight`, `RemoveLight`, `EnablePointLight` und `CBOnPointLightAddObject` (Aufbau); `OnPointLightCreate`, `OnPointLightDestroy`, die Stream-Funktionen, `CBSkyChange`, `TogglePointLight` und `CBOnPointLightRemoveObject` waren schon über die Registrierung benannt und wurden hier nicht Zeile für Zeile gelesen.
- Die Bedeutung der Flags `0x1000000`/`0x2000000` (Objekt bzw. Geometrie) folgt aus der Quelle (`AGCPLF_AFFECT_OBJECT`/`…GEOMETRY`); die Konstantenwerte sind nicht gegen den Header geprüft.
- Die Feldnamen der Offsets sind aus der Verwendung gefolgert.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmDynamicLightmap`](AgcmDynamicLightmap.md), [`AgcmEventNature`](AgcmEventNature.md), [`AgcmRender`](AgcmRender.md), [`AgpmEventPointLight`](AgpmEventPointLight.md), [`ApmEventManager`](ApmEventManager.md)
- **Erwähnt in:** [`AgpmEventPointLight`](AgpmEventPointLight.md)
