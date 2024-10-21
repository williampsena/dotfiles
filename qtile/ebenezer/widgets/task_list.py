from libqtile import widget
from ebenezer.core.config.settings import AppSettings


def build_task_list_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "widgets": [widget.TaskList()],
        "padding": 5,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "text_closed": "  ",
        "text_open": " 󰒉 ",
        "foreground": settings.colors.fg_normal,
    }

    args = default_args | kwargs

    return widget.WidgetBox(**args)
