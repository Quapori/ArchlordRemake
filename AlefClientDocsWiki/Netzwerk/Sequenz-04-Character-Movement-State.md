# Winsock Sequenz 04: Character Movement, Position und Action-State

*Navigation: [Wiki-Start](../README.md) · [Rubrik: Netzwerk und Protokoll](Index.md)*

Stand: 2026-09-05

Diese Datei vertieft [`AgpmCharacter`](../Module/AgpmCharacter.md) Operation `1`, weil sie im laufenden Spiel der wichtigste Client->Server-Kanal fuer Bewegung, Position, Zielauswahl und Action-State ist.

## Kurzfazit

- Movement/State laeuft ueber Modul `0x02` (`AgpmCharacter`), Hauptoperation `1`.
- Der Client verschachtelt darin mindestens zwei verschiedene Nested-Pakete:
  - `AgpmCharacter + 0x136f8`: Position/Movement-State
  - `AgpmCharacter + 0x2600c`: Action/Target/Skill-aehnlicher State
- Es gibt zwei Serialisierungsmodi:
  - normaler `AuPacket`-Modus ueber `FUN_004ea280`
  - kompakter Modus ueber `FUN_0057d820` / `FUN_0057d890`, wenn `AgcmCharacter + 0xddc != 0`
- Der periodische Positionssync wird in `FUN_005a2f50` alle ca. `500 ms` oder bei deutlicher Aenderung ausgelost.

## Lokaler Player und Zeitbasis

Wichtige `AgcmCharacter`-Offsets:

| Offset | Bedeutung |
|---:|---|
| `+0x15964` | CID des lokalen Characters |
| `+0x1596c` globalartig | Pointer auf lokalen Character |
| `+0x13a1c` | Client-Zeit/Tick, per `FUN_005a46d0` gesetzt |
| `+0xf08` | letzter Movement-Sendetick |
| `+0x15bfc..+0x15c04` | zuletzt gesendete Position |
| `+0x15c08` | zuletzt gesendeter Target-/Move-State |
| `+0x159b0/+0x159b4` | pending follow/move correction state |
| `+0x15978` | kurzer String-Kontext, in einem Paket bei `+0x1108` genutzt |

Character-Offsets fuer Position/State:

| Offset | Bedeutung |
|---:|---|
| `character + 0x04` | CID / Objekt-ID |
| `character + 0xd8` | X-Position |
| `character + 0xdc` | Y/Hoehenwert |
| `character + 0xe0` | Z-Position |
| `character + 0xe4..0xec` | naechster/aktueller Zielpunkt |
| `character + 0xf0..0xf8` | alternativer Zielpunkt, wenn `+0x7c != 0` |
| `character + 0x70` | Bewegung/Controller aktiv |
| `character + 0x74` | vermutlich "movement blocked" oder kein aktiver Move |
| `character + 0x78` | optionaler Statewert |
| `character + 0x7c` | Target-/Move-/Path-State-ID |
| `character + 0x80` | weiterer Statewert, in Movement-Paket gesendet |
| `character + 0x52a` | Action-/Life-State; Wert `0x02` blockiert mehrere Sends |

## Periodischer Positionssync: `FUN_005a2f50`

Diese Funktion prueft den lokalen Character und sendet Bewegungsdaten:

```c
uVar3 = FUN_004e4690(); // aktueller Tick

if (localChar != 0 &&
    localChar->controller != 0 &&
    localChar->blocked == 0) {

    if (DAT_009aed74 < uVar3) {
        pos = localChar + 0xe4..0xec;
        if (localChar->state_7c != 0) {
            pos = localChar + 0xf0..0xf8;
        }

        if (lastState != localChar->state_7c ||
            distance(lastSentPos, pos) > threshold) {
            FUN_005a03c0(localChar + 0xd8,
                         &pos,
                         localChar->state_7c,
                         localChar->field_80,
                         localChar->field_78);
            DAT_009aed74 = now + 500;
            lastSentPos = pos;
            lastState = localChar->state_7c;
        }
    }
}
```

Sicher:

- Sendefrequenz ist auf mindestens ca. `500 ms` begrenzt.
- Es wird nicht jedes Frame gesendet.
- Gesendet wird bei Ziel-/State-Aenderung oder wenn Distanz zur zuletzt gesendeten Position zu gross wird.
- Die Payload stammt aus lokaler Position und Bewegungsziel-/State-Feldern.

## Movement-Paket: `FUN_005a03c0`

`FUN_005a03c0` ist der zentrale Builder fuer Movement/Position.

### Normaler AuPacket-Modus

Wenn `AgcmCharacter + 0xddc == 0`:

```c
flags = (param_4 != 0)
      | ((param_5 != 0) ? 2 : 0)
      | ((param_6 != 0) ? 0x10 : 0);

nested = FUN_004ea280(AgpmCharacter + 0x136f8, 0, &len, 2,
                      param_2, param_3,
                      0,0,0,0,
                      &flags, &param_4);

mainOp = 1;
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &mainOp,
                      AgcmCharacter + 0x15964,
                      0,0,0,
                      nested,
                      ...);
```

Die sichtbare Feldreihenfolge zeigt:

| Feld | Quelle | Bedeutung |
|---|---|---|
| `param_2` | meist `localChar + 0xd8` | aktuelle Character-Position |
| `param_3` | Zielposition/Stateposition | Ziel-/Move-Punkt |
| `flags` | Bits `0x01`, `0x02`, `0x10` | optionale Felder vorhanden |
| `param_4` | oft `character +0x80` oder State-ID | Movement-State |

Danach wird ueber `FUN_004e45d0(packet, len, 0, -1, socketRoute)` gesendet. `socketRoute` kommt aus dem Character-Socket-Kontext, wenn vorhanden.

### Kompakter Modus

Wenn `AgcmCharacter + 0xddc != 0`:

```c
packet = FUN_0057d820(localCID, flags, param_4, param_2, param_3, &len);
```

`FUN_0057d820` baut kein normales `AgpmCharacter` Hauptpaket, sondern:

```c
packet = FUN_004ea280(base + 0x386f0, 1, &len, 0x40,
                      &flags, param_5, param_6,
                      0,0, &param_3, &param_4, 0,0);
FUN_004ea250(packet, len, flags);
```

Sicher:

- Kompakt-Opcode/Modul: `0x40`
- Layoutbasis: `localCharacterData + 0x386f0`
- `FUN_004ea250` patcht/markiert das erzeugte Paket nachtraeglich mit Laenge/Opcode/Keyfeld.

Interpretation:

- Das ist wahrscheinlich ein optimiertes Movement-Protokoll fuer spaetere Client-/Server-Versionen.
- Es spart das grosse `AgpmCharacter` Hauptlayout und sendet eine dedizierte Movement-Nachricht.

## Positions-/Stop-Pakete

### `FUN_005a0700`

Sendet Hauptoperation `1` mit Nested-Layout `+0x136f8`.

```c
nested source = localChar + 0xd8;
flags = 4;
mainOp = 1;
cid = localCID;
route = FUN_005a0200();
```

Bedingungen:

- lokaler Character vorhanden
- `AgpmCharacter` Modul vorhanden

Bedeutung:

- Normaler Positionssync des lokalen Characters.
- Flag `4` ist sehr wahrscheinlich "current position" oder "force position update".

### `FUN_005a05b0`

Sendet ebenfalls Hauptoperation `1` mit Nested-Layout `+0x136f8`, aber:

```c
flags = 0x40;
```

Bedeutung:

- Sonderzustand im Movement.
- Wegen Nutzung in Korrektur-/Follow-Pfaden wahrscheinlich Stop, Follow-Correction, Movement-Cancel oder Path-Ende.

## Action-/Target-Paket: `FUN_005a0860`

`FUN_005a0860` baut ein zweites Nested-Layout:

```c
nested = FUN_004ea280(AgpmCharacter + 0x2600c, 0, &len, 2,
                      &param_2,
                      &param_3,
                      &param_4,
                      0,0,0,
                      optional &param_5);

mainOp = 1;
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &mainOp,
                      localCID,
                      0,0,0,0,
                      nested,
                      ...);
```

Der Funktionskontext zeigt:

- Bei `param_2 == 1` wird ein Debug-/Queue-String `(%d);` an `AgcmCharacter + 0x15a34` angehaengt.
- Aufrufer pruefen Target-/Action-Zustaende.
- In `FUN_005a33e0` wird diese Funktion nach Ziel-/Action-Vorbereitung aufgerufen.

Interpretation:

- `+0x2600c` ist kein reines Positionspaket.
- Es transportiert wahrscheinlich Action, Target, Attack/Skill oder "move-to-target" Kontext.

### Kompakter Modus fuer Action: `FUN_0057d890`

Wenn der kompakte Modus aktiv ist:

```c
packet = FUN_004ea280(base + 0x4b004, 1, &len, 0x41,
                      &param_2, &param_3,
                      0,0,0,
                      optional &param_4,
                      optional &param_5,
                      optional &param_6,
                      optional &param_7);
FUN_004ea250(packet, len, param_2);
```

Sicher:

- Kompakt-Opcode/Modul: `0x41`
- Layoutbasis: `localCharacterData + 0x4b004`
- mehrere optionale Felder, nur gesetzt wenn Werte nicht null/false sind

Interpretation:

- Dedizierter, kompakter Action-/Target-State neben Movement-Opcode `0x40`.

## Resource-/Wertupdates: `FUN_005a0fd0` und `FUN_005a10f0`

Diese Funktionen senden `AgpmCharacter` Operation `7`.

### `FUN_005a0fd0`

```c
current = FUN_0058a5f0(character);
if (requested > current) requested = current;
op = 7;
packet = FUN_004ea280(AgpmCharacter + 0xde4, 1, &len, 2,
                      &op, character + 4, ..., &requestedLow, ...);
route = FUN_005a0200();
FUN_004e45d0(packet, len, 0, -1, route);
```

`FUN_0058a5f0` liest:

```c
low  = character + 0x538;
high = character + 0x53c;
```

Die Werte werden auf maximal `1,000,000,000` begrenzt. Das wirkt wie ein 64-bit Zaehler mit Dezimal-Cap.

### `FUN_005a10f0`

Sendet ebenfalls Operation `7`, aber mit negiertem Wert:

```c
current = FUN_0058a7e0(character);
if (requested > current) requested = current;
send -requested;
```

`FUN_0058a7e0` liest:

```c
value64 = character + 0x540;
```

Interpretation:

- Op `7` ist sehr wahrscheinlich ein Ressourcen-/Wertdelta: Geld, Exp, Punkte, HP/MP-artige Werte oder Verbrauch.
- Zwei interne 64-bit Werte an `+0x538/+0x53c` und `+0x540/+0x544` werden getrennt verwaltet.
- Server sendet dieselbe Operation in `AgpmCharacter::OnReceive`, dort ruft Op `7` `FUN_0058aa00` auf und verteilt Delta zwischen diesen Werten.

## Servervalidierung und Anti-Cheat-Relevanz

Aus dem Clientverhalten folgt, dass der Server mindestens folgende Dinge pruefen muss:

- CID passt zur gebundenen Socket-Session.
- Movement-Pakete kommen nicht fuer fremde CIDs.
- Positionsdelta seit letztem Paket ist plausibel.
- Zeitdifferenz zwischen Movement-Paketen ist plausibel.
- Action-/Target-Pakete referenzieren gueltige Targets.
- Character-State `0x52a == 0x02` blockiert mehrere Aktionen; Server muss denselben Status kennen.
- Ressourcen-/Wertdeltas in Op `7` duerfen nicht clientautoritativ vertraut werden.

Der Client sendet Movement nur alle ca. `500 ms`, aber der Server muss daraus interpolieren oder grob validieren. Die lokale Distanzschwelle verhindert Paketspam bei minimaler Bewegung.

## Wann wird gesendet?

| Ausloeser | Funktion | Paket |
|---|---|---|
| normaler Movement-Tick, ca. alle 500 ms | `FUN_005a2f50` -> `FUN_005a03c0` | `AgpmCharacter` Op `1`, Nested `+0x136f8` |
| lokale Positionskorrektur/aktueller Standort | `FUN_005a0700` | `AgpmCharacter` Op `1`, Flag `4` |
| Stop/Follow-/Correction-Ende | `FUN_005a05b0` | `AgpmCharacter` Op `1`, Flag `0x40` |
| Target/Action/Attack-/Skill-Kontext | `FUN_005a0860` | `AgpmCharacter` Op `1`, Nested `+0x2600c` |
| Ressource/Wert senden | `FUN_005a0fd0` | `AgpmCharacter` Op `7` |
| Ressource/Wert negativ/Verbrauch | `FUN_005a10f0` | `AgpmCharacter` Op `7` |

## Serverdatenbank / Runtime-Strukturen

### `character_runtime_state`

| Feld | Grund |
|---|---|
| `character_id` | CID in allen Movement-Paketen |
| `session_id` | CID muss zum Socket passen |
| `world_instance_id` | Movement ist zonengebunden |
| `pos_x`, `pos_y`, `pos_z` | `character +0xd8..0xe0` |
| `target_x`, `target_y`, `target_z` | `character +0xe4..0xec` oder `+0xf0..0xf8` |
| `move_state_id` | `character +0x7c` |
| `move_flags` | Bits `0x04`, `0x40`, `0x01`, `0x02`, `0x10` |
| `last_move_packet_at` | 500-ms Clientrhythmus und Servervalidierung |
| `last_validated_at` | Anti-speedhack/Plausibilitaet |

### `character_action_state`

| Feld | Grund |
|---|---|
| `character_id` | lokale CID |
| `target_character_id` | Action-/Target-Pfade |
| `action_type` | `param_2` in `FUN_005a0860` |
| `skill_id` / `ability_id` | moeglich bei Action-/Skill-Kontext |
| `queued_action` | Debugstrings `m_szNextAction`, `m_szActionQueue` |
| `sent_at` | Serverseitige Cooldown-/Rate-Pruefung |

### `character_counters`

| Feld | Grund |
|---|---|
| `character_id` | Op `7` CID |
| `counter_a_low/high` | `+0x538/+0x53c` |
| `counter_b_low/high` | `+0x540/+0x544` |
| `counter_c_low/high` | `+0x548/+0x54c` |
| `updated_at` | Server muss Deltas ordnen |

Die Namen `counter_a/b/c` sind bewusst neutral. Der Code zeigt 64-bit Werte und Caps, aber ohne weitere Kontextanalyse ist nicht sicher, ob es Exp, Geld, Punkte, HP/MP oder Spezialressourcen sind.

## Noch offen

- Feldtypen von `+0x136f8` und `+0x2600c` sollten als Byte-fuer-Byte Layout rekonstruiert werden.
- `FUN_0057d820`/`FUN_0057d890` nutzen eigene Opcodes `0x40`/`0x41`; es muss noch geprueft werden, wie der Server diese von normalen Modul-IDs unterscheidet.
- `FUN_005a33e0` ist ein grosser Action-/Target-Kontext und sollte als eigene Attack/Target-Sequenz analysiert werden.
- Debug-/Lua-Strings rund um `m_szNextAction`, `m_szActionQueue` und `m_szAttackSentAcc` koennen helfen, Operationen sauber zu benennen.

## Relevante Funktionen

| Funktion | Adresse | Rolle |
|---|---:|---|
| `FUN_005a2f50` | `0x005a2f50` | periodischer Positionssync, 500-ms Gate |
| `FUN_005a03c0` | `0x005a03c0` | Movement/Position Builder, normales Hauptpaket Op `1` |
| `FUN_005a0700` | `0x005a0700` | Positionsupdate mit Flag `4` |
| `FUN_005a05b0` | `0x005a05b0` | Movement-Sonderupdate mit Flag `0x40` |
| `FUN_005a0860` | `0x005a0860` | Action-/Target-State Builder, Hauptpaket Op `1` |
| `FUN_0057d820` | `0x0057d820` | kompakter Movement-Builder, Opcode `0x40` |
| `FUN_0057d890` | `0x0057d890` | kompakter Action-Builder, Opcode `0x41` |
| `FUN_005a0fd0` | `0x005a0fd0` | sendet Character Op `7`, positives/limitiertes 64-bit Delta |
| `FUN_005a10f0` | `0x005a10f0` | sendet Character Op `7`, negatives/Verbrauchsdelta |
| `FUN_0058a5f0` | `0x0058a5f0` | liest 64-bit Wert `+0x538/+0x53c` |
| `FUN_0058a7e0` | `0x0058a7e0` | liest 64-bit Wert `+0x540/+0x544` |
| `FUN_0058a910` | `0x0058a910` | setzt 64-bit Wert `+0x548/+0x54c` |
| `FUN_0058aa00` | `0x0058aa00` | Server-Op `7` verarbeitet Ressourcen-/Wertdelta |
