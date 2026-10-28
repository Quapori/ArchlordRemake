# AgcAuth (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse der Client-Klasse `AgcAuth` (Anmeldung über Startparameter des Launchers; mit der abgeleiteten `AgcGPAuth` und dem Singleton `AuthManager`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Vtables, Aufrufgraph, EP8-Quelle `Modules/AClient/AgcAuth/AgcAuth.cpp`, `AgcGPAuth.cpp`, `AgcAuth.h`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 9 von 10 Quellmethoden sind zugeordnet. `setProperty_impl(int)` fehlt im Binary, weil die Quelle `setProperty` nirgends mit einer Zahl aufruft.
- **Korrektur:** Die Namen von `0x0064F6D0` (vorher `~AgcAuth`) und `0x006013B0` (vorher `AgcGPAuth::init`) waren falsch; siehe Vtable-Abschnitt.
- **Abweichungen:** keine festgestellt; die Quelle der Basisklasse deckt sich mit dem Binary. Die Auswertung der Startparameter steht in `AgcGPAuth` (nicht Teil der zehn Methoden dieser Datei).

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcAuth.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `init` | `0x0064F310` | 285 | von Hand geprüft |
| 1 | `init` | `0x0064F6D0` | 144 | von Hand geprüft |
| 2 | `error_handling` | `0x0064F240` | 49 | von Hand geprüft |
| 3 | `final_process` | `0x007C6910` | 1 | gleiche Adresse wie `gemeinsamer Leer-Rumpf (`ret`), zusammengefaltet mit `AgcWindow::OnEditDeactive`` (vom Linker zusammengefaltet) |
| 4 | `isTest` | `0x0064F280` | 14 | von Hand geprüft |
| 5 | `setProperty_impl` | – | | nicht zugeordnet |
| 6 | `setProperty_impl` | `0x0064F430` | 126 | von Hand geprüft |
| 7 | `setProperty_impl` | `0x0064F4B0` | 127 | von Hand geprüft |
| 8 | `login` | `0x0064F530` | 204 | vtable/String |
| 9 | `encrypt` | `0x0064F290` | 121 | vtable/String |

9 von 10 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `~AgcAuth_body` (`0x00601310`), `scalar_deleting_dtor` (`0x00601390`), `init_cstr` (`0x0064F310`), `setProperty_impl_bool` (`0x0064F430`), `setProperty_impl_string` (`0x0064F4B0`), `setProperty_string` (`0x0064F600`), `init_string` (`0x0064F6D0`), `setProperty_bool` (`0x0073E280`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `this+0x08` | `Kopfknoten der Eigenschaften-Map `propertyMap_` (std::map, Schlüssel/Wert als Zeichenketten)` | `setProperty`, `~AgcAuth` |
| `AuthManager 0x009E2A3C` | `statische `AgcGPAuth`-Instanz` | `AuthManager` |

## Vtable und Aufbau

`AgcAuth` ist kein Modul, sondern eine Basisklasse für die Anmeldung über die Startparameter. Vtable `0x008BF0B8`: Slot 0 `init(std::string&)` (`0x0064F6D0`), 1 `error_handling` (`0x0064F240`), 2 `final_process` (`0x007C6910`, gemeinsamer Leer-Rumpf, identisch mit `AgcWindow::OnEditDeactive`), 3 `login` (`0x0064F530`), 4 `encrypt` (`0x0064F290`), 5 Löschwrapper (`0x00601390`, Rumpf des Destruktors `0x00601310`). Die vorherigen Namen `AgcAuth::~AgcAuth` (`0x0064F6D0`) und `AgcGPAuth::init` (`0x006013B0`) waren vertauscht: `0x0064F6D0` ist `init`, `0x006013B0` der Löschwrapper von `AgcGPAuth`.
Die tatsächlich benutzte Klasse ist `AgcGPAuth` (Vtable `0x008BF0D4`, gleiche Slots, aber Slot 0 `init` bei `0x0073E320`, Slot 3 `login` bei `0x0073E660`); `error_handling` (`0x0064F240`) und `encrypt` (`0x0064F290`) sind mit `AgcAuth` geteilt. Das Singleton baut `AuthManager()` (`0x006013D0`, statische Instanz bei `0x009E2A3C`, setzt erst die `AgcAuth`-, dann die `AgcGPAuth`-Vtable); es wird von Start- und Login-Code (`0x00410510`, `0x0060F900`, `0x0060FAC0`, `0x0065E660`, `0x00748D50` u. a.) gerufen.

## Eigenschaften und Start

`init(char const*)` (`0x0064F310`, 285 Byte) prüft zuerst `isTest` (`0x0064F280`, Datei `NoExcuteAuth.arc` über den Ignorier-Helfer `0x004F9C10`); ist die Datei da, kehrt es mit TRUE zurück und überspringt die Anmeldung. Sonst ruft es virtuell `init(std::string&)` mit der Befehlszeile (leere Zeichenkette bei NULL). `AgcAuth::init(std::string&)` (`0x0064F6D0`) speichert das Wort hinter dem letzten Leerzeichen als Eigenschaft `gamestring`.
Die Eigenschaften liegen in einer `std::map<string,string>` (`propertyMap_`, bei `this+8`); `setProperty` wandelt den Schlüssel in Kleinbuchstaben (`0x0064F600` für Zeichenketten, `0x0073E280` für `bool`) und ruft `setProperty_impl` (`0x0064F4B0` Zeichenkette, `0x0064F430` `bool` als `"true"`/`"false"`). `setProperty_impl(int)` ist im Binary nicht vorhanden: die Quelle ruft `setProperty` nirgends mit einer Zahl auf.
`AgcGPAuth::init` (`0x0073E320`, 809 Byte) ist der Weg, über den der Client mit Startparametern des Launchers arbeitet: bei vorhandener `NoExcuteAuth.arc` setzt es `AutoLogin` auf `false`; sonst muss die Befehlszeile `2:` enthalten, danach `Konto|Spielzeichenkette`: das Konto wird `member_id`, der Rest plus `|` und die MAC-Adresse (`GetAdaptersInfo`, erste Ethernet-Karte, Format `%02x-…`) wird `gamestring`, und `autologin` wird `true`. Schlägt die Adapterabfrage fehl, erscheint eine Meldung („Cannot read local MAC Address“) und `init` liefert FALSE.

## Anmelden und Verschlüsseln

`AgcAuth::login` (`0x0064F530`) trägt `member_id` und das Passwort `autologin` bei [`AgcmLogin`](AgcmLogin.md) ein (`SetIDPassword`), verbindet mit dem Login-Server (`ConnectLoginServer`) und zeigt, falls [`AgcmUIManager2`](AgcmUIManager2.md) da ist, den Wartedialog mit der Meldung `LOGIN_WAITING`. `AgcGPAuth::login` (`0x0073E660`, 164 Byte) benutzt stattdessen das Passwort `autopwd` und ruft nach dem Eintragen die Verbindungsfunktion `0x0060C030`. `encrypt` (`0x0064F290`) verschlüsselt Konto und Passwort nacheinander mit MD5 (`AuMD5Encrypt::EncryptString`, `0x004F95A0`) und liefert FALSE, wenn ein Zeiger fehlt oder ein Schritt scheitert.
`error_handling` (`0x0064F240`) zeigt „The game client is loaded only through the official website“ und öffnet bei Bestätigung `http://archlord.webzen.com`.

## Abweichungen von der EP8-Quelle

- Keine Abweichung von der EP8-Quelle in den gelesenen Funktionen.

## Grenzen

- Die Reihenfolge der Überladungen von `setProperty_impl` (int, bool, string) und von `init` (Zeiger, Zeichenkette) ist an den Rümpfen festgemacht, nicht an den Symbolnamen: `0x0064F430` setzt „true“/„false“ (bool), `0x0064F4B0` übernimmt eine Zeichenkette, `0x0064F310` ruft virtuell die Zeichenketten-Fassung, `0x0064F6D0` ist diese Fassung.
- Der Wert des Wartedialog-Textes `LOGIN_WAITING` und die Verbindung über `0x0060C030` (bei `AgcGPAuth::login`) sind nicht weiter verfolgt.
- Die Offsets sind nur für die Map (`+8`) belegt; `md5Encrypt_` liegt davor und ist nicht einzeln vermessen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 2, nicht im Client: 4.

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgcmLogin`](AgcmLogin.md), [`AgcmUIManager2`](AgcmUIManager2.md)
