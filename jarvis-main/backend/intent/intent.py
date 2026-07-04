from enum import Enum


class Intent(Enum):

    CHAT = "chat"

    OPEN_APP = "open_app"

    OPEN_WEBSITE = "open_website"

    SEARCH_FILE = "search_file"

    OPEN_PROJECT = "open_project"

    SYSTEM = "system"

    UNKNOWN = "unknown"