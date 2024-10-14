from libqtile import widget
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from libqtile.config import Key
from ebenezer.core.config.settings import AppSettings
from ebenezer.core.command import run_shell_command_stdout, run_shell_command
from ebenezer.core.notify import push_notification, push_notification_progress

def build_backlight_widget(settings: AppSettings):
    return widget.Backlight(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        backlight_name=settings.environment.backlight_name,
        fmt=" ",
        padding=2,
        mouse_callbacks={
            "Button1": __backlight_level__(settings)
        },
    )


def __get_backlight_level__(settings: AppSettings):
    cmd = settings.commands.get("backlight_level")

    if cmd is None:
        return "0"

    output = run_shell_command_stdout(cmd)

    return output.stdout.replace("%", "").replace("\n", "")


def __backlight_up__(settings: AppSettings):
    cmd = settings.commands.get("backlight_up")

    @lazy.function
    def inner(qtile):
        level = int(__get_backlight_level__(settings) or "0")

        if level >= 100:
            return

        if cmd:
            run_shell_command(cmd)

        __push_backlight_notification__(settings, "󰃠 Brightness")

    return inner


def __backlight_down__(settings: AppSettings):
    cmd = settings.commands.get("backlight_down")

    @lazy.function
    def inner(qtile):
        if cmd:
            run_shell_command(cmd)

        __push_backlight_notification__(settings, "󰃠 Brightness")

    return inner



def __backlight_level__(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        __push_backlight_notification__(settings, "󰃠 Brightness")

    return inner


def __push_backlight_notification__(settings: AppSettings, message: str):
    level = __get_backlight_level__(settings) or "0"
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=int(level))


def setup_backlight_keys(settings: AppSettings):
    return [
        Key([], "XF86MonBrightnessUp", __backlight_up__(settings)),
        Key([], "XF86MonBrightnessDown", __backlight_down__(settings)),
    ]
