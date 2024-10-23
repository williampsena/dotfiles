from libqtile import widget

from ebenezer.core.config.settings import AppSettings


def build_task_list_widget(settings: AppSettings, kwargs: dict):
    task_list_args = {
        "padding": 3,
        "borderwidth": 0,
        # "theme_mode": "preferred",
        # "theme_path": "/usr/share/icons/Papirus-Dark",
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
    }

    default_args = {
        "widgets": [
            widget.TaskList(**task_list_args),
        ],
        "padding": 5,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "text_closed": "  ",
        "text_open": " 󰒉 ",
        "foreground": settings.colors.fg_normal,
    }

    args = default_args | kwargs

    return widget.WidgetBox(**args)
