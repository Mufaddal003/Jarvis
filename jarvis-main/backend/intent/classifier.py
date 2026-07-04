from .intent import Intent


class IntentClassifier:

    WEBSITE = [
        "youtube",
        "google",
        "github",
        "linkedin",
        "chatgpt",
        "gmail",
        "spotify",
    ]

    APPS = [
        "cursor",
        "notepad",
        "chrome",
        "vscode",
        "calculator",
        "terminal",
        "cmd",
    ]

    def classify(self, text):

        cmd = text.lower()

        if any(site in cmd for site in self.WEBSITE):
            return Intent.OPEN_WEBSITE

        if any(app in cmd for app in self.APPS):
            return Intent.OPEN_APP

        if "project" in cmd:
            return Intent.OPEN_PROJECT

        if "file" in cmd:
            return Intent.SEARCH_FILE

        if "shutdown" in cmd:
            return Intent.SYSTEM

        return Intent.CHAT