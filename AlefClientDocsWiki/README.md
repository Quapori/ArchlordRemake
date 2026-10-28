# AlefClient Docs Wiki

Dokumentation aller Erkenntnisse über den Archlord-Client `AlefClient.exe`: Aufbau, Module, Netzwerkprotokoll, Verschlüsselung, Start/Login, Welt/Engine und die Zuordnung des Binarys zur EP8-C++-Quelle.

Das Wiki ist der zentrale Ort für alle bisherigen **und zukünftigen** Erkenntnisse. Wie man es erweitert, steht in der [Wiki-Pflege](Wiki-Pflege.md).

## Einstieg

| Ich will … | Seite |
|---|---|
| wissen, welche Client-Builds untersucht wurden | [Builds](Builds.md) |
| verstehen, wie die Zuordnung Binary ↔ Quelle funktioniert | [Methodik](Methodik.md) |
| den Aufbau des Clients (Modulschichten, Lebenszyklus) verstehen | [Architektur](Architektur.md) |
| Begriffe nachschlagen (ICF, vtable, Stub …) | [Glossar](Glossar.md) |
| ein bestimmtes Modul nachschlagen | [Module – Index](Module/Index.md) |
| die Gesamtkarte der benannten Funktionen | [Funktionskarte](Uebersichten/Funktionskarte.md) |
| wissen, welche Module noch keinen Bericht haben | [Modul-Übersicht](Uebersichten/Modul-Uebersicht.md) |
| Modulzeiger-Offsets (`this+0x…`) nachschlagen | [Member-Offsets](Uebersichten/Member-Offsets.md) |
| das Netzwerkprotokoll verstehen | [Netzwerk – Index](Netzwerk/Index.md) |
| wissen, wie der Client startet und sich anmeldet | [Start und Login – Index](Start-und-Login/Index.md) |
| Welt-, Shader- und Engine-Erkenntnisse | [Welt und Engine – Index](Welt-und-Engine/Index.md) |
| Datenentschlüsselung und Werkzeuge | [Daten und Werkzeuge – Index](Daten-und-Werkzeuge/Index.md) |
| Dateiformate und Editor-/Werkzeugcode aus der Quelle | [Formate und Werkzeugcode – Index](Formate-und-Werkzeugcode/Index.md) |
| alle Seiten auf einen Blick | [Alle Seiten](Alle-Seiten.md) |

## Rubriken

- [Module](Module/Index.md) – ein Bericht je Client-Modul/Klasse des 2017er Builds, mit Funktionsadressen, Offsets, Abweichungen von der Quelle und den Grenzen der Zuordnung.
- [Übersichten](Uebersichten/Index.md) – Funktionskarte (Gesamtstand und Methode), Modul-Übersicht, Member-Offsets.
- [Netzwerk](Netzwerk/Index.md) – Winsock-Beobachtungen, Paketfolgen je Spielfunktion (Login, Charakter, Items, Skills, Chat, Party, Handel, Quests, Monster …), Verschlüsselung.
- [Start und Login](Start-und-Login/Index.md) – Startmechanismus, kaputter Login-Callback-Pfad samt Workaround, UI-Probleme.
- [Welt und Engine](Welt-und-Engine/Index.md) – Weltdateien, Materialien, Shader, Octree, Wasser, Gras.
- [Daten und Werkzeuge](Daten-und-Werkzeuge/Index.md) – Entschlüsselung, Auslese-Roadmap, UI-Editor-Plan, Disassembly des 2013er Builds.
- [Formate und Werkzeugcode](Formate-und-Werkzeugcode/Index.md) – Dateiformate und Schreibcode aus der EP8-Quelle, mit Abgleich gegen das 2017er Binary (Start: [Karte: Sektordaten](Formate-und-Werkzeugcode/Karte-Sektordaten-Compact.md)).

## Stand

Die Zahlen (Anzahl Module, Abdeckung) stehen in [Module – Index](Module/Index.md). Gesicherte Aussagen und offene Punkte sind in jedem Bericht getrennt (Abschnitte „Kernbefund“, „Abweichungen“, „Grenzen“).

Grundregel dieser Dokumentation: nur belegen, was im Binary, in den Exporten oder in einem Live-Test nachgewiesen ist; Vermutungen sind als solche gekennzeichnet.
