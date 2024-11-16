import subprocess

from ebenezer.core.command import build_shell_command, run_shell_command
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args
from libqtile.widget import base


def _notifications_actions(cmd: str):
    if cmd is None:
        return

    result = subprocess.run(
        [
            build_shell_command(
                cmd, title="Confirm", question="Would you like to clear notifications?"
            )
        ],
        shell=True,
        capture_output=True,
        text=True,
    )

    choice = result.stdout.strip()

    if choice == "yes":
        run_shell_command("dunstctl history-clear")
    else:
        run_shell_command("dunstctl close-all")


class DunstWidget(base.ThreadPoolText):
    defaults = [
        ("update_interval", 3, "Interval to update the notification count"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)

        settings = config.pop("settings")

        self.count = 0
        self.modal_confirm_cmd = settings.commands.get("modal_confirm")
        self.animated = config.get("animated", False)
        self.bells_index = 0
        self.bells = ["󰂚", "󰂞"]
        self.foreground_zero = config.get("foreground_zero", settings.colors.fg_normal)
        self.foreground_count = config.get(
            "foreground_count", settings.colors.fg_normal
        )

        self.add_defaults(DunstWidget.defaults)
        self.add_callbacks(
            {
                "Button1": self.show_notifications,
                "Button3": self.clear_notifications,
            }
        )

    def poll(self):
        self.count = self.get_notification_count()

        if self.count == 0:
            self.foreground = self.foreground_zero
            return ""
        else:
            bell_icon = self.get_bell_icon()
            self.foreground = self.foreground_count
            return f"{bell_icon} {self.count}"

    def get_bell_icon(self):
        if self.animated is False:
            return self.bells[0]

        self.bells_index = 1 if self.bells_index == 0 else 0
        return self.bells[self.bells_index]

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
        if self.count == 0:
            return

        _notifications_actions(self.modal_confirm_cmd)


def build_notification_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "settings": settings,
        "default_text": "",
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 2,
        "foreground": settings.colors.fg_normal,
        "foreground_zero": settings.colors.fg_normal,
        "foreground_count": settings.colors.fg_yellow,
        "animated": False,
    }

    args = build_widget_args(
        settings,
        default_args,
        kwargs,
        ["foreground", "foreground_zero", "foreground_count"],
    )

    return DunstWidget(**args)
