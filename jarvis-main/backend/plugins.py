class Router:

    def route(self, command):

        cmd = command.lower()

        if "youtube" in cmd:
            return "youtube"

        if "google" in cmd:
            return "google"

        if "spotify" in cmd:
            return "spotify"

        if "open" in cmd:
            return "automation"

        return "llm"