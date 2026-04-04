# JakeOS

**An AI-augmented operating system for solo marketing.**

11 autonomous agents. 16 custom skills. Persistent memory. Self-correcting feedback loops. Built to handle the workload of 4-5 people while the human focuses on strategy.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=flat&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agents](https://img.shields.io/badge/Agents-11-green)]()
[![Skills](https://img.shields.io/badge/Skills-16-blue)]()

## Why This Exists

I'm the solo marketer at [LayerLens](https://layerlens.com), an AI evaluation infrastructure company. Content, social, SEO, AEO, influencer, brand. All one person.

Instead of hiring, I built an operating system. JakeOS is not a chatbot wrapper or a prompt library. It's a multi-agent system with persistent memory, scheduled execution, self-review cycles, and human-in-the-loop delivery. Every agent reads shared context, applies domain-specific logic, and outputs to Slack for human approval before anything ships.

**The result:** I operate at the output level of a 4-5 person marketing team. Story Scout costs dropped 91% ($110/day to under $10/week). The system has scaled from 7 agents + 4 skills to 11 agents + 16 skills without increasing complexity.

## Architecture

```
                        +---------------------------+
                        |     LAYER 1: INGESTION    |
                        |     (8 Data Sources)      |
                        +---------------------------+
                        | Web Search  | GitHub      |
                        | Twitter/X   | Slack       |
                        | Ahrefs      | Calendar    |
                        | Notion      | Product App |
                        +-------------+-------------+
                                  |
                                  v
                        +---------------------------+
                        |  LAYER 2: PROCESSING      |
                        |  (Domain-Specific Logic)  |
                        +---------------------------+
                        | Classify  | Prioritize    |
                        | Review    | Compare       |
                        | Draft     | Detect Drift  |
                        +---------------------------+
                                  |
                                  v
                        +---------------------------+
                        |  LAYER 3: DELIVERY        |
                        |  (Human-in-the-Loop)      |
                        +---------------------------+
                        | Approval Queue            |
                        | Review-and-Publish        |
                        | Alert-and-Decide          |
                        +---------------------------+
                                  |
                                  v
                            [Slack / Human]
```

**Key design principle:** Agents never take irreversible actions. They prepare, recommend, and draft. Humans execute.

**Agent communication:** No direct agent-to-agent messaging. All agents read from and write to shared data sources (Notion, Slack, filesystem). Output goes to designated Slack channels. Pipeline coordination happens through scheduling (e.g., Morning Brief at 7:00 AM feeds into Social Drafter at 7:30 AM).

## Agents

### Daily
| Agent | Schedule | What It Does |
|-------|----------|-------------|
| Morning Commander | 6:30 AM | Ranks tasks by due date, energy cost, and available time blocks |
| Morning Brief | 7:00 AM | Scans news, competitors, product updates. Outputs numbered approval queue |
| Social Drafter | 7:30 AM (MWF) | Drafts publish-ready social content. All drafts pass 12-rule copy review |
| Midday Update | 12:00 PM | Quick status check, surfaces blockers, adjusts afternoon priorities |
| Reactive Intel Monitor | Continuous | Watches for breaking AI news, model launches, competitor moves |

### Weekly
| Agent | Schedule | What It Does |
|-------|----------|-------------|
| Performance Feedback | Monday | Pulls GA4, Ahrefs, content logs. Reports what worked, what didn't |
| Agent Review | Friday | Self-review cycle. Identifies noisy agents, stale skills, drift |
| John Q Batch | Tuesday | Batch LinkedIn content with educational framing |
| Weekly Architect | Sunday | Pattern detection across completion rates, dropped categories, time accuracy |

### Monthly + On-Demand
| Agent | Schedule | What It Does |
|-------|----------|-------------|
| Strategist | 1st of month | Monthly retro + next month's strategic direction |
| Meeting to Tasks | On-demand | Pulls Fireflies transcripts, extracts action items to Notion |

## Skills (16)

| Category | Skills |
|----------|--------|
| **Content Creation** | Social Content Drafter, Content Repurposer, Email Newsletter Drafter, Community Content Drafter |
| **Quality Control** | Copy Reviewer (12-rule system with hard-fail and warning tiers) |
| **Research & Intel** | Competitive Intel Scanner, SEO Content Mapper, DevPulse |
| **Analytics** | Performance Analytics, Content Experiment Tracker |
| **Planning** | Weekly Content Planner |
| **Memory** | Learning Memory (persistent preferences, insights, copy patterns) |
| **Operations** | Branded Doc Generator, LayerLens Graphics, System Sweep |
| **Publishing** | Framer Blog Publisher |

All content-producing skills read Learning Memory at startup and enforce Copy Reviewer rules before delivery.

> Skills are available as a standalone open-source library: [ai-marketing-skills](https://github.com/jakemeany523/ai-marketing-skills)

## Memory System

50+ files across 8 categories. This is what gives the system continuity across sessions.

```
memory/
  sessions/           # Session notes for cross-session context
  reference/          # Brand voice, people, preferences, terminology
  context/            # Competitors, AI landscape, company info, strategy
  evolving/           # Active decisions, content pipeline status
  competitive-intel/  # Weekly CI scan results and baselines
```

**How it works:** Every session starts by reading `memory/sessions/index.md` to load recent context. Skills read category-specific memory (e.g., Social Content Drafter reads `reference/brand-voice.md` + `learning-memory.json`). The Learning Memory skill captures preferences from every interaction and makes them available to all downstream skills.

## Custom MCP Servers

| Server | Language | Purpose |
|--------|----------|---------|
| [Buffer MCP](https://github.com/jakemeany523/buffer-mcp) | Python | Social media scheduling via Buffer's GraphQL API |
| Fireflies MCP | TypeScript | Meeting transcript extraction and action item parsing |
| Pipedrive MCP | TypeScript | CRM access for deal tracking and contact management |

## Failure Modes (By Design)

This system is built to fail gracefully:

- **Cron-based execution** prevents cascading failures. If an agent fails, it retries next cycle
- **Approval queues** mean nothing ships without human review
- **Weekly self-review** (Agent Review) catches noisy output automatically
- **No agent-to-agent dependencies** means one broken agent doesn't take down the pipeline
- **Persistent memory** means the system recovers context even if the human disengages for days

## Results

| Metric | Before JakeOS | After JakeOS |
|--------|--------------|-------------|
| Story Scout cost | $110/day | <$10/week (91% reduction) |
| Agent count | 7 | 11 |
| Skill count | 4 | 16 |
| Content output | Manual, inconsistent | 3-4 Twitter/day, 2-3 LinkedIn/week, systematized |
| Competitor monitoring | Ad hoc | Weekly automated scans with baseline comparison |
| Content review | Manual checklist | 12-rule automated copy review on every piece |

## Getting Started

JakeOS is built on [Anthropic's Cowork platform](https://claude.ai) using Claude as the orchestration layer. The architecture is transferable to any AI agent framework.

To adapt this for your own use:

1. **Fork this repo**
2. **Edit `CLAUDE.md`** with your identity, permissions, and tool access
3. **Customize `memory/reference/`** with your brand voice, terminology, and preferences
4. **Adapt the skills** in `skills/` to your domain (or use [ai-marketing-skills](https://github.com/jakemeany523/ai-marketing-skills) as a starting point)
5. **Set up your integrations** (Slack, Notion, Calendar, etc.) via MCP servers

## License

MIT
