# First LLM Call

## Problem
Send a prompt to an LLM from Python, save the reply to a text file,
and measure token usage and latency.

## Stack
- Python 3.13
- Groq API (model: openai/gpt-oss-120b)
- python-dotenv

## Setup
1. Clone the repo and create a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate
2. Install dependencies:
   pip install groq python-dotenv
3. Create a `.env` file with your key:
   GROQ_API_KEY=your_key_here
4. Run:
   python python_llm_call.py

## Output
- `reply.txt` with the model's answer
- Terminal output with prompt tokens, reply tokens, total tokens and latency

## Notes
Tried Gemini, GitHub Models and Hugging Face first. Hit a 403 project
denial, a certificate error on the work network and a credits limit.
