# Cost Optimization Case Study: Story Scout

## The Problem

Story Scout v1 was burning **$110/day** in API costs. For a monitoring tool that runs 24/7, that's $3,300/month. Unacceptable for a solo marketer's tooling budget.

## Root Cause Analysis

The original pipeline made too many API calls per tweet:

```
v1 Pipeline (per tweet):
1. Classify relevance     -> 1 API call (Sonnet, max_tokens=256)
2. Determine tier         -> 1 API call (Sonnet, max_tokens=256)
3. Generate angle         -> 1 API call (Sonnet, max_tokens=512)
4. Draft post             -> 1 API call (Sonnet, max_tokens=1024)
5. Review draft           -> 1 API call (Sonnet, max_tokens=512)

= 5 API calls per tweet, regardless of relevance
```

With 25 tweets per poll and polling every 2 hours, that's **150 API calls per poll, 1,800 per day.**

## The Fix (5 Changes)

### 1. Keyword Pre-Filter (FREE)
Added a regex-based keyword filter that runs before any API call. 27 keywords related to AI, models, benchmarks, and evaluation. If a tweet doesn't contain any keyword, it's skipped entirely.

**Impact:** Eliminates 85-95% of tweets before any API cost is incurred. On a typical poll, 25 tweets become 1-4 that pass the filter.

### 2. Combined Classify + Tier (1 Call Instead of 2)
Merged classification and tiering into a single API call. The prompt asks for both relevance assessment and tier assignment in one response.

**Impact:** 50% reduction in classification cost per tweet.

### 3. Reduced max_tokens for Classification
Classification only needs to return HOT, WARM, or SKIP. Changed `max_tokens` from 256 to 16.

**Impact:** Faster responses, lower token costs, same accuracy.

### 4. Tier-Gated Pipeline
Only HOT stories proceed to angle generation, drafting, and review. WARM stories get logged to SQLite for future reference. SKIP stories are discarded.

**Impact:** Expensive drafting pipeline (3 API calls) only runs for ~5-10% of classified tweets.

### 5. WARM Logging, Not Processing
WARM stories are stored in a local SQLite database with metadata. They're searchable and can be promoted to HOT later, but they don't trigger any API calls beyond the initial classification.

**Impact:** Preserves data without incurring cost.

## Result

```
v2 Pipeline:
Tweet (25/poll)
  -> Keyword filter (FREE, regex)         = ~2-4 pass
  -> Classify + Tier (1 call, 16 tokens)  = ~2-4 API calls
  -> HOT only: Angle + Draft + Review     = ~0-1 tweets get full treatment

Per poll: 2-5 API calls (was 150)
Per day: 24-60 API calls (was 1,800)
```

**Final cost: Under $10/week.** That's a **91% reduction** from the original $110/day.

## Lessons

1. **Filter before you classify.** A free regex check eliminated most API calls entirely.
2. **Combine calls where possible.** Two separate LLM calls that could be one prompt is pure waste.
3. **Right-size your tokens.** A classification task doesn't need 256 tokens of output.
4. **Gate expensive operations.** Only run the full pipeline on content that earned it.
5. **Log, don't discard.** WARM stories might become relevant later. Store them cheaply (SQLite) instead of throwing them away or processing them expensively.
