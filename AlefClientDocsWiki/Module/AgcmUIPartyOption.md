# AgcmUIPartyOption (AlefClient.exe 2017-08-15)

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Module des 2017er Clients](Index.md)*

Automatisch erzeugte Modulanalyse (Skriptlauf `batch_all.py`) des Moduls `AgcmUIPartyOption` im Build SHA-256 `20009faa…e067b` (ImageBase `0x400000`). Belege: Ghidra-Dekompilat und Sprungtabellen-Auswertung, EP8-Quelle (`AgcmUIPartyOption` / `AgcmUIPartyOption.cpp`) und die Berichte zum **2013er Build** (`F951E56D…`, `ALEFCLIENT_ONRECEIVE_OPCODES.md`, `ALEFCLIENT_PAKETLAYOUTS.md`). Alle Adressen gelten nur für den 2017er Build. Die Texte dieses Berichts sind maschinell aus den Vergleichsergebnissen erzeugt und nicht von Hand durchgesehen.

## Kernbefund

- **Dispatch:** `OnReceive` bei `0x006BFE30` (vtable-Slot 9); Auswertung über Switch im Dekompilat.
- **Kein Operationsschalter:** In der Quelle bzw. im Binary wurde keine Verzweigung nach Operationen erkannt (`OnReceive` im Binary: 151 Byte).
- **Ereignisse:** `OnReceive` löst bis Tiefe 3 keine `EnumCallback`-Aufrufe aus.
- **Paketlayout:** 1 Paketdefinition(en) in der Quelle, 1 davon im 2017er Konstruktor (`006bf600`) mit identischen Feldtypen, Anzahlen und Flag-Länge wiedergefunden.

## Funktionskarte

| Adresse | Funktion | Beleg |
|---|---|---|
| `0x006BF600` | `AgcmUIPartyOption::ctor_or_dtor_006bf600` | merged |
| `0x006BF7A0` | `AgcmUIPartyOption::ctor_or_dtor_006bf7a0` | merged |
| `0x006BFE30` | `AgcmUIPartyOption::OnReceive` | merged |
| `0x006BFED0` | `AgcmUIPartyOption::CBDisplayPartyOptionGetItemMember` | ui |
| `0x006C0120` | `AgcmUIPartyOption::CBDisplayPartyOptionDivisionItemUpdate` | ui |
| `0x006C01B0` | `AgcmUIPartyOption::CBDisplayPartyOptionNoLoginMember` | ui |
| `0x006C01F0` | `AgcmUIPartyOption::CBReceiveInviteFailedNoLoginMember` | stage1 |
| `0x006C02E0` | `AgcmUIPartyOption::CBIsActivePartyOptionUIInviteMemberID` | ui |
| `0x006C0320` | `AgcmUIPartyOption::~AgcmUIPartyOption` | merged |
| `0x006C03F0` | `AgcmUIPartyOption::AddDisplay` | strmatch |
| `0x006C04A0` | `AgcmUIPartyOption::AddBoolean` | strmatch |
| `0x006C0620` | `AgcmUIPartyOption::OnInit` | merged |
| `0x006C0670` | `AgcmUIPartyOption::CBUpdateItemDivision` | stage1 |
| `0x006C06F0` | `AgcmUIPartyOption::CBUpdateExpDivision` | stage1 |
| `0x006C0770` | `AgcmUIPartyOption::CBAddParty` | stage1 |
| `0x006C07E0` | `AgcmUIPartyOption::CBUpdateParty` | stage1 |
| `0x006C0800` | `AgcmUIPartyOption::CBRemoveParty` | stage1 |
| `0x006C0860` | `AgcmUIPartyOption::OnAddModule` | merged |

18 Funktionen des Moduls sind benannt (Quelle der Namen: vtable/RTTI, Callback-Registrierung, Zeichenketten, Case-Zuordnung).

## Paketlayout

| Paket | Flag-Länge Quelle/2017/2013 | Felder Quelle/2017/2013 | Quelle = 2017 | Quelle = 2013 |
|---|---|---|---|---|
| `m_csPacket` | 1/1/1 | 7/7/7 | ja | ja |

**m_csPacket** (7 Felder, Flag-Länge 1):

| # | Maske | Typ | Anzahl | Beschreibung (Quelle) |
|---:|---|---|---:|---|
| 0 | `0x1` | INT32 | 1 | Item Template ID |
| 1 | `0x2` | INT32 | 1 | Item Owner CID |
| 2 | `0x4` | INT32 | 1 | Item Count |
| 3 | `0x8` | INT8 | 1 | # of physical convert |
| 4 | `0x10` | INT8 | 1 | # of socket |
| 5 | `0x20` | INT8 | 1 | # of converted socket |
| 6 | `0x40` | INT8 | 1 | option Count |

## Grenzen

- Die Auswertung folgt Aufrufen nur innerhalb des Adressbereichs des Moduls (von der ersten Funktion der Klasse bis zur ersten Funktion der nächsten Klasse). Gemeinsam genutzte Basisfunktionen (`GetEventFromBasePacket`, Sperren) werden bewusst nicht verfolgt, damit fremde Callbacks nicht zugerechnet werden.
- Die Ereignisse eines Cases ergeben sich aus `EnumCallback`-Aufrufen im Case selbst und in den bis Tiefe 3 erreichbaren Funktionen des Moduls; Aufrufe über Funktionszeiger oder Funktionen außerhalb des Moduls werden nicht verfolgt.
- Callback-Namen stammen aus der EP8-Quelle; im Binary tragen die Ereignisse nur Nummern. Die Zuordnung ist nur so verlässlich wie die ID-Reihenfolge (siehe Verschiebung oben).
- Unbekannte Callback-IDs (`-1`) entstehen, wenn die ID nicht als Konstante unmittelbar vor dem Aufruf gepusht wird.
- Die Paketfeld-Auswertung vergleicht nur Typ, Anzahl und Flag-Länge aus dem Konstruktor; die Feldreihenfolge in `OnReceive`/`MakePacket` und das Verhalten der Handler sind nicht Feld für Feld geprüft.
- Das Verhalten der Handler (Berechtigungen, Zustandsänderungen) wurde nicht gegen die Quelle zeilenweise abgeglichen, und die zugehörigen UI-/Server-Module sind nicht Teil dieser Analyse.

<!-- LUECKENREGISTER-NACHTRAG-BEGIN -->

## Lückenregister (Nachtrag)

Stand der Lückenabarbeitung (Register `ALEFCLIENT_2017_LUECKENREGISTER_PHASE1` bis `PHASE4`, Namenstabelle `names_all*.tsv`): eingebaut: 1, gemeinsamer Rumpf: 1, ohne Kandidat: 6, zugeordnet: 3.

Laut Register zugeordnet (teils schon in der Funktionskarte, teils nachträglich über Aufrufgraph, Konstanten oder Feldversätze):

| Methode | Zeilen | Adresse | Beleg |
|---|---:|---|---|
| `AddUserData` | 42 | `0x006BF800` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `SetPartyOption` | 32 | `0x006C0570` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |
| `CBPartyOptionInviteMember` | 61 | `0x006BFC80` | Handprüfung: Aufrufe, Aufrufer und Reihenfolge von Dekompilat und Quelle verglichen |

<!-- LUECKENREGISTER-NACHTRAG-END -->

## Querverweise

- **Erwähnt in:** [`AgcmParty`](AgcmParty.md), [`AgpmParty`](AgpmParty.md)
