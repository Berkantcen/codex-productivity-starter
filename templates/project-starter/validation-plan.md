# Validation Plan

Use this file to keep validation consistent and project-specific.

## Fast Checks

Run these for most small changes:

```bash
<format-or-lint-command>
<focused-test-command>
```

## Full Checks

Run these before larger handoffs or pull requests:

```bash
<full-test-command>
<typecheck-command>
<build-command>
```

## Surface-Specific Checks

| Changed Surface | Required Checks |
| --- | --- |
| UI/component | `<test command plus manual browser check>` |
| API/service | `<unit/integration test command>` |
| Database/schema | `<migration validation command>` |
| Config/deployment | `<build or smoke command>` |
| Docs only | `git diff --check` |

## Manual QA Checklist

- `<open page or run command>`
- `<verify expected behavior>`
- `<check edge case>`
- `<confirm no unrelated regression>`

## Known Validation Limits

- `<command>` currently fails because `<reason>`.
- `<environment>` is required for `<check>`.

When a validation command cannot be run, Codex should say why and provide the
strongest completed alternative.

