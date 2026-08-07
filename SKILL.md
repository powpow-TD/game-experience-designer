---
name: ai-game-experience-design
description: "Design, specify, diagnose, and validate AI-driven game experiences. Use for enemy AI, companion AI, NPCs, LLM characters, adaptive difficulty, procedural agents, AI-readable UI, AI behavior specifications, AI playtests, agent telemetry, trust boundaries, or player-agency risks."
---

# AI Game Experience Design

Use this skill to turn an AI capability into a deliberate, trustworthy player experience.

## Choose a workflow

- **Enemy or boss**: read `references/workflows.md` → *Enemy AI Specification*.
- **Companion**: read *Companion AI Specification* and `references/ai-experience-principles.md` → *Agency Budget* and *Failure Contract*.
- **NPC or LLM character**: read *NPC / LLM Interaction Specification* and *LLM Authority Boundary*.
- **Adaptive difficulty**: read *Adaptive Difficulty Plan* and *Adaptive Difficulty Contract*.
- **AI playtest or telemetry**: read *AI Playtest Protocol* and *Evidence Triangulation*.
- **Trust, safety, or player manipulation**: read *AI Risk and Trust Review*.

## Working method

1. State the intended player feeling and the AI's player-facing role.
2. Define what the player can observe, predict, influence, and recover from.
3. Specify AI authority, limits, fallback, and agency budget.
4. Build the smallest scene that tests player understanding and trust.
5. Record behavior, player explanation, telemetry, and the next decision separately.

## Core outputs

### AI experience brief
```markdown
## Target player and situation
## Intended feeling and player-facing AI role
## Player agency: protected choices and automation budget
## Observable cues, authority, limits, and fallback
## Experience risks and trust risks
## Minimum playtest and decision rule
```

### AI behavior specification
```markdown
## Player-facing role and combat/social fantasy
## Observable states, cues, and commitments
## Inputs, goals, decision policy, and action limits
## Counters, recovery paths, and fallback behavior
## Difficulty or personalization variables
## Telemetry, playtest tasks, and acceptance signals
```

## Resource routing

- Read `references/ai-experience-principles.md` for AI-specific reasoning.
- Read `references/workflows.md` for artifact templates.
- Read `chapters/` for topic-specific depth.
- Read `examples/` for concrete formats.

## Limits

Do not use this skill to conceal AI intervention, overclaim capability, or replace player research, accessibility work, privacy review, safety review, or final design ownership.
