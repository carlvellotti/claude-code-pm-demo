# Writing Style Guide

## Technical Style

### Characteristics
- Precise and specific language
- Heavy use of technical terminology and acronyms
- Detailed specifications and requirements
- Focus on implementation details
- Data-driven with metrics and benchmarks

### When to Use
- Engineering documentation
- API specifications
- System architecture documents
- Technical PRDs for engineering teams

### Example
"The authentication service shall implement OAuth 2.0 with PKCE flow, supporting refresh token rotation with a 24-hour TTL. The service must handle 10,000 concurrent auth requests with p99 latency under 200ms. Integration requires webhook endpoints for event propagation using HMAC-SHA256 signature verification."

### Key Phrases
- "shall/must implement"
- "performance requirements"
- "technical constraints"
- "system architecture"
- "API endpoints"
- "latency/throughput metrics"

---

## User-Friendly Style

### Characteristics
- Clear, conversational tone
- Avoids jargon and technical terms
- Focuses on user benefits and outcomes
- Uses analogies and examples
- Story-driven explanations

### When to Use
- Customer-facing documentation
- Product announcements
- User guides and help content
- Marketing materials

### Example
"Imagine never having to manually copy data between your apps again. Our new integration automatically syncs your customer information across all your tools, saving you hours each week. It's like having a personal assistant who never forgets to update your records."

### Key Phrases
- "you can now"
- "this helps you"
- "save time by"
- "simply click"
- "no technical knowledge required"
- "works like"

---

## Internal-Audience Style

### Characteristics
- Assumes organizational context
- Direct and action-oriented
- References internal tools and processes
- Includes strategic rationale
- Balances technical and business language

### When to Use
- Internal PRDs
- Team updates and memos
- Strategic planning documents
- Cross-functional communications

### Example
"Based on Q4 customer feedback and our H1 roadmap commitments, we're prioritizing the mobile workflow editor. This directly addresses the field worker use case (representing 40% of our TAM) and aligns with our expansion strategy. Engineering estimates 3 sprints using our existing React Native framework."

### Key Phrases
- "aligns with our"
- "based on [internal metric]"
- "cross-functional impact"
- "roadmap priority"
- "resource allocation"
- "strategic objective"

---

## Style Comparison Table

| Aspect | Technical | User-Friendly | Internal-Audience |
|--------|-----------|---------------|-------------------|
| **Audience** | Engineers, architects | End users, customers | Internal teams |
| **Tone** | Formal, precise | Conversational, warm | Direct, professional |
| **Detail Level** | Very high | Moderate | High but selective |
| **Jargon Usage** | Heavy | Minimal | Moderate |
| **Focus** | How it works | What you can do | Why we're doing it |
| **Metrics** | Technical KPIs | User benefits | Business impact |

## Switching Between Styles

When transitioning between styles, consider:
1. **Audience needs** - What does your reader need to know?
2. **Action required** - What should they do with this information?
3. **Context level** - How much background do they have?
4. **Emotional tone** - Should this inspire, inform, or direct?

## Quick Style Converter Examples

**Technical → User-Friendly**
- "API rate limiting at 1000 QPM" → "Can handle all your team's requests without slowdowns"
- "OAuth 2.0 integration" → "Secure sign-in using your existing accounts"

**User-Friendly → Internal-Audience**
- "Save hours each week" → "Reduces operational overhead by 15% (per CS team metrics)"
- "Easy to get started" → "2-week implementation timeline using standard deployment playbook"

**Internal-Audience → Technical**
- "Mobile expansion initiative" → "React Native implementation with offline-first architecture"
- "Customer-requested feature" → "Requirements traced to tickets #1234, #1235, #1236"