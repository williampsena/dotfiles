import configparser
from pathlib import Path
from libqtile.utils import guess_terminal
from files import home, qtile_home, resolve_file_path

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
    colors = {}

    def __init__(self, **args):
        self.colors = args.get("font", args)

    def get(self, color: str) -> str:
        return self.colors.get(color, "#fff")


class AppSettings:
    environment = AppSettingsEnvironment(**{})
    fonts = AppSettingsFonts(**{})
    groups = []
    groups_layout = []
    startup = []
    floating = {}
    colors: AppSettingsColors = AppSettingsColors(*{})
    commands = {}

    def __init__(self, **args):
        self.groups = args.get("groups", [])
        self.groups_layout = args.get("groups_layout", {"default": "monadtall"})
        self.startup = args.get("startup", [])
        self.floating = args.get("floating", {"wm_class": [], "title": []})
        self.environment = args.get("environment", self.environment)
        self.fonts = args.get("fonts", self.fonts)
        self.colors = args.get("colors", self.colors)
        self.commands = args.get("commands", self.commands)


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
