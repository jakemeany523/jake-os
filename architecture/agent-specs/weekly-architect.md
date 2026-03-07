# Weekly Architect

**Schedule:** Sunday at 7:00 PM (local timezone)
**Delivery:** Slack channel
**Type:** Claude scheduled task (cron-based)

## Purpose

Weekly review and planning agent. Reviews past week's execution, detects behavioral patterns, and builds next week's priority map. The self-improving feedback loop of the system.

## What It Tracks

### Execution Metrics
- **Completion rate:** Planned tasks done vs. planned
- **Dropped categories:** Which types of work are consistently skipped
- **Time accuracy:** Are estimates matching reality
- **Overflow patterns:** Which days consistently have unfinished work
- **Comms compliance:** Stayed within designated communication windows or was Slack open all day

### Personal Goals
- Exercise sessions completed (target: 4-5/week)
- Relationship time (intentional, not default)
- Hobby/skill development sessions
- Evening structure adherence

### Pattern Detection
The agent surfaces a "Pattern Alert" when it detects drift:

```
PATTERN ALERT:
- AI Mastery sessions skipped 3 of last 4 weeks. Consider moving to mornings only.
- Tuesday deep work block interrupted 4/4 weeks. May not be a viable deep block.
- Follow-ups database has 8 items over 7 days old. Schedule a catch-up block.
```

## Output Structure

1. **Last Week Scorecard:** Tasks done / planned, highlights, misses
2. **Carry-Forward:** Incomplete items that need rescheduling
3. **Next Week Priority Map:** Top 2-3 priorities per day, mapped to available time blocks
4. **Campaign Checkpoints:** Upcoming milestones from marketing calendar
5. **Personal Goals Check:** Hit/miss on exercise, relationship, hobby, skill dev
6. **Stale Follow-Ups:** Items open too long
7. **Pattern Alert:** Behavioral drift detection
8. **Skill Development Assignments:** AI mastery days, product marketing session, product leadership session
9. **Monday Content Topics:** Pre-drafted based on past week's events

## Design Decisions

**Why Sunday at 7 PM:** Gives time to review and adjust before Monday morning. Late enough that the weekend isn't interrupted, early enough to act on it.

**Why pattern detection over goal-setting:** Setting goals is easy. Noticing when you've drifted from them is hard. The system does the noticing; the human decides whether to recommit or adjust.

**Why suggest, never enforce:** The agent might say "consider dropping Product Leadership track, 0 sessions in 2 months." But it doesn't remove the track. Keeping agency with the human prevents the system from feeling controlling.
