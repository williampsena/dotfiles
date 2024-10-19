from typing import Any, List
from pathlib import Path
from ebenezer.core.files import qtile_home
from ebenezer.core.config.colors import AppSettingsColors
from ebenezer.core.config.environment import AppSettingsEnvironment
from ebenezer.core.config.fonts import AppSettingsFonts
from ebenezer.core.config.lock_screen import AppSettingsLockScreen
from ebenezer.core.config.loader import load_raw_settings
from ebenezer.core.config.monitoring import AppSettingsMonitoring

config_file = str(Path.joinpath(Path(qtile_home), "config.yml"))


class AppSettings:
    colors: AppSettingsColors = AppSettingsColors(*{})
    commands: dict[str, str] = {}
    environment = AppSettingsEnvironment(**{})
    floating: dict[str, List[str]] = {"wm_class": [], "title": []}
    fonts = AppSettingsFonts(**{})
    groups: list[Any] = []
    groups_layout: dict[str, str] = {"default": "monadtall"}
    lock_screen = AppSettingsLockScreen(**{})
    startup: dict[str, str] = {}
    monitoring: AppSettingsMonitoring = AppSettingsMonitoring(*{})

    def __init__(self, **kwargs):
        self.colors = kwargs.get("colors", self.colors)
        self.commands = kwargs.get("commands", self.commands)
        self.environment = kwargs.get("environment", self.environment)
        self.floating = kwargs.get("floating", self.floating)
        self.fonts = kwargs.get("fonts", self.fonts)
        self.groups = kwargs.get("groups", self.groups)
        self.groups_layout = kwargs.get("groups_layout", self.groups_layout)
        self.lock_screen = kwargs.get("lock_screen", self.lock_screen)
        self.startup = kwargs.get("startup", self.startup)
        self.monitoring = kwargs.get("monitoring", self.monitoring)


def load_settings(filepath: str = ""):
    if filepath == "":
        filepath = config_file

    raw_settings = load_raw_settings(filepath)
    raw_keys = ["commands", "floating", "groups", "groups_layout", "startup"]
    args = {k: v for k, v in raw_settings.items() if k in raw_keys}

    colors = raw_settings.get("colors")
    environment = raw_settings.get("environment")
    fonts = raw_settings.get("fonts", {})
    lock_screen = raw_settings.get("lock_screen")
    monitoring = raw_settings.get("monitoring")

    if colors:
        args["colors"] = AppSettingsColors(**colors)

    if environment:
        args["environment"] = AppSettingsEnvironment(**environment)

    if fonts:
        args["fonts"] = AppSettingsFonts(**fonts)

    if lock_screen:
        args["lock_screen"] = AppSettingsLockScreen(**lock_screen)

    if fonts:
        args["fonts"] = AppSettingsFonts(**fonts)

    if monitoring:
        args["monitoring"] = AppSettingsMonitoring(**monitoring)

    return AppSettings(**args)
