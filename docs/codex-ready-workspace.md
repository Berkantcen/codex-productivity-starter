# Codex-Ready Workspace

A Codex-ready workspace gives the agent enough durable context to work quickly
without loading the whole repository or asking the user to repeat basic facts.

## Minimum Useful Set

Start with six files:

- `AGENTS.md` for operating rules.
- `repo-map.md` for navigation.
- `validation-plan.md` for proof of readiness.
- `task-brief.md` for scoped task intake.
- `decision-log.md` for durable project decisions.
- `handoff-summary.md` for final response expectations.

This is intentionally small. The goal is not to document everything. The goal is
to remove repeated explanations and guide Codex toward the right files.

## What Good Looks Like

Good workspace context is:

- specific to the repository
- short enough to load at task start
- explicit about validation
- honest about known blockers
- clear about what should not be touched

Weak workspace context is:

- generic framework advice
- long architecture history
- stale commands
- hidden tribal knowledge
- broad permission to refactor

## Setup Loop

1. Inspect the real repository.
2. Fill the starter templates with concrete paths and commands.
3. Run one small task using the templates.
4. Update the templates with anything Codex had to rediscover.
5. Repeat until common tasks no longer need long setup prompts.
