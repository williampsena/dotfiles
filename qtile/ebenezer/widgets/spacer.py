from libqtile import bar, widget
from libqtile.log_utils import logger

from ebenezer.core.config.settings import AppSettings


def build_spacer(settings: AppSettings, kwargs: dict):
    default_args = {"length": bar.STRETCH}
    args = default_args | kwargs

    length = args.get("length")

    if length == "stretch":
        length = bar.STRETCH
    elif length == "calculated":
        length = bar.CALCULATED
    elif length == "static":
        length = bar.STATIC
    elif not isinstance(length, int):
        length = 1

    args["length"] = length

    return widget.Spacer(**args)
