import subprocess


class AppPlugin:

    APPS = {

        "notepad": "notepad",

        "calculator": "calc",

        "cmd": "cmd",

    }

    def run(self, command):

        text = command.lower()

        for app, exe in self.APPS.items():

            if app in text:

                subprocess.Popen(exe)

                return f"Opening {app}"

        return "Application not found."