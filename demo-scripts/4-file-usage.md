# Demo Script 4: Working with Files - PM Workflows

## Overview
Demonstrate how Claude Code can reference and synthesize information from multiple files to support common PM tasks.

## Part 1: Reference Information for PRD Creation (3 min)

### Setup the Scenario
"I need to write a PRD for a new feature. Instead of starting from scratch, let's use our existing resources."

### The Power of Context
```bash
# Prompt
"I need to create a PRD for an AI-powered workflow suggestion feature. Please:
1. Read our business-info.md to understand company context
2. Check our existing PRDs in example-prds folder for formatting  
3. Use 'technical' style from writing-styles.md
4. Include insights from customer interviews about automation
Create the PRD and save it as 'docs/prds/ai-suggestions-prd.md'"
```

**What to Emphasize:**
- Claude pulls from multiple sources automatically
- Maintains consistency with existing documents
- Incorporates real customer feedback
- Follows established patterns

### Show the Result
- Open the created PRD
- Point out how it matches company style
- Highlight customer quotes integrated

## Part 2: Synthesizing Customer Interviews (3 min)

### The Analysis Task
```bash
# Prompt
"Please analyze all customer interviews in data/customer-interviews/ and:
1. Identify the top 3 pain points mentioned across all interviews
2. Find specific quotes about mobile access needs
3. Calculate how many customers mentioned template requirements
4. Create a summary with actionable recommendations
Save this as 'research/customer-pain-points-analysis.md'"
```

**Key Points:**
- Claude reads multiple files simultaneously  
- Identifies patterns across interviews
- Quantifies feedback (X out of Y customers)
- Provides actionable output, not just data

### Follow-up Enhancement
"Now create a one-page executive summary of this analysis using our 'user-friendly' writing style"

## Part 3: Meeting Intelligence (3 min)

### Extract Action Items
```bash
# Prompt  
"Read all meeting transcripts in data/meeting-transcripts/ and:
1. Extract all action items grouped by person
2. Identify decisions that were made
3. Flag any conflicts or dependencies between meetings
4. Create a consolidated action tracker
Output as a table I can paste into our team wiki"
```

**Demonstration Value:**
- Saves hours of manual review
- Catches items that might be missed
- Creates accountability tracking
- Formats for immediate use

### Smart Follow-up
"Which action items are overdue based on the dates mentioned?"

## Part 4: Living Documentation (2 min)

### Cross-Reference Demo
```bash
# Prompt
"Our product-spec-for-review.md mentions several success metrics. 
Check if these align with:
1. The goals in our business-info.md
2. The KPIs mentioned in recent meeting notes
3. What customers actually said they measure
Flag any misalignments"
```

**This Shows:**
- Documents aren't siloed
- Claude maintains context across files
- Catches inconsistencies humans miss
- Ensures alignment

## Part 5: Real-Time Synthesis (2 min)

### Live Information Gathering
"Let's say the CEO just asked for a quick status on mobile feature demand"

```bash
# Prompt
"I need a 3-bullet Slack update on mobile feature demand. Check:
- Customer interviews for mobile mentions
- Meeting notes for mobile discussions  
- PRDs for planned mobile work
Keep it under 50 words"
```

**Result Example:**
"📱 Mobile Update:
• 3/3 interviewed customers cited mobile as critical blocker
• Team committed to mobile PWA in Q1 (Sprint 24-26)
• Would unblock $2.4M pipeline per sales team"

## Part 6: Creating New From Old (1 min)

### Template Generation
```bash
# Prompt
"Based on our 3 example PRDs, create a reusable PRD template that captures the common structure. Include placeholders and guidance comments"
```

**Value Prop:**
- Learn from existing patterns
- Standardize without starting fresh
- Build institutional knowledge

## Key Messages Throughout

1. **Multiplier Effect**: "Claude doesn't just read files - it synthesizes insights across them"

2. **Context Awareness**: "Your documents become Claude's knowledge base"

3. **Time Savings**: "Tasks that took hours now take minutes"

4. **Quality Improvement**: "Never miss important details scattered across documents"

## Interactive Moments

Ask audience:
- "What documents do you spend most time cross-referencing?"
- "What patterns do you look for in customer feedback?"
- "How do you currently track action items?"

Then show how Claude could help with their specific case.

## Common Questions

**Q: "Can Claude update multiple files at once?"**
A: "Yes! You can ask it to update action items across all relevant docs"

**Q: "What about sensitive information?"**
A: "Claude only sees what's in your local files. You control what's included"

**Q: "How accurate is the synthesis?"**
A: "Very accurate for factual extraction. Always verify strategic conclusions"

## Troubleshooting

If synthesis seems incomplete:
- Check all files are in specified folders
- Ask Claude to list what files it found first
- Be more specific about what to look for

## Transition to Next Demo
"You've seen how Claude works with existing files. Next, let's explore Planning Mode for more complex workflows..."