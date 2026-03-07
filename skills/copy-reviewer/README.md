# Copy Reviewer Skill

A 12-rule content review engine that checks any marketing content against brand voice guidelines. Built through 3 eval iterations to reach 100% accuracy on a 25-case test corpus.

## The 12 Rules

| # | Rule | What It Checks |
|---|------|---------------|
| 1 | Banned Phrase Detection | 47 specific phrases that signal generic AI content (e.g., "game-changer," "revolutionary," "what's notable") |
| 2 | AI Slop Scoring | Detects patterns common in unedited LLM output: excessive hedging, filler sentences, vague superlatives |
| 3 | Em Dash Ban | Zero tolerance. Every em dash is flagged. Use periods, commas, colons, semicolons, or parentheses instead. |
| 4 | "So What" Test | Every piece of content must answer: why should someone care about this right now? Data without narrative context fails. |
| 5 | Product Showcase | Content should demonstrate the product's capabilities where relevant, not just talk about the category |
| 6 | CTA Check | Appropriate call-to-action present. Not every post needs one, but sales-oriented content must have one. |
| 7 | Platform Rules | Twitter/X: concise by default (long-form only when earned). LinkedIn: professional tone, industry context. |
| 8 | ICP Coverage | Content maps to at least one defined ideal customer profile |
| 9 | Differentiation | Content is clearly attributable to this company, not generic enough that a competitor could post the same thing |
| 10 | Tone Calibration | Engineer reviewing data, not marketer selling. Dry humor and cultural fluency welcome. Hype language rejected. |
| 11 | Language Preferences | Specific word choices: "evaluate" over "test," "verification" over "monitoring," "infrastructure" over "tool" |
| 12 | Outdated Reference Detection | Catches references to deprecated models, old product names, or stale data points |

## Eval Results

| Version | Pass Rate | Changes |
|---------|-----------|---------|
| v1 | 88% (22/25) | Initial rule set. Failed on near-miss banned phrases and borderline tone. |
| v2 | 96% (24/25) | Tightened banned phrase matching. Added AI slop scoring threshold. |
| v3 | 100% (25/25) | Added edge case handling for compound banned phrases. Improved tone calibration examples. |

Test corpus: 25 cases covering clean passes, obvious failures, near-miss banned phrases, borderline tone, posts that technically follow rules but lack substance, and cross-platform format violations.

## Integration

The Copy Reviewer runs automatically inside the Social Drafter agent. Every draft is reviewed before delivery. It can also be invoked manually on any content: blog drafts, email copy, presentation text, video scripts.

## Output Format

```
COPY REVIEW: [PASS/FAIL]

Rule 1 (Banned Phrases): PASS
Rule 2 (AI Slop): PASS
Rule 3 (Em Dash): FAIL - Found 2 em dashes on lines 3 and 7
  Fix: Replace "the platform — which supports" with "the platform, which supports"
Rule 4 (So What): PASS
...

OVERALL: FAIL (1 rule violated)
SUGGESTED FIXES:
1. Line 3: Replace em dash with comma
2. Line 7: Replace em dash with period and start new sentence
```
