# AgpmFactors (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des gemeinsamen Moduls `AgpmFactors` (Faktoren: Charakterwerte, Schaden, Verteidigung, Gegenstandswerte; Lesen/Schreiben, Berechnen, Strom) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Disassembly (`x86dis.py`), Funktionstabelle (`ftable.py`), Vtable `0x008B17A0`, Typtabellen im Datenbereich, EP8-Quelle `Modules/APublic/AgpmFactors/AgpmFactors.cpp`, `AgpdFactors.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 63 von 126 Quellmethoden sind zugeordnet (dazu Konstruktor und Destruktorrumpf). Zugeordnet sind der Wertezugriff (alle zehn `GetValue`/`SetValue`/`GetValuePointer`-Fassungen), Anlegen/Löschen/Setzen der Faktoren, `CalcFactor`, `ReflectPacket`, `CopyFactor`, die Stromfunktionen, die Namenstabellen und die kleinen Zugriffe auf Rasse, Klasse, Stufe, Erfahrung und Punkte.
- **Nicht im Binary gefunden:** `MakePacket*` (Paketbau, in der Quelle nur im Server), `UpdateFactor` (beide), `InitUpdateFactor`, `CompareFactor`, `CalcResultFactor`/`CalcPercentFactor`, `AddResultFactor`, `CopyFactorNotZero`, `CopyFactorStatus`, `GetAttackableRange` und zwei weitere `IsInRange`-Fassungen (mit `AuBLOCKING`), `SetExp`, `GetMurderPoint`, `GetLevelBefore`, `GetSkillLevel`, `AllocAgpdFactor`/`FreeAgpdFactor`, `IsMustSend`, `PrintDataTypeLog` und `FindCharacterClassIndex(Rasse, Klasse)`. Ob sie eingebaut oder entfernt sind, ist offen.
- **Die 13 `SetCallbackUpdateFactor…`-Funktionen** liegen an den gemeinsamen `SetCallback`-Rümpfen (Kennungen 0 bis 12, siehe Liste unten); sie sind hier nicht einzeln den Adressen zugeordnet.
- **Hinweis:** `OnAddModule` meldet nur den Strom-Rückruf der Namensdatei (`AddStreamCallback(0, CharacterTypeStreamReadCB, CharacterTypeStreamWriteCB)`) an; `OnInit` und `OnDestroy` sind leer.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgpmFactors.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x0050C3E0` | 25 | vtable/String |
| 1 | `OnInit` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 2 | `OnIdle` | `0x0067FAB0` | 8 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf, ein Argument)` (vom Linker zusammengefaltet) |
| 3 | `OnDestroy` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf)` (vom Linker zusammengefaltet) |
| 4 | `InitFactor` | `0x0050C400` | 25 | von Hand geprüft |
| 5 | `DestroyFactor` | `0x0050B100` | 112 | von Hand geprüft |
| 6 | `DestroyFactor` | `0x0050B170` | 63 | von Hand geprüft |
| 7 | `SetFactor` | `0x0050C420` | 79 | von Hand geprüft |
| 8 | `SetFactor` | `0x0050B1B0` | 110 | von Hand geprüft |
| 9 | `SetFactors` | `0x0050B220` | 160 | von Hand geprüft |
| 10 | `GetFactor` | `0x0050B2C0` | 29 | von Hand geprüft |
| 11 | `IsUseFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 12 | `ReflectPacket` | `0x0050C470` | 414 | von Hand geprüft |
| 13 | `ReflectPacket` | `0x0050CF50` | 2152 | von Hand geprüft |
| 14 | `MakePacketFactor` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 15 | `MakePacketFactors` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 16 | `MakePacketFactorsOneType` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 17 | `MakePacketResult` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 18 | `MakePacketFactorsCharView` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 19 | `MakePacketFactorsCharHPMax` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 20 | `MakePacketFactorsCharHP` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 21 | `MakePacketFactorsItemView` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 22 | `MakePacketMoney` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 23 | `MakePacketItem` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 24 | `MakePacketItemRestrict` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 25 | `MakePacketLevel` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 26 | `MakePacketFactorDiffer` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 27 | `MakePacketFactorDiffer` | – | | nicht im Client-Binary gefunden: in der Quelle ruft sie nur der Server auf (Paketbau) |
| 28 | `GetAttackableRange` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 29 | `IsInRange` | `0x0050B2E0` | 129 | von Hand geprüft |
| 30 | `IsInRange` | `0x0050A540` | 243 | von Hand geprüft |
| 31 | `IsInRange` | – | | nicht zugeordnet |
| 32 | `IsInRange` | – | | nicht zugeordnet |
| 33 | `UpdateFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 34 | `UpdateFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 35 | `CalcFactor` | `0x0050D7C0` | 1335 | von Hand geprüft |
| 36 | `CalcFactor` | `0x0050C610` | 867 | von Hand geprüft |
| 37 | `InitUpdateFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 38 | `InitUpdateFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 39 | `InitCalcFactor` | `0x0050C980` | 58 | von Hand geprüft |
| 40 | `StreamRead` | `0x0050C9C0` | 213 | von Hand geprüft |
| 41 | `StreamReadFactor` | `0x0050B370` | 783 | von Hand geprüft |
| 42 | `StreamWrite` | `0x0050B690` | 140 | von Hand geprüft |
| 43 | `StreamWriteFactor` | `0x0050A640` | 432 | von Hand geprüft |
| 44 | `FindCharacterRaceIndex` | `0x0050B720` | 137 | von Hand geprüft |
| 45 | `FindCharacterClassIndex` | `0x0050A7F0` | 203 | von Hand geprüft |
| 46 | `FindCharacterClassIndex` | – | | nicht zugeordnet |
| 47 | `GetCharacterRaceName` | `0x0050B7B0` | 79 | von Hand geprüft |
| 48 | `GetCharacterClassName` | `0x0050B800` | 161 | von Hand geprüft |
| 49 | `GetCharacterGenderName` | `0x0050B8B0` | 73 | von Hand geprüft |
| 50 | `ParseCharacterTypeClass` | `0x0050A8C0` | 236 | von Hand geprüft |
| 51 | `CharacterTypeStreamReadCB` | `0x0050B900` | 364 | vtable/String |
| 52 | `CharacterTypeStreamWriteCB` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf); die Quelle gibt nur TRUE zurück` (vom Linker zusammengefaltet) |
| 53 | `CharacterTypeStreamRead` | `0x0050A9B0` | 238 | von Hand geprüft |
| 54 | `CharacterTypeStreamWrite` | `0x0067AC90` | 6 | gleiche Adresse wie `return TRUE (gemeinsamer Rumpf); die Quelle gibt nur TRUE zurück, im Binary keine eigene Funktion nachgewiesen` (vom Linker zusammengefaltet) |
| 55 | `GetFactorTypeName` | – | | nicht im Binary gefunden (kleine Funktion der Namenstabelle; vermutlich eingebaut) |
| 56 | `GetFactorININame` | – | | nicht im Binary gefunden (kleine Funktion der Namenstabelle; vermutlich eingebaut) |
| 57 | `GetFactorDetail` | – | | nicht im Binary gefunden (kleine Funktion der Namenstabelle; vermutlich eingebaut) |
| 58 | `CopyFactorNotNull` | `0x0050DD00` | 172 | von Hand geprüft |
| 59 | `CopyFactorNotZero` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 60 | `CopyFactorNotZero` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 61 | `CopyFactor` | `0x0050CAA0` | 265 | von Hand geprüft |
| 62 | `CopyFactorStatus` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 63 | `AddResultFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 64 | `AddResultFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 65 | `SetOwnerFactor` | `0x0050CC10` | 97 | von Hand geprüft |
| 66 | `SetCallbackUpdateFactorParty` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 67 | `SetCallbackUpdateFactorUI` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 68 | `SetCallbackUpdateFactorSkillPoint` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 69 | `SetCallbackUpdateFactorHeroicPoint` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 70 | `SetCallbackUpdateFactorDamage` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 71 | `SetCallbackUpdateFactorView` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 72 | `SetCallbackUpdateFactorMovement` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 73 | `SetCallbackUpdateFactorBonusExp` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 74 | `SetCallbackUpdateFactorHp` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 75 | `SetCallbackUpdateFactorMp` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 76 | `SetCallbackUpdateFactorMurdererPoint` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 77 | `SetCallbackUpdateFactorCharismaPoint` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 78 | `SetCallbackUpdateFactorDurability` | – | | gemeinsamer `SetCallback`-Rumpf (Kennung nach der Reihenfolge der Registrierung); nicht einzeln zugeordnet |
| 79 | `CompareFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 80 | `CompareFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 81 | `CalcResultFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 82 | `CalcPercentFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 83 | `GetValuePointer` | `0x0050AAC0` | 138 | von Hand geprüft |
| 84 | `GetValue` | `0x0050AB50` | 213 | von Hand geprüft |
| 85 | `SetValue` | `0x0050AC30` | 198 | von Hand geprüft |
| 86 | `GetValue` | `0x0050AD00` | 202 | von Hand geprüft |
| 87 | `SetValue` | `0x0050ADD0` | 214 | von Hand geprüft |
| 88 | `GetValuePointer` | `0x0050BA90` | 60 | von Hand geprüft |
| 89 | `GetValue` | `0x0050BAD0` | 81 | von Hand geprüft |
| 90 | `SetValue` | `0x0050CC80` | 97 | von Hand geprüft |
| 91 | `GetValue` | `0x0050BB30` | 81 | von Hand geprüft |
| 92 | `SetValue` | `0x0050CCF0` | 100 | von Hand geprüft |
| 93 | `IsFloatValue` | `0x0050AEB0` | 89 | von Hand geprüft |
| 94 | `GetRace` | `0x0050BB90` | 38 | von Hand geprüft |
| 95 | `CheckRace` | `0x0050BBC0` | 71 | von Hand geprüft |
| 96 | `GetGender` | `0x0050BC10` | 39 | von Hand geprüft |
| 97 | `GetClass` | `0x0050BC40` | 39 | von Hand geprüft |
| 98 | `CheckClass` | `0x0050BC70` | 72 | von Hand geprüft |
| 99 | `GetLevel` | `0x0050BCC0` | 39 | von Hand geprüft |
| 100 | `GetLevelBefore` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 101 | `GetLevelLimited` | `0x0050BCF0` | 23 | von Hand geprüft |
| 102 | `GetMurderPoint` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 103 | `GetExp` | `0x0050BD10` | 52 | von Hand geprüft |
| 104 | `GetMaxExp` | `0x0050BD50` | 52 | von Hand geprüft |
| 105 | `SetExp` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 106 | `SetMaxExp` | `0x0050CD60` | 84 | von Hand geprüft |
| 107 | `GetHP` | – | | eingebaut in die Aufrufer (11 Zeilen, Zugriff über `GetFactor`) |
| 108 | `GetMaxHP` | – | | eingebaut in die Aufrufer (11 Zeilen, Zugriff über `GetFactor`) |
| 109 | `GetMP` | – | | eingebaut in die Aufrufer (11 Zeilen, Zugriff über `GetFactor`) |
| 110 | `GetMaxMP` | – | | eingebaut in die Aufrufer (11 Zeilen, Zugriff über `GetFactor`) |
| 111 | `GetSP` | – | | eingebaut in die Aufrufer (11 Zeilen, Zugriff über `GetFactor`) |
| 112 | `GetMaxSP` | – | | eingebaut in die Aufrufer (11 Zeilen, Zugriff über `GetFactor`) |
| 113 | `GetSkillPoint` | `0x0050BD90` | 40 | von Hand geprüft |
| 114 | `GetSkillLevel` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 115 | `GetHeroicPoint` | `0x0050BDC0` | 26 | von Hand geprüft |
| 116 | `DivideFactor` | `0x0050BDE0` | 106 | von Hand geprüft |
| 117 | `DivideFactor` | `0x0050AF10` | 280 | von Hand geprüft |
| 118 | `InitDamageFactors` | `0x0050CDC0` | 387 | von Hand geprüft |
| 119 | `AllocAgpdFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 120 | `FreeAgpdFactor` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 121 | `SetFactorDataName` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 122 | `AllocFactorType` | `0x0050B030` | 96 | von Hand geprüft |
| 123 | `FreeFactorType` | `0x0050B090` | 74 | von Hand geprüft |
| 124 | `IsMustSend` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |
| 125 | `PrintDataTypeLog` | – | | kein Verweis im Binary gefunden (kein Aufruf in der Umgebung, keine Verwendung der zugehörigen Felder); Verbleib offen |

63 von 126 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgpmFactors_body` (`0x0050A490`), `GetValue_float` (`0x0050AD00`), `SetValue_float` (`0x0050ADD0`), `~AgpmFactors` (`0x0050B0E0`), `DestroyFactor_type` (`0x0050B170`), `SetFactor_ptr` (`0x0050B1B0`), `IsInRange_factor` (`0x0050B2E0`), `GetValuePointer_factor` (`0x0050BA90`), `GetValue_factor` (`0x0050BAD0`), `GetValue_factor_float` (`0x0050BB30`), `DivideFactor_factor` (`0x0050BDE0`), `AgpmFactors` (`0x0050BF50`), `SetValue_factor` (`0x0050CC80`), `SetValue_factor_float` (`0x0050CCF0`), `ReflectPacket_factor` (`0x0050CF50`), `CalcFactor_factor` (`0x0050D7C0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x08` | `Modulname (40 Byte)` | Konstruktor |
| `this+0xB84` | `Anzahl Rassen (Namenstabelle)` | `FindCharacterRaceIndex`, `CharacterTypeStreamReadCB` |
| `this+0xB88 / 0xB8C` | `Anzahl Geschlechter / Klassen` | `GetCharacterGenderName`, `GetCharacterClassName` |
| `this+0xB90` | `Rassen (68 Byte je Eintrag)` | `FindCharacterRaceIndex`, `GetCharacterRaceName` |
| `this+0x10E0` | `Geschlechter (68 Byte je Eintrag)` | `GetCharacterGenderName` |
| `this+0x1630` | `Klassentabelle (Rassen × 20 Klassen)` | `FindCharacterClassIndex`, `GetCharacterClassName` |
| `this+0x1A984` | `Paket-Beschreibungen je Typ (`0x12914` Byte je Typ)` | `ReflectPacket`, `CalcFactor` |
| `this+0x8070` | `Paket-Beschreibung des ganzen Faktors` | `ReflectPacket`, `CalcFactor` |
| `this+0x1311B0` | `Speicherpools der 15 Typen (`0x24` Byte je Typ)` | `AllocFactorType`, `FreeFactorType` |
| `this+0x1311D0 + Typ·0x24` | `Typindex des Pools (−1: kein Pool)` | `AllocFactorType`, `FreeFactorType` |
| `Faktor+0x04` | ``m_bPoint`` | `CopyFactor`, Konstruktor `AgpdFactor` |
| `Faktor+0x08` | `Zeiger je Typ (15), beginnend mit Result` | alle Zugriffe |
| `0x0094D488` | ``g_alFactorDetail` (Untertyp, Anzahl)` | `GetValue`, `SetValue`, `CalcFactor` |
| `0x0094D500` | ``g_nFactorSize` (16 Bit je Typ)` | `AllocFactorType`, `SetFactor` |
| `0x0094D520` | ``g_bFactorUseFloat` (je Typ 20 Ganzzahlen)` | `GetValue`, `SetValue`, `IsFloatValue` |
| `0x0094CF60 / 0x0094CFD8` | `Namen der Typen / ihrer Werte (Strom)` | `StreamRead`, `StreamReadFactor`, `StreamWrite*` |

## Vtable, Aufbau und Tabellen

`AgpmFactors` (Faktoren: Werte von Charakteren, Gegenständen und Fertigkeiten in 15 Typen) liegt im Binary bei `0x0050A490`–`0x0050DD00`, zwischen [`AgpmCharacter`](AgpmCharacter.md) davor und danach. Vtable `0x008B17A0`: 0 Löschwrapper (`0x0050B0E0`, ruft den Destruktorrumpf `0x0050A490`), 1 `OnAddModule` (`0x0050C3E0`), 2 `OnInit` und 6 `OnDestroy` am gemeinsamen Rumpf `0x0067AC90`, 3 bis 5 `OnIdle` usw. am Rumpf `0x0067FAB0`. Der Konstruktor (`0x0050BF50`, 1.162 Byte) trägt den Modulnamen „AgpmFactors“ ein, baut 15 Paketobjekte (je `0x12914` Byte, bei `this+0x1A984`), 15 Speicherpools (je `0x24` Byte bei `this+0x1311B0`) und die Namenstabelle auf und legt über `0x004EA680`/`0x004E9F80` die Paketformate an (Feldtypen 12 = Teilpaket, 5 = Ganzzahl, 0xFF = Ende); ein weiteres Paketobjekt bei `this+0x8070` beschreibt den ganzen Faktor mit seinen 15 Teilpaketen.
Die Faktoren stehen in `AgpdFactor` (`+0` Vtable, `+4` `m_bPoint`, `+8` 15 Zeiger, einer je Typ in der Reihenfolge Result, CharStatus, CharType, CharPoint, CharPointMax, CharPointRecoveryRate, Attribute, Damage, Defense, Attack, Item, Dirt, Price, Owner, Agro). Drei Tabellen im Datenbereich beschreiben die Typen: `g_alFactorDetail` bei `0x0094D488` (8 Byte je Typ: Untertyp oder −1/0, Anzahl), `g_nFactorSize` bei `0x0094D500` (16 Bit je Typ, Größe in Byte) und `g_bFactorUseFloat` bei `0x0094D520` (je Typ 20 Ganzzahlen, ob der Wert als Festkommazahl mit Faktor 100 gespeichert wird); die Namen der Typen und ihrer Werte stehen bei `0x0094CF60` (Anfangs-/Endzeichenkette) und `0x0094CFD8`.
Die Namenstabellen für Rasse, Klasse und Geschlecht (`AgpmFactorCharTypeNameSet`) liegen bei `this+0xB84`: Anzahl Rassen `+0xB84`, Geschlechter `+0xB88`, Klassen `+0xB8C`, Rassen ab `+0xB90` (68 Byte je Eintrag: Nummer, Name), Geschlechter ab `+0x10E0`, Klassentabelle ab `+0x1630` (je Rasse 20 Klassen). `CharacterTypeStreamReadCB` (`0x0050B900`) liest die Schlüssel `Race`, `Class` und `Gender` (Format `%d:%s`); `CharacterTypeStreamWriteCB` ist der Rumpf `0x0067AC90` (die Quelle gibt nur TRUE zurück).

## Anlegen und Löschen der Faktoren

`AllocFactorType` (`0x0050B030`) holt den Speicher des Typs aus dem Pool des Typs (`ApMemoryPool` `0x004E3F80`) oder mit `new`, wenn der Pool nicht eingerichtet ist (Typindex −1), und nullt ihn; `FreeFactorType` (`0x0050B090`) gibt ihn zurück. `DestroyFactor(Faktor)` (`0x0050B100`) gibt rekursiv zuerst den Result-Faktor und dann alle 15 Typen frei (mit `IsBadReadPtr` geprüft); `DestroyFactor(Faktor, Typ)` (`0x0050B170`) einen Typ; `InitFactor` (`0x0050C400`) ruft sie. `SetFactor(Ziel, Quelle, Typ)` (`0x0050C420`) und `SetFactor(PVOID*, …)` (`0x0050B1B0`) legen den Typ an und kopieren ihn; `SetFactors` (`0x0050B220`) macht das für alle Bits einer Maske; `GetFactor` (`0x0050B2C0`) liefert den Zeiger. `InitCalcFactor` (`0x0050C980`) zerstört den Faktor und legt einen Typ neu an (`InitFactor` ist dabei eingebaut).

## Werte lesen und schreiben

Die rekursive Zugriffskette läuft über die Typtabelle: `GetValuePointer` (`0x0050AAC0` für Rohzeiger, `0x0050BA90` für `AgpdFactor`), `GetValue` (Ganzzahl `0x0050AB50`/`0x0050BAD0`, Gleitkomma `0x0050AD00`/`0x0050BB30`) und `SetValue` (Ganzzahl `0x0050AC30`/`0x0050CC80`, Gleitkomma `0x0050ADD0`/`0x0050CCF0`) gehen bei einem Typ mit Untertyp (`g_alFactorDetail`) um `Größe · Index` weiter; bei einem Blatt (−1) prüfen sie den Index gegen die Anzahl und lesen bzw. schreiben das Feld; Festkommawerte werden mit 100 geteilt bzw. multipliziert. Die Fassungen für `AgpdFactor` holen den Typ zuerst (`GetFactor` bzw. beim Schreiben `SetFactor`). `IsFloatValue` (`0x0050AEB0`) liefert den Festkomma-Schalter. `DivideFactor` (`0x0050AF10` Rohzeiger, `0x0050BDE0` Faktor) teilt alle Werte; für den 64-Bit-Wert der Erfahrung (Typ 3 und 4, Index 3) wird ein 64-Bit-Aufruf benutzt.
Kleine Zugriffe: `GetRace`/`GetGender`/`GetClass` (`0x0050BB90`/`0x0050BC10`/`0x0050BC40`) lesen Nummer 0/1/2 aus dem Typ CharType (Result-Faktor zuerst), `CheckRace`/`CheckClass` (`0x0050BBC0`/`0x0050BC70`) prüfen eine Bitmaske (0 bedeutet alle); `GetLevel` (`0x0050BCC0`, Wert 7 der CharStatus), `GetLevelLimited` (`0x0050BCF0`, Wert 13), `GetExp`/`GetMaxExp` (`0x0050BD10`/`0x0050BD50`, 64 Bit aus zwei Werten), `GetSkillPoint` (`0x0050BD90`, Dirt-Wert 5, Result-Faktor zuerst), `GetHeroicPoint` (`0x0050BDC0`, Dirt-Wert 7), `SetMaxExp` (`0x0050CD60`) und `SetOwnerFactor` (`0x0050CC10`, Typ Owner mit Kennung und Zeiger). `GetHP`, `GetMP` u. a. sind in den Aufrufern eingebaut.

## Aktualisieren, Berechnen und Kopieren

`CalcFactor` (`0x0050D7C0` für `AgpdFactor`, 1.335 Byte, sechs Argumente; `0x0050C610` für Rohzeiger) addiert bzw. subtrahiert (`bAdd`) die Werte des Aktualisierungsfaktors auf den Faktor, begrenzt bei Bedarf auf 0 und meldet Änderungen von Stufe und Bewegung über den Rückruf (`EnumCallback` Kennung 0 und 1); die 64-Bit-Werte der Erfahrung werden mit Übertrag gerechnet. `ReflectPacket` (`0x0050C470` für einen Typ, `0x0050CF50` für den ganzen Faktor mit vier Argumenten) übernimmt ein Paket in den Faktor und löst dabei die Rückrufe aus: 7 und 8 (Stufe), 0 und 1 (Bewegung, Stufe, Werte), 5 (HP-Maximum), 3 (Schaden), 6, 2 (Fertigkeitspunkt), 9, 11, 10 und 12; danach ruft sie `InitDamageFactors`.
`InitDamageFactors` (`0x0050CDC0`) sichert den Punktefaktor in den Zwischenspeicher und nullt elf Werte des Punktefaktors (Index 9 bis 19). `CopyFactor` (`0x0050CAA0`, sechs Argumente) kopiert einen oder alle Typen, `CopyFactorNotNull` (`0x0050DD00`) kopiert alle gesetzten Typen außer dem Result-Faktor (`CopyFactor` ist hier eingebaut).

## Strom und Pakete

`StreamRead` (`0x0050C9C0`) liest die Werte zwischen den Zeilen „FactorStart“/„FactorEnd“, `StreamReadFactor` (`0x0050B370`) einen Typ (Schlüssel aus `0x0094CFD8`, Werte mit `atoi` bzw. `atof`, Festkomma × 100); `StreamWrite` (`0x0050B690`) und `StreamWriteFactor` (`0x0050A640`) schreiben ebenso. `CharacterTypeStreamRead` (`0x0050A9B0`) liest die Namensdatei über `ApModuleStream`; `ParseCharacterTypeClass` (`0x0050A8C0`) zerlegt einen Klassenwert („Nummer:Name:Name…“).
Reichweite: `IsInRange(Position, Position, Angriffsreichweite, Trefferreichweite, …)` (`0x0050A540`) rechnet den Abstand der Punkte (Wurzel) und liefert, ob er kleiner oder gleich der Summe ist; sonst den Punkt auf der Strecke; `IsInRange` mit zwei Faktoren (`0x0050B2E0`, sieben Argumente) holt die Reichweiten aus dem Attack-Typ des Result-Faktors (erster Wert beim Angreifer als Angriffsreichweite, Ersatzwert 100 bei Wert ≤ 0; erster Wert beim Ziel als Trefferreichweite) und ruft die Fassung mit Zahlen.

## Namenssuche

`FindCharacterRaceIndex` (`0x0050B720`) und `FindCharacterClassIndex(Klasse)` (`0x0050A7F0`) vergleichen den Namen mit den Tabellen und liefern die Nummer (−1 bei Misserfolg); `GetCharacterRaceName` (`0x0050B7B0`), `GetCharacterClassName` (`0x0050B800`) und `GetCharacterGenderName` (`0x0050B8B0`) suchen den Namen zur Nummer.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen (Typreihenfolge, Größen- und Festkommatabellen, 15 Typen).

## Grenzen

- Gelesen (Dekompilat) sind die Zugriffskette (`GetValue`/`SetValue`/`GetValuePointer`, beide Fassungen), `SetFactor`, `SetFactors`, `DestroyFactor`, `AllocFactorType`, `FreeFactorType`, `CopyFactor` (Struktur), `InitDamageFactors`, `StreamReadFactor`, `StreamWriteFactor`, `StreamWrite`, `StreamRead`, `CharacterTypeStreamReadCB`, `CharacterTypeStreamRead`, `ParseCharacterTypeClass`, die Namenssuche, `IsInRange` (beide Fassungen), `DivideFactor` und die Zugriffe auf Rasse, Stufe, Erfahrung und Punkte. `CalcFactor` und `ReflectPacket` sind in Aufbau und Rückrufkennungen gelesen, aber nicht mit der Quelle Zeile für Zeile verglichen; die Rückrufkennungen (0 bis 12) sind aus dem Binary abgelesen und nicht einzeln den Namen der `SetCallbackUpdateFactor…`-Funktionen zugeordnet.
- Die Zuordnung `GetLevelLimited` (Wert 13), `GetHeroicPoint` (Wert 7) und `GetSkillPoint` (Wert 5) folgt aus den Indizes der Aufzählungen in `AgpdFactors.h` (CharStatus: Level 7, BeforeLevel 12, LimitedLevel 13; Dirt: SkillLevel 4, SkillPoint 5, HeroicPoint 7), nicht aus Aufrufern.
- `CopyFactorNotNull` (`0x0050DD00`) ist aus der Form (Schleife über die gesetzten Typen ohne Result) geschlossen; die Funktion hat keine Zeichenkette und nur einen Aufrufer. `InitCalcFactor` (`0x0050C980`) ist dagegen über 10 Aufrufer und die Form (Zerstören, dann neuer Typ) zugeordnet.
- Die Funktionen `0x0050BEA0` (Namen mit 32 Zeichen in eine Struktur kopieren), `0x0050BE50` und `0x0050BEF0` (Konstruktoren der Namenstabelle) und `0x0050DDC0` (Vergleich zweier Positionen mit Schwelle) gehören zu Hilfsstrukturen und sind nicht Teil der Quellmethoden; `0x0050DDC0` liegt am Ende des Bereichs und gehört vielleicht schon zu `AgpmCharacter`.
- Dass die Funktionen unter „nicht im Binary gefunden“ fehlen, beruht auf dem Fehlen von Aufrufstellen und eindeutigen Merkmalen im Bereich `0x0050A470`–`0x0050DE30`; Aufrufe aus anderen Modulen wurden nicht für jede einzeln gesucht.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 3, gemeinsamer Rumpf: 16, nicht im Client: 29, ohne Kandidat: 20.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmCharacter`](AgpmCharacter.md)
- **Erwähnt in:** [`AgcmAuction`](AgcmAuction.md), [`AgcmCashMall`](AgcmCashMall.md), [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmGlyph`](AgcmGlyph.md), [`AgcmGuild`](AgcmGuild.md), [`AgcmItem`](AgcmItem.md), [`AgcmSkill`](AgcmSkill.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIGuideMessage`](AgcmUIGuideMessage.md), [`AgcmUIParty`](AgcmUIParty.md), [`AgcmUIPvP`](AgcmUIPvP.md), [`AgpmCombat`](AgpmCombat.md), [`AgpmUnion`](AgpmUnion.md)
