# Current Platform Integration Notes

Accessed 2026-08-08. Treat versions and package maturity as time-sensitive; confirm them in the target project before committing.

## Unity 6

| Capability | Current official reference | Design implication |
|---|---|---|
| Navigation | [AI Navigation 2.0.9 for Unity 6000.0](https://docs.unity3d.com/ja/current/Manual/com.unity.ai.navigation.html) | NavMesh surfaces, dynamic obstacles, and links support movement constraints; still define player-space reservations and recovery above pathfinding. |
| Behavior graphs | [Behavior 1.0.13 for Unity 6000.0](https://docs.unity3d.com/ja/current/Manual/com.unity.behavior.html) | Graph-based, event-driven behavior trees with runtime visualization support inspectable NPC logic; keep world knowledge, priorities, and player cues explicit. |

## Unreal Engine 5.8

| Capability | Current official reference | Design implication |
|---|---|---|
| StateTree | [StateTree overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-state-tree-in-unreal-engine) | It combines hierarchical states, selectors, tasks, transitions, and data binding. Use its explicit transition and failure paths to model commitments and recovery. |
| StateTree debugging | [StateTree Debugger](https://dev.epicgames.com/documentation/unreal-engine/statetree-debugger-quick-start-guide) | Runtime state/value traces and recorded sessions make the decision chain inspectable; make trace review an acceptance criterion. |
| Large populations | [MassGameplay overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine) | Representation, simulation, replication, LOD, and StateTree are separable. Preserve player-visible causal rules when lowering simulation fidelity. |

MassGameplay documentation labels some functionality experimental. Do not turn a documentation example into a shipping dependency without a project-specific maturity and rollback assessment.

## LLM/NPC backends

Use a model only behind an executable authority boundary. The [OpenAI API reference](https://platform.openai.com/docs/api-reference/debugging-requests?lang=curl) notes that model behavior can vary between snapshots and recommends pinned versions and application evals for consistency. Design consequence: log model/version/request IDs, define tool allowlists and server-side policy, evaluate refusal/fallback behavior, and never let fluent text imply unexecuted world change.

## Cross-platform rule

Engine assets, graphs, and model calls implement a decision; they do not define the player contract. Keep the experience contract, evidence status, authority boundary, and recovery behavior independent from the specific engine integration.
