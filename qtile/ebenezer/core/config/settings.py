from pathlib import Path
from typing import Any, List

from libqtile.log_utils import logger

from ebenezer.core.config.applications import AppSettingsApplications
from ebenezer.core.config.bar import AppSettingsBar
from ebenezer.core.config.colors import AppSettingsColors
from ebenezer.core.config.environment import AppSettingsEnvironment
from ebenezer.core.config.fonts import AppSettingsFonts
from ebenezer.core.config.keybindings import AppSettingsKeyBinding, build_keybindings
from ebenezer.core.config.loader import load_raw_settings
from ebenezer.core.config.lock_screen import AppSettingsLockScreen
from ebenezer.core.config.monitoring import AppSettingsMonitoring
from ebenezer.core.files import qtile_home


def _load_config_file(name: str) -> str | None:
    default_file = Path.joinpath(Path(qtile_home), f"{name}_default.yml")
    config_file = Path.joinpath(Path(qtile_home), f"{name}.yml")

    if config_file.exists():
        return str(config_file)

    if default_file.exists():
        logger.warning(
            "There is no file {config_file}, so the file {default_file} will be used.",
        )
        return str(default_file)

    return None


class AppSettings:
    applications: AppSettingsApplications = AppSettingsApplications(*{})
    bar: AppSettingsBar = AppSettingsBar(*{})
    colors: AppSettingsColors = AppSettingsColors(*{})
    commands: dict[str, str] = {}
    environment = AppSettingsEnvironment(**{})
    floating: dict[str, List[str]] = {"wm_class": [], "title": []}
    fonts = AppSettingsFonts(**{})
    groups: list[Any] = []
    groups_layout: dict[str, str] = {"default": "monadtall"}
    keybindings: List[AppSettingsKeyBinding] = []
    lock_screen = AppSettingsLockScreen(**{})
    monitoring: AppSettingsMonitoring = AppSettingsMonitoring(*{})
    startup: dict[str, str] = {}

    def __init__(self, **kwargs):
        self.applications = kwargs.get("applications", self.applications)
        self.bar = kwargs.get("bar", self.bar)
        self.colors = kwargs.get("colors", self.colors)
        self.commands = kwargs.get("commands", self.commands)
        self.environment = kwargs.get("environment", self.environment)
        self.floating = kwargs.get("floating", self.floating)
        self.fonts = kwargs.get("fonts", self.fonts)
        self.groups = kwargs.get("groups", self.groups)
        self.groups_layout = kwargs.get("groups_layout", self.groups_layout)
        self.keybindings = kwargs.get("keybindings", self.keybindings)
        self.lock_screen = kwargs.get("lock_screen", self.lock_screen)
        self.monitoring = kwargs.get("monitoring", self.monitoring)
        self.startup = kwargs.get("startup", self.startup)


def load_settings_by_files(
    config_filepath=None,
    colors_filepath=None,
    applications_filepath=None,
) -> AppSettings:
    if config_filepath is None:
        config_filepath = _load_config_file("config")

    if colors_filepath is None:
        colors_filepath = _load_config_file("colors")

    if applications_filepath is None:
        applications_filepath = _load_config_file("applications")

    raw_settings = load_raw_settings(
        config_filepath=config_filepath,
        colors_filepath=colors_filepath,
        applications_filepath=applications_filepath,
    )

    return load_settings(raw_settings)


def load_settings(raw_settings: dict) -> AppSettings:
    raw_keys = ["commands", "floating", "groups", "groups_layout", "startup"]
    args = {k: v for k, v in raw_settings.items() if k in raw_keys}

    bar = raw_settings.get("bar")
    applications = raw_settings.get("applications")
    colors = raw_settings.get("colors")
    environment = raw_settings.get("environment")
    fonts = raw_settings.get("fonts", {})
    keybindings = raw_settings.get("keybindings")
    lock_screen = raw_settings.get("lock_screen")
    monitoring = raw_settings.get("monitoring")

    if applications:
        args["applications"] = AppSettingsApplications(**applications)

    if bar:
        args["bar"] = AppSettingsBar(**bar)

    if colors:
        args["colors"] = AppSettingsColors(**colors)

    if environment:
        args["environment"] = AppSettingsEnvironment(**environment)

    if fonts:
        args["fonts"] = AppSettingsFonts(**fonts)

    if lock_screen:
        args["lock_screen"] = AppSettingsLockScreen(**lock_screen)

    if keybindings:
        args["keybindings"] = build_keybindings(keybindings)

    if monitoring:
        args["monitoring"] = AppSettingsMonitoring(**monitoring)

    return AppSettings(**args)
