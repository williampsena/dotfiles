from typing import List

from ebenezer.core.config.settings import AppSettings

DEFAULT_COLOR_ARGS: List[str] = ["foreground", "background"]


def build_widget_args(
    settings: AppSettings,
    default_args: dict,
    args: dict,
    color_keys: List[str] = DEFAULT_COLOR_ARGS,
):
    args = default_args | args

    return {
        k: (settings.colors.get_color(v) if k in color_keys else v)
        for k, v in args.items()
    }
