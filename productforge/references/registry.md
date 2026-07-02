# ProductForge Registry

Use this file when managing ProductForge extension packs.

## Goal

ProductForge should behave like one skill while still allowing product and engineering workflows to evolve. Extension packs are metadata records, not always separate installed skills. They let the agent discover optional methods, templates, and rule sources without loading them until needed.

## Registry Location

The built-in registry lives at `assets/default_registry.json`.

For personal customization, use:

```bash
python productforge/scripts/productforge.py init-registry
python productforge/scripts/productforge.py packs list
python productforge/scripts/productforge.py packs add --id my-pack --name "My Pack" --category workflow --description "..."
python productforge/scripts/productforge.py packs remove --id my-pack
```

By default, the script writes personal changes to:

- Windows: `%USERPROFILE%\.productforge\registry.json`
- macOS/Linux: `~/.productforge/registry.json`

Use `--registry path/to/registry.json` to manage a project-local registry.

## Pack Schema

Each pack has:

- `id`: lowercase letters, digits, and hyphens.
- `name`: human-facing name.
- `category`: `source`, `workflow`, `template`, or `adapter`.
- `description`: one concise sentence.
- `triggers`: words or phrases that suggest the pack.
- `actions`: ProductForge actions this pack helps with.
- `references`: local files or external URLs.
- `status`: `bundled`, `local`, `experimental`, or `deprecated`.

## Add Pack Rule

Add a pack when it provides repeatable value for at least one action. Do not add a pack just because a project is popular. A good pack changes how ProductForge asks questions, structures artifacts, verifies contracts, or decomposes tasks.

## Remove Pack Rule

Remove or deprecate a pack when it is stale, too broad, duplicates another pack, or encourages copying content instead of adapting method ideas.

## Progressive Disclosure Rule

Use triggers to decide whether to read a pack. Do not load all pack references during normal PRD, contract, or plan generation.
