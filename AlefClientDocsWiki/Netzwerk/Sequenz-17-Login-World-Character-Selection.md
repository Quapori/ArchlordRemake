# Winsock-Sequenz 17: Weltwahl, Union und Charakterlisten-Uebergang

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-09

## Ergebnis

Der aktuelle Login-Trace endet nicht bei einem Verschluesselungs-, Socket- oder
World-Listen-Fehler. Der Client hat die Anmeldung, dreimalige World-List-Antwort
und die Union-Antwort akzeptiert. Er wartet danach auf die fruehe, accountweite
Charakterlisten-Abschlussmeldung `AGPMLOGIN_CHARACTER_NAME_FINISH` (Operation
`5`). Diese Nachricht wurde in der aufgezeichneten Arbeitsphase nicht gesendet;
daher wird [`AgcmLogin`](../Module/AgcmLogin.md):SendGetCharacters` fuer die gewaehlte Welt nicht
ausgeloest und es erscheint keine nachfolgende Client-Anfrage Operation `6`.

Dies ist eine Protokollbefunddatei. An `AlefLogin`-Rust-Code, DB-Schema oder
Serverkonfiguration wurde bei dieser Analyse nichts geaendert.

## Belege

- Live-Log: `AlefLogin/server.log`, letzte passende Arbeitsphase vom
  `2026-09-08 18:28:58` bis `18:29:01` UTC. Die Datei wurde zuletzt am
  `2026-09-08 21:02:43` geschrieben; es liegt noch kein neuerer Loginversuch im
  Log vor.
- Client-Receive-Switch: `alefclient.pseudocode.c`,
  `FUN_0065e7f0` sowie `FUN_0065d4e0` / `FUN_0065d550`.
- Feldlayouts und originale Serverablauf-Referenz: [`FORCE_LOGIN_WORKAROUND.md`](../Start-und-Login/Login-Callback-Workaround.md),
  insbesondere Abschnitte ab Zeile 538 und 2195.
- Aktueller Server wurde nur gelesen: `AlefLogin/crates/aleflogin-server/src/main.rs`.

## Tatsaechlicher Ablauf im Log

| UTC | Richtung | Wrapper-Sequenz | Modul / Operation | Befund |
|---|---|---:|---|---|
| 18:28:58.830 | Client -> Server | 3 | `AgcmLogin` / `1` | Sign-On; Antwort wird akzeptiert. |
| 18:28:58.831 bis .867 | Client -> Server | 4, 5, 6 | [`AgpmWorld`](../Module/AgpmWorld.md) / World-List | Drei World-List-Requests, jeweils `RESULT_GETWORLD_ALL count=1` als Antwort. |
| 18:29:01.420 | Client -> Server | 7 | `AgcmLogin` / `3` | `UNION_INFO` fuer Account `bootstrap`, World `AlefWorld`. |
| 18:29:01.425 | Server -> Client | 6 | `AgcmLogin` / `3` | Union-Antwort mit `AUUNION_TYPE_RED_HEART` (`1`). |
| danach | Client -> Server | - | - | Kein weiteres Paket bis zum Verbindungsende. Insbesondere keine Operation `6`. |

Der Client-Request Operation `3` ist bytegenau dekodiert:

```
d6 62 00 0d ... 85 00 03
62 6f 6f 74 73 74 72 61 70 00 ...       # AccountID: 49 Byte fixed
41 6c 65 66 57 6f 72 6c 64 00 ...       # WorldName: 32 Byte fixed
... 6b
```

Die Hauptpaketmaske `0x0085` setzt die Felder `Operation` (Bit 0), `AccountID`
(Bit 2) und `WorldName` (Bit 7). `AccountID` ist auf dem Wire 49 Byte,
nicht 65 Byte.

## Client-seitige Receive-Dispatches

Der zentrale `AgcmLogin::OnReceive`-Switch ordnet die relevanten Server-
Operationen wie folgt zu:

| Server-Operation | Clientfunktion | Callback | Bedeutung |
|---:|---|---:|---|
| `3` `UNION_INFO` | `FUN_0065d4e0` | Event `5` | Nested `CharDetailInfo` wird gelesen; daraus wird nur `UnionInfo` benutzt. |
| `4` `CHARACTER_NAME` | `FUN_0065d550` | Event `6` | Ein accountweiter Charakter-/World-Eintrag. `CharName`, Gesamtzahl und Slot werden aus `CharDetailInfo` gelesen. |
| `5` `CHARACTER_NAME_FINISH` | direkt im Switch | Event `7` | Abschluss der accountweiten Vorab-Liste. |
| `6` `CHARACTER_INFO` | ist Client -> Server | - | `SendGetCharacters` fuer die bereits ausgewaehlte Welt. |
| `7` `CHARACTER_INFO_FINISH` | direkt im Switch | Event `8` | Abschluss der weltbezogenen Auswahlphase. |

Die Dekompilierung belegt den entscheidenden Teil unmittelbar:

```
Operation 3 -> FUN_0065d4e0 -> EnumCallback(5, ...)
Operation 4 -> FUN_0065d550 -> EnumCallback(6, ...)
Operation 5 -> EnumCallback(7, ...)
Operation 7 -> EnumCallback(8, ...)
```

Der Callback Event `7` ruft im normalen UI-Fluss
`AgcmLogin::SendGetCharacters(m_szWorldName, m_szAccount)` auf. Erst dadurch
geht die Client-Anfrage Operation `6` ueber den Socket. Der fehlende Client-
Traffic nach der Union-Antwort ist deshalb erwartbar und kein Timeout-Indiz.

## Korrekte Trennung der beiden Charakterphasen

Die gleich klingenden Operationen beschreiben zwei verschiedene Datenfluesse:

| Phase | Ausloeser | Server -> Client | Zweck |
|---|---|---|---|
| Accountweit, vor der Welt-Charakterauswahl | Client-Op `3` | Op `3` Union, dann Op `4` x N und Op `5` | Welche Charaktere bzw. Welten fuer den Account bereits bekannt sind; beendet den Vorlauf und aktiviert den naechsten UI-Schritt. |
| Gewaehlte Welt | Client-Op `6` | Vollstaendige Character-Add-Daten im [`AgpmCharacter`](../Module/AgpmCharacter.md)-Kanal, danach Op `7` | Charakterdaten fuer Auswahl, 3D-Instanziierung und Folgezustand. |

`MaxRegisterChars` im nested `CharDetailInfo` der Op-4-Eintraege ist dabei die
Gesamtzahl der Datenbankzeilen, nicht die maximale Slotanzahl.

## Abgleich mit dem nur gelesenen aktuellen Loginserver

Der aktuelle Handler fuer Client-Op `3` erzeugt ausschliesslich die
Union-Antwort (Op `3`, nested `UnionInfo=1`) und gibt sie als einzelne Antwort
zurueck. Er sendet keine Op-4-Eintraege und keine Op-5-Abschlussmeldung.

Der vorhandene Handler fuer Client-Op `6` kann zwar Op-4-Namenseintraege und
eine Op-7-Abschlussmeldung senden. Diese Reihenfolge liegt aber hinter der
nicht erreichten Client-Anfrage Op `6` und vermischt die zwei Protokollphasen.
Die Logsequenz passt exakt zu dieser Luecke.

Das ist keine Aufforderung zu einer Codeaenderung in dieser Analyse, sondern
der konkrete, reproduzierbare Fehlerbefund:

```
fehlend vor dem erwarteten Client-Op6:
  Server Op4 (pro accountweitem Eintrag, optional bei 0 Eintraegen)
  Server Op5 (immer, auch bei leerer Liste)
```

Bei einem frischen Account reicht fuer diesen Uebergang somit die
Op-3-Union-Antwort gefolgt von Op-5. Ohne Op-5 bleibt der Client genau an der
im Log beobachteten Stelle stehen.

## Grenzen und naechste Analyse

Die fehlende Op-5-Meldung erklaert das aktuelle Anmelde-Stillstehen vollstaendig.
Sie erklaert nicht allein die spaetere 3D-Charakterdarstellung: Nach Op-6
braucht der Client fuer bestehende Charaktere die vollstaendigen
`AGPMCHARACTER_PACKET_OPERATION_ADD`-Daten im separaten `AgpmCharacter`-Kanal.
`AgcmLogin` Op-7 ist nur das Ende dieser zweiten Phase. Die bereits vorhandene
Quellenanalyse verweist dafuer auf `AgsmCharacter::SendCharacterAllInfo` und
`MakePacketAddCharacter` mit Move-, Factor-, Ausruestungs- und Appearance-
Unterdaten.

Die naechsten rein analytischen Schritte sind daher:

1. Das exakte Op-4/Op-5-Wire-Format aus `SendCharacterName` und
   `SendCharacterNameFinish` gegen die Client-Deserializer kontrollieren und
   einen leeren sowie einen Eintragsfall als Byte-Spezifikation festschreiben.
2. Die Receive-Switches von `AgcmCharacter` fuer
   `AGPMCHARACTER_PACKET_OPERATION_ADD` bis zur lokalen
   `AgpmCharacter::AddCharacter`-Instanziierung zerlegen.
3. Den `MakePacketAddCharacter`-Baum auf die minimalen Felder fuer eine
   stabile Auswahlansicht reduzieren: IDs, Template, Name, Position, Faktoren,
   Appearance und notwendige Ausruestungsreferenzen.
