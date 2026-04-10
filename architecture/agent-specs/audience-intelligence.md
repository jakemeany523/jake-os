# Agent Spec: Audience Intelligence Weekly Report

**Not an autonomous scheduled agent.** This is a scripted data pipeline run manually every Monday morning (5-10 minutes). Documents here for system completeness.

**Script:** `mixpanel-weekly-intel.py`
**Companion:** `utm-link-generator.py`
**Full system doc:** `audience-intelligence-system.md`

---

## The Job

Close the blindspot between content performance (what performed) and audience identity (WHO engaged). Every week, identify which visitors are ICPs, which sign-ups are worth enriching, and which behaviors signal buying intent.

The output feeds directly into Clay (enrichment) and Pipedrive (pipeline), creating a direct line from a Twitter post to a named contact in the sales pipeline.

---

## When to Run

**Monday morning, during the 7:15-9:00 AM deep work block.**

This runs just before or just after the Monday content batch. You want this week's engager data before you build next week's content strategy.

The workflow integrates into the Monday Power Day structure from JakeOS-v3:
```
7:00 - 7:15   Morning brief (read Slack brief)
7:15 - 7:45   Run Audience Intelligence report (this workflow)
7:45 - 9:00   Content batch for the week
9:00 - 9:15   Standup
9:30 - 10:30  Load content into Buffer + UTM links applied
```

---

## Full Execution Sequence (45 min total, every Monday)

### Phase 1: Mixpanel Pull (10 min)

```bash
export MIXPANEL_API_KEY="c74d6f2bc122d8ada9a5c4ea0b3d00b9"
python3 mixpanel-weekly-intel.py
```

Review the report. Note:
- High-intent users (behavior score >= 7): add to Clay import list
- Sign-ups with company data: priority enrichment candidates
- Top pages: are ICPs hitting `/comparison` and `/pricing`? Or just `/models` (research phase)?
- UTM data (once live): which campaign drove the most sign-ups?

### Phase 2: Twitter Analytics Export (10 min)

*(Available once Twitter Analytics access is confirmed tomorrow, March 10)*

1. Go to Twitter Analytics > Tweets > Export last 7 days
2. Download CSV. Open it.
3. Filter by: Impressions >= 500 (or sort by top engagers)
4. Identify the top 20-30 accounts that replied, quoted, or mentioned @LayerLens this week
5. Cross-reference with Mixpanel high-intent list: did any of them also visit the site?

### Phase 3: Clay Enrichment (5 min)

1. Add the top 20-30 Twitter handles to the Clay "Social Engagers" table
2. Run enrichment: Clay auto-populates company, title, size, industry, LinkedIn
3. AI Classification column auto-runs (see Clay Classification Prompt in system doc)
4. Review Tier assignments. Check for false positives (most common: founders at non-AI companies get over-scored).

### Phase 4: Combine Scores and Route (10 min)

For each enriched contact, calculate combined score:

```
Combined Score = Clay Tier Score + Mixpanel Behavior Score

Tier 1 (Executive/Buyer): 10
Tier 2 (Technical Champion): 8
Tier 3 (Ecosystem Multiplier): 7
Tier 4 (Influence Layer): 5
Non-ICP: 0

Behavior score: from Mixpanel report (0-15)
```

**Routing decisions:**

| Combined Score | Action |
|---------------|--------|
| >= 13 | Push to Pipedrive as lead. Flag for Raj. |
| 8-12 | Add to Mailchimp nurture sequence (tag: evaluation) |
| 5-7 | Monitor. Add to Clay table, no action yet. |
| < 5 | Log only. Not worth enrichment credits. |

### Phase 5: Update Weekly Tracker (5 min)

Open `audience-intelligence-templates.xlsx` > "Weekly Persona Tracker" sheet.

Fill in for this week:
- Date
- Total Twitter engagers pulled
- Clay credits used
- Tier breakdown count
- ICP percentage
- Leads pushed to Pipedrive
- Average behavior score

This data feeds the Monthly Review attribution analysis.

### Phase 6: UTM Links for This Week's Content (5 min)

```bash
python3 utm-link-generator.py --quick
```

Copy the relevant tagged link for each post type. Paste into Buffer when loading the week's content batch.

---

## Data Sources

| Source | What It Provides | Access |
|--------|-----------------|--------|
| Mixpanel Export API | Site behavior, sign-ups, event data, intent signals | MIXPANEL_API_KEY env variable |
| Twitter Analytics CSV | Top engagers, impressions, profile data | Manual export (Twitter Analytics) |
| Clay | Enrichment: company, title, size, industry, LinkedIn | clay.com |
| audience-intelligence-templates.xlsx | Weekly tracker, attribution table | Local file |

---

## Outputs This Workflow Produces

| Output | Destination | Use |
|--------|------------|-----|
| Mixpanel intel report (.md file) | Local directory | Weekly review, action items |
| Clay enriched contacts | Clay table | Tier scoring, persona classification |
| Pipedrive leads (score >= 13) | Pipedrive | Raj's pipeline view |
| Mailchimp contacts (score 8-12) | Mailchimp list | Nurture automation |
| Weekly tracker row | audience-intelligence-templates.xlsx | Monthly attribution |

---

## Costs

| Tool | Cost |
|------|------|
| Mixpanel Export API | Included in account |
| Clay enrichment | ~30-50 credits/week (Starter plan: 2,000/month) |
| Twitter Analytics | Free with existing account |

Budget: well within Clay Starter capacity. 30-50 enrichments/week = 120-200/month. Starter provides 2,000. 6-10x headroom.

---

## When This System Is Fully Working (Milestones)

1. **Today:** Mixpanel behavior data + Clay enrichment + Pipedrive routing. Working.
2. **After Marin's fix (this week):** UTM data populates. Can trace specific posts to site visits.
3. **After Marin's fix (this week):** External referrer populates. Can see Twitter vs. LinkedIn vs. Google traffic.
4. **After Twitter Analytics access (tomorrow):** Can match Twitter engagers to Mixpanel visitors.
5. **After Mailchimp webhook (next week):** Email engagement feeds back into combined scoring.
6. **After 4 weeks of data:** Enough baseline to make content strategy decisions from ICP percentage data.

---

## Recurring Tasks to Add in Notion

These should be seeded in the Master Tasks DB as recurring items:

| Task | Recurrence | Category | Context |
|------|-----------|---------|---------|
| Run Mixpanel weekly intel report | Weekly (Monday) | Analytics/Reporting | Deep Work |
| Export Twitter Analytics, import engagers to Clay | Weekly (Monday) | Analytics/Reporting | Deep Work |
| Update weekly ICP tracking table | Weekly (Monday) | Analytics/Reporting | Admin |
| Review Mailchimp nurture performance | Weekly (Monday) | Analytics/Reporting | Admin |
| Pull Clarity recordings for top leads | Weekly (Monday) | Analytics/Reporting | Deep Work |
| Monthly content attribution review | Monthly (last Friday) | Analytics/Reporting | Deep Work |
