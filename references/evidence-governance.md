# Evidence Governance and Source Cards

## Status labels

| Status | Meaning | May it become a default rule? |
|---|---|---|
| `hypothesis` | plausible proposal without source or project evidence | no |
| `source-indexed` | complete source is locally searchable; no synthesis claim yet | no |
| `source-synthesized` | source has been read for the stated claim and translated into an original, scoped rule | conditionally |
| `project-validated` | tested against predeclared player and system evidence in a named project | yes, within that context |
| `superseded` | source claim is obsolete, unsafe, or replaced by a better current practice | no |

## Source-card protocol

For any important claim, record:

```markdown
## Claim
## Source and locator
## Evidence status and review date
## Applicable context
## What transfers / what does not
## Modern dependency or replacement
## Design consequence
## Disconfirming evidence or expiry trigger
```

Do not promote a chapter title, benchmark number, or case study into a general rule without filling the transfer and expiry fields.

## Local Game AI Pro corpus

Personal installations may contain `private_sources/game-ai-pro/` with 158 full-text PDFs, 13 ZIP audits, and 171 cards. These cards are source-index records, not automatically validated prescriptions. Use them to find the full source, then write a `source-synthesized` card only for a claim you have actually inspected.

## Review cadence without a project

- Recheck engine and model references before adopting a version-specific recommendation.
- Mark API, package, benchmark, and model-behavior claims with an access date.
- Revisit `conditional` or `historical` source material when the target platform, performance budget, or player contract changes.
- Keep project validation separate from source authority; a famous case study does not prove fit for a new game.
