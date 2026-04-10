# Benchmark Drop

Automated benchmark release content workflow with video pipeline.

## What It Does

When new evaluation data lands in Stratix, this skill automates the full benchmark-drop pipeline: pull data, identify SOTA results and regressions, generate branded comparison charts AND animated video assets, and produce publish-ready social copy.

## Workflow

1. Pull evaluation data from Stratix SDK (page_size=200, always)
2. Identify notable results (SOTA, regressions, model comparisons)
3. Generate branded PNG comparison charts (layerlens-graphics)
4. Render branded mp4 video via Remotion (horizontal + vertical)
5. Draft Twitter/X and LinkedIn copy
6. Run through Copy Reviewer
7. Package for approval (copy + static graphic + video)

## Video Pipeline

Built on Remotion (React-based programmatic video). The Stratix glue script pulls live leaderboard data and writes a JSON props file. Remotion renders branded mp4s with animated score bars, rank reveals, and consistent brand identity.

Templates:
- `benchmark-drop` (1920x1080, 6s) - horizontal for Twitter/LinkedIn
- `benchmark-drop-vertical` (1080x1920, 6s) - vertical for Reels/Shorts

One command, live data, ~30 seconds on M-series Mac.

## Integration Points

- **Stratix SDK:** Primary data source (pc.evaluations.get_many with benchmark filter)
- **Remotion:** Video rendering engine (data-driven React templates)
- **Branded Graphics:** Static chart generation with brand identity enforcement
- **Copy Reviewer:** Quality gate
- **Buffer:** Scheduling with video upload support
