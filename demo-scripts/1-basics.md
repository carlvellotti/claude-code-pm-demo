# Demo Script 1: Claude Code Basics & Multi-Agent Review

## Overview
Show fundamental Claude Code capabilities including file operations and the powerful multi-agent document review feature.

## Part 1: Getting Started (2 min)

### Setup
```bash
# In terminal
cd /path/to/PG-Demo
claude dev
```

### Opening Prompt
"Welcome Claude! Please give me a quick overview of what files and folders you can see in this project."

**Expected Output:**
- Claude lists directory structure
- Highlights key folders like docs, data, demo-scripts

### Basic File Operations
"Can you read the business-info.md file and tell me what company this demo is about?"

**Talking Points:**
- Claude can read any file in your project
- Maintains context across conversations
- Respects file permissions and access

## Part 2: Multi-Agent Document Review (5 min)

### Setup the Scenario
"I have a product specification document that needs review from multiple perspectives before we finalize it. Can you help?"

### The Power Prompt
"Please create three separate agents with these personas:
1. **'exec'** - A C-level executive focused on business impact, ROI, and strategic alignment
2. **'engineer'** - A senior engineer concerned with technical feasibility, performance, and implementation complexity  
3. **'clueless user'** - A non-technical end user focused on usability, clarity, and whether the feature solves their actual problems

Have each agent independently review the file 'docs/product-spec-for-review.md' and then compile all their feedback into a single comprehensive review document. Save the compiled review as 'reviews/smart-notification-multi-review.md'."

**What Happens:**
- Claude spins up three separate agent instances
- Each reviews the document from their unique perspective
- All feedback is synthesized into one organized document

**Expected Feedback Examples:**
- **Exec**: "ROI calculations missing. Need competitive advantage analysis."
- **Engineer**: "ML model training requirements underspecified. Data pipeline dependencies unclear."
- **User**: "Too much jargon. What does 'channel optimization' mean for me?"

### Follow-up Enhancement
"This is great! Now can you create a summary table showing which feedback items all three personas agreed on versus unique concerns from each?"

## Part 3: Practical File Management (2 min)

### Search Demonstration
"Search across all our customer interviews for mentions of 'mobile' and summarize the pain points."

**Talking Points:**
- Claude can search across multiple files
- Synthesizes findings, not just list matches
- Understands context, not just keywords

### Parallel Research Task
"I need you to research the latest flagship specs for Apple, Google, and Samsung phones. Create individual markdown files for each in a new folder called 'data/flagship-specs'. Work on all three in parallel."

**What to Emphasize:**
- Claude creates folders automatically
- Parallel processing for efficiency
- Structured output in separate files

## Key Messages Throughout

1. **File Access**: "Claude has full read/write access to your project, making it like a team member who can see everything you can"

2. **Multi-Agent Power**: "Instead of getting one perspective, you can instantly get diverse viewpoints on any document"

3. **Context Awareness**: "Claude remembers what we've discussed and understands relationships between files"

4. **Efficiency**: "Tasks that might take hours of manual work happen in seconds"

## Common Questions to Address

**Q: "Is this just ChatGPT with file access?"**
A: "No, it's much more. Claude Code understands your project structure, can perform complex multi-file operations, and maintains context across your entire codebase. Plus features like multi-agent reviews are unique to Claude Code."

**Q: "How does multi-agent work technically?"**
A: "Each agent is a separate Claude instance with its own persona and instructions. They work independently then Claude synthesizes their outputs."

**Q: "Can I customize the agent personas?"**
A: "Absolutely! These three are just examples. You can create agents for any perspective - legal reviewer, UX designer, customer success, etc."

## Troubleshooting

If multi-agent review seems slow:
- Mention it's processing three independent reviews
- Show the terminal to demonstrate activity

If file creation fails:
- Check permissions with `ls -la`
- Ensure we're in the right directory

## Transition to Next Demo
"Now that you've seen how Claude can work with files and provide multiple perspectives, let's look at how different tools like IDEs and Obsidian can visualize this work..."