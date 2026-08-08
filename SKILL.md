---
name: ai-game-experience-design
description: "Design, specify, diagnose, and validate AI-driven game experiences. Use for enemy, boss, companion, squad, NPC, LLM character, adaptive director, systemic-world, navigation, behavior-tree, utility-AI, planner, AI tooling, AI playtest, telemetry, player-agency, legibility, fairness, or trust decisions."
---

# AI Game Experience Design

Turn an AI capability into a player-readable, technically operable, testable game experience.

## Start with the experience contract

Before choosing an algorithm, write one sentence for each field:

1. **Situation and feeling**: who is the player, what do they notice, and what future do they anticipate?
2. **Player-facing role**: pressure, rival, support, tutor, world credibility, pacing, discovery, or practice.
3. **Player leverage**: what can the player predict, influence, counter, recover from, and still author?
4. **AI commitment**: what state, goal, cost, limitation, and escalation must be perceptible before it matters?
5. **Failure and recovery**: how can the AI fail, how is that detected, and what player recovery remains?
6. **Evidence**: what player explanation, observable behavior, and telemetry threshold would keep, change, or kill the feature?

Do not accept an implementation claim such as "use a behavior tree" as an experience contract.

## Work in five passes

### 1. Design the anticipation loop

Players react to the futures they infer, not only to events already on screen. State the cue, predicted consequence, player response, resolution, and learning update. Read `references/experience-engineering.md`.

### 2. Specify the behavior-to-experience chain

Trace **perception -> belief/state -> goal selection -> commitment -> action -> animation/audio/UI cue -> player choice -> recovery**. Put a player-visible assertion on every consequential transition. Read `references/game-ai-pro-patterns.md`.

### 3. Choose the smallest suitable decision architecture

| Need | Prefer | Do not use it as |
|---|---|---|
| Few discrete, auditable modes | FSM/HFSM | an unbounded exception pile |
| Authored priorities and interruptions | behavior tree | a substitute for world knowledge |
| Trade-offs that must vary continuously | utility scoring | opaque hidden weighting |
| Long, constrained goal sequences | planner/HTN/search | a reflex-only combat controller |
| Different needs at different layers | hybrid | permission to blur ownership |

Make the architecture reversible until the greybox proves its player value. Read `playbooks/ai-implementation-choice.md`.

### 4. Build an operable slice

Add deterministic replay, state/goal inspection, assertions for invariants, and a minimal encounter or interaction. Test the player mental model before producing content at scale. Read `references/operability-and-validation.md`.

### 5. Decide from triangulated evidence

Separate what happened (trace), what the player understood (explanation), what they felt (observation/interview), and whether it generalizes (telemetry). Never use win rate alone to prove fairness or fun.

## Route to the right playbook

- **Enemy or boss**: `playbooks/enemy-and-boss.md`
- **Companion, squad, or multiplayer bot**: `playbooks/companion-and-squad.md`
- **NPC, social simulation, or LLM character**: `playbooks/npc-and-llm.md`
- **Adaptive difficulty, pacing, or AI director**: `playbooks/adaptive-director.md`
- **Crowds, ambient life, procedural world, or navigation**: `playbooks/systemic-world.md`
- **Architecture or algorithm choice**: `playbooks/ai-implementation-choice.md`
- **Testing, debugging, simulation, autoplay, or telemetry**: `references/operability-and-validation.md`
- **Outdated techniques, source scope, or provenance**: `references/scope-and-modernization.md` and `references/source-coverage.md`
- **Evidence status, source cards, or decision confidence**: `references/evidence-governance.md`
- **Unity, Unreal, or LLM implementation boundary**: `references/current-platform-integration.md`

## Use the private source corpus when installed

This personal installation includes `private_sources/game-ai-pro/`: full text, 171 resource cards, and ZIP-content extracts from the local Game AI Pro collection. It is intentionally excluded from Git.

- Read `private_sources/game-ai-pro/resource_audit.json` to locate a specific PDF or ZIP.
- Read its matching `cards/pdf-*.md` or `cards/zip-*.md` before using it as evidence.
- Search `private_sources/game-ai-pro/full_text.txt` for a named technique, case study, or exact term; use `scripts/query-private-game-ai-pro.py` for repeatable lookup.
- Never copy private source passages, code, figures, or OCR into a public output. Synthesize and cite the official source instead.

If the private corpus is absent, state that source-specific claims need verification rather than inventing a citation.

## Required outputs

### AI experience contract

```markdown
## Player, situation, and intended feeling
## Player-facing AI role
## Anticipation loop: cue -> forecast -> choice -> resolution -> learning
## Protected player leverage: prediction, influence, counterplay, recovery, authorship
## Observable states, commitments, limits, and failure contract
## Behavior chain and implementation boundary
## Minimum playable slice and instrumentation
## Evidence thresholds and keep/change/kill rule
```

### Behavior and experience specification

```markdown
## Experience promise and non-goals
## Perception, belief/state, goals, and selection policy
## Commitments and player-readable cues
## Action limits, counters, yield rules, and recovery
## Space/resource reservations and coordination rules
## Difficulty, pacing, or personalization variables
## Debug views, replay hooks, telemetry, and acceptance tests
```

## Non-negotiable checks

- Preserve choices that define the player fantasy; automation must earn its agency cost.
- Make consequential AI action legible before, not after, the outcome.
- Keep claims, memory, and world actions within executable authority.
- Do not secretly invalidate earned outcomes through adaptation or retention optimization.
- Do not publish source text, scans, OCR, figures, or code from cited books. Use original synthesis and link to official sources.
- Label every decision rule with an evidence status: `hypothesis`, `source-indexed`, `source-synthesized`, `project-validated`, or `superseded`.
