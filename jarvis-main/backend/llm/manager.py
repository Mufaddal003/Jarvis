import os

from dotenv import load_dotenv

from .prompt import SYSTEM_PROMPT

from .groq_provider import GroqProvider

from .streaming import stream_response

load_dotenv()


class LLMManager:

    def __init__(self):

        self.provider = GroqProvider()

    def ask(
        self,
        prompt,
        history=None,
        stream=False,
    ):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
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

        response = self.provider.chat(
            messages=messages,
            temperature=float(
                os.getenv("TEMPERATURE", 0.7)
            ),
            max_tokens=int(
                os.getenv("MAX_TOKENS", 1024)
            ),
            stream=stream,
        )

        if stream:

            return stream_response(response)

        return response.choices[0].message.content