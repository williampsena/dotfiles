from typing import List
from libqtile.log_utils import logger


class AppSettingsKeyBinding:
    name: str = ""
    keys: List[str] = []
    action: str = ""
    command: str = ""

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", self.name)
        self.keys = kwargs.get("keys", "").split(" ")
        self.action = kwargs.get("action", self.action)
        self.command = kwargs.get("command", self.command)


def build_keybindings(items: List[dict]) -> List[AppSettingsKeyBinding]:
    try:
        return [AppSettingsKeyBinding(**i) for i in items]
    except Exception as error:
        logger.warning(
            "An exception occurred while trying to build keybindings.",
            error,
            exc_info=True,
        )
        return []
