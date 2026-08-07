# AI Experience Diagnosis Card

| Signal from players or team | Inspect first | Likely action |
|---|---|---|
| "It came out of nowhere." | commitment cue and perception trace | make the state/intent visible earlier; remove contradictory interrupts |
| "I knew it was coming but had no answer." | player leverage | add a route, timing, tool, resource, or interruption window |
| "The enemy feels random." | rule consistency and utility/planning inputs | simplify priorities; expose high-impact conditions; replay edge cases |
| "The companion ruined my plan." | resource and space reservation | protect player route/target/cover first; add yield and acknowledgement |
| "Difficulty is cheating." | adaptation contract | protect outcome; bound knobs; disclose or reduce intervention |
| "The world is lifeless." | visible causal loop | add a small readable reaction/consequence, not indiscriminate simulation |
| "The NPC promised something impossible." | authority boundary | constrain tools and claims; add in-character executable fallback |
| "We cannot debug it." | trace and inspectability | add state, goal, score/plan, path, reservation, and fallback visualization |
| "Metrics improved but play is worse." | evidence type mismatch | pair telemetry with explanation prompts and observation |

## Fast architecture choice

- Discrete, stable modes -> FSM/HFSM.
- Authored priorities and interrupts -> behavior tree.
- Continuous trade-offs -> utility scoring.
- Long constrained sequences -> planner/HTN/search.
- Large populations -> LOD/event simulation; preserve visible causality.
- Multiple answers -> hybrid with one owner per boundary.
