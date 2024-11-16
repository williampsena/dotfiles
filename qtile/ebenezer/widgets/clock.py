from ebenezer.core.config.settings import AppSettings
from libqtile import widget


def build_clock_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "padding": 2,
        "format": "%b %d, %I:%M %p",
    }

    args = default_args | kwargs

    return widget.Clock(**args)
