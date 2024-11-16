from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args
from libqtile import widget


def build_window_name_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "max_chars": 30,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        [
            "foreground",
        ],
    )

    return widget.WindowName(**args)
