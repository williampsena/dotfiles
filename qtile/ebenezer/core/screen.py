from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.bar import build_bar
from libqtile.config import Screen


def build_screen(settings: AppSettings) -> Screen:
    if settings.bar.position == "top":
        return Screen(top=build_bar(settings))
    else:
        return Screen(bottom=build_bar(settings))
