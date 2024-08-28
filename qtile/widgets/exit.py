from libqtile import widget
from settings import AppSettings
from libqtile.lazy import lazy
from widgets.backlight import build_backlight_widget


def build_exit_widget(settings: AppSettings):
    return widget.WidgetBox(
        widgets=[
            widget.QuickExit(
                default_text=" 󰍃",
                countdown_format=" {}  ",
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                padding=2,
                foreground=settings.colors.get("fg_normal"),
            ),
            widget.TextBox(
                "  ",
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                padding=2,
                foreground=settings.colors.get("fg_normal"),
                mouse_callbacks={"Button1": lazy.spawn("systemctl poweroff")},
            ),
            build_backlight_widget(settings),
            widget.Systray(),
        ],
        padding=12,
        font=settings.fonts.font_icon,
        text_closed=settings.environment.os_logo_icon,
        text_open=settings.environment.os_logo_icon,
        foreground=settings.environment.os_logo_icon_color,
    )


# return widget.QuickExit(fmt="", padding=5)
