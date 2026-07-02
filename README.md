# ProductForge

ProductForge is a product-engineering toolbox skill: one entry point for PRDs, SDD-style contracts, technical plans, implementation tasks, and readiness reviews.

It is designed for AI coding workflows where product intent must become executable contracts before implementation starts.

## Why This Exists

AI agents are fast, but speed without contracts creates drift. ProductForge keeps the workflow explicit:

1. `clarify` ambiguous product intent.
2. `prd` write product requirements.
3. `contract` define acceptance, API, data, UX, quality, and rollback contracts.
4. `tech-plan` design implementation from requirements and contracts.
5. `tasks` split work into traceable implementation steps.
6. `review` check consistency, feasibility, and testability.

## Project Name

The project name is **ProductForge** because the skill forges ideas into product decisions, contracts, technical plans, and executable tasks.

## Repository Layout

```text
productforge-skill/
  productforge/
    SKILL.md
    agents/openai.yaml
    references/
    assets/
      default_registry.json
      templates/
    scripts/productforge.py
  adapters/
    cursor/productforge.mdc
    claude/CLAUDE.md
  README.md
  LICENSE
```

## Install For Codex

Copy or symlink the `productforge/` folder into your Codex skills directory.

Then ask:

```text
Use $productforge to create a PRD, contracts, technical plan, and tasks for ...
```

## Use With Cursor Or Claude

Use the adapter files:

- Cursor: `adapters/cursor/productforge.mdc`
- Claude or other terminal agents: `adapters/claude/CLAUDE.md`

These files are thin bridges. The canonical rules remain in `productforge/SKILL.md`.

## Extension Packs

ProductForge uses a registry to make workflow packs pluggable without requiring many installed skills.

```bash
python productforge/scripts/productforge.py init-registry
python productforge/scripts/productforge.py packs list --verbose
python productforge/scripts/productforge.py templates
python productforge/scripts/productforge.py scaffold --action prd --title "Amazon Opportunity Finder" --dry-run
```

Personal packs are stored in `~/.productforge/registry.json` unless `--registry` is provided.

## Open-Source Inspirations

ProductForge is designed to borrow patterns from popular open-source product and AI-coding workflows, especially GitHub Spec Kit, BMAD Method, Context Engineering, AGENTS.md, Cursor rules, SuperClaude, and agent/skill marketplaces. It links to sources instead of vendoring large prompt or template bodies.
