# Experience Engineering for AI

This reference translates experience-design reasoning into AI design decisions.

## Work from the player's forecast

The important unit is not a raw AI event. It is the loop below:

| Moment | Design question | Example: enemy charge |
|---|---|---|
| Cue | What becomes noticeable? | stance change, audio, clear route |
| Forecast | What future does the player infer? | "I will be displaced if I stay." |
| Choice | What meaningful response exists? | dodge, interrupt, reposition, bait |
| Resolution | What confirms the rule? | charge follows the telegraph and has recovery |
| Learning | What carries into the next encounter? | player predicts timing and counter |

If the forecast is wrong because the system is inconsistent, fix the rule or cue. If the forecast is right but there is no meaningful response, fix player leverage.

## Separate experience variables from implementation variables

| Experience variable | Possible implementation variable | Do not confuse them |
|---|---|---|
| apprehension | sight range, sound, wind-up, route visibility | larger radius is not automatically more tension |
| mastery | counter window, rule consistency, feedback | lower win rate is not automatically more challenge |
| companionship | priority policy, spacing, acknowledgement | better pathfinding is not automatically more support |
| world credibility | schedules, perception, social memory, ambient rules | more simulation is not automatically more believable |
| discovery | information gating, agent hinting, spatial behavior | more hints are not automatically more clarity |

Start with a target experience variable and test whether the implementation changes it.

## Protect the decision that carries the feeling

Before an AI feature acts, identify the decision that creates the intended feeling. Preserve it unless the feature deliberately changes the fantasy.

- For tactical pressure, preserve route, target, timing, and risk assessment.
- For a companion, preserve the player's tactical initiative and recovery route.
- For a director, preserve the legitimacy of victory, defeat, and learning.
- For an LLM NPC, preserve the player's understanding of what is fiction, memory, and executable consequence.

## Use a minimum meaningful scene

Build the smallest scene in which the player can notice a rule, make a response, and see a consequence. Do not validate a behavior system only in a debug sandbox or validate a large content set before that loop works.

## Diagnose by broken link

| Player report | Likely broken link | First intervention |
|---|---|---|
| "That came out of nowhere." | cue -> forecast | add or clarify commitment; inspect state transition |
| "I knew, but could not do anything." | forecast -> choice | add counter, time, route, or resource |
| "Sometimes it works, sometimes not." | rule -> resolution | remove hidden exceptions; add trace assertion |
| "It plays the game for me." | choice -> authorship | return target, route, timing, or resource authority |
| "It talks like it can do anything." | promise -> authority | constrain tools, memory, claims, and fallback |
