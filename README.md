# ProductForge

ProductForge is an **Intent-to-Increment** product engineering skill.

It is built for AI-assisted product work where humans own intent, judgment, taste, and tradeoffs, while AI turns ideas into small, verifiable product increments: prototypes, code changes, tests, reviews, evidence, and next-iteration briefs.

## Core Idea

Future product work should not start from long feature lists. It should start from usage scenes and move quickly toward something the user can judge.

ProductForge uses this loop:

```text
Intent -> Scene -> Skeleton / Plan -> Contract -> Code -> Evidence -> Learning
```

The workflow has two primary paths:

1. **0-to-1 product design**: define scenes, generate a minimal interactive skeleton, collect human feedback, then harden the product.
2. **Continuous iteration**: maintain durable project context, write a short increment brief, read code, plan, implement, verify, review, and learn from data.

## Human / AI Division Of Labor

Humans own:

- Intent and problem framing.
- Product judgment and taste.
- Experience feedback.
- Priority and tradeoff decisions.
- Final acceptance.

AI owns:

- Turning intent into concrete scenes and product skeletons.
- Producing code-aware implementation plans.
- Implementing small increments.
- Running tests and checks.
- Reviewing its own diff.
- Producing evidence reports.
- Reading telemetry and feedback to propose the next increment.

## Workflow 1: 0-To-1

Use this when starting from a product idea, tool concept, market observation, or rough intent.

```text
scene -> skeleton -> feedback -> contract -> harden -> ship
```

1. `scene`: define usage scenes instead of feature lists.
2. `skeleton`: create the smallest interactive product backbone that can validate the core experience.
3. `feedback`: let the human judge usefulness, clarity, trust, speed, and taste.
4. `contract`: turn accepted behavior into SDD-style acceptance, UX, API, data, and quality contracts.
5. `harden`: add supporting modules only after the core loop works.
6. `ship`: implement, verify, review, and report evidence.

Example:

```text
Use $productforge zero-to-one for a tool that helps Amazon sellers discover product opportunities.
Start from usage scenes and generate the smallest interactive skeleton.
```

## Workflow 2: Existing Project Iteration

Use this when a repository already exists and AI should work as a durable engineering partner.

```text
context -> brief -> read-code -> plan -> implement -> verify -> review -> learn
```

1. `context`: maintain project background, rules, architecture, telemetry definitions, and AI collaboration constraints.
2. `brief`: write one short document for the next increment: problem, constraints, approach, acceptance, evidence.
3. `read-code`: inspect relevant files before proposing changes.
4. `plan`: produce a code-aware implementation plan.
5. `implement`: make a small, reviewable change.
6. `verify`: run tests, checks, and acceptance validation.
7. `review`: inspect the diff for bugs, regressions, missing tests, and contract gaps.
8. `learn`: use telemetry, logs, and feedback to choose the next increment.

Example:

```text
Use $productforge iterate in this repo.
Create an increment brief for improving onboarding conversion, read the code first, then propose and implement the smallest safe change.
```

## Standalone Actions

You can call any action directly:

| Action | Purpose |
| --- | --- |
| `scene` | Create a scene brief from intent |
| `skeleton` | Define a minimal interactive product skeleton |
| `feedback` | Capture human experience feedback and tradeoffs |
| `context` | Create or update durable project context |
| `brief` | Write a short increment brief |
| `prd` | Produce a PRD when explicitly useful |
| `contract` | Define SDD-style acceptance and quality contracts |
| `tech-plan` | Produce a code-aware technical plan |
| `tasks` | Split a plan into sequenced implementation tasks |
| `review` | Review artifacts or code for readiness |
| `evidence` | Produce verification and delivery evidence |
| `learn` | Analyze feedback or telemetry for the next increment |

## Install For Codex

Copy or symlink the `productforge/` folder into your Codex skills directory.

Then use:

```text
Use $productforge to turn this intent into a verifiable product increment: ...
```

## Use With Cursor Or Claude

Use the adapter files:

- Cursor: `adapters/cursor/productforge.mdc`
- Claude or other terminal agents: `adapters/claude/CLAUDE.md`

These adapters are thin bridges. The canonical workflow lives in `productforge/SKILL.md`.

## CLI Helpers

ProductForge includes a small registry and template helper:

```bash
python productforge/scripts/productforge.py init-registry
python productforge/scripts/productforge.py packs list --verbose
python productforge/scripts/productforge.py templates
python productforge/scripts/productforge.py scaffold --action scene --title "Amazon Opportunity Finder" --dry-run
python productforge/scripts/productforge.py scaffold --action brief --title "Improve onboarding conversion" --dry-run
```

Personal extension packs are stored in `~/.productforge/registry.json` unless `--registry` is provided.

## Repository Layout

```text
productforge-skill/
  productforge/
    SKILL.md
    agents/openai.yaml
    references/
      zero-to-one.md
      continuous-iteration.md
      project-context.md
      interactive-prototype.md
      telemetry-and-learning.md
      review-gates.md
    assets/
      default_registry.json
      templates/
    scripts/productforge.py
  adapters/
    cursor/productforge.mdc
    claude/CLAUDE.md
  README.md
  LICENSE
```

## Open-Source Inspirations

ProductForge borrows workflow ideas from popular open-source AI product and coding systems, without vendoring their prompt bodies:

- GitHub Spec Kit: specification-driven contracts, plans, tasks, and implementation.
- BMAD Method: role-based product, architecture, UX, QA, and delivery thinking.
- Context Engineering: context-rich execution packets and validation loops.
- AGENTS.md: durable project-level agent instructions.
- Cursor rules and Claude/Copilot ecosystems: cross-terminal adapter patterns.

ProductForge's opinionated addition is the **Intent-to-Increment** loop: start with scenes, validate experience through an interactive skeleton, then convert accepted behavior into contracts, implementation, evidence, and learning.
