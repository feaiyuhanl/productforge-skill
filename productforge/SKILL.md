---
name: productforge
description: Product and engineering workflow toolbox for PRDs, SDD-style contracts, technical plans, implementation tasks, and review checklists. Use when Codex needs to clarify a product idea, write or critique a PRD, define acceptance contracts, produce a technical proposal, split work into tasks, or orchestrate pluggable product-engineering workflow packs without loading many separate skills.
---

# ProductForge

ProductForge turns rough product intent into executable product and engineering artifacts. Use it as a single orchestration skill with progressive disclosure: load only the action guide, template, or extension pack needed for the current request.

## Action Router

First classify the user's request into one or more actions:

- `clarify`: turn ambiguity into decisions, assumptions, risks, and open questions.
- `prd`: produce a product requirements document with goals, users, scope, stories, metrics, and release constraints.
- `contract`: define SDD-style acceptance, API, data, UX, quality, and rollback contracts.
- `tech-plan`: create an implementation-oriented technical proposal.
- `tasks`: split approved PRD/contracts/technical plan into sequenced engineering tasks.
- `review`: check consistency, feasibility, traceability, testability, and missing contracts.

For detailed steps, read `references/actions.md`. For contract-heavy work, also read `references/contracts.md`.

## Operating Rules

- Keep one source of truth per artifact. Do not create duplicate PRD, contract, or plan sections with conflicting wording.
- Prefer explicit contracts over prose promises. Every important behavior should have an ID, owner surface, acceptance check, and verification method.
- Maintain traceability: tasks should cite PRD requirement IDs and contract IDs.
- Separate facts, assumptions, decisions, risks, and open questions.
- If requirements are unclear but work can continue, state assumptions and proceed. Ask only when the missing answer would make the work risky or invalid.
- For implementation guidance, fit the existing repo and constraints before proposing new architecture.
- For review, lead with blocking issues and concrete fixes, then summarize residual risk.

## Progressive Disclosure

Use only the needed resources:

- `references/actions.md`: detailed six-action workflow.
- `references/contracts.md`: contract taxonomy, SDD checks, and traceability rules.
- `references/registry.md`: extension pack model, install/uninstall/list workflow, and registry conventions.
- `references/source-map.md`: open-source inspirations and how to borrow from them without vendoring their content.
- `references/cross-terminal.md`: how to expose this skill to Codex, Cursor, Claude, and other terminal agents.
- `assets/templates/*.md`: output skeletons for each action.
- `assets/default_registry.json`: built-in workflow pack registry.
- `scripts/productforge.py`: deterministic helper for listing packs, adding/removing local packs, validating the registry, and scaffolding templates.

Do not load every reference by default. Load the minimum set for the requested action.

## Extension Packs

ProductForge is a toolbox skill, not a bundle that forces many skills into context. Extension packs are metadata entries that point to optional references, templates, rules, or external project URLs.

Use `scripts/productforge.py packs list` to inspect packs. Use `references/registry.md` before adding, removing, or changing packs.

Built-in pack categories:

- `source`: open-source method or rule source used as inspiration.
- `workflow`: local ProductForge workflow extension.
- `template`: reusable artifact skeleton.
- `adapter`: terminal-agent integration hint.

## Output Shape

When producing artifacts, keep sections concrete and decision-oriented. Prefer tables for traceability and contracts. Avoid motivational filler. End with the next action only when it follows from the user's current goal.
