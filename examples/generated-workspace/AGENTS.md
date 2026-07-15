# Agent Instructions

This repository contains a small customer support portal. Keep Codex focused on
incremental product work, bug fixes, and safe operational changes.

## Project Snapshot

- Project name: Support Hub
- Primary language/framework: TypeScript React
- Package manager/build tool: npm + Vite
- Main application entry points: `src/main.tsx`, `src/App.tsx`
- Main test locations: `src/**/*.test.tsx`, `src/**/*.test.ts`

## Working Rules

- Read the relevant route, feature module, and service before proposing changes.
- Keep list-page, API, and auth changes scoped to the task brief.
- Prefer existing hooks and service helpers over new abstractions.
- Do not edit generated API types manually.
- Report focused validation plus any manual browser checks that remain.

## Architecture Boundaries

- Shared utilities live in: `src/shared/`
- Feature modules live in: `src/features/`
- API/client code lives in: `src/services/`
- Generated code lives in: `src/generated/`
- Tests should follow examples in: `src/features/**/__tests__/`

## Validation Commands

Use the most relevant commands for the changed surface:

```bash
npm run lint
npm run test -- support
npm run build
```

## Handoff Expectations

Final responses should include:

- what changed
- validation performed
- any validation that could not be performed
- manual checks that remain
- files worth reviewing first
