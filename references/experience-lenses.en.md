# Game Experience Lens Library

Use this library as the skill's single source of truth. Select three to five lenses per review; never turn it into a checklist.

## Categories

- Experience: E01–E03
- Systems and Skill: E04–E08
- Narrative and Decision: E09–E16
- Multiplayer and Motivation: E17–E20
- Interface and Market: E21–E26
- Process, Production, and Culture: E27–E36
- Game AI: E37–E40

## E01: Emotional Promise

**Category**: Experience

**Use when**: Define the desired player feeling.

**Key question**: What future does the player emotionally anticipate?

**Failure pattern**: Feature lists with no felt purpose.

**Design move**: State the emotional transition before choosing mechanics.

**Selection keywords**: emotion feeling tension relief wonder

## E02: Expectation Gap

**Category**: Experience

**Use when**: A beat feels flat, unfair, or manipulative.

**Key question**: Which expectation changes, and is the change legible?

**Failure pattern**: Treating surprise as inherently good.

**Design move**: Map prediction → event → revised prediction.

**Selection keywords**: expectation surprise unfair twist

## E03: Experience Bridge

**Category**: Experience

**Use when**: Mechanics and fiction feel disconnected.

**Key question**: Do system events and fiction reinforce the same feeling?

**Failure pattern**: Narrative paint over contradictory rewards.

**Design move**: Align verbs, consequences, and story meaning.

**Selection keywords**: theme fiction mechanics narrative

## E04: Elegant Emergence

**Category**: Systems

**Use when**: Rules are multiplying.

**Key question**: Can a small rule set yield varied, understandable situations?

**Failure pattern**: Adding exceptions to simulate depth.

**Design move**: Prefer composable rules with visible causes.

**Selection keywords**: emergence rules systems complexity

## E05: Learnable Causality

**Category**: Systems

**Use when**: Players call AI random or opaque.

**Key question**: Can players infer why the system acted?

**Failure pattern**: Hidden state with no visible consequence.

**Design move**: Expose intent through behavior and feedback.

**Selection keywords**: ai readable random state feedback

## E06: Elastic Challenge

**Category**: Skill

**Use when**: Difficulty feedback polarizes.

**Key question**: Is failure caused by perception, execution, planning, or coordination?

**Failure pattern**: Only scaling health or damage.

**Design move**: Tune the failing layer and preserve recovery.

**Selection keywords**: difficulty challenge fail death skill

## E07: Recovery Path

**Category**: Skill

**Use when**: Failure causes quitting.

**Key question**: After failure, can players understand and re-enter play?

**Failure pattern**: Punishment without diagnosis or comeback.

**Design move**: Add information, recovery, or a smaller next goal.

**Selection keywords**: failure retry checkpoint frustration

## E08: Skill Range

**Category**: Skill

**Use when**: Newcomers and experts need different things.

**Key question**: Does the system permit entry, mastery, and expression?

**Failure pattern**: Making expertise mandatory at onboarding.

**Design move**: Separate baseline usability from mastery options.

**Selection keywords**: onboarding beginner expert mastery

## E09: Player Agency

**Category**: Narrative

**Use when**: Players feel railroaded.

**Key question**: Do actions change meaningfully within stated constraints?

**Failure pattern**: Offering cosmetic choices only.

**Design move**: Make consequences, trade-offs, or authorship observable.

**Selection keywords**: agency choice quest narrative

## E10: Character-System Consistency

**Category**: Narrative

**Use when**: Character writing conflicts with play.

**Key question**: Do missions and rewards validate the character's stated values?

**Failure pattern**: Rewarding behavior the fiction condemns.

**Design move**: Audit motivation, available verbs, and payoff together.

**Selection keywords**: character story quest reward consistency

## E11: World Storytelling

**Category**: Narrative

**Use when**: Exposition is heavy.

**Key question**: Can space, objects, routines, and consequences tell the story?

**Failure pattern**: Replacing interaction with explanation.

**Design move**: Embed evidence in playable world state.

**Selection keywords**: world environment storytelling lore

## E12: Decision Richness

**Category**: Decision

**Use when**: There is one dominant tactic or too many options.

**Key question**: Are there two or more forecastable, viable paths with different costs?

**Failure pattern**: Counting options as depth.

**Design move**: Design distinct predictions and trade-offs.

**Selection keywords**: decision strategy choice dominant

## E13: Information Balance

**Category**: Decision

**Use when**: Players guess or become overloaded.

**Key question**: What must be known, uncertain, scarce, or hidden?

**Failure pattern**: Hiding facts merely to create mystery.

**Design move**: Give enough evidence for intentional risk.

**Selection keywords**: information hidden uncertainty fog

## E14: Decision Rhythm

**Category**: Decision

**Use when**: Flow breaks or choices blur together.

**Key question**: When should thinking intensify and when should execution breathe?

**Failure pattern**: Constant high-stakes choice density.

**Design move**: Alternate commitment, feedback, and regrouping.

**Selection keywords**: flow pacing rhythm overload

## E15: Fair Readability

**Category**: Balance

**Use when**: Players blame the game for losses.

**Key question**: Can they explain outcome differences as decisions or execution?

**Failure pattern**: Untelegraphed reversals.

**Design move**: Signal causes before consequences matter.

**Selection keywords**: fairness unfair telegraph counterplay

## E16: Strategy Diversity

**Category**: Balance

**Use when**: Usage concentrates in one build or route.

**Key question**: Which strategy displaces others and why?

**Failure pattern**: Balancing only win rate.

**Design move**: Track pick rate, counterplay, cost, and learning burden.

**Selection keywords**: balance meta build winrate

## E17: Social Incentives

**Category**: Multiplayer

**Use when**: Cooperation breaks down.

**Key question**: Does individual optimization damage group experience?

**Failure pattern**: Assuming players naturally cooperate.

**Design move**: Align rewards, shared information, and anti-griefing.

**Selection keywords**: multiplayer team cooperation griefing

## E18: Mind Games

**Category**: Multiplayer

**Use when**: Competition is predictable.

**Key question**: Can players credibly vary intent without pure randomness?

**Failure pattern**: Confusing unpredictability with noise.

**Design move**: Create readable bluff, commitment, and counterplay.

**Selection keywords**: pvp bluff competitive prediction

## E19: Reward Expectation

**Category**: Motivation

**Use when**: Reward loops feel exploitative or empty.

**Key question**: What expectation does each reward schedule create?

**Failure pattern**: Adding rewards to compensate for weak play.

**Design move**: Reward learning, autonomy, and meaningful progress.

**Selection keywords**: reward loot dopamine retention

## E20: Player Remorse

**Category**: Motivation

**Use when**: Players regret time or purchases.

**Key question**: Does the loop create later resentment?

**Failure pattern**: Optimizing return rate alone.

**Design move**: Test post-session satisfaction, not only engagement.

**Selection keywords**: remorse grind monetization regret

## E21: Signal-to-Noise

**Category**: Interface

**Use when**: Important information is missed.

**Key question**: What competes for attention at the moment of choice?

**Failure pattern**: Adding another icon for every state.

**Design move**: Remove noise before adding a signal.

**Selection keywords**: ui hud signal noise attention

## E22: Diverse Redundancy

**Category**: Interface

**Use when**: A critical cue is often overlooked.

**Key question**: Can the same meaning arrive via behavior, space, sound, and UI?

**Failure pattern**: Repeating identical alerts.

**Design move**: Use different channels that corroborate each other.

**Selection keywords**: cue audio visual animation ui

## E23: Indirect Guidance

**Category**: Interface

**Use when**: Guidance breaks immersion.

**Key question**: Can the world invite the action without forcing the camera or modal?

**Failure pattern**: Hard-locking attention by default.

**Design move**: Use affordance, composition, movement, and sound.

**Selection keywords**: guidance tutorial waypoint immersion

## E24: Input Feel

**Category**: Interface

**Use when**: Controls feel unreliable.

**Key question**: What latency, assistance, mapping, and feedback shape perceived control?

**Failure pattern**: Treating input as implementation detail.

**Design move**: Prototype response and recovery before content.

**Selection keywords**: input control latency responsiveness

## E25: Value Curve

**Category**: Market

**Use when**: The concept lacks a clear audience reason.

**Key question**: Which experience dimensions are intentionally higher or lower than alternatives?

**Failure pattern**: Listing features without contrast.

**Design move**: Compare perceived value for a specific player.

**Selection keywords**: market audience positioning differentiation

## E26: Expectation Setting

**Category**: Market

**Use when**: Marketing and first play conflict.

**Key question**: What promise does onboarding make, and can play fulfill it?

**Failure pattern**: Selling an experience unavailable in the loop.

**Design move**: Align trailer, store copy, tutorial, and core play.

**Selection keywords**: marketing onboarding promise expectation

## E27: Hypothesis-Driven Iteration

**Category**: Process

**Use when**: A prototype cycle lacks learning.

**Key question**: What single risky experience claim will this build test?

**Failure pattern**: Building broadly before measuring.

**Design move**: Write hypothesis, minimal scene, signal, decision.

**Selection keywords**: prototype playtest iteration hypothesis

## E28: Greybox Fidelity

**Category**: Process

**Use when**: Production obscures what is being tested.

**Key question**: What is the cheapest representation that preserves the experience question?

**Failure pattern**: Polish before structural evidence.

**Design move**: Match prototype fidelity to uncertainty.

**Selection keywords**: greybox prototype polish production

## E29: Evidence Ladder

**Category**: Research

**Use when**: Design debate is opinion-only.

**Key question**: What claims are observations, data, interviews, or inference?

**Failure pattern**: Treating one quote as proof.

**Design move**: Label confidence and seek disconfirming evidence.

**Selection keywords**: data research telemetry interview evidence

## E30: Dependency Stack

**Category**: Production

**Use when**: Features keep being reworked.

**Key question**: Which unproven lower-layer capability does this depend on?

**Failure pattern**: Building content over uncertain foundations.

**Design move**: Validate perception → state → goal → action first.

**Selection keywords**: dependency architecture ai pipeline rework

## E31: Reversible Bets

**Category**: Production

**Use when**: A decision has broad, costly consequences.

**Key question**: How reversible is it and how strong is the evidence?

**Failure pattern**: Locking a platform-wide choice on intuition.

**Design move**: Experiment first on high-impact irreversible bets.

**Selection keywords**: risk architecture irreversible decision

## E32: Intent Ownership

**Category**: Collaboration

**Use when**: Teams implement different interpretations.

**Key question**: Who owns the experience result and what is non-negotiable?

**Failure pattern**: Assigning tasks without intent.

**Design move**: Communicate purpose, constraints, and autonomy.

**Selection keywords**: team ownership communication handoff

## E33: Progress Principle

**Category**: Collaboration

**Use when**: The team loses momentum.

**Key question**: Can contributors see meaningful validated progress?

**Failure pattern**: Measuring only task closure.

**Design move**: Ship small playable capability slices.

**Selection keywords**: milestone morale progress team

## E34: Decision Effects

**Category**: Leadership

**Use when**: A local fix creates second-order harm.

**Key question**: What changes downstream after this decision?

**Failure pattern**: Optimizing the immediate metric alone.

**Design move**: Trace behavior, content, and team consequences.

**Selection keywords**: second order consequence tradeoff leadership

## E35: Candor Loop

**Category**: Culture

**Use when**: Bad news arrives too late.

**Key question**: Can people state observations and counterevidence safely?

**Failure pattern**: Protecting a plan from criticism.

**Design move**: Separate observation, interpretation, and decision.

**Selection keywords**: retrospective feedback culture candor

## E36: Humility and Hunger

**Category**: Culture

**Use when**: The team repeats assumptions.

**Key question**: What would change our mind, and what do we still need to learn?

**Failure pattern**: Claiming certainty before evidence.

**Design move**: Maintain an explicit learning backlog.

**Selection keywords**: learning assumption unknown research

## E37: AI Intent Surface

**Category**: Game AI

**Use when**: AI looks clever internally but dumb externally.

**Key question**: Which goal, target, state, and limitation can the player perceive?

**Failure pattern**: Exposing debug data instead of meaningful cues.

**Design move**: Translate intent into diegetic and UI evidence.

**Selection keywords**: ai npc behavior tree intent target

## E38: AI Failure Contract

**Category**: Game AI

**Use when**: AI failure feels arbitrary.

**Key question**: What failure modes are possible, telegraphed, recoverable, and narratively acceptable?

**Failure pattern**: Pretending AI will never fail.

**Design move**: Design fallback behavior and player-facing explanation.

**Selection keywords**: ai error fallback hallucination failure

## E39: Companion Coordination

**Category**: Game AI

**Use when**: Allies obstruct or steal initiative.

**Key question**: How do ally goals negotiate space, timing, and player priority?

**Failure pattern**: Maximizing ally local utility.

**Design move**: Reserve player escape routes and announce commitments.

**Selection keywords**: companion ally cover coordination

## E40: LLM Boundary

**Category**: Game AI

**Use when**: Natural-language NPC scope is unclear.

**Key question**: Can memory, promises, and actions match actual system authority?

**Failure pattern**: Letting dialogue imply unavailable actions.

**Design move**: Constrain affordances and expose graceful fallback.

**Selection keywords**: llm npc memory dialogue natural language
