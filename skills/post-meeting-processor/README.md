# Post-Meeting Processor

Automated meeting follow-up pipeline.

## What It Does

Processes completed meetings by pulling Fireflies transcripts and generating follow-up emails, CRM activity logs, Notion tasks, and deal stage updates. Compresses what used to be 20 minutes of post-meeting admin into a single approval step.

## Workflow

1. Pull Fireflies transcript for the completed meeting
2. Extract action items and commitments
3. Draft follow-up email
4. Log activity in Pipedrive CRM
5. Create Notion tasks for action items
6. Suggest deal stage update if warranted
7. **Single approval gate** before execution

## Integration Points

- **Fireflies MCP:** Meeting transcript and summary
- **Pipedrive MCP:** Activity logging, deal updates
- **Notion:** Task creation
- **Gmail:** Follow-up email drafting
