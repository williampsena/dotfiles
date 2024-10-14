from libqtile import bar, widget
from libqtile.log_utils import logger
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.battery import build_battery_widget
from ebenezer.widgets.clock import build_clock_widget
from ebenezer.widgets.cpu import build_cpu_widget
from ebenezer.widgets.powermenu import build_powermenu_widget
from ebenezer.widgets.memory import build_memory_widget
from ebenezer.widgets.layout import build_current_layout_widget
from ebenezer.widgets.thermal import build_thermal_widget
from ebenezer.widgets.volume import build_volume_widget
from ebenezer.widgets.weather import build_weather_widget
from ebenezer.widgets.notification import build_notification_widget
from ebenezer.widgets.task_list import build_task_list_widget
from ebenezer.widgets.hide_tray import build_hide_tray


def build_top_bar(settings: AppSettings):
    widgets = (
        [
            widget.GroupBox(
                margin_y=3,
                margin_x=3,
                padding=5,
                borderwidth=3,
                active=settings.colors.fg_normal,
                inactive=settings.colors.fg_normal,
                this_current_screen_border=settings.colors.bg_topbar_selected,
                highlight_color=settings.colors.bg_topbar_selected,
                this_screen_border=settings.colors.fg_blue,
                highlight_method="block",
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                foreground=settings.colors.fg_normal,
                rounded=False,
                urgent_alert_method='border',
                urgent_border=settings.colors.fg_urgent,
            ),
            widget.Prompt(
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                foreground=settings.colors.fg_normal,
            ),
            build_task_list_widget(settings),
            widget.WindowName(
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                foreground=settings.colors.fg_normal,
            ),
            build_weather_widget(settings),
            build_clock_widget(settings),
            widget.Spacer(length=bar.STRETCH),
        ]
        + build_thermal_widget(settings)
        + build_cpu_widget(settings)
        + build_memory_widget(settings)
        + [
            build_battery_widget(settings),
            build_volume_widget(settings),
            build_hide_tray(settings),
            build_powermenu_widget(settings),
            build_notification_widget(settings),
            build_current_layout_widget(settings),
        ]
    )

    return bar.Bar(
        widgets,
        30,
        background=settings.colors.bg_topbar,
    )
