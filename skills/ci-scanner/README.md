# Competitive Intelligence Scanner

Automated weekly competitive research across 5 primary competitors. Combines web search with Ahrefs SEO data via MCP (Model Context Protocol) to produce a 1-page brief reviewable in under 5 minutes.

## How It Works

### Data Collection
For each competitor, the scanner pulls:
- **Web search:** Recent news, product announcements, blog posts, press releases
- **Ahrefs (via MCP):** Domain rating changes, new referring domains, organic keyword movement, top pages by traffic
- **Hiring signals:** Job postings that indicate strategic direction (e.g., "hiring 5 ML engineers" suggests product investment)
- **Content strategy:** What topics they're publishing about, frequency changes, new content formats

### Baseline Comparison
The scanner stores the previous week's scan as a baseline. Each new scan diffs against it:
- **New:** Things that appeared this week that weren't there last week
- **Changed:** Metrics that moved significantly (domain rating +/- 2, keyword ranking shifts > 5 positions)
- **Stable:** No significant changes (mentioned briefly, not elaborated)

This diff approach is critical. Most CI tools dump everything every week. The scanner surfaces what actually changed.

### Output
A structured 1-page brief:

```
COMPETITIVE INTEL BRIEF - Week of [date]

HEADLINE CHANGES (read these first):
- Competitor A launched [feature]. Relevant because [angle].
- Competitor B's domain rating increased by 3 points. Driven by [source].

DETAILED BREAKDOWN:
[Per-competitor sections with new/changed/stable items]

IMPLICATIONS:
[2-3 strategic takeaways for our positioning]
```

## Competitors Tracked

The scanner is configured for 5 competitors across three categories:
1. **Observability + Evaluation** (largest competitor, highest overlap)
2. **Crowdsourced Leaderboard** (different model, partial overlap)
3. **Independent Benchmarking** (reports vs. platform distinction)
4. **Trace-driven Evaluation** (closest product overlap)
5. **Ecosystem-locked Evaluation** (framework dependency differentiator)

## Design Decisions

**Why 5 competitors, not 10:** Attention is finite. Five competitors produce a reviewable brief. Ten would produce a document nobody reads.

**Why Ahrefs via MCP:** Direct API access through Model Context Protocol means the agent can pull live data without custom integration code. Domain rating, backlinks, and keyword data come from the same tool the SEO team uses manually.

**Why baseline comparison:** The insight isn't "Competitor A has a domain rating of 72." The insight is "Competitor A's domain rating went from 69 to 72 this week, driven by 15 new referring domains from tech publications." The delta is what matters.
