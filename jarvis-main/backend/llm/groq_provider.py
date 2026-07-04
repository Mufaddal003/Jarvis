import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()


class GroqProvider:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = os.getenv(
            "MODEL",
            "llama-3.3-70b-versatile"
        )

    def chat(
        self,
        messages,
        temperature=0.7,
        max_tokens=1024,
        stream=False,
    ):

        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_completion_tokens=max_tokens,
            stream=stream,
        )