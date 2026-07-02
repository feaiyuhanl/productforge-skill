# ProductForge Contracts

Use this file for SDD-style contract work and for reviewing whether PRD or technical-plan statements are implementable and testable.

## Contract Principles

- Use stable IDs: `REQ-001`, `CON-001`, `TASK-001`.
- Make each contract observable. A contract without a verification method is incomplete.
- Separate product behavior from implementation detail unless the implementation detail is a real constraint.
- Prefer measurable thresholds for performance, reliability, accessibility, and data quality.
- State negative behavior explicitly: denial, failure, empty state, timeout, duplicate, rollback, and permission boundaries.

## Contract Types

| Type | Use For | Required Fields |
| --- | --- | --- |
| Acceptance | User-visible behavior and business rules | ID, linked requirement, scenario, expected result, verification |
| API | Request/response behavior, errors, compatibility | ID, endpoint/interface, inputs, outputs, errors, versioning |
| Data | Schema, lifecycle, quality, privacy, retention | ID, entity, source, fields, invariants, retention |
| State | Workflow status, transitions, idempotency | ID, states, transition, guard, side effect |
| Permission | Role, access, policy boundary | ID, actor, allowed action, denied action, audit requirement |
| UX | Empty/loading/error states, accessibility | ID, surface, state, expected UI behavior, accessibility check |
| Quality | Performance, reliability, security, observability | ID, threshold, environment, measurement method |
| Rollback | Deployment and recovery behavior | ID, trigger, rollback action, data safety, owner |

## Acceptance Contract Template

| ID | Req | Given | When | Then | Verify |
| --- | --- | --- | --- | --- | --- |
| CON-001 | REQ-001 | User has valid input | User submits | System creates result and shows confirmation | E2E test |

## Traceability Matrix

Use this matrix when moving from PRD to technical plan or task plan:

| Requirement | Contracts | Design Area | Tasks | Verification |
| --- | --- | --- | --- | --- |
| REQ-001 | CON-001, CON-002 | API, UI | TASK-001, TASK-004 | Integration, E2E |

## Review Checklist

- Every high-priority requirement has at least one contract.
- Every contract has a verification method.
- Every task cites at least one requirement or contract unless it is setup work.
- Failure, permission, empty, and rollback states are covered.
- Metrics and analytics events have names, triggers, and dimensions.
- Data contracts include ownership, source, lifecycle, and retention when relevant.
