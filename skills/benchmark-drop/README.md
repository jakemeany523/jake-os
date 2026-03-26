# Benchmark Drop

Automated benchmark release content workflow.

## What It Does

When new evaluation data lands in Stratix, this skill automates the full benchmark-drop pipeline: pull data, identify SOTA results and regressions, generate branded comparison charts, and produce publish-ready social copy.

## Workflow

1. Pull evaluation data from Stratix SDK
2. Identify notable results (SOTA, regressions, model comparisons)
3. Generate branded PNG comparison charts
4. Draft Twitter/X and LinkedIn copy
5. Run through Copy Reviewer
6. Package for approval

## Integration Points

- **Stratix SDK:** Primary data source
- **Branded Graphics:** Chart generation with brand identity enforcement
- **Copy Reviewer:** Quality gate
