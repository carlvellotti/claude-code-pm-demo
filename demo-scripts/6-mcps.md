# Demo Script 6: MCPs - Connecting Claude to Your Tools

## Overview
Demonstrate how Model Context Protocols (MCPs) extend Claude's capabilities by connecting to external tools like Perplexity, Reddit, Slack, and Google Drive.

## Part 1: MCP Introduction (1 min)

### Simple Explanation
"MCPs are like plugins that give Claude superpowers. They let Claude talk to your other tools."

### Key Concept
"Think of MCPs as secure bridges between Claude and external services - each with specific permissions you control."

### Current Setup
```bash
# Show installed MCPs
"Which MCPs do I have connected?"
```

## Part 2: Perplexity MCP Demo (3 min)

### Research Task
```bash
# Prompt
"Use Perplexity to research current best practices for reducing notification fatigue in B2B SaaS products. Focus on 2024-2025 trends."
```

**What Happens:**
- Claude uses Perplexity for web search
- Gets current information beyond training data
- Synthesizes findings
- Cites sources

### Advanced Perplexity Usage
```bash
# Prompt
"Use Perplexity's reasoning capability to analyze the trade-offs between push notifications, email digests, and in-app notification centers for our use case"
```

**Value Points:**
- Real-time information
- Reasoning about complex decisions
- No manual web searching needed

## Part 3: Reddit MCP Demo (3 min)

### Pain Point Research
```bash
# Prompt
"Use Reddit MCP to find recent discussions in r/ProductManagement about PRD templates and documentation burden. Look for specific pain points and solutions people have tried."
```

**Demonstration:**
- Claude searches specific subreddit
- Pulls actual user discussions
- Identifies patterns in complaints
- Extracts practical solutions

### Deeper Dive
```bash
# Prompt
"Get the full thread content for the top 3 most relevant posts about PRD complexity"
```

**This Shows:**
- Detailed community insights
- Real user language and pain
- Unfiltered feedback

## Part 4: Slack MCP Demo (2 min)

### Status Update
```bash
# Prompt
"Post an update to our #product-team Slack channel:
- Completed analysis of Q1 customer interviews  
- Top 3 priorities identified: mobile, templates, notifications
- PRDs in progress, review needed by Friday
- Tag @design-team for mobile input"
```

**Key Benefits:**
- Direct posting from Claude
- No copy-paste needed
- Maintains context
- Can read responses back

### Integration Example
"After analyzing customer feedback, immediately share insights with the team"

## Part 5: Google Drive MCP (2 min)

### Document Management
```bash
# Prompt
"Upload the customer interview synthesis we created to our 'Product Research' folder in Google Drive. Make it viewable by anyone with the link."
```

**Workflow Enhancement:**
- Local analysis, cloud storage
- Team collaboration enabled
- Version control maintained
- Access management handled

### Retrieval Demo
```bash
# Prompt
"Pull down the latest roadmap document from our Product Planning folder and compare it with our current PRD priorities"
```

## Part 6: Combined MCP Workflow (3 min)

### End-to-End Demo
"Let me show you the power of combining MCPs"

```bash
# Prompt
"Execute a competitive analysis workflow:
1. Use Perplexity to research our top 3 competitors' recent product updates
2. Check Reddit for user opinions about these features
3. Create a competitive analysis document
4. Upload to Google Drive in our Research folder
5. Post a summary to #product-team on Slack with key takeaways"
```

**This Demonstrates:**
- Multiple MCPs working together
- Complex workflows automated
- Real-time external data
- Seamless tool integration

## Part 7: MCP Possibilities (1 min)

### Other Available MCPs
- **GitHub**: Create PRs, manage issues
- **Linear/Jira**: Create and update tickets  
- **Notion**: Sync documentation
- **Email**: Send updates
- **Calendar**: Schedule meetings
- **Database**: Query data directly

### Custom MCPs
"Your engineering team can build custom MCPs for internal tools"

## Key Messages

1. **Extended Reach**: "Claude isn't limited to local files - it can work with all your tools"

2. **Workflow Automation**: "Connect the dots between different platforms automatically"

3. **Real-Time Data**: "Get current information, not just training data"

4. **Permission Control**: "You decide what Claude can access and do"

## Common Questions

**Q: "Is this secure?"**
A: "Each MCP requires authentication and has limited, specific permissions you grant"

**Q: "Can Claude read all my Slack messages?"**
A: "No, only channels you explicitly grant access to"

**Q: "What if an MCP fails?"**
A: "Claude tells you and can often work around it or retry"

**Q: "Can I use multiple accounts?"**
A: "Yes, you can connect different accounts for different purposes"

## Interactive Demo

"What tool integration would most help your workflow?"

Based on answer, either:
- Show that MCP if available
- Explain how custom MCP could work
- Suggest alternative approach

## Pro Tips

1. **Start Small**: "Connect one MCP at a time to learn"

2. **Permission Minimization**: "Only grant necessary access"

3. **Workflow Design**: "Think about tool chains, not individual tools"

4. **Error Handling**: "MCPs can fail - have Claude plan for this"

## Troubleshooting

If MCP doesn't respond:
- Check connection in Claude settings
- Verify authentication is current
- Try simpler request first
- Show manual fallback option

## Transition to Final Demo
"You've seen how MCPs connect Claude to external tools. Finally, let's look at how specialized sub-agents can handle complex domain-specific tasks..."