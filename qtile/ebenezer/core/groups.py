from typing import List, Any
from libqtile.config import Group, Key
from ebenezer.core.keys import *
from ebenezer.core.config.settings import AppSettings


def build_groups(keys: List, settings: AppSettings):
    mod = settings.environment.modkey

    # Add key bindings to switch VTs in Wayland.
    # We can't check qtile.core.name in default config as it is loaded before qtile is started
    # We therefore defer the check until the key binding is run by using .when(func=...)
    for vt in range(1, 8):
        keys.append(
            Key(
                ["control", "mod1"],
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )

    groups: list[Any] = []
    group_layouts = [
        "monadtall",
        "monadtall",
        "tile",
        "tile",
        "monadtall",
        "monadtall",
        "monadtall",
        "monadtall",
        "monadtall",
    ]

    
    for i, g in enumerate(settings.groups):
        key = g
        label = f" {settings.groups[g]} "
        layout_default = settings.groups_layout.get("default", "monadtall")

        groups.append(
            Group(
                name=str(i + 1),
                layout=settings.groups_layout.get(key, layout_default),
                label=label,
            )
        )

    for g in groups:
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    g.name,
                    lazy.group[g.name].toscreen(),
                    desc="Switch to group {}".format(g.name),
                ),
                # mod1 + shift + letter of group = move focused window to group
                Key(
                    [mod, "shift"],
                    g.name,
                    lazy.window.togroup(g.name, switch_group=False),
                    desc="Move focused window to group {}".format(g.name),
                ),
            ]
        )

    return groups, keys
