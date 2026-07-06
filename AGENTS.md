# Agent Instructions

This repository is a public starter kit. Keep content practical, concise, and
safe to reuse across many software projects.

## Working Rules

- Prefer examples that are framework-agnostic unless a file is clearly scoped to
  a specific stack.
- Avoid company-private names, internal URLs, tokens, credentials, or proprietary
  implementation details.
- Keep templates copy-pasteable.
- Use plain Markdown and shell snippets that work on a typical Unix-like
  development machine.
- Do not add heavy dependencies for documentation-only changes.
- When adding a template, include enough structure for a user to apply it without
  needing another explanation.

## Validation

For documentation changes:

```bash
find . -name '*.md' -print
git diff --check
```

For future scripts, add a small validation command next to the script and mention
it in `README.md`.

