# LayerLens Video

Data-driven branded video generation built on Remotion.

## What It Does

Generates LayerLens-branded mp4 videos from live Stratix evaluation data. Videos are React components where time is a prop. Data goes in as JSON, branded mp4s come out. Integrated into the Social Content Drafter so data-heavy posts auto-trigger video rendering alongside static graphics.

## Architecture

```
Stratix SDK  -->  Python glue script  -->  JSON props  -->  Remotion render  -->  mp4
                                                                                  |
                                                                           Buffer / social
```

## Templates

| Template | Dimensions | Duration | Use Case |
|----------|-----------|----------|----------|
| benchmark-drop | 1920x1080 | 6s | Animated leaderboard reveal, top N models with score bars |
| benchmark-drop-vertical | 1080x1920 | 6s | Same, vertical for Reels/Shorts |
| model-launch-card | 1920x1080 | 4s | Single model + headline stat announcement |
| four-pillars | 1920x1080 | 8s | Observe / Evaluate / Improve / Trust kinetic explainer |

## Brand Enforcement

Every template wraps in a shared `<Frame>` component that enforces:
- White background, brand blue (#1454FF), brand navy (#072A78)
- Inter font via @remotion/google-fonts
- LayerLens logo bottom-right on every frame
- Footer: "Evaluated on Stratix by LayerLens"
- No dates, no pricing

## Integration Points

- **Stratix SDK:** Live evaluation data for template props
- **Social Content Drafter:** Auto-triggers video for data-heavy archetypes
- **Branded Graphics:** Static counterpart (same data, PNG output)
- **Buffer:** Scheduling with video upload support
- **Copy Reviewer:** Post copy reviewed before delivery

## Key Design Decisions

- Remotion chosen for code-driven, versionable, data-driven templates
- Templates are React components, so brand rules are enforced by code, not convention
- Glue script normalizes SDK pagination (page_size=200) and score formats (0-1 vs 0-100)
- Graceful fallback: if video render fails, post ships with static graphic only

## Stack

React 18, Remotion 4.x, TypeScript, @remotion/google-fonts, Python 3 (glue script)
