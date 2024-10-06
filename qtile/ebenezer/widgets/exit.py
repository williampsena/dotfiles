import subprocess
from libqtile import qtile, widget
from libqtile.lazy import lazy
from ebenezer.core.settings import AppSettings
from ebenezer.widgets.backlight import build_backlight_widget
from ebenezer.widgets.lock_screen import build_lock_screen_widget


def __shutdown__():
    result = subprocess.run(
        ['echo -e "Yes\nNo" | rofi -dmenu -p "Are you sure?"'],
        shell=True,
        capture_output=True,
        text=True,
    )

    choice = result.stdout.strip()

    if choice == "Yes":
        qtile.cmd_spawn('notify-send "Confirmed!" "🛑 𝐠𝐨𝐨𝐝𝐛𝐲𝐞, see you later..."')
        qtile.cmd_spawn("systemctl poweroff")
    else:
        qtile.cmd_spawn('notify-send "Cancelled!" "You chose No.')


def build_exit_widget(settings: AppSettings):
    return widget.WidgetBox(
        widgets=[
            widget.QuickExit(
                default_text=" 󰍃",
                countdown_format=" {}  ",
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                padding=2,
                foreground=settings.colors.get("fg_normal"),
            ),
            widget.TextBox(
                "  ",
                font=settings.fonts.font_icon,
                fontsize=settings.fonts.font_icon_size,
                padding=2,
                foreground=settings.colors.get("fg_normal"),
                mouse_callbacks={"Button1": __shutdown__},
            ),
            build_lock_screen_widget(settings),
            build_backlight_widget(settings),
            widget.Systray(),
        ],
        padding=12,
        font=settings.fonts.font_icon,
        text_closed=settings.environment.os_logo_icon,
        text_open=settings.environment.os_logo_icon,
        foreground=settings.environment.os_logo_icon_color,
    )
