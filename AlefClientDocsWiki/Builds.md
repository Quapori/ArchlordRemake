# Untersuchte Client-Builds

*Navigation: [Wiki-Start](README.md) · [Methodik](Methodik.md) · [Alle Seiten](Alle-Seiten.md)*

Es gibt zwei verschiedene `AlefClient.exe`-Builds im Projekt. Adressen und Funktionsnamen sind **nicht** zwischen ihnen übertragbar.

| | 2013er Build | 2017er Build (Hauptziel) |
|---|---|---|
| Linker-Zeitstempel (UTC) | 2013-04-02 08:01:38 | 2017-08-15 10:11:56 |
| SHA-256 | `F951E56DB985BA57FB9BA547FAD9984F9F21D5F3BB7367E58F22D6A84814B176` | `20009faa5db75de88ec09ae11324d479f85946b5ca37ad3c64ec4dcac29e067b` |
| PDB-Pfad im Binary | `D:\branch\Global\Release\Release_Global_Code\Bin\AlefClient.pdb` | `D:\Archlord\source_repos\branches\GB\Release\Alef\Bin\AlefClient.pdb` |
| Format | PE32, x86, Windows-GUI | PE32, x86, Windows-GUI |
| ImageBase | `0x00400000` | `0x00400000` |
| Datei-/Produktversion (Ressource) | 1.0.0.1 | 1.0.0.1 |
| Dokumentation | [Disassembly-2013](Daten-und-Werkzeuge/Disassembly-2013.md), ältere Netzwerk- und Welt-Berichte | alle Berichte unter [Module](Module/Index.md) und [Funktionskarte](Uebersichten/Funktionskarte.md) |

Beide Versionsressourcen tragen dieselbe Nummer 1.0.0.1; eine eigene Spiel- oder Episodenversion ist im Binary nicht festgestellt.

## Was für welchen Build gilt

- **Funktionsadressen, Offsets, Vtable-Slots** in den Berichten unter [Module](Module/Index.md), in der [Funktionskarte](Uebersichten/Funktionskarte.md) und in den [Member-Offsets](Uebersichten/Member-Offsets.md) gelten ausschließlich für den **2017er Build**.
- Die älteren Berichte (frühe Netzwerkfolgen, Weltdateien, Shader, Entschlüsselung) beschreiben den 2013er Build bzw. sind nicht auf einen Build festgelegt; der Erstbericht [Disassembly-2013](Daten-und-Werkzeuge/Disassembly-2013.md) bezieht sich ausdrücklich auf ihn. Vor der Übernahme einer Adresse immer prüfen, welcher Build gemeint ist.
- Quelle für den Abgleich ist die EP8-C++-Quelle (lokale Kopie der EP8-C++-Quelle); sie ist nicht identisch mit beiden Builds, Abweichungen stehen in den Berichten (Abschnitt „Abweichungen“).

## Hinweis zur Prüfung

Vor der Verwendung von Adressen aus den Berichten immer zuerst den SHA-256 der eigenen `AlefClient.exe` mit der Tabelle oben vergleichen. Eine abweichende Datei (anderer Hash) ist ein anderer Build, für den die Adressen nicht gelten.
