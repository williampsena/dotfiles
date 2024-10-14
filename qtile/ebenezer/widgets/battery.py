from libqtile import bar, widget
from libqtile.log_utils import logger
from ebenezer.core.config.settings import AppSettings


def build_battery_widget(settings: AppSettings):
    return widget.Battery(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        format="{char} {percent:2.0%}",
        charge_char="",
        discharge_char=" ",
        empty_char=" ",
        full_char=" ",
        not_charging_char="󰚦",
        unknown_char="󰛄 ",
        foreground=settings.colors.fg_normal,
        padding=5,
    )
