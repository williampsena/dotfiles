import psutil
from libqtile import widget
from libqtile.widget import Memory
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.formatter import burn_text
from libqtile.log_utils import logger
from ebenezer.widgets.helpers.args import build_widget_args


class ColorizedMemoryWidget(Memory):
    def __init__(self, **config):
        settings = config.pop("settings")
        super().__init__(**config)

        self.high_color = settings.colors.get_color(settings.monitoring.high_color)
        self.medium_color = settings.colors.get_color(settings.monitoring.medium_color)
        self.default_color = settings.colors.get_color(
            settings.monitoring.default_color
        )
        self.threshold_medium = config.get(
            "threshold_medium", settings.monitoring.threshold_medium
        )
        self.threshold_high = config.get(
            "threshold_high", settings.monitoring.threshold_high
        )

    def poll(self):
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        text = Memory.poll(self).lstrip()

        if mem.percent > self.threshold_high:
            self.foreground = self.high_color
            text = burn_text(text)
        elif mem.percent > self.threshold_medium:
            self.foreground = self.medium_color
        else:
            self.foreground = self.default_color

        return text.strip()


def build_memory_widget(settings: AppSettings, kwargs: dict):
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_purple,
    }

    icon_args = build_widget_args(
        settings, default_icon_args, kwargs.get("icon", {}), ["foreground"]
    )

    default_args = {
        "settings": settings,
        "threshold_medium": settings.monitoring.threshold_medium,
        "threshold_high": settings.monitoring.threshold_high,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "format": "{MemUsed: .0f}{mm}",
        "padding": 2,
        "foreground": settings.colors.fg_normal,
    }

    args = build_widget_args(
        settings, default_args, kwargs.get("sensor", {}), ["foreground"]
    )

    return [
        widget.TextBox(f"{icon_args.pop("text", "󰄧")} ", **icon_args),
        ColorizedMemoryWidget(**args),
    ]
