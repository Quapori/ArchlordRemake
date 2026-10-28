# Leerer/flackernder Bildschirm nach erfolgreichem Start (UI-Aufloesungsproblem)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Start, Anmeldung und Login-Umgehung](Index.md)*

Stand: 2026-09-05

Ziel dieser Datei: dokumentieren, warum `alefclient.exe` nach Ueberwindung der
Start-/GameGuard-Sperren (siehe [CLIENT_LAUNCH_AUTH_MECHANISM.md](Startmechanismus.md))
zwar durchlaeuft, aber nur einen flackernden, bildlosen weiss-blauen Verlauf zeigt statt der
Login-Oberflaeche.

## Ausgangsbefund

Nach Anlegen von `NoExcuteAuth.arc` und `NotCheckGameGuard.arc` startet der Client jetzt
vollstaendig durch (Website- und GameGuard-Sperre beide erfolgreich umgangen), zeigt danach
aber nur einen flackernden Bildschirm ohne erkennbares UI - laut Beobachtung ein
weiss-blauer Verlauf.

## Live-Diagnosedaten aus dem tatsaechlichen Testlauf

Zwei vom Client selbst erzeugte/aktualisierte Dateien im Installationsverzeichnis
(`C:\Spiele\Archlord\`) geben direkten Aufschluss, ganz ohne weiteres Reverse Engineering
noetig:

1. **`ini\COption.ini`** (vom Testlauf aktualisiert) zeigt die tatsaechlich verwendete
   Grafikkonfiguration:

   ```ini
   [Patch_Option]
   Width=2560
   Height=1080
   Bit=32
   Windowed=0
   ```

   Der Client laeuft im **Vollbild auf 2560x1080** - einer Ultrawide-Aufloesung
   (Seitenverhaeltnis ca. 2,37:1), die es 2013 beim Release des Clients nicht gab.

2. **`eff2_ApMemoryLog_at_programexit.txt`** (Effekt-Allokationszaehler beim Programmende)
   zeigt fuer beide protokollierten Arbeitsphasen ausschliesslich `Cnt: 0, Max: 0, new: 0, del: 0`
   fuer saemtliche Effekt-/Partikel-/Licht-Klassen (`AgcdEffLight`, `AgcdEffParticleSystem`,
   usw.). Das bestaetigt: der Client kommt nie ueber die allerfrueheste Ladephase hinaus -
   es wurde noch nie auch nur ein einziges Spiel-Effektobjekt erzeugt.

## Der wahrscheinliche Kernbefund: hartkodiertes 1024x768-UI-Layout

`alefclient.pseudocode.c`, Zeile 12407, im sequenziellen Ladephasen-Code (Fortschrittsbalken-
Schleife beim Start):

```c
sprintf(acStack_60c, "Ini\\%sUI_1024x768.ini");
FUN_00630a50();
```

Das ist **wortwoertlich hartkodiert** - kein dynamisches "waehle UI-Datei passend zur
aktuellen Aufloesung"-System. Der `ini`-Ordner enthaelt auch nur genau diese eine Datei
(`ui_1024x768.ini`, ca. 2,2 MB, verschluesselt) - keine Varianten fuer andere Aufloesungen
oder Seitenverhaeltnisse.

Das bedeutet: Das komplette 2D-UI (Login-Fenster, Eingabefelder, Buttons) ist in
Referenzkoordinaten fuer eine 4:3-Flaeche von 1024x768 definiert und muss vom Client zur
Laufzeit auf die tatsaechliche Backbuffer-Aufloesung umgerechnet werden. Bei einer um Faktor
~1,78 anderen Seitenverhaeltnis-Relation (2,37:1 vs. 1,33:1) ist es plausibel, dass diese
Umrechnung bei so extremen Ultrawide-Werten fehlschlaegt oder UI-Elemente ausserhalb des
sichtbaren Bereichs bzw. mit falscher Skalierung platziert - waehrend die 3D-Hintergrundszene
(Himmel-/Ladebildschirm-Gradient) unbeeinflusst bleibt, weil deren Perspektivprojektion sich
automatisch an jedes Seitenverhaeltnis anpasst. Das erklaert das beobachtete Bild exakt:
sichtbarer Farbverlauf (3D-Hintergrund rendert), aber keinerlei UI-Elemente.

Die genaue Umrechnungs-/Skalierungsfunktion (vermutlich Teil von `FUN_00630a50` oder der
UI-Manager-Klasse dahinter) wurde noch nicht im Detail nachvollzogen - siehe "Offene Punkte".

## Empfohlener Test

In `C:\Spiele\Archlord\ini\COption.ini` unter `[Patch_Option]`:

```ini
Width=1024
Height=768
Windowed=1
```

(oder ueber die In-Game-Grafikoptionen vor dem naechsten Start entsprechend setzen) und
erneut starten. Bei Erfolg schrittweise zu hoeheren, aber **nicht-ultrawiden** Aufloesungen
wechseln (z.B. 1280x1024 4:3, oder 1920x1080 16:9 als Zwischenschritt), um die Grenze zu
finden, ab der die UI-Skalierung wieder versagt.

Zusaetzlich vorhanden, falls mehr Diagnose noetig ist: `AlefClientD.exe` im
Installationsverzeichnis ist eine **Debug-Version** (18 MB gegenueber 5,7 MB der
Release-`alefclient.exe`) und liefert vermutlich mehr Diagnoseausgaben/Assertions.

## Status

**Bestaetigt durch Praxistest.** Mit

```ini
[Patch_Option]
Width=1024
Height=768
Windowed=1
```

startet der Client durch und zeigt den Login-Bereich - die 1024x768-Ultrawide-Diskrepanz war
tatsaechlich die Ursache fuer den leeren/flackernden Bildschirm. Damit ist auch indirekt
bestaetigt, dass der Fehler an der UI-Koordinaten-/Skalierungslogik lag und nicht an
Vollbild-Exclusive-Mode-Problemen (`Windowed=1` allein waere sonst nicht ausreichend gewesen,
ohne auch die Aufloesung zu aendern - beides wurde hier zusammen geaendert, siehe Offene
Punkte).

## Offene Punkte

1. **Nicht separat getestet**, ob `Windowed=1` bei `Width=2560/Height=1080` allein schon
   geholfen haette (reines Vollbild-Exclusive-Mode-Problem) oder ob wirklich die Aufloesung
   die entscheidende Variable war - beide Werte wurden gleichzeitig geaendert. Falls der
   man spaeter zu einer hoeheren, nicht-ultrawiden Aufloesung wechseln moechte (z.B.
   1920x1080 16:9), waere das ein guter Zwischentest, um die genaue Grenze
   (Seitenverhaeltnis vs. reine Aufloesungshoehe) einzugrenzen.
2. **`FUN_00630a50`** (der UI-Ini-Parser/-Layoutaufbau) sowie die dahinterliegende
   Koordinaten-Skalierungslogik (Umrechnung von 1024x768-Referenzkoordinaten auf die reale
   Backbuffer-Groesse) wurden nicht im Detail analysiert - waere der naechste Schritt, falls
   auch niedrigere/normale Aufloesungen das Problem nicht beheben.
3. **Flackern** koennte zusaetzlich (oder stattdessen) mit Vollbild-Exclusive-Mode-Problemen
   von altem Direct3D 9 unter modernen Windows-Versionen (DWM/Compositor-Konflikte)
   zusammenhaengen, unabhaengig vom Aufloesungsthema - falls Fenstermodus allein schon hilft,
   waere das ein Hinweis darauf.
4. **`ui_1024x768.ini`** selbst wurde nicht entschluesselt/inspiziert - waere mit dem
   bekannten RC4-Schema ([`DATA_DECRYPTION_PROGRESS.md`](../Daten-und-Werkzeuge/Datenentschluesselung.md), Key `1111`) vermutlich moeglich und
   koennte zeigen, ob dort ueberhaupt Koordinaten fuer andere Seitenverhaeltnisse als 4:3
   vorgesehen sind.
