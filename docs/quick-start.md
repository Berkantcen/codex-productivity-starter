# Quick Start

Use this guide to make a repository Codex-ready in about 15 minutes.

If you want a concrete target before starting, inspect
`examples/generated-workspace/` in this repository.

## Option A: Plugin Onboarding

Use this path for non-technical users or team rollout.

After the Codex Productivity plugin is installed, open a new workspace and ask:

```text
Make this workspace Codex-ready.
```

From any shell on the machine where you use Codex, install it from GitHub with:

```bash
codex plugin marketplace add Berkantcen/codex-productivity-starter --ref main
codex plugin add codex-productivity@codex-productivity-starter
```

Codex will inspect the workspace, create missing starter files, and fill the
first draft with concrete paths and validation notes where possible.

If the workspace is empty, Codex should ask a few plain-language questions first
about the project name, type of work, expected users, common tasks, boundaries,
and readiness checks. It can then create useful first drafts without requiring
the user to know terminal commands or repository structure.

## Option B: Manual Setup

Use this path when you want to copy the files yourself.

If you are reading this from a cloned checkout, run the copy command from this
repository root or replace the source path with an absolute path.

## 1. Copy The Starter

From this repository:

```bash
cp -R templates/project-starter/. /path/to/your-project/
```

## 2. Fill The Project Snapshot

Open `/path/to/your-project/AGENTS.md` and fill:

- project name
- framework/language
- package manager
- entry points
- test locations
- validation commands

## 3. Map The Repo

Open `repo-map.md` and list the paths Codex should inspect first for common
tasks.

This is the file that prevents repeated "where is this feature?" discovery.

## 4. Write The Validation Plan

Open `validation-plan.md` and write the real commands your project supports.

If a command is currently broken or needs environment setup, write that down.
Honest validation limits are more useful than fake confidence.

## 5. Use A Task Brief

Before asking Codex to work, fill `task-brief.md`.

Keep one task brief focused on one outcome. If the work naturally splits into
several features, create several task briefs.

## 6. Improve After Each Task

When Codex has to rediscover something useful, add it to:

- `repo-map.md` for navigation
- `validation-plan.md` for commands
- `decision-log.md` for durable decisions
- `AGENTS.md` for operating rules

The starter becomes more valuable as your project learns from real tasks.
