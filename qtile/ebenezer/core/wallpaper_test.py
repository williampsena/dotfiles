from ebenezer.core.wallpaper import change_wallpaper
from ebenezer.core.config.loader import TEST_CONFIG
from ebenezer.core.config.settings import load_settings


def test_change_wallpaper():
    settings = load_settings(TEST_CONFIG)
    widget = change_wallpaper(settings)
