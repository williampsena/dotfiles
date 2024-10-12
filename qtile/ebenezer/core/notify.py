from libqtile.lazy import lazy
from ebenezer.core.command import run_shell_command


def push_notification(title: str, message: str):
    return run_shell_command(
        'notify-send -r 999  -u low "$title" "$message"', title=title, message=message
    )


def push_notification_progress(message: str, progress: int, title: str = None):
    return run_shell_command(
        f"{__build_command__(title)} -h int:value:$progress",
        title=title,
        message=message,
        progress=progress,
    )


def __build_command__(title: str) -> str:
    if title is None:
        return 'notify-send -r 999 -u low "$message"'

    return 'notify-send -r 999  -u low "$title" "$message"'
