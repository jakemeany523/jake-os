# Monthly Strategist

**Schedule:** 1st of each month at 8:00 AM (local timezone)
**Delivery:** Slack channel
**Type:** Claude scheduled task (cron-based)

## Purpose

Strategic reset agent. Reviews the full month: work output, marketing metrics, personal goals, system health. Identifies 4-week trends that weekly reviews miss. Sets the strategic direction for the coming month.

## Output Structure

1. **Month in Review:** Tasks completed, content published, campaigns run
2. **Marketing Metrics:** Ahrefs keyword rankings, domain rating, organic traffic trends
3. **Campaign Calendar:** What's in flight, what's launching, what wrapped up
4. **Personal Goals Review:** Fitness phase progress, habit consistency, skill track hours
5. **Life Maintenance:** Quarterly items coming due (dentist, car service, subscription audit)
6. **Next Month's Top 5 Priorities:** Strategic focus areas
7. **Monthly Trend Analysis:** System adherence score (0-10), top 3 wins, top 3 friction points, recommended adjustments
8. **Skill Track Progress:** Hours invested, sessions completed, recommended adjustments

## Design Decisions

**Why monthly:** Weekly reviews catch tactical drift. Monthly reviews catch strategic drift. Different timescale, different insights.

**Why include life maintenance:** Preventive care and maintenance tasks are the first things dropped when work gets busy. Surfacing them in a monthly review prevents the "I haven't been to the dentist in 18 months" problem.

**Why a system adherence score:** A single number (0-10) forces an honest assessment of whether the system is being used. It's harder to ignore "adherence: 3/10" than a paragraph of nuanced analysis.
