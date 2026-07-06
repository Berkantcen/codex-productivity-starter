# Contributing

Thanks for improving Codex Productivity Starter.

## Good Contributions

- clearer templates
- realistic examples
- stack-specific starter variants
- validation patterns
- docs that reduce repeated project setup context

## Content Rules

- Keep examples generic and safe for public use.
- Do not include private company code, internal URLs, secrets, or customer data.
- Prefer practical files people can copy into a repository.
- Avoid long theory unless it directly improves usage.

## Suggested Change Format

When opening a PR, include:

- what template, doc, or example changed
- why the change helps Codex work more reliably
- any command used to validate the repo

## Local Validation

```bash
find . -name '*.md' -print
git diff --check
```

For plugin changes:

```bash
python3 plugins/codex-productivity/skills/codex-ready-workspace/scripts/init_codex_workspace.py --help
```

If you have Codex plugin development helpers installed, also run the plugin and
skill validators before publishing.
