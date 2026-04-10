---
rubric: social-post
version: 2026-04-09
applies_to: LayerLens Twitter/X and LinkedIn posts (Jake first-person voice)
threshold: 7.5
---

# Social Post Rubric (LayerLens)

Score every dimension 0-10. Be strict. A passing draft should average ≥7.5 with no dimension below 7.0.

## Dimensions

### 1. hook_strength
Does the first line create tension, stakes, or curiosity within 10 words? A "label hook" ("AI eval update") is a 3. A data-surprise hook with a specific number is typically a 7-9. A counter-narrative hook that overturns a reader assumption is 9-10. Bland statements of fact are 4-5.

### 2. voice_fit
Does it sound like Jake? First-person ("I ran", "I put"), direct, slightly irreverent, no hedging, no corporate "we," no AI tells. Profile reference: `memory/reference/profiles/layerlens.md`. Banned phrases in `copy-reviewer` SKILL.md trigger automatic cap at 4.

### 3. specificity
Does it cite a concrete number, model name, benchmark, dollar amount, or timestamp? Vague ("recent benchmarks show") is 3-4. One specific number in context is 7. Multiple specific numbers with a named model + benchmark is 9-10.

### 4. narrative_alignment
Does it connect to the Judgment Engineering thesis OR one of the Four Pillars (Observe / Evaluate / Improve / Trust)? A benchmark drop with no narrative connection is an auto 3. A benchmark drop that frames the result as evidence for a pillar is 7-9. A counter-narrative piece that reframes how practitioners should think about eval is 9-10.

### 5. shareability
Would a practitioner DM this to a coworker or quote-tweet it? Corporate announcements: 3-4. Educational but dry: 5-6. Has a "wait, what?" moment: 7-8. Contains a number or claim that forces a reaction: 9-10.

### 6. ending_quality
Does it end with a question, a strong takeaway, or a reader-actionable next step? Trailing off or a weak "let me know what you think" is 4. A precise question that invites a specific answer is 8. A claim that dares disagreement is 9-10.

## Hard caps (override scores)

- Contains an em dash → cap average at 3.0, flag for rewrite.
- Contains any banned phrase from copy-reviewer → cap voice_fit at 4.
- Wrong platform constraint (Twitter >280 chars, LinkedIn <200 words) → cap at 5.0.
- Invented numbers or unverified claims → cap at 2.0, flag for fact-check.

## Notes

Hook and specificity are the two dimensions that correlate hardest with actual engagement in the existing performance log. When rewriting in the loop, prefer fixing hook + specificity over shareability (which is a consequence of the first two).
