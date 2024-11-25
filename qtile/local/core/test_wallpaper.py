from local.core.config.loader import TEST_CONFIG
from local.core.config.settings import load_settings_by_files
from local.core.wallpaper import change_wallpaper


def test_change_wallpaper():
    settings = load_settings_by_files(config_filepath=TEST_CONFIG)
    widget = change_wallpaper(settings)
