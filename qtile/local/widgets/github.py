import requests
from local.core.command import build_shell_command
from local.core.config.settings import AppSettings
from local.core.requests import request_retry
from local.widgets.helpers.args import build_widget_args
from libqtile import widget
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile.widget import base


class GitHubNotifications(base.ThreadPoolText):
    """
    A widget that fetches GitHub notifications.
    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("update_interval", 10, "Update interval in seconds"),
        ("token", None, "GitHub Personal Access Token"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)

        self.settings = config.pop("settings")
        self.icon = config.pop("icon_widget")
        self.token = config.get(
            "token", self.settings.environment.github_notifications_token
        )
        self.add_defaults(GitHubNotifications.defaults)

    def poll(self):
        if self.token is None:
            return "No github token"

        try:

            def _do_request():
                headers = {
                    "Authorization": f"token {self.token}",
                    "Accept": "application/vnd.github.v3+json",
                }

                return requests.get(
                    "https://api.github.com/notifications", headers=headers
                )

            response = request_retry(_do_request)
            status_code = response.status_code

            if status_code == 200:
                notifications = response.json()
                count = len(notifications)

                if count == 0:
                    self.icon.foreground = self.icon.foreground_normal
                    return ""
                else:
                    self.icon.foreground = self.icon.foreground_alert
                    return f"{count}+"
            else:
                logger.warning("GitHub API Error... {status_code}")
                return " "
        except Exception as e:
            logger.warning("GitHub Notifications Error: {e}")
            return " "


def build_github_widget(settings: AppSettings, kwargs: dict):
    default_icon_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 6,
        "foreground": settings.colors.fg_white,
        "foreground_normal": settings.colors.fg_white,
        "foreground_alert": settings.colors.fg_yellow,
        "background": settings.colors.bg_topbar_arrow,
        "mouse_callbacks": {"Button1": go_to_notifications_url(settings)},
    }

    icon_args = build_widget_args(settings, default_icon_args, kwargs.get("icon", {}))

    icon_widget = widget.TextBox(f"{icon_args.pop("text", "")}", **icon_args)

    default_args = {
        "icon_widget": icon_widget,
        "settings": settings,
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "padding": 4,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
    }

    args = build_widget_args(settings, default_args, kwargs.get("widget", {}))

    return [
        icon_widget,
        GitHubNotifications(**args),
    ]


def go_to_notifications_url(settings: AppSettings):
    cmd = settings.commands.get("open_url")

    if cmd is None:
        return

    return lazy.spawn(build_shell_command(cmd, url="https://github.com/notifications"))
