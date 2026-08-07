# Example Review: An AI Companion Takes the Player's Cover

## Experience Summary

The intended experience is reliable support under pressure while the player keeps tactical initiative. Playtest notes say the companion “got me killed” after taking the nearest cover point.

## Evidence and Unknowns

The behavior spec optimizes for nearest high-score cover. It does not describe player-priority reservations, intent cues, or a recovery path. We do not yet know whether players object to the move itself or to losing their only visible escape route.

### E39: Companion Coordination
**Question**: How do companion goals negotiate space, timing, and player priority?

**Observation**: Local cover scoring can be rational for the companion while still removing the player's best option.

**Counter-reading**: Unpredictable ally movement might support battlefield chaos; the harmful case may be limited to narrow arenas.

**Directions**:
- A. Reserve the player's current and nearest escape cover. — Benefit: protects agency. — Cost: reduces companion tactical efficiency.
- B. Negotiate cover claims with a short pre-move cue and expiry. — Benefit: legible coordination. — Cost: extra animation, VO, and state complexity.

### E22: Diverse Redundancy
**Question**: Can the player receive the companion's commitment through more than one channel?

**Observation**: The current spec has no spatial marker, gesture, or audio cue for a cover claim.

**Counter-reading**: Strong cues may over-instrument a tense firefight.

**Directions**:
- A. Use a subtle body turn plus a contextual line. — Benefit: diegetic clarity. — Cost: can be missed in noise.
- B. Add a brief ground reservation marker only when paths conflict. — Benefit: high clarity at the critical moment. — Cost: UI intrusion.

## Minimum Validation Plan
- **Hypothesis**: Player-priority reservation plus one diegetic cue will halve “ally caused my death” attribution without reducing the companion's perceived usefulness.
- **Scene**: A greybox firefight with two safe cover points and one enemy push.
- **Signals**: Escape-route use, collision/cover conflicts, death attribution, post-task explanation of companion intent.
- **Threshold**: At least 70% of players can explain the companion's move; negative attribution is below half the baseline.
- **Decision**: Keep the approach if both thresholds hold; otherwise test arena topology before adding more UI.
