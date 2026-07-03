# Cross-Terminal Use

Use this file when adapting ProductForge for Codex, Cursor, Claude, or another terminal coding agent.

## Shared Principle

Keep `productforge/SKILL.md`, `references/`, `assets/`, and `scripts/` as the canonical source. Other tools should reference or copy the canonical files instead of maintaining divergent instructions.

## Codex

Use ProductForge as a native Codex skill when possible.

Install or copy the `productforge/` folder into a Codex skills directory:

```text
~/.codex/skills/productforge
```

On Windows, the equivalent default path is:

```text
%USERPROFILE%\.codex\skills\productforge
```

Then invoke it by name:

```text
Use $productforge to turn this intent into a verifiable product increment: ...
```

For repository-local usage without global installation, use `adapters/codex/AGENTS.md` as the repo root `AGENTS.md`, or merge its contents into the existing repo instructions.

Codex-specific source of truth:

```text
productforge/SKILL.md
productforge/agents/openai.yaml
adapters/codex/AGENTS.md
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
