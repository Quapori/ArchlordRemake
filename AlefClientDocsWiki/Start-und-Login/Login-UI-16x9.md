# Profil 1 Login-UI: 16:9-Test und Ruecknahme

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Start, Anmeldung und Login-Umgehung](Index.md)*

Stand: 2026-09-09

## Ergebnis

Der erste Versuch, die vorhandenen `_1280`-Loginsektionen von `1280x1024`
auf `1920x1080` umzubauen, wurde zurueckgenommen. Die sichtbaren Controls
waren nach dem Umbau nicht mehr bedienbar.

Die Ursache ist das clientinterne Layoutverhalten: Bei einer Hoehe von 1080
waehlt der Client Profil `1` und zentriert dessen bestehende 1280er Flaeche
bereits. Das manuelle Erweitern der Root-Canvas und Verschieben der
Root-Controls hat daher Darstellungs- und Hit-Test-Koordinaten getrennt.

Der Screenshot vom 2026-09-09 zeigt genau diesen Zustand: Hintergrund und
Logo bleiben auf der zentrierten 1280er Flaeche, waehrend die Serverauswahl
zusaetzlich nach rechts verschoben wurde. Die sichtbaren Schaltflaechen
stimmen dadurch nicht mehr mit ihren Klickbereichen ueberein.

## Aktueller Installationszustand

Die beiden UI-Konfigurationen sind bytegleich aus ihren Originalbackups
wiederhergestellt:

- `C:\Spiele\Archlord\ini\ui_1024x768.ini`
- `C:\Spiele\Archlord\ini\de\ui_1024x768.ini`

Alle sechs Profil-1-Loginsektionen haben wieder `Size=1280,1024` und die
urspruenglichen Positionen:

- `UI_LG_IDPASSWORD_1280`
- `UI_LG_2D_1280`
- `UI_LG_CHARCREATE_1280`
- `UI_LG_CHARSELECT_1280`
- `UI_LG_Loading_1280`
- `UI_SelectServer_1280`

Der beim fehlerhaften Test vorhandene Zustand ist ebenfalls gesichert unter:

`C:\Spiele\Archlord\backup-ui-16x9-failed-layout-20260909-223500`

## Sicherungen

Die unveraenderten Ausgangsdateien liegen weiterhin hier:

- `C:\Spiele\Archlord\backup-ui-16x9-20260909-220418\ini\ui_1024x768.ini`
- `C:\Spiele\Archlord\backup-ui-16x9-20260909-220420\ini\de\ui_1024x768.ini`
- `C:\Spiele\Archlord\backup-ui-16x9-20260909-220418\ini\COption.ini`

## Aufloesungsauswahl

Die Auswahlfunktion des Clients verwendet bei `1080` Pixel Hoehe Profil `1`:

```c
if (height > 1199 && width > 1599) return 2;
if (height > 1023 && height < 1200) return 1;
return 0;
```

Die Funktion liegt bei `FUN_00409ea0` in
`alefclient.pseudocode.c` um Zeile 9672. Es ist deshalb kein Selektor-Patch
fuer 1920x1080 erforderlich.

`COption.ini` wurde vom laufenden Client beim Start wieder auf `1024x768`
geschrieben. Fuer einen erneuten Aufloesungstest darf sie erst gesetzt werden,
wenn `alefclient.exe` beendet ist. Danach muss sie vor dem Start lauten:

```ini
[Patch_Option]
Width=1920
Height=1080
Windowed=1
```

## Konsequenz fuer den weiteren Umbau

Die vorhandenen 1280er Texturen werden ohne neue Assets nicht zu einer echten
1920er Hintergrundflaeche. Ein funktionierender 16:9-Umbau braucht zuerst eine
Messung der clientinternen Koordinatentransformation. Root-Controls duerfen
nicht pauschal um den freien Platz verschoben werden.

`tools\rebuild_login_16x9.ps1` dokumentiert nur den verworfenen heuristischen
Ansatz. Es darf nicht erneut mit `-Mode apply` gegen die Live-Installation
ausgefuehrt werden.
