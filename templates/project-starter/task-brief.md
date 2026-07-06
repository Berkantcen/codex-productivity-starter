# Task Brief

Use this file to give Codex one scoped task.

## Goal

Describe the outcome in one or two sentences.

```text
<What should be true after the task is complete?>
```

## Scope

In scope:

- `<path, feature, behavior, or workflow>`

Out of scope:

- `<unrelated cleanup, migration, or feature>`

## Context

- Related issue/PR/design/spec: `<link-or-none>`
- User-facing behavior: `<expected behavior>`
- Current problem: `<current behavior or gap>`
- Relevant files if known: `<paths-or-unknown>`

## Constraints

- Keep existing architecture unless the task explicitly requires changing it.
- Do not change public APIs unless requested.
- Do not modify generated files manually unless this project allows it.
- Do not introduce new dependencies without explaining why.

## Validation Required

Commands:

```bash
<focused-test-command>
<lint-or-typecheck-command>
```

Manual checks:

- `<manual check>`

## Handoff Format

Return:

- summary of changes
- validation results
- residual risks or follow-ups

