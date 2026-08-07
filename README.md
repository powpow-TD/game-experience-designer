# Game Experience Designer

> An English-language practical skill for turning player-experience goals into game systems, AI behavior specifications, prototypes, and playtest evidence.

Game Experience Designer is an original operational synthesis inspired by Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences*. It is built for game designers, technical designers, AI designers, and small cross-functional teams who need to move from an appealing intention to observable player behavior and a testable implementation plan.

It contains no scans, OCR, long quotations, figures, or replacement for the source book. The goal is to make its design thinking usable during real project work.

---

## Why this exists

Teams often describe a feature through implementation:

- “The companion should choose the best cover.”
- “The enemy should flank more intelligently.”
- “The reward loop needs more retention.”
- “The NPC should remember previous conversations.”

Those statements leave out the design question that matters: what should a player predict, feel, understand, decide, and learn?

An internally capable system can still create a poor experience. A companion may optimize cover while trapping the player. A difficult enemy may be mechanically fair while unreadable. An LLM NPC may sound convincing while promising actions the game cannot perform.

This skill turns an implementation discussion into an experience-engineering loop:

```text
Player and situation
        ↓
Intended emotional transition
        ↓
Player-visible behavior, information, and choices
        ↓
Risks and unproven assumptions
        ↓
Minimum prototype or playtest
        ↓
Evidence → decision → next iteration
```

---

## What this skill does

| Situation | What the skill helps produce |
|---|---|
| A feature starts as a vague idea | An experience brief with target player, emotional transition, core verb, constraints, and risk |
| An AI feature needs definition | A player-facing behavior specification: role, readable states, goals, actions, limits, fallback, and tests |
| An encounter is frustrating or shallow | A decision audit covering information, viable responses, counterplay, recovery, and telemetry |
| Difficulty feedback is contradictory | A failure-layer diagnosis: perception, reaction, planning, execution, or coordination |
| A team does not know what to build next | A smallest viable prototype and a keep/change/kill decision rule |
| A large decision risks rework | A dependency and reversibility analysis with explicit evidence gaps |
| A playtest produces opinions but no learning | A focused protocol with a question, player task, signals, thresholds, and interpretation rules |

---

## Core principles

### 1. Experience before features

Start with the desired change in the player's emotional forecast. A feature is only useful when it changes what the player believes could happen next, what they can do about it, or what the outcome means.

### 2. Decisions before option count

Depth comes from an internal process of prediction and trade-off. Two viable, readable strategies can be richer than ten interchangeable actions. More choices do not automatically create more agency.

### 3. Readability before cleverness

Players cannot appreciate an AI decision they cannot perceive. Make goals, state changes, action commitments, limits, and recovery paths legible through behavior, space, animation, sound, and restrained UI.

### 4. Evidence before certainty

Separate observation, telemetry, interview, inference, and assumption. A satisfying explanation is not proof. Every important claim should have a plausible way to be disproved.

### 5. Iteration before polish

Use the least-produced artifact that can test the experience question. A greybox scene with one enemy and one decision may teach more than a polished vertical slice with too many variables.

### 6. Alignment before optimization

Mechanics, narrative, interface, rewards, and production choices must support the same player experience. Local optimization that harms the overall experience is still a design failure.

---

## The practical knowledge map

The skill organizes the book's ideas into 17 application domains. Each chapter is written as actionable guidance rather than a substitute summary of the source text.

| # | Domain | Use it when | Typical game-AI question |
|---|---|---|---|
| 1 | [Experience Engine](chapters/ch01-experience-engine.md) | Defining the intended feeling | What future should the player emotionally anticipate? |
| 2 | [Elegance](chapters/ch02-elegance.md) | Rules keep accumulating | Can simpler rules create richer, learnable outcomes? |
| 3 | [Skill](chapters/ch03-skill.md) | Difficulty feedback is unclear | Is the player failing at perception, reaction, planning, or coordination? |
| 4 | [Story](chapters/ch04-story.md) | Fiction and play contradict each other | Does the NPC's behavior support its role and the game's values? |
| 5 | [Decisions](chapters/ch05-decisions.md) | Choice feels shallow or overloaded | What can the player predict, risk, and meaningfully trade? |
| 6 | [Balance](chapters/ch06-balance.md) | A strategy dominates | Which path is displacing others, and why? |
| 7 | [Multiplayer](chapters/ch07-multiplayer.md) | Social incentives matter | Does individual optimization harm team or match experience? |
| 8 | [Motivation and Implementation](chapters/ch08-motivation-implementation.md) | Rewards shape behavior | Does the loop build mastery or later remorse? |
| 9 | [Interface](chapters/ch09-interface.md) | Information is missed | How can an AI intention survive partial attention? |
| 10 | [Market](chapters/ch10-market.md) | Positioning is vague | Which player receives a distinctive experience promise? |
| 11 | [Planning and Iteration](chapters/ch11-planning-iteration.md) | A team needs learning | What single risky assumption should the next build test? |
| 12 | [Creating Knowledge](chapters/ch12-creating-knowledge.md) | Debate is intuition-only | What kind of evidence would change our mind? |
| 13 | [Dependencies](chapters/ch13-dependencies.md) | Rework spreads through a system | Which lower-level AI capability is still unproven? |
| 14 | [Power](chapters/ch14-power.md) | Ownership is unclear | Who owns the experience outcome and what is non-negotiable? |
| 15 | [Drive](chapters/ch15-drive.md) | Momentum is falling | Can the team see meaningful, playable progress? |
| 16 | [Complex Decisions](chapters/ch16-complex-decisions.md) | A costly commitment is approaching | How reversible is the decision and how strong is the evidence? |
| 17 | [Values](chapters/ch17-values.md) | Learning culture matters | Can the team expose observations and counterevidence safely? |

---

## Core models

The reference file [core-models.md](references/core-models.md) contains compact reasoning tools. These are not scorecards; use the model that matches the actual uncertainty.

| Model | Purpose | Output artifact |
|---|---|---|
| Emotional Forecast | Define how expectation and feeling should change | Experience brief |
| Experience Bridge | Align mechanics, fiction, and presentation | Consistency audit |
| Decision Field | Make choice quality visible | Encounter decision map |
| Readability Stack | Make consequential system behavior legible | AI cue plan |
| Challenge Decomposition | Locate the layer of player failure | Difficulty diagnosis |
| Reward Expectation Loop | Audit what rewards train | Motivation map |
| Hypothesis Loop | Turn a claim into evidence | Greybox / playtest plan |
| Dependency Stack | Prevent cascading rework | Capability dependency map |
| Decision Portfolio | Sequence costly commitments | Decision card |

---

## Six end-to-end workflows

The detailed templates live in [workflows.md](references/workflows.md). Use them as project artifacts, not as paperwork for its own sake.

### 1. Experience Brief

Use before implementation when a feature is still an intention.

```markdown
## Target player and situation
## Intended emotional transition
## Core player verb and forecast
## System constraints and player-visible evidence
## Risks and unknowns
## Minimum validation experiment
```

The brief should explain why a feature exists in terms a designer, engineer, artist, and producer can all test.

### 2. AI Behavior Specification

Use for enemies, companions, NPCs, crowds, directors, or LLM-driven characters.

```markdown
## Player-facing role
## Observable states and readable cues
## Goals, inputs, and decision policy
## Actions, limits, and fallback
## Player choices and recovery paths
## Test cases and telemetry
```

This keeps a behavior tree, utility system, planner, or model call connected to what a player can actually understand and respond to.

### 3. Encounter Decision Audit

Use for combat, stealth, puzzles, traversal, dialogue, and resource loops.

For each important moment, list:

1. What the player can observe.
2. Which responses are genuinely viable.
3. The cost, risk, and counterplay of each response.
4. What feedback teaches the next attempt after failure.

### 4. Playtest Protocol

Use when “we should playtest it” needs to become a learning activity rather than a collection of opinions.

Define the exact question before recruiting players. Observe behavior before asking for explanation. Decide in advance what evidence will preserve, change, or discard the current hypothesis.

### 5. Reward and Motivation Audit

Use for progression, quests, daily loops, loot, achievements, social rewards, and monetized incentives.

Map: trigger → player behavior → reward → new expectation → post-session feeling. Look for a loop that trains compulsive compliance while weakening mastery, autonomy, or trust.

### 6. Cross-Functional Decision Card

Use when a decision spans design, engineering, art, narrative, production, data, or player safety.

Record the experience intent, non-negotiable constraints, owner, dependencies, options, evidence, risks, decision date, and follow-up experiment.

---

## Examples

These examples are deliberately small. They show how to turn a question into an artifact a team can act on.

- [AI Companion Specification](examples/ai-companion-spec.md): preserve player initiative while coordinating cover.
- [Combat Decision Audit](examples/combat-decision-audit.md): locate a dominant tactic before adding more actions.
- [Playtest Protocol](examples/playtest-protocol.md): test whether an enemy charge is readable before changing difficulty.

### A short example

Instead of writing:

> The companion should choose the highest-scoring cover position.

Write:

> The companion should make the player feel supported under pressure without taking tactical initiative away. Before claiming cover, it must make its intended movement readable; when a conflict occurs, the player's current and nearest escape routes have priority. Test this in a two-cover greybox encounter and measure route conflicts, player explanations, and death attribution.

The second version is implementable, reviewable, and testable without pretending the underlying algorithm is the experience.

---

## Repository structure

```text
game-experience-designer/
├── SKILL.md                  # Agent workflow and routing
├── chapters/                 # 17 practical chapter guides
├── references/
│   ├── core-models.md        # Compact reasoning tools
│   └── workflows.md          # Repeatable project artifacts
├── examples/                 # Small applied examples
├── glossary.md               # Core terminology
├── patterns.md               # Reusable design patterns
├── cheatsheet.md             # Fast diagnosis map
├── AGENTS.md                 # Generic agent integration guidance
└── agents/openai.yaml        # Codex UI metadata
```

---

## Installation and use

Clone the repository into your Codex skills directory:

```powershell
git clone https://github.com/powpow-TD/game-experience-designer $env:USERPROFILE\.codex\skills\game-experience-designer
```

Then use natural task language. For example:

### Quick prompts

1. `Use game-experience-designer to turn this enemy concept into an AI behavior specification. Include player-facing role, readable states, fallback behavior, recovery paths, and a greybox test.`
2. `Use game-experience-designer to diagnose why our stealth encounter has one dominant strategy. Produce a decision field and the smallest prototype we should run next.`

```text
Use game-experience-designer to turn this enemy concept into an AI behavior specification.
Include player-facing role, readable states, fallback behavior, recovery paths, and a greybox test.
```

```text
Use game-experience-designer to diagnose why our stealth encounter has one dominant strategy.
Produce a decision field and the smallest prototype we should run next.
```

```text
Use game-experience-designer to create a playtest protocol for an LLM NPC memory system.
Focus on expectation management, player trust, and graceful fallback.
```

---

## Extending it for a project

Keep project-specific information outside the core book-derived material. Good extensions include:

- A game's target-player and experience-principle document.
- A shared vocabulary for AI states, tactics, animation tags, and telemetry.
- A decision-card template that matches the team's planning process.
- Domain constraints for online safety, platform policy, accessibility, performance, or localization.
- Recorded lessons from playtests and shipped features.

The useful pattern is: preserve the core model, add concrete project constraints, then link every new rule to player evidence or an explicit assumption.

---

## Contribution guidance

Useful contributions improve operational clarity without reproducing the source work. Examples:

- Better English phrasing or corrected terminology.
- New examples based on original, fictional game scenarios.
- Clearer workflow templates or evidence fields.
- Integration notes for other coding agents.
- Project-agnostic game-AI practice patterns that state their trade-offs.

Do not submit scans, OCR, long quotations, figures, or other copyrighted source material.

---

## Source and license

This repository is inspired by Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences*. Consult the original book for authoritative wording and full context.

Repository-original material is licensed under [CC BY-NC-SA 4.0](LICENSE). Rights in cited source works remain with their respective rightsholders.
