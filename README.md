# Jake-OS: AI Operating System for a Solo Marketing Department

A complete AI-augmented operating system built by one marketer to run an entire marketing function. 11 autonomous agents, 5 custom skills, 1 standalone monitoring agent, 1 custom Fireflies MCP server, all orchestrated through Claude, Slack, Notion, Google Calendar, Ahrefs, and Fireflies.

**Built with:** Claude (Anthropic), Claude Code, Cowork, Python, TypeScript, MCP (Model Context Protocol)

---

## The Problem

I'm a solo marketer at an AI startup. I run content, social, SEO, AEO (Answer Engine Optimization), competitive intel, influencer partnerships, and brand. The workload is designed for a team of 4-5 people. Instead of hiring, I built an AI operating system that handles the repetitive, high-volume work so I can focus on strategy and creative.

**Before Jake-OS:** 15 pain points. Tasks dying at every tool boundary. Meeting action items evaporating. 25-30 hours/week lost to unstructured evenings. Follow-ups vanishing across Slack, email, Telegram, and phone. No single system.

**After Jake-OS:** 11 agents running daily/weekly/monthly on autopilot. Content reviewed automatically against brand guidelines. Competitive intel surfaced weekly without manual research. Morning briefs delivered to Slack before I sit down. Meeting action items automatically converted to Notion tasks. The system comes to me; I don't go to it.

---

## System Architecture

```
+------------------------------------------------------------------+
|                         NOTION (Hub)                            |
|  +----------+ +--------+ +-----------+ +----------+            |
|  | Master   | |Projects| | Marketing | | Follow   |            |
|  | Tasks DB | |DB      | | Calendar  | | Ups DB   |            |
|  +----+-----+ +---+----+ +-----+-----+ +----+-----+            |
|       +------+-----+----------+-------------+                   |
|  +------------------------------------------+                   |
|  |         DAILY DASHBOARD PAGE             |                   |
|  | Today | Inbox | Week | Overdue           |                   |
|  | Waiting On | Skill Tracks               |                   |
|  +------------------------------------------+                   |
+---------------------------+--------------------------------------+
                            |
       +--------------------+--------------------+
       v                    v                    v
 +-----------+        +-----------+        +-------------+
 | Morning   |        | Weekly    |        | Monthly     |
 | Commander |        | Architect |        | Strategist  |
 | 6:15 AM   |        | Sun 7 PM  |        | 1st, 8 AM   |
 +-----+-----+        +-----+-----+        +------+------+
       +---------------------+---------------------+
                             v
       +--------------------+--------------------+
       v                    v                    v
 +-----------+        +-----------+        +-------------+
 | Morning   |        | Social    |        | Agent       |
 | Brief     |        | Drafter   |        | Review      |
 | 7:00 AM   |        | 7:30 AM   |        | Fri 3 PM    |
 +-----------+        +-----------+        +-------------+
       v
 +-----------+        +-----------+        +-------------+
 | Midday    |        | Reactive  |        | Weekly Perf |
 | Update    |        | Intel     |        | Feedback    |
 | 1:00 PM   |        | 12:00 PM  |        | Fri 4 PM    |
 +-----------+        +-----------+        +-------------+
                             |
              +--------------+
              v
+-----------------------------+
|  FIREFLIES MCP SERVER       |
|  (Custom TypeScript/GraphQL)|
|  Transcripts + summaries    |
|  + action items. 4 tools.   |
+-----------+-----------------+
            |
            v
+-----------------------------+
|  meeting-to-tasks           |
|  Fireflies -> Notion        |
|  Auto-creates tasks from    |
|  meeting action items       |
+-----------------------------+
```

---

## Autonomous Agents (11 Scheduled Tasks)

All agents run on cron schedules via Claude's scheduled task system. They execute autonomously: no manual trigger, no babysitting. Each agent reads from multiple data sources, synthesizes information, and delivers structured output to Slack or Notion.

### Daily Agents

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Morning Commander** | 6:15 AM daily | Reads Google Calendar, Notion tasks, Gmail action items, and yesterday's Fireflies meeting transcripts. Automatically creates Notion tasks from any meeting action items assigned to Jake. Delivers: today's top 5 priorities, meetings, specific workout (phase-aware from 12-week plan), overdue items, evening plan. |
| **Morning Brief** | 7:00 AM daily | Scans overnight AI/model/benchmark news (strict 24-hour filter). Checks Slack for action items. Pulls Ahrefs SEO data. Saves a structured context file that the Social Drafter reads 25 minutes later to produce chained content. |
| **Social Drafter** | 7:30 AM daily | Reads morning brief context and reactive intel from the day before. Scouts Stratix evaluations. Creates branded data visualizations. Drafts Twitter/X and LinkedIn posts. Runs every draft through the Copy Reviewer skill. Delivers a ready-to-publish package. |
| **Midday Update** | 1:00 PM daily | Scans Gmail for morning emails requiring action. Checks Slack for unresolved threads. Pulls this morning's Fireflies meetings to surface action items from meetings Jake just came out of. Lists afternoon calendar. Push-based: surfaces only what needs attention in the next 4 hours. |
| **Reactive Intel Monitor** | 12:00 PM daily | Scans for breaking AI model launches, benchmark results, competitor moves, and trending evaluation discussions. Drafts reactive content if something is worth responding to. Saves context file for the Social Drafter. DMs Jake only if something is actually worth acting on. |

### Weekly Agents

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Weekly Performance Feedback** | Friday 4:00 PM | Primary data source: GA4 MCP (real Google Analytics). Pulls week-over-week site metrics, top pages, traffic sources, daily trends. Also reads this week's Fireflies meetings to surface sales signals or Archie/Marc feedback on marketing performance. Produces the performance brief that feeds Sunday's Weekly Architect. |
| **Agent Review** | Friday 3:00 PM | Audits all skills, scheduled tasks, and MCP connectors. Checks Fireflies MCP health: verifies it is live and all 6 tasks that depend on it are pulling data. Flags if the Fireflies bot stopped being admitted to meetings. Rates each component A through F. |
| **John Q Batch** | Sunday 6:00 PM | Generates 3-5 satirical LinkedIn posts for a parody character account. John Q is a fictional "Chief AI Transformation Evangelist" who posts aggressive AI-slop content with complete sincerity, but every post has a genuinely sharp insight buried inside. |
| **Weekly Architect** | Sunday 7:00 PM | Reads GA4-backed performance brief, content log, and experiment tracker. Pulls this week's Fireflies transcripts and automatically creates Notion tasks for any commitments Jake made to Archie or Raj. Builds next week's day-by-day priority map with every priority tied to a data point or a meeting commitment. |

### Monthly Agent

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Monthly Strategist** | 1st of month, 8:00 AM | Full month review using GA4 MCP data. Pulls 30 days of Fireflies transcripts to surface strategic decisions, product updates from Marc, sales signals from Raj, and customer discovery insights. Month-over-month comparison table. Next month's priorities each tied to a data point or meeting intel. |

### On-Demand Agent

| Agent | Trigger | What It Does |
|-------|---------|-------------|
| **Meeting to Tasks** | Called by Morning Commander and Weekly Architect, or manually | Pulls Fireflies transcripts for a specified date range. Extracts action items assigned to Jake. Creates real Notion tasks (Status: Inbox) for each one. Reports back to Slack with a list of tasks created. Ensures meeting commitments land in Notion, not just in a Slack brief that gets buried. |

---

## Custom Skills (5 Built)

Skills are reusable prompt-and-tool bundles that execute specific workflows. Each was iterated through eval cycles to reach production quality.

### Copy Reviewer

**What:** 12-rule content review engine that checks any marketing content against brand voice guidelines.

**Rules enforced:** banned phrase detection (47 phrases), AI slop scoring, em dash ban (zero tolerance), "so what" test (every post needs narrative context), product showcase verification, CTA check, platform-specific formatting, ICP coverage, differentiation test, tone calibration, language preferences, outdated model reference detection.

**Eval results:** Iterated through 3 versions. v1: 88% pass rate on test corpus. v2: 96%. v3: 100%.

**Integration:** Runs automatically inside the Social Drafter agent. Every draft gets reviewed before it reaches me.

### Competitive Intelligence Scanner

**What:** Weekly competitive research across 5 primary competitors using web search and Ahrefs MCP tools.

**Process:** Pulls latest news, product announcements, hiring signals, content strategy changes, and domain metrics for each competitor. Compares against a stored baseline from the previous scan. Surfaces what actually changed.

**Output:** 1-page structured brief designed to be reviewed in under 5 minutes.

### Data Visualization Generator

**What:** Branded chart/graph creation skill that enforces visual identity standards.

**Capabilities:** Bar charts, line charts, scatter plots, comparison graphics, social cards. Every output gets: brand colors (specific hex values), official logo placement (bottom-right, auto-detects light/dark background), footer text, automatic overlap detection, date stripping (brand rule: no dates on graphics).

### Logo Compositing

**What:** Adds official brand logo watermark to any image.

**How:** Bundles exact SVG logo assets (color and white variants). Auto-detects image brightness at the placement region to select the correct variant. Never recreates or approximates the logo; always composites the official asset.

### Meeting to Tasks

**What:** Converts Fireflies meeting summaries into Notion tasks automatically.

**Process:** Parses action items from meeting summaries, identifies items assigned to Jake, creates Notion tasks with Status: Inbox so they surface in the daily task review. Called automatically by Morning Commander (daily) and Weekly Architect (weekly). Can also be triggered manually for any date range.

**Why this matters:** Before this, meeting action items either lived in a Fireflies summary no one checked or got mentioned in a Slack brief that got buried. Now every meeting commitment lands in the Notion task queue automatically.

---

## Fireflies MCP Server (Custom Build)

**Language:** TypeScript (MCP SDK)

Fireflies does not expose a REST API at accessible pricing tiers. This server wraps the Fireflies GraphQL API and exposes 4 tools to Claude:

| Tool | What It Does |
|------|-------------|
| `fireflies_list_meetings` | List meetings with optional date range filtering |
| `fireflies_get_transcript` | Full transcript with sentences and AI summary by meeting ID |
| `fireflies_get_recent_transcripts` | Primary scheduled task tool: pull N days of meetings with summaries and action items |
| `fireflies_search_transcripts` | Keyword search across all transcript sentence text |

**Integration:** Registered in Claude Desktop's MCP config. Available to all sessions and all 11 scheduled tasks automatically after restart.

**Which agents use it:** Morning Commander, Midday Update, Weekly Architect, Weekly Performance Feedback, Monthly Strategist, Agent Review (health check), Meeting to Tasks.

**Why Fireflies over tl;dv:** tl;dv requires a Business plan for API access. Fireflies offers GraphQL API access at significantly lower cost with equivalent data (transcripts, summaries, action items, speaker diarization).

---

## Standalone Agent: Story Scout

**Repo:** [story-scout](https://github.com/jakemeany523/story-scout) (private, available on request)

An autonomous Twitter monitoring agent built in Python. Runs 24/7, classifies AI stories by relevance and urgency, drafts social content for high-value stories, and delivers to Telegram.

### Cost Optimization Story

The first version cost **$110/day** in API calls. Through systematic optimization:

1. Added keyword pre-filter (free regex check before any API call)
2. Combined classification and tiering into a single API call (was 2 separate calls)
3. Reduced `max_tokens` from 256 to 16 for classification (only need HOT/WARM/SKIP)
4. Only run expensive drafting pipeline for HOT stories
5. WARM stories logged to DB, not processed further

**Result: Under $10/week.** 91% cost reduction while maintaining classification quality.

---

## Design Principles

The system is built ADHD-first. Every design decision addresses a specific friction point:

1. **One inbox, not six.** Every task from every source, including meeting action items from Fireflies, enters one Notion database. Views slice it by context.
2. **The system comes to you.** Agents push to Slack. You don't go to a dashboard.
3. **Priority-driven, not theme-driven.** No rigid theme days. The Morning Commander selects daily priorities based on deadlines, energy, and available time.
4. **Friction-free capture.** 10 seconds max to add anything. Categorize later.
5. **Built-in recovery.** Agents run whether you use the system or not. Miss a day, a week, a month: the system resets you.
6. **Guardrails, not willpower.** Time-boxed blocks, structured comms windows, research timers.
7. **Energy-aware scheduling.** Deep work mapped to medication peak hours. Lighter work after lunch. Evenings are structured recovery.
8. **Meeting intel feeds the system.** Fireflies recordings feed every planning layer: daily priorities, weekly plans, monthly strategy. Commitments become tasks automatically.

---

## Feedback Loops

The system is self-improving through three feedback cycles:

**Weekly (Sunday):** The Weekly Architect tracks completion rates, dropped categories, time accuracy, overflow patterns, and personal goals. Every priority in the week plan is tied to either a GA4 data point or a specific meeting commitment from Fireflies.

**Monthly (1st):** The Monthly Strategist reviews 4-week trends: system adherence score (0-10), top wins, top friction points, recommended adjustments, and skill track progress. Fireflies data from the full month surfaces sales signals and leadership feedback that otherwise gets buried.

**Quarterly:** The Monthly Strategist triggers a deeper audit: Is the Notion structure still working? Are recurring tasks still relevant? Have agents become noise instead of signal? Agents suggest changes; they don't make them automatically.

---

## Tech Stack

| Component | Technology | Cost |
|-----------|-----------|------|
| Agent orchestration | Claude (Anthropic) via Cowork scheduled tasks | Included in Claude subscription |
| Standalone agents | Python + Claude API (Sonnet) | ~$10/week for Story Scout |
| Task management | Notion (Master Tasks, Projects, Marketing Calendar, Follow-Ups) | Free tier |
| Delivery | Slack (all agent output to DM or channel) | Existing |
| SEO/Competitive data | Ahrefs via MCP connector | Existing subscription |
| Analytics | Google Analytics 4 via custom GA4 MCP server | Free |
| Meeting recordings | Fireflies via custom TypeScript MCP server | Pro plan |
| Calendar | Google Calendar (time-blocking, meeting awareness) | Existing |
| Monitoring | Twitter API via Story Scout | API costs above |
| Messaging | Telegram Bot API (Story Scout delivery) | Free |

---

## What's Next

- **Approval queue execution:** Currently the Morning Brief surfaces items and I manually draft. Closing the loop so "post 1, 3" triggers drafting, review, and scheduling automatically.
- **Buffer scheduling integration:** Connect the Social Drafter output directly to Buffer so approved posts get queued without manual copy-paste.
- **Fireflies MCP open source:** The custom Fireflies GraphQL MCP server may be worth releasing as a standalone repo. Basic wrapper but saves anyone building on Fireflies significant setup time.

---

## About

I'm Jake Meany, a solo marketer at an AI startup. I built this system because the alternative was burning out trying to do 5 people's jobs manually.

The thesis: if you understand what the work actually is (the specific steps, rules, and judgment calls), you can teach AI to do the repetitive parts and focus your human hours on the parts that actually need a human.

This isn't a framework or a template. It's a working system that runs every day. The agents file their reports whether I'm paying attention or not. That's the point.

**Tools used to build this:** Claude Code, Claude Cowork, Python, TypeScript, MCP (Model Context Protocol), Ahrefs API, Fireflies GraphQL API, Twitter API, Telegram Bot API, Notion, Slack, Google Calendar, Google Analytics 4.

---

## Repository Structure

```
jake-os/
  README.md                   # This file
  architecture/
    system-overview.md        # Full system design document
    agent-specs/              # Individual agent specifications
      morning-commander.md
      morning-brief.md
      social-drafter.md
      midday-update.md
      reactive-intel-monitor.md
      weekly-performance-feedback.md
      weekly-architect.md
      monthly-strategist.md
      agent-review.md
      john-q-batch.md
      meeting-to-tasks.md
  skills/
    copy-reviewer/
      README.md               # Skill overview + eval results
      rules.md                # The 12 review rules (sanitized)
    ci-scanner/
      README.md               # Skill overview
      framework.md            # Scan framework (sanitized)
    data-viz/
      README.md               # Skill overview + brand system
    logo-compositing/
      README.md               # Skill overview
    meeting-to-tasks/
      README.md               # Fireflies to Notion pipeline
  story-scout/
    README.md                 # Points to separate repo
  docs/
    cost-optimization.md      # Story Scout cost reduction case study
    design-principles.md      # ADHD-first design philosophy
    feedback-loops.md         # Self-improving system design
    fireflies-mcp.md          # Custom MCP server architecture
```

> Note: Proprietary company data, API keys, and brand-specific content have been removed. This repo documents the architecture, design decisions, and frameworks. Implementation details are available on request.
