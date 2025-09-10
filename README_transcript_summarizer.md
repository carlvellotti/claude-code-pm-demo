# YouTube Transcript Summarizer

A tool to test different summarization prompts against multiple AI models (Gemini, Grok, DeepSeek).

## Features

- **Three Prompt Types:**
  - **Short**: 2-3 sentence summary
  - **Medium**: Structured summary with key points and takeaways (~200 words)
  - **Detailed**: Comprehensive analysis with 7 sections including quotes and timestamps

- **Multiple AI Models:**
  - Google Gemini (gemini-pro)
  - X.AI Grok (grok-beta)
  - DeepSeek (deepseek-chat)

- **Performance Tracking:**
  - Response time measurement
  - Character count tracking
  - Error handling and reporting

## Setup

1. Install dependencies:
   ```bash
   pip install google-generativeai requests
   ```

2. Set up API keys as environment variables:
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key"
   export GROK_API_KEY="your-grok-api-key"
   export DEEPSEEK_API_KEY="your-deepseek-api-key"
   ```

## Usage

### Option 1: Direct Python execution
```bash
python transcript_summarizer.py
```

### Option 2: Use the helper script
```bash
./run_summarizer.sh
```
This script will prompt for API keys if they're not already set.

## Output

Results are saved in the `results/` directory:

- `results/gemini/` - Gemini model outputs
- `results/grok/` - Grok model outputs  
- `results/deepseek/` - DeepSeek model outputs
- `results/all_results.json` - Complete results with metadata
- `results/comparison_report.md` - Side-by-side comparison report

## Example Transcript

The tool uses `transcript_example.txt` which contains a YouTube interview transcript about AI agents and open-source AI.

## Prompt Templates

### Short Prompt
Focuses on extreme conciseness - just the main topic and key takeaway in 2-3 sentences.

### Medium Prompt
Structured format with:
- Main topic
- 3-5 key points
- Notable insights
- Practical takeaways

### Detailed Prompt
Comprehensive analysis including:
- Executive summary
- Main topics discussed
- Key insights with quotes
- Speaker background
- Technical concepts
- Actionable recommendations
- Resources mentioned

## Performance Comparison

The tool generates a comparison report showing:
- Response times for each model/prompt combination
- Character counts to verify length adherence
- Side-by-side output comparison
- Performance summary table