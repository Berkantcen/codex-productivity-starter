# Decision Log

Use this file for durable decisions Codex should not rediscover.

Keep entries short and concrete.

## Decisions

## 2026-07-15 - Keep Generated API Files Read-Only

Decision: Any API contract change must be made in the source schema and then
regenerated. Do not hand-edit files under `src/generated/`.

Reason: Manual edits are lost on regeneration and make contract drift harder to
debug.

Applies to: `src/generated/`, `src/services/`

Revisit when: The project replaces code generation or moves to handwritten API
clients.

## 2026-07-15 - Prefer Service Calls Over Direct Fetch In Components

Decision: UI components should call feature services instead of issuing direct
HTTP requests.

Reason: Services already centralize auth headers, retries, and error mapping.

Applies to: `src/features/`, `src/services/`

Revisit when: The project adopts a different shared data-fetching layer.
