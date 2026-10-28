# Warum `alefclient.exe` nur "ueber die offizielle Website" startet

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Start, Anmeldung und Login-Umgehung](Index.md)*

Stand: 2026-09-05

Ziel dieser Datei: den clientseitigen Start-Gate-Mechanismus dokumentieren, der `alefclient.exe`
daran hindert, ohne den (mittlerweile abgeschalteten) Webzen-Webseiten-Launcher zu starten -
inklusive des dabei gefundenen, eingebauten Bypasses. Alle Angaben aus statischer Analyse von
`alefclient.exe`; zusaetzlich wurden zwei historische Launcher-Programme
(`WebzenGameStarter-1029.exe`, `WebzenBrowserExt.exe`) grob gesichtet.

## Update: bestaetigt durch Praxistest + zweiter Bypass fuer GameGuard gefunden

Praxistest: Mit einer angelegten `NoExcuteAuth.arc` wird die Website-Token-Sperre
tatsaechlich uebersprungen. Danach blieb aber `nProtect GameGuard` haengen (versucht ein
Update zu pruefen, was ohne Webzen-Infrastruktur fehlschlaegt). Das ist ein **komplett
separater** Mechanismus mit eigenem Bypass - siehe Abschnitt "GameGuard-Integration" weiter
unten: die Datei **`NotCheckGameGuard.arc`** (ebenfalls nur Existenzpruefung, beliebiger
Inhalt) schaltet die komplette GameGuard-Anbindung auf einen Nichts-tun-Stub um.

## Kurzfazit

- Der Client validiert seine **Kommandozeile** beim Start. Sie muss die Zeichenfolge `2:`
  enthalten, gefolgt von `member_id|<Rest>`.
- Fehlt dieses Muster (z.B. weil der Client per Doppelklick direkt aus dem Explorer gestartet
  wird), zeigt der Client die Meldung
  *"The game client is loaded only through the official website."*
  und oeffnet `http://archlord.webzen.com` im Standardbrowser - **exakt der beobachtete
  beschriebene Effekt.**
- Der offizielle Ablauf war: Login auf `archlord.webzen.com` -> eine Browser-Extension/ein
  ActiveX-Starter (`WebzenGameStarter.exe`/`WebzenBrowserExt.exe`) empfaengt einen
  Session-Token von der Webseite und startet `alefclient.exe` mit genau diesem Token als
  Kommandozeilenparameter.
- **Es gibt einen eingebauten Bypass:** Existiert im Arbeitsverzeichnis eine Datei namens
  `NoExcuteAuth.arc` (beliebiger Inhalt, es wird nur auf Existenz geprueft), wird die gesamte
  Pruefung uebersprungen und der Client startet normal - mit Login ueber lokal gespeicherte
  `AutoLogin`-Konfiguration statt ueber den Website-Token.

## Der Ablauf im Detail

### Schritt 1: Initialisierung prueft die Kommandozeile

`FUN_00410490` (Teil der frühen Fenster-/App-Initialisierung, aufgerufen aus dem
`WinMain`-Umfeld):

```c
pCVar3 = GetCommandLineA();
FUN_00601b60(pCVar3);              // liefert/initialisiert das globale AgcGPAuth-Singleton
cVar1 = FUN_0064fb00(pCVar3);      // die eigentliche Pruefung
if (cVar1 == '\0') {
    piVar4 = FUN_00601b60();
    (**(code **)(*piVar4 + 4))();  // vtable-Slot 1 = FUN_0064fa30 = Fehlermeldung + Browser oeffnen
    return 0;                      // Initialisierung schlaegt fehl
}
return 1;
```

### Schritt 2: `FUN_00601b60` - das `AgcGPAuth`-Singleton

Lazy-Singleton (`FUN_00601b60`, Adresse `0x00601b60`), das ein Objekt konstruiert und dessen
Vtable-Zeiger zunaechst auf [`AgcAuth`](../Module/AgcAuth.md):vftable`, dann auf `AgcGPAuth::vftable` setzt (`AgcGPAuth`
erbt von `AgcAuth`; "GP" vermutlich fuer eine bestimmte Publisher-/Portalvariante). Waehrend der
Konstruktion wird `FUN_004f9f00()` aufgerufen - das ist derselbe CryptoAPI-Init-Wrapper, der
auch fuer die Datei-Entschluesselung genutzt wird (siehe
[DATA_DECRYPTION_PROGRESS.md](../Daten-und-Werkzeuge/Datenentschluesselung.md)).

`AgcGPAuth::vftable` (VA `0x008c9224`), per RTTI-Kette (siehe Methodik in
[WINSOCK_TRANSFORM_CIPHER_SUITE.md](../Netzwerk/Transform-Cipher.md)) verifiziert:

| Slot | Funktion | Bedeutung |
|---:|---|---|
| `+0x00` | `FUN_0073eff0` | Haupt-Validierung (Kommandozeile parsen) |
| `+0x04` | `FUN_0064fa30` | Fehlermeldung + `ShellExecuteA` auf `http://archlord.webzen.com` |
| `+0x08` | `FUN_007e2af0` | (nicht naeher untersucht) |
| `+0x0c` | `FUN_0073f330` | Destruktor-Support |
| `+0x10` | `FUN_0064fa80` | String-Vergleichshilfe (nutzt `FUN_004f9d80`, CryptoAPI) |
| `+0x14` | `FUN_00601b40` | Destruktor |

### Schritt 3: `FUN_0064fb00` - Bypass-Check + Dispatch

```c
undefined1 FUN_0064fb00(AgcGPAuth *this, char *cmdline) {
    if (FUN_004fa3d0("NoExcuteAuth.arc"))   // Bypass-Datei vorhanden?
        return 1;                            // -> IMMER erfolgreich, ueberspringt alles
    // ansonsten: this->vtable[0](cmdline_als_std_string)
    return this->IsValidLaunch(cmdline_or_empty_string);
}
```

`FUN_004fa3d0` ist an anderer Stelle im Client mehrfach als simpler "existiert diese Datei"-Test
genutzt (vgl. `FUN_0064fa70`, das denselben Aufruf fuer den zweiten, in `FUN_0073eff0`
sichtbaren Bypass-Punkt nutzt).

### Schritt 4: `FUN_0073eff0` (`AgcGPAuth::IsValidLaunch`) - das Token-Format

```c
undefined4 FUN_0073eff0(string *cmdline) {
    if (FUN_0064fa70())              // == NoExcuteAuth.arc vorhanden?
    {
        SetConfig("AutoLogin", ...); // lokale AutoLogin-Config nutzen statt Token
        return 1;
    }
    if (cmdline leer) return 0;

    pos = cmdline.find("2:");
    if (pos == npos) return 0;                    // FEHLSCHLAG: kein "2:" im Kommandozeilenstring
    cmdline = cmdline.substr(pos + 2);             // alles ab "2:" (exklusive) behalten

    pipePos = cmdline.find('|');
    if (pipePos == npos) return 0;                 // FEHLSCHLAG: kein "|" mehr vorhanden

    member_id = cmdline.substr(0, pipePos);        // Teil VOR "|"
    SetConfig("member_id", member_id);

    rest = cmdline.substr(pipePos + 1);            // Teil NACH "|" (vermutlich Session-Token)
    if (GetAdaptersInfo() fehlschlaegt) {
        MessageBoxA("Cannot read local MAC Address");
        return 0;                                   // FEHLSCHLAG
    }
    mac = erste Netzwerkkarten-MAC als "xx-xx-xx-xx-xx-xx";
    gamestring = rest + "|" + mac;                 // Token wird an lokale MAC gebunden!
    SetConfig("gamestring", gamestring);
    SetConfig("autologin", true);
    return 1;                                       // ERFOLG
}
```

**Erwartetes Kommandozeilenformat also (sinngemaess):**

```text
alefclient.exe ... 2:<member_id>|<session_token>
```

Bemerkenswert: der `session_token`-Teil wird lokal mit der **MAC-Adresse des ersten
Netzwerkadapters** verkettet (`<token>|<mac>`) und als `gamestring` gespeichert - das deutet
darauf hin, dass der eigentliche Login-Request (Sequenz 01, `FUN_0065d840`, siehe
[WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md](../Netzwerk/Sequenz-01-Login-Handshake.md)) diesen
kombinierten String an den Loginserver sendet, der Server also serverseitig pruefte, ob Token
und MAC-Adresse zusammenpassen (zusaetzliche Bindung an die Maschine, auf der der Website-Login
stattfand).

## Warum das den beobachteten Effekt exakt erklaert

Ohne den Website-Launcher fehlt der komplette `2:<member_id>|<token>`-Teil in der
Kommandozeile. `FUN_0073eff0` findet `"2:"` nicht (oder findet es zufaellig, aber dann kein
`"|"` danach), gibt `0` zurueck, `FUN_0064fb00` gibt `0` zurueck, `FUN_00410490` ruft daraufhin
den Fehlerpfad auf: **genau die beobachtete Meldung "The game client is loaded only
through the official website" plus das Oeffnen von `archlord.webzen.com`** (das heute ins
Leere laeuft, weil die Seite nicht mehr existiert - der `ShellExecuteA`-Aufruf selbst schlaegt
dabei nicht fehl, der Browser zeigt nur einen Fehler oder eine Parkingpage).

## Der Bypass: `NoExcuteAuth.arc`

Um den Client ohne Website/Token zu starten, reicht laut diesem Codepfad das Anlegen einer
leeren Datei `NoExcuteAuth.arc` im Arbeitsverzeichnis von `alefclient.exe` (`C:\Spiele\Archlord\`).
Effekt laut Code:

- Die gesamte Token-Pruefung wird uebersprungen.
- Der Login-Fluss nutzt stattdessen die lokale `AutoLogin`-Konfiguration (vermutlich Werte wie
  `member_id`/`autopwd`/`autologin` aus einer lokalen `.ini`, siehe bereits dokumentierten
  Bezug in [WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md](../Netzwerk/Sequenz-01-Login-Handshake.md),
  Abschnitt "Schritt 2").
- Das ist reine Client-Logik: der Login-**Server** braucht dafuer natuerlich trotzdem gueltige
  Zugangsdaten/eine erreichbare Serverinfrastruktur - dieser Bypass loest nur die
  Start-/Launcher-Sperre, nicht die (separate) Frage, ob ueberhaupt noch ein Loginserver
  antwortet.

**Nicht getestet** (dieses Projekt fuehrt die Datei nie aus, siehe [README.md](../Daten-und-Werkzeuge/Disassembly-2013.md)) -
das ist eine aus dem Kontrollfluss abgeleitete, aber nicht praktisch verifizierte Aussage.

## GameGuard-Integration (`nProtect GameGuard`) und ihr eigener Bypass

Voellig unabhaengig vom Website-Token-Mechanismus oben gibt es eine zweite Sperre: die
Anbindung an **nProtect GameGuard** (Ghidra-RTTI-Klassennamen `AuNPWrapper`, `AuNPBase`,
`AuNPGameLib` - "NP" = nProtect). Auch dafuer existiert ein dediziertes Bypass-Flag.

### Die Weiche: `FUN_004ee230` (`AuNPWrapper`-Konstruktor)

```c
undefined4 * FUN_004ee230(AuNPWrapper *this) {
    this->vtable = AuNPWrapper::vftable;
    if (!FUN_004fa3d0("NotCheckGameGuard.arc")) {
        // Bypass-Datei FEHLT -> echte GameGuard-Anbindung verwenden
        impl = new(8);
        impl->vtable = AuNPGameLib::vftable;
    } else {
        // Bypass-Datei VORHANDEN -> Nichts-tun-Stub verwenden
        impl = new(4);
        impl->vtable = AuNPBase::vftable;
    }
    this->impl = impl;
    this->initialized = impl->vtable[1]();   // ruft Init/Check-Methode auf
    return this;
}
```

`AuNPWrapper` ist, wie `AuCryptManager` und `AgcGPAuth`, ein Lazy-Singleton (Getter
`FUN_004ee570`, Adresse `0x004ee570`), wird also einmalig frueh im Programmstart konstruiert.

### `AuNPGameLib` (echt) vs. `AuNPBase` (Stub) - Vtable-Vergleich

Beide Vtables per RTTI verifiziert (`AuNPGameLib` VA `0x008b7880`, `AuNPBase` VA `0x008b7850`):

| Slot | `AuNPGameLib` (echt) | `AuNPBase` (Stub) |
|---:|---|---|
| `+0x04` ("Init/Check", wird in `FUN_004ee230` aufgerufen) | `FUN_004ee2e0` | `FUN_0057ebe0` |

`FUN_0057ebe0` (der Stub) ist:

```c
undefined4 FUN_0057ebe0(void) { return 1; }
```

**Das ist alles - der Stub tut buchstaeblich nichts und meldet sofort Erfolg.** Kein
Datei-Update-Check, keine Versionsabfrage, kein Laden einer GameGuard-DLL.

`FUN_004ee2e0` (die echte Implementierung, die bei fehlendem `NotCheckGameGuard.arc`
aufgerufen wird) ist genau der Update-Check, an dem der Start haengen bleibt:

```c
undefined4 FUN_004ee2e0(void) {
    // waehlt Dateinamen wie "ArchlordEnglishTest"/"ArchlordEnglish" je nach Sprachindex
    // und ob eine lokale *Test-Datei existiert
    handle = FUN_007ffc20(dateiname);          // vermutlich GameGuard-DLL/Modul initialisieren
    if (handle == 0) return 0;
    code = FUN_007ffbe0();                      // Ergebnis-/Fehlercode abfragen
    if (code == 0x755) return 1;                // 0x755 = Erfolg, alles andere = Fehler
    msg = handle->GetErrorString(code);         // Fehlertext vom GameGuard-Modul holen
    MessageBoxA(0, msg, "GameGuard Error", 0);  // <- genau diese Fehlerbox erscheint
    return 0;
}
```

Der Erfolgscode ist hartkodiert `0x755` (1877 dezimal). Jeder andere Rueckgabewert von
`FUN_007ffbe0()` (z.B. weil ein Update-/Versionsserver nicht erreichbar ist) fuehrt zur
"GameGuard Error"-Meldung.

### Fazit

**`NoExcuteAuth.arc` und `NotCheckGameGuard.arc` sind zwei unabhaengige Schalter fuer zwei
unabhaengige Systeme.** Wer nur die Website-Sperre umgehen will, aber GameGuard weiterhin
seinen (nicht mehr funktionierenden) Update-Check machen laesst, braucht zusaetzlich die
zweite Datei. Beide leer, im Arbeitsverzeichnis von `alefclient.exe`
(`C:\Spiele\Archlord\`), reiner Existenztest, Inhalt egal:

```text
C:\Spiele\Archlord\NoExcuteAuth.arc
C:\Spiele\Archlord\NotCheckGameGuard.arc
```

Auch hier gilt: nicht praktisch getestet in diesem Projekt (siehe [README.md](../Daten-und-Werkzeuge/Disassembly-2013.md)),
aus dem Kontrollfluss aber eindeutig abgeleitet - `FUN_0057ebe0` ist eine 1-Zeilen-Funktion
ohne jede Bedingung, an ihrer Wirkung gibt es keinen vernuenftigen Interpretationsspielraum.

## Update: echte Starter-DLLs installiert und ausgewertet

Beide Setups wurden tatsaechlich installiert. Damit standen die echten Programme
zur Verfuegung (statt nur der Installer-Huellen von vorhin):

- `WEBZEN\WebzenGameStarter\NPGameWebStarter.dll` (NPAPI-Browser-Plugin, registriert unter
  `SOFTWARE\MozillaPlugins\@Webzen.com/NPGameWebStarter`)
- `WEBZEN\BrowserExtension\NPWZCmnCtrl.dll` (zweites NPAPI-Plugin, registriert unter
  `SOFTWARE\MozillaPlugIns\@Webzen.com/NPBrowserExt\MimeTypes\application/x-WZBrowserExt`)

### `NPGameWebStarter.dll` - der eigentliche Website-Launcher

Aus den ASCII-Strings der DLL (kein Disassemblieren noetig, die Klartextnachrichten sind
eindeutig):

- **Von der Webseite aus per JavaScript aufrufbare Methoden** (NPAPI-Objekt-Methoden):
  `StartWebLauncher_SelectAuth`, `IsExecGameClient`, `GetModuleVersionINT`,
  `IsGameClientInstalled`. Die Webseite rief nach erfolgreichem Login also z.B.
  `plugin.StartWebLauncher_SelectAuth(<AuthCode>, ...)` per JavaScript auf.
- Debug-/Fehlermeldungen bestaetigen den Parametername: `"Not Currect AuthCode Value"` -
  die Webseite uebergibt einen **AuthCode**.
- Die DLL laedt dieselbe `StarterInfo.xml`/`StarterInfoTest.xml`, die auch lokal installiert
  ist (Format bestaetigt: `SELECT_GAME_TYPE`, `TYPE_%d`, `REG_ROOT_PATH`,
  `EXE_LAUNCHER_NAME`, `EXE_CLIENT_NAME` - exakt die oben gezeigten XML-Tags), liest daraus
  fuer das gewaehlte Spiel den Registry-Pfad (bei Archlord:
  `HKEY_LOCAL_MACHINE\SOFTWARE\WEBZEN\ArchLord`, Werte `file`/`folder`) und ermittelt so
  Installationsordner und Launcher-/Client-Dateinamen (`Archlord.exe` / `AlefClient.exe`).
- **Der eigentliche Start passiert nicht direkt auf `AlefClient.exe`**, sondern ueber eine
  dritte Datei: der String `\CMStarterCore.exe` taucht klar in der DLL auf, zusammen mit dem
  Format-String fuer die Kommandozeile, mit der sie per `ShellExecuteExA` (Verb `"open"`)
  gestartet wird:

  ```text
  %s|%s|%s|%s|%d|%d|%d|%d|%d
  ```

  (4 Strings + 5 Zahlen, Pipe-getrennt - vermutlich Spielename/-index, Installationspfad,
  AuthCode/Session-Info und diverse Flags aus der XML wie `GUID`/`WEB_ID`/`USED_WZLAUNCHER`).
  `CMStarterCore.exe` waere demnach dasjenige Programm, das daraus den finalen
  `2:<member_id>|<token>`-String baut und `Archlord.exe`/`AlefClient.exe` startet.

- **`CMStarterCore.exe` ist in KEINEM der beiden installierten Pakete enthalten** - weder im
  Installer-Bootstrapper (nur als Text-Referenz gefunden) noch im installierten Zielordner
  (`C:\Program Files (x86)\WEBZEN\` enthaelt nur die beiden `.dll`s, `StarterInfo*.xml` und
  `aa.ico`, kein `CMStarterCore.exe`).

### `NPWZCmnCtrl.dll` - Download-/Update-Infrastruktur, nicht der Launcher selbst

Diese zweite DLL ist entgegen der urspruenglichen Vermutung kein Teil der eigentlichen
Startlogik, sondern ein generischer **Plugin-Downloader/-Updater** (`WinHTTP`-basiert):
Strings wie `AvailablePlugIn`, `UpdatePlugIn`, `PlugInList`, `Fail to download Updater`
sowie eine Zertifikatspruefung heruntergeladener Module
(`Fail to find module's digital certificated. For safety, Delete(%s)`) zeigen: Diese DLL hat
zur Laufzeit **weitere Komponenten von einem Webzen-Server nachgeladen** - hoechstwahrscheinlich
inklusive `CMStarterCore.exe` selbst, das offenbar nicht Teil der statischen Installationspakete
war, sondern erst bei Bedarf heruntergeladen wurde. Das Manifest fordert zudem
`requireAdministrator` - lief also mit erhoehten Rechten (typisch fuer
ActiveX-Installer-Infrastruktur dieser Aera).

### Schlussfolgerung aus dieser Spur

`CMStarterCore.exe` ist damit vermutlich **nicht wiederherstellbar** ohne eine alte, separat
aufbewahrte Kopie - es wurde zur Laufzeit von der (nicht mehr existierenden)
Webzen-Serverinfrastruktur nachgeladen, nicht mit den Installern ausgeliefert. Fuer die
urspruengliche Fragestellung ist das aber irrelevant: Die beiden bereits gefundenen
Bypass-Dateien (`NoExcuteAuth.arc`, `NotCheckGameGuard.arc`) wirken direkt in
`alefclient.exe` selbst und machen die gesamte hier nachgezeichnete Kette
(Webseite -> `NPGameWebStarter.dll` -> `CMStarterCore.exe` -> `Archlord.exe`) ueberfluessig.

## Zu den bereitgestellten Installer-Bootstrappern (vor der Installation)

`WebzenGameStarter-1029.exe` und `WebzenBrowserExt.exe` wurden zunaechst nur als
Installer-Pakete gesichtet (ASCII-Strings plus ein Extraktionsversuch der eingebetteten
PE-Dateien), bevor sie tatsaechlich installiert wurden:

- Beide sind **Installer-Bootstrapper** (Strings verweisen auf `dotnetinstaller.exe`,
  `ISBEW64.exe` - ein InstallShield-MSI-Custom-Action-Helper -, `Disk1\setup.exe`), nicht die
  eigentlichen Launcher-Programme selbst.
- Es wurden je drei eingebettete PE-Dateien anhand gueltiger `MZ`+`PE`-Header extrahiert
  (grobes Carving zwischen aufeinanderfolgenden `MZ`-Signaturen, siehe
  `extract_gamestarter/`, `extract_browserext/`). **Ergebnis: Enttaeuschend fuer die
  eigentliche Fragestellung** - die extrahierten Bloecke enthalten nur
  Installer-Metadaten/Konfigurationsblöcke (`AppName=Webzen Game Starter`,
  `CompanyName=WEBZEN`), keinen ausfuehrbaren Programmcode mit `CreateProcess`-Aufruf auf
  `alefclient.exe` oder dem `2:<member_id>|<token>`-String.
- Schlussfolgerung: Diese Installer sind vermutlich mit einem proprietaeren Format (z.B.
  Setup Factory/InstallShield) gepackt, bei dem die eigentliche Nutzlast (das echte
  `WebzenGameStarter.exe`/`WebzenBrowserExt.exe`, moeglicherweise `CMStarterCore.exe`) in
  einem komprimierten, formatspezifischen Archivbereich liegt, der sich nicht durch simples
  `MZ`-Signatur-Carving sauber heraustrennen laesst. Eine korrekte Extraktion wuerde ein
  dediziertes Installer-Unpacking-Tool erfordern (z.B. Universal Extractor oder ein
  formatspezifischer Entpacker), nicht Standard-Reverse-Engineering-Technik. Fuer die
  eigentliche Fragestellung (warum startet `alefclient.exe` nicht) war das ohnehin nicht
  mehr noetig - die Antwort kam vollstaendig aus dem Client selbst.

## Offene Punkte

1. **Nicht extrahiert:** der eigentliche Launcher-Payload innerhalb der beiden Setup-Dateien
   (vermutlich `CMStarterCore.exe`), der den exakten Aufbau des `2:...|...`-Strings serverseitig
   zeigen wuerde (z.B. ob vor `2:` noch weitere Kommandozeilenteile stehen, oder ob es
   Anfuehrungszeichen/Escaping gibt).
2. **`FUN_0064fdf0`** (die Funktion, die `member_id`/`gamestring`/`autologin` als Config-Werte
   setzt) wurde nicht im Detail gelesen - moeglich, dass sie in eine In-Memory-Config oder direkt
   in eine Datei schreibt.
3. **Nicht verifiziert:** ob der Bypass (`NoExcuteAuth.arc`) tatsaechlich zu einem lauffaehigen
   Client fuehrt, da dafuer noch ein erreichbarer Loginserver noetig waere (nach Stand der Tests nicht
   mehr vorhanden) und weil dies bewusst nicht ausprobiert wurde (siehe [README.md](../Daten-und-Werkzeuge/Disassembly-2013.md)).
4. **`FUN_007e2af0`** (Vtable-Slot `+0x08` von `AgcAuth`/`AgcGPAuth`) nicht untersucht.
