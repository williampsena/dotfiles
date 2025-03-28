# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ebenezer.config.settings import load_settings_by_files
from ebenezer.core.groups import build_groups
from ebenezer.core.keys import build_keys
from ebenezer.core.layout import (
    build_layouts,
    centralize_window,
    is_ebenezer_window,
    set_floating_window,
)
from ebenezer.core.screen import build_screen
from ebenezer.core.startup import run_startup_once
from ebenezer.core.theme import preload_colors
from ebenezer.core.wallpaper import change_wallpaper
from libqtile import hook, qtile
from libqtile.config import Click, Drag, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger

settings = load_settings_by_files()
settings = preload_colors(settings, complete=True)

keys = build_keys(settings)
groups, keys = build_groups(keys, settings)

mod = settings.environment.modkey

widget_defaults = dict(
    font=settings.fonts.font_strong_bold,
    fontsize=settings.fonts.font_size,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [build_screen(settings), Screen()]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

layouts = build_layouts(settings)

center_windows_titles = ["ebenezer - configuration manager"]


def is_ebenezer_window(window):
    return any(title.lower() in window.name.lower() for title in center_windows_titles)


@hook.subscribe.startup_once
def start_once():
    try:
        settings = load_settings_by_files()
        run_startup_once(settings)
        change_wallpaper(settings)
    except Exception as error:
        logger.warning(
            "An exception occurred while trying to startup scripts run once.",
            error,
            exc_info=True,
        )


# Allows you to input a name when adding treetab section.
@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)


# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()


# A function for toggling between MAX and MONADTALL layouts
@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == "monadtall":
        qtile.current_group.layout = "max"
    elif current_layout_name == "max":
        qtile.current_group.layout = "monadtall"


@hook.subscribe.client_new
def prevent_minimize(window):
    if window.minimized:
        window.unminimize()


@hook.subscribe.startup_once
def set_wmname():
    import subprocess

    subprocess.run(["xsetroot", "-name", "LG3D"])


@hook.subscribe.client_managed
def set_floating(window):
    set_floating_window(window)

    if is_ebenezer_window(window):
        centralize_window(settings, window)
