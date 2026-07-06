# Open-Source Source Map

Use this file when explaining or extending the ProductForge method. ProductForge borrows workflow ideas, not vendored project content.

## Recommended Inspirations

| Source | Borrow | ProductForge Mapping |
| --- | --- | --- |
| `github/spec-kit` | Constitution, specify, plan, tasks, implementation sequence | `contract`, `tech-plan`, `tasks`, `evidence` |
| `coleam00/context-engineering-intro` | Product Requirements Prompt and context-rich execution packet | `context`, `brief`, `iterate` |
| `agentsmd/agents.md` | Project-level AI agent instructions | `project-context`, Codex adapter, repository rules |
| `PatrickJS/awesome-cursorrules` | Stack-specific coding rules and guardrails | extension packs and repo rules |
| `hesreallyhim/awesome-claude-code` | Claude Code ecosystem discovery | source discovery only |
| `github/awesome-copilot` | Cross-agent instructions and workflows | Codex, Cursor, Claude, and generic adapter patterns |
| `SuperClaude-Org/SuperClaude_Framework` | Command-oriented development workflow | action router |
| `wshobson/agents` | Agent, skill, plugin marketplace pattern | extension-pack registry |

## Removed From Default Registry

| Source | Reason |
| --- | --- |
| `bmad-code-org/BMAD-METHOD` | Useful as broad inspiration, but too role-heavy and UX/PRD-oriented for ProductForge's use-case-first 0-to-1 default path. Keep it out of automatic routing unless a user explicitly asks for that style. |

## Borrowing Rules

- Cite source projects in documentation when their method influenced a pack.
- Do not copy large prompt files or proprietary system prompts into ProductForge.
- Convert broad inspiration into small ProductForge rules, templates, or checklists.
- Keep license compatibility before vendoring any code, template, or long text.
- Prefer links plus short local summaries over duplicated content.
