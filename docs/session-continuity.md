# Session Continuity

One of the core problems with AI-assisted workflows is that every session starts from zero. Context dies between conversations. Strategic decisions, preferences, meeting commitments, and competitive intel evaporate the moment you close a tab.

Jake-OS solves this with a layered session continuity system.

## The Problem

Without session continuity:
- You re-explain the same preferences every session
- Strategic decisions from last week's conversation are forgotten
- Meeting commitments discussed in one session don't carry to the next
- Content experiments lose context on what was tested and what was learned
- Brand voice corrections made in one session repeat in the next

## How It Works

### Session Startup Protocol

Every session follows a three-step startup:

1. **Read the session index.** A lightweight `sessions/index.md` file lists all recent sessions with one-line summaries. This costs almost nothing to read but immediately orients the system.

2. **Load relevant context.** If the current task connects to a previous session, load the 1-2 most relevant session notes. These contain structured summaries: what was decided, what was produced, and what was left unfinished.

3. **Catchup check.** Compare recent Cowork sessions against saved notes. Any unsaved session gets its transcript read, summarized, and saved. This prevents context loss even when sessions end without explicit saving.

### Session Notes

Each session note is a structured markdown file with:
- Session date and ID
- What was worked on
- Key decisions made
- Deliverables produced
- Open items and follow-ups

### Layered Context Loading

Not all context is created equal. The system uses three tiers:

- **Always loaded:** Session index (tiny, cheap)
- **On-demand reference:** Brand voice, terminology, team info, SDK docs (loaded when relevant to the task)
- **Deep context:** Competitive intel, marketing strategy, AI landscape (loaded only when the task specifically requires it)

This keeps token usage efficient while ensuring nothing important is missed.

## Learning Memory

Beyond session continuity, the system maintains a persistent learning memory that captures:
- Content preferences and patterns
- Corrections and feedback
- Strategic decisions and their reasoning
- Experiment results and conclusions

Every content-producing skill reads learning memory at startup. This means corrections stick: if you tell the system once that a certain phrasing doesn't work, it remembers.

## The Result

Context compounds instead of resetting. A conversation about competitive positioning on Monday informs the social content drafted on Tuesday. A meeting commitment captured on Wednesday surfaces in Thursday's morning brief. Preferences set in week 1 still hold in week 10.

The system gets better the more you use it.
