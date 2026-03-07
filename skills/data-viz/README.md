# Data Visualization Generator

Branded chart and graphic creation skill with automated quality validation. Every output enforces visual identity standards: specific hex colors, logo placement, footer text, overlap detection, and date stripping.

## Capabilities

- Bar charts (grouped, stacked, horizontal)
- Line charts (single and multi-series)
- Scatter plots
- Comparison graphics (side-by-side model/product comparisons)
- Social cards (text-heavy branded images for Twitter/LinkedIn)
- Infographic-style data summaries

## Brand Enforcement

Every generated image includes:
- **Brand colors:** Primary blue (#1454FF), navy (#072A78), white background
- **Logo placement:** Bottom-right corner, official SVG asset composited (never recreated)
- **Background detection:** Auto-selects color or white logo variant based on background brightness at the logo region
- **Footer text:** "Evaluated on [Product] by [Company]" at bottom
- **No dates:** Brand rule. Dates are stripped from all graphics to keep content evergreen.

## Automated Validation

Before delivery, every graphic runs through:
1. **Overlap detection:** Checks if any text overlaps with other text, data points, or the logo
2. **Logo placement verification:** Confirms logo is in the correct position and variant
3. **Brand color compliance:** Verifies only approved colors are used
4. **Layout quality:** Checks margins, spacing, and readability

## Helper Functions

The skill ships with reusable functions for consistent output:
- `create_chart()`: Initializes a matplotlib figure with brand defaults
- `save_chart()`: Saves with logo compositing and validation
- `BRAND` dictionary: Color hex values, font sizes, spacing constants

## Example Output Types

**Benchmark Comparison:** Side-by-side bar chart showing model performance across multiple benchmarks. Each model gets a color from the brand palette. Logo bottom-right. No dates.

**Social Card:** Large stat number (e.g., "135+ Models Evaluated"), supporting text, branded background. Designed for Twitter/LinkedIn sharing.

**Trend Line:** Multi-series line chart showing metric movement over time. Legend, axis labels, and data points all checked for overlap before delivery.
