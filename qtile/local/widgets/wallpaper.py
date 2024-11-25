from local.core.command import lazy_command
from local.core.config.settings import AppSettings
from local.widgets.helpers.args import build_widget_args
from libqtile import widget


def build_wallpaper_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "mouse_callbacks": {
            "Button1": lazy_command(
                settings.commands.get("wallpaper_menu"),
                wallpaper_cmd=settings.commands.get("change_wallpaper"),
            )
        },
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
    )
    icon = kwargs.pop("icon", " ")

    return widget.TextBox(icon, **args)
