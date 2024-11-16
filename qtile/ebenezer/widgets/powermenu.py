from ebenezer.core.command import run_shell_command
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args
from libqtile import widget


def _powermenu_modal(settings: AppSettings):
    def inner():
        return run_shell_command(settings.commands.get("powermenu"), **{})

    return inner


def build_powermenu_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 4,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "mouse_callbacks": {"Button1": _powermenu_modal(settings)},
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
    )

    return widget.TextBox(args.pop("text", ""), **args)
