# AI Game Experience Design

> A practical skill for designing AI-driven game experiences that players can understand, influence, trust, and enjoy.

## Purpose

This repository focuses exclusively on the player experience of game AI: enemies, bosses, companions, systemic NPCs, LLM characters, adaptive difficulty, procedural agents, and AI-driven feedback.

It treats every AI feature as an **experience contract**. The central questions are: what role does the AI play for the player; what can the player observe, predict, influence, and recover from; what does the AI promise; and how does it behave at its limits?

The repository is an original operational synthesis inspired by Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences*. It is for game designers, technical designers, game-AI designers, and cross-functional teams who need to turn an AI idea into observable player behavior and a testable implementation plan.

---

## Why this exists

Teams often describe AI through implementation:

- “The companion should choose the best cover.”
- “The enemy should flank more intelligently.”
- “The NPC should remember previous conversations.”
- “The director should keep the player challenged.”

Those statements omit the design question that matters: what should the player predict, feel, understand, decide, and learn?

An internally capable system can still create a poor experience. A companion can optimize cover while trapping the player. A difficult enemy can be numerically fair but unreadable. An LLM NPC can sound convincing while promising world actions the game cannot perform. An adaptive system can remove frustration while also invalidating a player's sense of earned success.

This skill turns implementation discussion into an AI experience-engineering loop:

```text
Player and situation
        ↓
Player-facing AI role and intended feeling
        ↓
Visible cues, agency budget, authority, and limits
        ↓
Choices, risks, recovery, and trust boundaries
        ↓
Minimum prototype or playtest
        ↓
Behavior + explanation + telemetry → decision → next iteration
```

---

## What this skill produces

| Situation | Practical artifact |
|---|---|
| An AI idea is vague | AI Experience Brief: player, feeling, role, agency, limits, risks |
| An enemy or boss needs definition | Enemy AI Specification: readable states, commitments, counters, recovery, tests |
| A companion frustrates players | Companion Specification: player-priority rules, coordination cues, fallback, trust metrics |
| An NPC uses LLM dialogue | NPC / LLM Interaction Specification: memory, tools, authority, refusal, consequence, privacy |
| Difficulty feels rigged | Adaptive Difficulty Plan: adjustment signals, protected achievements, fairness tests |
| A team needs evidence | AI Playtest Protocol: hypothesis, greybox scene, explanation prompts, telemetry, thresholds |
| A risk crosses disciplines | AI Trust Review: misrepresentation, manipulation, bias, privacy, dependency, escalation |

---

## Core AI experience principles

### 1. Player-facing role before algorithm choice

Define whether an AI creates pressure, support, discovery, rivalry, companionship, world credibility, or practice. “Uses a planner” is implementation, not player value.

### 2. Legibility before cleverness

Players cannot value decisions they cannot perceive. Make consequential goals, commitments, limits, and recovery visible through behavior, space, animation, sound, and restrained UI.

### 3. Agency budget before automation

Every AI intervention spends player agency. Remove friction without automating the decisions that make the experience meaningful. Protect player routes, resources, timing, and authorship.

### 4. Failure contract before scale

Specify how an AI can fail, how a player notices, what fallback occurs, and what recovery remains. This is crucial for companions, procedural agents, and LLM characters.

### 5. Honest adaptation before retention optimization

Adapt pressure, information, pacing, or support while preserving the meaning of earned outcomes. Do not silently rewrite a result the player believes they achieved.

### 6. Executable authority before conversational promise

NPC memory, dialogue, promises, and world actions must stay within real system authority. A graceful limitation protects trust better than a fabricated consequence.

### 7. Evidence before certainty

Use telemetry for behavior, observation for moment-to-moment friction, player explanation for mental models, and interviews for meaning. No one source proves experience quality.

---

## The AI knowledge map

The 17 chapter guides convert the source's practical domains into AI-specific application guidance.

| # | Domain | Use it when | Typical question |
|---|---|---|---|
| 1 | AI Experience Intent | Defining an AI feature | What feeling and future should this AI create? |
| 2 | Legible AI Simplicity | Rules become opaque | Can players learn why the AI acts? |
| 3 | Adaptive Challenge | Difficulty feedback conflicts | Which player skill layer actually failed? |
| 4 | NPC Agency and Story | NPC behavior affects fiction | Can dialogue, memory, and action make the same promise? |
| 5 | Human-AI Decisions | AI removes or creates choices | What can the player predict, risk, and influence? |
| 6 | AI Strategy and Balance | AI counters dominate | Are alternatives readable and viable? |
| 7 | Social AI and Bots | Groups and competition matter | Does local optimization damage the match? |
| 8 | Motivation and Personalization | AI adjusts rewards or support | Does adaptation reinforce mastery and autonomy? |
| 9 | AI Cues and Interface | Intent is missed | What signal survives partial attention? |
| 10 | AI Product Promise | Feature positioning is vague | Can the player experience the promised capability? |
| 11 | AI Prototyping and Iteration | A team must learn quickly | What single AI experience claim should the next build test? |
| 12 | AI Evidence and Telemetry | Debate is intuition-only | What evidence would change our mind? |
| 13 | AI Dependency Stack | Rework spreads through a system | Which lower-layer capability is unproven? |
| 14 | AI Ownership and Explainability | Responsibility is unclear | Who owns the player outcome and how is behavior inspected? |
| 15 | AI Team Learning | Momentum falls | Can makers see playable, validated progress? |
| 16 | AI Architecture Decisions | A costly commitment approaches | How reversible is the decision and what experience does it enable? |
| 17 | AI Values and Trust | Trust risks appear | What does the AI know, do, hide, and fail at? |

---

## Seven end-to-end workflows

Detailed templates live in [workflows.md](references/workflows.md). Use them as working artifacts, not paperwork.

1. **AI Experience Brief** — define target player, feeling, role, agency budget, cues, limits, risks, and success signal.
2. **Enemy AI Specification** — define combat fantasy, states, target selection, commitments, counters, recovery, and difficulty variables.
3. **Companion AI Specification** — define support promise, player-priority rules, space negotiation, yield behavior, fallback, and trust metrics.
4. **NPC / LLM Interaction Specification** — define persona, memory scope, tool authority, action boundary, refusal, consequence model, and privacy limits.
5. **Adaptive Difficulty Plan** — define signals, adjustable variables, protected achievements, disclosure, stop conditions, and fairness tests.
6. **AI Playtest Protocol** — define one experience hypothesis, greybox scene, player task, explanation prompts, telemetry, thresholds, and decision rule.
7. **AI Risk and Trust Review** — define risks around deception, manipulation, bias, privacy, emotional dependency, safety, and escalation.

---

## Examples

- [AI Companion Specification](examples/ai-companion-spec.md): preserve player initiative while coordinating cover.
- [LLM NPC Boundary](examples/llm-npc-boundary.md): align memory, promises, and world authority.
- [Adaptive Difficulty Plan](examples/adaptive-difficulty-plan.md): adapt without invalidating earned success.
- [AI Playtest Protocol](examples/playtest-protocol.md): test whether an enemy charge is readable before changing numbers.

### A short example

Instead of writing:

> The companion should choose the highest-scoring cover position.

Write:

> The companion should make the player feel supported under pressure without taking tactical initiative away. Before claiming cover, it must make the movement readable; when a conflict occurs, the player's current and nearest escape routes have priority. Test this in a two-cover greybox encounter and measure route conflicts, player explanations, and death attribution.

The second version is implementable, reviewable, and testable without confusing an optimization rule with the experience itself.

---

## Repository structure

```text
ai-game-experience-design/
├── SKILL.md                         # Agent workflow and output templates
├── chapters/                        # 17 AI-focused chapter guides
├── references/
│   ├── ai-experience-principles.md  # Core AI experience reasoning
│   └── workflows.md                 # Seven reusable project artifacts
├── examples/                        # Applied AI design examples
├── glossary.md                      # AI experience vocabulary
├── patterns.md                      # Reusable design patterns
├── cheatsheet.md                    # Fast AI diagnosis map
├── AGENTS.md                        # Generic agent integration guidance
└── agents/openai.yaml               # Codex UI metadata
```

---

## Installation and use

```powershell
git clone https://github.com/powpow-TD/ai-game-experience-design $env:USERPROFILE\.codex\skills\ai-game-experience-design
```

Example prompts:

```text
Use ai-game-experience-design to write a companion AI specification for a tactical shooter. Protect player agency, describe readable commitments and fallback behavior, then propose a greybox playtest.
```

```text
Use ai-game-experience-design to define the authority boundary for an LLM quest-giver. Include memory scope, executable actions, refusals, world consequences, privacy limits, and trust tests.
```

---

## Extending for a project

Keep project-specific information outside the core book-derived material. Useful additions include an AI-state vocabulary, animation and telemetry naming, target-player principles, online-safety constraints, platform requirements, and documented lessons from playtests. Link every new rule to player evidence or an explicit assumption.

## Contribution guidance

Useful contributions improve AI experience clarity without reproducing source material: new fictional examples, clearer workflow fields, trade-off-aware game-AI patterns, and integration notes. Do not submit scans, OCR, long quotations, figures, or copyrighted source material.

## Source and license

The practical foundations were inspired by Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences*, extended here for AI game experience design. This repository contains no scans, OCR, long quotations, or figures from the source work.

Repository-original material is licensed under [CC BY-NC-SA 4.0](LICENSE). Rights in cited source works remain with their respective rightsholders.
