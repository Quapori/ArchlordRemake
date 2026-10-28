# AgcmUIOption (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Modulanalyse des Client-Moduls `AgcmUIOption` (Spieloptionen: Grafik, Ton, Anzeige, Ablehnungsoptionen, `COption.ini`) im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat, Aufrufgraph und UI-Registrierung, EP8-Quelle `Modules/AClient/AgcmUIOption/AgcmUIOption.cpp`. Alle Adressen gelten nur für den 2017er Build.

## Kernbefund

- **Abdeckung:** 101 von 135 Quellmethoden sind zugeordnet; Grundlage sind die UI-Registrierungen (`CB…`), der Aufrufgraph (`Update…`) und Zeichenketten. Elf der Zuordnungen wurden gegen Dekompilat und Quelle gelesen; keine war falsch.
- **Ablehnungsoptionen:** Bitbelegung gleich der Quelle (siehe Tabelle); damit sendet der Client sie unverändert an den Server (Paket [`AgpmCharacter`](AgpmCharacter.md), Operation „Optionsflag“).
- **Abweichung:** `SaveToINI` speichert sieben in der Quelle vorgesehene Schlüssel nicht (`Bit`, `Fog`, `MapView`, `Sky`, `REF_GR`, `VH_TIP`, `VH_UCLIE`), der Lader liest sie weiterhin.
- **Nicht zugeordnet:** viele kleine `Update…`-Funktionen (z. B. `UpdateViewName*`, `UpdateFog`, `UpdateSky`), die im Binary in `UpdateGameOption`/`LoadFromINI` eingefaltet sind.

## Funktionskarte

Quellmethoden in Definitionsreihenfolge (`AgcmUIOption.cpp`) mit der Adresse im 2017er Binary. Die Reihenfolge im Binary weicht ab (die Funktionen liegen in Gruppen sortiert), die Zuordnung stützt sich auf den Aufrufgraphen, Zeichenketten und Registrierungen und wurde bei den „von Hand geprüft“ markierten Funktionen gegen das Dekompilat gelesen.

| # | Methode | Adresse | Größe | Beleg |
|---:|---|---|---:|---|
| 0 | `OnAddModule` | `0x005DEF80` | 6121 | vtable/String |
| 1 | `OnInit` | `0x005E0770` | 3197 | vtable/String |
| 2 | `OnDestroy` | `0x005DA7F0` | 25 | vtable/String |
| 3 | `OnIdle` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 4 | `AddOptionUserData` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 5 | `InitGameOption` | `0x005DDE80` | 379 | Aufrufgraph (geprüft) |
| 6 | `UpdateGameOption` | `0x005DE7B0` | 1551 | Aufrufgraph (geprüft) |
| 7 | `UpdateAutoTuning` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 8 | `UpdateSpeedTuning` | `0x005DE5B0` | 221 | Aufrufgraph (geprüft) |
| 9 | `UpdateDisableOtherPlayerSkillEffect` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 10 | `UpdateCharView` | `0x005DA810` | 219 | Aufrufgraph (geprüft) |
| 11 | `UpdateMapView` | `0x005DA8F0` | 379 | Aufrufgraph (geprüft) |
| 12 | `UpdateWideView` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 13 | `UpdateNature` | `0x005DE000` | 414 | Aufrufgraph (geprüft) |
| 14 | `UpdateNaturalObj` | `0x005DAA70` | 117 | Aufrufgraph (geprüft) |
| 15 | `UpdateLensFlare` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 16 | `UpdateFog` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 17 | `UpdateSky` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 18 | `UpdateWater` | `0x005DAB00` | 187 | Aufrufgraph (geprüft) |
| 19 | `UpdateShadow` | `0x005DE1A0` | 303 | Aufrufgraph (geprüft) |
| 20 | `UpdateShadowChar` | `0x005DABC0` | 199 | Aufrufgraph (geprüft) |
| 21 | `UpdateShadowSelf` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 22 | `UpdateShadowObject` | `0x005DACA0` | 156 | Aufrufgraph (geprüft) |
| 23 | `UpdateEffect` | `0x005DE2E0` | 371 | Aufrufgraph (geprüft) |
| 24 | `UpdateEffectField` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 25 | `UpdateCriminal` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 26 | `UpdateWanted` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 27 | `UpdateMurderer` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 28 | `UpdateEffectCombat` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 29 | `UpdateEffectUI` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 30 | `UpdateEffectSkill` | `0x005DAD40` | 171 | Aufrufgraph (geprüft) |
| 31 | `UpdateBloom` | `0x005DADF0` | 783 | Zeichenkette |
| 32 | `UpdateAutoExposure` | `0x005DB100` | 275 | Zeichenketten/Konstanten (geprüft) |
| 33 | `UpdateMatEffect` | `0x005DB220` | 175 | Aufrufgraph (geprüft) |
| 34 | `UpdateAntiAliasing` | `0x005DB2D0` | 221 | Aufrufgraph (geprüft) |
| 35 | `UpdateImpact` | `0x005DE690` | 203 | Aufrufgraph (geprüft) |
| 36 | `UpdateBrightVal` | `0x005DB3B0` | 532 | Aufrufgraph (geprüft) |
| 37 | `UpdateBloomVal` | `0x005DB5D0` | 141 | Aufrufgraph (geprüft) |
| 38 | `UpdateBGMSoundEnable` | `0x005DB660` | 186 | Aufrufgraph (geprüft) |
| 39 | `UpdateBGMSoundVal` | `0x005DB720` | 167 | Aufrufgraph (geprüft) |
| 40 | `UpdateEffSoundEnable` | `0x005DB7D0` | 187 | Aufrufgraph (geprüft) |
| 41 | `UpdateEffSoundVal` | `0x005DB890` | 200 | Aufrufgraph (geprüft) |
| 42 | `UpdateEnvSoundEnable` | `0x005DB960` | 159 | Aufrufgraph (geprüft) |
| 43 | `UpdateEnvSoundVal` | `0x005DBA00` | 167 | Aufrufgraph (geprüft) |
| 44 | `UpdateUseEAX` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 45 | `UpdateSpeakerType` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 46 | `Update3DProvider` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 47 | `UpdateViewNameMine` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 48 | `UpdateViewNameMonster` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 49 | `UpdateViewNameGuild` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 50 | `UpdateViewNameParty` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 51 | `UpdateViewNameOthers` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 52 | `UpdateViewHelpBaloonTip` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 53 | `UpdateViewHelpBaloonChat` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 54 | `UpdateViewHelpUclie` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 55 | `UpdateViewSelfBars` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 56 | `UpdatePartyBuffIcon` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 57 | `UpdateViewHelmet` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 58 | `UpdateViewItem` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 59 | `UpdateUseNewSlot` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 60 | `CBLoginProcessEnd` | `0x005DEDC0` | 441 | Aufrufgraph (geprüft) |
| 61 | `CBAutoTuning` | `0x005DBAF0` | 87 | UI-Registrierung |
| 62 | `CBSpeedTuning` | `0x005DE760` | 34 | UI-Registrierung |
| 63 | `CBCharView` | `0x005DBB50` | 32 | UI-Registrierung |
| 64 | `CBMapView` | `0x005DBB70` | 32 | UI-Registrierung |
| 65 | `CBWideView` | `0x005DBB90` | 68 | UI-Registrierung |
| 66 | `CBNature` | `0x005DE470` | 68 | UI-Registrierung |
| 67 | `CBShadow` | `0x005DE4C0` | 68 | UI-Registrierung |
| 68 | `CBEffect` | `0x005DE510` | 68 | UI-Registrierung |
| 69 | `CBWater` | `0x005DBBE0` | 77 | UI-Registrierung |
| 70 | `CBBloom` | `0x005DBC30` | 225 | UI-Registrierung |
| 71 | `CBAutoExposure` | `0x005DBD20` | 77 | UI-Registrierung |
| 72 | `CBMatEffect` | `0x005DBD70` | 32 | UI-Registrierung |
| 73 | `CBAntiAliasing` | `0x005DBD90` | 32 | UI-Registrierung |
| 74 | `CBImpact` | `0x005DE790` | 32 | UI-Registrierung |
| 75 | `CBNaturalObj` | `0x005DBDB0` | 32 | UI-Registrierung |
| 76 | `CBLensFlare` | `0x005DBDD0` | 125 | UI-Registrierung |
| 77 | `CBFog` | `0x005DBE50` | 117 | UI-Registrierung |
| 78 | `CBSky` | `0x005DBED0` | 71 | UI-Registrierung |
| 79 | `CBShadowChar` | `0x005DBF20` | 32 | UI-Registrierung |
| 80 | `CBShadowSelf` | `0x005DBF40` | 117 | UI-Registrierung |
| 81 | `CBShadowObject` | `0x005DBFC0` | 32 | UI-Registrierung |
| 82 | `CBEffectField` | `0x005DBFE0` | 71 | UI-Registrierung |
| 83 | `CBCriminal` | `0x005DC030` | 116 | UI-Registrierung |
| 84 | `CBWanted` | `0x005DC0B0` | 116 | UI-Registrierung |
| 85 | `CBMurderer` | `0x005DC130` | 116 | UI-Registrierung |
| 86 | `CBEffectCombat` | `0x005DC1B0` | 71 | UI-Registrierung |
| 87 | `CBEffectUI` | `0x005DC200` | 71 | UI-Registrierung |
| 88 | `CBEffectSkill` | `0x005DC250` | 32 | UI-Registrierung |
| 89 | `CBBrightVal` | `0x005DC270` | 108 | UI-Registrierung |
| 90 | `CBBloomVal` | `0x005DC2E0` | 108 | UI-Registrierung |
| 91 | `CBBackgroundSoundEnable` | `0x005DC350` | 62 | UI-Registrierung |
| 92 | `CBBackgroundSoundVal` | `0x005DC390` | 108 | UI-Registrierung |
| 93 | `CBEffectSoundEnable` | `0x005DC400` | 62 | UI-Registrierung |
| 94 | `CBEffectSoundVal` | `0x005DC440` | 108 | UI-Registrierung |
| 95 | `CBEnvSoundEnable` | `0x005DC4B0` | 62 | UI-Registrierung |
| 96 | `CBEnvSoundVal` | `0x005DC4F0` | 108 | UI-Registrierung |
| 97 | `CBUseEAX` | `0x005DC560` | 96 | UI-Registrierung |
| 98 | `CBSpeakerType` | `0x005DC5C0` | 99 | UI-Registrierung |
| 99 | `CB3DProvider` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 100 | `CBViewNameMine` | `0x005DC6A0` | 116 | UI-Registrierung |
| 101 | `CBViewNameMonster` | `0x005DC720` | 116 | UI-Registrierung |
| 102 | `CBViewNameGuild` | `0x005DC7A0` | 114 | UI-Registrierung |
| 103 | `CBViewNameParty` | `0x005DC820` | 114 | UI-Registrierung |
| 104 | `CBViewNameOthers` | `0x005DC8A0` | 116 | UI-Registrierung |
| 105 | `CBViewHelpBaloonTip` | `0x005DC920` | 86 | UI-Registrierung |
| 106 | `CBViewHelpBaloonChat` | `0x005DC980` | 96 | UI-Registrierung |
| 107 | `CBViewHelpUclie` | `0x005DC9E0` | 96 | UI-Registrierung |
| 108 | `CBViewSelfBars` | `0x005DCA40` | 96 | UI-Registrierung |
| 109 | `LoadFromINI` | `0x005DCAA0` | 3361 | Zeichenketten/Konstanten (geprüft) |
| 110 | `SaveToINI` | `0x005D9970` | 2757 | Zeichenkette |
| 111 | `CBRefuseTrade` | `0x005DD7D0` | 91 | UI-Registrierung |
| 112 | `CBRefusePartyIn` | `0x005DD830` | 76 | UI-Registrierung |
| 113 | `CBRefuseGuildIn` | `0x005DD880` | 76 | UI-Registrierung |
| 114 | `CBRefuseGuildBattle` | `0x005DD8D0` | 76 | UI-Registrierung |
| 115 | `CBRefuseBattle` | `0x005DD920` | 76 | UI-Registrierung |
| 116 | `CBDisableSkillEffect` | `0x005DD970` | 77 | UI-Registrierung |
| 117 | `CBRefuseGuildRelation` | `0x005DD9C0` | 76 | UI-Registrierung |
| 118 | `CBRefuseBuddy` | `0x005DDA10` | 79 | UI-Registrierung |
| 119 | `CBVisiblePartyBuffIcon` | `0x005DDA60` | 93 | UI-Registrierung |
| 120 | `CBVisibleViewHelmet` | `0x005DDAC0` | 111 | UI-Registrierung |
| 121 | `CBVisibleViewItem` | `0x005DDB30` | 71 | UI-Registrierung |
| 122 | `CBUseNewSlot` | `0x005DDB80` | 89 | UI-Registrierung |
| 123 | `SendOptionFlag` | `0x005DA440` | 97 | von Hand geprüft |
| 124 | `CBDisplay3DProvider` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |
| 125 | `CBDisableOtherPlayerSkillEffect` | `0x005DDBE0` | 113 | UI-Registrierung |
| 126 | `CBSettingCharacterOK` | `0x005DDC60` | 121 | cbalign:AgcmUIOption |
| 127 | `CBUpdateOptionFlag` | `0x005DE560` | 66 | cbalign:AgcmUIOption |
| 128 | `RefreshRefuseControl` | `0x005DDCE0` | 163 | von Hand geprüft |
| 129 | `RefreshRefuseControl` | `0x005DA4E0` | 185 | von Hand geprüft |
| 130 | `SendOptionFlag` | `0x005DA5A0` | 210 | von Hand geprüft |
| 131 | `CBSystemMessage` | `0x005DDD90` | 123 | cbalign:AgcmUIOption |
| 132 | `AddSystemMessageForSkillEffect` | `0x005DA680` | 102 | Aufrufgraph (geprüft) |
| 133 | `AddSystemMessageForOtherSkillEffect` | `0x005DA6F0` | 102 | von Hand geprüft |
| 134 | `SetCallbackChangeOptionUseNewSlot` | – | | nicht zugeordnet (eingefaltet, klein oder ohne eindeutigen Anker) |

101 von 135 Quellmethoden sind einer Binary-Adresse zugeordnet.

Weitere Funktionen des Moduls ohne Quellmethode: `AgcmUIOption` (`0x005D9530`), `RefreshRefuseControl_005da4e0` (`0x005DA4E0`), `SendOptionFlag_005da5a0` (`0x005DA5A0`), `~AgcmUIOption` (`0x005DA7C0`), `SetScreenContrast` (`0x005DDE20`), `SetScreenBrightness` (`0x005DDE40`), `SetScreenGamma` (`0x005DDE60`).

## Member-Offsets

| Offset | Member | Beleg |
|---|---|---|
| `0xBD8` | `m_pcsAgcmCharacter` | `+0x1596C` ist der Self-Character-Zeiger (`SendOptionFlag`) |
| `0xE08 … 0xE20` | `Ablehnungs-Flags (siehe Tabelle)` | `RefreshRefuseControl`, `SendOptionFlag` |
| `0xF60` | `Flag „sofort in INI speichern“` | `Update…Val`-Funktionen |
| `0xF64` | `Flag „Speichern erlaubt“` | `SaveToINI` |
| `Charakter +0x78C` | `m_lOptionFlag` | `SendOptionFlag` |

## Ablehnungs-Optionen (Charakter-Optionsflag)

Die Optionen „Handel/Gruppe/Gildenkampf/… ablehnen“ werden als Bits im Optionsfeld des Charakters (`+0x78C`) an den Server gesendet. Die Zuordnung ist aus `RefreshRefuseControl` (`0x005DDCE0`) und `SendOptionFlag` (`0x005DA5A0`) gelesen und stimmt mit `AGPDCHAR_OPTION_REFUSE_*` der EP8-Quelle überein:

| Bit | Option | Member in `AgcmUIOption` |
|---:|---|---|
| `0x01` | Handel ablehnen | `+0xE08` |
| `0x02` | Gruppeneinladung ablehnen | `+0xE0C` |
| `0x04` | Gildenkampf ablehnen | `+0xE14` |
| `0x08` | Kampf ablehnen | `+0xE18` |
| `0x10` | Gildeneinladung ablehnen | `+0xE10` |
| `0x40` | Gildenbeziehung ablehnen | `+0xE1C` |
| `0x80` | Freundesanfrage ablehnen | `+0xE20` |

`SendOptionFlag(int, bool)` (`0x005DA440`) setzt oder löscht ein einzelnes Bit am eigenen Charakter und sendet es mit `SendPacketOptionFlag` (`0x005A2170`); `SendOptionFlag()` baut aus den sieben Membern das gesamte Feld und sendet es. `RefreshRefuseControl(int)` liest das Feld aus dem Server-Paket zurück und aktualisiert die neun zugehörigen Userdata (`0x005DA4E0`).

## Optionsdatei Ini\COption.ini

`SaveToINI` (`0x005D9970`, 2757 Byte) schreibt, `LoadFromINI` (`0x005DCAA0`, 3361 Byte) liest die Datei `Ini\COption.ini` über `ApModuleStream` (Abschnitte `Patch_Option`, `Video_Option`, `Sound_Option`, `Option_Option`, `ETC_Option`). Jede `Update…`-Funktion speichert sofort, wenn das Speicher-Flag (`+0xF60`) gesetzt ist; `SaveToINI` kehrt ohne Schreiben zurück, wenn `+0xF64` gleich 0 ist.

Schlüsselvergleich: `LoadFromINI` enthält alle 77 Schlüssel der Quelle. In `SaveToINI` fehlen im Binary sieben Schlüssel, die die Quelle schreibt: `Bit` (Farbtiefe), `Fog`, `MapView`, `Sky`, `REF_GR`, `VH_TIP`, `VH_UCLIE`. Das Dekompilat ist vollständig (349 Zeilen), die Zeichenketten kommen im Binary nur im Lader vor; die Schlüssel werden also gelesen, aber nicht wieder gespeichert.

## Meldungstexte

`CBLoginProcessEnd` (`0x005DEDC0`) lädt nach dem Login die Texte `Option_Msg_NEAR`, `_NORMAL`, `_FAR`, `_ALL`, `_OFF`, `_ON`, `_LOW`, `_MEDIUM`, `_HIGH` aus dem UI-Meldungstext (`GetUIMessage`), ruft `LoadFromINI` und `UpdateGameOption`.

## Voreinstellungen (InitGameOption 0x005DDE80)

`InitGameOption` setzt die Optionswerte zurück (`+0xC6C … +0xCC4`, z. B. `+0xC8C`, `+0xC94`, `+0xC9C` auf 2 und `+0xC6C`, `+0xC74`, `+0xC84` auf 1) und wählt in Abhängigkeit von `+0xF74 == 1` eine Variante mit abweichenden Werten (`+0xC54 = 1`, `+0xC6C/0xC74/0xC84 = 0`, `+0xC9C = 1`). Die Bedeutung von `+0xF74` ist aus dem Dekompilat nicht ableitbar (vermutlich Region/Rechnerklasse).

## Abweichungen von der EP8-Quelle

- `SaveToINI` schreibt sieben Schlüssel der Quelle nicht (siehe oben).
- Ansonsten keine Abweichung in den gelesenen Funktionen.

## Grenzen

- Rund ein Viertel der Methoden (34 von 135) ist nicht zugeordnet, vor allem die kleinen `Update…`-Funktionen, die der Compiler eingefaltet hat.
- Die Bedeutung der Zahlenwerte der Grafikoptionen (Stufen) wurde nicht gegen die Quell-Enums abgeglichen.
- Der Befund zu `SaveToINI` beruht auf dem Zeichenkettenvergleich im Dekompilat; ein Aufruf über Zeiger auf anderswo abgelegte Schlüssel ist nicht ausgeschlossen.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 2, ohne Kandidat: 32, zugeordnet: 1.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `Update3DProvider` | 13 | `0x005DC630` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt Module:** [`AgpmCharacter`](AgpmCharacter.md)
- **Erwähnt in:** [`AgcmEventEffect`](AgcmEventEffect.md), [`AgcmTextBoardMng`](AgcmTextBoardMng.md), [`AgcmUIMain`](AgcmUIMain.md), [`AgcmUIStatus`](AgcmUIStatus.md), [`AgcmWater`](AgcmWater.md)
