# Winsock-Sequenz 29: Root Cause fuer die fehlende Waffenanzeige in der Charakterauswahl

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-12

## Kontext

Sequenz 27/28 (parallele Session) und die vorangegangene Arbeitsphase hatten das
[`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md)-Bündelpaket byte-genau gegen eine reale Paketaufzeichnung
(EP7-Referenzclient, `Sniffer.exe`/`interceptor.dll`) verifiziert. Trotzdem
blieb die Waffe am Charaktermodell in der Charakterauswahl unsichtbar, ebenso
die "Schritt-nach-vorn"-Animation beim Selektieren. Reines Quellcode-Lesen
hatte an dieser Stelle sein Limit erreicht (siehe [`FORCE_LOGIN_WORKAROUND.md`](../Start-und-Login/Login-Callback-Workaround.md),
Abschnitt "AgpmOptimizedPacket2 implementiert ... Untersuchung hier
abgeschlossen"). Diese Arbeitsphase hat das Problem stattdessen mit einer Kette
von Live-Speicher-Hooks (Trampolin-Injektion, gleiche Technik wie
`install_oncharname_hook.py`) direkt im laufenden `alefclient.exe` verfolgt,
Schritt fuer Schritt von "Paket kommt an" bis zur exakten Byte-Adresse, an der
die Anzeige scheitert.

## Methode

Sechs nacheinander aufgebaute Trampolin-Hooks, jeweils an einer echten,
live aus dem Prozess gelesenen Instruktionsgrenze installiert (nie anhand
von Adressen allein vertraut -- immer zuerst die tatsaechlichen Bytes am
Zielpunkt gelesen und gegen die erwarteten Bytes geprueft, bevor gepatcht
wurde):

1. [`AgpmItem`](../Module/AgpmItem.md):OnReceive` (`0x0053eb40`, per Debug-String
   `"AgpmItem::OnReceive() Error (30) !!!\n"` identifiziert) -- **feuerte nie**,
   auch nicht beim mehrfachen Durchklicken der Charakterauswahl.
2. `AgpmItem`s virtueller `OnReceive`-Slot (`0x00544620`, RTTI-Name
   "AgpmItem.virtual_36") -- **feuerte ebenfalls nie** direkt nach dem Login.
3. Der generische, tabellengetriebene Feld-Parser `fcn.004e9fb0` (gefiltert auf
   1. Argument `== 0x42`) -- **feuerte nie**.
4. Erst nach der Erkenntnis, dass das Bündelpaket nur **einmal beim Laden der
   Charakterliste** gesendet wird (nicht bei jedem Charakterklick, das ist
   reine Client-UI-Logik danach) und die Hooks vor diesem Zeitpunkt installiert
   sein muessen: Hook 2 erneut, diesmal **vor** dem Login installiert --
   feuerte sofort und zuverlaessig bei jedem Charakterlisten-Ladevorgang.

## Fund 1: Die Funktion bei `0x00544620` heisst in Wahrheit `AgpmCharacter::OnReceive`

Radare2 hatte diese Adresse per RTTI/Vtable-Analyse "AgpmItem.virtual_36"
genannt. Der im Ghidra-Pseudocode (`alefclient.pseudocode.c`, `FUN_00544620`)
erhaltene Debug-String beweist aber: `"AgpmCharacter::OnReceive() Error (19)
!!!\n"`. Der Microsoft-Linker hat identischen, byte-fuer-byte kompilierten
Code fuer mehrere `AuPacket`-Klassen COMDAT-gefaltet; radare2 kann bei so
gefaltetem Code nur EINE willkuerliche Klasse als Namensgeber zuordnen. Diese
eine physische Funktion dispatcht per `switch(Operation)` auf ganz
unterschiedliche echte Handler:

```c
switch (local_61 /* = Operation-Feld aus dem Paket */) {
  case 0:  /* ADD */    if (*mode != 0) uVar4 = FUN_00541f30(...);  break;
  case 3:  /* z.B. UPDATE */ uVar4 = FUN_0053eb40(...); break;  // <- unser erster Hook!
  ...
}
```

Unser erstes Item-ADD-Paket setzt `Operation = 0`. Das erklaert restlos, warum
`0x0053eb40` nie feuerte: diese Funktion ist nur fuer eine ANDERE Operation
(3) zustaendig, nicht fuer `ADD`. Der Debug-String
`"AgpmItem::OnReceive() Error (30)"` an dieser Adresse ist real, aber
irrefuehrend -- es ist nicht der einzige, geschweige denn der fuer uns
relevante Empfangspfad.

## Fund 2: Vor dem eigentlichen Dispatch steht ein Kontext-Filter -- der aber nicht greift

Ganz am Anfang von `FUN_00544620` (dessen sechster Parameter, ein
`int*` auf zwei Werte -- Modus-Flag und erwartete Charakter-ID):

```c
if ((*param_6 == 0) && (param_6[1] != 0) && (param_6[1] != local_c /* ItemOwnerCID */)) {
    return 0;  // stilles Verwerfen bei CID-Mismatch
}
```

Live gemessen: `mode=1`, `expected_cid=0`. Da `mode != 0`, greift die
Bedingung nicht -- unsere Pakete werden nicht durch diesen Filter verworfen.
Diese Hypothese (Charakter-Kontext-Mismatch waehrend der Mehrfach-Charakter-
Ladephase) ist damit widerlegt.

## Fund 3: Das Item wird korrekt im Client-Cache registriert -- keine Fehlerpfade

Der volle Aufruf-Pfad fuer `Operation == 0`:

```
FUN_00544620 (AgpmCharacter::OnReceive, COMDAT-gefaltet)
  -> case 0: FUN_00541f30           (der wahre "AgpmItem::OnReceive"-ADD-Handler,
                                      traegt ebenfalls "AgpmItem::OnReceive() Error (N)"-Strings)
       -> FUN_00541de0(...)         liefert SOFORT einen gueltigen Cache-Eintrag
                                     (live gemessen: 0x2468000c / 0x24680664 /
                                     0x24680cbc fuer drei verschiedene Charaktere
                                     -- alle drei != 0, "already exists" statt "neu")
       -> (das "neu anlegen"-Codepfad mit FUN_00540d80 wird deshalb NIE erreicht;
           unser fruehester Hook direkt hinter diesem Aufruf feuerte konsequent nie)
       -> Feldzuweisungen direkt auf den Cache-Eintrag (Owner-Verknuepfung etc.)
       -> FUN_0053aed0(iVar1)       Abschlussvalidierung, live gemessen: **liefert 1
                                     (Erfolg) bei allen drei Items** -- kein einziger
                                     Fehlerpfad ("Error (2)"/"Error (3)") wird genommen
```

Die komplette Paket-Verarbeitung -- Parsen, Cache-Lookup, Feldzuweisung,
Validierung -- laeuft **fehlerfrei durch**. Das Item existiert danach korrekt
im clientseitigen Item-Verwaltungssystem.

## Fund 4: Das Event `0x65` feuert, ein Listener existiert -- aber bricht intern lautlos ab

`FUN_00541f30` feuert nach erfolgreicher Verarbeitung
`FUN_004e4070(0x65, item, 0)`. `FUN_004e4070` ist der generische
"EnumCallback"-Dispatcher des Clients:

```c
uint FUN_004e4070(int this, uint eventId, undefined4 a, undefined4 b) {
    if (eventId > 0x81) return 0;
    for (node = *(this + 0x5dc + eventId*4); node != NULL; node = node->next)
        if (node->fn != NULL) result &= node->fn(a, node->userdata, b);
    return result;
}
```

Live gemessen: fuer Event `0x65` existiert genau EIN registrierter Listener
(Listenkopf `0x165a9950`, `next = NULL`). Der Callback selbst liegt bei
`0x006ed670` und macht (Ghidra-Pseudocode, per direkter Disassemblierung
nachvollzogen):

```c
undefined4 fcn_006ed670(int item /* echtes erstes cdecl-Argument */, int userdata) {
    if (item == 0) return 0;
    if (userdata == 0) return 0;
    ecx = *(short*)(item + 0xc9a);         // Equip-Part-Index
    ecx2 = *(int*)(item + 0xc5c);          // Lookup-/Modul-Zeiger ("this" fuer die naechste Suche)
    result = fcn_004e40e0(ecx2 /* this */, ecx /* part index */);
    if (result == 0) {
        // FEHLSCHLAG-PFAD: [item+0x54] = 0, Bereich [item+0x58..+0x90) genullt.
        // Keine sichtbare 3D-Anhaengung.
        return 1;
    }
    // ERFOLGS-PFAD: [item+0x54] = 1, 14 DWORDs echte Attachment-Daten
    // via rep movsd kopiert -- DAS waere die sichtbare Waffe.
}
```

Live gemessen fuer alle drei Test-Items: `[item+0xc9a] == 0`,
`[item+0xc5c] == 0x00000000` -- der Part-Lookup schlaegt fehl, der
Fehlschlag-Pfad wird genommen, **lautlos, ohne Fehlermeldung, ohne Absturz**.

## Fund 5: Diese beiden Felder werden ausschliesslich von einer Funktion gesetzt, die nie laeuft

Eine gezielte Suche im kompletten dekompilierten Bestand
(`alefclient.pseudocode.c`, ca. eine Million Zeilen) nach Schreibzugriffen auf
`+0xc9a` fand genau EINE Fundstelle im gesamten Client: `FUN_006effa0`. Diese
Funktion (Aufrufkonvention `__fastcall`, `this` in `ecx`, nirgends per
direktem `call` referenziert -- nur ueber einen Funktionszeiger/Vtable-Slot
erreichbar) initialisiert einen groesseren Objektbereich:

```c
*(this + 0xc58) = FUN_004e42c0("AgpmFactors");
*(this + 0xc5c) = FUN_004e42c0("AgpmItem");      // <- genau das Feld aus Fund 4
*(this + 0xc6c) = FUN_004e42c0("AgpmCharacter");
... (noch gut ein Dutzend weiterer Modul-Zeiger per Namenssuche) ...
if (*(this + 0x1058) != 0 /* AgcmResourceLoader vorhanden */) {
    sVar1 = FUN_005876e0(this, 0x90, ...);
    *(short*)(this + 0xc9a) = sVar1;              // <- das andere Feld aus Fund 4
    ... registriert ca. 20 weitere Event-Callbacks, u.a. explizit fuer
        Adresse 0x006ed670 (unser Fund-4-Callback) selbst ...
}
```

Ein direkter Hook auf den Eintrittspunkt von `FUN_006effa0` (unconditional,
kein Filter) wurde waehrend eines kompletten Charakterauswahl-Ladezyklus
**kein einziges Mal ausgeloest**. Zur Bestaetigung wurde der volle
Feldbereich `[item+0xc54 .. +0xcb0)` eines betroffenen Items live ausgelesen:

```
+0xc54..+0xc90: fast durchgehend 0x00000000
+0xca0:         0xcccccccc   <- MSVC-Debug-Heap-Fuellmuster fuer "nie beschrieben"
+0xcac:         0xbbbbbbbb   <- ebenfalls ein Debug-Heap-Fuellmuster
```

Das ist der endgueltige Beweis: dieser Speicherbereich wurde seit der
Allokation nie durch einen Konstruktor beschrieben. `FUN_006effa0` ist genau
dieser fehlende Konstruktor/Initialisierer.

## Schlussfolgerung

Die vollstaendige Kausalkette, lueckenlos live bewiesen:

```
Server sendet AgpmOptimizedPacket2-Buendel (byte-korrekt)
  -> Client parst eingebettetes AgpmItem-ADD-Paket (fehlerfrei)
  -> Item wird im Cache registriert (fehlerfrei, Validierung liefert Erfolg)
  -> Event 0x65 wird gefeuert, Listener existiert und laeuft
  -> Listener braucht [item+0xc9a]/[item+0xc5c], die von FUN_006effa0 gesetzt werden
  -> FUN_006effa0 wird waehrend der Charakterauswahl NIE aufgerufen
  -> Item bleibt ohne 3D-Anhaengungsdaten -- keine sichtbare Waffe
```

Dies ist kein Fehler in unserer Server-Implementierung mehr -- die ist
nachweislich byte- und ablaufkorrekt. **Wichtige Korrektur gegenueber einer
ersten, zu vorsichtigen Einschaetzung:** Die Charaktermodelle selbst werden in
der Auswahl nachweislich als echte 3D-Objekte dargestellt (das ist die ganze
Grundlage der Sequenz-18/20-Funde zu `RpClump`/3D-Init). Das zugrundeliegende
3D-Objektsystem laeuft also waehrend der Charakterauswahl bereits vollstaendig
-- es ist NICHT abgeschaltet. `FUN_006effa0` faehrt folglich kein "totes"
Subsystem hoch, sondern ist ein KONSTRUKTOR/INITIALISIERER, der fuer JEDES
einzelne anzuhaengende Objekt (Charakter, Item, ...) separat aufgerufen werden
muss, wenn dieses Objekt in die 3D-Szene eingefuehrt wird. Fuer den Charakter
selbst laeuft ein aequivalenter Initialisierungsschritt offensichtlich (das
Modell steht ja da) -- fuer unser Item-Objekt fehlt der analoge Aufruf.

Die eigentliche offene Frage ist damit praeziser: **welcher Trigger ruft
`FUN_006effa0` (oder sein Aequivalent) fuer ein Item auf, wenn ein
Charaktermodell bereits vorhanden ist und ein Item nachtraeglich als
ausgeruestet hinzukommt** -- und warum feuert dieser Trigger bei uns nicht.
Moegliche Ursachen, noch ungeklaert:
- Der Trigger haengt an einer Reihenfolge (z.B. muss das Item-ADD-Paket NACH
  einem bestimmten anderen Ereignis ankommen, das bei uns fehlt oder falsch
  sortiert ist).
- Der Trigger haengt an einem Feld/Flag im Item- oder Charakterpaket, das wir
  nicht setzen (z.B. genau das schon separat diagnostizierte fehlende
  `FactorPacket`-Bit im [`AgpmCharacter`](../Module/AgpmCharacter.md)-Add -- moeglich, dass Level/XP UND
  die Ausruestungs-Initialisierung an denselben, bislang unvollstaendigen
  Charakter-Add-Zyklus gekoppelt sind).
- Es gibt einen separaten, expliziten "Item am Charakter anhaengen"-Aufruf
  (durch die Charakterauswahl-UI oder durch `AgsmCharacter`/`AgcmCharacter`
  ausgeloest), den der reale Server zusaetzlich zum reinen Item-ADD sendet
  und den wir noch nicht kennen.

Damit haengen die beiden beobachteten Symptome -- fehlende Waffe
UND `Level -1` in der Infobox -- wahrscheinlich an derselben Wurzel: das vom
Loginserver gesendete `AgpmCharacter`-Add-Paket ist nicht vollstaendig genug,
um den Client in den Zustand zu versetzen, in dem er sowohl reale
Charakterwerte anzeigt als auch nachfolgende Item-ADDs korrekt an das 3D-Modell
bindet. Auch die fehlende "Schritt-nach-vorn"-Animation beim Selektieren passt
in dieses Bild. Das ist kein architektonisches Limit, sondern eine konkrete,
auffindbare Luecke in dem, was der Loginserver beim Charakter-Add sendet.

## Offene naechste Schritte

1. ~~Das bereits separat diagnostizierte fehlende `FactorPacket`-Bit im
   `AgpmCharacter`-Add implementieren und pruefen, ob das die
   Item-Anhaengung mit ausloest~~ -- **erledigt und live getestet, siehe
   Nachtrag unten: behebt "Level -1", aber NICHT die Waffenanzeige. Beide
   Symptome haben also unterschiedliche Ursachen.**
2. Herausfinden, WER `FUN_006effa0` fuer ein sichtbares Objekt aufruft --
   ein Hardware-Breakpoint (Debug-Register, nicht die bisherige
   Software-Trampolin-Technik) auf Schreibzugriffe von `[+0xc9a]` waere
   hier der direkteste Weg, da die statische Suche nach Aufrufern (direkter
   Call, Datenreferenz) ergebnislos blieb -- der Aufruf ist rein indirekt
   (Funktionszeiger/Vtable).
3. EP8-Referenzquelle gezielt nach dem Aufrufer-Aequivalent von
   `FUN_006effa0` bzw. nach einer expliziten "Item am Charaktermodell
   anhaengen"-Funktion durchsuchen (z.B. in `AgcmCharacter`/[`AgcmItem`](../Module/AgcmItem.md)
   client-seitig) -- gezielte Quellensuche statt weiteres Live-Hooking, jetzt
   wo der genaue Mechanismus (Event `0x65`, die zwei Felder, der fehlende
   Konstruktor) bekannt ist.
4. Die "Schritt-nach-vorn"-Animation separat untersuchen -- ungeklaert, ob sie
   an derselben Ursache haengt oder eine eigene hat.

## Nachtrag 2026-09-12 (Fortsetzung): FactorPacket implementiert, Charakter/Item-Trennung bewiesen

Das fehlende `FactorPacket`-Bit (siehe "Offene naechste Schritte" oben) wurde
implementiert (`build_factor_packet` in `main.rs`, siehe Commit
`f04a4a6`): ein doppelt verschachteltes [`AgpmFactors`](../Module/AgpmFactors.md)-Envelope
(Result -> CharStatus/CharPoint/CharPointMax) mit echten, bereits in der DB
vorhandenen Werten (`level`, `hp`, seit Charaktererstellung aus
`character_templates` gesetzt, aber nie gesendet). **Live verifiziert:
die Charakterauswahl zeigt jetzt das korrekte Level statt `-1`.** Die Waffe
bleibt weiterhin unsichtbar -- die beiden Symptome haben also
unterschiedliche Ursachen, keine gemeinsame Wurzel wie zunaechst vermutet.

Um die eingangs (siehe Abschnitt "Schlussfolgerung") aufgeworfene Frage --
"faehrt die Charakterauswahl denselben Objekt-Lebenszyklus wie fuer Items
noetig hoch, weil die Charaktermodelle ja schon in 3D gerendert werden?" --
direkt zu pruefen, wurden dieselben zwei Hooks (Modul-Dispatch bei
`0x00544620`, Cache-Lookup bei `0x00541f7a`) erneut installiert, diesmal
OHNE Filter auf Modul-ID 4 (Item), um auch `AgpmCharacter`s eigenes ADD
(Modul-ID 2) einzufangen, das ueber denselben COMDAT-gefalteten Code laufen
MUESSTE, wenn beide Klassen wirklich denselben Mechanismus teilen.

**Ergebnis: ueber einen kompletten Login-bis-Charakterauswahl-Zyklus kam
ausschliesslich Modul-ID 4 (Item) durch diesen Pfad -- kein einziger
Modul-ID-2-Treffer (Charakter).** Das beweist: `AgpmCharacter`s ADD-Handling
ist NICHT mit `AgpmItem`s ADD-Handling COMDAT-gefaltet -- es laeuft ueber
eine andere, bislang nicht lokalisierte Funktion. Der Debug-String
`"AgpmCharacter::OnReceive() Error (19)"` in `0x00544620` war demnach ein
zufaelliger Namens-Treffer der Linker-Codefaltung (mehrere Klassen mit
strukturell identischem, aber nicht demselben, Code werden separat
gefaltet), keine Bestaetigung, dass beide Klassen tatsaechlich denselben
Mechanismus benutzen.

**Praezisierte Einschaetzung:** Charakter und Item durchlaufen im Client
nachweislich getrennte Verarbeitungspfade. `FUN_006effa0` (Konstruktor fuer
das ~15-Modul-Zeiger-plus-~20-Event-Callback-Objekt aus Fund 5) sieht nach
der Initialisierung fuer eine VOLLWERTIGE NETZWERK-Objektrepraesentation
aus (wie sie fuer andere Spieler/NPCs/Monster noetig waere), waehrend die
Charakterauswahl fuer den eigenen Vorschau-Charakter einen separaten,
leichteren rein lokalen Renderpfad nutzt (passend zur bereits in Sequenz 20
belegten `InitCharacter -> LoadCharacterData -> RpClumpClone`-Kette). Das
ist kein Widerspruch zur Beobachtung "die Charaktermodelle sind ja in 3D
sichtbar" -- es zeigt nur, dass diese Sichtbarkeit einen ANDEREN,
Item-unabhaengigen Mechanismus nutzt. Items scheinen strukturell auf das
schwerere Netzwerk-Objekt-System angewiesen zu sein, das in der
Charakterauswahl nicht aktiv ist.

Die statische Suche nach `FUN_006effa0`s Aufrufer (direkter Call-Xref,
Datenreferenz in `.rdata`/`.data`) blieb ergebnislos -- der Aufruf ist rein
indirekt (Funktionszeiger/Vtable-Slot, zur Laufzeit aufgeloest). Naechster
Schritt: Hardware-Breakpoints (Debug-Register `Dr0`-`Dr3` via
`SetThreadContext`, nicht die bisherige Software-Trampolin-Technik) auf
Schreibzugriffe von `[+0xc9a]`, um den tatsaechlichen Aufrufer zur Laufzeit
zu fangen, unabhaengig davon, ob er direkt, indirekt oder vtable-basiert
aufruft.

## Technische Hinweise zur Methode (fuer kuenftige Live-Hook-Arbeitsphasen)

- **Der Charakterauswahl-Ladevorgang passiert nur einmal**, beim ersten Aufbau
  der Charakterliste nach dem Login -- nicht bei jedem Klick auf einen
  Charakter (das ist reine Client-UI-Navigation ueber bereits vorhandene
  Daten). Hooks muessen laufen, BEVOR man sich einloggt, sonst verpassen sie
  den einzigen relevanten Moment. Ein einfaches Aus- und wieder Einloggen
  reicht, um den Ladevorgang erneut auszuloesen.
- **Relative Spruenge (`jne`/`jnz`, auch `jmp`) duerfen nie unveraendert aus
  dem Original in ein Trampolin kopiert werden** -- ihr Sprungziel ist relativ
  zur eigenen Adresse, und diese aendert sich beim Verschieben in eine neue
  Speicherallokation. Das hat in dieser Arbeitsphase real einen Absturz verursacht
  (Absturzadresse lag exakt im betroffenen Trampolin). Fix: den echten
  absoluten Zielwert aus dem Original-Offset berechnen und im Trampolin einen
  neuen, korrekt-relativen Sprungbefehl (`0F 85` mit frisch berechnetem
  `rel32`) einsetzen. Instruktionen ohne Adressbezug (z.B. `test`, `push imm32`,
  `mov r32,[base+idx*4+disp32]`) sind dagegen immer sicher, unveraendert zu
  kopieren.
- radare2s Klassennamen aus RTTI/Vtable-Analyse koennen bei vom Linker
  COMDAT-gefaltetem Code (identischer Maschinencode fuer mehrere Klassen)
  irrefuehrend sein -- die im Ghidra-Pseudocode erhaltenen Debug-Strings
  (`OutputDebugStringA`-Aufrufe) sind die verlaesslichere Quelle fuer die
  tatsaechliche, historische Methode-Zuordnung.

## Nachtrag 2026-09-12 (3. Fortsetzung): EP8-Quellensuche loest FUN_006effa0 auf, neues Paradox gefunden

Eine gezielte Suche im echten EP8-Quellcode (Client- und Server-Baum) hat
`FUN_006effa0` endgueltig identifiziert und damit die Einschaetzung aus dem
vorigen Nachtrag weiter praezisiert:

**`FUN_006effa0` ist `AgcmItem::OnAddModule()`** (`Modules/AClient/AgcmItem/
AgcmItem.cpp:365`), NICHT irgendein Pro-Item-Konstruktor. Es ist der
Post-Konstruktions-Bootstrap-Hook des `AgcmItem`-Singleton-Moduls, aufgerufen
GENAU EINMAL beim Programmstart durch die Kette
`AgcEngine::OnInitialize3D() -> OnRegisterModule() -> REGISTER_MODULE(AgcmItem)
-> ApModule::AddModule() -> this->OnAddModule() (virtueller Aufruf)` --
noch bevor der Login-Bildschirm ueberhaupt existiert. Das erklaert die "0
Treffer" endgueltig anders als gedacht: die Funktion ist nicht kaputt oder
unerreichbar, sie ist laengst gelaufen, bevor unser Hook je installiert
werden konnte (der immer erst NACH Prozessstart ansetzt). Auch die "kein
Aufrufer per statischer Analyse auffindbar"-Beobachtung ist damit erklaert:
`OnAddModule()` ist `virtual`, der einzige Aufruf geschieht rein ueber
Vtable-Dispatch, die Adresse taucht nirgendwo als Sprungziel oder
Datenreferenz auf.

Live-Nachpruefung bestaetigt das: das `AgcmItem`-Singleton-Objekt selbst
(gefunden als `userdata`/`arg_8h` in unserem Event-0x65-Callback, Adresse
z.B. `0x166877c0`) hat tatsaechlich `[+0xc9a]=4` und `[+0xc5c]=0x15fb2020`
(ein gueltiger `AgpmItem`-Modulzeiger) -- korrekt initialisiert. Unsere
fruehere Verwirrung kam daher, dass wir zwischenzeitlich die falschen Werte
gelesen hatten (vom Item-Objekt `arg_4h` statt vom Singleton `arg_8h`).

**Zweiter Fund, der die Spur wieder verkompliziert:** Im echten
Referenzquellcode ist Event 101 (`0x65`) klar identifiziert als
`ITEM_CB_ID_ADD_ITEM_EXTRADATA` (`AgpmItem.h:416`), gefeuert in
`AgpmItem::OnOperationAdd()` fuer "Siegel-Daten" (`AgpmItem.cpp:2865-2875`).
Der einzige dort registrierte Handler, `AgcmItem::CBAddItemExtraData`
(`AgcmItem.cpp:4116-4142`), kopiert in dieser Quellversion nur harmlose
`AgpdSealData` -- KEINE Part-Index-/Attachment-Logik. Unser eigener Client
hat an genau dieser Callback-Adresse (`0x006ed670`) aber nachweislich die
in Fund 4 (oben) beschriebene Anhaenge-Logik. Zwei Erklaerungen bleiben
offen: entweder ist unser kompilierter Client eine spaetere Patch-Revision
mit erweiterter Callback-Logik an derselben Registrierungsstelle, oder die
Registrierung/Event-Zuordnung hat sich zwischen dieser Quellversion und
unserem Client-Build verschoben. Fuer die Untersuchung selbst aendert das
nichts: der Callback laeuft nachweislich, mit gueltigen Eingabedaten.

### Das Paradox: Rueckgabewert ist gueltig, Erfolgspfad wird trotzdem nie erreicht

Eine saubere Neudisassemblierung von `0x006ed670` zeigte: `fcn.004e40e0`
wird mit DREI Argumenten aufgerufen (`this=lut_ptr`, `part_idx=4`,
`item_ptr`) und berechnet `*(int*)(table_base + part_idx*0x10 + 4) +
item_ptr` -- ein BERECHNETER ZEIGER, keine Bool'sche Erfolgsmeldung. Live
gemessen liefert dieser Aufruf durchgehend gueltige, plausible Adressen
(`item_ptr + 0x590`, konsistent ueber mehrere Items). Trotzdem wird der
direkt anschliessende Erfolgspfad (`mov dword[eax+0x54],1`, live per
dediziertem Hook DIREKT an dieser Instruktion ueberprueft) **kein einziges
Mal erreicht** -- auch nicht, nachdem der davorliegende bedingte Sprung
live per NOP forciert deaktiviert wurde.

Das noetigte einen zweiten Bypass-Versuch (den nachfolgenden `test esi,esi;
je`-Check ebenfalls per NOP entfernt) -- das fuehrte zu einem Absturz
(Absturzadresse `0x006ed6b1`, exakt die `rep movsd`-Kopierinstruktion
dahinter). Das ist ein wichtiges Ergebnis fuer sich: **die beiden
Pruefungen sind nicht redundant/tot** -- sie fangen echte, im Live-Betrieb
tatsaechlich auftretende Faelle ungueltiger Zeiger ab. Wir wissen nur noch
nicht, warum unser konkreter Fall (scheinbar gueltiger `eax`-Rueckgabewert
per unabhaengiger Messung) trotzdem als "ungueltig" behandelt wird -- ein
echter, unaufgeloester Widerspruch zwischen zwei eigentlich gleichwertigen
Messmethoden, der eine vorsichtigere, schrittweise Nachverfolgung braucht
(z.B. EFLAGS/ZF direkt an der Sprungentscheidung mitschneiden, statt aus
einem getrennt gemessenen Register-Snapshot zu schliessen) statt eines
erzwungenen Bypasses.

**Bewusst hier abgebrochen** (Arbeitsphase zu weit fortgeschritten fuer eine
sichere Fortsetzung des Bypass-Ansatzes) -- der Client wurde nach dem
Absturz sauber neu gestartet (frischer Prozess, keine Hooks mehr aktiv,
Originaldatei auf der Platte war nie betroffen). Fuer die naechste Arbeitsphase:

1. EFLAGS/ZF direkt am Sprungpunkt (`0x006ed696`) capturen, nicht nur den
   vorher separat gemessenen `eax`-Wert -- das loest das Paradox entweder
   auf (zeigt, dass ZF tatsaechlich gesetzt ist, obwohl `eax` scheinbar
   ungleich Null gemessen wurde -- z.B. durch ein Timing-/Registerproblem
   in unserer eigenen Messmethode) oder bestaetigt einen echten,
   unerwarteten Client-Mechanismus.
2. Pruefen, ob `*(int*)(lut_ptr + 0x38)` (die "Tabellenbasis", auf der die
   ganze Adressberechnung beruht) selbst gueltig/sinnvoll ist -- bisher nur
   indirekt ueber das Endergebnis der Rechnung erschlossen, nie direkt
   gemessen.
3. Erwaegen, ob unser Client tatsaechlich eine spaetere Patch-Revision
   gegenueber der vorliegenden EP8-Quelle ist (siehe "zweiter Fund" oben) --
   falls ja, waere ein neuerer/passenderer Quellstand fuer diese konkrete
   Funktion hilfreich, falls auftreibbar.

## Ergebnis 2026-09-13: Geloest -- fehlendes CharType (Race/Gender/Class) war die tatsaechliche Ursache

Eine externe Analyse (Quellenabgleich gegen den dekompilierten Client, ohne
Live-Speicherzugriff) fand den tatsaechlichen Fehler: `build_factor_packet`
liess das `CharType`-Unterpaket (Bit 2 der inneren Huelle -- Race/Gender/
Class, je INT32, 1-Byte-Maske `0x07`) komplett aus. Der Client bestimmt das
Koerpermodell zwar aus der Charakter-Template-ID, liest Rasse fuer
Laufzeitpruefungen (Item-Nutzbarkeit-nach-Rasse, Auswahl-Animation-nach-
Rasse) aber aus genau diesem Laufzeit-Faktor-Feld. Ohne `CharType` blieb
die Laufzeit-Rasse `-1` -- unabhaengig davon, dass das 3D-Modell laengst
korrekt geladen war. Das erklaert beide Symptome gleichzeitig ueber eine
einzige, gemeinsame Ursache:

- Item-Anhaengung: die Nutzbarkeitspruefung vor dem Anhaengen scheitert
  fuer Rasse `-1` immer, unabhaengig davon, ob der Item-Cache-Eintrag selbst
  fehlerfrei ist (passt zu allem, was in den Nachtraegen oben live bewiesen
  wurde -- Paket korrekt geparst, Item korrekt registriert, Event `0x65`
  feuert mit gueltigem Rueckgabewert, aber der Erfolgspfad wird nie
  erreicht: die hier gefundene Rassenpruefung ist die fehlende Erklaerung
  fuer genau dieses Paradox).
- Fehlende Vorwaerts-Animation beim Selektieren: die Animationsauswahl ist
  ebenfalls rassenabhaengig und liefert bei Rasse `-1` kein Ergebnis.

**Fix** (`build_factor_packet` in `main.rs`, `db::list_characters`s Join
gegen `character_templates`): Race/Gender/Class werden jetzt ueber
`race_tid` nachgeschlagen und als `CharType`-Unterpaket gesendet.
Ephemere Vorschau-Charaktere (`build_race_preview_packet`, kein echtes
Template) senden bewusst `race=-1` als Sentinel, wodurch das ganze
`CharType`-Unterpaket ausgelassen wird, statt einen falschen `0`-Wert zu
senden.

**Live verifiziert**: Waffe UND Vorwaerts-Animation sind nach dem Fix
beide korrekt. Damit ist diese Sequenz abgeschlossen -- das offene
Paradox aus dem vorigen Nachtrag ist aufgeloest (nicht durch Aufloesen
des Widerspruchs selbst, sondern durch Auffinden der tatsaechlichen,
vorgelagerten Ursache, die den Widerspruch nur als Symptom zeigte).

Die Diagnose der Callback-Identitaet (`0x006ED670`/Event `0x65`) aus den
vorigen Nachtraegen bleibt ungeklaert, ist aber fuer die geloeste Frage
nicht mehr relevant -- der Fehler lag vorgelagert in fehlenden Faktordaten,
nicht im Callback-Mechanismus selbst.
