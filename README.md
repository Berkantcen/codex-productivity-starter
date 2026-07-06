# Codex Productivity Starter

Make any software project easier for Codex to understand, change, review, and
handoff without repeating the same context in every thread.

This repository is a practical starter kit for Codex-ready workspaces. It gives
you templates for project context, task briefs, validation plans, decision logs,
and handoff summaries so AI-assisted development uses less repeated context and
produces more consistent results.

## What This Solves

Most teams waste time and tokens by explaining the same things repeatedly:

- how the project is structured
- where important features live
- which commands are safe to run
- how tests, lint, build, and manual QA should be validated
- what architectural decisions should not be rediscovered
- what the agent should report before handing work back

Codex works better when that context is written once, kept close to the repo,
and loaded only when relevant.

## Start Here

For the fastest setup, follow [Quick Start](docs/quick-start.md).

Copy the starter files into your project:

```bash
cp -R templates/project-starter/. /path/to/your-project/
```

Then fill the files in this order:

1. `AGENTS.md` - project-level operating rules for Codex.
2. `repo-map.md` - where important code, tests, docs, and configs live.
3. `validation-plan.md` - commands and manual checks that prove work is ready.
4. `task-brief.md` - the format for giving Codex a single scoped task.
5. `decision-log.md` - durable choices Codex should not rediscover.
6. `handoff-summary.md` - the expected final report format.

## Recommended Workflow

Use this prompt in a fresh Codex thread from your project root:

```text
Read AGENTS.md, repo-map.md, validation-plan.md, and task-brief.md.
Then inspect the relevant code before proposing or making changes.
Keep the scope tight to the task brief and report validation results clearly.
```

For a new project, ask Codex:

```text
Use the Codex Productivity Starter structure to make this repository
Codex-ready. Inspect the codebase first, then fill AGENTS.md, repo-map.md,
validation-plan.md, decision-log.md, and handoff-summary.md with concrete
project-specific guidance.
```

## Repository Contents

```text
templates/project-starter/
  AGENTS.md
  task-brief.md
  repo-map.md
  validation-plan.md
  decision-log.md
  handoff-summary.md

docs/
  quick-start.md
  codex-ready-workspace.md
  token-efficiency.md
  adoption-playbook.md
  youtube-series-outline.md

examples/
  react-feature-task/
  bug-investigation/
  pr-review/
```

## Principles

- Write durable project context once.
- Keep task instructions small and concrete.
- Load only the files needed for the current task.
- Prefer repo-specific validation over generic confidence.
- Preserve user work in dirty worktrees.
- Make final handoffs useful for humans, not just for logs.

## Who This Is For

- developers who use Codex daily
- teams piloting AI-assisted software delivery
- engineering managers evaluating practical AI workflows
- creators teaching agentic coding with real project examples

## Video Companion

The repo is designed to work well with a practical content series. See
[YouTube Series Outline](docs/youtube-series-outline.md) for a first five-video
sequence.

## Roadmap

- Add more real-world task examples.
- Add language-specific starter variants.
- Add a simple setup script.
- Package the workflow as a Codex plugin after the template proves useful.
