from libqtile import widget
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from libqtile.config import Key
from ebenezer.core.settings import AppSettings
from ebenezer.core.command import run_shell_command_stdout, run_shell_command
from ebenezer.core.notify import push_notification, push_notification_progress
import subprocess


def build_volume_widget(settings: AppSettings):
    return widget.Volume(
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        foreground=settings.colors.get("fg_normal"),
        padding=5,
        emoji=True,
        emoji_list=["󰝟", "󰕿", "󰖀", "󰕾"],
        limit_max_volume=True,
        step=5,
        mouse_callbacks={"Button1": lazy.spawn(settings.commands.get("mixer"))},
    )


def __get_current_volume__(settings: AppSettings):
    volume_level = settings.commands.get("volume_level")

    if volume_level is None:
        return None

    output = run_shell_command_stdout(volume_level)

    return output.stdout.replace("%", "").replace("\n", "")


def __is_muted__(settings: AppSettings):
    cmd = settings.commands.get("mute_status")

    if cmd is None:
        return False

    output = run_shell_command_stdout(cmd)

    return output.stdout.strip() == "yes"


def __push_volume_notification__(settings: AppSettings, message: str):
    level = __get_current_volume__(settings) or "0"
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=int(level))


def __volume_up__(settings: AppSettings):
    volume_cmd = settings.commands.get("volume_up")

    @lazy.function
    def inner(qtile):
        level = int(__get_current_volume__(settings) or "0")

        if level > 115:
            return

        __unmute__(settings)

        if volume_cmd:
            run_shell_command(volume_cmd)

        __push_volume_notification__(settings, "󰝝 Volume")

    return inner


def __volume_down__(settings: AppSettings):
    volume_cmd = settings.commands.get("volume_down")

    @lazy.function
    def inner(qtile):
        if volume_cmd:
            run_shell_command(volume_cmd)

        __push_volume_notification__(settings, "󰝞 Volume")

    return inner


def __lazy_unmute__(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        __unmute__(settings, notify=True)

    return inner


def __unmute__(settings: AppSettings, notify=False):
    volume_cmd = settings.commands.get("mute_off")

    if volume_cmd:
        run_shell_command(volume_cmd)

    if notify:
        push_notification("Volume 󰖁", "Muted")


def __lazy_mute_toggle__(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        __mute_toggle__(settings)

    return inner


def __mute_toggle__(settings: AppSettings):
    volume_cmd = settings.commands.get("mute")

    if volume_cmd:
        run_shell_command(volume_cmd)

    if __is_muted__(settings):
        push_notification("Volume ", "Muted")
    else:
        push_notification("Volume  󰕾", "On")


def setup_volume_keys(settings: AppSettings):
    return [
        Key(
            [],
            "XF86AudioRaiseVolume",
            __volume_up__(settings),
            desc="Up the volume",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            __volume_down__(settings),
            desc="Down the volume",
        ),
        Key(
            [],
            "XF86AudioMute",
            __lazy_mute_toggle__(settings),
            desc="Toggle mute",
        ),
        Key(
            [],
            "XF86AudioMicMute",
            __lazy_unmute__(settings),
            desc="Toggle mute the microphone",
        ),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play-pause"),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next song"),
        Key(
            [], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous song"
        ),
    ]
