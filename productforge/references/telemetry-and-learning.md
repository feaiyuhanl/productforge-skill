# Telemetry And Learning

Use this file when data, analytics, logs, or user feedback should drive the next increment.

## Principle

Data should decide the next product question, not just report the last release.

## Instrumentation Plan

Define:

- Event name.
- Trigger.
- Actor or account dimension.
- Important properties.
- Success, failure, and abandonment signals.
- Privacy or retention constraints.

## Learning Brief

Use this structure:

- Observation: what changed or what users did.
- Evidence: metric, log, feedback, or session evidence.
- Interpretation: likely reason, with confidence.
- Product implication: what should change.
- Next increment: problem, approach, acceptance, evidence.
- Caveats: data quality, sample size, bias, missing instrumentation.

## Guardrails

- Do not infer causality from weak data.
- Separate direct evidence from hypothesis.
- Track negative signals, not only success events.
- Prefer one actionable next increment over a broad roadmap.
