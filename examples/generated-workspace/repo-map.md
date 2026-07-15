# Repo Map

Use this file to help Codex find the right context quickly.

## High-Level Structure

| Area                        | Path               | Notes                                 |
| --------------------------- | ------------------ | ------------------------------------- |
| Application entry           | `src/main.tsx`     | Bootstraps the app shell              |
| Feature modules             | `src/features/`    | Route-level and domain feature code   |
| Shared components/utilities | `src/shared/`      | Reusable UI, hooks, and helpers       |
| API clients/services        | `src/services/`    | HTTP clients and feature-facing calls |
| Tests                       | `src/**/*.test.ts` | Focused unit and integration tests    |
| Scripts                     | `scripts/`         | Local automation and validation       |
| Docs                        | `docs/`            | Product and technical guidance        |

## Common Task Routes

| Task Type           | Start Here                      | Then Check                       |
| ------------------- | ------------------------------- | -------------------------------- |
| Add a UI feature    | `src/features/<feature>/`       | route file and shared components |
| Fix a bug           | failing feature route or hook   | related tests and service calls  |
| Change API behavior | `src/services/`                 | generated client and tests       |
| Update copy/i18n    | feature component and locale    | all supported locales            |
| Review a PR         | changed files                   | tests, validation plan, docs     |

## Important Conventions

- Naming: feature-first folders and descriptive hook names
- State management: local state first, shared state through existing providers
- Error handling: route-level boundaries plus service-level error mapping
- Logging/observability: use the existing telemetry helper, not ad hoc logs
- Styling/UI: reuse app shell and component library patterns
- Test data/fixtures: keep fixtures close to the changed feature

## Do Not Touch Without Explicit Approval

- `src/generated/`
- deployment and production credential flows
