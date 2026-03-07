# Story Scout

An autonomous Twitter monitoring agent that classifies AI stories by relevance and urgency, drafts social content for high-value stories, and delivers to Telegram.

**Full implementation:** [github.com/jakemeany523/story-scout](https://github.com/jakemeany523/story-scout) (private repo, available on request)

## Architecture

See the main [README](../README.md#standalone-agent-story-scout) for the full pipeline diagram and cost optimization case study.

## Key Stats

- **Cost:** Under $10/week for 24/7 monitoring (down from $110/day in v1)
- **Pipeline:** Keyword pre-filter (free) -> Classify + Tier (1 API call) -> Draft only HOT stories
- **Classification accuracy:** HOT/WARM/SKIP tiering with 91% cost reduction vs. naive approach
- **Tech stack:** Python, Claude API (Sonnet), Twitter API, Telegram Bot API, SQLite
