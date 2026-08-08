# AI Game Experience Design

> Design game AI that players can read, influence, trust, and learn from.

`AI Game Experience Design` is a skill for turning game-AI ideas into player-facing behavior specifications, implementation boundaries, operable prototypes, and evidence-based decisions.

It is for enemies and bosses, companions and squads, systemic NPCs, LLM characters, adaptive directors, navigation/crowds, AI tooling, and AI playtests etc.

## Why it exists

Most AI documents begin with implementation:

- "Use a behavior tree for the companion."
- "Make the enemy flank more intelligently."
- "Let the NPC remember conversations."
- "Use an AI director to retain struggling players."

Those are not yet design decisions. They omit what the player should anticipate, what choice remains theirs, how the AI communicates commitment, how it fails, and what would prove the feature works.

This skill starts with an **experience contract** and carries it through the full chain:

```text
Player situation and feeling
  -> player-facing AI role
  -> cue -> forecast -> player choice -> resolution -> learning
  -> perception -> belief -> goal -> commitment -> action
  -> debug/replay + player model + telemetry
  -> keep / change / kill decision
```

## What it produces

| Need | Artifact |
|---|---|
| Vague AI feature | AI Experience Contract |
| Enemy or boss | Behavior-to-experience specification and encounter test |
| Companion or squad | Player-first space and coordination contract |
| NPC / LLM character | Knowledge, authority, consequence, and safety boundary |
| Adaptive director | Bounded fairness and pacing contract |
| Systemic world | Visible causal-world promise and fidelity envelope |
| Architecture decision | Experience-first AI ADR and observability plan |
| Playtest / telemetry | Player-model protocol and keep/change/kill rule |

## The quality bar

Every consequential AI behavior must satisfy three requirements.

| Requirement | Player question |
|---|---|
| **Legibility** | "What is it doing, and why?" |
| **Leverage** | "What can I meaningfully do about it?" |
| **Reliability** | "Will the rule hold when it matters?" |

An internally sophisticated agent can still fail any one of them. The skill treats those failures as design and production problems, not as tuning afterthoughts.

## Core workflows

1. Write the player situation, intended feeling, and player-facing role.
2. Define the anticipation loop: cue -> forecast -> choice -> resolution -> learning.
3. Protect the player decisions that carry the fantasy.
4. Assign one accountable owner to each AI decision boundary.
5. Select the smallest architecture that is readable, inspectable, and reversible.
6. Build a minimum meaningful scene with replay and debug views.
7. Decide from trace, observation, player explanation, and telemetry separately.

## Playbooks

| Playbook | Use for |
|---|---|
| [Enemy and Boss](playbooks/enemy-and-boss.md) | telegraphs, counterplay, tactical space, difficulty scaling |
| [Companion and Squad](playbooks/companion-and-squad.md) | player priority, reservations, coordination, bots |
| [NPC and LLM](playbooks/npc-and-llm.md) | social simulation, memory, tools, claims, consequences, safety |
| [Adaptive Director](playbooks/adaptive-director.md) | difficulty, pacing, procedural pressure, fairness |
| [Systemic World](playbooks/systemic-world.md) | crowds, navigation, ambient life, LOD, player-modified worlds |
| [Implementation Choice](playbooks/ai-implementation-choice.md) | FSM, behavior tree, utility, planner, hybrid architecture |

## Reference library

- [Experience Engineering](references/experience-engineering.md): design AI around player forecasts and meaningful choice.
- [AI Experience Principles](references/ai-experience-principles.md): legibility, leverage, reliability, authority, and trust.
- [Game AI Patterns](references/game-ai-pro-patterns.md): durable decision, perception, spatial, scale, and tooling vocabulary.
- [Operability and Validation](references/operability-and-validation.md): replay, assertions, simulation, telemetry, and player-model tests.
- [Scope and Modernization](references/scope-and-modernization.md): what to retain, treat as historical, or exclude.
- [Source Coverage](references/source-coverage.md): source families and copyright boundary.
- [Game AI Pro Resource Register](references/game-ai-pro-resource-register.md): all 171 indexed local resources, public-safe routing, and initial disposition.
- [Evidence Governance](references/evidence-governance.md): source-card states and expiry rules.
- [Current Platform Integration](references/current-platform-integration.md): Unity 6, Unreal 5.8, and LLM-boundary notes.

## Examples

- [AI Experience Contract](examples/ai-experience-contract.md)
- [Companion Specification](examples/ai-companion-spec.md)
- [Combat Decision Audit](examples/combat-decision-audit.md)
- [Adaptive Difficulty Plan](examples/adaptive-difficulty-plan.md)
- [LLM NPC Boundary](examples/llm-npc-boundary.md)
- [AI Playtest Protocol](examples/playtest-protocol.md)

## Install

```powershell
git clone https://github.com/powpow-TD/ai-game-experience-design $env:USERPROFILE\.codex\skills\ai-game-experience-design
```

## Use

```text
Use ai-game-experience-design to specify a companion AI for a tactical shooter.
Protect player routes and initiative, make commitments readable, define yield and recovery behavior,
choose an inspectable architecture, and propose a greybox player-model test.
```

```text
Use ai-game-experience-design to design an LLM quest giver.
Define its knowledge/memory/tool authority, visible world consequences, refusal behavior, privacy and safety limits,
then give acceptance tests that distinguish fluent dialogue from trustworthy gameplay.
```

## Sources and license

This repository is an original, implementation-oriented synthesis informed by the *Game AI Pro* collections (Steve Rabin, series editor) and Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences* (Chinese edition: *体验引擎*). It contains no source scans, OCR, long quotations, figures, tables, or source code. See [Source Coverage](references/source-coverage.md).

Repository-original material is licensed under [CC BY-NC-SA 4.0](LICENSE). Rights in cited works remain with their respective rightsholders.
