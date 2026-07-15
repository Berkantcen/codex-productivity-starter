# Validation Plan

Use this file to keep validation consistent and project-specific.

## Fast Checks

Run these for most small changes:

```bash
npm run lint
npm run test -- support
```

## Full Checks

Run these before larger handoffs or pull requests:

```bash
npm run test
npm run typecheck
npm run build
```

## Surface-Specific Checks

| Changed Surface   | Required Checks                                  |
| ----------------- | ------------------------------------------------ |
| UI/component      | focused test plus browser check on the changed flow |
| API/service       | service tests plus error-state verification      |
| Database/schema   | migration validation and fixture refresh         |
| Config/deployment | build plus smoke check in the target environment |
| Docs only         | `git diff --check`                               |

## Manual QA Checklist

- open the changed route
- verify success, loading, and error states
- check one realistic edge case
- confirm no unrelated navigation regression

## Known Validation Limits

- end-to-end tests require staging credentials managed outside the repo
- email and third-party webhook checks need a shared sandbox environment

When a validation command cannot be run, Codex should say why and provide the
strongest completed alternative.
