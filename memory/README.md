# Memory System Architecture

Jake-OS maintains persistent context across sessions through a file-based memory system. Every session and agent has access to accumulated institutional knowledge, preferences, and strategic decisions.

## Structure

The memory system is organized into 8 categories:

### `sessions/`
Per-session structured summaries with YAML frontmatter. An `index.md` file tracks all sessions chronologically. Every new session reads the index at startup, and relevant session notes are loaded on demand. Unsaved sessions are automatically recovered via the catchup check protocol.

### `reference/`
Stable reference material that changes infrequently:
- **brand-voice.md** - Voice guidelines, tone rules, banned phrases
- **terms.md** - Terminology, acronyms, definitions
- **quick-ref.md** - Benchmark names, model lists, preferences
- **active-projects.md** - Current initiatives and timelines
- **stratix-sdk.md** - SDK methods, fields, and usage patterns
- **people.md** - Team roles and relationships
- **workflow-cheat-sheet.md** - Common task patterns

### `context/`
Domain context that evolves as the market moves:
- **competitors.md** - Competitive positioning and battlecards
- **ai-landscape.md** - Current model info and comparisons
- **company.md** - Product details, pricing, ICPs, differentiators
- **marketing-strategy.md** - Strategy, budget, campaign phases

### `evolving/`
Rapidly changing state that updates session to session:
- **decisions-and-context.md** - Active decisions, product state changes
- **content-pipeline-status.md** - What's blocked, unblocked, in progress

### `competitive-intel/`
CI scan baselines and historical briefs. The Competitive Intel Scanner skill compares each weekly scan against the stored baseline to surface what actually changed.

### `projects/`
Project-specific context files for ongoing initiatives (website rebuild, Twitter growth, narrative shift, etc.).

### `rlhf/`
Skill feedback and improvement data. Stores test samples, feedback from eval cycles, and version notes for skills like the Copy Reviewer.

### `archive/`
Retired guidelines and superseded context. Kept for reference but not actively read.

## How It Works

1. **Session startup:** Read `sessions/index.md` to load recent session history.
2. **On-demand loading:** Skills and agents read only the reference files they need (routed by the CLAUDE.md reference table).
3. **Learning memory:** A structured JSON store (`learning-memory.json`) captures preferences, content insights, and strategic decisions. Content-producing skills read this at startup, so the system improves with use.
4. **Content experiments:** Tracked in `content-experiments.json` with hypotheses, variants, results, and learnings.
5. **Session save:** At the end of productive sessions, a structured summary is written to `sessions/` and the index is updated.

## Design Decisions

- **File-based, not database.** Files are readable, versionable, and work natively with Claude's tools. No infrastructure to maintain.
- **Read routing, not monolithic context.** Rather than loading everything at startup, the CLAUDE.md reference table tells skills which files to read for which tasks. This keeps context focused and token-efficient.
- **Self-correcting.** The Strategic Drift Detector skill scans memory files against skills and content to catch inconsistencies before they compound.
