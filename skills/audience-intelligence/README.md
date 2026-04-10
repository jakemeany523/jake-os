# Audience Intelligence: Mixpanel Weekly Intel Script

**What:** Python script that pulls raw Mixpanel Export API data, analyzes 7-14 days of events, and produces a structured Markdown intelligence report identifying who is visiting the site, which behaviors signal buying intent, and which contacts are ready for CRM enrichment.

**File:** `mixpanel-weekly-intel.py`

**Purpose in the system:** Closes the blindspot between content performance and audience identity. Most analytics tells you what content performed. This tells you WHO was engaged and what they did on the site.

---

## What It Analyzes

The script processes all Mixpanel events for the target period and extracts:

**High-Intent Users (Behavior Scoring):**

| Event | Score | Why |
|-------|-------|-----|
| `stratix.sign-up.start` | +5 | Raised hand |
| `stratix.sign-up.success` | +5 | Converted |
| `stratix.public:compare-models` | +3 | Active product evaluation |
| `stratix.public:home-cta-click` | +2 | Conversion intent |
| `stratix.sign-in.start` | +2 | Returning user signal |
| `stratix.sign-in.success` | +2 | Active user |
| `stratix.share-benchmark.start` | +1 | Amplification intent |

**Intent Page Visits:**

| Page | Signal |
|------|--------|
| `/comparison` | Model Comparison (high intent) |
| `/sign-up` | Sign-up page (high intent) |
| `/pricing` | Pricing page (high intent) |
| `/evaluation-spaces` | Product exploration |
| `/benchmarks` | Technical evaluation |
| `/models` | Research phase |

**Sign-up enrichment data** (email, name, company when available).

**UTM attribution** (once `track_utm: true` is enabled in Mixpanel init).

**External referrers** (once `save_referrer: true` is enabled).

**Geography** (city, country breakdown).

---

## Output Format

Produces a Markdown report named `mixpanel-intel-YYYY-MM-DD-to-YYYY-MM-DD.md` containing:

1. **Summary** (total events, unique visitors, high-intent count, sign-up count)
2. **High-Intent Users** (sorted by behavior score, top 20, import into Clay)
3. **Sign-ups** (complete contact data, push to Clay for enrichment then Pipedrive)
4. **Intent Page Visits** (buying/evaluation signals)
5. **Event Breakdown** (top 15 events by volume)
6. **UTM Source Attribution** (empty until engineering enables `track_utm: true`)
7. **External Referrers** (empty until `save_referrer: true` is enabled)
8. **CTA Clicks** (conversion intent tracking)
9. **Top Pages** (top 15 by traffic)
10. **Top Countries**
11. **Action Items** (specific list of who to push to Clay/Pipedrive this week)

---

## Usage

```bash
# Set API key
export MIXPANEL_API_KEY="your_api_key_here"

# Run (last 7 days, default)
python3 mixpanel-weekly-intel.py

# Custom range
python3 mixpanel-weekly-intel.py --days 14
```

**When to run:** Every Monday at 9 AM, or whenever building this week's Clay import list.

---

## How It Fits Into the Weekly Workflow

```
Monday Morning
    |
    v
Run mixpanel-weekly-intel.py
    |
    v
Report: List of high-intent users (distinct IDs + behavior scores)
    |
    v
Cross-reference with Twitter Analytics engager list
    |
    v
Clay: Import handles, run enrichment + ICP scoring
    |
    v
Combined score = Clay Tier Score + Mixpanel Behavior Score
    |
    v
Score >= 13: Push to Pipedrive (Raj visibility)
Score 8-12: Add to Mailchimp nurture sequence
Score < 8: Monitor
```

---

## Real Output Sample (March 7-9, 2026 data)

From a 2-day test run:
- 8,773 total events
- 7,616 unique visitors
- 15 high-intent users
- 6 sign-ups

Notable identified users:
- `david.puente.mur@nttdata.com` (NTT Data, existing customer, behavior score 7)
- `art.two@agentruntime.com` (behavior score 12)
- `ledionbezati@gmail.com` (behavior score 10)

These users were not visible through any other channel.

---

## Known Gaps (Engineering Fixes Pending)

1. **No UTM data**: `track_utm: true` not yet set in Mixpanel init. Script detects this and surfaces the fix.
2. **No external referrer**: `save_referrer: true` not yet set. Same issue.
3. **Spam sign-ups**: Some sign-up events contain bot/test data. Needs cleanup from engineering.

Script handles all three gracefully: shows the gap and states what's needed, rather than silently producing empty sections.

---

## Cost

Mixpanel Export API: included in existing Mixpanel account. No additional cost.

Script runtime: ~10 seconds for a 7-day window.
