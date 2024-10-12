import subprocess
from libqtile import qtile, widget
from libqtile.lazy import lazy
from ebenezer.core.settings import AppSettings
from ebenezer.widgets.backlight import build_backlight_widget


def build_hide_tray(settings: AppSettings):
    return widget.WidgetBox(
        widgets=[
            build_backlight_widget(settings),
            widget.Systray(),
        ],
        padding=12,
        font=settings.fonts.font_icon,
        text_closed=settings.environment.os_logo_icon,
        text_open=settings.environment.os_logo_icon,
        foreground=settings.environment.os_logo_icon_color,
    )
