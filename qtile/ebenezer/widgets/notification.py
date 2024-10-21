import subprocess
from libqtile import widget, qtile
from libqtile.widget import base
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def __notifications_actions__():
    result = subprocess.run(
        ['echo -e "Yes\nNo" | rofi -dmenu -p "Would you like to clear notifications?"'],
        shell=True,
        capture_output=True,
        text=True,
    )

    choice = result.stdout.strip()

    if choice == "Yes":
        qtile.cmd_spawn("dunstctl history-clear")
    else:
        qtile.cmd_spawn("dunstctl close-all")


class DunstWidget(base.ThreadPoolText):
    defaults = [
        ("update_interval", 3, "Interval to update the notification count"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(DunstWidget.defaults)
        self.add_callbacks(
            {
                "Button1": self.show_notifications,
                "Button3": self.clear_notifications,
            }
        )

    def poll(self):
        count = self.get_notification_count()

        if count == 0:
            return f" {count}"
        else:
            return f"󰵙 {count}"

    def get_notification_count(self):
        try:
            output = (
                subprocess.check_output(["dunstctl", "count"]).decode("utf-8").strip()
            )

            lines = output.splitlines()

            history_count = int(lines[2].split(":")[1].strip())

            return history_count
        except Exception:
            return 0

    def show_notifications(self):
        subprocess.Popen(["dunstctl", "history-pop"])

    def clear_notifications(self):
        __notifications_actions__()


def build_notification_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "default_text": "",
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_normal,
    }

    args = build_widget_args(settings, default_args, kwargs, ["foreground"])

    return DunstWidget(**args)
