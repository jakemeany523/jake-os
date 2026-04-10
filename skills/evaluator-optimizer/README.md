---
name: evaluator-optimizer
description: |
  Shared evaluator-optimizer loop. Takes a draft artifact, runs it through the quality-judge skill against a named rubric, and if any dimension is below threshold, rewrites the weakest parts and re-scores. Loops until all dimensions clear threshold OR max_iterations is hit. The core "self-improving draft" primitive every content skill should use.

  Trigger on: "run the loop", "optimize this draft", "iterate until it passes", "evaluator-optimizer", or any call from another skill (social-content-drafter, mandamus-lawyer-linkedin-voice, email-newsletter-drafter, community-content-drafter, etc.) asking to refine a draft to a quality bar. Also trigger aggressively inside any LayerLens or Mandamus content drafting flow that has a matching rubric in quality-judge/rubrics/.
---

# Evaluator-Optimizer Loop

This skill is a reusable primitive. Other skills invoke it. It is NOT a drafter. It does not know how to write a LinkedIn post or an email. It only knows how to take a draft, score it, and drive it toward a quality bar.

## Inputs

When invoked, you must have:

1. **draft** — the artifact being refined (string, markdown, post text).
2. **rubric_name** — the filename under `.claude/skills/quality-judge/rubrics/` to score against (e.g. `social-post`, `mandamus-linkedin`, `email`, `ci-brief`).
3. **context** — optional. Any source material, profile reference, original brief, or dataset exemplars that should inform both the judge and the rewriter. Pass it through. **Must include platform constraints** (e.g. `platform: twitter, max_chars: 280`, `platform: linkedin, word_range: [300,500]`) so the rewriter self-constrains and never produces an iteration that blows a hard cap. Must also include `profile` (layerlens / mandamus-house) and, for Mandamus, `client`.
4. **threshold** — default 7.5/10 across all dimensions. Caller can override.
5. **max_iterations** — default 3. Caller can override. Hard ceiling is 5 to prevent runaway cost.
6. **cost_budget** — optional. Max LLM calls the loop is allowed to make (rewrite + judge = 2 calls per iteration). Defaults to 2 * max_iterations. Token counts per call are logged in the JSONL under `tokens_in` / `tokens_out` so weekly spend can be computed from the log alone.

## The loop

```
iteration = 0
lineage = []
draft_id_0 = new_id()
score = judge(draft, rubric_name, context, iteration=0)
lineage.append(draft_id_0)
calls_used = 1

while any_dimension_below(score, threshold) and iteration < max_iterations and calls_used + 2 <= cost_budget:
    iteration += 1
    weakest = lowest_dimensions(score)  # may be 1 or more if tied
    feedback = { d: score[d].reasoning for d in weakest }
    draft = rewrite(draft, weakest, feedback, context, platform_constraints=context.platform)
    calls_used += 1
    draft_id = new_id()
    score = judge(
        draft, rubric_name, context,
        iteration=iteration,
        parent_draft_id=draft_id_0,
        dimensions_targeted=weakest,
        lineage=lineage + [draft_id],
    )
    calls_used += 1
    lineage.append(draft_id)

return draft, score, iteration, lineage
```

## Rewrite rules

1. **Minimal edit.** Rewrite ONLY what is needed to fix the targeted dimensions. Do not touch passing dimensions. This prevents oscillation and keeps per-iteration attribution clean.
2. **Preserve voice.** The profile rules (brand-voice.md, mandamus house rules) still apply. Judge feedback is ADDITIVE to the voice floor, never a license to violate it.
3. **Fix ties in parallel.** If two dimensions tie for lowest, fix them both in one pass. Log all dimensions fixed in `dimensions_targeted`.
4. **Same-dimension-twice escalation.** If the same dimension fails twice in a row with <0.5 point improvement, stop the loop. Return best-so-far and flag `local_minimum: true` with the stuck dimension name.
5. **Pass platform constraints into the rewrite prompt.** The rewriter must know the char/word limit before it starts typing. Never let an iteration produce output that blows a hard-cap length rule.

## Invoking from another skill (pseudocode)

```
draft = write_initial_post(prompt, profile, exemplars)
result = evaluator_optimizer.run(
    draft=draft,
    rubric_name="social-post",
    context={
      "profile": "layerlens",
      "archetype": "benchmark_drop",
      "platform": "twitter",
      "max_chars": 280,
    },
    threshold=7.5,
    max_iterations=3,
)
deliver(result.draft, result.final_scores, result.iterations, result.lineage)
```

As an instruction-layer skill (not a code library), callers follow these steps in prose:

1. Write initial draft using the drafter's own rules.
2. Invoke `quality-judge` with rubric + draft + context (including platform constraints). Log.
3. If any dimension below threshold, identify lowest dimension(s). Rewrite ONLY those. Keep everything else identical. Respect platform constraints.
4. Re-invoke `quality-judge` with `iteration` and `dimensions_targeted` fields populated. Log.
5. Repeat up to max_iterations or until all pass or local minimum detected.
6. Deliver final draft with score block, iteration count, and lineage (list of draft_ids).

## Logging

Every iteration appends one line to:

```
/sessions/fervent-elegant-pasteur/mnt/LL Claude Project Files/memory/evolving/quality-scores.jsonl
```

The `quality-judge` skill handles the actual append. Loop's job is to ensure judge is called every iteration and `dimensions_targeted`, `lineage`, `tokens_in`, `tokens_out` fields are populated so the log is queryable.

## Stop conditions (priority order)

1. **All dimensions ≥ threshold** → status `passed`.
2. **Max iterations hit** → status `max_iterations_reached`.
3. **Cost budget exhausted** → status `cost_budget_exhausted`.
4. **Same dimension stuck <0.5 improvement twice** → status `local_minimum`, tell Jake which dimension.
5. **Judge error or malformed score** → status `judge_error`. Return draft unchanged.

## Output contract

```
{
  "draft": "<final text>",
  "iterations": <int>,
  "final_scores": { "<dimension>": <float>, ... },
  "avg_score": <float>,
  "status": "passed" | "max_iterations_reached" | "cost_budget_exhausted" | "local_minimum" | "judge_error",
  "rubric": "<rubric_name>",
  "rubric_version": "<from rubric file frontmatter>",
  "lineage": ["draft_id_0", "draft_id_1", ...],
  "calls_used": <int>,
  "tokens_total": { "in": <int>, "out": <int> }
}
```

The caller presents this to Jake alongside the final draft. Never hide the iteration count. Seeing "this draft went through 2 passes, started at 4.3 avg, ended at 8.3 avg, cost 4 LLM calls" is the highest-trust signal you can give.

## Self-grading bias note

The judge and the rewriter are the same model class. Scores may drift high because the model is scoring its own work. The weekly digest task must surface any rubric where model scores consistently exceed human-override scores by >1.5 points — that gap is the self-grading bias. Do not mitigate inside this skill; mitigate in the digest + the rubric anchors.

## What this skill does NOT do

- Does not draft from scratch.
- Does not decide rubric dimensions (that's in the rubric file).
- Does not override brand voice or hard-fail rules.
- Does not post, publish, or schedule.

## Anti-patterns

- Looping on a rubric with no ceiling (fix the rubric).
- Rewriting the whole draft every iteration (per-iteration attribution breaks).
- Skipping the log (the log IS the measurement layer).
- Letting an iteration produce output that violates a deterministic hard cap (platform constraints must be in the rewrite prompt).
