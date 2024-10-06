import subprocess
from string import Template
from typing import Any
from libqtile.log_utils import logger
from ebenezer.core.settings import AppSettings
from ebenezer.core.files import resolve_file_path
from ebenezer.core.wallpaper import change_wallpaper
from ebenezer.core.command import run_shell_command


def run_startup_once(settings: AppSettings):
    for raw_cmd in settings.startup:
        try:
            cmd = settings.startup[raw_cmd]
            run_shell_command(cmd, **__env_substitutions__(settings))
            logger.info(f"the script {cmd} was loaded")
        except Exception as e:
            logger.error(
                f"error while trying to run command {raw_cmd}", e, exc_info=True
            )


def run_startup_always(settings: AppSettings):
    change_wallpaper(settings)


def __env_substitutions__(settings: AppSettings) -> dict[str, Any]:
    return {
        "lock_screen_timeout": settings.lock_screen.timeout,
        "wallpaper_dir": settings.environment.wallpaper_dir,
        "wallpaper_timeout": settings.environment.wallpaper_timeout * 60,
    }
