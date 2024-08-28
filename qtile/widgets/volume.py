from libqtile import widget
from settings import AppSettings
from libqtile.log_utils import logger


def build_volume_widget(settings: AppSettings):
    return widget.Volume(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        foreground=settings.colors.get("fg_normal"),
        padding=5,
        emoji=True,
        emoji_list=["󰝟", "󰕿", "󰖀", "󰕾"],
        limit_max_volume=True,
        step=5,
    )
