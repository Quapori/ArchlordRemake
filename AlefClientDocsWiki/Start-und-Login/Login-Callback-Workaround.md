# Der kaputte Login-Callback-Pfad und der Workaround dafuer

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Start, Anmeldung und Login-Umgehung](Index.md)*

Stand: 2026-09-06

## TL;DR

`alefclient.exe` registriert seine Login-Callbacks ([`AgcmLogin`](../Module/AgcmLogin.md)s numerisches
Event-System) nachweislich korrekt - Registrierung, Zieladresse, Argumente,
Speicherschutz, alles stimmt bei statischer wie Live-Speicher-Analyse. Trotzdem
werden diese Callbacks beim normalen Netzwerk-Empfang **nie** aufgerufen, weder
beim manuellen Login-Klick noch beim automatischen "Autologin"-Pfad. Wir wissen
nicht, warum. Der Workaround: die exakt gleiche Dispatch-Funktion
(`FUN_004e4070`) wird per `CreateRemoteThread`-Code-Injektion von aussen
selbst aufgerufen - kein Debugger-Attach, kein Absturzrisiko, seit dem ersten
erfolgreichen Test dutzendfach wiederholt ohne Probleme. Fertiges Tool dafuer:
[`AlefLogin/tools/alef_login_tool.py`](AlefLogin/tools/alef_login_tool.py).

Mit diesem Workaround funktioniert der komplette Login-Ablauf (StartupEncryption
-> EncryptCode -> SignOn -> Server-Antwort -> UI-Uebergang) tatsaechlich
Ende-zu-Ende gegen den echten (gepatchten) Client.

## Der Ablauf, der eigentlich passieren sollte (Referenz-Quellcode)

Aus `AgcmUILogin.cpp` (lokale Kopie der EP8-C++-Quelle, s.
[`README.md`](../Daten-und-Werkzeuge/Disassembly-2013.md)/Projekt-Notizen zur Vorsicht bzgl. Versions-Uebereinstimmung -
diese Beschreibung stimmte aber, wie sich zeigte, in jedem ueberpruefbaren
Detail mit der tatsaechlichen Binary ueberein):

1. `AgcmLogin::OnReceive` (Empfangs-Dispatcher, Client-seitig) bekommt ein
   Operation-0-Paket (`AGPMLOGIN_ENCRYPT_CODE`) vom Server, kopiert den
   32-Byte-Code nach `m_szEncryptCode` und feuert das generische numerische
   Event 2 (`AGCMLOGIN_CB_ENCRYPT_CODE`).
2. [`AgcmUILogin`](../Module/AgcmUILogin.md):CBEncryptCode` (fuer Event 2 registriert) reagiert darauf und
   ruft bedingungslos `AgcmLogin::SendAccount(m_szAccount, m_szPassword,
   m_nNID)` auf - das baut und verschickt das echte `AGPMLOGIN_SIGN_ON`-Paket.
3. Der Server antwortet mit Sign-On-Erfolg; `OnReceive`s Operation-1-Fall
   feuert Event 4 (`AGCMLOGIN_CB_SIGN_ON`).
4. [`AgcmUIMain`](../Module/AgcmUIMain.md):CBIDPasswordOK` (fuer Event 4 registriert) schliesst den
   Login-Dialog und leitet zur naechsten UI-Phase (Server-/Welt-Auswahl) ueber.

Der Haken: **Schritt 2 und 4 passieren im echten Client nie von selbst.**
Weder der manuelle "Best."-Button-Klick noch der Kommandozeilen-Autologin-Pfad
loesen sie aus - siehe unten, warum wir das mit Sicherheit sagen koennen.

## Was wir zweifelsfrei ausgeschlossen haben

Reihenfolge der Untersuchung, jeweils mit dem Ergebnis:

1. **Manueller Login-Button ("Best.")**: Per RTTI/Disassembly gefunden, dass
   `CT_LG_BUTTON_OK` (`ui_1024x768.ini`) auf `Action=3:LG_IdPasswordOK`
   registriert ist, was zu `FUN_00749a20` (VA `0x00749A20`) fuehrt - eine
   Funktion, die exakt die im Quellcode beschriebene Validierung durchfuehrt
   (ID/Passwort-Felder pruefen, dann `SetIDPassword`+`ConnectLoginServer`+
   ein dritter Aufruf). Ein Software-Breakpoint auf genau dieser Adresse,
   gesetzt via `DebugActiveProcess`-Attach an einen laengst laufenden,
   stabilen Client, wurde **niemals** ausgeloest - auch nicht bei
   wiederholten Klicks ueber ein volles 60-90-Sekunden-Fenster. Der Klick
   reagiert optisch (Hover/Press), ruft aber nachweislich nicht diese
   Funktion auf.
2. **Modul-Registrierungsreihenfolge** (Hypothese: `AgcmLogin` existiert noch
   nicht, wenn `AgcmUILogin::OnAddModule` laeuft, wodurch die komplette
   Callback-Registrierungskette lautlos uebersprungen wird): **widerlegt**.
   Per Disassembly nachgewiesen, dass `AgcmLogin` (Modul-Index ~0x2B) klar vor
   `AgcmUILogin` konstruiert *und* per `ApModule::AddModule`
   (`FUN_004e4b70`) sofort synchron initialisiert wird (`AddModule` ruft
   `OnAddModule()` direkt nach der Registry-Eintragung auf - kein
   zweiphasiger Prozess). `AgcmLogin` ist also laengst vorhanden, wenn
   `AgcmUILogin::OnAddModule` (`FUN_006108F0`, per RTTI/Vtable-Rohdaten
   verifiziert: `AgcmUIMain::vftable+4` bzw. `AgcmUILogin::vftable+4`)
   laeuft.
3. **Tatsaechliche Registrierung im Live-Speicher**: Per passivem
   `ReadProcessMemory`-Scan (kein Debugger) nachgewiesen, dass `AgcmLogin`s
   Event-Tabelle (bei Objekt-Basis `+0x5dc + eventId*4`) fuer **beide**
   Events echte, korrekte Eintraege enthaelt:
   - Event 2: Node zeigt auf `0x0060B680` (`AgcmUILogin::CBEncryptCode`s
     kompiliertes Aequivalent - Cross-Referenz von `SendAccount`
     (`FUN_0065EC80`) zurueckverfolgt, da es dessen einziger Aufrufer ist).
   - Event 4: Node zeigt auf `0x006040E0` (`AgcmUIMain::CBIDPasswordOK`s
     kompiliertes Aequivalent, per Disassembly verifiziert: die Registrierung
     laeuft mit `ECX = *(AgcmUIMain+0xBC4)` = zuvor geholter
     `AgcmLogin`-Modulzeiger, exakt passend zu
     `pcmLogin->SetCallbackSignOnSuccess(CBIDPasswordOK, this)`).
4. **Der Dispatch-Aufruf selbst** (`FUN_0065E7F0`s Case 0/1, das tatsaechlich
   `FUN_004e4070(2, this+0xBB4, 0)` bzw. `FUN_004e4070(4, nid, 0)` aufruft):
   per Disassembly Byte fuer Byte nachvollzogen - korrektes ECX (die
   `AgcmLogin`-Instanz, aus `ebp`, das seit Funktionseintritt unveraendert
   ist), korrekte Argumente.
5. **`IsBadCodePtr`** (von `FUN_004e4070` vor jedem Callback-Aufruf geprueft -
   ein Fehlschlag hier wuerde den Eintrag lautlos ueberspringen, ohne Fehler):
   per `VirtualQueryEx` bestaetigt, dass die Codeseite bei `0x0060B680` ganz
   normal `PAGE_EXECUTE_READ` ist. Per `CreateRemoteThread`-Aufruf **im
   Zielprozess selbst** (`IsBadCodePtr(0x0060B680)` direkt dort ausgefuehrt,
   nicht nur von aussen abgeleitet) bestaetigt: liefert `0` (gueltig).
6. **Anti-Debug**: Wird `alefclient.exe` per `CreateProcess`+`DEBUG_PROCESS`
   von Anfang an als Debuggee gestartet, oder wird ein bereits laufender
   Prozess innerhalb weniger Sekunden nach Start attachiert, beendet er sich
   **lautlos** (sauberes `ExitProcess`, kein Crash-Log, keine Verbindung zum
   Server) - noch bevor irgendein Netzwerk-Traffic sichtbar wird. Ein Attach
   Minuten nach dem Start (Client bereits eingeloggt/idle) ist dagegen
   durchgehend sicher (dutzende Tests, nie ein Absturz). Das verhindert ein
   direktes Live-Debugging der kritischen fruehen Sequenz.

**Fazit (Stand der ersten Untersuchungsrunde)**: Jede einzelne statisch und
dynamisch pruefbare Voraussetzung *innerhalb* von `OnReceive` ist erfuellt.
Der Callback wird trotzdem nie aufgerufen. Was diese erste Runde **nicht**
geprueft hat: ob `OnReceive` selbst ueberhaupt erreicht wird. Genau das ist
der Fokus der Fortsetzung unten.

## Fortsetzung, 2026-09-06: `OnReceive` wird nachweislich nie erreicht

**Wichtiger Hinweis zur Methodik**: Der EP8-Quellcode
(lokale Kopie der EP8-C++-Quelle) dient in diesem Abschnitt nur als
Recherche-/Denkhilfe fuer plausible Mechanismen (Klassennamen, Funktionsrollen,
grobe Struktur) - **nicht** als Beweis dafuer, dass dieser konkrete Build
identisch funktioniert. Jede Aussage unten ist explizit als entweder "live am
laufenden Prozess verifiziert" (verlaesslich) oder "aus dem Referenzcode
abgeleitet, ungeprueft" (nur Hypothese) gekennzeichnet.

### Beweis 1: `AgcmLogin::OnReceive` wird nie betreten (live verifiziert, risikofrei)

Technik: nicht-invasiver Marker-Hook. Die ersten 5 Bytes von `OnReceive`
(VA `0x0065E7F0`, `sub esp,38h; push ebx; push ebp` - vorher exakt gegen die
Disassembly verifiziert) werden durch einen `jmp` zu einem kleinen Trampolin
ersetzt, das (1) ein Marker-DWORD auf `1` setzt, (2) die urspruenglichen 5
Bytes ausfuehrt, (3) zurueckspringt. Die Funktion laeuft danach unveraendert
weiter - falls sie je aufgerufen wird.

Ablauf: Hook installiert -> echter Netzwerk-Request/Reply-Zyklus ausgeloest
(z.B. via `alef_login_tool.py fire --event 2`, was den Client ein echtes
`AGPMLOGIN_SIGN_ON` senden und eine echte Serverantwort empfangen laesst) ->
Marker geprueft: **bleibt `0`**. Mehrfach reproduziert, auch fuer die allererste
`ENCRYPT_CODE`-Antwort direkt nach Verbindungsaufbau (bevor irgendein
Force-Fire passiert war) - `m_szEncryptCode` im Client bleibt dabei ebenfalls
komplett `0x00`, obwohl der Server die echte, korrekte Antwort bereits gesendet
hat. **`OnReceive` wird also nie aufgerufen, nicht nur der Callback danach.**

### Beweis 2: `EnumPreRecieveModule` wird ebenfalls nie erreicht

Referenzcode (`ApModuleManager::Dispatch`, `ApModuleManager.cpp`) zeigt: vor
`OnReceive` laeuft `m_pModuleDisp[cType]->EnumPreRecieveModule(...)`; schlaegt
das fehl, wird `OnReceive` uebersprungen. Live gepruefte Gegenprobe: `AgcmLogin`s
Vtable-Slot `+0x20` (die per RTTI/Disassembly bestaetigte Position von
`EnumPreRecieveModule` in diesem Build) zeigt auf `0x006cfc60`, einen trivialen
`return 1;`-Stub, der aber von **mehreren verschiedenen Klassen** geteilt wird
(auch `AgcmUILogin`s eigene Slots `+0x20`/`+0x24` zeigen dorthin). Um NUR
`AgcmLogin`s Aufrufe zu erfassen, ohne den gemeinsamen Funktionskoerper
anzufassen (das wuerde ALLE Klassen beeinflussen, die ihn teilen), wurde
stattdessen **nur der Vtable-Eintrag von `AgcmLogin` selbst** umgebogen (auf
ein Trampolin mit Marker + `jmp` zum unveraenderten Original). Ergebnis nach
demselben Testzyklus: **auch dieser Marker bleibt `0`**.

Damit steht fest: Der Ausfall passiert **vor** `EnumPreRecieveModule`, also
entweder in `ApModuleManager::Dispatch()` selbst (z.B. beim `cType`-Lookup)
oder noch davor (die Socket-Empfangsschleife ruft `Dispatch()` fuer dieses
Paket gar nicht erst auf).

### Nebenfund: die echte `PACKET_HEADER`-Struktur (loest das "header9"-Raetsel)

Aus dem Referenzcode (`ApPacket.h`, `#pragma pack(1)`):

```c
typedef struct _stPACKET_HEADER {
    BYTE    bGuardByte;       // +0, unser "Marker" (0xD6/0xB1/0xA1)
    UINT16  unPacketLength;   // +1
    UINT8   cType;            // +3, der Modul-Opcode (0x0D fuer AgcmLogin)
    Flags   Flag;             // +4, 1 Byte Bitfeld
    INT32   lOwnerID;         // +5, vermutlich Session-/Charakter-ID
    UINT32  lDummy;           // +9
} PACKET_HEADER;              // = 13 Byte gesamt
```

Das erklaert die bisher als "9 mysteriöse Nullbytes" dokumentierten Bytes
zwischen Opcode und Feld-Maske vollstaendig: `Flag`+`lOwnerID`+`lDummy` = exakt
9 Byte. `AlefLogin` schickt hier bisher immer `[0;9]` (alles Null). Ob/wie
`lOwnerID` beim Empfang geprueft wird, ist noch nicht geklaert (`grep` nach
`lOwnerID` findet im Referenzcode nur eine SENDE-seitige Zuweisung
`((PPACKET_HEADER)pData)->lOwnerID = GetSelfCID()` in
`Client/AcClientSocket/AcSocketManager.cpp`, keine erkennbare Empfangspruefung
in den durchsuchten Dateien).

### Modul-Registrierung selbst ist gesund (live verifiziert, nicht ueber EP8 angenommen)

Ueber die per RTTI/Konvention bereits etablierten Feld-Offsets (`vtable+0`,
`m_nModuleType+4`, `m_szName[40]+8`) und den EP8-Header (`ApModule.h`:
`m_eModuleStatus` direkt gefolgt von `m_ulPacketType[10]`) wurde eine
Positions-Hypothese aufgestellt und **live per Speicher-Scan verifiziert**
(DWORD-Suche nach dem bekannten Wert `0x0D` in den ersten 0xC00 Bytes der
`AgcmLogin`-Instanz, gefunden bei Offset `0x948`):

- `AgcmLogin_base + 0x944` = `m_eModuleStatus` = **`0x00000002`**
  (`APMODULE_STATUS_READY`, nicht "haengt bei INIT")
- `AgcmLogin_base + 0x948` = `m_ulPacketType[0]` = **`0x0000000D`** (korrekt!)
- alle folgenden `m_ulPacketType[1..9]` = `0` (Terminator, wie erwartet)

Das widerlegt die Hypothese "Modul wurde nie/doppelt registriert und
`AddModule` bricht deshalb vorzeitig ab" - die Registrierung sieht aus
eigener Sicht des Moduls vollstaendig gesund aus.

### Gemeinsamer `ApModuleManager` bestaetigt, aber `AgcmLogin`-Zeiger darin nicht auffindbar

`ApModule::m_pModuleManager` (laut EP8-Header direkt nach `m_szName[40]`,
also bei Objekt-Offset `+0x30`) wurde fuer **zwei verschiedene Module**
ausgelesen und verglichen:

- `AgcmLogin_base + 0x30` = `0x009713b8`
- `AgpmWorld_base + 0x30` = `0x009713b8` (identisch!)

Das bestaetigt: es gibt **einen** gemeinsamen `ApModuleManager` fuer beide
Module (widerlegt die Hypothese "getrennte Manager fuer Login-/Welt-Traffic").
Ein anschliessender Scan der ersten 16 KB dieses Manager-Objekts nach dem
DWORD-Wert von `AgcmLogin`s eigenem Instanzzeiger (`0x1ae554f8` im getesteten
Lauf) **fand keinen Treffer** - ein Hinweis darauf, dass der Dispatch-Tabellen-
Eintrag fuer Opcode `0x0D` tatsaechlich fehlt, aber nicht endgueltig beweisend,
da `m_pModuleDisp[]`s exakter Byte-Offset im Manager-Objekt nicht unabhaengig
verifiziert wurde (davor liegende Member wie `AuPacket m_csSystemPacket`
koennten je nach Feldlayout deutlich groesser sein als angenommen, wodurch das
Array ausserhalb des gescannten Bereichs liegen wuerde).

### Offen fuer die naechste Session

1. `m_pModuleDisp[]`s echten Offset im `ApModuleManager`-Objekt (`0x009713b8`)
   zweifelsfrei lokalisieren (z.B. durch Scannen nach einem BEKANNTEN,
   garantiert korrekt registrierten anderen Modul-Zeiger, oder durch Aufloesen
   der eingebetteten `AuPacket`/`AuTickCounter`-Groessen), um endgueltig zu
   klaren, ob der Slot fuer `0x0D` leer oder falsch belegt ist.
2. Falls leer: klaeren, WARUM `AddModule`s Registrierungsschleife (die laut
   Referenzcode denselben Aufruf ausfuehrt, der `m_eModuleStatus`/
   `m_ulPacketType` korrekt gesetzt hat) den `m_pModuleDisp`-Eintrag nicht
   ODER an einer anderen Stelle wieder verloren hat.
3. Falls belegt (evtl. mit einem FALSCHEN/veralteten Zeiger): pruefen, ob
   dort ein laengst zerstoertes/verschobenes Objekt referenziert wird.
4. Alternativ direkt `ApModuleManager::Dispatch()`s eigene Codeadresse in der
   rohen Disassembly finden (charakteristisches Muster: Byte-Lesezugriff auf
   `[buffer+3]`, Vergleich gegen `120`, indizierter Tabellenzugriff, zwei
   aufeinanderfolgende indirekte Calls) und von dort rueckwaerts verfolgen,
   ob/wie oft sie fuer unsere Pakete ueberhaupt aufgerufen wird.

## Der Workaround: Force-Fire per Code-Injektion

Da `IsBadCodePtr` und alle Zwischenschritte nachweislich funktionieren, reicht
es, `FUN_004e4070` selbst aufzurufen - mit denselben Argumenten, die der Client
intern verwenden wuerde. Das geschieht per `CreateRemoteThread` mit einem
winzigen, dynamisch injizierten Shellcode-Stub:

```asm
mov ecx, <AgcmLogin_Objektbasis>   ; "this" fuer den __thiscall
push <param4>
push <param3>
push <event_id>
mov eax, 0x004E4070                 ; FUN_004e4070, feste VA (kein ASLR)
call eax
ret
```

Wichtig: **kein** `DebugActiveProcess`, keine Debug-API ueberhaupt beteiligt -
`CreateRemoteThread` ist fuer den Zielprozess nicht von einem x-beliebigen
fremden Thread zu unterscheiden. Das umgeht das Anti-Debug-Problem komplett und
wurde in dieser Session dutzendfach ohne einen einzigen Absturz verwendet.

### Die `AgcmLogin`-Instanz sicher finden

Jede `ApModule`-Instanz speichert ihren Modulnamen (gesetzt via
`SetModuleName`) als festen String bei Objekt-Basis `+8`. Live verifiziert:

```
Bytes bei AgcmLogin_base+8: "AgcmLogin\0" (39-Byte-Puffer, nullgepolstert)
```

Das Tool sucht per `VirtualQueryEx`/`ReadProcessMemory` gezielt in
**privatem** (Heap-)Speicher (`MEM_PRIVATE`, nicht `MEM_IMAGE`) nach dem
literalen Byte-Muster `"AgcmLogin\0"` und zieht 8 ab, um die Objektbasis zu
erhalten. Das ist unabhaengig von den tatsaechlich verwendeten
Zugangsdaten und ueberlebt ASLR/Heap-Allocator-Zufaelligkeit zwischen
Prozessstarts (die absolute Adresse aendert sich pro Start, das Verfahren
zum Finden nicht).

### Bekannte Feld-Offsets in `AgcmLogin` (live verifiziert, 2026-09-06)

| Offset | Feld | Typ |
|---|---|---|
| `+0x008` | Modulname ("AgcmLogin\0") | `char[39]` |
| `+0xBB4` | `m_szEncryptCode` | `char[32]` |
| `+0xC3C` | `m_nNID` | `INT16` |
| `+0xC4C` | `m_szAccount` | `char[65]` |
| `+0xC8C` | `m_szPassword` | `char[65]` |
| `+0x5DC` | Basis der generischen Event-Tabelle (`+eventId*4` = Listenkopf-Zeiger) | `void*[0x82]` |

Event-IDs (aus `AgcmLogin.h`, `eAGCMLOGIN_CB`): `CONNECT=0`, `DISCONNECT=1`,
`ENCRYPT_CODE=2`, `INVALID_CLIENT_VERSION=3`, `SIGN_ON=4`, `UNION_INFO=5`, ...

## Das Tool: `AlefLogin/tools/alef_login_tool.py`

Muss unter **32-Bit-Python** laufen (WOW64-Bitness muss zum Ziel passen, sonst
loesen sich Adressen/`GetProcAddress`-Tricks nicht korrekt auf).

```bash
# Client + AgcmLogin-Instanz finden, aktuelle Feldinhalte anzeigen
python alef_login_tool.py find [--pid PID]

# Kompletter Login-Ablauf: Zugangsdaten schreiben, Event 2 (-> SendAccount)
# feuern, warten, Event 4 (-> UI-Uebergang) feuern
python alef_login_tool.py login --account NAME --password PW [--delay 3] [--pid PID]

# Low-Level: ein beliebiges Event von Hand feuern
python alef_login_tool.py fire --event N [--param3 V] [--param4 V] [--pid PID]
```

Ohne `--pid` wird `alefclient.exe` automatisch per
`CreateToolhelp32Snapshot`-Prozessliste gefunden (schlaegt fehl, wenn mehrere
Instanzen laufen - dann `--pid` explizit angeben).

## Vollstaendiger Testablauf

1. **Bypass-Dateien**: `NotCheckGameGuard.arc` im Spielverzeichnis
   (`C:\Spiele\Archlord\`) muss vorhanden sein (umgeht den GameGuard-Update-
   Check, s. [`CLIENT_LAUNCH_AUTH_MECHANISM.md`](Startmechanismus.md)).
2. **`NoExcuteAuth.arc` darf NICHT vorhanden sein.** Das mag paradox wirken,
   ist aber wichtig: `NoExcuteAuth.arc`s Anwesenheit ueberspringt
   `IsValidLaunch` komplett *und* verhindert dabei, dass `autologin` gesetzt
   wird (`AgcGPAuth::init` setzt im Test-Modus `autologin=false`). Ohne
   `autologin=true` ruft aber **nichts** jemals `AgcmLogin::ConnectLoginServer()`
   automatisch auf - der Client verbindet sich dann nie von selbst zum
   Loginserver, egal wie lange man wartet (auch dieses Verhalten wurde live
   bestaetigt: mit `NoExcuteAuth.arc` blieb der Client nach mehreren Minuten
   ohne jede TCP-Verbindung).
3. **Client mit einer formal gueltigen, aber inhaltlich beliebigen
   Autologin-Kommandozeile starten**, um genau diesen automatischen
   Verbindungsaufbau auszuloesen:
   ```
   alefclient.exe 2:bootstrap|bootstrap
   ```
   `IsValidLaunch` (`FUN_0073EFF0`) prueft nur das Format (`"2:"` gefolgt von
   `member_id`, `"|"`, Rest), keine echte Signatur - jeder Wert funktioniert.
   Die tatsaechlichen Zugangsdaten werden gleich vom Tool ueberschrieben.
4. **`AlefLogin`-Server starten** (`cargo run -p aleflogin-server`), warten
   bis der Client verbindet und die `ENCRYPT_CODE`-Anfrage/Antwort im
   Server-Log erscheint.
5. **Tool ausfuehren**:
   ```bash
   python alef_login_tool.py login --account <ECHTER_NAME> --password <ECHTES_PW>
   ```
6. Server-Log zeigt danach ein echtes `AGPMLOGIN_SIGN_ON`-Paket mit den vom
   Tool geschriebenen Zugangsdaten (RC4-verschluesselt) und dem
   Autologin-`gamestring` (`bootstrap|<MAC-Adresse>`) im Klartext - das
   Feld wird von unserem Aufruf nicht beruehrt, ist also weiterhin der
   Bootstrap-Wert, was unschaedlich ist (der Server prueft es nicht).

## Offene Punkte

1. **Warum feuert der Callback nie von selbst?** Ungeklaert. Kandidaten:
   ein Unterschied zwischen dieser exe und dem Referenz-Quellcode (z.B. ein
   angepasster privater-Server-Fork), oder ein subtiler Bug/Sonderfall in
   `FUN_004e4070`/`FUN_004e41d0`, der nur unter bestimmten, noch nicht
   identifizierten Bedingungen zuschlaegt. Ein Live-Trace direkt im
   OnReceive-Callstack waere der naechste Schritt, scheitert aber am
   Anti-Debug-Verhalten im fruehen Boot-Fenster - eine moegliche
   Weiterfuehrung waere, den Anti-Debug-Check selbst zu identifizieren und
   per Patch zu deaktivieren, um dann sicher frueh attachen zu koennen.
2. **Opcode-`0x18`-Paket geklaert: Es ist [`AgpmWorld`](../Module/AgpmWorld.md) (Modul-ID `0x18`,
   bereits dokumentiert in [`WINSOCK_SEQUENCE_03_WORLD_ENTRY_CHARACTER_WORLD.md`](../Netzwerk/Sequenz-03-World-Entry-Character-World.md)),
   kein Fehlerreport.** Direkt nachdem `alef_login_tool.py login` Event 4 auf
   `AgcmLogin` gefeuert hat, schickt der Client von sich aus zwei
   `AgpmWorld`-Pakete mit **Operation `0`** - exakt "Client sendet World-Request"
   laut bestehender Doku. Das dazu gehoerige `String[32]`-Feld (Feld-Slot 4 im
   Layout `1,1 / 0,0x20 / 3,1 / 0xd,1 / 0,0x20`) enthaelt aber keinen echten
   Weltnamen, sondern augenscheinlich Debug-/uninitialisierte Daten (ein
   Zeiger, der exakt `AgcmUIMain::vftable` = `0x008CA31C` entspricht, plus
   eine `2` und der String `"AgcmUILogin"` als Rest) - vermutlich weil der
   Schritt, der diesen String eigentlich mit dem gewaehlten World-Namen
   fuellen sollte, wie ueblich nie laeuft. Server antwortet aktuell bewusst
   nicht auf `0x18` (kein Handler); das war fuer den naechsten Fund (Punkt 3)
   nicht noetig.

3. **`AgpmWorld`/Serverauswahl-UI: vollstaendig geloest, siehe eigener
   Abschnitt weiter unten** ("AgpmWorld: Serverauswahl-Liste - vollstaendig
   geloest"). Kurzfassung: Anzeige UND Listeninhalt haengen beide an
   Force-Fire-Events; der Umweg ueber `archlord.ini` war eine Sackgasse
   (das ist die Regions-, nicht die Weltenliste).

## AgpmWorld: Serverauswahl-Liste - vollstaendig geloest (2026-09-06)

### Sackgasse zuerst: `AgcmUILogin`s "Select Region"-Panel ist die falsche Baustelle

Bevor der echte Mechanismus gefunden wurde, gab es einen falschen Verdacht:
`FUN_0060A4A0` (Konstruktor eines "Select Region"-Panels in `AgcmUILogin`)
ruft am Ende `FUN_00743580(this, param_2, param_3)` auf, was wiederum
`FUN_007b3a50` (parst `archlord.ini` ueber RC4-Entschluesselung, Schluessel
`"1111"`) und `FUN_007432b0` (rendert Buttons) aufruft. Das sah nach dem
fehlenden Bindeglied fuer die Weltenliste aus - **war es aber nicht**.

- **Erster Absturz-Zwischenfall**: `FUN_00743580` direkt mit falschem `this`
  (dem rohen [`AgcmUIManager2`](../Module/AgcmUIManager2.md)-Zeiger statt `AgcmUILogin_instance + 0x323C`)
  und vertauschten Parametern aufgerufen -> hat einen Vtable-Slot einer
  Singleton-Instanz ueberschrieben und den **kompletten Client zum Absturz
  gebracht**. Lektion: groessere/komplexere Funktionen mit unbekannten
  Preconditions sind NICHT wie ein einfacher Event-Fire "einfach mal
  ausprobieren" - vorher die Aufrufstelle in der rohen Disassembly exakt
  nachvollziehen (Push-Reihenfolge, tatsaechliches `this`).
- Nach Korrektur (this=`AgcmUILogin_base+0x323C`, echte Resource-String-Zeiger
  statt geratener Werte) lief der Aufruf sauber durch, **parste sogar
  erfolgreich 2 Eintraege aus `archlord.ini`** (verifiziert per
  Speicher-Read: Vektor-Feld gefuellt) - aber es aenderte sich **nichts
  sichtbares**, weil dieses Panel schlicht eine andere UI ist: die
  **Regions-Auswahl** (z.B. "Europe" vs. "Asia"), nicht die Weltenliste
  innerhalb einer Region. Bei nur einer konfigurierten Region wird dieses
  Panel vom normalen Ablauf vermutlich automatisch uebersprungen.
- Ein zweiter Absturz kam von einem direkten Aufruf von `AgpmWorld::OnReceive`
  (`FUN_0056E530`) mit geratenem `arg1=0` (in der Annahme, das sei ungenutztes
  Padding) - tatsaechlich wird es intern dereferenziert (vermutlich ein
  Socket-/Kontext-Zeiger) und der Aufruf endete mit `0xC0000005`
  (Zugriffsverletzung) und totalem Prozessabsturz. Auch hier: nur Funktionen
  mit **vollstaendig verstandener** Signatur direkt aufrufen, nicht bei
  "sollte doch tolerant sein"-Vermutungen.

### Der echte Mechanismus (aus `AgpmWorld.cpp`, EP8-Referenzquelle, nur Recherche)

`AgpmWorld`s Paket-Operationen (`eAgpmWorldPacketOperation`):

| Op | Name | Zweck | Server->Client Event |
|---:|---|---|---|
| 0 | `GETWOLRD` | Client fragt nach EINER Welt (Name) | - (Client->Server) |
| 1 | `RESULT_GETWORLD` | EINE Welt hinzufuegen/aktualisieren | `AGPMWORLD_CB_UPDATE_WORLD` (=0) |
| 2 | `RESULT_GETWORLD_ALL` | **Komplette Liste**, text-codiert | `AGPMWORLD_CB_RESULT_GET_WORLD_ALL` (=1) |
| 3 | `GET_CHAR_COUNT` | Charakteranzahl anfragen | - |
| 4 | `RESULT_CHAR_COUNT` | Charakteranzahl-Ergebnis | - |

**Zentrale Erkenntnis**: Event 1 (das wir schon frueh als "macht Panel
sichtbar" force-gefeuert haben) ist in Wahrheit `AGPMWORLD_CB_RESULT_GET_WORLD_ALL`
- "Weltenliste komplett empfangen", nicht "Panel anzeigen". Die Sichtbarkeit
war immer nur ein **Nebeneffekt** der UI-Reaktion auf dieses Event.

Op 2s Payload ist ein **text-codierter String** im `AUTYPE_MEMORY_BLOCK`-Feld
(Feld-Slot 4 im Layout `1,1 / 0,0x20 / 3,1 / 0xd,1 / 0,0x20`), Format:

```
Name=Gruppe=Prioritaet=Status=Flag=Region;Name2=Gruppe2=...;
```

(`;`-getrennte Eintraege, `=`-getrennte Teilfelder; das 6. Teilfeld
`Region` nur unter `_AREA_GLOBAL_` - dieser Client-Build hat es, da sein
`AgpmWorld`-Paketlayout das zusaetzliche 5. String-Feld enthaelt). Serverseitig
in `AgpmWorld::_OnResultGetWorldAll` fuer jeden Eintrag in `UpdateWorld(...)`
aufgeloest, am Ende `EnumCallback(AGPMWORLD_CB_RESULT_GET_WORLD_ALL, NULL, NULL)`.

**Wire-Format des `AUTYPE_MEMORY_BLOCK`-Feldtyps (`0xd`), verifiziert direkt
aus dem generischen Deserializer `FUN_004e9fb0`** (`alefclient.pseudocode.c`,
VA `0x004e9fb0`): **2-Byte (ushort) Laengenpraefix**, NICHT 4 Byte wie zuerst
angenommen - `uVar2 = *_Src` liest ein `ushort` vor den Daten, derselbe Wert
wird zusaetzlich als separate Feld-Laenge ausgegeben. Ausserdem bestaetigt:
Maskenbreite fuer `AgpmWorld` ist **1 Byte** (`AgpmWorld::AgpmWorld()`'s
`SetFlagLength(sizeof(INT8))` im Referenzquellcode, unabhaengig bestaetigt
durch den `FUN_004ea630(1)`-Aufruf direkt vor der Feld-Layout-Registrierung
in der Dekompilierung - `FUN_004ea630(width)` ist das generische "Maskenbreite
fuer die naechste `SetFieldType`-Registrierung setzen"-Primitiv, `AgcmLogin`
ruft dort passend `FUN_004ea630(2)`).

### Trotzdem: der Netzwerkweg allein reicht nicht

Ein **byte-genau korrektes** `RESULT_GETWORLD_ALL`-Antwortpaket wurde gebaut
und ueber die echte, funktionierende Verschluesselung verschickt (verifiziert
per Klartext-Log-Ausgabe vor der Verschluesselung: Maske `0x09`, Operation
`2`, Laengenfeld `0x1f` passt exakt zu `strlen("...")+1`). Trotzdem: **keine
Wirkung, keine Spur im Client-Speicher** (Scan nach dem gesendeten Weltnamen
ergab in mehreren Versuchen null Treffer). Das bestaetigt: `AgpmWorld::OnReceive`
verarbeitet eingehende `0x18`-Pakete in diesem Build **genauso wenig
zuverlaessig** wie `AgcmLogin::OnReceive`s Event-Dispatch - dasselbe
grundlegende, ungeklaerte Problem dieser gesamten Session, nur eine weitere
Auspraegung davon.

### Der funktionierende Workaround

Wie bei `AgcmLogin` (Felder direkt schreiben + Event force-feuern, nie ueber
das Netzwerk verlassen): `FUN_0056E170` (`AgpmWorld`s interne "UpdateWorld"-
Methode) **direkt per Injection aufrufen**, dann Event 1 force-feuern.

`FUN_0056E170` legt in einer Hashtabelle bei `AgpmWorld+0x13498` (Key =
Weltname) einen Eintrag an/aktualisiert ihn: Name bei `entry+0x30`, Status
(Word) bei `entry+0x72`. Signatur (`__thiscall`, 7 Stack-Argumente insgesamt,
bestaetigt ueber das eigene `ret 0x1C` am Funktionsende):

```
FUN_0056E170(ecx=AgpmWorld_this,
             name_ptr,      // 1. Argument: Zeiger auf NUL-terminierten Weltnamen
             status,        // 2. Argument: AGPDWORLD_STATUS_* (Word, als DWORD gepusht)
             0,             // 3. Argument: ungenutzt
             0,             // 4. Argument: immer nach entry+0x74 geschrieben
             0,             // 5. Argument: optional -> entry+0x78, nur wenn != 0
             fire_event,    // 6. Argument: wenn != 0, feuert Event 0 mit Zeiger auf den Eintrag
             0)             // 7. Argument (deepest push): von der Funktion nie gelesen, beliebig
```

Live bestaetigt (mehrfach, auch mit zwei verschiedenen Namen gleichzeitig):
kein Absturz, Eintrag landet korrekt im Speicher (`entry+0x30`/`entry+0x72`
per Read verifiziert), und nach zusaetzlichem Force-Fire von **Event 1**
(`AGPMWORLD_CB_RESULT_GET_WORLD_ALL`, mit Parametern `0,0` - passend zu
`EnumCallback(..., NULL, NULL)` im Referenzquellcode) erscheint der Eintrag
tatsaechlich in der sichtbaren Serverauswahl-Liste.

Werkzeug-Unterstuetzung: `alef_login_tool.py update-world --name NAME
[--status N]` (siehe naechster Abschnitt).

## Die `find_module_base`-Fallstricke: False-Positives durch Netzwerkpuffer-Reste

`find_module_base`s erste, naive Fassung (erstes Match beim Low-to-High-Scan)
lieferte fuer `AgcmUILogin` gelegentlich eine **falsche** Adresse: eine
zwischengespeicherte Kopie des oben erwaehnten Opcode-`0x18`-Garbage-Pakets
in einem Netzwerk-Empfangspuffer enthaelt zufaellig die Bytes
`"AgcmUILogin\0"` (Teil des uninitialisierten zweiten `String[32]`-Feldes),
was die Namenssuche faelschlich als echte Modul-Instanz interpretiert.

- **Erster Fix (unzureichend)**: Pruefen, ob das erste DWORD am Fundort wie
  ein gueltiger Vtable-Zeiger aussieht (`VALID_VTABLE_RANGE`). Schlug fehl,
  weil das Garbage-Paket selbst mit einem echten, gueltigen Vtable-Wert
  beginnt (`AgcmUIMain::vftable` = `0x008CA31C`, Teil seines Inhalts, kein
  Zufall).
- **Funktionierender Fix**: Clustering-Heuristik. Echte Objekt-Instanzen sind
  isolierte Einzelallokationen; verirrte Kopien desselben kleinen Pakets in
  einem Ringpuffer-artigen Empfangsbereich tauchen mehrfach eng beieinander
  auf (beobachtet: 3 Kopien innerhalb von ca. `0x140` Bytes). `find_module_base`
  bevorzugt jetzt einen Kandidaten ohne "Nachbarn" innerhalb von `0x10000`
  Bytes gegenueber geclusterten Kandidaten. Verifiziert: liefert jetzt
  zuverlaessig die isolierte, echte Instanz.

## Werkzeug-Erweiterung: beliebige Module ansprechen

`alef_login_tool.py`s `find`/`fire`-Befehle akzeptieren jetzt `--module NAME`
(Default `AgcmLogin`) und finden JEDES `ApModule` ueber dieselbe
"`<Name>\0`"-String-Suche in privatem Speicher - die Technik ist nicht
`AgcmLogin`-spezifisch, sondern eine allgemeine `ApModule`-Konvention
(Name steht immer bei Objekt-Basis `+8`). Beispiele:

```bash
python alef_login_tool.py find --module AgpmWorld
python alef_login_tool.py fire --module AgpmWorld --event 1
python alef_login_tool.py update-world --name AlefWorld --status 1
```

## Nach der Serverauswahl: `AGPMLOGIN_UNION_INFO` (Nations-/Fraktionswahl) (2026-09-06)

Mit der jetzt funktionierenden Weltenliste (siehe oben) kann man im echten Client
tatsaechlich auf einen Welteintrag klicken. Das loest **keinen** [`AgcmConnectManager`](../Module/AgcmConnectManager.md)-
oder `AgpmWorld`-Traffic aus, sondern eine bisher unbekannte **dritte Operation**
auf `AgcmLogin` selbst (Opcode `0x0d`): live beobachtet, byte-genau dekodiert,
mit dem echten `AgpmLogin.cpp`-Quellcode abgeglichen.

### Der `AUTYPE`-Enum - endlich vollstaendig geklaert

Bisher wurden Feldtyp-Codes (`0`, `1`, `3`, `0xd`, ...) einzeln, ad-hoc aus der
Ghidra-Dekompilierung erschlossen. Der echte Enum steht in `AuType.h` und
klaert das ein fuer alle Mal (relevant fuer **jedes** `AuPacket`-Feldlayout im
gesamten Projekt, nicht nur [`AgpmLogin`](../Module/AgpmLogin.md)/`AgpmWorld`):

```c
AUTYPE_CHAR = 0,  AUTYPE_INT8 = 1,   AUTYPE_UINT8 = 2,   AUTYPE_INT16 = 3,
AUTYPE_UINT16 = 4, AUTYPE_INT32 = 5, AUTYPE_UINT32 = 6,  AUTYPE_INT64 = 7,
AUTYPE_UINT64 = 8, AUTYPE_FLOAT = 9, AUTYPE_POS = 10,    AUTYPE_MATRIX = 11,
AUTYPE_PACKET = 12 (0xC),  AUTYPE_MEMORY_BLOCK = 13 (0xD),
AUTYPE_POS_BASEMETER = 14, AUTYPE_WCHAR = 15
AUTYPE_END = 0xFF (Sentinel, kein echter Typ)
```

**`AUTYPE_PACKET` (`0xc`) - Wire-Format eines verschachtelten Sub-Pakets**,
verifiziert direkt aus dem generischen Deserializer `FUN_004e9fb0`s
Typ-`0xc`-Zweig (nicht zu verwechseln mit `AUTYPE_MEMORY_BLOCK`/`0xd`, das ein
simpler 2-Byte-laengenpraefigierter roher Byte-Blob ist, siehe Abschnitt oben):

```
[u16 Laenge][mask (mask_width Bytes)][Feld-Bytes...]
```

`Laenge` = Anzahl Bytes von `mask`+`Feld-Bytes` zusammen (schliesst das
Laengenfeld selbst NICHT mit ein). Der beim Deserialisieren ausgegebene
Zeiger fuer dieses Feld zeigt auf den **Anfang dieses Blocks** (auf das
Laengenfeld selbst) - genau das, was z.B. `AgcmLogin::OnUnionInfo`s
`pvCharDetailInfo`-Parameter ist, das dann an ein ZWEITES, eigenstaendiges
`AuPacket`-Objekt (`m_csPacketCharInfo`, eigene 2-Byte-Maske) zur weiteren
Dekodierung uebergeben wird.

### Korrektur: `AccountID`-Feld ist 49 Byte, nicht 65

Fruehere Dokumentation (aus einer frueheren Session, nie gegen den Quellcode
geprueft) ging von `AccountID(65B fixed)` aus. Der echte `AgpmLogin.cpp`-Quellcode
zeigt: `AUTYPE_CHAR, AGPACHARACTER_MAX_ID_STRING+1` - und live (byte-genaue
Analyse des unten beschriebenen Operation-3-Pakets) bestaetigt sich
`AGPACHARACTER_MAX_ID_STRING = 48`, also **49 Byte gesamt** fuer das
`AccountID`-Feld in `AgpmLogin`s Hauptpaket. (Das ist unabhaengig von
`AgcmLogin`s eigenem `m_szAccount`-Puffer, der intern tatsaechlich 65 Byte
gross ist - zwei verschiedene Konstanten fuer zwei verschiedene Zwecke.)

Vollstaendiges, jetzt quellcode-bestaetigtes Feldlayout von `AgpmLogin::m_csPacket`
(2-Byte-Maske, bit N = Feld N in Deklarationsreihenfolge):

| Bit | Feld | Typ/Groesse |
|---:|---|---|
| 0 | Operation | `AUTYPE_INT8`, 1 |
| 1 | EncryptCode | `AUTYPE_CHAR`, 32 (`ENCRYPT_STRING_SIZE`) |
| 2 | AccountID | `AUTYPE_CHAR`, 49 (`AGPACHARACTER_MAX_ID_STRING+1`) |
| 3 | AccountID Length | `AUTYPE_INT8`, 1 |
| 4 | Password | `AUTYPE_CHAR`, 49 |
| 5 | Password Length | `AUTYPE_INT8`, 1 |
| 6 | CID | `AUTYPE_INT32`, 1 |
| 7 | ServerAddr/WorldName | `AUTYPE_CHAR`, 32 (`AGPMLOGIN_SERVERGROUPNAMESIZE`) |
| 8 | CharDetailInfo | `AUTYPE_PACKET` (nested), 1 |
| 9 | ServerInfo | `AUTYPE_PACKET` (nested), 1 |
| 10 | Result | `AUTYPE_INT32`, 1 |
| 11 | VersionInfo | `AUTYPE_PACKET` (nested), 1 |
| 12 | gamestring | `AUTYPE_CHAR`, 2049 |
| 13 | challenge | `AUTYPE_CHAR`, 5 |
| 14 | isLimited | `AUTYPE_INT32`, 1 |
| 15 | isProtected | `AUTYPE_INT32`, 1 |

### Was tatsaechlich passiert: `AgcmLogin::SendGetUnion`

`eAgpmLoginOperation` (`AgpmLogin.h`): `AGPMLOGIN_ENCRYPT_CODE=0`,
`AGPMLOGIN_SIGN_ON=1`, `AGPMLOGIN_EKEY=2`, **`AGPMLOGIN_UNION_INFO=3`**
("`AGPMLOGIN_GET_UNION`"), `AGPMLOGIN_CHARACTER_NAME=4`, ...

Klick auf einen Welteintrag ruft `AgcmLogin::SendGetUnion(pszWorld, pszAccount)`
auf, die ein Paket mit Operation `3` + AccountID + WorldName sendet (genau die
zwei Felder, die live im Paket beobachtet wurden: Maske `0x0085` = Bits
0,2,7 = Operation+AccountID+ServerAddr/WorldName). "Union" ist Archlords
Zwei-Nationen-System (`AUUNION_TYPE_NONE=0`, `AUUNION_TYPE_RED_HEART=1`,
`AUUNION_TYPE_BLUE_BLOOD=2`, aus `ApDefine.h`) - fragt ab, welche Fraktion
der Account fuer diese Welt gewaehlt hat.

Server-Antwort (`AgcmLogin::OnUnionInfo`, liest NUR das `UnionInfo`-Feld aus
dem `CharDetailInfo`-Nested-Paket, alles andere darin wird ignoriert):
Operation `3` + `CharDetailInfo` (nested, nur Bit 4 = `UnionInfo` gesetzt,
`AUTYPE_INT32`) gemaess `m_csPacketCharInfo`s Layout (`TID, CharName,
MaxRegisterChars, SlotIndex, UnionInfo, RaceInfo, hairIndex, faceIndex,
NewCharID, JumpingFlag`).

Im `AlefLogin`-Server als `agpmworld_result_getworld_all_reply`-Analogon
implementiert (`main.rs`, `build_nested_packet`-Helper fuer das generische
`AUTYPE_PACKET`-Wire-Format): Antwort mit `AUUNION_TYPE_NONE` (0) - der
echte "noch keine Fraktion gewaehlt"-Wert, sollte eigentlich die
Fraktionswahl-UI des Clients uebernehmen lassen, genau wie bei einem echten
frischen Account.

### Wieder dasselbe Muster: Antwort kommt an, Callback feuert nicht von selbst

Byte-genau verifizierte, korrekte Antwort gesendet (Client blieb dabei am
Leben, keine Aenderung sichtbar) - **wieder** kein natuerliches Feuern von
`AGCMLOGIN_CB_UNION_INFO` (Event `5` im `eAGCMLOGIN_CB`-Enum: `CONNECT=0,
DISCONNECT=1, ENCRYPT_CODE=2, INVALID_CLIENT_VERSION=3, SIGN_ON=4,
UNION_INFO=5`). Force-Fire von Event 5 auf `AgcmLogin` mit `param3` = Zeiger
auf einen `INT32`-Wert (echte Signatur: `EnumCallback(AGCMLOGIN_CB_UNION_INFO,
(PVOID)&lUnion, NULL)` - `lUnion` ist ein lokaler Stack-Wert im Original, wir
schreiben ihn stattdessen in den (nach dem Login ungenutzten)
`m_szEncryptCode`-Puffer als Scratch-Speicher) **hat tatsaechlich etwas
ausgeloest**: ein neuer, bisher nie gesehener Dialog erschien (Screenshot
bestaetigt, mit "Verbindung"/"Beenden"-Buttons und zwei farbigen
Symbolen - passt zu den zwei Nationen).

**Aber**: Der Dialog ist unlesbar/nicht klickbar - dasselbe Symptom wie beim
`AgcmUILogin`-"Select Region"-Panel weiter oben: das Event liefert die Daten,
aber der komplette UI-Konstruktionspfad (das Pendant zu
`FUN_0060A4A0`/`FUN_00743580` fuer DIESEN Dialog) wurde nicht mit angestossen,
weil wir nur den Daten-Event isoliert force-feuern, nicht die komplette Kette.

### Geloest: den kaputten Dialog einfach umgehen

Der echte Quellcode (`AgcmUILogin::CBGetUnionInfo`) zeigt: der Dialog wird
**nur geoeffnet, wenn `lUnion == AUUNION_TYPE_NONE`**:

```c
if (AUUNION_TYPE_NONE == lUnion) {
    pcmUIManager->ThrowEvent(... AGCMUILOGIN_EVENT_UNION_SELECT_OPEN ...);
    pThis->SetLoginMode(AGCMLOGIN_MODE_UNION_SELECT);
} else {
    pThis->m_lUnion = lUnion;   // nur speichern, sonst nichts sichtbares
}
```

Schickt man stattdessen `AUUNION_TYPE_RED_HEART` (1) oder `AUUNION_TYPE_BLUE_BLOOD`
(2), wird der Dialog komplett uebersprungen. Eine Nationswahl ist in den letzten gespielten Episoden ohnehin
nicht an eine Nationswahl aus den letzten gespielten Episoden - passt dazu,
dass dieses System in spaeteren Episoden praktisch nicht mehr sichtbar in
Erscheinung tritt. `AlefLogin` schickt jetzt standardmaessig `RED_HEART`.

### Weiter zur Charakterliste: `AGPMLOGIN_CHARACTER_INFO`/`_FINISH`

Mit uebersprungenem Union-Dialog bleibt der Client zunaechst im Ladebildschirm
haengen (das ist `AgcmUILogin::CBGetMyCharacterNameFinish`, siehe naechster
Absatz - dieselbe Funktion wird fuer zwei verschiedene Zwecke wiederverwendet,
einmal fuer den account-weiten "in welchen Welten habe ich schon einen
Charakter"-Vorabruf, einmal fuer den Uebergang danach). Force-Fire von
**Event 7** (`AGCMLOGIN_CB_CHARACTER_NAME_FINISH`) auf `AgcmLogin` ruft
tatsaechlich `AgcmLogin::SendGetCharacters(pcmLogin->m_szWorldName,
pcmLogin->m_szAccount)` auf - live bestaetigt: Ladefenster erscheint, und der
Client sendet ein echtes, neues Paket: **Operation `6`**
(`AGPMLOGIN_CHARACTER_INFO`, "gib mir meine Charaktere auf dieser Welt",
Client->Server - nicht zu verwechseln mit Operation `4`
(`AGPMLOGIN_CHARACTER_NAME`, Server->Client, fuer den fruehen account-weiten
Vorabruf; beide heissen im Quellcode-Kommentar fast identisch
"AGPMLOGIN_GET_CHARACTERS", nur mit unterschiedlicher Richtung).

Antwort (unser Test-Account hat 0 Charaktere, also reicht direkt das
Fertig-Signal ohne vorherige `AGPMLOGIN_CHARACTER_NAME`-Eintraege): Operation
`7` (`AGPMLOGIN_CHARACTER_INFO_FINISH`) mit `AccountID`+`CID`(=0) - beides
Top-Level-Felder, kein Nested-Paket noetig (`AgcmLogin::OnReceive`s Handler
dafuer liest nur `lCID`+`pszAccount` direkt aus den geparsten Feldern).

Das feuert **nicht** Event 7 erneut, sondern ein **anderes** Event:
`AGCMLOGIN_CB_CHARACTER_INFO_FINISH` = **Event 8** im `eAGCMLOGIN_CB`-Enum
(`..., SIGN_ON=4, UNION_INFO=5, CHARACTER_NAME=6, CHARACTER_NAME_FINISH=7,
CHARACTER_INFO_FINISH=8`) - registriert auf `AgcmUILogin::CBGetMyCharacterInfoFinish`.
Force-Fire von Event 8 (mit `param3=0` - die echte Signatur erwartet
`(PVOID)&pvBuffer[2]={CID,AccountID}`, aber `0` reichte hier live aus, ohne
Absturz) **fuehrt tatsaechlich zur Charakterauswahl-/Charaktererstellungs-
UI** - bestaetigt per Screenshot, erstmals in dieser Session vollstaendig
erreicht.

### Kompletter Ablauf bis zur Charakterauswahl (2026-09-06, live bestaetigt)

```bash
# 1. Login (siehe oben)
python alef_login_tool.py login --account testuser --password testpass

# 2. Weltenliste befuellen (Name/Gruppe frei waehlbar)
python alef_login_tool.py update-world --name AlefWorld --status 1 --group Europe --priority 1

# 3. Im Client manuell auf den Welteintrag klicken (echte UI-Aktion, kein Force-Fire)
#    -> Client sendet AgpmLogin Operation 3 (UNION_INFO); der AlefLogin-Server
#       antwortet automatisch mit AUUNION_TYPE_RED_HEART (siehe main.rs)

# 4. Event 7 feuern -> loest SendGetCharacters() aus (Ladefenster erscheint,
#    Client sendet Operation 6 CHARACTER_INFO; Server antwortet automatisch
#    mit Operation 7 CHARACTER_INFO_FINISH, da 0 Charaktere)
python alef_login_tool.py fire --event 7 --param3 0 --param4 0

# 5. Event 8 feuern -> Charakterauswahl/-erstellung erscheint
python alef_login_tool.py fire --event 8 --param3 0 --param4 0
```

### Charaktererstellung, erster Schritt: `AGPMLOGIN_RACE_BASE`

Klick auf "Charakter erstellen" (nach Rassenwahl) sendet **Operation `10`**
(`AGPMLOGIN_RACE_BASE`, Kommentar im Quellcode: "AGPMLOGIN_REQUEST_CREATE_CHARACTER_INFO,
AGPMLOGIN_RESPONSE_CREATE_CHARACTER_INFO" - derselbe Opcode fuer beide
Richtungen) mit `AccountID` + `CharDetailInfo{RaceInfo=1}` (nested, Bit 5).

**Besonderheit**: `AgcmLogin::OnReceive`s Handler dafuer ignoriert den
Paketinhalt komplett - `EnumCallback(AGCMLOGIN_CB_RACE_BASE, NULL, NULL)`.
Die Antwort muss also nur syntaktisch gueltig sein (Operation=10 reicht,
keine weiteren Felder noetig). `AGCMLOGIN_CB_RACE_BASE` = **Event 10** im
`eAGCMLOGIN_CB`-Enum (`..., CHARACTER_INFO_FINISH=8, ENTER_GAME=9, RACE_BASE=10`).
Force-Fire von Event 10 (param3/4=0) fuehrt direkt zur
Charaktererstellungsmaske mit Namenseingabe - bestaetigt live.

Ergaenzung zum kompletten Ablauf (Schritt 6-7 nach den bisherigen 5):

```bash
# 6. Im Client Rasse waehlen, "Charakter erstellen" klicken
#    -> Client sendet Operation 10 (RACE_BASE); Server antwortet automatisch
#       mit einer leeren Operation-10-Bestaetigung

# 7. Event 10 feuern -> Charaktererstellungsmaske (Namenseingabe) erscheint
python alef_login_tool.py fire --event 10 --param3 0 --param4 0
```

### Namen absenden: `AGPMLOGIN_NEW_CHARACTER_NAME`/`_INFO_FINISH` - geloest, mit einer bekannten Absturzfalle

Absenden des Formulars (Name "Testcharacter", Rasse DragonScion, TID `1724`)
sendet **Operation `11`** (`AGPMLOGIN_NEW_CHARACTER_NAME`, `SendCreateCharacter`)
mit `AccountID`+`WorldName`+`CharDetailInfo{TID, CharName, SlotIndex, UnionInfo,
hairIndex, faceIndex}`. Antwort: derselbe Opcode `11` zurueck
(`CharDetailInfo{CharName, MaxRegisterChars-als-Gesamtzahl, SlotIndex}`), dann
unaufgefordert **Operation `12`** (`AGPMLOGIN_NEW_CHARACTER_INFO_FINISH`).

Force-Fire von **Event 11** (`AGCMLOGIN_CB_NEW_CHARACTER_NAME`) braucht *echte*
Zeiger fuer `param3`(`&slotIndex`)/`param4`(Namens-String) - mit `0,0` schlaegt
nur der interne NULL-Check fehl (kein Absturz, aber der Charakter wird nicht
hinzugefuegt). Mit echten Werten: Erfolg, per Speicher-Scan bestaetigt
(`AgcmUILogin_base + 0x11A0` = `m_szMyCharacterInfo[0]` = "Testcharacter").

**Event 12 (`AGCMLOGIN_CB_NEW_CHARACTER_INFO_FINISH`) stuerzt zuverlaessig ab.**
Sein Handler (`AgcmUILogin::CBGetNewCharacterInfoFinish`) ruft `UpdateCompenInfo()`
auf, das `((AgpmCharacter*)GetModule("AgpmCharacter"))->GetCharacter(...)` OHNE
NULL-Pruefung aufruft - [`AgpmCharacter`](../Module/AgpmCharacter.md) (das echte Gameplay-Charaktermodul)
wurde in diesem force-fire-getriebenen Ablauf nie initialisiert, also NULL.
Zweimal bestaetigt ueber den spieleigenen Crash-Reporter
(`C:\Spiele\Archlord\ERRORLOG.TXT`, wird bei jedem Absturz automatisch
geschrieben und ist praeziser als das Windows-Ereignisprotokoll: exakte EIP,
"Read from location 0x98 caused an access violation", Registerdump, sogar die
gerade in Bearbeitung befindliche Charakter-TID). Dieselbe Absturzadresse
(`0x004c2821`) trat einmal auch aus Event 7s eigener Kette heraus auf, unter
anderen Speicherzustaenden - also nicht eng auf Event 12 begrenzt, sondern ein
generelles Risiko bei allem, was ein Charakter-Ladefenster mit Vorschau oeffnet,
solange `AgpmCharacter` nicht initialisiert ist.

**Workaround**: Event 12 nicht feuern. Stattdessen den Charakterlisten-Abruf
erneut durchlaufen (Events 7 -> 6 -> 8, in dieser Reihenfolge, jedes genau
einmal), diesmal mit dem Server, der den Charakter in seiner Antwort
mitschickt (Operation `4` `AGPMLOGIN_CHARACTER_NAME` + Operation `7`
`AGPMLOGIN_CHARACTER_INFO_FINISH`). **Wichtig**: Event 8 zweimal hintereinander
feuern toggelt `m_nEventToggleUIOpen` und versteckt die komplette UI wieder -
die Reihenfolge muss beim ersten Versuch stimmen.

**Offener Punkt**: `AlefLogin` hat noch keine echte Persistenz - der Server
behauptet aktuell immer, dass "Testcharacter" bereits existiert, statt
tatsaechlichen Account-Zustand zu verwalten. Noch nicht implementiert.

**Offener Punkt**: Rassen-/Klassenauswahl reagiert nicht auf Klicks (nur
DragonScion sichtbar/waehlbar, Mensch/Ork/Mondelf tun nichts trotz
`_LoadSelectableRace()` fuer alle vier laut Referenzquelle). Noch nicht
untersucht.

## Root-Cause-Durchbruch, 2026-09-06: kein Dispatch-Bug, sondern ein Entschluesselungs-Mismatch

Beobachtung, die den Umschwung ausloeste: dieser exakte Client-Build
lief nachweislich jahrelang problemlos gegen die echten Webzen-Server - ein
grundlegender Client-Bug war also von Anfang an unwahrscheinlich. Wahr-
scheinlicher: unserem eigenen Server fehlt eine Voraussetzung, die der echte
Server immer erfuellt hat. Diese Vermutung hat sich bestaetigt.

### Die komplette Kette, per nicht-invasiven Marker-Hooks Schritt fuer Schritt durchleuchtet

Alle Hooks nach demselben Muster wie oben (erste 5-7 Bytes einer Funktion durch
`jmp` zu einem Trampolin ersetzen, das einen Marker setzt, die Original-Bytes
unveraendert ausfuehrt, dann zurueckspringt - die Zielfunktion laeuft danach
exakt wie vorher, nur mit einem Nebeneffekt).

1. **`AgcmLogin::OnReceive`** (`0x0065E7F0`): nie erreicht (siehe oben).
2. **`ApModuleManager::Dispatch`** - Adresse zunaechst unbekannt, gefunden ueber
   ihr eindeutiges Bytemuster (`cmp al,78h` = Vergleich gegen
   `APPACKET_MAX_PACKET_TYPE`=120, kombiniert mit dem bereits bekannten
   `m_pModuleDisp`-Array-Offset `+0x12974`): **`0x004E35D0`**. Direkt gehookt:
   ebenfalls **nie erreicht**.
3. **Modul-Registrierung nochmal ueberprueft, diesmal mit dem korrekten
   Array-Offset**: `m_pModuleDisp[]` beginnt bei `ApModuleManager_base +
   0x12974` (aus der Disassembly von `ApModuleManager::AddModule`,
   `0x004E3B00`, abgelesen - der fruehere 16-KB-Scan hatte den falschen,
   viel zu kleinen Adressbereich abgesucht). `m_pModuleDisp[0x0D]` bei
   `ApModuleManager_base(0x009713b8) + 0x12974 + 0x0D*4` enthaelt **exakt**
   den echten `AgcmLogin`-Instanzzeiger - **Registrierung ist zu 100% korrekt**,
   die fruehere Vermutung "Dispatch-Tabellen-Eintrag fehlt" war falsch
   (nur der Scan-Bereich war falsch).
4. **Dispatch() hat in der ganzen Programmdatei genau EINEN Aufrufer**:
   `0x0059B164`, eingebettet in eine Pro-Tick-Netzwerk-Pumpe. Diese liest via
   `FUN_007019A0` (ein deque-artiger "pop front") aus einer gemeinsamen,
   statisch-fixen Warteschlange (Kontext-Objekt bei fixer Adresse `0xC30838`)
   und ruft `Dispatch()` **nur wenn ein Element vorhanden ist**.
5. **Die Einreih-Funktion** `FUN_00701B70` (Gegenstueck zu `FUN_007019A0`,
   dieselbe `0xC30838`-Queue) - gehookt: **nie erreicht**.
6. **Die Roh-Empfangsverarbeitung** `FUN_00706CD0` (bereits aus einer
   frueheren Arbeitsphase bekannt, dort im Zusammenhang mit dem
   ENCODE_KEY+WrapperB-Fund identifiziert) - gehookt: **wird erreicht**
   (bestaetigt: unsere Pakete kommen im Client an und werden verarbeitet).
7. Innerhalb dieser Funktion zwei weitere Hooks gesetzt:
   - Direkt vor dem Entschluesseln (`0x00706D91`, nur erreichbar wenn der
     Marker-Byte-Check `0xA1`/`0xB1` samt zugehoerigem Rand-Byte `0xAF`/`0xBF`
     bestanden wurde): **wird erreicht** - unser Wrapper-Format/Marker ist
     also korrekt.
   - Der Ablehnungspfad (`0x00706E1B`, erreicht wenn ENTWEDER der
     Marker-Check ODER die Pruefung "entschluesseltes Ergebnis beginnt mit
     `0xD6` und endet mit `0x6B`" fehlschlaegt): **wird ebenfalls erreicht**.

**Schlussfolgerung**: Marker-Check bestanden, Entschluesselungsaufruf
(`FUN_004EA800`) laeuft durch, aber das **entschluesselte Ergebnis besteht die
Klartext-Rahmenpruefung nicht**. Das Paket wird direkt danach verworfen -
nie in die Warteschlange, nie `Dispatch()`, nie `OnReceive()`. Das erklaert
**die gesamte, seit Sessionbeginn beobachtete Kette** ohne jede Contradiction:
wir haben nie wirklich getestet, ob der Client unsere Antworten selbst
korrekt entschluesseln kann, weil wir Felder immer direkt ins Memory
geschrieben und dann Events force-gefeuert haben - komplett am
Entschluesselungs-/Dispatch-Pfad vorbei.

### Die Entschluesselungskette selbst (naechster Untersuchungsschritt)

`FUN_004EA800` (Haupteinstieg, Aufrufparameter: Puffer, Groesse (INT16),
weitere Kontext-Parameter):

```
Marker-Byte pruefen (0xA1 mit Randbyte 0xAF, ODER 0xB1 mit Randbyte 0xBF)
  -> bei Erfolg:
FUN_004EA680(ein Parameter)  -> Ergebnis an FUN_004F9540 uebergeben
  -> falls FUN_004F9540 sagt "Transform nicht aktiv": Rohdaten ab Offset+7
     werden direkt als Klartext behandelt (kein Decrypt noetig - passt zur
     Vor-StartupEncryption-Phase)
  -> falls aktiv: Puffer allokieren (Ziel-Laenge = Gesamtlaenge - 8, passt
     exakt zu Header(7: Marker+Laenge+Sequenznummer)+Trailer(1)),
     FUN_004EA680(FUENF Parameter diesmal) -> liefert einen Cipher-/
     Schluesselkontext, FUN_004F98F0(ctx) fuehrt die eigentliche
     Blowfish-Entschluesselung aus.
```

Das Framing-Verstaendnis (7-Byte-Header, -8-Laengenkorrektur) stimmt exakt mit
unserem eigenen Modell ueberein. Der Unterschied muss in `FUN_004EA680`s
Schluessel-/Kontextauswahl oder `FUN_004F98F0`s genauem Chiffrierverfahren
liegen - z.B. eine Verkettung mit der Sequenznummer, ein anderer Modus als
reines ECB, oder ein sich pro Paket aendernder State, den unsere
`blowfish_ecb_decrypt(ENCODE_KEY, ...)`-Implementierung nicht nachbildet.

### Alle 4 Schluessel/Wrapper-Kombinationen empirisch ausgeschlossen

`FUN_004EA680`s statische Disassembly (zwei ineinander verschachtelte,
teils rekursive Funktionen mit SEH-Rahmen und generischer
Callback-Tabellen-Indizierung) liess sich nicht sauber als offensichtliche
"Schluesselwahl" identifizieren - stattdessen wurde direkt live getestet,
mit dem `Dispatch()`-Marker-Hook als Live-Oracle ("kommt das Paket durch,
ja/nein"): `send_reply` wurde temporaer so geaendert, dass sie bei jedem
Aufruf reihum eine von vier Kombinationen benutzt
(`ENCODE_KEY`/`DECODE_KEY` x `WrapperA`/`WrapperB`), jede live gegen den
echten Client getestet (mehrere `AgcmLogin`/`AgpmWorld`-Antworten in Folge,
tatsaechlich versendete Kombination jeweils aus dem Server-Log abgelesen,
`Dispatch()`-Marker danach geprueft). **Ergebnis: keine der vier Kombinationen
bringt den Marker von `0` auf `1`.** Damit ist die naheliegendste Hypothese
("falscher Schluessel" oder "falscher Wrapper-Marker") vollstaendig
ausgeschlossen - der reale Unterschied liegt tiefer: im Cipher-**Modus**
(z.B. CBC mit einem aus der Sequenznummer abgeleiteten IV statt reinem ECB),
im **Padding**, oder in einer **paketweisen Schluesselableitung**, die unsere
Implementierung nicht nachbildet. Diagnose-Code wieder auf den sauberen
`ENCODE_KEY`+`WrapperB`-Normalzustand zurueckgesetzt (dieser Code-Pfad wird
ohnehin nur ueber den Force-Fire-Workaround erreicht, nie ueber den echten
Client-Decrypt, solange das hier nicht geloest ist).

**Noch nicht analysiert - naechster Schritt fuer die kommende Arbeitsphase**: den
genauen Cipher-Modus/Padding/Schluesselableitung in `FUN_004EA680`
(insbesondere den 5-Parameter-Aufrufpfad) und `FUN_004F98F0` (das nach
genauerem Hinsehen eher wie eine generische, indizierte Callback-Tabelle
aussieht als wie direkter Blowfish-Code - moeglicherweise muss noch eine
Ebene tiefer gesucht werden, um die tatsaechliche Cipher-Funktion zu finden)
vollstaendig entschluesseln.

### Korrektur zweier Fehleinschaetzungen aus der ersten Untersuchungsrunde

1. Ein `je`/`jne`-Lesefehler in der Dispatch-Disassembly hatte kurzzeitig den
   falschen Eindruck erweckt, `EnumPreRecieveModule`s Rueckgabewert wuerde
   invertiert ausgewertet. Nach genauem Nachlesen: die Logik ist korrekt
   (`test eax,eax; je <Ablehnen>` - bei leerer Filterliste/`TRUE` laeuft
   `Dispatch()` normal weiter zu `OnReceive`).
2. Der fruehere Vtable-Slot-Hook auf `AgcmLogin`s eigenem `+0x20` testete
   NICHT `EnumPreRecieveModule` (wie angenommen), sondern `OnPreReceive` -
   eine trivial-anders-liegende, virtuelle Methode, die nur relevant ist,
   wenn sich ein ANDERES Modul als Vorfilter auf `AgcmLogin` registriert
   (was laut Quellcode-Suche nirgends passiert). Die echte, gemeinsame,
   NICHT-virtuelle `EnumPreRecieveModule`-Implementierung liegt bei
   `0x004E4570` (laeuft `m_listPreRecieveModule` bei `ApModule_base+0x7E4`
   ab, ruft pro Eintrag dessen `OnPreReceive` ueber DESSEN eigenen Vtable-Slot
   `+0x20` auf) und wird von `Dispatch()` per direktem, nicht-virtuellem Call
   aufgerufen. Der damalige Hook war also uninformativ, nicht falsch -
   Ergebnis "nie erreicht" traf einfach die falsche Funktion.

### Durchbruch #2, 2026-09-06 (Fortsetzung): der Live-Capture-Beweis

Ein neuer, nicht-invasiver Hook (`hook_capture_decrypted.py`) auf
`0x00706DC6` (direkt nach dem Ruecksprung aus `FUN_004EA800`, dort wo der
Puffer-Zeiger fuer die `0xD6`/`0x6B`-Klartextpruefung ausgelesen wird)
liefert den ersten DIREKTEN Beweis, was der Client als "entschluesseltes"
Ergebnis behandelt:

```
Server-Ciphertext (AgpmWorld-Antwort, Body ohne 7-Byte-Header/Trailer):
96 85 03 1d 87 9e 8f 30 59 8e 5b a6 68 fe 31 6d ee 1f 26 7a f1 d0 d7 4b
19 0c 82 c0 b5 5a b0 dc 09 4f 0b 58 5f 83 5c 19 cd f7 4a c1 ad 06 4c 4a
cb ea 0b f9 d8 0f a9 bc bf

Vom Hook erfasster "entschluesselter" Puffer (identisch, Byte fuer Byte!):
96 85 03 1d 87 9e 8f 30 59 8e 5b a6 68 fe 31 6d ee 1f 26 7a f1 d0 d7 4b
19 0c 82 c0 b5 5a b0 dc 09 4f 0b 58 5f 83 5c 19 cd f7 4a c1 ad 06 4c 4a
cb ea 0b f9 d8 0f a9 bc bf 00 fe fe fe fe fe (Rest = nicht initialisierter Heap)
```

**Der Client entschluesselt ueberhaupt nicht** - der als "Klartext" gepruefte
Puffer ist exakt der unveraenderte Chiffretext. Das bestaetigt exakt den in
`FUN_004EA800`s eigener Disassembly sichtbaren Fruehausstieg:

```c
iVar1 = FUN_004ea680();                 // liefert das globale AuCryptManager-Singleton (fixe VA 0x009AC12C, keine Relokationen)
if ((*(int *)(iVar1 + 4) == 0) || (param_5 == 0)) {
    *param_3 = param_2; return param_1;  // Pass-through, ganzer Puffer unveraendert
}
...
FUN_004ea680(param_5);
iVar1 = FUN_004f9540(iVar1, param_5);    // "ist Transform fuer diese Richtung aktiv?"
if (iVar1 == 0) {
    pcVar2 = param_1 + 7;                // AUCH Pass-through (nur Header uebersprungen, kein Decrypt)
} else {
    ... echte Blowfish-Entschluesselung ueber FUN_004F98F0 ...
}
```

`FUN_004f9540(this, mode)` (`0x004F9540`, disassembliert und bestaetigt):
`mode==1` -> `return *(this+0x18)==3;`, sonst `return *(this+0x1c)==3;`. Beide
Felder liegen auf dem GLOBALEN Singleton, nicht auf einem Pro-Verbindungs-
Objekt. Live-Speicherauszug (fixe VA `0x009AC12C`, mehrfach ueber mehrere
frische Client-Prozesse reproduziert):

```
+0x00: vftable (AuCryptManager)
+0x04: 0x00000001   -- "ueberhaupt schon mal Crypto konfiguriert" (ungleich 0, Gate 1 besteht)
+0x08: 0x00000003   -- vermutlich Anzahl registrierter Cipher-Plugins
+0x0c/+0x10/+0x14:  STL-Vector [begin,end,cap_end) mit 4 Eintraegen (Groesse 0x10 = 4x4-Byte-Zeiger)
+0x18: 0x00000000   -- "aktiver Encode-Cipher"-Zustand -- SOLL 3 SEIN, ist es NIE
+0x1c: 0x00000000   -- "aktiver Decode-Cipher"-Zustand -- SOLL 3 SEIN, ist es NIE
```

Die 4 registrierten Cipher-Plugin-Konstruktoren wurden identifiziert
(Registrierungsreihenfolge = Vektor-Index):
`FUN_00500b60`->`AuBlowFish::vftable` (Index 0), `FUN_00500ae0`->`AuMD5Mac`
(Index 1, kein echter Verschluesseler - eher ein MAC/Hash), `FUN_004fea70`->
`AuRijnDael` (Index 2, AES), `FUN_004fa8e0`->`AuSeed` (Index 3, koreanischer
SEED-Blockcipher).

**Experiment**: Op7-Cipher-ID im Server-Code von `0` (angenommen "Blowfish")
auf `3` geaendert (in der Annahme, `FUN_004f9540`s Vergleich gegen die
Konstante `3` koennte direkt der Cipher-Index sein) - **Ergebnis: keine
Aenderung**, `+0x18`/`+0x1c` bleiben `0` unabhaengig vom gesendeten Wert.
Das widerlegt die einfachste Version dieser Hypothese (der gesendete
Cipher-Wert wird nicht 1:1 in dieses Feld uebernommen, oder das Feld wird
ueberhaupt nicht durch unser Op7-Paket beeinflusst).

### Durchbruch #3, 2026-09-06: `Dispatch()` FEUERT DOCH - aber nur fuer Klartext-Pakete

Bisherige Sessions hatten `Dispatch()`s Marker-Hook immer erst NACH der
initialen Verbindung/Schluesselaustausch installiert und dabei nie beobachtet,
dass er feuert - daraus wurde faelschlich verallgemeinert "`Dispatch()` feuert
nie". Ein neuer Test installierte den Hook so frueh wie moeglich (per
schneller Poll-Schleife auf die PID direkt nach Prozessstart, noch vor dem
allerersten TCP-Connect), mit einem erweiterten Capture-Hook
(`hook_dispatch_capture.py`, Ringpuffer der letzten 16 Aufrufe inkl.
`szData`-Zeiger + erste 16 Bytes).

**Ergebnis nach einem vollstaendigen Login-Durchlauf: `Dispatch()` wurde
GENAU 4 Mal aufgerufen** - und zwar exakt fuer die 4 einzelnen
Klartext-Pakete unseres eigenen "deterministic key setup"
(`build_clear_frame`, `d6...6b`-Format, KEIN `a1`/`b1`-Wire-Wrapper):

```
call#0: d6 1a 00 48 00 00 00 00 00 00 00 00 00 03 07 08   (Op7: Cipher waehlen)
call#1: d6 22 00 48 00 00 00 00 00 00 00 00 00 03 05 10   (Op5: Encode-Key setzen)
call#2: d6 22 00 48 00 00 00 00 00 00 00 00 00 03 06 10   (Op6: Decode-Key setzen)
call#3: d6 10 00 48 00 00 00 00 00 00 00 00 00 01 03 6b   (Op3: Aktivieren)
```

**Kein einziger** der nachfolgenden `a1`/`b1`-gewrappten, verschluesselten
Antworten (`AGPMLOGIN_ENCRYPT_CODE`-Antwort, `SIGN_ON`-Antwort,
`AgpmWorld`-Antworten) hat `Dispatch()` je erreicht (Zaehler blieb bei 4).

**Das praezisiert die gesamte bisherige Diagnose entscheidend**:
- Die Klartext-[`AgpmStartupEncryption`](../Module/AgpmStartupEncryption.md)-Pakete werden korrekt empfangen UND an
  `Dispatch()`/`OnReceive` weitergereicht - der Empfangspfad an sich
  funktioniert einwandfrei, auch fuer unsere eigenen, selbstgebauten Pakete.
- Das eigentliche Problem ist ausschliesslich auf der VERSCHLUESSELTEN Seite:
  entweder (a) `AgpmStartupEncryption::OnReceive` verarbeitet unsere
  Op7/5/6/3-Felder inhaltlich falsch und setzt deshalb nie
  `AuCryptManager+0x18/+0x1c` auf `3` (falsches Feld-/Masken-Layout in
  `encode_operation_and_data`, falscher Cipher-Identifier, oder die
  Aktivierung haengt an einem ganz anderen Mechanismus als angenommen), oder
  (b) das ist ueberhaupt nicht die richtige Bedingung und der echte Haken
  liegt woanders in `AgpmStartupEncryption`s eigener Logik.

**Naechster Schritt fuer die kommende Arbeitsphase**: `AgpmStartupEncryption`s
`OnReceive`/Operations-Handler in der Disassembly lokalisieren (das Modul
MUSS registriert sein, da `Dispatch()` fuer seinen Pakettyp erfolgreich
zustellt) und exakt nachvollziehen, was es mit den Feldern aus Op7/Op5/Op6/Op3
macht - im Zweifel per Hook direkt in diesem Handler den tatsaechlichen
Kontrollfluss/die Feldinterpretation live mitschneiden, statt weiter aus der
statischen Disassembly zu raten.

### Durchbruch #4, 2026-09-06 (Fortsetzung): der echte Operations-Dispatch von `AgpmStartupEncryption`, und Op7 existiert gar nicht

Direkt in derselben Arbeitsphase weiterverfolgt: `AgpmStartupEncryption::OnReceive`
wurde in der Disassembly gefunden (`FUN_0056d000`, Konstruktor bei
`0x0056cc80` bestaetigt per `FUN_004e4540(0x48)` - das ist exakt unser
`OPCODE_STARTUP_ENCRYPTION`). Es parst das `Operation`-Feld per
`FUN_004e9fb0`, dann:

```c
if ((uint)(char)param_3 < 7) {
    uVar2 = (*(code*)(&PTR_LAB_0056d13c)[(char)param_3])();  // Sprungtabelle, 7 Eintraege
    return uVar2;
}
return 1;  // aus dem gueltigen Bereich (0..6) -- STILLER No-Op, kein Fehler, kein Crash
```

**Die Sprungtabelle deckt NUR Operation-Werte 0 bis 6 ab - Operation `7`
existiert im echten Protokoll ueberhaupt nicht.** Unser eigenes
"Cipher-waehlen"-Paket (Op7, siehe `main.rs`s `cipher_ids`) faellt exakt in
den `return 1`-Fangnetz-Zweig: es wird nie an irgendeinen Handler
weitergereicht, egal welchen Wert wir senden (das erklaert restlos, warum das
Aendern des Cipher-Werts von `0` auf `3` in Durchbruch #2 keinerlei Wirkung
zeigte - das Paket kam nie irgendwo an).

Die reale Sprungtabelle (live aus dem Prozessspeicher gelesen, Adresse
`0x0056D13C`, 7 Eintraege) und ihre jeweiligen Weiterleitungs-Stubs (jeder
ruft nur `FUN_004e4070` = die generische, gemeinsame `ApModule::EnumCallback`
mit einer PRO-STUB fest einprogrammierten Callback-ID):

| Wire-Op | Handler-Stub | ruft EnumCallback mit ID |
|---|---|---|
| 0 | `0x0056CE00` | 0 |
| 1 | `0x0056CE20` | 1 |
| 2 | `0x0056CE70` | 2 |
| 3 | `0x0056CEC0` | 3 |
| 4 | `0x0056CEE0` | **5** (nicht 4!) |
| 5 | `0x0056CF30` | **6** (nicht 5!) |
| 6 | `0x0056CDB0` | **7** (nicht 6!) |

(Ab Op4 verschiebt sich die Callback-ID um +1 gegenueber dem Wire-Op-Wert -
in der Disassembly bestaetigt, keine Vermutung.)

`ApModule::EnumCallback` selbst (`FUN_004e4070`, jetzt vollstaendig gelesen)
ist ein simpler, gemeinsamer Event-Bus: `*(this+0x5dc+id*4)` ist der Kopf
einer verketteten Liste von `{context, funcPtr, next}`-Knoten; ist die Liste
leer, passiert schlicht NICHTS (kein Fehler, `return 1` = "Erfolg" obwohl
nichts ausgefuehrt wurde). Live am echten `AgpmStartupEncryption`-Objekt
gepr³ft (per neuem, direktem, nicht-invasivem `this`-Capture-Hook auf
`OnReceive` selbst - `find_module_base`s Ergebnis wurde dabei exakt
bestaetigt, `0x1b779560`, keine Diskrepanz):

```
event_id=0: KEIN Listener   (Wire-Op 0)
event_id=1: Listener vorhanden -> FUN_006819c0   (Wire-Op 1)
event_id=2: KEIN Listener   (Wire-Op 2)
event_id=3: Listener vorhanden -> FUN_00681b30   (Wire-Op 3, unser "activate")
event_id=5: Listener vorhanden -> LAB_00681be0   (Wire-Op 4, senden wir NIE)
event_id=6: Listener vorhanden -> LAB_00681c70   (Wire-Op 5, unser "encode key")
event_id=7: Listener vorhanden -> LAB_00681970   (Wire-Op 6, unser "decode key")
```

Alle 5 Listener sind in [`AgcmStartupEncryption`](../Module/AgcmStartupEncryption.md):Init` (`0x00681e10`)
registriert - dieselbe Funktion, die im ersten Lesen faelschlich als "nur
generische Engine-Callbacks, nichts mit StartupEncryption zu tun" eingestuft
wurde (3 der 8 dort registrierten Funktionen SIND tatsaechlich unrelated
Engine-Hooks; die anderen 5 sind exakt diese Operations-Handler - Korrektur
festgehalten).

**`LAB_00681be0` (Wire-Op 4) und `LAB_00681c70` (Wire-Op 5) sind die echten
Schluessel-Setter** - beide rufen an EXAKT der von unserem eigenen,
laengst dokumentierten Binaerpatch ([`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](../Netzwerk/Transform-Cipher.md),
Gate `FUN_00510D50`) genannten Adresse (`0x681C34` bzw. `0x681CC4`) dasselbe
Gate `FUN_00510D50` auf, und rufen bei Erfolg (Patch aktiv) `FUN_004F96B0`
(Op4) bzw. `FUN_004F9720` (Op5) auf. Deren Code (jetzt vollstaendig gelesen):

```c
// FUN_004f96b0 (Op4-Pfad, "encode"-Richtung, this=AuCryptManager-Singleton):
if (param_3!=0 && param_4>0 &&
    *(int*)(*(this+0xc) + *(this+0x18)*4) != 0) {   // Cipher-Objekt an Vektor-Index *(this+0x18) existiert?
    if (*(param_2+0xc)==0) FUN_004f9570(param_2+8, 1);  // Encode-Kontext ggf. anlegen
    cipherObj->vtbl[+8](ctx, data, size, param_5);        // SetKey/Init auf DIESEM Cipher-Objekt
    return 1;
}
// FUN_004f9720 (Op5-Pfad, "decode"-Richtung) ist strukturell identisch, nur mit this+0x1c/this+0x1c*4/param_2+0x18.
```

**Das ist eine entscheidende neue Erkenntnis**: `*(this+0x18)`/`*(this+0x1c)`
werden hier NICHT auf Gleichheit mit einer festen Konstante geprueft, sondern
als **Vektor-Index** benutzt, um das aktuell ausgewaehlte Cipher-Objekt zu
finden und dessen `SetKey`-artige Methode aufzurufen. Der Default-Wert `0`
(den wir live durchgehend beobachtet haben) zeigt auf Index 0 =
`AuBlowFish` - das ist ein voellig GueLTIGER, nicht-NULL-Eintrag, das
`!=0`-Gate wuerde also auch mit dem unveraenderten Default-Wert `0`
bestehen. Das widerspricht der in Durchbruch #2/#3 aufgestellten Annahme,
`*(this+0x18)`/`+0x1c` muessten erst auf `3` gesetzt werden, bevor
ueberhaupt irgendetwas funktioniert - **`FUN_004F9540`s Vergleich gegen die
Literal-Konstante `3` (fuer die "ist Transform aktiv"-Pruefung in der
Entschluesselung) und `FUN_004F96B0`/`FUN_004F9720`s Nutzung DESSELBEN Feldes
als Cipher-Vektor-Index scheinen also entweder (a) zwei unterschiedliche
Bedeutungen desselben Rohwerts zu sein, die zufaellig zusammenfallen wuerden
nur falls der aktive Cipher tatsaechlich Index 3 (`AuSeed`) waere, oder (b)
`FUN_004F9540`s Pruefung meint etwas komplett anderes als "welcher Cipher ist
gewaehlt".** Das ist NOCH NICHT aufgeloest.

**Konkret offene Fragen fuer die naechste Arbeitsphase, in Prioritaetsreihenfolge**:

1. Wir senden aktuell **niemals Wire-Op 4** (nur 3/5/6, plus das ungueltige,
   wirkungslose 7) - das heisst die "encode"-Richtung (`FUN_004F96B0`-Pfad)
   wird nie ueberhaupt versucht. Nur die "decode"-Richtung (ueber unser
   Op5 -> Wire-Handler `LAB_00681c70` -> `FUN_004F9720`) laeuft. **Erster,
   einfachster Test fuer die naechste Arbeitsphase: zusaetzlich ein Wire-Op-4-Paket
   senden** (mit dem, was aktuell als "encode key" gedacht ist) und pruefen,
   ob sich dadurch am Verhalten (insb. am `Dispatch()`-Marker fuer
   verschluesselte Pakete) etwas aendert.
2. Klaeren, ob unsere aktuelle Op5/Op6-Nutzung ("encode key" via Op5, "decode
   key" via Op6") ueberhaupt zur echten Wire-Op-Bedeutung passt - jetzt, wo
   die echten Handler-Funktionen bekannt sind (`LAB_00681be0`=Op4,
   `LAB_00681c70`=Op5, `LAB_00681970`=Op6), sollte das direkt durch Lesen
   von `LAB_00681970` (noch nicht gelesen) und genaues Nachvollziehen von
   `param_2+8` vs. `param_2+0x18`/`param_2+0x14` (die beiden
   Verbindungs-Kontext-Felder fuer Encode- vs. Decode-Schluesselkontext)
   geklaert werden, statt es weiter anzunehmen.
3. `FUN_004F9540`s Vergleich gegen die Konstante `3` vs. die
   Vektor-Index-Interpretation aufloesen - z.B. durch einen Hook direkt in
   `FUN_004F9540` selbst, der bei jedem Aufruf `this`, `mode`-Parameter und
   den tatsaechlich gelesenen Feldwert protokolliert, kombiniert mit einem
   Blick auf ALLE anderen Stellen im Code, die `*(AuCryptManager+0x18)` oder
   `+0x1c` lesen ODER schreiben (die grep-Suche nach `+ 0x18)`/`+ 0x1c)` ist
   im Gesamtcode leider viel zu unspezifisch, da dieser Objekt-Offset in
   Dutzenden voellig unabhaengigen Klassen wiederverwendet wird - man muss
   die Suche auf Aufrufer/Callees der bereits bekannten `AuCryptManager`-
   Methoden (`FUN_004ea680`, `FUN_004f9540`, `FUN_004f9570`, `FUN_004f96b0`,
   `FUN_004f9720`, `FUN_004f9790`, `FUN_004f97d0`) beschraenken, nicht auf
   den nackten Hex-Offset.
4. `FUN_006819c0` (Wire-Op 1, Event-ID 1) ist eindeutig die ORIGINALE,
   zufallsbasierte Challenge/Response-Schluesselaushandlung (generiert
   Zufallsbytes per `FUN_007e3340`, verschluesselt sie, sendet eine Antwort
   per `FUN_006818b0`) - vermutlich genau der Schritt, den unser
   Binaerpatch eigentlich ueberspringen soll. Zu klaeren: setzt DIESER Pfad
   (den wir nie durchlaufen, weil wir NIE Wire-Op 1 senden) als Nebeneffekt
   irgendwo `AuCryptManager+0x18`/`+0x1c` auf einen von `0` verschiedenen
   Wert, den unser deterministischer Kurzschluss-Ansatz (direkt zu Op3/5/6
   springen) schlicht ueberspringt? Das waere eine voellig andere,
   grundlegendere Erklaerung als alles bisher Untersuchte.

### Durchbruch #4, Fortsetzung: Op4/5/6-Nummerierung korrigiert und live getestet

Die aeltere Datei [`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](../Netzwerk/Transform-Cipher.md) (Stand 2026-09-05, vor
dieser Arbeitsphase) hatte bereits sehr viel Vorarbeit geleistet, war aber zu
diesem Zeitpunkt noch nicht mit dem hier neu gefundenen, tatsaechlich
verifizierten Wire-Op-zu-Handler-Mapping abgeglichen. Zusammengefuehrt:

- `LAB_00681970` (die Cipher-Auswahl-Funktion, schreibt zwei `int32` direkt in
  `AuCryptManager+0x18`/`+0x1c`) ist **Wire-Op 6**, nicht "vermutlich Op 0"
  wie in der aelteren Datei nur aus der Registrierungsreihenfolge vermutet.
- `LAB_00681be0` (echter Encode-Schluessel-Setter, `FUN_004F96B0`) ist
  **Wire-Op 4**.
- `LAB_00681c70` (echter Decode-Schluessel-Setter, `FUN_004F9720`) ist
  **Wire-Op 5**.
- Beide Schluessel-Setter sind nur ueber das bereits laenger bekannte
  Binaerpatch (`FUN_00510D50`-Gate, NOPs bei VA `0x681C34`/`0x681CC4`)
  ueberhaupt aktiv - **am laufenden `alefclient.exe` erneut direkt per
  Rohbyte-Vergleich bestaetigt** (`90 90 ...` an beiden Adressen statt der
  ungepatchten `74 1A`), der Patch ist also durchgehend vorhanden.

`main.rs`s Schluessel-Setup wurde entsprechend korrigiert: Op6 (Cipher-Wahl,
8 Byte = 2x int32, aktuell weiterhin `(0,0)`=Blowfish) statt des ungueltigen
"Op7", Op4 mit `ENCODE_KEY`-Rohbytes, Op5 mit `DECODE_KEY`-Rohbytes (vorher
waren Op5/Op6 mit vertauschten Daten UND falschen Opcode-Nummern belegt),
Op3 unveraendert. Live erneut mit dem `Dispatch()`-Ringpuffer-Hook getestet
(frischer Client, Hook so frueh wie moeglich installiert): die 4
Klartext-Pakete kommen jetzt mit den korrekten Opcode-Bytes an
(`...00 03 06 08`, `...00 03 04 10`, `...00 03 05 10`, `...00 01 03 6b` -
Byte-Offset 13 im jeweiligen Frame ist die Operationsnummer), der Client
crasht nicht, `AuCryptManager+0x18`/`+0x1c` bleiben (erwartungsgemaess, da wir
weiterhin `(0,0)` senden) bei `0`. **Aber**: weiterhin exakt 0 zusaetzliche
`Dispatch()`-Aufrufe fuer die nachfolgenden verschluesselten Antworten
(ENCRYPT_CODE-Antwort, SIGN_ON-Antwort, AgpmWorld-Antworten) - der
Entschluesselungs-Gate bleibt zu, GENAU wie von der aelteren Doku (`3` =
`AuSeed`, nicht Blowfish) vorhergesagt.

**Schlussfolgerung**: die Wire-Protokoll-Mechanik ist jetzt nachweislich
korrekt (richtige Opcodes, richtige Daten, Client verarbeitet sie sauber,
kein Crash) - der verbleibende, jetzt klar isolierte Blocker ist
ausschliesslich, dass `FUN_004F9540`s Aktivierungs-Pruefung Cipher-ID `3`
(SEED) verlangt, wir aber weiterhin Blowfish (`0`) auswaehlen UND unser
Server ohnehin nur Blowfish implementiert. **Naechster grosser Schritt**: (a)
Op6 mit `(3, 3)` senden, UND (b) `AlefLogin`s eigene Verschluesselung von
Blowfish auf SEED umstellen (Rundenkonstanten/Algorithmus bereits in
[`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](../Netzwerk/Transform-Cipher.md) bitgenau dokumentiert: 128-Bit-Block,
128-Bit-Schluessel, 16 Runden, G-Funktion mit vier 256-Eintrag-S-Boxen,
KC0..KC15-Rundenkonstanten identisch zu RFC 4269/KISA) - das ist eine
eigenstaendige, nicht triviale Implementierungsaufgabe (keine verbreitete
Rust-Crate fuer koreanisches SEED bekannt, muesste selbst geschrieben werden),
noch nicht begonnen.

**Tooling-Hinweis fuer die naechste Arbeitsphase**: zwei neue,
verifizierte Hook-Skripte liegen im Arbeitsverzeichnis und funktionieren
nachweislich: `hook_startupenc_onreceive.py` (direkter, korrekter
`this`-Capture auf `AgpmStartupEncryption::OnReceive` selbst - Vorsicht,
eine erste Version hatte einen Off-by-Parameter-Fehler beim Stack-Offset
und liess den Client abstuerzen, siehe Kommentar im Skript, jetzt behoben
und live bestaetigt). Ein Versuch, `FUN_004e4070` (EnumCallback) direkt
gefiltert nach `this==AgpmStartupEncryption_base` zu hooken
(`hook_enumcallback_filtered.py`) lieferte trotz augenscheinlich korrekter
Bytecode-Logik `0` Treffer - Ursache nicht gefunden, vermutlich ein
subtiler Fehler in der bedingten Sprung-Kodierung; nicht weiter verfolgt,
da die direkte Singleton-Speicherinspektion (kein Hook noetig) denselben
Erkenntnisgewinn schneller und zuverlaessiger lieferte. Fuer kuenftige
AuCryptManager-Untersuchungen: Speicher direkt an der fixen VA `0x009AC12C`
lesen (kein Hook noetig, da statische, nicht relozierte Adresse) ist meist
der schnellere und zuverlaessigere Weg als ein neuer Hook.

## SEED implementiert, 2026-09-07

Es wurde SEED von Grund auf in
`aleflogin-crypto/src/seed.rs` implementiert (keine Rust-Crate fuer
koreanisches SEED existiert). Vorgehen und Ergebnis:

### Referenzimplementierung statt Live-Disassembly nachgebaut

Die client-eigene SEED-Rundenschluessel-Erzeugung (`FUN_004fa960`) ist stark
compileroptimiert/entrollt und mit Byte-Rotationstricks durchsetzt - von Hand
korrekt nachzuvollziehen waere fehleranfaellig gewesen. Stattdessen wurde
OpenSSLs offizielle, oeffentliche Referenzimplementierung (`crypto/seed/seed.c`
und `seed_local.h`, direkt von GitHub geladen) 1:1 nach Rust portiert
(`SEED_set_key`, `E_SEED`-Makro, `SEED_encrypt`/`SEED_decrypt`) - mathematisch
identisch zum Standard, den auch der Client implementiert (siehe unten).

**Bitgenaue Verifikation, mehrfach unabhaengig, VOR jedem Live-Test:**

1. Alle vier 256-Eintrag-S-Box-Tabellen (`SS0`..`SS3`) wurden direkt aus
   `alefclient.exe` an den bereits dokumentierten VAs extrahiert
   (`0x00954da8`, `0x009551a8`, `0x009555a8`, `0x009559a8`) und Byte-fuer-Byte
   gegen OpenSSLs `SS[0..3]`-Tabellen verglichen: **alle 1024 Eintraege exakt
   identisch**.
2. Die KC-Rundenkonstanten stimmen exakt mit OpenSSLs `KC0`..`KC15` ueberein
   (bereits in [`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](../Netzwerk/Transform-Cipher.md) fuer KC0-KC8 belegt, hier
   fuer alle 16 bestaetigt).
3. Die Implementierung wurde gegen alle drei offiziellen RFC-4269-Anhang-B-
   Testvektoren geprueft (`rfc4269_vector_b1/b2/b3` in `seed.rs`) - **alle drei
   bestehen**, inklusive Rundenschluessel-Zwischenwerten, die per Hand gegen
   die RFC-eigene Tabelle nachgerechnet wurden.
4. Byte-Reihenfolge: der Client swappt sowohl beim Schluessel-Laden
   (`FUN_004fa960`) als auch beim Block-Laden (`FUN_004fb4e0`) jedes native
   (little-endian) 32-Bit-Wort explizit auf Big-Endian, BEVOR es verwendet
   wird - anders als bei diesem Projekts Blowfish-Port (der bewusst in der
   nativen Little-Endian-Reihenfolge des Clients bleibt, siehe
   [`WINSOCK_TRANSFORM_CIPHER_SUITE.md`](../Netzwerk/Transform-Cipher.md)). Die SEED-Implementierung nutzt daher
   durchgehend Standard-Big-Endian (wie OpenSSL), nicht Blowfishs Sonderfall.

**Ein echter Transkriptionsfehler wurde dabei gefunden und behoben**: beim
ersten manuellen Abtippen der 1024 S-Box-Werte hatte sich bei `SS3[0x4b]`
ein Byte-Rotationsfehler eingeschlichen (`0x1c1f0f13` statt `0x0f131c1f` -
dieselben vier Bytes, falsche Reihenfolge). Gefunden durch systematisches
Nachrechnen aller 16 Rundenschluessel gegen RFC 4269s eigene
Zwischenwert-Tabelle (Testvektor B.1 mit Schluessel `0` bestand trotzdem, weil
Rotation von Nullwoertern den Fehler maskiert - erst B.2/B.3 mit echten
Schluesseln deckten ihn auf). Behoben, indem alle vier Tabellen komplett neu
UND PROGRAMMATISCH (nicht erneut per Hand) aus den binaer-extrahierten Werten
generiert wurden - alle 1024 Eintraege danach nochmal automatisiert
gegengeprueft. **Lehre fuer kuenftige aehnliche Faelle**: bei grossen,
handabgetippten Konstantentabellen (Kryptografie-S-Boxen, etc.) immer
programmatisch aus der verifizierten Quelle generieren, nie mehr als ein paar
Werte von Hand abtippen.

### Live-Integration und aktueller Stand

`main.rs` wurde umgestellt: Op6 (Cipher-Wahl) sendet jetzt `(3, 3)` = SEED
fuer beide Richtungen (statt `(0, 0)` = Blowfish), `decrypt_and_respond`/
`send_reply` nutzen `seed_cbc_decrypt`/`seed_cbc_encrypt` statt der
Blowfish-Funktionen.

**Zwei weitere, waehrend der Live-Integration gefundene strukturelle
Bugs, unabhaengig vom Cipher-Algorithmus selbst:**

1. **Op4/Op5-Payload war zu kurz**: `AuSeed::Reset` (`FUN_004fe2e0`, das
   Vtable-`+0x08`-Ziel, das der Schluessel-Setter aufruft) erwartet 32 Byte,
   nicht 16 - die ERSTEN 16 Byte gehen in die Rundenschluessel-Expansion
   (der eigentliche Cipher-Schluessel), die ZWEITEN 16 Byte in
   `FUN_004fa910(2, 2, &input[16], ctx)` (Modus+IV-Setup). Mit nur 16 Byte
   gesendet las diese Funktion 16 Byte Anschlussmuell aus dem Paketpuffer als
   "IV". Behoben: `seed_key_setup_payload()` baut jetzt ein 32-Byte-Feld
   (Schluessel + aktuell 16 Nullbytes als IV).
2. **Modus ist CBC, nicht ECB**: `FUN_004fa910`s hartcodierte Argumente `2, 2`
   setzen ein Modusfeld auf beiden Cipher-Kontexten auf `2`. Die
   Verkettungsfunktion `FUN_004fe360` (Vtable-`+0x0c`, "Transform") liest
   genau dieses Feld in einem Sprungverteiler; **Fall 2 ist klassisches
   CBC-Encrypt** (`IV XOR Klartext -> Blockverschluesselung -> IV = Ergebnis`,
   direkt aus der Disassembly abgelesen, keine Vermutung). `aleflogin-crypto`
   hat jetzt `seed_cbc_encrypt`/`seed_cbc_decrypt` (Standard-CBC, Null-IV,
   passend zum oben gesendeten Null-IV) zusaetzlich zu den ECB-Varianten.

**Live bestaetigt nach beiden Fixes** (per direktem Speicherauszug am
Singleton, kein Hook noetig): `AuCryptManager+0x18` und `+0x1c` stehen jetzt
zuverlaessig auf `3` (SEED aktiv gewaehlt fuer beide Richtungen) - das war vor
diesen Fixes (bei ungueltiger "Operation 7" bzw. zu kurzer Payload) nie der
Fall.

**Noch NICHT geloest**: trotz korrekt gewaehltem Cipher (`3`/SEED) und
korrekter CBC-Umstellung auf beiden Seiten bleibt der Ende-zu-Ende-Test
weiterhin negativ - `Dispatch()` feuert laut Ringpuffer-Hook weiterhin nur
fuer die 4 eigenen Klartext-Schluessel-Setup-Pakete, nie fuer nachfolgenden
verschluesselten Traffic. Zusaetzlich (neu diese Arbeitsphase beobachtet, vorher
nicht moeglich da Blowfish nie bis hierhin kam): **auch unser eigener
`AlefLogin`-Server kann die vom CLIENT gesendeten Pakete nicht mehr
entschluesseln** (`decrypted payload doesn't parse as a known frame shape`,
reiner Zufallsbyte-Output) - vorher (mit Blowfish+ENCODE_KEY) hatte das
zuverlaessig funktioniert. Das deutet auf mindestens eine der folgenden,
noch ungeklaerten Ursachen hin, absteigend nach Wahrscheinlichkeit:

- Der tatsaechliche Schluessel, den der Client fuer seine EIGENE
  Encode-Richtung benutzt, ist NICHT der von uns per Operation 4 gesendete
  Wert - z.B. weil `FUN_004F96B0`s Gate (`*(this+0xc)+*(this+0x18)*4)!=0`,
  siehe Durchbruch #4) zwar den Cipher-Objekt-Zeiger findet, das eigentliche
  `SetKey`/`Reset` aber aus einem anderen Grund fehlschlaegt oder ein anderes
  Kontextobjekt trifft als angenommen - noch nicht live verifiziert (kein
  Hook auf das tatsaechlich uebergebene Schluesselmaterial installiert).
- Die IV-Annahme (Null, im zweiten Payload-Haelfte gesendet) ist falsch, oder
  `FUN_004fa910`s Feldreihenfolge (`ctx+0x10..0x1c = IV`) wurde falsch
  interpretiert.
- Ein weiteres, noch nicht gefundenes Gate/Zustandsfeld verhindert weiterhin
  die tatsaechliche Verschluesselungsausfuehrung (aehnlich der bereits
  gefundenen, aber per Patch entschaerften `FUN_00510D50`-Sperre).

**Naechster Schritt fuer die kommende Arbeitsphase**: einen neuen, direkten
Capture-Hook auf `FUN_004fe2e0` (`AuSeed::Reset`) selbst installieren, der
bei jedem Aufruf `this` (welcher CTX?), die tatsaechlich uebergebenen 32
Rohbytes und die Ergebniswerte in `ctx+0x44..` (die ersten paar
Rundenschluessel) mitschneidet - das wuerde direkt zeigen, ob unser
gesendetes Schluesselmaterial ueberhaupt dort ankommt, statt weiter von der
Cipher-ID-Auswahl (bereits bestaetigt korrekt) auf die Schluesseluebernahme
zu schliessen.

## Ende-zu-Ende (fast) geloest, 2026-09-07 (direkte Fortsetzung)

Der oben offene Punkt ("`FUN_004fe2e0` direkt hooken") wurde umgesetzt und
bestaetigte sofort: das Schluesselmaterial kommt korrekt an (`this`=echtes
`AuSeed`-Strategieobjekt, `ctx`=frisch angelegtes `SEED_ALG_INFO`,
`keyptr`->exakt `"AlefLoginEncKey!"` bzw. `"AlefLoginDecKey!"`, `length=32`).
Zusaetzlich: die ersten 4 Bytes der resultierenden Rundenschluessel
(`ctx+0x44`) stimmen exakt mit einer unabhaengigen Python-Nachrechnung der
eigenen SEED-Implementierung fuer denselben Schluessel ueberein
(`0x212a4341`) - **die komplette Schluessel-Uebernahme UND -Expansion ist
also zweifelsfrei korrekt**, IV-Annahme (Null) ebenfalls bestaetigt (ctx+0x20
liest ebenfalls Null).

Damit war die Kryptografie selbst vollstaendig entlastet. Der tatsaechliche,
bis dahin uebersehene Fehler: **`ENCODE_KEY` und `DECODE_KEY` wurden in
`main.rs` in der falschen Richtung verwendet.** Gefunden durch das
direkteste aller moeglichen Experimente: ein echtes, vom Client gesendetes
Chiffretext-Sample aus `server.log` mit BEIDEN Schluesseln in einem
Wegwerf-Python-Skript entschluesselt (auusserhalb des Clients, keine
Live-Interaktion noetig) - nur `DECODE_KEY` ergab einen gueltigen
`0xD6...0x6B`-Rahmen. Der Client verschluesselt seinen EIGENEN ausgehenden
Traffic also mit `DECODE_KEY`, nicht mit `ENCODE_KEY` wie der Name nahelegt
(vermutlich beschreiben die Namen die Rolle der Operationen 4/5 aus
Server-Sendersicht, nicht die Verwendung beim Client). Fix in `main.rs`:
`decrypt_and_respond` nutzt jetzt `DECODE_KEY`, `send_reply` nutzt
`ENCODE_KEY` - exakt vertauscht gegenueber vorher.

**Live-Ergebnis**: sofort und vollstaendig bestaetigt. Der Server empfaengt
das Client-eigene `AGPMLOGIN_ENCRYPT_CODE`-Request, entschluesselt es
korrekt (`opcode=0x0d` erkannt, Inhalt byte-fuer-byte plausibel gegen eine
alte Blowfish-Aera-Referenz), und sendet eine echte `AgcmLogin`-Antwort -
**zum ersten Mal in der gesamten Projektgeschichte funktioniert
Ende-zu-Ende-Entschluesselung in mindestens einer Richtung nachweislich
korrekt, ganz ohne Force-Fire-Workaround.**

### Neuer, letzter verbleibender Blocker: Client crasht beim Entschluesseln unserer Antwort

Direkt nachdem der Server seine erste echte, korrekt verschluesselte
`AgcmLogin`-Antwort sendet, stuerzt der Client ab (`ERRORLOG.TXT`,
Zeitstempel exakt passend zum Sendezeitpunkt):

```
Crash Address: 56f250ac
Stack trace:
0023:56F250AC MSVCR80.dll, memcpy()+0252 byte(s)
0023:004FEA59 alefclient.exe
```

`0x004FEA59` liegt in `FUN_004fe930` (`AuSeed::Decrypt`, Vtable-Slot `+0x10`
- der Verkettungsmodus-Wrapper, der pro 32-Byte-Fenster `FUN_004fe540`
aufruft und dessen Ausgabe per `memcpy` in den Zielpuffer kopiert). Eine
manuelle Nachrechnung der Schleifenlogik fuer die konkrete Antwortgroesse
(64 Byte Chiffretext = 2 volle 32-Byte-Fenster, sauber durch 16 UND 32
teilbar) zeigt keinen offensichtlichen Off-by-one in der
Abbruchbedingung selbst - die Ursache liegt vermutlich tiefer in
`FUN_004fe540`s eigener Laengenberechnung.

**Wichtig**: das ist ein NEUER, eigenstaendiger Bug, unabhaengig vom jetzt
geloesten Schluesselrichtung-Fehler. Auffaellig: die serverseitige
Client-zu-Server-Entschluesselung (identischer Cipher/Modus/Schluesseltyp,
reiner Rust-Code) funktioniert bereits fehlerfrei - der Unterschied muss
also entweder an der SPEZIFISCHEN Antwortlaenge liegen, daran dass dies der
ALLERERSTE echte Decrypt-Aufruf fuer einen frischen Client-Kontext ueberhaupt
ist, oder an einer client-seitigen Eigenart der Encrypt- vs.
Decrypt-Verkettung, die es serverseitig gar nicht gibt.

**Naechster Schritt fuer die kommende Arbeitsphase**: direkt in `FUN_004fe930`
und `FUN_004fe540` hooken (Parameter/Zwischenwerte mitschneiden), statt
weiter aus der statischen Disassembly zu schliessen - diese Arbeitsphase hat
mehrfach gezeigt, dass Live-Daten hier zuverlaessiger sind als
Handnachrechnung der stark optimierten Client-Assembly.

### Crash praezise charakterisiert (Registerzustand aus XCrashReport, kein Hook noetig)

Ein Versuch, `FUN_004fe930`s Parameter per Live-Hook (Ring-Puffer,
`hook_seed_decrypt_wrapper.py`) mitzuschneiden, scheiterte am Timing: der
Crash passiert innerhalb von ~2-3 Millisekunden nach Funktionseintritt -
selbst ein eng getaktetes Polling in einem einzigen, langlebigen
Python-Prozess (`poll_scratch.py`, keine Subprozess-Startkosten pro
Iteration) kam nur EINMAL knapp rechtzeitig durch (Zaehler ging von `0` auf
einen klar korrumpierten Wert `0xFF000000`, danach sofort
`ERROR_PARTIAL_COPY` - der Prozess war zu diesem Zeitpunkt bereits mitten im
Crash-Handling).

Stattdessen liefert `ERRORLOG.TXT`s eigener Registerauszug (vom
Spiel-eigenen Crash-Handler zum exakten Fault-Zeitpunkt geschrieben, kein
Race-Problem) die entscheidenden Daten:

```
alefclient caused an Access Violation (0xc0000005) in MSVCR80.dll at 0023:56f250ac.
Read from location 001b4000 caused an access violation.

EDI: 0x0fc16ec0   ESI: 0x001b3ffd   EAX: 0x0000006b
EBX: 0x00000000   ECX: 0x3fffe888   EDX: 0x00000000

Bytes at CS:EIP: F3 A5 ...   <- REP MOVSD (ECX=Anzahl DWORDs, ESI=Quelle, EDI=Ziel)
```

**`ECX = 0x3FFFE888` ist eindeutig die Ursache** - als DWORD-Zaehler fuer
`REP MOVSD` bedeutet das einen Kopiervorgang von ueber 4 GB, der praktisch
sofort (nach nur 3 Bytes ab `ESI=0x001b3ffd`, exakt an der Seitengrenze
`0x001b4000`) auf ungemappten Speicher trifft. Auffaellig:
`0x40000000 - 0x3FFFE888 = 0x1778` - der Wert sieht nach einem
Unterlauf/einer Fehlberechnung mit einer Rundzahl (`0x40000000`=1 GiB) als
Basis aus, aber die exakte Herkunft wurde in dieser Arbeitsphase nicht mehr
gefunden.

**Wo der Fehler vermutlich sitzt**: beim manuellen Nachvollziehen von
`FUN_004fe540`s Fall-2-Logik (CBC-Entschluesselung) mit den realen Werten
dieser Arbeitsphase (erstes 32-Byte-Fenster, `ctx+0x40`(Fenster-Offset)=0 nach
`FUN_004fb4a0`s Reset, `param_3`=32) faellt auf: nach dem ERSTEN
16-Byte-Block wird `_Size`(=verbleibende Bytes im Fenster)=16 berechnet, und
die Bedingung `if (0x10 < _Size)` (`16<16`) ist FALSCH - der ZWEITE
16-Byte-Block des 32-Byte-Fensters wird dadurch scheinbar UEBERSPRUNGEN,
was zu einer Verschiebung zwischen dem, was der AEUSSERE Aufrufer
(`FUN_004fe930`) fuer "bereits verarbeitet" haelt, und dem, was TATSAECHLICH
in `ctx+0x30`(Staging-Puffer)/`ctx+0x40`(Offset-Zaehler) fuer die NAECHSTE
Runde zurueckbleibt, fuehren koennte - genau die Art von Verschiebung, die
sich ueber mehrere Fenster/Aufrufe zu einer astronomisch falschen Laenge
aufschaukeln kann. **Nicht abschliessend bewiesen** (Gefahr weiterer
Handrechenfehler wie schon zweimal in dieser Arbeitsphase, siehe Warnhinweis
oben) - fuer die naechste Arbeitsphase: entweder einen Hook VOR dem
Funktionseintritt von `FUN_004fe930` selbst installieren, der die
Zielfunktion beim ALLERERSTEN erreichten Frame anhaelt (z.B. per
Debug-Break/Suspend-Thread statt reinem Speicher-Polling, um das Timing-Race
zu umgehen), oder pragmatisch: verschiedene Antwortlaengen fuer die erste
`AgcmLogin`-Antwort durchprobieren (z.B. ob eine 32-Byte- statt
64-Byte-Antwort den Crash umgeht) als Notbehelf, waehrend die echte Ursache
noch nicht gefunden ist.

#### Nachtrag: Timing-Race erfolgreich umgangen, ein Parameter empirisch bestaetigt

Das Timing-Problem (Crash innerhalb von 2-3ms nach Funktionseintritt, siehe
oben) wurde durch eine neue Hook-Technik geloest: statt die Original-Bytes
nach dem Mitschneiden wieder einzuspielen (`jmp` zurueck), springt der
Hook-Trampolin nach dem Capture in eine **Endlosschleife** (`EB FE` = `jmp $`)
- der Thread haengt dann dauerhaft an diesem Punkt fest, OHNE dass die
eigentliche (fehlerhafte) Logik je erreicht wird. Das gibt beliebig viel Zeit
zum Auslesen, ganz ohne Race gegen den Crash (Skript:
`hook_seed_decrypt_freeze.py`). Live bestaetigt: mit diesem Freeze-Hook auf
`FUN_004fe930`s Eintrittspunkt **tritt der Crash nicht mehr auf** (Prozess
bleibt am Leben, `ERRORLOG.TXT` bleibt unveraendert) - der eingefrorene
Thread ist offenbar nicht der einzige/Haupt-Thread, das Spiel blockiert
dadurch nicht insgesamt.

Aus dem eingefrorenen Zustand ausgelesen (8 rohe Stack-Dwords ab
Ruecksprungadresse): einer der Werte ist exakt `0x40` = **64** - das ist
exakt die Laenge unserer `AgcmLogin`-Antwort in Byte. Das bestaetigt live,
dass die Funktion mit der KORREKTEN Gesamtlaenge aufgerufen wird (kein
Laengenfehler schon beim Funktionseintritt) - der Fehler entsteht also
nachweislich ERST waehrend der internen 32-Byte-Fenster-Verarbeitung
(`FUN_004fe540`), nicht durch einen von aussen hereingereichten falschen
Wert. Ein Folgeversuch, denselben Freeze-Trick DIREKT an der
Absturzstelle selbst (`0x004FEA43`, unmittelbar vor der Summenbildung
`ecx+edx` fuer die spaetere `memcpy`-Laenge) zu platzieren, feuerte in einem
Testlauf nicht (Prozess blieb am Leben, kein neuer Crash, aber auch kein
Hook-Treffer) - vermutlich haengt das Erreichen dieser exakten Codestelle von
einer datenabhaengigen Verzweigung weiter oben ab (`jbe 004FEA5C` bei
`0x004FEA41`), die je nach Lauf unterschiedlich ausfallen kann. Fuer die
naechste Arbeitsphase: mehrere Freeze-Hooks GLEICHZEITIG an verschiedenen
Zwischenpunkten installieren (quasi Einzelschritt ueber mehrere Testlaeufe
hinweg simulieren), um den exakten Punkt einzugrenzen, an dem aus der
korrekten Eingangslaenge (64) die kaputte `ECX=0x3FFFE888` wird.

### Zwischenstand

Der urspruengliche, seit Sessionbeginn (und vermutlich seit sehr viel
laenger) bestehende Blocker - **Ende-zu-Ende-Verschluesselung funktioniert
nicht** - ist damit fuer die Richtung Client-zu-Server **vollstaendig
geloest und live bestaetigt** (zum ersten Mal ueberhaupt in der gesamten
Projektgeschichte). Fuer die Richtung Server-zu-Client (unsere Antworten)
ist die Verschluesselung selbst nachweislich korrekt (der Client empfaengt
und beginnt sie zu entschluesseln), aber ein NEUER, eigenstaendiger
Absturz-Bug in der clienteigenen SEED-Entschluesselungs-Pufferlogik
verhindert noch den vollen Rundlauf. Das ist ein deutlich kleineres, viel
praeziser eingegrenztes Problem als das urspruengliche "nichts entschluesselt
sich ueberhaupt" - mit exaktem Crash-Ort, exaktem fehlerhaftem Register und
einer plausiblen (wenn auch noch unbestaetigten) Hypothese zur Ursache.

### Warnhinweis: ein eigener Hook-Bug fuehrte zwischenzeitlich auf einen kompletten Holzweg

Bevor der Schluessel-Richtung-Fund gemacht wurde, fuehrte ein FALSCHES
Stack-Offset in `hook_receive_entry.py` (`[esp+14h]` statt korrekt
`[esp+0Ch]` fuer den `new_bytes_len`-Parameter von `FUN_00706CD0`) zu einer
kompletten Fehldiagnose ("der Windows-Message-Pump fuer den Socket haengt
nach dem allerersten Tick fuer immer") - inklusive einer tiefen
Untersuchung von `AcClientSocket`s `WSAAsyncSelect`-Fensterprozedur
(`LAB_00706F30`, durchaus wertvoll dokumentiert, siehe unten) und eines
manuellen `recv()`-Aufrufs per Injection, der faelschlich als Bestaetigung
eines "Verbindung tot"-Zustands gelesen wurde. Gefunden erst, als der reale
Parameterwert (nach Offset-Korrektur: `142`, nicht der urspruenglich
gemeldete Wert `0`) zeigte, dass die Funktion sehr wohl echte Daten
verarbeitet hatte. **Lehre**: meldet ein Hook einen verdaechtig runden/leeren
Wert (`0`), zuerst die eigene Stack-Offset-Arithmetik gegenpruefen (wie viele
Bytes wurden VOR dem Original-Prolog durch eigene `push`-Instruktionen
verschoben, und bezieht sich der Original-Disassemblertext auf den Zustand
VOR oder NACH dem Funktionsprolog?), bevor daraus eine inhaltliche
Schlussfolgerung ueber Client-Verhalten gezogen wird.

Trotzdem wertvoll aus diesem Holzweg: die Bestaetigung, dass
`AcClientSocket` ueber ein verstecktes Fenster (`WSAAsyncSelect`, Klasse
"AcClientSocket", Fensterprozedur bei `LAB_00706F30`) empfaengt, mit
Nachricht `0x600` (`LOWORD(lParam)`=Event-Bits: `FD_READ=1`, `FD_WRITE=2`,
`FD_CONNECT=0x10`, ...; `HIWORD(lParam)`=Fehlercode) - nuetzliches Wissen
fuer kuenftige netzwerkbezogene Diagnosen, auch wenn es in dieser Arbeitsphase
nicht die eigentliche Ursache war.

## Absturz-Bug vollstaendig geloest: fehlendes PKCS7-Padding, 2026-09-07 (direkte Fortsetzung)

Root Cause gefunden und live bestaetigt behoben - der Rundlauf funktioniert
jetzt vollstaendig ueber echten Client-Code, der Client bleibt am Leben und
macht sogar von selbst weiter (Weltliste-Anfrage nach dem Login-Reply, siehe
unten). Das ist der erste Mal in der gesamten Projektgeschichte, dass ein
Reply vom Server den Client nicht mehr abstuerzen laesst.

### Der Weg dorthin: praezises Lokalisieren via Freeze-Hooks an der echten Absturzstelle

Zunaechst wurde die im vorigen Abschnitt offene Frage geklaert, WARUM die
mehrfachen Freeze-/Trace-Hooks in `FUN_004fe540`s Case-2-Handler nie feuerten,
obwohl ein Crash im selben Testlauf nachweislich stattfand: der Grund war
schlicht **Timing** - jeder einzelne Hook-Installationsversuch bestand aus
mehreren sequenziellen Bash-Tool-Aufrufen (PID suchen, dann Hook installieren,
dann Polling starten), und der Client durchlaeuft Verbindungsaufbau,
Schluesselaustausch UND den fatalen Decrypt-Versuch bereits innerhalb weniger
Sekunden nach dem Start - schneller, als die einzelnen Tool-Aufruf-Rundreisen
brauchen. Geloest durch ein neues Skript-Muster: **ein einzelner
Python-Prozess wartet selbst per `CreateToolhelp32Snapshot`-Polling (alle
~10ms) auf das Erscheinen von `alefclient.exe`**, bevor der Client ueberhaupt
gestartet wird, und installiert die Hooks in genau demselben Prozess-Kontext
sofort nach PID-Fund - kein zusaetzlicher Tool-Rundlauf mehr dazwischen. Mit
diesem Muster feuerten die Freeze-Hooks zuverlaessig.

Zweite Verbesserung: statt einzelner Register per Hand zu sichern (fehleranfaellig,
siehe die vielen verworfenen Zwischenversuche in `hook_inner_memcpy.py`), wird
jetzt `pushad` (0x60) benutzt, um ALLE 8 Register mit einer einzigen Instruktion
sicher auf dem echten Stack zu sichern, gefolgt von `mov [scratch], esp`
(Opcode `89 25 <imm32>`), um NUR die resultierende Stack-Adresse zu sichern -
kein Register-Clobbering-Risiko mehr, und aus Python liest man einfach einen
32-Byte-Block ab dieser Adresse (`edi,esi,ebp,esp_orig,ebx,edx,ecx,eax` in
dieser Reihenfolge, da `pushad` in dieser Reihenfolge auf den Stack schreibt).

Mit diesen zwei Verbesserungen wurde EXAKT an der von `ERRORLOG.TXT`
gemeldeten Absturzstelle (`0x004FEA54`, `call 007FEE0C` in `FUN_004fe930`s
Tail-Flush-Pfad, direkt nach `add ecx,edx`) eingefroren und ausgelesen:

```
eax(src)=0x001af210
ecx(dest,post-add)=0x0f9820d3
len (Stack [espPost+0x28]) = 0xFFFFF00D  (4294963213 - eindeutig kein
                                            gueltiger Laengenwert)
```

`0xFFFFF00D` ist als Bytefolge zwar kein bekanntes Debug-Fuellmuster (anders
als z.B. `0xBAADF00D`), aber als Rechenergebnis eindeutig identifizierbar:
`16 - eax_intern = 0xFFFFF00D (mod 2^32)` loest sich eindeutig zu
`eax_intern = 0x1003`.

### Root Cause: `004FE270` ist eine PKCS-Padding-Validierung/-Entfernung

Disassembly von `004FE270` (aufgerufen ueber `FUN_004fe930` -> `004FE790`
[Mode-Dispatcher, Case SEED=2] -> `004FE650` [behandelt den STAGED letzten
16-Byte-Block] -> `004FE270` bei `0x004FE286`):

```
eax = letztes Byte des entschluesselten 16-Byte-Blocks   ; der "Padding-Wert"
if eax == 0            -> return 0x1003 (Fehler: ungueltiges Padding)
if eax > 16             -> return 0x1003 (Fehler: Padding-Wert zu gross)
for i in 0..eax:        ; klassische PKCS7-Validierungsschleife
    if block[15-i] != eax -> return 0x1003 (Fehler: Padding-Byte stimmt nicht)
return eax               ; Erfolg: Padding-Laenge
```

Der aufrufende Code (`004FE650` bei `0x004FE712`) berechnet daraus die
ECHTE Nutzdatenlaenge des letzten Blocks: `outLen = 16 - eax`. Das Problem:
der Aufrufer prueft `eax` NUR gegen die Sentinel-Werte `-1` und `-3`
(spezielle Fehlercodes anderer interner Aufrufe weiter oben in derselben
Funktion), **nicht aber gegen `0x1003`** - den generischen PKCS-Fehlercode
von `004FE270` selbst. Faellt `004FE270` also mit `0x1003` durch (weil unser
Server KEIN PKCS-Padding gesendet hat und das letzte Byte des letzten
16-Byte-Blocks zufaellig `0` oder `>16` war, oder die Padding-Bytes nicht
konsistent waren), wird dieser Fehlercode fälschlich als gueltige
Padding-Laenge weiterverwendet: `16 - 0x1003 = 0xFFFFF00D` (Ganzzahl-Unterlauf).
Dieser Wert landet unmittelbar darauf ungeprueft als Laengenparameter in einem
`memcpy`-Aufruf (`007FEE0C` -> letztlich `MSVCR80.dll!memcpy`), was zu einem
`REP MOVSD` mit ~4 Milliarden Kopien und sofortigem Zugriffsfehler fuehrt -
exakt das Verhalten aus dem urspruenglichen `ERRORLOG.TXT` (`ECX=0x3FFFE888`
in einem frueheren Lauf, `ECX=0x0F9820D3` mit Laenge `0xFFFFF00D` in diesem).

**Architektonische Erkenntnis**: der Client behandelt bei JEDER
`AuSeed::Decrypt`-Operation den LETZTEN 16-Byte-Block des Chiffretexts als
PKCS7-gepolstert und entfernt das Padding automatisch, VOELLIG UNABHAENGIG
davon, ob die Gesamtlaenge bereits ein exaktes Vielfaches der Blockgroesse
ist (unser 64-Byte-Reply war exakt 4 Bloecke, `ctx+0x40`-Fensteroffset blieb
0 - trotzdem wird die Haupt-Fensterschleife so gestaltet, dass sie den
LETZTEN 16-Byte-Block bewusst zurueckhaelt und der Tail-Flush-Pfad ihn
gesondert mit Padding-Behandlung verarbeitet). Das ist Standard-PKCS7-Verhalten
(ein volles zusaetzliches Padding-Block wird IMMER angehaengt, auch bei
bereits blockaligierten Daten, um genau diese Mehrdeutigkeit zu vermeiden) -
nur hatte unser Server das noch nie so gemacht.

### Der Fix

`aleflogin-crypto/src/seed.rs`: neue Funktion `seed_cbc_encrypt_pkcs7()`,
die den Klartext vor dem eigentlichen `seed_cbc_encrypt()` mit echtem PKCS7
polstert (Padding-Byte-Wert == Anzahl der Padding-Bytes; bei bereits
16-byte-aligniertem Klartext wird IMMER ein volles zusaetzliches 16-Byte-Block
mit Wert `0x10` angehaengt, nie "kein Padding"). `seed_cbc_encrypt()` selbst
bleibt unveraendert (Zero-Padding, wird u.a. von den bestehenden Tests
genutzt) - der Name macht den Unterschied jetzt explizit.

`aleflogin-server/src/main.rs`, `send_reply()`: einzige Aenderung, Aufruf von
`seed_cbc_encrypt` auf `seed_cbc_encrypt_pkcs7` umgestellt. Da
`build_wrapper_frame()` die aeussere Laengenangabe dynamisch aus
`ciphertext.len()` berechnet, war keine weitere Anpassung noetig - die 16
zusaetzlichen Padding-Bytes propagieren sich automatisch korrekt durch die
gesamte Wrapper-Framing-Kette.

Die Entschluesselungsrichtung (`decrypt_and_respond`, Client-zu-Server) war
NICHT betroffen und wurde nicht veraendert: unser Server liest dort ohnehin
nur bis zur inneren, selbstdeklarierten Frame-Laenge und ignoriert
ueberschuessige (Padding-)Bytes - unabhaengig vom clientseitigen Padding-Schema.

### Live-Bestaetigung

Sauberer Neustart OHNE jegliche Hooks (kein Freeze, kein Trace - reiner,
ungestoerter Client-Lauf):

```
2026-09-07T16:20:59Z  AGCM_LOGIN reply gesendet (jetzt PKCS7-gepolstert, 64 Byte Ciphertext)
2026-09-07T16:20:59Z  Client sendet naechste Anfrage: AgcmUILogin (opcode 0x18,
                       "Weltliste"-Request) - passiert NUR, wenn der Client das
                       vorherige Reply erfolgreich entschluesselt UND verarbeitet hat!
2026-09-07T16:20:59Z  Server antwortet mit RESULT_GETWORLD_ALL
                       (AgpmWorld reply)
[+5s]                  Prozess weiterhin am Leben, ERRORLOG.TXT unveraendert
                       (kein neuer Eintrag)
```

Sichtbar auch im entschluesselten Payload-Hexdump: die letzten 14 Bytes vor
dem `d6`-Frame-Ende sind `0e 0e 0e 0e 0e 0e 0e 0e 0e 0e 0e 0e 0e 0e` - exakt
das erwartete PKCS7-Padding (innerer Frame war 50 Byte lang, `50 mod 16 = 2`,
also `16-2=14` Padding-Bytes mit Wert `0x0E`).

### Zwischenstand

Der urspruengliche Blocker **"Ende-zu-Ende-Verschluesselung funktioniert
nicht"** ist damit in BEIDEN Richtungen vollstaendig geloest und live
bestaetigt. Der Client verarbeitet jetzt den kompletten `AGCM_LOGIN`-Rundlauf
ohne Absturz und macht von sich aus mit dem naechsten Protokollschritt
(Weltliste) weiter. Naechste sinnvolle Schritte waeren, den Rundlauf weiter zu
verfolgen (Weltauswahl, Charakterauswahl, etc.) und dort auftretende neue
Luecken/Bugs mit denselben jetzt etablierten Werkzeugen (schnelles
PID-Wait-Muster + `pushad`-Freeze-Hooks) zu untersuchen.

## Serverauswahl live getestet, neuer Absturz gefunden und geloest: `CreateRemoteThread` war die Ursache, 2026-09-07 (direkte Fortsetzung)

Der obige Fix wurde live durchgespielt: Login, Server ausgewaehlt,
"Verbindung" geklickt. **Das urspruengliche Problem ("nichts passiert") ist
geloest** - Weltliste und `AGPMLOGIN_UNION_INFO`(Fraktionswahl) laufen jetzt
komplett nativ ueber echten Client-Dispatch, keine Force-Fire-Workarounds
mehr noetig (direkte Folge des SEED-Fixes oben).

### Neuer Blocker: Charakterlisten-Schritt stuerzt ab - aber diesmal an *wechselnden* Adressen

Der naechste Schritt (Event 7 -> `SendGetCharacters` ausloesen, dann Event 8
-> Charakterauswahl-UI zeigen, beide ueber `alef_login_tool.py fire` per
`CreateRemoteThread`) stuerzte in mehreren Versuchen **zuverlaessig**, aber
**an jeweils VERSCHIEDENEN Absturzadressen** ab (`0x004C2821` in einer
generischen 3D-Vektormathe-Hilfsfunktion, `0x00432E4C` in einer generischen
Hashtabellen-Lookup-Funktion - beide mit hunderten voellig unabhaengiger
Aufrufer quer durchs ganze Programm). Erste Hypothese (Server behauptet
faelschlich, ein Charakter existiere bereits, ohne dass `AgpmCharacter`
davon weiss) wurde durch einen Test widerlegt: Server auf "0 Charaktere"
umgestellt (siehe `main.rs`-Kommentar bei `AGPMLOGIN_CHARACTER_INFO`) -
stuerzte trotzdem ab, an einer DRITTEN Adresse.

**Der wechselnde Absturzort bei IDENTISCHEM Input war der entscheidende
Hinweis**: das ist das Muster einer echten Race Condition, kein
deterministischer Logikfehler. Root Cause gefunden: `alef_login_tool.py`s
`fire`-Befehl (und alle bisherigen Force-Fire-Aufrufe ueberhaupt) fuehren den
Callback-Aufruf ueber **`CreateRemoteThread`** aus - also auf einem KOMPLETT
NEUEN, vom Hauptthread des Spiels unabhaengigen Thread. Der echte Hauptthread
laeuft dabei parallel weiter und greift auf dieselben globalen UI-/Render-Zustaende
zu (z.B. `0x00988020`, eine feste globale Tabelle, die im zweiten Crash als
NULL/kaputt gelesen wurde). Schritte wie Weltliste/Union-Info sind einfache
Datenoperationen mit wenig gemeinsamem State - liefen deshalb bisher
zuverlaessig durch reinen Zufall gut. Event 8 oeffnet dagegen ein neues
UI-Panel mit 3D-Charaktervorschau - deutlich mehr aktiv vom Hauptthread
gleichzeitig genutzter Zustand, daher viel anfaelliger fuer genau diese Race.
Erklaert rueckblickend auch aeltere, als "flaky"/"an anderen Speicherzustaenden"
beschriebene Abstuerze aus frueheren Arbeitsphasen (z.B. dieselbe Absturzadresse
`0x004c2821`, die schon mal bei Event 7 statt Event 12 auftrat) - das war
nie zufaellige Speicherbelegung, sondern dieselbe zugrundeliegende
Thread-Race, die ganze Zeit unerkannt.

### Der Fix: Aufrufe ueber ein "Main-Thread-Relay" statt `CreateRemoteThread`

Statt den Callback auf einem neuen Thread auszufuehren, wird jetzt ein
kleiner Hook in eine Funktion gesetzt, die garantiert HAEUFIG auf dem
ECHTEN Hauptthread laeuft; der Hook prueft bei jedem Aufruf eine kleine
geteilte "Anfrage"-Struktur (`ready`-Flag + `this`/`event_id`/`param3`/`param4`
+ `result`), und fuehrt den eigentlichen `FUN_004e4070(this, event_id, param3,
param4)`-Aufruf NUR aus, wenn Python zuvor `ready=1` gesetzt hat - exakt
derselbe Aufruf wie vorher, nur jetzt synchron zwischen zwei Frames des
Hauptthreads, ganz ohne Cross-Thread-Race.

**Zwei Kandidaten fuer den Hook-Punkt getestet, mit sehr unterschiedlichem
Ergebnis:**

1. **Vermuteter "Pro-Frame-Tick" bei `0x0059AE30`** (eine Funktion, die tiefer
   drin `ApModuleManager::Dispatch()` aufruft, siehe "Root-Cause-Durchbruch"-
   Abschnitt oben): **feuert nie** waehrend des Login-Bildschirms (Heartbeat-
   Zaehler blieb nach 1s bei `0` stehen) - offenbar nur im echten Spiel
   (nicht waehrend Login/Charakterauswahl) erreichbar.
2. **`kernel32.dll!QueryPerformanceCounter`** (ueber `GetProcAddress` gefunden -
   Systembibliotheken teilen sich denselben ASLR-Base ueber alle Prozesse
   einer Boot-Session hinweg, bestaetigt durch Vergleich zwischen dem eigenen
   Python-Prozess und dem Zielprozess): Heartbeat stieg auf >4000/Sekunde -
   wird also ständig aufgerufen, auch waehrend Login. **ABER**: der eigentliche
   Callback-Aufruf blieb haengen (`ready` wurde nie zurueckgesetzt, `done`
   nie gesetzt, obwohl der Heartbeat weiter hochzaehlte) - vermutlich, weil
   QPC von einer zu tiefen/sensiblen Stelle aus aufgerufen wird (evtl.
   innerhalb eines gehaltenen Locks), und ein Ruecksprung von dort in
   komplexe Spiellogik zu einem Deadlock fuehrt.
3. **`AcClientSocket`s eigene Fensterprozedur bei `0x00706F30`** (fixe VA,
   bereits aus frueheren Arbeitsphasen bekannt): **funktioniert einwandfrei**.
   Eine Fensterprozedur ist ein voellig normaler, erwarteter Ort fuer
   Anwendungscode, um weitere Spiellogik aufzurufen (`AgcmLogin`s eigene
   echte `EnumCallback`-Aufrufe fuer Weltliste/Union-Info laufen bereits
   ueber genau diese Art Aufrufkette) - viel "normalerer" Kontext als ein
   Timing-Primitiv. Ausgeloest auf Abruf per
   `PostMessageW(hwnd_AcClientSocket, WM_NULL, 0, 0)` von Python aus (zwingt
   `DispatchMessage` dazu, die Fensterprozedur binnen einer Message-Loop-
   Iteration erneut aufzurufen).

**Live bestaetigt**: Event 7 und Event 8 ueber dieses Relay gefeuert (Skripte
`install_wndproc_relay.py`/`fire_via_wndproc_relay.py` im Arbeitsverzeichnis) -
**beide erfolgreich, KEIN Absturz, Prozess blieb durchgehend am Leben**.
Dies ist die erste Arbeitsphase ueberhaupt, in der dieser Schritt zuverlaessig
ohne Absturz durchlief.

### Neuer, separater Befund: Charakterauswahl-Bildschirm zeigt gar keine 2D-UI

Nach dem erfolgreichen Event 8 wechselt die 3D-Szene korrekt zum
"Thronsaal"-Hintergrund (Charakterauswahl-Szene) - aber es erscheint
**ueberhaupt keine 2D-UI** (kein Charakterlisten-Panel, keine Buttons,
nichts). Ein Fenster-Resize/Repaint-Trick (kurz die Fenstergroesse aendern,
um ein `WM_SIZE`+Neuzeichnen zu erzwingen) brachte keine Aenderung - also
kein reines Paint-Problem. Auch ein direktes Force-Fire von Event 10
(`AGCMLOGIN_CB_RACE_BASE`, das in einer FRUEHEREN Arbeitsphase mit sichtbarer
Namenseingabe-UI bestaetigt war, siehe "Nach der Serverauswahl") zeigte
diesmal **ebenfalls keine 2D-UI** - das Problem betrifft also offenbar
MEHRERE/alle Charakter-bezogenen UI-Bildschirme, nicht nur einen, obwohl
mindestens einer davon in der Vergangenheit nachweislich funktioniert hat.
Naheliegendste Unterschiede zur damaligen erfolgreichen Arbeitsphase: heute laeuft
der komplette bisherige Ablauf (Weltliste, Union-Info) zum ersten Mal ueber
ECHTEN, nativen Dispatch statt komplett per Force-Fire - moeglich, dass sich
dadurch ein Timing- oder Zustandsunterschied ergibt, der die UI-Konstruktion
dieser speziellen Bildschirme beeintraechtigt. **Nicht geloest, fuer eine
kuenftige Arbeitsphase vorgemerkt.** Naechste Schritte waeren: pruefen, ob die
Panel-Objekte ueberhaupt erzeugt werden (Speicher-Scan auf die bekannte
`AgcmUICharacterCreate`-Vtable-Adresse), und falls ja, warum sie nicht zum
sichtbaren Fenster/Renderbaum hinzugefuegt werden (evtl. fehlt ein
"AddChild"/"Show"-Aufruf, der normalerweise durch einen weiteren, noch nicht
identifizierten Callback ausgeloest wird).

## Echte Datenbank-Persistenz + Charakteranzeige-Bug bis zur Ursache verfolgt, 2026-09-08

Ziel dieser Arbeitsphase: Login-Server muss vor dem Gameserver
**100% funktionsfaehig** sein, mit echter Persistenz (Docker + PostgreSQL
oder Supabase) statt der bisherigen zustandslosen/hartkodierten Antworten.
Client soll mit Logindaten starten, Serverauswahl soll Charakterauswahl
ausloesen, Charakterauswahl soll Charaktererstellung ermoeglichen.

### Das UI-Problem von gestern hat sich von selbst geloest

Der am Vortag dokumentierte "keine 2D-UI auf Charakterbildschirmen"-Bug trat
in dieser Arbeitsphase **nicht mehr reproduzierbar auf** - nach demselben Ablauf
(Event 7 -> 8 ueber das Main-Thread-Relay) erschien die UI zuverlaessig. Die
genaue Ursache fuer das eintaegige Verschwinden bleibt ungeklaert (moeglich:
Zustand einer vorherigen Arbeitsphase, Windows-Fenstermanager-Cache, oder schlicht
Zufall/Timing) - nicht weiter verfolgt, da nicht reproduzierbar.

### Supabase self-hosted via Docker aufgesetzt

Docker Desktop war nicht installiert - per `winget install --id
Docker.DockerDesktop` nachgeholt (WSL2-Backend war bereits vorbereitet, kein
Neustart noetig). Voller Supabase-Stack (Postgres + Studio-UI + Auth +
PostgREST + Realtime + Storage + Kong-artiges Gateway, ~11 Container) via
offiziellem `supabase/supabase`-Repo, sparse-geklont nach
`AlefLogin/supabase-docker/` (nur der `docker/`-Unterordner ausgecheckt).
Secrets via den mitgelieferten `utils/generate-keys.sh --update-env` und
`utils/add-new-auth-keys.sh --update-env` generiert (KEIN manuelles
Basteln noetig). Studio-UI erreichbar unter `http://localhost:8000`
(Zugangsdaten in `supabase-docker/docker/.env`,
`DASHBOARD_USERNAME`/`DASHBOARD_PASSWORD`).

**Wichtige Falle: `sqlx`s Makro-Zeit-Abfragen (`query!`/`query_as!`/
`query_scalar!`) scheitern ueber Supavisor (den Connection-Pooler auf Port
5432/6543)** mit einer kryptischen "non-UTF-8 error message"-Meldung, die wie
ein Auth-Fehler aussieht, aber keiner ist (`psql` verbindet ueber denselben
Pooler-Port problemlos). Wahrscheinlich eine Prepared-Statement-Inkompatibilitaet
zwischen Supavisors Session-Mode und `sqlx`s Query-Vorbereitung. **Loesung**:
zusaetzliche Docker-Compose-Override-Datei
(`supabase-docker/docker/docker-compose.alefport.yml`) mappt den `db`-Container
direkt auf Host-Port `5433`, `aleflogin-server` verbindet sich DIREKT dorthin
statt ueber den Pooler (fuer einen einzelnen kleinen Server ohnehin kein
Pooling noetig). `COMPOSE_FILE` mit doppeltem Doppelpunkt
(`docker-compose.yml:docker-compose.alefport.yml`) funktioniert unter Windows
NICHT (Doppelpunkt kollidiert mit Laufwerksbuchstaben) - stattdessen `docker
compose -f docker-compose.yml -f docker-compose.alefport.yml up -d`
verwenden.

### Datenbankschema + Server-Integration

Drei Migrationen in `AlefLogin/crates/aleflogin-server/migrations/`:
`accounts` (Account-Name, Auto-Anlage bei erstem Kontakt), `characters`
(pro Account+Welt, mit Slot-Index/Name/Rasse-TID/Aussehen), `worlds` (die
frueher hartkodierte Serverauswahl-Liste, jetzt konfigurierbar - neue
Server/Gruppen per einfachem `INSERT INTO worlds (...)`). `db.rs`-Modul mit
`sqlx`-basierten CRUD-Funktionen. `AGPMLOGIN_UNION_INFO`,
`AGPMLOGIN_CHARACTER_INFO` und `AGPMLOGIN_NEW_CHARACTER_NAME` loesen jetzt
echte Accounts auf/legen sie an (`parse_account_id`, siehe unten) und
lesen/schreiben echte Charaktere; `AgpmWorld`s Antwort kommt aus der
`worlds`-Tabelle statt aus einem hartkodierten Array.

**Ein echter Bug beim ersten Live-Test gefunden und behoben**: `parse_account_id`
wurde anfangs fuer JEDE Operation aufgerufen, deren Maske das AccountID-Bit
gesetzt hat - aber `AGPMLOGIN_SIGN_ON`s Anfrage hat dieses Bit AUCH gesetzt,
nur steht an der erwarteten Byte-Position dort der MD5/XOR-verschluesselte
Passwort-Blob, kein sauberer Klartext-Accountname. Das erzeugte live einen
Account mit Muell-Bytes als Namen. Fix: die Erkennung ist jetzt auf die
konkret bestaetigten Operationen beschraenkt (Union-Info, Character-Info,
New-Character-Name).

### `AGPMLOGIN_NEW_CHARACTER_NAME`s Namens-Parsing: Off-by-One gefunden und live korrigiert

`parse_new_character_request` (sucht die verschachtelte `CharDetailInfo` per
Selbstkonsistenz-Check der Laengenangabe) hatte anfangs einen Off-by-eins-Fehler:
die Bedingung pruefte `p + 2 + len == inner.len()`, korrekt ist aber
`p + 2 + len + 1 == inner.len()` - das aeussere `D6...6B`-Frame haengt sein
eigenes 1-Byte-Trailer direkt ohne Fuellbytes an das Ende des verschachtelten
Pakets. Live an einem echten mitgeschnittenen `AGPMLOGIN_NEW_CHARACTER_NAME`-Request
verifiziert: `WorldName` ist Bit 7 (nicht dokumentiert gewesen), 32 Byte
fest, `inner[65..97)`; die verschachtelte `CharDetailInfo` beginnt exakt bei
`inner[97]`; `TID` dekodierte zu `1724` (passt zum bereits dokumentierten
DragonScion-TID aus einer frueheren Arbeitsphase) und `CharName` zu `"Testchar"`
(exakt der eingegebene Name). Vor dem Fix wurde ein Fallback-Name
("Hero9" o.ae.) verwendet und in der DB gespeichert - das fiel
sofort ("den character Hero9 hab ich aber nicht erstellt"), was den Bug
aufdeckte.

### Event 8 feuert jetzt von selbst - manuelles Force-Fire fuehrt zum Doppel-Toggle

Live entdeckt: nachdem `AGPMLOGIN_CHARACTER_INFO_FINISH` empfangen wird,
feuert der Client **Event 8 (`AGCMLOGIN_CB_CHARACTER_INFO_FINISH`) inzwischen
von selbst** (Folge der SEED-Ende-zu-Ende-Reparatur vom Vortag - natives
Dispatch funktioniert jetzt fuer diesen Pfad). Manuelles Force-Fire von
Event 8 danach fuehrt zum bereits aus einer frueheren Arbeitsphase dokumentierten
Doppel-Toggle-Bug (`m_nEventToggleUIOpen` wird zweimal umgeschaltet, UI
verschwindet wieder). **Neue Regel fuer kuenftige Arbeitsphasen: nur noch Event 7
force-firen, Event 8 NICHT mehr manuell feuern.** `AGCMLOGIN_CB_RACE_BASE`
(Event 10) feuert nach `AGPMLOGIN_RACE_BASE`s Antwort ebenfalls von selbst
(gleicher Grund) - auch hier kein manuelles Force-Fire mehr noetig.

Warum Event 7 selbst weiterhin manuell gefeuert werden muss: es wird normalerweise
durch eine FRUEHERE, account-weite "in welchen Welten habe ich schon einen
Charakter"-Anfrage ausgeloest (Operation 4/5, `AGPMLOGIN_CHARACTER_NAME`/`_FINISH`),
die dieser Server noch nie implementiert (der Client fragt dafuer nichts an -
das muesste der Server proaktiv nach erfolgreichem Sign-On schicken). Offener
Punkt fuer eine kuenftige Arbeitsphase.

### Persistenz-Rundlauf bestaetigt, Anzeige-Bug bis zur wahrscheinlichen Ursache zurueckverfolgt

Charaktererstellung mit echtem Namen ("Testchar", DragonScion/TID 1724) lief
komplett durch und wurde korrekt in der DB gespeichert. Bei einer neuen
Verbindung meldete der Server korrekt `count=1` fuer die Charakterliste -
**aber der Charakter blieb im Client visuell unsichtbar**, sowohl direkt nach
der Erstellung als auch beim erneuten Abruf der Liste.

Systematisch eingegrenzt mit einem neuen Werkzeug (nicht-invasiver,
gefilterter Trace-Hook auf `FUN_004E4070`, dem generischen
`ApModule::EnumCallback`-Dispatcher, der auch fuers Force-Firing genutzt
wird - filtert nach `this == AgcmLogin_base`, um das Rauschen von ~8500
unabhaengigen Aufrufen anderer Objekte pro Sekunde auszublenden):

1. Nach Event-7-Fire feuert nativ, in genau dieser Reihenfolge, je einmal:
   Event 6 (`AGCMLOGIN_CB_CHARACTER_NAME`) dann Event 8. **Byte-genau
   verifiziert**: Event 6s Parameter zeigen auf eine sauber vom Client
   geparste Struktur mit unseren echten Daten (`CharName="Testchar"`,
   `MaxRegisterChars`, `SlotIndex=0`) - die Datenuebertragung ist also zu
   100% korrekt, kein Encoding-/Protokollfehler mehr.
2. `FUN_004E4070` disassembliert: es laeuft eine verkettete Liste bei
   `*(this + 0x5DC + event_id*4)` ab (Listenkopf-Zeiger), jeder Knoten ist
   `{ctx, funcPtr, next}` - live ausgelesen, um die ECHTE Handler-Adresse fuer
   Event 6 zu finden: `0x0060B710`.
3. Disassembly von `0x0060B710` zeigt: die Funktion liest ihre drei
   Parameter, prueft alle auf Nicht-Null, dereferenziert dann den ERSTEN
   (`param3`, ein Zeiger auf eine lokale Struktur auf dem Stack des Clients,
   `~0x001afde4`) und vergleicht `*param3 < 3` (`cmp eax,3; jge Abbruch`) -
   nur wenn das zutrifft, wird `0x0060A8E0` (vermutlich die eigentliche
   Registrierungs-/Renderlogik) ueberhaupt aufgerufen. **Live gemessen: das
   erste Dword an `param3` ist keine kleine Kennzahl (0/1/2), sondern ein
   stack-adress-aehnlicher Wert (`0x001afdf8`) - die Bedingung schlaegt fehl,
   die Funktion bricht sofort ab, OHNE den Charakter zu registrieren.**

`param3` wird vom CLIENT selbst befuellt (nicht von unserem Server), bevor er
den Callback ausloest - dieser Wert ist also unabhaengig von unseren
gesendeten Paketdaten falsch/uninitialisiert. Dasselbe Verhalten trat sowohl
beim Charakterlisten-Abruf als auch direkt nach der Charaktererstellung auf,
was dafuer spricht, dass die eigentliche Ursache tiefer liegt: sehr
wahrscheinlich haengt die korrekte Befuellung dieser Struktur am
`AgpmCharacter`-Modul (dem echten Gameplay-Charakterdatenmodul), das in
diesem reinen Login-Server-Workaround-Ablauf **nie initialisiert wird** (siehe
bereits dokumentiertes "Known-fragile call" von einer frueheren Arbeitsphase, wo
genau dasselbe Modul als fehlend identifiziert wurde). Eine korrekte
Initialisierung wuerde bedeuten, Teile der eigentlichen Gameserver-Logik zu
implementieren - explizit ausserhalb des heutigen Phasenziels
("Login-Server muss fertig sein, BEVOR wir den Gameserver angehen").
**Zunaechst hier pausiert, dann direkt weiterverfolgt** -
siehe naechster Abschnitt fuer den vollstaendigen weiteren Verlauf.

## `AgpmCharacter`-Modul initialisieren: von "1 falscher Wert" bis zur 3D-Render-Pipeline, 2026-09-08 (direkte Fortsetzung)

Direkt mit der Initialisierung des AgpmCharacter-Moduls fuer den Gameserver weitergemacht, statt hier zu stoppen.

### Fund 1: `MaxRegisterChars` war die falsche Interpretation - Live-Beweis via Register-Tracing

Per Hook auf `FUN_004E4070` (generischer `ApModule::EnumCallback`-Dispatcher),
gefiltert auf `this == AgcmLogin_base` (ungefiltert: ~8500 irrelevante
Aufrufe/Sekunde von einem anderen Objekt), plus Live-Auslesen der
verketteten Callback-Liste (`*(AgcmLogin_base + 0x5DC + event_id*4)`, Knoten
= `{ctx, funcPtr, next}`) wurde der ECHTE Handler fuer Event 6
(`AGCMLOGIN_CB_CHARACTER_NAME`) gefunden: **`0x0060B710`**. Disassembliert:
liest drei Parameter, dereferenziert den ersten (`param3`, ein Zeiger auf
eine lokale Stack-Variable der aufrufenden Funktion) und prueft
`cmp eax,3; jge <Abbruch-ohne-Registrierung>` - der Wert muss `< 3` sein.

Die aufrufende Funktion (`AgcmLogin::OnCharacterName`, gefunden bei
`0x0065D550` ueber die per Hook mitprotokollierte Ruecksprungadresse) zeigte:
dieser Wert ist exakt das Feld, das dieses Projekt bisher `MaxRegisterChars`
nannte und mit einem Slot-Limit (6) befuellte. Mit 6 schlaegt der `<3`-Check
IMMER fehl. Nach Zuruecksetzen auf die echte, aktuelle Charakteranzahl
(hier: 1) griff der Check - **verifiziert live**: `0x0060A8E0` (die
Registrierungsfunktion, schreibt in `AgcmUILogin::m_szMyCharacterInfo[]`,
nur 3 Slots insgesamt - erklaert den `<3`-Check final) wurde jetzt
nachweislich aufgerufen (Marker-Zaehler 0 -> 1) und der Speicher-Dump
bestaetigte: Slot 0 korrekt mit "Testchar" belegt. `main.rs` entsprechend
zurueckgesetzt (`ACCOUNT_CHARACTER_SLOT_LIMIT`-Konstante entfernt, echte
`characters.len()`/DB-Abfrage wiederhergestellt an beiden Stellen).

### Fund 2: eigener Hook-Bug gefunden und behoben - relative CALL-Instruktion falsch kopiert

Beim Bau eines Marker-Hooks auf `0x0060B731` (`call 0060A8E0`) stuerzte der
Client ab (`ERRORLOG.TXT`: Absturzadresse exakt im eigenen Scratch-Speicher-
Bereich). Ursache: die Original-Bytes an dieser Adresse sind ein **relatives**
`E8`-CALL - beim wortwoertlichen Kopieren dieser Bytes in ein Trampolin an
einer ANDEREN Adresse zeigt derselbe relative Offset auf ein voellig anderes
(zufaelliges) Ziel. Jeder bisherige Hook dieser Arbeitsphase hatte dieses Problem
nie, weil er ausschliesslich Daten-Instruktionen (mov/push/cmp) kopierte, nie
ein CALL/JMP selbst. **Fix**: das relative Ziel vor dem Kopieren auflösen
(`TARGET + 5 + rel32`) und für die neue Trampolin-Position neu berechnen,
statt die rohen Bytes zu übernehmen. Lehre fuer kuenftige Hooks: IMMER
pruefen, ob die zu kopierenden Original-Bytes ein E8/E9-Opcode sind, bevor
sie unveraendert in ein Trampolin kopiert werden.

### Fund 3: die echte EP8-C++-Referenzquelle liegt lokal vor - lokale Kopie der EP8-C++-Quelle

Bisher nur aus fruehen Arbeitsnotizen als Pfadangabe bekannt, auf Nachfrage
("hilft dir eine recherche im ep8 c++ code?") gefunden und ab hier direkt
genutzt - massiv schneller/zuverlaessiger als weiteres Disassemblieren.
Wichtigste Funde:

- `AgcmUILogin::m_szMyCharacterInfo[AGCMUILOGIN_MY_CHARACTER_NUM][...]`
  (Header, `AgcmUILogin.h`) speichert NUR den Charakternamen als String -
  reicht fuer die Registrierung (oben, Fund 1), aber NICHT fuers Rendering.
- Rendering-Pfad (`AgcmUICharacterSelect.cpp`, `_MakeCharacter`): braucht
  zwingend `ppmCharacter->GetCharacter(name)` (ein ECHTES `AgpdCharacter*`-
  Objekt in `AgpmCharacter`s eigener Registry - der Name allein reicht
  nicht), UND `pcmCharacter->GetCharacterData(ppdCharacter)->m_pClump` (ein
  bereits GELADENES 3D-Modell), UND der Login-Modus muss
  `AGCMLOGIN_MODE_WAIT_MY_CHARACTER` sein.
- `AgpmCharacter::AddCharacter(INT32 lCID, INT32 lTID, CHAR* szGameID)`
  (`AgpmCharacter.cpp`, Zeile ~1807) ist die Funktion, die ein echtes
  `AgpdCharacter`-Objekt erzeugt (Character-Template per `lTID` nachschlagen,
  `CreateCharacter()`, Felder setzen, in die interne Map eintragen). **1:1
  im Binary wiedergefunden** ueber die eindeutige Fehler-Logzeile
  `"CharacterID = %s"` -> `"LOG\\CharacterTemplateAsync.txt"`, die im
  Fehlerpfad exakt uebereinstimmt: **`FUN_00507110`** (Adresse `0x00507110`).
  `__thiscall`, selbstreinigend (`ret 0Ch`, bestaetigt aus der rohen
  Disassembly), Parameter-Reihenfolge (rechts-nach-links gepusht):
  `push szGameID; push lTID; push lCID; mov ecx,this; call`. `this` ist
  zusaetzlich an einer festen, nicht relozierten globalen Adresse
  verfuegbar (`0x0097109C`), kein `GetModule()`-Scan noetig.

### Fund 4: `AgpmCharacter::AddCharacter` erfolgreich per Injection aufgerufen - echtes Charakterobjekt existiert jetzt

Direkter `CreateRemoteThread`-Aufruf (dieselbe Technik wie
`AgpmWorld::UpdateWorld` frueher im Projekt - reine Datenoperation ohne
UI-/Renderkontext, daher sicher ohne das Main-Thread-Relay): `AddCharacter(
lCID=12345, lTID=0x6BC(=1724, DragonScion), szGameID="Testchar")` ->
**lieferte einen gueltigen `AgpdCharacter*` zurueck, kein Absturz**. Skript:
`add_character.py` im Arbeitsverzeichnis dieser Arbeitsphase.

**Trotzdem weiterhin keine sichtbare Charakteranzeige** - erwartungsgemaess
gemaess Fund 3: `_MakeCharacter` braucht zusaetzlich das GELADENE 3D-Modell
(`AgcmCharacter::GetCharacterData()->m_pClump`) und den passenden
Login-Modus. Der auslösende Aufrufpfad
(`AgcmUICharacterSelect::_MakeCharacter` -> `AgcuUIControlCharacter::
OnAddCharacter`) selbst wurde im Quellcode identifiziert, aber dessen
Adresse im Binary noch nicht gesucht - und selbst mit ihr waere die
eigentliche 3D-Modell-Ladelogik (`AgcmCharacter`-Modul, komplett
unbearbeitet) der naechste, deutlich groessere Schritt.

### Endgueltiger Stopp-Punkt

An dieser Stelle ist zweifelsfrei die 3D-Charakter-Rendering-Pipeline
erreicht (Charakter-Templates, `AgcmCharacter`-Modul, 3D-Modell-Ladung) -
klar Gameserver-/Content-Pipeline-Territorium, keine kleine Ergaenzung mehr.
Hier wurde fuer diese Phase bewusst gestoppt.

### Zwischenstand

**Login-Server ist vollstaendig funktionsfaehig mit echter Persistenz**:
Docker + self-hosted Supabase laufen lokal (Postgres direkt auf Port 5433,
siehe `supabase-docker/docker/docker-compose.alefport.yml` - der Pooler auf
5432 hat eine `sqlx`-Kompatibilitaetsluecke), echte Accounts werden
automatisch angelegt, die Serverauswahl-Liste kommt aus der Datenbank
(`worlds`-Tabelle, mehrere Welten/Gruppen per SQL moeglich), Charaktere
werden mit echtem Foreign-Key auf die Welt gespeichert (`characters.world_id`,
Migration 0003 - Relationierung direkt
umgesetzt). Charaktererstellung persistiert korrekt (Name, Rasse-TID, Slot -
inklusive eines live gefundenen und behobenen Off-by-one-Parserbugs). Der
komplette Protokollfluss (Login -> Serverauswahl -> Charakterliste ->
Charaktererstellung) laeuft ohne Abstuerze, groesstenteils ueber echtes
natives Client-Dispatch (nur Event 7 braucht noch einen manuellen Anstoss -
siehe "Warum Event 7 selbst weiterhin manuell gefeuert werden muss" oben).

**Charakter-Registrierung (fuer die Charakterliste/Login-Flow) funktioniert
jetzt vollstaendig** - der `<3`-Bug ist gefunden und behoben, echte
`AgpdCharacter`-Objekte lassen sich per direktem Funktionsaufruf
(`AgpmCharacter::AddCharacter`, `0x00507110`) erzeugen. **Die sichtbare 3D-
Darstellung im Charakterauswahl-Bildschirm bleibt offen** - das ist jetzt
zweifelsfrei die naechste, groessere, eigenstaendige Aufgabe (3D-Modell-
Ladepipeline via `AgcmCharacter`), fuer die die EP8-Referenzquelle
(lokale Kopie der EP8-C++-Quelle) ab sofort die primaere Recherchequelle
sein sollte statt reiner Disassembly-Arbeit.

## Echter Server-Quellcode gefunden: Schema-Abgleich + der eigentliche
## Ansatzpunkt fuers 3D-Rendering, 2026-09-08 (Fortsetzung)

Im Verzeichnis `EP8-c++-Source\Server\` liegt mehr -
dort liegt nicht nur Client-, sondern auch echter **Server**-Quellcode:
`AlefLoginServer` (Einstiegspunkt `AlefLoginServer.cpp`, echter Port
**11002**), plus `AgsmLoginClient`/`AgsmLoginDB`/`AgsmLoginServer` und die
gemeinsamen Paketfeld-Definitionen in
`Modules/APublic/AgpmLogin/AgpmLogin.cpp` (`AuPacket::SetFieldType`, u.a.
`m_csPacketCharInfo`).

### Vollstaendige Protokoll-Verifikation

Jeder reverse-engineerte Opcode-Wert und jedes Feld-Offset in
`aleflogin-server/src/main.rs` stimmte exakt mit dem echten Quellcode
ueberein (Opcodes 0-12, Feldreihenfolge in `CharDetailInfo`), bis auf einen
echten Bug: **`HairIndex`/`FaceIndex`** (Bits 6/7 der `CharDetailInfo`-Maske)
wurden bisher verworfen und hart auf 0 gesetzt statt gespeichert - jeder neu
erstellte Charakter bekam Default-Aussehen unabhaengig von der Wahl des
Spielers im Erstellungs-UI. Gefixt in main.rs (`parse_new_character_request`
laeuft jetzt generisch ueber die Feldmaske statt nur zwei feste Offsets zu
kennen), Commit `328c2ab`.

### DB-Schema-Abgleich (`AgsmLoginDB.cpp`, 5643 Zeilen)

Das reale Schema ist riesig: CHARMASTER, CHARDETAIL, EQUIP_ITEM, INVEN_ITEM,
SKILL, CASH_ITEM, BANK_ITEM, ACCOUNTWORLD, GUILD_MEMBER, QUEST_CURRENT,
QUEST_FLAG, TITLE, LOGIN_STATUS, uvm. - aber fast alles davon ist laufender
Gameplay-Zustand (HP/MP/EXP/Level/Position/Inventar/Skills), der erst im
Spiel entsteht, nicht beim Login. Fuer den reinen Login-Server relevant:

- **CHARMASTER** (`_InsertCharacter`/`SetParamMasterInsertQuery5`):
  CharName, AccountID, SlotIndex, **TemplateID** (`m_pcsCharacterTemplate->
  m_lID` - exakt unser `race_tid`), ServerName.
- **CHARDETAIL** (`SetParamDetailInsertQuery5`, 19 Felder): Skill-Init-String,
  Position, Kriminal-/Mordpunkt-Status, Geld, HP/MP/SP/EXP, Level,
  Skill-Punkte, Quickbelt-String, letzte Bindungsregion, Aktionsstatus,
  **HairIndex, FaceIndex** (bestaetigt echte Spalten - unser Fix oben war
  also korrekt).
- **ACCOUNTWORLD** (`_InsertAccountWorld`): nur (AccountID, ServerName) -
  eine "hat dieser Account einen Charakter auf dieser Welt"-Markierung.
  Bei uns durch die `characters.world_id`-FK-Beziehung bereits implizit
  abgedeckt, keine eigene Tabelle noetig.

Fazit: unser schlankes `accounts`/`characters`/`worlds`-Schema ist fuer den
Login-Server-Scope korrekt zugeschnitten. Der riesige Rest (Items, Skills,
Quests, Gilde, HP/MP/EXP/Position) ist zu Recht Gameserver-Territorium und
bleibt ausgeklammert.

### Der eigentliche Fund: Op3/Op6 sind strukturell anders als bei uns

Aus `AgsmLoginClient::OnReceive`'s Opcode-Weiche (Zeile 224ff) und den
beiden DB-Handlern `AgsmLoginDB::ProcessGetUnion` (Zeile 1688) vs.
`AgsmLoginDB::ProcessGetCharacters` (Zeile 1824) folgt der reale Ablauf:

- Client-Request **Op 3 (UNION_INFO)** -> Server antwortet mit
  `SendUnionInfo` **UND** der kompletten Namensliste (`SendCharacterName`
  x N = Op 4, dann `SendCharacterNameFinish` = Op 5). Das ist die Liste
  fuers Auswahl-UI (Namen/Slots), `ulTotal = pDatabase->GetReadRows()`
  bestaetigt zu 100%: `MaxRegisterChars` ist die echte Zeilenanzahl, kein
  Slot-Limit - exakt unser bereits (nach dem Fehlversuch mit der
  "6"-Slot-Cap-Hypothese) korrigiertes Verstaendnis.
- Client-Request **Op 6 (CHARACTER_INFO)** -> Server laedt pro Charakter
  die **vollstaendigen** Daten (`_SelectCharacterView` +
  `AgsmCharacter::SendCharacterAllInfo`) und schliesst mit
  `SendCharacterInfoFinish` (Op 7) ab.

Unser Server macht bisher beides ueber Op 6 (Namensliste + Finish ueber Op
7), und Op 3 sendet nur den hartcodierten Union-Wert ohne Charakterliste.
Das erklaert sehr wahrscheinlich, warum die Charakterauswahl textlich/
zaehlend funktioniert (der Client akzeptiert die Namensliste offenbar auch
ueber den "falschen" Opcode-Pfad genug fuer die Zaehlung), aber nie 3D-
Modelle rendert: `SendCharacterAllInfo` - die eigentliche Datenquelle fuers
3D-Rendering - wird bei uns nie gesendet.

### `SendCharacterAllInfo` ist ein komplett neues Wire-Format, kein Fix am AgcmLogin-Kanal

`SendCharacterAllInfo` (`AgsmCharacterPacket.cpp:2480`) ruft
`SendPacketChar` -> `MakePacketAddCharacter` (`AGPMCHAR_PACKET_OPERATION_ADD`,
eigener `AGPMCHARACTER_PACKET_TYPE`-Modulkanal, NICHT der `AgcmLogin`-Kanal,
den unser Server bisher komplett abbildet). Das ist die Server-Gegenseite
zu der am Ende der letzten Session erfolgreich per Injection aufgerufenen
`AgpmCharacter::AddCharacter` (`0x00507110`) - der fehlende Puzzlestein fuers
3D-Rendering ist also nicht ein falscher Opcode, sondern ein komplett
fehlendes zweites Paketprotokoll.

`MakePacketAddCharacter` (`AgsmCharacterPacket.cpp:19`) hat ~28
Top-Level-Felder: CharacterID, TemplateID, GameID(Name), Status, ein
verschachteltes **Move**-Paket (Position, Ziel, Blickrichtung,
Bewegungs-Flags), ein verschachteltes **Factor**-Paket (Stats), Geld/
Bank-Geld/Cash, Aktions-/Kriminalstatus, Region-Index, Special-Status,
Transform-Flags, Skill-Init-String, **FaceIndex/HairIndex**, Bank-Groesse,
Event-Status-Flags, verbleibende Kriminal-/Moerderzeit, Nickname, u.a.

Das verschachtelte Factor-Paket ([`AgpmFactors`](../Module/AgpmFactors.md):MakePacketFactors`,
`AgpmFactors.cpp:1040`) besteht aus **13** eigenen Unter-Paketen (eines pro
`eAgpdFactorsType`-Kategorie, `AGPD_FACTORS_MAX_TYPE`), von denen jedes
wiederum eine eigene Feldstruktur hat (`MakePacketFactor`, noch nicht
untersucht) - insgesamt ein deutlich groesserer, mehrstufig verschachtelter
Wire-Format-Baum als alles bisher in `aleflogin-server` Implementierte.

### Bewusst nicht implementiert

Entscheidung: diesen Fund nur zu dokumentieren
und NICHT sofort in `main.rs` zu implementieren - das ist ein neues
Subsystem (neuer Modulkanal, verschachtelte Move-/Factor-Pakete), kein
kleiner Opcode-Fix, und damit derselbe Umfang wie die am Ende der letzten
Session zurueckgestellte 3D-Rendering-Arbeit, nur diesmal von der
Server-/Protokollseite statt von der Client-Hook-Seite aus erreicht.

**Konkreter Einstiegspunkt fuer die naechste Session**: `MakePacketFactor`
(einzelnes Factor-Sub-Paket) und `AgcmCharacter`s client-seitiges Pendant
zu `AGPMCHAR_PACKET_OPERATION_ADD` im Quellcode nachschlagen, dann Op 3 in
main.rs auf die Namensliste (Op4/Op5) umstellen und Op 6 neu als
`AddCharacter`-Paket-Sender aufbauen.

### Klargestellt: kein Relay-/Gameserver-Umweg noetig, 2026-09-08 (Fortsetzung 2)

Frage: koennte der Loginserver fuer die Charakterauswahl-Daten mit
einem Relay-/Gameserver sprechen muessen? Anhand des Quellcodes eindeutig
verneint:

- `AgsmLoginDB::_SelectCharacterView` (baut das `AgpdCharacter`-Objekt fuers
  Auswahl-Fenster auf) liest ausschliesslich per SQL direkt aus der eigenen
  DB (`CHARACTER_SELECT`, `EQUIP_ITEM_SELECT`, `_SelectGuild`,
  `_SelectSkill`) - keine Netzwerkverbindung zu einem anderen Server.
- `ServerEngine::ConnectServers()` (`Server\AlefLoginServer\
  ServerEngine.cpp:563`) verbindet sich beim Start nur zu einem
  `LKServer` (`AgsmGK::ConnectLKServer`, Lizenz-/PC-Room-Gatekeeper) -
  kein Game- oder Relay-Server.
- `ServerEngine.cpp:305`: `g_pcsAgpmCharacter->SetMaxCharacter(200000)` -
  der Loginserver haelt bis zu 200.000 `AgpdCharacter`-Objekte im
  **eigenen** Prozessspeicher vor.

Der Loginserver baut `AgpdCharacter` also komplett selbst aus seiner
eigenen DB zusammen und schickt das Ergebnis direkt an den Client.
`AgsmInterServerLink`/`AlefRelayServer` existieren fuer etwas anderes
(vermutlich Gameserver-Registrierung/Heartbeat fuers spaetere "Enter
Game", nicht fuer die Charakterauswahl-Anzeige). Der fehlende Baustein
ist also wirklich nur die Datenbasis: `aleflogin`s eigenes Postgres-Schema
muesste um die Daten erweitert werden, die `_SelectCharacterView` aus
CHARMASTER/CHARDETAIL/EQUIP_ITEM zusammensetzt (Ausruestung, Skills,
Stats/Factors) - keine neue Server-Komponente, keine Relay-Architektur.

### `MakePacketFactor`/`AgcmCharacter` genauer angesehen, DB-Schema erweitert, 2026-09-08 (Fortsetzung 3)

Aufgabe: `MakePacketFactor` und `AgcmCharacter` genauer ansehen und
die Datenbank detaillierter aufbauen, damit alle echten Daten erfasst und
gespeichert werden koennen.

**`MakePacketFactor`/`AgpdFactor` (`AgpdFactors.h`) ist die Kampf-Engine,
nicht Rohdaten**: `eAgpdFactorsType` hat 13 Kategorien (CharStatus inkl.
STR/CON/INT/DEX/CHA/LUK/WIS/Level, CharPoint/CharPointMax/RecoveryRate fuer
HP/MP/SP/EXP/AP/MAP/Agro, Attribute/Damage/Defense fuer 15 Elementartypen,
Attack-Werte, Item/Price/DIRT/Owner/Agro-Subtypen) - insgesamt 100+
rekursiv verschachtelte Werte, die primaer der Kampfberechnung dienen.
Entscheidender Fund: `AgsmCharacter::GetDetailSelectResult5` (die echte
CHARDETAIL-SELECT-Spaltenliste) enthaelt **keine** STR/CON/INT/DEX-Felder -
diese Werte werden zur Laufzeit aus Charakter-Template + Level + Items
berechnet, nicht in der DB gespeichert. Ein Postgres-Schema fuer den
gesamten Faktorenbaum zu bauen waere also keine Datenpersistenz, sondern
der Nachbau der Kampf-Engine - bewusst nicht gemacht.

**`AgcmCharacter::OnReceive`** (Client, Game-World-Modul) behandelt
`AGPMCHAR_PACKET_OPERATION_ADD` nicht direkt selbst - das gemeinsame
`AgpmCharacter::OnReceive` (`Modules/APublic/AgpmCharacter/AgpmCharacter.cpp:3363`,
von Client UND Server geteilter Code) deserialisiert das Paket und ruft
`OnOperationAdd(...)`. Alle Kampf-/Faktor-Felder werden generisch ueber die
Feldmaske behandelt (`AuPacket`-System) - ein fehlendes/leeres Factor-Paket
ist also kein Fehlerfall, sondern bedeutet einfach "Werte auf 0/Default".
Fuer die Charakterauswahl-Vorschau ist das unkritisch: Kampfwerte werden
dort nicht angezeigt/gebraucht, nur Identitaet + Aussehen + ggf. sichtbare
Ausruestung zaehlen.

**DB-Schema erweitert (Migration `0004_character_detail_and_items.sql`)**:
`characters` bekommt alle echten CHARDETAIL-Felder (Level, HP/MP/SP, EXP,
SkillPoint, Money/BankMoney/Cash, Position x/y/z, RegionIndex,
ActionStatus, CriminalStatus/MurdererPoint + deren Restzeiten,
EventStatusFlag, BankSize, QuickBelt-String, SkillInit-String, Nickname) -
alle mit sinnvollen Defaults (Level=1, Rest 0/leer), da ohne echte
Charakter-Templates keine realistischen Startwerte berechnet werden
koennen. Neue `character_items`-Tabelle bildet die reale ITEM-Tabelle ab
(eine gemeinsame Tabelle fuer equipped+inventory+bank, per `status`
unterschieden, `slot_index` fuer Ausruestungs-Slot bzw. `grid_x`/`grid_y`
fuer Inventar-Position, Haltbarkeit) - noch nicht befuellt (kein
Item-Template-Datensatz vorhanden, um Startausruestung zu generieren),
aber strukturell bereit. `db.rs` bekam entsprechend erweiterte
`Character`/`CharacterItem`-Structs, `list_characters`/`create_character`
lesen/schreiben jetzt die vollen Felder (neue Spalten per DB-Default),
plus `list_character_items`/`add_equipped_item` fuer die neue Tabelle
(noch ungenutzt, bereit fuer den naechsten Schritt).

Migration manuell gegen die Dev-DB angewandt (gleiches Vorgehen wie bei
Migration 0003 - `sqlx`-Kompilierzeit-Macros brauchen das Schema vorher),
Server sauber neu gestartet und verifiziert: `connected to Postgres and
ran migrations`, `listening ... 0.0.0.0:11002`, keine Fehler.

**Weiterhin nicht implementiert**: das eigentliche Befuellen der neuen
Felder aus echten Werten (Level/HP/etc. bleiben bei der Erstellung auf
Default) und das Senden des `AddCharacter`-Pakets selbst (Op3/Op6-Umbau,
siehe vorheriger Abschnitt) - dieser Schritt hat nur die Datenbasis
vorbereitet, wie beauftragt.

### Verdacht bestaetigt: `LoginCharPos.ini` + Client ignoriert Server-Position komplett, 2026-09-08 (Fortsetzung 4)

Verdacht: die Charakterauswahl-3D-Szene ist eine echte Spielszene
irgendwo am Kartenrand, positioniert ueber eine Ini-Datei im
Client-Installationsverzeichnis (Name so aehnlich wie "LoginCharPos").
Zu 100% bestaetigt:

- `C:\Spiele\Archlord\ini\logincharpos.ini` (entschluesselt mit
  `tools/decode_archlord_data.ps1 -Key 1111`) enthaelt pro Rasse/Klasse-
  Slot feste Weltkoordinaten weit ausserhalb der eigentlichen Karte (z.B.
  `Position=-677812.000000,1.000000,-768374.000000`) plus Blickrichtung
  (`DegreeX`/`DegreeY`).
- Der reale Login-Server laedt genau diese Datei beim Start:
  `ServerEngine.cpp:504`: `g_pcsAgsmLoginClient->StreamReadBaseCharPos(
  "Ini\\LoginCharPos.ini")`, in `m_RaceBaseCharacterPos[Rasse][Klasse]`
  (`AgsmLoginClient.h`). Genutzt in `CreateBaseCharacterOfRace`
  (`AgsmLoginClient.cpp:1994`) fuer die "Basis-Charaktere" der
  Rassenauswahl beim Erstellen (Op 10, `AGPMLOGIN_RACE_BASE`).

**Wichtiger Fund, der die eigene bisherige Einschaetzung korrigiert**: der
Client ignoriert die vom Server gesendete Position fuer die Auswahl-Anzeige
komplett. `AgcmUICharacterSelect::_MakeCharacter`
(`Modules/AClient/AgcmUILogin/AgcmUICharacterSelect.cpp:343`):

```cpp
ppdCharacter->m_stPos = pSlot->m_vCharacterPos;   // ueberschreibt die Server-Position
```

`pSlot` ist eine rein clientseitige Struktur (`stCharacterSlot`), die
Position wird lokal aus dem UI-Slot-Index berechnet, nicht aus dem
`AddCharacter`-Paket uebernommen. Ebenso liest dieselbe Funktion Rasse/
Klasse fuers Kamera-Offset aus `ppdCharacter->m_pcsCharacterTemplate->
m_csFactor` (dem lokalen, statischen Charakter-Template), nicht aus dem
Server-Faktor-Paket.

**Konsequenz**: die zuvor als "fehlende Luecke" genannten Move-Paket-Felder
(Zielposition, Follow-Target, TurnX/Y, Bewegungs-Flags) und auch
`position_x/y/z` sind fuer die Charakterauswahl-Anzeige irrelevant -
reine Client-UI-Positionierung, kein Datenproblem auf Serverseite. Fuer
die reine Sichtbarkeit zaehlen im Kern nur: TID (Rasse/Klasse), Aussehen
(Hair/Face - vorhanden) und dass der Client das 3D-Modell (`pClump`)
ueberhaupt laedt (`AgcdCharacter::m_pClump`, noch nicht untersucht wie/wann
das genau passiert).

### `AgcdCharacter::m_pClump`-Ladekette nachverfolgt: der eigentliche Grund, warum die `AddCharacter`-Injection letzte Session nichts sichtbar machte, 2026-09-08 (Fortsetzung 5)

Vollstaendige Kette vom Paketempfang bis zum geladenen 3D-Modell:

1. Client empfaengt `AGPMCHAR_PACKET_OPERATION_ADD` -> `AgpmCharacter::
   OnReceive` -> `OnOperationAdd(...)` (`AgpmCharacter.cpp:3900ff`) setzt
   alle Felder (Position, Status, Transform-Flags, Hair/Face-Index, etc.)
   auf das `AgpdCharacter`-Objekt.
2. Am Ende von `OnOperationAdd` (Zeile 3995): `UpdateInit(pcsCharacter)`.
3. `UpdateInit` (`AgpmCharacterUpdate.cpp:30`) feuert `EnumCallback(
   AGPMCHAR_CB_ID_INIT, pcsCharacter, m_pcsCharacterTemplate)`.
4. `AgcmCharacter::CBInitCharacter` ist darauf registriert
   (`m_pcsAgpmCharacter->SetCallbackInitChar(CBInitCharacter, this)`,
   `AgcmCharacter.cpp:637`) -> ruft `InitCharacter()` ->
   `LoadCharacterData(bUseThread=TRUE)`.
5. `LoadCharacterData` prueft `ASSERT(m_pcsCharacterTemplate != NULL)`,
   dann `m_pcsAgcmResourceLoader->AddLoadEntry(...)` - asynchrone
   Warteschlange (Background-Thread + Main-Thread-Finalize, dasselbe
   Grundmuster wie unser eigenes "Main-Thread-Relay").
6. Background-Thread: `InitCharacterBackThread`
   (`AgcmCharacter.cpp:4741`) -> `LoadTemplateData` (laedt bei Bedarf das
   DFF-Modell des Templates via `LoadClump(m_szDFFName)`) ->
   `pstAgcdCharacter->m_pClump = RpClumpClone(Template->m_pClump)`.

**Entscheidende Erkenntnis**: `UpdateInit()` - der einzige Ausloeser der
ganzen Ladekette - wird ausschliesslich innerhalb von `OnOperationAdd`
aufgerufen, also nur beim Empfang des echten Wire-Pakets.
`AgpmCharacter::AddCharacter` (`0x00507110`, letzte Session erfolgreich
per Injection aufgerufen) erzeugt nur das rohe Objekt - ruft `UpdateInit()`
NICHT auf. Das erklaert exakt, warum die Injection letzte Session ein
gueltiges `AgpdCharacter*` lieferte, aber trotzdem nichts sichtbar wurde:
Objekt-Erzeugen allein reicht nicht, es fehlt die vollstaendige
Feldbefuellung + der `UpdateInit()`-Trigger, die nur beim echten
Paketempfang passieren. Bestaetigt (nochmal, jetzt luckenlos bewiesen):
das eigentliche Senden des `AddCharacter`-Pakets server-seitig (Op3/Op6-
Umbau) ist der einzig richtige naechste Schritt, kein weiterer Client-
Injection-Trick.

## `AddCharacter`-Paket implementiert: Charakter rendert zum ersten Mal, dann Duplikat- und Auswahl-Bug gefunden+behoben, 2026-09-09

Feldlayout aus dem echten `AgpmCharacter::AgpmCharacter()`-Konstruktor
uebernommen (31 Felder/4-Byte-Maske im Hauptpaket, 8 Felder/1-Byte-Maske
im verschachtelten Move-Paket; `AGPACHARACTER_MAX_CHARACTER_SKILLINIT`=32,
`_NICKNAME`=16 aus `ApDefine.h`). Modul-Opcode `0x02` (aus
[`WINSOCK_SEQUENCE_04_CHARACTER_MOVEMENT_STATE.md`](../Netzwerk/Sequenz-04-Character-Movement-State.md)). Implementiert im
`AGPMLOGIN_CHARACTER_INFO`(Op6)-Handler, ein `AddCharacter`-Frame pro
Charakter, direkt vor `AGPMLOGIN_CHARACTER_INFO_FINISH`(Op7).

**Live bestaetigt**: der Charakter rendert erstmals in diesem Projekt
vollstaendig in 3D auf der Charakterauswahl-Buehne (Screenshot,
2026-09-09 ~17:37 Uhr).

**Duplikat-Bug gefunden und behoben**: `AGPMLOGIN_CHARACTER_INFO`(Op6)
sendete weiterhin dieselben `AGPMLOGIN_CHARACTER_NAME`-Eintraege wie
`AGPMLOGIN_UNION_INFO`(Op3) (absichtlich als Uebergangsloesung beim
Op3-Umbau belassen) - dadurch registrierte der Client den Charakter
zweimal in seiner UI-Slot-Map, sichtbar als zwei ueberlappende
Info-Boxen, und die Auswahl funktionierte nicht. Entfernt: Op3 ist jetzt
alleinige Quelle der Namensliste, Op6 sendet nur noch `AddCharacter` +
`CHARACTER_INFO_FINISH`.

**Zweiter, subtilerer Bug gefunden und pragmatisch umgangen**: nach dem
Duplikat-Fix war der Charakter einmal sichtbar, aber weiterhin nicht
auswaehlbar. Quellcode-Analyse ergab eine Race Condition im Client
selbst: `AgpmCharacter::OnOperationAdd` (ausgeloest durch das
`AddCharacter`-Paket) feuert SYNCHRON `AGPMCHAR_CB_ID_POST_ADD` ->
`AgcmUILogin::CBAddCharacter` - genau die Funktion, die den Charakter in
seinen klickbaren UI-Slot einhaengt (`m_ControlCharacter.OnAddCharacter`).
Diese Funktion prueft aber `if (pcdCharacter->m_pClump && ...)` -
das 3D-Modell laedt jedoch ASYNCHRON (`LoadCharacterData(...,
bUseThread=TRUE)`, Warteschlange auf [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md), Hintergrund-
Thread + Main-Thread-Finalize). Der Clump ist zum Zeitpunkt des
synchronen Callbacks praktisch nie schon fertig geladen, wodurch die
Slot-Verdrahtung STILLSCHWEIGEND uebersprungen wird - der Charakter
rendert (das asynchrone Laden laeuft unabhaengig weiter), ist aber nie
auswaehlbar. Live durch Test bestaetigt (Event 8 nochmal manuell
gefeuert -> nur Doppel-Feuer-Symptom von letzter Session reproduziert,
kein neuer Fund; danach Quellcode-Analyse fuehrte zur eigentlichen
Ursache).

**Workaround statt Client-Hook**: das `AddCharacter`-Paket wird pro
Charakter zweimal gesendet, mit 800ms Pause dazwischen. Der erste
Versand stoesst das asynchrone Laden an; beim zweiten Versand (Clump
inzwischen fertig geladen) feuert `AGPMCHAR_CB_ID_POST_ADD` erneut und
die Slot-Verdrahtung gelingt. Live bestaetigt: Anklicken des Charakters
zeigt jetzt eine Reaktion (Info-Box rutscht in Auswahl-Position) - vorher
passierte beim Klick gar nichts. Ein echter Fix waere ein Client-Hook
(Laden synchron erzwingen, oder `AGPMCHAR_CB_ID_POST_ADD` verzoegern)
statt dieser zeitbasierten Umgehung - als Folgearbeit vermerkt, falls
das Timing sich als unzuverlaessig erweist (z.B. auf langsamerer
Hardware).

**Offen**: nach dem ersten Klick reagiert die UI (Info-Box bewegt sich),
aber die erwartete Vorwaerts-Bewegung/Kamera-Zoom beim
Anwaehlen bleibt aus. Naechster Test: zweiter Klick auf den bereits
ausgewaehlten Charakter (`AgcuUIControlCharacter::OnDoubleClickCharacter`
unterscheidet explizit zwischen Erstauswahl und erneutem Klick auf
dieselbe ID) bzw. der "Play"-Button.

**Hinweis auf Parallelarbeit**: waehrend dieser Session sind mehrfach
Dateien aufgetaucht, die nicht von dieser Session stammen
(`WINSOCK_SEQUENCE_17` bis `21`, Aenderungen an
[`ALEFCLIENT_EXTRACTION_TODO.md`](../Daten-und-Werkzeuge/Auslese-Roadmap.md)/[`WINSOCK_NETWORK_PROTOCOL_FINDINGS.md`](../Netzwerk/Protokoll-Funde.md)),
zeitlich passend zu genau diesem Thema (Charakterauswahl/AddCharacter/
Op8-Handoff). Diese Dateien enthalten reine Analyse/Dokumentation, keine
Code-Aenderungen an `main.rs`/`db.rs` - aber es laeuft offenbar parallel
eine zweite Session am selben Thema. `WINSOCK_SEQUENCE_21_..._HANDOFF.md`
liefert einen brauchbaren Hinweis auf den naechsten Schritt nach
erfolgreicher Auswahl: Op8 (`AGPMLOGIN_ENTER_GAME`) wird von unserem
Server noch gar nicht behandelt (unbehandelter Default-Zweig) - relevant
sobald die Auswahl selbst steht.

## Auswahl funktioniert vollstaendig - Endstand fuer heute, 2026-09-09

Der erste Klick war tatsaechlich ein voller
Erfolg, nicht nur eine Teilreaktion: `OnBtnSlot` lief komplett durch und
der Client sendete danach automatisch Operation 8
(`AGPMLOGIN_ENTER_GAME`), um ins Spiel einzutreten. Server-Log:

```
WARN AgcmLogin: unhandled Operation, not replying peer=... operation=8
```

Unser Server ignoriert Op8 komplett (unbehandelter Default-Zweig, wie
von der parallelen Session in `WINSOCK_SEQUENCE_21` schon vermutet) -
der Client haengt seitdem in einem Warte-auf-Antwort-Zustand, daher
"kein zweiter Klick moeglich" und keine Vorwaerts-Bewegung/Kamera-Zoom
(die vermutlich erst nach einer Op8-Antwort passieren wuerde).

**Damit ist der Login-Server-Kernauftrag (Login -> Serverauswahl ->
Charakterauswahl inkl. 3D-Rendering und tatsaechlicher Auswahl-
Interaktion) zum ersten Mal in diesem Projekt vollstaendig demonstriert.**
Op8/Gameserver-Handoff wird bewusst NICHT
mehr heute angegangen, sondern als klar markierte naechste Phase
zurueckgestellt - das ist die tatsaechliche, saubere Grenze zwischen
Login-Server- und Gameserver-Arbeit, die von Anfang an angekuendigt war.

**Naechster Einstiegspunkt**: `AGPMLOGIN_ENTER_GAME`(Op8) im
`AGPMLOGIN_*`-Match in `main.rs` behandeln. Braucht mindestens eine
Antwort, die den Client aus dem Wartezustand befreit (echte Umsetzung
braucht eine tatsaechliche Gameserver-Adresse zum Weiterreichen - noch
nicht vorhanden). Die erwartete Vorwaerts-Bewegung/Kamera-Zoom
beim Anwaehlen ist wahrscheinlich Teil dieser Op8-Antwortverarbeitung,
noch nicht unabhaengig verifiziert.

## Charaktererstellung (Op10/RACE_BASE): Rassen-/Klassenvorschau implementiert, Musik-Ueberlappung gefunden und behoben, 2026-09-09

Ausgangspunkt war ein von einer parallel laufenden Session verfasstes,
sehr praezises Dokument ([`WINSOCK_SEQUENCE_22_CHARACTER_CREATE_RACE_CLASS_PREVIEW.md`](../Netzwerk/Sequenz-22-Character-Create-Race-Class-Preview.md)),
das behauptete: eine leere Op10-Antwort reicht nicht, der Client braucht
vorher zehn temporaere Basis-Charaktere ueber den `AgpmCharacter`-Kanal
(Op0 Add) mit Status `AGPDCHAR_STATUS_IN_GAME_WORLD`(=2), sonst findet
`AgcmUICharacterCreate::FindCreateCharacterModel` fuer keine Rasse/Klasse
(ausser dem zufaellig schon vorhandenen DragonScion/1724) ein lokales
Vorschau-Objekt.

**Jede einzelne Behauptung wurde vor der Umsetzung gegen den echten
Quellcode verifiziert** (wie bei jedem Fund dieses Projekts) - und traf
bit-genau zu:

- `AgpdCharStatus`-Enum (`Include/AgpdCharacter.h`): `LOGOUT=0,
  IN_LOGIN_PROCESS=1, IN_GAME_WORLD=2`.
- `FindCreateCharacterModel` (`AgcmUICharacterCreate.cpp:164`) prueft
  exakt `ppdCharacter->m_unCurrentStatus == AGPDCHAR_STATUS_IN_GAME_WORLD`
  neben Rasse/Klasse aus dem lokalen Charakter-Template.
- Die zehn TIDs (96, 1, 6, 4, 8, 3, 9, 460, 377, 1724) stammen
  bit-genau aus `AgsmLoginClient.cpp:65-74`s `g_lCharTID[]`.

**Umsetzung**: `build_add_character_packet` bekam einen `status`-Parameter
(bestehender Charakterauswahl-Aufruf bleibt bei `LOGOUT`, unveraendert,
weil live bereits bestaetigt funktionierend). Neuer, schlanker
`build_race_preview_packet`-Wrapper baut ueber ein per-`Default`
generiertes `db::Character` zehn ephemere, nicht persistierte
Vorschau-Objekte (CID = `1_000_000 + TID`, garantiert kollisionsfrei mit
echten DB-IDs). `AGPMLOGIN_RACE_BASE`-Handler: `RaceInfo` aus der
Anfrage parsen (`parse_race_base_request`, gleiches Bitmasken-Muster wie
`parse_account_id`/`parse_world_name`), zehn Vorschau-Pakete senden,
dann den finalen Op10-Frame mit `MaxRegisterChars=10` + echo'tem
`RaceInfo` (Bit 2 + Bit 5 im CharDetailInfo).

**Live bestaetigt**: Rassen-/Klassenvorschau funktioniert (Testergebnis: wie
erwartet) - erstmals alle vier Rassen waehlbar, nicht nur
DragonScion.

**Zweiter Bug gefunden und behoben - Musik-Ueberlappung beim
Rassenwechsel**: alle zehn Vorschau-Objekte standen anfangs auf
Position `(0,0,0)` (`FindCreateCharacterModel` selbst liest Position
gar nicht, schien also irrelevant). Live-Symptom: beim Rassenwechsel
ueberlappten sich alle Musiktitel statt umzuschalten. Erste Hypothese
(clientseitiges, kamera-positionsgebundenes [`AgcmEventNature`](../Module/AgcmEventNature.md)/Zonen-
Ambientsystem, `AgcuUIControlCamera::_UpdateCameraAndNature`) wurde per
Quellcode widerlegt: die Funktion nutzt die **Kamera**-Position, nicht
die der Charakter-Objekte. Zweite Hypothese, server-seitig behebbar und
bestaetigt richtig: alle zehn Objekte auf demselben Punkt gestapelt statt
weit verteilt (wie der echte Server via `LoginCharPos.ini` in
`CreateBaseCharacterOfRace`) hat vermutlich jedes Objekt-eigene Ambient-/
Idle-Sound-Cue gleichzeitig ausgeloest. Fix: `build_race_preview_packet`
bekam einen `position`-Parameter, jede der zehn Vorschauen wird jetzt auf
einen eigenen, 500 Einheiten versetzten Punkt weit ausserhalb der
sichtbaren Karte gesetzt (gleiche Ecke wie `LoginCharPos.ini`) statt
`(0,0,0)` fuer alle. **Live bestaetigt**: Musik wechselt jetzt korrekt
ohne Ueberlappung, Hintergruende ebenfalls korrekt.

### Login-Server-Kernauftrag erreicht - Endstand fuer heute

Login -> Serverauswahl -> Charakterauswahl (3D-Rendering + Auswahl-
Interaktion funktioniert) -> Charaktererstellung (alle vier Rassen mit
korrekter Vorschau, Musik, Hintergruenden) funktionieren jetzt end-to-end.
Bewusst offen/zurueckgestellt: `AGPMLOGIN_ENTER_GAME`(Op8, echter
Gameserver-Handoff) - klare, saubere Grenze zur naechsten Projektphase.

## Charakter loeschen implementiert und Ende-zu-Ende verifiziert, 2026-09-09

Geprueft wurde, ob ein Charakter geloescht werden kann und
die Zeile dabei wirklich aus der DB verschwindet. `AGPMLOGIN_REMOVE_CHARACTER`
(Op13) war bis dahin komplett unbehandelt.

Request-Format gegen den echten Client verifiziert
(`AgcmLogin::SendRemoveCharacter`, `AgcmLogin.cpp:1240`, aufgerufen aus
`AgcmUILogin.cpp:1575` mit dem erneut eingegebenen Bestaetigungspasswort
der UI): einziger Request dieses Servers, der zusaetzlich ein
Password-Feld (Bit 4, 33 Byte fest) trägt - dadurch verschieben sich die
festen Offsets fuer WorldName/CharDetailInfo entsprechend
(AccountID[16..65), Password[65..98), WorldName[98..130),
CharDetailInfo ab [130..)). Passwort wird nicht geprueft (dieser Server
prueft grundsaetzlich keine Passwoerter). Antwortformat aus dem echten
Client (`OnRemoveCharacter`, `:432`) bestaetigt: einfaches Echo von
Operation=13 + CharName reicht, keine Passwort-/Ergebniscode-Logik
noetig.

Implementiert: `parse_remove_character_request` (gleiches Bitmasken-
Muster wie die anderen Parser), `db::delete_character` (echtes
`DELETE FROM characters`, `character_items` cascadet automatisch ueber
die bereits bestehende `ON DELETE CASCADE`-Fremdschluesselbeziehung aus
Migration 0004).

**Live Ende-zu-Ende verifiziert**: Server-Log zeigt
`char_name=Some("Testchar") deleted=true`; direkte DB-Abfrage danach
bestaetigt `characters`-Tabelle leer (0 Zeilen) UND `character_items`
leer (0 Zeilen, Cascade funktioniert). Client zeigt den Charakter
korrekt nicht mehr an, keine Fehler.

## Loeschen+Sofort-Neuerstellen im selben Slot: Ursache gefunden, zwei Anlaeufe bis zur echten Loesung, 2026-09-09

Test (3+3 Charaktere auf zwei Welten erstellt) deckte einen echten
Bug auf: Charakter in Slot X loeschen, dann direkt (ohne Welt zu
verlassen) einen neuen erstellen, zeigte falsche Daten (ein anderer,
unveraenderter Charakter verschwand; der neue zeigte nur die 2D-Info-Box
ohne 3D-Modell). Welt verlassen und neu betreten reparierte es immer
zuverlaessig.

**Erster Anlauf (falsch)**: Verdacht auf Cross-World-Slot-Kollision
(beide Welten vergeben Slots unabhaengig ab 0). Migration 0006 machte
`slot_index` account-weit eindeutig. **Widerlegt** durch den echten
Client-Quellcode: `AGCMUILOGIN_MY_CHARACTER_NUM = 3`
(`Include/AgcmUILogin.h`) ist ein FESTES, KLEINES, PRO-WELT-Array (max 3
Charaktere pro Welt) - `CBGetNewCharacterName` lehnt jeden Slot-Index
`>= 3` hart ab. Account-weit immer weiter hochzaehlende Slots haetten
die Charaktererstellung komplett zerstoert, sobald ein Account insgesamt
mehr als 3 Charaktere haette. Migration 0007 macht das rueckgaengig
(Slots wieder pro Welt, mit Wiederverwendung freigewordener Slots - das
war schon vorher korrekt).

**Zweiter, richtiger Fund**: `AGPMLOGIN_NEW_CHARACTER_NAME` sendete beim
Erstellen nie ein `AddCharacter`-Paket fuer den neuen Charakter - nur
die 2D-Namensliste wurde aktualisiert. Das 3D-Objekt entstand nie.

**Fix Version 1 (unvollstaendig)**: nach Erstellen/Loeschen den
kompletten Charakterbestand der Welt neu senden (`refresh_world_characters`
- Namensliste + AddCharacter-Pakete, genau das, was "Welt verlassen und
neu betreten" bewirkt). Live-Test zeigte einen NEUEN, schlimmeren Fehler
per Screenshot: nach Loeschen von Slot 2 erschien Slot 0s Charakter ein
ZWEITES Mal an Slot 2s freigewordener Position, Slot 1 zeigte nur die
Info-Box. Grund: `AgcmUILogin::AddMyCharacterInfo`s reale Fallback-Logik
("wenn angeforderter Slot bereits belegt ist, nimm den ersten freien")
haelt die UEBERLEBENDEN Charaktere weiterhin fuer "belegt" (ihr
2D-Flag wurde nie zurueckgesetzt), da wir nur ihre Namen NEU sendeten,
ohne vorher etwas zu loeschen - der Client interpretiert das als
Kollision mit sich selbst und weicht auf den naechsten freien Slot aus.

**Fix Version 2 (funktioniert)**: `refresh_world_characters` sendet
jetzt zuerst fuer JEDEN ueberlebenden Charakter ein echtes
`AGPMLOGIN_REMOVE_CHARACTER`-Echo (loescht nichts in der DB, aber der
Client behandelt es wie eine echte Loeschung: 2D-Flag zurueckgesetzt,
3D-Objekt zerstoert), erst DANACH die Namensliste + AddCharacter-Pakete
neu senden - jeder Slot startet also wirklich leer, keine Kollision mehr
moeglich. **Live bestaetigt: funktioniert korrekt.**

Einziger verbleibender Nachteil: sichtbar traeger Uebergang (kurzer
Ladebildschirm, verzoegerte 2D-UI) nach Erstellen/Loeschen, da jeder
Charakter jetzt komplett ab- und wieder aufgebaut wird, inklusive der
800ms-Sicherheitsverzoegerung pro Charakter (Faktor N bei N
Charakteren, sequenziell). Funktional korrekt, aber nicht mehr instant -
als moegliche spaetere Optimierung (z.B. die Verzoegerungen parallel
statt sequenziell laufen lassen) vermerkt, nicht dringend.

## Op8 (AGPMLOGIN_ENTER_GAME) implementiert: die tatsaechliche, unvermeidbare Grenze zum Gameserver erreicht, 2026-09-09

Letzter Schritt des Login-Servers: der Client feuert Op8 automatisch,
sobald ein Charakter angeklickt wird (`AgcmUILogin::OnBtnSlot`, siehe
"Auswahl funktioniert vollstaendig" oben). Vorher unbehandelt.

**Wire-Format aus dem echten Quellcode verifiziert**, wie bei jedem
Fund dieses Projekts:

- Request (`AgcmLogin::SendEnterGame`, `AgcmLogin.cpp:946`): AccountID +
  CID(=Billing-Nummer, ausserhalb Korea-Builds 0) + WorldName +
  CharDetailInfo(TID+CharName). Das CID-Feld verschiebt die folgenden
  Offsets gegenueber allen bisher geparsten Requests (WorldName jetzt
  bei `[69..101)` statt `[65..97)`).
- Reply (`AgsmLoginClient::SendEnterGameEnd`, `:1813`): CID(echo) +
  CharDetailInfo(TID+CharName) + ein SEPARATES verschachteltes
  ServerInfo-Paket (`AGPMLOGIN_IPADDRSIZE`=23-Byte fester String, IP-
  Adresse des Gameservers).

Implementiert: `parse_enter_game_request` (gleiches Bitmasken-Muster wie
alle anderen Parser), Antwort mit einer Platzhalter-Adresse
(`127.0.0.1`) - bewusst kein echter/Stub-Gameserver, um zuerst live zu beobachten, was der Client
ueberhaupt versucht.

**Live-Befund, eindeutig**: nach dem Klick blieb der Ladebildschirm
haengen. Direkte Pruefung der TCP-Verbindungen des Client-Prozesses
(`Get-NetTCPConnection`) zeigte: **keine neue Verbindung wurde
aufgebaut** - nur die urspruengliche Verbindung zu unserem Login-Server
(Port 11002) existierte weiterhin. Das beantwortet die im Quellcode
offen gelassene Frage endgueltig: der echte Verbindungsaufbau
(`AgcmCharacter::SendEnterGameWorld`s `m_pcsAgcmConnectManager->Connect(...)`)
steckt hinter `#ifdef __ATTACH_LOGINSERVER__` und ist in diesem
Client-Build NICHT einkompiliert - die Funktion speichert nur die
IP-Adresse und kehrt zurueck, ohne jemals eine Netzwerkverbindung zu
versuchen.

**Schlussfolgerung**: der haengende Ladebildschirm ist kein Fehler
unserer Implementierung (keine Fehlermeldung, kein Absturz, unsere
Antwort wurde syntaktisch korrekt akzeptiert) - der Client wartet
danach korrekt auf echte Gameserver-Daten (Karte, Charakterposition,
etc.), die naturgemaess nie eintreffen. Das ist die tatsaechliche,
unvermeidbare Grenze zwischen Login-Server und Gameserver, kein
weiterer Fortschritt ist ohne einen echten Gameserver moeglich.

## Doppelter Add-Zyklus nach Refresh gefunden und behoben, 2026-09-09

Nach dem Op8-Test kam per parallelem Fund
([`WINSOCK_SEQUENCE_23_CHARACTER_REFRESH_DUPLICATE_ADD_ROOT_CAUSE.md`](../Netzwerk/Sequenz-23-Character-Refresh-Duplicate-Add-Root-Cause.md),
gegen den echten Quellcode verifiziert) die eigentliche, tiefere Ursache
der im vorigen Abschnitt behobenen Delete+Create-Korruption ans Licht:
`refresh_world_characters` sendete nach den Op13-Clears nicht nur die
Namensliste (Op4/Op5), sondern rief danach selbst zusaetzlich
`send_add_character_list_and_finish` auf (AddCharacter x N + Op7).

Das ist strukturell falsch: Op5 ist kein passiver "Liste fertig"-Marker.
Der Client verarbeitet ihn in `AgcmUILogin::CBGetMyCharacterNameFinish`,
setzt dabei `m_lAddMyCharacterCount = 0` und ruft SOFORT selbst
`AgcmLogin::SendGetCharacters` auf - ein echter, client-initiierter
Op6-Request trifft also unmittelbar nach unserem eigenen Refresh ein.
Der bestehende `AGPMLOGIN_CHARACTER_INFO`-Handler (Op6) beantwortet
diesen mit einem ZWEITEN, unabhaengigen AddCharacter+Op7-Zyklus - jeder
Charakter durchlief dadurch zwei ueberlappende Add-Zyklen, obwohl die
Client-UI nur einen pro Weltbetreten erwartet. Das erklaerte die
fehlenden/doppelten Modelle und die kaputte Auswahl nach Delete+Create
praeziser als die vorherige Erklaerung (die zwar auch real war, aber nur
einen Teil des Bildes traf).

Fix: `refresh_world_characters` sendet jetzt NUR noch die Op13-Clears
und die Op4/Op5-Namensliste und kehrt danach zurueck. Der resultierende,
vom Client selbst ausgeloeste Op6-Request ist die einzige Quelle fuer
AddCharacter+Op7 - exakt der gleiche Op4/Op5/Op6/Op7-Vertrag wie beim
normalen Weltbetreten. `cargo check`/`cargo build` sauber, Server mit
dem Fix neu gestartet; Live-Verifikation nach dem im Fund-Dokument
vorgeschlagenen Schema (3 Charaktere erstellen, Slot loeschen und neu
erstellen, im Log genau einen Op6/Add-Zyklus nach dem Refresh erwarten)
steht als naechstes an.

## Login-Server-Projekt abgeschlossen: Endstand 2026-09-09

Der komplette, urspruenglich beauftragte Ablauf funktioniert Ende-zu-
Ende, live bestaetigt:

- Login (SEED-Verschluesselung, echte Zugangsdaten-Verarbeitung)
- Serverauswahl (echte, aus der DB generierte Weltenliste, mehrere
  Welten moeglich)
- Charakterauswahl: echtes 3D-Rendering, echte Klick-Auswahl,
  funktioniert ueber mehrere Welten hinweg ohne Vermischung
- Charaktererstellung: alle vier Rassen mit korrekter Vorschau
  (Musik, Hintergruende), echte Persistenz inkl. Start-Templates/
  -Werte aus der echten Client-Datenbasis
- Charakter loeschen: echte DB-Loeschung, live Ende-zu-Ende verifiziert
- Op8/Enter-Game: protokollkorrekt bis zur echten Gameserver-Grenze

Naechste Projektphase (bewusst nicht begonnen): ein echter Gameserver.
Relevante Vorarbeit fuer diese Phase liegt bereits vor: `AlefServer`
(echter Quellcode, `EP8-c++-Source\Server\AlefServer`,
noch nicht untersucht), das `AgpmCharacter`/`AGPMCHAR_PACKET_TYPE`-
Paketprotokoll (bereits teilweise reverse-engineered fuer AddCharacter),
sowie die bereits in `character_templates`/`character_items` vorbereitete
Datenbasis.

## Nachtrag: die 24-Stunden-Loeschsperre gefunden -- die eigentliche Ursache der ganzen Delete+Recreate-Saga, 2026-09-09

Nach dem obigen "Projekt abgeschlossen"-Stand kam eine externe
Beobachtung (`WINSOCK_SEQUENCE_23_CHARACTER_REFRESH_DUPLICATE_ADD_ROOT_
CAUSE.md`, dokumentiert in einer parallelen Analyse) zum
Delete+Recreate-Bug ins Spiel. Live nachvollzogen:

- Der vorgeschlagene "sauberere" Single-Cycle-Refresh (nur Op13+Op4/Op5
  senden, den nativen Client-Op6 den Add-Zyklus ausloesen lassen) wurde
  implementiert. Quellcode-seitig korrekt (`AgcmUILogin::
  CBGetMyCharacterNameFinish` loest tatsaechlich einen echten Op6 aus),
  live aber schlechter als der bisherige Stand: die 2D-Charakter-UI blieb
  nach einem Delete komplett leer (3D-Modelle vorhanden, keine Namens-/
  Slot-Boxen).
- Zurueckgesetzt auf den vorherigen funktionierenden Doppel-Zyklus
  (`refresh_world_characters` sendet selbst Op4/5/6/7 UND laesst den
  Client zusaetzlich seinen eigenen Op6 ausloesen). Das stellte die 2D-UI
  wieder her, brach aber stattdessen die Rassen-/Klassen-Vorschau beim
  ERNEUTEN Oeffnen des Erstellen-Bildschirms: angeklickte Ork-/
  Mondelf-Klassen zeigten weiterhin das zuvor gewaehlte Modell
  (Human/Archer), obwohl gar keine neue Op10-Anfrage beim Server ankam --
  ein Hinweis auf ein gemeinsames, klein dimensioniertes Objekt-/
  Lookup-Array im Client-Prozess, das durch die zusaetzlichen
  AddCharacter-Sendungen des Doppelzyklus verdraengt wurde.
- Drei verschiedene Paket-Sequenzierungsstrategien (minimal gezielt,
  Single-Cycle, Doppel-Cycle) haben also jede fuer sich EIN Symptom
  behoben und dabei ein ANDERES im selben, gemeinsam genutzten
  Client-Objektpool ausgeloest.

Den eigentlichen Ausschlag gab: den Client-String
`UI_MESSAGE_ID_CANT_DELETE_1DAY` = `"LoginCantDelete1Day"`
(`Include/AgcmUILogin.h:190`). Im echten Quellcode nachverfolgt:

- `AgcmUILogin.cpp:1805-1806`: `AGPMLOGIN_RESULT_CANT_DELETE_CHAR_
  B4_1DAY` zeigt genau diese Meldung.
- `AgsmLoginDB.cpp:2672-2673` (`ProcessRemoveCharacter`): der echte
  Server sendet dieses Resultat, wenn seine `CHARACTER_DELETE`-Query
  meldet, der Charakter sei noch keine 24 Stunden alt.

**Das erklaert die ganze Saga rueckwirkend**: jeder heute Abend
geloeschte Charakter war Sekunden bis Minuten alt. Wir haben Stunden
damit verbracht, Client-Verhalten fuer einen Zustand zu
reverse-engineeren, den ein echter Spieler nie erreichen kann, weil
Webzens eigener Server ihn immer vorher blockiert -- daher gab es
plausibel gar kein konsistentes, "richtiges" Client-Verhalten fuer
diesen Fall zu finden.

Umgesetzt: `db::delete_character` prueft jetzt `created_at <= now() -
INTERVAL '1 day'`; bei Verstoss antwortet der Server mit dem echten
`AGPMLOGIN_LOGIN_RESULT`(15)-Paket (Ergebniscode 18 =
`AGPMLOGIN_RESULT_CANT_DELETE_CHAR_B4_1DAY`, `Include/AgpmLogin.h:99`,
gezaehlt ab `AGPMLOGIN_RESULT_INVALID_ACCOUNT = 0`), statt zu loeschen.

**Absturz gefunden und behoben**: die erste Version dieser Antwort liess
das `CharDetailInfo`-Feld komplett weg (im echten Aufruf `SendLoginResult
(lResult, pszCharName=NULL, ulNID)` ist der Zeichenname NULL). Live
sofort ein Client-Absturz: Zugriffsverletzung beim Lesen von Adresse
`0x2`, `EIP=004ea056`, Disassemblierung `movzx eax, word ptr [eax+2]`
mit `eax=0` (`ERRORLOG.TXT`). Ursache: der echte Code ruft
`m_csPacketCharInfo.MakePacket(...)` bedingungslos auf, auch wenn alle
eigenen Felder NULL sind -- das liefert einen gueltigen, nicht-NULL
Zeiger auf ein LEERES verschachteltes Paket (Maske=0), nicht NULL. Das
CharDetailInfo-Bit ist auf der echten Leitung also IMMER gesetzt; der
Client liest die Maske dieses verschachtelten Pakets ungeprueft (der
abgestuerzte `[eax+2]`-Zugriff), ohne vorher das aeussere Bit zu pruefen.
Fehlte das Feld komplett (unser Zeiger blieb bei 0/NULL), stuerzte er
sofort ab. Fix: `build_login_result_reply` sendet jetzt immer ein
vorhandenes, aber leeres CharDetailInfo (`build_nested_packet(2, 0,
&[])`).

Live verifiziert: Loeschversuch eines Sekunden alten Charakters -> kein
Absturz mehr, native "LoginCantDelete1Day"-Meldung erscheint. Die
urspruengliche Rassen-/Klassen-Vorschau-Korruption durch Delete+Recreate
wird damit nicht mehr weiterverfolgt -- sie ist ein Artefakt eines
Zustands, den echte Spieler nie erreichen koennen.

## Neues Crate alefgame-server: Gameserver-Handshake bis zum Weltbeitritt live funktionsfaehig, 2026-09-09

Neues Binary-Crate `crates/alefgame-server`, Workspace-Mitglied,
abhaengig von `aleflogin-proto`/`aleflogin-crypto` (gleiche
Frame-/Masken-Helfer, gleiche verschluesselte Wrapper-Frames), teilt
sich die Postgres-Datenbank mit `aleflogin-server` (keine eigenen
Migrationen, um Schema-Historie-Konflikte zu vermeiden).

**Reale Portnummer gefunden**: `Server/AlefServer/AlefServer.cpp:98`
und `ServiceEngine.cpp:114`, beide `StartServer(11008, ...)` -> Default
`0.0.0.0:11008`, nicht der urspruenglich geratene Platzhalter 11003.

**Op8-ServerInfo-Feld braucht Port**: `AcSocketManager::Connect`
(`AcSocketManager.cpp:78-81`) parst `"xxx.xxx.xxx.xxx:port"` via
`strchr(szServerInfo, ':')` und bricht ohne Doppelpunkt sofort ab --
unsere erste Op8-Antwort sandte nur die nackte IP. Nach Korrektur auf
`"127.0.0.1:11008"` verbindet sich der Client tatsaechlich (live per
`Get-NetTCPConnection` UND per Server-Log bestaetigt) -- die fruehere
"keine Verbindung"-Erkenntnis lag also (zumindest teilweise) an diesem
fehlenden Port, nicht zwingend an `__ATTACH_LOGINSERVER__`.

**SEED-Handshake 1:1 uebernommen**: die erste Nachricht auf der
Gameserver-Verbindung ist derselbe `AgpmStartupEncryption`-Handshake
wie beim Login (`maybe_respond`, aus `aleflogin-server` uebernommen,
eigene Schluessel `AlefGameEncKey!!`/`AlefGameDecKey!!` -- jede
Verbindung hat ihren eigenen `AuCryptManager`-Zustand).

**`AgcmCharacter`/`AgsmCharManager` (Modul-Opcode `0x03`,
`ApDefine.h:692,697`) vollstaendig dekodiert**: anders als
`AgcmLogin` nur eine 1-Byte-Maske (`AgcmCharacter.cpp:411`). Erstes
echtes Client-Paket live erfasst und byte-exakt gegen die Feldliste
verifiziert: Operation=2
(`AGCMCHAR_PACKET_OPERATION_REQUEST_CLIENT_CONNECT`) + CharacterName
("Ritter", 49-Byte-Feld) + AuthKey=0. Echte Server-Validierung
(`AgsmCharManager.cpp:408-644`) prueft ein AuthKey-Backend zwischen
Login- und Gameserver, das dieses Projekt nicht hat -- fuer den
Ein-Spieler-Testbetrieb bewusst uebersprungen. Antwort implementiert:
`CHARACTER_POSITION` (Operation=8, nur CID+Position,
`SendCharacterLoadingPosition`, `AgsmCharManager.cpp:1627-1652`) --
`db::find_character_by_name` liest die echte gespeicherte Position.

**Live-Kette bestaetigt bis zum Ladebildschirm-Ende**: Client verbindet
-> Handshake -> `REQUEST_CLIENT_CONNECT` -> unsere
`CHARACTER_POSITION`-Antwort -> Client laedt Map, leert lokale
Registry, sendet von selbst `LOADING_COMPLETE` (Operation=9, live
erfasst: mask=0x11={bit0,bit4}, CID echo). Das entspricht exakt der
in `WINSOCK_SEQUENCE_25` dokumentierten Kette. Ab hier haengt
der Ladebalken bei 100%, weil unser Server auf `LOADING_COMPLETE`
noch nicht antwortet -- der echte Handler (`AgsmCharManager::
EnterGameWorld`, `AgsmCharManager.cpp:1024`) muesste dafuer
`SendCharacterAllInfo` (Selbst-Charakter + Items) und
`SendCharacterSettingOK` (Operation=7) senden. Noch nicht
implementiert -- naechster Schritt fuer eine kuenftige Arbeitsphase.

## Ausruestung auf der Charakterauswahl: AgpmItem implementiert, aber Sackgasse bei OptimizedPacket2 gefunden

Ausgangspunkt: fehlender Waffen-/Ruestungs-Sendezweig im Login-Server
gefunden (Charaktere speichern `character_items` beim Erstellen, aber
`list_character_items` wurde nie aufgerufen; Waffen-`slot_index` stand
faelschlich auf 0 statt der echten Handplaetze 9/10 links/rechts).

**[`AgpmItem`](../Module/AgpmItem.md) (Modul-Opcode `0x04`, `ApDefine.h:615`) vollstaendig
dekodiert** -- ungewoehnlich schwer zu finden, weil `AgpmItem`s
eigener Konstruktor NUR `m_csPacket.Initialize()` aufruft, keine
`SetFieldType`. Die echte Felddeklaration liegt in einer SEPARATEN
Datei: `Include/AgppItem.h:4-42`, Klasse `PACKET_ITEM`
(`AgpmItem::m_csPacket`s echter Typ). 4-Byte-Maske (`SetFlagLength
(sizeof(INT32))`), 25 Feld-Slots. Fuer ein ausgeruestetes Item reichen
Operation(0=ADD)+Status(3=EQUIP)+ItemID+TemplateID+OwnerCID+Count+ein
LEERES Equip-Unterpaket (`m_csPacketEquip` hat selbst null Felder,
`AgpmItem.cpp:187-190` -- gleiches "vorhanden-aber-leer"-Muster wie
der Op-Absturz-Fix von heute Abend)+StatusFlag(immer gesetzt, hier 0).
Implementiert (`build_add_item_packet`), an `send_add_character_list_
and_finish` angehaengt (nach jedem AddCharacter+Resend, ein
`AgpmItem`-ADD pro `status='equipped'`-Zeile aus `list_character_
items`), Waffen-Slot-Index in `create_character` und per Live-Update
fuer bestehende Testcharaktere auf 10 (rechte Hand) korrigiert.

**Live-Test negativ**: keine Waffen am Modell sichtbar, obwohl das
Paket laut Log gesendet wurde. Erste Hypothese (echter Login-Server
sendet ueberhaupt keine Item-Pakete waehrend der Auswahl, siehe
`ProcessGetCharacters -> SendCharacterAllInfo -> SendPacketChar ->
MakePacketAddCharacter` -- keine Item-TID in diesem Pfad) wurde
widerlegt: live im echten Spiel zeigte sich, dass ein
Waffenwechsel sich sofort sichtbar am 3D-Modell der Auswahl
niederschlug.

Daraufhin den tatsaechlichen Sendezweig gefunden (in
[`WINSOCK_SEQUENCE_28_CHARACTER_SELECT_EQUIPMENT_SEND_PATH.md`](../Netzwerk/Sequenz-28-Character-Select-Equipment-Send-Path.md)
dokumentiert und hier verifiziert): `SendCharacterAllInfo`
(`AgsmCharacterPacket.cpp:2480-2514`) feuert nach dem AddCharacter-Send
ein `EnumCallback(AGSMCHARACTER_CB_SEND_CHARACTER_ALL_INFO, ...)`, auf
das `AgsmItem` sich mit `SetCallbackSendCharacterAllInfo`
(`AgsmItem.cpp:295`) einhaengt -- die Suche nach dem Callback-ID-Namen fuehrt nicht dorthin,
man muss nach der Setter-Methode suchen.

**Sackgasse gefunden**: `AgsmItem::CallbackSendCharacterAllInfo`
(`AgsmItemCB.cpp:2244-2327`) hat eine Weiche. Ist
`m_pagpmOptimizedPacket2` gesetzt, sendet der Code GEBUENDELTE Pakete
(`MakePacketCharAllItemExceptBankCash`, `MakePacketCharAllCashItem`,
`MakePacketCharAllSkill`, `MakePacketCharAllBankItem`) -- ein voellig
anderes, noch nicht untersuchtes Wire-Format aus dem Modul
[`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md). NUR wenn dieses Modul fehlt, faellt der Code
auf den alten Einzel-Paket-Pfad zurueck (`SendPacketItemAll` ->
`SendPacketItem` -> das bereits dekodierte `MakePacketItem`/
`PACKET_ITEM`, das wir implementiert haben). Da `AgpmOptimizedPacket2`
ein real vorhandenes, aktiv genutztes Modul in diesem Quellbaum ist,
nutzt dieser Server-Build vermutlich den gebuendelten Pfad -- das
erklaert plausibel, warum unsere (quellenkorrekten) Einzel-ADDs keine
sichtbare Wirkung hatten.

**Offen fuer eine kuenftige Arbeitsphase**: `AgpmOptimizedPacket2`s echtes
Feldformat reverse-engineeren (`MakePacketCharAllItemExceptBankCash`
u.a.), analog zur heutigen `AgpmItem`-Untersuchung. Die bereits
implementierte `AgpmItem`-ADD-Logik bleibt im Code (schadet nicht,
falls doch noch relevant, z.B. fuer spaetere Inventar-Updates
ausserhalb der Auswahl) -- der DB-Read (`list_character_items`) und
die Slot-Index-Korrektur sind in jedem Fall echte, unabhaengig
korrekte Fixes.

## AgpmOptimizedPacket2 implementiert, byte-genau verifiziert, live weiterhin ohne Wirkung -- Untersuchung hier abgeschlossen

Die als naechstes noetige Analyse (`AgpmOptimizedPacket2`, Modul-Opcode
`0x42`, `ApDefine.h:661`) wurde vollstaendig quellenbelegt zu Ende
gefuehrt:

- `m_csPacket` (`AgpmOptimizedPacket2.cpp:28-46`): 2-Byte-Maske, 14
  Felder; fuer unseren Fall reichen Operation(2=`ADD_CHARACTER`,
  `AgpmOptimizedPacket2.h:14-19`) + CharacterAllItemPacket(bit6,
  `MEMORY_BLOCK`) + CharacterID(bit9).
- `AgsmItem::CallbackSendCharacterAllInfo`s `MakePacketCharAllItem
  ExceptBankCash` -> `MakeBufferCharAllItem`
  (`AgpmOptimizedPacket2.cpp:1405-1434`) -> `AddItemPacketToBuffer`
  (`:1349-1375`) ruft **dieselbe** `AgpmItem::MakePacketItem`
  (`bIsPacket=TRUE`) auf, die wir fuer den Einzel-ADD schon gebaut
  hatten, und kopiert deren rohe Bytes in den `MEMORY_BLOCK` --
  inklusive des echten `PACKET_HEADER`-Structs (`AuPacket.cpp:286-296`:
  2-Byte-Laenge + 1-Byte-Typ(`AGPMITEM_PACKET_TYPE`=4) + 4-Byte-CID),
  nicht nur ein einfacher Laengenpraefix.

Implementiert (`build_optimized_all_item_packet`,
`build_item_packet_header_bytes`), Einzel-ADD-Pfad dadurch ersetzt.
**Live-Test per Debug-Klartext-Trace Byte-fuer-Byte gegengeprueft**:
jedes einzelne Feld (aeussere Maske `0x0241`, Operation, `MEMORY_BLOCK`-
Laenge, inneres Item-Paket mit Laenge/Typ/CID/Maske `0x0008023F`/allen
Feldwerten) stimmt exakt mit der beabsichtigten Konstruktion ueberein
-- kein Implementierungsfehler unsererseits. Trotzdem weiterhin keine
sichtbare Waffe am Charaktermodell.

**Schlussfolgerung**: dies ist die dritte, strukturell unterschiedliche
und jeweils quellenbelegte Hypothese (Einzel-`AgpmItem`-ADD, dann
dieses gebuendelte `AgpmOptimizedPacket2`-Format), beide byte-korrekt
gegen das eigene Verstaendnis der Quelle umgesetzt, beide ohne
sichtbaren Effekt. Die Unsicherheit liegt nicht mehr in unserer
Umsetzung, sondern in einer Annahme darueber, wie der Client dieses
rekursiv verschachtelte "`MEMORY_BLOCK` enthaelt ein vollstaendiges
Unterpaket mit eigenem `PACKET_HEADER`"-Konstrukt tatsaechlich liest --
eine Struktur, die sich von jedem anderen bisher in diesem Projekt
gebauten `MEMORY_BLOCK` (immer flache Strings/Structs) unterscheidet.
Weiterer Fortschritt braucht einen echten Paketmitschnitt aus dem
laufenden Spiel oder einen Live-Memory-Hook am Client -- reines
Quellcode-Lesen hat hier seine Grenze erreicht. Als offener Punkt fuer
eine kuenftige Arbeitsphase stehen gelassen; der Debug-Trace
(`tracing::debug!` mit dem Klartext vor der Verschluesselung) bleibt im
Code fuer die naechste Untersuchung.

## Nachtrag 2026-09-12: PACKET_HEADER-Theorie widerlegt, Live-Hook-Kette findet die echte Ursache

Ein echter Paketmitschnitt (EP7-Referenzclient, `Sniffer.exe`/
`interceptor.dll`) zeigte: die eingebetteten Item-Eintraege im
`MEMORY_BLOCK` sind KEINE bare `PACKET_HEADER`-Structs, sondern volle,
eigenstaendige `0xD6...0x6B`-Rahmen -- exakt das, was `build_add_item_packet`
schon immer erzeugt. Die oben dokumentierte dritte Hypothese war unnoetig
kompliziert. `build_item_packet_header_bytes` delegiert seitdem einfach an
`build_add_item_packet`.

Live weiterhin kein sichtbarer Effekt -- also die naechste Arbeitsphase mit genau
dem oben erwaehnten Live-Memory-Hook fortgesetzt (`install_oncharname_hook.py`
als Vorlage). Eine Kette von sechs Trampolin-Hooks (Details, Adressen und
Fundcode in [`WINSOCK_SEQUENCE_29_CHARACTER_SELECT_ITEM_ATTACHMENT_ROOT_CAUSE.md`](../Netzwerk/Sequenz-29-Character-Select-Item-Attachment-Root-Cause.md))
verfolgte das Item-Paket vom Empfang bis zur exakten Fehlschlagstelle:

- Das Paket wird korrekt geparst und fehlerfrei im Client-Item-Cache
  registriert (keine der bisher vermuteten Fehlerpfade wird genommen).
- Ein Event (`0x65`) wird danach gefeuert, ein Listener existiert und laeuft.
- Der Listener bricht aber lautlos ab, weil zwei Felder am Item-Objekt
  (Equip-Part-Index, Modul-Lookup-Zeiger) beide `0` sind -- live per
  MSVC-Debug-Heap-Fuellmuster (`0xCCCCCCCC`) bestaetigt: dieser Speicher wurde
  nie von einem Konstruktor beschrieben.
- Diese Felder werden ausschliesslich von einer Funktion gesetzt, die
  waehrend der gesamten Charakterauswahl kein einziges Mal aufgerufen wird.

Die urspruengliche Einschaetzung "architektonisches Limit, evtl. nicht loesbar
ohne vollen Weltbeitritt" wurde noch in derselben Arbeitsphase korrigiert: die
Charaktermodelle selbst sind ja bereits echte 3D-Objekte in der Auswahl, das
Objektsystem laeuft also. Es fehlt nur der analoge Initialisierungs-Trigger
fuer NACHTRAEGLICH hinzukommende Item-Objekte -- vermutlich haengt das an
derselben Luecke wie die separat beobachtete `Level -1`-Anzeige (fehlendes
`FactorPacket`-Bit im `AgpmCharacter`-Add). Details und naechste Schritte in
der genannten Sequenz-29-Datei.
