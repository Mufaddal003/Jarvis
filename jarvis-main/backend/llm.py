import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv("MODEL", "llama-3.3-70b-versatile")


class LLM:

    def __init__(self):
        print("Groq LLM Loaded")

    def ask(self, prompt, history=None):

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Jarvis, an intelligent AI desktop assistant. "
                    "Be concise, professional, and helpful."
                ),
            }
        ]

        if history:
            messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_completion_tokens=1024,
        )

        return response.choices[0].message.content