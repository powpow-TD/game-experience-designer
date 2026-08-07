# AI Experience Principles

## Anticipated futures are part of the experience

Players continuously forecast what an AI might do. Design the forecast deliberately: expose a cue, define the possible consequence, give the player a response, resolve it, then let the result update their model. Surprise is valuable only when the player can retrospectively learn a rule rather than conclude that the system is arbitrary.

## Legibility, leverage, and reliability form one quality bar

- **Legibility**: the player can form a useful explanation of consequential behavior.
- **Leverage**: the player has meaningful influence, counterplay, or authorship around that behavior.
- **Reliability**: the system respects its visible rules often enough for learning and trust.

Optimize all three. An impressive but opaque agent fails legibility; a helpful companion that takes over fails leverage; a readable agent with flaky execution fails reliability.

## Design the commitment, not only the action

An action is usually too late to communicate. Give consequential actions a commitment phase: wind-up, target lock, movement route, spoken intent, spatial reservation, or UI mark. Then define cancellation, interruption, and recovery. This converts internal decision state into a player decision.

## Agency is budgeted, not binary

Every intervention removes or reframes some choice. List protected choices before adding assistance: player path, target, timing, resource, strategy, authorship, and social consent. Automate only friction that does not carry the intended learning, drama, or expression.

## Preserve an honest competence model

Difficulty and personalization may adjust pressure, information, pacing, or support. They must not quietly change the meaning of a result the player believes they earned. Keep protected achievements, use bounded adjustments, and run fairness tests with informed and uninformed players.

## Separate conversational fluency from world authority

For LLM characters, specify memory scope, tools, allowed facts, action authority, refusal behavior, and persistence. Dialogue cannot promise an object, quest consequence, relationship change, or safety guarantee that the simulation cannot execute.

## Treat AI failure as a designed interaction

For every consequential failure, define detection, player-facing explanation, fallback, compensation if appropriate, and recovery. A hidden fallback can be useful for robustness but cannot conceal a result-changing intervention.

## Evidence has four distinct jobs

| Evidence | Answers |
|---|---|
| Behavior trace / replay | What did the system do? |
| Observation | Where did attention, hesitation, or frustration occur? |
| Player explanation | What rule did the player infer? |
| Telemetry / experiment | How often and for whom does the pattern recur? |

Do not collapse these into a single "fun score."
