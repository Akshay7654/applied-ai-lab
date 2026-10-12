import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise SystemExit("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)

prompt = "Explain what an API key is in 3 simple sentences."

try:
    start = time.time()
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
    )
    latency = time.time() - start
except Exception as e:
    print("Error type:", type(e).__name__)
    print("Details:", repr(getattr(e, "response", None) and e.response.text or e))
    raise SystemExit(1)

with open("reply.txt", "w", encoding="utf-8") as f:
    f.write(response.choices[0].message.content)

usage = response.usage
print("Reply saved to reply.txt")
print(f"Prompt tokens: {usage.prompt_tokens}")
print(f"Reply tokens:  {usage.completion_tokens}")
print(f"Total tokens:  {usage.total_tokens}")
print(f"Latency:       {latency:.2f} seconds")