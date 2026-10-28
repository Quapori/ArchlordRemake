# AgcmReturnToLogin (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmReturnToLogin` (Zurück zur Charakterauswahl: Anfrage, Schlüssel, Wiederverbinden zum Login-Server) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmReturnToLogin/AgcmReturnToLogin.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** vollständig: alle elf Methoden sind zugeordnet. Die drei `SetCallback…`-Einzeiler liegen an Adressen gemeinsamer Rümpfe (`SetCallback` mit fester Kennung 0, 1 bzw. 2): `SetCallbackRequestFailed` bei `0x006DA540` (zusammen mit [`AgcmWorld`](AgcmWorld.md):SetCallbackGetCharCount`), `SetCallbackEndProcess` bei `0x0053A200` und `SetCallBackReconnectLoginServer` bei `0x0057BED0`.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmReturnToLogin.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x006DA330` | 197 | vtable/String |
| 1 | `SendPacketRequest` | `0x006DA040` | 78 | von Hand geprüft |
| 2 | `SetCallbackRequestFailed` | `0x006DA540` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf mit Kennung 0 (auch `AgcmWorld::SetCallbackGetCharCount`)` (vom Linker zusammengefaltet) |
| 3 | `SetCallbackEndProcess` | `0x0053A200` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf mit Kennung 1` (vom Linker zusammengefaltet) |
| 4 | `SetCallBackReconnectLoginServer` | `0x0057BED0` | 20 | gleiche Adresse wie `gemeinsamer `SetCallback`-Rumpf mit Kennung 2` (vom Linker zusammengefaltet) |
| 5 | `CBReceiveRequestFailed` | `0x006DA090` | 23 | Callback-Registrierung |
| 6 | `CBReceiveAuthKey` | `0x006DA260` | 200 | Callback-Registrierung |
| 7 | `CBEndProcess` | `0x006DA0B0` | 58 | Callback-Registrierung |
| 8 | `ReconnectLoginServer` | `0x006DA1B0` | 176 | von Hand geprüft |
| 9 | `CBSocketOnConnect` | `0x006DA0F0` | 23 | von Hand geprüft |
| 10 | `SendReconnectLoginServer` | `0x006DA110` | 102 | von Hand geprüft |

11 von 11 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmReturnToLogin` (`0x006D9FF0`), `~AgcmReturnToLogin` (`0x006DA180`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xBA0` | `Zeiger `AgcmCharacter` (dessen `+0x15964` ist die eigene Charakter-ID)` | `SendPacketRequest` |
| `this+0xBAC` | ``m_lAuthKey`` | `ReconnectLoginServer`, `SendReconnectLoginServer` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmReturnToLogin` (`0x006DA180`), 1 `OnAddModule` (`0x006DA330`), 2 `OnInit` (`0x0067AC90`), 3 bis 5 `0x0067FAB0`, 6 und 7 `0x0067AC90`, 8 und 9 `0x004E3420`. Der Konstruktor (`0x006D9FF0`) trägt den Modulnamen `AgcmReturnToLogin` ein und setzt `m_lAuthKey` (`this+0xBAC`) auf 0. `OnAddModule` holt [`AgpmCharacter`](AgpmCharacter.md), [`AgpmReturnToLogin`](AgpmReturnToLogin.md), `AgcmCharacter`, [`AgcmConnectManager`](AgcmConnectManager.md) und [`AgcmLogin`](AgcmLogin.md) (Reihenfolge der Quelle) und meldet `CBReceiveRequestFailed` (`0x006DA090`), `CBReceiveAuthKey` (`0x006DA260`) und `CBEndProcess` (`0x006DA0B0`) an.

## Pakete und Rückrufe

`SendPacketRequest` (`0x006DA040`) baut aus der eigenen Charakter-ID (Feld `+0x15964` von `AgcmCharacter`, Zeiger bei `this+0xBA0`) das Anfragepaket (`MakePacketRequest`) und sendet es, wenn es länger als der Kopf (12 Byte) ist. `SendReconnectLoginServer` (`0x006DA110`) baut das Paket mit Konto (`AgcmLogin+0xC4C`) und Schlüssel (`this+0xBAC`) und sendet es zum Login-Server (Sendeart 2, laut Quelle `ACDP_SEND_LOGINSERVER`; Sendeziel aus dem Verbindungsmanager). `CBEndProcess` (`0x006DA0B0`) und `CBReceiveRequestFailed` (`0x006DA090`) lösen die Rückrufe 1 bzw. 0 aus; `CBSocketOnConnect` (`0x006DA0F0`, 23 Byte) löst Rückruf 2 (`RECONNECT_LOGINSERVER`) aus.
`ReconnectLoginServer` (`0x006DA1B0`) speichert den Schlüssel, kopiert die Server-Adresse (höchstens 23 Zeichen) – bei leerer Adresse aus `AgcmLogin+0xBD4` (`m_szIPAddress`) – und ruft die Verbindung des `AgcmConnectManager` (`0x006F4EC0`) mit `CBSocketOnConnect`; fehlt `AgcmLogin`, kehrt sie mit -1 zurück. Sie wird von `CBReceiveAuthKey` gerufen.

## CBReceiveAuthKey

`CBReceiveAuthKey` (`0x006DA260`, 200 Byte) ist Zeile für Zeile mit der Quelle abgeglichen: Prüfung der drei Zeiger, [`AgcmUIMain`](AgcmUIMain.md):OnClearSystemGrid` (`0x006066C0`), Socket-Manager `SetDestroyNormal` (`0x006FCEC0`), `AgpmCharacter::RemoveAllCharacters` (`0x005061E0`), `AgcmNatureEffect::StopNatureEffect(TRUE)` (`0x00638AF0`), bei vorhandenem [`AgcmUILogin`](AgcmUILogin.md) `OpenLoadingWindow(1)` (Rasse Mensch) und `SetLoginMode(5)` (`WAIT_MY_CHARACTER`), [`AgcmUIGuild`](AgcmUIGuild.md):InitMemberUIData` (`0x00777CC0`) und zuletzt `ReconnectLoginServer(Schlüssel, Adresse)`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die drei `SetCallback…`-Einzeiler sind über die Kennungen belegt: `CBReceiveRequestFailed`, `CBEndProcess` und `CBSocketOnConnect` lösen mit `EnumCallback` die Kennungen 0, 1 und 2 aus, und die Aufrufer in anderen Modulen passen zur Quelle (`AgcmUILogin`/[`AgcmTargeting`](AgcmTargeting.md) rufen `SetCallbackEndProcess` über `0x0053A200`; [`AgcmStartupEncryption`](AgcmStartupEncryption.md):OnAddModule` ruft `SetCallBackReconnectLoginServer` über `0x0057BED0`). Dass die Rümpfe wirklich mit denen anderer Klassen zusammengefaltet sind, folgt aus der gleichen Form (ein Aufruf `SetCallback(Kennung, Rückruf, Klasse)`), nicht aus einem Byte-Vergleich.
- Von den Modulzeigern sind nur `this+0xBA0` (`AgcmCharacter`) und `this+0xBAC` (Schlüssel) aus der Verwendung belegt; die übrigen liegen davor und sind nicht einzeln geprüft.
- `SendPacketRequest` hat im Binary nur einen Aufrufer (`0x0060F220`); dass dieser aus einem UI-Modul stammt, ist nicht geprüft.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 2.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmConnectManager`](AgcmConnectManager.md), [`AgcmLogin`](AgcmLogin.md), [`AgcmNatureEffect`](AgcmNatureEffect.md), [`AgcmStartupEncryption`](AgcmStartupEncryption.md), [`AgcmTargeting`](AgcmTargeting.md), [`AgcmUIGuild`](AgcmUIGuild.md), [`AgcmUILogin`](AgcmUILogin.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmWorld`](AgcmWorld.md), [`AgpmCharacter`](AgpmCharacter.md), [`AgpmReturnToLogin`](AgpmReturnToLogin.md)
- **Erwähnt in:** [`AgcmStartupEncryption`](AgcmStartupEncryption.md), [`AgcmTargeting`](AgcmTargeting.md)
