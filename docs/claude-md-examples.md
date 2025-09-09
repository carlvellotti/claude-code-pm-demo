# CLAUDE.md Examples and Best Practices

This document showcases different CLAUDE.md configurations and use cases to help you understand how to effectively guide Claude Code in your projects.

## Basic Structure Example

```markdown
# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview
Brief description of what this project does and its main purpose.

## Key Conventions
- Code style guidelines
- File naming patterns  
- Preferred libraries/frameworks
```

## Example 1: Web Application Project

```markdown
# CLAUDE.md

## Project Overview
This is a React-based web application using TypeScript and Material-UI.

## Conventions
- Use functional components with hooks (no class components)
- TypeScript strict mode is enabled
- Follow Airbnb ESLint rules
- Tests go in __tests__ folders using Jest

## File Structure
- /src/components - Reusable UI components
- /src/pages - Page-level components
- /src/utils - Helper functions
- /src/api - API integration layer

## Important Rules
- Never commit .env files
- Always run tests before suggesting commits
- Use semantic commit messages (feat:, fix:, docs:)

## Dependencies
- State management: Redux Toolkit
- Routing: React Router v6
- Forms: React Hook Form
- API calls: Axios with interceptors
```

## Example 2: Data Science Project

```markdown
# CLAUDE.md

## Project Context
Machine learning pipeline for customer churn prediction.

## Environment
- Python 3.9+ with poetry for dependency management
- Jupyter notebooks for exploration
- Scripts for production pipelines

## Conventions
- Follow PEP 8 style guide
- Type hints required for all functions
- Docstrings in NumPy format
- No print statements in production code

## Workflow Rules
- Raw data is immutable (never modify files in /data/raw)
- All data transformations must be reproducible
- Model experiments tracked in MLflow
- Results documented in /reports with visualizations

## Key Libraries
- pandas for data manipulation
- scikit-learn for modeling
- pytest for testing
- black for code formatting
```

## Example 3: API Development

```markdown
# CLAUDE.md

## Project Overview
RESTful API built with Node.js and Express.

## Critical Rules
- NEVER expose sensitive data in responses
- Always validate input with Joi schemas
- Use middleware for authentication
- Rate limiting enabled on all endpoints

## Code Standards
- Async/await over callbacks
- Error handling with custom error classes
- Logging with Winston
- API documentation with Swagger

## Testing Requirements
- Unit tests for all services
- Integration tests for endpoints
- Minimum 80% code coverage
- Load testing before deployment

## Security Practices
- Environment variables for secrets
- CORS properly configured
- Input sanitization mandatory
- SQL injection prevention via parameterized queries
```

## Example 4: Documentation Project

```markdown
# CLAUDE.md

## Purpose
Technical documentation for StreamlineAI platform.

## Writing Guidelines
- Active voice preferred
- Short sentences (max 25 words)
- One idea per paragraph
- Examples for every concept

## Structure Rules
- Each doc must have a TL;DR section
- Include "Prerequisites" when needed
- Step-by-step instructions with screenshots
- Troubleshooting section at the end

## Tone and Voice
- Professional but approachable
- Avoid jargon without explanation
- Use "you" to address the reader
- Encouraging and supportive tone

## Forbidden Practices
- Don't assume prior knowledge
- No walls of text
- Avoid passive constructions
- Never skip error handling examples
```

## Example 5: PM-Focused Project

```markdown
# CLAUDE.md

## Context
Product management workspace for feature planning and documentation.

## Document Standards
- PRDs follow company template
- User stories in Gherkin format
- Metrics defined before implementation
- All decisions documented with rationale

## Workflow Rules
- Always ask before creating new documents
- Check existing docs before writing
- Link related documents
- Update status tags regularly

## Communication Preferences
- Summarize long documents
- Highlight key decisions and trade-offs
- Flag risks and dependencies clearly
- Use tables for comparisons

## Integration Points
- Jira for task tracking
- Slack for updates
- Google Drive for document storage
- Figma for designs
```

## Example 6: Personal Productivity

```markdown
# CLAUDE.md

## Overview
Personal note-taking and task management system.

## Organization Rules
- Daily notes in /journal/YYYY-MM-DD.md
- Meeting notes in /meetings/
- Project docs in /projects/{project-name}/
- Archive completed items monthly

## Formatting Preferences
- Use checkboxes for todos
- Tag items with #hashtags
- Link related notes with [[wiki-links]]
- Time stamps for meeting notes

## Automation Requests
- Generate weekly summary from daily notes
- Extract action items from meeting notes
- Create project status updates
- Remind about overdue tasks

## Privacy Rules
- Redact personal information in examples
- No real names without permission
- Sanitize sensitive business data
- Confirm before external sharing
```

## Common Patterns and Best Practices

### 1. Be Specific About Preferences
```markdown
## Preferences
- PUT over PATCH for updates
- ISO 8601 for all date formats
- camelCase for JavaScript, snake_case for Python
- Tabs for indentation (not spaces)
```

### 2. Define Boundaries Clearly
```markdown
## Never Do This
- Modify production database directly
- Commit large files (>10MB)
- Use deprecated APIs
- Skip code review process
```

### 3. Provide Context for Decisions
```markdown
## Architecture Decisions
- Chose PostgreSQL over MySQL for JSON support
- Using microservices for independent scaling
- GraphQL for flexible client queries
- Redis for session management (performance)
```

### 4. Include Workflow Guidance
```markdown
## Development Workflow
1. Create feature branch from develop
2. Write tests first (TDD)
3. Implement feature
4. Run full test suite
5. Submit PR with description
6. Address review feedback
7. Squash commits before merge
```

### 5. Set Quality Standards
```markdown
## Quality Checklist
- [ ] All tests passing
- [ ] Code coverage >85%
- [ ] No linting errors
- [ ] Documentation updated
- [ ] Performance benchmarks met
- [ ] Security scan clean
- [ ] Accessibility standards met
```

## Tips for Effective CLAUDE.md Files

1. **Start Simple**: Begin with basic rules and expand as needed
2. **Be Consistent**: Use the same terminology throughout
3. **Update Regularly**: Keep the file current with project evolution
4. **Team Input**: Gather feedback from all stakeholders
5. **Examples Help**: Show good and bad examples
6. **Prioritize**: Put most important rules first
7. **Test It**: Verify Claude follows your guidance

## When to Update CLAUDE.md

- New team members join
- Project requirements change
- Common mistakes occur repeatedly
- New tools or libraries adopted
- Workflow processes updated
- Lessons learned from incidents

Remember: CLAUDE.md is a living document that should evolve with your project's needs!