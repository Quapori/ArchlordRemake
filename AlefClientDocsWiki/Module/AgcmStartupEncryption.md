# AgcmStartupEncryption (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmStartupEncryption` (Verbindungsaufbau mit Schlüsselaustausch, Anbindung an Login- und Spielserver) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtable, Aufrufgraph, Callback-Registrierung, EP8-Quelle `Modules/AClient/AgcmStartupEncryption/AgcmStartupEncryption.cpp`. Alle Adressen gelten nur für den 2017er Build. Die Verschlüsselung selbst (Funktionen `0x004F8xxx`) steht in `Netzwerk/Transform-Cipher.md` und den Login-Folgen.

## Kernbefund

- **Abdeckung:** siehe Zahl unten; alle elf Methoden sind zugeordnet.
- **Abweichungen:** keine festgestellt.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmStartupEncryption.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x00681900` | 330 | vtable/String |
| 1 | `SendRequestPublic` | `0x006812F0` | 172 | von Hand geprüft |
| 2 | `SendEncryptedRandom` | `0x006813A0` | 178 | von Hand geprüft |
| 3 | `CBAlgorithmType` | `0x00681460` | 77 | Callback-Registrierung |
| 4 | `CBPublic` | `0x006814B0` | 349 | Callback-Registrierung |
| 5 | `CBComplete` | `0x00681620` | 163 | Callback-Registrierung |
| 6 | `CBDynCodePublic` | `0x006816D0` | 130 | Callback-Registrierung |
| 7 | `CBDynCodePrivate` | `0x00681760` | 130 | Callback-Registrierung |
| 8 | `CBConnectLoginServer` | `0x006817F0` | 77 | Callback-Registrierung |
| 9 | `CBConnectGameServer` | `0x00681840` | 70 | Callback-Registrierung |
| 10 | `CBReconnectLoginServer` | `0x00681890` | 68 | Callback-Registrierung |

11 von 11 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmStartupEncryption` (`0x006811D0`), `ctor_or_dtor` (`0x00681290`), `~AgcmStartupEncryption` (`0x006818E0`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0xB98 / 0xB9C / 0xBA0 / 0xBA4 / 0xBA8` | `Zeiger [`AgpmStartupEncryption`](AgpmStartupEncryption.md) / [`AgcmLogin`](AgcmLogin.md) / [`AgcmReturnToLogin`](AgcmReturnToLogin.md) / [`AgcmConnectManager`](AgcmConnectManager.md) / `AgcmCharacter`` | `OnAddModule` |
| `Verbindung+0xC8078` | `Verschlüsselungskontext der Verbindung (Schlüssel/IV)` | `CBPublic`, `CBDynCode…` |
| `Verbindung+0xC807C` | `aktive Rolle (1 = öffentlich, 2 = privat)` | `CBComplete` |
| `Verbindung+0xC80BC` | `Servertyp (0 / 1)` | `CBComplete`, `SendRequestPublic` |

## Vtable und Aufbau

Vtable-Slots: 0 `~AgcmStartupEncryption` (`0x006818E0`, Löschwrapper), 1 `OnAddModule` (`0x00681900`), 2 `OnInit` (`0x0067AC90`), 3 bis 5 `0x0067FAB0`, 6 und 7 `0x0067AC90`, 8 `0x004E3420`. Der Konstruktor (`0x006811D0`) trägt `AgcmStartupEncryption` ein, der Destruktorrumpf ist `0x00681290`. `OnAddModule` holt `AgpmStartupEncryption` (`this+0xB98`), `AgcmLogin` (`+0xB9C`), `AgcmReturnToLogin` (`+0xBA0`), `AgcmConnectManager` (`+0xBA4`) und `AgcmCharacter` (`+0xBA8`) und meldet neun Rückrufe an, in dieser Reihenfolge: `CBAlgorithmType`, `CBPublic`, `CBComplete`, `CBDynCodePublic`, `CBDynCodePrivate` (bei `AgpmStartupEncryption`), dann `CBConnectLoginServer`, `CBConnectGameServer` und `CBReconnectLoginServer` bei `AgcmConnectManager` bzw. den Login-Modulen.

## Ablauf des Schlüsselaustauschs

Beim Verbinden fordern `CBConnectLoginServer` (`0x006817F0`), `CBConnectGameServer` (`0x00681840`) und `CBReconnectLoginServer` (`0x00681890`) über `SendRequestPublic` (`0x006812F0`) den öffentlichen Schlüssel an (Paket mit Operation 0, gesendet an die Verbindung der übergebenen NID); ist ein Merker (Feld `+4` des von `0x004EA6D0` gelieferten Objekts) nicht gesetzt, springen sie stattdessen direkt in den normalen Ablauf (`0x0065D100`, `0x005A21F0` bzw. `0x006DA110`); was der Merker bedeutet, ist nicht geklärt.
`CBAlgorithmType` (`0x00681460`) übernimmt zwei Zahlen (Algorithmus-Kennungen) aus dem Paket (nur wenn die Längenangabe 8 ist) in `AgpmStartupEncryption+0x18` und `+0x1C`. `CBPublic` (`0x006814B0`, 349 Byte) setzt mit dem empfangenen Schlüssel den Kontext der Rolle 1 (Funktion `0x004F8ED0` auf dem Kontext der Verbindung, `Verbindung+0xC8078`), fragt die Schlüssellänge ab (`0x004F8FF0`), erzeugt eine Zufallsfolge dieser Länge (`0x00878580` mit 0xFF), setzt damit den Kontext der Rolle 2 (`0x004F8F40`), verschlüsselt die Zufallsfolge (`0x004F8FB0`) und schickt sie mit `SendEncryptedRandom` (`0x006813A0`, Paketoperation 2 mit Schlüssel und Länge). Das entspricht dem in den Login-Berichten beschriebenen Ablauf.
`CBDynCodePublic` (`0x006816D0`) und `CBDynCodePrivate` (`0x00681760`) setzen aus dem Paket jeweils einen Schlüssel (Rolle 1 über `0x004F8ED0`, Rolle 2 über `0x004F8F40`) und geben TRUE. `CBComplete` (`0x00681620`) setzt die aktive Rolle der Verbindung (`Verbindung+0xC807C`) auf 2 und startet je nach Servertyp (`Verbindung+0xC80BC`: 0 = Spielserver, 1 = Login-Server) den weiteren Ablauf (`0x005A21F0` bzw. `0x0065D100`/`0x006DA110`).

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Gegen das Dekompilat gelesen sind alle Rückrufe außer `OnAddModule` im Detail (nur Aufrufreihenfolge); die Bedeutung der Funktionen `0x004F8xxx` (Schlüssel setzen, Länge, Verschlüsseln) stammt aus den Login-Berichten und der Live-Analyse, nicht aus diesem Modul.
- `SendRequestPublic` und `SendEncryptedRandom` (`0x006812F0`, `0x006813A0`) sind über ihre Aufrufer (`CBConnect…`, `CBPublic`) und die Paketoperation zugeordnet; ihre Rümpfe sind einander bis auf die Paketfelder gleich.
- Welche Bedeutung die Servertyp-Werte 0 und 1 haben, ist aus dem Verhalten von `CBComplete` gefolgert (0 → `0x005A21F0`, 1 → Login-Rückkehr).

## Querverweise

- **Erwähnt Module:** [`AgcmConnectManager`](AgcmConnectManager.md), [`AgcmLogin`](AgcmLogin.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgpmStartupEncryption`](AgpmStartupEncryption.md)
- **Erwähnt in:** [`AgcmReturnToLogin`](AgcmReturnToLogin.md)
