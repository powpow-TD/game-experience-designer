# AI Implementation Choice

## Decide from the player need outward

1. Name the player-facing role and the decision the player must retain.
2. List consequential decisions at each layer: perception, world knowledge, goal selection, tactical choice, motion, presentation.
3. Pick one accountable owner for each decision.
4. Choose the least complex architecture that makes the decision inspectable and replayable.
5. Prototype the hardest-to-reverse boundary in a small player-readable scene.

## Selection checklist

| Question | Likely direction |
|---|---|
| Is the problem mainly stable modes and explicit transitions? | FSM/HFSM |
| Is it authored priority and interruption? | behavior tree with explicit blackboard/world queries |
| Is it preference trade-off among comparable options? | utility scoring with visible inputs and score diagnostics |
| Is it long-horizon constrained sequencing? | planner, HTN, search, or a narrow planning layer |
| Does it require player-visible spatial opportunity? | tactical query / influence / reservation layer before selection |
| Does it require many agents without full-fidelity simulation? | LOD or event simulation with preserved player-facing consequences |

## Architecture review prompts

- Which player-observable rule would this architecture make hard to explain?
- What information is stale, uncertain, or too expensive to compute?
- What happens when planning fails, a path is blocked, or a player changes the scene?
- Where can design inspect and alter behavior without changing unrelated systems?
- What testing hook proves the important invariant?

## Output

Write a one-page ADR: experience claim, alternatives, selected ownership boundaries, observability plan, prototype, risk, reversal trigger, and evidence date.
