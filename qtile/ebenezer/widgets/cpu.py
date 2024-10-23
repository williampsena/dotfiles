from libqtile import widget
from libqtile.widget import CPU

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.formatter import burn_text
from ebenezer.widgets.helpers.args import build_widget_args


class ColorizedCPUWidget(CPU):
    """
    A widget that enhances the user experience by displaying cpu use using color and icons
    """

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
        text = CPU.poll(self)
        cpu = float(text.replace("%", ""))

        if cpu > self.threshold_high:
            self.foreground = self.high_color
            text = burn_text(text)
        elif cpu > self.threshold_medium:
            self.foreground = self.medium_color
        else:
            self.foreground = self.default_color

        return text


def build_cpu_widget(settings: AppSettings, kwargs: dict):
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_yellow,
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
        "format": "{load_percent}% ",
        "padding": 2,
        "foreground": settings.colors.fg_normal,
    }

    args = build_widget_args(
        settings, default_args, kwargs.get("sensor", {}), ["foreground"]
    )

    return [
        widget.TextBox(f"{icon_args.pop("text", "")} ", **icon_args),
        ColorizedCPUWidget(**args),
    ]
