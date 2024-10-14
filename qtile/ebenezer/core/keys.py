from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.volume import setup_volume_keys
from ebenezer.widgets.backlight import setup_backlight_keys
from ebenezer.core.command import build_shell_command
import os


def restore_all_minimized():
    for window in qtile.current_group.windows:
        if window.minimized:
            window.toggle_minimize()


def build_keys(settings: AppSettings):
    mod = settings.environment.modkey

    return (
        [
            Key(
                [mod],
                "Return",
                lazy.spawn(settings.environment.terminal),
                desc="Launch terminal",
            ),
            Key(
                [mod, "shift"],
                "Return",
                lazy.spawn(
                    build_shell_command(
                        "rofi -show drun -show-icons -theme $rofi_home/launcher.rasi"
                    )
                ),
                desc="Run Launcher",
            ),
            Key(
                [mod], "b", lazy.spawn(settings.environment.browser), desc="Web browser"
            ),
            Key(
                [mod, "control"],
                "x",
                lazy.spawn(os.path.expanduser(settings.lock_screen.command)),
                desc="Lock screen",
            ),
            Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
            Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
            Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            Key(
                [mod],
                "r",
                lazy.spawncmd(),
                desc="Spawn a command using a prompt widget",
            ),
            # A list of available commands that can be bound to keys can be found
            # at https://docs.qtile.org/en/latest/manual/config/lazy.html
            # Switch between windows
            Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
            Key(
                [mod],
                "space",
                lazy.layout.next(),
                desc="Move window focus to other window",
            ),
            # Move windows between left/right columns or move up/down in current stack.
            # Moving out of range in Columns layout will create new column.
            Key(
                [mod, "shift"],
                "h",
                lazy.layout.shuffle_left(),
                desc="Move window to the left",
            ),
            Key(
                [mod, "shift"],
                "l",
                lazy.layout.shuffle_right(),
                desc="Move window to the right",
            ),
            Key(
                [mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"
            ),
            Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
            # Grow windows. If current window is on the edge of screen and direction
            # will be to screen edge - window would shrink.
            Key(
                [mod, "control"],
                "h",
                lazy.layout.grow_left(),
                desc="Grow window to the left",
            ),
            Key(
                [mod, "control"],
                "l",
                lazy.layout.grow_right(),
                desc="Grow window to the right",
            ),
            Key(
                [mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"
            ),
            Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
            Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
            Key(
                [mod],
                "m",
                lazy.function(restore_all_minimized),
                desc="Restore all minimized windows",
            ),
            # Toggle between split and unsplit sides of stack.
            # Split = all windows displayed
            # Unsplit = 1 window displayed, like Max layout, but still with
            # multiple stack panes
            # Key(
            #     [mod, "shift"],
            #     "Return",
            #     lazy.layout.toggle_split(),
            #     desc="Toggle between split and unsplit sides of stack",
            # ),
            # Toggle between different layouts as defined below
            Key(
                [mod],
                "f",
                lazy.window.toggle_fullscreen(),
                desc="Toggle fullscreen on the focused window",
            ),
            Key(
                [mod],
                "t",
                lazy.window.toggle_floating(),
                desc="Toggle floating on the focused window",
            ),
            Key(
                [],
                "print",
                lazy.spawn(settings.commands.get("screenshot"), shell=True),
                desc="Take a screenshot",
            ),
            Key(
                [mod],
                "print",
                lazy.spawn(settings.commands.get("screenshot_full"), shell=True),
                desc="Take a screenshot of the full desktop",
            ),
        ]
        + setup_volume_keys(settings)
        + setup_backlight_keys(settings)
    )
