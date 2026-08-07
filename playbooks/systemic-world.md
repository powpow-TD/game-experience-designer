# Systemic World, Navigation, and Ambient AI

## Start from visible world promises

Specify what the player should believe: inhabitants respond to danger, a crowd makes room, a patrol searches plausibly, animals appear self-directed, or a procedural world maintains momentum. Build only the simulation depth needed to support that belief and its player interactions.

## Spatial design rules

- Model traversability, ownership, uncertainty, and temporal validity separately.
- Treat cover, target points, interaction points, escape paths, and camera-safe space as contested resources.
- Use flow fields, local avoidance, path planning, tactical queries, and LOD according to the number of agents and the player-visible consequence.
- Preserve causal continuity when reducing fidelity: a distant agent may update less often, but it should not visibly break a learned world rule.

## Ambient interactions

Use a constrained rule vocabulary: trigger, eligibility, resource/space claim, visible commitment, resolution, cooldown, and interruption. Ambient life becomes credible when it creates small, consistent causal stories without stealing attention from primary play.

## Scale test

Test normal, crowded, blocked, and player-modified cases. Measure frame cost, queue/reservation contention, path failure recovery, visual popping, and player recognition of the intended world rule.
