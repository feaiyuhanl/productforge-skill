# Continuous Iteration Workflow

Use this workflow when the user has an existing repository, product, dataset, or deployed workflow.

## Principle

Each iteration should be a small, reviewable product increment with durable context and explicit evidence.

## Flow

1. Load context.
   - Read project rules, README, AGENTS/CLAUDE/Cursor rules, architecture docs, and relevant recent decisions when available.
2. Write or refine the increment brief.
   - Problem, user impact, constraints, proposed approach, acceptance criteria, risks, and evidence plan.
3. Read code before planning.
   - Inspect relevant modules, tests, interfaces, schemas, and existing patterns.
4. Plan the change.
   - Identify exact files, data flows, contracts, tests, rollout impact, and rollback path.
5. Implement narrowly.
   - Keep the diff scoped to the increment. Avoid opportunistic refactors.
6. Verify.
   - Run relevant tests and checks. If unable, state why and provide manual verification steps.
7. Review.
   - Review the diff as if it were someone else's code. Lead with bugs, regressions, missing tests, and risky assumptions.
8. Learn.
   - Use data, telemetry, logs, feedback, or observed behavior to propose the next increment.

## Increment Brief Minimum

- Problem: what is being improved.
- Constraint: what must not change.
- Approach: how the increment will be solved.
- Acceptance: what must be true when complete.
- Evidence: how completion will be proven.

## Done Criteria

- The diff maps to the brief.
- Acceptance criteria map to verification evidence.
- The review found no unresolved blocking issue.
- Any data or feedback needed for the next iteration is named.
