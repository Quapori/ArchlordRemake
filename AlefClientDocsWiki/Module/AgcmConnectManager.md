# AgcmConnectManager (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmConnectManager` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmConnectManager` / `AgcmConnectManager.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x006F5110` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Opcodes:** Quelle `AGCMCONNECTMANAGER_PACKET_OPERATION_*` kennt 4 Operationen, davon 3 mit eigenem Case im 2017er Binary; ohne Case: `CONNECT_ZONESERVER` (2).
- **Vergleich mit 2013:** Die 2013er Berichte enthalten für dieses Modul keine Callback-Ereignisse je Operation; ein Abgleich ist nicht möglich.
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`006f4d80`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x006F4D80` | `AgcmConnectManager::ctor_or_dtor_006f4d80` | merged |
| `0x006F4E60` | `AgcmConnectManager::ctor_or_dtor_006f4e60` | merged |
| `0x006F50F0` | `AgcmConnectManager::~AgcmConnectManager` | merged |
| `0x006F5110` | `AgcmConnectManager::OnReceive` | merged |
| `0x006F4EC0` | `AgcmConnectManager::Connect` | casemap:AgcmConnectManager |
| `0x006F5040` | `AgcmConnectManager::SendZoningResult` | casemap:AgcmConnectManager |

6 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | CHAR/1/1 | 6/6/6 | ja | ja |

**m_csPacket** (6 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT8 | 1 | operation |
| 1 | `0x2` | INT32 | 1 | character id |
| 2 | `0x4` | INT8 | 1 | operation  status |
| 3 | `0x8` | CHAR | 23 | zone server address (xxx.xxx.xxx.xxx:port) |
| 4 | `0x10` | INT32 | 1 | zone server ID |
| 5 | `0x20` | PACKET | 1 | character server data// not used |

## Opcode-Tabelle

| Op | Name | 2017-Handler | Ereignisse 2017 | Vergleich mit 2013 |
|---:|---|---|---|---|
| 1 | `SEND_ZONESERVER_ADDR` | `0x006F4EC0` `Connect` | – | keine Callback-Ereignisse (beide) |
| 2 | `CONNECT_ZONESERVER` | – | – | kein Case (default) – wie 2013 |
| 3 | `CONNECT_ZONESERVER_RESULT` | `0x006F5040` `SendZoningResult` | – | keine Callback-Ereignisse (beide) |
| 5 | `PASS_CONTROL` | inline | – | keine Callback-Ereignisse (beide) |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, nicht als eigene Funktion: 1, nicht im Client: 3, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `Disconnect` | 14 | `0x006F4F60` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `GetLoginServerNID` | 8 | `0x006F50D0` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SendZoningMessage` | 24 | `0x006F4FC0` | automatischer Treffer (erster Lauf), nicht von Hand geprüft; Aufrufe, Aufrufer und Reihenfolge der Quelle |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmAuction`](AgcmAuction.md), [`AgcmReturnToLogin`](AgcmReturnToLogin.md), [`AgcmStartupEncryption`](AgcmStartupEncryption.md)
