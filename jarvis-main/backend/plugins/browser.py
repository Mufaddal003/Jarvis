import webbrowser


class BrowserPlugin:

    URLS = {

        "youtube": "https://youtube.com",

        "github": "https://github.com",

        "google": "https://google.com",

        "linkedin": "https://linkedin.com",

        "spotify": "https://open.spotify.com",

        "chatgpt": "https://chat.openai.com",
    }

    def run(self, command):

        text = command.lower()

        for key, value in self.URLS.items():

            if key in text:

                webbrowser.open(value)

                return f"Opening {key}"

        return "Website not found."