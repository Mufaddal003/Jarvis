import webbrowser
import subprocess


class AgentExecutor:

    def execute(self, plan):

        outputs = []

        for step in plan["steps"]:

            tool = step["tool"]

            action = step["action"]

            target = step.get("target")

            if tool == "browser":

                if action == "open":

                    webbrowser.open(target)

                    outputs.append(f"Opened {target}")

            elif tool == "app":

                subprocess.Popen(target)

                outputs.append(f"Opened {target}")

            elif tool == "chat":

                outputs.append(target)

        return "\n".join(outputs)