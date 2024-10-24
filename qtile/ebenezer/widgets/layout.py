from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_current_layout_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "padding": 6,
        "scale": 0.6,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "font": settings.fonts.font_icon,
    }

    args = build_widget_args(settings, default_args, kwargs, [])

    return widget.CurrentLayoutIcon(**args)
