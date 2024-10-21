from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_group_box(settings: AppSettings, kwargs: dict):
    default_args = {
        "margin_y": 3,
        "margin_x": 3,
        "padding": 1,
        "borderwidth": 2,
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
