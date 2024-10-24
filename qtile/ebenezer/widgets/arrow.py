from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_arrow_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "text": "",
        "font": settings.fonts.font_arrow,
        "fontsize": settings.fonts.font_arrow_size,
        "foreground": settings.colors.bg_topbar_arrow,
        "padding": 0,
    }

    args = build_widget_args(settings, default_args, kwargs, ["foreground"])

    return widget.TextBox(**args)
