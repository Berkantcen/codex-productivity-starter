# Token Efficiency

Token efficiency is not about making prompts tiny. It is about preventing the
same context from being rediscovered in every task.

## High-Impact Moves

### 1. Put Stable Context In Files

Do not paste project structure, commands, and conventions into every prompt.
Keep them in repo files:

- `AGENTS.md`
- `repo-map.md`
- `validation-plan.md`
- `decision-log.md`

Then ask Codex to read only the relevant files.

### 2. Keep Task Briefs Narrow

A good task brief says:

- what outcome is required
- what is in scope
- what is out of scope
- how success should be validated

This prevents the agent from spending tokens on adjacent cleanup or speculative
architecture work.

### 3. Use Progressive Disclosure

Start broad, then load details only when needed:

1. project operating rules
2. repo map
3. task brief
4. relevant source files
5. validation plan

This pattern is more efficient than preloading every standard and every example.

### 4. Record Reusable Decisions

If Codex discovers a rule that will matter again, add it to `decision-log.md`.

Examples:

- generated files should not be edited manually
- API clients must go through a shared service
- full test suite requires a local dependency
- deployments need a specific environment variable

### 5. Prefer Concrete Validation

Confidence is cheaper when it comes from commands and manual checks instead of
long explanation.

Ask for:

```text
Run the focused validation path and report commands, results, and remaining
manual checks.
```
