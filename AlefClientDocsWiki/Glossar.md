# Glossar

*Navigation: [Wiki-Start](README.md) · [Methodik](Methodik.md) · [Architektur](Architektur.md)*

| Begriff | Bedeutung |
|---|---|
| **EP8-Quelle** | Die C++-Referenzquelle (lokale Kopie der EP8-C++-Quelle), gegen die das Binary abgeglichen wird. Nicht identisch mit den untersuchten Builds. |
| **Build 2013 / 2017** | Die beiden untersuchten Binaries, siehe [Builds](Builds.md). |
| **Ghidra** | Disassembler/Dekompiler (12.1.x, Headless) für den Bulk-Export der Funktionen. |
| **`FUN_xxxxxxxx`** | Automatischer Ghidra-Name einer Funktion an Adresse `xxxxxxxx`; Ausgangszustand ohne PDB. |
| **ICF (Identical COMDAT Folding)** | Der Linker faltet Funktionen mit identischem Maschinencode zu einer Adresse zusammen. Folge: mehrere Quellmethoden/Klassen teilen sich eine Adresse, z. B. `0x0067AC90` (`return TRUE`). Siehe [Methodik](Methodik.md). |
| **Stub** | Winziger gemeinsamer Funktionsrumpf (leer, `return TRUE`, `OnIdle`-Rumpf). Nicht einer einzelnen Quellmethode zuordenbar. |
| **vtable / Slot** | Tabelle virtueller Methoden einer Klasse; die Slot-Nummer bestimmt die Methode (2 = `OnInit`, 3 = `OnIdle`, 7 = `OnDestroy` bei Modulen). |
| **RTTI** | Laufzeit-Typinformation; erlaubt, Vtables Klassennamen zuzuordnen. |
| **TU (Translation Unit)** | Eine übersetzte Quelldatei; ihre Funktionen liegen im Binary oft als zusammenhängender Adressbereich. `tu_<Modul>.json` hält den Abgleich. |
| **Anker** | Bereits sicher benannte Funktion, an der sich benachbarte Funktionen ausrichten lassen. |
| **Callee / Caller** | Aufgerufene / aufrufende Funktion (`fncalls.json`). Callee-Listen sind nach Adresse sortiert, nicht nach Aufrufreihenfolge. |
| **`OnAddModule`** | Modulmethode, die Partnermodule mit `GetModule("Name")` holt und Callbacks anmeldet. Daraus entstehen die [Member-Offsets](Uebersichten/Member-Offsets.md). |
| **`CBxxx`** | Callback-Handler (Naming der Quelle), z. B. `CBAddChar`. |
| **`OnReceive`** | Paketempfang eines `Agpm…`-Moduls; schaltet über ein Operationsbyte. |
| **Operationsbyte** | Byte im Paket, das die Aktion wählt (z. B. `ADD`, `REMOVE`, `UPDATE`); Karten in [Netzwerk](Netzwerk/Index.md). |
| **StartupEncryption** | Schlüsselaustausch beim Verbindungsaufbau (`AgpmStartupEncryption`), siehe [Transform-Cipher](Netzwerk/Transform-Cipher.md). |
| **`names_allN.tsv`** | Gesamtliste der vergebenen Namen (Adresse, Name, Beleg); die höchste Nummer ist der aktuelle Stand. |
| **`gm_<Modul>.tsv`** | Namensvorschläge/-festlegungen je Modul, werden mit `applygm.py` übernommen. |
| **„von Hand geprüft“** | Beleg-Stufe: Dekompilat und Quelle wurden gelesen und verglichen. |
| **„nicht Zeile für Zeile verglichen“** | Zuordnung über Struktur, Größenverhältnis oder Aufrufbeziehungen, nicht über einen Rumpfvergleich; schwächerer Beleg. |
| **Exportlücke** | Codebereich, den Ghidra nicht als Funktion angelegt hat und der im Export fehlt. |
