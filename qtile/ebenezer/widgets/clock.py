from libqtile import widget
from ebenezer.core.config.settings import AppSettings


def build_clock_widget(settings: AppSettings):
    return widget.Clock(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=2,
        format="%b %d, %I:%M %p",
    )
