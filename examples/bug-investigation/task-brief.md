# Example: Bug Investigation

## Goal

Find why users sometimes see a blank dashboard after login and propose the
smallest safe fix.

## Scope

In scope:

- login redirect flow
- dashboard route loading state
- API error handling for the initial dashboard request

Out of scope:

- redesigning authentication
- replacing the router
- broad dashboard refactors

## Context

- Login page: `src/features/auth/LoginPage.tsx`
- Dashboard route: `src/routes/dashboard.tsx`
- Dashboard API call: `src/services/dashboard.ts`
- Error boundary: `src/shared/ErrorBoundary.tsx`

## Investigation Instructions

1. Reproduce or inspect the route transition.
2. Check whether loading, empty, and error states are distinguishable.
3. Identify the smallest behavior change that prevents a blank screen.
4. Add or update the most focused test if possible.

## Validation Required

```bash
npm run test -- dashboard
npm run typecheck
```

