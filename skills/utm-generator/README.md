# UTM Link Generator

**What:** Python script that generates properly tagged UTM links for all LayerLens social posts, newsletters, and influencer content. Enforces consistent parameter values so attribution data in Mixpanel is clean and queryable.

**File:** `utm-link-generator.py`

**Purpose in the system:** Every link posted to social or sent in email should carry UTM parameters so Mixpanel can attribute site visits and sign-ups to the specific content piece that drove them. Without UTMs, all traffic looks like Direct.

---

## Why This Matters

Without UTM tagging:
- 100 clicks from a Twitter post look like "Direct" in Mixpanel
- You don't know which campaign drove a sign-up
- Influencer performance is invisible
- "Content-to-pipeline" attribution is impossible

With UTM tagging:
- Every post, link, and newsletter is trackable
- `utm_campaign=benchmark-drop` tells you benchmark content drove 40 sign-ups this month
- Influencer links carry `utm_source=influencer-[name]` so each creator's ROI is measurable
- The Mixpanel weekly intel report surfaces this automatically

---

## Parameters Enforced

**Valid Sources** (utm_source):
`twitter` / `linkedin` / `newsletter` / `youtube` / `reddit` / `hackernews`

**Valid Mediums** (utm_medium):
`social` / `email` / `partner` / `paid` / `referral`

**Valid Campaigns** (utm_campaign):
`benchmark-drop` / `thesis-narrative` / `product-demo` / `education-hub` / `agent-eval` / `influencer-collab` / `website-rebuild` / `show-hn`

**Content tag** (utm_content):
Auto-generated as `MMDD-short-desc`. Example: `0309-claude-swebench-drop`

---

## Usage

### Interactive mode (single link)
```bash
python3 utm-link-generator.py
```
Prompts for URL, source, medium, campaign, content description. Outputs tagged URL + character count.

### Quick mode (today's standard links)
```bash
python3 utm-link-generator.py --quick
```
Generates the 7 most common link patterns for today's date. Run this at the start of every content session.

```
Twitter benchmark drop:
  https://layerlens.com?utm_source=twitter&utm_medium=social&utm_campaign=benchmark-drop&utm_content=0309

Twitter thesis post:
  https://layerlens.com?utm_source=twitter&utm_medium=social&utm_campaign=thesis-narrative&utm_content=0309

Twitter product demo:
  https://layerlens.com?utm_source=twitter&utm_medium=social&utm_campaign=product-demo&utm_content=0309
...
```

### Batch mode (bulk from CSV)
```bash
python3 utm-link-generator.py --batch links.csv
```
CSV columns: `url, source, medium, campaign, content_desc`
Outputs: `links-utm.csv` with all generated links.

---

## Rule: Never Post a Naked Link

Every layerlens.com link that goes into a post, tweet, newsletter, or influencer brief should have UTM parameters. No exceptions. The generator enforces consistent parameter spelling so data is clean.

**Wrong:** `https://layerlens.com/benchmarks`
**Right:** `https://layerlens.com/benchmarks?utm_source=twitter&utm_medium=social&utm_campaign=benchmark-drop&utm_content=0309-gemini3-drop`

---

## Influencer Links

For the March Influencer Blitz, each creator gets their own tagged link:

```
utm_source=influencer-[creator-handle]
utm_medium=partner
utm_campaign=influencer-collab
utm_content=0309-[creator-handle]
```

Generate with interactive mode: enter `influencer-john_q_creator` as the source. The script allows non-standard source values with a warning, so influencer-specific names work.

---

## How It Fits Into the Weekly Workflow

```
Monday morning content batch
    |
    v
Run: python3 utm-link-generator.py --quick
    |
    v
Copy the relevant tagged link for each post type
    |
    v
Paste into tweets/posts before loading into Buffer
    |
    v
Mixpanel captures utm_source, utm_campaign on each site visit
    |
    v
Weekly intel report shows which campaigns are driving traffic/sign-ups
```

---

## Cost

No external dependencies. Pure Python standard library. Free.
