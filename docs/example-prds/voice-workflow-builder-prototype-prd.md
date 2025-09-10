# PRD: Voice Workflow Builder Prototype

**Document Status:** Draft  
**Last Updated:** January 2025  
**Author:** Demo Team  
**Purpose:** Rapid prototype for Claude Code capabilities demo

## Overview

Build a minimal voice-driven interface that allows users to create automation workflows using natural speech. This prototype demonstrates GPT Realtime API integration for workflow automation use cases.

## Core Features

### 1. Voice Conversation Flow
- User clicks "Start Building" button
- System asks: "What do you want to build?" or "What are the steps of your automation?"
- User describes their automation steps
- System follows up: "Okay, how does the user go from step one to step two and step two to step three?"
- User explains the transitions between steps

### 2. Dynamic Flow Chart Generation
- As user explains transitions, system builds visual flowchart in real-time
- Boxes represent workflow steps
- Arrows show transitions with labels based on user's explanation
- Example: Step 1 → "when approved" → Step 2 → "if rejected" → Step 3

### 3. Interactive Conversation
- Natural back-and-forth dialogue
- System asks clarifying questions as needed
- Voice responses processed through GPT Realtime API
- Visual updates happen live during conversation

### 4. Final Workflow Display
- Complete flowchart showing all steps and transitions
- Clear labels on arrows explaining how steps connect
- Simple completion state when conversation ends

## Simple UI Requirements

### Layout
- Clean, single-page interface
- Large "Start Building" button (primary CTA)
- Live flowchart canvas area
- Voice conversation status indicator

### Components Needed
- "Start Building" button to initiate conversation
- Voice activity indicator (listening/speaking states)
- Dynamic flowchart with boxes and labeled arrows
- Live conversation transcript (optional)
- Flowchart canvas that updates in real-time

## Technical Integration

### GPT Realtime API
- WebRTC connection for real-time speech
- Session configuration for workflow context
- Voice activity detection
- Speech-to-workflow interpretation
- CHATGPT_API_KEY configured in .env file

### Basic Tech Stack
- HTML5 + vanilla JavaScript (keep it simple)
- GPT Realtime API integration
- Basic CSS for styling
- No complex frameworks needed

## Demo Success Criteria

### Functional Requirements
- User clicks "Start Building" and conversation begins
- System asks initial question and follows up about step transitions
- Flowchart builds dynamically as user explains connections
- Arrows display clear labels explaining step transitions
- Complete workflow visualization at end of conversation

### Technical Requirements
- Voice input works reliably
- GPT Realtime API integration functional
- Responsive on desktop and mobile
- No crashes or errors during demo

## Out of Scope (Keep Simple)
- Complex workflow logic
- Database integration
- User authentication
- Workflow execution
- Advanced editing features
- Multiple workflow types

## Implementation Notes

This is a prototype for demonstration purposes. Focus on:
1. Clean, working voice interface
2. Clear visual feedback
3. Smooth user experience
4. Reliable GPT Realtime integration

Success = A working demo that shows the potential of voice-driven workflow creation.