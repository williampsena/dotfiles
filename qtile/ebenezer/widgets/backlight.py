from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy

from ebenezer.core.command import run_shell_command, run_shell_command_stdout
from ebenezer.core.config.settings import AppSettings
from ebenezer.core.notify import push_notification_progress
from ebenezer.widgets.helpers.args import build_widget_args


def build_backlight_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "backlight_name": settings.environment.backlight_name,
        "fmt": " ",
        "padding": 3,
        "mouse_callbacks": {"Button1": _backlight_level(settings)},
    }

    args = build_widget_args(settings, default_args, kwargs, [])

    return widget.Backlight(**args)


def _get_backlight_level(settings: AppSettings):
    cmd = settings.commands.get("backlight_level")

    if cmd is None:
        return "0"

    output = run_shell_command_stdout(cmd)

    return output.stdout.replace("%", "").replace("\n", "")


def _backlight_up(settings: AppSettings):
    cmd = settings.commands.get("backlight_up")

    @lazy.function
    def inner(qtile):
        level = int(_get_backlight_level(settings) or "0")

        if level >= 100:
            return

        if cmd:
            run_shell_command(cmd)

        __push_backlight_notification(settings, "󰃠 Brightness")

    return inner


def __backlight_down(settings: AppSettings):
    cmd = settings.commands.get("backlight_down")

    @lazy.function
    def inner(qtile):
        if cmd:
            run_shell_command(cmd)

        __push_backlight_notification(settings, "󰃠 Brightness")

    return inner


def _backlight_level(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        __push_backlight_notification(settings, "󰃠 Brightness")

    return inner


def __push_backlight_notification(settings: AppSettings, message: str):
    level = _get_backlight_level(settings) or "0"
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=int(level))


def setup_backlight_keys(settings: AppSettings):
    return [
        Key([], "XF86MonBrightnessUp", _backlight_up(settings)),
        Key([], "XF86MonBrightnessDown", __backlight_down(settings)),
    ]
