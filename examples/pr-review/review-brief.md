# Example: PR Review Brief

## Goal

Review the PR for correctness, regression risk, and missing validation.

## Scope

Focus on:

- behavior changes in touched files
- edge cases introduced by the diff
- tests or manual checks that should exist
- risky architecture or API changes

Ignore:

- unrelated style preferences
- broad refactors not required by the PR
- files not touched unless needed to understand the change

## Review Output

Lead with findings ordered by severity.

Each finding should include:

- severity
- file and line if available
- concrete risk
- suggested fix or validation

If no issues are found, say that clearly and mention residual test risk.

