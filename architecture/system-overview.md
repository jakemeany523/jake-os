# System Overview: Jake-OS

## Core Architecture

Jake-OS is a multi-agent system built on three layers: data ingestion, autonomous processing, and human-in-the-loop delivery.

### Layer 1: Data Ingestion

Agents pull from multiple sources on cron schedules:

- **Web search** (AI news, model releases, benchmark results, competitor activity)
- **GitHub trending** (ML/AI repositories, new tools, framework updates)
- **Twitter/X** (via Story Scout agent, keyword-filtered, classified by urgency)
- **Slack** (all workspace channels scanned for action items, mentions, blockers)
- **Ahrefs** (domain rating, organic keyword movements, competitor backlink changes)
- **Google Calendar** (today's meetings, available deep work blocks, conflicts)
- **Notion** (tasks, projects, follow-ups, campaign status)
- **Product app** (new evaluations, benchmark results, user activity)

### Layer 2: Autonomous Processing

Each agent applies domain-specific logic:

- **Classification:** Story Scout uses a keyword pre-filter (free) then a single LLM call to classify stories as HOT/WARM/SKIP
- **Prioritization:** Morning Commander ranks tasks by due date, energy required, and available time blocks
- **Review:** Social Drafter runs every draft through the 12-rule Copy Reviewer before output
- **Comparison:** CI Scanner diffs current state against a stored baseline to surface actual changes
- **Pattern detection:** Weekly Architect tracks behavioral drift across completion rates, dropped categories, and time accuracy

### Layer 3: Human-in-the-Loop Delivery

All agent output goes to Slack. The human reviews and acts. Key interaction patterns:

- **Approval queue:** Morning Brief numbers items and tags them POST/MONITOR/IGNORE. Human replies with item numbers to trigger drafting.
- **Review-and-publish:** Social Drafter delivers ready-to-post content. Human copies to Buffer.
- **Alert-and-decide:** Weekly Architect surfaces pattern alerts. Human decides whether to adjust.

Agents never take irreversible actions. They prepare, recommend, and draft. The human executes.

---

## Agent Communication

Agents don't communicate directly with each other. Each reads from shared data sources (Notion, Slack, filesystem) and writes its output to a designated channel. This keeps the system simple, debuggable, and easy to modify.

Future improvement: chain agents so Morning Brief output feeds into Social Drafter input, creating a daily pipeline from news to published content.

---

## Failure Modes and Recovery

**Agent fails to run:** Cron-based, so it'll attempt again next cycle. No cascading failures.

**Bad data in:** Agents that pull from web search can surface irrelevant news. The approval queue pattern means nothing gets published without human review.

**System abandonment:** The most common failure mode. Addressed by design principle #5 (built-in recovery). Agents run regardless of human engagement. When you come back, the data is there. The Weekly Architect catches drift patterns automatically.

**Noisy output:** If an agent's output becomes too verbose or irrelevant, the Friday Agent Review flags it. The system reviews itself weekly.
