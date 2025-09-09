# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a demo environment for showcasing Claude Code capabilities to product managers. The main focus is demonstrating file operations, MCPs (Model Context Protocol), agents, and PM workflows using a Vercel AI Chatbot as the example project.

## Demo Structure

- `DEMO` - Contains the complete demo script and timing for the PM presentation
- The actual codebase will be the Vercel AI Chatbot repository when cloned

## Demo Flow

1. Basic file operations (read, search, create documentation)
2. MCP integrations (Google Drive, Slack, GitHub, SlideSpeak) 
3. Agent workflows (research-synthesizer, business-analyst, dev-impl, pm-orchestrator)
4. CCPM requirements management
5. Implementation of persona-based suggested comments feature
6. PM orchestration (status updates, PR creation, slide generation)

## Key Demo Commands

```bash
# Clone the demo project
git clone https://github.com/vercel/ai-chatbot.git
cd ai-chatbot
npm install
npm run dev

# Start Claude Code
claude dev
```

## Demo Personas

- **Mentor**: Supportive, encouraging tone
- **Support Pro**: Direct, solution-focused responses  
- **Skeptical Engineer**: Critical, detail-oriented questions

## CCPM Integration

The demo uses CCPM (Claude Code Project Management) for requirements workflow:
- `/pm:prd-new` - Create new PRD
- `/pm:epic-decompose` - Break down into tasks
- `/pm:status` - Quick project snapshot
- `/pm:standup` - Generate standup notes

## Target Feature

Persona-based suggested comments panel that:
- Sits beside the chat composer
- Updates suggestions based on selected persona
- Inserts text into composer when clicked
- Requires no backend changes (UI-only demo)