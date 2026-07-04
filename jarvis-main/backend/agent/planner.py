import json

from backend.agent.tools import TOOLS


class AgentPlanner:

    def __init__(self, llm):

        self.llm = llm

    def create_plan(self, command):

        prompt = f"""
You are Jarvis AI.

{TOOLS}

User request:

{command}
"""

        response = self.llm.ask(prompt)

        try:

            return json.loads(response)

        except Exception:

            return {
                "steps": [
                    {
                        "tool": "chat",
                        "action": "reply",
                        "target": response
                    }
                ]
            }