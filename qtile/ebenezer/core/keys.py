import os
from typing import Any, List

from libqtile.config import Key
from libqtile.lazy import lazy

from ebenezer.core.command import lazy_spawn
from ebenezer.core.config.keybindings import AppSettingsKeyBinding
from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.backlight import setup_backlight_keys
from ebenezer.widgets.volume import setup_volume_keys


def _build_key_spawn(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy_spawn(binding.command),
    )


def _build_key_spawn_command(settings: AppSettings, binding: AppSettingsKeyBinding):
    cmd = settings.commands.get(binding.command)

    if cmd is None:
        return None

    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy_spawn(cmd),
    )


def _build_key_spawn_terminal(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy_spawn(settings.environment.terminal),
    )


def _build_key_spawn_browser(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy.spawn(settings.environment.browser),
    )


def _build_key_lock_screen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys),
        lazy.spawn(os.path.expanduser(settings.lock_screen.command)),
    )


def _build_key_next_layout(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.next_layout())


def _build_key_kill_window(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.window.kill())


def _build_key_reload_config(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.reload_config())


def _build_key_shutdown(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.shutdown())


def _build_key_spawn_cmd(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.spawncmd())


def _build_key_focus_left(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.left())


def _build_key_focus_right(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.right())


def _build_key_focus_down(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.down())


def _build_key_focus_up(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.up())


def _build_key_focus_next(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.next())


def _build_key_fullscreen(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.window.toggle_fullscreen()
    )


def _build_key_floating(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.window.toggle_floating()
    )


def _build_key_shuffle_left(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_left()
    )


def _build_key_shuffle_right(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_right()
    )


def _build_key_shuffle_down(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_down()
    )


def _build_key_shuffle_up(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.shuffle_up()
    )


def _build_key_grow_left(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.grow_left()
    )


def _build_key_grow_right(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.grow_right()
    )


def _build_key_grow_down(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.grow_down()
    )


def _build_key_grow_up(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(_format_keybinding(settings, binding.keys), lazy.layout.grow_up())


def _build_key_reset_windows(settings: AppSettings, binding: AppSettingsKeyBinding):
    return _build_key(
        _format_keybinding(settings, binding.keys), lazy.layout.normalize()
    )


ACTIONS = {
    "cmd": _build_key_spawn_cmd,
    "spawn": _build_key_spawn,
    "spawn_command": _build_key_spawn_command,
    "terminal": _build_key_spawn_terminal,
    "browser": _build_key_spawn_browser,
    "lock_screen": _build_key_lock_screen,
    "next_layout": _build_key_next_layout,
    "kill_window": _build_key_kill_window,
    "reload_config": _build_key_reload_config,
    "shutdown": _build_key_shutdown,
    "focus_left": _build_key_focus_left,
    "focus_right": _build_key_focus_right,
    "focus_up": _build_key_focus_up,
    "focus_down": _build_key_focus_down,
    "focus_next": _build_key_focus_next,
    "fullscreen": _build_key_fullscreen,
    "floating": _build_key_floating,
    "shuffle_left": _build_key_shuffle_left,
    "shuffle_right": _build_key_shuffle_right,
    "shuffle_up": _build_key_shuffle_up,
    "shuffle_down": _build_key_shuffle_down,
    "grow_left": _build_key_grow_left,
    "grow_right": _build_key_grow_right,
    "grow_down": _build_key_grow_down,
    "grow_up": _build_key_grow_up,
    "reset_windows": _build_key_reset_windows,
}


def build_keys(settings: AppSettings):
    mod = settings.environment.modkey

    keys = setup_volume_keys(settings) + setup_backlight_keys(settings)

    keys = _build_keys_from_config(settings, keys)

    return keys


def _build_keys_from_config(settings: AppSettings, keys: List[Any]):
    for binding in settings.keybindings:
        action_callable = ACTIONS.get(binding.action)
        key = None

        if action_callable:
            key = action_callable(settings, binding)

        if key:
            keys.append(key)

    return keys


def _build_key(keybinding: List[str], command):
    return Key(
        keybinding[:-1],
        keybinding[-1],
        command,
    )


def _format_keybinding(settings: AppSettings, keys: List[str]):
    return [k.replace("$mod", settings.environment.modkey) for k in keys]
