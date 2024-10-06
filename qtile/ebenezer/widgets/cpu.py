from libqtile import bar, widget
from libqtile.log_utils import logger
from ebenezer.core.settings import AppSettings


def build_cpu_widget(settings: AppSettings):
    return [
        widget.TextBox(
            " ",
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            padding=2,
            foreground=settings.colors.get("fg_yellow"),
        ),
        widget.CPU(
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            format="{load_percent}% ",
            padding=2,
            foreground=settings.colors.get("fg_normal"),
        ),
    ]
