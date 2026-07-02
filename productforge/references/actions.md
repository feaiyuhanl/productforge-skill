# ProductForge Actions

Use this file when the task needs one or more ProductForge core actions. Keep action outputs independently useful so users can call one action at a time.

## 1. clarify

Use `clarify` when the user has a rough idea, scattered notes, or a vague request.

Process:

1. Restate the product intent in one sentence.
2. Extract known facts and hard constraints.
3. List assumptions that allow progress.
4. Ask only the questions that would change the product direction, contract, or implementation.
5. Produce a decision log with default recommendations.

Output sections:

- Intent
- Known Inputs
- Assumptions
- Decisions Needed
- Recommended Defaults
- Next Artifact

## 2. prd

Use `prd` when the user wants a Product Requirements Document, product brief, feature spec, or release scope.

Process:

1. Define problem, target users, goals, non-goals, and success metrics.
2. Write user stories and jobs-to-be-done.
3. Define functional requirements with stable IDs such as `REQ-001`.
4. Capture non-functional constraints that affect engineering.
5. Mark assumptions, risks, dependencies, and out-of-scope items.
6. Include launch, analytics, and support requirements when relevant.

Output sections:

- Summary
- Problem
- Users And Use Cases
- Goals And Metrics
- Scope
- Requirements
- Non-Goals
- Dependencies
- Risks
- Open Questions

## 3. contract

Use `contract` when the user mentions SDD, specification-driven development, acceptance criteria, quality gates, API behavior, data behavior, or implementation contracts.

Process:

1. Convert important behavior into contract IDs such as `CON-001`.
2. Use Given/When/Then for user-facing behavior.
3. Define API, data, state, permission, performance, observability, and rollback contracts where relevant.
4. Link each contract to requirement IDs.
5. Define verification method: unit, integration, e2e, static check, manual QA, analytics, or operational monitor.
6. Identify missing contracts that make implementation risky.

Output sections:

- Contract Summary
- Acceptance Contracts
- Interface Contracts
- Data Contracts
- Quality Gates
- Verification Matrix
- Contract Gaps

## 4. tech-plan

Use `tech-plan` when the user needs a technical proposal, architecture plan, implementation approach, migration plan, or engineering RFC.

Process:

1. Start from requirements and contracts, not from favorite technology.
2. Inspect the current repository before proposing changes when code is available.
3. Identify affected modules, data flows, interfaces, and operational concerns.
4. Compare options only when the choice matters.
5. Pick a recommendation and explain tradeoffs.
6. Include testing, rollout, migration, and rollback plans.

Output sections:

- Context
- Requirements Trace
- Proposed Design
- Alternatives
- Implementation Plan
- Data And Interface Changes
- Testing Strategy
- Rollout And Rollback
- Risks

## 5. tasks

Use `tasks` when the user has enough PRD/contracts/technical plan to start execution.

Process:

1. Split work by dependency order, not by document order.
2. Keep each task independently reviewable.
3. Attach requirement IDs and contract IDs to each task.
4. Include test and documentation tasks where they verify contracts.
5. Mark blockers, parallelizable work, and acceptance evidence.

Output sections:

- Task Plan
- Milestones
- Parallel Work
- Blockers
- Acceptance Evidence

## 6. review

Use `review` when the user wants to critique a PRD, contract set, technical plan, task list, or implementation readiness.

Process:

1. Check whether goals, requirements, contracts, and tasks trace to each other.
2. Identify contradictions, hidden assumptions, vague language, untestable claims, and missing ownership.
3. Check feasibility against repo constraints and team constraints if available.
4. Rank issues by severity.
5. Suggest targeted rewrites or missing artifacts.

Output sections:

- Blocking Issues
- Important Issues
- Nice-To-Have Improvements
- Missing Contracts
- Traceability Notes
- Recommended Next Step
