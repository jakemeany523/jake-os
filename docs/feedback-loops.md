# Feedback Loops: A Self-Improving System

Jake-OS has three nested feedback loops operating at different timescales. Each one catches problems the faster loops miss.

## Loop 1: Daily (Morning Commander + Morning Brief)

**Cycle time:** 24 hours
**What it catches:** Missed tasks, overdue items, inbox accumulation, follow-up gaps

The Morning Commander surfaces anything that slipped through yesterday. If a task was planned but not done, it reappears today with overdue status. If a follow-up was promised by yesterday, it's flagged.

This is the "nothing falls through the cracks" loop. It doesn't analyze patterns; it just makes sure individual items stay visible.

## Loop 2: Weekly (Weekly Architect + Agent Review)

**Cycle time:** 7 days
**What it catches:** Behavioral drift, category neglect, time estimation errors, system degradation

The Weekly Architect looks at the week as a whole:
- What % of planned tasks got done?
- Which categories are consistently being skipped?
- Are time estimates accurate?
- Which days overflow?
- Are personal goals (exercise, relationships, skill development) being maintained?

The Agent Review (Friday) examines the system itself:
- Are skill triggers firing correctly?
- Is agent output still useful or becoming noise?
- Are there new automation opportunities?
- Do any components need upgrading?

**Pattern Alert example:**
```
AI Mastery sessions skipped 3 of last 4 weeks. Consider moving to mornings only.
Tuesday deep work block interrupted 4/4 weeks. This may not be a viable deep block.
Follow-ups database has 8 items over 7 days old. Schedule a catch-up block.
```

This loop catches trends that are invisible day-to-day. Skipping one AI mastery session doesn't register as a problem. Skipping three in four weeks is a pattern that needs addressing.

## Loop 3: Monthly (Monthly Strategist)

**Cycle time:** 30 days
**What it catches:** Strategic drift, goal abandonment, system staleness, life maintenance gaps

The Monthly Strategist reviews 4-week trends:
- System adherence score (0-10)
- Top 3 wins
- Top 3 friction points
- Recommended structural adjustments
- Skill track progress (hours, sessions, trajectory)

This loop catches things like: "You haven't done a single Product Leadership session in 2 months. Either recommit or drop the track." It's the honest conversation with yourself that's easy to avoid.

## Loop 4: Quarterly (Triggered by Monthly Strategist)

**Cycle time:** 90 days
**What it catches:** Structural issues, tool obsolescence, fundamental misalignment

Every third Monthly Strategist report includes a deeper audit:
- Is the Notion structure still serving you?
- Are any recurring tasks irrelevant?
- Should any tools be swapped?
- Are the agents' outputs genuinely useful?
- Full skill track progress review against original goals

This is the "burn it down and rebuild" escape valve. Most quarters won't need major changes. But the audit forces the question, preventing the system from becoming a monument to past decisions.

## Key Design Rule: Suggest, Never Enforce

All feedback loops produce recommendations, not actions. The Weekly Architect might say "consider moving AI Mastery to mornings only." It doesn't move anything. The Monthly Strategist might say "drop Product Leadership." It doesn't delete the track.

The human retains full agency. The system's job is to notice, analyze, and recommend. The human's job is to decide.

This matters for adoption. A system that makes changes on your behalf feels controlling. A system that presents data and lets you decide feels like a trusted advisor.
