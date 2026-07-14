# Terrain Importer für Blender

Dieses Blender-Add-on ist dazu gedacht, Terrain-Daten aus JSON-Dateien in Blender zu importieren. Die Terrain-Daten werden aus JSON-Dateien geladen, die mit dem Tool im [Archlord-Repository](https://github.com/osiy1996/archlord) erstellt wurden. Diese JSON-Dateien enthalten Informationen über Terrain-Meshes, Texturen und UV-Zuordnungen, die in Blender importiert werden, um Terrain-Modelle zu erstellen.

## Funktionen

- Importiert Terrain-Daten aus JSON-Dateien.
- Generiert Materialien basierend auf den Texturdaten im JSON.
- Unterstützt mehrere UV-Karten (UVBase, UVAlpha1, UVColor1, UVAlpha2, UVColor2).
- Option, eine neue Blender-Datei mit dem importierten Terrain zu erstellen und zu speichern.
- Option zur Erstellung von kontinent-spezifischen Daten.

## Anforderungen

- Blender 3.6.0 oder höher.
- JSON-Dateien, die mit dem Tool aus dem [Archlord-Repository](https://github.com/osiy1996/archlord) erstellt wurden.
- Texturdateien (in Formaten wie `.png`, `.jpg`, `.tga` usw.), die mit dem Terrain verknüpft sind.

## Installation

1. Laden Sie dieses Repository herunter oder klonen Sie es.
2. Öffnen Sie Blender und gehen Sie zu `Edit > Preferences > Add-ons`.
3. Klicken Sie auf `Installieren...` und wählen Sie die `.zip`-Datei dieses Repositorys aus.
4. Aktivieren Sie das "Terrain Importer"-Add-on.

## Einrichtung

1. Nach der Aktivierung des Add-ons finden Sie die "Terrain Importer"-Einstellungen im "Properties"-Panel unter dem "Scene"-Tab.
2. Konfigurieren Sie die folgenden Einstellungen:
   - **Materialerstellung**: Aktivieren Sie diese Option, um Materialien für die Terrain-Objekte zu erstellen.
   - **Kontinent-Erstellung**: Aktivieren Sie diese Option, um kontinent-spezifische Terrain-Daten zu erstellen.
   - **Textur-Ordner**: Geben Sie den Ordner an, in dem Ihre Terrain-Texturen gespeichert sind.
   - **Blender-Speicherort**: Geben Sie den Ordner an, in dem die Blender-Dateien gespeichert werden.
   - **JSON-Ordner**: Geben Sie den Ordner an, in dem sich Ihre JSON-Dateien befinden.

## Nutzung

1. Stellen Sie sicher, dass sich die benötigten JSON-Dateien im Ordner befinden, der im "JSON-Ordner"-Einstellung angegeben ist. Diese Dateien sollten mit dem [Archlord-Tool](https://github.com/osiy1996/archlord) erstellt worden sein.
2. Klicken Sie auf den Button "Import Terrain", um die Terrain-Daten zu importieren. Das Add-on verarbeitet alle JSON-Dateien im angegebenen Ordner und erstellt die entsprechenden Terrain-Objekte in Blender.
3. Wenn "Materialerstellung" aktiviert ist, wird das Add-on Materialien basierend auf den Texturen aus den JSON-Dateien generieren.
4. Nach dem Import können Sie die Blender-Datei im angegebenen Zielordner speichern.

## Fehlerbehebung

- Wenn keine JSON-Dateien im Ordner gefunden werden, stellen Sie sicher, dass der Pfad korrekt ist und die Dateien ordnungsgemäß mit dem Archlord-Tool generiert wurden.
- Wenn Texturen fehlen, überprüfen Sie, ob sie im angegebenen Textur-Ordner vorhanden sind.

## Lizenz

Dieses Add-on ist unter der MIT-Lizenz lizenziert. Siehe LICENSE für weitere Details.
