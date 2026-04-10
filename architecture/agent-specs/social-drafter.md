# Social Drafter

**Schedule:** Daily at 7:30 AM (local timezone, 30 min after Morning Brief)
**Delivery:** Workspace file + Slack notification
**Type:** Claude scheduled task (cron-based)
**Dependency:** Chrome extension (Claude in Chrome) required for all data gathering
**Skill file:** `.skills/skills/daily-social-drafter/SKILL.md`

## Purpose

Automated content creation pipeline. Reads the Morning Brief for editorial direction, scouts live product data via Chrome, creates branded data visualizations, drafts social posts, and runs every draft through the Copy Reviewer skill before delivery.

## Pre-Flight: Chrome Connection Check

The skill requires the Chrome browser extension for all data gathering. No web search fallbacks. No workarounds.

1. Check `tabs_context_mcp` for active Chrome connection
2. If connected: proceed to Phase 0
3. If disconnected: send Slack DM to Jake, wait, retry every 2 minutes
4. If still disconnected after 30 minutes: send follow-up DM, skip today's run

## Pipeline

```
0. Check What's Already Been Posted
   - Navigate to x.com (@LayerLens feed), review last 15-20 posts
   - Navigate to LinkedIn, review last 5-7 posts
   - Build "DO NOT REPEAT" list of recent topics
   |
   v
0.5. Read the Morning Brief
   - Find today's Morning Brief (runs at 7:00 AM, 30 min before)
   - Extract POST and MONITOR items from approval queue
   - POST items = primary content seeds
   - MONITOR items = secondary seeds if quota not filled
   - Cross-reference against DO NOT REPEAT list
   |
   v
1. Scout for New Data (via Chrome)
   A. Stratix Platform (app.layerlens.ai)
      - New evaluations, updated benchmarks, score changes
   B. LL Marketing Workspace
      - New synthetic datasets, tools, judge optimization runs
   C. Bleeding-Edge Research Reference
      - Cross-reference evals against benchmark reference guide
      - Determine which results are newsworthy vs. noise
   |
   v
2. Decide What to Post
   - Twitter/X: 3-4 posts (SOTA, regression, comparison, product)
   - LinkedIn: 1-2 posts (deeper analysis, 300-500 words min)
   - Priority: SOTA > regression > comparison > new capability > evergreen
   - Fallback: Stratix Premium feature content if nothing new
   |
   v
3. Draft Copy
   - Hard rules enforced: no em dashes, no banned phrases, no AI slop
   - Every post needs "so what" context and specific CTA
   - Every post must pass differentiation test
   |
   v
4. Generate Branded Visuals
   - layerlens-graphics skill creates charts/graphics
   - layerlens-logo skill adds official logo
   - Brand colors, footer text, overlap detection enforced
   |
   v
5. Copy Review (AUTOMATIC)
   - Every draft runs through the 12-rule Copy Reviewer
   - Banned phrases caught, tone calibrated, "so what" test applied
   - Fails get revised and re-checked until clean
   |
   v
6. Deliver Package
   - Content saved to workspace: social-drafts/YYYY-MM-DD/
   - Slack notification with summary
   - Human reviews, approves, copies to Buffer
```

## Output

A structured folder (`social-drafts/YYYY-MM-DD/`) containing:

- `brief.md`: what was found, content plan, rationale
- `twitter/`: 3-4 posts (each: copy markdown + branded graphic PNG)
- `linkedin/`: 1-2 posts (each: copy markdown + branded graphic PNG)
- Any flagged items that need human editing

## Skill Orchestration

| Skill | Phase | What It Does |
|-------|-------|-------------|
| `layerlens-graphics` | Phase 4 | Creates branded charts and social cards |
| `layerlens-logo` | Phase 4 (via graphics) | Adds official logo to all images |
| `copy-reviewer` | Phase 5 | Reviews every draft against brand guidelines |

## Key Integration: Morning Brief Chain

The Morning Brief (7:00 AM) surfaces overnight AI news, model releases, benchmark results, and competitor moves. It tags items as POST/MONITOR/IGNORE. The Social Drafter (7:30 AM) consumes this output as its primary editorial input, closing the loop from signal detection to publishable content.

This was originally listed as a "Future improvement" in the system architecture. Now implemented.

## Design Decisions

**Why Chrome-only:** Stratix, X, and LinkedIn all require authenticated browser access. Web search can't see live evaluation data or check what's already been posted. The Chrome extension is the single source of truth.

**Why auto-review:** The biggest quality risk in high-volume content is inconsistency. Running every draft through the same 12 rules ensures brand voice stays calibrated even when producing 20+ posts per week.

**Why daily instead of weekly batch:** Originally designed as a Monday-only batch. Switched to daily to capture reactive content opportunities (model launches, competitor moves) same-day. The Monday batch still happens for planned content.

**Why 7:30 AM (not 7:00):** Staggered 30 minutes after the Morning Brief so the brief's output file exists before the Social Drafter reads it. The brief sets editorial direction; the drafter executes.

## Future Phases

- **Phase 7 (Calendar Integration):** Check upcoming releases and product launches. Create teaser, announcement, and follow-up content aligned with the Narrative Shift phases.
- **Phase 8 (Short Demo Videos):** Screen-recording-style demos of Stratix Premium features. Start with annotated screenshot sequences.
