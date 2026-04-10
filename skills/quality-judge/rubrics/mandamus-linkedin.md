---
rubric: mandamus-linkedin
version: 2026-04-09b
applies_to: Mandamus client LinkedIn posts (ghostwritten attorney voice)
threshold: 7.5
---

# Mandamus LinkedIn Rubric

Score every dimension 0-10. Be strict. The Mandamus bar is higher than LayerLens because ghostwriting for attorneys has legal + reputational stakes.

## Dimensions

### 1. voice_match
Does it sound like THIS attorney (per `clients/<slug>.md`), not generic boutique-lawyer voice? First person "I," plain language, specific war-story cadence from the client profile. Generic boutique voice = 5. Distinct-but-shaky = 7. Indistinguishable from the client's own reference posts = 9-10.

### 2. hook_quality
One line, 5-12 words, contains either a metaphor, a number, or a tension. Label hooks ("A thought on non-competes") are 2-3. Story-in-5-words hooks are 8-10.

### 3. specificity
Numbers, days of the week, dollar amounts, time spans, anonymized war stories. Vague "clients often ask me" is 3. "One Tuesday morning, a founder called me about a $4M acquisition" is 9.

### 4. compliance_cleanliness
Zero unflagged compliance issues per state bar (NY, CA, etc.) and universal red flags from `references/compliance.md`. Any unflagged specialization claim, comparative claim, dollar-result claim without disclaimer, or testimonial-as-fact = instant cap at 3.0 and flag for attorney review.

### 5. structural_fit
Matches the structural template OR the practice-area-specific variant from the client profile. Hook on its own line, ≥8 paragraph breaks, exactly one CTA, ends with a question. Missing any = cap at 6.

### 6. house_rule_compliance
Zero em dashes. ≤3 hashtags (default 0). No URLs in body. No "I help X do Y" intro. No firm voice. No AI tells (banned phrase list). Any violation caps the rubric at 4.0.

### 7. closing_question
Ends with a question that is easy to answer in one sentence. Closed-ended or rhetorical questions are 4-5. Open but abstract ("what do you think?") is 5. Specific + emotionally accessible ("which one would you have taken, the 80% settlement on day one or the 100% chance after 18 months?") is 9-10.

## Hard caps (override scores)

- Em dash present → 3.0 max.
- Banned phrase present → 4.0 max.
- Specialization claim without bar certification flag → 3.0 max, compliance_cleanliness = 0.
- Firm voice ("at [Firm], we...") → 4.0 max.
- Dollar-amount result without disclaimer flag → 3.0 max.
- No closing question → 5.0 max.
- **No client profile loaded → voice_match capped at 5.0, flag `no_profile: true`.** The skill must refuse to silently use generic voice. If the judge is asked to score a draft with `context.client` missing or unknown, cap voice_match at 5.0 and surface the flag so the caller knows to stop and load a profile before re-running.

## Notes

This rubric is the FLOOR. The client profile and the exemplars bank can add per-practice-area dimensions that override or augment these (e.g., non-compete lawyers may use a "ruling + take" structure instead of war stories). If the client profile specifies additional dimensions, append them to this rubric at scoring time.
