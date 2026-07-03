#!/usr/bin/env python3
"""ProductForge registry and template helper."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from string import Template


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "assets" / "default_registry.json"
TEMPLATES = ROOT / "assets" / "templates"
PACK_ID = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}[a-z0-9]$")
VALID_ACTIONS = {
    "zero-to-one",
    "iterate",
    "scene",
    "skeleton",
    "feedback",
    "context",
    "brief",
    "prd",
    "contract",
    "tech-plan",
    "tasks",
    "review",
    "evidence",
    "learn",
    "clarify",
}
VALID_CATEGORIES = {"source", "workflow", "template", "adapter"}
VALID_STATUSES = {"bundled", "local", "experimental", "deprecated"}


def user_registry_path() -> Path:
    return Path.home() / ".productforge" / "registry.json"


def load_registry(path: Path) -> dict:
    if not path.exists():
        if path == user_registry_path():
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(DEFAULT_REGISTRY, path)
        else:
            raise SystemExit(f"Registry not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_registry_data(data)
    return data


def save_registry(path: Path, data: dict) -> None:
    validate_registry_data(data)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def validate_registry_data(data: dict) -> None:
    if not isinstance(data, dict):
        raise SystemExit("Registry must be a JSON object.")
    if data.get("version") != 1:
        raise SystemExit("Registry version must be 1.")
    packs = data.get("packs")
    if not isinstance(packs, list):
        raise SystemExit("Registry must contain a packs list.")

    seen: set[str] = set()
    for pack in packs:
        if not isinstance(pack, dict):
            raise SystemExit("Each pack must be an object.")
        required = {"id", "name", "category", "description", "triggers", "actions", "references", "status"}
        missing = required - set(pack)
        if missing:
            raise SystemExit(f"Pack is missing fields: {', '.join(sorted(missing))}")
        pack_id = pack["id"]
        if not isinstance(pack_id, str) or not PACK_ID.match(pack_id):
            raise SystemExit(f"Invalid pack id: {pack_id}")
        if pack_id in seen:
            raise SystemExit(f"Duplicate pack id: {pack_id}")
        seen.add(pack_id)
        if pack["category"] not in VALID_CATEGORIES:
            raise SystemExit(f"Invalid category for {pack_id}: {pack['category']}")
        if pack["status"] not in VALID_STATUSES:
            raise SystemExit(f"Invalid status for {pack_id}: {pack['status']}")
        for field in ("triggers", "actions", "references"):
            if not isinstance(pack[field], list):
                raise SystemExit(f"{pack_id}.{field} must be a list.")
        invalid_actions = set(pack["actions"]) - VALID_ACTIONS
        if invalid_actions:
            raise SystemExit(f"{pack_id} has invalid actions: {', '.join(sorted(invalid_actions))}")


def list_packs(args: argparse.Namespace) -> None:
    data = load_registry(args.registry)
    for pack in sorted(data["packs"], key=lambda item: item["id"]):
        actions = ", ".join(pack["actions"])
        print(f"{pack['id']:24} {pack['category']:9} {pack['status']:12} {actions}")
        if args.verbose:
            print(f"  {pack['name']}: {pack['description']}")
            if pack["references"]:
                print(f"  refs: {', '.join(pack['references'])}")


def add_pack(args: argparse.Namespace) -> None:
    data = load_registry(args.registry)
    if any(pack["id"] == args.id for pack in data["packs"]):
        raise SystemExit(f"Pack already exists: {args.id}")
    pack = {
        "id": args.id,
        "name": args.name,
        "category": args.category,
        "description": args.description,
        "triggers": args.trigger,
        "actions": args.action,
        "references": args.reference,
        "status": args.status,
    }
    data["packs"].append(pack)
    save_registry(args.registry, data)
    print(f"Added pack: {args.id}")


def remove_pack(args: argparse.Namespace) -> None:
    data = load_registry(args.registry)
    original = len(data["packs"])
    data["packs"] = [pack for pack in data["packs"] if pack["id"] != args.id]
    if len(data["packs"]) == original:
        raise SystemExit(f"Pack not found: {args.id}")
    save_registry(args.registry, data)
    print(f"Removed pack: {args.id}")


def validate_command(args: argparse.Namespace) -> None:
    load_registry(args.registry)
    print(f"Registry OK: {args.registry}")


def init_registry(args: argparse.Namespace) -> None:
    if args.registry.resolve() == DEFAULT_REGISTRY.resolve():
        raise SystemExit("Refusing to overwrite the bundled default registry.")
    if args.registry.exists() and not args.force:
        raise SystemExit(f"Registry already exists: {args.registry}. Use --force to replace it.")
    args.registry.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(DEFAULT_REGISTRY, args.registry)
    load_registry(args.registry)
    print(f"Initialized registry: {args.registry}")


def list_templates(_: argparse.Namespace) -> None:
    for path in sorted(TEMPLATES.glob("*.md")):
        print(path.stem)


def scaffold(args: argparse.Namespace) -> None:
    template_path = TEMPLATES / f"{args.action}.md"
    if not template_path.exists():
        raise SystemExit(f"Unknown action template: {args.action}")
    body = Template(template_path.read_text(encoding="utf-8")).safe_substitute(title=args.title)
    if args.dry_run:
        print(body)
        return
    output = args.output or Path(f"{args.action}-{slugify(args.title)}.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(body, encoding="utf-8", newline="\n")
    print(f"Wrote {output}")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage ProductForge packs and templates.")
    parser.add_argument("--registry", type=Path, default=user_registry_path(), help="Registry JSON path.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    packs = subparsers.add_parser("packs", help="Manage extension packs.")
    pack_subparsers = packs.add_subparsers(dest="pack_command", required=True)

    list_parser = pack_subparsers.add_parser("list", help="List extension packs.")
    list_parser.add_argument("--verbose", action="store_true")
    list_parser.set_defaults(func=list_packs)

    add_parser = pack_subparsers.add_parser("add", help="Add an extension pack.")
    add_parser.add_argument("--id", required=True)
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--category", choices=sorted(VALID_CATEGORIES), required=True)
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--trigger", action="append", required=True)
    add_parser.add_argument("--action", action="append", choices=sorted(VALID_ACTIONS), required=True)
    add_parser.add_argument("--reference", action="append", default=[])
    add_parser.add_argument("--status", choices=sorted(VALID_STATUSES), default="local")
    add_parser.set_defaults(func=add_pack)

    remove_parser = pack_subparsers.add_parser("remove", help="Remove an extension pack.")
    remove_parser.add_argument("--id", required=True)
    remove_parser.set_defaults(func=remove_pack)

    validate_parser = subparsers.add_parser("validate", help="Validate a registry.")
    validate_parser.set_defaults(func=validate_command)

    init_parser = subparsers.add_parser("init-registry", help="Create a local registry from the bundled default.")
    init_parser.add_argument("--force", action="store_true")
    init_parser.set_defaults(func=init_registry)

    templates_parser = subparsers.add_parser("templates", help="List templates.")
    templates_parser.set_defaults(func=list_templates)

    scaffold_parser = subparsers.add_parser("scaffold", help="Render an action template.")
    scaffold_parser.add_argument("--action", choices=sorted(VALID_ACTIONS), required=True)
    scaffold_parser.add_argument("--title", required=True)
    scaffold_parser.add_argument("--output", type=Path)
    scaffold_parser.add_argument("--dry-run", action="store_true")
    scaffold_parser.set_defaults(func=scaffold)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
