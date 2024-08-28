from libqtile import bar, widget
from libqtile.log_utils import logger
from settings import AppSettings
from wallpaper import build_wallpaper_widget
from widgets.battery import build_battery_widget
from widgets.clock import build_clock_widget
from widgets.cpu import build_cpu_widget
from widgets.exit import build_exit_widget
from widgets.memory import build_memory_widget
from widgets.layout import build_current_layout_widget
from widgets.thermal import build_thermal_widget
from widgets.volume import build_volume_widget
from widgets.weather import build_weather_widget


def build_top_bar(settings: AppSettings):
    widgets = (
        [
            widget.GroupBox(
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                foreground=settings.colors.get("fg_normal"),
                borderwidth=3,
                rounded=False,
                highlight_method="line",
            ),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            build_weather_widget(settings),
        ]
        + build_thermal_widget(settings)
        + build_cpu_widget(settings)
        + build_memory_widget(settings)
        + [
            build_battery_widget(settings),
            build_volume_widget(settings),
            build_clock_widget(settings),
            build_exit_widget(settings),
            build_current_layout_widget(settings),
            build_wallpaper_widget(settings),
        ]
    )

    return bar.Bar(
        widgets,
        30,
        background=settings.colors.get("bg_topbar"),
        # border_width=[4, 0, 4, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
    )
