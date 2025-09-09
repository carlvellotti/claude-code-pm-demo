# Ready-to-Use Demo Prompts

## Multi-Persona Review Prompt

```
Please create three separate agents with these personas:
1. 'exec' - A C-level executive focused on business impact, ROI, and strategic alignment
2. 'engineer' - A senior engineer concerned with technical feasibility, performance, and implementation complexity  
3. 'clueless user' - A non-technical end user focused on usability, clarity, and whether the feature solves their actual problems

Have each agent independently review the file 'docs/product-spec-for-review.md' and then compile all their feedback into a single comprehensive review document. Save the compiled review as 'reviews/smart-notification-multi-review.md'.
```

## Customer Interview Analysis

```
Please analyze all customer interviews in data/customer-interviews/ and:
1. Identify the top 3 pain points mentioned
2. Find quotes about mobile access needs
3. Count how many mentioned template requirements
4. Create actionable recommendations
Save as 'research/customer-synthesis.md'
```

## Meeting Intelligence Extraction

```
Read all meeting transcripts in data/meeting-transcripts/ and:
1. Extract all action items by person
2. Identify decisions made
3. Flag conflicts between meetings
Create a consolidated tracker
```

## Perplexity Research

```
Use Perplexity to research current best practices for reducing notification fatigue in B2B SaaS products. Focus on 2024-2025 trends and cite sources.
```

## Reddit Research

```
Use Reddit MCP to find recent discussions in r/ProductManagement about PRD templates and documentation burden.
```

## Planning PRD Agent

```
Use the planning-prd-agent from https://www.subagents.cc/agents/planning-prd-agent to create a comprehensive PRD for our Smart Notification System based on the customer pain points we discovered.
```

## Quick Demos

### CLAUDE.md Test
```
Add a rule to CLAUDE.md that all PRDs must include a competitive analysis section
```

Then:
```
Create a quick PRD outline for a notification system
```

### Parallel Research
```
Research the latest flagship specs for Apple, Google, and Samsung phones. Create individual markdown files for each in a new folder called 'data/flagship-specs'. Work on all three in parallel.
```

### Cross-Reference Check
```
Our product-spec-for-review.md mentions several success metrics. Check if these align with:
1. The goals in our business-info.md
2. The KPIs mentioned in recent meeting notes
3. What customers actually said they measure
Flag any misalignments
```

### Slack Summary
```
I need a 3-bullet Slack update on mobile feature demand. Check:
- Customer interviews for mobile mentions
- Meeting notes for mobile discussions  
- PRDs for planned mobile work
Keep it under 50 words
```

## End-to-End Mobile Strategy Demo

```
1. Analyze all mentions of mobile in our interviews and meetings
2. Research competitor mobile offerings using Perplexity  
3. Create a mobile strategy PRD using our template
4. Generate a 3-bullet executive summary for Slack
```

## Backup Prompts

### If MCPs fail:
```
Analyze our local customer interviews for insights about notification fatigue and create recommendations
```

### If file creation fails:
```
Show me what a multi-perspective review would look like for our notification system spec
```

### Quick value demo:
```
How much time would the tasks we just completed typically take if done manually?
```