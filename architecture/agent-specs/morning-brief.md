# Morning Brief (Chief of Staff v0.1)

**Schedule:** Daily at 7:00 AM (local timezone)
**Delivery:** Slack channel + workspace file
**Type:** Claude scheduled task (cron-based)

## Purpose

The intelligence briefing. Scans overnight AI/model/benchmark/competitor news from multiple sources and delivers a structured brief with an approval queue. Designed to replace 45-60 minutes of manual news monitoring with a 5-minute review.

## Data Sources (8-Step Gathering)

| Step | Source | What It Finds |
|------|--------|--------------|
| 1 | Web search | Overnight AI news: model releases, benchmark results, funding rounds, policy changes |
| 2 | GitHub trending | ML/AI repositories gaining traction, new tools, framework updates |
| 3 | Twitter/X signals | AI thought leader posts, viral threads, breaking announcements |
| 4 | LinkedIn signals | Industry commentary, partnership announcements, hiring patterns |
| 5 | Slack (all channels) | Overnight messages needing response, blockers, action items from teammates |
| 6 | Ahrefs | Competitor domain rating changes, new backlinks, keyword movement |
| 7 | SEO/AEO check | Own site: keyword ranking changes, new indexed pages, traffic anomalies |
| 8 | Product app | New evaluations run, benchmark results added, notable user activity |

## Output Structure

### Section 1: TL;DR (3-5 bullets)
The top 3-5 things that matter today. Written for a 30-second skim.

### Section 2: AI/Model News
Overnight developments, filtered to only what's relevant to the company's positioning.

### Section 3: Competitor Movement
Any changes in competitor activity, messaging, or metrics since yesterday.

### Section 4: Slack Action Items
Messages that need a response, grouped by urgency.

### Section 5: SEO/Metrics Snapshot
Quick numbers: keyword movements, traffic, domain changes.

### Section 6: Approval Queue
Numbered items tagged with recommended action:

```
APPROVAL QUEUE:
1. [POST] New model benchmark results dropped overnight. Draft comparison post.
2. [POST] Competitor launched new feature. Draft positioning response.
3. [MONITOR] Industry report published. Not actionable yet, track for weekly roundup.
4. [IGNORE] Minor competitor blog post. Not worth responding to.
```

**Interaction pattern:** Reply "post 1, 2" and drafts get created through the content pipeline (Social Drafter + Copy Reviewer).

## Design Decisions

**Why 7:00 AM (after Morning Commander at 6:15):** Morning Commander handles priorities and scheduling. Morning Brief handles intelligence. Separating them keeps each focused and prevents information overload in a single brief.

**Why an approval queue:** The system should surface opportunities, not make publishing decisions. The queue pattern gives the human final say while eliminating the discovery work.

**Why scan everything:** A solo marketer can't manually check Twitter, GitHub, LinkedIn, news sites, Slack, and internal tools every morning. The agent does the breadth; the human does the judgment.

**Strict 24-hour filter:** Only surfaces news from the last 24 hours. Prevents the brief from becoming a backlog dump.
