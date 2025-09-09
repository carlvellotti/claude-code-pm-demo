# DEMO RUN OF SHOW: Claude Code for Product Managers

**Total Duration:** 25-30 minutes  
**Audience:** Product Managers  
**Focus:** Non-coding use cases, research, documentation, workflow automation

## Pre-Demo Checklist

### Environment Setup
- [ ] Clone fresh Vercel AI Chatbot repo
- [ ] `claude dev` running in PG Demo folder
- [ ] Obsidian open with PG Demo as vault  
- [ ] VS Code/Cursor ready as backup IDE
- [ ] Terminal visible for transparency

### File Verification
- [ ] All demo files created and in place
- [ ] Customer interviews ready
- [ ] Meeting transcripts loaded
- [ ] Example PRDs available
- [ ] CLAUDE.md configured

### MCP Status
- [ ] Perplexity MCP connected
- [ ] Reddit MCP authenticated
- [ ] Slack workspace connected (optional)
- [ ] Google Drive authenticated (optional)

### Backup Plans Ready
- [ ] Screenshots of expected outputs
- [ ] Pre-written prompts in notes
- [ ] Fallback demos identified

---

## Opening (1 minute)

### Hook
"What if you could have an AI assistant that truly understands your entire product context - every interview, every PRD, every meeting note - and could help you synthesize insights in seconds instead of hours?"

### Introduction
"I'm going to show you Claude Code - not for writing code, but for supercharging your PM workflow. Think of it as your intelligent second brain that never forgets a detail."

### Set Expectations
"In the next 25 minutes, you'll see how to:
- Analyze customer feedback across dozens of interviews
- Create PRDs that follow your exact standards
- Get multiple perspectives on any document instantly
- Connect to your favorite tools
- Automate repetitive PM tasks"

---

## Section 1: Basics & Multi-Agent Review (5 minutes)

### 1.1 Quick Introduction (1 min)
```bash
# In terminal
cd /Users/carl/PG Demo
claude dev
```

**Prompt 1:**
"Welcome Claude! Please give me a quick overview of what files and folders you can see in this project."

**Talk Track:**
- "Claude can see and work with all your project files"
- "It's like having a team member who has read everything"

### 1.2 Multi-Agent Document Review (4 min)

**Setup:**
"I have a product spec that needs review before we finalize it. Let me show you something powerful."

**The Power Prompt:**
```
Please create three separate agents with these personas:
1. 'exec' - A C-level executive focused on business impact, ROI, and strategic alignment
2. 'engineer' - A senior engineer concerned with technical feasibility, performance, and implementation complexity  
3. 'clueless user' - A non-technical end user focused on usability, clarity, and whether the feature solves their actual problems

Have each agent independently review the file 'docs/product-spec-for-review.md' and then compile all their feedback into a single comprehensive review document. Save the compiled review as 'reviews/smart-notification-multi-review.md'.
```

**While it runs:**
- "Each persona brings unique perspective"
- "Catches things you might miss"
- "Like having instant focus group"

**Show result:**
- Open the compiled review
- Highlight contrasting viewpoints
- "This took 30 seconds vs hours of meetings"

---

## Section 2: File Visualization (3 minutes)

### 2.1 Obsidian for PMs (1.5 min)

**Action:** Open Obsidian

**Talk Track:**
- "See your product docs as connected knowledge"
- Show graph view: "Visual relationships between PRDs, interviews, specs"
- "Perfect for non-technical team members"
- "Beautiful markdown rendering"

### 2.2 IDE Alternative (1.5 min)

**Action:** Quick flash of VS Code

**Talk Track:**
- "Developers might prefer traditional IDE"
- "Same files, different view"
- "Use what makes you productive"
- "Changes anywhere sync instantly"

**Key Message:** "Claude Code doesn't lock you into any tool"

---

## Section 3: CLAUDE.md Configuration (3 minutes)

### 3.1 Show Current File (1 min)

**Prompt:**
"Can you show me what's in our CLAUDE.md file and explain how you use it?"

**Talk Track:**
- "Like onboarding doc for Claude"
- "Remembers your preferences"
- "Team standards built in"

### 3.2 Live Edit Demo (2 min)

**Prompt:**
"Add a rule to CLAUDE.md that all PRDs must include a competitive analysis section"

Then test:
"Create a quick PRD outline for a notification system"

**Show:** How it now includes competitive analysis automatically

**Key Message:** "Tell Claude your preferences once, applies forever"

---

## Section 4: Working with Files (4 minutes)

### 4.1 Customer Interview Synthesis (2 min)

**Prompt:**
```
Please analyze all customer interviews in data/customer-interviews/ and:
1. Identify the top 3 pain points mentioned
2. Find quotes about mobile access needs
3. Count how many mentioned template requirements
4. Create actionable recommendations
Save as 'research/customer-synthesis.md'
```

**While running:**
- "Reading 3 interviews simultaneously"
- "Finding patterns humans might miss"
- "Quantifying qualitative data"

### 4.2 Meeting Intelligence (2 min)

**Prompt:**
```
Read all meeting transcripts in data/meeting-transcripts/ and:
1. Extract all action items by person
2. Identify decisions made
3. Flag conflicts between meetings
Create a consolidated tracker
```

**Value Points:**
- "Never lose an action item"
- "Accountability tracking"
- "Cross-meeting insights"

---

## Section 5: MCPs - External Tools (5 minutes)

### 5.1 Perplexity Research (2 min)

**Prompt:**
```
Use Perplexity to research current best practices for reducing notification fatigue in B2B SaaS products. Focus on 2024-2025 trends and cite sources.
```

**Talk Track:**
- "Real-time web research"
- "Current information beyond training"
- "Automated competitive intelligence"

### 5.2 Reddit Insights (1.5 min)

**Prompt:**
```
Use Reddit MCP to find recent discussions in r/ProductManagement about PRD templates and documentation burden.
```

**Points:**
- "Real user voice"
- "Unfiltered feedback"
- "Trend identification"

### 5.3 Workflow Integration (1.5 min)

**If Slack/Drive connected:**
```
Post a summary of our customer interview findings to #product-team Slack channel
```

**If not connected:**
"Imagine posting directly to Slack, updating Jira tickets, syncing with Google Drive - all from Claude"

**Key Message:** "Claude connects your entire tool ecosystem"

---

## Section 6: Specialized Agents (4 minutes)

### 6.1 Planning PRD Agent Intro (1 min)

**Prompt:**
"I want to use the planning-prd-agent from https://www.subagents.cc/agents/planning-prd-agent - what does this specialized agent do?"

**Talk Track:**
- "Pre-built PM expertise"
- "Industry best practices included"
- "Like having senior PM consultant"

### 6.2 Live PRD Creation (3 min)

**Prompt:**
```
Use the planning-prd-agent to create a comprehensive PRD for our Smart Notification System based on the customer pain points we discovered.
```

**While running:**
- "Notice the structure"
- "Asks clarifying questions"
- "Includes sections you might forget"
- "Incorporates our research automatically"

**Show result highlights:**
- Success metrics
- Risk mitigation
- Phasing approach
- "This quality in 15 minutes vs 3 hours"

---

## Section 7: Putting It All Together (3 minutes)

### 7.1 End-to-End Workflow

**Scenario:** "Your CEO just asked for a mobile strategy"

**Live Demo Chain:**
1. "Analyze all mentions of mobile in our interviews and meetings"
2. "Research competitor mobile offerings using Perplexity"  
3. "Create a mobile strategy PRD using our template"
4. "Generate a 3-bullet executive summary for Slack"

**This shows:**
- Research → Analysis → Documentation → Communication
- All in one flow
- Minutes not days

### 7.2 ROI Calculation

"Let's calculate the time saved today:"
- Multi-perspective review: 3 hours → 30 seconds
- Customer interview synthesis: 4 hours → 2 minutes
- PRD creation: 3 hours → 15 minutes
- Meeting action extraction: 2 hours → 1 minute

"That's 12 hours of work in under 20 minutes"

---

## Closing (2 minutes)

### Recap Key Benefits
1. "All your product context at Claude's fingertips"
2. "Multiple perspectives instantly"
3. "External research automated"
4. "Best practices built in"
5. "Your whole workflow connected"

### Call to Action
"This isn't about replacing PM judgment - it's about multiplying your impact. Spend less time on documentation mechanics, more time on strategy and customer connection."

### Next Steps
- "Try Claude Code free"
- "Start with one use case"
- "Join the PM community at [link]"
- "Resources at docs.anthropic.com"

### Final Hook
"What would you do with 10 extra hours per week?"

---

## Q&A Preparation (3-5 minutes)

### Anticipated Questions

**"How is this different from ChatGPT?"**
- Project context awareness
- Multi-file operations
- Tool integrations
- Specialized agents

**"Is my data secure?"**
- Local files only
- You control access
- MCP permissions explicit
- No training on your data

**"What's the learning curve?"**
- Start simple - basic prompts
- Build up to complex workflows
- Community templates available
- No coding required

**"Can my whole team use it?"**
- Yes - shared standards via CLAUDE.md
- Each person their own instance
- Consistent outputs

**"What about cost?"**
- Show pricing tiers
- Calculate ROI based on time saved
- Free tier available

---

## Emergency Pivots

### If Multi-Agent is Slow
"This is analyzing from three perspectives simultaneously - worth the few extra seconds"

### If MCP Fails
"Let me show you how it works with local files while we troubleshoot the connection"

### If File Creation Errors
"Let me demonstrate with existing files - same concept"

### If Time Runs Short
Skip to Planning PRD Agent - highest impact demo

---

## Post-Demo Follow-up

### Send Attendees
1. Recording of demo
2. Link to get started
3. Example CLAUDE.md files
4. PM-specific templates
5. Community links

### Success Metrics
- Sign-ups within 24 hours
- Questions indicating interest
- Requests for team demos
- Specific use case discussions

Remember: Focus on **outcomes over features**. Every demo element should connect to real PM pain points and time savings.