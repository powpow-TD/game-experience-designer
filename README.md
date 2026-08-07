# Game Experience Designer

> A 40-lens, evidence-first review protocol for game AI, mechanics, UI, narrative, rewards, difficulty, and playtests.

## Why this exists

Most design reviews collapse trade-offs into a confident list of fixes. That is particularly harmful in game AI: “smarter,” “more realistic,” and “more content” are not player experiences. This skill keeps the designer in charge. It selects a small set of relevant experience lenses, surfaces competing readings, and turns the result into a minimal test.

## What it produces

For every selected lens, the review provides:

1. A specific question
2. An observation tied to the artifact, behavior, or data
3. A credible counter-reading
4. Two or three directions, each with an explicit benefit and cost

It ends with a minimum validation plan: hypothesis, scene, player task, signals, thresholds, and a keep/change/kill rule. See the [full AI companion example](examples/ai-companion-cover-review.md).

## The 40 lenses

The library is organized into seven practical groups:

| Group | Lenses | Typical use |
|---|---|---|
| Experience | E01–E03 | Emotional promise, expectation, theme-mechanics alignment |
| Systems & skill | E04–E08 | Emergence, readability, difficulty, recovery, mastery |
| Narrative & decision | E09–E16 | Agency, character consistency, choice, information, fairness, balance |
| Multiplayer & motivation | E17–E20 | Cooperation, mind games, rewards, remorse |
| Interface & market | E21–E26 | Signals, redundant cues, guidance, input, positioning |
| Process & culture | E27–E36 | Prototypes, evidence, dependencies, ownership, learning |
| Game AI | E37–E40 | Intent surfaces, failure contracts, companion coordination, LLM boundaries |

Read the full [lens library](references/experience-lenses.en.md).

## How it works

1. Identify the artifact's player, experience goal, evidence, and uncertainty.
2. Select only 3–5 relevant lenses.
3. Produce trade-off-aware directions rather than a single prescription.
4. Design the smallest test that could disconfirm the leading assumption.

The included `scripts/select_lenses.py` ranks candidate lenses from a local artifact. It is a routing aid, not a replacement for judgment.

## Install

```powershell
git clone https://github.com/powpow-TD/game-experience-designer $env:USERPROFILE\.codex\skills\game-experience-designer
```

Then ask Codex:

```text
Use game-experience-designer to review this AI or mechanic proposal. Focus on player expectation, decision quality, readable evidence, and a minimum playtest.
```

## Extend

Add project-specific lenses as `PX01`, `PX02`, and so on. Keep the same six fields used by the library: Category, Use when, Key question, Failure pattern, Design move, and Selection keywords. This works well for LLM input, live-service constraints, platform policy, or project-specific experience principles.

## Source and license

This repository is an original operational synthesis inspired by Tynan Sylvester's *Designing Games: A Guide to Engineering Experiences*. It contains no scans, OCR, long excerpts, or figures. Consult the original work for authoritative wording and full context.

Repository-original material is licensed under [CC BY-NC-SA 4.0](LICENSE). Rights in cited source works remain with their respective rightsholders.
