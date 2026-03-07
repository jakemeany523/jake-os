# Morning Commander

**Schedule:** Daily at 6:15 AM (local timezone)
**Delivery:** Slack DM or dedicated channel
**Type:** Claude scheduled task (cron-based)

## Purpose

The executive assistant agent. Reads from calendar, task management, and fitness plan to deliver a structured morning brief before the workday starts. Designed for ADHD: eliminates planning paralysis by pre-selecting the day's priorities.

## Data Sources

| Source | What It Reads | Why |
|--------|--------------|-----|
| Google Calendar | Today's meetings, available blocks | Calculate deep work capacity, prep notes |
| Notion Master Tasks | Tasks with Do Date = today, Status != Done | Today's work priorities |
| Notion Master Tasks | Due Date < today, Status != Done | Surface overdue items |
| Notion Master Tasks | Status = Inbox | Count unprocessed inbox items |
| Notion Follow-Ups | Status = Open, Promised Date <= today | Follow-ups due today |
| Notion Marketing Calendar | Status = In Flight | Campaign checkpoints |
| Fitness Plan | Current phase + day of week | Specific workout assignment |

## Output Structure

1. Day of week + total available deep work hours (calculated from calendar gaps)
2. Morning ritual reminder (medication, sunlight, mobility routine)
3. Top 3-5 work tasks sorted by priority (selected by due date, energy requirement, available time)
4. Today's meetings with times and 1-line prep notes
5. Today's workout (specific exercises, sets, reps from phase-aware 12-week plan)
6. AI mastery session (yes/no, based on every-other-day rotation)
7. Overdue items (count + top 3)
8. Follow-ups due today
9. Inbox count
10. Personal items (relationship time, errands, appointments)
11. Evening plan
12. Campaign checkpoint (if milestone this week)

## Design Decisions

**Why 6:15 AM:** Arrives before morning routine starts. Ready to read at 7:00 AM with coffee.

**Why pre-select tasks:** ADHD planning paralysis means an open task list causes decision fatigue. The agent narrows 50+ tasks down to 3-5 based on objective criteria. The human picks from a short list, not an infinite backlog.

**Why include fitness:** Exercise compliance drops when it's not part of the daily plan. Including specific exercises (not just "work out") reduces friction to starting.

**Why include personal items:** Work-life separation fails when personal tasks are in a separate system. One integrated brief prevents things from falling through the cracks.
