# NPC, Social Simulation, and LLM Characters

## Separate four layers

| Layer | Question |
|---|---|
| Presentation | What personality, voice, and social cue is expressed? |
| Knowledge | What facts, beliefs, uncertainty, and memory can the character hold? |
| Authority | Which tools and world actions can it actually execute? |
| Consequence | What persistent state visibly changes after the action? |

Never let a fluent presentation invent authority or consequence.

## Social and systemic NPCs

Use schedules, perceptions, knowledge representation, relationships, ambient rules, and world queries to create credible local behavior. Prefer a small causal rule set that produces readable consequences over broad simulation that players cannot observe or influence.

## LLM authority boundary

Specify allowed knowledge, memory retention, tool calls, action confirmation, forbidden claims, refusal voice, out-of-world fallback, privacy/consent, moderation/escalation, and logging. If the system cannot execute a promise, have the character explain the limit or direct the player to an executable route.

## Evaluation

Test continuity, player inference of capability, false-promise rate, consequence visibility, safe recovery, and player trust. Do not score an LLM character only by prose quality.
