from libqtile import widget
from ebenezer.core.settings import AppSettings


def build_backlight_widget(settings: AppSettings):
    return widget.Backlight(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        backlight_name=settings.environment.backlight_name,
        fmt=" {}",
    )
