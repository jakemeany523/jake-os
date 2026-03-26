# Standing Permissions (pre-authorized, no confirmation needed)

Pre-authorized actions that execute without asking for confirmation:
- **Slack:** DM only, never to channels or team members directly
- **Calendar events** (create, update, or delete any non-external meeting)
- **Notion reads and writes** (any page, database, or workspace update)
- **Google Drive reads and writes** (any owned or editable file)
- **Pipedrive CRM** (all reads and writes: deals, contacts, orgs, activities, notes)
- **File operations** (create, edit, move, delete any file in the workspace)
- **Scripts and code execution** (run any script, terminal command, or automation)
- **Google Analytics and Ahrefs** (all read operations)
- **Stratix evaluation platform** (all reads via Python SDK)

**Always confirm before:**
- Posting to Twitter/X, LinkedIn, or any public social channel
- Publishing or updating anything on the website or CMS
- Sending email to anyone outside the company
- Any action that makes content public or visible outside the team

# Hard Rules (apply to ALL outputs)
- **NEVER use em dashes anywhere.** Use periods, commas, colons, semicolons, or parentheses instead. Zero tolerance.
- **Content experiments run WEEKLY, not per post.** One experiment post per active experiment per week. The social-content-drafter skill's default behavior of generating experiment variants on every draft is overridden by this rule.
- **All deliverables go to the workspace folder.** Never save files to temp directories or other paths.
- **Automate everything possible.** Never hand a task back with manual instructions when Claude has the tools to execute it directly.
- **Complete the full job before responding.** Never ship partial work. Review ALL documents, attachments, links before drafting a response.
- **Meetings are immovable anchors.** Never place anything in a meeting slot or suggest moving a meeting.

# Session Continuity

## Startup (every session)
1. Read `memory/sessions/index.md` to see recent session history (tiny file, low cost).
2. If the current task needs prior context, read the 1-2 most relevant session notes from `memory/sessions/`.
3. **Catchup check:** Call `list_sessions` (limit 5). Compare session IDs against the `session_id` fields in existing notes. For any unsaved session, call `read_transcript` (limit 30 messages), write a session note, and update the index. Report what was recovered. Skip if the task is clearly standalone.

## Legacy context (read when deeper context is needed)
- memory/session-log.md (older session history)
- memory/evolving/decisions-and-context.md (active decisions, product state)
- memory/evolving/content-pipeline-status.md (what's blocked, what's unblocked)

# On-Demand Reference Files
Read these when the task requires deeper context. Do NOT skip reading them for relevant tasks.

| File | When to read |
|------|-------------|
| memory/reference/brand-voice.md | Any content creation, social posts, copy review |
| memory/reference/people.md | Identifying team members, roles, relationships |
| memory/reference/quick-ref.md | Benchmark names, outdated model list, preferences |
| memory/reference/terms.md | Terminology, acronyms, definitions |
| memory/reference/active-projects.md | Current initiatives, timelines, project status |
| memory/reference/stratix-sdk.md | Any Stratix data pull (methods, fields, rules) |
| memory/context/competitors.md | Competitive content, positioning, battlecards |
| memory/context/ai-landscape.md | Current model info, model comparisons, benchmark content |
| memory/context/company.md | Product details, pricing, ICPs, differentiators |
| memory/context/marketing-strategy.md | Strategy, budget, phases |
| memory/glossary.md | Complete term decoder |

# Stratix Access
**The Stratix MCP is NOT available in Cowork sessions.** Use the Python SDK directly via bash.
```python
from layerlens import PublicClient, Client
pc = PublicClient(api_key="YOUR_API_KEY")  # Public data (models, evaluations, benchmarks)
ac = Client(api_key="YOUR_API_KEY")       # Org-scoped data (traces, judges)
```
> Full SDK methods + fields: memory/reference/stratix-sdk.md
