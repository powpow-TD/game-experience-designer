# AI Experience Patterns

## Commitment Window
**Use when**: an AI action changes player risk or space.
**How**: expose an intent cue, commitment duration, cancellation rule, counter, and recovery.
**Trade-off**: clearer play may reduce surprise; vary context, not the core rule.

## Player-First Reservation
**Use when**: companions, squads, crowds, or enemies contend for space/resources.
**How**: reserve player routes, interactables, cover, camera space, and critical timing before local optimization.
**Trade-off**: agents occasionally take second-best actions; trust is worth the tactical loss.

## Inspectable Decision Chain
**Use when**: a design cannot explain why an AI acted.
**How**: expose perception, belief, goal, candidates/scores or plan, commitment, path, action, and fallback in replay.
**Trade-off**: tooling cost arrives early; it prevents content-scale blind debugging.

## Honest Director
**Use when**: adjusting challenge or pacing.
**How**: state signals, allowed knobs, protected outcomes, bounds, disclosure, and rollback.
**Trade-off**: less raw control over retention metrics; preserves competence and trust.

## Authority-Gated Character
**Use when**: an NPC or LLM presents social intelligence.
**How**: bind dialogue to scoped knowledge, memory, tools, world actions, and refusals.
**Trade-off**: fewer improvised promises; fewer broken expectations.

## Fidelity Envelope
**Use when**: simulating many agents or an open world.
**How**: reduce update frequency/detail outside player attention while preserving visible rules and causal outcomes.
**Trade-off**: more explicit LOD design; fewer immersion-breaking state jumps.
