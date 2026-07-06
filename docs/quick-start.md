# Quick Start

Use this guide to make a repository Codex-ready in about 15 minutes.

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

