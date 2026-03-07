# Agent Review (Meta-Agent)

**Schedule:** Friday at 3:00 PM (local timezone)
**Delivery:** Workspace file + Slack notification
**Type:** Claude scheduled task (cron-based)

## Purpose

The system reviewing itself. Audits all skills, scheduled tasks, and MCP connectors. Checks for quality, redundancy, gaps, and trigger reliability. The only agent whose job is to improve the other agents.

## What It Audits

### Skills Health Check
- **Trigger descriptions:** Are they specific enough to fire reliably? (Bad: "Create a scheduled task." Good: "Create a scheduled task when the user says 'schedule this,' 'automate this weekly,' or 'run this on a cron.'")
- **Rule specificity:** Are pass/fail criteria clear or subjective?
- **Redundancy:** Do any skills overlap in function?
- **Missing skills:** Based on weekly workflow patterns, what should exist but doesn't?

### Tasks Health Check
- **Execution status:** Did each task run this week? Any failures?
- **Output quality:** Is the output still useful or has it become noise?
- **New task ideas:** Based on manual work patterns, what should be automated next?

### Workflow Upgrades
- **Skill chaining opportunities:** Which skills could be connected into pipelines?
- **MCP connector utilization:** Are connected tools being used to their potential?
- **Bigger ideas:** Strategic automation opportunities beyond incremental improvements

### Quick Wins
- 3-5 specific, actionable improvements that can be made this week

## Grading System

Each component gets a letter grade:
- **A:** Working well, no changes needed
- **B:** Functional but has improvement opportunities
- **C:** Working but with notable issues
- **D:** Barely functional, needs significant work
- **F:** Broken or not being used

## Design Decisions

**Why a meta-agent:** Systems degrade over time. Triggers become stale, output becomes noisy, new needs emerge. Without a regular audit, the system slowly becomes less useful. The meta-agent prevents entropy.

**Why Friday at 3 PM:** End of the work week, after the Weekly Architect has context on what happened. Early enough to make quick fixes before the weekend.

**Why letter grades:** Forces a concrete assessment instead of "things are fine." It's easy to ignore "could be improved." It's hard to ignore "F: Broken."
