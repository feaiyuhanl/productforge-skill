# ProductForge Actions

Use this file to route ProductForge requests. Keep each output small enough to drive the next executable increment.

## Primary Paths

| Path | Use When | Required References |
| --- | --- | --- |
| `zero-to-one` | The user is starting from intent, idea, product direction, tool concept, or market opportunity | `zero-to-one.md`, `mvp-artifacts.md`, optionally `contracts.md`; read `interactive-prototype.md` only when UI is the chosen artifact |
| `iterate` | The user has an existing project and wants a codebase-aware increment | `continuous-iteration.md`, `project-context.md`, `review-gates.md` |
| `standalone` | The user asks for one artifact or review | The relevant file below |

## Zero-To-One Flow

1. `clarify`: identify product type, target actor, job, constraints, non-goals, and unknowns that would change direction.
2. `scene`: define usage scenes, actors, triggers, current workaround, desired outcome, emotional bar, and constraints.
3. `use-cases`: close the core functional loop: input, action, output, success signal, failure behavior, and acceptance check.
4. `skeleton`: choose the MVP validation artifact and define the smallest executable skeleton for that artifact.
5. `feedback`: capture user judgment, taste, tradeoffs, and experience defects against the chosen artifact.
6. `contract`: convert validated behavior into acceptance, interface, data, UX when relevant, quality, and rollback contracts.
7. `harden`: add base modules only after the core loop works: auth, persistence, settings, permissions, empty/error states, observability.
8. `ship`: produce implementation evidence, review findings, risks, and next validation step.

## Continuous Iteration Flow

1. `context`: maintain durable project context, repo rules, architecture notes, data definitions, and AI collaboration constraints.
2. `brief`: write a short increment brief: problem, constraints, approach, acceptance, evidence.
3. `read-code`: inspect relevant files before designing changes.
4. `plan`: produce code-aware implementation steps and risks.
5. `implement`: make the smallest coherent code change.
6. `verify`: run tests, static checks, manual checks, and contract validation.
7. `review`: inspect the diff as a reviewer; lead with bugs and missing tests.
8. `learn`: analyze usage data, feedback, logs, or telemetry to propose the next brief.

## Standalone Actions

| Action | Output | Template |
| --- | --- | --- |
| `clarify` | Intent boundary and direction-changing questions | `assets/templates/clarify.md` |
| `scene` | Scene brief | `assets/templates/scene.md` |
| `use-cases` | Functional experience and use-case closure brief | `assets/templates/use-cases.md` |
| `skeleton` | MVP validation skeleton brief | `assets/templates/skeleton.md` |
| `feedback` | Experience feedback log | `assets/templates/feedback.md` |
| `context` | Project context | `assets/templates/context.md` |
| `brief` | Increment brief | `assets/templates/brief.md` |
| `prd` | Product requirements document, only when explicitly useful | `assets/templates/prd.md` |
| `contract` | SDD-style contract set | `assets/templates/contract.md` |
| `tech-plan` | Technical plan | `assets/templates/tech-plan.md` |
| `tasks` | Sequenced task plan | `assets/templates/tasks.md` |
| `review` | Readiness or code review | `assets/templates/review.md` |
| `evidence` | Verification and delivery evidence | `assets/templates/evidence.md` |
| `learn` | Learning brief for the next increment | `assets/templates/learn.md` |

## Backward Compatibility

Older ProductForge requests map as follows:

- `clarify` -> first step of `zero-to-one` for new products, or `brief` for existing projects.
- `prd` -> `scene` plus `contract` for 0-to-1 work, or `brief` for existing projects.
- `contract`, `tech-plan`, `tasks`, and `review` remain valid standalone actions.
