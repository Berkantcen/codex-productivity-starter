# Task Brief

Use this file to give Codex one scoped task.

## Goal

Describe the outcome in one or two sentences.

```text
Add a bulk-close action to the support inbox so agents can resolve selected
tickets from the list view.
```

## Scope

In scope:

- inbox list selection behavior
- bulk-close action wiring
- focused tests for selection and success/error states

Out of scope:

- redesigning the inbox layout
- changing ticket status rules
- unrelated support dashboard cleanup

## Context

- Related issue/PR/design/spec: `SUP-142`
- User-facing behavior: agents can resolve selected tickets without opening each one
- Current problem: list view only allows one-by-one closing from the detail panel
- Relevant files if known: `src/features/inbox/`, `src/services/tickets.ts`

## Constraints

- Keep existing architecture unless the task explicitly requires changing it.
- Do not change public APIs unless requested.
- Do not modify generated files manually unless this project allows it.
- Do not introduce new dependencies without explaining why.

## Validation Required

Commands:

```bash
npm run test -- inbox
npm run typecheck
```

Manual checks:

- select multiple tickets and close them
- confirm the list refreshes and selection resets

## Handoff Format

Return:

- summary of changes
- validation results
- residual risks or follow-ups
