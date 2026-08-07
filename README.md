# AI Game Experience Design

> A practical skill for designing AI-driven game experiences that players can understand, influence, trust, and enjoy.

## Purpose

This repository focuses exclusively on the player experience of game AI: enemies, bosses, companions, systemic NPCs, LLM characters, adaptive difficulty, procedural agents, and AI-driven interface feedback.

It treats an AI feature as an experience contract. The central questions are: What role does this AI play for the player? What can the player observe, predict, influence, and recover from? What does the AI promise, and what happens when it reaches its limits?

## What it helps you build

| AI feature | Core artifact |
|---|---|
| Enemy or boss | Readable state, commitment, counterplay, recovery, difficulty variables |
| Companion | Support promise, player-priority rules, coordination cues, fallback, trust metrics |
| NPC or LLM character | Persona, memory scope, tool authority, action boundary, refusal behavior, privacy limits |
| Adaptive difficulty | Adjustment signals, protected achievements, disclosure, fairness tests |
| AI playtest | Hypothesis, greybox scene, player task, explanation prompts, telemetry, decision rule |
| AI safety/trust | Misrepresentation, manipulation, bias, privacy, emotional dependency, escalation paths |

## Knowledge structure

- **17 AI-focused chapters**: from experience intent and readable behavior to LLM boundaries and player trust.
- **AI experience principles**: player-facing role, agency budget, failure contract, honest adaptation, and evidence triangulation.
- **Seven workflows**: reusable specifications and plans for AI technical design.
- **Examples**: companion behavior, LLM NPC boundary, adaptive difficulty, combat decisions, and AI playtesting.

## Example prompts

```text
Use ai-game-experience-design to write a companion AI specification for a tactical shooter. Protect player agency, describe readable commitments and fallback behavior, then propose a greybox playtest.
```

```text
Use ai-game-experience-design to define the authority boundary for an LLM quest-giver. Include memory scope, executable actions, refusals, world consequences, privacy limits, and trust tests.
```

## Install

```powershell
git clone https://github.com/powpow-TD/ai-game-experience-design $env:USERPROFILE\.codex\skills\ai-game-experience-design
```

## Source and license

The original practical foundations were inspired by Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences*, extended here for AI game experience design. This repository contains no scans, OCR, long quotations, or figures from the source work.

Repository-original material is licensed under [CC BY-NC-SA 4.0](LICENSE). Rights in cited source works remain with their respective rightsholders.
