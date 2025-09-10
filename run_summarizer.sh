#!/bin/bash

# Script to run the transcript summarizer with API keys
# Usage: ./run_summarizer.sh

echo "YouTube Transcript Summarizer"
echo "============================="
echo ""

# Check if API keys are provided as arguments or environment variables
if [ -z "$GEMINI_API_KEY" ]; then
    echo "Please enter your GEMINI_API_KEY:"
    read -r GEMINI_API_KEY
fi

if [ -z "$GROK_API_KEY" ]; then
    echo "Please enter your GROK_API_KEY:"
    read -r GROK_API_KEY
fi

if [ -z "$DEEPSEEK_API_KEY" ]; then
    echo "Please enter your DEEPSEEK_API_KEY:"
    read -r DEEPSEEK_API_KEY
fi

# Export API keys
export GEMINI_API_KEY
export GROK_API_KEY  
export DEEPSEEK_API_KEY

# Run the Python script
python transcript_summarizer.py