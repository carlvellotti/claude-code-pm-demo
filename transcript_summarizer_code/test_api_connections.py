#!/usr/bin/env python3
"""
Test API connections for Gemini, ChatGPT, and DeepSeek
"""

import os
import time
import google.generativeai as genai
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_gemini():
    """Test Gemini API connection"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "❌ GEMINI_API_KEY not found in environment"
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        start = time.time()
        response = model.generate_content("Say 'Hello, I'm working!' in 5 words or less.")
        duration = time.time() - start
        
        return f"✅ Gemini: Connected successfully! Response: '{response.text.strip()}' (took {duration:.2f}s)"
    except Exception as e:
        return f"❌ Gemini: {str(e)}"

def test_chatgpt():
    """Test ChatGPT API connection"""
    api_key = os.environ.get("CHATGPT_API_KEY")
    if not api_key:
        return "❌ CHATGPT_API_KEY not found in environment"
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-4-turbo-preview",
            "messages": [
                {"role": "user", "content": "Say 'Hello, I'm working!' in 5 words or less."}
            ],
            "max_tokens": 10
        }
        
        start = time.time()
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data
        )
        duration = time.time() - start
        
        if response.status_code == 200:
            result = response.json()
            text = result["choices"][0]["message"]["content"].strip()
            return f"✅ ChatGPT: Connected successfully! Response: '{text}' (took {duration:.2f}s)"
        else:
            return f"❌ ChatGPT: HTTP {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"❌ ChatGPT: {str(e)}"

def test_grok():
    """Test Grok API connection"""
    api_key = os.environ.get("GROK_API_KEY")
    if not api_key:
        return "❌ GROK_API_KEY not found in environment"
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "grok-3",
            "messages": [
                {"role": "user", "content": "Say 'Hello, I'm working!' in 5 words or less."}
            ],
            "max_tokens": 10
        }
        
        start = time.time()
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers=headers,
            json=data
        )
        duration = time.time() - start
        
        if response.status_code == 200:
            result = response.json()
            text = result["choices"][0]["message"]["content"].strip()
            return f"✅ Grok: Connected successfully! Response: '{text}' (took {duration:.2f}s)"
        else:
            return f"❌ Grok: HTTP {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"❌ Grok: {str(e)}"

def test_deepseek():
    """Test DeepSeek API connection"""
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        return "❌ DEEPSEEK_API_KEY not found in environment"
    
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": "Say 'Hello, I'm working!' in 5 words or less."}
            ],
            "max_tokens": 10
        }
        
        start = time.time()
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data
        )
        duration = time.time() - start
        
        if response.status_code == 200:
            result = response.json()
            text = result["choices"][0]["message"]["content"].strip()
            return f"✅ DeepSeek: Connected successfully! Response: '{text}' (took {duration:.2f}s)"
        else:
            return f"❌ DeepSeek: HTTP {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"❌ DeepSeek: {str(e)}"

def main():
    """Run all API tests"""
    print("Testing API Connections...")
    print("=" * 60)
    
    # Test each API
    tests = [
        ("Gemini", test_gemini),
        ("ChatGPT", test_chatgpt),
        ("Grok", test_grok),
        ("DeepSeek", test_deepseek)
    ]
    
    for name, test_func in tests:
        print(f"\nTesting {name}...")
        result = test_func()
        print(result)
    
    print("\n" + "=" * 60)
    print("API connection tests complete!")

if __name__ == "__main__":
    main()