---
name: codex-ready-workspace
description: Create or update Codex-ready workspace onboarding files for a repository, project folder, or empty workspace. Use when the user asks to make a workspace Codex-ready, reduce repeated context or token usage, create starter files such as AGENTS.md/repo-map.md/validation-plan.md/task-brief.md/decision-log.md/handoff-summary.md, initialize guidance for non-technical users, ask onboarding questions for a new project, or audit a workspace for missing Codex productivity files.
---

# Codex Ready Workspace

## Overview

Create concise, practical workspace guidance that helps Codex work with less repeated context. Favor files that non-technical users can ask Codex to create or update with a simple prompt.

## Workflow

1. Determine the workspace mode:
   - Existing workspace: files, folders, README, package/build files, docs, or source are present.
   - Empty workspace: no meaningful project files exist yet.
2. For an existing workspace, inspect before writing files:
   - Read existing `AGENTS.md`, `README.md`, package/build files, docs, and obvious source directories.
   - Run `rg --files` when available to understand structure.
   - Check `git status --short --branch` when the workspace is a git repository.
3. For an empty workspace, ask the guided intake questions before writing final content.
4. Create missing starter files from bundled assets using `scripts/init_codex_workspace.py`.
5. Do not overwrite existing files unless the user explicitly asks for replacement.
6. Replace generic placeholders with concrete facts discovered from the workspace or provided in chat.
7. Keep the generated guidance short enough to be loaded at task start.
8. Report created files, skipped existing files, assumptions, and validation.

## Empty Workspace Intake

When there is nothing useful to inspect, ask concise questions in chat before filling the files. Keep the questions non-technical and avoid asking for terminal commands.

Ask these first:

1. What is the workspace or project name?
2. What kind of work will happen here? Examples: software project, analysis, product planning, operations, documentation, research.
3. Who will use this workspace? Examples: developers, analysts, product managers, QA, leadership.
4. What should Codex help with most often?
5. Are there files, data, systems, or topics Codex should avoid?
6. How should Codex prove work is ready? Examples: tests, reviewed document, checked spreadsheet, manual checklist, stakeholder approval.

If the user has a technical project in mind, also ask:

- What language, framework, or tool stack do you expect to use?
- What commands should Codex run for validation, if known?

If the user cannot answer everything, continue with sensible placeholders and mark unknowns clearly. Do not block the setup just because the workspace is new.

Use the answers to customize:

- `AGENTS.md` with audience, operating rules, boundaries, and handoff expectations.
- `repo-map.md` with expected folders or planned areas, even if they do not exist yet.
- `validation-plan.md` with known checks plus honest "not defined yet" entries.
- `task-brief.md` with a simple request format that matches the user's role.
- `decision-log.md` with any durable startup decisions from the intake.
- `handoff-summary.md` with a final report format the user can understand.

## Starter Files

Create or maintain these files:

- `AGENTS.md` - operating rules for Codex in this workspace.
- `repo-map.md` - paths Codex should inspect first for common tasks.
- `validation-plan.md` - commands and manual checks that prove work is ready.
- `task-brief.md` - a simple intake format for one scoped request.
- `decision-log.md` - durable choices Codex should not rediscover.
- `handoff-summary.md` - expected final response shape.

For non-code workspaces, still create the files, but adapt wording away from software-only terms. For example, use "documents", "data sources", "approval checks", and "review workflow" where that is more accurate than "source code" or "tests".

## Script

Use the bundled script when initializing files:

```bash
python3 <skill-folder>/scripts/init_codex_workspace.py <target-workspace>
```

Validation for the script:

```bash
python3 <skill-folder>/scripts/init_codex_workspace.py --help
```

Use `--force` only after the user explicitly asks to overwrite existing guidance.

## Customization Rules

- Prefer concrete paths and commands over generic advice.
- Keep files practical and concise; do not produce long theory.
- Preserve existing user content and dirty worktree changes.
- Avoid private names, internal URLs, tokens, credentials, and customer data.
- For code repositories, capture real package managers, entry points, test locations, generated code rules, and validation commands.
- For analyst/product workspaces, capture important folders, data inputs, review/approval steps, recurring deliverables, and handoff expectations.
- If validation commands are unknown, say so in `validation-plan.md` instead of inventing commands.
- For empty workspaces, include "planned" paths or sections only when they came from the user or are clearly framed as suggestions.

## Final Response

End with:

- files created or updated
- existing files preserved
- what was inferred from the workspace
- validation run
- the simplest next prompt the user can use for their first task
