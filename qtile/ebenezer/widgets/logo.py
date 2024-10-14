from libqtile import widget, qtile
from ebenezer.core.config.settings import AppSettings
from files import resolve_file_path


def build_os_logo(settings: AppSettings):
    if settings.environment.os_logo_icon != "":
        return [build_os_logo_icon(settings)]

    if settings.environment.os_logo != "":
        return [build_os_logo_image(settings)]

    return []


def build_os_logo_icon(settings: AppSettings):
    return widget.TextBox(
        settings.environment.os_logo_icon,
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=10,
        foreground=settings.environment.os_logo_icon_color,
        name="os_logo",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(settings.environment.terminal)
        },
    )


def build_os_logo_image(settings: AppSettings):
    return widget.Image(
        filename=resolve_file_path(settings.environment.os_logo),
        scale="False",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(settings.environment.terminal)
        },
    )
