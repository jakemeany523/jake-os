# Jake-OS: AI Operating System for a Solo Marketing Department

A complete AI-augmented operating system built by one marketer to run an entire marketing function. 7 autonomous agents, 5 custom skills, 1 standalone monitoring agent, all orchestrated through Claude, Slack, Notion, and Ahrefs.

**Built with:** Claude (Anthropic), Claude Code, Cowork, Python, MCP (Model Context Protocol)

---

## The Problem

I'm a solo marketer at an AI startup. I run content, social, SEO, AEO (Answer Engine Optimization), competitive intel, influencer partnerships, and brand. The workload is designed for a team of 4-5 people. Instead of hiring, I built an AI operating system that handles the repetitive, high-volume work so I can focus on strategy and creative.

**Before Jake-OS:** 15 pain points. Tasks dying at every tool boundary. Meeting action items evaporating. 25-30 hours/week lost to unstructured evenings. Follow-ups vanishing across Slack, email, Telegram, and phone. No single system.

**After Jake-OS:** 7 agents running daily/weekly/monthly on autopilot. Content reviewed automatically against brand guidelines. Competitive intel surfaced weekly without manual research. Morning briefs delivered to Slack before I sit down. The system comes to me; I don't go to it.

---

## System Architecture

```
+------------------------------------------------------------------+
|                        NOTION (Hub)                               |
|  +----------+ +--------+ +-----------+ +----------+              |
|  | Master   | |Projects| | Marketing | | Follow   |              |
|  | Tasks DB | |DB      | | Calendar  | | Ups DB   |              |
|  +----+-----+ +---+----+ +-----+-----+ +----+-----+             |
|       +------+-----+----------+-------------+                    |
|       +------------------------------------------+               |
|       |          DAILY DASHBOARD PAGE            |               |
|       | Today | Inbox | Week | Overdue           |               |
|       | Waiting On | Skill Tracks                |               |
|       +------------------------------------------+               |
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
                            |
                            v
                  +-------------------+
                  |   SLACK (#jake-os)|
                  +--------+----------+
                           |
          +----------------+----------------+
          v                v                v
   +----------+     +----------+     +----------+
   |Google Cal|     | Ahrefs   |     | Buffer   |
   |Time block|     | SEO/CI   |     | Content  |
   |+ personal|     | data     |     | schedule |
   +----------+     +----------+     +----------+
```

---

## Autonomous Agents (7 Scheduled) + 1 Manual Pipeline

All scheduled agents run on cron schedules via Claude's scheduled task system. They execute autonomously: no manual trigger, no babysitting. Each agent reads from multiple data sources, synthesizes information, and delivers structured output to Slack. The Audience Intelligence pipeline runs manually every Monday (10 min).

### Daily Agents

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Morning Commander** | 6:15 AM daily | Reads Google Calendar, Notion tasks, follow-ups, fitness plan. Delivers: today's top 5 priorities, meetings with prep notes, specific workout (phase-aware from 12-week plan), overdue items, evening plan. The "executive assistant" agent. |
| **Morning Brief** | 7:00 AM daily | The chief-of-staff. Scans overnight AI/model/benchmark news (web search + GitHub trending + Twitter signals). Checks all Slack channels for action items. Pulls Ahrefs competitor metrics and SEO data. Surfaces new product evaluations. Outputs an approval queue: numbered items tagged POST/MONITOR/IGNORE. I reply "post 1, 3" and drafts get created. |
| **Social Drafter** | 7:30 AM daily | Requires Chrome extension for live data. Reads the Morning Brief output (7:00 AM) as primary editorial input. Checks @LayerLens X and LinkedIn feeds to avoid repeats. Scouts Stratix (app.layerlens.ai) for new evaluations and LL Marketing workspace for new tools/data. Cross-references the Bleeding-Edge Benchmark Reference Guide. Creates branded graphics via the Data Viz + Logo skills. Drafts Twitter/X and LinkedIn posts. Runs every draft through the Copy Reviewer automatically. Sends Slack DM if Chrome is disconnected; waits up to 30 minutes, then skips. Falls back to evergreen Stratix Premium content when nothing new is available. |

### Weekly Agents

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Agent Review** | Friday 3:00 PM | Audits all skills, scheduled tasks, and MCP connectors. Checks trigger descriptions, identifies redundancies, suggests new skills to build. Rates each component A through F. Produces actionable improvement list. The system reviewing itself. |
| **John Q Batch** | Sunday 6:00 PM | Generates 3-5 satirical LinkedIn posts for a parody character account. Matches specific voice, topics, and formatting rules. (Yes, I automated my shitposting.) |
| **Weekly Architect** | Sunday 7:00 PM | Reviews past week: completion rate, dropped categories, time accuracy, overflow patterns. Builds next week's day-by-day priority map. Flags pattern drift. Assigns skill development sessions. Pre-drafts Monday content topics. Includes a "Pattern Alert" section that catches behavioral drift I wouldn't notice myself. |

### Monthly Agent

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Monthly Strategist** | 1st of month, 8:00 AM | Full month review: tasks completed, content published, campaigns. Marketing metrics snapshot from Ahrefs. Personal goals review (fitness, habits). Subscription audit reminder. Next month's top 5 priorities. Trend analysis across 4 weeks. The strategic reset. |

### Manual Pipeline: Audience Intelligence

| Pipeline | Cadence | What It Does |
|----------|---------|-------------|
| **Audience Intelligence** | Monday 7:15 AM (10 min) | Runs `mixpanel-weekly-intel.py` to pull last 7 days of site behavior. Identifies high-intent users by behavior score. Exports Twitter Analytics engager list. Imports into Clay for enrichment and ateam persona scoring. Combined score routes contacts: 13+ to Pipedrive (Raj's pipeline), 8-12 to Mailchimp nurture sequence. Updates weekly ICP tracking table. Closes the blindspot between content performance and audience identity. |

---

## Custom Skills (7 Built)

Skills are reusable prompt-and-tool bundles that execute specific workflows. Each was iterated through eval cycles to reach production quality.

### Copy Reviewer
**What:** 12-rule content review engine that checks any marketing content against brand voice guidelines.

**Rules enforced:** banned phrase detection (47 phrases), AI slop scoring, em dash ban (zero tolerance), "so what" test (every post needs narrative context), product showcase verification, CTA check, platform-specific formatting, ICP coverage, differentiation test, tone calibration, language preferences, outdated model reference detection.

**Eval results:** Iterated through 3 versions. v1: 88% pass rate on test corpus. v2: 96%. v3: 100%. The eval used 25 test cases covering edge cases like near-miss banned phrases, borderline tone, and posts that technically follow rules but lack substance.

**Integration:** Runs automatically inside the Social Drafter agent. Every draft gets reviewed before it reaches me.

### Competitive Intelligence Scanner
**What:** Weekly competitive research across 5 primary competitors using web search + Ahrefs MCP tools.

**Process:** Pulls latest news, product announcements, hiring signals, content strategy changes, and domain metrics for each competitor. Compares against a stored baseline from the previous scan. Surfaces what actually changed (not just "here's what they're doing" but "here's what's different from last week").

**Output:** 1-page structured brief designed to be reviewed in under 5 minutes.

### Data Visualization Generator
**What:** Branded chart/graph creation skill that enforces visual identity standards.

**Capabilities:** Bar charts, line charts, scatter plots, comparison graphics, social cards. Every output gets: brand colors (specific hex values), official logo placement (bottom-right, auto-detects light/dark background for logo variant), footer text, automatic overlap detection, date stripping (brand rule: no dates on graphics).

**Eval:** Automated validation pipeline checks overlap detection, logo placement, brand compliance, and layout quality. Shipped with helper functions (`create_chart()`, `save_chart()`, brand color dictionary) for consistent output.

### Logo Compositing
**What:** Adds official brand logo watermark to any image.

**How:** Bundles exact SVG logo assets (color and white variants). Auto-detects image brightness at the logo placement region to select the correct variant. Never recreates or approximates the logo; always composites the official asset.

### Daily Social Drafter (Orchestrator Skill)
**What:** End-to-end social content pipeline that orchestrates the Copy Reviewer, Data Viz, and Logo skills into a single daily workflow.

**Trigger:** Runs as the Social Drafter agent's core skill (7:30 AM daily). Also invocable manually ("draft social," "create posts," "run the daily drafter").

**Pipeline:** Reads Morning Brief output for editorial direction. Checks @LayerLens X and LinkedIn feeds to build a "do not repeat" list. Scouts Stratix (app.layerlens.ai) for new evaluations via Chrome. Cross-references the Bleeding-Edge Benchmark Reference Guide. Drafts Twitter/X (3-4 posts) and LinkedIn (1-2 posts). Creates branded graphics. Runs every draft through the 12-rule Copy Reviewer. Revises until clean. Delivers a ready-to-publish package to `social-drafts/YYYY-MM-DD/`.

**Chrome dependency:** Requires the Claude in Chrome extension for all data gathering. Sends a Slack DM notification if disconnected, waits up to 30 minutes, then skips. No web search fallbacks.

**Skills orchestrated:** Copy Reviewer (Phase 5), Data Visualization Generator (Phase 4), Logo Compositing (Phase 4).

### Mixpanel Intelligence Reporter (Audience Intelligence)
**What:** Python script that pulls Mixpanel Export API data and produces a weekly audience intelligence report. Identifies who is visiting the site, which behaviors signal buying intent, and which contacts are ready for CRM enrichment.

**Run:** Monday mornings, manually. `python3 mixpanel-weekly-intel.py`

**Output:** Markdown report with high-intent user list, sign-up data, intent page visits, UTM attribution (once live), and specific action items (who to push to Clay/Pipedrive this week).

**Integration:** Feeds directly into Clay enrichment workflow. Combined behavior score + Clay tier score determines Pipedrive routing. Full spec: `skills/audience-intelligence/README.md`

### UTM Link Generator (Audience Intelligence)
**What:** Python script that generates properly tagged UTM links for all social posts, newsletters, and influencer content. Enforces consistent parameter values so Mixpanel attribution data is clean.

**Run:** Monday mornings, before loading content into Buffer. `python3 utm-link-generator.py --quick` for the day's standard link set.

**Why it exists:** Without consistent UTM tagging, every layerlens.com link in a tweet looks like "Direct" in Mixpanel. This script eliminates that gap and makes content-to-pipeline attribution possible.

**Rule:** Never post a naked layerlens.com link. Every link gets UTM parameters. Full spec: `skills/utm-generator/README.md`

---

## Standalone Agent: Story Scout

**Repo:** [story-scout](https://github.com/jakemeany523/story-scout) (private, available on request)

An autonomous Twitter monitoring agent built in Python. Runs 24/7, classifies AI stories by relevance and urgency, drafts social content for high-value stories, and delivers to Telegram.

### Pipeline Architecture

```
Twitter API (25 tweets/poll, every 2 hours)
    |
    v
Keyword Pre-Filter (27 keywords, regex, FREE)
    |  Eliminates 85-95% of noise before any API call
    v
Combined Classify + Tier (1 Sonnet call, max_tokens=16)
    |  Returns: HOT / WARM / SKIP
    |
    +-- HOT: Generate angle -> Draft post -> Copy review -> Telegram
    |
    +-- WARM: Log to SQLite (no notification, searchable later)
    |
    +-- SKIP: Discard
```

### Cost Optimization Story

The first version cost **$110/day** in API calls. Through systematic optimization:

1. Added keyword pre-filter (free regex check before any API call)
2. Combined classification + tiering into a single API call (was 2 separate calls)
3. Reduced `max_tokens` from 256 to 16 for classification (only need HOT/WARM/SKIP)
4. Only run expensive drafting pipeline for HOT stories
5. WARM stories logged to DB, not processed further

**Result: Under $10/week.** 91% cost reduction while maintaining classification quality.

---

## Design Principles

The system is built ADHD-first. Every design decision addresses a specific friction point:

1. **One inbox, not six.** Every task from every source enters one Notion database. Views slice it by context.
2. **The system comes to you.** Agents push to Slack. You don't go to a dashboard.
3. **Priority-driven, not theme-driven.** No rigid theme days. The Morning Commander selects daily priorities based on deadlines, energy, and available time.
4. **Friction-free capture.** 10 seconds max to add anything. Categorize later.
5. **Built-in recovery.** Agents run whether you use the system or not. Miss a day, a week, a month: the system resets you.
6. **Guardrails, not willpower.** Time-boxed blocks, structured comms windows, research timers.
7. **Energy-aware scheduling.** Deep work mapped to medication peak hours. Lighter work after lunch. Evenings are structured recovery.
8. **The system learns.** Weekly pattern tracking, monthly trend analysis, quarterly audit. What's consistently skipped gets re-evaluated, not guilt-tripped.

---

## Feedback Loops

The system is self-improving through three feedback cycles:

**Weekly (Sunday):** The Weekly Architect tracks completion rates, dropped categories, time accuracy, overflow patterns, and personal goals. It surfaces a "Pattern Alert" when behavioral drift is detected. Example: "AI Mastery sessions skipped 3 of last 4 weeks. Consider moving to mornings only."

**Monthly (1st):** The Monthly Strategist reviews 4-week trends: system adherence score (0-10), top wins, top friction points, recommended adjustments, and skill track progress.

**Quarterly:** The Monthly Strategist triggers a deeper audit: Is the Notion structure still working? Are recurring tasks still relevant? Have agents become noise instead of signal?

Agents suggest changes; they don't make them automatically. The system stays adaptive without removing human control.

---

## Results

After running for 4+ weeks:

- **Morning clarity:** Know exactly what to do when I sit down. Every day.
- **Content velocity:** Went from ad-hoc posting to a structured batch workflow. 20 Twitter + 5 LinkedIn posts drafted in a Monday morning session.
- **Competitive intel:** No longer manually researching competitors. Weekly brief surfaces changes automatically.
- **Copy quality:** Every piece of content passes a 12-rule brand review before I see it. The AI slop problem is solved.
- **Cost efficiency:** Story Scout runs 24/7 monitoring for under $10/week.
- **Recovery mechanism:** Missed 3 days during a heavy sprint week. The system caught me up in one Sunday evening review. No lost tasks, no forgotten follow-ups.

---

## Tech Stack

| Component | Technology | Cost |
|-----------|-----------|------|
| Agent orchestration | Claude (Anthropic) via Cowork scheduled tasks | Included in Claude subscription |
| Standalone agents | Python + Claude API (Sonnet) | ~$10/week for Story Scout |
| Task management | Notion (Master Tasks, Projects, Marketing Calendar, Follow-Ups) | Free tier |
| Delivery | Slack (all agent output to #jake-os channel) | Existing |
| SEO/Competitive data | Ahrefs via MCP connector | Existing subscription |
| Social scheduling | Buffer | Free tier |
| Calendar | Google Calendar (time-blocking, meeting awareness) | Existing |
| Monitoring | Twitter API via Story Scout | API costs above |
| Messaging | Telegram Bot API (Story Scout delivery) | Free |
| Audience intelligence | Mixpanel Export API + Clay + Pipedrive + Mailchimp | Mixpanel: existing; Clay Starter: $134/mo |
| UTM attribution | Python script (utm-link-generator.py) | Free |

---

## What's Next

- **Audience Intelligence (shipped March 2026):** Mixpanel behavior scoring + Clay enrichment + ateam persona classification + Pipedrive routing. Closes the blindspot between content performance and audience identity.
- **Blog writer pipeline:** Research, write, SEO/AEO check, publish. The full content loop from signal to published article.
- **Approval queue execution:** ~~Currently the Morning Brief surfaces items and I manually draft.~~ Partially closed: Morning Brief output now feeds directly into the Social Drafter as editorial input. Next step: "post 1, 3" triggers drafting, review, and scheduling automatically from Slack.
- **Weekly metrics dashboard:** Ahrefs + Twitter + LinkedIn analytics pulled into a single branded graphic every Monday.
- **UTM attribution closing the loop:** Once Mixpanel `track_utm: true` is set (pending engineering), every social post will be traceable to specific site visits and sign-ups. Content-to-pipeline attribution becomes fully measurable.
- **Bookmark saver:** Twitter/LinkedIn bookmark to summary to searchable archive.

---

## About

I'm Jake Meany, a solo marketer at an AI startup. I built this system because the alternative was burning out trying to do 5 people's jobs manually. The thesis: if you understand what the work actually is (the specific steps, rules, and judgment calls), you can teach AI to do the repetitive parts and focus your human hours on the parts that actually need a human.

This isn't a framework or a template. It's a working system that runs every day. The agents file their reports whether I'm paying attention or not. That's the point.

**Tools used to build this:** Claude Code, Claude Cowork, Python, MCP (Model Context Protocol), Ahrefs API, Twitter API, Telegram Bot API, Notion, Slack, Google Calendar, Buffer.

---

## Repository Structure

```
jake-os/
  README.md              # This file
  architecture/
    system-overview.md    # Full system design document
    agent-specs/          # Individual agent specifications
      morning-commander.md
      morning-brief.md
      social-drafter.md
      weekly-architect.md
      monthly-strategist.md
      agent-review.md
      john-q-batch.md
      audience-intelligence.md  # Audience Intelligence pipeline spec
  skills/
    copy-reviewer/
      README.md           # Skill overview + eval results
      rules.md            # The 12 review rules (sanitized)
    ci-scanner/
      README.md           # Skill overview
      framework.md        # Scan framework (sanitized)
    data-viz/
      README.md           # Skill overview + brand system
    logo-compositing/
      README.md           # Skill overview
    daily-social-drafter/
      SKILL.md            # Full pipeline spec (8 phases)
      references/
        LLM-Agent-Benchmark-Reference-Guide.docx
    audience-intelligence/
      README.md           # Mixpanel weekly intel script overview
    utm-generator/
      README.md           # UTM link generator overview
  story-scout/
    README.md             # Points to separate repo
  docs/
    cost-optimization.md  # Story Scout cost reduction case study
    design-principles.md  # ADHD-first design philosophy
    feedback-loops.md     # Self-improving system design
```

> Note: Proprietary company data, API keys, and brand-specific content have been removed. This repo documents the architecture, design decisions, and frameworks. Implementation details are available on request.
