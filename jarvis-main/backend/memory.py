from collections import deque


class Memory:

    def __init__(self, max_history=25):

        self.messages = deque(maxlen=max_history)

    def add_user(self, text):

        self.messages.append(
            {
                "role": "user",
                "content": text,
            }
        )

    def add_assistant(self, text):

        self.messages.append(
            {
                "role": "assistant",
                "content": text,
            }
        )

    def get(self):

        return list(self.messages)

    def clear(self):

        self.messages.clear()