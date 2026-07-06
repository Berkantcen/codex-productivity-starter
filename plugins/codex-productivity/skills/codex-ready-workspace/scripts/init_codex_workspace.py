#!/usr/bin/env python3
"""Create missing Codex-ready workspace starter files."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_TEMPLATE_DIR = SCRIPT_DIR.parent / "assets" / "project-starter"


def copy_tree(template_dir: Path, target_dir: Path, force: bool) -> tuple[list[Path], list[Path]]:
    created: list[Path] = []
    skipped: list[Path] = []

    for source in sorted(template_dir.rglob("*")):
        if source.is_dir():
            continue

        relative = source.relative_to(template_dir)
        destination = target_dir / relative

        if destination.exists() and not force:
            skipped.append(relative)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        created.append(relative)

    return created, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create missing Codex-ready workspace starter files."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Workspace directory to initialize. Defaults to the current directory.",
    )
    parser.add_argument(
        "--template-dir",
        default=str(DEFAULT_TEMPLATE_DIR),
        help="Starter template directory. Defaults to the skill bundled assets.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files. Use only when the user explicitly asks for replacement.",
    )
    args = parser.parse_args()

    target_dir = Path(args.target).expanduser().resolve()
    template_dir = Path(args.template_dir).expanduser().resolve()

    if not template_dir.is_dir():
        raise SystemExit(f"Template directory not found: {template_dir}")
    if not target_dir.exists():
        raise SystemExit(f"Target directory not found: {target_dir}")
    if not target_dir.is_dir():
        raise SystemExit(f"Target is not a directory: {target_dir}")

    created, skipped = copy_tree(template_dir, target_dir, args.force)

    print(f"Target: {target_dir}")
    print(f"Template: {template_dir}")
    print(f"Created or updated: {len(created)}")
    for path in created:
        print(f"  + {path}")

    print(f"Skipped existing: {len(skipped)}")
    for path in skipped:
        print(f"  = {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
