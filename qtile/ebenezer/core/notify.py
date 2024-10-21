from ebenezer.core.command import run_shell_command

TEMPLATE_NOTIFY = 'notify-send -r 999 -u low "$message"'
TEMPLATE_WITH_TITLE = 'notify-send -r 999 -u low "$title" "$message"'


def push_notification(title: str, message: str):
    return run_shell_command(TEMPLATE_WITH_TITLE, title=title, message=message)


def push_notification_progress(message: str, progress: int):
    return run_shell_command(
        f"{TEMPLATE_NOTIFY} -h int:value:$progress",
        message=message,
        progress=str(progress),
    )
