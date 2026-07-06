# Example: React Feature Task

## Goal

Add a status filter to the orders list so users can filter by `Pending`,
`Shipped`, or `Cancelled`.

## Scope

In scope:

- orders list filter UI
- URL query parameter sync for `status`
- focused tests for filter state

Out of scope:

- redesigning the orders page
- changing backend API contracts
- changing unrelated filters

## Context

- List route: `src/routes/orders.tsx`
- Feature module: `src/features/orders/`
- Existing filters: `src/features/orders/OrderFilters.tsx`
- API service: `src/services/orders.ts`

## Validation Required

```bash
npm run test -- orders
npm run typecheck
```

Manual checks:

- open the orders list
- select each status
- refresh the page and confirm the selected status remains in the URL
