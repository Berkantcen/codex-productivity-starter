#!/usr/bin/env python3
"""Verify that manual starter templates and plugin bundled templates stay in sync."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
MANUAL_DIR = ROOT / "templates" / "project-starter"
PLUGIN_DIR = (
    ROOT
    / "plugins"
    / "codex-productivity"
    / "skills"
    / "codex-ready-workspace"
    / "assets"
    / "project-starter"
)


def list_files(directory: Path) -> dict[Path, bytes]:
    return {
        path.relative_to(directory): path.read_bytes()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


def main() -> int:
    manual_files = list_files(MANUAL_DIR)
    plugin_files = list_files(PLUGIN_DIR)

    manual_only = sorted(set(manual_files) - set(plugin_files))
    plugin_only = sorted(set(plugin_files) - set(manual_files))
    changed = sorted(
        path
        for path in set(manual_files) & set(plugin_files)
        if manual_files[path] != plugin_files[path]
    )

    if not manual_only and not plugin_only and not changed:
        print("Starter templates are in sync.")
        return 0

    if manual_only:
        print("Only in templates/project-starter:")
        for path in manual_only:
            print(f"  - {path}")

    if plugin_only:
        print("Only in plugin bundled assets:")
        for path in plugin_only:
            print(f"  - {path}")

    if changed:
        print("Content differs:")
        for path in changed:
            print(f"  - {path}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
