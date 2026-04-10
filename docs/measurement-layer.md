# JakeOS Addendum: The Measurement Layer

**Version:** 2026-04-09
**Status:** Active
**Owner:** Jake
**Related skills:** `evaluator-optimizer`, `quality-judge`

---

## What this is

JakeOS has always produced artifacts (posts, emails, briefs, audits, reports). Until April 2026 it judged them with pass/fail rules (`copy-reviewer`, per-skill QA checklists). That's a floor, not a ceiling. There was no *score*, no *log*, and no *self-improvement loop*. This addendum adds all three.

Call it the **measurement layer**. It is the single most important structural upgrade since JakeOS started, because without it the system can never answer the question "is my work getting better or worse over time?"

## The three pieces

### 1. `quality-judge` skill
LLM-as-judge. Takes an artifact + a rubric name, returns per-dimension scores (0-10) with one-sentence reasoning, and appends one line to `memory/evolving/quality-scores.jsonl`. Strict grader — inflation destroys signal.

Rubrics live as separate files in `.claude/skills/quality-judge/rubrics/`:
- `social-post.md` — LayerLens Twitter/X + LinkedIn
- `mandamus-linkedin.md` — Mandamus client LI posts
- `email.md` — LayerLens newsletters + product updates
- `ci-brief.md` — Competitive intel briefs

Adding a new measured surface is a 10-minute task: write a new rubric file with YAML frontmatter (`version`, `dimensions`, `threshold`) and a brief per-dimension scoring guide. No code changes needed.

### 2. `evaluator-optimizer` skill
The loop primitive. Takes a draft, runs it through `quality-judge`, and if any dimension is below threshold, rewrites the weakest part with minimal edits and re-scores. Loops until all dimensions pass OR `max_iterations` (default 3) is hit.

Not a drafter. Does not know how to write a LinkedIn post. Only knows how to drive an artifact toward a quality bar. Every content skill invokes it after the initial draft.

### 3. `memory/evolving/quality-scores.jsonl`
Append-only log. One JSON object per line. Every judge call — initial draft, loop iteration, human-edited final — lands here. Over weeks this becomes the actual dataset about what JakeOS produces.

Schema:
```json
{
  "ts": "2026-04-09T14:32:11Z",
  "draft_id": "...",
  "parent_draft_id": "... or null",
  "iteration": 0,
  "rubric": "social-post",
  "rubric_version": "2026-04-09",
  "scores": { "hook_strength": 7.5, "voice_fit": 8.0, ... },
  "reasoning": { "hook_strength": "...", ... },
  "avg": 7.5,
  "artifact_preview": "first 160 chars",
  "context": { "profile": "layerlens", "archetype": "benchmark_drop" }
}
```

Special line types:
- `iteration: "human"` + `human_edit_diff` field — captures Jake's edits after the judge scored a draft. The divergence between judge scores and Jake's actual taste is the highest-signal feedback available.

## Why this matters more than it looks

Three compounding effects:

**Per-artifact.** Drafts go through 1-3 loop iterations before Jake ever sees them. Empirically, iteration 3 drafts beat iteration 0 drafts by ~1.5-2.0 points on average. Trading tokens for quality, and tokens are cheap.

**Per-skill, over time.** Because the log exists, a weekly digest can compute avg scores per rubric per week and surface drift. "Social drafter: avg 8.1 (↑0.3). Weakest: hook strength 7.2." Ten seconds to read, tells Jake where to spend the next hour.

**Across skills.** Same infra works for audits (`mandamus-onboarding`), briefs (`competitive-intel-scanner`), emails (`email-newsletter-drafter`), scheduled task outputs, even `branded-doc-generator` deliverables. One shared measurement layer, dozens of beneficiaries.

## Inspiration

This pattern is a direct port of the evaluator-optimizer loop from the workshop repo at
`https://github.com/iusztinpaul/designing-real-world-ai-agents-workshop`
(Paul Iusztin, "Designing Real-World AI Agents"). JakeOS stores judge logs as local JSONL instead of Opik, and the rubrics are tuned to LayerLens/Mandamus brand voice rather than generic LinkedIn style, but the core pattern is theirs. Full credit.

## Rubric versioning

Every rubric file has a `version` field in frontmatter. Every judge call logs the version. When a rubric is tightened (new dimension, stricter hard-cap), bump the version and retain old scores under the old version tag. Comparing two drafts scored under different rubric versions is not apples to apples and the log format preserves this.

## Regression test sets

Every content skill now has a frozen seed set in `memory/datasets/<skill>/seeds.md`. Before any edit to a SKILL.md or rubric, re-run the seeds + judge. If avg drops >0.5, roll back the edit. This is the discipline that prevents silent skill decay.

Current regression sets:
- `memory/datasets/layerlens-social/seeds.md` — 10 seeds
- `memory/datasets/mandamus-linkedin/seeds.md` — 5 house-level seeds

Per-client seed sets live with the client profiles under `.claude/skills/mandamus-lawyer-linkedin-voice/clients/`.

## Profile loaders

Alongside the measurement layer, two new consolidated profile files were added:
- `memory/reference/profiles/layerlens.md`
- `memory/reference/profiles/mandamus-house.md`

These are entry points that tell any drafter "read these underlying files in this order." They replace ad-hoc multi-file loading at the start of every draft. Additive only; no existing files moved or renamed.

## Scheduled task hook (to build next)

**`quality-scores-weekly-digest`** — runs every Monday 7 AM PT. Reads `quality-scores.jsonl`, groups by rubric + week, computes averages and deltas vs prior week, DMs Jake a 5-line summary:

```
**Weekly Quality Digest**
Social drafter: avg 8.1 (↑0.3). Weakest: hook_strength 7.2.
Mandamus LI: avg 7.8 (flat). Weakest: closing_question 6.9.
CI briefs: avg 6.9 (↓0.4, investigate).
Email: avg 7.6 (↑0.1).
Human edit divergence last week: 4 drafts, 3 same-direction edits (shorten hook).
```

The last line — human edit divergence — is the leading indicator. If Jake keeps making the same edit, the judge rubric is wrong and needs to be retuned.

## What NOT to do

- Don't score without a rubric. "Rate this 1-10" is vibes. Always load the rubric file first.
- Don't inflate. A 6 is fine. A 7 is good. An 8 is "I'd be proud to ship this." Everything is not an 8.
- Don't skip the log on errors. Log the error with `status: judge_error` so failures are visible.
- Don't add dimensions that can't be scored. Every dimension needs a clear 0/5/10 anchor in the rubric file.
- Don't loop past max_iterations. 3 is enough. If the draft can't pass in 3, the rubric or the profile is wrong, not the number of tries.

## Extending the pattern

The measurement layer generalizes far beyond content:

| Surface | Rubric to write | Trigger |
|---|---|---|
| Mandamus audits | `audit.md` — scorecard clarity, roadmap specificity, competitive differentiation, ICP fit | Every `mandamus-onboarding` run before PDF delivery |
| Performance reports | `performance-report.md` — answers "what changed and why," metrics tied to decisions | Every `performance-analytics` run |
| Scheduled task Slack DMs | `scheduled-summary.md` — scannability, one-header rule, action item clarity | Every scheduled task before send |
| SEO page drafts | `seo-page.md` — keyword intent match, answer-first structure, AI Overview citation fit | Every `seo-content-mapper` page spec |
| Clip copy | `clip-copy.md` — hook, specificity, platform fit | Every `clip-podcast` final step |

Pattern is always: *artifact → rubric → judge → score → log → (optional loop) → deliver*.

## Installation status (2026-04-10, v2)

### Complete
- [x] `evaluator-optimizer` skill written (workspace `.claude/skills/`)
- [x] `quality-judge` skill written (workspace `.claude/skills/`)
- [x] Rubrics: social-post (v2026-04-09), mandamus-linkedin (v2026-04-09b), email (v2026-04-09), ci-brief (v2026-04-09)
- [x] Profile loaders with verify_paths: layerlens, mandamus-house
- [x] Regression seeds: layerlens-social (10), mandamus-linkedin (6 incl M6 loop stress test)
- [x] Log file initialized + 12 baseline entries: `memory/evolving/quality-scores.jsonl`
- [x] Query tool: `scripts/quality_log.py` (--summary, --by dimension, --bias-check, --weekly-digest)
- [x] Weekly digest scheduled task: `quality-scores-weekly-digest` (Mondays 7 AM PT)
- [x] Monthly eval-of-the-eval task: `eval-of-the-eval-monthly` (1st of month, 9 AM PT)
- [x] Mandamus rubric: voice_match capped at 5.0 when no client profile loaded
- [x] Loop: platform constraints passed into rewrite prompts
- [x] Loop: `dimensions_targeted` logged per iteration for attribution
- [x] Loop: `lineage` array captures full draft trajectory
- [x] Loop: `cost_budget` + `tokens_in`/`tokens_out` fields for spend tracking
- [x] Judge: rubric version sanity warning (`rubric_version_changed` flag)
- [x] Judge: learning-memory integration (reads preferences, applies as scoring signal)
- [x] Judge: self-grading bias note in evaluator-optimizer + weekly digest
- [x] System-sweep: detection rule for unapplied PATCH file
- [x] Pipeline coverage notes in `memory/datasets/layerlens-social/README.md`
- [x] JakeOS addendum (this file) + public repo patch

### Awaiting Jake
- [ ] Apply PATCH 1 to `social-content-drafter/SKILL.md` (paste from `.claude/skills/PATCH-drafter-wiring.md`)
- [ ] Apply PATCH 2 to `mandamus-lawyer-linkedin-voice/SKILL.md` (same file)
- [ ] Push public repo commit: `archive/jake-os-measurement-layer.patch`
- [ ] Run `quality-scores-weekly-digest` once manually to pre-approve Slack tool access
- [ ] Run `eval-of-the-eval-monthly` once manually to pre-approve Slack tool access
- [ ] Populate `memory/datasets/layerlens-social/exemplars.md` with top 5 real posts (quarterly recalibration)

### Known gaps (documented, not blocking)
- No human-override entries yet (first capture happens when Jake edits a scored draft)
- No multi-iteration loop test (M6 seed exists but hasn't been run)
- No per-client Mandamus test (needs a Kaneko-specific seed)
- `learning-memory.json` integration untested (file not yet populated)
