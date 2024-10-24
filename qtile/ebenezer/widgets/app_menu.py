from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_app_menu_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "padding": 10,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "text_closed": settings.environment.os_logo_icon,
        "text_open": settings.environment.os_logo_icon,
        "foreground": settings.environment.os_logo_icon_color,
    }

    args = build_widget_args(settings, default_args, kwargs, ["foreground"])
    icon = kwargs.pop("icon", settings.environment.os_logo_icon)

    return widget.TextBox(f" {icon}", **args)
