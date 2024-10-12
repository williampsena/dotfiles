import subprocess
from libqtile import qtile, widget
from libqtile.lazy import lazy
from ebenezer.core.settings import AppSettings
from ebenezer.core.command import run_shell_command


def __powermenu_modal__(settings: AppSettings):
    def inner():
        return run_shell_command(settings.commands.get("powermenu"), **{})

    return inner


def build_powermenu_widget(settings: AppSettings):
    return widget.TextBox(
        " ",
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=2,
        foreground=settings.colors.get("fg_normal"),
        mouse_callbacks={"Button1": __powermenu_modal__(settings)},
    )
