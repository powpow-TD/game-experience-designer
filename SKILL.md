---
name: game-experience-designer
description: "Review game design artifacts through 40 experience-design lenses. Use for GDDs, vision documents, ADRs, mechanic specs, prototypes, game AI, combat, NPCs, quests, UI, rewards, difficulty, narrative consistency, playtests, or player-experience risks. Select 3–5 relevant lenses and produce evidence-based observations, counter-readings, option sets with trade-offs, and a minimum validation plan."
---

# Game Experience Designer

## Workflow

1. Identify the artifact, player, target experience, constraints, evidence, and unknowns.
2. Read [the lens library](references/experience-lenses.en.md); select three to five lenses that cover the actual risk, not every possible concern.
3. For each lens, provide the lens question, an evidence-bound observation, a credible counter-reading, and two or three directions with explicit trade-offs.
4. Separate immediate experiments, prototype work, research/data work, and cross-functional decisions.
5. End with one minimum validation plan: hypothesis, scene, player task, observable signals, threshold, and keep/change/kill decision.

## Output contract

```markdown
## Experience Summary
## Evidence and Unknowns
## Selected Lenses
### E##: Lens Name
**Question**:
**Observation**: Cite artifact text, behavior, or data. Mark inference as inference.
**Counter-reading**:
**Directions**:
- A. … — Benefit: … — Cost: …
- B. … — Benefit: … — Cost: …
## Minimum Validation Plan
- Hypothesis:
- Minimal scene and player task:
- Signals and thresholds:
- Keep / Change / Kill rule:
## Skipped Lenses
```

## Behavioral rules

- Use calibrated language: “may,” “one reading is,” and “needs validation.”
- Do not prescribe a single correct design; preserve the designer's decision rights.
- Prefer evidence to rhetoric. State what is unknown.
- Use fewer lenses for a narrow artifact. A review with three sharp lenses is better than five generic ones.

## Resource routing

- Read `references/experience-lenses.en.md` for lens definitions and selection.
- Run `python scripts/select_lenses.py <artifact-path>` for a keyword-ranked candidate set; review the result before using it.
- Read `examples/` when the user needs an output model.
- Read a file in `chapters/` only when book-level context is necessary.

## Custom lenses

Append project lenses as `PX01`, `PX02`, and so on. Preserve Category, Use when, Key question, Failure pattern, Design move, and Selection keywords.

## Limits

This skill is an experience-design review protocol. It does not replace user research, legal review, accessibility testing, performance profiling, or ownership of final design decisions.
