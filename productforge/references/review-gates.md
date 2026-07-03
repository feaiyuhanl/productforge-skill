# Review Gates

Use this file before delivering an implementation or claiming an increment is complete.

## Planning Gate

- The agent read the relevant code and project context.
- The plan names affected files, interfaces, data, tests, and risks.
- The plan maps to the increment brief and contracts.

## Implementation Gate

- The diff is scoped to the increment.
- Existing patterns are followed.
- Error, empty, permission, and rollback states are considered when relevant.
- No unrelated refactor or formatting churn is included.

## Verification Gate

- Relevant tests or checks ran.
- Manual verification steps are listed when automation is unavailable.
- Acceptance criteria map to evidence.
- Known failures are stated with next action.

## Review Gate

Lead with findings:

- Bugs or regressions.
- Missing tests.
- Unclear behavior.
- Contract gaps.
- Data or telemetry gaps.
- Operational risk.

If no issues are found, state the remaining risk and test coverage limits.
