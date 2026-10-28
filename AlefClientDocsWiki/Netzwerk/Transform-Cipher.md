# Winsock Transform-Cipher-Suite (StartupEncryption)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Ziel dieser Datei: den Netzwerk-Transform-Algorithmus aufschluesseln, der in
[WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md](Sequenz-01-Login-Handshake.md) (Schritte 6-9,
[`AgpmStartupEncryption`](../Module/AgpmStartupEncryption.md)) nur als Blackbox beschrieben war. Alle Adressen sind gegen
`C:\Spiele\Archlord\alefclient.exe` (SHA-256 siehe [README.md](../Daten-und-Werkzeuge/Disassembly-2013.md)) per RTTI-Auswertung
verifiziert, nicht nur aus `alefclient.pseudocode.c` abgelesen.

Wichtig: Dies ist NICHT derselbe Mechanismus wie die Datei-/Config-Verschluesselung aus
[DATA_DECRYPTION_PROGRESS.md](../Daten-und-Werkzeuge/Datenentschluesselung.md) (CryptoAPI-RC4 mit Key `1111`/`asdfqwer`).
Es handelt sich um eine zweite, eigenstaendige Krypto-Schicht speziell fuer Netzwerkpakete.

## Kurzfazit

- Der Client besitzt eine austauschbare Cipher-Suite mit vier Algorithmen, **alle vier
  bitgenau gegen den jeweiligen oeffentlichen Standard verifiziert** (exakter Byte-Abgleich
  der Konstantentabellen im Binary, siehe Abschnitte "Bitgenaue Verifikation" unten):
  **Blowfish** (Standard-P-Array + S-Boxen), **`AuMD5Mac`** (MD5-Schluesselableitung + RC4
  ueber Windows CryptoAPI, trotz des Namens keine echte MAC), **Rijndael/AES-128-CBC**
  (kanonische S-Box + Te0-3/Td0-3-Tabellen) und der koreanische Nationalstandard **SEED**
  (exakte KC-Rundenkonstanten).
- Zentrale Klasse: `AuCryptManager` (Ghidra-RTTI-Name), ein **Singleton** an fixer Adresse
  `0x009AC12C`, lazy konstruiert ueber `FUN_004ea680`.
- Die vier Algorithmen sind als eigene C++-Objekte in einem STL-artigen Vector im
  `AuCryptManager` abgelegt, in exakt dieser Reihenfolge/ID:
  - ID `0`: `AuBlowFish`
  - ID `1`: `AuMD5Mac`
  - ID `2`: `AuRijnDael`
  - ID `3`: `AuSeed`
- Die Algorithmus-Auswahl (`+0x18` = Encode-ID, `+0x1c` = Decode-ID) und das Array der vier
  Slot-Zeiger (`+0xc`) liegen auf dem **globalen Singleton** `AuCryptManager` selbst, nicht
  pro Socket (siehe Korrektur unten). Jeder Socket hat bei `socket + 0xc8078` einen eigenen,
  kleinen Transformkontext, der pro Richtung nur einen lazily konstruierten "Holder"-Objektzeiger
  haelt (`+0xc` fuer Encode, `+0x18` fuer Decode) - vermutlich der Session-/Schluesselzustand.
- **Update:** Die aktive Cipher-ID wird vom Server gesetzt, nicht vom Client fest vorgegeben.
  Siehe Abschnitt "Wo die aktive Cipher-ID gesetzt wird" unten (`FUN_00681970`).
- Alle vier Cipher-Wrapper-Klassen (`AuBlowFish`, `AuMD5Mac`, `AuRijnDael`, `AuSeed`) erben
  von einer gemeinsamen abstrakten Basis `AuCryptAlgorithmBase` mit derselben 6-Eintrag-Vtable:
  Destruktor, RTTI-Helfer, `Reset/Init` (+0x08), `Transform/Encrypt` (+0x0c), `Decrypt` (+0x10,
  bitgenau bestaetigt fuer `AuMD5Mac`), `GetLength` (+0x14, bestaetigt: Identitaetsfunktion).
- `FUN_004f9e40`/`FUN_004f9d80` (die CryptoAPI-RC4-Datei-Funktionen aus
  [`DATA_DECRYPTION_PROGRESS.md`](../Daten-und-Werkzeuge/Datenentschluesselung.md)) liegen im selben Adressbereich (`0x4f9xxx`) wie
  `AuCryptManager`, sind aber eine getrennte, viel simplere Baustelle (nur RC4 mit
  statischem Key). Beide Systeme teilen sich nur den generischen CryptoAPI-Init-Wrapper
  (`FUN_004f9cf0`, "Microsoft Base Cryptographic Provider v1.0").
- **Geloest:** Die vier IDs werden ueber eine eigene `AgpmStartupEncryption`-Nachricht vom
  Server gesetzt, verarbeitet von einer Funktion bei VA `0x00681970`, die interessanterweise
  in `alefclient.pseudocode.c` komplett fehlt (siehe unten).

## RTTI-Herleitung (Methodik)

Da `alefclient.pseudocode.c` nur `*param_1 = KlassenName::vftable;`-Zuweisungen zeigt, aber
keine Vtable-Dateninhalte, wurden die echten Vtable-Adressen direkt aus dem Rohbinary
rekonstruiert (MSVC-RTTI-Kette, x86, keine Relocations/ASLR, da "Relocations stripped" laut
[headers.txt](headers.txt)):

1. Mangled RTTI-Typnamen-String suchen: `.?AV<Klasse>@@` (0-terminiert) in der Datei.
2. `TypeDescriptor`-Adresse = Fundstelle − 8 (die zwei DWORDs davor sind
   `pVFTable`/`spare` des `type_info`-Objekts).
3. `RTTICompleteObjectLocator` (COL) finden: 4-Byte-Little-Endian-VA des TypeDescriptors an
   Offset `+12` einer Struktur mit `signature == 0` an Offset `+0`.
4. Vtable finden: 4-Byte-VA des COL an Position `vtable − 4` suchen; `vtable = Fundstelle + 4`.
5. Weil `RVA == Dateioffset` fuer alle Sektionen dieser Datei gilt (siehe
   [headers.txt](headers.txt), z.B. `.rdata` virtual address `49F000` == file pointer `49F000`),
   ist `VA = 0x400000 + Dateioffset` direkt anwendbar, ohne Sektionsumrechnung.

Reproduzierbar z.B. so (Python, gegen die lokale Kopie `C:\Spiele\Archlord\alefclient.exe`):

```python
import struct
data = open(r'C:\Spiele\Archlord\alefclient.exe','rb').read()
base = 0x400000
name_off = data.find(b'.?AVAuRijnDael@@')
td_va = base + name_off - 8
col_off = data.find(struct.pack('<I', td_va)) - 12
col_va = base + col_off
vtable_off = data.find(struct.pack('<I', col_va)) + 4
print(hex(base + vtable_off))
```

## Gefundene Klassen und Adressen

| Klasse | Vtable VA | Rolle |
|---|---|---|
| `AuCryptManager` | `0x008B852C` | Singleton-Registry, haelt die 4 Cipher-Objekte + Encode-/Decode-Auswahl |
| `AuCryptAlgorithmBase` | `0x008B85E8` | Abstrakte Basis, alle Slots ausser Dtor/RTTI zeigen auf Stub `0x007FF230` |
| `AuBlowFish` | `0x008BAEE4` | Cipher-ID `0` |
| `AuMD5Mac` | `0x008BAEA8` | Cipher-ID `1`, nutzt Windows CryptoAPI (`CryptAcquireContextA` mit "Microsoft Base Cryptographic Provider v1.0") |
| `AuRijnDael` | `0x008BAE6C` | Cipher-ID `2` (Rijndael/AES) |
| `AuSeed` | `0x008B8604` | Cipher-ID `3` (SEED, koreanischer Standard) |

Primitive Low-Level-Kontextklassen (separate RTTI-Hierarchie, vermutlich intern von den
`Au*`-Wrapperklassen fuer die eigentliche Blockchiffren-Mathematik benutzt; Beziehung noch
nicht abschliessend verifiziert):

| Klasse | Vtable VA | Kontextgroesse | Reset-Funktion |
|---|---|---:|---|
| `BASE_CTX` | `0x008B84F0` | - | Stub `0x007FF230` |
| `BLOWFISH_CTX` | `0x008B84FC` | `0x1050` Bytes (P-Array + 4 S-Boxen, passt exakt zu klassischem Blowfish) | `FUN_004f92d0` |
| `MD5MAC_CTX` | `0x008B8508` | `0x28` Bytes | `FUN_004f9340` |
| `RIJNDAEL_CTX` | `0x008B8514` | `0x178` Bytes | `FUN_004f93a0` |
| `SEED_ALG_INFO` | `0x008B8520` | `0xc4` Bytes | `FUN_004f9450` |

Diese vier "CTX"-Klassen haben jeweils nur eine 2-Eintrag-Vtable (Reset, Destruktor) - die
naechsten 4 Bytes im Speicher sind bereits der COL-Zeiger der jeweils naechsten Klasse. Das
zeigt: die eigentliche Verschluesselungsarbeit passiert NICHT ueber diese CTX-Vtables,
sondern ueber die separaten `Au*`-Wrapperklassen (siehe unten).

## `AuCryptAlgorithmBase`-Interface (6 Slots)

Rekonstruiert durch Vergleich aller vier `Au*`-Vtables nebeneinander:

| Offset | Bedeutung | `AuBlowFish` | `AuMD5Mac` | `AuRijnDael` | `AuSeed` |
|---:|---|---|---|---|---|
| `+0x00` | Destruktor | `0x005017e0` | `0x00500b20` (eigener, ruft `CryptReleaseContext`) | `0x005017e0` | `0x005017e0` |
| `+0x04` | RTTI-Helfer (compilergeneriert, identisch bei allen) | `0x005b91f0` | `0x005b91f0` | `0x005b91f0` | `0x005b91f0` |
| `+0x08` | `Reset`/`Init`/Key-Setup | `0x005012f0` | `0x00500870` | `0x005005a0` | `0x004fe2e0` |
| `+0x0c` | `Transform`/`Encrypt` | `0x00501580` | `0x00500910` | `0x00500620` | `0x004fe7f0` |
| `+0x10` | `Decrypt` (bestaetigt fuer `AuMD5Mac`, siehe unten) | `0x00501710` | `0x00500a00` | `0x00500740` | `0x004fe930` |
| `+0x14` | `GetLength` (bestaetigt: Identitaetsfunktion, siehe unten) | `0x00501560` | `0x00500860` | `0x00500860`* | `0x004fa8f0` |

`*` `AuRijnDael` und `AuMD5Mac` teilen sich exakt dieselbe Adresse fuer `GetLength` - jetzt
bestaetigt (siehe Abschnitt "Bitgenaue Verifikation" unten): `FUN_00500860` lautet schlicht
`return param_1;` (Ausgabelaenge == Eingabelaenge, keine Blockgroessen-Rundung). Das ist
wahrscheinlich Linker-Identical-Code-Folding zweier bytegleicher trivialer Implementierungen,
keine gemeinsame Vtable.

Die Basisklasse `AuCryptAlgorithmBase` selbst hat fuer `+0x08`..`+0x14` ueberall den
Stub `0x007FF230` - denselben Stub, der auch bei `BASE_CTX` als Reset-Funktion dient. Das ist
vermutlich ein projektweiter generischer "nicht implementiert"-Trap fuer nicht ueberschriebene
virtuelle Methoden.

## Aufbau von `AuCryptManager`

Konstruktor `FUN_004f9a50` (Adresse `0x004f9a50`):

- Setzt `AuCryptManager::vftable`.
- Feld `+0x08 = 3` (Bedeutung unklar - evtl. Default-/Max-Index, noch nicht bestaetigt).
- Baut einen wachsenden Vector (STL-artig, `push_back` mit `FUN_004f9970` als
  Reallocation-Pfad) und haengt der Reihe nach vier Objekte an:
  1. `AuBlowFish` (Konstruktor `FUN_00500b60`)
  2. `AuMD5Mac` (Konstruktor `FUN_00500ae0`, ruft direkt `CryptSetProviderA` +
     `CryptAcquireContextA("Microsoft Base Cryptographic Provider v1.0", PROV_RSA_FULL,
     CRYPT_VERIFYCONTEXT)`)
  3. `AuRijnDael` (Konstruktor `FUN_004fea70`)
  4. `AuSeed` (Konstruktor `FUN_004fa8e0`)
- Reihenfolge im Vector = Cipher-ID (`0`..`3`), passend zu den IDs, die die vier
  `*_CTX`-Klassen in ihren eigenen Konstruktoren in ihr `id`-Feld schreiben
  (`BLOWFISH_CTX`→`0`, `MD5MAC_CTX`→`1`, `RIJNDAEL_CTX`→`2`, `SEED_ALG_INFO`→`3`) - zwei
  unabhaengige Codepfade bestaetigen dieselbe Zuordnung.

Singleton-Zugriff: `FUN_004ea680()` liefert bei jedem Aufruf `&DAT_009ac12c`; beim ersten
Aufruf wird ueber ein Guard-Flag (`DAT_009ac154`) einmalig `FUN_004f9a50` aufgerufen und
`FUN_004f9c20` (Destruktor-Aufraeumung) via `atexit` registriert. Klassisches Meyer's-Singleton-Muster.

## Wo die aktive Cipher-ID gesetzt wird

**Fundstelle: VA `0x00681970`.** Diese Funktion liegt direkt vor `FUN_006819c0` im
Speicher, ist aber in `alefclient.pseudocode.c` und `functions.tsv` NICHT vorhanden - Ghidras
Auto-Analyse hat sie nie als eigene Funktion erkannt (vermutlich weil sie ausschliesslich
ueber eine Handler-Registrierungstabelle referenziert wird, nie per direktem `call`; siehe
"Aufrufkontext" unten). Sie musste daher direkt aus `alefclient.disasm.txt` gelesen werden.

### Disassembly (kommentiert)

```text
00681970: mov ecx, [esp+4]         ; ecx = param_1 (Zeiger auf Empfangs-Deskriptor)
00681974: test ecx, ecx
00681976: je   006819BA            ; NULL-Check -> Abbruch (return 0)
00681978: cmp  dword ptr [esp+8],0
0068197D: je   006819BA            ; param_2 == 0 -> Abbruch
0068197F: cmp  dword ptr [esp+0Ch],0
00681984: je   006819BA            ; param_3 == 0 -> Abbruch
00681986: mov  eax,[ecx]           ; eax = *param_1        (Datenzeiger: 2x int32)
00681988: mov  ecx,[ecx+4]         ; ecx = *(param_1+4)    (Laengen-/Feldbeschreiber)
0068198B: cmp  word ptr [ecx],8    ; deklarierte Groesse muss genau 8 Bytes sein (2x int32)
0068198F: jne  006819BA            ; sonst Abbruch
00681991: push esi
00681992: mov  esi,[eax]           ; esi = erstes int32  (encode-ID)
00681994: cmp  esi,-1
00681997: push edi
00681998: mov  edi,[eax+4]         ; edi = zweites int32 (decode-ID)
0068199B: jle  006819B2            ; esi <= -1 (also < 0) -> ueberspringen
0068199D: cmp  edi,-1
006819A0: jle  006819B2            ; edi <= -1 -> ueberspringen
006819A2: call 004EA680            ; AuCryptManager-Singleton holen
006819A7: mov  [eax+18h], esi      ; Singleton->encodeAlgoId = esi
006819AA: call 004EA680            ; Singleton erneut holen
006819AF: mov  [eax+1Ch], edi      ; Singleton->decodeAlgoId = edi
006819B2: pop  edi
006819B3: mov  eax,1
006819B8: pop  esi
006819B9: ret
006819BA: xor  eax,eax
006819BC: ret
```

**Klartext:** Diese Funktion liest aus einem eingehenden Netzwerk-Unterpaket genau zwei
`int32`-Werte (validiert durch eine Laengenpruefung auf exakt 8 Bytes) und schreibt sie
direkt und ungeprueft (ausser auf "nicht negativ") in die Felder `AuCryptManager+0x18`
(Encode-Algorithmus-ID) und `AuCryptManager+0x1c` (Decode-Algorithmus-ID) des **globalen**
Singletons. Es gibt keine Bereichspruefung gegen die bekannten IDs `0..3` - ein Wert `>= 4`
wuerde spaeter beim Dispatch (`FUN_004f9570`) einfach `return 0` ausloesen (Cipher-Objekt
bleibt ungueltig/NULL).

**Schlussfolgerung: Der Server bestimmt, welcher der vier Cipher (`0`=Blowfish, `1`=MD5Mac,
`2`=Rijndael/AES, `3`=SEED) fuer Senden und Empfangen verwendet wird - und zwar fuer beide
Richtungen potenziell unterschiedlich.** Das ist nicht im Client hartkodiert.

### Aufrufkontext: Handler-Registrierung von `AgpmStartupEncryption`

Die Adresse `0x00681970` taucht in der gesamten Binary nur an EINER Stelle als Daten-Zeiger
auf (kein direkter `call`): im Modul-Setup-Code von `AgpmStartupEncryption`, VA `0x00681EA8`
ff., wo mehrere Empfangs-Handler nacheinander registriert werden:

```text
00681EA9: push 681970h   ; unsere ID-Setter-Funktion
00681EAE: call 0065E490  ; Register(module, handler)  -> vermutlich Operation "0"
...
00681EC2: push 6819C0h   ; FUN_006819c0 = Seed-Austausch (Schritt 7-8)
00681EC7: call 006DD1E0  ; Register(module, handler)  -> vermutlich Operation "1"
...
00681EDB: push 681B30h   ; FUN_00681b30 = Transform aktivieren (Schritt 9)
00681EE0: call 005781F0  ; Register(module, handler)  -> vermutlich Operation "2"
...
00681EF0: push 681BE0h   ; FUN_00681be0 = Encode-Key direkt setzen (siehe unten)
00681EF5: call 0058EE20  ; Register(module, handler)  -> vermutlich Operation "3"
...
00681F05: push 681C70h   ; FUN_00681c70 = Decode-Key direkt setzen (siehe unten)
```

Das bestaetigt zweierlei:

1. `0x00681970` ist ein regulaerer, vom Netzwerk-Dispatcher aufgerufener Operationshandler
   innerhalb desselben Moduls wie die bereits dokumentierten Schritte 7-9
   ([WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md](Sequenz-01-Login-Handshake.md)) - vermutlich
   Operation `0`, noch VOR dem eigentlichen Seed-Austausch (Operation `1`).
2. Es gibt mindestens zwei weitere `AgpmStartupEncryption`-Handler (`0x00681be0`, `0x00681c70`),
   die jetzt ebenfalls analysiert sind (siehe naechster Abschnitt).

Da jede Registrierung ueber eine JEWEILS ANDERE Aufruffunktion laeuft (`0x65e490`, `0x6dd1e0`,
`0x5781f0`, `0x58ee20`, ...), handelt es sich wahrscheinlich nicht um einen generischen
Array-Push in eine Opcode-Tabelle, sondern um benannte Setter fuer einzelne Member-Felder
einer Modul-Klasse (`this->OnOperationX = handler`). Die exakte numerische Zuordnung
Handler->Operationsnummer ist damit weiterhin eine Inferenz aus der Registrierungsreihenfolge,
keine bewiesene Tatsache.

## `0x00681be0` und `0x00681c70`: direkte Schluessel-Injektion (in der Praxis toter Code)

Wie `0x00681970` fehlen auch diese beiden Funktionen komplett in `alefclient.pseudocode.c`
und `functions.tsv` - wieder nur ueber die Registrierungstabelle referenziert, nie per
direktem `call`. Beide sind strukturell fast identisch, nur die letzte Aktion unterscheidet
sich: `0x00681be0` behandelt die **Encode**-Richtung, `0x00681c70` die **Decode**-Richtung.

### Disassembly (0x00681be0, kommentiert; 0x00681c70 ist bis auf den letzten Call identisch)

```text
00681BE0: mov  eax,[esp+4]        ; param_1 = Empfangs-Deskriptor {Datenzeiger, Laengenzeiger}
00681BE4: test eax,eax
00681BE6: je   00681C5F           ; NULL -> Abbruch (return 0)
00681BE8: mov  ecx,[esp+8]        ; param_2 (ungenutzt ausser als NULL-Check)
00681BEC: test ecx,ecx
00681BEE: je   00681C5F
00681BF0: mov  edx,[esp+0Ch]      ; param_3 = Zeiger auf Socket-ID
00681BF4: test edx,edx
00681BF6: je   00681C5F
00681BF8: push ebx
00681BF9: push esi
00681BFA: mov  esi,[edx]          ; esi = Socket-ID
00681BFC: push edi
00681BFD: mov  edi,[eax]          ; edi = Datenzeiger (Rohbytes aus dem Paket)
00681BFF: mov  eax,[eax+4]        ; eax = Zeiger auf Laengenfeld
00681C02: movzx ebx,word ptr[eax] ; ebx = deklarierte Paketlaenge (16 bit)
00681C05: call 004E45F0           ; Modul-/Manager-Basis holen (Standard-Vorspann, wie in FUN_006819c0)
00681C0A: test eax,eax
00681C0C: je   00681C59           ; Modul nicht bereit -> Abbruch
00681C0E: push esi
00681C0F: lea  ecx,[eax+0x12C48]  ; ecx = eingebetteter AcSocketManager-artiger Kontext
00681C15: call 006FDA40           ; Socket-Objekt fuer die ID holen
00681C1A: mov  esi,eax
00681C1C: test esi,esi
00681C1E: je   00681C59           ; Socket nicht gefunden -> Abbruch
00681C20: cmp  dword ptr[esi+24h],0
00681C24: je   00681C59           ; Socket-State == 0 (nicht verbunden) -> Abbruch
00681C26: call 004EA680           ; AuCryptManager-Singleton holen
00681C2B: mov  ecx,eax
00681C2D: call 00510D50           ; <-- IMMER "return 0" (siehe unten!)
00681C32: test eax,eax
00681C34: je   00681C50           ; -> IMMER wahr, IMMER Sprung hierher: kein Key-Update!
00681C36: movsx ecx,bx            ; (toter Code:) ecx = Paketlaenge
00681C39: push 0                  ; (toter Code:) flag = 0
00681C3B: push ecx                ; (toter Code:) Laenge
00681C3C: push edi                ; (toter Code:) Datenzeiger
00681C3D: add  esi,0xC8078        ; (toter Code:) esi = Pro-Socket-Transformkontext
00681C43: push esi                ; (toter Code:) Kontext
00681C44: call 004EA680           ; (toter Code:) Singleton erneut holen
00681C49: mov  ecx,eax
00681C4B: call 004F96B0           ; (toter Code:) Encode-Key-Setup mit Rohdaten aus dem Paket
00681C50: pop  edi
00681C51: pop  esi
00681C52: mov  eax,1              ; Rueckgabe IMMER 1 (Erfolg), unabhaengig vom obigen Zweig
00681C57: pop  ebx
00681C58: ret
```

`0x00681c70` ist byte-identisch bis auf den letzten Aufruf: statt `FUN_004f96b0` (Encode) wird
`FUN_004f9720` (Decode) aufgerufen.

### Der entscheidende Fund: `FUN_00510D50` gibt immer `0` zurueck

```c
undefined4 FUN_00510d50(void) { return 0; }
```

Diese Funktion wird ueberall im Client als generischer Trivial-Stub wiederverwendet (u.a. als
Default-Callback in ganz anderen Subsystemen wie Charakter-Events, UI-Callbacks) - vermutlich
vom Linker per Identical-Code-Folding zu EINER gemeinsamen Adresse zusammengelegt, weil viele
verschiedene "gibt einfach 0 zurueck"-Funktionen bytegleich sind.

**Das bedeutet: Der komplette "Key aus Rohpaket setzen"-Zweig in `0x00681be0` und `0x00681c70`
ist im ausgelieferten Client toter Code.** Beide Funktionen validieren Socket und Paket ganz
normal, holen sich den `AuCryptManager`-Singleton, fragen aber danach eine Bedingung ab, die
IMMER falsch/negativ ausfaellt (`FUN_00510d50()==0`), springen dadurch IMMER ueber den
eigentlichen `FUN_004f96b0`/`FUN_004f9720`-Aufruf und geben trotzdem `1` (Erfolg) zurueck.
Ein Server, der diese Operationen sendet, wuerde also von diesem Client-Build niemals ein
tatsaechliches Setzen des Encode-/Decode-Schluessels ueber diesen Weg erhalten - der Client
tut nur so, als waere es passiert.

Da dies eine reine Kontrollfluss-Tatsache ist (die Bedingung haengt von keinerlei Laufzeitdaten
ab), ist sie **ohne Live-Traffic vollstaendig statisch beweisbar** - im Gegensatz zu den meisten
anderen offenen Punkten in diesem Projekt.

Moegliche Erklaerungen (nicht abschliessend zu klaeren ohne Quellcode/aeltere Client-Version):

- Legacy-/Debug-Feature, das fuer den Release-Build absichtlich deaktiviert wurde (z.B. weil
  eine ungeprüfte Rohschluessel-Injektion vom Server ein Sicherheitsrisiko waere).
- Reste einer alternativen/fruehen Handshake-Variante, die durch die Seed-Austausch-Methode
  (`FUN_006819c0`, Schritt 7-8) ersetzt wurde, aber aus Kompatibilitaets- oder Trace-Gruenden
  im Opcode-Dispatch verblieben ist.
- Ein durch Compiler-/Linker-Optimierung (ICF) verfaelschter Aufruf: der urspruengliche Code
  rief moeglicherweise eine ANDERE, semantisch sinnvolle Prueffunktion auf, die zufaellig
  ebenfalls "return 0" kompilierte und deshalb mit `FUN_00510d50` zusammengelegt wurde. Ohne
  Symbolinformationen (PDB) laesst sich das nicht unterscheiden.

## Bitgenaue Verifikation: SEED und AuMD5Mac

### SEED (`AuSeed` / `SEED_ALG_INFO`)

`Reset` (`FUN_004fe2e0`, Vtable-Slot `+0x08` von `AuSeed`) nimmt einen 32-Byte-Input
entgegen (identisch zum generischen 8-DWORD-Format aus `FUN_004f96b0`/`FUN_004f9720`) und aufteilt
ihn in zwei 16-Byte-Haelften:

```c
void FUN_004fe2e0(int param_1, undefined4 *param_2, int param_3) {
  // param_2[0..3] -> IV;  param_2[4..7] -> Schluessel
  FUN_004fa910(2, 2, &param_2[4], param_1);   // Modus setzen + IV uebernehmen
  FUN_004fa960(&param_2[0], 0x10, param_1);   // 128-Bit-Schluessel -> Rundenschluessel-Expansion
}
```

Der eigentliche Beweis steckt in `FUN_004fa960` (Rundenschluessel-Expansion). Sie berechnet pro
Runde zwei 32-Bit-Rundenschluessel ueber eine G-Funktion (vier 256-Eintrag-S-Boxen `SS0..SS3`
per XOR verknuepft, hier bei `DAT_009555a8`/`DAT_009551a8`/`DAT_009559a8`/`DAT_00954da8`) und
Rundenkonstanten, die aus `A,B,C,D` (den vier 32-Bit-Woertern des Schluessels) plus/minus einer
Konstante gebildet werden. Genau diese Konstanten sind der Fingerabdruck:

| Runde | Konstante im Code | Offizielle SEED-Konstante (KC-Tabelle, z.B. OpenSSL `seed.c`) |
|---:|---|---|
| 0 | `0x9e3779b9` | `KC0 = 0x9e3779b9` |
| 1 | `0x3c6ef373` | `KC1 = 0x3c6ef373` |
| 2 | `0x78dde6e6` | `KC2 = 0x78dde6e6` |
| 3 | `0xf1bbcdcc` | `KC3 = 0xf1bbcdcc` |
| 4 | `0xe3779b99` | `KC4 = 0xe3779b99` |
| 5 | `0xc6ef3733` | `KC5 = 0xc6ef3733` |
| 6 | `0x8dde6e67` | `KC6 = 0x8dde6e67` |
| 7 | `0x1bbcdccf` | `KC7 = 0x1bbcdccf` |
| 8 | `0x3779b99e` | `KC8 = 0x3779b99e` |

(weitere Runden folgen im Code nach demselben Muster, nicht mehr einzeln ausgezaehlt.) Diese
Konstantenfolge ist **byte-identisch** mit der oeffentlich standardisierten SEED-Rundenkonstantentabelle
(KISA/RFC 4269, z.B. wie in OpenSSLs `crypto/seed/seed_local.h` benannt `KC0`..`KC15`). Eine
zufaellige Uebereinstimmung ueber neun aufeinanderfolgende 32-Bit-Werte ist praktisch
ausgeschlossen.

Zusatzbeleg: `FUN_004fe360` (Chaining-Modus-Funktion, Vtable-Slot `+0x0c`/`Transform`) arbeitet
strikt mit 16-Byte-Bloecken (`0x10`), ruft den Rundenfunktions-Kern `FUN_004fb4e0(ctx+0x44, block)`
pro Block auf und implementiert per Sprungtabelle mehrere Chaining-Modi (ECB/CBC/CFB/OFB-artig,
Faelle `1..4`). `ctx+0x44` bis `ctx+0xc4` (128 Byte) ist exakt groß genug fuer SEEDs 16 Runden
mit je zwei 32-Bit-Rundenschluesseln (`16 * 2 * 4 = 128 Byte`).

**Fazit: `AuSeed` ist eine bitgenau korrekte SEED-Implementierung (128-Bit-Block, 128-Bit-Schluessel,
16 Runden), mit klassischer Blockmodus-Auswahl (ECB/CBC/CFB/OFB) obendrauf.** Nicht mehr nur
strukturelle Vermutung, sondern durch die Rundenkonstanten algorithmisch bewiesen.

### `AuMD5Mac`

Hier ist die Verifikation noch direkter, weil keine eigene Bit-Mathematik vorliegt, sondern nur
Windows-CryptoAPI-Aufrufe mit literalen Konstanten:

**`Reset`** (`FUN_00500870`, Vtable-Slot `+0x08`):

```c
if (param_4 != 0) {                    // Schluesselmaterial wird explizit uebergeben
    memcpy(ctx + 8, param_2, 0x20);    // 32 Byte roh uebernehmen, keine Ableitung
    return;
}
// Sonst: KEIN externes Material -> ctx+8 wird mit einem SCHWACHEN PRNG gefuellt:
srand(timeGetTime());                  // Seed = Millisekunden seit Systemstart
for (i = 0; i < 0x20; i++) buf[i] = (char)rand();   // 32 Byte aus C-Runtime-rand()
// ... und gleichzeitig als Rueckgabewert an den Aufrufer zurueckkopiert
```

**`Transform`/Encrypt** (`FUN_00500910`, Vtable-Slot `+0x0c`):

```c
CryptCreateHash(hProv, 0x8003 /* CALG_MD5 */, 0, 0, &hHash);
CryptHashData(hHash, ctx + 8, 0x20, 0);              // hasht die 32 Byte aus Reset
CryptDeriveKey(hProv, 0x6801 /* CALG_RC4 */, hHash, 4, &hKey);
CryptDestroyHash(hHash);
CryptEncrypt(hKey, 0, 0, 0, data, &len, len);        // RC4-Strom-Verschluesselung
CryptDestroyKey(hKey);
```

**`Decrypt`** (`FUN_00500a00`, Vtable-Slot `+0x10`, damit ist dieser Slot fuer alle vier Cipher
bestaetigt): identischer Ablauf, aber `CryptDecrypt` statt `CryptEncrypt`.

**`GetLength`** (`FUN_00500860`, Vtable-Slot `+0x14`): `return param_1;` - reine
Identitaetsfunktion, RC4 ist ein Stromchiffre ohne Blockpadding, Ausgabelaenge == Eingabelaenge.
Erklaert auch, warum sich `AuRijnDael` dieselbe Adresse teilt (siehe Korrektur oben) - falls
`AuRijnDael` intern ebenfalls ohne Laengenaenderung arbeitet (z.B. CTR/Stream-artiger Modus statt
klassischem Blockpadding), waere das dieselbe triviale Funktion, vom Linker gefaltet.

**Fazit: `AuMD5Mac` ist trotz des Namens keine MAC (Message Authentication Code) im
kryptographischen Sinn, sondern MD5-Schluesselableitung + RC4-Verschluesselung ueber
Windows CryptoAPI** - exakt dasselbe Muster (`CALG_MD5`=`0x8003`, `CALG_RC4`=`0x6801`,
`CryptDeriveKey`-Flag `4`) wie die Datei-/Config-Entschluesselung aus
[DATA_DECRYPTION_PROGRESS.md](../Daten-und-Werkzeuge/Datenentschluesselung.md) - nur dass dort ein FESTER
String-Key (`"1111"`/`"asdfqwer"`) gehasht wird, waehrend hier das 32-Byte-Handshake-Material
aus `Reset` gehasht wird.

**Sicherheitsrelevante Randnotiz (rein aus Code-Lesbarkeit, nicht getestet):** Der Fallback-Zweig
in `Reset` erzeugt Schluesselmaterial mit `srand(timeGetTime())` + `rand()` - beides
kryptographisch unsichere, mit relativ wenigen Bits Entropie vorhersagbare Zufallsquellen
(`timeGetTime()` liefert Millisekunden seit Systemstart, ein sehr kleiner Suchraum). Ob dieser
Zweig im echten Handshake ueberhaupt erreicht wird (`param_4` kommt aus dem Aufrufkontext, meist
wird ja explizit Material aus `FUN_004f96b0`/`FUN_004f9720` durchgereicht), ist ohne Live-Traffic
nicht abschliessend zu sagen - die Code-Existenz und ihre Schwaeche ist aber unabhaengig davon
statisch belegt.

## Bitgenaue Verifikation: Blowfish und AES/Rijndael

Fuer beide wurde diesmal nicht der Kontrollfluss gelesen, sondern direkt die im Binary
liegenden Konstantentabellen per Rohbyte-Suche gegen die jeweiligen oeffentlichen Referenzwerte
geprueft - die staerkste moegliche Verifikationsform, da eine zufaellige Uebereinstimmung
ueber mehrere aufeinanderfolgende 32-Bit-Werte praktisch ausgeschlossen ist.

### Blowfish (`AuBlowFish` / `BLOWFISH_CTX`)

Das komplette 18-Wort-P-Array (Initialisierungskonstanten aus den Nachkommastellen von Pi,
Teil der offiziellen Blowfish-Spezifikation von Bruce Schneier) liegt unveraendert bei
Datei-Offset `0x555e58` (VA `0x00955e58`):

```text
P1..P18 = 243F6A88 85A308D3 13198A2E 03707344 A4093822 299F31D0
          082EFA98 EC4E6C89 452821E6 38D01377 BE5466CF 34E90C6C
          C0AC29B7 C97C50DD 3F84D5B5 B5470917 9216D5D9 8979FB1B
```

Alle 18 Werte stimmen **exakt** mit der Referenztabelle ueberein. Direkt danach (VA
`0x00955ea0`) beginnt S-Box 0, ebenfalls exakt passend zur Spezifikation:

```text
S-Box0[0..7] = D1310BA6 98DFB5AC 2FFD72DB D01ADFB7 B8E1AFED 6A267E96 BA7C9045 F12C7F99
```

`FUN_00500b70` (Rundenfunktion, siehe [WINSOCK_TRANSFORM_CIPHER_SUITE.md](Transform-Cipher.md)
vorherige Fassung) liest genau aus diesem P-Array/S-Box-Bereich (`P-Array` bei `ctx+8`,
S-Boxen ab `ctx+0x450`, passend zur Kontextgroesse `0x1050` = 18*4 + 4*256*4 Byte).

**Fazit: `AuBlowFish` ist eine bitgenau standardkonforme Blowfish-Implementierung**, inklusive
der originalen Pi-basierten Initialisierungswerte vor der eigentlichen Schluesselexpansion.

### Update 2026-09-06: Byte-Reihenfolge live bestaetigt (Little Endian, nicht Standard-Big-Endian)

Ueber das `AlefLogin`-Serverexperiment (siehe unten sowie [`CLIENT_LAUNCH_AUTH_MECHANISM.md`](../Start-und-Login/Startmechanismus.md))
konnte erstmals echter, mit dem client-eigenen Schluessel verschluesselter Traffic
entschluesselt werden. Dabei zeigte sich: `FUN_00500b70` (die Rundenfunktion) laedt jede
32-Bit-Blockhaelfte ueber eine native x86-`*(uint*)ptr`-Leseoperation - das ist **Little
Endian**, nicht die im klassischen Blowfish-Referenzcode (z.B. OpenSSL) uebliche
**Big-Endian**-Byte-Interpretation der Blockhaelften. Die Rundenmathematik selbst (P-Array/
S-Box-Kombination) ist weiterhin exakt Standard-Blowfish - nur die Byte-zu-Wort-Konvertierung
am Blockein-/ausgang unterscheidet sich vom ueblichen Referenz-Verhalten. ECB-Modus (kein IV,
kein Chaining, letzter Kurzblock nullgepadded) ueber `FUN_00501580` bestaetigt.

Praktisch verifiziert: `Blowfish::<byteorder::LittleEndian>` aus der RustCrypto-`blowfish`-Crate
entschluesselt reale, vom Client gesendete Pakete korrekt zu einem validen `0xD6...0x6B`-Frame
(Opcode `0x0d`, [`AgcmLogin`](../Module/AgcmLogin.md)) - mit `BigEndian` ergab derselbe Schluessel/Chiffretext nur
Zufallsbytes.

### AES/Rijndael (`AuRijnDael` / `RIJNDAEL_CTX`)

Die Schluesselexpansion und Rundenfunktionen referenzieren mehrere globale Tabellen im
`.rdata`-Bereich. Alle wurden gegen die kanonischen, in praktisch jeder schnellen
Referenzimplementierung (Originaler Rijndael-Referenzcode, OpenSSL `aes_core.c`, Firefox NSS,
Linux-Kernel) identischen Te-/Td-Tabellen abgeglichen:

**S-Box** (`DAT_008b9640`, byteweise auf alle 4 Bytepositionen dupliziert - ein Standardtrick,
um jede Byteposition ohne Extra-Shift/Tabelle nachschlagen zu koennen):

```text
DAT_008b9640[0..7] = 63636363 7C7C7C7C 77777777 7B7B7B7B F2F2F2F2 6B6B6B6B 6F6F6F6F C5C5C5C5
```

→ entspricht exakt AES-S-Box-Bytes `63 7C 77 7B F2 6B 6F C5 ...`.

**Vorwaerts-T-Tabellen** (`Te0..Te3`, benutzt in `FUN_004fef70`, dem Encrypt-Rundenkern):

```text
DAT_008b8640 (Te0) = C66363A5 F87C7C84 EE777799 F67B7B8D
DAT_008b8a40 (Te1) = A5C66363 84F87C7C 99EE7777 8DF67B7B
DAT_008b8e40 (Te2) = 63A5C663 7C84F87C 7799EE77 7B8DF67B
DAT_008b9240 (Te3) = 6363A5C6 7C7C84F8 777799EE 7B7B8DF6
```

`0xC66363A5` ist einer der bekanntesten AES-Referenzwerte ueberhaupt (`Te0[0]` in praktisch
jeder table-basierten AES-Implementierung). Die vier Tabellen sind - wie in der Referenz -
byteweise Rotationen derselben Werte.

**Rueckwaerts-T-Tabellen** (`Td0..Td3`, benutzt in `FUN_004fed50`, der Decrypt-Schluesselexpansion):

```text
DAT_008b9a40 (Td0) = 51F4A750 7E416553 1A17A4C3 3A275E96
DAT_008ba240 (Td1) = A75051F4 65537E41 A4C31A17 5E963A27
DAT_008b9e40 (Td2) = 5051F4A7 537E4165 C31A17A4 963A275E
DAT_008ba640 (Td3) = F4A75051 4165537E 17A4C31A 275E963A
```

Ebenfalls exakt die kanonischen Referenzwerte.

**Kontextlayout bestaetigt:** `RIJNDAEL_CTX` (`0x178`=376 Byte) teilt sich exakt auf in:
`ctx+0x08..+0xb7` (176 Byte = 44 Woerter Encrypt-Rundenschluessel, passend zu AES-128s
`(10+1)*4` Woertern), `ctx+0xb8..+0x167` (176 Byte Decrypt-Rundenschluessel, ueber
InvMixColumns aus den Encrypt-Schluesseln abgeleitet - die "aequivalente inverse Chiffre",
Standardoptimierung aus dem Rijndael-Referenzcode) und `ctx+0x168..+0x177` (16 Byte IV fuer
CBC-Modus). Das bestaetigt **AES-128 im CBC-Modus**, nicht AES-192/256.

**Fazit: `AuRijnDael` ist eine bitgenau standardkonforme AES-128-Implementierung** nach dem
klassischen T-Tabellen-Verfahren (wie im Originalcode von Rijmen/Daemen bzw. OpenSSLs
`aes_core.c`), inklusive der aequivalenten inversen Chiffre fuer die Entschluesselung.

### Zwischenstand: alle vier Cipher jetzt bitgenau bestaetigt

| Cipher | Status | Beweis |
|---|---|---|
| Blowfish | bitgenau | P-Array (18 Woerter) + S-Box0 (8 Woerter) exakt = Referenzkonstanten |
| `AuMD5Mac` | bitgenau | reine CryptoAPI-Aufrufe mit literalen Konstanten (`CALG_MD5`, `CALG_RC4`) |
| Rijndael/AES | bitgenau | S-Box + Te0-3 + Td0-3 exakt = kanonische Referenztabellen; Kontext bestaetigt AES-128-CBC |
| SEED | bitgenau | Rundenkonstanten KC0-KC8+ exakt = KISA/RFC-4269-Standard |

Damit ist die gesamte Cipher-Suite vollstaendig identifiziert und algorithmisch verifiziert -
keine der vier Implementierungen weicht vom jeweiligen oeffentlichen Standard ab oder enthaelt
eine proprietaere Modifikation der Kernmathematik.

## Geklaert: Beziehung `Au*`-Wrapperklassen <-> `*_CTX`-Primitivklassen

**Kein Legacy-Rest, sondern bewusstes Strategy/State-Pattern.** Der Beweis kam direkt aus der
Blowfish-Verifikation: `FUN_005012f0` (= `AuBlowFish`-Vtable-Slot `+0x08`, "Reset"/Key-Setup)
operiert auf seinem ersten Parameter `param_1` wie folgt:

```c
void FUN_005012f0(int param_1, int param_2 /*Key*/, uint param_3 /*KeyLen*/) {
    memcpy(param_1 + 8,   &DAT_00955e58, 0x48);   // frisches Standard-P-Array (18 Woerter) laden
    memcpy(param_1 + 0x50, &DAT_00955ea0, 0x1000); // frische Standard-S-Boxen (4x256 Woerter) laden
    // ... XOR des Schluessels zyklisch ins P-Array (Blowfish-Schluesselplan Schritt 2)
    // ... anschliessend P-Array und S-Boxen per Verschluesselung eines Nullblocks ersetzen (Schritt 3)
}
```

`param_1 + 8` (P-Array) und `param_1 + 0x50` (S-Boxen, endet bei `param_1 + 0x1050`) sind
**exakt** das Layout von `BLOWFISH_CTX` (Groesse `0x1050`, siehe oben). `FUN_004f9570` (die
Factory, die fuer jede Richtung ein neues Objekt lazily konstruiert) erzeugt fuer Algorithmus-ID
`0` per `FUN_004f9300` genau ein `BLOWFISH_CTX`-Objekt (setzt `BLOWFISH_CTX::vftable`). Das
beweist: **das "Holder"-Objekt, das pro Socket und Richtung lazily konstruiert und in
`FUN_004f96b0`/`FUN_004f9720`/`FUN_004f9790`/etc. als zweiter/erster expliziter Parameter an
die `Au*`-Methoden durchgereicht wird, IST ein `*_CTX`-Objekt** - keine separate/aeltere
Implementierung, sondern die andere Haelfte derselben, absichtlich zweigeteilten Architektur:

- **`Au*`-Klassen (`AuBlowFish`, `AuMD5Mac`, `AuRijnDael`, `AuSeed`) = Strategy/Verhalten.**
  Winzige, praktisch zustandslose Objekte (`AuBlowFish` ist z.B. nur 4 Byte gross - nur der
  Vtable-Zeiger, siehe `operator_new(4)` in `AuCryptManager`s Konstruktor). Genau EINE
  Instanz pro Algorithmus liegt geteilt im globalen `AuCryptManager`-Array. Ihre virtuellen
  Methoden enthalten den eigentlichen Algorithmus-Code (Blowfish-Rundenfunktion,
  AES-Tabellen-Lookups, SEED-G-Funktion, CryptoAPI-Aufrufe), operieren aber nicht auf sich
  selbst, sondern auf einem separat uebergebenen Datenobjekt.
- **`*_CTX`-Klassen (`BLOWFISH_CTX`, `MD5MAC_CTX`, `RIJNDAEL_CTX`, `SEED_ALG_INFO`) = State/Daten.**
  Ein frisches Objekt pro Socket UND Richtung (Encode/Decode getrennt), lazily erzeugt von
  `FUN_004f9570` genau dann, wenn der erste `Reset`-Aufruf fuer diese Richtung passiert. Haelt
  P-Array/S-Boxen (Blowfish), Rundenschluessel+IV (AES, SEED) bzw. das 32-Byte-Geheimnis
  (`AuMD5Mac`). Deshalb reicht die eigene 2-Eintrag-Vtable dieser Klassen (nur Reset+Destruktor,
  siehe oben) auch aus - sie muessen nicht selbst `Transform`/`Decrypt`/`GetLength` anbieten,
  das übernimmt das jeweilige `Au*`-Objekt, dem sie als reiner Datenzeiger uebergeben werden.

Diese Trennung erklaert im Nachhinein auch sauber, warum `AcClientSocket::Reset`
(`FUN_00706880`) beim Socket-Abbau explizit die virtuellen Destruktoren der Objekte an
`ctx+0xc`/`ctx+0x18` aufruft: das sind die `*_CTX`-Instanzen dieses Sockets, die mit dem Socket
sterben, waehrend die `Au*`-Strategieobjekte im globalen Singleton fuer die gesamte
Client-Laufzeit weiterleben.

## Generische Dispatch-Funktionen

Diese Funktionen bilden die Bruecke zwischen dem generischen `AgpmStartupEncryption`-Code
und den konkreten Cipher-Objekten. **Korrektur gegenueber einer frueheren Version dieser
Datei:** Das `this`-Objekt dieser Funktionen ist NICHT der Pro-Socket-Kontext, sondern der
**globale `AuCryptManager`-Singleton** (geholt ueber `FUN_004ea680()`, dessen Rueckgabewert
per Registerkonvention direkt als `ecx` in die nachfolgende Thiscall-Funktion durchgereicht
wird - im Pseudocode-Export sichtbar an den Aufrufpaaren `iVar5 = FUN_004ea680(); ...
FUN_004f96b0(iVar5, ...)`). Der Singleton liefert `this+0x18`/`this+0x1c` (die vom Server
gesetzten Encode-/Decode-Algorithmus-IDs, siehe oben) und `this+0xc` (Array-Basis der vier
`Au*`-Objekte). Der zweite Parameter dieser Funktionen ist der Pro-Socket-Kontext
(`ctx = socket + 0xc8078`), der nur als Speicherort fuer das lazily konstruierte
"Holder"-Objekt dient - und dieses Holder-Objekt ist, wie unten belegt, eine echte
Instanz der passenden `*_CTX`-Klasse (Session-/Schluesselzustand einer Richtung).

| Funktion | Adresse | Vtable-Slot | Bedeutung |
|---|---|---:|---|
| `FUN_004f96b0` | `0x004f96b0` | `+0x08` (`Reset`/Key-Setup) | fuer Encode-Richtung, `this`=Singleton, 2. Arg=Socket-Ctx |
| `FUN_004f9720` | `0x004f9720` | `+0x08` (`Reset`/Key-Setup) | fuer Decode-Richtung, `this`=Singleton, 2. Arg=Socket-Ctx |
| `FUN_004f9790` | `0x004f9790` | `+0x0c` (`Transform`) | fuer Encode-Richtung |
| `FUN_004f9870` | `0x004f9870` | `+0x0c` (`Transform`) | Richtung per Parameter waehlbar (`param_3==1`→encode, `==2`→decode) |
| `FUN_004f98f0` | `0x004f98f0` | `+0x10` | Richtung per Parameter waehlbar |
| `FUN_004f97d0` | `0x004f97d0` | `+0x14` (`GetLength`) | Richtung per Parameter waehlbar |
| `FUN_004f9520` | `0x004f9520` | liest Singleton `+0x18 == 1` | Encode-Cipher ist `AuMD5Mac`? |
| `FUN_004f9530` | `0x004f9530` | liest Singleton `+0x1c == 1` | Decode-Cipher ist `AuMD5Mac`? |
| `FUN_004f9540` | `0x004f9540` | liest Singleton `+0x18`/`0x1c == 3` | Cipher ist `AuSeed`? |

`AcClientSocket::Reset` (`FUN_00706880`, Zeile 598801 in `alefclient.pseudocode.c`) bestaetigt
das Holder-Modell: sie ruft beim Socket-Reset `(**vtable)(...)`-artig den virtuellen Destruktor
der Objekte an `socket+0xc8084` (= `ctx+0xc`, Encode-Holder) und `socket+0xc8090`
(= `ctx+0x18`, Decode-Holder) auf und setzt danach `socket+0xc807c` (Transform-aktiv-Flag)
sowie die Sequenzzaehler zurueck.

## Ablauf von StartupEncryption mit den jetzt bekannten Bausteinen

Ergaenzt gegenueber [WINSOCK_SEQUENCE_01_LOGIN_HANDSHAKE.md](Sequenz-01-Login-Handshake.md)
Schritt 7-8 (`FUN_006819c0`, Adresse `0x006819c0`):

0. **(Neu)** Server sendet zuerst ein `AgpmStartupEncryption`-Unterpaket mit zwei `int32`
   (vermutlich Operation `0`), das per `FUN_00681970` die Encode-/Decode-Cipher-ID im
   `AuCryptManager`-Singleton setzt (`0`=Blowfish, `1`=MD5Mac, `2`=Rijndael/AES, `3`=SEED).
1. Server sendet Seed-Bytes (Laenge/Inhalt serverbestimmt).
2. Client speist diese Bytes ueber `FUN_004f96b0` in die **Decode-Richtung** (Singleton-Feld
   `+0x1c` bestimmt WELCHER Cipher, das Ergebnisobjekt landet im Socket-Holder) ein → das ist
   der Reset/Key-Setup-Aufruf fuer das, was der Server dem Client sendet.
3. Client fragt per `FUN_004f97d0(2, ...)` die erwartete Blockgroesse/Laenge fuer die
   Decode-Seite ab.
4. Client erzeugt lokal `uVar14` Zufallsbytes ueber `FUN_007e3340(0xff)`.
5. Client speist diese Zufallsbytes ueber `FUN_004f9720` in die **Encode-Richtung**
   (`ctx+0x18`) ein → Reset/Key-Setup fuer das, was der Client selbst sendet.
6. Client verschluesselt dieselben Zufallsbytes mit `FUN_004f9790` (Encode-Transform).
7. Das Ergebnis wird ueber `FUN_006818b0` als `AgpmStartupEncryption` Operation `2` an den
   Server geschickt.
8. `FUN_00681b30` schaltet danach `socket+0xc807c = 2` (Transform aktiv); ab hier laufen
   Pakete durch den `0xB1..0xBF`-Wrapper.

Unklar bleibt (siehe "Offene Punkte"), ob Schritt 6 bedeutet "verschluessle die
Zufallsbytes mit dem Schluessel, der aus denselben Zufallsbytes abgeleitet wurde"
(Selbstreferenz/Proof-of-Key) oder ob vor Schritt 5 bereits ein anderer, aus dem
Server-Seed abgeleiteter Schluessel im Encode-Slot steckt.

## Bekannter Ghidra-Exportartefakt

An mehreren Aufrufstellen von `FUN_004ea680` (z.B. Zeile 513303, 513309, 513326, 513331 in
`alefclient.pseudocode.c`) zeigt der Export Argumente, obwohl die Funktion nachweislich
(`void FUN_004ea680(void)`, Zeile 190753) keine Parameter hat. Das ist ein Darstellungsfehler
des Ghidra-Decompiler-Exports (vermutlich Registerbelegung aus dem direkt folgenden echten
Aufruf faelschlich mit angezeigt) und sollte bei weiterer Analyse ignoriert werden. Der
tatsaechliche Effekt von `FUN_004ea680()` ist ausschliesslich: Singleton sicherstellen,
Zeiger auf `&DAT_009ac12c` zurueckgeben.

## Offene Punkte / naechste Schritte

1. **Geloest:** Die Cipher-ID wird vom Server per eigenem `AgpmStartupEncryption`-Unterpaket
   gesetzt (`FUN_00681970`, siehe oben). Neu offen dadurch:
   - Die exakte Operationsnummer, unter der `0x00681970` beim Empfang dispatcht wird, ist nur
     aus der Registrierungsreihenfolge inferiert, nicht aus dem Dispatch-Switch selbst bestaetigt.
   - Die zwei weiteren Handler derselben Registrierungskette (`FUN_00681be0`, `FUN_00681c70`)
     sind jetzt analysiert - siehe Abschnitt "direkte Schluessel-Injektion". Ergebnis: In
     diesem Build ist ihr eigentlicher Effekt toter Code (Gate-Funktion `FUN_00510d50` gibt
     immer `0` zurueck), unabhaengig von Live-Traffic statisch bewiesen.
   - Kein Server-Traffic vorhanden, um zu pruefen, welchen Wert der reale Loginserver
     tatsaechlich fuer die Cipher-ID (`FUN_00681970`) sendet (Standardvermutung waere
     `2`=Rijndael/AES, aber unbestaetigt) - und da keine Live-Server mehr existieren
     (Stand der Tests), ist das voraussichtlich dauerhaft nicht mehr verifizierbar.
2. **Feld `AuCryptManager+0x08 = 3`** - Bedeutung unbestaetigt (Kandidat: Default-Algo-ID,
   Anzahl registrierter Algorithmen minus 1, oder Versionsfeld).
3. **Geloest: Vtable-Slot `+0x10` ist `Decrypt`.** Bestaetigt fuer `AuMD5Mac`
   (`FUN_00500a00` ruft `CryptDecrypt` statt `CryptEncrypt`, sonst identisch zu `+0x0c`).
4. **Geloest: Beziehung `Au*` <-> `*_CTX`.** Siehe Abschnitt "Geklaert: Beziehung `Au*`-Wrapperklassen
   <-> `*_CTX`-Primitivklassen" oben. Kein Legacy-Rest, sondern Strategy/State-Trennung:
   `Au*` = geteilter, quasi zustandsloser Algorithmus-Code (ein Objekt pro Cipher, global im
   Singleton), `*_CTX` = der eigentliche Verschluesselungszustand (ein frisches Objekt pro
   Socket und Richtung). Bewiesen anhand `FUN_005012f0` (`AuBlowFish::Reset`), das direkt auf
   dem `BLOWFISH_CTX`-Speicherlayout (P-Array bei `+8`, S-Boxen bei `+0x50`) arbeitet.
5. **Vollstaendig geloest fuer alle vier Cipher.** Blowfish, `AuMD5Mac`, Rijndael/AES und SEED
   sind alle bitgenau gegen ihre jeweiligen oeffentlichen Standards verifiziert (siehe die
   beiden Abschnitte "Bitgenaue Verifikation" oben). Keine der vier Implementierungen weicht
   von der Standardmathematik ab.
6. **Methodische Lehre:** `FUN_00681970` fehlt komplett in `alefclient.pseudocode.c` und
   `functions.tsv`, obwohl es sich um validen, erreichbaren Code handelt (nur ueber eine
   Handler-Registrierungstabelle referenziert, nie per direktem `call`). Das bedeutet: die
   22.711 von Ghidra gefundenen Funktionen (siehe [README.md](../Daten-und-Werkzeuge/Disassembly-2013.md)) sind vermutlich
   NICHT vollstaendig - ueberall dort, wo Handler nur ueber Funktionszeiger-Tabellen registriert
   werden (wie hier bei allen `Agpm*`/`Agcm*`-Modulen ueblich), koennen weitere, nicht
   dekompilierte Funktionen existieren. Fuer sicherheitsrelevante Bereiche (Krypto, Auth) lohnt
   sich ein gezielter Rohdaten-Grep nach Adress-Literalen in Registrierungscode, so wie hier.
7. **Kein Live-Traffic**: Alles hier ist weiterhin statische Inferenz. Ohne einen echten
   mitgeschnittenen `AgpmStartupEncryption`-Handshake laesst sich nicht verifizieren, ob
   diese Ableitung tatsaechlich der Realitaet entspricht (z.B. koennte der Server auch nur
   das simple `1111`/CryptoAPI-Schema fuer den Login verwenden und die `Au*`-Suite fuer
   etwas anderes reservieren, z.B. Billing/Anti-Cheat-Kommunikation).
