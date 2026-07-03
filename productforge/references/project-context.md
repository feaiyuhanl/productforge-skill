# Project Context

Use this file when creating or maintaining durable context for an existing project.

## Purpose

Project context prevents the agent from rediscovering the same constraints every iteration. It should be concise, stable, and easy to update.

## Recommended Sections

- Product intent: what the project exists to do.
- Users and scenes: primary actors and repeated usage situations.
- Core loop: the smallest loop that creates value.
- Architecture: major modules, data flow, boundaries, and external services.
- Standards: code style, testing expectations, accessibility, security, and performance rules.
- Data and telemetry: metrics, event names, data sources, and definitions.
- Known tradeoffs: intentional shortcuts, technical debt, and rejected alternatives.
- AI workflow rules: how agents should read, plan, implement, verify, and report.

## Storage Targets

- Codex: skill references plus project `AGENTS.md` when useful.
- Claude: `CLAUDE.md`.
- Cursor: `.cursor/rules/*.mdc`.
- Generic repos: `docs/productforge/project-context.md`.

## Update Rule

Update project context only when a fact should influence future iterations. Do not add transient task notes.
