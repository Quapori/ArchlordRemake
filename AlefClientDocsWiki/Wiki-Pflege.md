# Wiki-Pflege

*Navigation: [Wiki-Start](README.md) · [Methodik](Methodik.md) · [Alle Seiten](Alle-Seiten.md)*

Hinweise zum Erweitern und Korrigieren dieses Wikis.

## Aufbau

- **Wurzel**: `README.md`, `Builds.md`, `Methodik.md`, `Architektur.md`, `Glossar.md`, `Wiki-Pflege.md`, `Alle-Seiten.md`.
- **Rubrikordner**: `Module/`, `Uebersichten/`, `Netzwerk/`, `Start-und-Login/`, `Welt-und-Engine/`, `Daten-und-Werkzeuge/`, `Formate-und-Werkzeugcode/`. Jede Rubrik hat eine `Index.md`.

## Neue Erkenntnis eintragen

1. Seite im passenden Rubrikordner anlegen (Modulberichte als `Module/<Modul>.md`, Paketfolgen als `Netzwerk/Sequenz-<NN>-<Thema>.md`).
2. Die Seite in der `Index.md` der Rubrik und in [Alle Seiten](Alle-Seiten.md) eintragen.
3. Relative Links auf `.md`-Dateien prüfen; kaputte Ziele vermeiden.

## Schreibregeln

- **Deutsch** ist die Hauptsprache. Sachlich und belegt schreiben.
- **Beleg nennen**: Jede Zuordnung nennt ihren Beleg (Zeichenkette, Vtable, Aufrufgraph, Paketfeld, Quelle). Vermutungen sind als solche gekennzeichnet; die Abschnitte „Abweichungen“ und „Grenzen“ nie weglassen.
- **Build angeben**: Adressen gelten nur für den genannten Build, siehe [Builds](Builds.md).
- **Adressen** als `0x00xxxxxx` in Backticks; Klassen und Methoden als `Klasse::Methode`.
- **Offen markieren**: Was nicht zugeordnet ist, mit Grund nennen (eingebaut, Werkzeugcode, Regionscode, Exportlücke, ICF-Stub).
- Keine Zugangsdaten, Schlüssel aus Live-Systemen oder private Pfade aufnehmen.
- Keine Gesprächs- oder Arbeitsprotokolle („wir“, „ich“, „der Nutzer“); Befunde im Passiv oder als Sachaussage formulieren.

## Prüfung

Vor der Veröffentlichung prüfen: alle relativen Links erreichbar, keine privaten Pfade, keine Ich-Form, jede Zahl und Adresse mit Beleg. Die letzte Prüfung beschreibt [Prüfung des Wikis auf Richtigkeit](Uebersichten/Wiki-Pruefung.md).
