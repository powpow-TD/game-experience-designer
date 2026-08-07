# AI Operability and Validation

## Build observability into the first slice

Implement these before scaling AI content:

- deterministic seed, replay input, and behavior trace;
- visualized perception, state/belief, goal, candidate scores or plan, target, path, reservation, and fallback;
- assertions for invariants such as player-route protection, authority limit, and valid target;
- a performance budget by population and update frequency;
- a compact scenario library that exercises interruption, recovery, contention, and degraded fidelity.

## Test at three levels

| Level | Test | Pass signal |
|---|---|---|
| Unit / invariant | Does the rule hold? | no invalid transition, forbidden action, or broken reservation |
| Scenario / replay | Does the system recover under a known disturbance? | deterministic trace reaches expected observable outcome |
| Player model | Do players infer and use the rule? | prediction and explanation accuracy; viable counter choice |

## Use automation to learn, not to certify fun

Autoplay agents, simulations, genetic search, and large-scale tests are excellent for balance surfaces, regressions, economy stress, and impossible-state discovery. They do not replace player playtests for fear, fairness, readability, companionship, or trust. Treat their output as a candidate hypothesis to test with players.

## Telemetry schema

For a consequential AI moment, log:

```text
encounter/context, player state and intent proxy,
AI perception confidence, state/belief, selected goal,
candidate options/scores or plan id, commitment cue time,
player response, resolution, fallback/recovery, performance cost
```

Pair this with a short player explanation prompt: "What did you think it would do, why, and what could you have done?"

## Keep/change/kill rule

Set the rule before testing. Example: keep a charge only if most target players correctly predict its threat before contact, at least two counters are used successfully, and traces show no player-route violation; otherwise change cue/rule/scope before tuning damage.
