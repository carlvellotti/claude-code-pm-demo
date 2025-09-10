# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a demo environment for showcasing Claude Code capabilities to product managers. The main focus is demonstrating file operations, MCPs (Model Context Protocol), agents, and PM workflows. The demo is structured to show end-to-end product development from research to implementation using a 3-agent workflow.

## Repository Architecture

### Core Structure
- `DEMO*` files - Complete demo scripts, run-of-show, and preparation materials
- `demo-scripts/` - Individual demo modules (1-7) with specific focus areas
- `docs/` - Business context, writing styles, example PRDs, and architecture guides
- `data/` - Customer interviews and meeting transcripts for synthesis exercises
- `slides/` - Presentation materials for stakeholder communications

### Key Demo Components
- **Business Context** (`docs/business-info.md`) - StreamlineAI company profile and strategic context
- **Writing Styles** (`docs/writing-styles.md`) - Technical, user-friendly, and internal-audience styles
- **Example PRDs** (`docs/example-prds/`) - Mobile workflow editor, AI suggestion engine, quick start templates
- **Customer Data** (`data/customer-interviews/`, `data/meeting-transcripts/`) - Interview synthesis and analysis materials

## Demo Flow and Timing (25-30 minutes)

1. **Basic file operations** (2-3 min) - Read, search, create documentation
2. **MCP testing** (3-4 min) - Perplexity search/reasoning, Reddit community insights
3. **Research Agent** (5-6 min) - Pain point synthesis using Perplexity MCP
4. **Requirements & Documentation Agent** (5-6 min) - PRD creation using CCPM, Google Drive, Slack MCPs
5. **Implementation Agent** (5-6 min) - Prototype development and testing
6. **Buffer time** (4-5 min) - Narration and Q&A

## Key Demo Commands

### Initial Setup
```bash
# Clone the actual demo project (Vercel AI Chatbot)
git clone https://github.com/vercel/ai-chatbot.git
cd ai-chatbot
npm install
npm run dev

# Start Claude Code
claude dev
```

### CCPM Requirements Management
```bash
# Initialize CCPM in project
curl -sSL https://raw.githubusercontent.com/automazeio/ccpm/main/ccpm.sh | bash
# Then in Claude REPL: /pm:init
```

### MCP Commands (Available in Demo)
- **Perplexity MCP** - `mcp__perplexity-mcp__perplexity_ask` and `mcp__perplexity-mcp__perplexity_reason`
- **Reddit MCP** - `mcp__reddit__get_subreddit_hot_posts`, `mcp__reddit__get_post_content`
- **Google Drive, Slack, GitHub** - Document storage, team communication, PR creation

## 3-Agent Workflow Architecture

### Research Agent
- **Tools**: Perplexity MCP, Reddit MCP, Read, Edit
- **Purpose**: Search and analyze topics, synthesize pain points
- **Output**: 400-500 word pain points document with TL;DR, key issues, quotes, market signals

### Requirements & Documentation Agent  
- **Tools**: CCPM MCP, Google Drive MCP, Slack MCP, Read, Edit
- **Purpose**: Convert research into formal requirements and documentation
- **Output**: Structured PRD, stored documentation, team communications

### Implementation Agent
- **Tools**: Read, Edit, Bash, Grep, Glob, Git
- **Purpose**: Build working prototypes from requirements
- **Output**: Minimal viable implementation demonstrating core functionality

## Demo Personas and Writing Styles

### Demo Personas
- **Mentor**: Supportive, encouraging tone for guidance scenarios
- **Support Pro**: Direct, solution-focused responses for troubleshooting  
- **Skeptical Engineer**: Critical, detail-oriented questions for review scenarios

### Writing Styles (see `docs/writing-styles.md`)
- **Technical**: Precise language, specifications, implementation details
- **User-Friendly**: Conversational, benefit-focused, minimal jargon
- **Internal-Audience**: Strategic context, business rationale, cross-functional language

## Demo Best Practices

### File Operations
- Always use existing demo data files for synthesis exercises
- Reference business context from `docs/business-info.md` for realistic scenarios
- Use customer interview data for pain point analysis

### MCP Demonstrations
- Test Perplexity connection first with simple search
- Use Reddit MCP for community insight gathering
- Show combined MCP workflows for end-to-end automation

### Agent Workflows
- Always run agents in sequence: Research → Requirements → Implementation
- Use realistic business scenarios from provided data
- Keep implementations surgical and demo-focused

## Troubleshooting and Contingencies

### MCP Issues
- If Drive or Slack MCP fails, paste text manually and continue
- Reddit MCP can substitute for some Perplexity functionality
- Always have manual fallback options prepared

### Implementation Issues
- For TypeScript/build failures: "diagnose and apply minimal fix"
- Keep changes surgical and focused on working demo
- Prioritize demonstration over perfect code

### Timing Issues
- Skip slide generation if running short
- Focus on core 3-agent workflow over peripheral features
- Have backup prompts ready in `DEMO-PROMPTS.md`

## Success Metrics for Demo

- **Time Savings**: Demonstrate 12+ hours → 20 minutes workflow compression
- **Quality**: Professional outputs following best practices
- **Integration**: Connected tool ecosystem functionality
- **Accessibility**: Show PM capabilities without coding requirements

## Best Practices for Version Control

- Never commit anything unless confirming first