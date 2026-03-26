# Social Content Drafter

Drafts publish-ready social content for Twitter/X and LinkedIn.

## What It Does

The core content creation skill. Pulls live evaluation data from Stratix, generates branded data visualizations, drafts platform-native copy, and runs every draft through the Copy Reviewer before delivery.

## Workflow

1. Read learning memory for accumulated preferences and patterns
2. Check Stratix for fresh evaluation data worth highlighting
3. Read morning brief context and reactive intel (if available)
4. Draft platform-specific content (Twitter/X format vs. LinkedIn format)
5. Generate branded comparison graphics when data supports it
6. Run every draft through the Copy Reviewer skill
7. Deliver a ready-to-publish package with copy + graphics

## Integration Points

- **Stratix SDK:** Pulls model evaluations, benchmark results, SOTA data
- **Copy Reviewer:** Every draft is auto-reviewed before delivery
- **Learning Memory:** Reads preferences at startup, applies accumulated patterns
- **Content Experiments:** Respects active experiment cadence (weekly, not per-post)
- **Morning Brief:** Chains from the morning brief context file when available

## Key Design Decisions

- Brand voice rules are baked into the generation prompt, not just checked after the fact
- Graphics follow strict brand identity: specific hex colors, logo placement, no dates
- Platform-specific formatting (Twitter character limits, LinkedIn paragraph structure)
- Experiment variants only generated when explicitly requested
