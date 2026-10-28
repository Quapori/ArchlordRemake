# AgcmUIArchlord (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIArchlord` (Archlord-Meldungen und Wächter-Effekte) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph und Registrierungen, EP8-Quelle `Modules/AClient/AgcmUIArchlord/AgcmUIArchlord.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 12 von 12 Quellmethoden sind zugeordnet; die Zuordnung wurde hier gegen das Dekompilat geprüft (Anmeldereihenfolge, Textverzweigungen, `SetTextEffect`-Konstanten).
- **Meldungen:** vier Schritte und fünf Meldungs-IDs, jeweils mit eigenem UI-Text.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIArchlord.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00698150` | 304 | vtable/String |
| 1 | `CBGuardInfo` | `0x00697DD0` | 138 | Callback-Registrierung |
| 2 | `CBSetArchlord` | `0x00697E60` | 125 | Callback-Registrierung |
| 3 | `CBCancelArchlord` | `0x00697EE0` | 125 | Callback-Registrierung |
| 4 | `CBSetGuard` | `0x00697F60` | 132 | Callback-Registrierung |
| 5 | `CBCancelGuard` | `0x00697FF0` | 132 | Callback-Registrierung |
| 6 | `CBCurrentStep` | `0x00698080` | 186 | Callback-Registrierung |
| 7 | `CBMessageId` | `0x00697B20` | 102 | Callback-Registrierung |
| 8 | `CBGrant` | `0x00697BA0` | 23 | Callback-Registrierung |
| 9 | `CBPlaySetNewArchlordSound` | `0x00697BC0` | 39 | Callback-Registrierung |
| 10 | `SetTextEffect` | `0x00697BF0` | 299 | Zeichenkette |
| 11 | `AddEvent` | `0x00697D20` | 40 | Zeichenkette |

12 von 12 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIArchlord` (`0x00697A80`), `~AgcmUIArchlord` (`0x00697D50`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBA4` | `Ereignis-ID `Notice_New_Archlord`` | `AddEvent`, `CBPlaySetNewArchlordSound` |

## Vtable

Vtable bei `0x008CE47C`: Slot 0 Destruktor `0x00697D50`, 1 `OnAddModule` (`0x00698150`), 2/6/7 der gemeinsame `return TRUE`-Rumpf `0x0067AC90` (u. a. `OnInit`, `OnDestroy`).

## Callbacks (OnAddModule, 0x00698150)

Holt [`AgpmArchlord`](AgpmArchlord.md), [`AgcmArchlord`](AgcmArchlord.md) und [`AgcmUIManager2`](AgcmUIManager2.md) und meldet bei `AgpmArchlord` neun Callbacks an – in derselben Reihenfolge wie die Quelle:

| Anmeldung | Handler | Adresse |
|---|---|---|
| Archlord gesetzt | `CBSetArchlord` | `0x00697E60` |
| Archlord aufgehoben | `CBCancelArchlord` | `0x00697EE0` |
| Wächter gesetzt | `CBSetGuard` | `0x00697F60` |
| Wächter aufgehoben | `CBCancelGuard` | `0x00697FF0` |
| Wächter-Information | `CBGuardInfo` | `0x00697DD0` |
| aktueller Schritt | `CBCurrentStep` | `0x00698080` |
| Meldungs-ID | `CBMessageId` | `0x00697B20` |
| Ereignis gewährt | `CBGrant` | `0x00697BA0` |
| neuer Archlord (Ton) | `CBPlaySetNewArchlordSound` | `0x00697BC0` |

Danach `AddEvent` (`0x00697D20`): ein UI-Ereignis `Notice_New_Archlord`.

## Meldungen

`CBCurrentStep` (`0x00698080`) wählt zum Schritt 1–4 (Dungeon, Belagerung, Archlord-Kampf, Ende) einen UI-Text (`0x282`–`0x285`), zeigt ihn als Effekt und als Systemmeldung. `CBMessageId` (`0x00697B20`) zeigt zu den Meldungs-IDs 0–4 je eine Systemmeldung (UI-Texte `0x286`–`0x289` und `0x290`; nicht aufeinanderfolgend, wie die Textnummern der Quelle). Die Verzweigungen entsprechen der Quelle.

## Text-Effekt (SetTextEffect, 0x00697BF0)

Zeigt den Text im Effektfenster: Schriftart 3, Skalierung 1,0, Farbe `0xFF00FF00` (grün), Dauer 5000 ms, mit Hintergrundbild `RegionInfo.png`; die senkrechte Lage ist 19 % der Fensterhöhe (einmalig berechnet, `static`). Zusatz- und Obertext werden vorher geleert. Alle Konstanten wurden aus den Daten der Exe gelesen und stimmen mit der Quelle überein.

## UI-Namen (aus dem Binary)

Die Namen stammen aus den Registrierungsfunktionen des Moduls (`0x00697D20`), nicht übersetzte Namen sind koreanisch (Codepage 949). `Id` ist der zweite Parameter (bei Anzeigen die Anzeige-ID). Eine mit `FUN_…` bezeichnete Funktion ist nicht benannt.

**Ereignis** (1)

| Name | Id | Handler |
|---|---:|---|
| `Notice_New_Archlord` | 0 | – |


## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- `CBGuardInfo`, `CBSetArchlord`, `CBCancelArchlord`, `CBSetGuard` und `CBCancelGuard` wurden nur nach ihrer Registrierung zugeordnet, ihr Inhalt (Texte mit eingesetzten Namen/Zahlen) wurde nicht einzeln gelesen.
- Die Server-Seite der Archlord-Pakete steht im Bericht [AgpmArchlord](AgpmArchlord.md).

## Querverweise

- **Erwähnt Module:** [`AgcmArchlord`](AgcmArchlord.md), [`AgcmUIManager2`](AgcmUIManager2.md), [`AgpmArchlord`](AgpmArchlord.md)
