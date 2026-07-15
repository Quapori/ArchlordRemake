# Archlord-Client-Textdateien — INI, TXT & XML: Aufbau, Funktion und Zusammenhang

Reverse-engineerte Notizen dazu, wie die losen Text-Konfigurationsdateien des Archlord-Clients (`.ini`, `.txt`, `.xml`) intern aufgebaut sind, wofür die einzelnen Dateifamilien da sind, und wie sie sich untereinander referenzieren. Wie die anderen Asset-Seiten beschreibt dies **nur Format und Struktur**, unabhängig von einer bestimmten Programmiersprache oder Implementierung. Baut auf [extraction.de.md](extraction.de.md) auf — dort steht, *wie* diese Dateien entschlüsselt/entpackt werden; dieser Text behandelt nur, was *in* ihnen steht, sobald sie als Klartext vorliegen.

## 1. Drei Endungen, aber nicht drei Formate

Die Dateiendung sagt fast nichts über den tatsächlichen Inhalt aus — sowohl `.ini` als auch `.txt` werden für mehrere, grundverschiedene Strukturen verwendet. Welches Format eine konkrete Datei nutzt, lässt sich nur am Inhalt erkennen, nicht am Namen:

| Format | Beispiel-Dateien | Erkennungsmerkmal |
|---|---|---|
| Klassisches INI | `grasstemplate.ini`, `waterstatust1.ini`, `worldmap.ini`, `teleportpoint.ini`, `skyset.ini`, `ArchlordColor.ini`, `uidatalist.ini` | `[Section]` + `Key=Value`; die Keys sind bereits die echten Feldnamen |
| Indiziertes ("Template"-) INI | `charactertemplateclient.ini`, `charactertemplateanimation.ini`, `charactertemplatepublic.ini`, `charactertemplatecustomize.ini`, `charactertemplateeventeffect.ini`, `itemtemplateentry.ini`, `ini/ItemTemplate/*.ini`, `objecttemplate.ini`, `effect/ini/new/<id>_eff.ini` | Ein Kopfblock vor der ersten `[Section]` bildet Positionsnummern auf Feldnamen ab; jede `[N]`-Sektion enthält `Position=Wert`-Zeilen |
| TSV-Tabelle (trotz `.txt`- oder sogar `.ini`-Endung) | `itemdatatable.txt`, `itemtooltip.txt`, `skill_*.txt`, `questtemplate.ini`, `questgroup.ini` | erste nicht-leere Zeile ist eine Tab-getrennte Kopfzeile, jede weitere Zeile eine Tab-getrennte Datenzeile |
| Sonderformate (Einzelfälle) | `growupfactor.txt`, `XlsTxtInfo.Txt` | eigene, dateispezifische Blockstruktur — siehe Abschnitt 3 |
| XML | lose `.xml`-Dateien im Client-Baum | siehe Abschnitt 4 — bislang nicht strukturell reverse-engineert |

Praktische Erkennungsreihenfolge: zuerst die wenigen namentlich bekannten Sonderfälle ausschließen, dann die erste nicht-leere Zeile prüfen — enthält sie ein Tabulatorzeichen und sieht *nicht* aus wie `Zahl=...`, ist es eine TSV-Tabelle; andernfalls wird die Datei als INI-Grammatik geparst (Abschnitt 2). Ohne diese Reihenfolge würde z. B. `questtemplate.ini` fälschlich als INI interpretiert, obwohl es eine Tabelle ist.

## 2. Die INI-Grammatik: eine Syntax, zwei Nutzungsarten

Jede Datei, die als INI erkannt wird, teilt sich dieselbe simple Grammatik:

- Leerzeilen sowie Zeilen, die mit `;` oder `#` beginnen, werden ignoriert.
- `[Name]` eröffnet eine neue Sektion.
- `Key=Value` innerhalb einer Sektion ist ein Feld dieser Sektion (Whitespace um `Key` und `Value` wird getrimmt).

Auf dieser einen Grammatik bauen zwei völlig unterschiedliche Nutzungsarten auf:

**a) Klassische Form.** Der Key *ist* bereits der Feldname. `waterstatust1.ini` enthält z. B. Sektionen wie `[WaterTextures]`, `[WaveTextures]` und `[Setting]` mit direkt lesbaren Keys. Ungewöhnlich dabei: eine einzelne Sektion kann mehrere logische Datensätze hintereinander enthalten, getrennt nicht durch weitere `[Section]`-Marker, sondern durch das wiederholte Auftreten eines "ID-artigen" Keys (z. B. `GRASS_ID=` in `grasstemplate.ini`, `ID=` in `waterstatust1.ini`). Jedes erneute Auftreten dieses Keys markiert den Beginn eines neuen Datensatzes innerhalb derselben Sektion — eine kompakte Art, eine kleine Tabelle in eine einzige Sektion zu packen.

**b) Indizierte ("Template"-) Form.** Vor der ersten `[Section]` steht ein Kopfblock, der Positionsnummern auf Feldnamen abbildet. Danach ist jede `[N]`-Sektion eine Datenzeile (meist nach einer numerischen TID benannt), deren Zeilen `Position=Wert` lauten — die Position muss erst über den Kopfblock aufgelöst werden, um zu wissen, welches Feld gemeint ist. Schematisch:

```
; Kopfblock — noch außerhalb jeder Sektion, bildet Position -> Feldname ab
0=TID
1=Name
2=DFF
3=DEFAULT_ARMOUR_DFF

; Datensätze — jede [N]-Sektion ist eine "Zeile"
[1042]
0=1042
1=Beispielname
2=1234567
3=0

[1043]
0=1043
2=2345678
```

Der Vorteil: Tausende nahezu identische Zeilen bleiben kompakt (keine wiederholten Feldnamen pro Zeile), sind aber trotzdem über den gemeinsamen Kopfblock selbstbeschreibend. Fehlt eine Position in einer Sektion (wie `1=` in `[1043]` oben), bleibt das Feld für diesen Datensatz einfach leer.

Bemerkenswert: Eine Datei ohne Kopfblock vor der ersten Sektion ist einfach die klassische Form — die Positions-Feldname-Abbildung ist dann leer, sodass jeder Key unverändert als sein eigener Feldname durchgereicht wird. Es handelt sich um dieselbe Grammatik mit zwei möglichen Ergebnissen, nicht um zwei getrennte Parser.

Zwei Dinge gelten für beide Formen:

- **Doppelte Keys werden nicht überschrieben.** Taucht ein Feldname (bzw. bei der indizierten Form: eine Position) innerhalb eines Datensatzes mehrfach auf, werden alle Werte als geordnete Liste gesammelt statt den vorherigen Wert stillschweigend zu ersetzen. Relevant z. B. bei wiederholten Effekt-Slots oder mehreren `FN`-Textureinträgen.
- **Keine deklarierte Kodierung.** Dateien liegen je nach Sprachversion in `utf-8-sig`, `cp949` (Koreanisch) oder Latin-1 vor; ohne BOM/Deklaration hilft nur eine Versuchskette dieser Kodierungen. Und: eine Datei mit `.ini`-Endung kann trotzdem noch RC4-verschlüsselt sein — das lässt sich nur durch einen Entschlüsselungsversuch plus Plausibilitätsprüfung feststellen (siehe [extraction.de.md § Lose Dateien](extraction.de.md#3-lose-dateien)).

## 3. TXT: meistens Tabellen, gelegentlich INI, selten Einzelfälle

Die meisten `.txt`-Dateien (`itemdatatable.txt`, `itemtooltip.txt`, `skill_const.txt`, `npcdialog.txt` usw.) sind schlichte TSV-Tabellen: erste Zeile = Tab-getrennte Spaltenköpfe, jede weitere Zeile ein Datensatz. Die erste Spalte enthält dabei üblicherweise die TID/ID des Datensatzes.

Manche `.txt`-Dateien nutzen stattdessen die indizierte INI-Grammatik aus Abschnitt 2b. `charactercustomizelist.txt` ist das Beispiel: der Kopfblock bildet Positionen auf Feldnamen wie `Type`, `Number`, `Sell Name`, `Case`, `CharacterTID`, `UseLevel`, `Price(Money)` und `Price(Skull)` ab; jede `[N]`-Sektion ist eine käufliche Charakter-Customization-Option, die über `CharacterTID` auf eine Charakter-Template-TID zurückverweist.

Zwei Dateien sind waschechte Einzelfälle mit eigener Blockstruktur:

- **`growupfactor.txt`** — wiederholte Blöcke: eine Zeile, die nur aus einer einzelnen Zahl besteht, eröffnet einen neuen Block für diese Charakter-TID; die nächste Zeile, die mit `LV` beginnt, ist die Spaltenkopfzeile für diesen Block; danach folgen Tab-getrennte Zeilen mit den Stat-Wachstumswerten pro Level für genau diese Charakter-TID — bis der nächste einzelne-Zahl-Marker den nächsten Block eröffnet.
- **`XlsTxtInfo.Txt`** — eine flache, kommagetrennte Manifestliste (Pfad, Byte-Größe, Zeilenanzahl, Spaltenanzahl je Quelltabelle). Sie beschreibt die *anderen* Textdateien (aus welcher Ursprungs-Tabelle sie exportiert wurden), ist selbst aber keine Spieldaten-Quelle.

`questtemplate.ini` und `questgroup.ini` sind der deutlichste Beweis dafür, dass man der Endung nicht trauen darf: Beide heißen `.ini`, sind inhaltlich aber TSV-Tabellen wie in Abschnitt 1 beschrieben.

## 4. XML — vorhanden, aber (noch) nicht reverse-engineert

Lose `.xml`-Dateien liegen im Client-Baum neben `.ini`/`.txt` und durchlaufen denselben Entschlüsselungs-oder-Klartext-Pfad wie diese (RC4 mit Passwort `"1111"`, Beibehaltung des Ergebnisses nur wenn es plausibel nach Klartext aussieht — führendes `<`, BOM usw. — siehe [extraction.de.md § Lose Dateien](extraction.de.md#3-lose-dateien)).

Anders als bei INI/TXT wurde bislang **keine interne XML-Struktur** für dieses Projekt reverse-engineert oder von einem der vorhandenen Tools inhaltlich geparst — jeder Extraktions- und Datenbank-Schritt im Projekt behandelt XML ausschließlich als undurchsichtigen Durchreich-Text (entschlüsseln/kopieren, nicht interpretieren). Dieser Abschnitt beschreibt also bewusst eine bekannte Lücke statt ein Format zu erfinden; sobald jemand konkrete `.xml`-Inhalte auswertet, gehört das Ergebnis hierher.

## 5. Wie die Dateien sich gegenseitig referenzieren

Keine einzelne Datei aus Abschnitt 1–3 steht für sich allein — fast der gesamte Wert dieser Ebene entsteht erst durch die Verweise zwischen den Dateien. Ein paar wiederkehrende Muster:

**a) Ein Datensatz, mehrere Dateien — der Charakter-Fall.** `charactertemplatepublic.ini`, `charactertemplateclient.ini`, `charactertemplateanimation.ini`, `charactertemplatecustomize.ini`, `charactertemplateeventeffect.ini` (sowie die Skill-Varianten) sind unabhängige indizierte INI-Dateien, die sich denselben `[TID]`-Sektionsraum teilen. Keine davon ist für sich vollständig — ein Charakter entsteht erst durch das Zusammenführen aller Dateien über dieselbe TID. Was die einzelnen Felder (`DFF`, `ANIMATION_NAME0`, `DEFAULT_FACE…`) konkret bedeuten und wie sie zu Dateinamen aufgelöst werden, steht in [meshes.de.md § 6](meshes.de.md) und [animation.de.md § 5](animation.de.md#5-wie-alles-zusammenhängt).

**b) Zweistufige Indirektion — der Item-Fall.** `itemtemplateentry.ini` bildet eine Item-TID nicht direkt auf Felder ab, sondern nur auf `TemplateName` und `TemplateFileName` — letzteres ein relativer Pfad auf eine zweite, ebenfalls indizierte INI-Datei unter `ini/ItemTemplate/`, in der die eigentlichen Felder (wieder unter derselben TID) stehen. Anders als beim Charakter-Fall (reine TID-Übereinstimmung über unabhängig benannte Dateien) führt hier ein Feldwert selbst auf den Dateinamen der zweiten Datei.

**c) Vorlage vs. platzierte Instanz — der Objekt-Fall.** `objecttemplate.ini` beschreibt, *was* ein Objekt ist (Mesh, Kollision, Event-Effekt) — einmal pro Objekt-TID. Für jeden Weltblock existiert daneben eine eigene `obj<blockid>.ini`, die dieselbe Block-Adressierung wie das Weltraster in [terrain.de.md § 1](terrain.de.md#1-welt-koordinatensystem) verwendet; jede Zeile darin ist eine platzierte Instanz (Position, Skalierung, Rotation, Octree-Referenzen), die über ein `tid`-Feld auf `objecttemplate.ini` zurückverweist. Dieselbe Trennung wie beim Charakter zwischen "Aussehen" und "Wo" — nur dass "Wo" hier pro Weltblock in einer eigenen Datei liegt statt in einem globalen Feld.

**d) Eine dritte Tabelle für "was passiert wann" — Event-Effekte.** Das Feld `AGCMEVENTEFFECT_EFFECT_DATA` (Aufbau: `slot:effect_id:offset_x:offset_y:offset_z:scale:parent_node_id:start_gap`) taucht unabhängig voneinander in `charactertemplateeventeffect.ini`, `objecttemplate.ini` und jeder Datei unter `ini/ItemTemplate/` auf. Keine dieser Dateien speichert einen Effekt-Asset-Dateinamen direkt — `effect_id` verweist stattdessen auf `effect/ini/new/<effect_id>_eff.ini`, selbst wieder eine indizierte INI mit den eigentlichen Effekt-Assets. Drei völlig unabhängige "Besitzer"-Kategorien (Charakter, Objekt, Item) laufen so über eine einzige, geteilte Effekt-Namensraum-Datei zusammen.

**e) TSV-Tabellen tragen den Fremdschlüssel als Spalte statt als Sektion.** Da TSV-Tabellen keine `[TID]`-Sektionen haben, steht die Referenz stattdessen in einer gewöhnlichen Spalte (`Tid`, `TID`, `CharTID` usw.). Die pro-Block-`CharTID`-Zeilen in `growupfactor.txt` etwa verweisen auf denselben TID-Raum wie `charactertemplatepublic.ini` — nur eben spaltenbasiert statt sektionsbasiert.

**f) Gemeinsamer Nenner: die numerische TID ist der universelle Fremdschlüssel.** Unabhängig davon, welches der vier Formate aus Abschnitt 1 eine Datei nutzt, ist der Verknüpfungsschlüssel über nahezu die gesamte Textdatei-Ebene hinweg dieselbe einfache Ganzzahl (oder ein Doppelpunkt-getrennter Wert, der eine solche enthält). Nichts auf dieser Ebene nutzt XML-artige verschachtelte Referenzen oder GUIDs — alles löst sich am Ende über flache numerische IDs auf, entweder in eine weitere `[Sektion]` oder eine weitere Tabellenzeile.

## 6. Praktischer Ablauf, um eine unbekannte Datei einzuordnen

1. Format am Inhalt bestimmen, nicht an der Endung: zuerst die wenigen namentlich bekannten Sonderfälle (`growupfactor.txt`, `XlsTxtInfo.Txt`) ausschließen, dann die Tab-in-erster-Zeile-Heuristik aus Abschnitt 1 anwenden.
2. Falls INI-Grammatik erkannt wurde: prüfen, ob vor der ersten `[Section]` bereits Zeilen stehen — falls ja, ist das der Positions-Feldname-Kopfblock (indizierte Form); falls nein, sind die Keys bereits die Feldnamen (klassische Form).
3. Das ID-Schema der Datei identifizieren (Sektionsnummer bei indiziertem INI, benannte ID-Spalte bei TSV) und diesem in die Datei/Tabelle folgen, die diese ID tatsächlich "besitzt", um die vollständige Information zusammenzusetzen (Abschnitt 5).
4. Doppelte Keys innerhalb eines Datensatzes als Werteliste behandeln, nicht als sich gegenseitig überschreibende Einzelwerte.
5. Mit einer Fallback-Kette dekodieren (`utf-8-sig`, `cp949`, Latin-1), da keine Datei ihre Kodierung deklariert — und im Zweifel prüfen, ob die Datei trotz Klartext-verdächtiger Endung noch RC4-verschlüsselt ist ([extraction.de.md § 1](extraction.de.md#1-drei-arten-gepackter-daten)).

Eine Referenzimplementierung dieses gesamten Prozesses existiert im Tooling des Projekts (siehe [../tools/](../tools/README.de.md)).

English version: [text-formats.md](text-formats.md)
