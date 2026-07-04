from backend.plugins.manager import PluginManager

from backend.plugins.browser import BrowserPlugin

from backend.plugins.app import AppPlugin

from .intent import Intent


class Planner:

    def __init__(self):

        self.plugins = PluginManager()

        self.plugins.register(
            Intent.OPEN_WEBSITE,
            BrowserPlugin(),
        )

        self.plugins.register(
            Intent.OPEN_APP,
            AppPlugin(),
        )

    def execute(self, intent, command):

        return self.plugins.execute(
            intent,
            command,
        )