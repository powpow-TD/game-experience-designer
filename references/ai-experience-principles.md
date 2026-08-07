# AI Game Experience Principles

## Player-Facing Role
Define an AI actor by what it contributes to the player's experience: pressure, support, discovery, rivalry, companionship, world credibility, or practice. “Uses a behavior tree” is not a role.

## Legibility Before Optimization
An internally optimal action that players cannot predict or explain creates distrust. Make goal, commitment, limitation, and consequence visible through behavior and restrained feedback.

## Agency Budget
Every AI intervention spends player agency. Automation should remove friction without taking away the decisions the experience depends on. Reserve critical routes, resources, and authorship for the player.

## Failure Contract
State how an AI can fail, how a player notices, what fallback occurs, and what recovery remains. This is essential for companions, procedural agents, and LLM NPCs.

## Adaptive Difficulty Contract
Adapt observable pressure, information, pacing, or support while preserving the meaning of success. Never silently rewrite a result the player believes they earned.

## LLM Authority Boundary
Keep NPC memory, dialogue, promises, and actions within executable system authority. When a request exceeds that boundary, acknowledge and redirect without fabricating world impact.

## Evidence Triangulation
Use telemetry for behavior, observation for moment-to-moment friction, player explanation for mental models, and interviews for meaning. No single source proves experience quality.

## Trust Review
Review manipulation, deception, privacy, bias, safety, consent, and unwanted emotional dependence before shipping an AI interaction.
