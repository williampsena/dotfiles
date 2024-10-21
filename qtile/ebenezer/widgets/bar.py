from typing import List, Any
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
from ebenezer.widgets.spacer import build_spacer
from ebenezer.widgets.task_list import build_task_list_widget
from ebenezer.widgets.hidden_tray import build_hidden_tray
from ebenezer.widgets.helpers.args import build_widget_args
from ebenezer.widgets.window_name import build_window_name


def build_bar(settings: AppSettings):
    widgets = __build_widgets__(settings)

    return bar.Bar(
        widgets,
        settings.bar.size,
        background=settings.colors.bg_topbar,
        margin=settings.bar.margin,
    )


def build_fallback_bar(settings: AppSettings):
    return [
        __build_group__(settings, {}),
        __build_separator__(settings, {}),
        __build_prompt__(settings, {}),
        build_clock_widget(settings, {}),
        build_spacer(settings, {}),
        build_current_layout_widget(settings, {}),
    ]


def __build_group__(settings: AppSettings, kwargs: dict):
    default_args = {
        "margin_y": 3,
        "margin_x": 3,
        "padding": 3,
        "borderwidth": 3,
        "active": settings.colors.fg_normal,
        "inactive": settings.colors.fg_normal,
        "this_current_screen_border": settings.colors.bg_topbar_selected,
        "this_screen_border": settings.colors.fg_blue,
        "other_current_screen_border": settings.colors.bg_topbar_selected,
        "highlight_color": settings.colors.bg_topbar_selected,
        "highlight_method": "text",
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "rounded": False,
        "urgent_alert_method": "border",
        "urgent_border": settings.colors.fg_urgent,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        [
            "active",
            "inactive",
            "this_current_screen_border",
            "this_screen_border",
            "other_current_screen_border",
            "highlight_color",
            "foreground",
            "urgent_border",
        ],
    )

    return widget.GroupBox(**args)


def __build_separator__(settings: AppSettings, args: dict):
    return widget.Sep(**args)


def __build_prompt__(settings: AppSettings, kwargs: dict):
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        [
            "foreground",
        ],
    )

    return widget.Prompt(**args)


def __build_task_list_widget__(settings: AppSettings, args: dict):
    return build_task_list_widget(settings, args)


WIDGETS = {
    "group_box": __build_group__,
    "separator": __build_separator__,
    "prompt": __build_prompt__,
    "task_list": __build_task_list_widget__,
    "window_name": build_window_name,
    "weather": build_weather_widget,
    "clock": build_clock_widget,
    "spacer": build_spacer,
    "thermal": build_thermal_widget,
    "cpu": build_cpu_widget,
    "memory": build_memory_widget,
    "battery": build_battery_widget,
    "volume": build_volume_widget,
    "notification": build_notification_widget,
    "powermenu": build_powermenu_widget,
    "hidden_tray": build_hidden_tray,
    "current_layout": build_current_layout_widget,
}


def __build_widget__(settings: AppSettings, widget_type: str, args: dict):
    builder = WIDGETS.get(widget_type)

    if builder is None:
        return None

    return builder(settings, args)


def __build_widgets__(settings: AppSettings):
    try:
        widgets: List[Any] = []

        for config in settings.bar.widgets:
            next_widgets = __build_widget__(settings, config.type, config.args)

            if next_widgets is None:
                logger.warn(
                    f"Widget {config.type} could not be found: {config.__dict__}"
                )
                continue
            elif isinstance(next_widgets, list):
                widgets = widgets + next_widgets
            else:
                widgets.append(next_widgets)

        return widgets
    except Exception as e:
        logger.warning("An error ocurred while trying to build bar", e, exc_info=True)
        return build_fallback_bar(settings)
