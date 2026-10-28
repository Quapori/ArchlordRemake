# Lückenplan: Spielablauf und Datenaustausch Client ↔ Server

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Übersichten und Karten](Index.md)*

Ursprünglicher Planstand (Ausgangslage): names_all264.tsv, 214 von 415 Modulen mit Bericht. Der Plan ist inzwischen ausgeführt; den aktuellen Stand nennt der nächste Abschnitt.

## Ergebnis der Abarbeitung (Stand names_all307)

**Der Plan wurde ausgeführt; die Zahlen in Abschnitt 1 sind die ursprüngliche Schätzung und enthalten einen Zählfehler** (Opcode-Zeilen der Paketberichte wurden als Lücken gezählt; die echte Zahl offener Quellmethoden lag bei etwa 4.100, nicht bei 651). Die gültigen Ergebnisse stehen in den Lückenregistern `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE3` und als Nachtrag am Ende jedes betroffenen Modulberichts.

| Status | Phase 1 (Netz) | Phase 2 (Welt) | Phase 3 (Spiel) |
|---|---:|---:|---:|
| zugeordnet | 705 | 14 | 24 |
| gemeinsamer Rumpf | 877 | 39 | 81 |
| nicht im Client (Beleg aus Quelle) | 885 | 192 | 52 |
| eingebaut | 440 | 54 | 47 |
| ohne Kandidat / nicht als eigene Funktion | 682 | 186 | 46 |
| Kandidat unbestätigt (nicht benannt) | 235 | 3 | 4 |

**Phase 4 (Oberfläche, Darstellung, Engine, Hilfsbibliotheken; 281 Klassen, 3.109 Lücken) wurde ebenfalls ausgeführt** (`ALEFCLIENT_2017_LUECKENREGISTER_PHASE4`): zugeordnet 362, gemeinsamer Rumpf 94, nicht im Client 537, eingebaut 738, ohne Kandidat / nicht als eigene Funktion 1.120, Kandidat unbestätigt 264. Davon sind etwa 230 Namen von Hand gegen Quelle und Dekompilat geprüft, der Rest automatisch.

**Verbesserung nach den Phasen:** Der Quellindex von `gapclose.py` löst jetzt `#define NAME "Text"`-Makros in Zeichenketten auf (dadurch fanden sich u. a. `AgpmSkill::SetSkillType` und `SetTooptipType`), und ein beschädigter regulärer Ausdruck (versehentliche Rückschritt-Zeichen statt ``) wurde repariert; die Konstantenwertung war vorher wirkungslos. Folge: der Backtest zeigt für die automatische Zuordnung jetzt 13 % falsche Treffer bei Schwelle 8 (vorher 0 %), deshalb werden Treffer seitdem nur noch von Hand geprüft übernommen. Außerdem listet [`ALEFCLIENT_2017_UNBENANNTE_FUNKTIONEN.md`](Unbenannte-Funktionen.md) die großen unbenannten Funktionen des Spiel- und Engine-Bereichs nach Nachbarklasse.

Vorgehen: Die automatische Zuordnung war zunächst bei Punktschwelle 8 mit „0 Fehlern“ im Backtest gemessen worden; diese Messung war wegen der wirkungslosen Konstantenwertung (siehe oben) falsch. Der korrigierte Backtest zeigt etwa 13 % falsche Treffer. Deshalb folgten drei Prüfrunden, in denen jeder Kandidat mit eindeutiger Adresse gegen Quelle und Dekompilat gelesen wurde (`gapclose.py kv`). Die verbleibenden Kandidaten (Phase 1: 235, Phase 2: 3, Phase 3: 4, Phase 4: 264) teilen sich eine Adresse mit mehreren Quellfunktionen, stehen auf Sprungstubs oder haben nur einen Einzelbeleg; sie bleiben bewusst unbenannt.

**Prüfung des Wikis (Stand dieser Seite):** Die Register führen eine Zuordnung nur noch dann als „zugeordnet“, wenn die Namenstabelle den Namen an dieser Adresse trägt (vorher blieben 72 Zuordnungen aus dem ersten Lauf im Register stehen, obwohl die Handprüfung sie verworfen oder umbenannt hatte; Phase 1: 725 → 705, Phase 4: 429 → 362 (nach der Einzelprüfung der automatischen Namen)). Treffer aus dem ersten Lauf sind als „automatischer Treffer … nicht von Hand geprüft“ gekennzeichnet. Einzelheiten: [`ALEFCLIENT_2017_WIKI_PRUEFUNG.md`](Wiki-Pruefung.md).


## 1. Ausgangslage in Zahlen

In den Berichten sind 4.736 von 6.812 Quellmethoden zugeordnet, **2.109 sind offen**. Davon gehören nicht alle zum Spielablauf:

| Gruppe | offene Methoden | Behandlung |
|---|---:|---|
| Spielablauf und Netzwerk (dieser Plan) | **651** in 64 Modulen | Phasen 1 bis 3 |
| Oberfläche (`AgcmUI…`, `AcUI…`, `AgcUI…`) | 657 | optional, Phase 4 |
| Darstellung (Render, Wasser, Gras, Schatten, Effekte, Schrift, Kamera u. a.) | 720 | nicht im Plan (kein Datenaustausch) |
| Editor- und Packer-Bibliotheken (`AuPackingManager`, `AuIniManagerA`) | 81 | nur Negativ-Einstufung mit Beleg |

Abgrenzung „Spielablauf/Datenaustausch“: (a) Module mit `OnReceive` (Paketverarbeitung), (b) Module der Weltdaten und der Verbindung (Karte, Objekte, Octree, Faktoren, Kampf, Raster, Wegsuche, Paketschicht, Verbindung, Sperren) und (c) die Spiel-Client-Module (Gegenstände, Fertigkeiten, Handel, Auktion, Gilde, Quest, Ereignis-NPCs usw.).

### Phase 1 – Netzwerkmodule (17 Module, 39 Lücken)
| Modul | Methoden | offen | zugeordnet |
|---|---:|---:|---:|
| [`AgcmPrivateTrade`](../Module/AgcmPrivateTrade.md) | 54 | 11 | 79 % |
| [`AgpmWantedCriminal`](../Module/AgpmWantedCriminal.md) | 20 | 8 | 60 % |
| [`AgpmGuild`](../Module/AgpmGuild.md) | 141 | 3 | 97 % |
| [`AgcmRecruit`](../Module/AgcmRecruit.md) | 36 | 2 | 94 % |
| [`AgpmEventGuide`](../Module/AgpmEventGuide.md) | 7 | 2 | 71 % |
| [`AgpmSummons`](../Module/AgpmSummons.md) | 16 | 2 | 87 % |
| [`AgcmConnectManager`](../Module/AgcmConnectManager.md) | 10 | 1 | 90 % |
| [`AgpmAuction`](../Module/AgpmAuction.md) | 63 | 1 | 98 % |
| [`AgpmBuddy`](../Module/AgpmBuddy.md) | 22 | 1 | 95 % |
| [`AgpmChannel`](../Module/AgpmChannel.md) | 21 | 1 | 95 % |
| [`AgpmEventItemConvert`](../Module/AgpmEventItemConvert.md) | 8 | 1 | 87 % |
| [`AgpmEventSkillMaster`](../Module/AgpmEventSkillMaster.md) | 21 | 1 | 95 % |
| [`AgpmGuildWarehouse`](../Module/AgpmGuildWarehouse.md) | 18 | 1 | 94 % |
| [`AgpmOptimizedPacket2`](../Module/AgpmOptimizedPacket2.md) | 78 | 1 | 98 % |
| [`AgpmRefinery`](../Module/AgpmRefinery.md) | 10 | 1 | 90 % |
| [`AgpmRemission`](../Module/AgpmRemission.md) | 10 | 1 | 90 % |
| [`AgpmRide`](../Module/AgpmRide.md) | 11 | 1 | 90 % |

### Phase 2 – Weltzustand und Infrastruktur des Austauschs (17 Module, 435 Lücken)
| Modul | Methoden | offen | zugeordnet |
|---|---:|---:|---:|
| [`AgcmMap`](../Module/AgcmMap.md) | 146 | 80 | 45 % |
| [`ApmMap`](../Module/ApmMap.md) | 143 | 76 | 46 % |
| [`AgpmFactors`](../Module/AgpmFactors.md) | 126 | 63 | 50 % |
| [`AgcmOcTree`](../Module/AgcmOcTree.md) | 44 | 26 | 40 % |
| [`AgpmCombat`](../Module/AgpmCombat.md) | 51 | 26 | 49 % |
| `AuCryptManager` | 31 | 21 | 32 % |
| [`ApmObject`](../Module/ApmObject.md) | 54 | 20 | 62 % |
| `ApModule` | 56 | 19 | 66 % |
| `ApAdmin` | 35 | 18 | 48 % |
| [`AgpmGrid`](../Module/AgpmGrid.md) | 49 | 17 | 65 % |
| `ApLockManager` | 17 | 14 | 17 % |
| [`AgcmResourceLoader`](../Module/AgcmResourceLoader.md) | 48 | 13 | 72 % |
| [`AgcmTargeting`](../Module/AgcmTargeting.md) | 48 | 13 | 72 % |
| [`ApmOcTree`](../Module/ApmOcTree.md) | 40 | 13 | 67 % |
| [`AgpmPathFind`](../Module/AgpmPathFind.md) | 13 | 10 | 23 % |
| `AuPacket` | 14 | 4 | 71 % |
| `ApMutualEx` | 7 | 2 | 71 % |

### Phase 3 – Spiel-Clientmodule (30 Module, 177 Lücken)
| Modul | Methoden | offen | zugeordnet |
|---|---:|---:|---:|
| [`AgcmItem`](../Module/AgcmItem.md) | 199 | 65 | 67 % |
| [`AgcmSkill`](../Module/AgcmSkill.md) | 141 | 56 | 60 % |
| [`AgpmUnion`](../Module/AgpmUnion.md) | 10 | 6 | 40 % |
| [`AgcmAuction`](../Module/AgcmAuction.md) | 20 | 5 | 75 % |
| [`AgcmCashMall`](../Module/AgcmCashMall.md) | 10 | 3 | 70 % |
| [`AgcmEventGuild`](../Module/AgcmEventGuild.md) | 9 | 3 | 66 % |
| [`AgcmEventSkillMaster`](../Module/AgcmEventSkillMaster.md) | 11 | 3 | 72 % |
| [`AgcmEventTeleport`](../Module/AgcmEventTeleport.md) | 11 | 3 | 72 % |
| [`AgcmGuild`](../Module/AgcmGuild.md) | 71 | 3 | 95 % |
| [`AgcmQuest`](../Module/AgcmQuest.md) | 14 | 3 | 78 % |
| [`AgcmSiegeWar`](../Module/AgcmSiegeWar.md) | 36 | 3 | 91 % |
| [`AgpmEventNPCTrade`](../Module/AgpmEventNPCTrade.md) | 9 | 3 | 66 % |
| [`AgcmAdmin`](../Module/AgcmAdmin.md) | 9 | 2 | 77 % |
| [`AgcmArchlord`](../Module/AgcmArchlord.md) | 6 | 2 | 66 % |
| [`AgcmBillInfo`](../Module/AgcmBillInfo.md) | 6 | 2 | 66 % |
| [`AgcmEventBank`](../Module/AgcmEventBank.md) | 5 | 1 | 80 % |
| [`AgcmEventCharCustomize`](../Module/AgcmEventCharCustomize.md) | 4 | 1 | 75 % |
| [`AgcmEventGacha`](../Module/AgcmEventGacha.md) | 5 | 1 | 80 % |
| [`AgcmEventItemConvert`](../Module/AgcmEventItemConvert.md) | 5 | 1 | 80 % |
| [`AgcmEventItemRepair`](../Module/AgcmEventItemRepair.md) | 4 | 1 | 75 % |
| [`AgcmEventManager`](../Module/AgcmEventManager.md) | 7 | 1 | 85 % |
| [`AgcmEventNPCDialog`](../Module/AgcmEventNPCDialog.md) | 4 | 1 | 75 % |
| [`AgcmEventProduct`](../Module/AgcmEventProduct.md) | 6 | 1 | 83 % |
| [`AgcmEventQuest`](../Module/AgcmEventQuest.md) | 4 | 1 | 75 % |
| [`AgcmEventRefinery`](../Module/AgcmEventRefinery.md) | 4 | 1 | 75 % |
| [`AgcmEventSiegeWarNPC`](../Module/AgcmEventSiegeWarNPC.md) | 3 | 1 | 66 % |
| [`AgcmTuner`](../Module/AgcmTuner.md) | 5 | 1 | 80 % |
| [`AgcmWarInfo`](../Module/AgcmWarInfo.md) | 14 | 1 | 92 % |
| [`AgpmBattleGround`](../Module/AgpmBattleGround.md) | 5 | 1 | 80 % |
| [`AgpmResourceInfo`](../Module/AgpmResourceInfo.md) | 5 | 1 | 80 % |

## 2. Warum die Lücken nicht „einfach“ zu schließen sind

Eine offene Methode hat nach der bisherigen Arbeit fast immer einen von vier Gründen: (1) die Funktion ist im Binary eingebaut (inline) und hat keine eigene Adresse, (2) sie wurde vom Linker entfernt, weil sie im Client nie gerufen wird (Editor, Server, Testcode), (3) sie existiert, wurde aber noch nicht zugeordnet, (4) das Binary weicht von der Quelle ab. Nur (3) lässt sich durch Benennen schließen; (1), (2) und (4) schließt man durch einen **Beleg**. Ziel des Plans ist deshalb, jede der 651 Methoden in genau eine der Klassen **zugeordnet / eingebaut (Beleg) / nicht im Client (Beleg) / abweichend / offen** zu bringen, mit nachprüfbarem Beleg. Eine Quote von 100 % „zugeordnet“ ist nicht erreichbar und wird nicht versprochen.

## 3. Automatische Abarbeitung: Aufbau der Pipeline

Neues Werkzeug `gapclose.py` (mit Hilfsmodulen), das eine Lückenliste Stück für Stück abarbeitet. Jeder Schritt ist ein Skript; Entscheidungen mit Unsicherheit gehen in eine Prüfwarteschlange.

**Schritt 0 – Lückenliste.** Aus allen Berichten und `tu_<Modul>.json` wird `rea_export/gaps.json` erzeugt (Modul, Methode, Fassung, Quelldatei, Zeilen, Parameter, Stufe Netz/Welt/Spiel). Grundlage ist `rea_export/_gapscope.json`.

**Schritt 1 – Quellfakten je Methode.** Aufrufer in der Quelle (alle Module, klassifiziert als Client / Server `Agsm*` / Editor), Aufgerufene, Zeichenketten, Konstanten, Paketkennungen (`AGPMxxx_PACKET_…`), `#ifdef`-Schutz (`_DEBUG`, Server, Editor), virtuell ja/nein.

**Schritt 2 – Kandidaten im Binary.** Fünf unabhängige Quellen: (a) unbenannte Funktionen im Adressbereich des Moduls (`ftable.py`, auch Export-Lücken per capstone), (b) Aufrufsignatur: die bereits benannten Aufgerufenen wie in der Quelle, (c) Zeichenketten und Zahlenkonstanten, (d) Aufrufstelle: Der Quellaufrufer ist bereits zugeordnet und enthält einen sonst unerklärten Aufruf an dieser Stelle, (e) bei Paketfunktionen: Folge der `AuPacket::MakePacket`/`GetField`-Feldtypen gegen die Paketdefinition (`SetFieldType`-Listen).

**Schritt 3 – Bewertung.** Punktzahl aus (a) bis (e); automatisch übernommen wird nur ein **eindeutiger** Kandidat mit mindestens drei unabhängigen Belegen. Alles andere kommt in die Prüfwarteschlange.

**Schritt 4 – Prüfwarteschlange.** Je Kandidat werden Dekompilat und Quelle nebeneinander gelesen (manuell, je Modul). Ergebnis: bestätigt, verworfen oder „unklar“.

**Schritt 5 – Negativ-Einstufung mit Beleg.** Für Methoden ohne Kandidat: (i) *nicht im Client*, wenn alle Aufrufer in der Quelle Server-, Editor- oder Testmodule sind oder unter `#ifdef` fallen **und** in den Client-Aufrufern keine Aufrufstelle fehlt; (ii) *eingebaut*, wenn ein Aufrufer im Binary den Rumpf als Befehlsmuster enthält (Vergleich von Aufrufsignatur und Konstanten); (iii) sonst *offen* mit Angabe, was fehlt. Die Belege (Aufrufer, Adresse, Muster) landen im Bericht.

**Schritt 6 – Ausgabe.** `gm_<Modul>.tsv` (vor jedem Lauf gesichert; `graphmatch.py` wird **nicht** mehr benutzt, weil es diese Dateien überschreibt), neue `names_allN.tsv`, `extras_<Modul>.json` (Gründe je Methode), Neuaufbau der Berichte, Funktionskarte, Modulübersicht und Wiki.

**Schritt 7 – Qualitätsschranken** je Modul vor dem Übernehmen: keine Namenskollision, kein Überschreiben eines geprüften Namens ohne Korrekturvermerk, Wiki ohne kaputte Links, Zahlen im Bericht stimmen mit der Tabelle, ein Commit je Modul oder Modulgruppe.

## 4. Phasen und Reihenfolge

| Phase | Inhalt | Umfang | Ergebnis |
|---|---|---|---|
| 0 | Werkzeug bauen und an zwei Modulen testen (`AgpmGrid` ohne Aufrufstellen, `AgcmPrivateTrade` mit Paketfunktionen) | 1 Arbeitsphase | Pipeline, Prüfung der Trefferquote |
| 1 | Netzwerkmodule: alle `Send…`/`Make…Packet`/Rückruf-Lücken, danach Paketvollständigkeit (jedes im Client gesendete Paket hat eine zugeordnete Sendefunktion, jede Empfangsart eine Verteilung) | 17 Module, 39 Lücken | lückenlose Sende- und Empfangsseite je Protokollmodul |
| 2 | Weltzustand: `AgpmFactors`, `AgpmCombat`, `ApmObject`, `AgpmGrid`, `AgpmPathFind`, `ApmMap`, `AgcmMap`, `ApmOcTree`/`AgcmOcTree`, `AgcmTargeting`, `AgcmResourceLoader`, `ApModule`, `ApAdmin`, Sperren, `AuPacket`, `AuCryptManager` | 17 Module, 435 Lücken | Karte, Objekte, Faktoren und Kampfrechnung mit Beleg |
| 3 | Spiel-Clientmodule: `AgcmItem` (65), `AgcmSkill` (56), danach die 28 kleinen Ereignis-, Gilden- und Handelsmodule | 30 Module, 177 Lücken | Gegenstands-, Fertigkeits- und NPC-Ablauf |
| 4 (optional) | Oberflächenmodule, soweit sie Pakete auslösen ([`AgcmUIItem`](../Module/AgcmUIItem.md), [`AgcmUISkill2`](../Module/AgcmUISkill2.md), [`AgcmUICharacter`](../Module/AgcmUICharacter.md), [`AgcmUILogin`](../Module/AgcmUILogin.md)) | 657 Lücken | nur auf Anforderung |

## 5. Erwartete Ergebnisse und Aufwand (Schätzung, keine Zusage)

Aus den bisherigen Modulen: etwa ein Viertel bis ein Drittel der offenen Methoden ließ sich nachträglich zuordnen, der größte Teil wurde als eingebaut oder nicht im Client eingestuft. Für die 651 Lücken heißt das grob **150 bis 250 neue Zuordnungen**, **250 bis 350 Belege „eingebaut/nicht im Client“** und **50 bis 150 bleiben offen** (Abweichungen oder nicht entscheidbar). Aufwand: Phase 0 und 1 klein, Phase 2 am größten (ApmMap, AgcmMap, AgpmFactors), Phase 3 mittel.

## 6. Risiken

- Falsche Zuordnung durch Ähnlichkeit gleich gebauter Funktionen (Dreiergruppen wie Figur/NPC/Monster): nur eindeutige Treffer automatisch, Gruppen immer mit Aufrufstelle belegen.
- Der Beleg „nicht im Client“ beruht auf der EP8-Quelle; das 2017er Binary kann neuer sein (Abweichungen werden als solche geführt, nicht als „fehlt“).
- Einige Funktionen liegen in Export-Lücken (kein Dekompilat): sie werden nur mit Disassembly geprüft und entsprechend gekennzeichnet.

## 7. Festlegungen der Planung

Die Planung legte fest:

1. **Umfang:** Phasen 0 bis 3 (651 Lücken). Phase 4 (Oberfläche) bleibt außen vor.
2. **Arbeitsweise:** automatisch, mit Prüfwarteschlange; eindeutige Treffer ohne Rückfrage übernehmen.
3. **Reihenfolge:** ein Modul nach dem anderen.
4. **Versionierung:** ein Commit je Phase oder je Modulgruppe.
5. **Stoppregel:** nach jeder Phase ein kurzer Zwischenstand (Zahlen und auffällige Abweichungen); bei mehr als 10 % verworfenen Kandidaten in einem Modul wird angehalten.
