# Logo Compositing Skill

Adds the official brand logo watermark to any image. Uses bundled SVG assets (never recreates or approximates the logo) with automatic background brightness detection for variant selection.

## How It Works

1. Takes any input image (PNG, JPG, or generated chart)
2. Analyzes pixel brightness at the logo placement region (bottom-right)
3. Selects the appropriate logo variant:
   - **Color variant:** For light/white backgrounds
   - **White variant:** For dark/colored backgrounds
4. Composites the logo at the correct position with appropriate sizing
5. Returns the branded image

## Design Decisions

**Why bundled SVG assets:** Logo integrity is non-negotiable for brand teams. LLMs can approximate logos from description, but approximation introduces errors (wrong proportions, missing elements, color shifts). Bundling the exact SVG files and compositing them ensures pixel-perfect output every time.

**Why auto-detect brightness:** Manual variant selection adds friction and error. The skill checks the actual pixel values in the logo region and makes the right choice automatically. Works for solid backgrounds, gradients, and photographic backgrounds.

**Why a separate skill from Data Viz:** Data Viz creates charts and includes logos as part of its pipeline. Logo Compositing is a standalone tool for adding the logo to any image: screenshots, photos, partner graphics, event materials. Different use cases, shared logo assets.
