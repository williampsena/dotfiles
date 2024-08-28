from libqtile import qtile
from settings import AppSettings
from files import resolve_file_path
from libqtile.widget.wallpaper import Wallpaper


def build_wallpaper_widget(setting: AppSettings):
    wallpaper_dir = setting.environment.wallpaper_dir
    if wallpaper_dir is None:
        return

    return Wallpaper(
        directory=wallpaper_dir,
        max_chars=0,
        fmt="",
        random_selection=True,
    )
