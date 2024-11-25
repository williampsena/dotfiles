from typing import Any

from local.core.command import run_shell_command
from local.core.config.settings import AppSettings
from libqtile.log_utils import logger

DEFAULT_TIMEOUT = 3


def run_startup_once(settings: AppSettings):
    for raw_cmd in settings.startup:
        try:
            cmd = settings.startup[raw_cmd]
            run_shell_command(
                cmd, timeout=DEFAULT_TIMEOUT, **_env_substitutions(settings)
            )
            logger.info(f"the script {cmd} was loaded")
        except Exception as e:
            logger.warning(
                f"error while trying to run command {raw_cmd}", e, exc_info=True
            )


def _env_substitutions(settings: AppSettings) -> dict[str, Any]:
    return {
        "lock_screen_timeout": settings.lock_screen.timeout,
        "wallpaper_dir": settings.environment.wallpaper_dir,
        "wallpaper_timeout": settings.environment.wallpaper_timeout * 60,
    }
