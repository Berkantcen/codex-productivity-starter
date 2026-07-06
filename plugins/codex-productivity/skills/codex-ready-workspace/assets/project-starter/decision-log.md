# Decision Log

Use this file for durable decisions Codex should not rediscover.

Keep entries short and concrete.

## Template

```md
## YYYY-MM-DD - <decision title>

Decision: <what was decided>

Reason: <why this is the preferred direction>

Applies to: <paths, modules, workflows, or task types>

Revisit when: <condition that would make this decision stale>
```

## Decisions

## YYYY-MM-DD - Example: Prefer Existing Service Layer

Decision: New API calls should go through the existing service layer instead of
calling `fetch` directly from UI components.

Reason: The service layer already centralizes auth, error handling, retries, and
test mocking.

Applies to: `src/services/`, `src/features/`

Revisit when: The project introduces a new API client architecture.
