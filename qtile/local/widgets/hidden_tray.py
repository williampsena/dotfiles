from local.core.config.settings import AppSettings
from local.widgets.backlight import build_backlight_widget
from local.widgets.helpers.args import build_widget_args
from local.widgets.wallpaper import build_wallpaper_widget
from libqtile import widget


def build_hidden_tray(settings: AppSettings, kwargs: dict):
    default_args = {
        "padding": 10,
        "font": settings.fonts.font_icon,
        "text_closed": settings.environment.os_logo_icon,
        "text_open": settings.environment.os_logo_icon,
        "foreground": settings.environment.os_logo_icon_color,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(settings, default_args, kwargs)

    default_systray_args = {
        "padding": 4,
        "font": settings.fonts.font_icon,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    systray_args = build_widget_args(
        settings,
        default_systray_args,
        kwargs.get("systray", {}),
    )

    default_textbox_args = {
        "padding": 4,
        "font": settings.fonts.font_icon,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    backlight_args = build_widget_args(
        settings,
        default_textbox_args,
        kwargs.get("backlight", {}),
    )

    wallpaper_args = build_widget_args(
        settings,
        default_textbox_args,
        kwargs.get("wallpaper", {}),
    )

    space_args = build_widget_args(
        settings,
        default_textbox_args,
        kwargs.get("space", {}),
    )

    return widget.WidgetBox(
        widgets=[
            widget.Systray(**systray_args),
            widget.Spacer(length=1, **space_args),
            build_backlight_widget(settings, backlight_args),
            build_wallpaper_widget(settings, wallpaper_args),
        ],
        **args
    )
