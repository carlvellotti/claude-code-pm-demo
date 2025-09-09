# Demo Script 5: Planning Mode - Think Before You Act

## Overview
Demonstrate Planning Mode, which allows Claude to create comprehensive plans before executing, perfect for complex PM tasks.

## Part 1: Introduction to Planning Mode (1 min)

### Set the Context
"Sometimes you want to think through an approach before diving in. That's what Planning Mode is for."

### Key Benefit
"Instead of Claude immediately starting work, it creates a detailed plan you can review and adjust."

## Part 2: Basic Planning Mode Demo (3 min)

### Enable Planning Mode
```bash
# In Claude interface, mention you can toggle modes
"I'm going to switch to Planning Mode for our next task"
```

### Complex Task Example
```bash
# Prompt
"I need to prepare for our Q2 planning session. This involves:
1. Analyzing all Q1 customer feedback
2. Reviewing current PRD status
3. Identifying top opportunities
4. Creating a prioritized roadmap
5. Preparing a presentation deck outline

Create a plan for how to approach this"
```

**What Claude Does:**
- Breaks down the task into steps
- Identifies which files to read
- Suggests analysis approach
- Proposes output structure
- **Asks for approval before starting**

### Review and Refine
"This plan looks good, but let's add competitive analysis to step 3"

**Key Point:** You can refine the plan before execution begins

## Part 3: Planning Mode for Research (3 min)

### Research Task
```bash
# Prompt  
"I want to understand our notification overload problem deeply. Plan how to:
1. Analyze all mentions across customer interviews
2. Check meeting notes for internal discussions
3. Review any existing PRDs that might address this
4. Research competitor solutions
5. Create a recommendation document"
```

**Planning Output Shows:**
- Which files to analyze and in what order
- What patterns to look for
- How to structure findings
- Time estimates for each step

### The Power of Planning
"Before Claude spends time analyzing, we can:
- Adjust the scope
- Add missing sources
- Clarify output format
- Set priorities"

## Part 4: Collaborative Planning (2 min)

### Scenario
"My design lead asked me to figure out our mobile strategy"

```bash
# Prompt
"Create a plan for developing our mobile strategy that I can share with the design lead for feedback. Include:
- Stakeholder input needed
- Research required  
- Timeline estimate
- Deliverables
- Success criteria"
```

**Value Demonstration:**
- Plan becomes alignment tool
- Catches missing steps early
- Sets clear expectations
- Can be shared before work begins

### Stakeholder Integration
"I can now share this plan with design and engineering before we invest time in the analysis"

## Part 5: Planning vs Auto Mode (2 min)

### Quick Comparison

**Auto Mode:**
```bash
"Summarize customer feedback about templates"
```
- Claude immediately reads files and creates summary

**Planning Mode:**
```bash
"Create a comprehensive template strategy based on all available data"
```
- Claude first outlines approach
- You review and approve
- Then execution begins

### When to Use Each

| Use Planning Mode When: | Use Auto Mode When: |
|------------------------|-------------------|
| Task is complex/multi-step | Task is straightforward |
| You need stakeholder buy-in | You know exactly what you want |
| Approach isn't clear | Path is obvious |
| Mistakes would be costly | Quick iteration is fine |

## Part 6: Advanced Planning Example (1 min)

### Complex Workflow
```bash
# Prompt
"Plan a complete feature development cycle for smart notifications:
1. Research phase (interviews, competition)
2. Requirements phase (PRD, technical spec)
3. Design phase (wireframes, user flows)
4. Communication phase (stakeholder updates, wiki)
Include which tools and people to involve at each stage"
```

**This Demonstrates:**
- Planning beyond just document creation
- Incorporating human workflows
- Thinking about dependencies
- Full lifecycle consideration

## Key Messages

1. **Think First**: "Planning mode prevents wasted effort on wrong approaches"

2. **Stakeholder Alignment**: "Plans can be shared and refined before work begins"

3. **Complex Task Management**: "Break down overwhelming projects into clear steps"

4. **Risk Reduction**: "Catch missing requirements or data before starting"

## Interactive Elements

Ask audience:
- "What complex tasks do you struggle to start?"
- "Where would planning help your workflow?"

Then create a live plan for their suggestion.

## Common Questions

**Q: "Can I save and reuse plans?"**
A: "Yes! Plans can be saved as templates for recurring tasks"

**Q: "How detailed are the plans?"**
A: "You control the level - ask for high-level or step-by-step"

**Q: "Can I partially execute a plan?"**
A: "Absolutely. Approve only the steps you want to run"

## Pro Tips

1. **Plan Templates**: "Save good plans as templates for recurring tasks"

2. **Time Estimates**: "Ask Claude to estimate time for each step"

3. **Risk Identification**: "Request Claude identify risks in the plan"

4. **Checkpoint Setting**: "Build in review points for long plans"

## Troubleshooting

If plan seems too generic:
- Provide more context about constraints
- Specify desired output format
- Reference similar successful projects

If plan is overwhelming:
- Ask for phases instead of all steps
- Request priority ordering
- Focus on MVP approach first

## Transition to Next Demo
"Planning Mode helps you think through complex tasks. Next, let's see how MCPs (Model Context Protocols) connect Claude to external tools..."