# Jake-OS: AI Operating System for a Solo Marketing Department

A complete AI-augmented operating system built by one marketer to run an entire marketing function. 11 autonomous agents, 16 custom skills, a persistent memory system, a standalone monitoring agent, a custom Fireflies MCP server, and a self-correcting feedback architecture, all orchestrated through Claude, Slack, Notion, Google Calendar, Ahrefs, Pipedrive, and Fireflies.

**Built with:** Claude (Anthropic), Claude Code, Cowork, Python, TypeScript, MCP (Model Context Protocol)

---

## The Problem

Solo marketer at an AI startup. Content, social, SEO, AEO (Answer Engine Optimization), competitive intel, influencer partnerships, CRM, and brand. The workload is designed for a team of 4-5 people. Instead of hiring, I built an AI operating system that handles the repetitive, high-volume work so I can focus on strategy and creative.

**Before Jake-OS:** Tasks dying at every tool boundary. Meeting action items evaporating. Follow-ups vanishing across Slack, email, Telegram, and phone. No single system.

**After Jake-OS:** 11 agents running daily/weekly/monthly on autopilot. Content reviewed automatically against brand guidelines. Competitive intel surfaced weekly without manual research. Morning briefs delivered to Slack before I sit down. Meeting action items automatically converted to Notion tasks. CRM updated from meeting transcripts. The system comes to me; I don't go to it.

---

## System Architecture

```
+------------------------------------------------------------------+
|                         NOTION (Hub)                              |
|  +----------+ +--------+ +-----------+ +----------+              |
|  | Master   | |Projects| | Marketing | | Follow   |              |
|  | Tasks DB | |DB      | | Calendar  | | Ups DB   |              |
|  +----+-----+ +---+----+ +-----+-----+ +----+-----+              |
|       +------+-----+----------+-------------+                     |
|  +------------------------------------------+                     |
|  |         DAILY DASHBOARD PAGE             |                     |
|  | Today | Inbox | Week | Overdue           |                     |
|  | Waiting On | Skill Tracks               |                     |
|  +------------------------------------------+                     |
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
              +--------------+--------------+
              v                             v
+-----------------------------+  +-----------------------------+
|  FIREFLIES MCP SERVER       |  |  PIPEDRIVE CRM MCP          |
|  (Custom TypeScript/GraphQL)|  |  Deals, contacts, orgs,     |
|  Transcripts + summaries    |  |  activities, notes.          |
|  + action items. 4 tools.   |  |  Full read/write access.     |
+-----------+-----------------+  +-----------------------------+
            |
            v
+-----------------------------+
|  MEMORY SYSTEM              |
|  Persistent context across  |
|  sessions. 50+ files in 8   |
|  categories. Self-updating. |
+-----------------------------+
```

---

## Autonomous Agents (11 Scheduled Tasks)

All agents run on cron schedules via Claude's scheduled task system. They execute autonomously: no manual trigger, no babysitting. Each agent reads from multiple data sources, synthesizes information, and delivers structured output to Slack or Notion.

### Daily Agents

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Morning Commander** | 6:15 AM daily | Reads Google Calendar, Notion tasks, Gmail action items, and yesterday's Fireflies meeting transcripts. Automatically creates Notion tasks from any meeting action items. Delivers: today's top 5 priorities, meetings, overdue items, evening plan. |
| **Morning Brief** | 7:00 AM daily | Scans overnight AI/model/benchmark news (strict 24-hour filter). Checks Slack for action items. Pulls Ahrefs SEO data. Saves a structured context file that the Social Drafter reads 25 minutes later to produce chained content. |
| **Social Drafter** | 7:30 AM daily | Reads morning brief context and reactive intel from the day before. Scouts Stratix evaluations. Creates branded data visualizations. Drafts Twitter/X and LinkedIn posts. Runs every draft through the Copy Reviewer skill. Delivers a ready-to-publish package. |
| **Midday Update** | 1:00 PM daily | Scans Gmail for morning emails requiring action. Checks Slack for unresolved threads. Pulls morning Fireflies meetings to surface action items. Lists afternoon calendar. Push-based: surfaces only what needs attention in the next 4 hours. |
| **Reactive Intel Monitor** | 12:00 PM daily | Scans for breaking AI model launches, benchmark results, competitor moves, and trending evaluation discussions. Drafts reactive content if something is worth responding to. Saves context file for the Social Drafter. |

### Weekly Agents

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Weekly Performance Feedback** | Friday 4:00 PM | Primary data source: GA4 MCP (real Google Analytics). Pulls week-over-week site metrics, top pages, traffic sources, daily trends. Also reads Fireflies meetings to surface sales signals or leadership feedback. Produces the performance brief that feeds Sunday's Weekly Architect. |
| **Agent Review** | Friday 3:00 PM | Audits all skills, scheduled tasks, and MCP connectors. Checks Fireflies MCP health: verifies it is live and all 6 tasks that depend on it are pulling data. Rates each component A through F. |
| **John Q Batch** | Sunday 6:00 PM | Generates 3-5 satirical LinkedIn posts for a parody character account. John Q is a fictional "Chief AI Transformation Evangelist" who posts aggressive AI-slop content with complete sincerity, but every post has a genuinely sharp insight buried inside. |
| **Weekly Architect** | Sunday 7:00 PM | Reads GA4-backed performance brief, content log, and experiment tracker. Pulls this week's Fireflies transcripts and automatically creates Notion tasks for any commitments made. Builds next week's day-by-day priority map with every priority tied to a data point or a meeting commitment. |

### Monthly Agent

| Agent | Schedule | What It Does |
|-------|----------|-------------|
| **Monthly Strategist** | 1st of month, 8:00 AM | Full month review using GA4 MCP data. Pulls 30 days of Fireflies transcripts to surface strategic decisions, product updates, sales signals, and customer discovery insights. Month-over-month comparison table. Next month's priorities each tied to a data point or meeting intel. |

### On-Demand Agent

| Agent | Trigger | What It Does |
|-------|---------|-------------|
| **Meeting to Tasks** | Called by Morning Commander and Weekly Architect, or manually | Pulls Fireflies transcripts for a specified date range. Extracts action items. Creates real Notion tasks (Status: Inbox) for each one. Ensures meeting commitments land in Notion, not just in a Slack brief. |

---

## Custom Skills (16 Built)

Skills are reusable prompt-and-tool bundles that execute specific workflows. Each was iterated through eval cycles.

### Content Creation & Distribution

| Skill | What It Does |
|-------|-------------|
| **Social Content Drafter** | Drafts publish-ready social content for Twitter/X and LinkedIn with copy-reviewer rules baked into generation, live Stratix data integration, branded graphics, and narrative alignment. The core content creation skill. |
| **Blog Writer Pipeline** | End-to-end article production. Takes a target keyword and chains Ahrefs MCP (keyword + SERP research), Copy Reviewer (brand voice enforcement), and graphics generation into a single autonomous workflow with one approval gate at the outline stage. |
| **Blog Production Pipeline** | Full blog workflow from research through SEO/AEO optimization, copy review, and CMS insertion via Framer. Bridges research, writing, quality control, and publishing. |
| **LinkedIn Education Drafter** | LinkedIn-specific educational content for enterprise buyers and tech leaders. Frameworks, insights, and decision-making narratives rather than benchmark charts. |
| **Content Repurposer** | Converts one content asset into multi-platform distribution packages: Twitter threads, LinkedIn posts, newsletter excerpts, social snippets. Each platform gets native content, not copy-pasted reformats. |
| **Benchmark Drop** | Automates benchmark-drop workflow: pulls Stratix evaluation data, identifies SOTA results and regressions, generates publish-ready social copy and branded PNG comparison charts. |

### Quality & Brand

| Skill | What It Does |
|-------|-------------|
| **Copy Reviewer** | 12-rule content review engine. Checks any marketing content against brand voice guidelines: 47 banned phrases, AI slop scoring, em dash ban, "so what" test, product showcase verification, CTA check, platform-specific formatting, ICP coverage, differentiation test, tone calibration, outdated model detection. Iterated through 3 versions to 100% eval pass rate. |
| **Strategic Drift Detector** | Detects semantic drift when skills, scheduled tasks, and content files fall out of sync with source-of-truth memory context files. Catches stale differentiators, outdated model counts, misaligned competitive framing, and product positioning changes. |

### Intelligence & Research

| Skill | What It Does |
|-------|-------------|
| **Competitive Intel Scanner** | Weekly competitive research across 7 competitors using web search and Ahrefs MCP. Compares against a stored baseline from the previous scan. Surfaces what actually changed. Output: 1-page brief designed for 5-minute review. |
| **Viral Content Scout** | Monitors competitor Twitter accounts, AI thought leaders, and trending evaluation content. Identifies engagement opportunities: high-signal moments to quote-tweet, reply to, or riff on with original angles. |
| **Performance Analytics** | On-demand marketing analysis pulling from GA4, Ahrefs, Slack, web search, and content logs. Produces actionable insights about content effectiveness, traffic, SEO rankings, and channel ROI. |

### CRM & Meeting Automation

| Skill | What It Does |
|-------|-------------|
| **Meeting Prep Generator** | Auto-generates meeting prep briefs by pulling CRM data (Pipedrive), email history, Fireflies transcripts, and calendar context. Outputs a 2-minute actionable brief with attendee context, deal status, last interactions, and talking points. |
| **Post-Meeting Processor** | Processes completed meetings: pulls Fireflies transcripts, generates follow-up emails, CRM activity logs, Notion tasks, and deal stage updates. Automates post-meeting admin into a single approval step. |

### Operations & Tracking

| Skill | What It Does |
|-------|-------------|
| **Influencer Blitz Tracker** | Tracks influencer campaign across outreach status, creator responses, deliverables, spend, and ROI metrics. Maintains a persistent tracker with status for each creator and partner. |
| **Phase Tracker** | Checks progress against the 90-Day Plan, tracking phase completion, milestone status, and weekly focus alignment. Identifies what's done, behind schedule, or needs attention. |
| **Shareable Report Formatter** | Transforms raw report output into polished, shareable documents (PDF, slides, formatted docs) suitable for leadership or external stakeholder distribution. |

---

## Memory System (Persistent Context)

Jake-OS includes a persistent memory architecture that gives every session and agent access to accumulated context. The system maintains 50+ files across 8 categories, enabling session continuity and institutional knowledge retention.

### Memory Architecture

```
memory/
  sessions/              # Per-session notes with structured summaries
    index.md             # Session history index (read at startup)
  reference/             # Stable reference material
    brand-voice.md       # Voice guidelines for all content
    terms.md             # Terminology, acronyms, definitions
    quick-ref.md         # Benchmark names, model lists, preferences
    active-projects.md   # Current initiatives and timelines
    stratix-sdk.md       # SDK methods and fields
    people.md            # Team roles and relationships
  context/               # Domain context that evolves
    competitors.md       # Competitive positioning and battlecards
    ai-landscape.md      # Current model info and comparisons
    company.md           # Product details, pricing, ICPs
    marketing-strategy.md # Strategy, budget, phases
  evolving/              # Rapidly changing state
    decisions-and-context.md  # Active decisions, product state
    content-pipeline-status.md # What's blocked/unblocked
  competitive-intel/     # CI scan baselines and history
  projects/              # Project-specific context
  rlhf/                  # Skill feedback and improvement data
  archive/               # Retired guidelines and old context
```

### Session Continuity

Every session starts by reading the session index. If the current task needs prior context, it loads the relevant session notes. A catchup check compares recent Cowork sessions against saved notes and recovers any unsaved sessions automatically.

This means context doesn't die between sessions. Strategic decisions, content preferences, meeting commitments, and competitive intel persist and compound.

### Learning Memory

A structured JSON store that captures preferences, content insights, copy patterns, and strategic decisions over time. Every content-producing skill reads learning memory at startup, so the system gets better the more it's used.

---

## CLAUDE.md (Operating Instructions)

The system is governed by a `CLAUDE.md` file that acts as the operating manual for every session. It defines:

- **Standing permissions:** What tools and integrations the system can use autonomously vs. what requires confirmation
- **Hard rules:** Universal constraints (formatting rules, delivery paths, experiment cadence)
- **Session startup protocol:** What to read and check at the beginning of every session
- **Reference file routing:** Which memory files to read for which types of tasks
- **Integration access:** How to connect to Stratix, Pipedrive, and other tools

A sanitized version is included in this repo at [`CLAUDE.md`](CLAUDE.md).

---

## Fireflies MCP Server (Custom Build)

**Language:** TypeScript (MCP SDK)

Wraps the Fireflies GraphQL API and exposes 4 tools to Claude:

| Tool | What It Does |
|------|-------------|
| `fireflies_list_meetings` | List meetings with optional date range filtering |
| `fireflies_get_transcript` | Full transcript with sentences and AI summary by meeting ID |
| `fireflies_get_recent_transcripts` | Pull N days of meetings with summaries and action items |
| `fireflies_search_transcripts` | Keyword search across all transcript sentence text |

**Which agents use it:** Morning Commander, Midday Update, Weekly Architect, Weekly Performance Feedback, Monthly Strategist, Agent Review (health check), Meeting to Tasks.

---

## Standalone Agent: Story Scout

**Repo:** [story-scout](https://github.com/jakemeany523/story-scout) (private, available on request)

An autonomous Twitter monitoring agent built in Python. Runs 24/7, classifies AI stories by relevance and urgency, drafts social content for high-value stories, and delivers to Telegram.

### Cost Optimization

The first version cost **$110/day** in API calls. Through systematic optimization (keyword pre-filter, combined classification calls, reduced token limits, tiered processing), brought it down to **under $10/week**. 91% cost reduction while maintaining classification quality.

---

## Design Principles

1. **One inbox, not six.** Every task from every source, including meeting action items from Fireflies, enters one Notion database. Views slice it by context.
2. **The system comes to you.** Agents push to Slack. You don't go to a dashboard.
3. **Priority-driven, not theme-driven.** No rigid theme days. The Morning Commander selects daily priorities based on deadlines, energy, and available time.
4. **Friction-free capture.** 10 seconds max to add anything. Categorize later.
5. **Built-in recovery.** Agents run whether you use the system or not. Miss a day, a week, a month: the system resets you.
6. **Self-correcting.** The Strategic Drift Detector catches when skills and content fall out of sync with source-of-truth context files. The system notices its own inconsistencies.
7. **Meeting intel feeds the system.** Fireflies recordings feed every planning layer: daily priorities, weekly plans, monthly strategy. Commitments become tasks automatically.
8. **Context compounds.** The memory system means every session builds on the last. Preferences, decisions, and competitive intel persist and improve over time.

---

## Feedback Loops

The system is self-improving through three feedback cycles:

**Weekly (Sunday):** The Weekly Architect tracks completion rates, dropped categories, time accuracy, overflow patterns, and personal goals. Every priority in the week plan is tied to either a GA4 data point or a specific meeting commitment from Fireflies.

**Monthly (1st):** The Monthly Strategist reviews 4-week trends: system adherence score (0-10), top wins, top friction points, recommended adjustments. Fireflies data from the full month surfaces sales signals and leadership feedback.

**Quarterly:** Deeper audit: Is the Notion structure still working? Are recurring tasks still relevant? Have agents become noise instead of signal? Agents suggest changes; they don't make them automatically.

---

## Tech Stack

| Component | Technology | Cost |
|-----------|-----------|------|
| Agent orchestration | Claude (Anthropic) via Cowork scheduled tasks | Included in Claude subscription |
| Standalone agents | Python + Claude API (Sonnet) | ~$10/week for Story Scout |
| Task management | Notion (Master Tasks, Projects, Marketing Calendar, Follow-Ups) | Free tier |
| Delivery | Slack (all agent output to DM) | Existing |
| CRM | Pipedrive via MCP connector | Existing subscription |
| SEO/Competitive data | Ahrefs via MCP connector | Existing subscription |
| Analytics | Google Analytics 4 via custom GA4 MCP server | Free |
| Meeting recordings | Fireflies via custom TypeScript MCP server | Pro plan |
| Calendar | Google Calendar (time-blocking, meeting awareness) | Existing |
| Monitoring | Twitter API via Story Scout | API costs above |
| Messaging | Telegram Bot API (Story Scout delivery) | Free |
| Memory | File-based persistent context (50+ files, 8 categories) | Free |

---

## What's Changed Since v1

The initial version (March 2026) had 7 agents and 4 skills. Since then:

- **Agents:** 7 to 11 (added Reactive Intel Monitor, John Q Batch, Midday Update, Meeting to Tasks)
- **Skills:** 4 to 16 (added Social Content Drafter, Blog Writer Pipeline, Blog Production Pipeline, LinkedIn Education Drafter, Content Repurposer, Benchmark Drop, Strategic Drift Detector, Viral Content Scout, Performance Analytics, Meeting Prep Generator, Post-Meeting Processor, Influencer Blitz Tracker, Phase Tracker, Shareable Report Formatter)
- **Memory system:** Built from scratch. 50+ persistent files across 8 categories. Session continuity. Learning memory that compounds.
- **CRM integration:** Added Pipedrive MCP for deal tracking, meeting prep, and post-meeting processing
- **Self-correction:** Strategic Drift Detector catches when the system falls out of sync with itself
- **Copy Reviewer:** Iterated through 3 versions with structured eval cycles (88% to 96% to 100% pass rate)
- **CLAUDE.md:** Formalized operating instructions with standing permissions, hard rules, and reference file routing

---

## Repository Structure

```
jake-os/
  README.md                   # This file
  CLAUDE.md                   # Operating instructions (sanitized)
  architecture/
    system-overview.md        # Full system design document
    agent-specs/              # Individual agent specifications
  skills/
    copy-reviewer/            # Brand voice review engine (12 rules, 47 banned phrases)
    ci-scanner/               # Weekly competitive intelligence
    data-viz/                 # Branded chart/graph generation
    logo-compositing/         # Brand logo watermarking
    social-content-drafter/   # Core social content creation
    blog-writer-pipeline/     # End-to-end article production
    blog-production-pipeline/ # Full blog workflow with CMS
    linkedin-education-drafter/ # LinkedIn enterprise content
    content-repurposer/       # Multi-platform content adaptation
    benchmark-drop/           # Benchmark release content workflow
    strategic-drift-detector/ # Self-correction system
    viral-content-scout/      # Engagement opportunity monitoring
    performance-analytics/    # Marketing performance analysis
    meeting-prep-generator/   # CRM-powered meeting briefs
    post-meeting-processor/   # Meeting follow-up automation
    influencer-blitz-tracker/ # Campaign tracking
    phase-tracker/            # 90-day plan progress
    shareable-report-formatter/ # Report formatting for stakeholders
  memory/
    README.md                 # Memory system architecture
  docs/
    cost-optimization.md      # Story Scout cost reduction case study
    design-principles.md      # Design philosophy
    feedback-loops.md         # Self-improving system design
    session-continuity.md     # How context persists across sessions
  story-scout/
    README.md                 # Points to separate repo
```

> Note: Proprietary company data, API keys, and brand-specific content have been removed. This repo documents the architecture, design decisions, and frameworks. Implementation details are available on request.

---

## About

I'm Jake Meany, a solo marketer at an AI startup. I built this system because the alternative was trying to do 5 people's jobs manually.

The thesis: if you understand what the work actually is (the specific steps, rules, and judgment calls), you can teach AI to do the repetitive parts and focus your human hours on the parts that actually need a human.

This isn't a framework or a template. It's a working system that runs every day. The agents file their reports whether I'm paying attention or not. That's the point.

**Tools used to build this:** Claude Code, Claude Cowork, Python, TypeScript, MCP (Model Context Protocol), Ahrefs API, Fireflies GraphQL API, Twitter API, Telegram Bot API, Pipedrive, Notion, Slack, Google Calendar, Google Analytics 4.
