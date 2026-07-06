# ProductForge

ProductForge is an **Intent-to-Increment** product engineering skill.

It is built for AI-assisted product work where humans own intent, judgment, taste, and tradeoffs, while AI turns ideas into small, verifiable product increments: use cases, prototypes, code changes, tests, reviews, evidence, and next-iteration briefs.

## Core Idea

Future product work should not start from long feature lists or default UI mockups. It should start from usage scenes, close the core use cases, then choose the smallest artifact the user can judge.

ProductForge uses this loop:

```text
Intent -> Scene -> Use Cases -> MVP Artifact -> Contract -> Code -> Evidence -> Learning
```

The workflow has two primary paths:

1. **0-to-1 product design**: clarify intent, define scenes, close use cases, choose the MVP validation artifact, collect human feedback, then harden the product.
2. **Continuous iteration**: maintain durable project context, write a short increment brief, read code, plan, implement, verify, review, and learn from data.

## Human / AI Division Of Labor

Humans own:

- Intent and problem framing.
- Product judgment and taste.
- Experience feedback.
- Priority and tradeoff decisions.
- Final acceptance.

AI owns:

- Turning intent into concrete scenes, use cases, and product skeletons.
- Producing code-aware implementation plans.
- Implementing small increments.
- Running tests and checks.
- Reviewing its own diff.
- Producing evidence reports.
- Reading telemetry and feedback to propose the next increment.

## Workflow 1: 0-To-1

Use this when starting from a product idea, tool concept, market observation, or rough intent.

```text
clarify -> scene -> use-cases -> skeleton -> feedback -> contract -> harden -> ship
```

1. `clarify`: define the intent boundary, product type, non-goals, and direction-changing unknowns.
2. `scene`: define usage scenes instead of feature lists.
3. `use-cases`: close the functional loop: input, action, output, success signal, and failure behavior.
4. `skeleton`: choose and define the smallest MVP artifact, such as a skill, CLI, API, workflow, document, notebook, or UI.
5. `feedback`: let the human judge usefulness, clarity, trust, speed, taste, and whether the loop closes.
6. `contract`: turn accepted behavior into SDD-style acceptance, UX when relevant, API, data, and quality contracts.
7. `harden`: add supporting modules only after the core loop works.
8. `ship`: implement, verify, review, and report evidence.

Example:

```text
Use $productforge zero-to-one for a tool that helps Amazon sellers discover product opportunities.
Start from usage scenes, close the core use cases, then choose the smallest MVP artifact.
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
| `clarify` | Define the intent boundary and direction-changing questions |
| `scene` | Create a scene brief from intent |
| `use-cases` | Close the core functional experience loop |
| `skeleton` | Define the selected MVP validation skeleton |
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

## Use With Codex

ProductForge supports Codex in two ways.

### Option 1: Native Codex Skill

Copy or symlink the `productforge/` folder into your Codex skills directory.

Windows example:

```powershell
Copy-Item -Recurse .\productforge "$env:USERPROFILE\.codex\skills\productforge"
```

macOS/Linux example:

```bash
cp -R ./productforge ~/.codex/skills/productforge
```

Then invoke it directly:

```text
Use $productforge to turn this intent into a verifiable product increment: ...
```

The native Codex entrypoint is `productforge/SKILL.md`; `productforge/agents/openai.yaml` provides UI metadata.

### Option 2: Project-Level Codex Adapter

If you do not want to install the skill globally, copy `adapters/codex/AGENTS.md` into the target repository root as `AGENTS.md`, or merge its contents into an existing `AGENTS.md`.

Then ask Codex:

```text
Use the ProductForge workflow in this repository to run a zero-to-one or iterate flow for ...
```

## Use With Codex, Cursor, Or Claude

Use the adapter files when the target tool does not load Codex skills directly:

- Codex project adapter: `adapters/codex/AGENTS.md`
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
python productforge/scripts/productforge.py scaffold --action use-cases --title "Amazon Opportunity Finder" --dry-run
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
      mvp-artifacts.md
      interactive-prototype.md
      telemetry-and-learning.md
      review-gates.md
    assets/
      default_registry.json
      templates/
    scripts/productforge.py
  adapters/
    codex/AGENTS.md
    cursor/productforge.mdc
    claude/CLAUDE.md
  README.md
  LICENSE
```

## Open-Source Inspirations

ProductForge borrows workflow ideas from popular open-source AI product and coding systems, without vendoring their prompt bodies:

- GitHub Spec Kit: specification-driven contracts, plans, tasks, and implementation.
- Context Engineering: context-rich execution packets and validation loops.
- AGENTS.md: durable project-level agent instructions.
- Codex, Cursor, Claude, and Copilot ecosystems: cross-terminal adapter patterns.

ProductForge's opinionated addition is the **Intent-to-Increment** loop: start with scenes and use cases, choose the right MVP artifact, then convert accepted behavior into contracts, implementation, evidence, and learning. UI prototypes are supported when screens are the right validation artifact, but they are not the default constraint.
