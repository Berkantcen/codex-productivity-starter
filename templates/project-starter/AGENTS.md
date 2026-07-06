# Agent Instructions

Use this file to teach Codex how to work inside this repository.

Replace the placeholders with concrete project guidance. Keep this file short
enough to be read at the start of most tasks.

## Project Snapshot

- Project name: `<project-name>`
- Primary language/framework: `<language-and-framework>`
- Package manager/build tool: `<tooling>`
- Main application entry points: `<paths>`
- Main test locations: `<paths>`

## Working Rules

- Inspect the relevant files before proposing or editing code.
- Keep changes scoped to the task brief.
- Prefer existing project patterns over new abstractions.
- Do not rewrite unrelated code while solving a narrow task.
- Preserve user changes in dirty worktrees.
- Report validation results, including commands that could not be run.

## Architecture Boundaries

- Shared utilities live in: `<path>`
- Feature modules live in: `<path>`
- API/client code lives in: `<path>`
- Generated code lives in: `<path-or-none>`
- Tests should follow examples in: `<path>`

## Validation Commands

Use the most relevant commands for the changed surface:

```bash
<lint-command>
<test-command>
<build-command>
```

## Handoff Expectations

Final responses should include:

- what changed
- validation performed
- any validation that could not be performed
- manual checks that remain
- files worth reviewing first
