#!/usr/bin/env python3
"""
YouTube Transcript Summarization Tool
Tests different prompts against multiple AI models (Gemini, Grok, DeepSeek)
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple
import google.generativeai as genai
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Prompt templates
PROMPTS = {
    "short": """Summarize this YouTube transcript in 2-3 sentences. Focus only on the main topic and key takeaway. Be extremely concise.

Transcript:
{transcript}""",
    
    "medium": """Create a structured summary of this YouTube transcript with the following sections:
- Main Topic (1 sentence)
- Key Points (3-5 bullet points)
- Notable Insights (2-3 sentences)
- Practical Takeaways (2-3 bullet points)

Keep the total summary under 200 words.

Transcript:
{transcript}""",
    
    "detailed": """Provide a comprehensive analysis of this YouTube transcript including:

1. **Executive Summary** (3-4 sentences overview)
2. **Main Topics Discussed** (List each major topic with 2-3 sentence description)
3. **Key Insights and Quotes** (5-7 most important points with relevant quotes)
4. **Speaker Background** (If mentioned in transcript)
5. **Technical Concepts Explained** (Define any specialized terms or concepts)
6. **Actionable Recommendations** (What viewers should do based on content)
7. **Additional Resources Mentioned** (Tools, frameworks, companies, etc.)

Format with clear headings and bullet points. Include timestamp references where relevant.

Transcript:
{transcript}"""
}


class TranscriptSummarizer:
    def __init__(self):
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY")
        self.chatgpt_api_key = os.environ.get("CHATGPT_API_KEY")
        self.grok_api_key = os.environ.get("GROK_API_KEY")
        
        # Initialize results directory
        self.results_dir = Path("results")
        self.results_dir.mkdir(exist_ok=True)
    
    def load_transcript(self, filepath: str = "transcript_example.txt") -> str:
        """Load the transcript from file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def call_gemini(self, prompt: str) -> Tuple[str, float, Dict]:
        """Call Gemini API and return response with timing"""
        if not self.gemini_api_key:
            return "Error: GEMINI_API_KEY not found", 0, {"error": "API key missing"}
        
        try:
            genai.configure(api_key=self.gemini_api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            start_time = time.time()
            response = model.generate_content(prompt)
            end_time = time.time()
            
            return response.text, end_time - start_time, {"status": "success"}
        except Exception as e:
            return f"Error: {str(e)}", 0, {"error": str(e)}
    
    def call_grok(self, prompt: str) -> Tuple[str, float, Dict]:
        """Call Grok API and return response with timing"""
        if not self.grok_api_key:
            return "Error: GROK_API_KEY not found", 0, {"error": "API key missing"}
        
        try:
            headers = {
                "Authorization": f"Bearer {self.grok_api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "model": "grok-3",
                "temperature": 0.7
            }
            
            start_time = time.time()
            response = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers=headers,
                json=data
            )
            end_time = time.time()
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"], end_time - start_time, {"status": "success"}
            else:
                return f"Error: {response.status_code} - {response.text}", 0, {"error": response.text}
                
        except Exception as e:
            return f"Error: {str(e)}", 0, {"error": str(e)}
    
    def call_chatgpt(self, prompt: str) -> Tuple[str, float, Dict]:
        """Call ChatGPT API and return response with timing"""
        if not self.chatgpt_api_key:
            return "Error: CHATGPT_API_KEY not found", 0, {"error": "API key missing"}
        
        try:
            headers = {
                "Authorization": f"Bearer {self.chatgpt_api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "model": "gpt-4-turbo-preview",
                "temperature": 0.7
            }
            
            start_time = time.time()
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            end_time = time.time()
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"], end_time - start_time, {"status": "success"}
            else:
                return f"Error: {response.status_code} - {response.text}", 0, {"error": response.text}
                
        except Exception as e:
            return f"Error: {str(e)}", 0, {"error": str(e)}
    
    
    def run_all_tests(self):
        """Run all prompt/model combinations"""
        transcript = self.load_transcript()
        results = {
            "timestamp": datetime.now().isoformat(),
            "transcript_length": len(transcript),
            "results": {}
        }
        
        models = {
            "gemini": self.call_gemini,
            "chatgpt": self.call_chatgpt,
            "grok": self.call_grok
        }
        
        print("Starting transcript summarization tests...")
        print(f"Transcript length: {len(transcript)} characters\n")
        
        for prompt_type, prompt_template in PROMPTS.items():
            results["results"][prompt_type] = {}
            print(f"\nTesting {prompt_type} prompt...")
            
            for model_name, model_func in models.items():
                print(f"  - Running {model_name}...", end="", flush=True)
                
                prompt = prompt_template.format(transcript=transcript)
                response, duration, metadata = model_func(prompt)
                
                # Save individual result
                result_data = {
                    "prompt_type": prompt_type,
                    "model": model_name,
                    "response": response,
                    "duration_seconds": duration,
                    "metadata": metadata,
                    "response_length": len(response),
                    "timestamp": datetime.now().isoformat()
                }
                
                results["results"][prompt_type][model_name] = result_data
                
                print(f" Done ({duration:.2f}s, {len(response)} chars)")
        
        # Save complete results
        with open(self.results_dir / "all_results.json", 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Generate consolidated prompt files
        self.generate_prompt_files(results)
        
        print("\nAll tests completed!")
        print(f"Results saved to: {self.results_dir}")
    
    def generate_prompt_files(self, results: Dict):
        """Generate one file per prompt type with all model responses"""
        for prompt_type, prompt_template in PROMPTS.items():
            content = []
            content.append(f"# {prompt_type.capitalize()} Summary Results\n")
            content.append(f"Generated: {datetime.now().isoformat()}\n")
            content.append(f"Transcript Length: {results['transcript_length']} characters\n")
            
            # Add the prompt
            content.append("\n## Prompt:\n")
            content.append("```\n")
            content.append(prompt_template.replace("{transcript}", "[TRANSCRIPT TEXT HERE]"))
            content.append("\n```\n")
            
            # Add each model's response
            if prompt_type in results["results"]:
                for model in ["gemini", "chatgpt", "grok"]:
                    if model in results["results"][prompt_type]:
                        data = results["results"][prompt_type][model]
                        content.append(f"\n## {model.capitalize()} Response:\n")
                        content.append(f"**Duration**: {data['duration_seconds']:.2f} seconds\n")
                        content.append(f"**Length**: {data['response_length']} characters\n")
                        content.append(f"**Status**: {data['metadata'].get('status', 'error')}\n")
                        content.append("\n```\n")
                        content.append(data['response'])
                        if not data['response'].endswith('\n'):
                            content.append('\n')
                        content.append("```\n")
            
            # Save to file
            filename = self.results_dir / f"{prompt_type}_summary_results.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.writelines(content)
        
        print(f"\nCreated 3 summary files:")
        for prompt_type in PROMPTS.keys():
            print(f"  - {prompt_type}_summary_results.txt")
    
    def generate_comparison_report(self, results: Dict):
        """Generate a markdown report comparing all results"""
        report = ["# YouTube Transcript Summarization Comparison Report\n"]
        report.append(f"Generated: {results['timestamp']}\n")
        report.append(f"Transcript Length: {results['transcript_length']} characters\n")
        
        for prompt_type in ["short", "medium", "detailed"]:
            report.append(f"\n## {prompt_type.capitalize()} Summary Comparison\n")
            
            for model in ["gemini", "chatgpt", "grok"]:
                if model in results["results"][prompt_type]:
                    data = results["results"][prompt_type][model]
                    report.append(f"\n### {model.capitalize()}\n")
                    report.append(f"- **Duration**: {data['duration_seconds']:.2f} seconds\n")
                    report.append(f"- **Length**: {data['response_length']} characters\n")
                    report.append(f"- **Status**: {data['metadata'].get('status', 'error')}\n")
                    report.append("\n**Summary:**\n")
                    report.append("```\n")
                    report.append(data['response'][:1000] + "..." if len(data['response']) > 1000 else data['response'])
                    report.append("\n```\n")
        
        # Performance summary
        report.append("\n## Performance Summary\n")
        report.append("| Model | Prompt Type | Duration (s) | Response Length |\n")
        report.append("|-------|-------------|--------------|----------------|\n")
        
        for prompt_type in ["short", "medium", "detailed"]:
            for model in ["gemini", "chatgpt", "grok"]:
                if model in results["results"][prompt_type]:
                    data = results["results"][prompt_type][model]
                    if data['metadata'].get('status') == 'success':
                        report.append(f"| {model} | {prompt_type} | {data['duration_seconds']:.2f} | {data['response_length']} |\n")
        
        # Save report
        with open(self.results_dir / "comparison_report.md", 'w', encoding='utf-8') as f:
            f.writelines(report)


if __name__ == "__main__":
    summarizer = TranscriptSummarizer()
    summarizer.run_all_tests()