---
name: productforge
description: Intent-to-increment product engineering workflow for turning human intent into verifiable product increments. Use when Codex needs to design a 0-to-1 product from clarified intent, usage scenes, closed use cases, MVP capability maps, and the right validation artifact such as a skill, CLI, API, workflow, or UI; run continuous iteration in an existing codebase; maintain project context and rules; write short increment briefs; read code before planning; implement and verify changes; review its own work; define SDD-style contracts; or analyze telemetry and feedback for the next iteration.
---

# ProductForge

ProductForge turns human intent into verifiable product increments. Use it as a single orchestration skill with progressive disclosure: load only the workflow, template, or extension pack needed for the current request.

## Workflow Router

First classify the request into one path:

- `zero-to-one`: clarify intent, define scenes, close the core use cases, map the MVP capability system, choose the validation artifact, collect feedback, then harden the product.
- `iterate`: work inside an existing project with durable context, a short increment brief, code reading, implementation, verification, review, and learning.
- `standalone`: produce or review a specific artifact such as a scene brief, increment brief, contract, technical plan, task plan, evidence report, or learning brief.

For routing details, read `references/actions.md`. For contract-heavy work, read `references/contracts.md`.

## Operating Rules

- Preserve human agency. Treat the user as owner of intent, judgment, taste, priority, and tradeoff decisions.
- Let AI own execution acceleration. Convert intent into use cases, prototypes, plans, code changes, tests, reviews, and evidence.
- Start 0-to-1 work from functional experience and usage scenes, not feature lists or UI screens.
- Close the smallest use-case loop before choosing an MVP artifact. UI is one possible artifact, not the default constraint.
- Build the smallest artifact that validates the core experience before filling in supporting modules.
- In existing projects, maintain durable context and use one short increment brief per iteration.
- Read repository context and relevant code before proposing implementation changes.
- Prefer explicit contracts over prose promises. Every important behavior should have an ID, owner surface, acceptance check, and verification method.
- Maintain traceability: increments should cite scene, requirement, contract, task, and verification IDs.
- Separate facts, assumptions, decisions, risks, and open questions.
- If intent is unclear but work can continue, state assumptions and proceed. Ask only when the missing answer would change product direction or implementation risk.
- For implementation guidance, fit the existing repo and constraints before proposing new architecture.
- Every delivered increment should produce evidence: tests run, acceptance mapping, review findings, and residual risk.
- Data and feedback should drive the next brief. Do not treat analytics as a reporting afterthought.

## Progressive Disclosure

Use only the needed resources:

- `references/actions.md`: router and action map.
- `references/zero-to-one.md`: functional-experience-first product discovery and MVP validation workflow.
- `references/continuous-iteration.md`: existing-project iteration workflow.
- `references/project-context.md`: durable project memory, rules, and AI collaboration context.
- `references/mvp-artifacts.md`: choose the right validation artifact for a skill, CLI, API, workflow, UI, or document-backed product.
- `references/interactive-prototype.md`: UI prototype expectations; use only after UI is selected as the validation artifact.
- `references/contracts.md`: contract taxonomy, SDD checks, and traceability rules.
- `references/telemetry-and-learning.md`: data, feedback, instrumentation, and next-iteration loop.
- `references/review-gates.md`: implementation, verification, and self-review gates.
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

When producing artifacts, keep sections concrete and decision-oriented. Prefer short briefs, traceability tables, and contract matrices over long prose. End with the next executable increment or validation step only when it follows from the user's current goal.
