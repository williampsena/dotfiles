from typing import List

from ebenezer.core.config.settings import AppSettings


def build_widget_args(
    settings: AppSettings, default_args: dict, args: dict, color_keys: List[str]
):
    args = default_args | args

    return {
        k: (settings.colors.get_color(v) if k in color_keys else v)
        for k, v in args.items()
    }
