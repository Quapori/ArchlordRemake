# Archlord UI Editor - Detaillierter Umsetzungsplan

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Daten, Auslese und Werkzeuge](Index.md)*

Stand: 2026-09-09

## 1. Zielbild

Es soll ein lokales Windows-Desktop-Tool entstehen, mit dem die UI-Dateien von
`alefclient.exe` visuell bearbeitet werden koennen. Der Schwerpunkt der ersten
Version ist ein WYSIWYG-naher Editor fuer Login-, Charakterwahl- und
Charaktererstellungsfenster. Spaeter soll derselbe Editor auch die Ingame-UI
bearbeiten koennen.

Der Editor arbeitet ohne Patch am Client-Binary. Er liest die vorhandenen
verschluesselten UI-Konfigurationen, zeigt sie auf einer frei waehbaren
Arbeitsflaeche an und kann eine geaenderte Konfiguration erst auf einen
expliziten Export wieder RC4-kodiert zurueckschreiben.

Die wichtigste Sicherheitsregel lautet:

> Der Editor bearbeitet immer eine Arbeitskopie. Ein Schreiben nach
> `C:\Spiele\Archlord\ini\` ist ein separater, bestaetigter Exportschritt mit
> automatischem Backup.

## 2. Ausgangslage und bekannte Formate

### 2.1 UI-Konfiguration

Die UI liegt in diesen verschluesselten Dateien:

- `C:\Spiele\Archlord\ini\ui_1024x768.ini`
- `C:\Spiele\Archlord\ini\de\ui_1024x768.ini`

Sie werden mit dem bestaetigten CryptoAPI-Verfahren entschluesselt:

- Key: ASCII `1111`
- MD5 -> RC4-Schluesselableitung via `CryptDeriveKey`
- RC4-Decrypt beim Lesen, RC4-Encrypt beim Schreiben

Die vorhandene `tools\decode_archlord_data.ps1` implementiert diesen Vorgang
bereits und kann als Referenz fuer eine native Implementierung dienen.

Die entschluesselte Datei enthaelt 210 Sektionen. Jede Sektion beginnt mit
`[Name]`; wichtige UI-Eigenschaften sind unter anderem:

```ini
Pos=516,444
Size=250,162
UIPos=0:516,444
Texture=1:LG_IDPass_Main.png
CtrlName=CT_LG_MAIN
CtrlParent=CT_LG_MAIN
CtrlDisplay=1:Text
CtrlFont=0:-1:1.000000:1:0:0:0
```

### 2.2 Besondere Parserregel: `CtrlParent`

`CtrlParent` gehoert semantisch zum **folgenden** `CtrlType`-/`CtrlName`-Block,
nicht zum vorhergehenden. Der Parser darf die Datei deshalb nicht als
herkoemmliches INI-Format mit frei stehenden Key-Value-Paaren behandeln.

Beispiel:

```ini
CtrlName=CONTROL_8884
...
CtrlParent=CONTROL_8884
CtrlType=3:.
CtrlName=CONTROL_20458
```

`CONTROL_20458` ist ein Child von `CONTROL_8884`.

### 2.3 UI-Bildressourcen

Die Bilder sind im virtuellen Archiv abgelegt:

- `C:\Spiele\Archlord\texture\ui\Reference.Dat`
- `C:\Spiele\Archlord\texture\ui\Data.Dat`

`Reference.Dat` ist mit demselben Key `1111` verschluesselt. Nach dem
Entschluesseln liefert es pro Datei Name, Offset und Groesse. Das UI-Archiv
enthaelt 1.244 Dateien, davon 1.243 PNG-Dateien und eine BMP-Datei, mit rund
108,5 MB virtueller Nutzlast.

Das Tool kann die benoetigten Bilder on demand aus `Data.Dat` lesen; ein
vollstaendiges Entpacken in die Spielinstallation ist nicht noetig.

### 2.4 Aufloesungsprofile

Der Client kennt aktuell drei interne Profilindizes:

| Index | Historisches Zielprofil |
|---:|---|
| 0 | 1024x768 |
| 1 | 1280x1024 |
| 2 | 1600x1200 |

Der Client waehlt fuer Hoehen von 1024 bis 1199 Profil 1. Daher verwendet
1920x1080 ohne Binary-Patch ebenfalls Profil 1. Die Namen `_1280` muessen fuer
dieses Vorgehen beibehalten werden; der Editor darf sie nur auf expliziten
Wunsch umbenennen.

## 3. Empfohlene technische Architektur

### 3.1 Produktform

Empfehlung: eigenstaendige Anwendung `AlefUiEditor` mit:

- Tauri 2 als Desktop-Container und Rust-Backend
- React + TypeScript fuer die Bedienoberflaeche
- Konva oder PixiJS fuer die Canvas-Szene und Drag-and-drop
- Rust-Crates fuer Binario, RC4, Archivzugriff und sicheren Dateiexport

Diese Kombination ist sinnvoll, weil der Editor eine dichte, interaktive
Canvas-Oberflaeche braucht, waehrend das Backend sicher auf lokale Binaer- und
Konfigurationsdateien zugreifen muss. Das vorhandene Rust-Workspace
`AlefLogin` ist ein guter Ort fuer wiederverwendbare Rust-Hilfscrates, der
Editor sollte aber ein eigenes Desktop-Projekt bleiben.

Alternative fuer eine rein native Oberflaeche: Rust + `egui`. Diese Alternative
hat weniger Web-Tooling, bietet aber weniger Komfort fuer komplexe Canvas-
Interaktionen, Baumansichten, Inspector-Panels und Bildbearbeitung.

### 3.2 Projektstruktur

Vorgesehene Struktur:

```text
AlefUiEditor/
  src-tauri/
    src/
      archive.rs          # Reference.Dat + Data.Dat lesen
      crypto.rs           # 1111/RC4-Encode und Decode
      document.rs         # UI-Dokument laden, speichern, diffen
      ini_ui_parser.rs    # zustandsbehafteter UI-Parser/Serializer
      model.rs            # gemeinsame serialisierbare Datenmodelle
      export.rs           # Backup, atomarer Export, Verifikation
      commands.rs         # Tauri-API fuer Frontend
  src/
    app/
      App.tsx
      routes.tsx
    model/
      uiDocument.ts
      selection.ts
      undo.ts
    components/
      CanvasViewport.tsx
      UiNodeRenderer.tsx
      HierarchyTree.tsx
      PropertyInspector.tsx
      TextureBrowser.tsx
      ProfileSelector.tsx
      ExportDialog.tsx
      DiffPanel.tsx
    styles/
  tests/
    fixtures/
```

## 4. Datenmodell

### 4.1 Verlustfreies Dokumentmodell

Das Dokumentmodell muss mehr speichern als nur bekannte Properties. Die Datei
enthaelt viele unvollstaendig verstandene Keys, mehrfach vorkommende Keys und
reihenfolgeabhaengige Daten. Der Export darf unbekannte Zeilen nicht verlieren
oder umsortieren.

Vorgeschlagenes Modell:

```text
UiDocument
  sourcePath
  locale
  lineEnding
  sections: UiSection[]
  originalBytesHash

UiSection
  name
  rawHeaderEntries: UiEntry[]
  controls: UiControl[]
  rawTrailingEntries: UiEntry[]

UiControl
  name
  type
  parentName: optional string
  entries: UiEntry[]
  sourceRange

UiEntry
  key
  value
  rawLine
  ordinal
```

Bekannte Eigenschaften erhalten zusaetzlich typisierte Views:

```text
Position { x, y }
Size { width, height }
UiPosition { profileIndex, x, y }
TextureLayer { stateIndex, fileName }
Color { rgb, alpha }
```

Die `entries` bleiben trotzdem die Quelle der Wahrheit. Eine UI-Aenderung
modifiziert nur die relevante Zeile und bewahrt die Reihenfolge aller anderen
Zeilen.

### 4.2 Hierarchieaufbau

Beim Parsen einer Sektion gilt:

1. Header bis zum ersten `CtrlType` lesen.
2. Eine temporaere `pendingParentName` speichern, wenn `CtrlParent` gelesen
   wird.
3. Beim naechsten `CtrlType` einen neuen Control-Block beginnen und den
   temporaeren Parent zuweisen.
4. Root-Controls haben keinen Parent.
5. Fehlende, doppelte oder zyklische Parents als Warnung markieren, nicht
   stillschweigend verwerfen.

Der Renderer nutzt die Parent-Hierarchie fuer absolute Canvas-Positionen:

```text
absolutePosition(child) = absolutePosition(parent) + child.localPosition
```

## 5. Bedienoberflaeche

### 5.1 Hauptlayout

Die Anwendung verwendet eine Arbeitsoberflaeche ohne verschachtelte Karten:

```text
+----------------------- Toolbar ------------------------------------+
| Datei | Sprache | Profil | Aufloesung | Zoom | Undo | Redo | Export |
+-------------+-------------------------------+----------------------+
| Hierarchie  |            Canvas             | Eigenschaften        |
|             |  Hintergrund + UI-Controls    | Position, Groesse,   |
| Fensterbaum |  Hilfslinien, Auswahl, Raster | Textur, Text, Parent |
+-------------+-------------------------------+----------------------+
| Status: Datei, Sektion, Auswahl, Koordinaten, Aenderungsstatus    |
+---------------------------------------------------------------------+
```

### 5.2 Canvas

Die Canvas zeigt die Zielaufloesung in echten logischen Pixeln und wird nur
ueber Zoom skaliert. Die Arbeitsflaeche darf nicht responsiv umbrochen werden;
so bleiben Koordinaten und Pixelbezug nachvollziehbar.

Funktionen:

- Profilgroesse waehlen, z. B. 1920x1080
- Zoom von 10 bis 800 Prozent
- Pan per mittlerer Maustaste oder Space+Drag
- Raster ein/aus, konfigurierbare Schrittweite
- Hilfslinien fuer Mitte, Kanten und ausgewaehlte Controls
- Sichtbarkeit einzelner Root-Controls und Gruppen umschalten
- Auswahlrahmen, Resize-Griffe und Parent-Pfad anzeigen
- Child-Controls optional isoliert oder mit Parent anzeigen
- Texturfehler klar markieren, aber Canvas weiter rendern

### 5.3 Hierarchiebaum

Der linke Bereich zeigt Sektion, Root-Controls und Child-Controls. Er braucht:

- Suche nach Abschnitt, `CtrlName`, Textur und sichtbarem Text
- Expand/Collapse
- Sichtbarkeit und Sperre pro Node
- direkte Auswahl im Canvas und im Baum in beide Richtungen
- Warnsymbol fuer fehlende Textur, fehlenden Parent oder Duplikatnamen

### 5.4 Property Inspector

Der rechte Bereich bearbeitet den aktuellen Node mit klaren Feldern:

- `Pos` X/Y mit Steppern
- `Size` Breite/Hoehe mit Steppern
- `UIPos` je Profilindex 0/1/2
- Parent als Dropdown mit Baumansicht
- `Texture=N:Dateiname` als Zustandsliste
- `CtrlDisplay`, `CtrlFont`, Farbe und Alpha
- rohe Eintragsliste fuer fortgeschrittene Bearbeitung

Alle numerischen Eingaben werden validiert. Ungueltige Werte werden nicht in
das Dokument uebernommen.

### 5.5 Texturbrowser

Der Texturbrowser liest Dateinamen aus dem UI-Archiv, erzeugt kleine
Thumbnail-Caches ausserhalb des Spielordners und bietet:

- Suche nach Dateiname
- Filter nach PNG/BMP, Groesse und Namenspraefix
- Vorschau der Originalgroesse
- Anzeige, welche Controls die Textur aktuell verwenden
- Auswahl einer Textur fuer den aktiven Layer

Die erste Version veraendert keine `Data.Dat`- oder `Reference.Dat`-Archive.
Sie kann ausschliesslich vorhandene Texturen referenzieren.

## 6. WYSIWYG-Genauigkeit

### 6.1 Was korrekt sichtbar sein soll

- Position, Groesse und Parent-Offset jedes Controls
- mehrere Texturzustands-Layer
- Reihenfolge der Controls nach Quelldatei, soweit beobachtbar
- feste Pixelpositionen auf der gewaehlten Arbeitsflaeche
- einfache Texte, Farben und Alpha
- fehlende oder nicht passende Ressourcen

### 6.2 Was als Approximation markiert werden muss

- exakte FreeType-Schriftmetriken des Clients
- unbekannte Control-Typen
- Clientseitige Animationen und `AnimDefault`
- EventMap-Aktionen und Script-Callbacks
- dynamische Daten wie Charaktername, Serverliste oder Ladefortschritt
- komplexe Clipping-, Masken- und Blendregeln des RenderWare-Renderers
- Klickverhalten, solange es nicht im echten Client getestet ist

Die Vorschau darf daher den Status `Editor Preview` statt `Exact Game Render`
zeigen. Ein Export gilt erst nach Clienttest als bestaetigt.

## 7. Bearbeitungsfunktionen in Ausbaustufen

### Stufe A: Read-only Inspector

- verschluesselte Root- und DE-Datei laden
- alle 210 Sektionen anzeigen
- Hierarchie rekonstruieren
- Texturen aus `texture\ui` laden
- 1024-, 1280- und 1600-Profil anzeigen
- keine Schreibfunktion

Abnahmekriterium: Die sechs Loginfenster koennen mit den bekannten PNGs und
ihren Controls angezeigt werden.

### Stufe B: Sichere Layoutbearbeitung

- Drag-and-drop fuer `Pos`
- numerische Bearbeitung von `Pos`, `Size`, `UIPos`
- Mehrfachauswahl und Verschiebung
- Undo/Redo mit kommandobasiertem Verlauf
- Snap an Canvas-Mitte, Kanten, Raster und andere Controls
- lokale Arbeitsdatei `.alefui-workspace.json`

Abnahmekriterium: Ein Control kann verschoben, gespeichert, erneut geladen und
an derselben Position gerendert werden.

### Stufe C: Diff und Export

- Original gegen Arbeitskopie vergleichen
- geaenderte Sektionen, Controls und Properties anzeigen
- Exportziel klar anzeigen
- vor jedem Export Zeitstempel-Backup erzeugen
- in temporaere Datei kodieren
- temporaere Datei erneut dekodieren und gegen Arbeitsdokument vergleichen
- erst danach atomar in die Ziel-INI umbenennen

Abnahmekriterium: Ein Test-Export veraendert nur erwartete Zeilen; die
dekodierte Ausgabedatei ist parsebar und semantisch identisch mit der
Arbeitskopie.

### Stufe D: Profilwerkzeuge

- Profil 0, 1 und 2 vergleichen
- Sektion duplizieren
- Root-Controls per Ankerregel auf neue Canvasgroesse umsetzen
- Vorschlag fuer links/mitte/rechts und oben/mitte/unten anzeigen
- Aenderungen nur nach Nutzerbestaetigung uebernehmen

Abnahmekriterium: Die aktuelle 1280x1024-zu-1920x1080-Transformation ist im
Editor reproduzierbar, pruefbar und rueckgaengig machbar.

### Stufe E: Erweiterte Bearbeitung

- EventMap als lesbare Event-/Action-Ansicht
- Texttabellen (`uimessage.txt`, `sysstr.txt`) verknuepfen
- Control-Typ-spezifische Inspector-Panels
- UI-Zustandsvorschau fuer Buttons und Textur-Layer
- Import neuer Texturen in ein separates modifizierendes Archivprojekt

Neue Texturen und Archiv-Repacking bleiben bewusst nach der stabilen
Layoutbearbeitung, weil sie mehr Risiken als das reine INI-Editing bergen.

## 8. Export- und Backupstrategie

Vor jedem Live-Export:

1. Zielpfad auf `C:\Spiele\Archlord\ini\` validieren.
2. Originaldatei hashen und in einen zeitgestempelten Backupordner kopieren.
3. Arbeitsdokument verlustfrei serialisieren.
4. In eine Temporaerdatei RC4-kodieren.
5. Temporaerdatei dekodieren und erneut parsen.
6. Struktur, Sektionenzahl und erwartete geaenderte Properties vergleichen.
7. Ziel nur bei erfolgreicher Verifikation ersetzen.
8. Erfolg, Hashes und Backup-Pfad im Exportprotokoll zeigen.

Der Editor darf nie stillschweigend nach `Data.Dat`, `Reference.Dat` oder
`alefclient.exe` schreiben.

## 9. Tests

### Parser-Tests

- 210 Sektionen aus Root- und DE-Datei erkennen
- `CtrlParent` zum folgenden Control zuordnen
- unbekannte Zeilen und Wiederholungen verlustfrei erhalten
- Parse -> Serialize ohne Aenderung: Bytevergleich nach Decode
- absichtlich fehlende oder zyklische Parents mit Warnung behandeln

### Archiv-Tests

- `Reference.Dat` entschluesseln
- 1.244 UI-Eintraege erkennen
- bekannte Datei wie `LG_Base_1280.png` aus `Data.Dat` lesen
- PNG-Signatur und Bilddimensionen pruefen
- fehlende Texturen als sichtbare Platzhalter anzeigen

### Editor-Tests

- Root-Control verschieben und Child bleibt relativ
- Parent verschieben und Child bewegt sich auf Canvas mit
- Undo/Redo stellt exakte Werte wieder her
- Zoom aendert keine gespeicherten Koordinaten
- Multi-Select nutzt dieselbe Delta-Verschiebung

### Export-Tests

- nur die beabsichtigten `Pos`, `Size` und `UIPos`-Zeilen unterscheiden sich
- Backup existiert vor dem Ersetzen der Live-Datei
- fehlerhafter Re-Parse verhindert Export
- Export nach bereits umgebautem Profil verlangt bewusste Bestaetigung

### Clienttest-Matrix

| Test | Erwartung |
|---|---|
| 1024x768 | Profil 0 unveraendert |
| 1280x1024 | Profil 1, solange nicht umgebaut |
| 1920x1080 | umgebautes Profil 1 |
| 2560x1080 | aktuell ebenfalls Profil 1; kein natives Ultrawide-Ziel |
| DE-Datei | deutsche Textvariante und gleiche Geometrie |

## 10. Risiken und Gegenmassnahmen

| Risiko | Gegenmassnahme |
|---|---|
| INI-Parser verliert unbekannte Daten | verlustfreies Zeilenmodell und Roundtrip-Test |
| Falsche Parent-Zuordnung | spezialisierter Parser und Hierarchie-Tests |
| Vorschau weicht vom Client ab | klare Kennzeichnung, Exportdiff, Clienttest |
| Falsches Schreiben in Live-Datei | Arbeitskopie, Backup, atomarer Export |
| UI-Archiv sehr gross | on-demand Lesen, Thumbnail-Cache ausserhalb der Installation |
| Neue Texturen schwer repackbar | Repacking erst nach stabiler Layoutversion |
| Profil 1 trifft auch Ultrawide | Aufloesung im Editor klar anzeigen; spaeter eigener Binary-Patch oder separates Profil |

## 11. Empfohlene Reihenfolge

1. Rust-Parser und verlustfreies Dokumentmodell bauen.
2. UI-Archivleser und PNG-Vorschau bauen.
3. Read-only Login-Canvas mit Hierarchie und Inspector liefern.
4. Positionieren, Auswahl, Raster und Undo/Redo ergaenzen.
5. Diff, Backup und sicheren Export implementieren.
6. Den aktuellen 1920x1080-Loginumbau im Editor reproduzieren.
7. Erst danach EventMap, Texttabellen, Ingame-UI und neue Texturen angehen.

## 12. Definition of Done fuer Version 1

Version 1 ist fertig, wenn eine Person ohne manuelles Editieren der
verschluesselten INI-Datei folgende Aufgabe ausfuehren kann:

1. Root- oder DE-UI-Datei laden.
2. `UI_LG_CHARSELECT_1280` fuer 1920x1080 anzeigen.
3. Ein Root-Control und seine Child-Controls visuell identifizieren.
4. Das Root-Control pixelgenau verschieben.
5. Aenderung im Diff sehen und rueckgaengig machen.
6. Einen sicheren Export mit Backup erzeugen.
7. Die exportierte Datei erneut im Editor und danach im Client laden.
