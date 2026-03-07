# Social Drafter

**Schedule:** Daily at 7:30 AM (local timezone)
**Delivery:** Workspace file + Slack notification
**Type:** Claude scheduled task (cron-based)

## Purpose

Automated content creation pipeline. Scouts recent product evaluations and benchmark data, creates branded data visualizations, drafts social posts, and runs every draft through the Copy Reviewer skill before delivery.

## Pipeline

```
1. Scout Data Sources
   - Recent product evaluations and benchmark results
   - Overnight news (from Morning Brief output)
   - Trending topics in AI/ML
   |
   v
2. Select Content Angles
   - SOTA (state of the art) result? -> Comparison post
   - Regression detected? -> Analysis post
   - New model launched? -> First-look post
   - Competitor move? -> Positioning post
   |
   v
3. Generate Branded Visuals
   - Data Visualization skill creates charts/graphics
   - Brand colors, logo placement, footer text enforced
   - Overlap detection runs automatically
   |
   v
4. Draft Posts
   - Twitter/X: concise, data-first, narrative hook
   - LinkedIn: longer format, professional tone, industry context
   |
   v
5. Copy Review (AUTOMATIC)
   - Every draft runs through the 12-rule Copy Reviewer
   - Banned phrases caught, tone calibrated, "so what" test applied
   - Fails get flagged with specific fixes
   |
   v
6. Deliver Package
   - Ready-to-post content saved to workspace
   - Slack notification with summary
   - Human reviews, approves, copies to Buffer
```

## Output

A markdown file with:
- 3-5 Twitter/X posts (each with: post text, suggested visual, review status)
- 1-2 LinkedIn posts (longer format, same review process)
- Any flagged items that need human editing

## Design Decisions

**Why auto-review:** The biggest quality risk in high-volume content is inconsistency. Running every draft through the same 12 rules ensures brand voice stays calibrated even when producing 20+ posts per week.

**Why daily instead of weekly batch:** Originally designed as a Monday-only batch. Switched to daily to capture reactive content opportunities (model launches, competitor moves) same-day. The Monday batch still happens for planned content.
