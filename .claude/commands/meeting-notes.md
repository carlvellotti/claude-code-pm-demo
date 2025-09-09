# Extract Meeting Notes and Action Items

You are an expert at synthesizing meeting transcripts into clear, actionable summaries. Follow these steps:

1. **Input**: Read the meeting transcript provided

2. **Extract Key Information**:
   - Meeting metadata (date, attendees, duration)
   - Main discussion topics
   - Decisions made
   - Action items by person
   - Follow-up items
   - Key metrics or data points mentioned

3. **Create Structured Output**:

```markdown
# Meeting Summary: [Meeting Title]
**Date:** [Date]
**Attendees:** [List]
**Duration:** [Time]

## Key Discussion Points
- [Bullet points of main topics, 3-5 items]

## Decisions Made
1. [Numbered list of concrete decisions]

## Action Items
### [Person Name]
- [ ] [Specific action with deadline if mentioned]
- [ ] [Another action]

### [Next Person]
- [ ] [Their actions]

## Important Metrics/Data
- [Any numbers, percentages, or KPIs mentioned]

## Next Steps
- [What happens next]
- [Follow-up meeting if scheduled]

## Risks/Concerns Raised
- [Any blockers or concerns mentioned]
```

4. **Additional Outputs**:
   - Create a brief Slack update (2-3 sentences)
   - Flag any urgent items needing immediate attention
   - Note any resource requests or dependencies

5. **Save Output**:
   - Save summary to `/meeting-summaries/[date]-[meeting-name]-summary.md`
   - Copy action items to relevant project tracking location

Focus on clarity and actionability. The summary should be scannable in under 1 minute.