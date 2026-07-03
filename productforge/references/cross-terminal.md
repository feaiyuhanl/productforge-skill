# Cross-Terminal Use

Use this file when adapting ProductForge for Codex, Cursor, Claude, or another terminal coding agent.

## Shared Principle

Keep `productforge/SKILL.md`, `references/`, `assets/`, and `scripts/` as the canonical source. Other tools should reference or copy the canonical files instead of maintaining divergent instructions.

## Codex

Install or copy the `productforge/` folder into a Codex skills directory, then invoke it by name:

```text
Use $productforge to create a PRD and acceptance contracts for this idea: ...
```

## Cursor

Use `adapters/cursor/productforge.mdc` as a project rule. Keep it short and point it back to `productforge/SKILL.md`.

## Claude

Use `adapters/claude/CLAUDE.md` as a project instruction bridge. Keep it short and point it back to `productforge/SKILL.md`.

## Generic Terminal Agents

Put this sentence in the agent's project instruction file:

```text
For product and engineering work, use the ProductForge intent-to-increment workflow from productforge/SKILL.md and load only the referenced files needed for the requested path.
```

## Sync Rule

When changing behavior, edit the canonical ProductForge skill first, then update adapters only if their bridge text becomes inaccurate.
