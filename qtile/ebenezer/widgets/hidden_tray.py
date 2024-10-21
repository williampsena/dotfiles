from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.backlight import build_backlight_widget
from ebenezer.widgets.helpers.args import build_widget_args


def build_hidden_tray(settings: AppSettings, kwargs: dict):
    default_args = {
        "padding": 10,
        "font": settings.fonts.font_icon,
        "text_closed": settings.environment.os_logo_icon,
        "text_open": settings.environment.os_logo_icon,
        "foreground": settings.environment.os_logo_icon_color,
    }

    args = build_widget_args(settings, default_args, kwargs, ["foreground"])

    return widget.WidgetBox(
        widgets=[
            widget.Systray(padding=4),
            widget.Spacer(length=1),
            build_backlight_widget(settings, kwargs.get("backlight", {})),
        ],
        **args
    )
