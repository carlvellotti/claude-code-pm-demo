# Demo Script 3: CLAUDE.md - Teaching Claude Your Preferences

## Overview
Show how CLAUDE.md acts as persistent instructions for Claude Code, making it understand your project's specific needs and conventions.

## Part 1: Introduction (1 min)

### Opening Hook
"What if Claude could remember your preferences and rules across every conversation? That's what CLAUDE.md does."

### Quick Explanation
"CLAUDE.md is like a team onboarding doc for Claude. It teaches Claude your project's conventions, rules, and preferences."

## Part 2: Exploring Existing CLAUDE.md (2 min)

### Show Current File
"Let's look at the CLAUDE.md in this project"

```bash
# Prompt to Claude
"Can you show me what's in our CLAUDE.md file and explain how you use it?"
```

**Expected Response:**
- Claude reads the file
- Explains each section's purpose
- Mentions it references this automatically

### Key Points to Highlight
- "Claude reads this file at the start of every session"
- "It's like setting preferences that stick"
- "Project-specific, not global"

## Part 3: Real Examples (3 min)

### Show Examples File
"Let's look at different ways teams use CLAUDE.md"

```bash
# Prompt
"Read the claude-md-examples.md file and show me the PM-focused example"
```

### Demonstrate Impact

1. **Without CLAUDE.md:**
   ```
   "Create a new PRD for user authentication"
   ```
   Result: Generic PRD format

2. **With CLAUDE.md:**
   ```
   "Create a new PRD for user authentication"
   ```
   Result: Follows company template, includes required sections, uses correct tone

### Live Edit Demo
"Let's add a new rule and see it work immediately"

```bash
# Prompt
"Add a rule to CLAUDE.md that all PRDs must include a competitive analysis section"
```

Then test:
```bash
"Create a quick PRD outline for a notification system"
```

Show how it now includes competitive analysis automatically.

## Part 4: Common PM Rules (2 min)

### Useful CLAUDE.md Patterns for PMs

1. **Document Standards**
   ```markdown
   ## Document Rules
   - All PRDs must include success metrics
   - User stories in Given/When/Then format
   - Always link to relevant research
   ```

2. **Communication Preferences**
   ```markdown
   ## Output Preferences
   - Summarize long documents to 1 page
   - Use bullet points over paragraphs
   - Include Slack-ready summaries
   ```

3. **Workflow Rules**
   ```markdown
   ## Workflow
   - Check for existing docs before creating new
   - Always save PRDs in /docs/prds/
   - Tag documents with status (draft/review/approved)
   ```

### Interactive Demo
"What rules would help your workflow?"

Get audience suggestion, then:
```bash
# Add their suggestion
"Add a rule to CLAUDE.md that [audience suggestion]"
```

## Part 5: Advanced Uses (2 min)

### Show Power Features

1. **Integration Instructions**
   ```markdown
   ## External Tools
   - Format Jira tickets with project tag [STRM-XXX]
   - Include Figma links for all UI changes
   - Reference Slack threads with permalink
   ```

2. **Team Conventions**
   ```markdown
   ## Team Standards
   - PM: Sarah owns roadmap decisions
   - Design: Jessica approves all UX changes
   - Eng: Marcus estimates all technical work
   ```

3. **Forbidden Actions**
   ```markdown
   ## Never Do This
   - Don't delete files without confirming
   - Don't share customer names in examples
   - Don't commit changes without review
   ```

## Part 6: Best Practices (1 min)

### Quick Tips
1. "Start simple - add rules as you discover needs"
2. "Make it scannable - Claude reads it every time"
3. "Be specific - 'use bullet points' not 'be concise'"
4. "Update regularly - it's a living document"

### Team Collaboration
"Your whole team can contribute to CLAUDE.md"
- Engineers add technical conventions
- Designers add style guidelines  
- PMs add document standards

## Key Messages

1. **Persistent Memory**: "Unlike chat systems that forget, CLAUDE.md remembers"

2. **Team Alignment**: "Everyone using Claude gets same standards"

3. **Evolving Document**: "Grows with your project needs"

4. **No Repeated Instructions**: "Tell Claude once, applies forever"

## Common Questions

**Q: "Can I have multiple CLAUDE.md files?"**
A: "One per project, but you can include different sections for different needs"

**Q: "What if Claude ignores a rule?"**
A: "Be more specific or put important rules at the top"

**Q: "Can CLAUDE.md reference other files?"**
A: "Yes! You can tell Claude to check other documents for context"

## Live Q&A Prompts

If someone asks about specific use case:
```bash
"Show me a CLAUDE.md example for [their use case] from the examples file"
```

If someone wants to see rule priority:
```bash
"If I have conflicting rules in CLAUDE.md, which takes precedence?"
```

## Transition to Next Demo
"Now that Claude knows your preferences through CLAUDE.md, let's see how it can work with your existing documents and data..."