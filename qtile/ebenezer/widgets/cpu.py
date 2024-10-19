import psutil
from libqtile import bar, widget
from libqtile.widget import CPU
from libqtile.log_utils import logger
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.formatter import burn_text


class ColorizedCPUWidget(CPU):
    def __init__(self, **config):
        super().__init__(**config)
        settings = config.get("settings")

        self.high_color = settings.colors.get_color(settings.monitoring.high_color)
        self.medium_color = settings.colors.get_color(settings.monitoring.medium_color)
        self.default_color = settings.colors.get_color(
            settings.monitoring.default_color
        )
        self.threshold_medium = settings.monitoring.threshold_medium
        self.threshold_high = settings.monitoring.threshold_high

    def poll(self):
        text = CPU.poll(self)
        cpu = int(float(text.replace("%", "")))

        if cpu > self.threshold_high:
            self.foreground = self.high_color
            text = burn_text(text)
        elif cpu > self.threshold_medium:
            self.foreground = self.medium_color
        else:
            self.foreground = self.default_color

        return text


def build_cpu_widget(settings: AppSettings):
    return [
        widget.TextBox(
            " ",
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            padding=2,
            foreground=settings.colors.fg_yellow,
        ),
        ColorizedCPUWidget(
            settings=settings,
            threshold_medium=1,
            threshold_high=2,
            font=settings.fonts.font_icon,
            fontsize=settings.fonts.font_icon_size,
            format="{load_percent}% ",
            padding=2,
            foreground=settings.colors.fg_normal,
        ),
    ]
