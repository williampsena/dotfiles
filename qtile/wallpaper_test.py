import wallpaper
from settings import load_settings


def test_fetch_wallpapers():
    settings = load_settings()
    widget = wallpaper.build_wallpaper_widget(settings)

    assert widget.directory == settings.environment.wallpaper_dir
    assert widget.random_selection == True
