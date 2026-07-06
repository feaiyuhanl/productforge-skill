# ProductForge Codex Adapter

Use this adapter when ProductForge is not installed as a native Codex skill but the repository should still follow the ProductForge workflow.

## Canonical Source

Use the canonical workflow from `productforge/SKILL.md`.

Load only the ProductForge references needed for the requested path:

- `zero-to-one`: use `productforge/references/zero-to-one.md` and `productforge/references/mvp-artifacts.md`; use `productforge/references/interactive-prototype.md` only when UI is the selected artifact.
- `iterate`: use `productforge/references/continuous-iteration.md`, `productforge/references/project-context.md`, and `productforge/references/review-gates.md`.
- Contract-heavy work: use `productforge/references/contracts.md`.
- Data or feedback work: use `productforge/references/telemetry-and-learning.md`.

## Codex Workflow Rules

- Start 0-to-1 product work from usage scenes and use-case closure, not feature lists or default UI mockups.
- In existing projects, read repository context and relevant code before planning changes.
- Keep every increment small enough to verify, review, and roll back.
- Preserve traceability across intent, scene, use case, brief, contract, task, code change, evidence, and learning.
- Deliver evidence for completed work: tests/checks run, acceptance mapping, review findings, and residual risk.

## Invocation Examples

```text
Use the ProductForge zero-to-one workflow for this idea: ...
```

```text
Use the ProductForge iterate workflow in this repo. Read code first, then propose and implement the smallest safe increment for ...
```
