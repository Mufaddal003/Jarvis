class Router:

    def route(self, command):

        command = command.lower()

        if "youtube" in command:
            return "youtube"

        if "google" in command:
            return "google"

        if "spotify" in command:
            return "spotify"

        return "chat"