from libqtile import widget
from libqtile.log_utils import logger
from settings import AppSettings


def build_memory_widget(settings: AppSettings):
    return [
        widget.TextBox(
            "󰄧",
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            padding=2,
            foreground=settings.colors.get("fg_purple"),
        ),
        widget.Memory(
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            format="{MemUsed: .0f}{mm} ",
            padding=2,
            foreground=settings.colors.get("fg_normal"),
        ),
    ]
