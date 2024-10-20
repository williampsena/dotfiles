from libqtile import widget

from ebenezer.core.command import run_shell_command
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def __powermenu_modal__(settings: AppSettings):
    def inner():
        return run_shell_command(settings.commands.get("powermenu"), **{})

    return inner


def build_powermenu_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 4,
        "foreground": settings.colors.fg_normal,
        "mouse_callbacks": {"Button1": __powermenu_modal__(settings)},
    }

    args = build_widget_args(settings, default_args, kwargs, ["foreground"])

    return widget.TextBox(args.pop("text", ""), **args)
