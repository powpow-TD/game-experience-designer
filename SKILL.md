---
name: game-experience-designer
description: "Apply the practical design thinking of Game Experience Designer to game AI, mechanics, NPCs, quests, UI, rewards, difficulty, narrative consistency, planning, prototypes, and playtests. Use when turning an experience goal into system constraints, diagnosing why a player experience fails, writing an AI behavior specification, or designing a minimum validation experiment."
---

# Game Experience Designer

Use this skill as a practical knowledge base for engineering player experience. It turns experience goals into system constraints, player-visible behavior, and validation work.

## Choose a workflow

- **Define a feature**: read `references/workflows.md` → *Experience Brief*.
- **Specify game AI**: read *AI Behavior Specification* plus Chapters 3, 5, 9, and 13 as needed.
- **Diagnose an encounter**: read `references/core-models.md` → *Decision Field*, *Readability Stack*, and *Challenge Decomposition*.
- **Plan validation**: read *Hypothesis Loop* and `references/workflows.md` → *Playtest Protocol*.
- **Make a production decision**: read *Dependency Stack*, *Decision Portfolio*, and Chapter 16.

## Working method

1. State the target player and intended emotional transition.
2. Translate it into player-visible system behavior, choices, feedback, and constraints.
3. Identify the riskiest unproven assumption.
4. Build the smallest prototype that can test that assumption.
5. Record observation, interpretation, decision, and the next experiment separately.

## Output templates

### Experience brief
```markdown
## Target player and situation
## Intended emotional transition
## Core player verb and forecast
## System constraints and player-visible evidence
## Risks and unknowns
## Minimum validation experiment
```

### AI behavior specification
```markdown
## Player-facing role
## Observable states and readable cues
## Goals, inputs, and decision policy
## Actions, limits, and fallback
## Player choices and recovery paths
## Test cases and telemetry
```

## Resource routing

- Read `references/core-models.md` for compact reasoning tools.
- Read `references/workflows.md` for repeatable planning artifacts.
- Read `chapters/` only for a topic's deeper context.
- Read `examples/` for concrete application patterns.

## Limits

Do not treat this skill as a substitute for player research, accessibility work, performance testing, legal review, or final design ownership. Treat its claims as structured hypotheses to validate.
