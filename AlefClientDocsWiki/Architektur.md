# Architektur des Clients

*Navigation: [Wiki-Start](README.md) · [Module – Index](Module/Index.md) · [Methodik](Methodik.md)*

Der Client folgt der Modulstruktur der EP8-Quelle (`Modules/AClient`, `Modules/APublic`, `Modules/AUtility`). Dieser Überblick fasst zusammen, was durch die Berichte belegt ist.

## Namenspräfixe

| Präfix | Bedeutung | Beispiele |
|---|---|---|
| `Agcm…` | Client-Modul (Spiellogik/Darstellung nur im Client) | [`AgcmCharacter`](Module/AgcmCharacter_Angriff.md), [`AgcmItem`](Module/AgcmItem.md), [`AgcmRender`](Module/AgcmRender.md), [`AgcmWater`](Module/AgcmWater.md) |
| `AgcmUI…` | Client-Oberfläche je Spielfunktion | [`AgcmUIMain`](Module/AgcmUIMain.md), [`AgcmUIItem`](Module/AgcmUIItem.md), [`AgcmUIManager2`](Module/AgcmUIManager2.md) |
| `Agpm…` | gemeinsames Modul (Daten und Paketformat, im Client und im Server genutzt) | [`AgpmCharacter`](Module/AgpmCharacter.md), [`AgpmItem`](Module/AgpmItem.md), [`AgpmSkill`](Module/AgpmSkill.md) |
| `Apm…` | gemeinsame Basismodule (Karte, Events, Octree) | [`ApmEventManager`](Module/ApmEventManager.md) |
| `Agc…`, `Ac…`, `AcUI…` | Client-Klassen unterhalb der Module (Fenster, Chat, Konsole) | [`AgcChatManager`](Module/AgcChatManager.md), [`AcUIGacha`](Module/AcUIGacha.md) |
| `Au…`, `Ap…` | Hilfsklassen und Basistypen (u. a. `AuCryptManager`, Netzwerk) | siehe [Transform-Cipher](Netzwerk/Transform-Cipher.md) |

## Lebenszyklus eines Moduls

Alle Module erben von einer gemeinsamen Modulbasis und werden von einem Modulmanager verwaltet. Belegt sind (Vtable-Slots in den Berichten, z. B. [`AgcmWater`](Module/AgcmWater.md), [`AgcmShrine`](Module/AgcmShrine.md), [`AgcmTargeting`](Module/AgcmTargeting.md)):

| Slot | Methode | Aufgabe |
|---:|---|---|
| 0 | Destruktor | – |
| 1 | `OnAddModule` | holt die Partnermodule per `GetModule("Name")` und meldet Callbacks an |
| 2 | `OnInit` | Initialisierung (viele Module: gemeinsamer `return TRUE`-Rumpf) |
| 3 | `OnIdle` | Takt pro Frame |
| 4, 5 | – | bei vielen Modulen der gemeinsame Rumpf `0x0067FAB0` |
| 6 | – | bei vielen Modulen der gemeinsame Rumpf `0x0067AC90` |
| 7 | `OnDestroy` | Aufräumen |

Die Zeiger auf Partnermodule liegen an festen Offsets von `this` (z. B. `+0xB98…`), siehe [Member-Offsets](Uebersichten/Member-Offsets.md).

## Zusammenspiel der Module

- **Callbacks**: Module melden sich mit `SetCallback…(CBxxx, this)` bei Partnermodulen an (z. B. `CBAddChar`, `CBRemoveChar`). Die Handler sind in den Berichten benannt; die `SetCallback…`-Einzeiler selbst sind per ICF zusammengefaltet (siehe [Methodik](Methodik.md)).
- **UI-Anbindung**: UI-Module registrieren beim Manager ([`AgcmUIManager2`](Module/AgcmUIManager2.md)) Funktionen, Anzeigen, Benutzerdaten, Ereignisse und Boolean-Werte unter festen Namen (`Func_…`, `DP_…`, `UD_…`, `Event_…`); die Layouts selbst kommen aus Dateien.
- **Netzwerk**: `Agpm…`-Module besitzen `OnReceive`-Schalter über Operationsbytes und `Make…`/`Send…`-Funktionen für Pakete; Verschlüsselung und Rahmenformat stehen unter [Netzwerk](Netzwerk/Index.md), die Anmeldung unter [Start und Login](Start-und-Login/Index.md).
- **Welt/Rendering**: Karte ([`AgcmMap`](Module/Index.md)), Octree ([`AgcmOcTree`](Module/AgcmOcTree.md)), Wasser ([`AgcmWater`](Module/AgcmWater.md)), Gras ([`AgcmGrass`](Module/AgcmGrass.md)), Schatten/LOD/PostFX; Details unter [Welt und Engine](Welt-und-Engine/Index.md).

## Wo suche ich was?

| Frage | Ort |
|---|---|
| Wie heißt die Funktion bei `0x00xxxxxx`? | [Funktionskarte](Uebersichten/Funktionskarte.md), dann der Bericht des Moduls |
| Wo liegt das Feld `this+0x…` eines Moduls? | [Member-Offsets](Uebersichten/Member-Offsets.md) |
| Welcher Operationscode gehört zu welchem Paket? | [Netzwerk – Index](Netzwerk/Index.md) |
| Wie lief der Login/Start im Test? | [Start und Login](Start-und-Login/Index.md) |
