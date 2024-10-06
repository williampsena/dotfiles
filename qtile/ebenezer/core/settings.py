import configparser
from typing import Any
from pathlib import Path
from libqtile.utils import guess_terminal
from ebenezer.core.files import home, qtile_home, resolve_file_path

config_file = str(Path.joinpath(Path(qtile_home), "config.ini"))


class AppSettingsEnvironment:
    mod = "mod4"
    browser = "firefox"
    terminal = guess_terminal()
    wallpaper_dir = ""
    wallpaper_timeout = "60"
    os_logo = ""
    os_logo_icon: str = ""
    os_logo_icon_color: str = ""
    theme = "ebenezer"
    backlight_name: str = ""
    weather_api_key: str = ""
    city_id: str = ""

    def __init__(self, **args):
        self.mod = args.get("mod", self.mod)
        self.browser = args.get("browser", self.browser)
        self.terminal = args.get("terminal", self.terminal)
        self.wallpaper_dir = resolve_file_path(
            args.get("wallpaper_dir", self.wallpaper_dir)
        )
        self.wallpaper_timeout = int(
            args.get("wallpaper_timeout", self.wallpaper_timeout)
        )
        self.theme = args.get("theme", self.theme)
        self.os_logo = args.get("os_logo", self.os_logo)
        self.os_logo_icon = args.get("os_logo_icon", self.os_logo_icon)
        self.os_logo_icon_color = args.get(
            "os_logo_icon_color", self.os_logo_icon_color
        )
        self.backlight_name = args.get("backlight_name", self.backlight_name)
        self.weather_api_key = args.get("weather_api_key", self.weather_api_key)
        self.city_id = args.get("city_id", self.city_id)


class AppSettingsFonts:
    font: str = ""
    font_regular: str = ""
    font_light: str = ""
    font_strong: str = ""
    font_strong_bold: str = ""
    font_size: int = 10
    font_icon: str = ""
    font_icon_size: int = 10

    def __init__(self, **args):
        self.font = args.get("font", self.font)
        self.font_regular = args.get("font_regular", self.font_regular)
        self.font_light = args.get("font_light", self.font_light)
        self.font_strong = args.get("font_strong", self.font_strong)
        self.font_strong_bold = args.get("font_strong_bold", self.font_strong_bold)
        self.font_size = int(args.get("font_size", str(self.font_size)))
        self.font_icon = args.get("font_icon", self.font_icon)
        self.font_icon_size = int(args.get("font_icon_size", str(self.font_icon_size)))


class AppSettingsColors:
    colors: dict[str, str] = {}

    def __init__(self, **args):
        self.colors = args.get("font", args)

    def get(self, color: str) -> str:
        return self.colors.get(color, "#fff")


class AppLockScreen:
    command = ""
    timeout = 10
    font = ""
    font_size = 17
    joke_providers = "reddit,icanhazdad"
    joke_foreground_color = "#000"
    joke_text_color = "#fff"
    icanhazdad_joke_url = "https://icanhazdadjoke.com/"
    reddit_joke_url = "https://www.reddit.com/r/ProgrammerDadJokes.json"
    blurtype = "0x5"
    blank_color = "#00000000"
    clear_color = "#ffffff22"
    default_color = "#9db4c0"
    key_color = "#8a8ea800"
    text_color = "#4BC1CC"
    wrong_color = "#D50000"
    verifying_color = "#41445800"

    def __init__(self, **args):
        self.command = args.get("command", self.command)
        self.timeout = args.get("timeout", str(self.timeout))
        self.font = args.get("font", self.font)
        self.font_size = int(args.get("font_size", str(self.font_size)))
        self.joke_providers = args.get("joke_providers", self.joke_providers).split(",")
        self.joke_foreground_color = args.get(
            "joke_foreground_color", self.joke_foreground_color
        )
        self.joke_text_color = args.get("joke_text_color", self.joke_text_color)
        self.icanhazdad_joke_url = args.get(
            "icanhazdad_joke_url", self.icanhazdad_joke_url
        )
        self.reddit_joke_url = args.get("reddit_joke_url", self.reddit_joke_url)
        self.blurtype = args.get("blurtype", self.blurtype)
        self.blank_color = args.get("blank_color", self.blank_color)
        self.clear_color = args.get("clear_color", self.clear_color)
        self.default_color = args.get("default_color", self.default_color)
        self.key_color = args.get("key_color", self.key_color)
        self.text_color = args.get("text_color", self.text_color)
        self.wrong_color = args.get("wrong_color", self.wrong_color)
        self.verifying_color = args.get("verifying_color", self.verifying_color)


class AppSettings:
    environment = AppSettingsEnvironment(**{})
    fonts = AppSettingsFonts(**{})
    groups: list[Any] = []
    groups_layout: dict[str, str] = {}
    startup: dict[str, str] = {}
    floating: dict[str, str] = {}
    colors: AppSettingsColors = AppSettingsColors(*{})
    commands: dict[str, str] = {}
    lock_screen = AppLockScreen(**{})

    def __init__(self, **args):
        self.groups = args.get("groups", [])
        self.groups_layout = args.get("groups_layout", {"default": "monadtall"})
        self.startup = args.get("startup", [])
        self.floating = args.get("floating", {"wm_class": [], "title": []})
        self.environment = args.get("environment", self.environment)
        self.fonts = args.get("fonts", self.fonts)
        self.colors = args.get("colors", self.colors)
        self.commands = args.get("commands", self.commands)
        self.lock_screen = args.get("lock_screen", self.lock_screen)


def load_settings():
    config = configparser.ConfigParser()
    config.sections()
    config.read(config_file)

    environment = AppSettingsEnvironment(
        **__build__dict_from_ini__(config, "environment")
    )
    fonts = AppSettingsFonts(**__build__dict_from_ini__(config, "fonts"))
    colors = AppSettingsColors(**__build__dict_from_ini__(config, "colors"))
    commands = __build__dict_from_ini__(config, "commands")
    lock_screen = AppLockScreen(**__build__dict_from_ini__(config, "lock_screen"))

    groups = [(key, config["groups"][key]) for key in list(config["groups"].keys())]
    groups_layout = __build__dict_from_ini__(config, "groups.layout")
    startup = __build__dict_from_ini__(config, "startup")
    floating = {
        "wm_class": __build__list_from_string_ini__(config, "floating", "wm_class"),
        "title": __build__list_from_string_ini__(config, "floating", "title"),
    }

    app_settings = AppSettings(
        environment=environment,
        fonts=fonts,
        colors=colors,
        commands=commands,
        lock_screen=lock_screen,
        groups=groups,
        groups_layout=groups_layout,
        startup=startup,
        floating=floating,
    )

    return app_settings


def __build__dict_from_ini__(config, section):
    return {key: config[section][key] for key in list(config[section].keys())}


def __build__list_from_string_ini__(config, section, key):
    value = config[section].get(key, "")

    if value == "":
        return list()

    return value.split(" ")
