# Game AI Patterns for Player Experience

Use these durable patterns as implementation vocabulary. They are not prescriptions; select them only after the experience contract is clear.

## Decision layer

| Pattern | Use when | Player-experience responsibility | Common failure |
|---|---|---|---|
| FSM / HFSM | modes and transitions are few and inspectable | make mode changes legible | transition exceptions become invisible spaghetti |
| Behavior tree | authored priorities and interruption rules dominate | expose commitment and priority changes | tree encodes facts it cannot observe or explain |
| Utility scoring | options trade off continuously | show why high-impact priorities shift | hidden weights feel random or unfair |
| Planner / HTN / search | long constrained sequences matter | let players see the plan's commitment and disruption | expensive plans hide latency and recovery |
| Hybrid | different layers need different reasoning | assign one owner per decision boundary | duplicate authority causes contradictory behavior |

## World knowledge and spatial reasoning

Keep world knowledge separate from decision logic. Feed decisions with perception, tactical queries, influence/possibility fields, navigation, formations, cover, and reservations. For each query, state freshness, confidence, cost, and what the player can infer from the result.

For crowds, squads, and companions, solve player-space conflicts before local movement optimality. Reserve player exit paths, current cover, interactable targets, camera visibility, and animation timing; then let agents negotiate what remains.

## Perception and reaction

Model what the agent knows, how certain it is, and how quickly it may act. Avoid omniscient response unless the fantasy explicitly promises it. Use perception delay, certainty, attention, reaction time, and communication to create readable limitations rather than accidental incompetence.

## Scale and simulation

Use AI level of detail, event-based simulation, scheduling, and data-driven behavior to preserve consequences at scale. Degrade fidelity deliberately: retain the player-visible promise and causal outcomes, reduce invisible decision frequency or simulation detail. Never let LOD change a rule the player is actively learning.

## Debuggability is a feature requirement

Give designers a way to inspect perception, belief, selected goal, candidate scores or plan, reservation conflict, current commitment, fallback, and final action. If a meaningful behavior cannot be inspected and replayed, it is not ready for broad content production.

## Modern boundary

Classic search, behavior trees, utility systems, navigation, and simulation patterns remain useful. Do not import their original engine assumptions, hardware targets, exact performance claims, or model choices as current best practice. See `scope-and-modernization.md`.
