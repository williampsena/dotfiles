from libqtile.config import Screen
from ebenezer.widgets.bar import build_bar
from ebenezer.core.config.settings import AppSettings


def build_screen(settings: AppSettings) -> Screen:
    if settings.bar.position == "top":
        return Screen(top=build_bar(settings))
    else:
        return Screen(bottom=build_bar(settings))
