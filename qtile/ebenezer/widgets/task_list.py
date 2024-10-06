from libqtile import widget
from ebenezer.core.settings import AppSettings


def build_task_list_widget(settings: AppSettings):
    return widget.WidgetBox(
        widgets=[widget.TaskList()],
        padding=5,
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        text_closed="  ",
        text_open=" 󰒉 ",
        foreground=settings.colors.get("fg_normal"),
    )
