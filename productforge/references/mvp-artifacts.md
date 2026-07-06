# MVP Validation Artifacts

Use this file after ProductForge has clarified intent, scenes, and core use cases.

## Principle

Choose the smallest artifact that can validate the functional experience. A prototype is not automatically a webpage. UI is appropriate only when the product judgment depends on layout, navigation, direct manipulation, visual state, or multi-step on-screen interaction.

## Artifact Selection

| Product Type | Preferred MVP Artifact | Validates |
| --- | --- | --- |
| Codex skill | `SKILL.md`, references, templates, sample prompts, dry-run checks | Triggering, workflow, output shape, boundaries, repeatability |
| CLI tool | Command surface, help text, sample inputs/outputs, tests | Invocation ergonomics, IO contract, error handling |
| API or service | Contract, schema, mock call, integration example | Interface clarity, data shape, failure semantics |
| Workflow or method | Playbook, checklist, artifact templates, example run | Decision order, handoffs, acceptance criteria |
| Notebook or analysis tool | Reproducible notebook, sample dataset, expected outputs | Calculation path, evidence quality, interpretation |
| Document-backed product | Template, example filled artifact, review rubric | Structure, completeness, downstream usefulness |
| Web or app UI | Interactive UI skeleton | Navigation, visual hierarchy, state feedback, direct manipulation |

## Selection Gate

Before creating any skeleton, state:

- Chosen artifact type.
- Why this artifact validates the core use case better than the alternatives.
- What the user can judge from it.
- What remains mocked or deferred.
- What evidence will prove the loop works.

## Skill Product Pattern

When the product is itself a Codex skill:

- Define trigger phrases and non-triggers.
- Keep `SKILL.md` lean and route detailed procedures into `references/`.
- Provide templates for repeated outputs.
- Add deterministic scripts only for fragile or repeated operations.
- Include sample user requests and expected artifact shapes.
- Validate with scaffold, lint, dry-run, or representative prompts.
- Integrate existing skills only after the ProductForge use cases show a real need.

## UI Guardrail

Do not build a UI skeleton just because the user says "product", "tool", "MVP", or "prototype". First decide whether the product's core value is judged through a screen. If not, use the artifact that matches the actual consumption path.
