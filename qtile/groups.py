from typing import List
from libqtile.config import Group, Key
from keys import *
from settings import AppSettings


def build_groups(keys: List, settings: AppSettings):
    mod = settings.environment.mod

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

    groups = []
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
        key = g[0]
        label = f" {g[1]} "
        layout_default = settings.groups_layout.get("default", "monadtall")

        groups.append(
            Group(
                name=str(i + 1),
                layout=settings.groups_layout.get(key, layout_default),
                label=label,
            )
        )

    for i in groups:
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                # mod1 + shift + letter of group = move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=False),
                    desc="Move focused window to group {}".format(i.name),
                ),
            ]
        )

    return groups, keys
