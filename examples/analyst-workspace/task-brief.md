# Example: Analyst Workspace Task Brief

## Goal

Prepare a weekly operations summary that highlights the biggest fulfillment
delays, likely causes, and the actions leadership should review.

## Scope

In scope:

- summarize this week’s fulfillment and cancellation data
- identify the top three operational bottlenecks
- recommend next actions for leadership review

Out of scope:

- changing source data pipelines
- rebuilding dashboards
- long-term forecasting work

## Context

- Source spreadsheet: `inputs/weekly-operations.xlsx`
- Previous summary deck: `reports/weekly-operations-summary.pptx`
- Known issue log: `notes/incidents.md`
- Audience: operations manager and regional leads

## Constraints

- Keep the summary understandable for non-technical readers.
- Separate confirmed data from inference.
- Flag missing or suspicious data instead of filling gaps silently.
- Use the existing report structure unless the request says otherwise.

## Validation Required

Checks:

- numbers in the summary match the source spreadsheet
- each recommendation links back to observed data
- risks and data gaps are called out clearly

## Handoff Format

Return:

- executive summary
- key bottlenecks with evidence
- data quality limits
- suggested follow-up actions
